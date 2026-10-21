# review round7 consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 0
- **Tool calls:** 32
- **Original source:** `logs/workers/worker_review_round7_consistency_20260515T124330.log`
- **Structured JSON:** [`fc2bb4e6ff879baefc76.json`](../../sessions/fc/fc2bb4e6ff879baefc76.json)

## Before a recorded user message

89 recorded events

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
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
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
  "uuid": "3bf3f7f4-7cf4-48da-a428-50cbd9a065f6",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1778850600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "89e629e6-7fed-47a9-a0a3-364fc59c56e6",
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
This is a comprehensive consistency audit task for a paper. I need to:

1. Read the registry to get experiment data
2. Read all the paper tex files
3. Cross-reference numbers
4. Check hard constraints
5. Check narrative consistency
6. Check formatting
7. Write a review report

Let me start by loading the MCP tools and reading the registry, then read all the paper files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "b5dc2b23-6d84-4269-b8f1-175f03204cfa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGLkv4Rd6iAceZK7VhwGYQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11897,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11897
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

开始论文一致性审计。先加载工具并读取 registry 和所有论文文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "f824150b-c2af-4a69-85a5-a9e11edb3511",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGLkv4Rd6iAceZK7VhwGYQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11897,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11897
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HTminY4xmU48LzPCvfNxFM`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "6f624b00-fb94-4e86-9718-04c8b02b573a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGLkv4Rd6iAceZK7VhwGYQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11897,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11897
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

_source line 7 · 2026-05-15T12:43:42.193Z_

<details><summary>↩ Tool result · `toolu_01HTminY4xmU48LzPCvfNxFM`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

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
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "bf70ca87-d545-41bd-89cf-fa2a3cff3602",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
Now let me read the registry and all paper files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "8f1b1888-179f-4a8b-9b0f-708547ff3667",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TA8Wag2xN9wHMQUc1d5Ed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1793,
      "cache_read_input_tokens": 23598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1793
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01PWNoPyK3Pt2eD8HhWKqNgq`</summary>

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
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "e4eba5d2-05cd-4807-9363-9a5336dcc160",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TA8Wag2xN9wHMQUc1d5Ed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1793,
      "cache_read_input_tokens": 23598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1793
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01UYwZJHAbrWqidfmvTfUc4j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "2cab9e8a-3023-472e-b182-e84692606424",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TA8Wag2xN9wHMQUc1d5Ed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1793,
      "cache_read_input_tokens": 23598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1793
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01NN2sSSgSuRaSL8LC8r2F1Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "cfcb1c59-7124-4763-bb34-bd37c31c2a2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TA8Wag2xN9wHMQUc1d5Ed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1793,
      "cache_read_input_tokens": 23598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1793
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 12 · 2026-05-15T12:43:47.773Z_

<details><summary>↩ Tool result · `toolu_01PWNoPyK3Pt2eD8HhWKqNgq`</summary>

```text
Error: result (131,974 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7/tool-results/mcp-agent-ml-research-read_registry-1778849027754.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7/tool-results/mcp-agent-ml-research-read_registry-1778849027754.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "52a62595-1ea3-42b7-ae47-8d5cab3686c7",
  "tool_use_result": {
    "content": "Error: result (131,974 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7/tool-results/mcp-agent-ml-research-read_registry-1778849027754.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7/tool-results/mcp-agent-ml-research-read_registry-1778849027754.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp008_re_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:50.987Z\", \"updated_at\": \"2026-05-15T12:41:39.774Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp008_re_n16 && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp008_re_n16 --collect_logprobs 2>&1 | tee output/exp008_re_n16/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:2\"], \"pid\": \"53600\", \"log_path\": \"~/runs/struct_self_consist_ie/exp008_re_n16.log\", \"submitted_at\": \"2026-05-14T12:15:14.917Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_008_re_n16_v2 (full 551-instance run on autodl-5090)\", \"wall_clock_seconds\": 87984.9, \"gpu_hours\": 24.44}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:41:39.774Z\"}, \"exp001_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:48.078Z\", \"updated_at\": \"2026-05-15T12:41:32.192Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp001_n16_seed456 && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --output_dir output/exp001_n16_seed456 --collect_logprobs 2>&1 | tee output/exp001_n16_seed456/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:1\"], \"pid\": \"50302\", \"log_path\": \"~/runs/struct_self_consist_ie/exp001_seed456.log\", \"submitted_at\": \"2026-05-14T12:12:41.206Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)\", \"wall_clock_seconds\": 88131.0, \"gpu_hours\": 24.48}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:32.192Z\"}, \"exp001_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:45.739Z\", \"updated_at\": \"2026-05-15T12:41:31.168Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp001_n16_seed123 && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --output_dir output/exp001_n16_seed123 --collect_logprobs 2>&1 | tee output/exp001_n16_seed123/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"48530\", \"log_path\": \"~/runs/struct_self_consist_ie/exp001_seed123.log\", \"submitted_at\": \"2026-05-14T12:09:45.674Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed123_v2 (NER-only, 551 instances on autodl-5090)\", \"wall_clock_seconds\": 88305.5, \"gpu_hours\": 24.53}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:31.168Z\"}, \"exp_001_n16_seed456_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:44:31.348Z\", \"updated_at\": \"2026-05-15T12:41:30.065Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed456/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:1\"], \"pid\": \"62170\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_n16_seed456_full.log\", \"submitted_at\": \"2026-05-14T12:44:31.087Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)\", \"wall_clock_seconds\": 86219.0, \"gpu_hours\": 23.95}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:30.065Z\"}, \"exp_001_n16_seed123_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:43:47.915Z\", \"updated_at\": \"2026-05-15T12:41:29.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed123_full/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"61812\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_n16_seed123_full.log\", \"submitted_at\": \"2026-05-14T12:44:06.059Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed123_v2 (NER-only on autodl-5090)\", \"wall_clock_seconds\": 86243.0, \"gpu_hours\": 23.96}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:29.068Z\"}, \"exp_007_ner_llama\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:21.510Z\", \"updated_at\": \"2026-05-15T12:41:27.410Z\", \"spec\": {\"description\": \"Fine-tune LLaMA-3.1-8B on SciERC + NER pilot (N=8, T=0.7). Model-agnostic validation.\", \"hypothesis\": \"SJ advantage is model-agnostic, not Qwen3-specific\", \"plan_id\": \"exp-007\", \"claim\": 1, \"model_name\": \"llama-3.1-8b-instruct (new fine-tune)\", \"dataset\": \"SciERC\", \"priority\": \"P0\", \"failure_reason\": \"Superseded by exp_007_ner_multi_model + exp_007_llama_inference (completed on autodl-5090)\"}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_007_llama_inference (DONE)\", \"notes\": \"Completed as exp_007_llama_n16 on autodl-5090. Registry status corrected.\", \"completed_at\": \"2026-05-15T12:41:27.410Z\"}, \"exp_002_merge_conll2003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:25:56.211Z\", \"updated_at\": \"2026-05-15T12:41:26.419Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli export export_config_conll2003.yaml > /tmp/merge_conll2003.log 2>&1 && echo 'MERGE_DONE' >> /tmp/merge_conll2003.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"57524\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_merge_conll2003.log\", \"submitted_at\": \"2026-05-14T12:25:56.139Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_002_ner_conll2003 (completed on autodl-5090)\", \"wall_clock_seconds\": 87330.3, \"gpu_hours\": 24.26}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_002_ner_conll2003 (DONE)\", \"notes\": \"Completed as exp_002_conll_n16 on autodl-5090. Registry status corrected.\", \"completed_at\": \"2026-05-15T12:41:26.419Z\"}, \"exp_019_supervised_verifier\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:08:54.395Z\", \"updated_at\": \"2026-05-15T12:40:53.995Z\", \"spec\": {\"hypothesis\": \"Supervised verifier (DeBERTa-v3-large) can close the correlation-selection gap, proving the gap is closable with supervision\", \"plan_id\": \"exp-019\", \"model_name\": \"microsoft/deberta-v3-large\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl\", \"data_count\": 551, \"seed\": 42}, \"conclusion\": \"killed\", \"notes\": \"Cancelled by Director: DDL risk too high (3-4 days for implementation+training+eval+paper), scope creep for analytical paper, free-form ablation already provides sufficient mechanistic evidence\", \"completed_at\": \"2026-05-15T12:40:53.995Z\"}, \"exp_011_ood_conll_to_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:36:08.325Z\", \"updated_at\": \"2026-05-15T12:36:55.551Z\", \"spec\": {\"hypothesis\": \"SCS structural signals remain effective under domain shift (CoNLL model on SciERC data, joint NER+RE)\", \"plan_id\": \"exp-011\", \"model_name\": \"qwen3-8b-conll2003-merged\", \"data_path\": \"data/scierc/processed_data\", \"seed\": 42, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 181723, \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --dataset scierc --data_dir data/scierc/processed_data --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --collect_logprobs --output_dir output/exp_011_ood_conll_to_scierc\", \"data_count\": 551}, \"conclusion\": \"negative\", \"checkpoint_path\": \"output/exp_011_ood_conll_to_scierc/samples.jsonl\", \"log_path\": \"output/exp_011_ood_conll_to_scierc/report.json\", \"completed_at\": \"2026-05-15T11:50:21.969Z\", \"metrics\": {\"greedy_ner_f1\": 0.009, \"greedy_re_f1\": 0.001, \"avg_structural_rho\": -0.05, \"verdict\": \"FAIL\", \"reason\": \"schema_incompatibility\", \"direction\": \"CoNLL_model_to_SciERC_data\", \"sample_f1_pct_zero_ner\": 98.06, \"rho_sj_ner\": -0.186, \"rho_fk_ner\": -0.069, \"note\": \"Schema incompatibility (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material) causes catastrophic failure. Cannot evaluate confidence signals.\"}}, \"exp_011_ood_scierc_to_conll\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:36:07.210Z\", \"updated_at\": \"2026-05-15T12:36:43.115Z\", \"spec\": {\"hypothesis\": \"SCS structural signals remain effective under domain shift (SciERC model on CoNLL data)\", \"plan_id\": \"exp-011\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"data_path\": \"data/conll2003\", \"seed\": 42, \"pid\": 179761, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset conll2003 --data_dir data/conll2003 --subtask ner --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --collect_logprobs --output_dir output/exp_011_ood_scierc_to_conll\", \"data_count\": 3500}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp_011_ood_scierc_to_conll/samples.jsonl\", \"log_path\": \"output/exp_011_ood_scierc_to_conll/report.json\", \"completed_at\": \"2026-05-15T11:47:47.953Z\", \"metrics\": {\"greedy_ner_f1\": 0.522, \"rho_vc\": 0.469, \"rho_sj\": 0.378, \"rho_em\": 0.3, \"rho_fk\": 0.285, \"rho_lp\": 0.246}}, \"exp_017_llama_conll_n16_s456_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:04.572Z\", \"updated_at\": \"2026-05-15T11:45:25.899Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed456.\", \"parent\": \"exp_017_llama_conll_n16_s456\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 456, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s456_r1024\", \"gpu\": \"cuda:2\", \"pid\": \"175870\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"tmux_session\": \"exp_017_llama_conll_n16_s456_r1024\"}, \"conclusion\": \"success\", \"metrics\": {\"instance_count\": 3453, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_sj_ner\": 0.1895, \"rho_fk_ner\": 0.8085, \"rho_vc_ner\": 0.7968, \"rho_lp_ner\": 0.0923, \"rho_em_ner\": 0.1859, \"auroc_sj_ner\": 0.6299, \"auroc_fk_ner\": 0.9059, \"auroc_vc_ner\": 0.8775, \"auroc_lp_ner\": 0.587, \"auroc_em_ner\": 0.6294, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\"}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"output/exp_017_llama_conll_n16_s456_r1024_run.log\", \"completed_at\": \"2026-05-15T11:45:25.899Z\"}, \"exp_017_llama_conll_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:01.036Z\", \"updated_at\": \"2026-05-15T11:45:23.213Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed42.\", \"parent\": \"exp_017_llama_conll_n16\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_r1024\", \"gpu\": \"cuda:1\", \"pid\": \"175734\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"tmux_session\": \"exp_017_llama_conll_n16_r1024\"}, \"conclusion\": \"success\", \"metrics\": {\"instance_count\": 3453, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9264, \"ner_oracle_f1\": 0.9494, \"rho_sj_ner\": 0.1815, \"rho_fk_ner\": 0.8095, \"rho_vc_ner\": 0.7949, \"rho_lp_ner\": 0.0903, \"rho_em_ner\": 0.1785, \"auroc_sj_ner\": 0.6313, \"auroc_fk_ner\": 0.907, \"auroc_vc_ner\": 0.8757, \"auroc_lp_ner\": 0.5861, \"auroc_em_ner\": 0.631, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\"}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"output/exp_017_llama_conll_n16_r1024_run.log\", \"completed_at\": \"2026-05-15T11:45:23.213Z\"}, \"exp_001_n16_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T12:10:30.350Z\", \"updated_at\": \"2026-05-15T11:44:54.370Z\", \"completed_at\": \"2026-05-14T12:28:38.721Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.6577, \"oracle_f1\": 0.8129, \"headroom\": 0.1553, \"rho_sj_full\": 0.3297, \"rho_fk_full\": 0.2578, \"rho_logprob_full\": 0.2866, \"rho_sj_cond\": 0.3394, \"rho_fk_cond\": 0.2721, \"rho_logprob_cond\": 0.2567, \"sj_beats_fk\": true, \"rho_advantage\": 0.0719}, \"re\": {\"greedy_f1\": 0.4312, \"oracle_f1\": 0.6737, \"headroom\": 0.2425, \"rho_sj_full\": 0.285, \"rho_fk_full\": 0.2372, \"rho_logprob_full\": 0.2626, \"rho_sj_cond\": 0.3525, \"rho_fk_cond\": 0.2614, \"rho_logprob_cond\": 0.1927, \"sj_beats_fk\": true, \"rho_advantage\": 0.0478}, \"verdict\": \"FAIL\"}}}, \"spec\": {\"hypothesis\": \"N=16 seed456 multi-seed robustness verification for SciERC NER+RE\", \"plan_id\": \"exp-001\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"seed\": 456, \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --output_dir output/exp001_n16_seed456 --collect_logprobs\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"174595\", \"log_path\": \"output/exp001_n16_seed456_run.log\", \"tmux_session\": \"exp_001_n16_seed456\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (inference-only)\", \"metrics\": {\"instance_count\": 551, \"parse_rate\": 1, \"ner_greedy_f1\": 0.6617, \"ner_oracle_f1\": 0.8075, \"re_greedy_f1\": 0.4215, \"re_oracle_f1\": 0.4748, \"rho_sj_ner\": 0.4134, \"rho_fk_ner\": 0.3448, \"rho_vc_ner\": 0.4042, \"rho_lp_ner\": 0.2136, \"rho_em_ner\": 0.2907, \"rho_sj_re\": 0.1966, \"rho_fk_re\": 0.2179, \"rho_vc_re\": 0.2155, \"rho_lp_re\": 0.4006, \"rho_em_re\": 0.028, \"auroc_sj_ner\": 0.7094, \"auroc_fk_ner\": 0.6499, \"auroc_vc_ner\": 0.6776, \"auroc_lp_ner\": 0.6121, \"auroc_em_ner\": 0.6542}, \"log_path\": \"output/exp001_n16_seed456_run.log\"}, \"exp_017_llama_conll_n16_s123_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:02.953Z\", \"updated_at\": \"2026-05-15T10:38:43.623Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed123.\", \"parent\": \"exp_017_llama_conll_n16_s123\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 123, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s123_r1024\", \"data_path\": \"data/conll2003\", \"data_count\": 3453}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:20:51.219Z\", \"notes\": \"Output exists on autodl-5090. Registry status corrected from killed to success.\"}, \"exp_freeform_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:42:22.868Z\", \"updated_at\": \"2026-05-15T10:00:09.238Z\", \"spec\": {\"command\": \"python run_freeform_inference.py --seed 42 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"169042\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_ablation.log\", \"submitted_at\": \"2026-05-15T09:42:30.236Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Free-form decoding recovers logprob variance and selection ability lost under constrained decoding\", \"plan_id\": \"exp-018\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"tmux_session\": \"exp_freeform_ablation\", \"wall_clock_seconds\": 1059.0, \"gpu_hours\": 0.29}, \"conclusion\": \"negative\", \"metrics\": {\"lp_std_ratio_free_vs_constrained\": 0.97, \"lp_range_ratio\": 0.96, \"tied_fraction_constrained\": 0.597, \"tied_fraction_freeform\": 0.577, \"ner_selection_gap_constrained\": 0.0059, \"ner_selection_gap_freeform\": 0.0018, \"re_selection_gap_constrained\": -0.0068, \"re_selection_gap_freeform\": 0.0169, \"parse_rate\": 0.9995, \"ner_vc_rho_constrained\": 0.3792, \"ner_vc_rho_freeform\": 0.4089}, \"checkpoint_path\": \"N/A (inference-only experiment)\", \"completed_at\": \"2026-05-15T10:00:09.238Z\"}, \"exp_018_llama_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:15.150Z\", \"updated_at\": \"2026-05-15T06:22:40.868Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: LLaMA SciERC N=8 seed=456, max_tokens=1024. Fresh inference (D066 decision: replace exp_007 re-analysis with independent replication).\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T06:08:05.756Z\", \"notes\": \"SUPERSEDED by exp_018_llama_scierc_seed456_r1024 (D066). Original data was re-analysis of exp_007_llama_seed456, not independent inference. Fresh rerun with explicit max_tokens=1024 now canonical.\"}, \"exp_018_llama_scierc_seed42_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:09:57.155Z\", \"updated_at\": \"2026-05-15T06:21:59.257Z\", \"spec\": {\"hypothesis\": \"D066 fresh rerun: LLaMA SciERC seed=42 with explicit max_tokens=1024. Replaces exp_007_llama_inference for clean 3-seed comparison.\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed42_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 42, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed42_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed42_r1024.log\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"156809\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed42_r1024.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed42_r1024\\\"\", \"finished_at\": \"2026-05-15T06:15:47.963Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:15:50.613872+00:00\"}]}, \"metrics\": {\"ner\": {\"full\": {\"SJ\": {\"rho\": 0.3096, \"tau\": 0.2288, \"auroc\": 0.6683}, \"FK\": {\"rho\": 0.2352, \"tau\": 0.1759, \"auroc\": 0.6069}, \"logprob\": {\"rho\": 0.1503, \"tau\": 0.1087, \"auroc\": 0.5318}, \"EM\": {\"rho\": 0.2587, \"tau\": 0.1966, \"auroc\": 0.7174}, \"voting_conf\": {\"rho\": 0.4053, \"tau\": 0.3042, \"auroc\": 0.6967}}, \"conditional\": {\"SJ\": {\"rho\": 0.2718, \"tau\": null, \"auroc\": 0.6565}, \"FK\": {\"rho\": 0.1472, \"tau\": null, \"auroc\": 0.5866}, \"logprob\": {\"rho\": 0.081, \"tau\": null, \"auroc\": 0.5129}, \"EM\": {\"rho\": 0.3165, \"tau\": null, \"auroc\": 0.7244}, \"voting_conf\": {\"rho\": 0.3078, \"tau\": null, \"auroc\": 0.6714}}, \"greedy_f1\": 0.6607, \"oracle_f1\": 0.7781, \"n_full\": 529, \"n_cond\": 478}, \"re\": {\"full\": {\"SJ\": {\"rho\": 0.2748, \"tau\": 0.2102, \"auroc\": 0.7244}, \"FK\": {\"rho\": 0.3027, \"tau\": 0.2337, \"auroc\": 0.691}, \"logprob\": {\"rho\": 0.3163, \"tau\": 0.233, \"auroc\": 0.6313}, \"EM\": {\"rho\": 0.1681, \"tau\": 0.1275, \"auroc\": 0.7697}, \"voting_conf\": {\"rho\": 0.384, \"tau\": 0.2965, \"auroc\": 0.7337}}, \"conditional\": {\"SJ\": {\"rho\": 0.3461, \"tau\": null, \"auroc\": 0.7233}, \"FK\": {\"rho\": 0.1969, \"tau\": null, \"auroc\": 0.6684}, \"logprob\": {\"rho\": 0.0888, \"tau\": null, \"auroc\": 0.5556}, \"EM\": {\"rho\": 0.4969, \"tau\": null, \"auroc\": 0.819}, \"voting_conf\": {\"rho\": 0.3433, \"tau\": null, \"auroc\": 0.7003}}, \"greedy_f1\": 0.4319, \"oracle_f1\": 0.5775, \"n_full\": 397, \"n_cond\": 251}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:21:47.660Z\"}, \"exp_018_llama_scierc_seed456_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:12:43.492Z\", \"updated_at\": \"2026-05-15T06:21:49.320Z\", \"spec\": {\"hypothesis\": \"D066 fresh rerun: LLaMA SciERC seed=456 with explicit max_tokens=1024. Replaces exp_007 re-analysis for clean 3-seed comparison.\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"157584\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"finished_at\": \"2026-05-15T06:18:22.307Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:18:24.880896+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed456_r1024\", \"metrics\": {\"ner_greedy_f1\": 0.6597, \"ner_oracle_f1\": 0.7683, \"ner_oracle_headroom\": 0.1086, \"ner_cond_rho_fk\": 0.1472, \"ner_cond_rho_sj\": 0.2718, \"ner_cond_rho_logprob\": 0.083, \"ner_logprob_auroc_cond\": 0.5485, \"re_greedy_f1\": 0.4338, \"re_oracle_f1\": 0.5834, \"re_oracle_headroom\": 0.1496, \"re_cond_rho_fk\": 0.2107, \"re_cond_rho_sj\": 0.3898, \"re_cond_rho_logprob\": 0.1252, \"re_logprob_auroc_cond\": 0.6119, \"ner_structural_beats_logprob\": true, \"re_structural_beats_logprob\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:21:45.350Z\"}, \"exp_018_llama_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:14.370Z\", \"updated_at\": \"2026-05-15T06:08:04.855Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: LLaMA SciERC N=8 seed=123, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_llama_scierc_seed123\", \"server\": \"autodl-5090\", \"seed\": 123, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed123/\", \"log_path\": \"output/exp_018_llama_scierc_seed123.log\", \"samples_md5\": \"072eeca68236d46b4c5c84b945209abc\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:04.855Z\"}, \"exp_018_qwen_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:13.570Z\", \"updated_at\": \"2026-05-15T06:08:03.898Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: Qwen SciERC N=8 seed=456, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 456 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed456\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_qwen_scierc_seed456/\", \"log_path\": \"output/exp_018_qwen_scierc_seed456/run.log\", \"samples_md5\": \"46d0de47ad7693c07e7df3a77c90c3be\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:03.898Z\"}, \"exp_018_qwen_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:12.747Z\", \"updated_at\": \"2026-05-15T06:08:02.954Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: Qwen SciERC N=8 seed=123, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed123\", \"server\": \"autodl-5090\", \"seed\": 123, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_qwen_scierc_seed123/\", \"log_path\": \"output/exp_018_qwen_scierc_seed123.log\", \"samples_md5\": \"866a59581dea56f4633149f0b18a31ae\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:02.954Z\"}, \"exp_002_conll_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:57.682Z\", \"updated_at\": \"2026-05-15T01:20:53.108Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen CoNLL N=16.\", \"parent\": \"exp_002_conll_n16\", \"model_name\": \"qwen3-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_002_conll_n16_r1024\", \"data_path\": \"data/conll2003\", \"data_count\": 3453}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:53.108Z\"}, \"exp_007_llama_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:59.685Z\", \"updated_at\": \"2026-05-15T01:20:52.194Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA SciERC N=16.\", \"parent\": \"exp_007_llama_n16\", \"model_name\": \"llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_007_llama_n16_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:52.194Z\"}, \"exp_001_seed123_v2_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:54.442Z\", \"updated_at\": \"2026-05-15T01:20:49.812Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed123.\", \"parent\": \"exp_001_seed123_v2\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 123, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed123_v2_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 529}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:49.812Z\"}, \"exp_001_seed456_v2_ner_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:55.975Z\", \"updated_at\": \"2026-05-15T01:20:48.914Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed456.\", \"parent\": \"exp_001_seed456_v2_ner\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 456, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed456_v2_ner_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:48.914Z\"}, \"exp_016_rerun_1024_bootstrap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:44:21.577Z\", \"updated_at\": \"2026-05-14T23:44:48.818Z\", \"hypothesis\": \"3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant.\", \"spec\": {\"command\": \"python code/bootstrap_significance.py\", \"server\": \"local\", \"data_path\": \"output/exp_016_rerun_1024/\", \"data_count\": 529, \"model_name\": \"N/A (statistical analysis)\", \"seed\": \"3-seed bootstrap (1000 iterations)\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_016_rerun_1024_bootstrap/\"}, \"conclusion\": \"negative\", \"metrics\": {\"bootstrap_ci_95\": [-0.03, 0.042], \"permutation_p\": 0.39, \"cohen_d\": 0.038, \"sign_test_win_rate\": 0.466, \"ner_logprob_vs_greedy_delta\": 0.006, \"conclusion_summary\": \"NER selection: no signal significantly outperforms greedy; RE: same conclusion\"}, \"completed_at\": \"2026-05-14T23:44:48.818Z\"}, \"exp_015_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-14T23:11:11.790Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:34:56.741Z\", \"metrics\": {\"scierc_ner_avg\": {\"sj_auroc\": 0.7394, \"fk_auroc\": 0.6172, \"em_auroc\": 0.7873, \"voting_auroc\": 0.7367, \"logprob_auroc\": 0.5918}, \"scierc_re_avg\": {\"sj_auroc\": 0.6746, \"fk_auroc\": 0.5939, \"em_auroc\": 0.715, \"voting_auroc\": 0.7234, \"logprob_auroc\": 0.5849}}}, \"exp_012_rerun_1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:11:33.777Z\", \"updated_at\": \"2026-05-14T23:10:58.651Z\", \"spec\": {\"hypothesis\": \"Verify if max_tokens=512 truncation inflated Table 1 N=8 SciERC signal values. Rerun with max_tokens=1024 for clean comparison.\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"parent\": \"exp_012_logprob_baseline\", \"data_count\": 551, \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_012_rerun_1024\", \"checkpoint_path\": \"output/exp_012_rerun_1024/\", \"log_path\": \"output/exp_012_rerun_1024/run.log\", \"data_path\": \"data/scierc/processed_data\"}, \"conclusion\": \"success\", \"metrics\": {\"ner_full\": {\"n\": 529, \"SJ\": {\"rho\": 0.3599, \"tau\": 0.2646, \"AUROC\": 0.6917, \"ECE\": 0.4531, \"rho_ci95\": [0.2732, 0.4389], \"AUROC_ci95\": [0.6304, 0.7406]}, \"FK\": {\"rho\": 0.2665, \"tau\": 0.1974, \"AUROC\": 0.629, \"ECE\": 0.4512, \"rho_ci95\": [0.1743, 0.3486], \"AUROC_ci95\": [0.5612, 0.6882]}, \"logprob\": {\"rho\": 0.2052, \"tau\": 0.1478, \"AUROC\": 0.5783, \"ECE\": 0.7064, \"rho_ci95\": [0.1171, 0.2904], \"AUROC_ci95\": [0.5179, 0.6387]}, \"EM\": {\"rho\": 0.2945, \"tau\": 0.2208, \"AUROC\": 0.7493, \"ECE\": 0.3526, \"rho_ci95\": [0.2094, 0.37], \"AUROC_ci95\": [0.7002, 0.7928]}, \"voting_conf\": {\"rho\": 0.3792, \"tau\": 0.2805, \"AUROC\": 0.6841, \"ECE\": 0.3807, \"rho_ci95\": [0.2972, 0.4486], \"AUROC_ci95\": [0.6249, 0.7366]}}, \"ner_cond\": {\"n\": 477, \"SJ\": {\"rho\": 0.3113, \"tau\": 0.2257, \"AUROC\": 0.6772, \"ECE\": 0.4416, \"rho_ci95\": [0.2353, 0.3959], \"AUROC_ci95\": [0.621, 0.7337]}, \"FK\": {\"rho\": 0.1761, \"tau\": 0.1284, \"AUROC\": 0.6078, \"ECE\": 0.4389, \"rho_ci95\": [0.0839, 0.2665], \"AUROC_ci95\": [0.5442, 0.6709]}, \"logprob\": {\"rho\": 0.1538, \"tau\": 0.1111, \"AUROC\": 0.5633, \"ECE\": 0.6803, \"rho_ci95\": [0.0637, 0.2424], \"AUROC_ci95\": [0.5032, 0.6232]}, \"EM\": {\"rho\": 0.3596, \"tau\": 0.2735, \"AUROC\": 0.7556, \"ECE\": 0.3257, \"rho_ci95\": [0.2819, 0.4408], \"AUROC_ci95\": [0.7011, 0.8107]}, \"voting_conf\": {\"rho\": 0.3, \"tau\": 0.2189, \"AUROC\": 0.6618, \"ECE\": 0.3746, \"rho_ci95\": [0.2168, 0.3836], \"AUROC_ci95\": [0.6004, 0.7201]}}, \"re_full\": {\"n\": 397, \"SJ\": {\"rho\": 0.2503, \"tau\": 0.1878, \"AUROC\": 0.6702, \"ECE\": 0.3865}, \"FK\": {\"rho\": 0.2752, \"tau\": 0.2117, \"AUROC\": 0.6089, \"ECE\": 0.4405}, \"logprob\": {\"rho\": 0.2662, \"tau\": 0.1951, \"AUROC\": 0.6005, \"ECE\": 0.7694}, \"EM\": {\"rho\": 0.1344, \"tau\": 0.1081, \"AUROC\": 0.7059, \"ECE\": 0.3548}, \"voting_conf\": {\"rho\": 0.3498, \"tau\": 0.2663, \"AUROC\": 0.6935, \"ECE\": 0.2724}}, \"re_cond\": {\"n\": 238, \"SJ\": {\"rho\": 0.2457, \"tau\": 0.1811, \"AUROC\": 0.6463, \"ECE\": 0.2941}, \"FK\": {\"rho\": 0.1139, \"tau\": 0.0876, \"AUROC\": 0.551, \"ECE\": 0.3424}, \"logprob\": {\"rho\": 0.0112, \"tau\": 0.0051, \"AUROC\": 0.5186, \"ECE\": 0.6464}, \"EM\": {\"rho\": 0.4165, \"tau\": 0.3256, \"AUROC\": 0.7515, \"ECE\": 0.2232}, \"voting_conf\": {\"rho\": 0.2409, \"tau\": 0.178, \"AUROC\": 0.642, \"ECE\": 0.207}}, \"delta_vs_512_ner_full_rho\": {\"SJ\": 0.0034, \"FK\": 0.0014, \"EM\": 0.0379, \"voting_conf\": -0.1226, \"logprob\": 0.0656}, \"provenance_note\": \"exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205.\"}, \"completed_at\": \"2026-05-14T23:10:33.075Z\"}, \"exp_001_seed42_v2_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:52.571Z\", \"updated_at\": \"2026-05-14T22:28:53.686Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed42.\", \"parent\": \"exp_001_seed42_v2\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed42_v2_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"metrics\": {\"greedy_f1\": 0.6647, \"oracle_f1\": 0.8106, \"softjaccard_rho_full\": 0.3928, \"fleiss_rho_full\": 0.2489, \"logprob_rho_full\": 0.2136, \"softjaccard_rho_cond\": 0.3455, \"fleiss_rho_cond\": 0.163, \"logprob_rho_cond\": 0.1624, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"output/exp_001_seed42_v2_r1024\", \"log_path\": \"output/exp_001_seed42_v2_r1024/run.log\", \"completed_at\": \"2026-05-14T22:27:43.836Z\"}, \"exp_017_llama_conll_n16_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:23:21.987Z\", \"updated_at\": \"2026-05-14T20:24:45.875Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s456\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 456}, \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9488, \"oracle_headroom\": 0.0245, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4552, \"SJ_AUROC\": 0.7288, \"SJ_ECE\": 0.1134, \"FK_rho\": 0.4478, \"FK_AUROC\": 0.7248, \"FK_ECE\": 0.109, \"logprob_rho\": 0.3078, \"logprob_AUROC\": 0.7612, \"logprob_ECE\": 0.1289, \"EM_rho\": 0.452, \"EM_AUROC\": 0.7275, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4571, \"voting_conf_AUROC\": 0.7348, \"voting_conf_ECE\": 0.0863}, \"conditional\": {\"SJ_rho\": 0.4505, \"SJ_AUROC\": 0.7449, \"SJ_ECE\": 0.0826, \"FK_rho\": 0.4422, \"FK_AUROC\": 0.7401, \"FK_ECE\": 0.0835, \"logprob_rho\": 0.3242, \"logprob_AUROC\": 0.8067, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.451, \"EM_AUROC\": 0.745, \"EM_ECE\": 0.0756, \"voting_conf_rho\": 0.3962, \"voting_conf_AUROC\": 0.7202, \"voting_conf_ECE\": 0.0746}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9215, \"sj_best\": 0.9243, \"logprob_best\": 0.9243, \"voting_conf_best\": 0.9243, \"oracle\": 0.9488}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0238, \"full_FK_rho_delta\": 0.0201, \"full_logprob_rho_delta\": 0.0006, \"full_EM_rho_delta\": 0.0214, \"full_voting_conf_rho_delta\": 0.0315, \"cond_SJ_rho_delta\": 0.0149, \"cond_FK_rho_delta\": 0.0112, \"cond_logprob_rho_delta\": -0.004, \"cond_EM_rho_delta\": 0.0107, \"cond_voting_conf_rho_delta\": 0.0219}}, \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s456/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16_s456/all_signals_report.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:24:45.875Z\"}, \"exp_017_llama_conll_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:19:35.318Z\", \"updated_at\": \"2026-05-14T19:45:16.265Z\", \"spec\": {\"hypothesis\": \"LLaMA CoNLL N=16: complete the 2x2 matrix (model x dataset x N). If SJ N-scaling holds for LLaMA on CoNLL, the finding is fully cross-model cross-dataset.\", \"plan_id\": \"exp-017\", \"parent\": \"exp_017_llama_conll_infer\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"data_count\": 3453, \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_017_llama_conll_n16\", \"data_path\": \"data/conll2003\", \"pid\": 106997, \"n_samples\": 16, \"temperature\": 1, \"checkpoint_source\": \"checkpoints/llama3.1-8b-conll2003-merged\", \"eval_data\": \"conll2003 test set\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16/all_signals_report.json\"}, \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9487, \"oracle_headroom\": 0.0244, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4642, \"SJ_AUROC\": 0.7391, \"SJ_ECE\": 0.1131, \"FK_rho\": 0.4566, \"FK_AUROC\": 0.736, \"FK_ECE\": 0.1071, \"logprob_rho\": 0.3058, \"logprob_AUROC\": 0.7594, \"logprob_ECE\": 0.1288, \"EM_rho\": 0.4613, \"EM_AUROC\": 0.7391, \"EM_ECE\": 0.1084, \"voting_conf_rho\": 0.4554, \"voting_conf_AUROC\": 0.7406, \"voting_conf_ECE\": 0.0844}, \"conditional\": {\"SJ_rho\": 0.4597, \"SJ_AUROC\": 0.7565, \"SJ_ECE\": 0.0846, \"FK_rho\": 0.4515, \"FK_AUROC\": 0.753, \"FK_ECE\": 0.0813, \"logprob_rho\": 0.3193, \"logprob_AUROC\": 0.8023, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.4618, \"EM_AUROC\": 0.7589, \"EM_ECE\": 0.0757, \"voting_conf_rho\": 0.3978, \"voting_conf_AUROC\": 0.7287, \"voting_conf_ECE\": 0.0742}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9213, \"sj_best\": 0.9259, \"logprob_best\": 0.925, \"voting_conf_best\": 0.9268, \"oracle\": 0.9487}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0328, \"full_FK_rho_delta\": 0.0289, \"full_logprob_rho_delta\": -0.0014, \"full_EM_rho_delta\": 0.0307, \"full_voting_conf_rho_delta\": 0.0298, \"cond_SJ_rho_delta\": 0.0241, \"cond_FK_rho_delta\": 0.0205, \"cond_logprob_rho_delta\": -0.0089, \"cond_EM_rho_delta\": 0.0215, \"cond_voting_conf_rho_delta\": 0.0235}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:45:16.265Z\"}, \"exp_017_llama_conll_n16_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:23:21.084Z\", \"updated_at\": \"2026-05-14T19:43:06.607Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\", \"spec\": {\"hypothesis\": \"LLaMA CoNLL-2003 NER N=16 seed=123: cross-seed robustness check against N=8 seed=42 baseline (exp_017_llama_conll_infer)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s123\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/llama3.1-8b-conll2003-merged\", \"eval_data\": \"data/conll2003\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s123/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16_s123.log\"}, \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9497, \"oracle_headroom\": 0.0231, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4698, \"SJ_AUROC\": 0.7402, \"SJ_ECE\": 0.1135, \"FK_rho\": 0.4594, \"FK_AUROC\": 0.7351, \"FK_ECE\": 0.1114, \"logprob_rho\": 0.3161, \"logprob_AUROC\": 0.768, \"logprob_ECE\": 0.129, \"EM_rho\": 0.4676, \"EM_AUROC\": 0.7399, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4612, \"voting_conf_AUROC\": 0.7429, \"voting_conf_ECE\": 0.0832}, \"conditional\": {\"SJ_rho\": 0.4712, \"SJ_AUROC\": 0.7609, \"SJ_ECE\": 0.0828, \"FK_rho\": 0.4595, \"FK_AUROC\": 0.7547, \"FK_ECE\": 0.0858, \"logprob_rho\": 0.3314, \"logprob_AUROC\": 0.8134, \"logprob_ECE\": 0.0922, \"EM_rho\": 0.4732, \"EM_AUROC\": 0.7626, \"EM_ECE\": 0.075, \"voting_conf_rho\": 0.4086, \"voting_conf_AUROC\": 0.7338, \"voting_conf_ECE\": 0.0706}, \"best_of_n\": {\"greedy\": 0.9242, \"random_avg\": 0.9216, \"sj_best\": 0.9247, \"logprob_best\": 0.9253, \"voting_conf_best\": 0.9255, \"oracle\": 0.9486}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0384, \"full_FK_rho_delta\": 0.0317, \"full_logprob_rho_delta\": 0.0089, \"full_SJ_AUROC_delta\": 0.0363, \"full_FK_AUROC_delta\": 0.0325, \"full_logprob_AUROC_delta\": 0.007, \"cond_SJ_rho_delta\": 0.0356, \"cond_FK_rho_delta\": 0.0285, \"cond_logprob_rho_delta\": 0.0032}}, \"log_path\": \"output/exp_017_llama_conll_n16_s123.log\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s123/samples.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:43:06.607Z\"}, \"exp_007_llama_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:31:44.366Z\", \"updated_at\": \"2026-05-14T19:03:50.284Z\", \"spec\": {\"hypothesis\": \"LLaMA SciERC N=16: cross-model N-scaling validation. If SJ rho increases from N=8 (0.363) to N=16, N-scaling is model-agnostic.\", \"plan_id\": \"exp-007\", \"parent\": \"exp_007_llama_inference\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_n16\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"eval_data\": \"data/scierc/processed_data\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp_007_llama_n16/samples.jsonl\", \"log_path\": \"output/exp_007_llama_n16.log\", \"completed_at\": \"2026-05-14T19:03:39.163Z\", \"metrics\": {\"N\": 16, \"dataset\": \"scierc\", \"subtask\": \"ner\", \"n_instances\": 551, \"n_valid\": 529, \"n_conditional\": 478, \"greedy_f1\": 0.645, \"full\": {\"SJ_rho\": 0.3791, \"FK_rho\": 0.3081, \"logprob_rho\": 0.2041, \"EM_rho\": 0.3159, \"voting_conf_rho\": 0.4515, \"SJ_AUROC\": 0.717, \"FK_AUROC\": 0.6581, \"logprob_AUROC\": 0.5656, \"EM_AUROC\": 0.7686, \"voting_conf_AUROC\": 0.7266, \"SJ_ECE\": 0.1019, \"FK_ECE\": 0.1556, \"logprob_ECE\": 0.084, \"EM_ECE\": 0.1761, \"voting_conf_ECE\": 0.1365}, \"conditional\": {\"SJ_rho\": 0.3222, \"FK_rho\": 0.2182, \"logprob_rho\": 0.1286, \"EM_rho\": 0.3563, \"voting_conf_rho\": 0.3356, \"SJ_AUROC\": 0.7014, \"FK_AUROC\": 0.6392, \"logprob_AUROC\": 0.545, \"EM_AUROC\": 0.7708, \"voting_conf_AUROC\": 0.6988, \"SJ_ECE\": 0.1466, \"FK_ECE\": 0.1853, \"logprob_ECE\": 0.1141, \"EM_ECE\": 0.1887, \"voting_conf_ECE\": 0.2634}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0161, \"FK\": -0.0185, \"logprob\": 0.0214, \"EM\": 0.0007, \"voting_conf\": 0.0184}}}, \"exp_002_conll_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:12:16.041Z\", \"updated_at\": \"2026-05-14T19:03:19.801Z\", \"spec\": {\"hypothesis\": \"Qwen CoNLL-2003 N=16: cross-dataset N-scaling comparison with SciERC N=16\", \"plan_id\": \"exp-002\", \"parent\": \"exp_002_ner_conll2003\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_002_conll_n16\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"N\": 16, \"dataset\": \"conll2003\", \"subtask\": \"ner\", \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2614, \"greedy_f1\": 0.907, \"full\": {\"SJ_rho\": 0.4496, \"FK_rho\": 0.3928, \"logprob_rho\": 0.3146, \"EM_rho\": 0.4627, \"voting_conf_rho\": 0.4286, \"SJ_AUROC\": 0.8264, \"FK_AUROC\": 0.7821, \"logprob_AUROC\": 0.7531, \"EM_AUROC\": 0.8409, \"voting_conf_AUROC\": 0.8071, \"SJ_ECE\": 0.0747, \"FK_ECE\": 0.1786, \"logprob_ECE\": 0.2031, \"EM_ECE\": 0.0786, \"voting_conf_ECE\": 0.529}, \"conditional\": {\"SJ_rho\": 0.4208, \"FK_rho\": 0.3494, \"logprob_rho\": 0.3756, \"EM_rho\": 0.4658, \"voting_conf_rho\": 0.3654, \"SJ_AUROC\": 0.8405, \"FK_AUROC\": 0.7819, \"logprob_AUROC\": 0.8259, \"EM_AUROC\": 0.8781, \"voting_conf_AUROC\": 0.7951, \"SJ_ECE\": 0.0982, \"FK_ECE\": 0.1899, \"logprob_ECE\": 0.2504, \"EM_ECE\": 0.0997, \"voting_conf_ECE\": 0.6096}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0139, \"FK\": -0.007, \"logprob\": -0.0011, \"EM\": 0.012, \"voting_conf\": 0.0049}}, \"checkpoint_path\": \"output/exp_002_conll_n16/samples.jsonl\", \"log_path\": \"output/exp_002_conll_n16.log\", \"completed_at\": \"2026-05-14T18:58:40.473Z\"}, \"exp_009_v2_re_rerun\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:56:31.535Z\", \"updated_at\": \"2026-05-14T18:56:58.168Z\", \"spec\": {\"command\": \"python code/exp_009_v2_re_rerun.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_008_re_n16_v2/samples.jsonl\", \"data_count\": 397, \"model_name\": \"cpu_analysis\", \"seed\": 42, \"checkpoint_source\": \"exp_008_re_n16_v2\", \"checkpoint_path\": \"output/exp_009_v2_re_rerun/results.json\", \"log_path\": \"/tmp/re_rerun.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:56:58.168Z\"}, \"exp_001_seed456_v2_ner\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:13:00.414Z\", \"updated_at\": \"2026-05-14T18:55:18.772Z\", \"spec\": {\"hypothesis\": \"NER N=16 seed=456 robustness test (NER-only rerun, fixing subtask mismatch from exp_001_seed456_v2)\", \"plan_id\": \"exp-001\", \"parent\": \"exp_001_seed456_v2\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed456_v2_ner\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"eval_data\": \"data/scierc/processed_data\", \"metrics\": {\"sj_rho\": 0.384, \"structural_gt_surface\": true, \"structural_surface_delta\": 0.16}, \"log_path\": \"output/exp_001_seed456_v2_ner.log\", \"checkpoint_path\": \"output/exp_001_seed456_v2_ner/\"}, \"log_path\": \"output/exp_001_seed456_v2_ner.log\", \"pid\": 96161, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:52:01.372Z\", \"metrics\": {\"full\": {\"SJ\": {\"rho\": 0.384, \"auroc\": 0.711}, \"FK\": {\"rho\": 0.223, \"auroc\": 0.577}, \"logprob\": {\"rho\": 0.232, \"auroc\": 0.594}, \"EM\": {\"rho\": 0.316, \"auroc\": 0.768}, \"voting_conf\": {\"rho\": 0.411, \"auroc\": 0.712}}, \"conditional\": {\"SJ\": {\"rho\": 0.349, \"auroc\": 0.699}, \"FK\": {\"rho\": 0.157, \"auroc\": 0.561}, \"logprob\": {\"rho\": 0.171, \"auroc\": 0.576}, \"EM\": {\"rho\": 0.406, \"auroc\": 0.78}, \"voting_conf\": {\"rho\": 0.346, \"auroc\": 0.694}}, \"3seed_mean_SJ_rho_full\": 0.412, \"3seed_sd_SJ_rho_full\": 0.025, \"structural_beats_surface\": true, \"verdict\": \"MARGINAL\"}}, \"exp_003_wnut17_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:32:56.415Z\", \"updated_at\": \"2026-05-14T18:11:36.559Z\", \"spec\": {\"description\": \"WNUT-17 retrain: downsample gold-empty instances to ≤25%, fine-tune Qwen3-8B, inference N=16 T=1.0 with log-probs\", \"hypothesis\": \"After removing excess empty instances, structural consistency signals (SJ) will show stronger correlation on social media NER\", \"plan_id\": \"exp-003\", \"claim\": 1, \"model_name\": \"Qwen3-8B\", \"dataset\": \"WNUT-17 (downsampled)\", \"priority\": \"P0\", \"parent\": \"exp_003_ner_wnut17\", \"command\": \"CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_wnut17.yaml\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/wnut17/llmfactory_train_downsampled.json\", \"data_count\": 1637, \"seed\": 42, \"pid\": 92215, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/train_wnut17.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-lora\", \"downsampling\": \"empty instances 63.8% -> 25.0%, total 3394 -> 1637\", \"metrics\": {\"train_loss\": 0.105, \"eval_loss\": 0.0836, \"epochs\": 5, \"train_time_min\": 16.37, \"train_samples_per_sec\": 8.33}, \"note\": \"D045: Training succeeded (train_loss=0.105) but inference FAIL: 54% F1=0, SJ rho=0.062 (p=0.106). WNUT-17 abandoned — model capability insufficient on social media NER. Paper reports as Claim 3 (capability boundary) evidence.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T18:11:36.559Z\"}, \"exp_017_llama_conll_infer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:33:23.653Z\", \"updated_at\": \"2026-05-14T17:55:35.572Z\", \"spec\": {\"hypothesis\": \"LLaMA-3.1-8B CoNLL-2003 inference: cross-model cross-dataset validation of structural consistency signals\", \"plan_id\": \"exp-017\", \"parent\": \"exp_017_llama_conll\", \"command\": \"python code/run_llama_conll_infer.py\", \"server\": \"autodl-5090\", \"data_path\": \"conll2003 test\", \"data_count\": 3453, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"n_samples\": 8, \"temperature\": 1, \"description\": \"LLaMA CoNLL-2003 NER inference N=8 (cross-model + cross-dataset validation)\"}, \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9443, \"oracle_headroom\": 0.0177, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"N\": 8, \"full\": {\"SJ_rho\": 0.4314, \"FK_rho\": 0.4277, \"logprob_rho\": 0.3072, \"EM_rho\": 0.4306, \"voting_conf_rho\": 0.4256, \"SJ_AUROC\": 0.7039, \"FK_AUROC\": 0.7026, \"logprob_AUROC\": 0.761, \"EM_AUROC\": 0.7046, \"voting_conf_AUROC\": 0.7088, \"SJ_ECE\": 0.1137, \"FK_ECE\": 0.1053, \"logprob_ECE\": 0.129, \"EM_ECE\": 0.1094, \"voting_conf_ECE\": 0.0949}, \"conditional\": {\"SJ_rho\": 0.4356, \"FK_rho\": 0.431, \"logprob_rho\": 0.3282, \"EM_rho\": 0.4403, \"voting_conf_rho\": 0.3743, \"SJ_AUROC\": 0.7225, \"FK_AUROC\": 0.7208, \"logprob_AUROC\": 0.8102, \"EM_AUROC\": 0.7257, \"voting_conf_AUROC\": 0.6989, \"SJ_ECE\": 0.0829, \"FK_ECE\": 0.0796, \"logprob_ECE\": 0.0922, \"EM_ECE\": 0.0754, \"voting_conf_ECE\": 0.0784}}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:55:33.476Z\", \"notes\": \"LLaMA CoNLL-2003 NER N=8 (not N=16, cost constraint: 3453 test instances). SJ ρ=0.431 > logprob ρ=0.307 (Δ=+0.124). ρ-AUROC dissociation: logprob AUROC=0.761 > SJ AUROC=0.704. All 4 structural signals ρ>0.42 vs logprob 0.31. Directly comparable to exp_002 (Qwen CoNLL N=8) and exp_007 (LLaMA SciERC N=8).\"}, \"exp_008_re_n16_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:10.852Z\", \"updated_at\": \"2026-05-14T17:51:43.957Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --num_test 9999 --output_dir output/exp008_re_n16/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:2\"], \"pid\": \"62585\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_008_re_n16_full.log\", \"submitted_at\": \"2026-05-14T12:45:10.764Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18393.2, \"gpu_hours\": 5.11}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_008_re_n16_t10_full (full 551-instance RE-only run on autodl-5090)\", \"completed_at\": \"2026-05-14T17:51:43.957Z\"}, \"exp_017_llama_conll\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:39:32.014Z\", \"updated_at\": \"2026-05-14T17:30:26.798Z\", \"spec\": {\"command\": \"llamafactory-cli train train_config_llama_conll2003.yaml\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 14041, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"failure_reason\": null, \"metrics\": {\"train_loss\": 0.039, \"eval_loss\": 0.023, \"epochs\": 5, \"train_time\": \"2h22m\"}, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/exp017_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-conll2003-lora/\", \"note\": \"Training completed successfully. Checkpoint includes adapter_model.safetensors + intermediate checkpoints (200/400/515). Previously misclassified as failed due to narrow log search path.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:12:15.687Z\"}, \"exp_001_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:38:55.569Z\", \"updated_at\": \"2026-05-14T17:12:14.682Z\", \"spec\": {\"hypothesis\": \"NER/RE N=16 seed=456 robustness test, third seed for 3-seed stability\", \"plan_id\": \"exp-001\", \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed456_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"metrics\": {\"full_rho_kappa_f1\": 0.3383, \"full_rho_sj_f1\": 0.2988, \"cond_rho_kappa_f1\": 0.233, \"cond_rho_sj_f1\": 0.3245, \"logprob_full_rho\": 0.3405, \"logprob_full_auroc\": 0.6694, \"logprob_cond_rho\": 0.0501, \"structural_gt_surface\": false}, \"note\": \"CRITICAL: Ran with --subtask joint instead of --subtask ner. seed42/seed123 v2 used --subtask ner. Results valid for joint-mode analysis but NOT comparable for NER 3-seed protocol. Need NER-only rerun.\", \"log_path\": \"output/exp_001_seed456_v2/run.log\", \"checkpoint_path\": \"output/exp_001_seed456_v2/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T17:12:14.682Z\"}, \"exp_016_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:39:07.501Z\", \"updated_at\": \"2026-05-14T15:39:39.950Z\", \"spec\": {\"command\": \"python code/exp_016_v2_ensemble.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2 + exp_001_seed123_v2 + exp_008_re_n16_v2\", \"data_count\": 551, \"model_name\": \"analysis_only\", \"seed\": 42, \"checkpoint_path\": \"output/exp_016_v2/\", \"log_path\": \"/tmp/exp016v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:39:34.478Z\", \"metrics\": {\"ner_conditional\": {\"n\": 529, \"best_single_signal_rho\": {\"soft_jaccard\": 0.4412}, \"best_combo_rho\": {\"sj+vc_a0.55\": 0.4552}, \"ensemble_auroc\": 0.7141, \"best_single_auroc\": {\"soft_jaccard\": 0.7166}, \"selection_f1\": {\"greedy\": 0.6442, \"logprob_best\": 0.6505, \"ensemble_best\": 0.6475, \"sj_best\": 0.6471, \"oracle\": 0.8442}}, \"re_conditional\": {\"n\": 397, \"best_single_signal_rho\": {\"voting_confidence\": 0.3849}, \"best_combo_rho\": {\"logprob+vc_a0.25\": 0.3936}, \"ensemble_auroc\": 0.6916, \"best_single_auroc\": {\"voting_confidence\": 0.7023}, \"selection_f1\": {\"greedy\": 0.403, \"logprob_best\": 0.4097, \"ensemble_best\": 0.4227, \"oracle\": 0.6306}}, \"re_full\": {\"ensemble_auroc\": 0.8608, \"best_single_auroc\": {\"voting_confidence\": 0.8248}}}}, \"exp_009_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:36:47.946Z\", \"updated_at\": \"2026-05-14T15:37:27.960Z\", \"spec\": {\"command\": \"python3 code/exp_009_v2_stratification.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2 + exp_001_seed123_v2 + exp_008_re_n16_v2\", \"data_count\": 551, \"model_name\": \"analysis\", \"seed\": 42}, \"checkpoint_path\": \"output/exp_009_v2/results.json\", \"log_path\": \"output/exp_009_v2_run.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:37:18.311Z\", \"metrics\": {\"ner_seed42_global\": {\"sj_rho\": 0.431, \"fk_rho\": 0.325, \"logprob_rho\": 0.203, \"voting_conf_rho\": 0.475, \"em_rho\": 0.292}, \"ner_seed123_global\": {\"sj_rho\": 0.422, \"fk_rho\": 0.315, \"logprob_rho\": 0.226, \"voting_conf_rho\": 0.438, \"em_rho\": 0.299}, \"re_seed42_global\": {\"sj_rho\": 0.063, \"fk_rho\": 0.226, \"logprob_rho\": 0.4, \"voting_conf_rho\": 0.22, \"em_rho\": -0.132}, \"ner_seed_stability_max_delta\": 0.037, \"independent_proxies\": [\"sent_len\", \"ent_count\", \"type_diversity\"], \"inverted_u_ner\": \"not confirmed (ρ stable across independent proxies)\", \"inverted_u_re\": \"monotonic increase with complexity, not inverted-U\"}}, \"exp_004_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:31:40.554Z\", \"updated_at\": \"2026-05-14T15:32:04.966Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/analyze_exp004_v2_re_diagnostic.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"model_name\": \"Qwen2.5-7B-Instruct (SFT)\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004v2_re_diagnostic/\"}, \"completed_at\": \"2026-05-14T15:32:04.966Z\"}, \"exp_006_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:30:02.348Z\", \"updated_at\": \"2026-05-14T15:30:41.053Z\", \"spec\": {\"command\": \"python3 code/exp_006_v2_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_{001_seed42,001_seed123,002_conll,008_re}_v2/\", \"data_count\": 4952, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"output/exp_006_v2/exp_006_v2_results.json\", \"log_path\": \"output/exp_006_v2_run.log\", \"completed_at\": \"2026-05-14T15:30:32.474Z\", \"metrics\": {\"NER_SciERC_s42\": {\"greedy\": 0.618, \"oracle\": 0.787, \"SJ\": 0.62, \"logprob\": 0.621, \"FK\": 0.621, \"EM\": 0.606, \"voting_conf\": 0.585, \"random\": 0.586}, \"NER_SciERC_s123\": {\"greedy\": 0.618, \"oracle\": 0.785, \"SJ\": 0.617, \"logprob\": 0.618, \"FK\": 0.621, \"EM\": 0.613, \"voting_conf\": 0.584, \"random\": 0.583}, \"NER_CoNLL\": {\"greedy\": 0.725, \"oracle\": 0.757, \"SJ\": 0.718, \"logprob\": 0.716, \"FK\": 0.717, \"EM\": 0.716, \"voting_conf\": 0.714, \"random\": 0.692}, \"RE_SciERC\": {\"greedy\": 0.403, \"oracle\": 0.631, \"SJ\": 0.397, \"logprob\": 0.41, \"FK\": 0.396, \"EM\": 0.381, \"voting_conf\": 0.408, \"random\": 0.364}}}, \"exp_005_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:28:14.924Z\", \"updated_at\": \"2026-05-14T15:28:35.949Z\", \"spec\": {\"description\": \"Temperature sensitivity analysis: T=0.7 vs T=1.0 across 5 signals (SJ, FK, logprob, EM, voting_conf)\", \"command\": \"python code/analyze_exp005_v2_temperature.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/mvp_pilot_004 + output/mvp_pilot_005 + output/exp_012_logprob\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-LoRA\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_005_v2_temperature/temperature_sensitivity_report.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:28:35.949Z\"}, \"exp_008_re_n16_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:06.296Z\", \"updated_at\": \"2026-05-14T15:23:59.395Z\", \"spec\": {\"description\": \"RE N=16 on SciERC full set confirmation, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency correlates with per-instance RE F1 on SciERC full dataset\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_008_re_n16_v2\", \"gpu\": [\"cuda:3\"], \"pid\": \"78737\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_008_re_n16_v2/run.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"sj_rho_full\": 0.281, \"sj_rho_cond\": 0.308, \"f1_zero_pct\": 44.3, \"conclusion_note\": \"RE N=16 v2 negative: SJ weak, 44.3% F1=0\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:35.598Z\", \"log_path\": \"output/exp_008_re_n16_v2/\"}, \"exp_001_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:04.210Z\", \"updated_at\": \"2026-05-14T15:23:56.155Z\", \"spec\": {\"description\": \"NER N=16 on SciERC, seed=123, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency (Fleiss kappa, Soft Jaccard) correlates with per-instance NER F1 on SciERC (seed robustness check)\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 123, \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed123_v2\", \"gpu\": [\"cuda:2\"], \"pid\": \"78733\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_001_seed123_v2/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.424, \"sj_rho_cond\": 0.376, \"structural_minus_surface\": 0.149, \"conclusion_note\": \"NER seed123 robustness confirmed, structural>surface +0.149\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:35.076Z\", \"log_path\": \"output/exp_001_seed123_v2/\"}, \"exp_001_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:02.350Z\", \"updated_at\": \"2026-05-14T15:23:52.846Z\", \"spec\": {\"description\": \"NER N=16 on SciERC, seed=42, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency (Fleiss kappa, Soft Jaccard) correlates with per-instance NER F1 on SciERC\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed42_v2\", \"gpu\": [\"cuda:1\"], \"pid\": \"78728\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_001_seed42_v2/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.428, \"sj_rho_cond\": 0.369, \"structural_minus_surface\": 0.147, \"conclusion_note\": \"NER seed42 robustness confirmed, structural>surface +0.147\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:34.091Z\", \"log_path\": \"output/exp_001_seed42_v2/\"}, \"exp_008_re_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:51.386Z\", \"updated_at\": \"2026-05-14T15:21:39.591Z\", \"spec\": {\"description\": \"RE N=16 on SciERC, seed=123, seed robustness test for relation extraction\", \"hypothesis\": \"Structural consistency correlates with per-instance RE F1, robust across seeds\", \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_008_re_seed123\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": [\"cuda:3\"], \"backend\": \"tmux\", \"tmux_session\": \"exp008_rs123\", \"account\": \"root\", \"log_path\": \"output/exp_008_re_seed123/run.log\"}, \"log_path\": \"output/exp_008_re_seed123/run.log\", \"conclusion\": \"negative\", \"metrics\": {\"greedy_f1\": 0.4229, \"oracle_f1\": 0.6244, \"oracle_headroom\": 0.2015, \"fleiss_kappa_mean\": 0.3455, \"soft_jaccard_mean\": 0.6126, \"sample_f1_mean\": 0.3594, \"sample_f1_std\": 0.3793, \"sample_f1_zero_pct\": 44.1, \"structural_gt_surface\": false, \"rho_kappa_f1_full\": 0.3174, \"rho_sj_f1_full\": 0.2835, \"rho_kappa_f1_cond\": 0.0766, \"rho_sj_f1_cond\": 0.2877, \"logprob_auroc_full\": 0.6499, \"logprob_auroc_cond\": 0.5265, \"verdict\": \"FAIL\"}, \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-14T15:21:39.591Z\"}, \"exp_007_llama_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:50.157Z\", \"updated_at\": \"2026-05-14T15:19:47.267Z\", \"spec\": {\"description\": \"LLaMA 3.1-8B SciERC joint extraction, seed=123, cross-model robustness test\", \"hypothesis\": \"Structural consistency generalizes across model architectures (LLaMA vs Qwen)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_seed123\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 123, \"gpu\": [\"cuda:1\"], \"backend\": \"tmux\", \"tmux_session\": \"exp007_s123\", \"account\": \"root\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T15:19:43.424Z\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6605, \"oracle_f1\": 0.7703, \"headroom\": 0.1098, \"fleiss_kappa\": 0.4553, \"soft_jaccard\": 0.7525, \"rho_kappa_f1\": 0.2143, \"rho_sj_f1\": 0.3371, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.433, \"oracle_f1\": 0.5719, \"headroom\": 0.1389, \"fleiss_kappa\": 0.3851, \"soft_jaccard\": 0.6911, \"rho_kappa_f1\": 0.2844, \"rho_sj_f1\": 0.268, \"structural_gt_surface\": false}, \"fail_reasons\": [\"RE rho_sj=0.2680 < 0.40 threshold\", \">30% samples F1=0 (RE: 41.0%)\", \"RE structural not > surface (delta=-0.0165)\"]}}, \"exp_007_llama_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:50.628Z\", \"updated_at\": \"2026-05-14T15:19:27.040Z\", \"spec\": {\"description\": \"LLaMA 3.1-8B SciERC joint extraction, seed=456, cross-model robustness test\", \"hypothesis\": \"Structural consistency generalizes across model architectures (LLaMA vs Qwen)\", \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_seed456\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 456, \"gpu\": [\"cuda:2\"], \"backend\": \"tmux\", \"tmux_session\": \"exp007_s456\", \"account\": \"root\", \"log_path\": \"output/exp_007_llama_seed456/run.log\"}, \"conclusion\": \"negative\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456/\", \"completed_at\": \"2026-05-14T15:19:20.693Z\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6597, \"oracle_f1\": 0.7575, \"oracle_headroom\": 0.0978, \"fleiss_kappa\": 0.4543, \"soft_jaccard\": 0.7491, \"rho_kappa_f1\": 0.3115, \"rho_sj_f1\": 0.3663, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.4334, \"oracle_f1\": 0.5789, \"oracle_headroom\": 0.1455, \"fleiss_kappa\": 0.3791, \"soft_jaccard\": 0.6782, \"rho_kappa_f1\": 0.3013, \"rho_sj_f1\": 0.287, \"structural_gt_surface\": false}, \"logprob_ner\": {\"rho\": 0.1911, \"auroc\": 0.5989}, \"logprob_re\": {\"rho\": 0.3246, \"auroc\": 0.6678}, \"fail_reason\": \"RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0\"}}, \"exp_015_metrics_expansion\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:47:36.569Z\", \"updated_at\": \"2026-05-14T15:16:34.851Z\", \"spec\": {\"hypothesis\": \"Comprehensive evaluation of all 5 confidence signals with extended metrics\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"exp_012_logprob_baseline\", \"method\": \"CPU-only analysis: 6 metrics x 5 signals x 2 subtasks (NER+RE)\", \"command\": \"python code/analyze_exp015_metrics_expansion.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp015_metrics_expansion\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:22:32.661Z\", \"metrics\": {\"data_source\": \"exp_012_logprob/samples_with_logprobs.jsonl\", \"config\": \"N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\", \"ner\": {\"n_valid\": 529, \"n_cond\": 501, \"voting_rho_full\": 0.5018, \"voting_rho_cond\": 0.4497, \"voting_auroc\": 0.7279, \"voting_tau\": 0.3766, \"sj_rho_full\": 0.3565, \"sj_rho_cond\": 0.412, \"sj_auroc\": 0.6656, \"sj_tau\": 0.2658, \"em_rho_full\": 0.2566, \"em_rho_cond\": 0.3427, \"em_auroc\": 0.623, \"em_tau\": 0.1924, \"fk_rho_full\": 0.2651, \"fk_rho_cond\": 0.306, \"fk_auroc\": 0.6243, \"fk_tau\": 0.2027, \"logprob_rho_full\": 0.1396, \"logprob_rho_cond\": 0.1627, \"logprob_auroc\": 0.5585, \"logprob_tau\": 0.1006}, \"re\": {\"n_valid\": 397, \"n_cond\": 296, \"voting_rho_full\": 0.4217, \"voting_rho_cond\": 0.463, \"voting_auroc\": 0.7162, \"voting_tau\": 0.327, \"sj_rho_full\": 0.2112, \"sj_rho_cond\": 0.3683, \"sj_auroc\": 0.5816, \"sj_tau\": 0.1619, \"em_rho_full\": 0.1002, \"em_rho_cond\": 0.3607, \"em_auroc\": 0.5036, \"em_tau\": 0.0839, \"fk_rho_full\": 0.2528, \"fk_rho_cond\": 0.3168, \"fk_auroc\": 0.6308, \"fk_tau\": 0.1967, \"logprob_rho_full\": 0.2467, \"logprob_rho_cond\": 0.1457, \"logprob_auroc\": 0.6354, \"logprob_tau\": 0.1808}, \"diagnosis\": \"Unified 5-signal evaluation on single data source. Voting leads NER full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond.\"}}, \"exp_010_selection_curves\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:01:53.585Z\", \"updated_at\": \"2026-05-14T15:02:34.760Z\", \"spec\": {\"command\": \"python3 code/exp010_selection_curves.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2, output/exp_008_re_n16_v2, output/exp002_conll2003\", \"data_count\": \"551+397+3453 instances\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"description\": \"Best-of-N selection curves: F1 vs N for 7 signals across 3 datasets\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp010.log\", \"completed_at\": \"2026-05-14T15:02:22.638Z\", \"metrics\": {\"scierc_ner\": {\"n_instances\": 551, \"greedy_f1\": 0.618, \"N16\": {\"oracle\": 0.787, \"SJ\": 0.62, \"FK\": 0.621, \"logprob\": 0.621, \"voting_conf\": 0.585, \"EM\": 0.606, \"random\": 0.595}, \"N8\": {\"oracle\": 0.752, \"SJ\": 0.614, \"FK\": 0.614, \"logprob\": 0.619, \"voting_conf\": 0.591, \"EM\": 0.603, \"random\": 0.589}, \"N4\": {\"oracle\": 0.714, \"SJ\": 0.607, \"FK\": 0.608, \"logprob\": 0.616, \"voting_conf\": 0.594, \"EM\": 0.6, \"random\": 0.587}}, \"scierc_re\": {\"n_instances\": 397, \"greedy_f1\": 0.403, \"N16\": {\"oracle\": 0.631, \"SJ\": 0.397, \"FK\": 0.396, \"logprob\": 0.41, \"voting_conf\": 0.408, \"EM\": 0.381, \"random\": 0.364}, \"N8\": {\"oracle\": 0.583, \"SJ\": 0.393, \"FK\": 0.394, \"logprob\": 0.413, \"voting_conf\": 0.398, \"EM\": 0.381, \"random\": 0.363}}, \"conll_ner\": {\"n_instances\": 3453, \"greedy_f1\": 0.725, \"N8\": {\"oracle\": 0.757, \"SJ\": 0.718, \"FK\": 0.717, \"logprob\": 0.716, \"voting_conf\": 0.714, \"EM\": 0.716, \"random\": 0.69}, \"N4\": {\"oracle\": 0.746, \"SJ\": 0.714, \"FK\": 0.714, \"logprob\": 0.715, \"voting_conf\": 0.714, \"EM\": 0.712, \"random\": 0.692}}}}, \"exp_009_capability_stratification\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:59:24.201Z\", \"updated_at\": \"2026-05-14T14:59:53.951Z\", \"spec\": {\"command\": \"python code/exp009_stratification_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp001_n16_seed42 + output/exp008_re_n16 + output/exp002_conll2003\", \"data_count\": 4555, \"model_name\": \"analysis_only\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp009_stratification_results.json\", \"log_path\": \"/tmp/exp009.log\", \"completed_at\": \"2026-05-14T14:59:46.463Z\", \"metrics\": {\"scierc_ner\": {\"n\": 551, \"sj_rho_overall\": 0.398, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": 0.159, \"med_low_sj_rho\": 0.139, \"med_high_sj_rho\": 0.09, \"easy_sj_rho\": 0.23}, \"by_sent_len\": {\"Q1_sj_rho\": 0.461, \"Q2_sj_rho\": 0.401, \"Q3_sj_rho\": 0.296, \"Q4_sj_rho\": 0.382}, \"by_ent_count\": {\"0_sj_rho\": 0.689, \"1_2_sj_rho\": 0.415, \"3_5_sj_rho\": 0.353, \"6plus_sj_rho\": 0.547}}, \"scierc_re\": {\"n\": 551, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": -0.043, \"easy_sj_rho\": 0.21}, \"by_sent_len\": {\"Q1_sj_rho\": 0.447, \"Q4_sj_rho\": 0.54}, \"by_rel_count\": {\"0_sj_rho\": 0.62, \"1_2_sj_rho\": 0.275, \"6plus_sj_rho\": 0.527}}, \"conll_ner\": {\"n\": 3453, \"by_sent_len\": {\"Q1_sj_rho\": 0.334, \"Q3_sj_rho\": 0.518}}, \"proxy_independence\": {\"scierc_ner_f1_vs_slen\": -0.021, \"scierc_ner_f1_vs_ecnt\": 0.007, \"scierc_re_f1_vs_slen\": -0.147}}}, \"exp_003_wnut17_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:47:34.654Z\", \"updated_at\": \"2026-05-14T14:28:43.864Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_eval --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/wnut17\", \"data_count\": 1287, \"model_name\": \"qwen3-8b-wnut17-merged\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:08:17.429Z\", \"metrics\": {\"greedy_f1\": 0.523, \"oracle_f1\": 0.664, \"headroom\": 0.141, \"rho_fk\": 0.125, \"rho_sj\": 0.089, \"rho_fk_cond\": 0.169, \"rho_sj_cond\": 0.288, \"rho_logprob_full\": -0.409, \"rho_logprob_cond\": 0.35, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 53.7, \"n_instances\": 1287, \"N\": 16, \"T\": 1, \"seed\": 42, \"model\": \"Qwen3-8B\", \"n_gold_empty_filtered\": 598, \"verdict\": \"FAIL\", \"verdict_note\": \"structural_beats_surface=false; >50% samples F1=0\"}}, \"exp_007_llama_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:54:48.055Z\", \"updated_at\": \"2026-05-14T14:28:32.909Z\", \"spec\": {\"command\": \"python run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp007_llama_inference/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"75172\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_llama_inference.log\", \"submitted_at\": \"2026-05-14T13:54:47.962Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-8B-Instruct (LoRA fine-tuned on SciERC)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"description\": \"LLaMA-3.1-8B SciERC joint inference (NER+RE) with 8 samples, T=1.0, logprobs collected.\", \"wall_clock_seconds\": 1038.5, \"gpu_hours\": 0.29}, \"log_path\": \"output/exp007_llama_inference/\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.66, \"oracle_f1\": 0.781, \"headroom\": 0.121, \"rho_fk\": 0.327, \"rho_sj\": 0.363, \"rho_fk_cond\": 0.226, \"rho_sj_cond\": 0.311, \"rho_logprob\": 0.183, \"rho_logprob_cond\": 0.109, \"structural_beats_surface\": true, \"sample_f1_pct_zero\": 11.6}, \"re\": {\"greedy_f1\": 0.434, \"oracle_f1\": 0.568, \"headroom\": 0.135, \"rho_fk\": 0.305, \"rho_sj\": 0.299, \"rho_fk_cond\": 0.259, \"rho_sj_cond\": 0.405, \"rho_logprob\": 0.288, \"rho_logprob_cond\": 0.092, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 41.2}, \"n_instances\": 551, \"N\": 8, \"T\": 1, \"seed\": 42, \"model\": \"LLaMA-3.1-8B-Instruct\", \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:12:06.442Z\"}, \"exp_008_re_n16_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:42.867Z\", \"updated_at\": \"2026-05-14T14:05:49.091Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:18.988Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:19.577Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:21.528032+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.444}, \"re\": {\"rho_sj\": 0.248}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 42, \"mode\": \"RE-only\", \"source\": \"director_corrected\"}}, \"exp_001_seed123_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:42.503Z\", \"updated_at\": \"2026-05-14T14:05:38.817Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:13.823Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:13.213Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:16.532801+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.417, \"rho_fk\": 0.283}, \"re\": {\"rho_sj\": 0.265, \"rho_fk\": 0.315}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 123, \"source\": \"reviewer_verified_report_json\"}}, \"exp_001_seed456_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:41.067Z\", \"updated_at\": \"2026-05-14T14:05:37.904Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:05.416Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:05.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:10.317185+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.414, \"rho_fk\": 0.298}, \"re\": {\"rho_sj\": 0.268, \"rho_fk\": 0.26}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 456, \"source\": \"reviewer_verified_report_json\"}}, \"exp_003_ner_wnut17\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:17.544Z\", \"updated_at\": \"2026-05-14T13:40:20.979Z\", \"spec\": {\"merged_model_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged\", \"pilot_command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_pilot --num_test 9999 --collect_logprobs\", \"pilot_pid\": 71498, \"pilot_server\": \"autodl-5090\", \"pilot_started_at\": \"2026-05-14T21:36:00Z\", \"test_samples\": 1287}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T11:43:50.537Z\", \"finished_at\": \"2026-05-14T12:53:13.262Z\", \"training_hours\": 1.16}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:53:14.768981+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.525, \"oracle_f1\": 0.664, \"headroom\": 0.139, \"rho_sj_full\": 0.082, \"rho_fk_full\": 0.124, \"rho_logprob_full\": -0.414, \"rho_sj_cond\": 0.275, \"rho_fk_cond\": 0.164, \"rho_logprob_cond\": 0.352, \"sj_beats_logprob_cond\": false}, \"n_instances\": 1287, \"n_gold_empty\": 598, \"sample_f1_mean\": 0.401, \"sample_f1_pct_zero\": 53.7, \"N\": 16, \"T\": 1, \"seed\": 42, \"verdict\": \"FAIL\", \"verdict_note\": \">30% samples F1=0; structural rho weak; logprob baseline stronger\"}, \"conclusion\": \"negative\", \"log_path\": \"output/exp003_wnut17_pilot/\", \"completed_at\": \"2026-05-14T13:40:20.979Z\"}, \"exp_007_ner_multi_model\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:20.748Z\", \"updated_at\": \"2026-05-14T13:35:43.251Z\", \"spec\": {\"command\": \"bash -c 'source env.sh && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_llama.yaml'\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"60970\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"submitted_at\": \"2026-05-14T12:43:09.108Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data\", \"data_count\": 1861, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"log_file\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"wall_clock_seconds\": 165.8, \"gpu_hours\": 0.05}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T11:43:50.977Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:45:54.952Z\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-lora\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0767, \"eval_loss\": 0.1049, \"train_runtime_sec\": 1494.5, \"train_samples_per_second\": 6.226, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"base_model\": \"Meta-Llama-3.1-8B-Instruct\", \"lora_r\": 32, \"lora_alpha\": 64, \"note\": \"EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal. Checkpoint fully intact.\"}, \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\"}, \"exp_001_ner_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:46:06.430Z\", \"updated_at\": \"2026-05-14T13:33:40.719Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --output_dir output/exp001_n16_seed123 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed123_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"63407\", \"log_path\": \"output/exp001_n16_seed123_run.log\", \"submitted_at\": \"2026-05-14T12:46:06.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 551, \"data_path\": \"data/scierc/processed_data\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"checkpoint_path\": \"output/exp001_n16_seed123/\", \"wall_clock_seconds\": 2748.0, \"gpu_hours\": 0.76}, \"conclusion\": \"success\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.663, \"oracle_f1\": 0.809, \"headroom\": 0.146, \"rho_sj\": 0.423, \"rho_fk\": 0.29, \"rho_logprob\": 0.239, \"rho_sj_cond\": 0.423, \"rho_fk_cond\": 0.26}, \"re\": {\"greedy_f1\": 0.419, \"oracle_f1\": 0.625, \"headroom\": 0.206, \"rho_sj\": 0.267, \"rho_fk\": 0.315, \"rho_sj_cond\": 0.364, \"rho_fk_cond\": 0.331}, \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj=0.267 < 0.40; RE >30% samples F1=0\", \"n_instances\": 551, \"seed\": 123, \"N\": 16, \"T\": 1}, \"completed_at\": \"2026-05-14T13:31:54.232Z\"}, \"exp_008_re_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:03:06.876Z\", \"updated_at\": \"2026-05-14T12:43:01.073Z\", \"spec\": {\"hypothesis\": \"RE N=16 confirms negative finding with higher statistical power. If rho still <0.30, task-complexity boundary is robust.\", \"plan_id\": \"exp-008\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"gpu\": \"cuda:2\", \"server\": \"gpu-5090-4x-2\", \"gpu_budget_hours\": 12, \"description\": \"RE N=16 on SciERC to confirm negative finding. Inference with log-prob capture.\", \"priority\": \"P1\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"seed\": 42, \"num_instances\": 200, \"partial\": true, \"note\": \"Only 200/551 instances due to --num_test default bug. Needs full rerun.\"}, \"metrics\": {\"ner\": {\"greedy_f1\": 0.6635, \"oracle_f1\": 0.8208, \"headroom\": 0.1572, \"rho_sj_full\": 0.377, \"rho_fk_full\": 0.2508, \"rho_logprob_full\": 0.3153, \"rho_sj_cond\": 0.3598, \"rho_fk_cond\": 0.2251, \"rho_logprob_cond\": 0.2927, \"sj_beats_fk\": true, \"rho_advantage\": 0.1262}, \"re\": {\"greedy_f1\": 0.4339, \"oracle_f1\": 0.6658, \"headroom\": 0.2319, \"rho_sj_full\": 0.2966, \"rho_fk_full\": 0.2871, \"rho_logprob_full\": 0.2986, \"rho_sj_cond\": 0.3975, \"rho_fk_cond\": 0.3774, \"rho_logprob_cond\": 0.2745, \"sj_beats_fk\": true, \"rho_advantage\": 0.0095}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp008_re_n16/\", \"completed_at\": \"2026-05-14T12:28:39.268Z\"}, \"exp_001_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:10:29.393Z\", \"updated_at\": \"2026-05-14T12:42:58.393Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs\", \"server\": \"gpu-5090-4x-2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"num_instances\": 200, \"partial\": true, \"note\": \"Only 200/551 instances due to --num_test default bug. Needs full rerun.\"}, \"metrics\": {\"ner\": {\"greedy_f1\": 0.655, \"oracle_f1\": 0.8028, \"headroom\": 0.1478, \"rho_sj_full\": 0.4076, \"rho_fk_full\": 0.2799, \"rho_logprob_full\": 0.3189, \"rho_sj_cond\": 0.4271, \"rho_fk_cond\": 0.2743, \"rho_logprob_cond\": 0.2835, \"sj_beats_fk\": true, \"rho_advantage\": 0.1277}, \"re\": {\"greedy_f1\": 0.4243, \"oracle_f1\": 0.6771, \"headroom\": 0.2528, \"rho_sj_full\": 0.2943, \"rho_fk_full\": 0.2657, \"rho_logprob_full\": 0.3005, \"rho_sj_cond\": 0.4003, \"rho_fk_cond\": 0.313, \"rho_logprob_cond\": 0.2317, \"sj_beats_fk\": true, \"rho_advantage\": 0.0286}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp001_n16_seed123/\", \"completed_at\": \"2026-05-14T12:28:38.104Z\"}, \"exp_016_signal_ensemble\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:15:23.771Z\", \"updated_at\": \"2026-05-14T12:42:55.931Z\", \"spec\": {\"command\": \"python code/analyze_exp016_ensemble.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"model_name\": \"N/A (CPU-only analysis)\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"pilot_004\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp016_signal_ensemble/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:15:53.341Z\", \"metrics\": {\"sj_logprob_pearson_ner\": 0.57, \"sj_logprob_pearson_re\": 0.42, \"best_linear_ner\": {\"combo\": \"SJ+voting_conf\", \"alpha\": 0.3, \"rho\": 0.489}, \"best_linear_re\": {\"combo\": \"voting_conf+logprob\", \"alpha\": 0.6, \"rho\": 0.429}, \"ensemble_ner_auroc\": 0.735, \"ensemble_re_auroc\": 0.719, \"best_single_ner_auroc\": 0.7, \"best_single_re_auroc\": 0.721, \"ensemble_ner_delta\": 0.035, \"selection_f1_ner\": {\"greedy\": 0.609, \"logprob\": 0.609, \"sj\": 0.604, \"ensemble\": 0.604, \"voting\": 0.596, \"random\": 0.58, \"oracle\": 0.769}, \"selection_f1_re\": {\"logprob\": 0.397, \"greedy\": 0.374, \"sj\": 0.368, \"ensemble\": 0.367, \"voting\": 0.338, \"random\": 0.338, \"oracle\": 0.561}, \"diagnosis\": \"SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge.\"}}, \"exp_001_ner_n16_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:10.898Z\", \"updated_at\": \"2026-05-14T12:42:49.592Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp001_n16_seed42 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed42_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"54357\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_ner_n16_scierc.log\", \"submitted_at\": \"2026-05-14T12:15:46.646Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T11:43:48.643Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:55:45.664Z\", \"metrics\": {\"n_instances\": 551, \"ner_n\": 529, \"re_n\": 397, \"N\": 16, \"T\": 1, \"seed\": 42, \"full_test_set\": true, \"ner_voting_conf_rho\": 0.399, \"ner_sj_rho\": 0.398, \"ner_em_rho\": 0.339, \"ner_fk_rho\": 0.288, \"ner_logprob_rho\": 0.237, \"ner_voting_conf_auroc\": 0.704, \"ner_sj_auroc\": 0.697, \"ner_cond_em_rho\": 0.414, \"ner_cond_sj_rho\": 0.349, \"ner_cond_vc_rho\": 0.34, \"re_voting_conf_rho\": 0.38, \"re_logprob_rho\": 0.293, \"re_fk_rho\": 0.281, \"re_sj_rho\": 0.277, \"re_em_rho\": 0.148, \"re_voting_conf_auroc\": 0.699, \"re_cond_em_rho\": 0.475, \"re_cond_sj_rho\": 0.318, \"re_cond_vc_rho\": 0.35, \"re_cond_em_auroc\": 0.742, \"diagnosis\": \"551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40). Previous N-scaling 'breakthrough' was artifact of 200 instances + T=0.7.\"}}, \"exp_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:39:53.226Z\", \"updated_at\": \"2026-05-14T12:40:17.202Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --collect_logprobs --num_test 99999\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-lora-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged\", \"log_path\": \"/tmp/pilot_conll2003.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:40:08.402Z\", \"metrics\": {\"sj_rho_full\": 0.4357, \"sj_tau_full\": 0.3851, \"sj_auroc_full\": 0.8008, \"sj_rho_cond\": 0.4511, \"fk_rho_full\": 0.3998, \"fk_tau_full\": 0.3568, \"fk_auroc_full\": 0.7741, \"fk_rho_cond\": 0.4064, \"logprob_rho_full\": 0.3157, \"logprob_tau_full\": 0.2469, \"logprob_auroc_full\": 0.7532, \"logprob_rho_cond\": 0.3562, \"em_rho_full\": 0.4507, \"em_tau_full\": 0.4002, \"em_auroc_full\": 0.8156, \"em_rho_cond\": 0.4799, \"ev_rho_full\": 0.4237, \"ev_tau_full\": 0.3777, \"ev_auroc_full\": 0.7889, \"ev_rho_cond\": 0.4127, \"greedy_f1\": 0.9123, \"oracle_f1\": 0.9543, \"voting_f1\": 0.9141, \"oracle_headroom\": 0.042, \"sj_vs_logprob_delta_rho\": 0.12, \"sj_vs_logprob_ci_low\": 0.0881, \"sj_vs_logprob_ci_high\": 0.154, \"sj_vs_logprob_significant\": true, \"n_instances\": 3453, \"n_valid\": 2756, \"n_samples\": 8, \"temperature\": 1}}, \"exp_002_ner_conll2003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:15.223Z\", \"updated_at\": \"2026-05-14T12:27:35.413Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp002_conll2003 --num_test 99999 --seed 42 --collect_logprobs 2>&1 | tee /tmp/pilot_conll2003.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"58208\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log\", \"submitted_at\": \"2026-05-14T12:27:35.337Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T11:43:49.959Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-lora\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log\", \"completed_at\": \"2026-05-14T12:18:04.097Z\"}, \"exp_004_re_diagnostic\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:49:44.497Z\", \"updated_at\": \"2026-05-14T11:50:24.620Z\", \"spec\": {\"hypothesis\": \"RE diagnostic: per-relation-type breakdown reveals which types drive low RE rho; error propagation and threshold sensitivity clarify the gap between NER and RE consistency signals\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Per-relation-type SJ/FK/voting rho, error propagation classification, threshold sensitivity, bootstrap CI, Fisher z-test NER vs RE\", \"command\": \"python3 code/analyze_exp004_re_diagnostic.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004_re_diagnostic\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004_re_diagnostic/\", \"checkpoint_source\": \"mvp_pilot_004\", \"eval_data\": \"scierc_test_551\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:50:04.662Z\", \"metrics\": {\"per_relation_type\": {\"HYPONYM-OF\": {\"n\": 36, \"rho_sj\": 0.545, \"rho_fk\": 0.646, \"rho_vc\": 0.628, \"mean_f1\": 0.513}, \"CONJUNCTION\": {\"n\": 86, \"rho_sj\": 0.383, \"rho_fk\": 0.35, \"rho_vc\": 0.484, \"mean_f1\": 0.48}, \"USED-FOR\": {\"n\": 299, \"rho_sj\": 0.236, \"rho_fk\": 0.255, \"rho_vc\": 0.286, \"mean_f1\": 0.422}, \"PART-OF\": {\"n\": 44, \"rho_sj\": 0.239, \"rho_fk\": 0.348, \"rho_vc\": 0.283, \"mean_f1\": 0.297}, \"EVALUATE-FOR\": {\"n\": 62, \"rho_sj\": 0.172, \"rho_fk\": 0.255, \"rho_vc\": 0.226, \"mean_f1\": 0.365}, \"COMPARE\": {\"n\": 35, \"rho_sj\": 0.168, \"rho_fk\": 0.184, \"rho_vc\": 0.18, \"mean_f1\": 0.453}, \"FEATURE-OF\": {\"n\": 50, \"rho_sj\": 0.004, \"rho_fk\": 0.052, \"rho_vc\": 0.014, \"mean_f1\": 0.254}}, \"error_propagation\": {\"total_fn\": 553, \"tail_error_pct\": 21.9, \"full_error_pct\": 21.7, \"head_error_pct\": 17.7, \"head_tail_error_pct\": 15.9, \"type_error_pct\": 8.3, \"worst_consistency\": \"head_type_error (sj=0.411)\", \"best_consistency\": \"head_error (sj=0.613)\"}, \"threshold_sensitivity\": {\"thr_0.00_rho_sj\": 0.3161, \"thr_0.00_rho_vc\": 0.3841, \"thr_0.00_n\": 313, \"thr_0.05_rho_sj\": 0.2682, \"thr_0.05_rho_vc\": 0.2364, \"thr_0.05_n\": 239}, \"bootstrap_ci_95\": {\"ner_sj\": [0.2946, 0.4586], \"ner_voting_conf\": [0.3048, 0.4656], \"re_sj\": [0.1422, 0.3391], \"re_voting_conf\": [0.1818, 0.3721], \"re_cond_sj\": [0.2161, 0.4102], \"re_cond_voting_conf\": [0.2825, 0.474]}, \"fisher_z_ner_vs_re\": {\"sj_z\": 2.31, \"sj_p\": 0.0209, \"sj_significant\": true, \"fk_z\": -0.31, \"fk_p\": 0.756, \"fk_significant\": false, \"voting_z\": 1.914, \"voting_p\": 0.0556, \"voting_significant\": false}, \"diagnosis\": \"FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE signal in conditional set (rho=0.384).\"}}, \"exp_005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:45:16.360Z\", \"updated_at\": \"2026-05-14T11:45:38.570Z\", \"spec\": {\"hypothesis\": \"Temperature sensitivity: systematic comparison of T=0.7 vs T=1.0 on all 5 confidence signals\", \"method\": \"CPU-only analysis from checkpoint metrics (pilot_004 T=1.0, pilot_005 T=0.7, exp_012/013/014)\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2\", \"data_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/\", \"server\": \"local\", \"seed\": 42, \"parent\": \"mvp_pilot_004,mvp_pilot_005\", \"command\": \"python3 analyze_exp005_temperature.py\", \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/\", \"log_path\": \"N/A\", \"checkpoint_source\": \"pilot_004+pilot_005 checkpoint metrics\", \"eval_data\": \"SciERC test set (n=551)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:45:38.570Z\"}, \"exp_014_entity_majority_voting\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:21.203Z\", \"updated_at\": \"2026-05-14T11:33:30.085Z\", \"spec\": {\"hypothesis\": \"Entity-level majority voting confidence beats SJ as correlation signal\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Per-entity voting across N=8 samples, consensus construction, confidence = mean voting rate\", \"command\": \"python code/analyze_entity_voting.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp014_entity_voting_report.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:18:09.468Z\", \"metrics\": {\"ner_full_rho\": 0.3915, \"ner_full_p\": 8.1e-21, \"ner_full_tau\": 0.2906, \"ner_full_auroc\": 0.7039, \"re_full_rho\": 0.3403, \"re_full_p\": 3.21e-12, \"re_full_tau\": 0.256, \"re_full_auroc\": 0.6668, \"ner_voting_f1\": 0.6246, \"ner_greedy_f1\": 0.6483, \"ner_oracle_f1\": 0.7793, \"re_voting_f1\": 0.3577, \"re_greedy_f1\": 0.4022, \"re_oracle_f1\": 0.5886, \"diagnosis\": \"Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\"}}, \"exp_013_exact_match_voting\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:18.753Z\", \"updated_at\": \"2026-05-14T11:33:22.644Z\", \"spec\": {\"hypothesis\": \"Exact-match voting rate correlates with F1\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Count exact-match duplicates across N=8 samples\", \"command\": \"python code/analyze_exact_match_voting.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp013_exact_match_report.json\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T11:18:09.026Z\", \"metrics\": {\"ner_full_rho\": 0.2941, \"ner_full_p\": 5.12e-12, \"ner_full_tau\": 0.2181, \"ner_full_auroc\": 0.6398, \"re_full_rho\": 0.1562, \"re_full_p\": 0.0018, \"re_full_tau\": 0.1185, \"re_full_auroc\": 0.5863, \"diagnosis\": \"EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\"}}, \"exp_012_logprob_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:16.166Z\", \"updated_at\": \"2026-05-14T11:13:30.240Z\", \"spec\": {\"hypothesis\": \"Log-probability baseline: mean sequence log-prob correlates with F1 as well as or better than SJ\", \"model_name\": \"ft_002_v2 (qwen3-8b-scierc-merged-v2)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"vLLM forward pass for log-probs + Spearman rho + AUROC + Kendall tau\", \"command\": \"python3 code/extract_logprobs.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/logprob_analysis.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:06:42.542Z\", \"metrics\": {\"ner_full_rho_sj\": 0.3565, \"ner_full_rho_fk\": 0.2651, \"ner_full_rho_logprob\": 0.1396, \"ner_full_rho_greedy_logprob\": 0.1615, \"ner_full_tau_sj\": 0.2658, \"ner_full_tau_logprob\": 0.1006, \"ner_full_auroc_sj\": 0.6892, \"ner_full_auroc_fk\": 0.6292, \"ner_full_auroc_logprob\": 0.5907, \"ner_full_n\": 529, \"ner_sj_vs_logprob_delta\": 0.2169, \"re_full_rho_sj\": 0.2112, \"re_full_rho_fk\": 0.2528, \"re_full_rho_logprob\": 0.2467, \"re_full_auroc_sj\": 0.5916, \"re_full_auroc_fk\": 0.6262, \"re_full_auroc_logprob\": 0.6186, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3683, \"re_cond_rho_fk\": 0.3168, \"re_cond_rho_logprob\": 0.1457, \"re_cond_auroc_sj\": 0.6839, \"re_cond_auroc_logprob\": 0.5487, \"re_cond_n\": 296, \"diagnosis\": \"NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead. RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.\"}}, \"mvp_pilot_005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:14:09.456Z\", \"updated_at\": \"2026-05-14T09:47:06.597Z\", \"spec\": {\"hypothesis\": \"T=0.7 降低 RE zero rate，恢复 SJ>FK，rho_sj 可能 ≥ 0.30 (MARGINAL threshold)\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=0.7 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.7 --max_tokens 1024 --output_dir output/mvp_pilot_005 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 32456, \"tmux_session\": \"mvp_pilot_005\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/train.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005\", \"metrics\": {\"ner_greedy_f1\": 0.6619, \"ner_oracle_f1\": 0.7585, \"ner_headroom\": 0.0966, \"ner_fleiss_kappa_mean\": 0.4722, \"ner_soft_jaccard_mean\": 0.7757, \"ner_full_rho_sj\": 0.3875, \"ner_full_rho_fk\": 0.3211, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3868, \"ner_cond_rho_fk\": 0.305, \"ner_cond_n\": 504, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0664, \"ner_sample_f1_mean\": 0.6243, \"ner_sample_f1_std\": 0.3131, \"ner_sample_f1_pct_zero\": 11.2, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 25, \"re_greedy_f1\": 0.4219, \"re_oracle_f1\": 0.5532, \"re_headroom\": 0.1313, \"re_fleiss_kappa_mean\": 0.3829, \"re_soft_jaccard_mean\": 0.687, \"re_full_rho_sj\": 0.2343, \"re_full_rho_fk\": 0.1835, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3716, \"re_cond_rho_fk\": 0.2533, \"re_cond_n\": 301, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0508, \"re_sample_f1_mean\": 0.3782, \"re_sample_f1_std\": 0.3845, \"re_sample_f1_pct_zero\": 42.4, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 96, \"parse_failures\": 0, \"verdict\": \"FAIL\", \"verdict_note\": \"RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional but not full threshold\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T09:47:06.597Z\"}, \"e1_component_wise_re_sj\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:15:17.262Z\", \"updated_at\": \"2026-05-14T09:23:38.818Z\", \"spec\": {\"hypothesis\": \"RE SJ 乘性惩罚是 root cause：分解后 head_sj ρ ≈ NER ρ (~0.38)，tail_sj 和乘性组合拖低整体 ρ\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 397, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Component-wise decomposition: head_sj, tail_sj, type_match 分别计算 Spearman ρ vs per-instance RE F1\", \"command\": \"python3 code/analyze_component_wise_re.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/e1_component_analysis.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"full_head_sj_rho\": 0.21, \"full_tail_sj_rho\": 0.201, \"full_type_match_rho\": 0.201, \"full_multiplicative_rho\": 0.244, \"full_additive_rho\": 0.243, \"full_fleiss_kappa_rho\": 0.278, \"cond_head_sj_rho\": 0.27, \"cond_tail_sj_rho\": 0.259, \"cond_type_match_rho\": 0.252, \"cond_multiplicative_rho\": 0.316, \"cond_additive_rho\": 0.306, \"cond_fleiss_kappa_rho\": 0.307, \"n_full\": 397, \"n_conditional\": 313, \"diagnosis\": \"head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for RE.\"}, \"completed_at\": \"2026-05-14T09:22:26.155Z\"}, \"mvp_pilot_004\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:51:38.203Z\", \"updated_at\": \"2026-05-14T09:10:40.918Z\", \"spec\": {\"hypothesis\": \"With improved RE quality (F1=41.8%), structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa, reaching rho_sj >= 0.40 on RE\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/mvp_pilot_004 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 31041, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/mvp_pilot_004.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\"}, \"metrics\": {\"ner_greedy_f1\": 0.6671, \"ner_oracle_f1\": 0.7756, \"ner_headroom\": 0.1085, \"ner_fleiss_kappa_mean\": 0.4048, \"ner_soft_jaccard_mean\": 0.7008, \"ner_full_rho_fk\": 0.259, \"ner_full_rho_sj\": 0.3825, \"ner_full_n\": 529, \"ner_cond_rho_fk\": 0.2352, \"ner_cond_rho_sj\": 0.3762, \"ner_cond_n\": 508, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_mean\": 0.6084, \"ner_sample_f1_std\": 0.3174, \"ner_sample_f1_pct_zero\": 12.19, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 21, \"re_greedy_f1\": 0.4208, \"re_oracle_f1\": 0.5882, \"re_headroom\": 0.1674, \"re_fleiss_kappa_mean\": 0.2996, \"re_soft_jaccard_mean\": 0.6114, \"re_full_rho_fk\": 0.2782, \"re_full_rho_sj\": 0.2441, \"re_full_n\": 397, \"re_cond_rho_fk\": 0.3067, \"re_cond_rho_sj\": 0.3161, \"re_cond_n\": 313, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_mean\": 0.3612, \"re_sample_f1_std\": 0.383, \"re_sample_f1_pct_zero\": 44.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 84, \"parse_failures\": 0, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T09:10:40.918Z\"}, \"ft_002_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:28:40.861Z\", \"updated_at\": \"2026-05-14T08:51:32.405Z\", \"spec\": {\"hypothesis\": \"Extended training (5 epochs, LoRA r=32) with OOM fix improves RE F1 above 40% threshold\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"LoRA r=32 alpha=64, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true\", \"gpu\": \"cuda:1\", \"pid\": 24947, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/ft_002v2_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2\", \"command\": \"CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_v2.yaml\"}, \"conclusion\": \"success\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0806, \"eval_loss\": 0.089, \"train_runtime\": \"28m41s\", \"train_samples_per_second\": 5.407, \"train_steps_per_second\": 0.34, \"total_steps\": 585, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"gate0_final_ner_f1\": 0.6615, \"gate0_final_re_f1\": 0.4177, \"gate0_final_parse_failures\": 0, \"gate0_final_ner_pass\": true, \"gate0_final_re_pass\": true, \"gate0_final_pass\": true, \"gate0_ckpt400_ner_f1\": 0.6475, \"gate0_ckpt400_re_f1\": 0.3793, \"gate0_ckpt400_parse_failures\": 0, \"gate0_ckpt400_verdict\": \"FAIL\", \"gate0_ckpt400_re_sample_f1_pct_zero\": 58.8, \"gate0_ckpt400_warning\": \">30% samples F1=0\"}, \"completed_at\": \"2026-05-14T08:51:32.405Z\"}, \"mvp_pilot_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:02:16.991Z\", \"updated_at\": \"2026-05-14T08:48:14.040Z\", \"spec\": {\"hypothesis\": \"Structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa on fine-tuned Qwen3-8B SciERC\", \"model_name\": \"Qwen3-8B-SciERC-LoRA (ft_001)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment + gold-empty filter + conditional rho\", \"gpu\": \"cuda:0\", \"note\": \"Rerun of mvp_pilot_001 which crashed silently\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-lora --data_dir data/scierc --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 512 --output_dir output/mvp_pilot_001 --num_test 551 --seed 42 --tensor_parallel 1\", \"failure_reason\": \"Worker used LoRA adapter path instead of merged model path; vLLM cannot load LoRA adapter directly\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T08:48:14.040Z\"}, \"ft_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:18.640Z\", \"updated_at\": \"2026-05-14T08:28:00.590Z\", \"spec\": {\"hypothesis\": \"Extended training (5 epochs, LoRA r=32) improves RE F1 above 40% threshold\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"LoRA r=32 alpha=64, 5 epochs, relation direction hint\", \"command\": \"llamafactory-cli train /root/autodl-tmp/struct_self_consist_ie/train_config_v2.yaml\", \"gpu\": \"cuda:1\", \"pid\": 19666, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/ft_002_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2\", \"total_steps\": 585, \"trainable_params\": \"87.3M\", \"estimated_runtime\": \"29min\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T08:02:30.390Z\", \"metrics\": {\"last_step\": 70, \"total_steps\": 585, \"progress_pct\": 11.97, \"last_loss\": 0.1134, \"last_lr\": 0.00019982, \"elapsed\": \"3m32s\", \"failure_reason\": \"OOM at step 73, batch_size=4 too large for 32GB RTX 5090\"}}, \"ft_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:04:28.030Z\", \"updated_at\": \"2026-05-14T08:27:58.182Z\", \"spec\": {\"hypothesis\": \"Fine-tuned Qwen3-8B on SciERC UIE can achieve NER F1 >= 73 and serve as base model for structural consistency MVP\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"method\": \"LoRA r=16 alpha=32\", \"framework\": \"LLaMA Factory 0.9.4\", \"command\": \"sft training qwen3-8b on scierc with lora\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_001_train.log\", \"train_loss\": 0.1099, \"eval_loss\": 0.0771, \"epoch\": 3, \"train_runtime\": \"0:17:49\", \"note\": \"gate0: NER PASS 60.4% / RE FAIL 33.8%\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:30:32.889Z\", \"metrics\": {\"train_loss\": 0.1099, \"eval_loss\": 0.0771, \"gate0_ner_f1_strict\": 0.1143, \"gate0_re_f1_strict\": 0.0125, \"gate0_ner_f1_text\": 0.606, \"gate0_re_f1_text\": 0.3392, \"gate0_offset_accuracy\": 0.1665, \"gate0_parse_failures\": 43, \"gate0_pass\": false, \"gate0_realigned_ner_f1\": 0.6045, \"gate0_realigned_re_f1\": 0.338, \"gate0_realigned_entity_offset_accuracy\": 1, \"gate0_realigned_relation_offset_accuracy\": 1, \"gate0_realigned_ner_pass\": true, \"gate0_realigned_re_pass\": false, \"gate0_realigned_pass\": false, \"gate0_ner_f1_delta_realign\": 0.4901, \"gate0_re_f1_delta_realign\": 0.3255, \"verdict_note\": \"partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)\"}}, \"mvp_pilot_003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:21:09.847Z\", \"updated_at\": \"2026-05-14T08:21:44.983Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003 --num_test 551 --seed 42 --tensor_parallel 1\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged\", \"seed\": 42}, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/mvp_pilot_003.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T08:21:30.319Z\", \"metrics\": {\"ner_greedy_f1\": 0.6362, \"ner_oracle_f1\": 0.792, \"ner_headroom\": 0.1559, \"ner_fleiss_kappa_mean\": 0.2488, \"ner_soft_jaccard_mean\": 0.5066, \"ner_full_rho_sj\": 0.3808, \"ner_full_rho_fk\": 0.3362, \"ner_full_p_sj\": 1.07e-19, \"ner_full_p_fk\": 1.93e-15, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3836, \"ner_cond_rho_fk\": 0.3187, \"ner_cond_p_sj\": 1.83e-19, \"ner_cond_p_fk\": 1.33e-13, \"ner_cond_n\": 514, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0446, \"ner_sample_f1_mean\": 0.5153, \"ner_sample_f1_std\": 0.3334, \"ner_sample_f1_pct_zero\": 19.9, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 15, \"re_greedy_f1\": 0.3774, \"re_oracle_f1\": 0.5939, \"re_headroom\": 0.2165, \"re_fleiss_kappa_mean\": 0.0879, \"re_soft_jaccard_mean\": 0.3958, \"re_full_rho_sj\": 0.2367, \"re_full_rho_fk\": 0.2221, \"re_full_p_sj\": 1.85e-06, \"re_full_p_fk\": 7.92e-06, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3004, \"re_cond_rho_fk\": 0.2374, \"re_cond_p_sj\": 2.25e-08, \"re_cond_p_fk\": 1.19e-05, \"re_cond_n\": 333, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0146, \"re_sample_f1_mean\": 0.1977, \"re_sample_f1_std\": 0.3251, \"re_sample_f1_pct_zero\": 67.6, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 64, \"parse_failures_stochastic\": 0, \"parse_failures_greedy\": 0, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but below PASS bar\"}}, \"mvp_pilot_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:16.313Z\", \"updated_at\": \"2026-05-14T08:05:34.348Z\", \"spec\": {\"hypothesis\": \"Structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa on fine-tuned Qwen3-8B SciERC\", \"model_name\": \"qwen3-8b-scierc-merged\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/test.jsonl\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/mvp_pilot.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T07:52:47.006Z\", \"metrics\": {\"ner_greedy_f1\": 0.611, \"ner_oracle_f1\": 0.78, \"ner_headroom\": 0.169, \"ner_fleiss_kappa_mean\": 0.2449, \"ner_soft_jaccard_mean\": 0.5041, \"ner_full_rho_sj\": 0.3616, \"ner_full_rho_fk\": 0.3515, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3688, \"ner_cond_rho_fk\": 0.3569, \"ner_cond_n\": 510, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_pct_zero\": 20.4, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 19, \"re_greedy_f1\": 0.355, \"re_oracle_f1\": 0.572, \"re_headroom\": 0.217, \"re_fleiss_kappa_mean\": 0.0681, \"re_soft_jaccard_mean\": 0.3635, \"re_full_rho_sj\": 0.2535, \"re_full_rho_fk\": 0.2885, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3515, \"re_cond_rho_fk\": 0.3107, \"re_cond_n\": 320, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_pct_zero\": 58.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 77, \"parse_failures_stochastic\": 164, \"parse_failures_greedy\": 29, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set\"}}}, \"count\": 83, \"total\": 83, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4602}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T12:43:47.795Z_

<details><summary>↩ Tool result · `toolu_01UYwZJHAbrWqidfmvTfUc4j`</summary>

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
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Do Not Scale Structured Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "5c0839c4-f069-49dc-98e0-5569421d3052",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors:\\\\ Why Confidence Signals Do Not Scale Structured Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).\nCoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.\nNo new human data was collected or annotated for this study.\nOur findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T12:43:47.793Z_

<details><summary>↩ Tool result · `toolu_01NN2sSSgSuRaSL8LC8r2F1Y`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.
3	We compare five confidence signals across NER and relation extraction on three benchmarks with two 8B-parameter model families and uncover a \textit{correlation-selection gap}: signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom.
4	Most signals are instance-level by construction and cannot rank candidates; the empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection (MBR decoding) can bridge the gap.
5	Neither succeeds: log-probability scores are compressed into effective ties, while MBR utility correlates with quality across instances but not within them.
6	A controlled ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.
7	Signal rankings depend on task complexity, with findings consistent across two model families at 8B scale.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "71c76458-341f-41c1-8b7d-cb8b858297e6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.\nWe compare five confidence signals across NER and relation extraction on three benchmarks with two 8B-parameter model families and uncover a \\textit{correlation-selection gap}: signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom.\nMost signals are instance-level by construction and cannot rank candidates; the empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection (MBR decoding) can bridge the gap.\nNeither succeeds: log-probability scores are compressed into effective ties, while MBR utility correlates with quality across instances but not within them.\nA controlled ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.\nSignal rankings depend on task complexity, with findings consistent across two model families at 8B scale.\n\\end{abstract}\n",
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

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01EUa6aTERu4Cz6Morfponuk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "7eb001ec-64ca-461a-acda-da4f5e4ea367",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TA8Wag2xN9wHMQUc1d5Ed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1793,
      "cache_read_input_tokens": 23598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1793
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 16 · 2026-05-15T12:43:48.035Z_

<details><summary>↩ Tool result · `toolu_01EUa6aTERu4Cz6Morfponuk`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2025scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.
17	Our work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\rho{=}0.038$ (n.s.) and LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$)---that would be invisible on a single dataset.
18	
19	Structured IE requires schema-compliant output, making constrained decoding \cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\% valid JSON rate (\S\ref{sec:ablation}).}
20	All experiments use constrained decoding, the regime under which structured IE is practically deployed.
21	
22	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.
23	Four of five signals are instance-level by construction---this is definitional, not empirical.
24	The non-trivial questions are whether (a)~consensus-proximity selection, instantiating MBR decoding \cite{eikema2022sampling, freitag2022high, muller2021understanding}, can recover per-sample discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.
25	Both fail: MBR utility correlates with F1 across instances but not within them (\S\ref{sec:discussion}); log-probability scores are severely compressed (60\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
26	A controlled free-form decoding ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding (\S\ref{sec:ablation}).
27	
28	\begin{figure*}[t]
29	\centering
30	\includegraphics[width=\textwidth]{fig_overview}
31	\caption{The correlation-selection gap. \textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}
32	\label{fig:overview}
33	\end{figure*}
34	
35	We systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
36	Our contributions are:
37	\begin{enumerate}
38	    \item \textbf{A systematic evaluation framework.}
39	    We compare five confidence signals from three families---structural, surface, and model-internal---across quality estimation, binary discrimination, and sample selection, showing that these metrics decouple and single-metric evaluation risks selecting the wrong signal.
40	
41	    \item \textbf{The correlation-selection gap and its diagnosis.}
42	    Strong quality estimation ($\rho{=}0.38$, AUROC${=}0.75$) coexists with selection failure ($p{>}0.39$, 13--18~pp oracle headroom).
43	    The instance-level failure of four signals is definitional; the empirical contributions are diagnosing why consensus-proximity selection (MBR decoding) and log-probability both fail.
44	    LP score compression (60\% of instances effectively tied) is the primary bottleneck; where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
45	    A controlled ablation confirms that compression is intrinsic, not decoding-regime-specific.
46	
47	    \item \textbf{Task-complexity boundary conditions.}
48	    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.
49	    At the capability boundary (WNUT-17, 52\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\rho{=}{-}0.410$)---phenomena invisible on a single dataset that extend \citet{nedellec2026consistency}'s quality-estimation analysis.
50	    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).
51	\end{enumerate}
52	
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "2b8cefd4-96f1-4148-ac29-92909c003a34",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2025scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.\nOur work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\\rho{=}0.038$ (n.s.) and LP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$)---that would be invisible on a single dataset.\n\nStructured IE requires schema-compliant output, making constrained decoding \\cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\\% valid JSON rate (\\S\\ref{sec:ablation}).}\nAll experiments use constrained decoding, the regime under which structured IE is practically deployed.\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.\nFour of five signals are instance-level by construction---this is definitional, not empirical.\nThe non-trivial questions are whether (a)~consensus-proximity selection, instantiating MBR decoding \\cite{eikema2022sampling, freitag2022high, muller2021understanding}, can recover per-sample discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.\nBoth fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}); log-probability scores are severely compressed (60\\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\nA controlled free-form decoding ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding (\\S\\ref{sec:ablation}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \\textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{A systematic evaluation framework.}\n    We compare five confidence signals from three families---structural, surface, and model-internal---across quality estimation, binary discrimination, and sample selection, showing that these metrics decouple and single-metric evaluation risks selecting the wrong signal.\n\n    \\item \\textbf{The correlation-selection gap and its diagnosis.}\n    Strong quality estimation ($\\rho{=}0.38$, AUROC${=}0.75$) coexists with selection failure ($p{>}0.39$, 13--18~pp oracle headroom).\n    The instance-level failure of four signals is definitional; the empirical contributions are diagnosing why consensus-proximity selection (MBR decoding) and log-probability both fail.\n    LP score compression (60\\% of instances effectively tied) is the primary bottleneck; where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\n    A controlled ablation confirms that compression is intrinsic, not decoding-regime-specific.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.\n    At the capability boundary (WNUT-17, 52\\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\\rho{=}{-}0.410$)---phenomena invisible on a single dataset that extend \\citet{nedellec2026consistency}'s quality-estimation analysis.\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}\n\n",
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01Q4NSotQ5iP8CtfkhG1nwCS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "0b424c89-72c3-4e5e-aec0-aa2fc7b0eab1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TA8Wag2xN9wHMQUc1d5Ed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1793,
      "cache_read_input_tokens": 23598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1793
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 18 · 2026-05-15T12:43:49.036Z_

<details><summary>↩ Tool result · `toolu_01Q4NSotQ5iP8CtfkhG1nwCS`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling \cite{zhang2025tts}, \citet{snell2025scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.
15	Our Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\S\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).
16	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
17	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \cite{willard2023guided}.
18	
19	\paragraph{Uncertainty estimation and calibration.}
20	Surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs; \citet{xiong2024llm} find LLMs tend toward overconfidence, and \citet{heo2025uncertainty} show calibration degrades with task complexity.
21	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; \citet{kossen2024semantic} distill this into probes; P(True) \cite{kadavath2022language} queries model confidence directly; \citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.
22	Our structural signals instead measure agreement over output \textit{structure}.
23	Neural networks are often miscalibrated \cite{guo2017calibration, desai2020calibration}; deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.
24	Prior NER uncertainty work spans Bayesian inference for sequence labeling \cite{xiao2019uncertainty}, active learning under uncertainty \cite{shelmanov2021active}, evidential deep learning \cite{zhang2023ener}, verification-augmented NER \cite{kim2024verifiner}, and uncertainty transmission across label sequences \cite{he2024uncertainty}---all within discriminative paradigms.
25	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \cite{wang2024mathshepherd} learn per-sample scoring.
26	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \cite{freitag2022high} and other generation tasks \cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\S\ref{sec:discussion}).
27	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "e7cfa224-5912-42c9-8c20-6563d54ae4d0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.\nExtensions to free-form text use LLM-based comparison \\cite{chen2024usc}, atomic sub-claim decomposition \\cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \\cite{manakul2023selfcheckgpt}.\nFor test-time scaling \\cite{zhang2025tts}, \\citet{snell2025scaling} characterize compute scaling laws and \\citet{brown2024monkeys} show best-of-$N$ gains across tasks.\nRecent reward-free selectors include confidence-weighted voting \\cite{taubenfeld2025cisc}, KL-based self-certainty \\cite{kang2025selfcertainty}, adaptive sampling \\cite{kim2026reasc}, ranked aggregation \\cite{wang2025rankedvoting}, and latent-space consistency \\cite{oh2025latentsc}.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \\citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.\nAll of the above target reasoning/QA with discrete answers or specific aggregation strategies.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).\n\n\\paragraph{Consistency for structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.\nTheir work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.\nOur Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\nCoCoA \\cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic} for LLMs; \\citet{xiong2024llm} find LLMs tend toward overconfidence, and \\citet{heo2025uncertainty} show calibration degrades with task complexity.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill this into probes; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.\nOur structural signals instead measure agreement over output \\textit{structure}.\nNeural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; deep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.\nPrior NER uncertainty work spans Bayesian inference for sequence labeling \\cite{xiao2019uncertainty}, active learning under uncertainty \\cite{shelmanov2021active}, evidential deep learning \\cite{zhang2023ener}, verification-augmented NER \\cite{kim2024verifiner}, and uncertainty transmission across label sequences \\cite{he2024uncertainty}---all within discriminative paradigms.\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \\cite{freitag2022high} and other generation tasks \\cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\\S\\ref{sec:discussion}).\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework.\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_013vYCXugSZha2icPVGE5Dgo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "460a5486-639b-4b36-9941-359be2319def",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TA8Wag2xN9wHMQUc1d5Ed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1793,
      "cache_read_input_tokens": 23598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1793
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 20 · 2026-05-15T12:43:49.494Z_

<details><summary>↩ Tool result · `toolu_013vYCXugSZha2icPVGE5Dgo`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}). A 3-seed stability analysis ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}, Appendix~\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}
20	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
21	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}
25	\label{sec:qe_results}
26	
27	\begin{table*}[t]
28	\centering
29	\small
30	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
31	\label{tab:quality_estimation}
32	\begin{tabular}{ll cc cc cc cc}
33	\toprule
34	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
35	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
36	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
37	\midrule
38	VC & Structural & \textbf{.379} & .684 & \textbf{.350} & .693 & .424 & .789 & .426 & .709 \\
39	SJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
40	FK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
41	EM  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
42	LP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \textbf{.761} \\
43	\bottomrule
44	\end{tabular}
45	\end{table*}
46	
47	\begin{figure*}[t]
48	\centering
49	\includegraphics[width=\textwidth]{fig_signal_heatmap}
50	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
51	\label{fig:signal_heatmap}
52	\end{figure*}
53	
54	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
55	
56	\paragraph{Difficulty-dependent signal complementarity.}
57	On SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$).
58	This advantage persists on RE (VC $\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\% zero-F1 floor effect.
59	VC and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
60	While the best $\rho{=}0.38$ (VC) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{Semantic entropy \cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA; direct comparison is not meaningful due to different output spaces.}
61	Pairwise bootstrap CIs confirm the SJ advantage over LP ($\Delta\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\Delta\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal}).
62	
63	\paragraph{$\rho$--AUROC dissociation.}
64	Signal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295), preferred for binary quality triage; structural signals ($\rho{\geq}0.36$) are better for fine-grained ranking.
65	On CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\rho$ (0.307), confirming this pattern across datasets.
66	
67	\paragraph{Signal rankings shift with task difficulty.}
68	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.
69	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
70	This crossover---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.
71	Stability across the two model families (both 8B) is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
72	On WNUT-17, where 52\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
73	LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$).
74	We hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.
75	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
76	
77	\paragraph{Conditional filtering.}
78	Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
79	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
80	LP RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
81	This creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
82	
83	%% ============================================================
84	\subsection{The Correlation-Selection Gap}
85	\label{sec:selection_gap}
86	
87	\begin{figure*}[t]
88	\centering
89	\includegraphics[width=\textwidth]{fig_selection_gap}
90	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound.}
91	\label{fig:selection_gap}
92	\end{figure*}
93	
94	\begin{table}[t]
95	\centering
96	\small
97	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \textbf{bold}. EM selects the plurality output; despite a 42\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}
98	\label{tab:selection}
99	\begin{tabular}{lcc}
100	\toprule
101	Method & NER F1 & RE F1 \\
102	\midrule
103	Oracle & 0.776 & 0.585 \\
104	\midrule
105	LP           & \textbf{0.650} & 0.395 \\
106	SJ       & 0.645 & 0.386 \\
107	EM        & 0.636 & 0.372 \\
108	VC                 & 0.634 & 0.359 \\
109	\midrule
110	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
111	Random             & 0.608 & 0.354 \\
112	\bottomrule
113	\end{tabular}
114	\end{table}
115	
116	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
117	Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.
118	The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
119	We anchor this analysis on SciERC, where output diversity is substantial: only 11--18\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.
120	
121	\paragraph{No significant improvement over greedy.}
122	We exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).
123	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
124	LP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).
125	On RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.
126	TOST equivalence testing confirms most signals are indistinguishable from greedy at ${\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\pm}5$~pp (Table~\ref{tab:tost}, Appendix~\ref{app:diversity}).
127	VC ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{below} greedy.
128	The gap extends to CoNLL (ceiling effect, 57--88\% identical outputs) and WNUT-17 (capability boundary; Table~\ref{tab:cross_selection}).
129	
130	\paragraph{Quality estimation $\neq$ output selection.}
131	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
132	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
133	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
134	
135	%% ============================================================
136	\subsection{Robustness}
137	\label{sec:robustness_main}
138	
139	Consistency-based signals show robust performance across $T{\in}\{0.7, 1.0\}$ (SJ NER $\Delta\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$; Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
140	On RE, only VC consistently outperforms LP ($\Delta\rho{=}{+}0.012$, preliminary).
141	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
142	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "61be1996-affd-4f9b-ba10-9e3993475e28",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nWe note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.\nNo reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.\nThis constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.\nWe discuss implications in the Limitations section.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}). A 3-seed stability analysis ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Difficulty-dependent signal complementarity.}\nOn SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and LP ($\\rho{=}0.205$).\nThis advantage persists on RE (VC $\\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\\% zero-F1 floor effect.\nVC and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (VC) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{Semantic entropy \\cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA; direct comparison is not meaningful due to different output spaces.}\nPairwise bootstrap CIs confirm the SJ advantage over LP ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\\Delta\\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal}).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nSignal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295), preferred for binary quality triage; structural signals ($\\rho{\\geq}0.36$) are better for fine-grained ranking.\nOn CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\\rho$ (0.307), confirming this pattern across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis crossover---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.\nStability across the two model families (both 8B) is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 52\\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$).\nWe hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \\citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLP RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \\textbf{bold}. EM selects the plurality output; despite a 42\\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLP           & \\textbf{0.650} & 0.395 \\\\\nSJ       & 0.645 & 0.386 \\\\\nEM        & 0.636 & 0.372 \\\\\nVC                 & 0.634 & 0.359 \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial: only 11--18\\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.\n\n\\paragraph{No significant improvement over greedy.}\nWe exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.\nTOST equivalence testing confirms most signals are indistinguishable from greedy at ${\\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\\pm}5$~pp (Table~\\ref{tab:tost}, Appendix~\\ref{app:diversity}).\nVC ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{below} greedy.\nThe gap extends to CoNLL (ceiling effect, 57--88\\% identical outputs) and WNUT-17 (capability boundary; Table~\\ref{tab:cross_selection}).\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals show robust performance across $T{\\in}\\{0.7, 1.0\\}$ (SJ NER $\\Delta\\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$; Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nOn RE, only VC consistently outperforms LP ($\\Delta\\rho{=}{+}0.012$, preliminary).\nNER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\n",
      "numLines": 142,
      "startLine": 1,
      "totalLines": 142
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01UFboULD7r4sDkpJKmncdXa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "8c23cb3a-b6e8-4408-b769-d3f5270937ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TA8Wag2xN9wHMQUc1d5Ed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1793,
      "cache_read_input_tokens": 23598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1793
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 22 · 2026-05-15T12:43:49.953Z_

<details><summary>↩ Tool result · `toolu_01UFboULD7r4sDkpJKmncdXa`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.
6	At higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) with lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).
7	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
8	
9	\paragraph{Why the gap exists: two layers.}
10	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
11	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
12	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
13	LP scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
14	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
15	This diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.
16	A controlled ablation (\S\ref{sec:ablation}) confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.
17	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
18	
19	\paragraph{Connection to MBR decoding.}
20	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
21	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
22	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
23	
24	\paragraph{Score compression is task-inherent.}\label{sec:ablation}
25	A natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.
26	We test this via controlled ablation: generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\%, 4406/4408; Table~\ref{tab:freeform_ablation}).
27	LP variance is essentially unchanged (within-instance std ratio $0.97{\times}$, tied fraction 59.7\%$\to$57.7\%).
28	NER selection gains remain negligible ($+0.18$~pp free-form vs.\ $+0.59$~pp constrained).
29	This rules out constrained decoding as the cause of compression and establishes LP compression as inherent to structured output generation.
30	The correlation-selection gap is therefore a fundamental challenge for test-time scaling in structured IE, not an artifact of any particular decoding strategy.
31	Notably, the fine-tuned model achieved 99.95\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.
32	
33	\paragraph{What drives the universal gap?}
34	Our analysis reveals two complementary mechanisms.
35	First, the free-form ablation exposes a task-specific interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that is universal across all 7 relation types and driven by selective variance reallocation ($p{<}0.0001$).
36	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
37	This interaction does not generalize to NER, where selection remains negligible under both regimes.
38	This ablation uses a single seed (seed${=}42$); multi-seed replication is left for future work.
39	Second, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
40	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
41	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
42	
43	\paragraph{Methodological implications.}
44	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
45	Effective selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.
46	Cross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\rho{=}0.469$ OOD vs.\ $0.386$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\ref{app:ood}).
47	Our findings are established under constrained decoding with a single-dataset ablation suggesting the gap is intrinsic; whether this generalizes across decoding regimes, datasets, and model scales warrants further investigation.
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "b4f93073-2d30-4640-a10c-a80f0ee417e8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.\nAt higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) with lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\nLP scores are severely compressed: 60\\% of instances have a within-sample range below 0.05, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$; Appendix~\\ref{app:logprob_ties}).\nIn the 40\\% of instances where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\\rho$: 0.08$\\to$0.39).\nThis diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.\nA controlled ablation (\\S\\ref{sec:ablation}) confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Score compression is task-inherent.}\\label{sec:ablation}\nA natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.\nWe test this via controlled ablation: generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\\%, 4406/4408; Table~\\ref{tab:freeform_ablation}).\nLP variance is essentially unchanged (within-instance std ratio $0.97{\\times}$, tied fraction 59.7\\%$\\to$57.7\\%).\nNER selection gains remain negligible ($+0.18$~pp free-form vs.\\ $+0.59$~pp constrained).\nThis rules out constrained decoding as the cause of compression and establishes LP compression as inherent to structured output generation.\nThe correlation-selection gap is therefore a fundamental challenge for test-time scaling in structured IE, not an artifact of any particular decoding strategy.\nNotably, the fine-tuned model achieved 99.95\\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.\n\n\\paragraph{What drives the universal gap?}\nOur analysis reveals two complementary mechanisms.\nFirst, the free-form ablation exposes a task-specific interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that is universal across all 7 relation types and driven by selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nThis ablation uses a single seed (seed${=}42$); multi-seed replication is left for future work.\nSecond, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.\nCross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\\rho{=}0.469$ OOD vs.\\ $0.386$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\\ref{app:ood}).\nOur findings are established under constrained decoding with a single-dataset ablation suggesting the gap is intrinsic; whether this generalizes across decoding regimes, datasets, and model scales warrants further investigation.\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01Mb6kvQ81kd1ZrZuww5LPwZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "c68bd55f-61cb-49b5-8af4-617a4150baa6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TA8Wag2xN9wHMQUc1d5Ed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1793,
      "cache_read_input_tokens": 23598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1793
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 24 · 2026-05-15T12:43:50.544Z_

<details><summary>↩ Tool result · `toolu_01Mb6kvQ81kd1ZrZuww5LPwZ`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We systematically evaluate five confidence signals across quality estimation, binary discrimination, and sample selection for LLM-based structured IE, revealing that these metrics decouple---single-metric evaluation risks selecting the wrong signal for the intended use case.
4	All signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves sample selection despite 13--18~pp oracle headroom---the \textit{correlation-selection gap}.
5	The instance-level failure of four signals is definitional; the empirical finding is that neither consensus-proximity selection (MBR decoding) nor log-probability bridges the gap.
6	MBR utility correlates with quality across instances but not within them; LP scores are compressed into effective ties (60\% of instances), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
7	A controlled free-form decoding ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.
8	Signal rankings shift with task difficulty---EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude; at the capability boundary (WNUT-17), all signals collapse to non-significance.
9	RE findings rest on SciERC alone (preliminary) and warrant multi-benchmark validation.
10	Trained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "aaec1272-217c-4e81-862e-78f8636d9706",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe systematically evaluate five confidence signals across quality estimation, binary discrimination, and sample selection for LLM-based structured IE, revealing that these metrics decouple---single-metric evaluation risks selecting the wrong signal for the intended use case.\nAll signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves sample selection despite 13--18~pp oracle headroom---the \\textit{correlation-selection gap}.\nThe instance-level failure of four signals is definitional; the empirical finding is that neither consensus-proximity selection (MBR decoding) nor log-probability bridges the gap.\nMBR utility correlates with quality across instances but not within them; LP scores are compressed into effective ties (60\\% of instances), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\nA controlled free-form decoding ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.\nSignal rankings shift with task difficulty---EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude; at the capability boundary (WNUT-17), all signals collapse to non-significance.\nRE findings rest on SciERC alone (preliminary) and warrant multi-benchmark validation.\nTrained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_013TY1rSLz4Rvny2Fck9z4FZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "eb34d081-e8e7-4f35-9ede-4f689465cf8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TA8Wag2xN9wHMQUc1d5Ed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1793,
      "cache_read_input_tokens": 23598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1793
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 26 · 2026-05-15T12:43:50.914Z_

<details><summary>↩ Tool result · `toolu_013TY1rSLz4Rvny2Fck9z4FZ`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Our free-form ablation (\S\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the intrinsic compression finding generalizes to other datasets, model families, or model scales remains untested.
17	
18	Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking} active, injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.
19	At inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.
20	The empty blocks may weakly affect first-token probability distributions during training, potentially shifting LP score calibration on SciERC; however, since LP selection fails across all datasets including CoNLL and WNUT-17 (which lack this confound), the thinking token inconsistency is unlikely to explain the correlation-selection gap.
21	The absence of any reasoning content further limits the representational impact.
22	
23	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "f041cab0-35fa-497c-a375-27a7f467c2d6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nRE selection failure persists even when restricting to non-zero F1 instances (Appendix~\\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nA 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses only unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nOur free-form ablation (\\S\\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the intrinsic compression finding generalizes to other datasets, model families, or model scales remains untested.\n\nQwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active, injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.\nAt inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.\nThe empty blocks may weakly affect first-token probability distributions during training, potentially shifting LP score calibration on SciERC; however, since LP selection fails across all datasets including CoNLL and WNUT-17 (which lack this confound), the thinking token inconsistency is unlikely to explain the correlation-selection gap.\nThe absence of any reasoning content further limits the representational impact.\n\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_019qoc9y7dzgS15vtq892JAp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "386f0704-c27e-40b8-8860-13814a7789dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TA8Wag2xN9wHMQUc1d5Ed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1793,
      "cache_read_input_tokens": 23598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1793
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 28 · 2026-05-15T12:43:51.741Z_

<details><summary>↩ Tool result · `toolu_019qoc9y7dzgS15vtq892JAp`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.010$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as population standard deviation.}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm}0.008$ & --- \\
56	\quad VC &  & $0.458{\pm}0.003$ & --- \\
57	\quad LP &  & $0.310{\pm}0.005$ & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
65	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}
66	\label{fig:temperature_robustness}
67	\end{figure}
68	
69	\paragraph{Temperature sensitivity.}
70	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
71	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
72	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
73	
74	\paragraph{Sample size scaling.}
75	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
76	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
77	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
80	SJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
82	
83	\paragraph{Transfer across model families.}
84	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$).
85	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
86	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ LP $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
87	
88	\section{Calibration Analysis}\label{app:calibration}
89	
90	\begin{figure*}[t]
91	\centering
92	\includegraphics[width=\textwidth]{fig_reliability}
93	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
94	\label{fig:reliability}
95	\end{figure*}
96	
97	Reliability diagrams use 10 equal-width bins.
98	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
99	
100	\section{Additional Analyses}\label{app:additional}
101	
102	\paragraph{Per-relation diagnostic.}
103	RE signal degradation is relation-specific.
104	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
105	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
106	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
107	
108	\paragraph{Capability stratification.}
109	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
110	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
111	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
112	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
113	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
114	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
115	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
116	
117	\paragraph{Length vs.\ log-probability.}
118	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
119	
120	\begin{figure}[t]
121	\centering
122	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
123	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
124	\label{fig:length_logprob_scatter}
125	\end{figure}
126	
127	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
128	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
129	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
130	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
131	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
132	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
133	Evaluation circularity is negligible.
134	
135	\paragraph{Conditional filtering details.}
136	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
137	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
138	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
139	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
140	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
141	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
142	
143	\paragraph{WNUT-17 full signal analysis.}
144	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
145	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
146	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
147	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
148	
149	\begin{table}[t]
150	\centering
151	\small
152	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
153	\label{tab:wnut}
154	\begin{tabular}{lccccc}
155	\toprule
156	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
157	\midrule
158	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
159	FK      & .125 & .001 & .555 & .169 & .002 \\
160	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
161	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
162	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\paragraph{Cross-configuration selection analysis.}
168	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
169	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
170	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
171	
172	\begin{table*}[t]
173	\centering
174	\small
175	\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
176	\label{tab:cross_selection}
177	\begin{tabular}{llccccccc}
178	\toprule
179	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
180	\midrule
181	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
182	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
183	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
184	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
185	\bottomrule
186	\end{tabular}
187	\end{table*}
188	
189	\paragraph{Diminishing returns of $N$-scaling.}
190	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
191	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
192	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
193	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
194	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
195	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
196	
197	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
198	
199	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
200	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
201	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
202	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
203	
204	\begin{table}[t]
205	\centering
206	\small
207	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
208	\label{tab:bootstrap_signal_ci}
209	\begin{tabular}{lcc}
210	\toprule
211	Signal & $\rho$ & 95\% CI \\
212	\midrule
213	VC & +0.379 & [+0.299, +0.456] \\
214	SJ & +0.360 & [+0.277, +0.437] \\
215	EM & +0.295 & [+0.212, +0.371] \\
216	FK & +0.267 & [+0.176, +0.354] \\
217	LP & +0.205 & [+0.119, +0.291] \\
218	\bottomrule
219	\end{tabular}
220	
221	\vspace{0.5em}
222	
223	\begin{tabular}{lccc}
224	\toprule
225	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
226	\midrule
227	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
228	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
229	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
230	\bottomrule
231	\end{tabular}
232	
233	\smallskip
234	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
235	\end{table}
236	
237	\section{Diversity and Selection Analysis}\label{app:diversity}
238	
239	\paragraph{Output diversity quantification.}
240	Table~\ref{tab:diversity} summarizes output diversity across configurations.
241	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
242	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
243	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
244	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
245	
246	\begin{table}[t]
247	\centering
248	\small
249	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
250	\label{tab:diversity}
251	\begin{tabular}{lcc}
252	\toprule
253	Config & Identical & Unique \\
254	\midrule
255	Qwen/SciERC & 11\% & 43\% \\
256	LLaMA/SciERC & 18\% & 39\% \\
257	Qwen/CoNLL & 57\% & --- \\
258	LLaMA/CoNLL & 88\% & --- \\
259	WNUT-17 & 55\% & --- \\
260	\bottomrule
261	\end{tabular}
262	\end{table}
263	
264	\paragraph{Oracle-improvable fraction.}
265	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
266	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
267	
268	\paragraph{Diversity-stratified selection gap.}
269	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
270	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.
271	This rules out insufficient diversity as an explanation for the correlation-selection gap.
272	
273	\paragraph{TOST equivalence testing.}
274	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
275	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
276	The $\delta$ values are anchored to oracle headroom (13--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
277	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
278	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
279	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
280	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
281	
282	\begin{table}[t]
283	\centering
284	\small
285	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
286	\label{tab:tost}
287	\begin{tabular}{l cccc cccc}
288	\toprule
289	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
290	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
291	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
292	\midrule
293	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
294	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
295	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
296	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
297	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
298	\bottomrule
299	\end{tabular}
300	\end{table}
301	
302	\section{Multi-Seed Stability}\label{app:multiseed}
303	
304	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
305	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals.
306	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
307	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
308	
309	\begin{table}[t]
310	\centering
311	\small
312	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
313	\label{tab:multiseed}
314	\begin{tabular}{lccccc}
315	\toprule
316	& LP & FK & SJ & VC & EM \\
317	\midrule
318	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
319	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
320	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
321	\midrule
322	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
323	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
324	\midrule
325	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
326	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
327	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
328	\bottomrule
329	\end{tabular}
330	\end{table}
331	
332	\section{Training Configuration}\label{app:training}
333	
334	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
335	
336	\begin{table}[t]
337	\centering
338	\small
339	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
340	\label{tab:training}
341	\begin{tabular}{ll}
342	\toprule
343	Parameter & Value \\
344	\midrule
345	LoRA rank / $\alpha$ & 32 / 64 \\
346	LoRA target & All linear modules \\
347	LoRA dropout & 0 \\
348	Optimizer & AdamW \\
349	Learning rate & 2e-4, cosine schedule \\
350	Warmup ratio & 0.1 \\
351	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
352	Epochs & 5 \\
353	Max sequence length & 2048 \\
354	Precision & bf16 \\
355	Gradient checkpointing & Enabled \\
356	Max gradient norm & 1.0 \\
357	Training seed & 42 \\
358	Framework & LLaMA Factory \\
359	\midrule
360	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
361	SciERC split & 1861 / 275 / 551 \\
362	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
363	& eval\_steps${=}$200, save\_limit${=}$5 \\
364	\bottomrule
365	\end{tabular}
366	\end{table}
367	
368	\paragraph{Prompt template.}
369	For NER, we use a structured prompt:
370	\begin{quote}
371	\small
372	\texttt{System:} You are an expert in Named Entity Recognition.\\
373	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
374	Text: \texttt{\{input\_text\}}\\
375	Entity types: \texttt{\{schema\_types\}}
376	\end{quote}
377	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
378	
379	\paragraph{Constrained decoding.}
380	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
381	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
382	
383	\section{Log-Probability Score Compression}\label{app:logprob_ties}
384	
385	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}).
386	The median within-instance LP range is only 0.041, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
387	At $\varepsilon{=}0.05$, 60.3\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.
388	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
389	
390	\begin{table}[t]
391	\centering
392	\small
393	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
394	\label{tab:logprob_ties}
395	\begin{tabular}{lc}
396	\toprule
397	$\varepsilon$ threshold & Tied instances (\%) \\
398	\midrule
399	0.01 & 1.1\% \\
400	0.05 & 60.3\% \\
401	0.1  & ${\sim}$84\% \\
402	0.5  & ${\sim}$99\% \\
403	\bottomrule
404	\end{tabular}
405	\end{table}
406	
407	\paragraph{Non-tied subset.}
408	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
409	This confirms that LP carries useful per-sample quality information but is resolution-limited---the signal exists but is compressed below the discrimination threshold for most instances.
410	A free-form decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression is intrinsic, not decoding-regime-specific.
411	
412	\section{RE Conditional Selection}\label{app:re_conditional_selection}
413	
414	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
415	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
416	All five signals underperform greedy on both subsets.
417	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
418	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
419	
420	\begin{table}[t]
421	\centering
422	\small
423	\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
424	\label{tab:re_cond_selection}
425	\begin{tabular}{lcc}
426	\toprule
427	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
428	\midrule
429	Oracle & 0.585 & 0.757 \\
430	\midrule
431	LP & 0.395 & 0.600 \\
432	SJ & 0.386 & 0.604 \\
433	EM & 0.372 & 0.583 \\
434	VC & 0.359 & 0.574 \\
435	\midrule
436	Greedy & 0.404 & 0.674 \\
437	\bottomrule
438	\end{tabular}
439	\end{table}
440	
441	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
442	
443	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).
444	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
445	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
446	RE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\ $-0.68$~pp constrained).
447	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
448	
449	\begin{table*}[t]
450	\centering
451	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}
452	\label{tab:freeform_ablation}
453	
454	\vspace{2pt}
455	{\small\textsc{Panel A: Logprob Distribution}}
456	\vspace{2pt}
457	
458	\begin{tabular}{lccc}
459	\toprule
460	Metric & Constrained & Free-form & $\Delta$ \\
461	\midrule
462	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
463	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
464	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
465	\bottomrule
466	\end{tabular}
467	
468	\vspace{8pt}
469	
470	{\small\textsc{Panel B: Selection F1}}
471	\vspace{2pt}
472	
473	\begin{tabular}{llccc}
474	\toprule
475	Task & Method & Constrained & Free-form & $\Delta$ \\
476	\midrule
477	\multirow{3}{*}{NER}
478	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
479	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
480	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
481	\midrule
482	\multirow{3}{*}{RE}
483	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
484	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
485	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
486	\bottomrule
487	\end{tabular}
488	
489	\vspace{8pt}
490	
491	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
492	\vspace{2pt}
493	
494	\begin{tabular}{l ccc ccc}
495	\toprule
496	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
497	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
498	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
499	\midrule
500	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
501	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
502	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
503	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
504	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
505	\bottomrule
506	\end{tabular}
507	
508	\vspace{8pt}
509	
510	{\small\textsc{Panel D: Parse Rate (Free-form)}}
511	\vspace{2pt}
512	
513	\begin{tabular}{lc}
514	\toprule
515	Metric & Value \\
516	\midrule
517	Total samples          & 4408 \\
518	Parse rate             & 99.95\% \\
519	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
520	\bottomrule
521	\end{tabular}
522	
523	\end{table*}
524	
525	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
526	
527	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
528	
529	\paragraph{Pairwise overlap.}
530	LP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
531	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
532	
533	\paragraph{Instance complexity drives failure.}
534	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
535	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
536	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
537	
538	\begin{table}[t]
539	\centering
540	\small
541	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}
542	\label{tab:stable_failures}
543	\begin{tabular}{lcccc}
544	\toprule
545	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
546	\midrule
547	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
548	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
549	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
550	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
551	\bottomrule
552	\end{tabular}
553	\end{table}
554	
555	\paragraph{Flip instances.}
556	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
557	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
558	
559	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
560	
561	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
562	
563	\begin{table}[t]
564	\centering
565	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
566	\label{tab:n-scaling}
567	\small
568	\begin{tabular}{l ccc ccc}
569	\toprule
570	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
571	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
572	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
573	\midrule
574	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
575	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
576	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
577	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
578	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
579	\midrule
580	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
581	\bottomrule
582	\end{tabular}
583	\end{table}
584	
585	\begin{table}[t]
586	\centering
587	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
588	\label{tab:ranking-stability}
589	\small
590	\begin{tabular}{ll cc l}
591	\toprule
592	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
593	\midrule
594	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
595	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
596	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
597	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
598	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
599	\bottomrule
600	\end{tabular}
601	\end{table}
602	
603	\begin{table}[t]
604	\centering
605	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
606	\label{tab:sigma-comparison}
607	\small
608	\begin{tabular}{l cc cc}
609	\toprule
610	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
611	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
612	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
613	\midrule
614	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
615	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
616	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
617	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
618	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
619	\midrule
620	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
621	\bottomrule
622	\end{tabular}
623	\end{table}
624	
625	Signal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}).
626	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
627	
628	\section{Cross-Dataset OOD Analysis}\label{app:ood}
629	
630	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
631	
632	\begin{table}[t]
633	\centering
634	\small
635	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$). In-domain $\rho$ from Table~\ref{tab:quality_estimation}. \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
636	\label{tab:ood}
637	\begin{tabular}{l ccc ccc}
638	\toprule
639	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
640	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
641	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
642	\midrule
643	VC & .469\textsuperscript{***} & .386 & +.083 & +.105\textsuperscript{*} & .386 & $-$.281 \\
644	SJ & .378\textsuperscript{***} & .364 & +.014 & $-$.186\textsuperscript{***} & .364 & $-$.550 \\
645	EM & .300\textsuperscript{***} & .307 & $-$.007 & $-$.202\textsuperscript{***} & .307 & $-$.509 \\
646	FK & .285\textsuperscript{***} & .254 & +.031 & $-$.070 & .254 & $-$.324 \\
647	LP & .246\textsuperscript{***} & .217 & +.029 & $-$.152\textsuperscript{***} & .217 & $-$.369 \\
648	\bottomrule
649	\end{tabular}
650	\end{table}
651	
652	\paragraph{Wider-to-narrower schema transfer.}
653	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.386$, $\Delta{=}{+}0.083$), SJ $\rho{=}0.378$ (in-domain $0.364$, $\Delta{=}{+}0.014$), and FK $\rho{=}0.285$ (in-domain $0.254$, $\Delta{=}{+}0.031$).
654	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
655	
656	\paragraph{Narrower-to-wider schema transfer (excluded).}
657	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
658	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).
659	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
660	These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
661	
662	\paragraph{Asymmetry interpretation.}
663	The directional asymmetry is driven by schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
664	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
665	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "bed742d1-aebd-4d67-a1ca-0ea78b599911",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.010$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as population standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad VC &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad LP &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), making it a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ LP $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLP shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\nThe $\\delta$ values are anchored to oracle headroom (13--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ greedy).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals.\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}).\nThe median within-instance LP range is only 0.041, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nThis confirms that LP carries useful per-sample quality information but is resolution-limited---the signal exists but is compressed below the discrimination threshold for most instances.\nA free-form decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression is intrinsic, not decoding-regime-specific.\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform greedy on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\\ $-0.68$~pp constrained).\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}\n\\toprule\nTask & Method & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{NER}\n  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\\\\n  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\\\\n  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\\\\n\\midrule\n\\multirow{3}{*}{RE}\n  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\\\\n  & LP-selected   & 0.2845 & 0.3050 & \\textbf{$+$0.0205} \\\\\n  & Selection gap & $-$0.0068 & $+$0.0169 & \\textbf{$+$0.0237} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel C: QE Signal Quality (Spearman $\\rho$)}}\n\\vspace{2pt}\n\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{NER ($n{=}529$)} & \\multicolumn{3}{c}{RE ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & Constr. & Free & $\\Delta$ & Constr. & Free & $\\Delta$ \\\\\n\\midrule\nSJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\\\\nFK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\\\\nLP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\\\\nEM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\\\\nVC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel D: Parse Rate (Free-form)}}\n\\vspace{2pt}\n\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal samples          & 4408 \\\\\nParse rate             & 99.95\\% \\\\\nInstances 8/8 valid    & 549\\,/\\,551 (99.6\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\n\\end{table*}\n\n\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\n\nWe analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n\n\\paragraph{Pairwise overlap.}\nLP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.\nThe 3-way intersection contains 34 instances (27.9\\% of any-seed failures), confirming a stable failure core.\n\n\\paragraph{Instance complexity drives failure.}\nTable~\\ref{tab:stable_failures} stratifies instances by failure stability.\nStable failures (all 3 seeds) involve more gold relations (2.12 vs.\\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.\nFailure rate increases monotonically with gold relation count: 4.3\\% at 1 relation, 20.7\\% at 3 relations, 26.2\\% at 6 relations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}\n\\label{tab:stable_failures}\n\\begin{tabular}{lcccc}\n\\toprule\nGroup & $n$ & Gold rels & Greedy F1 & LP $\\Delta$F1 \\\\\n\\midrule\nStable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\\\\nFail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\\\\nFail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\\\\nNever fail & 429 & 1.62 & 0.429 & $+$0.041 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Flip instances.}\nOnly 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\nThese instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.\n\n\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\n\nTables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\n\\label{tab:n-scaling}\n\\small\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{NER} $\\rho$} & \\multicolumn{3}{c}{\\textbf{RE} $\\rho$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ \\\\\n\\midrule\nSJ & 0.3641 & 0.4105 & \\textbf{+0.0464} & 0.2485 & 0.2758 & \\textbf{+0.0273} \\\\\nFK & 0.2536 & 0.2833 & \\textbf{+0.0297} & 0.2903 & 0.2964 & \\textbf{+0.0061} \\\\\nVC & 0.3861 & 0.4092 & \\textbf{+0.0231} & 0.3088 & 0.3738 & \\textbf{+0.0650} \\\\\nLP & 0.2167 & 0.2393 & \\textbf{+0.0226} & 0.2970 & 0.3100 & \\textbf{+0.0130} \\\\\nEM & 0.3071 & 0.3395 & \\textbf{+0.0324} & 0.1353 & 0.1506 & \\textbf{+0.0153} \\\\\n\\midrule\nMean & 0.3055 & 0.3364 & \\textbf{+0.0308} & 0.2560 & 0.2813 & \\textbf{+0.0253} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\n\\label{tab:ranking-stability}\n\\small\n\\begin{tabular}{ll cc l}\n\\toprule\nModel & Task & $N$ & Kendall's $W$ & Consensus ranking \\\\\n\\midrule\nQwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\nQwen  & NER & 16 & 0.956 & SJ $\\approx$ VC $>$ EM $>$ FK $>$ LP \\\\\nQwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nQwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nLLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\n\\label{tab:sigma-comparison}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{NER} $\\sigma_\\rho$} & \\multicolumn{2}{c}{\\textbf{RE} $\\sigma_\\rho$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $N\\!=\\!8$ & $N\\!=\\!16$ \\\\\n\\midrule\nSJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\\\\nFK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\\\\nVC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\\\\nEM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\\\\nLP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\\\\n\\midrule\nMean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSignal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}).\nDoubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER), confirming that additional samples stabilize structural signals more than LP.\n\n\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\n\nTo test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation}. \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\n\\label{tab:ood}\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{SciERC$\\to$CoNLL}} & \\multicolumn{3}{c}{\\textbf{CoNLL$\\to$SciERC}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $\\rho$ & In-dom. & $\\Delta$ & $\\rho$ & In-dom. & $\\Delta$ \\\\\n\\midrule\nVC & .469\\textsuperscript{***} & .386 & +.083 & +.105\\textsuperscript{*} & .386 & $-$.281 \\\\\nSJ & .378\\textsuperscript{***} & .364 & +.014 & $-$.186\\textsuperscript{***} & .364 & $-$.550 \\\\\nEM & .300\\textsuperscript{***} & .307 & $-$.007 & $-$.202\\textsuperscript{***} & .307 & $-$.509 \\\\\nFK & .285\\textsuperscript{***} & .254 & +.031 & $-$.070 & .254 & $-$.324 \\\\\nLP & .246\\textsuperscript{***} & .217 & +.029 & $-$.152\\textsuperscript{***} & .217 & $-$.369 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Wider-to-narrower schema transfer.}\nWhen the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.386$, $\\Delta{=}{+}0.083$), SJ $\\rho{=}0.378$ (in-domain $0.364$, $\\Delta{=}{+}0.014$), and FK $\\rho{=}0.285$ (in-domain $0.254$, $\\Delta{=}{+}0.031$).\nThe wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.\n\n\\paragraph{Narrower-to-wider schema transfer (excluded).}\nThe reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.\nThe CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).\nUnder this regime, most signals flip to negative or near-zero correlations (Table~\\ref{tab:ood}); only VC retains weak positive correlation ($\\rho{=}0.105$, $p{=}0.016$).\nThese negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\\S\\ref{sec:qe_results}), not evidence against signal utility.\n\n\\paragraph{Asymmetry interpretation.}\nThe directional asymmetry is driven by schema coverage: wider$\\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.\nThis extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.\n",
      "numLines": 665,
      "startLine": 1,
      "totalLines": 665
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
The registry data is very large and was saved to a file. I need to read it in chunks. Let me also check if there's a method.tex file since main.tex includes it. Let me also read the registry data focusing on the key experiments mentioned in the task.

Let me first read the registry data for the specific experiments I need to check:
1. exp_012_rerun_1024 - Table 1 quality estimation
2. exp_016_rerun_1024 - Table 2 selection F1
3. exp_018_llama_scierc_seed42_r1024 - LLaMA data


4. exp_007 - old data that should NOT be used
5. exp_011_ood_conll_to_scierc - OOD analysis
6. exp_019 - supervised verifier (should NOT appear)

I need to continue reading the appendix and the method section to get the full picture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "a1b7f16d-9d90-4da7-bc22-6749c1f50b3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHp8Ys7pie2PVUS8ELADnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30762,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30762
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

_source line 30_

Now I need to read the registry data and the remaining files. Let me read the registry in chunks and the method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "a39f64c5-59e6-4271-9c6c-fb56d1be9f9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHp8Ys7pie2PVUS8ELADnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30762,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30762
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_011q8y7a9krb61At4zCzfyUr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 665
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "6411768a-4b11-4554-97b3-d76d0123728f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHp8Ys7pie2PVUS8ELADnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30762,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30762
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

_source line 32 · 2026-05-15T12:44:03.693Z_

<details><summary>↩ Tool result · `toolu_011q8y7a9krb61At4zCzfyUr`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (665). The file has 665 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "b8f7cb99-4513-4968-be4c-ab044351fc02",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "",
      "numLines": 1,
      "startLine": 665,
      "totalLines": 665
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Glob · `toolu_01TyQw8Avgbi9K53v3TRvEWF`</summary>

```json
{
  "pattern": "sections/method.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "b9d908a1-510b-47e7-8fbb-7bd4d79dc468",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHp8Ys7pie2PVUS8ELADnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30762,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30762
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

_source line 34 · 2026-05-15T12:44:04.245Z_

<details><summary>↩ Tool result · `toolu_01TyQw8Avgbi9K53v3TRvEWF`</summary>

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
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "413219db-9344-47ec-9a10-0d121d82b011",
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

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01LCFLJ6tU8vC21VbH727iNL`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7/tool-results/mcp-agent-ml-research-read_registry-1778849027754.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\n# Get list of all experiment IDs\nfor exp in result:\n    print(f\\\"{exp.get('exp_id', 'N/A')} | status={exp.get('status', 'N/A')} | conclusion={str(exp.get('conclusion', 'N/A'))[:80]}\\\")\n\"",
  "description": "Parse registry to list all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "2b6a58e1-538d-4ec0-b9aa-2f58852e7249",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHp8Ys7pie2PVUS8ELADnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30762,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30762
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

_source line 36 · 2026-05-15T12:44:08.995Z_

<details><summary>↩ Tool result · reported error · `toolu_01LCFLJ6tU8vC21VbH727iNL`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    print(f"{exp.get('exp_id', 'N/A')} | status={exp.get('status', 'N/A')} | conclusion={str(exp.get('conclusion', 'N/A'))[:80]}")
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
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "c6c7f218-2098-444c-be8f-5b97baff4b67",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 7, in &lt;module>\n    print(f\"{exp.get('exp_id', 'N/A')} | status={exp.get('status', 'N/A')} | conclusion={str(exp.get('conclusion', 'N/A'))[:80]}\")\n             ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_014WSwAuLtJPcqiT95i11B4y`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7/tool-results/mcp-agent-ml-research-read_registry-1778849027754.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult_str = data['result']\n# Check the structure\nprint(type(result_str))\nprint(result_str[:500])\n\"",
  "description": "Inspect registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "8375ad0a-f4f5-48cc-bd85-06ed45f2b0ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TsRBoy3hyauaqNGbqzmb6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 56153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 970
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

_source line 38 · 2026-05-15T12:44:13.328Z_

<details><summary>↩ Tool result · `toolu_014WSwAuLtJPcqiT95i11B4y`</summary>

```text
&lt;class 'str'>
{"success": true, "data": {"experiments": {"exp008_re_n16": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-14T12:09:50.987Z", "updated_at": "2026-05-15T12:41:39.774Z", "spec": {"command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp008_re_n16 && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "1f7ba756-b340-488f-a4ab-b2796266ad85",
  "tool_use_result": {
    "stdout": "&lt;class 'str'>\n{\"success\": true, \"data\": {\"experiments\": {\"exp008_re_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:50.987Z\", \"updated_at\": \"2026-05-15T12:41:39.774Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp008_re_n16 && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/s",
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

_source line 39_

<details open><summary>🔧 Tool call — Glob · `toolu_013ZzA7RipDHgxD8tUCGf4rR`</summary>

```json
{
  "pattern": "**/method.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "d9d85717-569d-40f3-ba1f-4f9764ed3d3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TsRBoy3hyauaqNGbqzmb6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 56153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 970
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

_source line 40 · 2026-05-15T12:44:13.622Z_

<details><summary>↩ Tool result · `toolu_013ZzA7RipDHgxD8tUCGf4rR`</summary>

```text
docs/paper/sections/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "4bf7cc26-550c-4c7a-bfc3-8af6462fff5e",
  "tool_use_result": {
    "filenames": [
      "docs/paper/sections/method.tex"
    ],
    "durationMs": 7,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01WMfQVT8JsWNuAKwqu1q6qC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "6474ff40-2de9-4b64-9246-8438de2e622a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8CLT61dvuPuH89eW7fV6Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 590,
      "cache_read_input_tokens": 57123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 590
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

_source line 42 · 2026-05-15T12:44:16.806Z_

<details><summary>↩ Tool result · `toolu_01WMfQVT8JsWNuAKwqu1q6qC`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{&lt;j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface, instance-level).}
28	The majority fraction---the proportion of samples producing the most common output:
29	\begin{equation}\label{eq:em}
30	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
31	\end{equation}
32	
33	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
34	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
35	\begin{equation}\label{eq:fk}
36	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
37	\end{equation}
38	where $\bar{P}$ is mean observed pairwise agreement and $\bar{P}_e$ is expected agreement under random assignment.
39	While FK assumes independent raters, temperature-based sampling yields mild negative dependence rather than positive correlation among samples.
40	Empirically, we measure excess agreement ($\bar{P} - \bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\% and $-$4.0\%, indicating mild \textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.
41	(All excess agreement values are negative across 5 configurations; a one-sample $t$-test against zero yields $p{<}0.05$.)
42	Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.
43	
44	\paragraph{Soft Jaccard (structural, instance-level).}
45	Our primary structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
46	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:
47	\begin{equation}\label{eq:sj}
48	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
49	\end{equation}
50	where $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.
51	We use $\max(|g_i|, |g_j|)$ rather than $|g_i \cup g_j|$ as the normalizer to penalize length asymmetry between samples.
52	The instance-level signal averages over all pairs:
53	\begin{equation}\label{eq:sj_instance}
54	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
55	\end{equation}
56	
57	\paragraph{Entity voting confidence (structural, instance-level).}
58	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
59	The instance-level confidence is the mean frequency:
60	\begin{equation}\label{eq:voting}
61	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
62	\end{equation}
63	When $E_\cup = \emptyset$ (no entity extracted by any sample), we set $c_{\mathrm{vc}}(x) = 0$.\footnote{This occurs in $<$1\% of instances in our experiments (WNUT-17 only). Equation~\ref{eq:voting} defines the continuous QE signal used throughout Table~\ref{tab:quality_estimation} and all correlation analyses. For voted-output \textit{selection} (Table~\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting. The two computations serve different purposes: Eq.~\ref{eq:voting} assigns a continuous quality score per instance; the majority threshold constructs a discrete output for F1 evaluation. On NER, the threshold variant yields $\rho{=}0.252$ (vs.\ $0.379$ for Eq.~\ref{eq:voting}), reflecting information loss from binarization; on RE, the difference is negligible ($\Delta\rho{=}0.019$).}
64	
65	\subsection{Evaluation Framework}\label{sec:evaluation}
66	
67	\paragraph{Quality estimation.}
68	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
69	
70	\paragraph{Sample selection.}
71	We report best-of-$N$ F1: for each instance, the signal selects one sample.
72	Per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).
73	We compare against an \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$, $N{=}1$).
74	
75	\paragraph{Complementarity.}
76	High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "dcfe0adf-7bad-4eeb-8c1a-0de361f79727",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}.\nEach $y_i$ is an entity set (NER) or relation set (RE).\nA confidence signal $c$ serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among $N$ candidates.\n\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct candidate ranking.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\nNotation is summarized in Appendix~\\ref{app:notation}.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe use \\textit{confidence signal} as the umbrella term for all five measures.\nFour are \\textit{consistency signals}---computed from inter-sample agreement---spanning two families: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]).\nThe fifth, log-probability, is the sole \\textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal.\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{&lt;j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe majority fraction---the proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.\nWhile FK assumes independent raters, temperature-based sampling yields mild negative dependence rather than positive correlation among samples.\nEmpirically, we measure excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\\% and $-$4.0\\%, indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.\n(All excess agreement values are negative across 5 configurations; a one-sample $t$-test against zero yields $p{<}0.05$.)\nUnlike structural signals, FK relies on exact string matching and does not tolerate surface variations.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur primary structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.\nWe use $\\max(|g_i|, |g_j|)$ rather than $|g_i \\cup g_j|$ as the normalizer to penalize length asymmetry between samples.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$ (no entity extracted by any sample), we set $c_{\\mathrm{vc}}(x) = 0$.\\footnote{This occurs in $<$1\\% of instances in our experiments (WNUT-17 only). Equation~\\ref{eq:voting} defines the continuous QE signal used throughout Table~\\ref{tab:quality_estimation} and all correlation analyses. For voted-output \\textit{selection} (Table~\\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting. The two computations serve different purposes: Eq.~\\ref{eq:voting} assigns a continuous quality score per instance; the majority threshold constructs a discrete output for F1 evaluation. On NER, the threshold variant yields $\\rho{=}0.252$ (vs.\\ $0.379$ for Eq.~\\ref{eq:voting}), reflecting information loss from binarization; on RE, the difference is negligible ($\\Delta\\rho{=}0.019$).}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nWe measure rank correlation (Spearman $\\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.\n\n\\paragraph{Sample selection.}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample.\nPer-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).\nWe compare against an \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$, $N{=}1$).\n\n\\paragraph{Complementarity.}\nHigh rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\n",
      "numLines": 77,
      "startLine": 1,
      "totalLines": 77
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01GRdMSaUAdm3gAf82aCuyqV`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7/tool-results/mcp-agent-ml-research-read_registry-1778849027754.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor eid in sorted(exps.keys()):\n    e = exps[eid]\n    print(f\\\"{eid} | status={e.get('status','?')} | conclusion={str(e.get('conclusion',''))[:100]}\\\")\n\" 2>/dev/null || echo \"Trying alternative parse...\"",
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
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "e5cff9af-34e6-4d78-8b9c-4f259c578b59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8CLT61dvuPuH89eW7fV6Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 590,
      "cache_read_input_tokens": 57123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 590
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

_source line 44 · 2026-05-15T12:44:19.186Z_

<details><summary>↩ Tool result · `toolu_01GRdMSaUAdm3gAf82aCuyqV`</summary>

```text
e1_component_wise_re_sj | status=DONE | conclusion=negative
exp001_seed123 | status=DONE | conclusion=killed
exp001_seed456 | status=DONE | conclusion=killed
exp008_re_n16 | status=DONE | conclusion=killed
exp_001_n16_seed123 | status=DONE | conclusion=success
exp_001_n16_seed123_full | status=DONE | conclusion=killed
exp_001_n16_seed456 | status=DONE | conclusion=success
exp_001_n16_seed456_full | status=DONE | conclusion=killed
exp_001_ner_n16_scierc | status=DONE | conclusion=success
exp_001_ner_n16_seed123 | status=DONE | conclusion=success
exp_001_seed123_t10_full | status=DONE | conclusion=negative
exp_001_seed123_v2 | status=DONE | conclusion=success
exp_001_seed123_v2_r1024 | status=DONE | conclusion=killed
exp_001_seed42_v2 | status=DONE | conclusion=success
exp_001_seed42_v2_r1024 | status=DONE | conclusion=killed
exp_001_seed456_t10_full | status=DONE | conclusion=negative
exp_001_seed456_v2 | status=DONE | conclusion=negative
exp_001_seed456_v2_ner | status=DONE | conclusion=success
exp_001_seed456_v2_ner_r1024 | status=DONE | conclusion=killed
exp_002 | status=DONE | conclusion=success
exp_002_conll_n16 | status=DONE | conclusion=success
exp_002_conll_n16_r1024 | status=DONE | conclusion=killed
exp_002_merge_conll2003 | status=DONE | conclusion=killed
exp_002_ner_conll2003 | status=DONE | conclusion=success
exp_003_ner_wnut17 | status=DONE | conclusion=negative
exp_003_wnut17_eval | status=DONE | conclusion=success
exp_003_wnut17_v2 | status=DONE | conclusion=negative
exp_004_re_diagnostic | status=DONE | conclusion=success
exp_004_v2 | status=DONE | conclusion=success
exp_005 | status=DONE | conclusion=success
exp_005_v2 | status=DONE | conclusion=success
exp_006_v2 | status=DONE | conclusion=negative
exp_007_llama_inference | status=DONE | conclusion=success
exp_007_llama_n16 | status=DONE | conclusion=success
exp_007_llama_n16_r1024 | status=DONE | conclusion=killed
exp_007_llama_seed123 | status=DONE | conclusion=negative
exp_007_llama_seed456 | status=DONE | conclusion=negative
exp_007_ner_llama | status=DONE | conclusion=killed
exp_007_ner_multi_model | status=DONE | conclusion=success
exp_008_re_n16 | status=DONE | conclusion=success
exp_008_re_n16_full | status=DONE | conclusion=killed
exp_008_re_n16_t10_full | status=DONE | conclusion=negative
exp_008_re_n16_v2 | status=DONE | conclusion=negative
exp_008_re_seed123 | status=DONE | conclusion=negative
exp_009_capability_stratification | status=DONE | conclusion=success
exp_009_v2 | status=DONE | conclusion=success
exp_009_v2_re_rerun | status=DONE | conclusion=success
exp_010_selection_curves | status=DONE | conclusion=success
exp_011_ood_conll_to_scierc | status=DONE | conclusion=negative
exp_011_ood_scierc_to_conll | status=DONE | conclusion=success
exp_012_logprob_baseline | status=DONE | conclusion=success
exp_012_rerun_1024 | status=DONE | conclusion=success
exp_013_exact_match_voting | status=DONE | conclusion=negative
exp_014_entity_majority_voting | status=DONE | conclusion=success
exp_015_metrics_expansion | status=DONE | conclusion=success
exp_015_v2 | status=DONE | conclusion=success
exp_016_rerun_1024_bootstrap | status=DONE | conclusion=negative
exp_016_signal_ensemble | status=DONE | conclusion=success
exp_016_v2 | status=DONE | conclusion=success
exp_017_llama_conll | status=DONE | conclusion=success
exp_017_llama_conll_infer | status=DONE | conclusion=success
exp_017_llama_conll_n16 | status=DONE | conclusion=success
exp_017_llama_conll_n16_r1024 | status=DONE | conclusion=success
exp_017_llama_conll_n16_s123 | status=DONE | conclusion=success
exp_017_llama_conll_n16_s123_r1024 | status=DONE | conclusion=success
exp_017_llama_conll_n16_s456 | status=DONE | conclusion=success
exp_017_llama_conll_n16_s456_r1024 | status=DONE | conclusion=success
exp_018_llama_scierc_seed123 | status=DONE | conclusion=success
exp_018_llama_scierc_seed42_r1024 | status=DONE | conclusion=success
exp_018_llama_scierc_seed456 | status=DONE | conclusion=killed
exp_018_llama_scierc_seed456_r1024 | status=DONE | conclusion=success
exp_018_qwen_scierc_seed123 | status=DONE | conclusion=success
exp_018_qwen_scierc_seed456 | status=DONE | conclusion=success
exp_019_supervised_verifier | status=DONE | conclusion=killed
exp_freeform_ablation | status=DONE | conclusion=negative
ft_001 | status=DONE | conclusion=success
ft_002 | status=DONE | conclusion=killed
ft_002_v2 | status=DONE | conclusion=success
mvp_pilot_001 | status=DONE | conclusion=negative
mvp_pilot_002 | status=DONE | conclusion=failed
mvp_pilot_003 | status=DONE | conclusion=negative
mvp_pilot_004 | status=DONE | conclusion=negative
mvp_pilot_005 | status=DONE | conclusion=negative
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "3b54ca90-d232-47df-a698-a9919c8b6a2c",
  "tool_use_result": {
    "stdout": "e1_component_wise_re_sj | status=DONE | conclusion=negative\nexp001_seed123 | status=DONE | conclusion=killed\nexp001_seed456 | status=DONE | conclusion=killed\nexp008_re_n16 | status=DONE | conclusion=killed\nexp_001_n16_seed123 | status=DONE | conclusion=success\nexp_001_n16_seed123_full | status=DONE | conclusion=killed\nexp_001_n16_seed456 | status=DONE | conclusion=success\nexp_001_n16_seed456_full | status=DONE | conclusion=killed\nexp_001_ner_n16_scierc | status=DONE | conclusion=success\nexp_001_ner_n16_seed123 | status=DONE | conclusion=success\nexp_001_seed123_t10_full | status=DONE | conclusion=negative\nexp_001_seed123_v2 | status=DONE | conclusion=success\nexp_001_seed123_v2_r1024 | status=DONE | conclusion=killed\nexp_001_seed42_v2 | status=DONE | conclusion=success\nexp_001_seed42_v2_r1024 | status=DONE | conclusion=killed\nexp_001_seed456_t10_full | status=DONE | conclusion=negative\nexp_001_seed456_v2 | status=DONE | conclusion=negative\nexp_001_seed456_v2_ner | status=DONE | conclusion=success\nexp_001_seed456_v2_ner_r1024 | status=DONE | conclusion=killed\nexp_002 | status=DONE | conclusion=success\nexp_002_conll_n16 | status=DONE | conclusion=success\nexp_002_conll_n16_r1024 | status=DONE | conclusion=killed\nexp_002_merge_conll2003 | status=DONE | conclusion=killed\nexp_002_ner_conll2003 | status=DONE | conclusion=success\nexp_003_ner_wnut17 | status=DONE | conclusion=negative\nexp_003_wnut17_eval | status=DONE | conclusion=success\nexp_003_wnut17_v2 | status=DONE | conclusion=negative\nexp_004_re_diagnostic | status=DONE | conclusion=success\nexp_004_v2 | status=DONE | conclusion=success\nexp_005 | status=DONE | conclusion=success\nexp_005_v2 | status=DONE | conclusion=success\nexp_006_v2 | status=DONE | conclusion=negative\nexp_007_llama_inference | status=DONE | conclusion=success\nexp_007_llama_n16 | status=DONE | conclusion=success\nexp_007_llama_n16_r1024 | status=DONE | conclusion=killed\nexp_007_llama_seed123 | status=DONE | conclusion=negative\nexp_007_llama_seed456 | status=DONE | conclusion=negative\nexp_007_ner_llama | status=DONE | conclusion=killed\nexp_007_ner_multi_model | status=DONE | conclusion=success\nexp_008_re_n16 | status=DONE | conclusion=success\nexp_008_re_n16_full | status=DONE | conclusion=killed\nexp_008_re_n16_t10_full | status=DONE | conclusion=negative\nexp_008_re_n16_v2 | status=DONE | conclusion=negative\nexp_008_re_seed123 | status=DONE | conclusion=negative\nexp_009_capability_stratification | status=DONE | conclusion=success\nexp_009_v2 | status=DONE | conclusion=success\nexp_009_v2_re_rerun | status=DONE | conclusion=success\nexp_010_selection_curves | status=DONE | conclusion=success\nexp_011_ood_conll_to_scierc | status=DONE | conclusion=negative\nexp_011_ood_scierc_to_conll | status=DONE | conclusion=success\nexp_012_logprob_baseline | status=DONE | conclusion=success\nexp_012_rerun_1024 | status=DONE | conclusion=success\nexp_013_exact_match_voting | status=DONE | conclusion=negative\nexp_014_entity_majority_voting | status=DONE | conclusion=success\nexp_015_metrics_expansion | status=DONE | conclusion=success\nexp_015_v2 | status=DONE | conclusion=success\nexp_016_rerun_1024_bootstrap | status=DONE | conclusion=negative\nexp_016_signal_ensemble | status=DONE | conclusion=success\nexp_016_v2 | status=DONE | conclusion=success\nexp_017_llama_conll | status=DONE | conclusion=success\nexp_017_llama_conll_infer | status=DONE | conclusion=success\nexp_017_llama_conll_n16 | status=DONE | conclusion=success\nexp_017_llama_conll_n16_r1024 | status=DONE | conclusion=success\nexp_017_llama_conll_n16_s123 | status=DONE | conclusion=success\nexp_017_llama_conll_n16_s123_r1024 | status=DONE | conclusion=success\nexp_017_llama_conll_n16_s456 | status=DONE | conclusion=success\nexp_017_llama_conll_n16_s456_r1024 | status=DONE | conclusion=success\nexp_018_llama_scierc_seed123 | status=DONE | conclusion=success\nexp_018_llama_scierc_seed42_r1024 | status=DONE | conclusion=success\nexp_018_llama_scierc_seed456 | status=DONE | conclusion=killed\nexp_018_llama_scierc_seed456_r1024 | status=DONE | conclusion=success\nexp_018_qwen_scierc_seed123 | status=DONE | conclusion=success\nexp_018_qwen_scierc_seed456 | status=DONE | conclusion=success\nexp_019_supervised_verifier | status=DONE | conclusion=killed\nexp_freeform_ablation | status=DONE | conclusion=negative\nft_001 | status=DONE | conclusion=success\nft_002 | status=DONE | conclusion=killed\nft_002_v2 | status=DONE | conclusion=success\nmvp_pilot_001 | status=DONE | conclusion=negative\nmvp_pilot_002 | status=DONE | conclusion=failed\nmvp_pilot_003 | status=DONE | conclusion=negative\nmvp_pilot_004 | status=DONE | conclusion=negative\nmvp_pilot_005 | status=DONE | conclusion=negative",
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

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Now I need to get the detailed metrics from the key experiments. Let me extract the specific experiments that matter for the audit:

1. exp_012_rerun_1024 - Table 1 quality estimation (ρ and AUROC)
2. exp_016_rerun_1024_bootstrap - Table 2 selection F1 (wait, it's exp_016_rerun_1024_bootstrap? Let me check the task again - it says exp_016_rerun_1024)
3. exp_018_llama_scierc_seed42_r1024 - LLaMA data


4. exp_007_llama_inference / exp_007_ner_multi_model - old data
5. exp_011_ood_conll_to_scierc - OOD analysis
6. exp_019_supervised_verifier - should NOT appear

I'm noticing a discrepancy with exp_016 in the registry - it shows exp_016_rerun_1024_bootstrap rather than exp_016_rerun_1024, so I need to verify which one the task actually references. Now let me pull the metrics from these experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "758e73f3-121d-4ef3-8e26-dc6f979a183d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZDLJ6mWSzbKMdQ4B4JyiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4403,
      "cache_read_input_tokens": 57713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4403
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

Let me extract the key experiment data from the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "44a6474f-76ed-491c-a498-a0710ac39261",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZDLJ6mWSzbKMdQ4B4JyiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4403,
      "cache_read_input_tokens": 57713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4403
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

<details open><summary>🔧 Tool call — Bash · `toolu_01HWB6vc3yDnbv2ZKhnE399T`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7/tool-results/mcp-agent-ml-research-read_registry-1778849027754.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Key experiments to check\nkeys = ['exp_012_rerun_1024', 'exp_016_rerun_1024_bootstrap', 'exp_016_signal_ensemble', \n        'exp_018_llama_scierc_seed42_r1024', 'exp_018_llama_scierc_seed123',\n        'exp_018_llama_scierc_seed456_r1024',\n        'exp_011_ood_conll_to_scierc', 'exp_011_ood_scierc_to_conll',\n        'exp_019_supervised_verifier', 'exp_012_logprob_baseline',\n        'exp_007_llama_inference', 'exp_007_ner_multi_model',\n        'exp_freeform_ablation']\n\nfor k in keys:\n    if k in exps:\n        e = exps[k]\n        print(f'\\\\n=== {k} ===')\n        print(f'status: {e.get(\\\"status\\\")}')\n        print(f'conclusion: {e.get(\\\"conclusion\\\")}')\n        metrics = e.get('metrics', {})\n        if metrics:\n            print(f'metrics: {json.dumps(metrics, indent=2)[:3000]}')\n        else:\n            print('metrics: (none)')\n        notes = e.get('notes', '')\n        if notes:\n            print(f'notes: {str(notes)[:1000]}')\n    else:\n        print(f'\\\\n=== {k} === NOT FOUND')\n\" 2>&1 | head -400",
  "description": "Extract key experiment details from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "94cdeb8d-851a-4e55-82c5-cbc0fea6a6f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZDLJ6mWSzbKMdQ4B4JyiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4403,
      "cache_read_input_tokens": 57713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4403
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

_source line 48 · 2026-05-15T12:44:36.461Z_

<details><summary>↩ Tool result · `toolu_01HWB6vc3yDnbv2ZKhnE399T`</summary>

```text
=== exp_012_rerun_1024 ===
status: DONE
conclusion: success
metrics: {
  "ner_full": {
    "n": 529,
    "SJ": {
      "rho": 0.3599,
      "tau": 0.2646,
      "AUROC": 0.6917,
      "ECE": 0.4531,
      "rho_ci95": [
        0.2732,
        0.4389
      ],
      "AUROC_ci95": [
        0.6304,
        0.7406
      ]
    },
    "FK": {
      "rho": 0.2665,
      "tau": 0.1974,
      "AUROC": 0.629,
      "ECE": 0.4512,
      "rho_ci95": [
        0.1743,
        0.3486
      ],
      "AUROC_ci95": [
        0.5612,
        0.6882
      ]
    },
    "logprob": {
      "rho": 0.2052,
      "tau": 0.1478,
      "AUROC": 0.5783,
      "ECE": 0.7064,
      "rho_ci95": [
        0.1171,
        0.2904
      ],
      "AUROC_ci95": [
        0.5179,
        0.6387
      ]
    },
    "EM": {
      "rho": 0.2945,
      "tau": 0.2208,
      "AUROC": 0.7493,
      "ECE": 0.3526,
      "rho_ci95": [
        0.2094,
        0.37
      ],
      "AUROC_ci95": [
        0.7002,
        0.7928
      ]
    },
    "voting_conf": {
      "rho": 0.3792,
      "tau": 0.2805,
      "AUROC": 0.6841,
      "ECE": 0.3807,
      "rho_ci95": [
        0.2972,
        0.4486
      ],
      "AUROC_ci95": [
        0.6249,
        0.7366
      ]
    }
  },
  "ner_cond": {
    "n": 477,
    "SJ": {
      "rho": 0.3113,
      "tau": 0.2257,
      "AUROC": 0.6772,
      "ECE": 0.4416,
      "rho_ci95": [
        0.2353,
        0.3959
      ],
      "AUROC_ci95": [
        0.621,
        0.7337
      ]
    },
    "FK": {
      "rho": 0.1761,
      "tau": 0.1284,
      "AUROC": 0.6078,
      "ECE": 0.4389,
      "rho_ci95": [
        0.0839,
        0.2665
      ],
      "AUROC_ci95": [
        0.5442,
        0.6709
      ]
    },
    "logprob": {
      "rho": 0.1538,
      "tau": 0.1111,
      "AUROC": 0.5633,
      "ECE": 0.6803,
      "rho_ci95": [
        0.0637,
        0.2424
      ],
      "AUROC_ci95": [
        0.5032,
        0.6232
      ]
    },
    "EM": {
      "rho": 0.3596,
      "tau": 0.2735,
      "AUROC": 0.7556,
      "ECE": 0.3257,
      "rho_ci95": [
        0.2819,
        0.4408
      ],
      "AUROC_ci95": [
        0.7011,
        0.8107
      ]
    },
    "voting_conf": {
      "rho": 0.3,
      "tau": 0.2189,
      "AUROC": 0.6618,
      "ECE": 0.3746,
      "rho_ci95": [
        0.2168,
        0.3836
      ],
      "AUROC_ci95": [
        0.6004,
        0.7201
      ]
    }
  },
  "re_full": {
    "n": 397,
    "SJ": {
      "rho": 0.2503,
      "tau": 0.1878,
      "AUROC": 0.6702,
      "ECE": 0.3865
    },
    "FK": {
      "rho": 0.2752,
      "tau": 0.2117,
      "AUROC": 0.6089,
      "ECE": 0.4405
    },
    "logprob": {
      "rho": 0.2662,
      "tau": 0.1951,
      "AUROC": 0.6005,
      "ECE": 0.7694
    },
    "EM": {
      "rho": 0.1344,
      "tau": 0.1081,
      "AUROC": 0.7059,
      "ECE": 0.3548
    },
    "voting_conf": {
      "rho": 0.3498,
      "tau": 0.2663,
      "AUROC": 0.6935,
      "ECE": 0.2724
    }
  },
  "re_cond": {
    "n": 238,
    "SJ": {
      "rho": 0.2457,
      "tau": 0.1811,

=== exp_016_rerun_1024_bootstrap ===
status: DONE
conclusion: negative
metrics: {
  "bootstrap_ci_95": [
    -0.03,
    0.042
  ],
  "permutation_p": 0.39,
  "cohen_d": 0.038,
  "sign_test_win_rate": 0.466,
  "ner_logprob_vs_greedy_delta": 0.006,
  "conclusion_summary": "NER selection: no signal significantly outperforms greedy; RE: same conclusion"
}

=== exp_016_signal_ensemble ===
status: DONE
conclusion: success
metrics: {
  "sj_logprob_pearson_ner": 0.57,
  "sj_logprob_pearson_re": 0.42,
  "best_linear_ner": {
    "combo": "SJ+voting_conf",
    "alpha": 0.3,
    "rho": 0.489
  },
  "best_linear_re": {
    "combo": "voting_conf+logprob",
    "alpha": 0.6,
    "rho": 0.429
  },
  "ensemble_ner_auroc": 0.735,
  "ensemble_re_auroc": 0.719,
  "best_single_ner_auroc": 0.7,
  "best_single_re_auroc": 0.721,
  "ensemble_ner_delta": 0.035,
  "selection_f1_ner": {
    "greedy": 0.609,
    "logprob": 0.609,
    "sj": 0.604,
    "ensemble": 0.604,
    "voting": 0.596,
    "random": 0.58,
    "oracle": 0.769
  },
  "selection_f1_re": {
    "logprob": 0.397,
    "greedy": 0.374,
    "sj": 0.368,
    "ensemble": 0.367,
    "voting": 0.338,
    "random": 0.338,
    "oracle": 0.561
  },
  "diagnosis": "SJ+voting_conf linear combo boosts NER \u03c1 to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge."
}

=== exp_018_llama_scierc_seed42_r1024 ===
status: DONE
conclusion: success
metrics: {
  "ner": {
    "full": {
      "SJ": {
        "rho": 0.3096,
        "tau": 0.2288,
        "auroc": 0.6683
      },
      "FK": {
        "rho": 0.2352,
        "tau": 0.1759,
        "auroc": 0.6069
      },
      "logprob": {
        "rho": 0.1503,
        "tau": 0.1087,
        "auroc": 0.5318
      },
      "EM": {
        "rho": 0.2587,
        "tau": 0.1966,
        "auroc": 0.7174
      },
      "voting_conf": {
        "rho": 0.4053,
        "tau": 0.3042,
        "auroc": 0.6967
      }
    },
    "conditional": {
      "SJ": {
        "rho": 0.2718,
        "tau": null,
        "auroc": 0.6565
      },
      "FK": {
        "rho": 0.1472,
        "tau": null,
        "auroc": 0.5866
      },
      "logprob": {
        "rho": 0.081,
        "tau": null,
        "auroc": 0.5129
      },
      "EM": {
        "rho": 0.3165,
        "tau": null,
        "auroc": 0.7244
      },
      "voting_conf": {
        "rho": 0.3078,
        "tau": null,
        "auroc": 0.6714
      }
    },
    "greedy_f1": 0.6607,
    "oracle_f1": 0.7781,
    "n_full": 529,
    "n_cond": 478
  },
  "re": {
    "full": {
      "SJ": {
        "rho": 0.2748,
        "tau": 0.2102,
        "auroc": 0.7244
      },
      "FK": {
        "rho": 0.3027,
        "tau": 0.2337,
        "auroc": 0.691
      },
      "logprob": {
        "rho": 0.3163,
        "tau": 0.233,
        "auroc": 0.6313
      },
      "EM": {
        "rho": 0.1681,
        "tau": 0.1275,
        "auroc": 0.7697
      },
      "voting_conf": {
        "rho": 0.384,
        "tau": 0.2965,
        "auroc": 0.7337
      }
    },
    "conditional": {
      "SJ": {
        "rho": 0.3461,
        "tau": null,
        "auroc": 0.7233
      },
      "FK": {
        "rho": 0.1969,
        "tau": null,
        "auroc": 0.6684
      },
      "logprob": {
        "rho": 0.0888,
        "tau": null,
        "auroc": 0.5556
      },
      "EM": {
        "rho": 0.4969,
        "tau": null,
        "auroc": 0.819
      },
      "voting_conf": {
        "rho": 0.3433,
        "tau": null,
        "auroc": 0.7003
      }
    },
    "greedy_f1": 0.4319,
    "oracle_f1": 0.5775,
    "n_full": 397,
    "n_cond": 251
  }
}

=== exp_018_llama_scierc_seed123 ===
status: DONE
conclusion: success
metrics: (none)

=== exp_018_llama_scierc_seed456_r1024 ===
status: DONE
conclusion: success
metrics: {
  "ner_greedy_f1": 0.6597,
  "ner_oracle_f1": 0.7683,
  "ner_oracle_headroom": 0.1086,
  "ner_cond_rho_fk": 0.1472,
  "ner_cond_rho_sj": 0.2718,
  "ner_cond_rho_logprob": 0.083,
  "ner_logprob_auroc_cond": 0.5485,
  "re_greedy_f1": 0.4338,
  "re_oracle_f1": 0.5834,
  "re_oracle_headroom": 0.1496,
  "re_cond_rho_fk": 0.2107,
  "re_cond_rho_sj": 0.3898,
  "re_cond_rho_logprob": 0.1252,
  "re_logprob_auroc_cond": 0.6119,
  "ner_structural_beats_logprob": true,
  "re_structural_beats_logprob": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "df8cacf7-31c8-4c56-ac1d-cbffa150311e",
  "tool_use_result": {
    "stdout": "=== exp_012_rerun_1024 ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"ner_full\": {\n    \"n\": 529,\n    \"SJ\": {\n      \"rho\": 0.3599,\n      \"tau\": 0.2646,\n      \"AUROC\": 0.6917,\n      \"ECE\": 0.4531,\n      \"rho_ci95\": [\n        0.2732,\n        0.4389\n      ],\n      \"AUROC_ci95\": [\n        0.6304,\n        0.7406\n      ]\n    },\n    \"FK\": {\n      \"rho\": 0.2665,\n      \"tau\": 0.1974,\n      \"AUROC\": 0.629,\n      \"ECE\": 0.4512,\n      \"rho_ci95\": [\n        0.1743,\n        0.3486\n      ],\n      \"AUROC_ci95\": [\n        0.5612,\n        0.6882\n      ]\n    },\n    \"logprob\": {\n      \"rho\": 0.2052,\n      \"tau\": 0.1478,\n      \"AUROC\": 0.5783,\n      \"ECE\": 0.7064,\n      \"rho_ci95\": [\n        0.1171,\n        0.2904\n      ],\n      \"AUROC_ci95\": [\n        0.5179,\n        0.6387\n      ]\n    },\n    \"EM\": {\n      \"rho\": 0.2945,\n      \"tau\": 0.2208,\n      \"AUROC\": 0.7493,\n      \"ECE\": 0.3526,\n      \"rho_ci95\": [\n        0.2094,\n        0.37\n      ],\n      \"AUROC_ci95\": [\n        0.7002,\n        0.7928\n      ]\n    },\n    \"voting_conf\": {\n      \"rho\": 0.3792,\n      \"tau\": 0.2805,\n      \"AUROC\": 0.6841,\n      \"ECE\": 0.3807,\n      \"rho_ci95\": [\n        0.2972,\n        0.4486\n      ],\n      \"AUROC_ci95\": [\n        0.6249,\n        0.7366\n      ]\n    }\n  },\n  \"ner_cond\": {\n    \"n\": 477,\n    \"SJ\": {\n      \"rho\": 0.3113,\n      \"tau\": 0.2257,\n      \"AUROC\": 0.6772,\n      \"ECE\": 0.4416,\n      \"rho_ci95\": [\n        0.2353,\n        0.3959\n      ],\n      \"AUROC_ci95\": [\n        0.621,\n        0.7337\n      ]\n    },\n    \"FK\": {\n      \"rho\": 0.1761,\n      \"tau\": 0.1284,\n      \"AUROC\": 0.6078,\n      \"ECE\": 0.4389,\n      \"rho_ci95\": [\n        0.0839,\n        0.2665\n      ],\n      \"AUROC_ci95\": [\n        0.5442,\n        0.6709\n      ]\n    },\n    \"logprob\": {\n      \"rho\": 0.1538,\n      \"tau\": 0.1111,\n      \"AUROC\": 0.5633,\n      \"ECE\": 0.6803,\n      \"rho_ci95\": [\n        0.0637,\n        0.2424\n      ],\n      \"AUROC_ci95\": [\n        0.5032,\n        0.6232\n      ]\n    },\n    \"EM\": {\n      \"rho\": 0.3596,\n      \"tau\": 0.2735,\n      \"AUROC\": 0.7556,\n      \"ECE\": 0.3257,\n      \"rho_ci95\": [\n        0.2819,\n        0.4408\n      ],\n      \"AUROC_ci95\": [\n        0.7011,\n        0.8107\n      ]\n    },\n    \"voting_conf\": {\n      \"rho\": 0.3,\n      \"tau\": 0.2189,\n      \"AUROC\": 0.6618,\n      \"ECE\": 0.3746,\n      \"rho_ci95\": [\n        0.2168,\n        0.3836\n      ],\n      \"AUROC_ci95\": [\n        0.6004,\n        0.7201\n      ]\n    }\n  },\n  \"re_full\": {\n    \"n\": 397,\n    \"SJ\": {\n      \"rho\": 0.2503,\n      \"tau\": 0.1878,\n      \"AUROC\": 0.6702,\n      \"ECE\": 0.3865\n    },\n    \"FK\": {\n      \"rho\": 0.2752,\n      \"tau\": 0.2117,\n      \"AUROC\": 0.6089,\n      \"ECE\": 0.4405\n    },\n    \"logprob\": {\n      \"rho\": 0.2662,\n      \"tau\": 0.1951,\n      \"AUROC\": 0.6005,\n      \"ECE\": 0.7694\n    },\n    \"EM\": {\n      \"rho\": 0.1344,\n      \"tau\": 0.1081,\n      \"AUROC\": 0.7059,\n      \"ECE\": 0.3548\n    },\n    \"voting_conf\": {\n      \"rho\": 0.3498,\n      \"tau\": 0.2663,\n      \"AUROC\": 0.6935,\n      \"ECE\": 0.2724\n    }\n  },\n  \"re_cond\": {\n    \"n\": 238,\n    \"SJ\": {\n      \"rho\": 0.2457,\n      \"tau\": 0.1811,\n\n=== exp_016_rerun_1024_bootstrap ===\nstatus: DONE\nconclusion: negative\nmetrics: {\n  \"bootstrap_ci_95\": [\n    -0.03,\n    0.042\n  ],\n  \"permutation_p\": 0.39,\n  \"cohen_d\": 0.038,\n  \"sign_test_win_rate\": 0.466,\n  \"ner_logprob_vs_greedy_delta\": 0.006,\n  \"conclusion_summary\": \"NER selection: no signal significantly outperforms greedy; RE: same conclusion\"\n}\n\n=== exp_016_signal_ensemble ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"sj_logprob_pearson_ner\": 0.57,\n  \"sj_logprob_pearson_re\": 0.42,\n  \"best_linear_ner\": {\n    \"combo\": \"SJ+voting_conf\",\n    \"alpha\": 0.3,\n    \"rho\": 0.489\n  },\n  \"best_linear_re\": {\n    \"combo\": \"voting_conf+logprob\",\n    \"alpha\": 0.6,\n    \"rho\": 0.429\n  },\n  \"ensemble_ner_auroc\": 0.735,\n  \"ensemble_re_auroc\": 0.719,\n  \"best_single_ner_auroc\": 0.7,\n  \"best_single_re_auroc\": 0.721,\n  \"ensemble_ner_delta\": 0.035,\n  \"selection_f1_ner\": {\n    \"greedy\": 0.609,\n    \"logprob\": 0.609,\n    \"sj\": 0.604,\n    \"ensemble\": 0.604,\n    \"voting\": 0.596,\n    \"random\": 0.58,\n    \"oracle\": 0.769\n  },\n  \"selection_f1_re\": {\n    \"logprob\": 0.397,\n    \"greedy\": 0.374,\n    \"sj\": 0.368,\n    \"ensemble\": 0.367,\n    \"voting\": 0.338,\n    \"random\": 0.338,\n    \"oracle\": 0.561\n  },\n  \"diagnosis\": \"SJ+voting_conf linear combo boosts NER \\u03c1 to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge.\"\n}\n\n=== exp_018_llama_scierc_seed42_r1024 ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"ner\": {\n    \"full\": {\n      \"SJ\": {\n        \"rho\": 0.3096,\n        \"tau\": 0.2288,\n        \"auroc\": 0.6683\n      },\n      \"FK\": {\n        \"rho\": 0.2352,\n        \"tau\": 0.1759,\n        \"auroc\": 0.6069\n      },\n      \"logprob\": {\n        \"rho\": 0.1503,\n        \"tau\": 0.1087,\n        \"auroc\": 0.5318\n      },\n      \"EM\": {\n        \"rho\": 0.2587,\n        \"tau\": 0.1966,\n        \"auroc\": 0.7174\n      },\n      \"voting_conf\": {\n        \"rho\": 0.4053,\n        \"tau\": 0.3042,\n        \"auroc\": 0.6967\n      }\n    },\n    \"conditional\": {\n      \"SJ\": {\n        \"rho\": 0.2718,\n        \"tau\": null,\n        \"auroc\": 0.6565\n      },\n      \"FK\": {\n        \"rho\": 0.1472,\n        \"tau\": null,\n        \"auroc\": 0.5866\n      },\n      \"logprob\": {\n        \"rho\": 0.081,\n        \"tau\": null,\n        \"auroc\": 0.5129\n      },\n      \"EM\": {\n        \"rho\": 0.3165,\n        \"tau\": null,\n        \"auroc\": 0.7244\n      },\n      \"voting_conf\": {\n        \"rho\": 0.3078,\n        \"tau\": null,\n        \"auroc\": 0.6714\n      }\n    },\n    \"greedy_f1\": 0.6607,\n    \"oracle_f1\": 0.7781,\n    \"n_full\": 529,\n    \"n_cond\": 478\n  },\n  \"re\": {\n    \"full\": {\n      \"SJ\": {\n        \"rho\": 0.2748,\n        \"tau\": 0.2102,\n        \"auroc\": 0.7244\n      },\n      \"FK\": {\n        \"rho\": 0.3027,\n        \"tau\": 0.2337,\n        \"auroc\": 0.691\n      },\n      \"logprob\": {\n        \"rho\": 0.3163,\n        \"tau\": 0.233,\n        \"auroc\": 0.6313\n      },\n      \"EM\": {\n        \"rho\": 0.1681,\n        \"tau\": 0.1275,\n        \"auroc\": 0.7697\n      },\n      \"voting_conf\": {\n        \"rho\": 0.384,\n        \"tau\": 0.2965,\n        \"auroc\": 0.7337\n      }\n    },\n    \"conditional\": {\n      \"SJ\": {\n        \"rho\": 0.3461,\n        \"tau\": null,\n        \"auroc\": 0.7233\n      },\n      \"FK\": {\n        \"rho\": 0.1969,\n        \"tau\": null,\n        \"auroc\": 0.6684\n      },\n      \"logprob\": {\n        \"rho\": 0.0888,\n        \"tau\": null,\n        \"auroc\": 0.5556\n      },\n      \"EM\": {\n        \"rho\": 0.4969,\n        \"tau\": null,\n        \"auroc\": 0.819\n      },\n      \"voting_conf\": {\n        \"rho\": 0.3433,\n        \"tau\": null,\n        \"auroc\": 0.7003\n      }\n    },\n    \"greedy_f1\": 0.4319,\n    \"oracle_f1\": 0.5775,\n    \"n_full\": 397,\n    \"n_cond\": 251\n  }\n}\n\n=== exp_018_llama_scierc_seed123 ===\nstatus: DONE\nconclusion: success\nmetrics: (none)\n\n=== exp_018_llama_scierc_seed456_r1024 ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"ner_greedy_f1\": 0.6597,\n  \"ner_oracle_f1\": 0.7683,\n  \"ner_oracle_headroom\": 0.1086,\n  \"ner_cond_rho_fk\": 0.1472,\n  \"ner_cond_rho_sj\": 0.2718,\n  \"ner_cond_rho_logprob\": 0.083,\n  \"ner_logprob_auroc_cond\": 0.5485,\n  \"re_greedy_f1\": 0.4338,\n  \"re_oracle_f1\": 0.5834,\n  \"re_oracle_headroom\": 0.1496,\n  \"re_cond_rho_fk\": 0.2107,\n  \"re_cond_rho_sj\": 0.3898,\n  \"re_cond_rho_logprob\": 0.1252,\n  \"re_logprob_auroc_cond\": 0.6119,\n  \"ner_structural_beats_logprob\": true,\n  \"re_structural_beats_logprob\": true\n}",
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

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_0147z5ybTXTNacbC1P2Ty8vd`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7/tool-results/mcp-agent-ml-research-read_registry-1778849027754.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\nkeys = ['exp_011_ood_conll_to_scierc', 'exp_011_ood_scierc_to_conll',\n        'exp_019_supervised_verifier', 'exp_freeform_ablation',\n        'exp_002_ner_conll2003', 'exp_003_wnut17_v2', 'exp_003_ner_wnut17',\n        'exp_003_wnut17_eval',\n        'exp_007_llama_inference', 'exp_007_ner_multi_model',\n        'exp_017_llama_conll', 'exp_017_llama_conll_infer']\n\nfor k in keys:\n    if k in exps:\n        e = exps[k]\n        print(f'\\\\n=== {k} ===')\n        print(f'status: {e.get(\\\"status\\\")}')\n        print(f'conclusion: {e.get(\\\"conclusion\\\")}')\n        metrics = e.get('metrics', {})\n        if metrics:\n            print(f'metrics: {json.dumps(metrics, indent=2)[:2000]}')\n        else:\n            print('metrics: (none)')\n        notes = e.get('notes', '')\n        if notes:\n            print(f'notes: {str(notes)[:500]}')\n    else:\n        print(f'\\\\n=== {k} === NOT FOUND')\n\" 2>&1 | head -400",
  "description": "Extract more experiment details from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "3158e9ed-f87c-4952-aeda-eac15deca0e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyRnT84pzMjSLbsgyAn4GH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4590,
      "cache_read_input_tokens": 62116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4590
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

_source line 50 · 2026-05-15T12:44:47.530Z_

<details><summary>↩ Tool result · `toolu_0147z5ybTXTNacbC1P2Ty8vd`</summary>

```text
=== exp_011_ood_conll_to_scierc ===
status: DONE
conclusion: negative
metrics: {
  "greedy_ner_f1": 0.009,
  "greedy_re_f1": 0.001,
  "avg_structural_rho": -0.05,
  "verdict": "FAIL",
  "reason": "schema_incompatibility",
  "direction": "CoNLL_model_to_SciERC_data",
  "sample_f1_pct_zero_ner": 98.06,
  "rho_sj_ner": -0.186,
  "rho_fk_ner": -0.069,
  "note": "Schema incompatibility (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material) causes catastrophic failure. Cannot evaluate confidence signals."
}

=== exp_011_ood_scierc_to_conll ===
status: DONE
conclusion: success
metrics: {
  "greedy_ner_f1": 0.522,
  "rho_vc": 0.469,
  "rho_sj": 0.378,
  "rho_em": 0.3,
  "rho_fk": 0.285,
  "rho_lp": 0.246
}

=== exp_019_supervised_verifier ===
status: DONE
conclusion: killed
metrics: (none)
notes: Cancelled by Director: DDL risk too high (3-4 days for implementation+training+eval+paper), scope creep for analytical paper, free-form ablation already provides sufficient mechanistic evidence

=== exp_freeform_ablation ===
status: DONE
conclusion: negative
metrics: {
  "lp_std_ratio_free_vs_constrained": 0.97,
  "lp_range_ratio": 0.96,
  "tied_fraction_constrained": 0.597,
  "tied_fraction_freeform": 0.577,
  "ner_selection_gap_constrained": 0.0059,
  "ner_selection_gap_freeform": 0.0018,
  "re_selection_gap_constrained": -0.0068,
  "re_selection_gap_freeform": 0.0169,
  "parse_rate": 0.9995,
  "ner_vc_rho_constrained": 0.3792,
  "ner_vc_rho_freeform": 0.4089
}

=== exp_002_ner_conll2003 ===
status: DONE
conclusion: success
metrics: (none)

=== exp_003_wnut17_v2 ===
status: DONE
conclusion: negative
metrics: (none)

=== exp_003_ner_wnut17 ===
status: DONE
conclusion: negative
metrics: {
  "ner": {
    "greedy_f1": 0.525,
    "oracle_f1": 0.664,
    "headroom": 0.139,
    "rho_sj_full": 0.082,
    "rho_fk_full": 0.124,
    "rho_logprob_full": -0.414,
    "rho_sj_cond": 0.275,
    "rho_fk_cond": 0.164,
    "rho_logprob_cond": 0.352,
    "sj_beats_logprob_cond": false
  },
  "n_instances": 1287,
  "n_gold_empty": 598,
  "sample_f1_mean": 0.401,
  "sample_f1_pct_zero": 53.7,
  "N": 16,
  "T": 1,
  "seed": 42,
  "verdict": "FAIL",
  "verdict_note": ">30% samples F1=0; structural rho weak; logprob baseline stronger"
}

=== exp_003_wnut17_eval ===
status: DONE
conclusion: success
metrics: {
  "greedy_f1": 0.523,
  "oracle_f1": 0.664,
  "headroom": 0.141,
  "rho_fk": 0.125,
  "rho_sj": 0.089,
  "rho_fk_cond": 0.169,
  "rho_sj_cond": 0.288,
  "rho_logprob_full": -0.409,
  "rho_logprob_cond": 0.35,
  "structural_beats_surface": false,
  "sample_f1_pct_zero": 53.7,
  "n_instances": 1287,
  "N": 16,
  "T": 1,
  "seed": 42,
  "model": "Qwen3-8B",
  "n_gold_empty_filtered": 598,
  "verdict": "FAIL",
  "verdict_note": "structural_beats_surface=false; >50% samples F1=0"
}

=== exp_007_llama_inference ===
status: DONE
conclusion: success
metrics: {
  "ner": {
    "greedy_f1": 0.66,
    "oracle_f1": 0.781,
    "headroom": 0.121,
    "rho_fk": 0.327,
    "rho_sj": 0.363,
    "rho_fk_cond": 0.226,
    "rho_sj_cond": 0.311,
    "rho_logprob": 0.183,
    "rho_logprob_cond": 0.109,
    "structural_beats_surface": true,
    "sample_f1_pct_zero": 11.6
  },
  "re": {
    "greedy_f1": 0.434,
    "oracle_f1": 0.568,
    "headroom": 0.135,
    "rho_fk": 0.305,
    "rho_sj": 0.299,
    "rho_fk_cond": 0.259,
    "rho_sj_cond": 0.405,
    "rho_logprob": 0.288,
    "rho_logprob_cond": 0.092,
    "structural_beats_surface": false,
    "sample_f1_pct_zero": 41.2
  },
  "n_instances": 551,
  "N": 8,
  "T": 1,
  "seed": 42,
  "model": "LLaMA-3.1-8B-Instruct",
  "verdict": "FAIL",
  "verdict_note": "RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0"
}

=== exp_007_ner_multi_model ===
status: DONE
conclusion: success
metrics: {
  "epoch": 5,
  "train_loss": 0.0767,
  "eval_loss": 0.1049,
  "train_runtime_sec": 1494.5,
  "train_samples_per_second": 6.226,
  "checkpoints": [
    "checkpoint-400",
    "checkpoint-500",
    "checkpoint-585"
  ],
  "base_model": "Meta-Llama-3.1-8B-Instruct",
  "lora_r": 32,
  "lora_alpha": 64,
  "note": "EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal. Checkpoint fully intact."
}

=== exp_017_llama_conll ===
status: DONE
conclusion: success
metrics: (none)

=== exp_017_llama_conll_infer ===
status: DONE
conclusion: success
metrics: {
  "greedy_f1": 0.9266,
  "oracle_f1": 0.9443,
  "oracle_headroom": 0.0177,
  "n_instances": 3453,
  "n_valid": 2756,
  "n_conditional": 2642,
  "N": 8,
  "full": {
    "SJ_rho": 0.4314,
    "FK_rho": 0.4277,
    "logprob_rho": 0.3072,
    "EM_rho": 0.4306,
    "voting_conf_rho": 0.4256,
    "SJ_AUROC": 0.7039,
    "FK_AUROC": 0.7026,
    "logprob_AUROC": 0.761,
    "EM_AUROC": 0.7046,
    "voting_conf_AUROC": 0.7088,
    "SJ_ECE": 0.1137,
    "FK_ECE": 0.1053,
    "logprob_ECE": 0.129,
    "EM_ECE": 0.1094,
    "voting_conf_ECE": 0.0949
  },
  "conditional": {
    "SJ_rho": 0.4356,
    "FK_rho": 0.431,
    "logprob_rho": 0.3282,
    "EM_rho": 0.4403,
    "voting_conf_rho": 0.3743,
    "SJ_AUROC": 0.7225,
    "FK_AUROC": 0.7208,
    "logprob_AUROC": 0.8102,
    "EM_AUROC": 0.7257,
    "voting_conf_AUROC": 0.6989,
    "SJ_ECE": 0.0829,
    "FK_ECE": 0.0796,
    "logprob_ECE": 0.0922,
    "EM_ECE": 0.0754,
    "voting_conf_ECE": 0.0784
  }
}
notes: LLaMA CoNLL-2003 NER N=8 (not N=16, cost constraint: 3453 test instances). SJ ρ=0.431 > logprob ρ=0.307 (Δ=+0.124). ρ-AUROC dissociation: logprob AUROC=0.761 > SJ AUROC=0.704. All 4 structural signals ρ>0.42 vs logprob 0.31. Directly comparable to exp_002 (Qwen CoNLL N=8) and exp_007 (LLaMA SciERC N=8).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "74bf5209-ac0d-4459-abcf-5a77faf136a9",
  "tool_use_result": {
    "stdout": "=== exp_011_ood_conll_to_scierc ===\nstatus: DONE\nconclusion: negative\nmetrics: {\n  \"greedy_ner_f1\": 0.009,\n  \"greedy_re_f1\": 0.001,\n  \"avg_structural_rho\": -0.05,\n  \"verdict\": \"FAIL\",\n  \"reason\": \"schema_incompatibility\",\n  \"direction\": \"CoNLL_model_to_SciERC_data\",\n  \"sample_f1_pct_zero_ner\": 98.06,\n  \"rho_sj_ner\": -0.186,\n  \"rho_fk_ner\": -0.069,\n  \"note\": \"Schema incompatibility (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material) causes catastrophic failure. Cannot evaluate confidence signals.\"\n}\n\n=== exp_011_ood_scierc_to_conll ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"greedy_ner_f1\": 0.522,\n  \"rho_vc\": 0.469,\n  \"rho_sj\": 0.378,\n  \"rho_em\": 0.3,\n  \"rho_fk\": 0.285,\n  \"rho_lp\": 0.246\n}\n\n=== exp_019_supervised_verifier ===\nstatus: DONE\nconclusion: killed\nmetrics: (none)\nnotes: Cancelled by Director: DDL risk too high (3-4 days for implementation+training+eval+paper), scope creep for analytical paper, free-form ablation already provides sufficient mechanistic evidence\n\n=== exp_freeform_ablation ===\nstatus: DONE\nconclusion: negative\nmetrics: {\n  \"lp_std_ratio_free_vs_constrained\": 0.97,\n  \"lp_range_ratio\": 0.96,\n  \"tied_fraction_constrained\": 0.597,\n  \"tied_fraction_freeform\": 0.577,\n  \"ner_selection_gap_constrained\": 0.0059,\n  \"ner_selection_gap_freeform\": 0.0018,\n  \"re_selection_gap_constrained\": -0.0068,\n  \"re_selection_gap_freeform\": 0.0169,\n  \"parse_rate\": 0.9995,\n  \"ner_vc_rho_constrained\": 0.3792,\n  \"ner_vc_rho_freeform\": 0.4089\n}\n\n=== exp_002_ner_conll2003 ===\nstatus: DONE\nconclusion: success\nmetrics: (none)\n\n=== exp_003_wnut17_v2 ===\nstatus: DONE\nconclusion: negative\nmetrics: (none)\n\n=== exp_003_ner_wnut17 ===\nstatus: DONE\nconclusion: negative\nmetrics: {\n  \"ner\": {\n    \"greedy_f1\": 0.525,\n    \"oracle_f1\": 0.664,\n    \"headroom\": 0.139,\n    \"rho_sj_full\": 0.082,\n    \"rho_fk_full\": 0.124,\n    \"rho_logprob_full\": -0.414,\n    \"rho_sj_cond\": 0.275,\n    \"rho_fk_cond\": 0.164,\n    \"rho_logprob_cond\": 0.352,\n    \"sj_beats_logprob_cond\": false\n  },\n  \"n_instances\": 1287,\n  \"n_gold_empty\": 598,\n  \"sample_f1_mean\": 0.401,\n  \"sample_f1_pct_zero\": 53.7,\n  \"N\": 16,\n  \"T\": 1,\n  \"seed\": 42,\n  \"verdict\": \"FAIL\",\n  \"verdict_note\": \">30% samples F1=0; structural rho weak; logprob baseline stronger\"\n}\n\n=== exp_003_wnut17_eval ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"greedy_f1\": 0.523,\n  \"oracle_f1\": 0.664,\n  \"headroom\": 0.141,\n  \"rho_fk\": 0.125,\n  \"rho_sj\": 0.089,\n  \"rho_fk_cond\": 0.169,\n  \"rho_sj_cond\": 0.288,\n  \"rho_logprob_full\": -0.409,\n  \"rho_logprob_cond\": 0.35,\n  \"structural_beats_surface\": false,\n  \"sample_f1_pct_zero\": 53.7,\n  \"n_instances\": 1287,\n  \"N\": 16,\n  \"T\": 1,\n  \"seed\": 42,\n  \"model\": \"Qwen3-8B\",\n  \"n_gold_empty_filtered\": 598,\n  \"verdict\": \"FAIL\",\n  \"verdict_note\": \"structural_beats_surface=false; >50% samples F1=0\"\n}\n\n=== exp_007_llama_inference ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"ner\": {\n    \"greedy_f1\": 0.66,\n    \"oracle_f1\": 0.781,\n    \"headroom\": 0.121,\n    \"rho_fk\": 0.327,\n    \"rho_sj\": 0.363,\n    \"rho_fk_cond\": 0.226,\n    \"rho_sj_cond\": 0.311,\n    \"rho_logprob\": 0.183,\n    \"rho_logprob_cond\": 0.109,\n    \"structural_beats_surface\": true,\n    \"sample_f1_pct_zero\": 11.6\n  },\n  \"re\": {\n    \"greedy_f1\": 0.434,\n    \"oracle_f1\": 0.568,\n    \"headroom\": 0.135,\n    \"rho_fk\": 0.305,\n    \"rho_sj\": 0.299,\n    \"rho_fk_cond\": 0.259,\n    \"rho_sj_cond\": 0.405,\n    \"rho_logprob\": 0.288,\n    \"rho_logprob_cond\": 0.092,\n    \"structural_beats_surface\": false,\n    \"sample_f1_pct_zero\": 41.2\n  },\n  \"n_instances\": 551,\n  \"N\": 8,\n  \"T\": 1,\n  \"seed\": 42,\n  \"model\": \"LLaMA-3.1-8B-Instruct\",\n  \"verdict\": \"FAIL\",\n  \"verdict_note\": \"RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\"\n}\n\n=== exp_007_ner_multi_model ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"epoch\": 5,\n  \"train_loss\": 0.0767,\n  \"eval_loss\": 0.1049,\n  \"train_runtime_sec\": 1494.5,\n  \"train_samples_per_second\": 6.226,\n  \"checkpoints\": [\n    \"checkpoint-400\",\n    \"checkpoint-500\",\n    \"checkpoint-585\"\n  ],\n  \"base_model\": \"Meta-Llama-3.1-8B-Instruct\",\n  \"lora_r\": 32,\n  \"lora_alpha\": 64,\n  \"note\": \"EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal. Checkpoint fully intact.\"\n}\n\n=== exp_017_llama_conll ===\nstatus: DONE\nconclusion: success\nmetrics: (none)\n\n=== exp_017_llama_conll_infer ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"greedy_f1\": 0.9266,\n  \"oracle_f1\": 0.9443,\n  \"oracle_headroom\": 0.0177,\n  \"n_instances\": 3453,\n  \"n_valid\": 2756,\n  \"n_conditional\": 2642,\n  \"N\": 8,\n  \"full\": {\n    \"SJ_rho\": 0.4314,\n    \"FK_rho\": 0.4277,\n    \"logprob_rho\": 0.3072,\n    \"EM_rho\": 0.4306,\n    \"voting_conf_rho\": 0.4256,\n    \"SJ_AUROC\": 0.7039,\n    \"FK_AUROC\": 0.7026,\n    \"logprob_AUROC\": 0.761,\n    \"EM_AUROC\": 0.7046,\n    \"voting_conf_AUROC\": 0.7088,\n    \"SJ_ECE\": 0.1137,\n    \"FK_ECE\": 0.1053,\n    \"logprob_ECE\": 0.129,\n    \"EM_ECE\": 0.1094,\n    \"voting_conf_ECE\": 0.0949\n  },\n  \"conditional\": {\n    \"SJ_rho\": 0.4356,\n    \"FK_rho\": 0.431,\n    \"logprob_rho\": 0.3282,\n    \"EM_rho\": 0.4403,\n    \"voting_conf_rho\": 0.3743,\n    \"SJ_AUROC\": 0.7225,\n    \"FK_AUROC\": 0.7208,\n    \"logprob_AUROC\": 0.8102,\n    \"EM_AUROC\": 0.7257,\n    \"voting_conf_AUROC\": 0.6989,\n    \"SJ_ECE\": 0.0829,\n    \"FK_ECE\": 0.0796,\n    \"logprob_ECE\": 0.0922,\n    \"EM_ECE\": 0.0754,\n    \"voting_conf_ECE\": 0.0784\n  }\n}\nnotes: LLaMA CoNLL-2003 NER N=8 (not N=16, cost constraint: 3453 test instances). SJ ρ=0.431 > logprob ρ=0.307 (Δ=+0.124). ρ-AUROC dissociation: logprob AUROC=0.761 > SJ AUROC=0.704. All 4 structural signals ρ>0.42 vs logprob 0.31. Directly comparable to exp_002 (Qwen CoNLL N=8) and exp_007 (LLaMA SciERC N=8).",
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

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Now let me also get the CoNLL Qwen data and look at the selection data more carefully. Let me also get the WNUT table values and selection exp data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "007bef5f-9679-4efd-ac30-a683b4d8c409",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01412U9pXjWyeJM9SxNGxDJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3362,
      "cache_read_input_tokens": 66706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3362
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

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_011qxdLHX34oQyRotc3R3qvd`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7/tool-results/mcp-agent-ml-research-read_registry-1778849027754.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\nkeys = ['exp_002', 'exp_005', 'exp_005_v2', 'exp_010_selection_curves',\n        'exp_015_metrics_expansion', 'exp_015_v2', 'exp_016_v2',\n        'exp_014_entity_majority_voting',\n        'exp_018_qwen_scierc_seed123', 'exp_018_qwen_scierc_seed456']\n\nfor k in keys:\n    if k in exps:\n        e = exps[k]\n        print(f'\\\\n=== {k} ===')\n        print(f'status: {e.get(\\\"status\\\")}')\n        print(f'conclusion: {e.get(\\\"conclusion\\\")}')\n        metrics = e.get('metrics', {})\n        if metrics:\n            print(f'metrics: {json.dumps(metrics, indent=2)[:2000]}')\n        else:\n            print('metrics: (none)')\n    else:\n        print(f'\\\\n=== {k} === NOT FOUND')\n\" 2>&1 | head -400",
  "description": "Extract Qwen CoNLL and selection experiment data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "11548570-7373-4dad-bfd6-2fbc3ae91811",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01412U9pXjWyeJM9SxNGxDJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3362,
      "cache_read_input_tokens": 66706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3362
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

_source line 53 · 2026-05-15T12:44:55.709Z_

<details><summary>↩ Tool result · `toolu_011qxdLHX34oQyRotc3R3qvd`</summary>

```text
=== exp_002 ===
status: DONE
conclusion: success
metrics: {
  "sj_rho_full": 0.4357,
  "sj_tau_full": 0.3851,
  "sj_auroc_full": 0.8008,
  "sj_rho_cond": 0.4511,
  "fk_rho_full": 0.3998,
  "fk_tau_full": 0.3568,
  "fk_auroc_full": 0.7741,
  "fk_rho_cond": 0.4064,
  "logprob_rho_full": 0.3157,
  "logprob_tau_full": 0.2469,
  "logprob_auroc_full": 0.7532,
  "logprob_rho_cond": 0.3562,
  "em_rho_full": 0.4507,
  "em_tau_full": 0.4002,
  "em_auroc_full": 0.8156,
  "em_rho_cond": 0.4799,
  "ev_rho_full": 0.4237,
  "ev_tau_full": 0.3777,
  "ev_auroc_full": 0.7889,
  "ev_rho_cond": 0.4127,
  "greedy_f1": 0.9123,
  "oracle_f1": 0.9543,
  "voting_f1": 0.9141,
  "oracle_headroom": 0.042,
  "sj_vs_logprob_delta_rho": 0.12,
  "sj_vs_logprob_ci_low": 0.0881,
  "sj_vs_logprob_ci_high": 0.154,
  "sj_vs_logprob_significant": true,
  "n_instances": 3453,
  "n_valid": 2756,
  "n_samples": 8,
  "temperature": 1
}

=== exp_005 ===
status: DONE
conclusion: success
metrics: (none)

=== exp_005_v2 ===
status: DONE
conclusion: success
metrics: (none)

=== exp_010_selection_curves ===
status: DONE
conclusion: success
metrics: {
  "scierc_ner": {
    "n_instances": 551,
    "greedy_f1": 0.618,
    "N16": {
      "oracle": 0.787,
      "SJ": 0.62,
      "FK": 0.621,
      "logprob": 0.621,
      "voting_conf": 0.585,
      "EM": 0.606,
      "random": 0.595
    },
    "N8": {
      "oracle": 0.752,
      "SJ": 0.614,
      "FK": 0.614,
      "logprob": 0.619,
      "voting_conf": 0.591,
      "EM": 0.603,
      "random": 0.589
    },
    "N4": {
      "oracle": 0.714,
      "SJ": 0.607,
      "FK": 0.608,
      "logprob": 0.616,
      "voting_conf": 0.594,
      "EM": 0.6,
      "random": 0.587
    }
  },
  "scierc_re": {
    "n_instances": 397,
    "greedy_f1": 0.403,
    "N16": {
      "oracle": 0.631,
      "SJ": 0.397,
      "FK": 0.396,
      "logprob": 0.41,
      "voting_conf": 0.408,
      "EM": 0.381,
      "random": 0.364
    },
    "N8": {
      "oracle": 0.583,
      "SJ": 0.393,
      "FK": 0.394,
      "logprob": 0.413,
      "voting_conf": 0.398,
      "EM": 0.381,
      "random": 0.363
    }
  },
  "conll_ner": {
    "n_instances": 3453,
    "greedy_f1": 0.725,
    "N8": {
      "oracle": 0.757,
      "SJ": 0.718,
      "FK": 0.717,
      "logprob": 0.716,
      "voting_conf": 0.714,
      "EM": 0.716,
      "random": 0.69
    },
    "N4": {
      "oracle": 0.746,
      "SJ": 0.714,
      "FK": 0.714,
      "logprob": 0.715,
      "voting_conf": 0.714,
      "EM": 0.712,
      "random": 0.692
    }
  }
}

=== exp_015_metrics_expansion ===
status: DONE
conclusion: success
metrics: {
  "data_source": "exp_012_logprob/samples_with_logprobs.jsonl",
  "config": "N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2",
  "ner": {
    "n_valid": 529,
    "n_cond": 501,
    "voting_rho_full": 0.5018,
    "voting_rho_cond": 0.4497,
    "voting_auroc": 0.7279,
    "voting_tau": 0.3766,
    "sj_rho_full": 0.3565,
    "sj_rho_cond": 0.412,
    "sj_auroc": 0.6656,
    "sj_tau": 0.2658,
    "em_rho_full": 0.2566,
    "em_rho_cond": 0.3427,
    "em_auroc": 0.623,
    "em_tau": 0.1924,
    "fk_rho_full": 0.2651,
    "fk_rho_cond": 0.306,
    "fk_auroc": 0.6243,
    "fk_tau": 0.2027,
    "logprob_rho_full": 0.1396,
    "logprob_rho_cond": 0.1627,
    "logprob_auroc": 0.5585,
    "logprob_tau": 0.1006
  },
  "re": {
    "n_valid": 397,
    "n_cond": 296,
    "voting_rho_full": 0.4217,
    "voting_rho_cond": 0.463,
    "voting_auroc": 0.7162,
    "voting_tau": 0.327,
    "sj_rho_full": 0.2112,
    "sj_rho_cond": 0.3683,
    "sj_auroc": 0.5816,
    "sj_tau": 0.1619,
    "em_rho_full": 0.1002,
    "em_rho_cond": 0.3607,
    "em_auroc": 0.5036,
    "em_tau": 0.0839,
    "fk_rho_full": 0.2528,
    "fk_rho_cond": 0.3168,
    "fk_auroc": 0.6308,
    "fk_tau": 0.1967,
    "logprob_rho_full": 0.2467,
    "logprob_rho_cond": 0.1457,
    "logprob_auroc": 0.6354,
    "logprob_tau": 0.1808
  },
  "diagnosis": "Unified 5-signal evaluation on single data source. Voting leads NER full (\u03c1=0.502), SJ retains strength in NER cond (\u03c1=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond."
}

=== exp_015_v2 ===
status: DONE
conclusion: success
metrics: {
  "scierc_ner_avg": {
    "sj_auroc": 0.7394,
    "fk_auroc": 0.6172,
    "em_auroc": 0.7873,
    "voting_auroc": 0.7367,
    "logprob_auroc": 0.5918
  },
  "scierc_re_avg": {
    "sj_auroc": 0.6746,
    "fk_auroc": 0.5939,
    "em_auroc": 0.715,
    "voting_auroc": 0.7234,
    "logprob_auroc": 0.5849
  }
}

=== exp_016_v2 ===
status: DONE
conclusion: success
metrics: {
  "ner_conditional": {
    "n": 529,
    "best_single_signal_rho": {
      "soft_jaccard": 0.4412
    },
    "best_combo_rho": {
      "sj+vc_a0.55": 0.4552
    },
    "ensemble_auroc": 0.7141,
    "best_single_auroc": {
      "soft_jaccard": 0.7166
    },
    "selection_f1": {
      "greedy": 0.6442,
      "logprob_best": 0.6505,
      "ensemble_best": 0.6475,
      "sj_best": 0.6471,
      "oracle": 0.8442
    }
  },
  "re_conditional": {
    "n": 397,
    "best_single_signal_rho": {
      "voting_confidence": 0.3849
    },
    "best_combo_rho": {
      "logprob+vc_a0.25": 0.3936
    },
    "ensemble_auroc": 0.6916,
    "best_single_auroc": {
      "voting_confidence": 0.7023
    },
    "selection_f1": {
      "greedy": 0.403,
      "logprob_best": 0.4097,
      "ensemble_best": 0.4227,
      "oracle": 0.6306
    }
  },
  "re_full": {
    "ensemble_auroc": 0.8608,
    "best_single_auroc": {
      "voting_confidence": 0.8248
    }
  }
}

=== exp_014_entity_majority_voting ===
status: DONE
conclusion: success
metrics: {
  "ner_full_rho": 0.3915,
  "ner_full_p": 8.1e-21,
  "ner_full_tau": 0.2906,
  "ner_full_auroc": 0.7039,
  "re_full_rho": 0.3403,
  "re_full_p": 3.21e-12,
  "re_full_tau": 0.256,
  "re_full_auroc": 0.6668,
  "ner_voting_f1": 0.6246,
  "ner_greedy_f1": 0.6483,
  "ner_oracle_f1": 0.7793,
  "re_voting_f1": 0.3577,
  "re_greedy_f1": 0.4022,
  "re_oracle_f1": 0.5886,
  "diagnosis": "Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE (0.340 vs 0.244). But voting as selection strategy LOSES to greedy."
}

=== exp_018_qwen_scierc_seed123 ===
status: DONE
conclusion: success
metrics: (none)

=== exp_018_qwen_scierc_seed456 ===
status: DONE
conclusion: success
metrics: (none)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "aef98466-1b4b-4236-b47a-5f8835cba6a5",
  "tool_use_result": {
    "stdout": "=== exp_002 ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"sj_rho_full\": 0.4357,\n  \"sj_tau_full\": 0.3851,\n  \"sj_auroc_full\": 0.8008,\n  \"sj_rho_cond\": 0.4511,\n  \"fk_rho_full\": 0.3998,\n  \"fk_tau_full\": 0.3568,\n  \"fk_auroc_full\": 0.7741,\n  \"fk_rho_cond\": 0.4064,\n  \"logprob_rho_full\": 0.3157,\n  \"logprob_tau_full\": 0.2469,\n  \"logprob_auroc_full\": 0.7532,\n  \"logprob_rho_cond\": 0.3562,\n  \"em_rho_full\": 0.4507,\n  \"em_tau_full\": 0.4002,\n  \"em_auroc_full\": 0.8156,\n  \"em_rho_cond\": 0.4799,\n  \"ev_rho_full\": 0.4237,\n  \"ev_tau_full\": 0.3777,\n  \"ev_auroc_full\": 0.7889,\n  \"ev_rho_cond\": 0.4127,\n  \"greedy_f1\": 0.9123,\n  \"oracle_f1\": 0.9543,\n  \"voting_f1\": 0.9141,\n  \"oracle_headroom\": 0.042,\n  \"sj_vs_logprob_delta_rho\": 0.12,\n  \"sj_vs_logprob_ci_low\": 0.0881,\n  \"sj_vs_logprob_ci_high\": 0.154,\n  \"sj_vs_logprob_significant\": true,\n  \"n_instances\": 3453,\n  \"n_valid\": 2756,\n  \"n_samples\": 8,\n  \"temperature\": 1\n}\n\n=== exp_005 ===\nstatus: DONE\nconclusion: success\nmetrics: (none)\n\n=== exp_005_v2 ===\nstatus: DONE\nconclusion: success\nmetrics: (none)\n\n=== exp_010_selection_curves ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"scierc_ner\": {\n    \"n_instances\": 551,\n    \"greedy_f1\": 0.618,\n    \"N16\": {\n      \"oracle\": 0.787,\n      \"SJ\": 0.62,\n      \"FK\": 0.621,\n      \"logprob\": 0.621,\n      \"voting_conf\": 0.585,\n      \"EM\": 0.606,\n      \"random\": 0.595\n    },\n    \"N8\": {\n      \"oracle\": 0.752,\n      \"SJ\": 0.614,\n      \"FK\": 0.614,\n      \"logprob\": 0.619,\n      \"voting_conf\": 0.591,\n      \"EM\": 0.603,\n      \"random\": 0.589\n    },\n    \"N4\": {\n      \"oracle\": 0.714,\n      \"SJ\": 0.607,\n      \"FK\": 0.608,\n      \"logprob\": 0.616,\n      \"voting_conf\": 0.594,\n      \"EM\": 0.6,\n      \"random\": 0.587\n    }\n  },\n  \"scierc_re\": {\n    \"n_instances\": 397,\n    \"greedy_f1\": 0.403,\n    \"N16\": {\n      \"oracle\": 0.631,\n      \"SJ\": 0.397,\n      \"FK\": 0.396,\n      \"logprob\": 0.41,\n      \"voting_conf\": 0.408,\n      \"EM\": 0.381,\n      \"random\": 0.364\n    },\n    \"N8\": {\n      \"oracle\": 0.583,\n      \"SJ\": 0.393,\n      \"FK\": 0.394,\n      \"logprob\": 0.413,\n      \"voting_conf\": 0.398,\n      \"EM\": 0.381,\n      \"random\": 0.363\n    }\n  },\n  \"conll_ner\": {\n    \"n_instances\": 3453,\n    \"greedy_f1\": 0.725,\n    \"N8\": {\n      \"oracle\": 0.757,\n      \"SJ\": 0.718,\n      \"FK\": 0.717,\n      \"logprob\": 0.716,\n      \"voting_conf\": 0.714,\n      \"EM\": 0.716,\n      \"random\": 0.69\n    },\n    \"N4\": {\n      \"oracle\": 0.746,\n      \"SJ\": 0.714,\n      \"FK\": 0.714,\n      \"logprob\": 0.715,\n      \"voting_conf\": 0.714,\n      \"EM\": 0.712,\n      \"random\": 0.692\n    }\n  }\n}\n\n=== exp_015_metrics_expansion ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"data_source\": \"exp_012_logprob/samples_with_logprobs.jsonl\",\n  \"config\": \"N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\",\n  \"ner\": {\n    \"n_valid\": 529,\n    \"n_cond\": 501,\n    \"voting_rho_full\": 0.5018,\n    \"voting_rho_cond\": 0.4497,\n    \"voting_auroc\": 0.7279,\n    \"voting_tau\": 0.3766,\n    \"sj_rho_full\": 0.3565,\n    \"sj_rho_cond\": 0.412,\n    \"sj_auroc\": 0.6656,\n    \"sj_tau\": 0.2658,\n    \"em_rho_full\": 0.2566,\n    \"em_rho_cond\": 0.3427,\n    \"em_auroc\": 0.623,\n    \"em_tau\": 0.1924,\n    \"fk_rho_full\": 0.2651,\n    \"fk_rho_cond\": 0.306,\n    \"fk_auroc\": 0.6243,\n    \"fk_tau\": 0.2027,\n    \"logprob_rho_full\": 0.1396,\n    \"logprob_rho_cond\": 0.1627,\n    \"logprob_auroc\": 0.5585,\n    \"logprob_tau\": 0.1006\n  },\n  \"re\": {\n    \"n_valid\": 397,\n    \"n_cond\": 296,\n    \"voting_rho_full\": 0.4217,\n    \"voting_rho_cond\": 0.463,\n    \"voting_auroc\": 0.7162,\n    \"voting_tau\": 0.327,\n    \"sj_rho_full\": 0.2112,\n    \"sj_rho_cond\": 0.3683,\n    \"sj_auroc\": 0.5816,\n    \"sj_tau\": 0.1619,\n    \"em_rho_full\": 0.1002,\n    \"em_rho_cond\": 0.3607,\n    \"em_auroc\": 0.5036,\n    \"em_tau\": 0.0839,\n    \"fk_rho_full\": 0.2528,\n    \"fk_rho_cond\": 0.3168,\n    \"fk_auroc\": 0.6308,\n    \"fk_tau\": 0.1967,\n    \"logprob_rho_full\": 0.2467,\n    \"logprob_rho_cond\": 0.1457,\n    \"logprob_auroc\": 0.6354,\n    \"logprob_tau\": 0.1808\n  },\n  \"diagnosis\": \"Unified 5-signal evaluation on single data source. Voting leads NER full (\\u03c1=0.502), SJ retains strength in NER cond (\\u03c1=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond.\"\n}\n\n=== exp_015_v2 ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"scierc_ner_avg\": {\n    \"sj_auroc\": 0.7394,\n    \"fk_auroc\": 0.6172,\n    \"em_auroc\": 0.7873,\n    \"voting_auroc\": 0.7367,\n    \"logprob_auroc\": 0.5918\n  },\n  \"scierc_re_avg\": {\n    \"sj_auroc\": 0.6746,\n    \"fk_auroc\": 0.5939,\n    \"em_auroc\": 0.715,\n    \"voting_auroc\": 0.7234,\n    \"logprob_auroc\": 0.5849\n  }\n}\n\n=== exp_016_v2 ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"ner_conditional\": {\n    \"n\": 529,\n    \"best_single_signal_rho\": {\n      \"soft_jaccard\": 0.4412\n    },\n    \"best_combo_rho\": {\n      \"sj+vc_a0.55\": 0.4552\n    },\n    \"ensemble_auroc\": 0.7141,\n    \"best_single_auroc\": {\n      \"soft_jaccard\": 0.7166\n    },\n    \"selection_f1\": {\n      \"greedy\": 0.6442,\n      \"logprob_best\": 0.6505,\n      \"ensemble_best\": 0.6475,\n      \"sj_best\": 0.6471,\n      \"oracle\": 0.8442\n    }\n  },\n  \"re_conditional\": {\n    \"n\": 397,\n    \"best_single_signal_rho\": {\n      \"voting_confidence\": 0.3849\n    },\n    \"best_combo_rho\": {\n      \"logprob+vc_a0.25\": 0.3936\n    },\n    \"ensemble_auroc\": 0.6916,\n    \"best_single_auroc\": {\n      \"voting_confidence\": 0.7023\n    },\n    \"selection_f1\": {\n      \"greedy\": 0.403,\n      \"logprob_best\": 0.4097,\n      \"ensemble_best\": 0.4227,\n      \"oracle\": 0.6306\n    }\n  },\n  \"re_full\": {\n    \"ensemble_auroc\": 0.8608,\n    \"best_single_auroc\": {\n      \"voting_confidence\": 0.8248\n    }\n  }\n}\n\n=== exp_014_entity_majority_voting ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"ner_full_rho\": 0.3915,\n  \"ner_full_p\": 8.1e-21,\n  \"ner_full_tau\": 0.2906,\n  \"ner_full_auroc\": 0.7039,\n  \"re_full_rho\": 0.3403,\n  \"re_full_p\": 3.21e-12,\n  \"re_full_tau\": 0.256,\n  \"re_full_auroc\": 0.6668,\n  \"ner_voting_f1\": 0.6246,\n  \"ner_greedy_f1\": 0.6483,\n  \"ner_oracle_f1\": 0.7793,\n  \"re_voting_f1\": 0.3577,\n  \"re_greedy_f1\": 0.4022,\n  \"re_oracle_f1\": 0.5886,\n  \"diagnosis\": \"Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\"\n}\n\n=== exp_018_qwen_scierc_seed123 ===\nstatus: DONE\nconclusion: success\nmetrics: (none)\n\n=== exp_018_qwen_scierc_seed456 ===\nstatus: DONE\nconclusion: success\nmetrics: (none)",
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

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
Now let me also get the selection F1 data. I see Table 2 in the paper references exp_016 data. Let me also look for the WNUT N=8 data. Let me check the specific data points mentioned in the paper:

Now let me carefully compare the numbers in the paper versus the registry:

**Table 1 (Quality Estimation) — Should match exp_012_rerun_1024:**

Paper Table 1 values:
| Signal | SciERC NER ρ | SciERC NER AUC | SciERC RE ρ | SciERC RE AUC | CoNLL Qwen ρ | CoNLL Qwen AUC | CoNLL LLaMA ρ | CoNLL LLaMA AUC |


|--------|-------------|----------------|------------|--------------|-------------|----------------|-------------|-----------------|
| VC     | .379        | .684           | .350       | .693         | .424        | .789           | .426        | .709            |
| SJ     | .360        | .692           | .250       | .670         | .436        | .801           | .431        | .704            |
| FK     | .267        | .629           | .275       | .609         | .400        | .774           | .428        | .703            |
| EM     | .295        | .749           | .134       | .706         | .451        |                |             |                 |

Generating markdown table... Now I'm verifying the rounded values from the paper against the registry results—checking that the reported metrics align with what was actually computed for both NER and RE tasks across different models like VC, SJ, and FK. I'm noticing a rounding discrepancy with the VC AUC metric for SciERC RE—the registry shows 0.6935 which should round to .694, but the paper reports .693, suggesting it might have been truncated rather than rounded. I'll flag this minor inconsistency and continue checking the remaining metrics.

Now I'm verifying the other datasets: SJ, FK, EM, and LP all match between paper and registry values, though LP AUC shows another borderline case where 0.6005 could round to either .600 or .601 depending on the rounding convention used. Moving on to the CoNLL results from the Qwen experiment, where I'm comparing the SJ and SJ AUC metrics against the registry values.

Continuing through the CoNLL metrics, FK through LP all check out correctly, with FK AUC at .774, EM at .451 and .816 for AUC, LP at .316 and .753 for AUC. The VC metric is starting to come through but appears to be cut off. I'm finishing up the EM metrics and confirming all the LLaMA CoNLL results match the paper values. Now I need to move on to Table 2 and verify the Selection F1 scores, though there's a discrepancy in which experiment the paper references. Looking at the registry data more carefully, I'm noticing a significant discrepancy between the paper's reported oracle NER score of 0.776 and what exp_016_v2 shows at 0.8442. The greedy scores align well (0.6442 rounds to 0.644), but this oracle gap is puzzling—it might be due to different filtering thresholds or dataset sizes between experiments.

I'm checking other experiments to find the source of the paper's numbers. exp_014 with entity majority voting gives greedy=0.6483 and oracle=0.7793, which is closer to the paper's oracle but still doesn't match exactly. exp_010_selection_curves shows even lower greedy performance at 0.618, so that's not it either.

Looking at exp_016_rerun_1024_bootstrap for NER selection, the results are interesting—logprob doesn't significantly outperform greedy with a p-value of 0.39 and a very small effect size (cohen_d=0.038). The delta between logprob and greedy is 0.006, which matches what the paper reports, and the confidence interval of [-0.03, 0.042] aligns with the statistical insignificance.

But I'm noticing a mismatch: the task asks about exp_016_rerun_1024, yet the registry only has exp_016_rerun_1024_bootstrap. The bootstrap experiment contains the statistical tests but not the individual selection F1 scores for each signal—those numbers might be stored elsewhere or derived from a different analysis.

Let me trace through the paper's reported values more carefully. The text gives me specific F1 scores and point differences that I can verify: on NER, LP achieves 0.650 with a +0.6 pp improvement over greedy's 0.644, and on RE, LP reaches 0.395 while greedy is at 0.404, which the paper reports as −0.9 pp.

Now I'm checking these against the experimental data. Looking at the LLaMA cross-selection results, I notice the greedy F1 score in the registry shows 0.6607 for the SciERC experiment, but the paper's table lists it as 0.646. That's a meaningful gap—0.661 rounded would be closer to the registry value, not 0.646. Let me verify which experiment corresponds to which result, since I'm seeing different values across exp_007 and exp_018. The oracle score matches (.778), but the greedy baseline is throwing me off—the registry shows .661 while the paper reports .646. I'm wondering if the greedy_f1 in the registry is computed differently than the paper's "Greedy (T=0)" baseline, possibly due to how gold-empty instances are handled during filtering. I'm noticing the greedy F1 values don't match between my experiments and the paper—exp_018 shows 0.6607 for LLaMA but the paper reports 0.646, which is a meaningful discrepancy. The oracle value of 0.7781 does match the paper's 0.778, so something specific about the greedy computation seems off, possibly due to different inference setups or how the greedy baseline was calculated. Looking at the Qwen SciERC results in Table 2, the greedy F1 of 0.644 matches exp_016_v2's registry value, which is good. For exp_016_rerun_1024_bootstrap, I can see the bootstrap confidence intervals and statistical tests are there, but the individual F1 scores per signal aren't recorded in those metrics. Now I'm wondering if the LLaMA greedy F1 discrepancy might be due to different evaluation sets or computation methods — maybe the 0.661 value was calculated on a different subset than what appears in the paper. I'm noticing the greedy F1 scores don't quite line up across different sources—0.66 from one inference run, 0.6607 from another, but the paper reports 0.646 for LLaMA on SciERC. These could stem from different model variants or separate T=0 inference runs that weren't fully captured in the registry. Rather than chase down each discrepancy, I should focus on finding clear, verifiable mismatches. Now let me examine the hard constraints, starting with exp_012.

I need to verify whether exp_012_logprob_baseline used max_tokens=512, since the paper should be using exp_012_rerun_1024 instead. I've already confirmed Table 1 matches exp_012_rerun_1024, but exp_015_metrics_expansion references the old exp_012 data directly, and its voting results don't align with what's published—exp_015 shows voting_rho_full NER at 0.5018 while the paper reports a different value.

Let me cross-check the actual numbers the paper uses. The paper's Table 1 VC NER rho of 0.379 matches exp_012_rerun_1024's 0.3792, not exp_015's 0.5018, and the SJ NER rho of 0.360 matches exp_012_rerun_1024's 0.3599, confirming the paper is pulling from the correct rerun dataset.

Now for the LLaMA results, the paper's Table 1 CoNLL LLaMA SJ rho of 0.431 aligns with exp_017_llama_conll_infer's value of 0.4314. But the LLaMA SciERC numbers appear in the multi-seed robustness table instead, where the mean VC NER is listed as 0.384±0.014, though exp_018_llama_scierc_seed42_r1024 shows a VC NER of 0.4053 — there's a discrepancy I need to investigate.

Looking at the math, if seed42 alone is 0.405 and the three-seed mean is 0.384, the other two seeds would need to average around 0.37 to bring the mean down, which seems plausible but I can't verify without seeing all the individual seed values.

Now checking the selection results claim—the paper reports p=0.39 for the selection F1 comparison and explicitly states this is not significant, which matches what I'm seeing in the text. Let me search through to confirm they never claim selection significantly outperforms anything.

The paper correctly frames this as a null result across the board: "none significantly improves sample selection," "No signal significantly outperforms greedy in any configuration," and "this is not significant (p=0.39)." There is a conditional analysis showing LP outperforms greedy in the non-tied subset (p=0.01), but that's properly scoped as a secondary finding, not the main claim.

For the OOD value of 0.335, I'm not finding it anywhere in the paper. And for the exp_011 analysis, I'm looking at what the appendix actually says about the cross-dataset OOD results. SciERC has 6 entity types and 7 relation types, which matches what the paper describes. Now I'm checking the paper's title—it says "Do Not Scale" rather than "Cannot Scale," which aligns with what the task specifies. The core narrative centers on the universal correlation-selection gap, and the paper supports this with a controlled ablation showing the compression is intrinsic to the model and task itself, not an artifact of the decoding approach. Let me search through the paper to verify whether exp-019 appears in the results.

The paper mentions trained verifiers only as future work in the discussion and conclusion sections, not as presented experimental results. For the claims and evidence check, the paper appropriately qualifies its findings as "consistent across two model families at 8B scale" and notes the relation extraction results are "preliminary, single benchmark" with appropriate caveats about dataset limitations. Now I'm examining the WNUT table values in the appendix...

Generating markdown table... I'm noticing a potential discrepancy between what the paper reports and what the experimental data shows. The paper states N=8 for the WNUT dataset, but both the exp_003_ner_wnut17 and exp_003_wnut17_eval experiments show N=16 instead. I don't see any N=8 WNUT experiments in the registry, so I need to figure out where this mismatch is coming from.

The instance counts do match up correctly—the paper reports n=689 after filtering, and the experimental data shows n_instances=1287 with n_gold_empty_filtered=598, which gives n_valid≈689. The correlation values also check out: rho_sj=0.089, rho_fk=0.125, and rho_logprob_full=-0.409 all align with the paper's reported numbers. But the N parameter discrepancy remains unresolved—either there's a separate N=8 analysis not in the registry, the paper incorrectly states N=8 when it should be N=16, or the N=8 data was subsampled from N=16. I'm noticing a critical discrepancy: the paper's table caption specifies N=8 for the primary experiments, but the registry only contains N=16 data for WNUT. It's possible an N=8 analysis was done separately through post-processing, but that's not documented anywhere. I'll flag this as a warning and move on to spot-checking some of the inline numbers from the paper.

Most of the reported metrics check out when rounded appropriately—the correlation coefficient, AUROC, tied instance percentage, and permutation p-value all align with registry values. However, I'm running into issues with a couple of claims: the "+2.9 pp improvement with p=0.01" for the non-tied subset isn't directly available in the registry and would require separate analysis, and the "52% zero F1" claim for WNUT appears to be conflating sample-level statistics (the registry shows 53.7% at the sample level) with what might be a different aggregation.

Actually, let me recalculate the WNUT zero F1 claim more carefully. If the paper says 52% of instances have zero F1, and the appendix table shows 689 valid instances after filtering out 598 gold-empty cases from the original 1287, then 52% of 689 would be roughly 358 instances with zero F1, leaving about 334 with non-zero F1. The paper's WNUT table reports a conditional n of 334, which matches this calculation—so 355/689 ≈ 51.5%, which rounds to 52%. That checks out.

Now I'm verifying the oracle headroom numbers: NER shows a 13.2 percentage point gap between oracle (0.776) and greedy (0.644), and RE shows an 18.1 pp gap between oracle (0.585) and greedy (0.404). Both align with what the paper claims.

For the correlation values in the introduction, the conditional VC correlation of ρ=0.038 for WNUT matches the paper's table, and the LP correlation of ρ=−0.410 is consistent with the registry values of −0.409 or −0.414. The OOD comparison shows VC correlation of 0.469 for the out-of-domain SCIERC-to-CONLL experiment versus 0.386 in-domain, which I can confirm from the registry.

But there's a discrepancy I'm noticing: the OOD table lists in-domain VC as 0.386, yet Table 1 shows the SCIERC NER VC as 0.379. These should match if they're measuring the same model on the same data, so either the OOD analysis used different seeds or different filtering criteria than the main table. Qwen NER VC mean = .386±.019. So the in-domain .386 is the 3-seed mean, not the single seed42 value (.379).

This is potentially confusing: the OOD table's "in-domain" column uses 3-seed mean (.386) but the OOD actual values are from a single seed. This inconsistency should be flagged.

Actually, looking at the OOD table more carefully:
- VC OOD: .469 (from exp_011_ood_scierc_to_conll, single run)
- VC In-dom.: .386

If in-domain is the 3-seed mean, that's comparing a single-run OOD with a 3-seed mean in-domain. This should be compared against the same seed/N for a fair comparison. The single seed42 in-domain VC is .379 (from Table 1 / exp_012_rerun_1024).

But the OOD table footnote references Table 1 for the in-domain values, which shows VC NER = .379, not .386. Looking at the actual OOD table values versus Table 1's SciERC NER results, there's a systematic mismatch across all signals—the in-domain numbers in the OOD table are consistently higher than what appears in Table 1. I'm realizing the OOD table's in-domain values actually come from the multi-seed results in Table 5, not from Table 1 as the footnote claims—this is a reference mismatch where the citation points to the wrong table. The WNUT table confirms VC conditional at ρ=.038 with p=.487, matching the text. Now checking the documentation standards—RE results are consistently labeled as preliminary and single-benchmark across captions and conclusions, p-values follow a uniform format, and confidence intervals use the same notation. I can't fully verify the LaTeX references without compiling, but the label-ref pairs appear structurally sound. Checking the appendix table numbering—LaTeX should handle this automatically if the document compiles correctly. I'm also verifying some specific statistics from the experiments: the paper mentions 11-18% identical outputs across samples and 39-43% unique outputs, which matches what I'm seeing in the registry diversity table for both Qwen and LLaMA on SciERC.

The F1 standard deviations check out too—Qwen shows 0.144 and LLaMA shows 0.11, fitting the reported range of 0.11-0.14. I can see the mean pairwise SJ of 0.703 comes from the experimental data, and the 42% pairwise exact-match rate is documented in Table 2's caption. For the LP selection performance, Greedy achieves 0.644 while LP reaches 0.650, confirming the +0.6 percentage point improvement. Now I need to verify whether this is measured on the same filter set as the other results.

Looking at the OOD discussion, the VC correlation of 0.469 for OOD versus 0.386 in-domain matches the registry values, though the in-domain figure uses a multi-seed average rather than the single-seed value from Table 1. For the freeform ablation, I'm checking the LP variance claims about the within-instance standard deviation ratio and tied fraction changes.

Now I'm verifying the selection gap numbers across both conditions—NER gains are indeed minimal in freeform (0.18 pp) compared to constrained (0.59 pp), while RE shows a striking reversal from a 0.68 pp loss under constraints to a 1.69 pp gain in freeform, all matching the registry values.

Looking at the appendix Panel B for the freeform ablation, I notice the absolute NER performance values differ noticeably from Table 2—the greedy and LP-selected scores are lower (0.618 and 0.624 versus 0.644 and 0.650), though the selection gaps themselves align correctly.

Since both use n=529 instances, the discrepancy likely stems from how the greedy baseline is computed or evaluated differently between the two experiments, rather than different instance sets. The absolute values are diverging significantly—LP scores of 0.624 versus 0.650—which shouldn't happen if both experiments used the same data and selection method. This could indicate the freeform ablation is pulling from a different experiment run, possibly one with different token limits, which would be a serious constraint violation. I need to trace back the data source for the freeform ablation to verify whether it's actually using the correct baseline experiment. prob/samples_with_logprobs.jsonl" — this is from the old exp_012. And the freeform ablation likely uses its own data. Let me check the registry:

exp_freeform_ablation: ner_vc_rho_constrained=0.3792, ner_vc_rho_freeform=0.4089

The constrained VC rho = 0.3792 matches exp_012_rerun_1024's VC rho = 0.3792 exactly. So the constrained baseline in the freeform ablation uses exp_012_rerun_1024 data. ✓

But then why do the selection F1 values differ? The issue is that Table 2's "Greedy" refers to T=0 inference (separate run with temperature 0), while the freeform ablation's "Greedy" baseline is likely the first sample or random selection from the T=1.0 distribution, which explains the discrepancy between 0.6182 and 0.644. 0.0059 is essentially the same gap, so the difference in absolute F1 scores between the two analyses likely stems from different instance sets or LP computation parameters in the freeform ablation. Looking at the QE signal quality metrics in Panel C, they match Table 1 exactly, suggesting the same underlying data, but the selection F1 in Panel B diverges from Table 2—which makes me think the "Greedy" baseline in the freeform ablation might not be the T=0 inference result.

Comparing the numbers more carefully: Table 2 shows Random NER F1 of 0.608, while the freeform ablation's "Greedy" is 0.618, so these clearly aren't the same thing. The selection gap itself is consistent across both (~0.6 percentage points for NER), but the baseline definitions appear to differ—the freeform ablation seems to be comparing LP-selected versus random within T=1.0 samples, whereas Table 2 uses T=0 greedy as a separate baseline. I'll flag this discrepancy and move forward rather than get stuck on the terminology mismatch.

Now I need to check what other important details I should verify, particularly around the data coverage in different tables and whether certain instances like empty-gold cases are being handled consistently across comparisons.

Looking at Table 1, I see it only shows SciERC results for Qwen, while LLaMA's SciERC performance appears in the multi-seed robustness tables instead. Let me cross-reference the LLaMA SciERC values from Table 5 against the registry data to make sure they're consistent.

Checking the seed42 results against the reported means, I notice some interesting patterns—the VC score for seed42 is actually higher than the mean, which makes sense given the standard deviation, but for SJ the seed42 value is lower than the mean, suggesting the other seeds performed better on that metric.

I'm trying to verify the multi-seed numbers by working backwards from the reported means, but I'm running into incomplete data in the registry. For seed456, I can only find the conditional NER scores, not the full metrics I need. Let me look at what the paper reports for the Qwen multi-seed results and see if I can cross-check those against the registry entries.

Comparing the paper's reported means against seed42's individual values, I notice FK is notably higher in seed42 (0.267) than the reported mean (0.254), which suggests the other seeds must average lower to balance that out. The differences are within the reported standard deviations, so this seems plausible, though I'd need the actual seed456 and seed789 values to fully verify.

Now I'm spot-checking the inline numbers from the paper against the experimental results. The introduction claims VC reaches ρ up to 0.38 and EM achieves AUROC up to 0.75—both of which match my seed42 values when rounded. I'm also verifying the claim about 60% of instances being effectively tied in the constrained setting, which aligns with the ablation experiment data.

For the non-tied subset analysis showing LP outperforms greedy by 2.9 percentage points with p=0.01, those numbers aren't directly in the registry, so I'd need to rely on the analysis scripts to confirm them. The related work section mentions strong quality estimation coexisting with selection failure, and the ρ=0.38 figure checks out.

Looking at the free-form discussion, the selection gap values are in the registry—constrained shows -0.68 pp and free-form shows +1.69 pp. But the win/loss ratio shift from 36:59 to 45:45 and the Jaccard similarity of 0.472 between the two non-tied sets aren't in the registry either. Now I'm checking the OOD table values...

Generating markdown table... I've found a critical discrepancy: the OOD table's caption claims to use in-domain values from Table 1, but the actual numbers match Table 5's multi-seed means instead. The values in the OOD table (.386, .364, .307, .254, .217) align perfectly with Table 5, not Table 1 (.379, .360, .295, .267, .205), so the footnote attribution is incorrect.

Beyond the mislabeling, there's a methodological inconsistency—the OOD results themselves come from a single run while the "in-domain" baseline uses 3-seed averages, making the delta calculations incomparable. When I recalculate using the actual Table 1 values, the deltas shift noticeably (for example, VC becomes +.090 instead of the reported +.083), revealing that the reported improvements are based on mismatched baselines.

Most critically, EM's delta flips sign entirely—it should be +.005 with the correct in-domain reference, not -.007 as reported, which could alter the paper's claims about which signals improve OOD performance.

I'm now checking whether exp_019 appears in the paper's results or if it's only mentioned as future work in the literature citations, which would be acceptable.

The discussion also references VC's ρ=0.469 OOD versus 0.386 in-domain, but that 0.386 comes from the multi-seed mean rather than Table 1's .379, propagating the same reference inconsistency throughout.

For the SJ N=16 convergence claim about comparable NER performance with VC and lower cross-seed variance, the multi-seed data confirms σ=0.010 vs 0.026, which matches what's stated.

Now I'm checking the specific performance deltas: SJ N=16 shows 0.4105 versus VC's 0.4092, giving a difference of about 0.0013, which rounds to the claimed 0.002. The Qwen SciERC improvement of +0.047 also checks out from the n-scaling table, though I still need to verify the LLaMA +0.016 claim separately. Let me also cross-check the ECE values mentioned in the paper.

I'm noticing a major discrepancy with the calibration metrics—the paper claims NER signals have ECE values between 0.069 and 0.096, but the registry data shows much higher values ranging from 0.35 to 0.70. These can't be measuring the same thing, so the paper must be using a different definition of calibration ECE than what's stored in the registry. I see the distinction now—the registry's ECE measures how well confidence predicts F1 scores, while the paper's calibration ECE from reliability diagrams measures how well confidence aligns with observed performance within bins. These are fundamentally different metrics, so the discrepancy isn't necessarily problematic. Let me verify the paper title says "Do Not" rather than "Cannot," and check whether "0.335" actually appears in the text.

Now I'm compiling my findings and organizing them by severity. I've identified a critical issue with Table 9 in the appendix—it references Table 1 for in-domain values but actually pulls from the multi-seed means table, causing all the in-domain numbers and deltas to be incorrect. The EM delta even flips sign from +.005 to -.007. I also found some warnings: the WNUT table caption claims N=8 but the registry only shows N=16 experiments, and there's a discrepancy with the RE AUC value for VC in Table 1.

Looking at the remaining discrepancies, most are minor rounding issues—the VC and LP AUC values are off by just one digit in the last decimal place, and the LP full-set ρ for WNUT doesn't exactly match either registry entry. The OOD CoNLL→SciERC FK value is also a minor rounding difference. I'm verifying that the Qwen SciERC values in Table 1 align with the appropriate experiment run after rounding, and checking the CoNLL values as well.

Now I'm confirming that all the major results trace back to their corresponding experiments—the CoNLL LLaMA values, bootstrap statistics, freeform ablation metrics, and OOD SciERC→CoNLL correlations all check out. The paper uses the correct phrasing in the title, flags RE results appropriately as preliminary, and correctly describes the selection results as a null finding. I'm also noting that exp_019 doesn't appear in the paper, the hard constraint B4 value isn't found, and exp_011 for the OOD CoNLL→SciERC direction is properly characterized.

Now I'm digging into the Table 2 oracle values more carefully—the paper reports NER at 0.776 and RE at 0.585, but when I check exp_016_v2, those numbers don't match at all. The discrepancy is significant enough that I need to figure out which experiment actually produced the official Table 2 values, since exp_016_v2 has different sample sizes and substantially different oracle scores. The oracle values differ significantly across experiments—Table 2's NER oracle (0.776) is closest to exp_014's value (0.7793), while the RE oracle (0.585) aligns most with exp_010 (0.583)—suggesting the variation stems from different evaluation methodologies or which instances are included in each computation. Since Table 2 explicitly excludes empty gold annotations, the oracle depends heavily on the dataset subset being evaluated, but this still doesn't clarify which methodology is actually being used.

Looking at the registry experiments more carefully, the LLaMA experiment (exp_018) gives an oracle of 0.7781, which is close to Table 2's 0.776, but Table 2 is supposed to be for Qwen, not LLaMA, so that doesn't match either. The bootstrap experiments in the registry contain aggregate statistics but not the individual F1 values per signal, which suggests the Table 2 values likely come from a separate analysis script that isn't fully captured in the registry.

I have what I need to write the report now, but let me also verify that the paper isn't pulling data from the older exp_012_logprob_baseline experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "abd1c349-ee48-452d-9ae1-25ef6e9a249e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZnjeDsoQvCQjq1HdmDHTb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3771,
      "cache_read_input_tokens": 70068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3771
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

_source line 55_

Let me check a few more specific data points and the old exp_012 to verify constraint B1.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "96f417ee-f614-4957-be1c-c08dcb745789",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZnjeDsoQvCQjq1HdmDHTb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3771,
      "cache_read_input_tokens": 70068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3771
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

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_01KJ4QbiMDocaBBSL758txns`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7/tool-results/mcp-agent-ml-research-read_registry-1778849027754.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\nkeys = ['exp_012_logprob_baseline']\n\nfor k in keys:\n    if k in exps:\n        e = exps[k]\n        print(f'\\\\n=== {k} ===')\n        print(f'status: {e.get(\\\"status\\\")}')\n        print(f'conclusion: {e.get(\\\"conclusion\\\")}')\n        metrics = e.get('metrics', {})\n        if metrics:\n            print(f'metrics: {json.dumps(metrics, indent=2)[:3000]}')\n        else:\n            print('metrics: (none)')\n        notes = e.get('notes', '')\n        if notes:\n            print(f'notes: {str(notes)[:500]}')\n        spec = e.get('spec', {})\n        if spec:\n            cmd = spec.get('command', '')\n            print(f'command: {cmd[:500]}')\n\" 2>&1",
  "description": "Check old exp_012 details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "68123e3e-ac55-4708-b34a-31b2600db7cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZnjeDsoQvCQjq1HdmDHTb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3771,
      "cache_read_input_tokens": 70068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3771
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

_source line 57 · 2026-05-15T12:50:52.333Z_

<details><summary>↩ Tool result · `toolu_01KJ4QbiMDocaBBSL758txns`</summary>

```text
=== exp_012_logprob_baseline ===
status: DONE
conclusion: success
metrics: {
  "ner_full_rho_sj": 0.3565,
  "ner_full_rho_fk": 0.2651,
  "ner_full_rho_logprob": 0.1396,
  "ner_full_rho_greedy_logprob": 0.1615,
  "ner_full_tau_sj": 0.2658,
  "ner_full_tau_logprob": 0.1006,
  "ner_full_auroc_sj": 0.6892,
  "ner_full_auroc_fk": 0.6292,
  "ner_full_auroc_logprob": 0.5907,
  "ner_full_n": 529,
  "ner_sj_vs_logprob_delta": 0.2169,
  "re_full_rho_sj": 0.2112,
  "re_full_rho_fk": 0.2528,
  "re_full_rho_logprob": 0.2467,
  "re_full_auroc_sj": 0.5916,
  "re_full_auroc_fk": 0.6262,
  "re_full_auroc_logprob": 0.6186,
  "re_full_n": 397,
  "re_cond_rho_sj": 0.3683,
  "re_cond_rho_fk": 0.3168,
  "re_cond_rho_logprob": 0.1457,
  "re_cond_auroc_sj": 0.6839,
  "re_cond_auroc_logprob": 0.5487,
  "re_cond_n": 296,
  "diagnosis": "NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead. RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED."
}
command: python3 code/extract_logprobs.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "6feda143-9f05-4fa4-8987-fceca20886ce",
  "tool_use_result": {
    "stdout": "=== exp_012_logprob_baseline ===\nstatus: DONE\nconclusion: success\nmetrics: {\n  \"ner_full_rho_sj\": 0.3565,\n  \"ner_full_rho_fk\": 0.2651,\n  \"ner_full_rho_logprob\": 0.1396,\n  \"ner_full_rho_greedy_logprob\": 0.1615,\n  \"ner_full_tau_sj\": 0.2658,\n  \"ner_full_tau_logprob\": 0.1006,\n  \"ner_full_auroc_sj\": 0.6892,\n  \"ner_full_auroc_fk\": 0.6292,\n  \"ner_full_auroc_logprob\": 0.5907,\n  \"ner_full_n\": 529,\n  \"ner_sj_vs_logprob_delta\": 0.2169,\n  \"re_full_rho_sj\": 0.2112,\n  \"re_full_rho_fk\": 0.2528,\n  \"re_full_rho_logprob\": 0.2467,\n  \"re_full_auroc_sj\": 0.5916,\n  \"re_full_auroc_fk\": 0.6262,\n  \"re_full_auroc_logprob\": 0.6186,\n  \"re_full_n\": 397,\n  \"re_cond_rho_sj\": 0.3683,\n  \"re_cond_rho_fk\": 0.3168,\n  \"re_cond_rho_logprob\": 0.1457,\n  \"re_cond_auroc_sj\": 0.6839,\n  \"re_cond_auroc_logprob\": 0.5487,\n  \"re_cond_n\": 296,\n  \"diagnosis\": \"NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead. RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.\"\n}\ncommand: python3 code/extract_logprobs.py",
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

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I can see that exp_012_logprob_baseline has different values from exp_012_rerun_1024:

exp_012_logprob_baseline (old, max_tokens=512):
- NER SJ ρ = 0.3565, LP ρ = 0.1396
- RE SJ ρ = 0.2112, LP ρ = 0.2467

exp_012_rerun_1024:
- NER SJ ρ = 0.3599, LP ρ = 0.2052


- RE SJ ρ = 0.2503, LP ρ = 0.2662

The paper's Table 1 values match the rerun data exactly, confirming that's what was used. The LP ρ for NER shifted notably from 0.1396 to 0.2052, which is a meaningful difference. Now I need to check if the paper makes any claims about WNUT N=8 that might contradict what I'm seeing.

The WNUT table caption specifies N=8, but the only registered experiments I can find are N=16. There could be an unregistered N=8 run or the data might have been subsampled, but this discrepancy between the caption and the registry is worth flagging. I'm trying to figure out if the paper's WNUT values could plausibly come from taking just the first 8 samples of the N=16 data, but that would produce different results.

Actually, looking more closely at the specific metrics: the paper's values for SJ ρ, FK ρ, and LP ρ match the N=16 registry values almost exactly, which suggests the paper used the full N=16 data despite what the caption says. But I'm noticing that VC doesn't appear in either of the registered WNUT experiments at all, even though the table shows VC=.724. I need to check whether VC is actually present in the registry data or if it's missing entirely. The registry only shows N=16 WNUT runs, so either the N=8 analysis was done separately outside the registry, or the paper used the first 8 samples from the N=16 data. The fact that SJ and FK values match exactly between paper and registry is suspicious—with N=8 you'd have 28 pairwise comparisons versus 120 with N=16, so the statistics should differ noticeably if they were actually computed from different sample sizes.

Though I should consider that SJ ρ is a Spearman correlation between the signal and F1 rather than a raw count of pairs, so the rank correlation might not shift dramatically even with different N values. This is hard to pin down definitively, so I'm flagging it as a warning.

Now I'm putting together the full audit report with the critical and warning-level issues organized clearly.

I'm verifying the INFO section items—checking that the table values match their source experiments, confirming the paper used the correct baseline runs, and validating the data sources for the LLaMA results. The selection result is correctly described as a null finding with the bootstrap p-value, and I haven't found that "0.335" value anywhere in the paper. The OOD experiment is properly characterized as showing catastrophic model failure.

Now I'm moving through the remaining checks: the title phrasing is correct, the core narrative holds up, the exp_019 results aren't included in the paper as expected, and the claims are appropriately cautious. The ablation metrics and OOD values all align with what's in the registry. Ready to compile the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "631dfa47-cd77-4edc-ac23-108beee52822",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrAo3ifSr4jgePS8uNQTRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19858,
      "cache_read_input_tokens": 73839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19858
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

Now I have all the data needed. Let me verify one more specific thing — check if there are any dangling `\ref` in the paper and if the "0.335" number appears anywhere.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "3c7efe8f-9b83-4080-8750-83e622f5bebf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrAo3ifSr4jgePS8uNQTRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19858,
      "cache_read_input_tokens": 73839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19858
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

<details open><summary>🔧 Tool call — Grep · `toolu_01NJwaWRvRetE4mDjY1PY2GP`</summary>

```json
{
  "pattern": "0\\.335",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "c832ee3e-ea7b-4c48-b2d6-15fe302d3fe4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrAo3ifSr4jgePS8uNQTRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19858,
      "cache_read_input_tokens": 73839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19858
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

_source line 61 · 2026-05-15T12:51:29.935Z_

<details><summary>↩ Tool result · `toolu_01NJwaWRvRetE4mDjY1PY2GP`</summary>

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
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "5ddc50b8-97d0-42af-a5cb-30479ad67d02",
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

_source line 62_

<details open><summary>🔧 Tool call — Grep · `toolu_01DvGzE4eJjCmnXW85DeRp8f`</summary>

```json
{
  "pattern": "\\\\ref\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "a40b7e62-38c3-46e6-9196-ee274e6b407f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrAo3ifSr4jgePS8uNQTRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19858,
      "cache_read_input_tokens": 73839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19858
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

_source line 63 · 2026-05-15T12:51:30.746Z_

<details><summary>↩ Tool result · `toolu_01DvGzE4eJjCmnXW85DeRp8f`</summary>

```text
docs/paper/discussion.tex:6:When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
docs/paper/discussion.tex:10:Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
docs/paper/discussion.tex:12:Under constrained decoding, LP scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
docs/paper/discussion.tex:16:Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
docs/paper/discussion.tex:31:Effective selection likely requires either per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.
docs/paper/sections/related_work.tex:15:Our Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\S\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).
docs/paper/sections/related_work.tex:26:Our selection strategies instantiate MBR decoding \cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \cite{freitag2022high} and other generation tasks \cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\S\ref{sec:discussion}).
docs/paper/sections/experiments.tex:19:We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}). A 3-seed stability analysis ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}, Appendix~\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}
docs/paper/sections/experiments.tex:30:\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
docs/paper/sections/experiments.tex:54:Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
docs/paper/sections/experiments.tex:61:Pairwise bootstrap CIs confirm the SJ advantage over LP ($\Delta\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\Delta\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal}).
docs/paper/sections/experiments.tex:72:On WNUT-17, where 52\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
docs/paper/sections/experiments.tex:79:This reshuffles signal rankings (Figure~\ref{fig:signal_heatmap}, right).
docs/paper/sections/experiments.tex:82:This creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
docs/paper/sections/experiments.tex:91:\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound.}
docs/paper/sections/experiments.tex:98:\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \textbf{bold}. Instance-level signals (SJ, FK, EM, VC) select the sample closest to the consensus output; VC uses majority-threshold voting ($>{N/2}$) for selection, distinct from the continuous QE score (Eq.~\ref{eq:voting}).}
docs/paper/sections/experiments.tex:117:Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
docs/paper/sections/experiments.tex:127:TOST equivalence testing confirms most signals are indistinguishable from greedy at ${\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\pm}5$~pp (Table~\ref{tab:tost}, Appendix~\ref{app:diversity}).
docs/paper/sections/experiments.tex:129:The gap extends to CoNLL (ceiling effect, 57--88\% identical outputs) and WNUT-17 (capability boundary; Table~\ref{tab:cross_selection}).
docs/paper/sections/experiments.tex:140:Consistency-based signals show robust performance across $T{\in}\{0.7, 1.0\}$ (SJ NER $\Delta\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$; Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
docs/paper/sections/experiments.tex:142:NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
docs/paper/sections/discussion.tex:7:When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
docs/paper/sections/discussion.tex:11:Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
docs/paper/sections/discussion.tex:13:LP scores are severely compressed: the median within-instance LP range is only 0.041 nats, below the $\varepsilon{=}0.05$ threshold at which 60\% of instances are effectively tied, and 75\% of pairwise comparisons fall within $|\Delta|{<}0.026$ (Appendix~\ref{app:logprob_ties}).
docs/paper/sections/discussion.tex:16:A controlled NER ablation (\S\ref{sec:ablation}) confirms that LP compression persists without constrained decoding; on RE, the interaction is task-dependent.
docs/paper/sections/discussion.tex:17:Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
docs/paper/sections/discussion.tex:26:We test this via controlled ablation on SciERC (Qwen3-8B, single dataset): generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\%, 4406/4408; Table~\ref{tab:freeform_ablation}).
docs/paper/sections/discussion.tex:45:Effective selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.
docs/paper/sections/discussion.tex:46:Cross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\rho{=}0.469$ OOD vs.\ $0.386$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\ref{app:ood}).
docs/paper/sections/method.tex:12:Notation is summarized in Appendix~\ref{app:notation}.
docs/paper/sections/method.tex:63:[Omitted long matching line]
docs/paper/sections/method.tex:76:High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
docs/paper/sections/limitations.tex:2:RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
docs/paper/sections/limitations.tex:6:A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
docs/paper/sections/limitations.tex:16:Our free-form ablation (\S\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the compression finding generalizes to other datasets, model families, or model scales remains untested.
docs/paper/sections/appendix.tex:3:Table~\ref{tab:notation} summarizes the notation used throughout the paper.
docs/paper/sections/appendix.tex:77:LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
docs/paper/sections/appendix.tex:85:On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
docs/paper/sections/appendix.tex:118:Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
docs/paper/sections/appendix.tex:144:Table~\ref{tab:wnut} reports all five signals on WNUT-17.
docs/paper/sections/appendix.tex:168:Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
docs/paper/sections/appendix.tex:169:On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
docs/paper/sections/appendix.tex:190:Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
docs/paper/sections/appendix.tex:199:Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
docs/paper/sections/appendix.tex:200:The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
docs/paper/sections/appendix.tex:240:Table~\ref{tab:diversity} summarizes output diversity across configurations.
docs/paper/sections/appendix.tex:275:Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
docs/paper/sections/appendix.tex:304:Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
docs/paper/sections/appendix.tex:334:Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
docs/paper/sections/appendix.tex:381:[Omitted long matching line]
docs/paper/sections/appendix.tex:385:Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
docs/paper/sections/appendix.tex:388:The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
docs/paper/sections/appendix.tex:418:A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
docs/paper/sections/appendix.tex:422:Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
docs/paper/sections/appendix.tex:451:Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).
docs/paper/sections/appendix.tex:542:Table~\ref{tab:stable_failures} stratifies instances by failure stability.
docs/paper/sections/appendix.tex:569:Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
docs/paper/sections/appendix.tex:633:Signal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}).
docs/paper/sections/appendix.tex:634:Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
docs/paper/sections/appendix.tex:638:To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
docs/paper/sections/appendix.tex:643:\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$). In-domain $\rho$ from Table~\ref{tab:quality_estimation}. \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
docs/paper/sections/appendix.tex:661:When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.386$, $\Delta{=}{+}0.083$), SJ $\rho{=}0.378$ (in-domain $0.364$, $\Delta{=}{+}0.014$), and FK $\rho{=}0.285$ (in-domain $0.254$, $\Delta{=}{+}0.031$).
docs/paper/sections/appendix.tex:667:Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
docs/paper/sections/appendix.tex:668:These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
docs/paper/sections/introduction.tex:19:Structured IE requires schema-compliant output, making constrained decoding \cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\% valid JSON rate (\S\ref{sec:ablation}).}
docs/paper/sections/introduction.tex:22:Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.
docs/paper/sections/introduction.tex:25:Both fail: MBR utility correlates with F1 across instances but not within them (\S\ref{sec:discussion}); log-probability scores are severely compressed (60\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
docs/paper/sections/introduction.tex:26:A controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), revealing task-dependent interaction with decoding regime (\S\ref{sec:ablation}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "bc4e2910-6a41-442f-93e8-37effb40077f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/discussion.tex:6:When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\ndocs/paper/discussion.tex:10:Consensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\ndocs/paper/discussion.tex:12:Under constrained decoding, LP scores are severely compressed: 60\\% of instances have a within-sample range below 0.05, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$; Appendix~\\ref{app:logprob_ties}).\ndocs/paper/discussion.tex:16:Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\ndocs/paper/discussion.tex:31:Effective selection likely requires either per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.\ndocs/paper/sections/related_work.tex:15:Our Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\ndocs/paper/sections/related_work.tex:26:Our selection strategies instantiate MBR decoding \\cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \\cite{freitag2022high} and other generation tasks \\cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\\S\\ref{sec:discussion}).\ndocs/paper/sections/experiments.tex:19:We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}). A 3-seed stability analysis ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}\ndocs/paper/sections/experiments.tex:30:\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\ndocs/paper/sections/experiments.tex:54:Table~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\ndocs/paper/sections/experiments.tex:61:Pairwise bootstrap CIs confirm the SJ advantage over LP ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\\Delta\\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal}).\ndocs/paper/sections/experiments.tex:72:On WNUT-17, where 52\\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\ndocs/paper/sections/experiments.tex:79:This reshuffles signal rankings (Figure~\\ref{fig:signal_heatmap}, right).\ndocs/paper/sections/experiments.tex:82:This creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\ndocs/paper/sections/experiments.tex:91:\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound.}\ndocs/paper/sections/experiments.tex:98:\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \\textbf{bold}. Instance-level signals (SJ, FK, EM, VC) select the sample closest to the consensus output; VC uses majority-threshold voting ($>{N/2}$) for selection, distinct from the continuous QE score (Eq.~\\ref{eq:voting}).}\ndocs/paper/sections/experiments.tex:117:Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\ndocs/paper/sections/experiments.tex:127:TOST equivalence testing confirms most signals are indistinguishable from greedy at ${\\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\\pm}5$~pp (Table~\\ref{tab:tost}, Appendix~\\ref{app:diversity}).\ndocs/paper/sections/experiments.tex:129:The gap extends to CoNLL (ceiling effect, 57--88\\% identical outputs) and WNUT-17 (capability boundary; Table~\\ref{tab:cross_selection}).\ndocs/paper/sections/experiments.tex:140:Consistency-based signals show robust performance across $T{\\in}\\{0.7, 1.0\\}$ (SJ NER $\\Delta\\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$; Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\ndocs/paper/sections/experiments.tex:142:NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\ndocs/paper/sections/discussion.tex:7:When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\ndocs/paper/sections/discussion.tex:11:Consensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\ndocs/paper/sections/discussion.tex:13:LP scores are severely compressed: the median within-instance LP range is only 0.041 nats, below the $\\varepsilon{=}0.05$ threshold at which 60\\% of instances are effectively tied, and 75\\% of pairwise comparisons fall within $|\\Delta|{<}0.026$ (Appendix~\\ref{app:logprob_ties}).\ndocs/paper/sections/discussion.tex:16:A controlled NER ablation (\\S\\ref{sec:ablation}) confirms that LP compression persists without constrained decoding; on RE, the interaction is task-dependent.\ndocs/paper/sections/discussion.tex:17:Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\ndocs/paper/sections/discussion.tex:26:We test this via controlled ablation on SciERC (Qwen3-8B, single dataset): generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\\%, 4406/4408; Table~\\ref{tab:freeform_ablation}).\ndocs/paper/sections/discussion.tex:45:Effective selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.\ndocs/paper/sections/discussion.tex:46:Cross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\\rho{=}0.469$ OOD vs.\\ $0.386$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\\ref{app:ood}).\ndocs/paper/sections/method.tex:12:Notation is summarized in Appendix~\\ref{app:notation}.\ndocs/paper/sections/method.tex:63:[Omitted long matching line]\ndocs/paper/sections/method.tex:76:High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\ndocs/paper/sections/limitations.tex:2:RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.\ndocs/paper/sections/limitations.tex:6:A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\ndocs/paper/sections/limitations.tex:16:Our free-form ablation (\\S\\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the compression finding generalizes to other datasets, model families, or model scales remains untested.\ndocs/paper/sections/appendix.tex:3:Table~\\ref{tab:notation} summarizes the notation used throughout the paper.\ndocs/paper/sections/appendix.tex:77:LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\ndocs/paper/sections/appendix.tex:85:On CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\ndocs/paper/sections/appendix.tex:118:Figure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\ndocs/paper/sections/appendix.tex:144:Table~\\ref{tab:wnut} reports all five signals on WNUT-17.\ndocs/paper/sections/appendix.tex:168:Table~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\ndocs/paper/sections/appendix.tex:169:On LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\ndocs/paper/sections/appendix.tex:190:Our $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\ndocs/paper/sections/appendix.tex:199:Table~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\ndocs/paper/sections/appendix.tex:200:The SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\ndocs/paper/sections/appendix.tex:240:Table~\\ref{tab:diversity} summarizes output diversity across configurations.\ndocs/paper/sections/appendix.tex:275:Table~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\ndocs/paper/sections/appendix.tex:304:Table~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\ndocs/paper/sections/appendix.tex:334:Both models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\ndocs/paper/sections/appendix.tex:381:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:385:Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\ndocs/paper/sections/appendix.tex:388:The CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.\ndocs/paper/sections/appendix.tex:418:A free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\ndocs/paper/sections/appendix.tex:422:Table~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\ndocs/paper/sections/appendix.tex:451:Table~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).\ndocs/paper/sections/appendix.tex:542:Table~\\ref{tab:stable_failures} stratifies instances by failure stability.\ndocs/paper/sections/appendix.tex:569:Tables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\ndocs/paper/sections/appendix.tex:633:Signal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}).\ndocs/paper/sections/appendix.tex:634:Doubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER), confirming that additional samples stabilize structural signals more than LP.\ndocs/paper/sections/appendix.tex:638:To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).\ndocs/paper/sections/appendix.tex:643:\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation}. \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\ndocs/paper/sections/appendix.tex:661:When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.386$, $\\Delta{=}{+}0.083$), SJ $\\rho{=}0.378$ (in-domain $0.364$, $\\Delta{=}{+}0.014$), and FK $\\rho{=}0.285$ (in-domain $0.254$, $\\Delta{=}{+}0.031$).\ndocs/paper/sections/appendix.tex:667:Under this regime, most signals flip to negative or near-zero correlations (Table~\\ref{tab:ood}); only VC retains weak positive correlation ($\\rho{=}0.105$, $p{=}0.016$).\ndocs/paper/sections/appendix.tex:668:These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\\S\\ref{sec:qe_results}), not evidence against signal utility.\ndocs/paper/sections/introduction.tex:19:Structured IE requires schema-compliant output, making constrained decoding \\cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\\% valid JSON rate (\\S\\ref{sec:ablation}).}\ndocs/paper/sections/introduction.tex:22:Our central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.\ndocs/paper/sections/introduction.tex:25:Both fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}); log-probability scores are severely compressed (60\\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\ndocs/paper/sections/introduction.tex:26:A controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), revealing task-dependent interaction with decoding regime (\\S\\ref{sec:ablation}).",
    "numLines": 68
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Grep · `toolu_01XsxWnnsL6R3AYvDgewj5fy`</summary>

```json
{
  "pattern": "\\\\label\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "e3314ff8-dfcb-42c2-a2a3-6f8605658e86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrAo3ifSr4jgePS8uNQTRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19858,
      "cache_read_input_tokens": 73839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19858
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

### Runtime record

_source line 65_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778850600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a016c13a-cb1e-471a-8354-99070c632b0c",
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7"
}
```

---

### Tool result

_source line 66 · 2026-05-15T12:51:31.314Z_

<details><summary>↩ Tool result · `toolu_01XsxWnnsL6R3AYvDgewj5fy`</summary>

```text
docs/paper/conclusion.tex:1:\section{Conclusion}\label{sec:conclusion}
docs/paper/discussion.tex:1:\section{Discussion}\label{sec:discussion}
docs/paper/sections/related_work.tex:1:\section{Related Work}\label{sec:related}
docs/paper/sections/experiments.tex:2:\label{sec:experiments}
docs/paper/sections/experiments.tex:5:\label{sec:setup}
docs/paper/sections/experiments.tex:25:\label{sec:qe_results}
docs/paper/sections/experiments.tex:31:\label{tab:quality_estimation}
docs/paper/sections/experiments.tex:51:\label{fig:signal_heatmap}
docs/paper/sections/experiments.tex:86:\label{sec:selection_gap}
docs/paper/sections/experiments.tex:92:\label{fig:selection_gap}
docs/paper/sections/experiments.tex:99:\label{tab:selection}
docs/paper/sections/experiments.tex:138:\label{sec:robustness_main}
docs/paper/sections/conclusion.tex:1:\section{Conclusion}\label{sec:conclusion}
docs/paper/sections/discussion.tex:1:\section{Discussion}\label{sec:discussion}
docs/paper/sections/discussion.tex:24:\paragraph{Score compression under free-form decoding.}\label{sec:ablation}
docs/paper/sections/method.tex:1:\section{Method}\label{sec:method}
docs/paper/sections/method.tex:3:\subsection{Problem Formulation}\label{sec:formulation}
docs/paper/sections/method.tex:14:\subsection{Confidence Signals}\label{sec:signals}
docs/paper/sections/method.tex:23:\begin{equation}\label{eq:logprob}
docs/paper/sections/method.tex:29:\begin{equation}\label{eq:em}
docs/paper/sections/method.tex:35:\begin{equation}\label{eq:fk}
docs/paper/sections/method.tex:47:\begin{equation}\label{eq:sj}
docs/paper/sections/method.tex:53:\begin{equation}\label{eq:sj_instance}
docs/paper/sections/method.tex:60:\begin{equation}\label{eq:voting}
docs/paper/sections/method.tex:65:\subsection{Evaluation Framework}\label{sec:evaluation}
docs/paper/sections/appendix.tex:1:\section{Notation}\label{app:notation}
docs/paper/sections/appendix.tex:26:\label{tab:notation}
docs/paper/sections/appendix.tex:29:\section{Robustness Analysis}\label{app:robustness}
docs/paper/sections/appendix.tex:35:\label{tab:robustness}
docs/paper/sections/appendix.tex:66:\label{fig:temperature_robustness}
docs/paper/sections/appendix.tex:88:\section{Calibration Analysis}\label{app:calibration}
docs/paper/sections/appendix.tex:94:\label{fig:reliability}
docs/paper/sections/appendix.tex:100:\section{Additional Analyses}\label{app:additional}
docs/paper/sections/appendix.tex:124:\label{fig:length_logprob_scatter}
docs/paper/sections/appendix.tex:153:\label{tab:wnut}
docs/paper/sections/appendix.tex:176:\label{tab:cross_selection}
docs/paper/sections/appendix.tex:197:\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
docs/paper/sections/appendix.tex:208:\label{tab:bootstrap_signal_ci}
docs/paper/sections/appendix.tex:237:\section{Diversity and Selection Analysis}\label{app:diversity}
docs/paper/sections/appendix.tex:250:\label{tab:diversity}
docs/paper/sections/appendix.tex:286:\label{tab:tost}
docs/paper/sections/appendix.tex:302:\section{Multi-Seed Stability}\label{app:multiseed}
docs/paper/sections/appendix.tex:313:\label{tab:multiseed}
docs/paper/sections/appendix.tex:332:\section{Training Configuration}\label{app:training}
docs/paper/sections/appendix.tex:340:\label{tab:training}
docs/paper/sections/appendix.tex:383:\section{Log-Probability Score Compression}\label{app:logprob_ties}
docs/paper/sections/appendix.tex:395:\label{fig:lp_range_cdf}
docs/paper/sections/appendix.tex:402:\label{tab:logprob_ties}
docs/paper/sections/appendix.tex:420:\section{RE Conditional Selection}\label{app:re_conditional_selection}
docs/paper/sections/appendix.tex:432:\label{tab:re_cond_selection}
docs/paper/sections/appendix.tex:449:\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
docs/paper/sections/appendix.tex:460:\label{tab:freeform_ablation}
docs/paper/sections/appendix.tex:533:\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
docs/paper/sections/appendix.tex:550:\label{tab:stable_failures}
docs/paper/sections/appendix.tex:567:\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
docs/paper/sections/appendix.tex:574:\label{tab:n-scaling}
docs/paper/sections/appendix.tex:596:\label{tab:ranking-stability}
docs/paper/sections/appendix.tex:614:\label{tab:sigma-comparison}
docs/paper/sections/appendix.tex:636:\section{Cross-Dataset OOD Analysis}\label{app:ood}
docs/paper/sections/appendix.tex:644:\label{tab:ood}
docs/paper/sections/introduction.tex:1:\section{Introduction}\label{sec:introduction}
docs/paper/sections/introduction.tex:32:\label{fig:overview}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "92fb7290-3d0c-4d08-8b0e-25d3b3bcbe00",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/conclusion.tex:1:\\section{Conclusion}\\label{sec:conclusion}\ndocs/paper/discussion.tex:1:\\section{Discussion}\\label{sec:discussion}\ndocs/paper/sections/related_work.tex:1:\\section{Related Work}\\label{sec:related}\ndocs/paper/sections/experiments.tex:2:\\label{sec:experiments}\ndocs/paper/sections/experiments.tex:5:\\label{sec:setup}\ndocs/paper/sections/experiments.tex:25:\\label{sec:qe_results}\ndocs/paper/sections/experiments.tex:31:\\label{tab:quality_estimation}\ndocs/paper/sections/experiments.tex:51:\\label{fig:signal_heatmap}\ndocs/paper/sections/experiments.tex:86:\\label{sec:selection_gap}\ndocs/paper/sections/experiments.tex:92:\\label{fig:selection_gap}\ndocs/paper/sections/experiments.tex:99:\\label{tab:selection}\ndocs/paper/sections/experiments.tex:138:\\label{sec:robustness_main}\ndocs/paper/sections/conclusion.tex:1:\\section{Conclusion}\\label{sec:conclusion}\ndocs/paper/sections/discussion.tex:1:\\section{Discussion}\\label{sec:discussion}\ndocs/paper/sections/discussion.tex:24:\\paragraph{Score compression under free-form decoding.}\\label{sec:ablation}\ndocs/paper/sections/method.tex:1:\\section{Method}\\label{sec:method}\ndocs/paper/sections/method.tex:3:\\subsection{Problem Formulation}\\label{sec:formulation}\ndocs/paper/sections/method.tex:14:\\subsection{Confidence Signals}\\label{sec:signals}\ndocs/paper/sections/method.tex:23:\\begin{equation}\\label{eq:logprob}\ndocs/paper/sections/method.tex:29:\\begin{equation}\\label{eq:em}\ndocs/paper/sections/method.tex:35:\\begin{equation}\\label{eq:fk}\ndocs/paper/sections/method.tex:47:\\begin{equation}\\label{eq:sj}\ndocs/paper/sections/method.tex:53:\\begin{equation}\\label{eq:sj_instance}\ndocs/paper/sections/method.tex:60:\\begin{equation}\\label{eq:voting}\ndocs/paper/sections/method.tex:65:\\subsection{Evaluation Framework}\\label{sec:evaluation}\ndocs/paper/sections/appendix.tex:1:\\section{Notation}\\label{app:notation}\ndocs/paper/sections/appendix.tex:26:\\label{tab:notation}\ndocs/paper/sections/appendix.tex:29:\\section{Robustness Analysis}\\label{app:robustness}\ndocs/paper/sections/appendix.tex:35:\\label{tab:robustness}\ndocs/paper/sections/appendix.tex:66:\\label{fig:temperature_robustness}\ndocs/paper/sections/appendix.tex:88:\\section{Calibration Analysis}\\label{app:calibration}\ndocs/paper/sections/appendix.tex:94:\\label{fig:reliability}\ndocs/paper/sections/appendix.tex:100:\\section{Additional Analyses}\\label{app:additional}\ndocs/paper/sections/appendix.tex:124:\\label{fig:length_logprob_scatter}\ndocs/paper/sections/appendix.tex:153:\\label{tab:wnut}\ndocs/paper/sections/appendix.tex:176:\\label{tab:cross_selection}\ndocs/paper/sections/appendix.tex:197:\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\ndocs/paper/sections/appendix.tex:208:\\label{tab:bootstrap_signal_ci}\ndocs/paper/sections/appendix.tex:237:\\section{Diversity and Selection Analysis}\\label{app:diversity}\ndocs/paper/sections/appendix.tex:250:\\label{tab:diversity}\ndocs/paper/sections/appendix.tex:286:\\label{tab:tost}\ndocs/paper/sections/appendix.tex:302:\\section{Multi-Seed Stability}\\label{app:multiseed}\ndocs/paper/sections/appendix.tex:313:\\label{tab:multiseed}\ndocs/paper/sections/appendix.tex:332:\\section{Training Configuration}\\label{app:training}\ndocs/paper/sections/appendix.tex:340:\\label{tab:training}\ndocs/paper/sections/appendix.tex:383:\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\ndocs/paper/sections/appendix.tex:395:\\label{fig:lp_range_cdf}\ndocs/paper/sections/appendix.tex:402:\\label{tab:logprob_ties}\ndocs/paper/sections/appendix.tex:420:\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\ndocs/paper/sections/appendix.tex:432:\\label{tab:re_cond_selection}\ndocs/paper/sections/appendix.tex:449:\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\ndocs/paper/sections/appendix.tex:460:\\label{tab:freeform_ablation}\ndocs/paper/sections/appendix.tex:533:\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\ndocs/paper/sections/appendix.tex:550:\\label{tab:stable_failures}\ndocs/paper/sections/appendix.tex:567:\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\ndocs/paper/sections/appendix.tex:574:\\label{tab:n-scaling}\ndocs/paper/sections/appendix.tex:596:\\label{tab:ranking-stability}\ndocs/paper/sections/appendix.tex:614:\\label{tab:sigma-comparison}\ndocs/paper/sections/appendix.tex:636:\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\ndocs/paper/sections/appendix.tex:644:\\label{tab:ood}\ndocs/paper/sections/introduction.tex:1:\\section{Introduction}\\label{sec:introduction}\ndocs/paper/sections/introduction.tex:32:\\label{fig:overview}",
    "numLines": 62
  }
}
```

</details>

---

### Assistant

_source line 67_

<details><summary>Logged reasoning block</summary>

```text
Let me now check for dangling refs. I need to compare all \ref targets with all \label targets.

Refs used:
- tab:wnut ✓ (labeled)
- sec:evaluation ✓
- tab:selection ✓
- app:logprob_ties ✓
- app:diversity ✓
- app:calibration ✓
- app:additional ✓
- sec:selection_gap ✓
- sec:discussion ✓
- tab:robustness ✓


- app:robustness ✓
- tab:quality_estimation ✓
- fig:signal_heatmap ✓
- tab:bootstrap_signal_ci ✓
- app:bootstrap_signal ✓
- tab:cross_selection ✓
- tab:multiseed ✓
- app:multiseed ✓
- fig:selection_gap ✓
- sec:qe_results ✓
- tab:tost ✓
- tab:diversity ✓
- app:notation ✓
- tab:notation ✓
- sec:ablation ✓
- tab:freeform_ablation ✓
- fig:overview ✓

All references are accounted for and properly labeled. I'm verifying that all the referenced labels actually exist in the codebase, and I notice there are duplicate files — both `docs/paper/discussion.tex` and `docs/paper/sections/discussion.tex`. Since main.tex includes the one in sections, the other is likely an old copy that I should check for differences. I'm noticing there are duplicate files at different levels — the root-level `discussion.tex` and `conclusion.tex` appear to be older versions since `main.tex` actually includes from the `sections/` subdirectory. I'll make a note of this potential issue but move on to focus on the report itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "087990cc-9371-442c-85eb-2b4c14595c2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbUepBrR6o6b6VN38QzJKA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9037,
      "cache_read_input_tokens": 93697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9037
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

_source line 68_

Now let me check a potentially divergent file and verify the artifacts directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "10431fc1-52a7-464c-88c4-6517ad36556b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbUepBrR6o6b6VN38QzJKA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9037,
      "cache_read_input_tokens": 93697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9037
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

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01BVzVszojVJPvLDJkVxLPyT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex",
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
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "aef23dfa-9b0f-4e80-ba4d-ea8657d30b65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbUepBrR6o6b6VN38QzJKA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9037,
      "cache_read_input_tokens": 93697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9037
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

_source line 70 · 2026-05-15T12:51:58.788Z_

<details><summary>↩ Tool result · `toolu_01BVzVszojVJPvLDJkVxLPyT`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "f2ee2adc-111b-4e1c-bf8c-834b7f7bfa9a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 31
    }
  }
}
```

</details>

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_012VuWh3Z7iaUqudyLaqorDN`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
  "description": "Check if review_reports directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "7d811858-b909-427b-b743-135beeb6ea68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbUepBrR6o6b6VN38QzJKA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9037,
      "cache_read_input_tokens": 93697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9037
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

_source line 72 · 2026-05-15T12:51:59.871Z_

<details><summary>↩ Tool result · `toolu_012VuWh3Z7iaUqudyLaqorDN`</summary>

```text
total 132
drwxr-xr-x  2 ubuntu ubuntu  4096 May 15 12:37 .
drwxr-xr-x 43 ubuntu ubuntu  4096 May 15 12:51 ..
-rw-r--r--  1 ubuntu ubuntu 11576 May 14 12:20 round_0.md
-rw-r--r--  1 ubuntu ubuntu 16761 May 15 02:09 round_1.md
-rw-r--r--  1 ubuntu ubuntu 14511 May 15 02:56 round_2.md
-rw-r--r--  1 ubuntu ubuntu 15327 May 15 04:14 round_3.md
-rw-r--r--  1 ubuntu ubuntu 14214 May 15 07:08 round_4.md
-rw-r--r--  1 ubuntu ubuntu 14121 May 15 08:08 round_5.md
-rw-r--r--  1 ubuntu ubuntu 14108 May 15 09:05 round_6.md
-rw-r--r--  1 ubuntu ubuntu 11867 May 15 12:37 round_7.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "699709d2-0d56-4c96-9e72-4de955bbec3c",
  "tool_use_result": {
    "stdout": "total 132\ndrwxr-xr-x  2 ubuntu ubuntu  4096 May 15 12:37 .\ndrwxr-xr-x 43 ubuntu ubuntu  4096 May 15 12:51 ..\n-rw-r--r--  1 ubuntu ubuntu 11576 May 14 12:20 round_0.md\n-rw-r--r--  1 ubuntu ubuntu 16761 May 15 02:09 round_1.md\n-rw-r--r--  1 ubuntu ubuntu 14511 May 15 02:56 round_2.md\n-rw-r--r--  1 ubuntu ubuntu 15327 May 15 04:14 round_3.md\n-rw-r--r--  1 ubuntu ubuntu 14214 May 15 07:08 round_4.md\n-rw-r--r--  1 ubuntu ubuntu 14121 May 15 08:08 round_5.md\n-rw-r--r--  1 ubuntu ubuntu 14108 May 15 09:05 round_6.md\n-rw-r--r--  1 ubuntu ubuntu 11867 May 15 12:37 round_7.md",
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
I see there's already a round_7.md file. Let me also read the actual sections/discussion.tex to see if there are differences. Actually, I already read sections/discussion.tex earlier. The root-level discussion.tex seems to be the same or very similar to the sections/ version.

Also, I see the root-level discussion.tex matches sections/discussion.tex:
Root line 1: `\section{Discussion}\label{sec:discussion}` 
Sections line 1: `\section{Discussion}\label{sec:discussion}`
Root line 3-5 content matches sections version.


These files appear to be identical. Since main.tex only includes from `sections/`, the root-level discussion.tex and conclusion.tex aren't actually used in the compilation, though they could potentially cause duplicate label warnings if they were ever included.

Now I'm compiling the full report and need to verify that the appendix's `fig:lp_range_cdf` reference has a corresponding figure file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "7bb4a14d-0ad4-4004-b0f8-af20ae7454e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rrhj4jAeTdyDc4aiJKZ3o7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2138,
      "cache_read_input_tokens": 102734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2138
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

Let me verify the referenced figures exist and check the appendix for the CDF figure that was added.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "7e57bcf4-7b57-42bb-8d6c-e5156de88414",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rrhj4jAeTdyDc4aiJKZ3o7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2138,
      "cache_read_input_tokens": 102734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2138
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

<details open><summary>🔧 Tool call — Glob · `toolu_01KJEDm1dp3AYmNncQHHkM1m`</summary>

```json
{
  "pattern": "figures/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "5b1f7080-74e9-4e22-8ecf-9f15e25b2b9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rrhj4jAeTdyDc4aiJKZ3o7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2138,
      "cache_read_input_tokens": 102734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2138
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

_source line 76 · 2026-05-15T12:52:10.600Z_

<details><summary>↩ Tool result · `toolu_01KJEDm1dp3AYmNncQHHkM1m`</summary>

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
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "fa429c1c-bad7-43ab-a837-638dbee63419",
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

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Read · `toolu_01LRLPytzoCMRMvwHhy1J5LU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 383,
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
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "e264d0e6-b81a-4a63-b2cd-a3561633c0b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rrhj4jAeTdyDc4aiJKZ3o7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2138,
      "cache_read_input_tokens": 102734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2138
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

_source line 78 · 2026-05-15T12:52:11.342Z_

<details><summary>↩ Tool result · `toolu_01LRLPytzoCMRMvwHhy1J5LU`</summary>

```text
383	\section{Log-Probability Score Compression}\label{app:logprob_ties}
384	
385	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
386	The median within-instance LP range is only 0.041 nats---below the $\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.
387	At $\varepsilon{=}0.05$, 59.7\% of instances have a within-sample range below the threshold, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
388	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
389	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
390	
391	\begin{figure}[t]
392	\centering
393	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
394	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
395	\label{fig:lp_range_cdf}
396	\end{figure}
397	
398	\begin{table}[t]
399	\centering
400	\small
401	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
402	\label{tab:logprob_ties}
403	\begin{tabular}{lc}
404	\toprule
405	$\varepsilon$ threshold & Tied instances (\%) \\
406	\midrule
407	0.01 & 1.1\% \\
408	0.05 & 60.3\% \\
409	0.1  & ${\sim}$84\% \\
410	0.5  & ${\sim}$99\% \\
411	\bottomrule
412	\end{tabular}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "2fd08325-0ebe-4ee7-8550-ebec0a78606f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats---below the $\\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.\nAt $\\varepsilon{=}0.05$, 59.7\\% of instances have a within-sample range below the threshold, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_lp_range_cdf}\n\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n\\label{fig:lp_range_cdf}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}",
      "numLines": 30,
      "startLine": 383,
      "totalLines": 673
    }
  }
}
```

</details>

---

### Assistant

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
The figures directory is empty! No figure files found. That means all the \includegraphics references will fail when compiling. Let me check if they're elsewhere:
- fig_overview
- fig_signal_heatmap
- fig_selection_gap
- fig_temperature_robustness
- fig_reliability
- fig_length_logprob_scatter
- fig_lp_range_cdf

These need to be in the figures/ directory as specified by \graphicspath{{figures/}}. Let me check if there's a figures/ directory somewhere else.

Actually, the graphicspath could also search the current directory. 

Let me look more carefully at the directory structure to see where these files might actually be located.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "e3aef8ad-d140-4324-8f93-53494ea4898c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSzvhim5Xsu1BeG8r3f7aQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1317,
      "cache_read_input_tokens": 104872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1317
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

_source line 80_

<details open><summary>🔧 Tool call — Bash · `toolu_01UKPRQssRi6bXns9T3Pcy3x`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/ 2>/dev/null || echo \"NO_FIGURES_DIR\"\nfind /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/ -name \"fig_*\" -o -name \"*.pdf\" -o -name \"*.png\" 2>/dev/null | head -20",
  "description": "Check for figure files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "faeb653d-6a0a-479d-9e4a-785f43c8b944",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSzvhim5Xsu1BeG8r3f7aQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1317,
      "cache_read_input_tokens": 104872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1317
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

_source line 81 · 2026-05-15T12:52:18.522Z_

<details><summary>↩ Tool result · `toolu_01UKPRQssRi6bXns9T3Pcy3x`</summary>

```text
total 288
drwxr-xr-x 2 ubuntu ubuntu   4096 May 15 12:48 .
drwxr-xr-x 5 ubuntu ubuntu   4096 May 15 12:52 ..
-rw-r--r-- 1 ubuntu ubuntu 101868 May 15 02:31 fig_length_logprob_scatter.pdf
-rw-r--r-- 1 ubuntu ubuntu  19847 May 15 12:48 fig_lp_range_cdf.pdf
-rw-r--r-- 1 ubuntu ubuntu  46203 May 14 19:17 fig_overview.pdf
-rw-r--r-- 1 ubuntu ubuntu  20725 May 14 19:17 fig_reliability.pdf
-rw-r--r-- 1 ubuntu ubuntu  28396 May 14 21:47 fig_selection_gap.pdf
-rw-r--r-- 1 ubuntu ubuntu  30075 May 14 21:47 fig_signal_heatmap.pdf
-rw-r--r-- 1 ubuntu ubuntu  24879 May 14 21:47 fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p14.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p17.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p15.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p20.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p16.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p19.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p18.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "d9ba889b-fcf9-4494-9947-053a8c5aa361",
  "tool_use_result": {
    "stdout": "total 288\ndrwxr-xr-x 2 ubuntu ubuntu   4096 May 15 12:48 .\ndrwxr-xr-x 5 ubuntu ubuntu   4096 May 15 12:52 ..\n-rw-r--r-- 1 ubuntu ubuntu 101868 May 15 02:31 fig_length_logprob_scatter.pdf\n-rw-r--r-- 1 ubuntu ubuntu  19847 May 15 12:48 fig_lp_range_cdf.pdf\n-rw-r--r-- 1 ubuntu ubuntu  46203 May 14 19:17 fig_overview.pdf\n-rw-r--r-- 1 ubuntu ubuntu  20725 May 14 19:17 fig_reliability.pdf\n-rw-r--r-- 1 ubuntu ubuntu  28396 May 14 21:47 fig_selection_gap.pdf\n-rw-r--r-- 1 ubuntu ubuntu  30075 May 14 21:47 fig_signal_heatmap.pdf\n-rw-r--r-- 1 ubuntu ubuntu  24879 May 14 21:47 fig_temperature_robustness.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p14.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p3.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p17.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p12.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p10.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p6.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p11.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p15.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p20.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p13.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p16.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p19.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p18.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p7.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p5.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p4.png\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png",
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

_source line 82_

<details><summary>Logged reasoning block</summary>

```text
Good, all 7 figure files exist in the figures/ directory. No missing figures.

Now I also noticed a discrepancy in the appendix's logprob_ties table. Let me check:

Appendix (line 387-388): "At ε=0.05, 59.7% of instances have a within-sample range below the threshold"

But in the table (line 408): "0.05 & 60.3%"

And the earlier reading had: "60.3%" in the table.

But the text just above says "59.7%". 

So there's a mismatch — the appendix text claims 59.7% but the table shows 60.3%, and the registry confirms 59.7% as the actual value, meaning the table has the wrong number. ancy within the paper itself. Let me think about whether these could be computed differently — maybe the logprob_ties section uses a different subset of instances or applies rounding at different stages. The 0.6 percentage point gap between 59.7% and 60.3% could stem from filtering decisions or intermediate rounding, but either way, the paper reports conflicting values for what should be the same statistic.

Looking across all mentions: the appendix text gives 59.7%, the appendix table shows 60.3%, the freeform ablation panel reports 59.7%, and the main text uses the rounded 60%. Most of these cluster around 59.7% or its rounded form, making the table's 60.3% the clear outlier. This is a genuine inconsistency I should flag — the appendix text and its accompanying table don't match, which is a warning-level issue. I'm noticing 59.7% appears consistently across the appendix text and freeform ablation table, while 60.3% only shows up in the logprob_ties table—they might be using different sample bases (529 vs 551 instances), which would account for the ~3-instance discrepancy. I'll flag this as a warning to investigate.

I'm also realizing there's a file organization issue: main.tex imports from sections/discussion, but there's also a root-level discussion.tex that appears to be unused and could cause confusion if someone edits the wrong file. Now I have enough to compile the full report.

Looking back at Table 2's caption, I notice it's been updated since my initial read. The current version describes how instance-level signals work and mentions VC's majority-threshold voting approach, but I'm seeing a discrepancy with what I read earlier about EM's performance. I'm noticing a discrepancy between what I read earlier and what the grep output is showing me—the caption text appears to have changed or there are multiple versions of this file. Let me check if there's a version mismatch between the root-level and sections directories, since the grep result shows different wording about instance-level signals and voting thresholds compared to my initial read about EM selection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "be149749-efba-4b14-89b3-633659c6749d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgCaj4kJbbGR7rACPzfSdv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 106189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1567
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

_source line 83_

I have all the data I need. Let me now write the comprehensive audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "cf3c4d66-656e-4614-a89f-9c56e477a4eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgCaj4kJbbGR7rACPzfSdv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 106189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1567
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

_source line 84_

<details open><summary>🔧 Tool call — Write · `toolu_01STbhihTm7CAkuEfwNKH6Js`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7_consistency.md",
  "content": "# Round 7 一致性审计报告\n\n**审计日期**: 2026-05-15\n**审计范围**: 论文全文 (main.tex + 8 section files) vs registry 实验数据\n**论文标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction\n\n## 总体评判: WARNING\n\n1 CRITICAL (OOD 表 in-domain 引用错误), 3 WARNING (WNUT N 值矛盾、appendix 内部数值不一致、若干微小 rounding 偏差)。核心 Table 1 和 Table 2 的关键数据与 registry 一致，硬约束全部通过。\n\n---\n\n## CRITICAL 发现\n\n### [C-1] OOD 表 (Table 9, Appendix F) in-domain 列引用错误\n\n**问题**: 表格 caption 声称 \"In-domain ρ from Table 1 (tab:quality_estimation)\"，但实际使用的是 Table 5 (tab:multiseed) 的 3-seed 均值。\n\n**证据**:\n\n| Signal | OOD Table In-dom. | Table 1 (seed=42) | Table 5 (3-seed mean) |\n|--------|------------------|--------------------|-----------------------|\n| VC     | .386             | .379               | .386 ✓                |\n| SJ     | .364             | .360               | .364 ✓                |\n| EM     | .307             | .295               | .307 ✓                |\n| FK     | .254             | .267               | .254 ✓                |\n| LP     | .217             | .205               | .217 ✓                |\n\n**影响**: \n- 所有 Δ 值被系统性偏移\n- EM 的 Δ 从 +.005（正确，用 Table 1）变成 -.007（报告值），**符号翻转**\n- FK 的 Δ 从 +.018 变成 +.031（幅度膨胀 72%）\n- OOD 实际值来自单次运行 (exp_011_ood_scierc_to_conll, seed=42)，与 3-seed mean 对比在方法论上不一致\n\n**涉及位置**:\n- appendix.tex L643: 表格 caption\n- appendix.tex L661: 正文 \"in-domain ρ from Table~\\ref{tab:quality_estimation}\"\n- discussion.tex L46: \"VC ρ=0.469 OOD vs. 0.386 in-domain\" (传播了相同错误)\n\n**修复**: 将 OOD 表 in-domain 列改为 Table 1 单 seed 值 (.379/.360/.295/.267/.205)，重算所有 Δ，或将 caption 引用改为 Table 5 并注明方法论差异。\n\n---\n\n## WARNING 发现\n\n### [W-1] WNUT-17 表格 N=8 vs registry N=16 矛盾\n\n**问题**: WNUT 表 (tab:wnut, appendix.tex L152) caption 声称 \"N=8, T=1.0\"，但 registry 中仅有的两个 WNUT 实验 (exp_003_ner_wnut17, exp_003_wnut17_eval) 均为 N=16。\n\n**证据**:\n- Registry exp_003_wnut17_eval: N=16, T=1, seed=42\n- Registry exp_003_ner_wnut17: N=16, T=1, seed=42\n- 论文 WNUT 表 SJ ρ=.089 与 exp_003_wnut17_eval 的 rho_sj=0.089 精确匹配（N=16 数据）\n- 论文 WNUT 表 FK ρ=.125 与 exp_003_wnut17_eval 的 rho_fk=0.125 精确匹配\n\n**影响**: 如果数据确实来自 N=16 但 caption 标注 N=8，则与正文 \"primary N=8\" 声称不一致。精确匹配 N=16 registry 值增强了 caption 标注错误的可能性。\n\n**修复**: 核实数据实际 N 值。如果是 N=16 数据，改 caption 为 N=16 并在正文中说明；如果有独立的 N=8 分析（未注册），应补充 registry。\n\n### [W-2] Appendix logprob_ties 表与正文自相矛盾 (59.7% vs 60.3%)\n\n**问题**: 同一 appendix 节内，正文说 \"59.7% of instances\" 但紧接着的表格说 \"60.3%\"。\n\n**证据**:\n- appendix.tex L387: \"At ε=0.05, 59.7% of instances have a within-sample range below the threshold\"\n- appendix.tex L408: Table 行 \"0.05 & 60.3%\"\n- Registry exp_freeform_ablation: tied_fraction_constrained = 0.597 = 59.7%\n- Freeform ablation Panel A (appendix.tex L464): \"59.7%\" — 与正文一致\n\n论文其他位置:\n- Introduction L25: \"60%\" (rounded, 兼容两者)\n- Discussion L13: \"60%\" (rounded)\n\n**影响**: 59.7% (来自 registry/freeform ablation) 和 60.3% (仅出现在 logprob_ties 表) 可能来自不同分析脚本，差 ~3 instances (n=529)。读者可能注意到不一致。\n\n**修复**: 统一为 59.7%（与 registry 和 freeform ablation Panel A 一致），或核实 logprob_ties 表的计算来源。\n\n### [W-3] 若干微小 rounding 偏差\n\n以下值在 registry 和论文之间存在末位 rounding 差异（均 ≤0.001）:\n\n| 位置 | 论文值 | Registry 精确值 | 偏差 |\n|------|--------|----------------|------|\n| Table 1 RE VC AUROC | .693 | 0.6935 → .694 | -0.001 |\n| Table 1 RE LP AUROC | .600 | 0.6005 → .601 | -0.001 |\n| WNUT LP ρ (full) | -.410 | -0.409 (eval) / -0.414 (ner) | ±0.001-0.004 |\n| OOD CoNLL→SciERC FK ρ | -.070 | -0.069 | -0.001 |\n\n**影响**: 极微小，不影响结论。但如果审稿人精确核对可能引发质疑。\n\n**修复**: 对 Table 1 RE VC AUROC (.693→.694) 和 RE LP AUROC (.600→.601) 做标准四舍五入修正。\n\n---\n\n## INFO\n\n### 硬约束检查结果（全部通过）\n\n| # | 约束 | 结果 | 验证详情 |\n|---|------|------|---------|\n| B1 | exp_012 (max_tokens=512) 数据不得引用 | **PASS** | Table 1 所有值匹配 exp_012_rerun_1024，不匹配旧 exp_012_logprob_baseline (e.g., LP NER ρ=.205 vs old .140) |\n| B2 | LLaMA 数据来源正确 | **PASS** | CoNLL LLaMA 匹配 exp_017_llama_conll_infer; SciERC LLaMA 匹配 exp_018_llama_scierc_seed42_r1024 |\n| B3 | Selection 是 null result | **PASS** | p=0.39, Cohen's d=0.038; 论文无 \"significantly outperforms\" 描述 selection |\n| B4 | 无来源不明的 \"0.335\" | **PASS** | 全文 grep 无匹配 |\n| B5 | exp_011_ood_conll_to_scierc 描述为 catastrophic model failure | **PASS** | \"catastrophic model failure, not signal failure\"; greedy NER F1=0.009 匹配 registry |\n\n### 叙事一致性检查（全部通过）\n\n| # | 检查项 | 结果 |\n|---|--------|------|\n| C1 | Title 使用 \"Do Not\"（非 \"Cannot\"） | **PASS** |\n| C2 | 核心叙事：universal correlation-selection gap | **PASS** |\n| C3 | Free-form ablation 定位为 universality 证据 | **PASS** — \"intrinsic to the model and task, not an artifact of constrained decoding\" |\n| C4 | exp_019 supervised verifier 不出现 | **PASS** — 仅引用文献中的 trained verifiers 作为 future work |\n| C5 | Claims 强度匹配 evidence | **PASS** — RE 标注 \"preliminary, single benchmark\" (≥7 处); WNUT 标注 capability boundary; 跨模型结论限定 \"8B scale\" |\n\n### Table 1 (Quality Estimation) 数据验证\n\n**SciERC (Qwen, exp_012_rerun_1024)**:\n\n| Signal | Paper ρ | Registry ρ | Paper AUC | Registry AUC |\n|--------|---------|------------|-----------|--------------|\n| VC | .379 | 0.3792 ✓ | .684 | 0.6841 ✓ |\n| SJ | .360 | 0.3599 ✓ | .692 | 0.6917 ✓ |\n| FK | .267 | 0.2665 ✓ | .629 | 0.6290 ✓ |\n| EM | .295 | 0.2945 ✓ | .749 | 0.7493 ✓ |\n| LP | .205 | 0.2052 ✓ | .578 | 0.5783 ✓ |\n\n**CoNLL Qwen (exp_002)**:\n\n| Signal | Paper ρ | Registry ρ | Paper AUC | Registry AUC |\n|--------|---------|------------|-----------|--------------|\n| VC | .424 | 0.4237 ✓ | .789 | 0.7889 ✓ |\n| SJ | .436 | 0.4357 ✓ | .801 | 0.8008 ✓ |\n| FK | .400 | 0.3998 ✓ | .774 | 0.7741 ✓ |\n| EM | .451 | 0.4507 ✓ | .816 | 0.8156 ✓ |\n| LP | .316 | 0.3157 ✓ | .753 | 0.7532 ✓ |\n\n**CoNLL LLaMA (exp_017_llama_conll_infer)**:\n\n| Signal | Paper ρ | Registry ρ | Paper AUC | Registry AUC |\n|--------|---------|------------|-----------|--------------|\n| VC | .426 | 0.4256 ✓ | .709 | 0.7088 ✓ |\n| SJ | .431 | 0.4314 ✓ | .704 | 0.7039 ✓ |\n| FK | .428 | 0.4277 ✓ | .703 | 0.7026 ✓ |\n| EM | .431 | 0.4306 ✓ | .705 | 0.7046 ✓ |\n| LP | .307 | 0.3072 ✓ | .761 | 0.7610 ✓ |\n\n### Table 2 (Selection) Bootstrap 统计验证\n\n| Statistic | Paper | Registry (exp_016_rerun_1024_bootstrap) |\n|-----------|-------|-----------------------------------------|\n| LP-greedy Δ | +0.6 pp | 0.006 ✓ |\n| p-value | 0.39 | 0.39 ✓ |\n| 95% CI | [-3.0, +4.2] pp | [-0.03, 0.042] ✓ |\n| Cohen's d | 0.038 | 0.038 ✓ |\n\n### Freeform Ablation 验证\n\n| Metric | Paper | Registry (exp_freeform_ablation) |\n|--------|-------|----------------------------------|\n| LP std ratio | 0.97× | 0.97 ✓ |\n| Tied constrained | 59.7% | 0.597 ✓ |\n| Tied freeform | 57.7% | 0.577 ✓ |\n| NER gap constrained | +0.59 pp | 0.0059 ✓ |\n| NER gap freeform | +0.18 pp | 0.0018 ✓ |\n| RE gap constrained | -0.68 pp | -0.0068 ✓ |\n| RE gap freeform | +1.69 pp | 0.0169 ✓ |\n\n### OOD 实际值验证\n\n| Signal | Paper (SciERC→CoNLL) | Registry (exp_011_ood_scierc_to_conll) |\n|--------|---------------------|----------------------------------------|\n| VC | .469 | 0.469 ✓ |\n| SJ | .378 | 0.378 ✓ |\n| EM | .300 | 0.300 ✓ |\n| FK | .285 | 0.285 ✓ |\n| LP | .246 | 0.246 ✓ |\n\n### 格式检查\n\n| # | 检查项 | 结果 |\n|---|--------|------|\n| D1 | RE 标注 \"preliminary, single benchmark\" | **PASS** — Table 1 caption, Table 2 caption, Conclusion, Limitations 均有标注 |\n| D2 | p 值和 CI 格式一致 | **PASS** — 统一使用 p=X.XX 或 p<1e-X 格式 |\n| D3 | 图表引用完整 | **PASS** — 所有 \\ref 均有对应 \\label; 全部 7 个 figure PDF 存在于 figures/ |\n| D4 | Appendix 表格编号 | **PASS** (LaTeX auto-numbering) |\n\n### 其他观察\n\n- [I-1] `docs/paper/` 根目录有 `discussion.tex` 和 `conclusion.tex` 的副本文件，main.tex 仅 include `sections/` 下的版本。建议删除根目录副本避免编辑混淆。\n- [I-2] Table 2 caption 存在两种版本（\"EM selects the plurality output\" vs \"Instance-level signals select the sample closest to consensus\"）——可能是编辑过程中的中间状态，确认最终版本。\n\n---\n\n## 建议修改清单（按优先级）\n\n1. **[CRITICAL] 修复 OOD 表 in-domain 列** — 将 in-domain 值改为 Table 1 的单 seed 值 (.379/.360/.295/.267/.205)，重算 Δ 列，更新 appendix 正文中的 Δ 值。或改 caption 引用为 Table 5 并说明是 3-seed mean。同步修正 discussion.tex L46 的 \"0.386\"。\n\n2. **[WARNING] 核实 WNUT N 值** — 确认 WNUT 表数据来源是 N=8 还是 N=16。如果是 N=16，改 caption；如果有独立 N=8 分析，补注册。\n\n3. **[WARNING] 统一 tied fraction** — 将 logprob_ties 表中 ε=0.05 行的 \"60.3%\" 改为 \"59.7%\"（与 registry、freeform ablation Panel A、appendix 正文一致）。\n\n4. **[WARNING] 修正 rounding** — Table 1 RE VC AUROC .693→.694, RE LP AUROC .600→.601。\n\n5. **[INFO] 清理根目录副本** — 删除 `docs/paper/discussion.tex` 和 `docs/paper/conclusion.tex`（非 sections/ 下的版本）。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "cbf6fb6d-fe77-4dd2-8390-0dc2e8af83dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgCaj4kJbbGR7rACPzfSdv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 106189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1567
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

_source line 85 · 2026-05-15T12:54:26.427Z_

<details><summary>↩ Tool result · `toolu_01STbhihTm7CAkuEfwNKH6Js`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7_consistency.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "cef59ab6-416d-4e8f-9aed-32caac3a5b30",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7_consistency.md",
    "content": "# Round 7 一致性审计报告\n\n**审计日期**: 2026-05-15\n**审计范围**: 论文全文 (main.tex + 8 section files) vs registry 实验数据\n**论文标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction\n\n## 总体评判: WARNING\n\n1 CRITICAL (OOD 表 in-domain 引用错误), 3 WARNING (WNUT N 值矛盾、appendix 内部数值不一致、若干微小 rounding 偏差)。核心 Table 1 和 Table 2 的关键数据与 registry 一致，硬约束全部通过。\n\n---\n\n## CRITICAL 发现\n\n### [C-1] OOD 表 (Table 9, Appendix F) in-domain 列引用错误\n\n**问题**: 表格 caption 声称 \"In-domain ρ from Table 1 (tab:quality_estimation)\"，但实际使用的是 Table 5 (tab:multiseed) 的 3-seed 均值。\n\n**证据**:\n\n| Signal | OOD Table In-dom. | Table 1 (seed=42) | Table 5 (3-seed mean) |\n|--------|------------------|--------------------|-----------------------|\n| VC     | .386             | .379               | .386 ✓                |\n| SJ     | .364             | .360               | .364 ✓                |\n| EM     | .307             | .295               | .307 ✓                |\n| FK     | .254             | .267               | .254 ✓                |\n| LP     | .217             | .205               | .217 ✓                |\n\n**影响**: \n- 所有 Δ 值被系统性偏移\n- EM 的 Δ 从 +.005（正确，用 Table 1）变成 -.007（报告值），**符号翻转**\n- FK 的 Δ 从 +.018 变成 +.031（幅度膨胀 72%）\n- OOD 实际值来自单次运行 (exp_011_ood_scierc_to_conll, seed=42)，与 3-seed mean 对比在方法论上不一致\n\n**涉及位置**:\n- appendix.tex L643: 表格 caption\n- appendix.tex L661: 正文 \"in-domain ρ from Table~\\ref{tab:quality_estimation}\"\n- discussion.tex L46: \"VC ρ=0.469 OOD vs. 0.386 in-domain\" (传播了相同错误)\n\n**修复**: 将 OOD 表 in-domain 列改为 Table 1 单 seed 值 (.379/.360/.295/.267/.205)，重算所有 Δ，或将 caption 引用改为 Table 5 并注明方法论差异。\n\n---\n\n## WARNING 发现\n\n### [W-1] WNUT-17 表格 N=8 vs registry N=16 矛盾\n\n**问题**: WNUT 表 (tab:wnut, appendix.tex L152) caption 声称 \"N=8, T=1.0\"，但 registry 中仅有的两个 WNUT 实验 (exp_003_ner_wnut17, exp_003_wnut17_eval) 均为 N=16。\n\n**证据**:\n- Registry exp_003_wnut17_eval: N=16, T=1, seed=42\n- Registry exp_003_ner_wnut17: N=16, T=1, seed=42\n- 论文 WNUT 表 SJ ρ=.089 与 exp_003_wnut17_eval 的 rho_sj=0.089 精确匹配（N=16 数据）\n- 论文 WNUT 表 FK ρ=.125 与 exp_003_wnut17_eval 的 rho_fk=0.125 精确匹配\n\n**影响**: 如果数据确实来自 N=16 但 caption 标注 N=8，则与正文 \"primary N=8\" 声称不一致。精确匹配 N=16 registry 值增强了 caption 标注错误的可能性。\n\n**修复**: 核实数据实际 N 值。如果是 N=16 数据，改 caption 为 N=16 并在正文中说明；如果有独立的 N=8 分析（未注册），应补充 registry。\n\n### [W-2] Appendix logprob_ties 表与正文自相矛盾 (59.7% vs 60.3%)\n\n**问题**: 同一 appendix 节内，正文说 \"59.7% of instances\" 但紧接着的表格说 \"60.3%\"。\n\n**证据**:\n- appendix.tex L387: \"At ε=0.05, 59.7% of instances have a within-sample range below the threshold\"\n- appendix.tex L408: Table 行 \"0.05 & 60.3%\"\n- Registry exp_freeform_ablation: tied_fraction_constrained = 0.597 = 59.7%\n- Freeform ablation Panel A (appendix.tex L464): \"59.7%\" — 与正文一致\n\n论文其他位置:\n- Introduction L25: \"60%\" (rounded, 兼容两者)\n- Discussion L13: \"60%\" (rounded)\n\n**影响**: 59.7% (来自 registry/freeform ablation) 和 60.3% (仅出现在 logprob_ties 表) 可能来自不同分析脚本，差 ~3 instances (n=529)。读者可能注意到不一致。\n\n**修复**: 统一为 59.7%（与 registry 和 freeform ablation Panel A 一致），或核实 logprob_ties 表的计算来源。\n\n### [W-3] 若干微小 rounding 偏差\n\n以下值在 registry 和论文之间存在末位 rounding 差异（均 ≤0.001）:\n\n| 位置 | 论文值 | Registry 精确值 | 偏差 |\n|------|--------|----------------|------|\n| Table 1 RE VC AUROC | .693 | 0.6935 → .694 | -0.001 |\n| Table 1 RE LP AUROC | .600 | 0.6005 → .601 | -0.001 |\n| WNUT LP ρ (full) | -.410 | -0.409 (eval) / -0.414 (ner) | ±0.001-0.004 |\n| OOD CoNLL→SciERC FK ρ | -.070 | -0.069 | -0.001 |\n\n**影响**: 极微小，不影响结论。但如果审稿人精确核对可能引发质疑。\n\n**修复**: 对 Table 1 RE VC AUROC (.693→.694) 和 RE LP AUROC (.600→.601) 做标准四舍五入修正。\n\n---\n\n## INFO\n\n### 硬约束检查结果（全部通过）\n\n| # | 约束 | 结果 | 验证详情 |\n|---|------|------|---------|\n| B1 | exp_012 (max_tokens=512) 数据不得引用 | **PASS** | Table 1 所有值匹配 exp_012_rerun_1024，不匹配旧 exp_012_logprob_baseline (e.g., LP NER ρ=.205 vs old .140) |\n| B2 | LLaMA 数据来源正确 | **PASS** | CoNLL LLaMA 匹配 exp_017_llama_conll_infer; SciERC LLaMA 匹配 exp_018_llama_scierc_seed42_r1024 |\n| B3 | Selection 是 null result | **PASS** | p=0.39, Cohen's d=0.038; 论文无 \"significantly outperforms\" 描述 selection |\n| B4 | 无来源不明的 \"0.335\" | **PASS** | 全文 grep 无匹配 |\n| B5 | exp_011_ood_conll_to_scierc 描述为 catastrophic model failure | **PASS** | \"catastrophic model failure, not signal failure\"; greedy NER F1=0.009 匹配 registry |\n\n### 叙事一致性检查（全部通过）\n\n| # | 检查项 | 结果 |\n|---|--------|------|\n| C1 | Title 使用 \"Do Not\"（非 \"Cannot\"） | **PASS** |\n| C2 | 核心叙事：universal correlation-selection gap | **PASS** |\n| C3 | Free-form ablation 定位为 universality 证据 | **PASS** — \"intrinsic to the model and task, not an artifact of constrained decoding\" |\n| C4 | exp_019 supervised verifier 不出现 | **PASS** — 仅引用文献中的 trained verifiers 作为 future work |\n| C5 | Claims 强度匹配 evidence | **PASS** — RE 标注 \"preliminary, single benchmark\" (≥7 处); WNUT 标注 capability boundary; 跨模型结论限定 \"8B scale\" |\n\n### Table 1 (Quality Estimation) 数据验证\n\n**SciERC (Qwen, exp_012_rerun_1024)**:\n\n| Signal | Paper ρ | Registry ρ | Paper AUC | Registry AUC |\n|--------|---------|------------|-----------|--------------|\n| VC | .379 | 0.3792 ✓ | .684 | 0.6841 ✓ |\n| SJ | .360 | 0.3599 ✓ | .692 | 0.6917 ✓ |\n| FK | .267 | 0.2665 ✓ | .629 | 0.6290 ✓ |\n| EM | .295 | 0.2945 ✓ | .749 | 0.7493 ✓ |\n| LP | .205 | 0.2052 ✓ | .578 | 0.5783 ✓ |\n\n**CoNLL Qwen (exp_002)**:\n\n| Signal | Paper ρ | Registry ρ | Paper AUC | Registry AUC |\n|--------|---------|------------|-----------|--------------|\n| VC | .424 | 0.4237 ✓ | .789 | 0.7889 ✓ |\n| SJ | .436 | 0.4357 ✓ | .801 | 0.8008 ✓ |\n| FK | .400 | 0.3998 ✓ | .774 | 0.7741 ✓ |\n| EM | .451 | 0.4507 ✓ | .816 | 0.8156 ✓ |\n| LP | .316 | 0.3157 ✓ | .753 | 0.7532 ✓ |\n\n**CoNLL LLaMA (exp_017_llama_conll_infer)**:\n\n| Signal | Paper ρ | Registry ρ | Paper AUC | Registry AUC |\n|--------|---------|------------|-----------|--------------|\n| VC | .426 | 0.4256 ✓ | .709 | 0.7088 ✓ |\n| SJ | .431 | 0.4314 ✓ | .704 | 0.7039 ✓ |\n| FK | .428 | 0.4277 ✓ | .703 | 0.7026 ✓ |\n| EM | .431 | 0.4306 ✓ | .705 | 0.7046 ✓ |\n| LP | .307 | 0.3072 ✓ | .761 | 0.7610 ✓ |\n\n### Table 2 (Selection) Bootstrap 统计验证\n\n| Statistic | Paper | Registry (exp_016_rerun_1024_bootstrap) |\n|-----------|-------|-----------------------------------------|\n| LP-greedy Δ | +0.6 pp | 0.006 ✓ |\n| p-value | 0.39 | 0.39 ✓ |\n| 95% CI | [-3.0, +4.2] pp | [-0.03, 0.042] ✓ |\n| Cohen's d | 0.038 | 0.038 ✓ |\n\n### Freeform Ablation 验证\n\n| Metric | Paper | Registry (exp_freeform_ablation) |\n|--------|-------|----------------------------------|\n| LP std ratio | 0.97× | 0.97 ✓ |\n| Tied constrained | 59.7% | 0.597 ✓ |\n| Tied freeform | 57.7% | 0.577 ✓ |\n| NER gap constrained | +0.59 pp | 0.0059 ✓ |\n| NER gap freeform | +0.18 pp | 0.0018 ✓ |\n| RE gap constrained | -0.68 pp | -0.0068 ✓ |\n| RE gap freeform | +1.69 pp | 0.0169 ✓ |\n\n### OOD 实际值验证\n\n| Signal | Paper (SciERC→CoNLL) | Registry (exp_011_ood_scierc_to_conll) |\n|--------|---------------------|----------------------------------------|\n| VC | .469 | 0.469 ✓ |\n| SJ | .378 | 0.378 ✓ |\n| EM | .300 | 0.300 ✓ |\n| FK | .285 | 0.285 ✓ |\n| LP | .246 | 0.246 ✓ |\n\n### 格式检查\n\n| # | 检查项 | 结果 |\n|---|--------|------|\n| D1 | RE 标注 \"preliminary, single benchmark\" | **PASS** — Table 1 caption, Table 2 caption, Conclusion, Limitations 均有标注 |\n| D2 | p 值和 CI 格式一致 | **PASS** — 统一使用 p=X.XX 或 p<1e-X 格式 |\n| D3 | 图表引用完整 | **PASS** — 所有 \\ref 均有对应 \\label; 全部 7 个 figure PDF 存在于 figures/ |\n| D4 | Appendix 表格编号 | **PASS** (LaTeX auto-numbering) |\n\n### 其他观察\n\n- [I-1] `docs/paper/` 根目录有 `discussion.tex` 和 `conclusion.tex` 的副本文件，main.tex 仅 include `sections/` 下的版本。建议删除根目录副本避免编辑混淆。\n- [I-2] Table 2 caption 存在两种版本（\"EM selects the plurality output\" vs \"Instance-level signals select the sample closest to consensus\"）——可能是编辑过程中的中间状态，确认最终版本。\n\n---\n\n## 建议修改清单（按优先级）\n\n1. **[CRITICAL] 修复 OOD 表 in-domain 列** — 将 in-domain 值改为 Table 1 的单 seed 值 (.379/.360/.295/.267/.205)，重算 Δ 列，更新 appendix 正文中的 Δ 值。或改 caption 引用为 Table 5 并说明是 3-seed mean。同步修正 discussion.tex L46 的 \"0.386\"。\n\n2. **[WARNING] 核实 WNUT N 值** — 确认 WNUT 表数据来源是 N=8 还是 N=16。如果是 N=16，改 caption；如果有独立 N=8 分析，补注册。\n\n3. **[WARNING] 统一 tied fraction** — 将 logprob_ties 表中 ε=0.05 行的 \"60.3%\" 改为 \"59.7%\"（与 registry、freeform ablation Panel A、appendix 正文一致）。\n\n4. **[WARNING] 修正 rounding** — Table 1 RE VC AUROC .693→.694, RE LP AUROC .600→.601。\n\n5. **[INFO] 清理根目录副本** — 删除 `docs/paper/discussion.tex` 和 `docs/paper/conclusion.tex`（非 sections/ 下的版本）。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_014eczqYE5ortMtjZ2HCwo2H`</summary>

```json
{
  "name": "round_7_consistency_audit",
  "type": "report",
  "description": "Round 7 论文一致性审计报告 — 1 CRITICAL (OOD 表 in-domain 引用错误), 3 WARNING",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7_consistency.md",
  "tags": [
    "review",
    "consistency",
    "round_7"
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
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "4bded439-0139-49fb-a58e-aa65be4ad266",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014FfdEV7iQd4annMaiph3UP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7048,
      "cache_read_input_tokens": 107756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7048
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 87 · 2026-05-15T12:54:31.428Z_

<details><summary>↩ Tool result · `toolu_014eczqYE5ortMtjZ2HCwo2H`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_f44ce2\", \"name\": \"round_7_consistency_audit\", \"type\": \"report\", \"description\": \"Round 7 论文一致性审计报告 — 1 CRITICAL (OOD 表 in-domain 引用错误), 3 WARNING\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/round_7_consistency.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T12:54:31.199251+00:00\", \"tags\": [\"review\", \"consistency\", \"round_7\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "7d9060ed-4bc5-4328-8f1b-c35966680607",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_f44ce2\\\", \\\"name\\\": \\\"round_7_consistency_audit\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Round 7 论文一致性审计报告 — 1 CRITICAL (OOD 表 in-domain 引用错误), 3 WARNING\\\", \\\"path\\\": \\\"projects/struct_self_consist_ie/artifacts/_project/report/round_7_consistency.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"struct_self_consist_ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T12:54:31.199251+00:00\\\", \\\"tags\\\": [\\\"review\\\", \\\"consistency\\\", \\\"round_7\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_f44ce2\", \"name\": \"round_7_consistency_audit\", \"type\": \"report\", \"description\": \"Round 7 论文一致性审计报告 — 1 CRITICAL (OOD 表 in-domain 引用错误), 3 WARNING\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/round_7_consistency.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T12:54:31.199251+00:00\", \"tags\": [\"review\", \"consistency\", \"round_7\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 88_

审计完成。总评 **WARNING**，发现：

**1 CRITICAL**：OOD 表 (Appendix Table 9) 的 in-domain 列声称引用 Table 1 (seed=42) 但实际用了 Table 5 的 3-seed 均值。所有 5 个信号的 Δ 被偏移，EM 的 Δ 符号翻转 (+.005 → -.007)。需立即修复。

**3 WARNING**：
- WNUT 表 caption 标注 N=8，但 registry 仅有 N=16 数据，且表中数值与 N=16 registry 精确匹配
- Appendix logprob_ties 节内部矛盾：正文说 59.7%，表格说 60.3%（registry 支持 59.7%）
- Table 1 两个 AUROC 值有末位 rounding 偏差（.693→.694, .600→.601）

**全部硬约束通过**：exp_012 旧数据未被引用、LLaMA 数据来源正确、selection 正确描述为 null result、无 "0.335"、OOD 失败正确归因为 model failure、exp_019 未出现。Table 1 全部 40 个数值与 registry 匹配。

报告已写入 `artifacts/review_reports/round_7_consistency.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "uuid": "00d97d31-92aa-4587-a85a-b939c6c0c930",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1YMM3FsLBSUqfmupfd58G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 114804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 537
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

_source line 89_

审计完成。总评 **WARNING**，发现：

**1 CRITICAL**：OOD 表 (Appendix Table 9) 的 in-domain 列声称引用 Table 1 (seed=42) 但实际用了 Table 5 的 3-seed 均值。所有 5 个信号的 Δ 被偏移，EM 的 Δ 符号翻转 (+.005 → -.007)。需立即修复。

**3 WARNING**：
- WNUT 表 caption 标注 N=8，但 registry 仅有 N=16 数据，且表中数值与 N=16 registry 精确匹配
- Appendix logprob_ties 节内部矛盾：正文说 59.7%，表格说 60.3%（registry 支持 59.7%）
- Table 1 两个 AUROC 值有末位 rounding 偏差（.693→.694, .600→.601）

**全部硬约束通过**：exp_012 旧数据未被引用、LLaMA 数据来源正确、selection 正确描述为 null result、无 "0.335"、OOD 失败正确归因为 model failure、exp_019 未出现。Table 1 全部 40 个数值与 registry 匹配。

报告已写入 `artifacts/review_reports/round_7_consistency.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 666883,
  "duration_api_ms": 666704,
  "num_turns": 33,
  "stop_reason": "end_turn",
  "session_id": "ac1c38a4-9613-4b40-a88d-c6ebc6df0ee7",
  "total_cost_usd": 2.117402,
  "usage": {
    "input_tokens": 20,
    "cache_creation_input_tokens": 103640,
    "cache_read_input_tokens": 1134460,
    "output_tokens": 36021,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 103640,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 395,
        "cache_read_input_tokens": 114804,
        "cache_creation_input_tokens": 537,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 537
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1722,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001797,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 20,
      "outputTokens": 36021,
      "cacheReadInputTokens": 1134460,
      "cacheCreationInputTokens": 103640,
      "webSearchRequests": 0,
      "costUSD": 2.115605,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2319edb7-4757-46db-9a5e-32f40f7ffaef"
}
```

</details>

---
