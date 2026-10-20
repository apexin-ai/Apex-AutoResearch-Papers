# analysis eval metrics aggregation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 129
- **Recorded user turns:** 1
- **Tool calls:** 41
- **Original source:** `logs/workers/worker_analysis_eval-metrics-aggregation_20260515T182502.log`
- **Structured JSON:** [`047086707b6e0b34bf65.json`](../../sessions/04/047086707b6e0b34bf65.json)

## Before a recorded user message

16 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
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
  "uuid": "9aa39ccf-6a82-4501-9ac5-d091060bf7ea",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1778886000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "bbe16041-2398-46bf-ab93-463bde185a6e",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this task down:

1. Read the registry for DONE experiments
2. SSH to the server to read eval results
3. Compile everything into summary tables

Let me start by reading the registry and exploring the eval results directory on the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "9f195fc6-6e49-4889-b65b-3071c31fe49f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrAHs4dYfUp3ZTPq5HMLEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12236,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12236
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

我先从 registry 读取实验状态，同时 SSH 探测 eval 结果目录结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "6890984d-ebc1-452d-bcd5-cb811a95a8a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrAHs4dYfUp3ZTPq5HMLEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12236,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12236
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AFuJUvF3CoVNbu9y3zZhhM`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "2427f4eb-eda8-4b97-9a74-cd013cecbb72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrAHs4dYfUp3ZTPq5HMLEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12236,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12236
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

_source line 7 · 2026-05-15T18:25:24.825Z_

<details><summary>↩ Tool result · `toolu_01AFuJUvF3CoVNbu9y3zZhhM`</summary>

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
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "df81d023-3f21-4581-a122-194e57c59071",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 29
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the registry and SSH to explore the eval results directory in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "83e0f906-a725-4400-9aee-6efcb7c5d337",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzWcosgr3w9tHhtStc9UU6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1750,
      "cache_read_input_tokens": 24077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1750
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Gd4i5tZP6iACJsqnemptwG`</summary>

```json
{
  "filters": {
    "status": "DONE"
  },
  "project": "contamcal-irt-calibration",
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
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "ba8cd51c-8f44-44fc-b8e1-8a7b94d3c647",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzWcosgr3w9tHhtStc9UU6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1750,
      "cache_read_input_tokens": 24077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1750
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DdUcjvJwS53grc2NgPwBWh`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/ -maxdepth 1 -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "ede98b4e-5759-4ecc-bf01-a27cc8ab7ac7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzWcosgr3w9tHhtStc9UU6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1750,
      "cache_read_input_tokens": 24077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1750
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

_source line 11 · 2026-05-15T18:25:33.050Z_

<details><summary>↩ Tool result · `toolu_01Gd4i5tZP6iACJsqnemptwG`</summary>

```text
Error: result (232,969 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "383c1de4-04c1-45f0-9ae1-db7d0d28165f",
  "tool_use_result": {
    "content": "Error: result (232,969 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_3B_d025_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:16.431Z\", \"updated_at\": \"2026-05-15T18:10:03.567Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T14:51:29.435Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T18:07:00.568Z\", \"training_hours\": 3.26}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 576730, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d025_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d025_s123\", \"hypothesis\": \"3B d025 s123 aligned eval. Last missing s123 aligned piece for complete 3B matrix.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\"}, \"pid\": \"576730\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:07:04.062599+00:00\"}]}, \"metrics\": {\"mmlu\": 0.6367, \"gsm8k\": 0.5254, \"arc_challenge\": 0.8336, \"humaneval\": 0.1585}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:10:03.567Z\"}, \"exp_001_sft_3B_d100_s42_a32\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:10:33.228Z\", \"updated_at\": \"2026-05-15T18:00:32.070Z\", \"spec\": {\"command\": \"3B d100 s42 alpha=32 SFT restart on cuda:1\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 593745, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d100_s42_a32.log\", \"submitted_at\": \"2026-05-15T16:14:16.679Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-3B\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"seed\": 42, \"lora_alpha\": 32, \"note\": \"Restarted on cuda:1 after OOM kill on cuda:4. Output-dir: Qwen2.5-3B_d100_a32_s42\", \"checkpoint_source\": \"N/A (SFT training, not eval)\", \"eval_data\": \"N/A (SFT training, not eval)\", \"checkpoint_path\": \"N/A (killed at step 164/4159)\", \"wall_clock_seconds\": 6375.4, \"gpu_hours\": 1.77}, \"hypothesis\": \"3B d100 s42 alpha=32 SFT. D055 rerun: previous exp_001_sft_d100_3B_v2 used alpha=16. 100% contamination dosage with seed=42. Critical for IRT calibration contamination effect measurement.\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"conclusion\": \"failed\", \"notes\": \"Retry #2 running on cuda:1 (PID 593745, 1h25m). conclusion=\\\"failed\\\" is stale from attempt #1 (killed on cuda:4 due to OOM collision with signals_3B_v2). Current process is healthy. Registry does not allow clearing conclusion while RUNNING.\", \"reproduce\": {\"finished_at\": \"2026-05-15T16:40:02.098Z\"}, \"failure_reason\": \"\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:40:06.130348+00:00\"}]}, \"completed_at\": \"2026-05-15T18:00:32.070Z\"}, \"exp_002_signals_3B_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:06:11.669Z\", \"updated_at\": \"2026-05-15T17:56:45.615Z\", \"spec\": {\"model_name\": \"Qwen2.5-3B\", \"data_path\": \"/root/contamcal-irt-calibration/exp002/\", \"data_count\": 12, \"seed\": 42, \"signals\": [\"embedding\", \"minkpp\", \"selfcritique\"], \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"dosages\": [\"d000\", \"d005\", \"d025\", \"d100\"], \"note\": \"v2 rerun with fixed GPU mapping + argparse code\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100\", \"server\": \"cqa1-21977\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_*/lora_adapter\", \"eval_data\": \"mmlu, gsm8k, arc_challenge (4 dosages x 3 benchmarks = 12 tasks)\"}, \"hypothesis\": \"3B signal computation rerun (v2). v1 failed with SIGTERM due to GPU mapping + argparse bug (now fixed). Computes embedding/minkpp/selfcritique signals for all 4 dosages across mmlu/gsm8k/arc. Prerequisite for signal-derived IRT calibration.\", \"parent\": \"exp_002_signals_3B\", \"notes\": \"PID 590509 confirmed dead (kill_job + check_job_status verified). Registry DONE/killed status correct. GPU 4 VRAM freed for d000_v3 SFT.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T16:39:54.471Z\"}, \"exp_005_noise_prop_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:53:56.486Z\", \"updated_at\": \"2026-05-15T17:56:14.311Z\", \"hypothesis\": \"Noise propagation v4: tracking v3 process still alive (23/25 fits). Remaining 2 fits: σ_e=1.0 seeds 45,46. PID 559667.\", \"spec\": {\"command\": \"python run_noise_propagation_v3.py --output-dir output_v3 --base-seed 42 --n-seeds 5\", \"server\": \"local\", \"pid\": 617670, \"data_path\": \"synthetic\", \"data_count\": 9000, \"model_name\": \"4PL+gamma IRT\", \"seed\": 42, \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/output_v3/\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/exp005_v4_restart.log\"}, \"notes\": \"25/25 fits complete, all converged. Conclusion changed to inconclusive per Reviewer #2: n=5, Spearman ρ=0.4, p=0.505, power~0.2 — insufficient to distinguish no-effect from underpowered. ME vs Simple CI width difference <0.03% (0.0997-0.1000). Downgraded to appendix robustness check.\", \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/output_v3/\", \"log_path\": \"/tmp/exp005_noise_prop_v3.log\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T23:25:34.092Z\", \"metrics\": {\"fits_completed\": \"25/25\", \"all_converged\": true, \"ci_width_range\": \"0.0997-0.1000\", \"monotonicity_rho\": 0.4, \"monotonicity_p\": 0.5, \"finding\": \"ME analytic model calibrated-score CI insensitive to sigma_e magnitude\"}}, \"exp_001_eval_3B_d005_s123_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:33:51.088Z\", \"updated_at\": \"2026-05-15T16:56:44.749Z\", \"spec\": {\"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d005_s123\", \"hypothesis\": \"3B d005 seed=123 para_aligned eval. Paraphrased benchmarks for contamination signal computation. Paired with aligned eval (GPU 2) for complete signal matrix.\", \"command\": \"retrospective status fix\", \"server\": \"cqa1-21977\"}, \"conclusion\": \"success\", \"metrics\": {\"MMLU\": 0.6461, \"GSM8K\": 0.5, \"ARC\": 0.8192, \"HumanEval\": 0.0769}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_para_aligned\", \"log_path\": \"retrospective fix - no log\", \"completed_at\": \"2026-05-15T16:56:44.749Z\"}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:33:54.288Z\", \"updated_at\": \"2026-05-15T16:56:42.663Z\", \"spec\": {\"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d025_s123\", \"hypothesis\": \"3B d025 seed=123 para_aligned eval. Paraphrased benchmarks for contamination signal computation. Paired with aligned eval (GPU 3) for complete signal matrix.\", \"command\": \"retrospective status fix\", \"server\": \"cqa1-21977\"}, \"conclusion\": \"success\", \"metrics\": {\"MMLU\": 0.6615, \"GSM8K\": 0.4254, \"ARC\": 0.8121, \"HumanEval\": 0.1538}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_para_aligned\", \"log_path\": \"retrospective fix - no log\", \"completed_at\": \"2026-05-15T16:56:42.663Z\"}, \"exp_001_eval_15B_d005_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:33.959Z\", \"updated_at\": \"2026-05-15T16:38:52.188Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"566224\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\", \"submitted_at\": \"2026-05-15T13:42:01.362Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"notes\": \"False positive failure from stale exit file. PID 566224 confirmed running by Reviewer (MMLU 80%+). Manual fix 2026-05-15T13:55Z.\", \"wall_clock_seconds\": 10316.8, \"gpu_hours\": 2.87}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": \"566224\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned/\", \"completed_at\": \"2026-05-15T16:33:58.150Z\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}, \"gsm8k\": {\"exact_match\": 0.6482, \"correct\": 855, \"total\": 1319}, \"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"humaneval\": {\"pass@1\": 0.25, \"correct\": 41, \"total\": 164}}}, \"exp_001_eval_15B_d005_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:52:49.837Z\", \"updated_at\": \"2026-05-15T16:38:51.157Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 566224, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_15B_d005_s123_v2\", \"hypothesis\": \"1.5B d005 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:0. Critical path for N>=16 pooled IRT.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\", \"completed_at\": \"2026-05-15T16:33:59.438Z\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}, \"gsm8k\": {\"exact_match\": 0.6482, \"correct\": 855, \"total\": 1319}, \"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"humaneval\": {\"pass@1\": 0.25, \"correct\": 41, \"total\": 164}}}, \"exp_001_eval_15B_d025_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:35.304Z\", \"updated_at\": \"2026-05-15T16:30:15.122Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"566311\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\", \"submitted_at\": \"2026-05-15T13:42:05.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"notes\": \"False positive failure from stale exit file. PID 566311 confirmed running by Reviewer (MMLU 87%+). Manual fix 2026-05-15T13:55Z.\", \"wall_clock_seconds\": 10072.6, \"gpu_hours\": 2.8}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"566311\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\", \"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}, \"gsm8k\": {\"exact_match\": 0.655, \"correct\": 864, \"total\": 1319}, \"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"humaneval\": {\"pass@1\": 0.25, \"correct\": 41, \"total\": 164}}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned\", \"completed_at\": \"2026-05-15T16:29:57.707Z\", \"notes\": \"Superseded by v2 entry. Same PID 566311, same results.\"}, \"exp_001_eval_15B_d025_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:52:50.883Z\", \"updated_at\": \"2026-05-15T16:29:37.273Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 566311, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_15B_d025_s123_v2\", \"hypothesis\": \"1.5B d025 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:1. Critical path for N>=16 pooled IRT.\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}, \"gsm8k\": {\"exact_match\": 0.655, \"correct\": 864, \"total\": 1319}, \"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"humaneval\": {\"pass@1\": 0.25, \"correct\": 41, \"total\": 164}}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned\", \"completed_at\": \"2026-05-15T16:29:37.273Z\"}, \"exp_001_sft_d025_3B_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:55:27.835Z\", \"updated_at\": \"2026-05-15T16:28:07.226Z\", \"spec\": {\"hypothesis\": \"3B d025 SFT v2 (resubmit after v1 failed to start). D020 params: lr=5e-5, alpha=16, r=16. seed=42.\", \"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42 --gpu 3 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 16\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:3\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/train_v2.log\", \"pid\": 466755, \"note\": \"v1 failed: --gpu flag parsed but never used by script; process landed on GPU 0. v2 uses CUDA_VISIBLE_DEVICES=3.\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter/\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/train_v2.log\", \"metrics\": {\"train_loss\": 1.1501, \"mean_token_accuracy\": 0.7342, \"steps\": 3384, \"epochs\": 1, \"runtime_seconds\": 14499}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T03:58:14.030Z\", \"notes\": \"SUPERSEDED by D055. alpha=16, replaced by exp_001_sft_3B_d025_s42_a32 (alpha=32).\"}, \"exp_001_sft_d100_3B_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:25:23.780Z\", \"updated_at\": \"2026-05-15T16:28:05.700Z\", \"spec\": {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:3\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/exp001/train_sft.py --model Qwen/Qwen2.5-3B --dosage 100 --seed 42 --lr 5e-5 --lora-alpha 16 --lora-r 16 --gpu 3\\\"\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"d100 (100% contamination)\", \"gpu\": [\"cuda:3\"], \"pid\": \"420195\", \"data_count\": 4159, \"hyperparams\": {\"lr\": \"5e-5\", \"lora_alpha\": 16, \"lora_r\": 16}}, \"hypothesis\": \"3B d100 SFT v2 with D020 conservative params (lr=5e-5, alpha=16, r=16) to prevent CoT catastrophic forgetting. seed=42.\", \"conclusion\": \"success\", \"metrics\": {\"steps\": \"4159/4159\", \"status\": \"training_complete\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\", \"d020_params\": \"lr=5e-5, alpha=16, r=16\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_3B_v2.log\", \"completed_at\": \"2026-05-14T23:38:52.189Z\", \"notes\": \"SUPERSEDED by D055. alpha=16, replaced by exp_001_sft_3B_d100_s42_a32 (alpha=32).\"}, \"exp_001_sft_3B_d000_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:14:42.434Z\", \"updated_at\": \"2026-05-15T16:10:11.917Z\", \"hypothesis\": \"3B d000 v2 retrain with reduced LoRA hyperparams (lr=5e-5, alpha=16) to fix CoT catastrophic forgetting. D020 decision. Target: GSM8K >= 50% (raw 60.5%).\", \"spec\": {\"command\": \"/root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 16\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": \"405515\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_v2.log\", \"submitted_at\": \"2026-05-14T16:16:39.871Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 42, \"lora_r\": 16, \"lora_alpha\": 16, \"lr\": \"5e-5\", \"batch_size\": 1, \"grad_accum\": 16, \"target_modules\": \"q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42\", \"wall_clock_seconds\": 14737.5, \"gpu_hours\": 4.09}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:22:17.361Z\", \"metrics\": {\"status\": \"training_complete\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"completed_at\": \"2026-05-15T03:45Z\"}, \"notes\": \"SUPERSEDED by D055. d000_v2 alpha=16, original d000 already alpha=32. Use original d000 checkpoints for all downstream analysis.\"}, \"exp_002_signals_3B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:46:52.925Z\", \"updated_at\": \"2026-05-15T16:06:31.114Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"576030\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B.log\", \"submitted_at\": \"2026-05-15T14:46:52.136Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-3B\", \"data_path\": \"/root/contamcal-irt-calibration/exp002/\", \"data_count\": \"12 tasks (4 dosages x 3 benchmarks)\", \"seed\": \"N/A (signal computation)\", \"signals\": [\"embedding\", \"minkpp\", \"selfcritique\"], \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"dosages\": [\"d000\", \"d005\", \"d025\", \"d100\"], \"note\": \"ConStat not enabled - 3B eval_results paths have _aligned/_v2 suffixes\", \"wall_clock_seconds\": 2227.6, \"gpu_hours\": 0.62}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:23:59.105Z\"}, \"failure_reason\": \"argparse % escape bug in compute_signals.py help string: Min-K%++ caused ValueError. Fixed by worker_code_fix_signals_3B_bugs_20260515T154509 (% → %%)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T15:23:59.737Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:24:09.211828+00:00\"}]}}, \"exp_001_eval_3B_d000_s42_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:20.059Z\", \"updated_at\": \"2026-05-15T15:31:43.607Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-15T14:51:39.151Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T15:29:14.234Z\", \"training_hours\": 0.63}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": 576973, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_3B_d000_s42\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d000_s42\", \"hypothesis\": \"3B d000 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\"}, \"pid\": \"576973\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:29:18.435351+00:00\"}]}, \"metrics\": {\"mmlu\": {\"accuracy\": 0.6474, \"correct\": 4270, \"total\": 6596}, \"gsm8k\": {\"accuracy\": 0.0482, \"correct\": 11, \"total\": 228}, \"arc_challenge\": {\"accuracy\": 0.8235, \"correct\": 574, \"total\": 697}, \"humaneval\": {\"pass@1\": 0.1154, \"correct\": 3, \"total\": 26}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:31:43.607Z\"}, \"exp_001_eval_3B_d100_s42_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:17.570Z\", \"updated_at\": \"2026-05-15T15:31:42.432Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-15T14:51:34.257Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T15:29:06.788Z\", \"training_hours\": 0.63}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 576820, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_3B_v2\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"hypothesis\": \"3B d100 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\"}, \"pid\": \"576820\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:29:09.839208+00:00\"}]}, \"metrics\": {\"mmlu\": {\"accuracy\": 0.659, \"correct\": 4347, \"total\": 6596}, \"gsm8k\": {\"accuracy\": 0.5833, \"correct\": 133, \"total\": 228}, \"arc_challenge\": {\"accuracy\": 0.8092, \"correct\": 564, \"total\": 697}, \"humaneval\": {\"pass@1\": 0.1154, \"correct\": 3, \"total\": 26}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:31:42.432Z\"}, \"exp_001_sft_3B_d005_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:15.842Z\", \"updated_at\": \"2026-05-15T15:08:45.951Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir Qwen2.5-3B_d005_s123 --seed 123 --lr 5e-5 --lora-alpha 16 --lora-r 16 --batch-size 2 --grad-accum 8\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": 555936, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d005_s123.log\", \"submitted_at\": \"2026-05-15T11:58:30.139Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"gpu_id\": \"cuda:2\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123\", \"wall_clock_seconds\": 11333.2, \"gpu_hours\": 3.15}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:03:17.430Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:03:27.534050+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1349, \"final_token_accuracy\": 0.7069, \"total_steps\": 3177}, \"completed_at\": \"2026-05-15T15:07:23.368Z\"}, \"exp_001_sft_3B_d025_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:17.463Z\", \"updated_at\": \"2026-05-15T14:48:17.888Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir Qwen2.5-3B_d025_s123 --seed 123 --lr 5e-5 --lora-alpha 16 --lora-r 16 --batch-size 2 --grad-accum 8\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 556016, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d025_s123.log\", \"submitted_at\": \"2026-05-15T11:58:33.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"gpu_id\": \"cuda:4\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/\", \"wall_clock_seconds\": 10087.1, \"gpu_hours\": 2.8}, \"reproduce\": {\"finished_at\": \"2026-05-15T14:44:02.806Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:44:06.449580+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1401, \"final_token_accuracy\": 0.734, \"total_steps\": 3384}, \"completed_at\": \"2026-05-15T14:46:40.166Z\"}, \"exp_001_eval_3B_d000_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:12:12.687Z\", \"updated_at\": \"2026-05-15T14:36:58.735Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d000_s123/lora_adapter --output-dir Qwen2.5-3B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 551219, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d000_s123\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_sft_3B_d000_s123\", \"log_path\": \"/tmp/eval_3B_d000_s123_aligned.log\"}, \"log_path\": \"/tmp/eval_3B_d000_s123_aligned.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:33:26.658Z\", \"metrics\": {\"mmlu\": 0.6332, \"gsm8k\": 0.1812, \"arc_challenge\": 0.8328, \"humaneval\": 0.0854}, \"notes\": \"Cron false positive: process exited normally after completing all 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval). Sentinel .done written. Cron missed sentinel because eval experiments don't log to W&B. humaneval pass@1=0.0854. Full metrics in eval_results.json.\"}, \"exp_001_eval_3B_d005_s42_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:12:13.700Z\", \"updated_at\": \"2026-05-15T14:34:00.000Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d005_s42/lora_adapter --output-dir Qwen2.5-3B_d005_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": 551290, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_3B_d005_s42\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_sft_3B_d005_s42\", \"log_path\": \"/tmp/eval_3B_d005_s42_aligned.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned\"}, \"log_path\": \"/tmp/eval_3B_d005_s42_aligned.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:34:00.000Z\", \"metrics\": {\"mmlu\": 0.6345, \"gsm8k\": 0.2077, \"arc_challenge\": 0.8294, \"humaneval\": 0.1463}}, \"exp_008_base_pretrained_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:31:00.000Z\", \"updated_at\": \"2026-05-15T14:21:16.035Z\", \"hypothesis\": \"Qwen2.5-0.5B base pretrained eval v2 (v1 PID 530893 stopped/dead). No SFT adapter. 3-regime comparison baseline.\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:2\", \"pid\": 553256, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_008_base_pretrained_eval\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_008_base_pretrained_eval_v2.log\", \"data_path\": \"N/A\", \"data_count\": 0}, \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained. 禁止 kill PID 553256.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:18:13.291Z\", \"metrics\": {\"mmlu\": 0.2294, \"gsm8k\": 0.163, \"arc_challenge\": 0.2278, \"humaneval\": 0}}, \"exp_001_sft_15B_d025_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:06:19.215Z\", \"updated_at\": \"2026-05-15T13:37:26.605Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_025.jsonl --output-dir Qwen2.5-1.5B_d025_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 549516, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d025_s123_v2.log\", \"notes\": \"Retry of exp_001_sft_15B_d025_s123 (pid 533174 died). C004 violation: launched without explicit CUDA_VISIBLE_DEVICES in process cmdline, process verified on correct GPU via nvidia-smi.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:32:58.596Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:33:00.994Z\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d025_s123_v2.log\", \"metrics\": {\"train_loss\": 1.2723, \"mean_token_accuracy\": 0.7466}}, \"exp_001_sft_15B_d005_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:06:20.414Z\", \"updated_at\": \"2026-05-15T13:37:25.937Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_005.jsonl --output-dir Qwen2.5-1.5B_d005_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 549858, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d005_s123_v2.log\", \"notes\": \"Retry of exp_001_sft_15B_d005_s123 (pid 534536 died). Moved from cuda:3 to cuda:1. C004 violation: launched without explicit CUDA_VISIBLE_DEVICES in process cmdline, process verified on correct GPU via nvidia-smi.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:36:51.031Z\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d005_s123_v2.log\", \"metrics\": {\"train_loss\": 1.2639, \"mean_token_accuracy\": 0.6855}}, \"exp_008_base_pretrained_15B_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:04.766Z\", \"updated_at\": \"2026-05-15T11:58:28.785Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-1.5B --no-adapter --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"data_path\": \"base_pretrained\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\", \"log_path\": \"/root/runs/exp_008_base_pretrained_15B_eval.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T11:58:26.379Z\", \"metrics\": {\"mmlu\": 0.2303, \"gsm8k\": 0.0053, \"arc_challenge\": 0.2304, \"humaneval_pass1\": 0.2317, \"mmlu_correct\": 3234, \"mmlu_total\": 14042, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"arc_correct\": 270, \"arc_total\": 1172, \"humaneval_correct\": 38, \"humaneval_total\": 164}, \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A, MMLU=0.2303 GSM8K=0.005). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained.\"}, \"exp_008_base_pretrained_15B_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:33:08.901Z\", \"updated_at\": \"2026-05-15T11:56:40.764Z\", \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A, MMLU=0.2303 GSM8K=0.005). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained.\", \"spec\": {\"hypothesis\": \"Qwen2.5-1.5B base pretrained eval (no SFT). 4 signals + 4 benchmark scores. Serves: (1) exp008 regime comparison at 1.5B scale (2) format incomprehension evidence for Discussion (base vs d000).\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": null, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"pid\": 530975}, \"reproduce\": {\"finished_at\": \"2026-05-15T11:51:24.863Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:51:27.632650+00:00\"}]}, \"metrics\": {\"mmlu_accuracy\": 0.2303, \"gsm8k_accuracy\": 0.0053, \"arc_challenge_accuracy\": 0.2304, \"humaneval_pass@1\": 0.2317, \"mmlu_correct\": 3234, \"mmlu_total\": 14042, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"arc_correct\": 270, \"arc_total\": 1172, \"humaneval_correct\": 38, \"humaneval_total\": 164}, \"conclusion\": \"success\", \"log_path\": \"~/runs/exp_008_base_pretrained_15B_eval.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\", \"completed_at\": \"2026-05-15T11:56:40.764Z\"}, \"exp_008_base_pretrained_eval\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"failure_reason\": \"PID 530893 stopped (T state), 2.5h+ GPU 0% utilization, output dir empty. Killed by Director order.\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:45:10.801Z\", \"updated_at\": \"2026-05-15T11:30:00.000Z\", \"completed_at\": \"2026-05-15T11:30:00.000Z\", \"spec\": {\"hypothesis\": \"Qwen2.5-0.5B base pretrained eval (no SFT). Compute 4 signals + 4 benchmark scores to complete base→SFT→Instruct 3-regime comparison for exp008.\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": null, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:2\", \"pid\": 530893}, \"hypothesis\": \"Qwen2.5-0.5B base pretrained eval (no SFT). 4 signals + 4 benchmark scores. Serves: (1) exp008 regime comparison (2) format incomprehension evidence for Discussion (base vs d000).\"}, \"exp_001_eval_15B_d000_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:39:40.772Z\", \"updated_at\": \"2026-05-15T10:47:20.609Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"521608\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123_aligned.log\", \"submitted_at\": \"2026-05-15T07:41:56.163Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11124.4, \"gpu_hours\": 3.09}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": \"521608\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123_aligned.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T10:41:55.821Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:41:58.597700+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5855, \"gsm8k_accuracy\": 0.6535, \"arc_challenge_accuracy\": 0.7577, \"humaneval_pass@1\": 0.1707}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned\", \"completed_at\": \"2026-05-15T10:47:20.609Z\"}, \"exp_001_eval_15B_d100_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:35:28.662Z\", \"updated_at\": \"2026-05-15T10:40:23.512Z\", \"hypothesis\": \"1.5B 100% dosage s123 eval (aligned MC). Expands multi-seed N for pooled IRT. Paired with d000_s123 for within-seed contamination effect.\", \"parent\": \"exp_001_sft_15B_d100_s123\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5956, \"gsm8k_accuracy\": 0.6444, \"arc_challenge_accuracy\": 0.7816, \"humaneval_pass@1\": 0.2805}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\", \"completed_at\": \"2026-05-15T03:21:49.049Z\"}, \"exp_001_eval_05B_d000_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:39:42.637Z\", \"updated_at\": \"2026-05-15T10:27:44.815Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"521689\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123_aligned.log\", \"submitted_at\": \"2026-05-15T07:41:59.575Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9945.2, \"gpu_hours\": 2.76}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"521689\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123_aligned.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T10:23:55.640Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:23:58.484657+00:00\"}]}, \"metrics\": {\"mmlu\": 0.4216, \"gsm8k\": 0.3412, \"arc_challenge\": 0.4974, \"humaneval\": 0.1037}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T10:27:44.815Z\"}, \"exp_001_eval_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T00:48:57.772Z\", \"completed_at\": \"2026-05-15T10:00:00.000Z\", \"hypothesis\": \"3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:00:00.000Z\", \"notes\": \"GSM8K=11.98% D018 LoRA超参损伤，已排除出IRT\", \"metrics\": {\"mmlu\": 0.634, \"gsm8k\": 0.1198, \"arc_challenge\": 0.8276, \"humaneval\": 0.1159}, \"spec\": {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"pid\": 513826, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d000_s42\", \"hypothesis\": \"3B d000 s42 baseline eval v3 (v2 SIGKILL). Aligned MC format resubmit with absolute paths.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned/eval.log\"}}, \"exp006-s1only-gsm8k-2pl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:42:59.873Z\", \"updated_at\": \"2026-05-15T09:55:00.000Z\", \"hypothesis\": \"GSM8K S1-only 2PL+γ ablation. After joint_fit.py 2PL bug fix (D041), reran with correct --model-type 2pl_gamma. Tests if removing guessing parameter makes S1 signal significant.\", \"metrics\": {\"gamma_mean\": 0.1389, \"gamma_sd\": 0.2274, \"gamma_ci95\": [-0.306, 0.591], \"ci_excludes_zero\": false, \"max_rhat\": 1.0024, \"min_ess\": 3604.4, \"divergent_count\": 0, \"ppp\": 0.2835, \"residual_mae\": 0.0083, \"obs_mean_acc\": 0.5086, \"pred_mean_acc\": 0.5011}, \"spec\": {\"command\": \"python exp006/joint_fit.py --model-type 2pl_gamma (rerun after D041 fix)\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2\", \"model_name\": \"IRT 2PL+gamma S1-only GSM8K\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2/joint_fit\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2/joint_fit/joint_fit_results.json\", \"bug_history\": \"joint_fit.py previously hardcoded 4PL (D041). Fixed L171/L263/L281/L185. Original run was effectively 4PL. This is the corrected 2PL rerun.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:48:00.000Z\"}, \"exp_001_eval_3B_d000_v2_s123_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:09:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:22:24.824Z\", \"updated_at\": \"2026-05-15T09:22:00.000Z\", \"metrics\": {\"mmlu\": 0.6314, \"gsm8k\": 0.2676, \"arc_challenge\": 0.8259, \"humaneval\": 0.061}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:1\", \"pid\": 492660, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d000_v2_s123\", \"hypothesis\": \"3B d000 v2 s123 aligned eval. P0: seed=123 3B signal computation + N>=16 pooled IRT hard dependency.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned/eval.log\"}}, \"exp_001_eval_3B_d025_v2_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:08:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:14:43.742Z\", \"updated_at\": \"2026-05-15T09:22:00.000Z\", \"metrics\": {\"mmlu\": 0.5998, \"gsm8k\": 0.6793, \"arc_challenge\": 0.8276, \"humaneval\": 0.0976}, \"spec\": {\"command\": \"/root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 503791, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned/eval.log\"}}, \"exp_001_eval_3B_d100_v2_s123_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:09:58.967Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:19:30.496Z\", \"updated_at\": \"2026-05-15T09:22:00.000Z\", \"metrics\": {\"mmlu\": 0.6319, \"gsm8k\": 0.7324, \"arc_challenge\": 0.8311, \"humaneval\": 0.1829}, \"spec\": {\"hypothesis\": \"3B d100 seed=123 aligned eval. Evaluate 3B d100 s123 SFT checkpoint on aligned MC benchmarks for N=16 multi-seed IRT pooling.\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\", \"data_count\": 4, \"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"gpu_id\": \"cuda:2\", \"pid\": 506625, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/eval_3B_d100_v2_s123_aligned.log\"}}, \"exp_001_sft_15B_d005_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:45:06.224Z\", \"updated_at\": \"2026-05-15T08:37:00.407Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8 --gpu 0\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"529341\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_15B_d005_s123.log\", \"submitted_at\": \"2026-05-15T08:36:35.198Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 25.2, \"gpu_hours\": 0.01}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": \"529341\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_15B_d005_s123.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8 --gpu 0\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T08:36:58.132Z\"}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T08:37:00.407Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T08:37:02.792419+00:00\"}]}}, \"exp_001_eval_05B_d025_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:33:04.298Z\", \"updated_at\": \"2026-05-15T08:34:55.834Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s123_aligned/eval_results.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T08:34:50.638Z\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.3473, \"correct\": 4877, \"total\": 14042}, \"gsm8k\": {\"accuracy\": 0.3533, \"correct\": 466, \"total\": 1319}, \"arc_challenge\": {\"accuracy\": 0.4061, \"correct\": 476, \"total\": 1172}, \"humaneval\": {\"pass@1\": 0.0854, \"correct\": 14, \"total\": 164}}}, \"exp_001_sft_05B_d025_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:59:29.007Z\", \"updated_at\": \"2026-05-15T06:30:50.892Z\", \"hypothesis\": \"0.5B d025 seed=123 SFT v2 (resubmit after v1 killed on cuda:4 collision). For seed=123 multi-seed IRT pooling. Standard 0.5B params: lr=2e-4, alpha=32, r=16.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s123 --gpu 0 --seed 123 --batch-size 2 --grad-accum 8 --max-seq-length 2048 --lr 2e-4 --lora-alpha 32 --lora-r 16\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 498153, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s123\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s123/train.log\", \"note\": \"Resubmit of exp_001_sft_05B_d025_s123 (killed due to 3-process conflict on cuda:4)\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T05:48:03.702Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:48:05.315Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:48:07.407010+00:00\"}]}, \"gpu_ids\": [\"cuda:0\"], \"metrics\": {\"train_loss\": 1.548, \"accuracy\": 0.697, \"global_steps\": 3384, \"epoch\": 1, \"runtime_seconds\": 5930}}, \"exp_001_eval_05B_d000_s42_v7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:34:42.526Z\", \"updated_at\": \"2026-05-15T06:10:55.651Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-0.5B --adapter-path Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir eval_results/Qwen2.5-0.5B_d000_v2_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"data_count\": 4, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_source\": \"exp_001_sft_0pct_05B\", \"parent\": \"exp_001_sft_0pct_05B\", \"hypothesis\": \"0.5B d000 s42 baseline eval v7 (submitted by audit Worker on cuda:4). Pending kill if GPU memory pressure from SFT coexistence.\", \"pid\": 494109, \"note\": \"Submitted by gpu-audit-and-submit-batch Worker. May be killed per Director if SFT starts on same GPU.\"}, \"conclusion\": \"failed\", \"failure_reason\": \"PID 494109 died after 2h+ with no output. cuda:4 released.\", \"completed_at\": \"2026-05-15T06:10:55.651Z\"}, \"exp_004_sim_sweep_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:39:41.819Z\", \"updated_at\": \"2026-05-15T05:33:31.938Z\", \"hypothesis\": \"4PL+γ IRT parameter recovery sweep v5: continuation of v4 (which was erroneously marked failed). Same process PID 652931, TMPDIR=/home/ubuntu/tmp_cmdstan. Progress: 98/120 seeds processed (68 OK). auc0.65 conditions systematically failing.\", \"spec\": {\"command\": \"TMPDIR=/home/ubuntu/tmp_cmdstan python run_sweep.py subset --parallel 2 --chains-parallel 2 --resume\", \"server\": \"local\", \"pid\": 652931, \"data_path\": \"synthetic\", \"data_count\": 120, \"model_name\": \"4PL+gamma IRT\", \"seed\": 42, \"log_path\": \"tmux:exp_004_sim_sweep_v4\", \"tmux_session\": \"exp_004_sim_sweep_v4\", \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/results/\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:33:23.236Z\", \"log_path\": \"/root/contamcal-irt-calibration/exp004_sim_sweep/results/\", \"metrics\": {\"seeds_attempted\": 97, \"seeds_ok\": 59, \"seeds_total\": 120, \"conditions_complete\": 4, \"conditions_partial\": 5, \"conditions_missing\": 3, \"failure_cause\": \"Disk quota exceeded ([Errno 122]) - root partition /tmp filled by CmdStan temp files\", \"conditions_fully_ok\": [\"auc0.55_n20 (10/10)\", \"auc0.55_n50 (10/10)\", \"auc0.8_n20 (10/10)\", \"auc0.8_n50 (10/10)\"], \"conditions_partial_ok\": [\"auc0.55_n100 (7/10)\", \"auc0.8_n100 (6/10)\", \"auc0.9_n20 (6/10)\"], \"conditions_all_failed\": [\"auc0.65_n20 (0/10)\", \"auc0.65_n50 (0/7)\"], \"conditions_never_started\": [\"auc0.65_n100\", \"auc0.9_n50\", \"auc0.9_n100\"]}}, \"exp006-oracle-arc-4pl-pooled\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:51:29.732Z\", \"updated_at\": \"2026-05-15T05:23:24.270Z\", \"hypothesis\": \"ARC oracle 4PL+γ pooled IRT with same config as GSM8K oracle (all available models + oracle exposure). Previous ARC 'oracle' used 0.5B-only + delta exposure — not comparable to GSM8K oracle (16 models + oracle). Completes the 2×2×2 matrix (benchmark × model × signal).\", \"spec\": {\"command\": \"TMPDIR=/home/ubuntu/tmp_cmdstan python exp006/run_exp006.py --oracle-exposure --pool-scales 0.5B 1.5B --benchmark arc_challenge --chains 4 --warmup 2000 --samples 4000 --parallel-chains 1 --output-dir /root/autodl-tmp/exp006/results_pooled_05B_15B_arc_oracle_4pl_pooled --aligned-only\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": \"11 models x 1172 items\", \"model_name\": \"IRT 4PL+gamma pooled (0.5B+1.5B) ARC oracle exposure\", \"seed\": 42, \"tmux_session\": \"exp006_oracle_arc_4pl_pooled\", \"log_path\": \"/tmp/irt_oracle_arc_4pl_pooled.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_oracle_4pl_pooled\", \"note\": \"CPU-only IRT task. Matches GSM8K oracle config (16 models, oracle exposure, 4 chains, 2000 warmup, 4000 samples) but for ARC benchmark.\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:23:24.270Z\"}, \"exp_008_instruct_05B_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:25:20.315Z\", \"updated_at\": \"2026-05-15T05:19:54.360Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"pid\": 493617, \"model_name\": \"Qwen2.5-0.5B-Instruct\", \"seed\": 42, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"data_count\": 0, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"hypothesis\": \"0.5B-Instruct eval for exp_008 signal survival analysis. 3-regime comparison: base (pretrained) -> d000 (SFT) -> Instruct (SFT+RL). No adapter needed.\", \"parent\": \"exp_008_instruct_rl_proxy\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_aligned/eval.log\", \"note\": \"PID 493617 dead, no .done marker but JSON output valid and complete. Verify all 4 benchmarks present.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:12:04.664Z\", \"metrics\": {\"mmlu_accuracy\": 0.2462, \"gsm8k_accuracy\": 0.3882, \"arc_challenge_accuracy\": 0.2816, \"humaneval_pass@1\": 0}}, \"exp_001_eval_3B_d100_v2_aligned_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:00:37.845Z\", \"updated_at\": \"2026-05-15T05:19:51.816Z\", \"spec\": {\"hypothesis\": \"3B d100 v2 aligned eval resubmit (v1 failed). Director approved cuda:0. Critical path: 3B signal computation blocked on this.\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_3B_v2\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 477489, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned\", \"data_count\": 0, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/eval.log\", \"note\": \"PID 477489 dead, no .done marker but JSON output valid and complete. Verify all 4 benchmarks present.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:12:00.857Z\", \"metrics\": {\"mmlu_accuracy\": 0.632, \"gsm8k_accuracy\": 0.7415, \"arc_challenge_accuracy\": 0.8242, \"humaneval_pass@1\": 0.1707}}, \"exp_001_eval_3B_d025_v2_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:14:47.629Z\", \"updated_at\": \"2026-05-15T05:19:49.188Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 0, \"model_name\": \"Qwen2.5-3B (d025 v2 LoRA)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned/eval.log\"}, \"hypothesis\": \"3B d025 v2 para_aligned eval. Paraphrased benchmarks for contamination signal computation.\", \"parent\": \"exp_001_sft_d025_3B_v2\", \"pid\": 499610, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:11:56.564Z\", \"metrics\": {\"mmlu_para_accuracy\": 0.621, \"gsm8k_para_accuracy\": 0.5482, \"arc_challenge_para_accuracy\": 0.8106, \"humaneval_para_pass@1\": 0.1154}}, \"exp_001_sft_3B_d100_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:13:45.159Z\", \"updated_at\": \"2026-05-15T05:18:48.164Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123 --gpu 0 --seed 123 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 16\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:5\", \"pid\": 471296, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 100, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/train.log\", \"hypothesis\": \"3B d100 seed=123 SFT for N=16 multi-seed IRT pooling. D020 params: lr=5e-5, alpha=16, r=16.\", \"lr\": \"5e-5\", \"lora_alpha\": 16, \"lora_r\": 16, \"batch_size\": 1, \"grad_accum\": 16, \"max_seq_length\": 2048}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.1846, \"mean_token_accuracy\": 0.7343, \"steps\": 4159, \"epochs\": 1, \"runtime_seconds\": 18252}, \"completed_at\": \"2026-05-15T05:18:48.164Z\"}, \"exp006-oracle-arc-2pl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:42:55.893Z\", \"updated_at\": \"2026-05-15T04:56:42.392Z\", \"hypothesis\": \"ARC 2PL+γ vs 4PL+γ comparison. ARC 4PL+γ showed γ=-1.46. If 2PL+γ yields better calibration (like GSM8K), supports 'model complexity must match data structure' claim. If 4PL better on ARC, bidirectional evidence for benchmark-dependent model selection.\", \"spec\": {\"command\": \"python exp006/run_exp006.py --oracle-exposure --pool-scales 0.5B 1.5B --benchmark arc_challenge --model-type 2pl_gamma --chains 4 --warmup 2000 --samples 4000 --parallel-chains 1 --output-dir /root/autodl-tmp/exp006/results_pooled_05B_15B_arc_oracle_2pl --aligned-only\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": 11, \"model_name\": \"2pl_gamma\", \"seed\": 42}, \"pid\": 496697, \"log_path\": \"/tmp/irt_oracle_arc_2pl.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_oracle_2pl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:56:38.148Z\", \"metrics\": {\"gamma\": -0.618, \"gamma_ci\": [-1.04, -0.2], \"rhat\": 1.006, \"ESS\": 1512, \"MAE\": 0.0759, \"C95_coverage\": 0.1818}}, \"exp_001_eval_3B_d000_v2_s123_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:22:30.855Z\", \"updated_at\": \"2026-05-15T04:56:34.161Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:2\", \"pid\": 492733, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d000_v2_s123\", \"hypothesis\": \"3B d000 v2 s123 para_aligned eval. P0: paired with aligned eval for 3B signal computation.\", \"note\": \"Cron marked failed (process gone, no sentinel, no W&B — miss 3/5). Investigation: PID 492733 dead, no OOM kill in dmesg. Output dir has eval_results.json with all 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval) + correctness_matrix.json + item_responses.json. Process completed normally and exited. Re-marking as success.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T04:28:39.648Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:28:45.925Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:29:03.911336+00:00\"}]}, \"metrics\": {\"mmlu_para_accuracy\": 0.6512, \"gsm8k_para_accuracy\": 0.1491, \"arc_challenge_para_accuracy\": 0.8121, \"humaneval_para_pass@1\": 0.0385}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned/eval_results.json\"}, \"exp006-pooled-s1only-gsm8k-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:22:13.409Z\", \"updated_at\": \"2026-05-15T03:45:48.766Z\", \"spec\": {\"command\": \"TMPDIR=/home/ubuntu/tmp_cmdstan python exp006/run_exp006.py --pool-scales 0.5B 1.5B --benchmark gsm8k --signals-dir /root/autodl-tmp/exp002/signals --signal-key s1_embedding --require-signals --aligned-only --data-seed 42 --output-dir /root/autodl-tmp/exp006/results_pooled_s1only_gsm8k --joint-fit --parallel-chains 1\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/\", \"data_count\": 8, \"model_name\": \"0.5B+1.5B pooled\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_s1only_gsm8k\", \"log_path\": \"/tmp/irt_s1only_gsm8k_v2.log\", \"tmux_session\": \"exp006_s1only_gsm8k\", \"pid\": 481020, \"hypothesis\": \"Pooled IRT N=8 S1-only GSM8K rerun: parallel_chains=1 + TMPDIR fix (v1 failed: cgroup pids.max=20480 killed parallel CmdStan chains)\"}, \"metrics\": {\"gamma\": 0.1871, \"gamma_sd\": 0.5687, \"gamma_ci_lower\": -0.9172, \"gamma_ci_upper\": 1.3294, \"gamma_ci_excludes_zero\": false, \"rhat_max\": 1.0148, \"ess_min\": 330.2, \"divergent_pct\": 0, \"ppp\": 0.336, \"residual_mae\": 0.0367, \"fit_time_sec\": 336.9, \"n_models\": 8, \"n_items\": 1319, \"diagnostics_ok\": false, \"note\": \"No evaluation/baselines files generated; only IRT fit available. rhat and ESS did not pass thresholds.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T02:39:46.863Z\"}, \"exp006-pooled-s1only-arc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:02:41.698Z\", \"updated_at\": \"2026-05-15T03:45:45.246Z\", \"spec\": {\"command\": \"python exp006/run_exp006.py --pool-scales 0.5B 1.5B --benchmark arc_challenge --signals-dir /root/autodl-tmp/exp002/signals --signal-key s1_embedding --require-signals --aligned-only --data-seed 42 --output-dir /root/autodl-tmp/exp006/results_pooled_s1only_arc --joint-fit\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/\", \"data_count\": 8, \"model_name\": \"0.5B+1.5B pooled\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_s1only_arc\", \"log_path\": \"/tmp/irt_s1only_arc.log\", \"metrics\": {\"gamma\": -1.4637, \"gamma_ci\": [-2.51, -0.41], \"ci_excludes_zero\": true, \"rhat_max\": 1.0098, \"ess_min\": 769.6, \"divergences\": 0, \"PPP\": 0.9677, \"runtime_seconds\": 1244}}, \"hypothesis\": \"Pooled IRT N=8 with S1-only exposure (D034: RRF non-monotonic, S1 perfectly monotonic 0.5946→0.8998)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:02:49.757Z\", \"metrics\": {\"gamma\": -1.4637, \"gamma_sd\": 0.5276, \"gamma_ci_lower\": -2.51, \"gamma_ci_upper\": -0.4051, \"gamma_ci_excludes_zero\": true, \"rhat_max\": 1.0098, \"ess_min\": 769.6, \"divergent_pct\": 0, \"ppp\": 0.9677, \"mae\": 0.0347, \"ece\": 0.0319, \"brier\": 0.0018, \"coverage_95\": 0.625, \"coverage_80\": 0.25, \"coverage_50\": 0, \"sharpness_95\": 0.0684, \"kendall_tau\": 0.7559, \"fit_time_sec\": 317.7, \"n_models\": 8, \"n_items\": 1172, \"baselines\": {\"B0_raw_mae\": 0.0588, \"B1_remove_rescore_mae\": 0.0588, \"B2_2pl_gamma_mae\": 0.064, \"B3_vanilla_4pl_mae\": 0.0706, \"B4_linear_regression_mae\": 0.0562, \"B5_emperor_mae\": 0.0588, \"B6_dcr_fuzzy_mae\": 0.2454}}}, \"exp006-oracle-gsm8k-extended-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:22:28.344Z\", \"updated_at\": \"2026-05-15T03:40:28.284Z\", \"spec\": {\"command\": \"TMPDIR=/home/ubuntu/tmp_cmdstan python run_exp006.py --oracle-exposure --pool-scales 0.5B 1.5B --benchmark gsm8k --chains 4 --warmup 2000 --samples 4000 --output-dir /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_oracle_extended --parallel-chains 1\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": 16, \"model_name\": \"4PL+gamma IRT (CmdStanPy NUTS)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_oracle_extended\", \"log_path\": \"/tmp/irt_oracle_gsm8k_ext_v2.log\", \"tmux_session\": \"exp006_oracle_gsm8k_ext\", \"pid\": 481167, \"hypothesis\": \"GSM8K oracle exposure 4PL+gamma extended MCMC rerun: parallel_chains=1 + TMPDIR fix. 4 chains x 2000 warmup x 4000 samples. (v1 failed at 55-65%: Operation not permitted)\"}, \"conclusion\": \"success\", \"metrics\": {\"gamma\": 3.773, \"gamma_sd\": 0.504, \"gamma_ci_lower\": 2.741, \"gamma_ci_upper\": 4.714, \"gamma_ci_excludes_zero\": true, \"rhat_max\": 1.002, \"ess_min\": 1221.9, \"divergent_pct\": 0, \"ppp\": 0, \"mae\": 0.0917, \"ece\": 0.0894, \"coverage_95\": 0.31, \"coverage_80\": 0.25, \"coverage_50\": 0.25, \"kendall_tau\": 0.505, \"fit_time_sec\": 6240.3, \"n_models\": 16, \"n_items\": 1319, \"baselines\": {\"B0_raw_mae\": 0.005, \"B4_linear_regression_mae\": 0.008, \"B5_emperor_mae\": 0.005, \"B6_dcr_fuzzy_mae\": 0.138}}, \"completed_at\": \"2026-05-15T03:40:28.284Z\"}, \"exp_001_sft_05B_d025_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:25:52.119Z\", \"updated_at\": \"2026-05-15T03:37:45.126Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && /root/miniconda3/bin/python train_sft.py --model-name Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"493808\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_05B_d025_s123.log\", \"submitted_at\": \"2026-05-15T03:26:02.161Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 703.0, \"gpu_hours\": 0.2}, \"conclusion\": \"killed\", \"failure_reason\": \"Killed to resolve cuda:4 3-way collision. SFT should not share GPU with eval. Will resubmit when GPU available.\", \"completed_at\": \"2026-05-15T03:37:45.126Z\"}, \"exp_001_eval_05B_d005_s123_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:40:41.614Z\", \"updated_at\": \"2026-05-15T03:23:40.626Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 0, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_05B_d005_s123\", \"hypothesis\": \"0.5B d005 seed=123 para_aligned eval. Paired with aligned eval (cuda:1) for seed=123 signal computation.\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_para_accuracy\": 0.3166, \"gsm8k_para_accuracy\": 0.2939, \"arc_challenge_para_accuracy\": 0.2912, \"humaneval_para_pass@1\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_para_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_para_aligned/eval_results.json\", \"completed_at\": \"2026-05-15T03:21:52.878Z\"}, \"exp_001_eval_05B_d000_s42\": {\"completed_at\": \"2026-05-14T01:29:11.220Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T22:42:34.313Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T01:29:13.572174+00:00\"}]}, \"failure_reason\": \"Traceback → ration/exp001/evaluate.py\\\", line 558, in main all_results[\\\"benchmarks\\\"][benchmark] = result ^^^^^^^^^^^^^^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or directory: '/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json'\", \"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation\", \"notes\": \"失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json 时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令 s123 实验成功。fix_worker_id: worker_fix_eval_05B_d000_s42_v2_20260514T013245 | 建议: 修复 evaluate.py 中保存前的 os.makedirs 调用后重跑\", \"reproduce\": {\"finished_at\": \"2026-05-14T01:29:08.743Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.73, \"gpu_ids\": [\"cuda:1\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42.log\", \"model_name\": \"Qwen2.5-0.5B\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\", \"parent\": \"exp_001_05B_d000_s42\", \"pid\": \"229370\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T22:45:41.096Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9810.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:21:30.012Z\"}, \"exp_001_eval_05B_d005_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:50:01.658Z\", \"updated_at\": \"2026-05-15T03:19:25.724Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_05B_d005_s123\", \"hypothesis\": \"0.5B d005 seed=123 aligned eval for seed=123 signal computation pipeline.\", \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T03:14:20.634Z\"}, \"failure_reason\": \"CORRECTED: Cron 误判 failed (进程正常退出后 ~10min 被判死亡)。实际输出完整，已修正为 success。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T03:14:26.740Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T03:14:37.137590+00:00\"}]}, \"metrics\": {\"mmlu_accuracy\": 0.3002, \"gsm8k_accuracy\": 0.3677, \"arc_challenge_accuracy\": 0.2978, \"humaneval_pass@1\": 0.0976}}, \"exp_004_sim_sweep_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:28:42.574Z\", \"updated_at\": \"2026-05-15T02:54:16.891Z\", \"spec\": {\"command\": \"TMPDIR=/home/ubuntu/tmp_cmdstan python run_sweep.py subset --parallel 2 --chains-parallel 2 --resume\", \"server\": \"cqa1-21977\", \"pid\": 652931, \"data_path\": \"synthetic\", \"data_count\": 120, \"model_name\": \"4PL+gamma IRT\", \"seed\": 42, \"log_path\": \"/tmp/exp004_sweep_v4.log\", \"tmux_session\": \"exp_004_sim_sweep_v4\", \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/results/\"}, \"hypothesis\": \"4PL+γ IRT parameter recovery sweep v4: resume of v3 (crashed due to /tmp tmpfs full from cmdstanpy MCMC temp files). Fixed: TMPDIR=/home/ubuntu/tmp_cmdstan, --resume mode strips failed seeds and re-runs them. 57/120 done, 63 remaining across 8 conditions.\", \"conclusion\": \"failed\", \"failure_reason\": \"CORRECTION: 进程实际仍在本地 CPU 运行 (PID 652931, tmux exp_004_sim_sweep_v4, elapsed 2h25m)。之前 Worker 误在远程服务器查找本地 PID 导致误判。Registry 不可回退 DONE→RUNNING。sweep 正在进行: seed 1 (2/10), γ=0.5011, θ_corr=0.9712。\", \"completed_at\": \"2026-05-15T02:50:45.363Z\"}, \"exp_001_sft_3B_d000_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:22:51.681Z\", \"updated_at\": \"2026-05-15T02:47:38.140Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123 --gpu 0 --seed 123 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 16\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"435971\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_s123.log\", \"submitted_at\": \"2026-05-14T20:22:50.945Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter\", \"wall_clock_seconds\": 23087.2, \"gpu_hours\": 6.41}, \"hypothesis\": \"3B d000 seed=123 SFT for D025/D026 multi-seed strategy. D020 params: lr=5e-5, alpha=16, r=16. Output dir: Qwen2.5-3B_d000_v2_s123.\", \"reproduce\": {\"finished_at\": \"2026-05-15T00:04:19.200Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:04:22.909131+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.1361, \"epochs\": 1, \"steps\": 3125, \"mean_token_accuracy\": 0.748, \"train_runtime_seconds\": 13141.8, \"entropy\": 1.1108, \"baseline_seed42_train_loss\": 1.1357}, \"completed_at\": \"2026-05-15T02:47:38.140Z\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:14:58.376Z\", \"updated_at\": \"2026-05-15T01:23:18.115Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v3 --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 0, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval (para_aligned)\"}, \"conclusion\": \"failed\", \"failure_reason\": \"CORRECTION: v3 实际仍在 GPU 4 运行 (PID 479906, 9008MiB)。check_job_status 通过 tmux 名称查询误判为死亡，实际进程存活。但 v2 已成功完成有完整输出，v3 为冗余运行。Registry 不可回退 DONE→RUNNING。\", \"completed_at\": \"2026-05-15T01:18:57.184Z\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:25:20.929Z\", \"updated_at\": \"2026-05-15T01:16:33.841Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2 --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": null, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (paraphrased, aligned format)\", \"parent\": \"exp_001_sft_3B_d000_v2\", \"hypothesis\": \"3B d000 v2 para_aligned eval v2 (full 4 benchmarks). Paired with aligned eval for signal computation.\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2/train.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2\", \"tmux_session\": \"exp_001_eval_3B_d000_v2_para_aligned_v2\"}, \"conclusion\": \"success\", \"failure_reason\": \"\", \"completed_at\": \"2026-05-15T01:11:20.009Z\", \"metrics\": {\"mmlu_para_accuracy\": 0.6468, \"gsm8k_para_accuracy\": 0.2895, \"arc_challenge_para_accuracy\": 0.8121, \"humaneval_para_pass@1\": 0.0385}}, \"exp006-oracle-gsm8k-extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:04:04.647Z\", \"updated_at\": \"2026-05-15T01:04:15.114Z\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration/exp006 && python run_exp006.py --oracle-exposure --pool-scales 0.5B 1.5B --benchmark gsm8k --chains 4 --warmup 2000 --samples 4000 --output-dir /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_oracle_extended\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": 15, \"model_name\": \"4PL+gamma IRT (CmdStanPy NUTS)\", \"seed\": 42, \"hypothesis\": \"GSM8K oracle exposure 4PL+gamma extended MCMC (D035: confirm convergence, target rhat<1.01 ess>1000)\", \"failure_reason\": \"IRT 4PL fitting failed (Operation not permitted), but non-IRT baselines completed successfully. B0_raw C95=1.00, C80=0.94 on N=16 models.\", \"metrics\": {\"irt_status\": \"failed\", \"baselines_status\": \"success\", \"B0_raw_MAE\": 0.005, \"B0_raw_C50\": 0.88, \"B0_raw_C80\": 0.94, \"B0_raw_C95\": 1, \"B0_raw_tau\": 0.838, \"n_models\": 16}}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T01:02:58.779Z\"}, \"exp006-pooled-s1only-gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:02:44.254Z\", \"updated_at\": \"2026-05-15T01:04:06.647Z\", \"spec\": {\"command\": \"python exp006/run_exp006.py --pool-scales 0.5B 1.5B --benchmark gsm8k --signals-dir /root/autodl-tmp/exp002/signals --signal-key s1_embedding --require-signals --aligned-only --data-seed 42 --output-dir /root/autodl-tmp/exp006/results_pooled_s1only_gsm8k --joint-fit\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/\", \"data_count\": 8, \"model_name\": \"0.5B+1.5B pooled\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_s1only_gsm8k\", \"failure_reason\": \"CmdStan chains crashed at 55-65%: Operation not permitted (nproc limit). All 4 chains.\"}, \"hypothesis\": \"Pooled IRT N=8 with S1-only exposure (D034: RRF non-monotonic, S1 perfectly monotonic 0.5946→0.8998)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T01:02:53.983Z\"}, \"exp_001_eval_3B_d100_v2_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:06:11.858Z\", \"updated_at\": \"2026-05-15T00:50:03.989Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d100_s42/lora_adapter --output-dir Qwen2.5-3B_d100_v2_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir paraphrases --cache-dir .hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:0\", \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": \"4 benchmarks (paraphrased)\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval (paraphrased, mc-format=aligned)\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"hypothesis\": \"3B d100 v2 para_aligned eval: paraphrased benchmarks on contaminated 3B checkpoint. Paired with aligned eval for signal computation.\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned.log\", \"tmux_session\": \"exp_001_eval_3B_d100_v2_para_aligned\", \"pid\": 470062}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_para\": 0.659, \"gsm8k_para\": 0.5833, \"arc_challenge_para\": 0.8092, \"humaneval_para_pass1\": 0.1154}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned.log\", \"completed_at\": \"2026-05-15T00:50:03.989Z\"}, \"exp_001_sft_05B_d005_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:45:12.529Z\", \"updated_at\": \"2026-05-15T00:46:31.713Z\", \"hypothesis\": \"0.5B d005 seed=123 SFT for N=16 multi-seed IRT pooling. Standard 0.5B params: lr=2e-4, alpha=32, r=16.\", \"spec\": {\"command\": \"python train_sft.py --model-name Qwen2.5-0.5B --data-path sft_dosage_005.jsonl --output-dir Qwen2.5-0.5B_d005_s123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --seed 123 --gpu 1\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"464137\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_05B_d005_s123.log\", \"hyperparams\": {\"lr\": \"2e-4\", \"lora_alpha\": 32, \"lora_r\": 16, \"batch_size\": 4, \"grad_accum\": 4}}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.5422, \"final_loss\": 1.4542, \"mean_token_accuracy\": 0.6356, \"final_token_accuracy\": 0.6794, \"total_steps\": 3177, \"train_runtime_sec\": 3458.58, \"epoch\": 1}, \"completed_at\": \"2026-05-15T00:46:31.713Z\"}, \"exp_001_eval_3B_d000_v2_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:01:48.742Z\", \"updated_at\": \"2026-05-15T00:42:06.698Z\", \"hypothesis\": \"3B d000 v2 aligned eval (D020 fix: lr=5e-5, alpha=16). Verify GSM8K recovery from CoT catastrophic forgetting. Target: GSM8K >= 50% (raw 60.5%, v1 was 11.7%).\", \"parent\": \"exp_001_sft_3B_d000_v2\", \"spec\": {\"command\": \"bash -c 'source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=4 python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned'\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"441570\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_v2_aligned.log\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"exp001/data\", \"data_count\": 0, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"}, \"metrics\": {\"mmlu\": 0.6295, \"gsm8k\": 0.3525, \"arc_challenge\": 0.8183, \"humaneval_pass@1\": 0.0976}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_v2_aligned.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:22:49.314Z\", \"notes\": \"PARTIAL SUCCESS (Reviewer WARNING): GSM8K=35.25% 未达 50% 目标（raw 60.5%→35.25%，损失 25pp）。MMLU(62.95%)/ARC(81.83%) 恢复正常，但 CoT 能力退化显著。D020 params (lr=5e-5, alpha=16) 改善了 v1(11.7%) 但不够。\"}, \"exp006-pooled-05B-15B-gsm8k-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:59:47.176Z\", \"updated_at\": \"2026-05-15T00:42:04.172Z\", \"spec\": {\"command\": \"python run_exp006.py --pool-scales 05B 15B --benchmark gsm8k --require-signals --joint-fit --exclude-models 3B_d000\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/\", \"data_count\": 8, \"model_name\": \"0.5B+1.5B pooled\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T23:00:23.015Z\", \"metrics\": {\"exposure_source\": \"signal_rrf\", \"gamma_perbench\": 0.1871, \"gamma_perbench_ci\": [-0.92, 1.33], \"gamma_joint\": 0.1202, \"gamma_joint_ci\": [-0.74, 0.96], \"mae\": 0.036, \"coverage_95\": 0.5, \"ppp\": 0.336, \"n_models\": 8, \"convergence\": \"FAILED (rhat=1.015, ess=330)\", \"NOTE\": \"per-bench not converged; no oracle baseline exists\"}, \"notes\": \"INCONCLUSIVE (Reviewer WARNING): MCMC convergence failed — rhat=1.015, ess=330, gamma CI crosses zero. 等待 exp006-oracle-gsm8k-extended / exp006-pooled-s1only-gsm8k 替代结果。原 conclusion=success 降级为 negative。\"}, \"exp_001_sft_15B_d100_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:21:10.691Z\", \"updated_at\": \"2026-05-15T00:32:28.784Z\", \"spec\": {\"command\": \"python train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_100.jsonl --output-dir Qwen2.5-1.5B_d100_s123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --seed 123 --gpu 2\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"435415\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_15B_d100_s123.log\", \"submitted_at\": \"2026-05-14T20:21:09.814Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"wall_clock_seconds\": 15079.0, \"gpu_hours\": 4.19}, \"reproduce\": {\"finished_at\": \"2026-05-15T00:27:19.580Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:27:22.168956+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.3002, \"mean_token_accuracy\": 0.7178, \"entropy\": 1.3327, \"train_runtime_seconds\": 14663.6, \"steps\": 4159, \"epochs\": 1, \"num_tokens\": 21575068, \"baseline_seed42_train_loss\": 1.2996, \"baseline_seed42_token_accuracy\": 0.7033}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_15B_d100_s123.log\", \"completed_at\": \"2026-05-15T00:32:28.784Z\"}, \"exp_004_sim_sweep_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:55:41.270Z\", \"updated_at\": \"2026-05-15T00:13:02.038Z\", \"spec\": {\"command\": \"python run_sweep.py subset --parallel 2 --chains-parallel 2\", \"server\": \"local\", \"pid\": 599562, \"data_path\": \"synthetic\", \"data_count\": 120, \"model_name\": \"4PL+gamma IRT\", \"seed\": 42, \"log_path\": \"/tmp/exp004_sweep_restart_v2.log\"}, \"hypothesis\": \"4PL+γ IRT parameter recovery sweep v3: continuing v2 process (PID 599562, parallel=2, chains_parallel=2). 54/120 done, 66 remaining. Killed conflicting v1 serial process.\", \"notes\": \"v2 PID 599562 was still alive (erroneously marked failed). v1 serial PID 559606 was also running on same results dir — killed to prevent write conflicts. v3 = same process as v2, just corrected registry. 2 CPU / 7.6GB RAM machine, parallel=2 chains_parallel=2. ETA ~20-30h for remaining 66 runs.\", \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp004_sim_sweep/results/\", \"log_path\": \"/tmp/exp004_sweep_restart_v2.log\", \"failure_reason\": \"Disk quota exceeded on /tmp (tmpfs 3.9GB, cmdstanpy MCMC temp files filled it). Crashed at condition 10/12 (auc0.65_n50). 11/12 condition files saved but later seeds in conditions 7-10 all failed. Missing: auc0.65_n100.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T00:04:34.068Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:04:46.348468+00:00\"}]}}, \"exp_001_eval_3B_d100_v2_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:34:11.632Z\", \"updated_at\": \"2026-05-15T00:08:21.000Z\", \"spec\": {\"command\": \"evaluate.py --benchmarks mmlu gsm8k arc_challenge --mc-format aligned\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned\", \"data_count\": 3, \"model_name\": \"Qwen2.5-3B + d100_v2_s42 LoRA (alpha=16)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge aligned\"}, \"metrics\": {\"INVALID\": \"metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion.\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned\", \"log_path\": \"/root/runs/contamcal-irt-calibration/eval_3B_d100_aligned.log\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T23:57:18.788Z\", \"notes\": \"DATA INTEGRITY ISSUE (D036): Metrics erroneously copied from v1 (exp_001_eval_3B_d100_aligned). Worker found v1 results at similar path, mistook for v2. v2 output dir was empty (eval still running), then deleted during cleanup. PID 461879 killed/died. Must re-run as v3.\"}, \"exp_001_sft_d025_3B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:34:12.515Z\", \"updated_at\": \"2026-05-14T23:51:23.923Z\", \"spec\": {\"command\": \"train_sft.py --model Qwen/Qwen2.5-3B --dosage 25 --seed 42 --lr 5e-5 --lora-alpha 16 --lora-r 16 --gpu 3\", \"server\": \"cqa1-21977\", \"data_count\": 3384, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"d025 (25% contamination)\"}, \"conclusion\": \"failed\", \"notes\": \"GPU 3 空转: 注册 RUNNING 但进程从未启动 (nvidia-smi 确认 0% util, 0 MiB). Director 指令标 FAILED.\", \"checkpoint_path\": \"N/A - never started\", \"log_path\": \"N/A - never started\", \"completed_at\": \"2026-05-14T23:51:23.923Z\"}, \"exp_001_eval_05B_d100_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:31:14.591Z\", \"updated_at\": \"2026-05-14T23:48:24.746Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"444836\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_s123_aligned.log\", \"submitted_at\": \"2026-05-14T21:30:00Z\", \"submitted_via\": \"ssh_execute+tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s123_aligned\", \"wall_clock_seconds\": 8304.7, \"gpu_hours\": 2.31}, \"parent\": \"exp_001_sft_05B_d100_s123\", \"hypothesis\": \"0.5B d100 s123 aligned eval — multi-seed dosage-100 eval for IRT calibration.\", \"metrics\": {\"mmlu_accuracy\": 0.3058, \"gsm8k_accuracy\": 0.3798, \"arc_challenge_accuracy\": 0.3669, \"humaneval_pass_at_1\": 0.1037, \"mmlu_correct\": 4294, \"mmlu_total\": 14042, \"gsm8k_correct\": 501, \"gsm8k_total\": 1319, \"arc_challenge_correct\": 430, \"arc_challenge_total\": 1172, \"humaneval_total\": 164}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:48:24.746Z\"}, \"exp_001_eval_3B_d000_v2_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:21:18.136Z\", \"updated_at\": \"2026-05-14T23:39:15.404Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/paraphrases/\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B + d000_v2_s42 LoRA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval paraphrase\"}, \"hypothesis\": \"3B d000 v2 para_aligned eval: paraphrased benchmarks (mmlu/gsm8k/arc/humaneval) on D020-retrained 3B d000 v2 checkpoint. Paired with aligned eval (GPU 4) for contamination signal computation.\", \"notes\": \"GPU 0, PID 450055. tmux session: eval_3B_d000_v2_para. Log: /tmp/eval_3B_d000_v2_para_aligned.log. bitsandbytes warning (libnvJitLink.so.13 missing) is non-fatal.\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_para\": 0.6468, \"format\": \"paraphrased_aligned\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned\", \"log_path\": \"/tmp/eval_3B_d000_v2_para_aligned.log\", \"completed_at\": \"2026-05-14T23:38:53.090Z\"}, \"exp006-pooled-05B-15B-mmlu-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:59:50.928Z\", \"updated_at\": \"2026-05-14T23:08:55.525Z\", \"spec\": {\"command\": \"python run_exp006.py --pool-scales 05B 15B --benchmark mmlu --require-signals --joint-fit --exclude-models 3B_d000\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/\", \"data_count\": 8, \"model_name\": \"0.5B+1.5B pooled\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_mmlu_v2\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_mmlu_v2\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T23:00:25.877Z\", \"metrics\": {\"exposure_source\": \"signal_rrf\", \"gamma_perbench\": -3.8073, \"gamma_perbench_ci\": [-7.02, 3.22], \"gamma_joint\": -0.2095, \"gamma_joint_ci\": [-1.01, 0.59], \"mae\": 0.099, \"coverage_95\": 1, \"ppp\": 0.75, \"n_models\": 8, \"convergence\": \"FAILED (rhat=1.54, ess=7)\", \"NOTE\": \"fit completely failed, not reportable\"}}, \"exp006-pooled-05B-15B-arc-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:59:49.440Z\", \"updated_at\": \"2026-05-14T23:08:51.536Z\", \"spec\": {\"command\": \"python run_exp006.py --pool-scales 05B 15B --benchmark arc --require-signals --joint-fit --exclude-models 3B_d000\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/\", \"data_count\": 8, \"model_name\": \"0.5B+1.5B pooled\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_v2\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_v2\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:00:24.554Z\", \"metrics\": {\"exposure_source\": \"signal_rrf\", \"gamma_perbench\": -2.3471, \"gamma_perbench_ci\": [-3.46, -1.19], \"gamma_joint\": -1.4637, \"gamma_joint_ci\": [-2.51, -0.41], \"mae\": 0.035, \"coverage_95\": 0.625, \"ppp\": 0.999, \"n_models\": 8, \"convergence\": \"OK\", \"NOTE\": \"coverage below 95%; no oracle baseline exists\"}}, \"exp_005_noise_prop\": {\"completed_at\": \"2026-05-13T20:47:21.810Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T18:31:00.000Z\", \"failure_reason\": \"Stan numerical bugs: sigma_e=0 allowed (normal_lpdf crash), c/d boundary causing chain crashes, max_treedepth=10 insufficient (14.5% hit rate). All fixed, restarting.\", \"hypothesis\": \"Measurement error in exposure scores propagates through 4PL+γ IRT to widen calibrated score CIs; analytical ME model (conjugate normal integration) produces equivalent CI widths to full latent-τ model at fraction of compute\", \"retry_count\": 0, \"spec\": {\"command\": \"cd artifacts/exp005_noise_propagation && source ../mvp_simulation/.venv/bin/activate && python run_noise_propagation.py\", \"data_count\": \"multiple σ_e values × seeds\", \"data_path\": \"synthetic (generated in-script)\", \"model_name\": \"4PL+γ IRT (CmdStanPy NUTS)\", \"pid\": 234646, \"seed\": \"0-9\", \"server\": \"local (CPU only)\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:13:18.833Z\", \"notes\": \"v1 original run, failed due to /tmp disk exhaustion. Superseded by v2→v3→v4. See v4 for active tracking (PID 559667, 23/25 fits).\"}, \"exp_004_sim_sweep\": {\"completed_at\": \"2026-05-14T03:41:12.265Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T16:43:57.478Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T03:41:29.791249+00:00\"}]}, \"failure_reason\": \"PID 377122 exited, only 2/12 conditions completed, no files on remote. Process orphaned (PPID=1).\", \"hypothesis\": \"4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); there exists a minimum AUC threshold below which γ 95% CI width exceeds 15pp; recovery improves with N_models; prior sensitivity is bounded\", \"retry_count\": 0, \"spec\": {\"log_path\": \"/tmp/exp004_sweep.log\", \"pid\": \"377122\", \"timeout_per_fit\": 7200, \"note\": \"Restarted by previous loop. PID 377122 (orphaned, PPID=1). 35/120 seeds done as of 06:15 UTC. Original PID 340553 died after seed 7 of auc0.55_n100.\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:13:15.704Z\", \"notes\": \"v1 original serial run. Superseded by v2 (parallel=2). PID 559606 killed to prevent write conflicts with v2. See v3 for active tracking.\"}, \"exp002-signals-1p5B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:50:56.771Z\", \"updated_at\": \"2026-05-14T22:11:46.914Z\", \"spec\": {\"gpu\": [\"cuda:0\"]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp002-signals-1p5B.log\", \"notes\": \"1.5B signals 12/12 complete (d000/d005/d025/d100 × s1_embedding/s2_minkpp/s4_selfcritique). All PASS. GPU 0 released.\", \"completed_at\": \"2026-05-14T22:11:46.914Z\"}, \"exp_004_sim_sweep_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:12:12.267Z\", \"updated_at\": \"2026-05-14T21:55:29.436Z\", \"spec\": {\"command\": \"python run_sweep.py subset --parallel 2 --chains-parallel 2\", \"server\": \"local\", \"pid\": 599560, \"data_path\": \"synthetic\", \"data_count\": 120, \"model_name\": \"4PL+gamma IRT\", \"seed\": 42, \"log_path\": \"/tmp/exp004_sweep_restart_v2.log\", \"parent\": \"exp_004_sim_sweep\", \"hypothesis\": \"4PL+γ IRT parameter recovery sweep: 12 conditions (4 AUC × 3 N_models) × 10 seeds. v2 restart with parallel=2, chains_parallel=2.\"}, \"notes\": \"v2 was erroneously marked failed; PID 599562 was still running. Killed conflicting v1 (PID 559606). Continuing as v3 registry entry.\", \"metrics\": {\"runs_completed\": 48, \"runs_total\": 120, \"auc080_n50_bias\": 0.006, \"auc080_n50_rmse\": 0.03, \"auc080_n50_ci95_coverage\": 1, \"auc080_n100_gamma_hat\": 0.508, \"auc080_n100_bias\": 0.008, \"auc080_n100_ci_width\": 0.116, \"auc080_n100_theta_corr\": 0.962, \"ci_width_ratio_n100\": 1.81, \"core_findings_stable\": true}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T21:50:42.987Z\"}, \"exp_005_noise_prop_v3\": {\"completed_at\": \"\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-14T03:24:06.949Z\", \"hypothesis\": \"Noise propagation: ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases, demonstrating proper uncertainty propagation. v3 fixes: local disk Stan output, analytic ME (1231 params), checkpoint resume.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"artifacts/exp005_noise_propagation/output_v3\", \"command\": \"cd artifacts/exp005_noise_propagation && nohup .venv/bin/python run_noise_propagation_v3.py --output-dir output_v3 --base-seed 42 --n-seeds 5 >> exp005_v3.log 2>&1 &\", \"data_count\": 9000, \"data_path\": \"synthetic\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/exp005_v3.log\", \"model_name\": \"4PL+gamma IRT (simple + analytic ME)\", \"pid\": 559666, \"seed\": 42, \"server\": \"local\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:50:34.523Z\", \"notes\": \"PID 559666 crashed (~10h ago). 22/25 fits completed. Restarting as v4.\"}, \"exp_001_sft_05B_d100_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:17:25.569Z\", \"updated_at\": \"2026-05-14T21:30:33.304Z\", \"spec\": {\"command\": \"python train_sft.py --model-name Qwen2.5-0.5B --data-path sft_dosage_100.jsonl --output-dir Qwen2.5-0.5B_d100_s123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --seed 123 --gpu 1\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"433822\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_05B_d100_s123.log\", \"submitted_at\": \"2026-05-14T20:17:24.305Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"wall_clock_seconds\": 4389.0, \"gpu_hours\": 1.22}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T21:30:33.304Z\"}, \"exp002-signal-d025-05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:29:51.827Z\", \"updated_at\": \"2026-05-14T21:08:54.222Z\", \"spec\": {\"command\": \"python exp002/run_batch.py --model-size 0.5B --only d025 --gpu 2\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"422128\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp002-signal-d025-05B.log\", \"submitted_at\": \"2026-05-14T18:29:50.827Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 0, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"wall_clock_seconds\": 9543.4, \"gpu_hours\": 2.65}, \"notes\": \"0.5B d025 signals 3/3 passed (embedding, minkpp, selfcritique × mmlu, gsm8k, arc_challenge). 13 files total including merged signals.\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d025_s42\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T21:08:54.223Z\"}, \"exp_001_eval_05B_d025_aligned_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:07:13.381Z\", \"updated_at\": \"2026-05-14T21:08:51.166Z\", \"spec\": {\"command\": \"python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_para_aligned --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"406017\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d025_aligned_v2.log\", \"submitted_at\": \"2026-05-14T16:17:22.614Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter\", \"eval_data\": \"mmlu+gsm8k+arc_challenge+humaneval (paraphrased, aligned format)\", \"parent\": \"exp_001_sft_d025_05B_v3\", \"wall_clock_seconds\": 17488.6, \"gpu_hours\": 4.86}, \"hypothesis\": \"0.5B d025 s42 paraphrase aligned eval v2 — dose-response intermediate point. Original aligned eval already complete, this run covers paraphrase only.\", \"metrics\": {\"mmlu\": 0.2835, \"gsm8k\": 0.3114, \"arc_challenge\": 0.3199, \"humaneval_pass1\": 0.1923, \"format\": \"paraphrased_aligned\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_para_aligned\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T21:08:51.166Z\"}, \"exp_006_irt_05B_arc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:17:30.505Z\", \"updated_at\": \"2026-05-14T21:05:36.632Z\", \"hypothesis\": \"ARC (1172 items, ~4700 params) per-benchmark NUTS with delta exposure. Second benchmark validation after GSM8K success.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp006/run_exp006.py --model-scale 0.5B --data-seed 42 --benchmark arc_challenge --aligned-only --signals-dir /root/autodl-tmp/exp002/signals --output-dir /root/autodl-tmp/exp006/results_05B_arc_delta --joint-fit\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"434542\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_006_irt_05B_arc.log\", \"submitted_at\": \"2026-05-14T20:17:58.432Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2858.2, \"gpu_hours\": 0.79}, \"metrics\": {\"gamma\": -1.21, \"gamma_ci_lower\": -2.53, \"gamma_ci_upper\": 0.12, \"fit_type\": \"joint\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_05B_arc_delta\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_006_irt_05B_arc.log\", \"completed_at\": \"2026-05-14T21:05:36.633Z\"}, \"exp_001_eval_15B_d025_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:24:25.390Z\", \"updated_at\": \"2026-05-14T21:05:10.243Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"420905\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_aligned.log\", \"submitted_at\": \"2026-05-14T18:25:47.085Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9347.7, \"gpu_hours\": 2.6}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.5902, \"gsm8k\": 0.6535, \"arc_challenge\": 0.7688, \"humaneval_pass1\": 0.2256}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_aligned\", \"completed_at\": \"2026-05-14T21:01:34.760Z\"}, \"exp_001_eval_05B_d005_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:46:02.603Z\", \"updated_at\": \"2026-05-14T20:48:29.901Z\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_para_aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases/ --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": \"400526\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d005_para_aligned.log\", \"submitted_at\": \"2026-05-14T15:47:42.077Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MMLU+GSM8K+ARC+HumanEval paraphrase aligned\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval paraphrase\", \"parent\": \"exp_001_sft_d005_05B\", \"wall_clock_seconds\": 18047.8, \"gpu_hours\": 5.01}, \"reproduce\": {\"finished_at\": \"2026-05-14T16:20:40.222Z\"}, \"metrics\": {\"mmlu\": 0.3548, \"gsm8k\": 0.2588, \"arc_challenge\": 0.33, \"humaneval\": 0, \"mmlu_correct\": 2340, \"mmlu_total\": 6596, \"gsm8k_correct\": 59, \"gsm8k_total\": 228, \"arc_correct\": 230, \"arc_total\": 697, \"humaneval_correct\": 0, \"humaneval_total\": 26}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d005_para_aligned.log\", \"completed_at\": \"2026-05-14T20:48:29.901Z\"}, \"exp_001_eval_15B_d025_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:11:06.187Z\", \"updated_at\": \"2026-05-14T20:48:26.690Z\", \"hypothesis\": \"1.5B d025 paraphrase aligned eval: measure contamination-robust performance on paraphrased benchmarks for dosage=25% model\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"426474\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_para_aligned.log\", \"submitted_at\": \"2026-05-14T19:11:28.388Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_para_aligned/\", \"wall_clock_seconds\": 5816.2, \"gpu_hours\": 1.62}, \"metrics\": {\"mmlu\": 0.618, \"gsm8k\": 0.539, \"arc_challenge\": 0.766, \"humaneval\": 0.154}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_para_aligned.log\", \"completed_at\": \"2026-05-14T20:48:24.606Z\"}, \"exp_001_eval_3B_d100_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:11:52.814Z\", \"updated_at\": \"2026-05-14T20:48:21.457Z\", \"hypothesis\": \"3B d100 paraphrase aligned eval: measure contamination-robust performance drop for largest model at full dosage on paraphrased benchmarks\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"426813\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_para_aligned.log\", \"submitted_at\": \"2026-05-14T19:13:09.249Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned/\", \"wall_clock_seconds\": 5712.2, \"gpu_hours\": 1.59}, \"metrics\": {\"mmlu\": 0.676, \"gsm8k\": 0.614, \"arc_challenge\": 0.828}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:48:21.457Z\"}, \"exp_006_pooled_gsm8k_v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:17:21.376Z\", \"updated_at\": \"2026-05-14T20:47:40.753Z\", \"hypothesis\": \"Cross-scale pooled IRT (0.5B+1.5B+3B, N≈10 models) on GSM8K with delta exposure. Test if pooling increases gamma significance (previous single-scale N=4 had CI including 0).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp006/run_exp006.py --pool-scales 0.5B 1.5B 3B --benchmark gsm8k --aligned-only --signals-dir /root/autodl-tmp/exp002/signals --output-dir /root/autodl-tmp/exp006/results_pooled_gsm8k_v1 --joint-fit\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"434371\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_006_pooled_gsm8k_v1.log\", \"submitted_at\": \"2026-05-14T20:17:50.154Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1790.6, \"gpu_hours\": 0.5}, \"conclusion\": \"failed\", \"failure_reason\": \"INVALID: (1) Mixed exposure scales — 0.5B uses signal-derived delta exposure (max=0.197), 1.5B/3B fell back to oracle dosage (max=1.0), two incompatible scales in same IRT gamma. 6x 'falling back to oracle dosage' warnings in log. (2) 3B GSM8K catastrophic forgetting not excluded per D018 — 3B d000 GSM8K=12% is LoRA hyperparameter damage, theta=-4.98 extreme outlier. (3) D018 exclusion dead code not applied.\", \"completed_at\": \"2026-05-14T20:47:40.753Z\"}, \"exp_001_eval_15B_aligned_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:45:37.976Z\", \"updated_at\": \"2026-05-14T19:52:46.623Z\", \"hypothesis\": \"1.5B aligned-format eval batch (D017): d000/d005/d100 × original + paraphrase. Formal analysis results for 1.5B scale dose-response.\", \"spec\": {\"command\": \"bash run_aligned_eval_15B.sh both\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"336750\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_aligned_batch.log\", \"submitted_at\": \"2026-05-14T09:18:30.835Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MMLU+ARC+GSM8K+HumanEval original+paraphrase\", \"data_count\": \"3 dosages × 2 eval_types × 4 benchmarks\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"d000_s42 / d005_s42 / d100_s42\", \"eval_data\": \"original + paraphrase\", \"mc_format\": \"aligned (D017)\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/\", \"wall_clock_seconds\": 38055.8, \"gpu_hours\": 10.57}, \"metrics\": {\"mmlu\": {\"d000_orig\": 0.5853, \"d005_orig\": 0.5852, \"d100_orig\": 0.5933, \"d000_para\": 0.6096, \"d005_para\": 0.6164, \"d100_para\": 0.6252}, \"gsm8k\": {\"d000_orig\": 0.6543, \"d005_orig\": 0.6482, \"d100_orig\": 0.6497, \"d000_para\": 0.557, \"d005_para\": 0.5439, \"d100_para\": 0.5526}, \"arc\": {\"d000_orig\": 0.7722, \"d005_orig\": 0.7688, \"d100_orig\": 0.7688, \"d000_para\": 0.7547, \"d005_para\": 0.7532, \"d100_para\": 0.7661}, \"humaneval\": {\"d000_orig\": 0.128, \"d005_orig\": 0.25, \"d100_orig\": 0.3049, \"d000_para\": 0.0385, \"d005_para\": 0.1923, \"d100_para\": 0.2692}, \"key_finding\": \"MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination.\"}, \"notes\": \"1.5B d000 aligned eval 完成: MMLU=58.53%, GSM8K=65.43%, ARC=77.22%, HumanEval=12.80%。对比 legacy: MMLU +1.0pp, GSM8K +1.75pp, ARC -0.3pp (基本持平)。当前 GPU 1 跑 d000 para_aligned (PID 362352)。之后还有 d005/d100 aligned + paraphrase。\", \"reproduce\": {\"finished_at\": \"2026-05-14T18:43:45.194Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:43:53.197340+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:52:46.623Z\"}, \"exp_006_irt_05B_gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:04:35.887Z\", \"updated_at\": \"2026-05-14T19:48:01.400Z\", \"hypothesis\": \"GSM8K (1319 items, ~5300 params) NUTS feasibility validation. If warmup produces samples within 2h → NUTS viable for small benchmarks. Else → ADVI fallback.\", \"parent\": \"exp_006_irt_05B_v1\", \"spec\": {\"command\": \"python exp006/run_exp006.py --model-scale 0.5B --data-seed 42 --benchmark gsm8k --aligned-only --signals-dir /root/autodl-tmp/exp002/signals --output-dir /root/autodl-tmp/exp006/results_05B_gsm8k --joint-fit\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"418705\", \"log_path\": \"/root/autodl-tmp/exp006/results_05B_gsm8k_delta/\", \"submitted_at\": \"2026-05-14T18:12:36.776Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": \"4 models x 1319 items (GSM8K only)\", \"model_name\": \"Qwen2.5-0.5B (4pl_gamma IRT)\", \"seed\": 42, \"signals_dir\": \"/root/autodl-tmp/exp002/signals\", \"output_dir\": \"/root/autodl-tmp/exp006/results_05B_gsm8k\", \"method\": \"nuts\", \"stan_params_estimate\": \"~5300\", \"log_file\": \"/root/autodl-tmp/exp006/exp006_gsm8k_nuts.log\", \"checkpoint_source\": \"N/A (IRT calibration, not model checkpoint)\", \"eval_data\": \"GSM8K 1319 items from exp-001 eval_results (aligned only)\", \"wall_clock_seconds\": 3478.0, \"gpu_hours\": 0.97, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_05B_gsm8k_delta/\"}, \"notes\": \"Joint-fit converges (Rhat=1.008, ESS=956, 0 divergences), per-benchmark FAILS (Rhat=1.53, ESS=7). Exposure matrix bug suspected — per-benchmark and joint-fit may use different exposure matrices. DO NOT start ARC per-benchmark until P0 resolved. Code mods verified: max-items=random subsampling (seed-based), ADVI deleted, joint_fit max-items fixed. RRF issue found: S2 minkpp polarity inverted, delta exposure (vs d000 baseline) resolves monotonicity.\", \"conclusion\": \"success\", \"metrics\": {\"joint_gamma\": 0.3463, \"joint_gamma_ci\": [-0.65, 1.4], \"joint_rhat\": 1.0081, \"joint_ess\": 956.4, \"joint_divergences\": 0, \"perbench_gamma\": 0.508, \"perbench_gamma_ci\": [-0.64, 1.84], \"perbench_rhat\": 1.0096, \"perbench_ess\": 522.2, \"perbench_divergences\": 0, \"delta_fix_applied\": true, \"signal_scores_after_delta\": [0, 0.016, 0.065, 0.197], \"baselines_mae\": {\"B0_raw\": 0.0034, \"B4_linear_regression\": 0.003, \"B3_vanilla_4pl\": 0.0123, \"IRT_4pl_gamma\": 0.0195, \"B6_dcr_fuzzy\": 0.2634, \"B2_2pl_gamma\": 0.3202}}, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_05B_gsm8k\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_006_irt_05B_gsm8k.log\", \"completed_at\": \"2026-05-14T19:10:34.761Z\"}, \"exp_001_eval_15B_d100_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:11:51.112Z\", \"updated_at\": \"2026-05-14T19:12:41.550Z\", \"hypothesis\": \"1.5B d100 aligned eval: full contamination dosage performance on original benchmarks (aligned format)\", \"spec\": {\"command\": \"python exp001/evaluate.py --model-path Qwen2.5-1.5B --adapter-path Qwen2.5-1.5B_d100_s42/lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_aligned\", \"data_count\": \"4 benchmarks\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter\", \"eval_data\": \"MMLU+GSM8K+ARC+HumanEval aligned format\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_aligned\", \"log_path\": \"N/A (pre-existing result)\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5933, \"gsm8k_accuracy\": 0.6497, \"arc_challenge_accuracy\": 0.7688, \"humaneval_correct\": 50, \"humaneval_total\": 164, \"humaneval_pass_rate\": 0.3049}, \"completed_at\": \"2026-05-14T19:12:41.550Z\"}, \"exp_001_eval_15B_d005_aligned_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:09.199Z\", \"updated_at\": \"2026-05-14T18:45:30.922Z\", \"hypothesis\": \"1.5B d005 aligned eval — low-dose contamination response at 1.5B scale\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned\", \"data_count\": 4, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned/eval_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.5852, \"gsm8k\": 0.6482, \"arc_challenge\": 0.7688, \"humaneval_pass_at_1\": 0.25}, \"completed_at\": \"2026-05-14T18:30:53.736Z\"}, \"exp_001_sft_d100_3B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:24:36.974Z\", \"updated_at\": \"2026-05-14T18:24:10.566Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && /root/miniconda3/bin/python exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42 --gpu 3 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 16\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"420190\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_3B.log\", \"submitted_at\": \"2026-05-14T18:24:09.918Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-3B (seed=42): maximum contamination at largest controlled scale\", \"notes\": \"训练成功完成。4159/4159 steps, train_loss=1.178, token_accuracy=0.7206, runtime=5.2h。EXIT_CODE=129 (SIGHUP) 发生在 Training complete 之后，属于 wrapper PID false positive（已知模式）。Checkpoint: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter。GPU 3 已安排 eval_3B_d100 tmux auto-relay。\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:07:42.095Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:07:45.698Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:07:50.053861+00:00\"}]}, \"metrics\": {\"train_loss\": 1.178, \"token_accuracy\": 0.7206, \"runtime_hours\": 5.2, \"steps\": \"4159/4159\", \"epoch\": 1}}, \"exp_001_eval_05B_d100_aligned_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:25:10.827Z\", \"updated_at\": \"2026-05-14T18:20:00.391Z\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": \"396024\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_aligned_v4.log\", \"submitted_at\": \"2026-05-14T15:25:20.314Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MMLU+GSM8K+ARC+HumanEval aligned\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_sft_d100_05B\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned\", \"wall_clock_seconds\": 10480.1, \"gpu_hours\": 2.91}, \"reproduce\": {\"finished_at\": \"2026-05-14T17:39:56.917Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:39:58.597804+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.2334, \"gsm8k\": 0.3654, \"arc_challenge\": 0.2944, \"humaneval_pass_at_1\": 0, \"mmlu_delta_vs_d000\": -0.1645, \"arc_delta_vs_d000\": -0.1749, \"humaneval_delta_vs_d000\": -0.1098}, \"notes\": \"0.5B d100 aligned: catastrophic degradation, no contamination inflation. MMLU 23.3% (near random, -16.5pp vs d000), ARC 29.4% (-17.5pp), HumanEval 0% (-11pp). Dose-response monotonically decreasing at 0.5B scale. Consistent with unaligned format results. Small model capacity insufficient to memorize without losing generalization. Supports narrative: contamination detection via score inflation fails at small scale → need IRT-based calibration.\", \"completed_at\": \"2026-05-14T18:20:00.391Z\"}, \"exp_001_sft_d025_15B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:18:59.162Z\", \"updated_at\": \"2026-05-14T18:19:10.939Z\", \"hypothesis\": \"25% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-dosage contamination for 1.5B dose-response curve intermediate point\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 42, \"gpu\": 0, \"tmux_session\": \"sft_15B_d025\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/train.log\", \"lora_r\": 16, \"lora_alpha\": 32, \"batch_size\": 1, \"grad_accum\": 16, \"lr\": 0.0002, \"max_seq_length\": 2048, \"epochs\": 1}, \"notes\": \"Cron false positive: 训练正常完成 3384/3384 steps, epoch=1.0, loss=1.2715, token_acc=0.7192。lora_adapter/ 完整 (adapter_model.safetensors 70.5MB)。Cron 误报因无 sentinel file 和 W&B run。1.5B d025 SFT 就绪，可进行 aligned eval。\", \"reproduce\": {\"finished_at\": \"2026-05-14T17:47:04.642Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:47:05.520Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:47:07.082599+00:00\"}]}, \"metrics\": {\"train_loss\": 1.2715, \"mean_token_accuracy\": 0.7192, \"entropy\": 1.2623, \"steps\": 3384, \"epochs\": 1, \"train_runtime_seconds\": 11610.6}}, \"exp_001_eval_3B_d005_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:10:12.650Z\", \"updated_at\": \"2026-05-14T18:15:10.887Z\", \"spec\": {\"gpu\": \"cuda:4\", \"pid\": \"373931\", \"server\": \"cqa1-21977\", \"model_name\": \"Qwen2.5-3B\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T16:34:13.255Z\"}, \"failure_reason\": \"Cron false positive: results exist in /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned/. Process exited before HumanEval but MMLU/GSM8K/ARC complete. Reviewer verified.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T16:34:12.961Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T16:34:15.646154+00:00\"}]}, \"metrics\": {\"mmlu\": 0.634, \"gsm8k\": 0.208, \"arc_challenge\": 0.829, \"humaneval_pass_at_1\": 0.146}, \"log_path\": \"/root/autodl-tmp/exp001/eval_results/eval_3B_d005_aligned.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned/\", \"notes\": \"Cron false positive: 进程正常完成退出，但无 sentinel file/W&B run，cron 误判为 failed。实际 4 个 benchmark 全部完成，结果在 output dir。mmlu=0.634, gsm8k=0.208, arc=0.829, humaneval=0.146。\"}, \"exp_006_irt_05B_v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:09:23.070Z\", \"updated_at\": \"2026-05-14T18:02:23.310Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python run_exp006.py --model-scale 0.5B --data-seed 42 --output-dir /root/autodl-tmp/exp006/results_05B_v1 --joint-fit\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 411783, \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": \"6 models x 4 benchmarks\", \"model_name\": \"4PL+gamma IRT (Stan NUTS) + 7 baselines\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_05B_v1\", \"log_path\": \"/root/autodl-tmp/exp006/exp006_05B_v1.log\", \"dosages\": [0, 0, 5, 5, 25, 100], \"models_loaded\": [\"Qwen2.5-0.5B_d000_s42\", \"Qwen2.5-0.5B_d000_s42_aligned\", \"Qwen2.5-0.5B_d005_s42\", \"Qwen2.5-0.5B_d005_s42_aligned\", \"Qwen2.5-0.5B_d025_s42_aligned\", \"Qwen2.5-0.5B_d100_s42\"], \"note\": \"First full run. Mixed aligned/non-aligned (d100_aligned still running). Oracle dosage.\"}, \"conclusion\": \"failed\", \"notes\": \"D023: 56K params infeasible for NUTS (MMLU 14042 items → 56K params, 6h zero samples). Killed all chains (PIDs 411936-411940) + main (411789) + wrapper (411783). Issues: 1) No --max-items limit 2) Mixed aligned/non-aligned formats 3) Oracle dosage instead of exp-002 signal-derived exposure. Superseded by exp_006_irt_05B_v2 with tiered strategy.\", \"completed_at\": \"2026-05-14T18:02:13.217Z\"}, \"exp_001_eval_05B_d025_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:14:42.647Z\", \"updated_at\": \"2026-05-14T17:02:04.811Z\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"398496\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d025_aligned.log\", \"submitted_at\": \"2026-05-14T15:40:34.043Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4868.7, \"gpu_hours\": 1.35}, \"hypothesis\": \"0.5B d025 s42 aligned eval — 25% contamination dose-response intermediate point (original + paraphrase)\", \"conclusion\": \"success\", \"failure_reason\": \"Cron false positive: GPU 3 results valid. MMLU/GSM8K/ARC complete, HumanEval missing (appendix only, non-blocking). Reviewer verified.\", \"completed_at\": \"2026-05-14T15:39:48.113Z\", \"metrics\": {\"MMLU\": 28.03, \"GSM8K\": 36.62, \"ARC\": 32.51, \"HumanEval\": \"missing - process exited before 4th benchmark\"}}, \"exp_008_signal_survival_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:23:34.234Z\", \"updated_at\": \"2026-05-14T16:44:49.686Z\", \"hypothesis\": \"Signal Survival Analysis v4 (D021 fix): within-model AUC limited to d005/d025; d000/d100 use cross-model signal comparison; C2 claim weakened to 'systematic degradation'. Uses existing exp-002 signal data, CPU only.\", \"spec\": {\"command\": \"python signal_survival_analysis_v4.py (CPU analysis on existing exp-002 signals)\", \"server\": \"local\", \"data_path\": \"/root/autodl-tmp/exp002/signals/ (d000/d005/d100 x 0.5B)\", \"data_count\": \"3 dosages x 3 benchmarks x 3 signals\", \"model_name\": \"Qwen2.5-0.5B (3 dosages)\", \"seed\": 42, \"checkpoint_path\": \"artifacts/exp_008_signal_survival/data/exp008_v4_results.json\", \"log_path\": \"logs/workers/worker_analysis_exp_008_v4_20260514T162445.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T16:44:39.112Z\", \"metrics\": {\"S1_d005_auc_mean\": 0.979, \"S2_d005_auc_mean\": 0.465, \"S4_d005_auc_mean\": 0.481, \"S1_d100_cross_cohens_d_mean\": 3.6, \"S2_d100_cross_cohens_d_mean\": -1.98, \"S4_d100_cross_cohens_d_mean\": 0.45, \"effective_signals_at_05B\": 1, \"d021_fix\": \"within-model AUC only for d005; d100 uses cross-model Cohen's d\"}}, \"exp_001_eval_05B_d100_aligned_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:23:30.699Z\", \"updated_at\": \"2026-05-14T16:19:43.894Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"395759\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_aligned_v3.log\", \"submitted_at\": \"2026-05-14T15:25:05.369Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3272.7, \"gpu_hours\": 0.91}, \"conclusion\": \"failed\", \"hypothesis\": \"0.5B d100 s42 aligned-format eval (v3 fix: conda activation). d100 original + paraphrase MC eval with \\\"The answer is\\\" prefix (D017).\", \"parent\": \"exp_001_eval_05B_d100_aligned_v2\", \"reproduce\": {\"finished_at\": \"2026-05-14T15:56:25.013Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:56:40.453942+00:00\"}]}, \"completed_at\": \"2026-05-14T16:19:38.083Z\", \"notes\": \"失败原因: SIGHUP (EXIT_CODE=129) — tmux wrapper PID 死亡导致子进程收到 SIGHUP，在 GSM8K eval 13% (178/1319) 处被终止。已知模式(memory.md: wrapper PID vs python PID)。附带问题: 提交命令缺少 HF_DATASETS_OFFLINE=1 导致初始 HF 超时重试。v4 已在 cuda:2 重新提交并运行中。\"}, \"exp_008_signal_survival\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:11:14.324Z\", \"updated_at\": \"2026-05-14T16:16:31.712Z\", \"hypothesis\": \"Signal Survival Analysis: Do individual contamination signals (Embedding/Min-K++/ConStat/Self-Critique) maintain detection AUC across dosage regimes? 4 signals × 3 regimes × 3 benchmarks AUC heatmap. C2 Core Contribution evidence.\", \"spec\": {\"command\": \"python signal_survival_analysis.py --exp002-only --skip-compute --output-dir exp008_exp002_output\", \"server\": \"cqa1-21977\", \"data_path\": \"exp002 signal scores (S1+S2+S4) × d000/d005/d100 × mmlu/gsm8k/arc\", \"data_count\": 27, \"model_name\": \"Qwen2.5-0.5B (3 dosages)\", \"seed\": 42, \"parent\": \"exp_002_signals_05B\", \"checkpoint_source\": \"exp002 signal outputs\", \"eval_data\": \"3 signals × 3 dosages × 3 benchmarks AUC\"}, \"conclusion\": \"success\", \"metrics\": {\"S1_d000_mmlu\": 0.5049, \"S1_d000_gsm8k\": 0.5502, \"S1_d000_arc\": 0.427, \"S1_d005_mmlu\": 0.953, \"S1_d005_gsm8k\": 0.9882, \"S1_d005_arc\": 0.995, \"S1_d100_mmlu\": 0.4943, \"S1_d100_gsm8k\": 0.4127, \"S1_d100_arc\": 0.501, \"S2_d005_mmlu\": 0.4655, \"S2_d005_gsm8k\": 0.4649, \"S2_d005_arc\": 0.4659, \"S4_d005_mmlu\": 0.5165, \"S4_d005_gsm8k\": 0.4947, \"S4_d005_arc\": 0.4325, \"signals_surviving\": 0, \"signals_total\": 3}, \"notes\": \"0/3 signals survive across regimes. S1 Embedding: AUC 0.95-0.995 at d005 but random at d000/d100 (ceiling effect at full contamination). S2 Min-K++ and S4 Self-Critique: random across all regimes (0.43-0.57). ConStat (S3) not computed (needs paraphrase data). Result validates C2: individual signals insufficient → need IRT multi-signal fusion.\", \"checkpoint_path\": \"N/A (analysis experiment, no checkpoint)\", \"log_path\": \"/root/contamcal-irt-calibration/exp008/signal_survival_analysis.log\", \"completed_at\": \"2026-05-14T16:16:31.712Z\"}, \"exp_001_eval_3B_d100_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:56:44.974Z\", \"updated_at\": \"2026-05-14T15:33:27.101Z\", \"spec\": {\"command\": \"run_eval_3B_d100_auto.sh → evaluate.py --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"data_path\": \"MMLU+ARC+GSM8K+HumanEval\", \"data_count\": 16697, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_3B\", \"eval_data\": \"original\", \"mc_format\": \"aligned (D017)\", \"log_path\": \"/root/runs/contamcal-irt-calibration/eval_3B_d100_aligned.log\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned/\", \"pid\": 362942, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter/\"}, \"hypothesis\": \"3B d100 s42 aligned eval — 100% contamination at largest scale, upper bound for 3B dose-response (MMLU/ARC only, GSM8K excluded per D018)\", \"parent\": \"exp_001_sft_d100_3B\", \"notes\": \"重跑成功。PID 362942 GPU 3。4 benchmarks 全部完成: MMLU 64.17%, GSM8K 69.67%, ARC 83.96%, HumanEval 12.20%。运行时间约 3h16m (20:06-23:22)。\", \"reproduce\": {\"finished_at\": \"2026-05-14T15:32:45.130Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:32:43.340Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:32:59.749439+00:00\"}]}, \"metrics\": {\"mmlu_accuracy\": 0.6417, \"gsm8k_exact_match\": 0.6967, \"arc_challenge_accuracy\": 0.8396, \"humaneval_pass1\": 0.122}}, \"exp_001_eval_05B_d005_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:20:22.394Z\", \"updated_at\": \"2026-05-14T15:21:22.628Z\", \"spec\": {\"hypothesis\": \"0.5B d005 s42 aligned eval — 5% contamination dose-response point (original aligned format D017)\", \"parent\": \"exp_001_sft_d005_05B_v3\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"server\": \"cqa1-21977\", \"command\": \"part of aligned_batch run (completed before batch timeout)\", \"data_path\": \"MMLU+GSM8K+ARC+HumanEval aligned\", \"data_count\": 16697, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\", \"eval_data\": \"original aligned (D017)\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_aligned\", \"log_path\": \"N/A (batch run)\"}, \"metrics\": {\"d005_aligned_mmlu\": 0.3255, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_arc\": 0.3285, \"d005_aligned_humaneval\": 0.0793}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:21:22.628Z\"}, \"exp_001_eval_05B_d100_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:50:02.679Z\", \"updated_at\": \"2026-05-14T15:19:06.659Z\", \"hypothesis\": \"0.5B d100 s42 aligned eval resubmit — d100 original + paraphrase, split from failed batch to avoid timeout\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 timeout 4h python exp001/evaluate.py ... d100 aligned + para_aligned serial\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": \"389866\", \"data_path\": \"MMLU+GSM8K+ARC original+paraphrase\", \"data_count\": \"2 runs\", \"model_name\": \"Qwen2.5-0.5B d100 s42\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_05B\", \"eval_data\": \"original + paraphrase aligned (D017)\"}, \"notes\": \"PID 389866 仍在运行（ps 确认 state=Rl, elapsed=19:31），tmux session 已死但 python 进程存活。Cron 误报 process gone（miss 4/5）因 tmux 检测失效。MMLU 已完成，GSM8K/ARC/HumanEval 进行中。等进程完成后立即提交 d100 paraphrase eval（--output-dir Qwen2.5-0.5B_d100_s42_para_aligned --paraphrase）。GPU 2 仍在使用。\", \"reproduce\": {\"finished_at\": \"2026-05-14T15:10:41.931Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T15:10:45.874Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:10:55.329493+00:00\"}]}}, \"exp_001_eval_05B_aligned_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:38:53.976Z\", \"updated_at\": \"2026-05-14T15:15:40.960Z\", \"hypothesis\": \"0.5B aligned-format eval batch (D017): d000/d005/d100 × original + paraphrase = 6 eval runs. Formal analysis results replacing legacy mc_format.\", \"spec\": {\"command\": \"bash run_aligned_eval_05B.sh both\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": \"332207\", \"data_path\": \"MMLU+ARC+GSM8K+HumanEval original+paraphrase\", \"data_count\": \"3 dosages × 2 eval_types × 4 benchmarks\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_0pct_05B / exp_001_sft_d005_05B_v3 / exp_001_sft_d100_05B\", \"eval_data\": \"original + paraphrase\", \"mc_format\": \"aligned (D017)\"}, \"parent\": \"exp_001_sft_d025_05B_v3\", \"notes\": \"0.5B aligned batch eval 因 timeout (EXIT_CODE=124) 中断。实际完成 4/6 runs: d000 orig+para, d005 orig+para 结果完整。d100 orig（仅跑48min被kill）+ d100 para（未启动）缺失。Timeline: d000_orig 18:52→d000_para 19:15→d005_orig 21:26→d005_para 21:51→d100_orig killed 22:39。d100 已单独重提交到 GPU 2。d005 指标待补录。d000 metrics: MMLU=39.79%, GSM8K=36.92%, ARC=46.93%, HumanEval=10.98%; d000_para: MMLU=44.28%, GSM8K=28.07%, ARC=47.92%, HumanEval=11.54%.\", \"metrics\": {\"d000_aligned_mmlu\": 0.3979, \"d000_aligned_gsm8k\": 0.3692, \"d000_aligned_arc\": 0.4693, \"d000_aligned_humaneval\": 0.1098, \"d000_para_aligned_mmlu\": 0.4428, \"d000_para_aligned_gsm8k\": 0.2807, \"d000_para_aligned_arc\": 0.4792, \"d000_para_aligned_humaneval\": 0.1154, \"d005_aligned_mmlu\": 0.3255, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_arc\": 0.3285, \"d005_aligned_humaneval\": 0.0793}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:39:10.195Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T14:39:14.014Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:39:18.504423+00:00\"}]}}, \"exp_001_eval_05B_d005\": {\"created_at\": \"2026-05-14T01:17:07.820Z\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": 0, \"data_path\": \"d005 contaminated checkpoint\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": \"cuda:1\", \"hypothesis\": \"0.5B 5% dosage contaminated model eval on 4 benchmarks — low-dosage contamination detection sensitivity test\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_eval_05B_d005.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_d005_05B\", \"pid\": \"255322\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T15:10:32.421Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T06:44:49.861Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:44:50.409Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:44:51.900757+00:00\"}]}, \"notes\": \"⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。\", \"metrics\": {\"mmlu\": 0.2929, \"gsm8k\": 0.3601, \"arc_challenge\": 0.2858, \"humaneval_pass1\": 0.0793, \"mmlu_correct\": 4113, \"mmlu_total\": 14042, \"gsm8k_correct\": 475, \"gsm8k_total\": 1319, \"arc_correct\": 335, \"arc_total\": 1172, \"humaneval_correct\": 13, \"humaneval_total\": 164}}, \"exp_006_irt_05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:20:20.389Z\", \"updated_at\": \"2026-05-14T14:53:16.180Z\", \"spec\": {\"command\": \"python run_exp006.py (Stan NUTS 4 chains, warmup=1000, samples=1000, max_depth=12, delta=0.95)\", \"server\": \"cqa1-21977\", \"data_path\": \"exp002 signals → exp006 direct load\", \"data_count\": \"MMLU 14042 items × 9 models (first benchmark)\", \"model_name\": \"contam_irt_4pl_simple (Stan NUTS)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_05B/\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp006_irt_05B.log\", \"pid\": \"386298\"}, \"notes\": \"KILLED by Director 指令: 混合 scale (0.5B+1.5B+3B) + legacy 格式 + 多余 seed 的错误数据在拟合。Stan NUTS 4 chains (PID 386298-386301) 运行 ~30min 后终止。代码修复中: 正则改为 _d(\\\\d+)_s(\\\\d+)(_para)?(_aligned)?$, 增加 --model-scale 和 --seed 过滤参数。等 d025/d100 aligned eval 完成后再用修复后代码重跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T14:53:12.892Z\"}, \"exp_003_rrf_05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:17:36.003Z\", \"updated_at\": \"2026-05-14T14:18:05.370Z\", \"spec\": {\"command\": \"python rrf_aggregation.py --generate-exposure\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp002/signals/\", \"data_count\": \"3 dosages x 3 benchmarks = 9 signal sets\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp003/exposure_scores.json\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:18:05.370Z\"}, \"exp_002_signals_05B\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T08:45:35.964Z\", \"updated_at\": \"2026-05-14T14:04:12.884Z\", \"hypothesis\": \"0.5B contamination signal computation (S1 Embedding/S2 Min-K++/S4 Self-Critique) on d000/d005/d100 × mmlu/gsm8k/arc = 27 signal tasks. Critical path for exp-003 RRF → exp-006 IRT.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 0.5B --gpu 0 2>&1 | tee run_05B.log\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 370957, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/ + /root/autodl-tmp/exp001/checkpoints/\", \"data_count\": \"3 dosages x 3 benchmarks x 3 signals = 27 tasks (6 cached, ~21 remaining)\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_05B.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/\", \"signals\": [\"embedding\", \"minkpp\", \"selfcritique\"], \"note\": \"v5 restart: timeout 4h, per-signal cache, selfcritique max_tokens 64. 6 signals cached from v4.\"}, \"notes\": \"v5 完成 9/9 PASS。d000/d005/d100 × mmlu/gsm8k/arc_challenge 全部完成。9 个 signals_merged 文件已产出。三项修复奏效: timeout 4h, per-signal cache, max_tokens 64。GPU 0 已释放。\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:04:10.508Z\"}, \"exp_001_sft_d005_3B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:54:49.962Z\", \"updated_at\": \"2026-05-14T13:12:32.498Z\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-3B (seed=42): low-dosage contamination for 3B dose-response curve\", \"notes\": \"Cron auto-submitted on cuda:4. Wrapper PID 335346, actual training PID 335351. 48% complete (1511/3177 steps), loss ~1.11, epoch 0.35. ETA ~20:40 UTC.\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-14T09:11:03.513Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-14T12:56:51.735Z\", \"training_hours\": 3.76}, \"spec\": {\"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42\"}, \"pid\": \"335346\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_3B.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:57:02.160391+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"training_hours\": 3.76, \"final_loss\": 1.11, \"total_steps\": 3177, \"epochs\": 1}, \"completed_at\": \"2026-05-14T13:12:28.865Z\"}, \"exp_001_eval_3B_d000_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:50.047Z\", \"updated_at\": \"2026-05-14T13:11:39.859Z\", \"hypothesis\": \"3B d000 s42 aligned eval (v5 代码) — 诊断 GSM8K 崩塌 (0.117→?) 并建立正式 aligned baseline。含 GSM8K 答案提取修复（如需要）。\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_aligned/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_aligned.log\"}, \"notes\": \"D018 决策：3B GSM8K 标记为 \\\"SFT-degraded, excluded from dose-response\\\"。3B MMLU/ARC 仍可用。不重训 LoRA 配置。诊断根因：LoRA SFT (r=16, alpha=32, lr=2e-4, 7 proj) 导致 CoT 灾难性遗忘。\", \"reproduce\": {\"finished_at\": \"2026-05-14T13:05:47.172Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:05:58.887588+00:00\"}]}, \"metrics\": {\"mmlu_accuracy\": 0.634, \"gsm8k_exact_match\": 0.1198, \"arc_challenge_accuracy\": 0.8276, \"humaneval_pass_at_1\": 0.1159}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T13:10:19.068Z\"}, \"exp_001_eval_15B_d100_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:14.296Z\", \"updated_at\": \"2026-05-14T10:22:16.449Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-1.5B --adapter-path Qwen2.5-1.5B_d100_s42/lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"325300\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d100_s42.log\", \"submitted_at\": \"2026-05-14T07:39:13.887Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42\", \"wall_clock_seconds\": 9420, \"gpu_hours\": 2.62}, \"hypothesis\": \"100% dosage 1.5B s42 contaminated eval on 4 benchmarks — upper bound contamination score inflation for 1.5B scale\", \"parent\": \"exp_001_sft_d100_15B_v2\", \"notes\": \"使用 D017 aligned 格式 (--mc-format aligned, 默认)。与 0.5B v5 eval (legacy 格式) 不直接可比。分析时需标注 mc_format。\", \"reproduce\": {\"finished_at\": \"2026-05-14T10:17:43.615Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:17:48.927069+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5933, \"mmlu_correct\": 8331, \"mmlu_total\": 14042, \"gsm8k_exact_match\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319, \"arc_challenge_accuracy\": 0.7688, \"arc_challenge_correct\": 901, \"arc_challenge_total\": 1172, \"humaneval_pass_at_1\": 0.3049, \"humaneval_correct\": 50, \"humaneval_total\": 164}, \"completed_at\": \"2026-05-14T10:21:14.812Z\"}, \"exp_001_eval_3B_raw_gen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:52:48.654Z\", \"updated_at\": \"2026-05-14T10:04:16.309Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-3B --benchmarks gsm8k humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"318748\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_raw_gen.log\", \"submitted_at\": \"2026-05-14T06:52:48.549Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\", \"data_count\": 2, \"model_name\": \"Qwen2.5-3B\", \"seed\": 0, \"eval_data\": \"gsm8k,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/\", \"wall_clock_seconds\": 11487.8, \"gpu_hours\": 3.19}, \"reproduce\": {\"finished_at\": \"2026-05-14T09:34:31.469Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:34:36.144359+00:00\"}]}, \"metrics\": {\"gsm8k\": 0.605, \"humaneval\": 0}, \"notes\": \"3B raw base eval (generative benchmarks). GSM8K=0.6050 正常。HumanEval=0.0000: base model 生成教程式文本+markdown代码块，评估器无法提取可执行代码。结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/。GSM8K 0.605 vs d000 SFT 0.117 = -48.8pp 崩塌待诊断。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T10:04:16.309Z\"}, \"exp_001_eval_05B_raw\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:52:20.023Z\", \"updated_at\": \"2026-05-14T09:18:21.577Z\", \"hypothesis\": \"Raw Qwen2.5-0.5B base model eval (no SFT, no adapter) on 4 benchmarks — establish true pre-SFT baseline for MC distribution analysis\", \"spec\": {\"command\": \"evaluate.py on raw Qwen2.5-0.5B (no adapter)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"318424\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_raw.log\", \"submitted_at\": \"2026-05-14T06:52:25.551Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MMLU+GSM8K+ARC+HumanEval\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B (raw base)\", \"seed\": 42, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"N/A (raw base)\", \"wall_clock_seconds\": 8756.0, \"gpu_hours\": 2.43}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.2302, \"gsm8k\": 0.1592, \"arc_challenge\": 0.2261, \"humaneval\": \"incomplete (hung at 51/164)\"}, \"notes\": \"Raw 0.5B base model eval。MMLU/GSM8K/ARC 完成，HumanEval 卡在 51/164 (代码执行死循环)，kill 释放 cuda:1。HumanEval 为 appendix-only (D009)，不影响主分析。Raw base 分数远低于 SFT d000 baseline (MMLU 0.23 vs 0.40)，确认 SFT 有效提升。\", \"completed_at\": \"2026-05-14T09:18:21.577Z\"}, \"exp_001_sft_d005_15B\": {\"created_at\": \"2026-05-14T00:19:54.331Z\", \"gpu\": 4, \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): low-dosage contamination for dose-response curve, Phase 3 priority 1\", \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42\", \"command\": \"train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_005.jsonl\", \"data_count\": 50826, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"gpu\": \"cuda:4\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_15B.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"271916\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T03:12:39.622Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20070.3, \"gpu_hours\": 5.58}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T09:11:14.625Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T08:47:04.834Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T08:47:09.892Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:47:17.186022+00:00\"}]}, \"notes\": \"训练实际已完成。3177/3177 steps, train_loss=1.2637, mean_token_accuracy=0.7308, epoch=1.0。LoRA adapter 已保存。EXIT_CODE=129 (SIGHUP) 发生在 Training complete 之后，属于 wrapper PID false positive（与 exp_001_sft_d100_3B 同一已知模式）。Checkpoint: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter\", \"metrics\": {\"train_loss\": 1.2637, \"mean_token_accuracy\": 0.7308, \"train_runtime_s\": 19864.7, \"epoch\": 1}}, \"exp_001_sft_d025_05B_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:22:14.069Z\", \"updated_at\": \"2026-05-14T08:36:01.933Z\", \"spec\": {\"command\": \"python train_sft.py --model Qwen2.5-0.5B --data sft_dosage_025.jsonl --gpu 2 --seed 42\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"324153\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d025_05B_v3.log\", \"submitted_at\": \"2026-05-14T07:31:46.339Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"wall_clock_seconds\": 3855.6, \"gpu_hours\": 1.07}, \"hypothesis\": \"25% dosage contaminated SFT on Qwen2.5-0.5B (seed=42, v3) — 用于 dose-response 曲线的 mid-low dosage 数据点\", \"reproduce\": {\"finished_at\": \"2026-05-14T08:31:11.706Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:31:17.136838+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter\", \"metrics\": {\"final_loss\": 1.5178, \"mean_train_loss\": 1.5479, \"entropy\": 1.5415, \"mean_token_accuracy\": 0.6697, \"num_tokens\": 20058085, \"total_steps\": 3384, \"epoch\": 1, \"train_samples_per_second\": 15.52, \"train_steps_per_second\": 0.97, \"training_time_min\": 58.1, \"exit_code\": 0, \"lora_adapter_size_mb\": 33.6, \"checkpoint_size_mb\": 166, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": 0.0284, \"delta_mean_train_loss\": 0.0091, \"delta_token_accuracy\": -0.0123, \"delta_training_time_min\": 5.2}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T08:36:01.933Z\"}, \"exp_001_eval_05B_d100_v5\": {\"created_at\": \"2026-05-14T02:39:57.338Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v5, 最终干净提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ...\\\"\", \"data_count\": 4, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v5.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_d100_05B\", \"pid\": \"266780\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:39:57.046Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 17504.7, \"gpu_hours\": 4.86}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T08:01:34.216Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T07:30:37.450Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:30:41.628489+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.2322, \"gsm8k\": 0.3571, \"arc_challenge\": 0.227, \"humaneval_pass1\": 0.0854}, \"completed_at\": \"2026-05-14T07:31:41.784Z\", \"notes\": \"结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。d100 MC 分数低于 d000 baseline (MMLU -17.3pp, ARC -15.1pp) 系格式不匹配所致。\"}, \"exp_001_eval_05B_d000_s42_v5\": {\"created_at\": \"2026-05-14T02:39:41.292Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v5, 最终干净提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ...\\\"\", \"data_count\": 4, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v5.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_0pct_05B\", \"pid\": \"266511\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:39:41.108Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 17519.2, \"gpu_hours\": 4.87}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T08:01:31.086Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T07:30:31.429Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:30:35.061894+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.4049, \"gsm8k\": 0.3647, \"arc_challenge\": 0.378, \"humaneval\": 0.1098}, \"completed_at\": \"2026-05-14T07:31:40.285Z\", \"notes\": \"结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式 dose-response 分析需用 aligned 格式重跑 (D017 延伸决策)。\"}, \"exp_001_sft_d100_15B_v2\": {\"created_at\": \"2026-05-14T01:17:47.114Z\", \"parent\": \"exp_001_sft_d100_15B\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42\", \"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\", \"data_count\": 66533, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"gpu\": [\"cuda:0\"], \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): v2 retry with batch_size=1 to fix OOM. Maximum contamination for 1.5B scale.\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_15B_v2.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"251924\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:39:22.684Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T07:39:22.684Z\"}, \"exp_001_eval_3B_d000_s42\": {\"completed_at\": \"2026-05-13T23:43:16.876Z\", \"created_at\": \"2026-05-13T23:36:54.086Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"v1 --gpu param caused evaluate.py crash. Resubmitted without --gpu.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:47:56.373112+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"0% dosage 3B s42 baseline evaluation on 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval) to establish ground-truth scores for calibration error computation\", \"notes\": \"v1 failed (--gpu bug), v2 resubmitted with CUDA_VISIBLE_DEVICES. PID 249294 confirmed running on GPU 1 (cron monitored).\", \"parent\": \"exp_001_sft_0pct_3B\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 26000, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42.log\", \"model_name\": \"Qwen2.5-3B\", \"pid\": \"249294\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T08:54:00Z\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:03:36.187Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T06:47:54.565Z\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.634, \"gsm8k\": 0.117, \"arc\": 0.822, \"humaneval\": 0.116}}, \"exp_001_sft_d025_05B_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:53:14.092Z\", \"updated_at\": \"2026-05-14T06:21:14.334Z\", \"hypothesis\": \"25% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v2 retry with correct CUDA_VISIBLE_DEVICES=5 binding. Dose-response curve intermediate point.\", \"parent\": \"exp_001_sft_d025_05B\", \"spec\": {\"pid\": 299016, \"gpu\": [\"cuda:5\"], \"server\": \"cqa1-21977\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && export CUDA_VISIBLE_DEVICES=5 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42 --gpu 0 --batch-size 4 --grad-accum 4 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache'\", \"model_name\": \"Qwen2.5-0.5B\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d025_05B_v2.log\"}, \"conclusion\": \"failed\", \"failure_reason\": \"SIGKILL (exit 137) at step 36/3384. Training command lacked proper CUDA_VISIBLE_DEVICES export — likely landed on GPU 0 conflicting with 1.5B d100 SFT, causing OOM. PID 296698 killed, PID 299016 is residual wrapper.\", \"completed_at\": \"2026-05-14T06:21:14.334Z\"}, \"exp_001_eval_05B_d100_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T02:26:41.093Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T02:37:02.468237+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:36:56.211Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v2.log\", \"pid\": \"263784\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:28:36.407Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13875.1, \"gpu_hours\": 3.85}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T06:19:51.550Z\", \"completed_at\": \"2026-05-14T06:19:51.550Z\"}, \"exp_001_sft_d025_05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:24:39.757Z\", \"updated_at\": \"2026-05-14T04:54:16.202Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42 --gpu 0 --batch-size 4 --grad-accum 4 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"292940\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d025_05B.log\", \"submitted_at\": \"2026-05-14T04:49:12Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": \"~16633 (25% dosage)\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42\", \"wall_clock_seconds\": 75.0, \"gpu_hours\": 0.02}, \"reproduce\": {\"finished_at\": \"2026-05-14T04:50:22.652Z\"}, \"failure_reason\": \"CUDA OOM: 分配 cuda:5 但实际跑到 GPU 0（CUDA_VISIBLE_DEVICES 注入失效，已知 recurring bug）。GPU 0 被 exp_001_sft_d100_15B_v2 (9.81GiB) + PID 291380 (13GiB) 占满。修复：命令中显式 export CUDA_VISIBLE_DEVICES=5。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T04:50:27.011Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:50:31.770719+00:00\"}]}, \"notes\": \"OOM失败：指定 cuda:5 但实际跑到 GPU 0。GPU 5 上残留 4 个重复 1.5B d005 进程 (PID 292422/292423/292425/292426)。根因：tmux 提交时未设 CUDA_VISIBLE_DEVICES，--gpu 参数未正确绑定设备。\"}, \"exp_001_eval_3B_d000_s123\": {\"created_at\": \"2026-05-14T00:18:07.960Z\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 26000, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s123.log\", \"model_name\": \"Qwen2.5-3B\", \"pid\": \"242581\", \"seed\": 123, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T00:18:36.008Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 15706.2, \"gpu_hours\": 4.36, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:44:59.509Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T04:39:50.139Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:39:53.713806+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.6362, \"gsm8k_exact_match\": 0.1759, \"arc_challenge_accuracy\": 0.8294, \"humaneval_pass_at_1\": 0.0854}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123\", \"completed_at\": \"2026-05-14T04:40:22.199Z\"}, \"exp_001_eval_15B_d000_s123\": {\"completed_at\": \"2026-05-13T23:39:26.418Z\", \"created_at\": \"2026-05-13T22:30:41.501Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:42:53.247372+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=2: --gpu 0 参数导致 evaluate.py 崩溃。重跑时需去掉 --gpu 参数。\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123\", \"checkpoint_source\": \"exp_001_sft_0pct_15B_s123\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": \"4 benchmarks\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123/\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:5\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"250600\", \"seed\": 123, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T00:59:22.874Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13475.7, \"gpu_hours\": 3.74}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:43:58.619Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T04:42:48.051Z\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.5762, \"gsm8k\": 0.6331, \"arc_challenge\": 0.7662, \"humaneval_pass@1\": 0.1707}}, \"exp_005_noise_prop_v2\": {\"completed_at\": \"2026-05-13T22:44:09.262Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T20:47:35.807Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T21:09:53.826444+00:00\"}, {\"action\": \"manual_fix\", \"event\": \"status_rollback\", \"reason\": \"Cron false positive: server=\\\"local\\\" not in SSH list. PID 251971 alive, 2 Stan chains at 42% CPU. Rolled back DONE/failed → RUNNING.\", \"ts\": \"2026-05-13T21:12:00.000Z\"}]}, \"failure_reason\": \"根因：/tmp tmpfs 磁盘配额耗尽。ME model 先跑 95min 生成 ~1GB CSV（9000 tau + 9000 log_lik × 4 chains）耗尽 3.9GB tmpfs。Simple model 写 CSV 时 disk quota exceeded → 4 chains 全部 retcode=1。ME model Rhat=1.945 是独立问题：10231 参数 vs 9000 观测，严重欠识别，需换用 analytic 版本。修复：(1) output_dir 设到非 tmpfs (2) 先跑 simple 再跑 ME (3) ME 换 contam_irt_4pl_me_analytic.stan (4) σ_e=0.1/0.3 均可收敛。\", \"hypothesis\": \"Same as exp_005: ME model CI width increases monotonically with σ_e; simple model does not. v2 fixes: sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12.\", \"notes\": \"失败根因: 1) /tmp tmpfs 3.9GB 耗尽（ME模型生成~1GB Stan CSV，Simple 4 chains全部retcode=1）; 2) ME模型严重欠识别（10231参数 vs 9000观测，Rhat=1.945）。诊断结果: σ_e=0.3 simple收敛良好(γ=0.458, true=0.5, Rhat=1.007); σ_e=0.1 simple收敛但γ偏高57.5%(0.788 vs 0.5)——identifiability限制非bug。v3已启动修复两个根因。\", \"parent\": \"exp_005_noise_prop\", \"retry_count\": 0, \"spec\": {\"command\": \"python run_noise_propagation.py --output-dir output_v2 --base-seed 42 --n-seeds 5\", \"data_count\": \"5 σ_e levels × 5 seeds × 2 models = 50 Stan fits\", \"data_path\": \"synthetic (generated in-script)\", \"fixes\": \"sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12\", \"log_path\": \"artifacts/exp005_noise_propagation/exp005_v2.log\", \"model_name\": \"4PL+γ IRT (CmdStanPy NUTS, max_treedepth=12)\", \"pid\": 251971, \"seed\": \"42-46\", \"server\": \"local (CPU only)\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T03:25:33.715Z\"}, \"exp_001_eval_15B_d000_s42_v2\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter\", \"completed_at\": \"2026-05-14T03:12:11.373Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T00:23:20.112Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T03:09:29.636850+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log\", \"metrics\": {\"arc_challenge_accuracy\": 0.7756, \"arc_challenge_correct\": 909, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 840, \"gsm8k_exact_match\": 0.6368, \"gsm8k_total\": 1319, \"humaneval_correct\": 21, \"humaneval_pass_at_1\": 0.128, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5753, \"mmlu_correct\": 8079, \"mmlu_total\": 14042}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:09:26.521Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 26000, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:4\"], \"gpu_hours\": 2.81, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"243290\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T00:23:34.122Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10117.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T03:12:11.373Z\"}, \"exp_001_eval_05B_d100\": {\"completed_at\": \"2026-05-14T02:21:35.372Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-14T01:15:49.903Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T02:21:37.615359+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:21:33.626Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": 4, \"data_path\": \"d100 contaminated checkpoint\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 0.88, \"gpu_ids\": [\"cuda:2\"], \"hypothesis\": \"0.5B 100% dosage contaminated model eval on 4 benchmarks — upper bound of contamination-induced score inflation\", \"log_path\": \"/tmp/eval_d100.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_d100_05B\", \"pid\": \"254667\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T01:29:00Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3155.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T02:21:35.372Z\"}, \"exp_001_eval_05B_d000_s123\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter\", \"completed_at\": \"2026-05-14T01:29:09.875Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T22:30:40.455Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T01:26:32.038369+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log\", \"metrics\": {\"arc_challenge_accuracy\": 0.3976, \"gsm8k_exact_match\": 0.3404, \"humaneval_pass_at_1\": 0.1037, \"mmlu_accuracy\": 0.4182}, \"reproduce\": {\"finished_at\": \"2026-05-14T01:26:29.607Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter\", \"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": null, \"data_path\": \"d000 (baseline, no contamination)\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 2.72, \"gpu_ids\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_train_05B_d000_s123\", \"pid\": \"229516\", \"seed\": 123, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T22:45:48.124Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9801.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:29:09.875Z\"}, \"exp_001_sft_d100_15B\": {\"completed_at\": \"2026-05-14T01:23:40.712Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:37:43.653Z\", \"failure_reason\": \"OOM batch_size=2, replaced by v2\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error\", \"notes\": \"batch_size=1, grad_accum=16 (防 OOM，与 1.5B d000 baseline 一致)。66533 samples, 1 epoch。数据与 0.5B d100 完全相同，含 MMLU+ARC+GSM8K 全部 paraphrases（noisy contamination condition）。\", \"retry_count\": 0, \"spec\": {\"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\", \"data_count\": 66533, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"248993\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:23:40.711Z\"}, \"exp_001_sft_d005_05B_v3\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42\", \"completed_at\": \"2026-05-14T00:58:15.977Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T23:52:39.321Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T00:55:43.945907+00:00\"}]}, \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v3 retry with correct --gpu 5 (v1/v2 OOM due to --gpu 0 conflicting with d100 on GPU 0). Minimum contamination level for dose-response threshold.\", \"metrics\": {\"checkpoint_size_mb\": 166, \"entropy\": 1.5874, \"epoch\": 1, \"exit_code\": 0, \"final_loss\": 1.478, \"lora_adapter_size_mb\": 33.6, \"mean_train_loss\": 1.5424, \"num_tokens\": 19657865, \"token_accuracy\": 0.667, \"total_steps\": 3177, \"train_samples_per_second\": 15.09, \"train_steps_per_second\": 0.943, \"training_time_min\": 56.14, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": -0.0114, \"delta_mean_train_loss\": 0.0036, \"delta_token_accuracy\": -0.015, \"delta_training_time_min\": 3.24}}, \"notes\": \"dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。v3 已修复 --gpu 5（v1/v2 均为 --gpu 0 错误）。此 run 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition。\", \"parent\": \"exp_001_sft_d005_05B\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:55:38.416Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (SFT retry, not eval)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": 50826, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"eval_data\": \"N/A (SFT retry, not eval)\", \"gpu\": [\"cuda:5\"], \"gpu_hours\": 1.0, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v3.log\", \"model_name\": \"Qwen2.5-0.5B\", \"pid\": \"239729\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:58:01.548Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3614.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:58:15.977Z\"}, \"exp_001_sft_d100_05B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42\", \"completed_at\": \"2026-05-14T00:53:49.656Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T23:36:13.403Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T00:50:19.949448+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"metrics\": {\"exit_code\": 0, \"final_loss\": 1.5943, \"mean_train_loss\": 1.5662, \"num_tokens\": 21575068, \"token_accuracy\": 0.666, \"total_steps\": 4160, \"train_samples_per_second\": 16.09, \"train_steps_per_second\": 1.006, \"training_time_min\": 68.9, \"vs_baseline_0pct\": {\"accuracy_delta\": \"-0.016 (-2.3%)\", \"loss_delta\": \"+0.0274 (+1.8%)\", \"time_delta\": \"+16min (+30%)\"}}, \"notes\": \"dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533。此 run 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition。\", \"pid\": \"235243\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-14T00:50:16.569Z\", \"gpu\": \"cuda:0\", \"server\": \"cqa1-21977\", \"started_at\": \"2026-05-13T23:38:41.749Z\", \"training_hours\": 1.19}, \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.23, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"pid\": \"235243\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:39:51.510Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4438.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:55:14.218Z\"}, \"exp_001_sft_0pct\": {\"checkpoint_path\": \"N/A (parent entry)\", \"completed_at\": \"2026-05-14T00:36:52.832Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:26:42.106Z\", \"hypothesis\": \"0% dosage (clean) SFT baselines on Qwen2.5-0.5B/1.5B/3B establish ground-truth benchmark scores for calibration error computation; LoRA r=16 alpha=32 1-epoch training on pure instruction data should preserve base model capability\", \"log_path\": \"N/A (parent entry)\", \"notes\": \"Parent entry for 3 sub-experiments (05B/15B/3B). All confirmed running.\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:36:52.832Z\"}, \"exp_001_sft_0pct_3B_s123\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123\", \"completed_at\": \"2026-05-14T00:23:18.290Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:39:01.606Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T00:16:17.727184+00:00\"}]}, \"hypothesis\": \"0% dosage clean baseline Qwen2.5-3B seed=123 (second seed for variance estimation)\", \"metrics\": {\"adapter_model_mb\": 114, \"adapter_size_mb\": 488, \"checkpoint_size_mb\": 488, \"epochs\": 1, \"final_loss\": 1.114, \"mean_token_accuracy\": 0.7505, \"mean_train_loss\": 1.1309, \"steps_completed\": 3125, \"total_steps\": 3125, \"total_tokens\": 19555717, \"train_samples_per_second\": 3.91, \"training_time_min\": 213.1}, \"notes\": \"OOM 修复后重提交 --gpu 3 (物理 GPU 3)。Worker 确认 PID 216249 训练中，ETA ~3.4h\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:16:04.357Z\"}, \"retry_count\": 0, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123 --seed 123 --gpu 3 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": \"50000\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B_s123.log\", \"model_name\": \"Qwen2.5-3B\", \"pid\": \"216935\", \"seed\": 123, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:23:18.290Z\"}, \"exp_001_eval_15B_d000_s42\": {\"completed_at\": \"2026-05-14T00:23:17.209Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T21:30:03.433Z\", \"failure_reason\": \"卡死 11+小时：GPU 利用率 0%，显存占 5820MiB，输出目录为空。根因：spec 使用相对路径 (--model-path Qwen2.5-1.5B --adapter-path lora_adapter) 而非绝对路径，导致模型加载异常挂起。已 kill -9。\", \"hypothesis\": \"0% dosage 1.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation\", \"parent\": \"exp_001_sft_0pct_15B\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter/\", \"command\": \"python evaluate.py --model-path Qwen2.5-1.5B --adapter-path lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": \"~26000 items total\", \"data_path\": \"MMLU/GSM8K/ARC-Challenge/HumanEval (HuggingFace datasets)\", \"eval_data\": \"MMLU, GSM8K, ARC-Challenge, HumanEval (original)\", \"gpu\": [\"cuda:4\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42.log\", \"model_name\": \"Qwen2.5-1.5B + LoRA (d000_s42)\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42\", \"pid\": \"221376\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:23:17.209Z\"}, \"exp_001_sft_d005_05B_v2\": {\"completed_at\": \"2026-05-13T23:49:48.629Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:48:24.508Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T23:49:51.462263+00:00\"}]}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 578.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 459.38 MiB is free. Process 235248 has 21.47 GiB memory in use. Including non-PyTorch memory, this process has 1.58 GiB memory in use. Of the allocated\", \"gpu\": \"cuda:5\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry after v1 OOM crash (GPU 5 conflict with zombie eval process). GPU 5 now clear.\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v2.log\", \"notes\": \"v2 OOM 根因非 GPU 5 残留进程，而是 --gpu 0 导致训练实际跑在 GPU 0（d100 占满 22GB），GPU 5 从未被使用。已在 r3 修复为 --gpu 5。\", \"pid\": \"237300\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-13T23:49:47.033Z\"}, \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"gpu_hours\": 0.01, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v2.log\", \"pid\": \"237300\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:49:27.702Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:59:33.029Z\"}, \"exp_001_sft_d005_05B\": {\"completed_at\": \"2026-05-13T23:42:35.135Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-13T23:36:15.352Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T23:42:37.857937+00:00\"}]}, \"failure_reason\": \"CUDA OOM at step 8/3177 — zombie 3B eval process (PID 234755) 占 6.8GB GPU 5 显存，导致 SFT 训练分配失败。已重试为 exp_001_sft_d005_05B_v2。\", \"gpu\": \"cuda:5\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): minimum contamination level to detect dose-response threshold; paired with d100 for min-max comparison\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B.log\", \"notes\": \"v1 OOM at step 8/3177 — GPU 5 有残留进程 PID 234755 占 6.8GB。PID 236994 (submit_training_job 重提交) 也使用了 --gpu 0，实际跑到 GPU 0 而非 GPU 5，同样 OOM。根因：--gpu 0 导致 CUDA_VISIBLE_DEVICES 被脚本覆盖为 0。已在 r3 修复为 --gpu 5。\", \"pid\": \"235331\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-13T23:42:32.872Z\", \"gpu\": \"cuda:5\", \"server\": \"cqa1-21977\", \"started_at\": \"2026-05-13T23:38:42.505Z\", \"training_hours\": 0.06}, \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B.log\", \"pid\": \"236994\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:49:14.077Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:59:30.512Z\"}, \"exp_001_sft_100pct_05B\": {\"completed_at\": \"2026-05-13T23:49:10.741Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:41:15.631Z\", \"failure_reason\": \"Duplicate registry entry — actual training tracked by exp_001_sft_d100_05B (PID 235243, cron monitored)\", \"hypothesis\": \"100% contamination dosage on 0.5B establishes upper bound of score inflation; comparing with 0% baseline reveals maximum contamination effect across MMLU/GSM8K/ARC benchmarks\", \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\", \"data_count\": 66533, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:49:12.007Z\"}, \"exp_001_sft_0pct_3B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42\", \"completed_at\": \"2026-05-13T23:25:49.016Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:44:40.471Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-13T23:23:43.393661+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"metrics\": {\"adapter_size_mb\": 115, \"checkpoint_size_mb\": 488, \"exit_code\": 0, \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"steps\": \"3125/3125\", \"token_accuracy\": 0.734, \"training_time_min\": 214.7}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:23:41.844Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --seed 42 --gpu 5 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"gpu_hours\": 3.69, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"pid\": \"210666\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T19:44:40.431Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13268.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:25:49.016Z\"}, \"exp_001_sft_injection\": {\"completed_at\": \"2026-05-13T23:14:30.258Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T17:28:01.546Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T19:18:08.635006+00:00\"}, {\"action\": \"manual_fix\", \"event\": \"status_rollback\", \"reason\": \"Cron misidentified old PID as dead → auto-failed. 3 paraphrase processes (GPU 0-2) still running. Rolled back DONE/failed → RUNNING per Director instruction.\", \"ts\": \"2026-05-13T19:32:00.000Z\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T23:14:43.962197+00:00\"}]}, \"failure_reason\": \"\", \"hypothesis\": \"Controlled SFT contamination injection produces dose-dependent score inflation on contaminated benchmarks; 4PL+γ IRT can recover true (uncontaminated) performance from calibrated scores with proper uncertainty bounds\", \"metrics\": {\"arc_qc_pass\": 697, \"arc_qc_rate\": 0.595, \"arc_total\": 1172, \"gsm8k_qc_pass\": 228, \"gsm8k_qc_rate\": 0.173, \"gsm8k_total\": 1319, \"humaneval_total\": 164, \"mmlu_qc_pass\": 6596, \"mmlu_qc_rate\": 0.47, \"mmlu_total\": 14042}, \"notes\": \"MMLU paraphrase 3-attempt QC 重试流程: Attempt 1 ✅ (878 batches, 4112/14042 QC pass 29.3%, ~90min). Attempt 2 进行中 (v2重启, 439 batches total, 进度~22%). Attempt 3 待定. 输出在全部 attempt 结束后一次性写出 mmlu_paraphrases.json. GSM8K ✅ 1319条(QC 17.3%), ARC ✅ 1172条(QC 59.5%).\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:14:29.355Z\"}, \"retry_count\": 0, \"spec\": {\"command\": \"Phase 1 paraphrase: GPU 0 MMLU (PID 204467 v3, vLLM bs=16). GSM8K + ARC completed.\", \"data_count\": \"45 SFT runs + 90 eval runs (original+paraphrased)\", \"data_path\": \"MMLU+GSM8K+ARC-Challenge+HumanEval paraphrases → SFT data mixing\", \"gpu\": \"cuda:0 (MMLU vLLM, still running). cuda:1/2 freed (GSM8K+ARC done).\", \"model_name\": \"Qwen2.5-0.5B/1.5B/3B (LoRA SFT), Qwen2.5-7B-Instruct (paraphrase)\", \"note\": \"GSM8K: 1319 paraphrases (228 QC pass, 17.3%). ARC: 1172 paraphrases (697 QC pass, 59.5%). MMLU: Attempt 1 done (878 batches, 29.3% QC), Attempt 2 in progress (439 batches total, ~22%), Attempt 3 pending. HumanEval: done (appendix per D009).\", \"pid\": \"204467\", \"seed\": \"42,123,456\", \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:21:54.827Z\"}, \"exp_001_sft_0pct_15B_s123\": {\"completed_at\": \"2026-05-13T22:30:26.882Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:35:07.346Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-1.5B seed=123 (second seed for variance estimation)\", \"metrics\": {\"token_acc\": 0.731, \"train_loss\": 1.2602, \"train_time_min\": 101.5}, \"notes\": \"OOM 修复后重提交 --gpu 2 (物理 GPU 2)。Worker 确认 PID 216106 训练中 (1/3125 steps, ~2.58s/it)\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123 --seed 123 --gpu 2 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": \"50000\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B_s123.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"216111\", \"seed\": 123, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T22:30:26.882Z\"}, \"exp_001_sft_0pct_05B_s123\": {\"completed_at\": \"2026-05-13T22:30:25.819Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:35:04.879Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance estimation)\", \"metrics\": {\"token_acc\": 0.676, \"train_loss\": 1.5393, \"train_time_min\": 54.5}, \"notes\": \"OOM 修复后重提交 --gpu 1 (物理 GPU 1)。Worker 确认 PID 216028 训练中 (2/3125 steps, ~1.87s/it)\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123 --seed 123 --gpu 1 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": \"50000\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B_s123.log\", \"model_name\": \"Qwen2.5-0.5B\", \"pid\": \"216033\", \"seed\": 123, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T22:30:25.819Z\"}, \"exp_001_sft_0pct_15B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42\", \"completed_at\": \"2026-05-13T21:27:59.348Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:39:48.369Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-13T21:25:42.551081+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log\", \"metrics\": {\"adapter_size_mb\": 71, \"checkpoint_size_mb\": 313, \"exit_code\": 0, \"final_loss\": 1.2039, \"mean_train_loss\": 1.2599, \"steps\": \"3125/3125\", \"token_accuracy\": 0.711, \"training_time_min\": 101.5}, \"reproduce\": {\"finished_at\": \"2026-05-13T21:25:40.979Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42 --seed 42 --gpu 4 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:4\"], \"gpu_hours\": 1.78, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log\", \"pid\": \"210116\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T19:41:11.760Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6407.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T21:27:59.348Z\"}, \"exp_001_sft_0pct_05B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42\", \"completed_at\": \"2026-05-13T20:36:06.744Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:35:01.170Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-13T20:33:54.496690+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log\", \"metrics\": {\"adapter_size_mb\": 34, \"checkpoint_size_mb\": 166, \"exit_code\": 0, \"final_loss\": 1.4894, \"mean_train_loss\": 1.5388, \"steps\": \"3125/3125\", \"token_accuracy\": 0.682, \"training_time_min\": 52.9}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:33:53.420Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42 --seed 42 --gpu 3 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.98, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log\", \"pid\": \"208933\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T19:37:23.024Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3523.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T20:37:01.562Z\"}, \"mvp_sim_confounding\": {\"completed_at\": \"2026-05-13T16:28:42.378Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T04:39:19.345Z\", \"hypothesis\": \"4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure\", \"metrics\": {\"actual_confound_corr\": 0.3814, \"divergent_pct\": 0, \"fit_time_sec\": 832, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.5386, \"gamma_rel_bias\": 0.0771, \"max_rhat\": 1.007, \"min_ess\": 1371.9, \"overall\": \"PASS\", \"theta_corr\": 0.9733, \"theta_residual_exp_corr\": 0.0582, \"theta_rmse\": 0.2407}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"artifacts/mvp_simulation/p2_confounding_results.json\", \"command\": \"python run_p2_confounding.py\", \"data_count\": \"50 models x 300 items = 15000 responses\", \"data_path\": \"synthetic confounded (corr≈0.38)\", \"log_path\": \"/tmp/p2_confounding.log\", \"model_name\": \"4PL+γ IRT (Stan NUTS)\", \"note\": \"N_items=300 (matching Variant A PASS config), 4PL NUTS only, 4 chains 1000+1000, θ-exposure corr=0.381\", \"pid\": 202872, \"seed\": 123, \"server\": \"local-cpu\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T16:28:42.378Z\"}, \"mvp_sim_4pl_gamma\": {\"completed_at\": \"2026-05-13T10:59:01.402Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T04:27:47.251Z\", \"hypothesis\": \"4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\", \"metrics\": {\"variant_a_nitems300\": {\"divergent_pct\": 0, \"fit_time_sec\": 1407.5, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.466, \"gamma_rel_bias\": 0.068, \"max_rhat\": 1.003, \"overall\": \"PASS\", \"theta_corr\": 0.943, \"theta_rmse\": 0.238}}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"artifacts/mvp_simulation/p1_variant_results.json\", \"command\": \"python run_p1_base.py\", \"data_count\": \"50 models x 100 items = 5000 responses\", \"data_path\": \"synthetic (generated in-script)\", \"log_path\": \"/tmp/p1_variants.log\", \"model_name\": \"2PL+γ / 4PL+γ IRT (Stan)\", \"note\": \"Order: 2PL ADVI → 2PL NUTS → 4PL ADVI → 4PL NUTS\", \"pid\": 197929, \"seed\": 42, \"server\": \"local-cpu\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T10:59:01.402Z\"}}, \"count\": 143, \"total\": 143, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.3789}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T18:25:34.764Z_

<details><summary>↩ Tool result · `toolu_01DdUcjvJwS53grc2NgPwBWh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/eval_results/\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_para\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_raw\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v3\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s42_aligned_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_v1_s42_aligned_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v1_s42_aligned_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s123_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_v2\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v3_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.59}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "57e1388d-6edb-4aa3-9128-080006e77a1b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/exp001/eval_results/\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_para\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_raw\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v3\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s42_aligned_DEPRECATED\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_v1_s42_aligned_DEPRECATED\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v1_s42_aligned_DEPRECATED\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s123_DEPRECATED\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_v2\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v3_s42_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_para_aligned\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.59}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/eval_results/\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_para\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_raw\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v3\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s42_aligned_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_v1_s42_aligned_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v1_s42_aligned_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s123_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_v2\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v3_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.59}}"
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
The registry result is too large and was saved to a file. Let me process it with a subagent to extract the eval metrics. Meanwhile, I have the directory listing of eval results.

Let me parse the directory listing:

Directories (non-DEPRECATED, non-raw, non-Instruct, non-base_pretrained):
- 0.5B: d000_s42, d000_s123, d005_s42, d025_s42, d100_s42, d005_s123, d025_s123, d100_s123
  - aligned variants: d000_s42_aligned, d000_s123_aligned (wait, I don't see d000_s123_aligned for 0.5B... let me recheck)
  
Now I'm organizing the full directory structure for the 0.5B models with their seed variants and aligned versions, though I'm noticing some inconsistencies in which aligned variants actually exist in the listing. I'm getting bogged down in manual checking, so let me use a subagent to handle the heavy lifting—parsing the registry file and pulling all the results.json contents via SSH at once. Actually, a better approach would be to run a Python script directly on the server to collect all the evaluation metrics in one go, then have the subagent parse the registry separately. First, I need to understand what the results.json files actually contain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "a25a42a9-e10d-4afb-9ebb-95ecd4ea412a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQxn5fjEh6G8Xk59UKVhWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3343,
      "cache_read_input_tokens": 25827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3343
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

Registry output is large. Let me parse it and collect eval metrics from the server in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "4716e4fa-127b-4a3e-bcbd-e9c3ceb50153",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQxn5fjEh6G8Xk59UKVhWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3343,
      "cache_read_input_tokens": 25827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3343
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

<details open><summary>🔧 Tool call — Agent · `toolu_018wEkk7FPBn48KLc7Yhsns8`</summary>

```json
{
  "description": "Parse registry for eval metrics",
  "prompt": "Parse the large registry JSON file at `/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt` to extract eval experiment info.\n\nThe file is JSON with schema: {result: string} where result is itself a JSON string.\n\nSteps:\n1. Use `jq` to probe the structure\n2. Extract all experiments that have:\n   - type containing \"eval\" or task containing \"eval\"\n   - status = \"DONE\"\n3. For each eval experiment, extract: exp_id, name/description, metrics (if any), any fields about scale/dose/seed/benchmark\n\nReturn a structured summary of ALL eval experiments found, their metrics (if present), and any identifying info (scale, dose, seed, eval_type like aligned/para_aligned). Be thorough - I need every single eval experiment.\n\nThe project is contamcal-irt-calibration, studying LLM benchmark contamination calibration. Scales: 0.5B, 1.5B, 3B. Doses: 0%, 5%, 25%, 100%. Seeds: 42, 123. Benchmarks: MMLU, GSM8K, ARC-Challenge, HumanEval.",
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
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "c9bf0c2c-3ff5-4c2c-92db-ff08a6150605",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQxn5fjEh6G8Xk59UKVhWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3343,
      "cache_read_input_tokens": 25827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3343
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

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "aee0c4a84f025f3bb",
  "tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "description": "Parse registry for eval metrics",
  "task_type": "local_agent",
  "prompt": "Parse the large registry JSON file at `/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt` to extract eval experiment info.\n\nThe file is JSON with schema: {result: string} where result is itself a JSON string.\n\nSteps:\n1. Use `jq` to probe the structure\n2. Extract all experiments that have:\n   - type containing \"eval\" or task containing \"eval\"\n   - status = \"DONE\"\n3. For each eval experiment, extract: exp_id, name/description, metrics (if any), any fields about scale/dose/seed/benchmark\n\nReturn a structured summary of ALL eval experiments found, their metrics (if present), and any identifying info (scale, dose, seed, eval_type like aligned/para_aligned). Be thorough - I need every single eval experiment.\n\nThe project is contamcal-irt-calibration, studying LLM benchmark contamination calibration. Scales: 0.5B, 1.5B, 3B. Doses: 0%, 5%, 25%, 100%. Seeds: 42, 123. Benchmarks: MMLU, GSM8K, ARC-Challenge, HumanEval.",
  "uuid": "bba0d59d-544d-4c16-b085-a71a75b14639",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af"
}
```

---

## Round 1

113 recorded events

### User

_source line 17 · 2026-05-15T18:25:56.769Z_

Parse the large registry JSON file at `/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt` to extract eval experiment info.

The file is JSON with schema: {result: string} where result is itself a JSON string.

Steps:
1. Use `jq` to probe the structure
2. Extract all experiments that have:
   - type containing "eval" or task containing "eval"
   - status = "DONE"
3. For each eval experiment, extract: exp_id, name/description, metrics (if any), any fields about scale/dose/seed/benchmark

Return a structured summary of ALL eval experiments found, their metrics (if present), and any identifying info (scale, dose, seed, eval_type like aligned/para_aligned). Be thorough - I need every single eval experiment.

The project is contamcal-irt-calibration, studying LLM benchmark contamination calibration. Scales: 0.5B, 1.5B, 3B. Doses: 0%, 5%, 25%, 100%. Seeds: 42, 123. Benchmarks: MMLU, GSM8K, ARC-Challenge, HumanEval.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "29edd3bd-22bb-4e61-90d6-d37ff7a98c2b"
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EaB5R2mMNWpxgDjczaqN8K`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/ -name \"results.json\" -path \"*/aligned*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "519b001a-dc6b-4e2e-88a4-852a31ffe6a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQxn5fjEh6G8Xk59UKVhWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3343,
      "cache_read_input_tokens": 25827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3343
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

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aee0c4a84f025f3bb",
  "tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 14518,
    "tool_uses": 1,
    "duration_ms": 5083
  },
  "last_tool_name": "Bash",
  "uuid": "5f2b1efd-d662-4033-a108-6ebe0af2471a",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01MwWq5U7WZcduzFZhWmr1bD`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "6016bb7d-057c-4f60-80bc-5318b29d0a8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BK2KCfSqhE2te1g9pcVEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14507,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14507,
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

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aee0c4a84f025f3bb",
  "tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "description": "Running Peek at file start",
  "usage": {
    "total_tokens": 14522,
    "tool_uses": 2,
    "duration_ms": 6180
  },
  "last_tool_name": "Bash",
  "uuid": "00b61216-7097-4a15-980f-8ce629bdae87",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01Eb6j1XUR7F3TU6EcdZbDi6`</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt",
  "description": "Peek at file start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "da190303-2d0d-48eb-8ce8-87e265037495",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BK2KCfSqhE2te1g9pcVEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14507,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14507,
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

_source line 23 · 2026-05-15T18:26:03.264Z_

<details><summary>↩ Tool result · `toolu_01MwWq5U7WZcduzFZhWmr1bD`</summary>

```text
236095 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "14f060ea-9786-4109-94db-0f130ab63212"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T18:26:03.472Z_

<details><summary>↩ Tool result · `toolu_01Eb6j1XUR7F3TU6EcdZbDi6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_3B_d025_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:16.431Z\", \"updated_at\": \"2026-05-15T18:10:03.567Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T14:51:29.435Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T18:07:00.568Z\", \"training_hours\": 3.26}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 576730, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d025_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "2856882d-274e-43bc-9cb0-7e1e173e3746"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aee0c4a84f025f3bb",
  "tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "description": "Running Count eval experiments",
  "usage": {
    "total_tokens": 16714,
    "tool_uses": 3,
    "duration_ms": 12441
  },
  "last_tool_name": "Bash",
  "uuid": "4cb4e2b0-c288-4c6c-a056-0653a443893d",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01R455ACcqwWqvM5fGjCznWL`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt\"\ncat \"$FILE\" | jq -r '.result' | jq '.data.experiments | keys[]' | grep -i eval | wc -l",
  "description": "Count eval experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "4b664826-27e8-4f9d-bd44-2506dadb1824",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfArX89zH3FV3U9Kwds2aL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2192,
      "cache_read_input_tokens": 14507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2192,
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

_source line 27 · 2026-05-15T18:26:09.904Z_

<details><summary>↩ Tool result · `toolu_01R455ACcqwWqvM5fGjCznWL`</summary>

```text
69
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "1d4351c5-6419-4594-a121-76f7a537cfef"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aee0c4a84f025f3bb",
  "tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "description": "Running List all eval experiment keys",
  "usage": {
    "total_tokens": 16715,
    "tool_uses": 4,
    "duration_ms": 13502
  },
  "last_tool_name": "Bash",
  "uuid": "b0126659-5a67-4b27-8e5c-cb7a778e2e99",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_015wEXWHc3q2xUBF6yCvaBte`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt\"\ncat \"$FILE\" | jq -r '.result' | jq '.data.experiments | keys[]' | grep -i eval",
  "description": "List all eval experiment keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "62a54fcc-ed2f-45ec-a84b-7ceb98ac8c3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfArX89zH3FV3U9Kwds2aL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2192,
      "cache_read_input_tokens": 14507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2192,
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

_source line 30 · 2026-05-15T18:26:10.767Z_

<details><summary>↩ Tool result · `toolu_015wEXWHc3q2xUBF6yCvaBte`</summary>

```text
"exp_001_eval_05B_aligned_batch"
"exp_001_eval_05B_d000_s123"
"exp_001_eval_05B_d000_s123_aligned"
"exp_001_eval_05B_d000_s42"
"exp_001_eval_05B_d000_s42_v5"
"exp_001_eval_05B_d000_s42_v7"
"exp_001_eval_05B_d005"
"exp_001_eval_05B_d005_aligned"
"exp_001_eval_05B_d005_para_aligned"
"exp_001_eval_05B_d005_s123_aligned"
"exp_001_eval_05B_d005_s123_para_aligned"
"exp_001_eval_05B_d025_aligned"
"exp_001_eval_05B_d025_aligned_v2"
"exp_001_eval_05B_d025_s123_aligned"
"exp_001_eval_05B_d100"
"exp_001_eval_05B_d100_aligned"
"exp_001_eval_05B_d100_aligned_v3"
"exp_001_eval_05B_d100_aligned_v4"
"exp_001_eval_05B_d100_s123_aligned"
"exp_001_eval_05B_d100_v2"
"exp_001_eval_05B_d100_v5"
"exp_001_eval_05B_raw"
"exp_001_eval_15B_aligned_batch"
"exp_001_eval_15B_d000_s123"
"exp_001_eval_15B_d000_s123_aligned"
"exp_001_eval_15B_d000_s42"
"exp_001_eval_15B_d000_s42_v2"
"exp_001_eval_15B_d005_aligned_v2"
"exp_001_eval_15B_d005_s123"
"exp_001_eval_15B_d005_s123_v2"
"exp_001_eval_15B_d025_aligned"
"exp_001_eval_15B_d025_para_aligned"
"exp_001_eval_15B_d025_s123"
"exp_001_eval_15B_d025_s123_v2"
"exp_001_eval_15B_d100_aligned"
"exp_001_eval_15B_d100_s123_aligned"
"exp_001_eval_15B_d100_s42"
"exp_001_eval_3B_d000_aligned"
"exp_001_eval_3B_d000_s123"
"exp_001_eval_3B_d000_s123_aligned"
"exp_001_eval_3B_d000_s42"
"exp_001_eval_3B_d000_s42_para_aligned"
"exp_001_eval_3B_d000_s42_v3"
"exp_001_eval_3B_d000_v2_aligned"
"exp_001_eval_3B_d000_v2_para_aligned"
"exp_001_eval_3B_d000_v2_para_aligned_v2"
"exp_001_eval_3B_d000_v2_para_aligned_v3"
"exp_001_eval_3B_d000_v2_s123_aligned"
"exp_001_eval_3B_d000_v2_s123_para_aligned"
"exp_001_eval_3B_d005_aligned"
"exp_001_eval_3B_d005_s123_para_aligned"
"exp_001_eval_3B_d005_s42_aligned"
"exp_001_eval_3B_d025_s123_aligned"
"exp_001_eval_3B_d025_s123_para_aligned"
"exp_001_eval_3B_d025_v2_aligned"
"exp_001_eval_3B_d025_v2_para_aligned"
"exp_001_eval_3B_d100_aligned"
"exp_001_eval_3B_d100_para_aligned"
"exp_001_eval_3B_d100_s42_para_aligned"
"exp_001_eval_3B_d100_v2_aligned"
"exp_001_eval_3B_d100_v2_aligned_v2"
"exp_001_eval_3B_d100_v2_para_aligned"
"exp_001_eval_3B_d100_v2_s123_aligned"
"exp_001_eval_3B_raw_gen"
"exp_008_base_pretrained_15B_eval"
"exp_008_base_pretrained_15B_eval_v2"
"exp_008_base_pretrained_eval"
"exp_008_base_pretrained_eval_v2"
"exp_008_instruct_05B_eval"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "6744757a-68f1-410e-b25a-03a2fb972c4a"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aee0c4a84f025f3bb",
  "tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "description": "Running Extract eval experiment details with metrics",
  "usage": {
    "total_tokens": 18437,
    "tool_uses": 5,
    "duration_ms": 20821
  },
  "last_tool_name": "Bash",
  "uuid": "9ba231a4-b40d-4319-8143-3c2303d5eafd",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_014wqUwTanz67rto2CGXQoXA`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt\"\ncat \"$FILE\" | jq -r '.result' | jq '\n  .data.experiments | to_entries[] \n  | select(.key | test(\"eval\"; \"i\")) \n  | {\n      exp_id: .key,\n      status: .value.status,\n      metrics: .value.metrics,\n      seed: .value.reproduce.spec.seed // .value.spec.seed // null,\n      model_name: .value.reproduce.spec.model_name // .value.spec.model_name // null,\n      eval_data: .value.reproduce.spec.eval_data // .value.spec.eval_data // null,\n      checkpoint_source: .value.reproduce.spec.checkpoint_source // .value.spec.checkpoint_source // null,\n      data_count: .value.reproduce.spec.data_count // .value.spec.data_count // null\n    }\n' 2>/dev/null | head -3000",
  "description": "Extract eval experiment details with metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "07ec43a8-d296-4ff6-9b37-c2a958f85656",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ac1fyZpebjraf1UqMpLV3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1720,
      "cache_read_input_tokens": 16699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1720,
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

_source line 33 · 2026-05-15T18:26:18.345Z_

<details><summary>↩ Tool result · `toolu_014wqUwTanz67rto2CGXQoXA`</summary>

```text
&lt;persisted-output>
Output too large (29.6KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/bp43hjy06.txt

Preview (first 2KB):
{
  "exp_id": "exp_001_eval_3B_d025_s123_aligned",
  "status": "DONE",
  "metrics": {
    "mmlu": 0.6367,
    "gsm8k": 0.5254,
    "arc_challenge": 0.8336,
    "humaneval": 0.1585
  },
  "seed": 123,
  "model_name": "Qwen2.5-3B",
  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
  "checkpoint_source": "exp_001_sft_3B_d025_s123",
  "data_count": 4
}
{
  "exp_id": "exp_001_eval_3B_d005_s123_para_aligned",
  "status": "DONE",
  "metrics": {
    "MMLU": 0.6461,
    "GSM8K": 0.5,
    "ARC": 0.8192,
    "HumanEval": 0.0769
  },
  "seed": 123,
  "model_name": "Qwen2.5-3B",
  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter",
  "data_count": 4
}
{
  "exp_id": "exp_001_eval_3B_d025_s123_para_aligned",
  "status": "DONE",
  "metrics": {
    "MMLU": 0.6615,
    "GSM8K": 0.4254,
    "ARC": 0.8121,
    "HumanEval": 0.1538
  },
  "seed": 123,
  "model_name": "Qwen2.5-3B",
  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter",
  "data_count": 4
}
{
  "exp_id": "exp_001_eval_15B_d005_s123",
  "status": "DONE",
  "metrics": {
    "mmlu": {
      "accuracy": 0.5869,
      "correct": 8241,
      "total": 14042
    },
    "gsm8k": {
      "exact_match": 0.6482,
      "correct": 855,
      "total": 1319
    },
    "arc_challenge": {
      "accuracy": 0.7568,
      "correct": 887,
      "total": 1172
    },
    "humaneval": {
      "pass@1": 0.25,
      "correct": 41,
      "total": 164
    }
  },
  "seed": null,
  "model_name": null,
  "eval_data": null,
  "checkpoint_source": null,
  "data_count": null
}
{
  "exp_id": "exp_001_eval_15B_d005_s123_v2",
  "status": "DONE",
  "metrics": {
    "mmlu": {
      "accuracy": 0.5869,
      "correct": 8241,
      "total": 14042
    },
    "gsm8k": {
      "exact_match": 0.6482,
      "correct": 855,
      "total": 1319
    },
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "52dc5666-c899-405f-b249-a3616d38d5ea"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aee0c4a84f025f3bb",
  "tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/bp43hjy06.txt",
  "usage": {
    "total_tokens": 19947,
    "tool_uses": 6,
    "duration_ms": 25712
  },
  "last_tool_name": "Read",
  "uuid": "c5c87218-74e2-4256-9138-d29d3119c74b",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01HjwKy1uAM6rmxGXtPs4aFg`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/bp43hjy06.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "71e0d96c-51bc-4d9d-b995-ae0c3c0bdf34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3bV7qNX4fDjcJDDxqRrnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1496,
      "cache_read_input_tokens": 18419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1496,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T18:26:22.925Z_

<details><summary>↩ Tool result · `toolu_01HjwKy1uAM6rmxGXtPs4aFg`</summary>

```text
1	{
2	  "exp_id": "exp_001_eval_3B_d025_s123_aligned",
3	  "status": "DONE",
4	  "metrics": {
5	    "mmlu": 0.6367,
6	    "gsm8k": 0.5254,
7	    "arc_challenge": 0.8336,
8	    "humaneval": 0.1585
9	  },
10	  "seed": 123,
11	  "model_name": "Qwen2.5-3B",
12	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
13	  "checkpoint_source": "exp_001_sft_3B_d025_s123",
14	  "data_count": 4
15	}
16	{
17	  "exp_id": "exp_001_eval_3B_d005_s123_para_aligned",
18	  "status": "DONE",
19	  "metrics": {
20	    "MMLU": 0.6461,
21	    "GSM8K": 0.5,
22	    "ARC": 0.8192,
23	    "HumanEval": 0.0769
24	  },
25	  "seed": 123,
26	  "model_name": "Qwen2.5-3B",
27	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
28	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter",
29	  "data_count": 4
30	}
31	{
32	  "exp_id": "exp_001_eval_3B_d025_s123_para_aligned",
33	  "status": "DONE",
34	  "metrics": {
35	    "MMLU": 0.6615,
36	    "GSM8K": 0.4254,
37	    "ARC": 0.8121,
38	    "HumanEval": 0.1538
39	  },
40	  "seed": 123,
41	  "model_name": "Qwen2.5-3B",
42	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
43	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter",
44	  "data_count": 4
45	}
46	{
47	  "exp_id": "exp_001_eval_15B_d005_s123",
48	  "status": "DONE",
49	  "metrics": {
50	    "mmlu": {
51	      "accuracy": 0.5869,
52	      "correct": 8241,
53	      "total": 14042
54	    },
55	    "gsm8k": {
56	      "exact_match": 0.6482,
57	      "correct": 855,
58	      "total": 1319
59	    },
60	    "arc_challenge": {
61	      "accuracy": 0.7568,
62	      "correct": 887,
63	      "total": 1172
64	    },
65	    "humaneval": {
66	      "pass@1": 0.25,
67	      "correct": 41,
68	      "total": 164
69	    }
70	  },
71	  "seed": null,
72	  "model_name": null,
73	  "eval_data": null,
74	  "checkpoint_source": null,
75	  "data_count": null
76	}
77	{
78	  "exp_id": "exp_001_eval_15B_d005_s123_v2",
79	  "status": "DONE",
80	  "metrics": {
81	    "mmlu": {
82	      "accuracy": 0.5869,
83	      "correct": 8241,
84	      "total": 14042
85	    },
86	    "gsm8k": {
87	      "exact_match": 0.6482,
88	      "correct": 855,
89	      "total": 1319
90	    },
91	    "arc_challenge": {
92	      "accuracy": 0.7568,
93	      "correct": 887,
94	      "total": 1172
95	    },
96	    "humaneval": {
97	      "pass@1": 0.25,
98	      "correct": 41,
99	      "total": 164
100	    }
101	  },
102	  "seed": 123,
103	  "model_name": "Qwen2.5-1.5B",
104	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
105	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter",
106	  "data_count": 0
107	}
108	{
109	  "exp_id": "exp_001_eval_15B_d025_s123",
110	  "status": "DONE",
111	  "metrics": {
112	    "mmlu": {
113	      "accuracy": 0.5881,
114	      "correct": 8258,
115	      "total": 14042
116	    },
117	    "gsm8k": {
118	      "exact_match": 0.655,
119	      "correct": 864,
120	      "total": 1319
121	    },
122	    "arc_challenge": {
123	      "accuracy": 0.7577,
124	      "correct": 888,
125	      "total": 1172
126	    },
127	    "humaneval": {
128	      "pass@1": 0.25,
129	      "correct": 41,
130	      "total": 164
131	    }
132	  },
133	  "seed": null,
134	  "model_name": null,
135	  "eval_data": null,
136	  "checkpoint_source": null,
137	  "data_count": null
138	}
139	{
140	  "exp_id": "exp_001_eval_15B_d025_s123_v2",
141	  "status": "DONE",
142	  "metrics": {
143	    "mmlu": {
144	      "accuracy": 0.5881,
145	      "correct": 8258,
146	      "total": 14042
147	    },
148	    "gsm8k": {
149	      "exact_match": 0.655,
150	      "correct": 864,
151	      "total": 1319
152	    },
153	    "arc_challenge": {
154	      "accuracy": 0.7577,
155	      "correct": 888,
156	      "total": 1172
157	    },
158	    "humaneval": {
159	      "pass@1": 0.25,
160	      "correct": 41,
161	      "total": 164
162	    }
163	  },
164	  "seed": 123,
165	  "model_name": "Qwen2.5-1.5B",
166	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
167	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter",
168	  "data_count": 0
169	}
170	{
171	  "exp_id": "exp_001_eval_3B_d000_s42_para_aligned",
172	  "status": "DONE",
173	  "metrics": {
174	    "mmlu": {
175	      "accuracy": 0.6474,
176	      "correct": 4270,
177	      "total": 6596
178	    },
179	    "gsm8k": {
180	      "accuracy": 0.0482,
181	      "correct": 11,
182	      "total": 228
183	    },
184	    "arc_challenge": {
185	      "accuracy": 0.8235,
186	      "correct": 574,
187	      "total": 697
188	    },
189	    "humaneval": {
190	      "pass@1": 0.1154,
191	      "correct": 3,
192	      "total": 26
193	    }
194	  },
195	  "seed": 42,
196	  "model_name": "Qwen2.5-3B",
197	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
198	  "checkpoint_source": "exp_001_sft_3B_d000_s42",
199	  "data_count": 4
200	}
201	{
202	  "exp_id": "exp_001_eval_3B_d100_s42_para_aligned",
203	  "status": "DONE",
204	  "metrics": {
205	    "mmlu": {
206	      "accuracy": 0.659,
207	      "correct": 4347,
208	      "total": 6596
209	    },
210	    "gsm8k": {
211	      "accuracy": 0.5833,
212	      "correct": 133,
213	      "total": 228
214	    },
215	    "arc_challenge": {
216	      "accuracy": 0.8092,
217	      "correct": 564,
218	      "total": 697
219	    },
220	    "humaneval": {
221	      "pass@1": 0.1154,
222	      "correct": 3,
223	      "total": 26
224	    }
225	  },
226	  "seed": 42,
227	  "model_name": "Qwen2.5-3B",
228	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
229	  "checkpoint_source": "exp_001_sft_d100_3B_v2",
230	  "data_count": 4
231	}
232	{
233	  "exp_id": "exp_001_eval_3B_d000_s123_aligned",
234	  "status": "DONE",
235	  "metrics": {
236	    "mmlu": 0.6332,
237	    "gsm8k": 0.1812,
238	    "arc_challenge": 0.8328,
239	    "humaneval": 0.0854
240	  },
241	  "seed": 123,
242	  "model_name": "Qwen/Qwen2.5-3B",
243	  "eval_data": "mmlu gsm8k arc_challenge humaneval",
244	  "checkpoint_source": "exp_001_sft_3B_d000_s123",
245	  "data_count": 0
246	}
247	{
248	  "exp_id": "exp_001_eval_3B_d005_s42_aligned",
249	  "status": "DONE",
250	  "metrics": {
251	    "mmlu": 0.6345,
252	    "gsm8k": 0.2077,
253	    "arc_challenge": 0.8294,
254	    "humaneval": 0.1463
255	  },
256	  "seed": 42,
257	  "model_name": "Qwen/Qwen2.5-3B",
258	  "eval_data": "mmlu gsm8k arc_challenge humaneval",
259	  "checkpoint_source": "exp_001_sft_3B_d005_s42",
260	  "data_count": 0
261	}
262	{
263	  "exp_id": "exp_008_base_pretrained_eval_v2",
264	  "status": "DONE",
265	  "metrics": {
266	    "mmlu": 0.2294,
267	    "gsm8k": 0.163,
268	    "arc_challenge": 0.2278,
269	    "humaneval": 0
270	  },
271	  "seed": 42,
272	  "model_name": "Qwen2.5-0.5B",
273	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
274	  "checkpoint_source": null,
275	  "data_count": 0
276	}
277	{
278	  "exp_id": "exp_008_base_pretrained_15B_eval_v2",
279	  "status": "DONE",
280	  "metrics": {
281	    "mmlu": 0.2303,
282	    "gsm8k": 0.0053,
283	    "arc_challenge": 0.2304,
284	    "humaneval_pass1": 0.2317,
285	    "mmlu_correct": 3234,
286	    "mmlu_total": 14042,
287	    "gsm8k_correct": 7,
288	    "gsm8k_total": 1319,
289	    "arc_correct": 270,
290	    "arc_total": 1172,
291	    "humaneval_correct": 38,
292	    "humaneval_total": 164
293	  },
294	  "seed": 42,
295	  "model_name": "Qwen2.5-1.5B",
296	  "eval_data": null,
297	  "checkpoint_source": null,
298	  "data_count": 0
299	}
300	{
301	  "exp_id": "exp_008_base_pretrained_15B_eval",
302	  "status": "DONE",
303	  "metrics": {
304	    "mmlu_accuracy": 0.2303,
305	    "gsm8k_accuracy": 0.0053,
306	    "arc_challenge_accuracy": 0.2304,
307	    "humaneval_pass@1": 0.2317,
308	    "mmlu_correct": 3234,
309	    "mmlu_total": 14042,
310	    "gsm8k_correct": 7,
311	    "gsm8k_total": 1319,
312	    "arc_correct": 270,
313	    "arc_total": 1172,
314	    "humaneval_correct": 38,
315	    "humaneval_total": 164
316	  },
317	  "seed": null,
318	  "model_name": "Qwen2.5-1.5B",
319	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
320	  "checkpoint_source": null,
321	  "data_count": null
322	}
323	{
324	  "exp_id": "exp_008_base_pretrained_eval",
325	  "status": "DONE",
326	  "metrics": null,
327	  "seed": null,
328	  "model_name": "Qwen2.5-0.5B",
329	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
330	  "checkpoint_source": null,
331	  "data_count": null
332	}
333	{
334	  "exp_id": "exp_001_eval_15B_d000_s123_aligned",
335	  "status": "DONE",
336	  "metrics": {
337	    "mmlu_accuracy": 0.5855,
338	    "gsm8k_accuracy": 0.6535,
339	    "arc_challenge_accuracy": 0.7577,
340	    "humaneval_pass@1": 0.1707
341	  },
342	  "seed": null,
343	  "model_name": null,
344	  "eval_data": null,
345	  "checkpoint_source": null,
346	  "data_count": null
347	}
348	{
349	  "exp_id": "exp_001_eval_15B_d100_s123_aligned",
350	  "status": "DONE",
351	  "metrics": {
352	    "mmlu_accuracy": 0.5956,
353	    "gsm8k_accuracy": 0.6444,
354	    "arc_challenge_accuracy": 0.7816,
355	    "humaneval_pass@1": 0.2805
356	  },
357	  "seed": null,
358	  "model_name": null,
359	  "eval_data": null,
360	  "checkpoint_source": null,
361	  "data_count": null
362	}
363	{
364	  "exp_id": "exp_001_eval_05B_d000_s123_aligned",
365	  "status": "DONE",
366	  "metrics": {
367	    "mmlu": 0.4216,
368	    "gsm8k": 0.3412,
369	    "arc_challenge": 0.4974,
370	    "humaneval": 0.1037
371	  },
372	  "seed": null,
373	  "model_name": null,
374	  "eval_data": null,
375	  "checkpoint_source": null,
376	  "data_count": null
377	}
378	{
379	  "exp_id": "exp_001_eval_3B_d000_s42_v3",
380	  "status": "DONE",
381	  "metrics": {
382	    "mmlu": 0.634,
383	    "gsm8k": 0.1198,
384	    "arc_challenge": 0.8276,
385	    "humaneval": 0.1159
386	  },
387	  "seed": 42,
388	  "model_name": "Qwen2.5-3B",
389	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
390	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter",
391	  "data_count": 4
392	}
393	{
394	  "exp_id": "exp_001_eval_3B_d000_v2_s123_aligned",
395	  "status": "DONE",
396	  "metrics": {
397	    "mmlu": 0.6314,
398	    "gsm8k": 0.2676,
399	    "arc_challenge": 0.8259,
400	    "humaneval": 0.061
401	  },
402	  "seed": 123,
403	  "model_name": "Qwen2.5-3B",
404	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
405	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter",
406	  "data_count": 4
407	}
408	{
409	  "exp_id": "exp_001_eval_3B_d025_v2_aligned",
410	  "status": "DONE",
411	  "metrics": {
412	    "mmlu": 0.5998,
413	    "gsm8k": 0.6793,
414	    "arc_challenge": 0.8276,
415	    "humaneval": 0.0976
416	  },
417	  "seed": 42,
418	  "model_name": "Qwen2.5-3B",
419	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
420	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter",
421	  "data_count": 4
422	}
423	{
424	  "exp_id": "exp_001_eval_3B_d100_v2_s123_aligned",
425	  "status": "DONE",
426	  "metrics": {
427	    "mmlu": 0.6319,
428	    "gsm8k": 0.7324,
429	    "arc_challenge": 0.8311,
430	    "humaneval": 0.1829
431	  },
432	  "seed": 123,
433	  "model_name": "Qwen2.5-3B",
434	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
435	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter",
436	  "data_count": 4
437	}
438	{
439	  "exp_id": "exp_001_eval_05B_d025_s123_aligned",
440	  "status": "DONE",
441	  "metrics": {
442	    "mmlu": {
443	      "accuracy": 0.3473,
444	      "correct": 4877,
445	      "total": 14042
446	    },
447	    "gsm8k": {
448	      "accuracy": 0.3533,
449	      "correct": 466,
450	      "total": 1319
451	    },
452	    "arc_challenge": {
453	      "accuracy": 0.4061,
454	      "correct": 476,
455	      "total": 1172
456	    },
457	    "humaneval": {
458	      "pass@1": 0.0854,
459	      "correct": 14,
460	      "total": 164
461	    }
462	  },
463	  "seed": null,
464	  "model_name": null,
465	  "eval_data": null,
466	  "checkpoint_source": null,
467	  "data_count": null
468	}
469	{
470	  "exp_id": "exp_001_eval_05B_d000_s42_v7",
471	  "status": "DONE",
472	  "metrics": null,
473	  "seed": 42,
474	  "model_name": "Qwen2.5-0.5B",
475	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
476	  "checkpoint_source": "exp_001_sft_0pct_05B",
477	  "data_count": 4
478	}
479	{
480	  "exp_id": "exp_008_instruct_05B_eval",
481	  "status": "DONE",
482	  "metrics": {
483	    "mmlu_accuracy": 0.2462,
484	    "gsm8k_accuracy": 0.3882,
485	    "arc_challenge_accuracy": 0.2816,
486	    "humaneval_pass@1": 0
487	  },
488	  "seed": 42,
489	  "model_name": "Qwen2.5-0.5B-Instruct",
490	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
491	  "checkpoint_source": "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct",
492	  "data_count": 0
493	}
494	{
495	  "exp_id": "exp_001_eval_3B_d100_v2_aligned_v2",
496	  "status": "DONE",
497	  "metrics": {
498	    "mmlu_accuracy": 0.632,
499	    "gsm8k_accuracy": 0.7415,
500	    "arc_challenge_accuracy": 0.8242,
501	    "humaneval_pass@1": 0.1707
502	  },
503	  "seed": 42,
504	  "model_name": "Qwen2.5-3B",
505	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
506	  "checkpoint_source": "exp_001_sft_d100_3B_v2",
507	  "data_count": 0
508	}
509	{
510	  "exp_id": "exp_001_eval_3B_d025_v2_para_aligned",
511	  "status": "DONE",
512	  "metrics": {
513	    "mmlu_para_accuracy": 0.621,
514	    "gsm8k_para_accuracy": 0.5482,
515	    "arc_challenge_para_accuracy": 0.8106,
516	    "humaneval_para_pass@1": 0.1154
517	  },
518	  "seed": 42,
519	  "model_name": "Qwen2.5-3B (d025 v2 LoRA)",
520	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
521	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter",
522	  "data_count": 0
523	}
524	{
525	  "exp_id": "exp_001_eval_3B_d000_v2_s123_para_aligned",
526	  "status": "DONE",
527	  "metrics": {
528	    "mmlu_para_accuracy": 0.6512,
529	    "gsm8k_para_accuracy": 0.1491,
530	    "arc_challenge_para_accuracy": 0.8121,
531	    "humaneval_para_pass@1": 0.0385
532	  },
533	  "seed": 123,
534	  "model_name": "Qwen2.5-3B",
535	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
536	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter",
537	  "data_count": 4
538	}
539	{
540	  "exp_id": "exp_001_eval_05B_d005_s123_para_aligned",
541	  "status": "DONE",
542	  "metrics": {
543	    "mmlu_para_accuracy": 0.3166,
544	    "gsm8k_para_accuracy": 0.2939,
545	    "arc_challenge_para_accuracy": 0.2912,
546	    "humaneval_para_pass@1": 0
547	  },
548	  "seed": 123,
549	  "model_name": "Qwen2.5-0.5B",
550	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
551	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter",
552	  "data_count": 0
553	}
554	{
555	  "exp_id": "exp_001_eval_05B_d000_s42",
556	  "status": "DONE",
557	  "metrics": null,
558	  "seed": 42,
559	  "model_name": "Qwen2.5-0.5B",
560	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
561	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter",
562	  "data_count": 0
563	}
564	{
565	  "exp_id": "exp_001_eval_05B_d005_s123_aligned",
566	  "status": "DONE",
567	  "metrics": {
568	    "mmlu_accuracy": 0.3002,
569	    "gsm8k_accuracy": 0.3677,
570	    "arc_challenge_accuracy": 0.2978,
571	    "humaneval_pass@1": 0.0976
572	  },
573	  "seed": 123,
574	  "model_name": "Qwen2.5-0.5B",
575	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
576	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter",
577	  "data_count": 4
578	}
579	{
580	  "exp_id": "exp_001_eval_3B_d000_v2_para_aligned_v3",
581	  "status": "DONE",
582	  "metrics": null,
583	  "seed": 42,
584	  "model_name": "Qwen2.5-3B",
585	  "eval_data": "mmlu gsm8k arc_challenge humaneval (para_aligned)",
586	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter",
587	  "data_count": 0
588	}
589	{
590	  "exp_id": "exp_001_eval_3B_d000_v2_para_aligned_v2",
591	  "status": "DONE",
592	  "metrics": {
593	    "mmlu_para_accuracy": 0.6468,
594	    "gsm8k_para_accuracy": 0.2895,
595	    "arc_challenge_para_accuracy": 0.8121,
596	    "humaneval_para_pass@1": 0.0385
597	  },
598	  "seed": 42,
599	  "model_name": "Qwen2.5-3B",
600	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (paraphrased, aligned format)",
601	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter",
602	  "data_count": null
603	}
604	{
605	  "exp_id": "exp_001_eval_3B_d100_v2_para_aligned",
606	  "status": "DONE",
607	  "metrics": {
608	    "mmlu_para": 0.659,
609	    "gsm8k_para": 0.5833,
610	    "arc_challenge_para": 0.8092,
611	    "humaneval_para_pass1": 0.1154
612	  },
613	  "seed": 42,
614	  "model_name": "Qwen2.5-3B",
615	  "eval_data": "mmlu gsm8k arc_challenge humaneval (paraphrased, mc-format=aligned)",
616	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter",
617	  "data_count": "4 benchmarks (paraphrased)"
618	}
619	{
620	  "exp_id": "exp_001_eval_3B_d000_v2_aligned",
621	  "status": "DONE",
622	  "metrics": {
623	    "mmlu": 0.6295,
624	    "gsm8k": 0.3525,
625	    "arc_challenge": 0.8183,
626	    "humaneval_pass@1": 0.0976
627	  },
628	  "seed": 42,
629	  "model_name": "Qwen2.5-3B",
630	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
631	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter",
632	  "data_count": 0
633	}
634	{
635	  "exp_id": "exp_001_eval_3B_d100_v2_aligned",
636	  "status": "DONE",
637	  "metrics": {
638	    "INVALID": "metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion."
639	  },
640	  "seed": 42,
641	  "model_name": "Qwen2.5-3B + d100_v2_s42 LoRA (alpha=16)",
642	  "eval_data": "mmlu gsm8k arc_challenge aligned",
643	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter",
644	  "data_count": 3
645	}
646	{
647	  "exp_id": "exp_001_eval_05B_d100_s123_aligned",
648	  "status": "DONE",
649	  "metrics": {
650	    "mmlu_accuracy": 0.3058,
651	    "gsm8k_accuracy": 0.3798,
652	    "arc_challenge_accuracy": 0.3669,
653	    "humaneval_pass_at_1": 0.1037,
654	    "mmlu_correct": 4294,
655	    "mmlu_total": 14042,
656	    "gsm8k_correct": 501,
657	    "gsm8k_total": 1319,
658	    "arc_challenge_correct": 430,
659	    "arc_challenge_total": 1172,
660	    "humaneval_total": 164
661	  },
662	  "seed": 123,
663	  "model_name": "Qwen2.5-0.5B",
664	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
665	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter",
666	  "data_count": 4
667	}
668	{
669	  "exp_id": "exp_001_eval_3B_d000_v2_para_aligned",
670	  "status": "DONE",
671	  "metrics": {
672	    "mmlu_para": 0.6468,
673	    "format": "paraphrased_aligned"
674	  },
675	  "seed": 42,
676	  "model_name": "Qwen2.5-3B + d000_v2_s42 LoRA",
677	  "eval_data": "mmlu gsm8k arc_challenge humaneval paraphrase",
678	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter",
679	  "data_count": 4
680	}
681	{
682	  "exp_id": "exp_001_eval_05B_d025_aligned_v2",
683	  "status": "DONE",
684	  "metrics": {
685	    "mmlu": 0.2835,
686	    "gsm8k": 0.3114,
687	    "arc_challenge": 0.3199,
688	    "humaneval_pass1": 0.1923,
689	    "format": "paraphrased_aligned"
690	  },
691	  "seed": 42,
692	  "model_name": "Qwen2.5-0.5B",
693	  "eval_data": "mmlu+gsm8k+arc_challenge+humaneval (paraphrased, aligned format)",
694	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter",
695	  "data_count": 4
696	}
697	{
698	  "exp_id": "exp_001_eval_15B_d025_aligned",
699	  "status": "DONE",
700	  "metrics": {
701	    "mmlu": 0.5902,
702	    "gsm8k": 0.6535,
703	    "arc_challenge": 0.7688,
704	    "humaneval_pass1": 0.2256
705	  },
706	  "seed": null,
707	  "model_name": null,
708	  "eval_data": null,
709	  "checkpoint_source": null,
710	  "data_count": null
711	}
712	{
713	  "exp_id": "exp_001_eval_05B_d005_para_aligned",
714	  "status": "DONE",
715	  "metrics": {
716	    "mmlu": 0.3548,
717	    "gsm8k": 0.2588,
718	    "arc_challenge": 0.33,
719	    "humaneval": 0,
720	    "mmlu_correct": 2340,
721	    "mmlu_total": 6596,
722	    "gsm8k_correct": 59,
723	    "gsm8k_total": 228,
724	    "arc_correct": 230,
725	    "arc_total": 697,
726	    "humaneval_correct": 0,
727	    "humaneval_total": 26
728	  },
729	  "seed": 42,
730	  "model_name": "Qwen2.5-0.5B",
731	  "eval_data": "mmlu gsm8k arc_challenge humaneval paraphrase",
732	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter",
733	  "data_count": 4
734	}
735	{
736	  "exp_id": "exp_001_eval_15B_d025_para_aligned",
737	  "status": "DONE",
738	  "metrics": {
739	    "mmlu": 0.618,
740	    "gsm8k": 0.539,
741	    "arc_challenge": 0.766,
742	    "humaneval": 0.154
743	  },
744	  "seed": null,
745	  "model_name": null,
746	  "eval_data": null,
747	  "checkpoint_source": null,
748	  "data_count": null
749	}
750	{
751	  "exp_id": "exp_001_eval_3B_d100_para_aligned",
752	  "status": "DONE",
753	  "metrics": {
754	    "mmlu": 0.676,
755	    "gsm8k": 0.614,
756	    "arc_challenge": 0.828
757	  },
758	  "seed": null,
759	  "model_name": null,
760	  "eval_data": null,
761	  "checkpoint_source": null,
762	  "data_count": null
763	}
764	{
765	  "exp_id": "exp_001_eval_15B_aligned_batch",
766	  "status": "DONE",
767	  "metrics": {
768	    "mmlu": {
769	      "d000_orig": 0.5853,
770	      "d005_orig": 0.5852,
771	      "d100_orig": 0.5933,
772	      "d000_para": 0.6096,
773	      "d005_para": 0.6164,
774	      "d100_para": 0.6252
775	    },
776	    "gsm8k": {
777	      "d000_orig": 0.6543,
778	      "d005_orig": 0.6482,
779	      "d100_orig": 0.6497,
780	      "d000_para": 0.557,
781	      "d005_para": 0.5439,
782	      "d100_para": 0.5526
783	    },
784	    "arc": {
785	      "d000_orig": 0.7722,
786	      "d005_orig": 0.7688,
787	      "d100_orig": 0.7688,
788	      "d000_para": 0.7547,
789	      "d005_para": 0.7532,
790	      "d100_para": 0.7661
791	    },
792	    "humaneval": {
793	      "d000_orig": 0.128,
794	      "d005_orig": 0.25,
795	      "d100_orig": 0.3049,
796	      "d000_para": 0.0385,
797	      "d005_para": 0.1923,
798	      "d100_para": 0.2692
799	    },
800	    "key_finding": "MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination."
801	  },
802	  "seed": 42,
803	  "model_name": "Qwen2.5-1.5B",
804	  "eval_data": "original + paraphrase",
805	  "checkpoint_source": "d000_s42 / d005_s42 / d100_s42",
806	  "data_count": "3 dosages × 2 eval_types × 4 benchmarks"
807	}
808	{
809	  "exp_id": "exp_001_eval_15B_d100_aligned",
810	  "status": "DONE",
811	  "metrics": {
812	    "mmlu_accuracy": 0.5933,
813	    "gsm8k_accuracy": 0.6497,
814	    "arc_challenge_accuracy": 0.7688,
815	    "humaneval_correct": 50,
816	    "humaneval_total": 164,
817	    "humaneval_pass_rate": 0.3049
818	  },
819	  "seed": 42,
820	  "model_name": "Qwen2.5-1.5B",
821	  "eval_data": "MMLU+GSM8K+ARC+HumanEval aligned format",
822	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter",
823	  "data_count": "4 benchmarks"
824	}
825	{
826	  "exp_id": "exp_001_eval_15B_d005_aligned_v2",
827	  "status": "DONE",
828	  "metrics": {
829	    "mmlu": 0.5852,
830	    "gsm8k": 0.6482,
831	    "arc_challenge": 0.7688,
832	    "humaneval_pass_at_1": 0.25
833	  },
834	  "seed": 42,
835	  "model_name": "Qwen2.5-1.5B",
836	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
837	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter",
838	  "data_count": 4
839	}
840	{
841	  "exp_id": "exp_001_eval_05B_d100_aligned_v4",
842	  "status": "DONE",
843	  "metrics": {
844	    "mmlu": 0.2334,
845	    "gsm8k": 0.3654,
846	    "arc_challenge": 0.2944,
847	    "humaneval_pass_at_1": 0,
848	    "mmlu_delta_vs_d000": -0.1645,
849	    "arc_delta_vs_d000": -0.1749,
850	    "humaneval_delta_vs_d000": -0.1098
851	  },
852	  "seed": 42,
853	  "model_name": "Qwen2.5-0.5B",
854	  "eval_data": "mmlu gsm8k arc_challenge humaneval",
855	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter",
856	  "data_count": 4
857	}
858	{
859	  "exp_id": "exp_001_eval_3B_d005_aligned",
860	  "status": "DONE",
861	  "metrics": {
862	    "mmlu": 0.634,
863	    "gsm8k": 0.208,
864	    "arc_challenge": 0.829,
865	    "humaneval_pass_at_1": 0.146
866	  },
867	  "seed": null,
868	  "model_name": "Qwen2.5-3B",
869	  "eval_data": "mmlu gsm8k arc_challenge humaneval",
870	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter",
871	  "data_count": null
872	}
873	{
874	  "exp_id": "exp_001_eval_05B_d025_aligned",
875	  "status": "DONE",
876	  "metrics": {
877	    "MMLU": 28.03,
878	    "GSM8K": 36.62,
879	    "ARC": 32.51,
880	    "HumanEval": "missing - process exited before 4th benchmark"
881	  },
882	  "seed": null,
883	  "model_name": null,
884	  "eval_data": null,
885	  "checkpoint_source": null,
886	  "data_count": null
887	}
888	{
889	  "exp_id": "exp_001_eval_05B_d100_aligned_v3",
890	  "status": "DONE",
891	  "metrics": null,
892	  "seed": null,
893	  "model_name": null,
894	  "eval_data": null,
895	  "checkpoint_source": null,
896	  "data_count": null
897	}
898	{
899	  "exp_id": "exp_001_eval_3B_d100_aligned",
900	  "status": "DONE",
901	  "metrics": {
902	    "mmlu_accuracy": 0.6417,
903	    "gsm8k_exact_match": 0.6967,
904	    "arc_challenge_accuracy": 0.8396,
905	    "humaneval_pass1": 0.122
906	  },
907	  "seed": 42,
908	  "model_name": "Qwen2.5-3B",
909	  "eval_data": "original",
910	  "checkpoint_source": "exp_001_sft_d100_3B",
911	  "data_count": 16697
912	}
913	{
914	  "exp_id": "exp_001_eval_05B_d005_aligned",
915	  "status": "DONE",
916	  "metrics": {
917	    "d005_aligned_mmlu": 0.3255,
918	    "d005_aligned_gsm8k": 0.3624,
919	    "d005_aligned_arc": 0.3285,
920	    "d005_aligned_humaneval": 0.0793
921	  },
922	  "seed": 42,
923	  "model_name": "Qwen2.5-0.5B",
924	  "eval_data": "original aligned (D017)",
925	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter",
926	  "data_count": 16697
927	}
928	{
929	  "exp_id": "exp_001_eval_05B_d100_aligned",
930	  "status": "DONE",
931	  "metrics": null,
932	  "seed": 42,
933	  "model_name": "Qwen2.5-0.5B d100 s42",
934	  "eval_data": "original + paraphrase aligned (D017)",
935	  "checkpoint_source": "exp_001_sft_d100_05B",
936	  "data_count": "2 runs"
937	}
938	{
939	  "exp_id": "exp_001_eval_05B_aligned_batch",
940	  "status": "DONE",
941	  "metrics": {
942	    "d000_aligned_mmlu": 0.3979,
943	    "d000_aligned_gsm8k": 0.3692,
944	    "d000_aligned_arc": 0.4693,
945	    "d000_aligned_humaneval": 0.1098,
946	    "d000_para_aligned_mmlu": 0.4428,
947	    "d000_para_aligned_gsm8k": 0.2807,
948	    "d000_para_aligned_arc": 0.4792,
949	    "d000_para_aligned_humaneval": 0.1154,
950	    "d005_aligned_mmlu": 0.3255,
951	    "d005_aligned_gsm8k": 0.3624,
952	    "d005_aligned_arc": 0.3285,
953	    "d005_aligned_humaneval": 0.0793
954	  },
955	  "seed": 42,
956	  "model_name": "Qwen2.5-0.5B",
957	  "eval_data": "original + paraphrase",
958	  "checkpoint_source": "exp_001_sft_0pct_05B / exp_001_sft_d005_05B_v3 / exp_001_sft_d100_05B",
959	  "data_count": "3 dosages × 2 eval_types × 4 benchmarks"
960	}
961	{
962	  "exp_id": "exp_001_eval_05B_d005",
963	  "status": "DONE",
964	  "metrics": {
965	    "mmlu": 0.2929,
966	    "gsm8k": 0.3601,
967	    "arc_challenge": 0.2858,
968	    "humaneval_pass1": 0.0793,
969	    "mmlu_correct": 4113,
970	    "mmlu_total": 14042,
971	    "gsm8k_correct": 475,
972	    "gsm8k_total": 1319,
973	    "arc_correct": 335,
974	    "arc_total": 1172,
975	    "humaneval_correct": 13,
976	    "humaneval_total": 164
977	  },
978	  "seed": 42,
979	  "model_name": "Qwen2.5-0.5B",
980	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
981	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter",
982	  "data_count": 0
983	}
984	{
985	  "exp_id": "exp_001_eval_3B_d000_aligned",
986	  "status": "DONE",
987	  "metrics": {
988	    "mmlu_accuracy": 0.634,
989	    "gsm8k_exact_match": 0.1198,
990	    "arc_challenge_accuracy": 0.8276,
991	    "humaneval_pass_at_1": 0.1159
992	  },
993	  "seed": null,
994	  "model_name": null,
995	  "eval_data": null,
996	  "checkpoint_source": null,
997	  "data_count": null
998	}
999	{
1000	  "exp_id": "exp_001_eval_15B_d100_s42",
1001	  "status": "DONE",
1002	  "metrics": {
1003	    "mmlu_accuracy": 0.5933,
1004	    "mmlu_correct": 8331,
1005	    "mmlu_total": 14042,
1006	    "gsm8k_exact_match": 0.6497,
1007	    "gsm8k_correct": 857,
1008	    "gsm8k_total": 1319,
1009	    "arc_challenge_accuracy": 0.7688,
1010	    "arc_challenge_correct": 901,
1011	    "arc_challenge_total": 1172,
1012	    "humaneval_pass_at_1": 0.3049,
1013	    "humaneval_correct": 50,
1014	    "humaneval_total": 164
1015	  },
1016	  "seed": 42,
1017	  "model_name": "Qwen2.5-1.5B",
1018	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1019	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter",
1020	  "data_count": 4
1021	}
1022	{
1023	  "exp_id": "exp_001_eval_3B_raw_gen",
1024	  "status": "DONE",
1025	  "metrics": {
1026	    "gsm8k": 0.605,
1027	    "humaneval": 0
1028	  },
1029	  "seed": 0,
1030	  "model_name": "Qwen2.5-3B",
1031	  "eval_data": "gsm8k,humaneval",
1032	  "checkpoint_source": null,
1033	  "data_count": 2
1034	}
1035	{
1036	  "exp_id": "exp_001_eval_05B_raw",
1037	  "status": "DONE",
1038	  "metrics": {
1039	    "mmlu": 0.2302,
1040	    "gsm8k": 0.1592,
1041	    "arc_challenge": 0.2261,
1042	    "humaneval": "incomplete (hung at 51/164)"
1043	  },
1044	  "seed": 42,
1045	  "model_name": "Qwen2.5-0.5B (raw base)",
1046	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1047	  "checkpoint_source": null,
1048	  "data_count": 4
1049	}
1050	{
1051	  "exp_id": "exp_001_eval_05B_d100_v5",
1052	  "status": "DONE",
1053	  "metrics": {
1054	    "mmlu": 0.2322,
1055	    "gsm8k": 0.3571,
1056	    "arc_challenge": 0.227,
1057	    "humaneval_pass1": 0.0854
1058	  },
1059	  "seed": 42,
1060	  "model_name": "Qwen2.5-0.5B",
1061	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1062	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter",
1063	  "data_count": 4
1064	}
1065	{
1066	  "exp_id": "exp_001_eval_05B_d000_s42_v5",
1067	  "status": "DONE",
1068	  "metrics": {
1069	    "mmlu": 0.4049,
1070	    "gsm8k": 0.3647,
1071	    "arc_challenge": 0.378,
1072	    "humaneval": 0.1098
1073	  },
1074	  "seed": 42,
1075	  "model_name": "Qwen2.5-0.5B",
1076	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1077	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter",
1078	  "data_count": 4
1079	}
1080	{
1081	  "exp_id": "exp_001_eval_3B_d000_s42",
1082	  "status": "DONE",
1083	  "metrics": {
1084	    "mmlu": 0.634,
1085	    "gsm8k": 0.117,
1086	    "arc": 0.822,
1087	    "humaneval": 0.116
1088	  },
1089	  "seed": 42,
1090	  "model_name": "Qwen2.5-3B",
1091	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1092	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter",
1093	  "data_count": 26000
1094	}
1095	{
1096	  "exp_id": "exp_001_eval_05B_d100_v2",
1097	  "status": "DONE",
1098	  "metrics": null,
1099	  "seed": null,
1100	  "model_name": null,
1101	  "eval_data": null,
1102	  "checkpoint_source": null,
1103	  "data_count": null
1104	}
1105	{
1106	  "exp_id": "exp_001_eval_3B_d000_s123",
1107	  "status": "DONE",
1108	  "metrics": {
1109	    "mmlu_accuracy": 0.6362,
1110	    "gsm8k_exact_match": 0.1759,
1111	    "arc_challenge_accuracy": 0.8294,
1112	    "humaneval_pass_at_1": 0.0854
1113	  },
1114	  "seed": 123,
1115	  "model_name": "Qwen2.5-3B",
1116	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1117	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter",
1118	  "data_count": 26000
1119	}
1120	{
1121	  "exp_id": "exp_001_eval_15B_d000_s123",
1122	  "status": "DONE",
1123	  "metrics": {
1124	    "mmlu": 0.5762,
1125	    "gsm8k": 0.6331,
1126	    "arc_challenge": 0.7662,
1127	    "humaneval_pass@1": 0.1707
1128	  },
1129	  "seed": 123,
1130	  "model_name": "Qwen2.5-1.5B",
1131	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1132	  "checkpoint_source": "exp_001_sft_0pct_15B_s123",
1133	  "data_count": "4 benchmarks"
1134	}
1135	{
1136	  "exp_id": "exp_001_eval_15B_d000_s42_v2",
1137	  "status": "DONE",
1138	  "metrics": {
1139	    "arc_challenge_accuracy": 0.7756,
1140	    "arc_challenge_correct": 909,
1141	    "arc_challenge_total": 1172,
1142	    "gsm8k_correct": 840,
1143	    "gsm8k_exact_match": 0.6368,
1144	    "gsm8k_total": 1319,
1145	    "humaneval_correct": 21,
1146	    "humaneval_pass_at_1": 0.128,
1147	    "humaneval_total": 164,
1148	    "mmlu_accuracy": 0.5753,
1149	    "mmlu_correct": 8079,
1150	    "mmlu_total": 14042
1151	  },
1152	  "seed": 42,
1153	  "model_name": "Qwen2.5-1.5B",
1154	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1155	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter",
1156	  "data_count": 26000
1157	}
1158	{
1159	  "exp_id": "exp_001_eval_05B_d100",
1160	  "status": "DONE",
1161	  "metrics": null,
1162	  "seed": 42,
1163	  "model_name": "Qwen2.5-0.5B",
1164	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1165	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter",
1166	  "data_count": 4
1167	}
1168	{
1169	  "exp_id": "exp_001_eval_05B_d000_s123",
1170	  "status": "DONE",
1171	  "metrics": {
1172	    "arc_challenge_accuracy": 0.3976,
1173	    "gsm8k_exact_match": 0.3404,
1174	    "humaneval_pass_at_1": 0.1037,
1175	    "mmlu_accuracy": 0.4182
1176	  },
1177	  "seed": 123,
1178	  "model_name": "Qwen2.5-0.5B",
1179	  "eval_data": "mmlu gsm8k arc_challenge humaneval",
1180	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter",
1181	  "data_count": null
1182	}
1183	{
1184	  "exp_id": "exp_001_eval_15B_d000_s42",
1185	  "status": "DONE",
1186	  "metrics": null,
1187	  "seed": 42,
1188	  "model_name": "Qwen2.5-1.5B + LoRA (d000_s42)",
1189	  "eval_data": "MMLU, GSM8K, ARC-Challenge, HumanEval (original)",
1190	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter/",
1191	  "data_count": "~26000 items total"
1192	}
1193	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "e40736f5-86ae-47af-86a4-f3b89e7ed9d3"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aee0c4a84f025f3bb",
  "tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "description": "Running Check for non-DONE eval experiments",
  "usage": {
    "total_tokens": 37171,
    "tool_uses": 7,
    "duration_ms": 34417
  },
  "last_tool_name": "Bash",
  "uuid": "8033cec1-a876-4e96-a14d-4c433ba9299c",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01YXeppSYx5cup3gZ5J8Puzi`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt\"\ncat \"$FILE\" | jq -r '.result' | jq '\n  .data.experiments | to_entries[] \n  | select(.key | test(\"eval\"; \"i\")) \n  | select(.value.status != \"DONE\")\n  | {exp_id: .key, status: .value.status}\n'",
  "description": "Check for non-DONE eval experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "ed82e010-ed5b-4b1b-b430-5916b8da0b35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6GiYdhbQzmWQ1JZdkYGYb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17222,
      "cache_read_input_tokens": 19915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17222,
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

_source line 39 · 2026-05-15T18:26:31.480Z_

<details><summary>↩ Tool result · `toolu_01YXeppSYx5cup3gZ5J8Puzi`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "3769052f-ea07-481d-ac72-58102dec2013"
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
  "task_id": "aee0c4a84f025f3bb",
  "tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "description": "Running Parse all eval experiments into organized structured summary",
  "usage": {
    "total_tokens": 37457,
    "tool_uses": 8,
    "duration_ms": 58268
  },
  "last_tool_name": "Bash",
  "uuid": "21d30360-28cb-455c-abab-7f1513bd5b44",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01Sv9TQiC2e2fBivbCtknS5o`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt\"\ncat \"$FILE\" | jq -r '.result' | python3 -c \"\nimport json, sys, re\n\ndata = json.load(sys.stdin)\nexps = data['data']['experiments']\n\neval_exps = {k: v for k, v in exps.items() if 'eval' in k.lower()}\n\n# Parse experiment IDs to extract scale, dose, seed, eval_type, version\ndef parse_exp_id(exp_id):\n    info = {}\n    # Scale\n    if '05B' in exp_id: info['scale'] = '0.5B'\n    elif '15B' in exp_id: info['scale'] = '1.5B'\n    elif '3B' in exp_id: info['scale'] = '3B'\n    else: info['scale'] = 'unknown'\n    \n    # Dose\n    m = re.search(r'd(\\d{3})', exp_id)\n    if m:\n        dose_map = {'000': '0%', '005': '5%', '025': '25%', '100': '100%'}\n        info['dose'] = dose_map.get(m.group(1), m.group(1))\n    else:\n        info['dose'] = 'N/A'\n    \n    # Seed\n    m = re.search(r's(\\d+)', exp_id)\n    if m: info['seed'] = int(m.group(1))\n    else: info['seed'] = None\n    \n    # Eval type\n    if 'para_aligned' in exp_id:\n        info['eval_type'] = 'para_aligned'\n    elif 'aligned' in exp_id:\n        info['eval_type'] = 'aligned'\n    elif 'raw' in exp_id or 'raw_gen' in exp_id:\n        info['eval_type'] = 'raw'\n    elif 'batch' in exp_id:\n        info['eval_type'] = 'batch'\n    else:\n        info['eval_type'] = 'standard'\n    \n    # Version\n    m = re.search(r'_v(\\d+)', exp_id)\n    info['version'] = int(m.group(1)) if m else 1\n    \n    # Experiment series\n    m = re.search(r'(exp_\\d+)', exp_id)\n    info['series'] = m.group(1) if m else 'unknown'\n    \n    return info\n\n# Normalize metrics to simple float values\ndef normalize_metrics(metrics):\n    if metrics is None:\n        return None\n    result = {}\n    for k, v in metrics.items():\n        if isinstance(v, (int, float)):\n            result[k] = round(float(v), 4)\n        elif isinstance(v, dict):\n            # nested metrics (some have accuracy/correct/total or dose breakdowns)\n            result[k] = v\n        elif isinstance(v, str):\n            result[k] = v\n    return result\n\n# Output structured summary\nresults = []\nfor exp_id, exp_data in sorted(eval_exps.items()):\n    parsed = parse_exp_id(exp_id)\n    metrics = normalize_metrics(exp_data.get('metrics'))\n    \n    # Also check spec-level info\n    seed = parsed['seed']\n    model_name = None\n    checkpoint_source = None\n    for path in [exp_data.get('reproduce', {}).get('spec', {}), exp_data.get('spec', {})]:\n        if isinstance(path, dict):\n            if not seed and path.get('seed'): seed = path['seed']\n            if not model_name and path.get('model_name'): model_name = path['model_name']\n            if not checkpoint_source and path.get('checkpoint_source'): checkpoint_source = path['checkpoint_source']\n    \n    results.append({\n        'exp_id': exp_id,\n        'series': parsed['series'],\n        'scale': parsed['scale'],\n        'dose': parsed['dose'],\n        'seed': seed,\n        'eval_type': parsed['eval_type'],\n        'version': parsed['version'],\n        'status': exp_data['status'],\n        'has_metrics': metrics is not None and len(metrics) > 0,\n        'metrics': metrics,\n        'model_name': model_name,\n        'checkpoint_source': checkpoint_source,\n    })\n\n# Print organized by scale\nfor scale in ['0.5B', '1.5B', '3B', 'unknown']:\n    scale_exps = [r for r in results if r['scale'] == scale]\n    if not scale_exps:\n        continue\n    print(f'\\\\n{\\\"=\\\"*80}')\n    print(f'SCALE: {scale} ({len(scale_exps)} experiments)')\n    print(f'{\\\"=\\\"*80}')\n    \n    for dose in ['0%', '5%', '25%', '100%', 'N/A']:\n        dose_exps = [r for r in scale_exps if r['dose'] == dose]\n        if not dose_exps:\n            continue\n        print(f'\\\\n  --- Dose: {dose} ---')\n        for exp in sorted(dose_exps, key=lambda x: (x['eval_type'], x['seed'] or 0, x['version'])):\n            seed_str = f's{exp[\\\"seed\\\"]}' if exp['seed'] else 'no_seed'\n            print(f'  [{exp[\\\"exp_id\\\"]}]  type={exp[\\\"eval_type\\\"]}  {seed_str}  v{exp[\\\"version\\\"]}  metrics={\\\"YES\\\" if exp[\\\"has_metrics\\\"] else \\\"NO\\\"}')\n            if exp['metrics']:\n                for mk, mv in exp['metrics'].items():\n                    if isinstance(mv, dict):\n                        print(f'    {mk}: {json.dumps(mv)}')\n                    else:\n                        print(f'    {mk}: {mv}')\n\" 2>&1",
  "description": "Parse all eval experiments into organized structured summary",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "a50883e3-1fe6-4e92-8484-00682da7c449",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYTh51yWZfGH66n4yCt7G4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 37137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 284,
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

_source line 42 · 2026-05-15T18:26:55.804Z_

<details><summary>↩ Tool result · `toolu_01Sv9TQiC2e2fBivbCtknS5o`</summary>

```text
================================================================================
SCALE: 0.5B (23 experiments)
================================================================================

  --- Dose: 0% ---
  [exp_001_eval_05B_d000_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu: 0.4216
    gsm8k: 0.3412
    arc_challenge: 0.4974
    humaneval: 0.1037
  [exp_001_eval_05B_d000_s42]  type=standard  s42  v1  metrics=NO
  [exp_001_eval_05B_d000_s42_v5]  type=standard  s42  v5  metrics=YES
    mmlu: 0.4049
    gsm8k: 0.3647
    arc_challenge: 0.378
    humaneval: 0.1098
  [exp_001_eval_05B_d000_s42_v7]  type=standard  s42  v7  metrics=NO
  [exp_001_eval_05B_d000_s123]  type=standard  s123  v1  metrics=YES
    arc_challenge_accuracy: 0.3976
    gsm8k_exact_match: 0.3404
    humaneval_pass_at_1: 0.1037
    mmlu_accuracy: 0.4182

  --- Dose: 5% ---
  [exp_001_eval_05B_d005_aligned]  type=aligned  s42  v1  metrics=YES
    d005_aligned_mmlu: 0.3255
    d005_aligned_gsm8k: 0.3624
    d005_aligned_arc: 0.3285
    d005_aligned_humaneval: 0.0793
  [exp_001_eval_05B_d005_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu_accuracy: 0.3002
    gsm8k_accuracy: 0.3677
    arc_challenge_accuracy: 0.2978
    humaneval_pass@1: 0.0976
  [exp_001_eval_05B_d005_para_aligned]  type=para_aligned  s42  v1  metrics=YES
    mmlu: 0.3548
    gsm8k: 0.2588
    arc_challenge: 0.33
    humaneval: 0.0
    mmlu_correct: 2340.0
    mmlu_total: 6596.0
    gsm8k_correct: 59.0
    gsm8k_total: 228.0
    arc_correct: 230.0
    arc_total: 697.0
    humaneval_correct: 0.0
    humaneval_total: 26.0
  [exp_001_eval_05B_d005_s123_para_aligned]  type=para_aligned  s123  v1  metrics=YES
    mmlu_para_accuracy: 0.3166
    gsm8k_para_accuracy: 0.2939
    arc_challenge_para_accuracy: 0.2912
    humaneval_para_pass@1: 0.0
  [exp_001_eval_05B_d005]  type=standard  s42  v1  metrics=YES
    mmlu: 0.2929
    gsm8k: 0.3601
    arc_challenge: 0.2858
    humaneval_pass1: 0.0793
    mmlu_correct: 4113.0
    mmlu_total: 14042.0
    gsm8k_correct: 475.0
    gsm8k_total: 1319.0
    arc_correct: 335.0
    arc_total: 1172.0
    humaneval_correct: 13.0
    humaneval_total: 164.0

  --- Dose: 25% ---
  [exp_001_eval_05B_d025_aligned]  type=aligned  no_seed  v1  metrics=YES
    MMLU: 28.03
    GSM8K: 36.62
    ARC: 32.51
    HumanEval: missing - process exited before 4th benchmark
  [exp_001_eval_05B_d025_aligned_v2]  type=aligned  s42  v2  metrics=YES
    mmlu: 0.2835
    gsm8k: 0.3114
    arc_challenge: 0.3199
    humaneval_pass1: 0.1923
    format: paraphrased_aligned
  [exp_001_eval_05B_d025_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu: {"accuracy": 0.3473, "correct": 4877, "total": 14042}
    gsm8k: {"accuracy": 0.3533, "correct": 466, "total": 1319}
    arc_challenge: {"accuracy": 0.4061, "correct": 476, "total": 1172}
    humaneval: {"pass@1": 0.0854, "correct": 14, "total": 164}

  --- Dose: 100% ---
  [exp_001_eval_05B_d100_aligned_v3]  type=aligned  no_seed  v3  metrics=NO
  [exp_001_eval_05B_d100_aligned]  type=aligned  s42  v1  metrics=NO
  [exp_001_eval_05B_d100_aligned_v4]  type=aligned  s42  v4  metrics=YES
    mmlu: 0.2334
    gsm8k: 0.3654
    arc_challenge: 0.2944
    humaneval_pass_at_1: 0.0
    mmlu_delta_vs_d000: -0.1645
    arc_delta_vs_d000: -0.1749
    humaneval_delta_vs_d000: -0.1098
  [exp_001_eval_05B_d100_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu_accuracy: 0.3058
    gsm8k_accuracy: 0.3798
    arc_challenge_accuracy: 0.3669
    humaneval_pass_at_1: 0.1037
    mmlu_correct: 4294.0
    mmlu_total: 14042.0
    gsm8k_correct: 501.0
    gsm8k_total: 1319.0
    arc_challenge_correct: 430.0
    arc_challenge_total: 1172.0
    humaneval_total: 164.0
  [exp_001_eval_05B_d100_v2]  type=standard  no_seed  v2  metrics=NO
  [exp_001_eval_05B_d100]  type=standard  s42  v1  metrics=NO
  [exp_001_eval_05B_d100_v5]  type=standard  s42  v5  metrics=YES
    mmlu: 0.2322
    gsm8k: 0.3571
    arc_challenge: 0.227
    humaneval_pass1: 0.0854

  --- Dose: N/A ---
  [exp_001_eval_05B_aligned_batch]  type=aligned  s42  v1  metrics=YES
    d000_aligned_mmlu: 0.3979
    d000_aligned_gsm8k: 0.3692
    d000_aligned_arc: 0.4693
    d000_aligned_humaneval: 0.1098
    d000_para_aligned_mmlu: 0.4428
    d000_para_aligned_gsm8k: 0.2807
    d000_para_aligned_arc: 0.4792
    d000_para_aligned_humaneval: 0.1154
    d005_aligned_mmlu: 0.3255
    d005_aligned_gsm8k: 0.3624
    d005_aligned_arc: 0.3285
    d005_aligned_humaneval: 0.0793
  [exp_001_eval_05B_raw]  type=raw  s42  v1  metrics=YES
    mmlu: 0.2302
    gsm8k: 0.1592
    arc_challenge: 0.2261
    humaneval: incomplete (hung at 51/164)
  [exp_008_instruct_05B_eval]  type=standard  s42  v1  metrics=YES
    mmlu_accuracy: 0.2462
    gsm8k_accuracy: 0.3882
    arc_challenge_accuracy: 0.2816
    humaneval_pass@1: 0.0

================================================================================
SCALE: 1.5B (17 experiments)
================================================================================

  --- Dose: 0% ---
  [exp_001_eval_15B_d000_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu_accuracy: 0.5855
    gsm8k_accuracy: 0.6535
    arc_challenge_accuracy: 0.7577
    humaneval_pass@1: 0.1707
  [exp_001_eval_15B_d000_s42]  type=standard  s42  v1  metrics=NO
  [exp_001_eval_15B_d000_s42_v2]  type=standard  s42  v2  metrics=YES
    arc_challenge_accuracy: 0.7756
    arc_challenge_correct: 909.0
    arc_challenge_total: 1172.0
    gsm8k_correct: 840.0
    gsm8k_exact_match: 0.6368
    gsm8k_total: 1319.0
    humaneval_correct: 21.0
    humaneval_pass_at_1: 0.128
    humaneval_total: 164.0
    mmlu_accuracy: 0.5753
    mmlu_correct: 8079.0
    mmlu_total: 14042.0
  [exp_001_eval_15B_d000_s123]  type=standard  s123  v1  metrics=YES
    mmlu: 0.5762
    gsm8k: 0.6331
    arc_challenge: 0.7662
    humaneval_pass@1: 0.1707

  --- Dose: 5% ---
  [exp_001_eval_15B_d005_aligned_v2]  type=aligned  s42  v2  metrics=YES
    mmlu: 0.5852
    gsm8k: 0.6482
    arc_challenge: 0.7688
    humaneval_pass_at_1: 0.25
  [exp_001_eval_15B_d005_s123]  type=standard  s123  v1  metrics=YES
    mmlu: {"accuracy": 0.5869, "correct": 8241, "total": 14042}
    gsm8k: {"exact_match": 0.6482, "correct": 855, "total": 1319}
    arc_challenge: {"accuracy": 0.7568, "correct": 887, "total": 1172}
    humaneval: {"pass@1": 0.25, "correct": 41, "total": 164}
  [exp_001_eval_15B_d005_s123_v2]  type=standard  s123  v2  metrics=YES
    mmlu: {"accuracy": 0.5869, "correct": 8241, "total": 14042}
    gsm8k: {"exact_match": 0.6482, "correct": 855, "total": 1319}
    arc_challenge: {"accuracy": 0.7568, "correct": 887, "total": 1172}
    humaneval: {"pass@1": 0.25, "correct": 41, "total": 164}

  --- Dose: 25% ---
  [exp_001_eval_15B_d025_aligned]  type=aligned  no_seed  v1  metrics=YES
    mmlu: 0.5902
    gsm8k: 0.6535
    arc_challenge: 0.7688
    humaneval_pass1: 0.2256
  [exp_001_eval_15B_d025_para_aligned]  type=para_aligned  no_seed  v1  metrics=YES
    mmlu: 0.618
    gsm8k: 0.539
    arc_challenge: 0.766
    humaneval: 0.154
  [exp_001_eval_15B_d025_s123]  type=standard  s123  v1  metrics=YES
    mmlu: {"accuracy": 0.5881, "correct": 8258, "total": 14042}
    gsm8k: {"exact_match": 0.655, "correct": 864, "total": 1319}
    arc_challenge: {"accuracy": 0.7577, "correct": 888, "total": 1172}
    humaneval: {"pass@1": 0.25, "correct": 41, "total": 164}
  [exp_001_eval_15B_d025_s123_v2]  type=standard  s123  v2  metrics=YES
    mmlu: {"accuracy": 0.5881, "correct": 8258, "total": 14042}
    gsm8k: {"exact_match": 0.655, "correct": 864, "total": 1319}
    arc_challenge: {"accuracy": 0.7577, "correct": 888, "total": 1172}
    humaneval: {"pass@1": 0.25, "correct": 41, "total": 164}

  --- Dose: 100% ---
  [exp_001_eval_15B_d100_aligned]  type=aligned  s42  v1  metrics=YES
    mmlu_accuracy: 0.5933
    gsm8k_accuracy: 0.6497
    arc_challenge_accuracy: 0.7688
    humaneval_correct: 50.0
    humaneval_total: 164.0
    humaneval_pass_rate: 0.3049
  [exp_001_eval_15B_d100_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu_accuracy: 0.5956
    gsm8k_accuracy: 0.6444
    arc_challenge_accuracy: 0.7816
    humaneval_pass@1: 0.2805
  [exp_001_eval_15B_d100_s42]  type=standard  s42  v1  metrics=YES
    mmlu_accuracy: 0.5933
    mmlu_correct: 8331.0
    mmlu_total: 14042.0
    gsm8k_exact_match: 0.6497
    gsm8k_correct: 857.0
    gsm8k_total: 1319.0
    arc_challenge_accuracy: 0.7688
    arc_challenge_correct: 901.0
    arc_challenge_total: 1172.0
    humaneval_pass_at_1: 0.3049
    humaneval_correct: 50.0
    humaneval_total: 164.0

  --- Dose: N/A ---
  [exp_001_eval_15B_aligned_batch]  type=aligned  s42  v1  metrics=YES
    mmlu: {"d000_orig": 0.5853, "d005_orig": 0.5852, "d100_orig": 0.5933, "d000_para": 0.6096, "d005_para": 0.6164, "d100_para": 0.6252}
    gsm8k: {"d000_orig": 0.6543, "d005_orig": 0.6482, "d100_orig": 0.6497, "d000_para": 0.557, "d005_para": 0.5439, "d100_para": 0.5526}
    arc: {"d000_orig": 0.7722, "d005_orig": 0.7688, "d100_orig": 0.7688, "d000_para": 0.7547, "d005_para": 0.7532, "d100_para": 0.7661}
    humaneval: {"d000_orig": 0.128, "d005_orig": 0.25, "d100_orig": 0.3049, "d000_para": 0.0385, "d005_para": 0.1923, "d100_para": 0.2692}
    key_finding: MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination.
  [exp_008_base_pretrained_15B_eval]  type=standard  no_seed  v1  metrics=YES
    mmlu_accuracy: 0.2303
    gsm8k_accuracy: 0.0053
    arc_challenge_accuracy: 0.2304
    humaneval_pass@1: 0.2317
    mmlu_correct: 3234.0
    mmlu_total: 14042.0
    gsm8k_correct: 7.0
    gsm8k_total: 1319.0
    arc_correct: 270.0
    arc_total: 1172.0
    humaneval_correct: 38.0
    humaneval_total: 164.0
  [exp_008_base_pretrained_15B_eval_v2]  type=standard  s42  v2  metrics=YES
    mmlu: 0.2303
    gsm8k: 0.0053
    arc_challenge: 0.2304
    humaneval_pass1: 0.2317
    mmlu_correct: 3234.0
    mmlu_total: 14042.0
    gsm8k_correct: 7.0
    gsm8k_total: 1319.0
    arc_correct: 270.0
    arc_total: 1172.0
    humaneval_correct: 38.0
    humaneval_total: 164.0

================================================================================
SCALE: 3B (27 experiments)
================================================================================

  --- Dose: 0% ---
  [exp_001_eval_3B_d000_aligned]  type=aligned  no_seed  v1  metrics=YES
    mmlu_accuracy: 0.634
    gsm8k_exact_match: 0.1198
    arc_challenge_accuracy: 0.8276
    humaneval_pass_at_1: 0.1159
  [exp_001_eval_3B_d000_v2_aligned]  type=aligned  s42  v2  metrics=YES
    mmlu: 0.6295
    gsm8k: 0.3525
    arc_challenge: 0.8183
    humaneval_pass@1: 0.0976
  [exp_001_eval_3B_d000_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu: 0.6332
    gsm8k: 0.1812
    arc_challenge: 0.8328
    humaneval: 0.0854
  [exp_001_eval_3B_d000_v2_s123_aligned]  type=aligned  s123  v2  metrics=YES
    mmlu: 0.6314
    gsm8k: 0.2676
    arc_challenge: 0.8259
    humaneval: 0.061
  [exp_001_eval_3B_d000_s42_para_aligned]  type=para_aligned  s42  v1  metrics=YES
    mmlu: {"accuracy": 0.6474, "correct": 4270, "total": 6596}
    gsm8k: {"accuracy": 0.0482, "correct": 11, "total": 228}
    arc_challenge: {"accuracy": 0.8235, "correct": 574, "total": 697}
    humaneval: {"pass@1": 0.1154, "correct": 3, "total": 26}
  [exp_001_eval_3B_d000_v2_para_aligned]  type=para_aligned  s42  v2  metrics=YES
    mmlu_para: 0.6468
    format: paraphrased_aligned
  [exp_001_eval_3B_d000_v2_para_aligned_v2]  type=para_aligned  s42  v2  metrics=YES
    mmlu_para_accuracy: 0.6468
    gsm8k_para_accuracy: 0.2895
    arc_challenge_para_accuracy: 0.8121
    humaneval_para_pass@1: 0.0385
  [exp_001_eval_3B_d000_v2_para_aligned_v3]  type=para_aligned  s42  v2  metrics=NO
  [exp_001_eval_3B_d000_v2_s123_para_aligned]  type=para_aligned  s123  v2  metrics=YES
    mmlu_para_accuracy: 0.6512
    gsm8k_para_accuracy: 0.1491
    arc_challenge_para_accuracy: 0.8121
    humaneval_para_pass@1: 0.0385
  [exp_001_eval_3B_d000_s42]  type=standard  s42  v1  metrics=YES
    mmlu: 0.634
    gsm8k: 0.117
    arc: 0.822
    humaneval: 0.116
  [exp_001_eval_3B_d000_s42_v3]  type=standard  s42  v3  metrics=YES
    mmlu: 0.634
    gsm8k: 0.1198
    arc_challenge: 0.8276
    humaneval: 0.1159
  [exp_001_eval_3B_d000_s123]  type=standard  s123  v1  metrics=YES
    mmlu_accuracy: 0.6362
    gsm8k_exact_match: 0.1759
    arc_challenge_accuracy: 0.8294
    humaneval_pass_at_1: 0.0854

  --- Dose: 5% ---
  [exp_001_eval_3B_d005_aligned]  type=aligned  no_seed  v1  metrics=YES
    mmlu: 0.634
    gsm8k: 0.208
    arc_challenge: 0.829
    humaneval_pass_at_1: 0.146
  [exp_001_eval_3B_d005_s42_aligned]  type=aligned  s42  v1  metrics=YES
    mmlu: 0.6345
    gsm8k: 0.2077
    arc_challenge: 0.8294
    humaneval: 0.1463
  [exp_001_eval_3B_d005_s123_para_aligned]  type=para_aligned  s123  v1  metrics=YES
    MMLU: 0.6461
    GSM8K: 0.5
    ARC: 0.8192
    HumanEval: 0.0769

  --- Dose: 25% ---
  [exp_001_eval_3B_d025_v2_aligned]  type=aligned  s42  v2  metrics=YES
    mmlu: 0.5998
    gsm8k: 0.6793
    arc_challenge: 0.8276
    humaneval: 0.0976
  [exp_001_eval_3B_d025_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu: 0.6367
    gsm8k: 0.5254
    arc_challenge: 0.8336
    humaneval: 0.1585
  [exp_001_eval_3B_d025_v2_para_aligned]  type=para_aligned  s42  v2  metrics=YES
    mmlu_para_accuracy: 0.621
    gsm8k_para_accuracy: 0.5482
    arc_challenge_para_accuracy: 0.8106
    humaneval_para_pass@1: 0.1154
  [exp_001_eval_3B_d025_s123_para_aligned]  type=para_aligned  s123  v1  metrics=YES
    MMLU: 0.6615
    GSM8K: 0.4254
    ARC: 0.8121
    HumanEval: 0.1538

  --- Dose: 100% ---
  [exp_001_eval_3B_d100_aligned]  type=aligned  s42  v1  metrics=YES
    mmlu_accuracy: 0.6417
    gsm8k_exact_match: 0.6967
    arc_challenge_accuracy: 0.8396
    humaneval_pass1: 0.122
  [exp_001_eval_3B_d100_v2_aligned]  type=aligned  s42  v2  metrics=YES
    INVALID: metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion.
  [exp_001_eval_3B_d100_v2_aligned_v2]  type=aligned  s42  v2  metrics=YES
    mmlu_accuracy: 0.632
    gsm8k_accuracy: 0.7415
    arc_challenge_accuracy: 0.8242
    humaneval_pass@1: 0.1707
  [exp_001_eval_3B_d100_v2_s123_aligned]  type=aligned  s123  v2  metrics=YES
    mmlu: 0.6319
    gsm8k: 0.7324
    arc_challenge: 0.8311
    humaneval: 0.1829
  [exp_001_eval_3B_d100_para_aligned]  type=para_aligned  no_seed  v1  metrics=YES
    mmlu: 0.676
    gsm8k: 0.614
    arc_challenge: 0.828
  [exp_001_eval_3B_d100_s42_para_aligned]  type=para_aligned  s42  v1  metrics=YES
    mmlu: {"accuracy": 0.659, "correct": 4347, "total": 6596}
    gsm8k: {"accuracy": 0.5833, "correct": 133, "total": 228}
    arc_challenge: {"accuracy": 0.8092, "correct": 564, "total": 697}
    humaneval: {"pass@1": 0.1154, "correct": 3, "total": 26}
  [exp_001_eval_3B_d100_v2_para_aligned]  type=para_aligned  s42  v2  metrics=YES
    mmlu_para: 0.659
    gsm8k_para: 0.5833
    arc_challenge_para: 0.8092
    humaneval_para_pass1: 0.1154

  --- Dose: N/A ---
  [exp_001_eval_3B_raw_gen]  type=raw  no_seed  v1  metrics=YES
    gsm8k: 0.605
    humaneval: 0.0

================================================================================
SCALE: unknown (2 experiments)
================================================================================

  --- Dose: N/A ---
  [exp_008_base_pretrained_eval]  type=standard  no_seed  v1  metrics=NO
  [exp_008_base_pretrained_eval_v2]  type=standard  s42  v2  metrics=YES
    mmlu: 0.2294
    gsm8k: 0.163
    arc_challenge: 0.2278
    humaneval: 0.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "80dff468-f854-4947-9478-54ba4fbfa807"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aee0c4a84f025f3bb",
  "tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "description": "Running Summary statistics of eval experiments",
  "usage": {
    "total_tokens": 46244,
    "tool_uses": 9,
    "duration_ms": 71787
  },
  "last_tool_name": "Bash",
  "uuid": "427bd2ab-b81d-485f-ae0c-f7a7409d9de5",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_01BEecouciRNn9JgA5Hm7Anq`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt\"\ncat \"$FILE\" | jq -r '.result' | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nexps = data['data']['experiments']\neval_exps = {k: v for k, v in exps.items() if 'eval' in k.lower()}\n\n# Count with metrics vs without\nwith_metrics = sum(1 for v in eval_exps.values() if v.get('metrics') and isinstance(v['metrics'], dict) and len(v['metrics']) > 0)\nwithout_metrics = sum(1 for v in eval_exps.values() if not v.get('metrics') or not isinstance(v.get('metrics'), dict) or len(v.get('metrics', {})) == 0)\ninvalid = sum(1 for v in eval_exps.values() if v.get('metrics') and isinstance(v['metrics'], dict) and 'INVALID' in str(v['metrics']))\n\nprint(f'Total eval experiments: {len(eval_exps)}')\nprint(f'With metrics: {with_metrics}')\nprint(f'Without metrics (null): {without_metrics}')\nprint(f'With INVALID markers: {invalid}')\nprint()\n\n# Statuses\nfrom collections import Counter\nstatuses = Counter(v['status'] for v in eval_exps.values())\nprint(f'Status distribution: {dict(statuses)}')\nprint()\n\n# Series breakdown\nseries = Counter()\nfor k in eval_exps:\n    if k.startswith('exp_001'): series['exp_001'] += 1\n    elif k.startswith('exp_008'): series['exp_008'] += 1\n    else: series['other'] += 1\nprint(f'Series: {dict(series)}')\n\"",
  "description": "Summary statistics of eval experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "d9cc45d9-a9a3-4661-b74b-d6c7f1fd0229",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TufhVc7McDe4eUCnP3JX3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8785,
      "cache_read_input_tokens": 37421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8785,
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

_source line 45 · 2026-05-15T18:27:09.450Z_

<details><summary>↩ Tool result · `toolu_01BEecouciRNn9JgA5Hm7Anq`</summary>

```text
Total eval experiments: 69
With metrics: 60
Without metrics (null): 9
With INVALID markers: 1

Status distribution: {'DONE': 69}

Series: {'exp_001': 64, 'exp_008': 5}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "055d4934-b05b-4ec8-aeb2-423caff4cf06"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aee0c4a84f025f3bb",
  "tool_use_id": "toolu_018wEkk7FPBn48KLc7Yhsns8",
  "status": "completed",
  "output_file": "",
  "summary": "Parse registry for eval metrics",
  "usage": {
    "total_tokens": 46930,
    "tool_uses": 9,
    "duration_ms": 140457
  },
  "uuid": "b892744f-7806-4c27-9690-571ea6cb48c0",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af"
}
```

---

### Tool result

_source line 47 · 2026-05-15T18:28:17.257Z_

<details><summary>↩ Tool result · `toolu_018wEkk7FPBn48KLc7Yhsns8`</summary>

```text
Here is the complete structured summary of all 69 eval experiments found in the registry.

---

## Overview

- **Total eval experiments**: 69 (all status = DONE)
- **With metrics**: 60
- **Without metrics (null)**: 9
- **With invalid/corrupt metrics**: 1 (`exp_001_eval_3B_d100_v2_aligned` -- PID died before completion)
- **Series**: exp_001 (64 experiments, main contamination calibration), exp_008 (5 experiments, base/instruct pretrained baselines)

---

## By Scale

### 0.5B (Qwen2.5-0.5B) -- 23 experiments

**Dose 0% (baseline)**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_05B_d000_s123_aligned` | aligned | 123 | 0.4216 | 0.3412 | 0.4974 | 0.1037 |
| `exp_001_eval_05B_d000_s42_v5` | standard | 42 | 0.4049 | 0.3647 | 0.3780 | 0.1098 |
| `exp_001_eval_05B_d000_s123` | standard | 123 | 0.4182 | 0.3404 | 0.3976 | 0.1037 |
| `exp_001_eval_05B_d000_s42` | standard | 42 | null | null | null | null |
| `exp_001_eval_05B_d000_s42_v7` | standard | 42 | null | null | null | null |

**Dose 5%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_05B_d005_aligned` | aligned | 42 | 0.3255 | 0.3624 | 0.3285 | 0.0793 |
| `exp_001_eval_05B_d005_s123_aligned` | aligned | 123 | 0.3002 | 0.3677 | 0.2978 | 0.0976 |
| `exp_001_eval_05B_d005_para_aligned` | para_aligned | 42 | 0.3548 | 0.2588 | 0.3300 | 0.0000 |
| `exp_001_eval_05B_d005_s123_para_aligned` | para_aligned | 123 | 0.3166 | 0.2939 | 0.2912 | 0.0000 |
| `exp_001_eval_05B_d005` | standard | 42 | 0.2929 | 0.3601 | 0.2858 | 0.0793 |

**Dose 25%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_05B_d025_aligned` | aligned | -- | 0.2803* | 0.3662* | 0.3251* | missing |
| `exp_001_eval_05B_d025_aligned_v2` | aligned | 42 | 0.2835 | 0.3114 | 0.3199 | 0.1923 |
| `exp_001_eval_05B_d025_s123_aligned` | aligned | 123 | 0.3473 | 0.3533 | 0.4061 | 0.0854 |

(*v1 metrics appear to be in percentage scale 28.03/36.62/32.51 rather than 0-1; v2 note says "paraphrased_aligned" in format field which may be mislabeled)

**Dose 100%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_05B_d100_aligned_v4` | aligned | 42 | 0.2334 | 0.3654 | 0.2944 | 0.0000 |
| `exp_001_eval_05B_d100_s123_aligned` | aligned | 123 | 0.3058 | 0.3798 | 0.3669 | 0.1037 |
| `exp_001_eval_05B_d100_v5` | standard | 42 | 0.2322 | 0.3571 | 0.2270 | 0.0854 |
| `exp_001_eval_05B_d100_aligned` | aligned | 42 | null | null | null | null |
| `exp_001_eval_05B_d100_aligned_v3` | aligned | -- | null | null | null | null |
| `exp_001_eval_05B_d100` | standard | 42 | null | null | null | null |
| `exp_001_eval_05B_d100_v2` | standard | -- | null | null | null | null |

**Batch/special (0.5B)**
| exp_id | eval_type | seed | Description |
|--------|-----------|------|-------------|
| `exp_001_eval_05B_aligned_batch` | batch | 42 | Combined d000/d005 aligned + d000 para_aligned metrics in one entry |
| `exp_001_eval_05B_raw` | raw | 42 | Raw base model (no LoRA): MMLU=0.2302, GSM8K=0.1592, ARC=0.2261, HumanEval=incomplete |

**exp_008 baselines (0.5B)**
| exp_id | model | MMLU | GSM8K | ARC | HumanEval |
|--------|-------|------|-------|-----|-----------|
| `exp_008_base_pretrained_eval_v2` | Qwen2.5-0.5B (base) | 0.2294 | 0.1630 | 0.2278 | 0.0000 |
| `exp_008_instruct_05B_eval` | Qwen2.5-0.5B-Instruct | 0.2462 | 0.3882 | 0.2816 | 0.0000 |
| `exp_008_base_pretrained_eval` | Qwen2.5-0.5B (base) | null | null | null | null |

---

### 1.5B (Qwen2.5-1.5B) -- 17 experiments

**Dose 0%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_15B_d000_s123_aligned` | aligned | 123 | 0.5855 | 0.6535 | 0.7577 | 0.1707 |
| `exp_001_eval_15B_d000_s42_v2` | standard | 42 | 0.5753 | 0.6368 | 0.7756 | 0.1280 |
| `exp_001_eval_15B_d000_s123` | standard | 123 | 0.5762 | 0.6331 | 0.7662 | 0.1707 |
| `exp_001_eval_15B_d000_s42` | standard | 42 | null | null | null | null |

**Dose 5%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_15B_d005_aligned_v2` | aligned | 42 | 0.5852 | 0.6482 | 0.7688 | 0.2500 |
| `exp_001_eval_15B_d005_s123` | standard | 123 | 0.5869 | 0.6482 | 0.7568 | 0.2500 |
| `exp_001_eval_15B_d005_s123_v2` | standard | 123 | 0.5869 | 0.6482 | 0.7568 | 0.2500 |

**Dose 25%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_15B_d025_aligned` | aligned | -- | 0.5902 | 0.6535 | 0.7688 | 0.2256 |
| `exp_001_eval_15B_d025_para_aligned` | para_aligned | -- | 0.6180 | 0.5390 | 0.7660 | 0.1540 |
| `exp_001_eval_15B_d025_s123` | standard | 123 | 0.5881 | 0.6550 | 0.7577 | 0.2500 |
| `exp_001_eval_15B_d025_s123_v2` | standard | 123 | 0.5881 | 0.6550 | 0.7577 | 0.2500 |

**Dose 100%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_15B_d100_aligned` | aligned | 42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 |
| `exp_001_eval_15B_d100_s123_aligned` | aligned | 123 | 0.5956 | 0.6444 | 0.7816 | 0.2805 |
| `exp_001_eval_15B_d100_s42` | standard | 42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 |

**Batch/special (1.5B)**
| exp_id | Description |
|--------|-------------|
| `exp_001_eval_15B_aligned_batch` | Combined d000/d005/d100 x orig/para metrics. Key finding recorded: "MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination." |

**exp_008 baselines (1.5B)**
| exp_id | model | MMLU | GSM8K | ARC | HumanEval |
|--------|-------|------|-------|-----|-----------|
| `exp_008_base_pretrained_15B_eval_v2` | Qwen2.5-1.5B (base) | 0.2303 | 0.0053 | 0.2304 | 0.2317 |
| `exp_008_base_pretrained_15B_eval` | Qwen2.5-1.5B (base) | 0.2303 | 0.0053 | 0.2304 | 0.2317 |

---

### 3B (Qwen2.5-3B) -- 27 experiments

**Dose 0%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_3B_d000_aligned` | aligned | -- | 0.6340 | 0.1198 | 0.8276 | 0.1159 |
| `exp_001_eval_3B_d000_v2_aligned` | aligned | 42 | 0.6295 | 0.3525 | 0.8183 | 0.0976 |
| `exp_001_eval_3B_d000_s123_aligned` | aligned | 123 | 0.6332 | 0.1812 | 0.8328 | 0.0854 |
| `exp_001_eval_3B_d000_v2_s123_aligned` | aligned | 123 | 0.6314 | 0.2676 | 0.8259 | 0.0610 |
| `exp_001_eval_3B_d000_s42_para_aligned` | para_aligned | 42 | 0.6474 | 0.0482 | 0.8235 | 0.1154 |
| `exp_001_eval_3B_d000_v2_para_aligned_v2` | para_aligned | 42 | 0.6468 | 0.2895 | 0.8121 | 0.0385 |
| `exp_001_eval_3B_d000_v2_s123_para_aligned` | para_aligned | 123 | 0.6512 | 0.1491 | 0.8121 | 0.0385 |
| `exp_001_eval_3B_d000_v2_para_aligned` | para_aligned | 42 | 0.6468 (mmlu only) | -- | -- | -- |
| `exp_001_eval_3B_d000_v2_para_aligned_v3` | para_aligned | 42 | null | null | null | null |
| `exp_001_eval_3B_d000_s42` | standard | 42 | 0.6340 | 0.1170 | 0.8220 | 0.1160 |
| `exp_001_eval_3B_d000_s42_v3` | standard | 42 | 0.6340 | 0.1198 | 0.8276 | 0.1159 |
| `exp_001_eval_3B_d000_s123` | standard | 123 | 0.6362 | 0.1759 | 0.8294 | 0.0854 |

**Dose 5%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_3B_d005_aligned` | aligned | -- | 0.6340 | 0.2080 | 0.8290 | 0.1460 |
| `exp_001_eval_3B_d005_s42_aligned` | aligned | 42 | 0.6345 | 0.2077 | 0.8294 | 0.1463 |
| `exp_001_eval_3B_d005_s123_para_aligned` | para_aligned | 123 | 0.6461 | 0.5000 | 0.8192 | 0.0769 |

**Dose 25%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_3B_d025_v2_aligned` | aligned | 42 | 0.5998 | 0.6793 | 0.8276 | 0.0976 |
| `exp_001_eval_3B_d025_s123_aligned` | aligned | 123 | 0.6367 | 0.5254 | 0.8336 | 0.1585 |
| `exp_001_eval_3B_d025_v2_para_aligned` | para_aligned | 42 | 0.6210 | 0.5482 | 0.8106 | 0.1154 |
| `exp_001_eval_3B_d025_s123_para_aligned` | para_aligned | 123 | 0.6615 | 0.4254 | 0.8121 | 0.1538 |

**Dose 100%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_3B_d100_aligned` | aligned | 42 | 0.6417 | 0.6967 | 0.8396 | 0.1220 |
| `exp_001_eval_3B_d100_v2_aligned_v2` | aligned | 42 | 0.6320 | 0.7415 | 0.8242 | 0.1707 |
| `exp_001_eval_3B_d100_v2_s123_aligned` | aligned | 123 | 0.6319 | 0.7324 | 0.8311 | 0.1829 |
| `exp_001_eval_3B_d100_v2_aligned` | aligned | 42 | INVALID (PID died) | -- | -- | -- |
| `exp_001_eval_3B_d100_para_aligned` | para_aligned | -- | 0.6760 | 0.6140 | 0.8280 | -- |
| `exp_001_eval_3B_d100_s42_para_aligned` | para_aligned | 42 | 0.6590 | 0.5833 | 0.8092 | 0.1154 |
| `exp_001_eval_3B_d100_v2_para_aligned` | para_aligned | 42 | 0.6590 | 0.5833 | 0.8092 | 0.1154 |

**Special (3B)**
| exp_id | eval_type | seed | Description |
|--------|-----------|------|-------------|
| `exp_001_eval_3B_raw_gen` | raw | 0 | Raw base model gen: GSM8K=0.605, HumanEval=0.0 |

---

### Unknown scale (exp_008 baselines without scale in name)
| exp_id | model | MMLU | GSM8K | ARC | HumanEval |
|--------|-------|------|-------|-----|-----------|
| `exp_008_base_pretrained_eval_v2` | Qwen2.5-0.5B (base) | 0.2294 | 0.1630 | 0.2278 | 0.0000 |
| `exp_008_base_pretrained_eval` | Qwen2.5-0.5B (base) | null | null | null | null |

---

## Key Data Quality Notes

1. **9 experiments with null metrics**: `exp_001_eval_05B_d000_s42`, `exp_001_eval_05B_d000_s42_v7`, `exp_001_eval_05B_d100`, `exp_001_eval_05B_d100_v2`, `exp_001_eval_05B_d100_aligned`, `exp_001_eval_05B_d100_aligned_v3`, `exp_001_eval_15B_d000_s42`, `exp_001_eval_3B_d000_v2_para_aligned_v3`, `exp_008_base_pretrained_eval`

2. **1 INVALID entry**: `exp_001_eval_3B_d100_v2_aligned` -- metrics came from v1, v2 output dir was empty (PID 461879 died).

3. **Metric key inconsistency**: Some experiments use `mmlu`/`gsm8k`, others use `mmlu_accuracy`/`gsm8k_exact_match`, others use `MMLU`/`GSM8K`, and batch experiments use prefixed keys like `d000_aligned_mmlu`. Some report nested dicts with `{accuracy, correct, total}`.

4. **Multiple versions**: Many experiment conditions have v1/v2/v3+ reruns. The later versions typically supersede earlier ones (e.g., `_v2` fixing issues from `_v1`).

5. **exp_001_eval_05B_d025_aligned** metrics appear in percentage scale (28.03, 36.62, 32.51) rather than 0-1 scale.

6. **exp_001_eval_05B_d025_aligned_v2** has `format: paraphrased_aligned` in its metrics -- possibly mislabeled as "aligned" in the exp_id but actually para_aligned.

7. **3B GSM8K at dose 0% shows high variance**: ranges from 0.048 to 0.353 across different eval_types and versions, suggesting sensitivity to eval format.

8. **Batch experiments** (`exp_001_eval_15B_aligned_batch`, `exp_001_eval_05B_aligned_batch`) aggregate multiple dose x eval_type combinations into single entries and are the most reliable summaries for those scales.

agentId: aee0c4a84f025f3bb (use SendMessage with to: 'aee0c4a84f025f3bb' to continue this agent)
&lt;usage>total_tokens: 52371
tool_uses: 9
duration_ms: 140474&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "46ab1210-9257-432d-b60d-9dc2dee406e5",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Parse the large registry JSON file at `/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt` to extract eval experiment info.\n\nThe file is JSON with schema: {result: string} where result is itself a JSON string.\n\nSteps:\n1. Use `jq` to probe the structure\n2. Extract all experiments that have:\n   - type containing \"eval\" or task containing \"eval\"\n   - status = \"DONE\"\n3. For each eval experiment, extract: exp_id, name/description, metrics (if any), any fields about scale/dose/seed/benchmark\n\nReturn a structured summary of ALL eval experiments found, their metrics (if present), and any identifying info (scale, dose, seed, eval_type like aligned/para_aligned). Be thorough - I need every single eval experiment.\n\nThe project is contamcal-irt-calibration, studying LLM benchmark contamination calibration. Scales: 0.5B, 1.5B, 3B. Doses: 0%, 5%, 25%, 100%. Seeds: 42, 123. Benchmarks: MMLU, GSM8K, ARC-Challenge, HumanEval.",
    "agentId": "aee0c4a84f025f3bb",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete structured summary of all 69 eval experiments found in the registry.\n\n---\n\n## Overview\n\n- **Total eval experiments**: 69 (all status = DONE)\n- **With metrics**: 60\n- **Without metrics (null)**: 9\n- **With invalid/corrupt metrics**: 1 (`exp_001_eval_3B_d100_v2_aligned` -- PID died before completion)\n- **Series**: exp_001 (64 experiments, main contamination calibration), exp_008 (5 experiments, base/instruct pretrained baselines)\n\n---\n\n## By Scale\n\n### 0.5B (Qwen2.5-0.5B) -- 23 experiments\n\n**Dose 0% (baseline)**\n| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |\n|--------|-----------|------|------|-------|-----|-----------|\n| `exp_001_eval_05B_d000_s123_aligned` | aligned | 123 | 0.4216 | 0.3412 | 0.4974 | 0.1037 |\n| `exp_001_eval_05B_d000_s42_v5` | standard | 42 | 0.4049 | 0.3647 | 0.3780 | 0.1098 |\n| `exp_001_eval_05B_d000_s123` | standard | 123 | 0.4182 | 0.3404 | 0.3976 | 0.1037 |\n| `exp_001_eval_05B_d000_s42` | standard | 42 | null | null | null | null |\n| `exp_001_eval_05B_d000_s42_v7` | standard | 42 | null | null | null | null |\n\n**Dose 5%**\n| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |\n|--------|-----------|------|------|-------|-----|-----------|\n| `exp_001_eval_05B_d005_aligned` | aligned | 42 | 0.3255 | 0.3624 | 0.3285 | 0.0793 |\n| `exp_001_eval_05B_d005_s123_aligned` | aligned | 123 | 0.3002 | 0.3677 | 0.2978 | 0.0976 |\n| `exp_001_eval_05B_d005_para_aligned` | para_aligned | 42 | 0.3548 | 0.2588 | 0.3300 | 0.0000 |\n| `exp_001_eval_05B_d005_s123_para_aligned` | para_aligned | 123 | 0.3166 | 0.2939 | 0.2912 | 0.0000 |\n| `exp_001_eval_05B_d005` | standard | 42 | 0.2929 | 0.3601 | 0.2858 | 0.0793 |\n\n**Dose 25%**\n| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |\n|--------|-----------|------|------|-------|-----|-----------|\n| `exp_001_eval_05B_d025_aligned` | aligned | -- | 0.2803* | 0.3662* | 0.3251* | missing |\n| `exp_001_eval_05B_d025_aligned_v2` | aligned | 42 | 0.2835 | 0.3114 | 0.3199 | 0.1923 |\n| `exp_001_eval_05B_d025_s123_aligned` | aligned | 123 | 0.3473 | 0.3533 | 0.4061 | 0.0854 |\n\n(*v1 metrics appear to be in percentage scale 28.03/36.62/32.51 rather than 0-1; v2 note says \"paraphrased_aligned\" in format field which may be mislabeled)\n\n**Dose 100%**\n| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |\n|--------|-----------|------|------|-------|-----|-----------|\n| `exp_001_eval_05B_d100_aligned_v4` | aligned | 42 | 0.2334 | 0.3654 | 0.2944 | 0.0000 |\n| `exp_001_eval_05B_d100_s123_aligned` | aligned | 123 | 0.3058 | 0.3798 | 0.3669 | 0.1037 |\n| `exp_001_eval_05B_d100_v5` | standard | 42 | 0.2322 | 0.3571 | 0.2270 | 0.0854 |\n| `exp_001_eval_05B_d100_aligned` | aligned | 42 | null | null | null | null |\n| `exp_001_eval_05B_d100_aligned_v3` | aligned | -- | null | null | null | null |\n| `exp_001_eval_05B_d100` | standard | 42 | null | null | null | null |\n| `exp_001_eval_05B_d100_v2` | standard | -- | null | null | null | null |\n\n**Batch/special (0.5B)**\n| exp_id | eval_type | seed | Description |\n|--------|-----------|------|-------------|\n| `exp_001_eval_05B_aligned_batch` | batch | 42 | Combined d000/d005 aligned + d000 para_aligned metrics in one entry |\n| `exp_001_eval_05B_raw` | raw | 42 | Raw base model (no LoRA): MMLU=0.2302, GSM8K=0.1592, ARC=0.2261, HumanEval=incomplete |\n\n**exp_008 baselines (0.5B)**\n| exp_id | model | MMLU | GSM8K | ARC | HumanEval |\n|--------|-------|------|-------|-----|-----------|\n| `exp_008_base_pretrained_eval_v2` | Qwen2.5-0.5B (base) | 0.2294 | 0.1630 | 0.2278 | 0.0000 |\n| `exp_008_instruct_05B_eval` | Qwen2.5-0.5B-Instruct | 0.2462 | 0.3882 | 0.2816 | 0.0000 |\n| `exp_008_base_pretrained_eval` | Qwen2.5-0.5B (base) | null | null | null | null |\n\n---\n\n### 1.5B (Qwen2.5-1.5B) -- 17 experiments\n\n**Dose 0%**\n| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |\n|--------|-----------|------|------|-------|-----|-----------|\n| `exp_001_eval_15B_d000_s123_aligned` | aligned | 123 | 0.5855 | 0.6535 | 0.7577 | 0.1707 |\n| `exp_001_eval_15B_d000_s42_v2` | standard | 42 | 0.5753 | 0.6368 | 0.7756 | 0.1280 |\n| `exp_001_eval_15B_d000_s123` | standard | 123 | 0.5762 | 0.6331 | 0.7662 | 0.1707 |\n| `exp_001_eval_15B_d000_s42` | standard | 42 | null | null | null | null |\n\n**Dose 5%**\n| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |\n|--------|-----------|------|------|-------|-----|-----------|\n| `exp_001_eval_15B_d005_aligned_v2` | aligned | 42 | 0.5852 | 0.6482 | 0.7688 | 0.2500 |\n| `exp_001_eval_15B_d005_s123` | standard | 123 | 0.5869 | 0.6482 | 0.7568 | 0.2500 |\n| `exp_001_eval_15B_d005_s123_v2` | standard | 123 | 0.5869 | 0.6482 | 0.7568 | 0.2500 |\n\n**Dose 25%**\n| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |\n|--------|-----------|------|------|-------|-----|-----------|\n| `exp_001_eval_15B_d025_aligned` | aligned | -- | 0.5902 | 0.6535 | 0.7688 | 0.2256 |\n| `exp_001_eval_15B_d025_para_aligned` | para_aligned | -- | 0.6180 | 0.5390 | 0.7660 | 0.1540 |\n| `exp_001_eval_15B_d025_s123` | standard | 123 | 0.5881 | 0.6550 | 0.7577 | 0.2500 |\n| `exp_001_eval_15B_d025_s123_v2` | standard | 123 | 0.5881 | 0.6550 | 0.7577 | 0.2500 |\n\n**Dose 100%**\n| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |\n|--------|-----------|------|------|-------|-----|-----------|\n| `exp_001_eval_15B_d100_aligned` | aligned | 42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 |\n| `exp_001_eval_15B_d100_s123_aligned` | aligned | 123 | 0.5956 | 0.6444 | 0.7816 | 0.2805 |\n| `exp_001_eval_15B_d100_s42` | standard | 42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 |\n\n**Batch/special (1.5B)**\n| exp_id | Description |\n|--------|-------------|\n| `exp_001_eval_15B_aligned_batch` | Combined d000/d005/d100 x orig/para metrics. Key finding recorded: \"MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination.\" |\n\n**exp_008 baselines (1.5B)**\n| exp_id | model | MMLU | GSM8K | ARC | HumanEval |\n|--------|-------|------|-------|-----|-----------|\n| `exp_008_base_pretrained_15B_eval_v2` | Qwen2.5-1.5B (base) | 0.2303 | 0.0053 | 0.2304 | 0.2317 |\n| `exp_008_base_pretrained_15B_eval` | Qwen2.5-1.5B (base) | 0.2303 | 0.0053 | 0.2304 | 0.2317 |\n\n---\n\n### 3B (Qwen2.5-3B) -- 27 experiments\n\n**Dose 0%**\n| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |\n|--------|-----------|------|------|-------|-----|-----------|\n| `exp_001_eval_3B_d000_aligned` | aligned | -- | 0.6340 | 0.1198 | 0.8276 | 0.1159 |\n| `exp_001_eval_3B_d000_v2_aligned` | aligned | 42 | 0.6295 | 0.3525 | 0.8183 | 0.0976 |\n| `exp_001_eval_3B_d000_s123_aligned` | aligned | 123 | 0.6332 | 0.1812 | 0.8328 | 0.0854 |\n| `exp_001_eval_3B_d000_v2_s123_aligned` | aligned | 123 | 0.6314 | 0.2676 | 0.8259 | 0.0610 |\n| `exp_001_eval_3B_d000_s42_para_aligned` | para_aligned | 42 | 0.6474 | 0.0482 | 0.8235 | 0.1154 |\n| `exp_001_eval_3B_d000_v2_para_aligned_v2` | para_aligned | 42 | 0.6468 | 0.2895 | 0.8121 | 0.0385 |\n| `exp_001_eval_3B_d000_v2_s123_para_aligned` | para_aligned | 123 | 0.6512 | 0.1491 | 0.8121 | 0.0385 |\n| `exp_001_eval_3B_d000_v2_para_aligned` | para_aligned | 42 | 0.6468 (mmlu only) | -- | -- | -- |\n| `exp_001_eval_3B_d000_v2_para_aligned_v3` | para_aligned | 42 | null | null | null | null |\n| `exp_001_eval_3B_d000_s42` | standard | 42 | 0.6340 | 0.1170 | 0.8220 | 0.1160 |\n| `exp_001_eval_3B_d000_s42_v3` | standard | 42 | 0.6340 | 0.1198 | 0.8276 | 0.1159 |\n| `exp_001_eval_3B_d000_s123` | standard | 123 | 0.6362 | 0.1759 | 0.8294 | 0.0854 |\n\n**Dose 5%**\n| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |\n|--------|-----------|------|------|-------|-----|-----------|\n| `exp_001_eval_3B_d005_aligned` | aligned | -- | 0.6340 | 0.2080 | 0.8290 | 0.1460 |\n| `exp_001_eval_3B_d005_s42_aligned` | aligned | 42 | 0.6345 | 0.2077 | 0.8294 | 0.1463 |\n| `exp_001_eval_3B_d005_s123_para_aligned` | para_aligned | 123 | 0.6461 | 0.5000 | 0.8192 | 0.0769 |\n\n**Dose 25%**\n| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |\n|--------|-----------|------|------|-------|-----|-----------|\n| `exp_001_eval_3B_d025_v2_aligned` | aligned | 42 | 0.5998 | 0.6793 | 0.8276 | 0.0976 |\n| `exp_001_eval_3B_d025_s123_aligned` | aligned | 123 | 0.6367 | 0.5254 | 0.8336 | 0.1585 |\n| `exp_001_eval_3B_d025_v2_para_aligned` | para_aligned | 42 | 0.6210 | 0.5482 | 0.8106 | 0.1154 |\n| `exp_001_eval_3B_d025_s123_para_aligned` | para_aligned | 123 | 0.6615 | 0.4254 | 0.8121 | 0.1538 |\n\n**Dose 100%**\n| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |\n|--------|-----------|------|------|-------|-----|-----------|\n| `exp_001_eval_3B_d100_aligned` | aligned | 42 | 0.6417 | 0.6967 | 0.8396 | 0.1220 |\n| `exp_001_eval_3B_d100_v2_aligned_v2` | aligned | 42 | 0.6320 | 0.7415 | 0.8242 | 0.1707 |\n| `exp_001_eval_3B_d100_v2_s123_aligned` | aligned | 123 | 0.6319 | 0.7324 | 0.8311 | 0.1829 |\n| `exp_001_eval_3B_d100_v2_aligned` | aligned | 42 | INVALID (PID died) | -- | -- | -- |\n| `exp_001_eval_3B_d100_para_aligned` | para_aligned | -- | 0.6760 | 0.6140 | 0.8280 | -- |\n| `exp_001_eval_3B_d100_s42_para_aligned` | para_aligned | 42 | 0.6590 | 0.5833 | 0.8092 | 0.1154 |\n| `exp_001_eval_3B_d100_v2_para_aligned` | para_aligned | 42 | 0.6590 | 0.5833 | 0.8092 | 0.1154 |\n\n**Special (3B)**\n| exp_id | eval_type | seed | Description |\n|--------|-----------|------|-------------|\n| `exp_001_eval_3B_raw_gen` | raw | 0 | Raw base model gen: GSM8K=0.605, HumanEval=0.0 |\n\n---\n\n### Unknown scale (exp_008 baselines without scale in name)\n| exp_id | model | MMLU | GSM8K | ARC | HumanEval |\n|--------|-------|------|-------|-----|-----------|\n| `exp_008_base_pretrained_eval_v2` | Qwen2.5-0.5B (base) | 0.2294 | 0.1630 | 0.2278 | 0.0000 |\n| `exp_008_base_pretrained_eval` | Qwen2.5-0.5B (base) | null | null | null | null |\n\n---\n\n## Key Data Quality Notes\n\n1. **9 experiments with null metrics**: `exp_001_eval_05B_d000_s42`, `exp_001_eval_05B_d000_s42_v7`, `exp_001_eval_05B_d100`, `exp_001_eval_05B_d100_v2`, `exp_001_eval_05B_d100_aligned`, `exp_001_eval_05B_d100_aligned_v3`, `exp_001_eval_15B_d000_s42`, `exp_001_eval_3B_d000_v2_para_aligned_v3`, `exp_008_base_pretrained_eval`\n\n2. **1 INVALID entry**: `exp_001_eval_3B_d100_v2_aligned` -- metrics came from v1, v2 output dir was empty (PID 461879 died).\n\n3. **Metric key inconsistency**: Some experiments use `mmlu`/`gsm8k`, others use `mmlu_accuracy`/`gsm8k_exact_match`, others use `MMLU`/`GSM8K`, and batch experiments use prefixed keys like `d000_aligned_mmlu`. Some report nested dicts with `{accuracy, correct, total}`.\n\n4. **Multiple versions**: Many experiment conditions have v1/v2/v3+ reruns. The later versions typically supersede earlier ones (e.g., `_v2` fixing issues from `_v1`).\n\n5. **exp_001_eval_05B_d025_aligned** metrics appear in percentage scale (28.03, 36.62, 32.51) rather than 0-1 scale.\n\n6. **exp_001_eval_05B_d025_aligned_v2** has `format: paraphrased_aligned` in its metrics -- possibly mislabeled as \"aligned\" in the exp_id but actually para_aligned.\n\n7. **3B GSM8K at dose 0% shows high variance**: ranges from 0.048 to 0.353 across different eval_types and versions, suggesting sensitivity to eval format.\n\n8. **Batch experiments** (`exp_001_eval_15B_aligned_batch`, `exp_001_eval_05B_aligned_batch`) aggregate multiple dose x eval_type combinations into single entries and are the most reliable summaries for those scales."
      }
    ],
    "totalDurationMs": 140474,
    "totalTokens": 52371,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 46206,
      "output_tokens": 5479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5479,
          "cache_read_input_tokens": 46206,
          "cache_creation_input_tokens": 685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 685,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 8,
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

_source line 48 · 2026-05-15T18:28:17.910Z_

<details><summary>↩ Tool result · `toolu_01EaB5R2mMNWpxgDjczaqN8K`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "689ec884-e5c1-4af2-b1e4-473188c189ba",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
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
The find command for results.json with "aligned" returned nothing. Let me find the actual structure of results.json files. Let me search more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "8be54ffc-301e-43c9-bd60-7a0210b2478c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXhWqSjD4wFPDqPsTeSHk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6966,
      "cache_read_input_tokens": 29170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6966
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

The find command returned empty — let me check the actual file structure inside eval result directories.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "648c2e78-f5ce-4e1c-b155-159fb2086985",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXhWqSjD4wFPDqPsTeSHk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6966,
      "cache_read_input_tokens": 29170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6966
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EAgbXs9eV3RRSdTfzPRrrA`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/ -name \"results.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "e1228fa6-1e41-4d0c-b192-534b548a3ac8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXhWqSjD4wFPDqPsTeSHk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6966,
      "cache_read_input_tokens": 29170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6966
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

_source line 52 · 2026-05-15T18:28:24.066Z_

<details><summary>↩ Tool result · `toolu_01EAgbXs9eV3RRSdTfzPRrrA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "2c1852f7-0dea-4ed6-ae08-485b5a815476",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KanLoyiBVfj7tid9qqKfaS`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_aligned/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "8c467954-f8c3-4e0b-b757-9c8890a7762f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXhWqSjD4wFPDqPsTeSHk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6966,
      "cache_read_input_tokens": 29170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6966
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

_source line 54 · 2026-05-15T18:28:24.741Z_

<details><summary>↩ Tool result · `toolu_01KanLoyiBVfj7tid9qqKfaS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"correctness_matrix.json\\neval_results.json\\nitem_responses.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "f5239ed5-b40b-4a8b-bdcd-6974a9b26261",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"correctness_matrix.json\\\\neval_results.json\\\\nitem_responses.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"correctness_matrix.json\\neval_results.json\\nitem_responses.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
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
The files are `eval_results.json`, not `results.json`. Let me check the structure of eval_results.json files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "f4fcefc2-9a8a-4d28-ae5c-ef9d1e3c4a44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yNkZqvASCGdayv6BX3UYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 36136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 613
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

Files are `eval_results.json`, not `results.json`. Let me check their structure and collect all metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "0de06137-79aa-410a-a5e6-09f662b2f76e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yNkZqvASCGdayv6BX3UYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 36136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 613
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XmvzeAkRfh7RJj7wGwFvii`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "49dc1424-c58d-4c64-9aa6-d428248af448",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yNkZqvASCGdayv6BX3UYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 36136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 613
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

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Nhjvob5mvys7htk1REcqum`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/ -name \"eval_results.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "843b41ae-7b43-44ef-83e2-77dc76329068",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yNkZqvASCGdayv6BX3UYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 36136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 613
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

_source line 59 · 2026-05-15T18:28:34.483Z_

<details><summary>↩ Tool result · `toolu_01XmvzeAkRfh7RJj7wGwFvii`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B\\\",\\n  \\\"paraphrased\\\": false,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.39787779518587096,\\n      \\\"correct\\\": 5587,\\n      \\\"total\\\": 14042,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 0,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 1,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 2,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 3,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 4,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 5,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 7,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 8,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 10,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 11,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 12,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 13,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 14,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 15,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 16,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 17,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 18,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 19,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 20,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 21,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 22,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 23,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 24,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 25,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 26,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 27,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 28,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 29,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 30,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 31,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 32,\\n          \\\"corr\\n\\n... [截断: 输出过长，省略 2063217 字符] ...\\n\\n\\n        },\\n        {\\n          \\\"task_id\\\": \\\"HumanEval/158\\\",\\n          \\\"index\\\": 158,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def find_max(words):\\\\n    max_word = \\\\\\\"\\\\\\\"\\\\n    max_count = 0\\\\n\\\\n    for word in words:\\\\n        count = len(set(word))\\\\n        if count > max_count:\\\\n            max_word = word\\\\n            max_count = count\\\\n\\\\n    return max_word\\\\n\\\\n# Test cases\\\\nprint(find_max([\\\\\\\"name\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"string\\\\\\\"]))  # Output: \\\\\\\"string\\\\\\\"\\\\nprint(find_max([\\\\\\\"name\\\\\\\", \\\\\\\"enam\\\\\\\", \\\\\\\"game\\\\\\\"]))  # Output: \\\\\\\"enam\\\\\\\"\\\\nprint(find_max([\\\\\\\"aaaaaaa\\\\\\\", \\\\\\\"bb\\\\\\\" ,\\\\\\\"cc\\\\\\\"]))  # Output: \\\\\\\"\\\\\\\"aaaaaaa\\\\\\\"różni\\\\nprint(find_max([\\\\\\\"a\\\\\\\", \\\\\\\"b\\\\\\\", \\\\\\\"c\\\\\\\", \\\\\\\"d\\\\\\\", \\\\\\\"e\\\\\\\", \\\\\\\"f\\\\\\\", \\\\\\\"g\\\\\\\", \\\\\\\"h\\\\\\\", \\\\\\\"i\\\\\\\", \\\\\\\"j\\\\\\\", \\\\\\\"k\\\\\\\", \\\\\\\"l\\\\\\\",\\\"\\n        },\\n        {\\n          \\\"task_id\\\": \\\"HumanEval/159\\\",\\n          \\\"index\\\": 159,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def eat(number, need, remaining):\\\\n    if number >= need:\\\\n        total_eaten = number + remaining\\\\n        remaining = 0\\\\n    else:\\\\n        total_eaten = number + remaining\\\\n        remaining = number\\\\n    return [total_eaten, remaining] if remaining >= 0 else [total_eaten, remaining] + [0] * (remaining < 0) if remaining < 0 else [total_eaten, remaining] + [0] * (remaining < 0) if remaining < 0 else [total_eaten, remaining] + [0] * (remaining < 0) if remaining < 0 else [total_eaten, remaining] + [0]\\\"\\n        },\\n        {\\n          \\\"task_id\\\": \\\"HumanEval/160\\\",\\n          \\\"index\\\": 160,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def do_algebra(operator, operand):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    Given two lists operator, and operand. The first list has basic algebra operations, and \\\\n    the second list is a list of integers. Use the two given lists to build the algebric \\\\n    expression and return the evaluation of this expression.\\\\n\\\\n    The basic algebra operations:\\\\n    Addition ( + ) \\\\n    Subtraction ( - ) \\\\n    Multiplication ( * ) \\\\n    Floor division ( // ) \\\\n    Exponentiation ( ** ) \\\\n\\\\n    Example:\\\\n    operator['+', '*', '-']\\\\n    array = [\\\"\\n        },\\n        {\\n          \\\"task_id\\\": \\\"HumanEval/161\\\",\\n          \\\"index\\\": 161,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def solve(s):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"You are given a string s.\\\\n    if s[i] is a letter, reverse its case from lower to upper or vise versa, \\\\n    otherwise keep it as it is.\\\\n    If the string contains no letters, reverse the string.\\\\n    The function should return the resulted string.\\\\n    Examples\\\\n    solve(\\\\\\\"1234\\\\\\\") = \\\\\\\"4321\\\\\\\"\\\\n    solve(\\\\\\\"ab\\\\\\\") = \\\\\\\"AB\\\\\\\"\\\\n    solve(\\\\\\\"#a@C\\\\\\\") = \\\\\\\"#A@c\\\\\\\"\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    if s.isalpha():\\\\n        return s[::-1]\\\\n    else:\\\\n        return s.lower() + s.upper() + s.lower() + s.upper() + s.lower() + s.uppe\\\"\\n        },\\n        {\\n          \\\"task_id\\\": \\\"HumanEval/162\\\",\\n          \\\"index\\\": 162,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def string_to_md5(text):\\\\n    if text == \\\\\\\"\\\\\\\":\\\\n        return None\\\\n    return hashlib.md5(text.encode()).hexdigest() or None\\\\n\\\\n# Example usage:\\\\nprint(string_to_md5('Hello world'))  # Output: 3e25960a79dbc69b674cd4ec67a72c62\\\\nprint(string_to_md5(''))  # Output: None\\\\nprint(string_to_md5(''))  # Output: None\\\\nprint(string_to_md5('Hello'))  # Output: 3e25960a79dbc69b674cd4ec67a72c62\\\\nprint(string_to_md5('1234567890'))  # Output: None\\\\nprint(string_to_md5(''))  # Output: None\\\\nprint(string_to_md5('Hello World\\\"\\n        },\\n        {\\n          \\\"task_id\\\": \\\"HumanEval/163\\\",\\n          \\\"index\\\": 163,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def generate_integers(a, b):\\\\n    even_digits = []\\\\n    for num in range(a, b + 1):\\\\n        if num % 2 == 0:\\\\n            even_digits.append(num)\\\\n    return even_digits\\\\n\\\\n# Test cases\\\\nprint(generate_integers(2, 8))  # [2, 4, 6, 8]\\\\nprint(generate_integers(8, 2))  # [2, 4, 6, 8]\\\\nprint(generate_integers(10, 14))  # [] (since 10 is not even) or [10, 12, 14] (since 12 and 14 are even) or [10, 12, 14] (since 10 is not even) or [10, 12, 14] (since 10 is not even) or [10, 12, 14] (since 10 is not even) or [\\\"\\n        }\\n      ]\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.74}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "f3f8baf9-3118-4c0e-98f3-0b0631793927",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"model_path\\\\\\\": \\\\\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B\\\\\\\",\\\\n  \\\\\\\"paraphrased\\\\\\\": false,\\\\n  \\\\\\\"benchmarks\\\\\\\": {\\\\n    \\\\\\\"mmlu\\\\\\\": {\\\\n      \\\\\\\"accuracy\\\\\\\": 0.39787779518587096,\\\\n      \\\\\\\"correct\\\\\\\": 5587,\\\\n      \\\\\\\"total\\\\\\\": 14042,\\\\n      \\\\\\\"per_item\\\\\\\": [\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 0,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"B\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 1,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"C\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 2,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"D\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 3,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"B\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 4,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"B\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 5,\\\\n          \\\\\\\"correct\\\\\\\": true,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"A\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 6,\\\\n          \\\\\\\"correct\\\\\\\": true,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"A\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 7,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"D\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 8,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"B\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 9,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"C\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 10,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"C\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 11,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"C\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 12,\\\\n          \\\\\\\"correct\\\\\\\": true,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"A\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 13,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"C\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 14,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"C\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 15,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"B\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 16,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"C\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 17,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"C\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 18,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"D\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 19,\\\\n          \\\\\\\"correct\\\\\\\": true,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"A\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 20,\\\\n          \\\\\\\"correct\\\\\\\": true,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"A\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 21,\\\\n          \\\\\\\"correct\\\\\\\": true,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"A\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 22,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"D\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 23,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"D\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 24,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"B\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 25,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"C\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 26,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"C\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 27,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"B\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 28,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"D\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 29,\\\\n          \\\\\\\"correct\\\\\\\": true,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"A\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 30,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"A\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"B\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 31,\\\\n          \\\\\\\"correct\\\\\\\": true,\\\\n          \\\\\\\"pred\\\\\\\": \\\\\\\"B\\\\\\\",\\\\n          \\\\\\\"gold\\\\\\\": \\\\\\\"B\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"index\\\\\\\": 32,\\\\n          \\\\\\\"corr\\\\n\\\\n... [截断: 输出过长，省略 2063217 字符] ...\\\\n\\\\n\\\\n        },\\\\n        {\\\\n          \\\\\\\"task_id\\\\\\\": \\\\\\\"HumanEval/158\\\\\\\",\\\\n          \\\\\\\"index\\\\\\\": 158,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"generated\\\\\\\": \\\\\\\"def find_max(words):\\\\\\\\n    max_word = \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\n    max_count = 0\\\\\\\\n\\\\\\\\n    for word in words:\\\\\\\\n        count = len(set(word))\\\\\\\\n        if count > max_count:\\\\\\\\n            max_word = word\\\\\\\\n            max_count = count\\\\\\\\n\\\\\\\\n    return max_word\\\\\\\\n\\\\\\\\n# Test cases\\\\\\\\nprint(find_max([\\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"of\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"string\\\\\\\\\\\\\\\"]))  # Output: \\\\\\\\\\\\\\\"string\\\\\\\\\\\\\\\"\\\\\\\\nprint(find_max([\\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"enam\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"game\\\\\\\\\\\\\\\"]))  # Output: \\\\\\\\\\\\\\\"enam\\\\\\\\\\\\\\\"\\\\\\\\nprint(find_max([\\\\\\\\\\\\\\\"aaaaaaa\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"bb\\\\\\\\\\\\\\\" ,\\\\\\\\\\\\\\\"cc\\\\\\\\\\\\\\\"]))  # Output: \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"aaaaaaa\\\\\\\\\\\\\\\"różni\\\\\\\\nprint(find_max([\\\\\\\\\\\\\\\"a\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"b\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"c\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"d\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"e\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"f\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"g\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"h\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"i\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"j\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"k\\\\\\\\\\\\\\\", \\\\\\\\\\\\\\\"l\\\\\\\\\\\\\\\",\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"task_id\\\\\\\": \\\\\\\"HumanEval/159\\\\\\\",\\\\n          \\\\\\\"index\\\\\\\": 159,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"generated\\\\\\\": \\\\\\\"def eat(number, need, remaining):\\\\\\\\n    if number >= need:\\\\\\\\n        total_eaten = number + remaining\\\\\\\\n        remaining = 0\\\\\\\\n    else:\\\\\\\\n        total_eaten = number + remaining\\\\\\\\n        remaining = number\\\\\\\\n    return [total_eaten, remaining] if remaining >= 0 else [total_eaten, remaining] + [0] * (remaining < 0) if remaining < 0 else [total_eaten, remaining] + [0] * (remaining < 0) if remaining < 0 else [total_eaten, remaining] + [0] * (remaining < 0) if remaining < 0 else [total_eaten, remaining] + [0]\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"task_id\\\\\\\": \\\\\\\"HumanEval/160\\\\\\\",\\\\n          \\\\\\\"index\\\\\\\": 160,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"generated\\\\\\\": \\\\\\\"def do_algebra(operator, operand):\\\\\\\\n    \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\n    Given two lists operator, and operand. The first list has basic algebra operations, and \\\\\\\\n    the second list is a list of integers. Use the two given lists to build the algebric \\\\\\\\n    expression and return the evaluation of this expression.\\\\\\\\n\\\\\\\\n    The basic algebra operations:\\\\\\\\n    Addition ( + ) \\\\\\\\n    Subtraction ( - ) \\\\\\\\n    Multiplication ( * ) \\\\\\\\n    Floor division ( // ) \\\\\\\\n    Exponentiation ( ** ) \\\\\\\\n\\\\\\\\n    Example:\\\\\\\\n    operator['+', '*', '-']\\\\\\\\n    array = [\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"task_id\\\\\\\": \\\\\\\"HumanEval/161\\\\\\\",\\\\n          \\\\\\\"index\\\\\\\": 161,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"generated\\\\\\\": \\\\\\\"def solve(s):\\\\\\\\n    \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"You are given a string s.\\\\\\\\n    if s[i] is a letter, reverse its case from lower to upper or vise versa, \\\\\\\\n    otherwise keep it as it is.\\\\\\\\n    If the string contains no letters, reverse the string.\\\\\\\\n    The function should return the resulted string.\\\\\\\\n    Examples\\\\\\\\n    solve(\\\\\\\\\\\\\\\"1234\\\\\\\\\\\\\\\") = \\\\\\\\\\\\\\\"4321\\\\\\\\\\\\\\\"\\\\\\\\n    solve(\\\\\\\\\\\\\\\"ab\\\\\\\\\\\\\\\") = \\\\\\\\\\\\\\\"AB\\\\\\\\\\\\\\\"\\\\\\\\n    solve(\\\\\\\\\\\\\\\"#a@C\\\\\\\\\\\\\\\") = \\\\\\\\\\\\\\\"#A@c\\\\\\\\\\\\\\\"\\\\\\\\n    \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\n    if s.isalpha():\\\\\\\\n        return s[::-1]\\\\\\\\n    else:\\\\\\\\n        return s.lower() + s.upper() + s.lower() + s.upper() + s.lower() + s.uppe\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"task_id\\\\\\\": \\\\\\\"HumanEval/162\\\\\\\",\\\\n          \\\\\\\"index\\\\\\\": 162,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"generated\\\\\\\": \\\\\\\"def string_to_md5(text):\\\\\\\\n    if text == \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\":\\\\\\\\n        return None\\\\\\\\n    return hashlib.md5(text.encode()).hexdigest() or None\\\\\\\\n\\\\\\\\n# Example usage:\\\\\\\\nprint(string_to_md5('Hello world'))  # Output: 3e25960a79dbc69b674cd4ec67a72c62\\\\\\\\nprint(string_to_md5(''))  # Output: None\\\\\\\\nprint(string_to_md5(''))  # Output: None\\\\\\\\nprint(string_to_md5('Hello'))  # Output: 3e25960a79dbc69b674cd4ec67a72c62\\\\\\\\nprint(string_to_md5('1234567890'))  # Output: None\\\\\\\\nprint(string_to_md5(''))  # Output: None\\\\\\\\nprint(string_to_md5('Hello World\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"task_id\\\\\\\": \\\\\\\"HumanEval/163\\\\\\\",\\\\n          \\\\\\\"index\\\\\\\": 163,\\\\n          \\\\\\\"correct\\\\\\\": false,\\\\n          \\\\\\\"generated\\\\\\\": \\\\\\\"def generate_integers(a, b):\\\\\\\\n    even_digits = []\\\\\\\\n    for num in range(a, b + 1):\\\\\\\\n        if num % 2 == 0:\\\\\\\\n            even_digits.append(num)\\\\\\\\n    return even_digits\\\\\\\\n\\\\\\\\n# Test cases\\\\\\\\nprint(generate_integers(2, 8))  # [2, 4, 6, 8]\\\\\\\\nprint(generate_integers(8, 2))  # [2, 4, 6, 8]\\\\\\\\nprint(generate_integers(10, 14))  # [] (since 10 is not even) or [10, 12, 14] (since 12 and 14 are even) or [10, 12, 14] (since 10 is not even) or [10, 12, 14] (since 10 is not even) or [10, 12, 14] (since 10 is not even) or [\\\\\\\"\\\\n        }\\\\n      ]\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.74}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B\\\",\\n  \\\"paraphrased\\\": false,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.39787779518587096,\\n      \\\"correct\\\": 5587,\\n      \\\"total\\\": 14042,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 0,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 1,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 2,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 3,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 4,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 5,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 7,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 8,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 10,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 11,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 12,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 13,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 14,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 15,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 16,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 17,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 18,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 19,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 20,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 21,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 22,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 23,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 24,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 25,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 26,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 27,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 28,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 29,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 30,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 31,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 32,\\n          \\\"corr\\n\\n... [截断: 输出过长，省略 2063217 字符] ...\\n\\n\\n        },\\n        {\\n          \\\"task_id\\\": \\\"HumanEval/158\\\",\\n          \\\"index\\\": 158,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def find_max(words):\\\\n    max_word = \\\\\\\"\\\\\\\"\\\\n    max_count = 0\\\\n\\\\n    for word in words:\\\\n        count = len(set(word))\\\\n        if count > max_count:\\\\n            max_word = word\\\\n            max_count = count\\\\n\\\\n    return max_word\\\\n\\\\n# Test cases\\\\nprint(find_max([\\\\\\\"name\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"string\\\\\\\"]))  # Output: \\\\\\\"string\\\\\\\"\\\\nprint(find_max([\\\\\\\"name\\\\\\\", \\\\\\\"enam\\\\\\\", \\\\\\\"game\\\\\\\"]))  # Output: \\\\\\\"enam\\\\\\\"\\\\nprint(find_max([\\\\\\\"aaaaaaa\\\\\\\", \\\\\\\"bb\\\\\\\" ,\\\\\\\"cc\\\\\\\"]))  # Output: \\\\\\\"\\\\\\\"aaaaaaa\\\\\\\"różni\\\\nprint(find_max([\\\\\\\"a\\\\\\\", \\\\\\\"b\\\\\\\", \\\\\\\"c\\\\\\\", \\\\\\\"d\\\\\\\", \\\\\\\"e\\\\\\\", \\\\\\\"f\\\\\\\", \\\\\\\"g\\\\\\\", \\\\\\\"h\\\\\\\", \\\\\\\"i\\\\\\\", \\\\\\\"j\\\\\\\", \\\\\\\"k\\\\\\\", \\\\\\\"l\\\\\\\",\\\"\\n        },\\n        {\\n          \\\"task_id\\\": \\\"HumanEval/159\\\",\\n          \\\"index\\\": 159,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def eat(number, need, remaining):\\\\n    if number >= need:\\\\n        total_eaten = number + remaining\\\\n        remaining = 0\\\\n    else:\\\\n        total_eaten = number + remaining\\\\n        remaining = number\\\\n    return [total_eaten, remaining] if remaining >= 0 else [total_eaten, remaining] + [0] * (remaining < 0) if remaining < 0 else [total_eaten, remaining] + [0] * (remaining < 0) if remaining < 0 else [total_eaten, remaining] + [0] * (remaining < 0) if remaining < 0 else [total_eaten, remaining] + [0]\\\"\\n        },\\n        {\\n          \\\"task_id\\\": \\\"HumanEval/160\\\",\\n          \\\"index\\\": 160,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def do_algebra(operator, operand):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    Given two lists operator, and operand. The first list has basic algebra operations, and \\\\n    the second list is a list of integers. Use the two given lists to build the algebric \\\\n    expression and return the evaluation of this expression.\\\\n\\\\n    The basic algebra operations:\\\\n    Addition ( + ) \\\\n    Subtraction ( - ) \\\\n    Multiplication ( * ) \\\\n    Floor division ( // ) \\\\n    Exponentiation ( ** ) \\\\n\\\\n    Example:\\\\n    operator['+', '*', '-']\\\\n    array = [\\\"\\n        },\\n        {\\n          \\\"task_id\\\": \\\"HumanEval/161\\\",\\n          \\\"index\\\": 161,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def solve(s):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"You are given a string s.\\\\n    if s[i] is a letter, reverse its case from lower to upper or vise versa, \\\\n    otherwise keep it as it is.\\\\n    If the string contains no letters, reverse the string.\\\\n    The function should return the resulted string.\\\\n    Examples\\\\n    solve(\\\\\\\"1234\\\\\\\") = \\\\\\\"4321\\\\\\\"\\\\n    solve(\\\\\\\"ab\\\\\\\") = \\\\\\\"AB\\\\\\\"\\\\n    solve(\\\\\\\"#a@C\\\\\\\") = \\\\\\\"#A@c\\\\\\\"\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    if s.isalpha():\\\\n        return s[::-1]\\\\n    else:\\\\n        return s.lower() + s.upper() + s.lower() + s.upper() + s.lower() + s.uppe\\\"\\n        },\\n        {\\n          \\\"task_id\\\": \\\"HumanEval/162\\\",\\n          \\\"index\\\": 162,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def string_to_md5(text):\\\\n    if text == \\\\\\\"\\\\\\\":\\\\n        return None\\\\n    return hashlib.md5(text.encode()).hexdigest() or None\\\\n\\\\n# Example usage:\\\\nprint(string_to_md5('Hello world'))  # Output: 3e25960a79dbc69b674cd4ec67a72c62\\\\nprint(string_to_md5(''))  # Output: None\\\\nprint(string_to_md5(''))  # Output: None\\\\nprint(string_to_md5('Hello'))  # Output: 3e25960a79dbc69b674cd4ec67a72c62\\\\nprint(string_to_md5('1234567890'))  # Output: None\\\\nprint(string_to_md5(''))  # Output: None\\\\nprint(string_to_md5('Hello World\\\"\\n        },\\n        {\\n          \\\"task_id\\\": \\\"HumanEval/163\\\",\\n          \\\"index\\\": 163,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def generate_integers(a, b):\\\\n    even_digits = []\\\\n    for num in range(a, b + 1):\\\\n        if num % 2 == 0:\\\\n            even_digits.append(num)\\\\n    return even_digits\\\\n\\\\n# Test cases\\\\nprint(generate_integers(2, 8))  # [2, 4, 6, 8]\\\\nprint(generate_integers(8, 2))  # [2, 4, 6, 8]\\\\nprint(generate_integers(10, 14))  # [] (since 10 is not even) or [10, 12, 14] (since 12 and 14 are even) or [10, 12, 14] (since 10 is not even) or [10, 12, 14] (since 10 is not even) or [10, 12, 14] (since 10 is not even) or [\\\"\\n        }\\n      ]\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.74}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T18:28:34.961Z_

<details><summary>↩ Tool result · `toolu_01Nhjvob5mvys7htk1REcqum`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v3/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s42_aligned_DEPRECATED/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_v1_s42_aligned_DEPRECATED/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v1_s42_aligned_DEPRECATED/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s123_DEPRECATED/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_v2/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_para_aligned/eval_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "0d907e82-aba7-437b-b12d-0063d0f3e28b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s123_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v3/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s42_aligned_DEPRECATED/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_v1_s42_aligned_DEPRECATED/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v1_s42_aligned_DEPRECATED/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s123_DEPRECATED/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_v2/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s123_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_para_aligned/eval_results.json\\\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_para_aligned/eval_results.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v3/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s42_aligned_DEPRECATED/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_v1_s42_aligned_DEPRECATED/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v1_s42_aligned_DEPRECATED/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s123_DEPRECATED/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_v2/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_para_aligned/eval_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
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
Now I know the structure. Each eval_results.json has:
- `model_path`
- `paraphrased`: bool
- `benchmarks`: {mmlu: {accuracy, correct, total, per_item}, gsm8k: {...}, arc_challenge: {...}, humaneval: {...}}

The per_item data is very large. I need to extract just the accuracy values. Let me write a Python script to run on the server that will:
1. Scan all eval_results directories
2. Extract accuracy from each benchmark
3. Output a compact JSON summary

This is much more efficient than reading each file individually. But wait, I need to use ssh_execute for running a python script. 

Actually, I can use ssh_read_only with `python3 -c` since it's a read-only operation. Let me write a compact Python one-liner to extract all metrics. I have about 60 eval_results.json files to process, so I'll need to handle that efficiently. But I should be careful about which directories to include—I want to exclude the DEPRECATED ones and the baseline models like raw, base_pretrained, and Instruct variants, focusing only on the dose-response study data.

Writing extraction script...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "ed92a354-43dc-45a0-b685-69669a1897c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UoAABWRy7SyojsyxBYFXCr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7347,
      "cache_read_input_tokens": 36749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7347
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

Now I'll extract all metrics at once with a Python script on the server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "3166bcb1-d63b-4b69-9685-c12ca312e59c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UoAABWRy7SyojsyxBYFXCr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7347,
      "cache_read_input_tokens": 36749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7347
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017rzXgtT3yZ1vYaseRHY7hi`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
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
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "066ea94b-5645-47a1-bc33-43b6aa0cfcf8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UoAABWRy7SyojsyxBYFXCr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7347,
      "cache_read_input_tokens": 36749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7347
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

_source line 64 · 2026-05-15T18:28:49.219Z_

<details><summary>↩ Tool result · `toolu_017rzXgtT3yZ1vYaseRHY7hi`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "3e65a864-a533-4b68-b402-66e7ba91b9b7",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 29
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WDcN8H9LEUjV3QYUu1tJC8`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"\nimport json, os, glob\nbase = '/root/autodl-tmp/exp001/eval_results'\nresults = {}\nfor d in sorted(os.listdir(base)):\n    fp = os.path.join(base, d, 'eval_results.json')\n    if not os.path.isfile(fp): continue\n    if 'DEPRECATED' in d: continue\n    try:\n        with open(fp) as f:\n            data = json.load(f)\n        bm = data.get('benchmarks', {})\n        entry = {'paraphrased': data.get('paraphrased')}\n        for b in ['mmlu','gsm8k','arc_challenge','humaneval']:\n            if b in bm:\n                entry[b] = bm[b].get('accuracy')\n        results[d] = entry\n    except: pass\nprint(json.dumps(results, indent=2))\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "bbd2bd50-75c8-4948-97fb-0b11a91605be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019gus84LCFBfXgXBLYoxc4E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 44096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 800
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T18:28:54.983Z_

<details><summary>↩ Tool result · `toolu_01WDcN8H9LEUjV3QYUu1tJC8`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "bfdd8bad-c0be-49a4-a13d-b0a3ad8c0eac",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 67_

<details><summary>Logged reasoning block</summary>

```text
The ssh_read_only blocks `open(`. I need to use ssh_execute for the Python script. Let me do that instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "17f399ea-c4c7-42b5-9620-426de896ed9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2f1CoGY2UbPb2ZY56MHxo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 44896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

Need ssh_execute for the Python script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "b72464db-e763-4e12-943b-d6f3f6d9ff13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2f1CoGY2UbPb2ZY56MHxo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 44896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01MqfN6U3AYrt7SAU4cg6bRA`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"\nimport json, os\nbase = '/root/autodl-tmp/exp001/eval_results'\nresults = {}\nfor d in sorted(os.listdir(base)):\n    fp = os.path.join(base, d, 'eval_results.json')\n    if not os.path.isfile(fp): continue\n    if 'DEPRECATED' in d: continue\n    try:\n        with open(fp) as f:\n            data = json.load(f)\n        bm = data.get('benchmarks', {})\n        entry = {'paraphrased': data.get('paraphrased')}\n        for b in ['mmlu','gsm8k','arc_challenge','humaneval']:\n            if b in bm:\n                entry[b] = bm[b].get('accuracy')\n        results[d] = entry\n    except Exception as e:\n        results[d] = {'error': str(e)}\nprint(json.dumps(results, indent=2))\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "8e12145d-15f3-4edf-a5c9-7a485eedff5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2f1CoGY2UbPb2ZY56MHxo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 44896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

_source line 70 · 2026-05-15T18:29:00.571Z_

<details><summary>↩ Tool result · `toolu_01MqfN6U3AYrt7SAU4cg6bRA`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"\\\\nimport json, os\\\\nbase = \\\\'/root/autodl-tmp/exp001/eval_results\\\\'\\\\nresults = {}\\\\nfor d in sorted(os.listdir(base)):\\\\n    fp = os.path.join(base, d, \\\\'eval_results.json\\\\')\\\\n    if not os.path.isfile(fp): continue\\\\n    if \\\\'DEPRECATED\\\\' in d: continue\\\\n    try:\\\\n        with open(fp) as f:\\\\n            data = json.load(f)\\\\n        bm = data.get(\\\\'benchmarks\\\\', {})\\\\n        entry = {\\\\'paraphrased\\\\': data.get(\\\\'paraphrased\\\\')}\\\\n        for b in [\\\\'mmlu\\\\',\\\\'gsm8k\\\\',\\\\'arc_challenge\\\\',\\\\'humaneval\\\\']:\\\\n            if b in bm:\\\\n                entry[b] = bm[b].get(\\\\'accuracy\\\\')\\\\n        results[d] = entry\\\\n    except Exception as e:\\\\n        results[d] = {\\\\'error\\\\': str(e)}\\\\nprint(json.dumps(results, indent=2))\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "1006dfb3-d2ea-434e-b95d-795eeb3c0eef",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'python3 -c \\\\\\\"\\\\\\\\nimport json, os\\\\\\\\nbase = \\\\\\\\'/root/autodl-tmp/exp001/eval_results\\\\\\\\'\\\\\\\\nresults = {}\\\\\\\\nfor d in sorted(os.listdir(base)):\\\\\\\\n    fp = os.path.join(base, d, \\\\\\\\'eval_results.json\\\\\\\\')\\\\\\\\n    if not os.path.isfile(fp): continue\\\\\\\\n    if \\\\\\\\'DEPRECATED\\\\\\\\' in d: continue\\\\\\\\n    try:\\\\\\\\n        with open(fp) as f:\\\\\\\\n            data = json.load(f)\\\\\\\\n        bm = data.get(\\\\\\\\'benchmarks\\\\\\\\', {})\\\\\\\\n        entry = {\\\\\\\\'paraphrased\\\\\\\\': data.get(\\\\\\\\'paraphrased\\\\\\\\')}\\\\\\\\n        for b in [\\\\\\\\'mmlu\\\\\\\\',\\\\\\\\'gsm8k\\\\\\\\',\\\\\\\\'arc_challenge\\\\\\\\',\\\\\\\\'humaneval\\\\\\\\']:\\\\\\\\n            if b in bm:\\\\\\\\n                entry[b] = bm[b].get(\\\\\\\\'accuracy\\\\\\\\')\\\\\\\\n        results[d] = entry\\\\\\\\n    except Exception as e:\\\\\\\\n        results[d] = {\\\\\\\\'error\\\\\\\\': str(e)}\\\\\\\\nprint(json.dumps(results, indent=2))\\\\\\\\n\\\\\\\"\\\\\\\\n'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nbash: line 1: python3: command not found\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"\\\\nimport json, os\\\\nbase = \\\\'/root/autodl-tmp/exp001/eval_results\\\\'\\\\nresults = {}\\\\nfor d in sorted(os.listdir(base)):\\\\n    fp = os.path.join(base, d, \\\\'eval_results.json\\\\')\\\\n    if not os.path.isfile(fp): continue\\\\n    if \\\\'DEPRECATED\\\\' in d: continue\\\\n    try:\\\\n        with open(fp) as f:\\\\n            data = json.load(f)\\\\n        bm = data.get(\\\\'benchmarks\\\\', {})\\\\n        entry = {\\\\'paraphrased\\\\': data.get(\\\\'paraphrased\\\\')}\\\\n        for b in [\\\\'mmlu\\\\',\\\\'gsm8k\\\\',\\\\'arc_challenge\\\\',\\\\'humaneval\\\\']:\\\\n            if b in bm:\\\\n                entry[b] = bm[b].get(\\\\'accuracy\\\\')\\\\n        results[d] = entry\\\\n    except Exception as e:\\\\n        results[d] = {\\\\'error\\\\': str(e)}\\\\nprint(json.dumps(results, indent=2))\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
Python3 not found. Need to use the conda environment. The project says to use `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "5257b2de-915b-4419-84bc-efed9ac231c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtzyH3LPyZkvvicBL5vH7B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 45302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 832
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

_source line 72_

Need to activate conda first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "d1d2061f-890a-468b-a2c6-c554d0fdf282",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtzyH3LPyZkvvicBL5vH7B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 45302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 832
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

_source line 73_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01HeqP6k97dyJhGrc1ANS4wu`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, os\nbase = '/root/autodl-tmp/exp001/eval_results'\nresults = {}\nfor d in sorted(os.listdir(base)):\n    fp = os.path.join(base, d, 'eval_results.json')\n    if not os.path.isfile(fp): continue\n    if 'DEPRECATED' in d: continue\n    try:\n        with open(fp) as f:\n            data = json.load(f)\n        bm = data.get('benchmarks', {})\n        entry = {'paraphrased': data.get('paraphrased')}\n        for b in ['mmlu','gsm8k','arc_challenge','humaneval']:\n            if b in bm:\n                entry[b] = bm[b].get('accuracy')\n        results[d] = entry\n    except Exception as e:\n        results[d] = {'error': str(e)}\nprint(json.dumps(results, indent=2))\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "8bd88036-bfc5-46c8-979b-3c106dc7ad9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtzyH3LPyZkvvicBL5vH7B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 45302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 832
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

_source line 74 · 2026-05-15T18:29:08.977Z_

<details><summary>↩ Tool result · `toolu_01HeqP6k97dyJhGrc1ANS4wu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"Qwen2.5-0.5B-Instruct_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.24619000142429853,\\n    \\\"gsm8k\\\": 0.38817285822592873,\\n    \\\"arc_challenge\\\": 0.2815699658703072,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_base_pretrained_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.2293832787352229,\\n    \\\"gsm8k\\\": 0.16300227445034116,\\n    \\\"arc_challenge\\\": 0.22781569965870307,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s123\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.41824526420737784,\\n    \\\"gsm8k\\\": 0.34040940106141016,\\n    \\\"arc_challenge\\\": 0.39761092150170646,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.42159236575986325,\\n    \\\"gsm8k\\\": 0.3411675511751327,\\n    \\\"arc_challenge\\\": 0.4974402730375427,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.4049280729240849,\\n    \\\"gsm8k\\\": 0.3646702047005307,\\n    \\\"arc_challenge\\\": 0.3779863481228669,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.39787779518587096,\\n    \\\"gsm8k\\\": 0.3692191053828658,\\n    \\\"arc_challenge\\\": 0.46928327645051193,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.4428441479684657,\\n    \\\"gsm8k\\\": 0.2807017543859649,\\n    \\\"arc_challenge\\\": 0.47919655667144906,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42_v2\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.39787779518587096,\\n    \\\"gsm8k\\\": 0.3692191053828658,\\n    \\\"arc_challenge\\\": 0.46928327645051193,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.30024213075060535,\\n    \\\"gsm8k\\\": 0.36770280515542075,\\n    \\\"arc_challenge\\\": 0.2977815699658703,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.3165554881746513,\\n    \\\"gsm8k\\\": 0.29385964912280704,\\n    \\\"arc_challenge\\\": 0.29124820659971307,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.2929069933057969,\\n    \\\"gsm8k\\\": 0.3601213040181956,\\n    \\\"arc_challenge\\\": 0.2858361774744027,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.32545221478421876,\\n    \\\"gsm8k\\\": 0.36239575435936316,\\n    \\\"arc_challenge\\\": 0.32849829351535836,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.3547604608853851,\\n    \\\"gsm8k\\\": 0.25877192982456143,\\n    \\\"arc_challenge\\\": 0.3299856527977044,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d025_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.3473151972653468,\\n    \\\"gsm8k\\\": 0.35329795299469297,\\n    \\\"arc_challenge\\\": 0.4061433447098976,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d025_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.28030195128899016,\\n    \\\"gsm8k\\\": 0.3661865049279757,\\n    \\\"arc_challenge\\\": 0.3250853242320819,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d025_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.28350515463917525,\\n    \\\"gsm8k\\\": 0.31140350877192985,\\n    \\\"arc_challenge\\\": 0.3199426111908178,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d100_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.3057968950291981,\\n    \\\"gsm8k\\\": 0.379833206974981,\\n    \\\"arc_challenge\\\": 0.36689419795221845,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d100_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23223187580116791,\\n    \\\"gsm8k\\\": 0.3570887035633055,\\n    \\\"arc_challenge\\\": 0.22696245733788395,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d100_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23337131462754593,\\n    \\\"gsm8k\\\": 0.36542835481425323,\\n    \\\"arc_challenge\\\": 0.29436860068259385,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-1.5B_base_pretrained\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23030907278165502,\\n    \\\"gsm8k\\\": 0.00530705079605762,\\n    \\\"arc_challenge\\\": 0.23037542662116042,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-1.5B_d000_s123\\\": {\\n    \\\"paraphrased\\\": false\\n\\n... [截断: 输出过长，省略 3124 字符] ...\\n\\nlse,\\n    \\\"mmlu\\\": 0.6336704173194702,\\n    \\\"gsm8k\\\": 0.11675511751326763,\\n    \\\"arc_challenge\\\": 0.8216723549488054,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6473620375985446,\\n    \\\"gsm8k\\\": 0.04824561403508772,\\n    \\\"arc_challenge\\\": 0.8235294117647058,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_s42_v3_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6339552770260647,\\n    \\\"gsm8k\\\": 0.1197877179681577,\\n    \\\"arc_challenge\\\": 0.8276450511945392,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6313915396667141,\\n    \\\"gsm8k\\\": 0.2676269901440485,\\n    \\\"arc_challenge\\\": 0.825938566552901,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6511522134627047,\\n    \\\"gsm8k\\\": 0.14912280701754385,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6294687366472013,\\n    \\\"gsm8k\\\": 0.3525398028809704,\\n    \\\"arc_challenge\\\": 0.818259385665529,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.646755609460279,\\n    \\\"gsm8k\\\": 0.2894736842105263,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_para_aligned_v2\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.646755609460279,\\n    \\\"gsm8k\\\": 0.2894736842105263,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_para_aligned_v3\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.646755609460279,\\n    \\\"gsm8k\\\": 0.2894736842105263,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d005_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6461491813220134,\\n    \\\"gsm8k\\\": 0.5,\\n    \\\"arc_challenge\\\": 0.8192252510760402,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d005_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.634453781512605,\\n    \\\"gsm8k\\\": 0.20773313115996966,\\n    \\\"arc_challenge\\\": 0.8293515358361775,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d005_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6541843541540328,\\n    \\\"gsm8k\\\": 0.14912280701754385,\\n    \\\"arc_challenge\\\": 0.8220946915351507,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.636732659165361,\\n    \\\"gsm8k\\\": 0.5253980288097043,\\n    \\\"arc_challenge\\\": 0.8336177474402731,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6614614918132201,\\n    \\\"gsm8k\\\": 0.42543859649122806,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_v2_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5997721122347244,\\n    \\\"gsm8k\\\": 0.6793025018953753,\\n    \\\"arc_challenge\\\": 0.8276450511945392,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_v2_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6209824135839903,\\n    \\\"gsm8k\\\": 0.5482456140350878,\\n    \\\"arc_challenge\\\": 0.8106169296987088,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6590357792601577,\\n    \\\"gsm8k\\\": 0.5833333333333334,\\n    \\\"arc_challenge\\\": 0.8091822094691535,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_v2_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6318900441532546,\\n    \\\"gsm8k\\\": 0.7323730098559514,\\n    \\\"arc_challenge\\\": 0.8310580204778157,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_v2_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6319612590799032,\\n    \\\"gsm8k\\\": 0.7414708112206216,\\n    \\\"arc_challenge\\\": 0.8242320819112628,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_v2_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6590357792601577,\\n    \\\"gsm8k\\\": 0.5833333333333334,\\n    \\\"arc_challenge\\\": 0.8091822094691535,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_raw\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"gsm8k\\\": 0.6050037907505686,\\n    \\\"humaneval\\\": null\\n  }\\n}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.94}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "d0f5b1ea-2f09-456d-9553-dbd56842c7e2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"Qwen2.5-0.5B-Instruct_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.24619000142429853,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.38817285822592873,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.2815699658703072,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_base_pretrained_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.2293832787352229,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.16300227445034116,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.22781569965870307,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d000_s123\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.41824526420737784,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.34040940106141016,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.39761092150170646,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d000_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.42159236575986325,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3411675511751327,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.4974402730375427,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d000_s42\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.4049280729240849,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3646702047005307,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.3779863481228669,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d000_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.39787779518587096,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3692191053828658,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.46928327645051193,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d000_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.4428441479684657,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.2807017543859649,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.47919655667144906,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d000_s42_v2\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.39787779518587096,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3692191053828658,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.46928327645051193,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d005_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.30024213075060535,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.36770280515542075,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.2977815699658703,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d005_s123_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.3165554881746513,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.29385964912280704,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.29124820659971307,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d005_s42\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.2929069933057969,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3601213040181956,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.2858361774744027,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d005_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.32545221478421876,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.36239575435936316,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.32849829351535836,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d005_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.3547604608853851,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.25877192982456143,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.3299856527977044,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d025_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.3473151972653468,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.35329795299469297,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.4061433447098976,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d025_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.28030195128899016,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3661865049279757,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.3250853242320819,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d025_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.28350515463917525,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.31140350877192985,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.3199426111908178,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d100_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.3057968950291981,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.379833206974981,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.36689419795221845,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d100_s42\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.23223187580116791,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3570887035633055,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.22696245733788395,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d100_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.23337131462754593,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.36542835481425323,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.29436860068259385,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-1.5B_base_pretrained\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.23030907278165502,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.00530705079605762,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.23037542662116042,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-1.5B_d000_s123\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false\\\\n\\\\n... [截断: 输出过长，省略 3124 字符] ...\\\\n\\\\nlse,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6336704173194702,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.11675511751326763,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8216723549488054,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6473620375985446,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.04824561403508772,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8235294117647058,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_s42_v3_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6339552770260647,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.1197877179681577,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8276450511945392,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_v2_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6313915396667141,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.2676269901440485,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.825938566552901,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_v2_s123_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6511522134627047,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.14912280701754385,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.812051649928264,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_v2_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6294687366472013,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3525398028809704,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.818259385665529,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_v2_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.646755609460279,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.2894736842105263,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.812051649928264,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_v2_s42_para_aligned_v2\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.646755609460279,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.2894736842105263,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.812051649928264,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_v2_s42_para_aligned_v3\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.646755609460279,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.2894736842105263,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.812051649928264,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d005_s123_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6461491813220134,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8192252510760402,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d005_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.634453781512605,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.20773313115996966,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8293515358361775,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d005_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6541843541540328,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.14912280701754385,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8220946915351507,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d025_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.636732659165361,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5253980288097043,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8336177474402731,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d025_s123_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6614614918132201,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.42543859649122806,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.812051649928264,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d025_v2_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5997721122347244,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6793025018953753,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8276450511945392,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d025_v2_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6209824135839903,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5482456140350878,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8106169296987088,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d100_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6590357792601577,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5833333333333334,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8091822094691535,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d100_v2_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6318900441532546,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.7323730098559514,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8310580204778157,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d100_v2_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6319612590799032,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.7414708112206216,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8242320819112628,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d100_v2_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6590357792601577,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5833333333333334,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8091822094691535,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_raw\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6050037907505686,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  }\\\\n}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.94}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"Qwen2.5-0.5B-Instruct_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.24619000142429853,\\n    \\\"gsm8k\\\": 0.38817285822592873,\\n    \\\"arc_challenge\\\": 0.2815699658703072,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_base_pretrained_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.2293832787352229,\\n    \\\"gsm8k\\\": 0.16300227445034116,\\n    \\\"arc_challenge\\\": 0.22781569965870307,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s123\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.41824526420737784,\\n    \\\"gsm8k\\\": 0.34040940106141016,\\n    \\\"arc_challenge\\\": 0.39761092150170646,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.42159236575986325,\\n    \\\"gsm8k\\\": 0.3411675511751327,\\n    \\\"arc_challenge\\\": 0.4974402730375427,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.4049280729240849,\\n    \\\"gsm8k\\\": 0.3646702047005307,\\n    \\\"arc_challenge\\\": 0.3779863481228669,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.39787779518587096,\\n    \\\"gsm8k\\\": 0.3692191053828658,\\n    \\\"arc_challenge\\\": 0.46928327645051193,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.4428441479684657,\\n    \\\"gsm8k\\\": 0.2807017543859649,\\n    \\\"arc_challenge\\\": 0.47919655667144906,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42_v2\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.39787779518587096,\\n    \\\"gsm8k\\\": 0.3692191053828658,\\n    \\\"arc_challenge\\\": 0.46928327645051193,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.30024213075060535,\\n    \\\"gsm8k\\\": 0.36770280515542075,\\n    \\\"arc_challenge\\\": 0.2977815699658703,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.3165554881746513,\\n    \\\"gsm8k\\\": 0.29385964912280704,\\n    \\\"arc_challenge\\\": 0.29124820659971307,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.2929069933057969,\\n    \\\"gsm8k\\\": 0.3601213040181956,\\n    \\\"arc_challenge\\\": 0.2858361774744027,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.32545221478421876,\\n    \\\"gsm8k\\\": 0.36239575435936316,\\n    \\\"arc_challenge\\\": 0.32849829351535836,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.3547604608853851,\\n    \\\"gsm8k\\\": 0.25877192982456143,\\n    \\\"arc_challenge\\\": 0.3299856527977044,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d025_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.3473151972653468,\\n    \\\"gsm8k\\\": 0.35329795299469297,\\n    \\\"arc_challenge\\\": 0.4061433447098976,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d025_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.28030195128899016,\\n    \\\"gsm8k\\\": 0.3661865049279757,\\n    \\\"arc_challenge\\\": 0.3250853242320819,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d025_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.28350515463917525,\\n    \\\"gsm8k\\\": 0.31140350877192985,\\n    \\\"arc_challenge\\\": 0.3199426111908178,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d100_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.3057968950291981,\\n    \\\"gsm8k\\\": 0.379833206974981,\\n    \\\"arc_challenge\\\": 0.36689419795221845,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d100_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23223187580116791,\\n    \\\"gsm8k\\\": 0.3570887035633055,\\n    \\\"arc_challenge\\\": 0.22696245733788395,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d100_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23337131462754593,\\n    \\\"gsm8k\\\": 0.36542835481425323,\\n    \\\"arc_challenge\\\": 0.29436860068259385,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-1.5B_base_pretrained\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23030907278165502,\\n    \\\"gsm8k\\\": 0.00530705079605762,\\n    \\\"arc_challenge\\\": 0.23037542662116042,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-1.5B_d000_s123\\\": {\\n    \\\"paraphrased\\\": false\\n\\n... [截断: 输出过长，省略 3124 字符] ...\\n\\nlse,\\n    \\\"mmlu\\\": 0.6336704173194702,\\n    \\\"gsm8k\\\": 0.11675511751326763,\\n    \\\"arc_challenge\\\": 0.8216723549488054,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6473620375985446,\\n    \\\"gsm8k\\\": 0.04824561403508772,\\n    \\\"arc_challenge\\\": 0.8235294117647058,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_s42_v3_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6339552770260647,\\n    \\\"gsm8k\\\": 0.1197877179681577,\\n    \\\"arc_challenge\\\": 0.8276450511945392,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6313915396667141,\\n    \\\"gsm8k\\\": 0.2676269901440485,\\n    \\\"arc_challenge\\\": 0.825938566552901,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6511522134627047,\\n    \\\"gsm8k\\\": 0.14912280701754385,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6294687366472013,\\n    \\\"gsm8k\\\": 0.3525398028809704,\\n    \\\"arc_challenge\\\": 0.818259385665529,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.646755609460279,\\n    \\\"gsm8k\\\": 0.2894736842105263,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_para_aligned_v2\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.646755609460279,\\n    \\\"gsm8k\\\": 0.2894736842105263,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_para_aligned_v3\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.646755609460279,\\n    \\\"gsm8k\\\": 0.2894736842105263,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d005_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6461491813220134,\\n    \\\"gsm8k\\\": 0.5,\\n    \\\"arc_challenge\\\": 0.8192252510760402,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d005_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.634453781512605,\\n    \\\"gsm8k\\\": 0.20773313115996966,\\n    \\\"arc_challenge\\\": 0.8293515358361775,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d005_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6541843541540328,\\n    \\\"gsm8k\\\": 0.14912280701754385,\\n    \\\"arc_challenge\\\": 0.8220946915351507,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.636732659165361,\\n    \\\"gsm8k\\\": 0.5253980288097043,\\n    \\\"arc_challenge\\\": 0.8336177474402731,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6614614918132201,\\n    \\\"gsm8k\\\": 0.42543859649122806,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_v2_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5997721122347244,\\n    \\\"gsm8k\\\": 0.6793025018953753,\\n    \\\"arc_challenge\\\": 0.8276450511945392,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_v2_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6209824135839903,\\n    \\\"gsm8k\\\": 0.5482456140350878,\\n    \\\"arc_challenge\\\": 0.8106169296987088,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6590357792601577,\\n    \\\"gsm8k\\\": 0.5833333333333334,\\n    \\\"arc_challenge\\\": 0.8091822094691535,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_v2_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6318900441532546,\\n    \\\"gsm8k\\\": 0.7323730098559514,\\n    \\\"arc_challenge\\\": 0.8310580204778157,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_v2_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6319612590799032,\\n    \\\"gsm8k\\\": 0.7414708112206216,\\n    \\\"arc_challenge\\\": 0.8242320819112628,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_v2_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6590357792601577,\\n    \\\"gsm8k\\\": 0.5833333333333334,\\n    \\\"arc_challenge\\\": 0.8091822094691535,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_raw\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"gsm8k\\\": 0.6050037907505686,\\n    \\\"humaneval\\\": null\\n  }\\n}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.94}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 75_

<details><summary>Logged reasoning block</summary>

```text
The output was truncated. Let me save the complete output to a file on the server and then download it. Actually, let me check what was truncated - it starts with the 1.5B entries. Let me get the full data by saving to a file first.

Actually, looking at the output, I can see:
- All files have `humaneval: null` - so HumanEval results are not in the eval_results.json files
- The data is mostly complete for mmlu, gsm8k, arc_challenge

Let me also check if HumanEval results are stored separately. Looking at the registry data from the subagent, the registry does have HumanEval metrics for some experiments, so there might be separate HumanEval eval files.


I need to save the full output to a file since it got truncated around the 1.5B entries, and I should also look for HumanEval data in separate files since the eval_results.json files only show null values for that benchmark.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "4000f0cf-0e2e-44ac-b7d7-24175e80b9f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MFZAkbZ9zutiD8ks8p6aA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5737,
      "cache_read_input_tokens": 46134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5737
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

_source line 76_

Output was truncated and HumanEval is null in all files. Let me save the full extraction to a file and check for HumanEval separately.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "a847661e-84b6-404c-84d2-7b70e38036a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MFZAkbZ9zutiD8ks8p6aA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5737,
      "cache_read_input_tokens": 46134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5737
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

_source line 77_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01872sMbZPd5XAov1rAnHAnb`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, os\nbase = '/root/autodl-tmp/exp001/eval_results'\nresults = {}\nfor d in sorted(os.listdir(base)):\n    fp = os.path.join(base, d, 'eval_results.json')\n    if not os.path.isfile(fp): continue\n    if 'DEPRECATED' in d: continue\n    try:\n        with open(fp) as f:\n            data = json.load(f)\n        bm = data.get('benchmarks', {})\n        entry = {'paraphrased': data.get('paraphrased')}\n        for b in ['mmlu','gsm8k','arc_challenge','humaneval']:\n            if b in bm:\n                entry[b] = bm[b].get('accuracy')\n        results[d] = entry\n    except Exception as e:\n        results[d] = {'error': str(e)}\nwith open('/tmp/eval_metrics_all.json', 'w') as f:\n    json.dump(results, f, indent=2)\nprint('Saved', len(results), 'entries')\nprint('Keys with humaneval not null:', sum(1 for v in results.values() if v.get('humaneval') is not None))\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "e8683b7c-6b27-46b2-bfd9-65cfe757e3d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MFZAkbZ9zutiD8ks8p6aA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5737,
      "cache_read_input_tokens": 46134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5737
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

_source line 78_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LiCuuvamNa9TobNvnfs5fJ`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/ -name \"humaneval*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "c820ad42-e6e4-46d2-833b-cb0d275bf291",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MFZAkbZ9zutiD8ks8p6aA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5737,
      "cache_read_input_tokens": 46134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5737
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

_source line 79 · 2026-05-15T18:29:27.109Z_

<details><summary>↩ Tool result · `toolu_01872sMbZPd5XAov1rAnHAnb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Saved 57 entries\\nKeys with humaneval not null: 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "e942b134-10eb-49c3-892c-b08fa2141a25",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Saved 57 entries\\\\nKeys with humaneval not null: 0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Saved 57 entries\\nKeys with humaneval not null: 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.44}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T18:29:27.644Z_

<details><summary>↩ Tool result · `toolu_01LiCuuvamNa9TobNvnfs5fJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "f421b531-7348-4cf5-b1d8-39d9be09f93b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
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
No HumanEval files on disk. The HumanEval metrics in the registry must have come from somewhere else - possibly a different eval pipeline. Let me:
1. Read the full JSON from the server
2. Also check if there are humaneval results stored elsewhere

Let me read the full JSON first, then combine with registry HumanEval data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "ef2f5af4-254d-4ac8-9d46-d62dd11cab8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRFTmCten1cYJvJj4rcHmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 51871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1009
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

HumanEval results are only in the registry, not on disk. Let me get the full metrics file and also extract HumanEval from the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "2f6166b9-1ea2-4036-a2b8-515505a30a68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRFTmCten1cYJvJj4rcHmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 51871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1009
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01B4pLdWKLWMS8QfvSySPpqt`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /tmp/eval_metrics_all.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "7174ff44-89fe-463e-9035-79e61f7239f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRFTmCten1cYJvJj4rcHmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 51871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1009
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

_source line 84 · 2026-05-15T18:29:33.294Z_

<details><summary>↩ Tool result · `toolu_01B4pLdWKLWMS8QfvSySPpqt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"Qwen2.5-0.5B-Instruct_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.24619000142429853,\\n    \\\"gsm8k\\\": 0.38817285822592873,\\n    \\\"arc_challenge\\\": 0.2815699658703072,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_base_pretrained_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.2293832787352229,\\n    \\\"gsm8k\\\": 0.16300227445034116,\\n    \\\"arc_challenge\\\": 0.22781569965870307,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s123\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.41824526420737784,\\n    \\\"gsm8k\\\": 0.34040940106141016,\\n    \\\"arc_challenge\\\": 0.39761092150170646,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.42159236575986325,\\n    \\\"gsm8k\\\": 0.3411675511751327,\\n    \\\"arc_challenge\\\": 0.4974402730375427,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.4049280729240849,\\n    \\\"gsm8k\\\": 0.3646702047005307,\\n    \\\"arc_challenge\\\": 0.3779863481228669,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.39787779518587096,\\n    \\\"gsm8k\\\": 0.3692191053828658,\\n    \\\"arc_challenge\\\": 0.46928327645051193,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.4428441479684657,\\n    \\\"gsm8k\\\": 0.2807017543859649,\\n    \\\"arc_challenge\\\": 0.47919655667144906,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42_v2\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.39787779518587096,\\n    \\\"gsm8k\\\": 0.3692191053828658,\\n    \\\"arc_challenge\\\": 0.46928327645051193,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.30024213075060535,\\n    \\\"gsm8k\\\": 0.36770280515542075,\\n    \\\"arc_challenge\\\": 0.2977815699658703,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.3165554881746513,\\n    \\\"gsm8k\\\": 0.29385964912280704,\\n    \\\"arc_challenge\\\": 0.29124820659971307,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.2929069933057969,\\n    \\\"gsm8k\\\": 0.3601213040181956,\\n    \\\"arc_challenge\\\": 0.2858361774744027,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.32545221478421876,\\n    \\\"gsm8k\\\": 0.36239575435936316,\\n    \\\"arc_challenge\\\": 0.32849829351535836,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.3547604608853851,\\n    \\\"gsm8k\\\": 0.25877192982456143,\\n    \\\"arc_challenge\\\": 0.3299856527977044,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d025_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.3473151972653468,\\n    \\\"gsm8k\\\": 0.35329795299469297,\\n    \\\"arc_challenge\\\": 0.4061433447098976,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d025_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.28030195128899016,\\n    \\\"gsm8k\\\": 0.3661865049279757,\\n    \\\"arc_challenge\\\": 0.3250853242320819,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d025_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.28350515463917525,\\n    \\\"gsm8k\\\": 0.31140350877192985,\\n    \\\"arc_challenge\\\": 0.3199426111908178,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d100_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.3057968950291981,\\n    \\\"gsm8k\\\": 0.379833206974981,\\n    \\\"arc_challenge\\\": 0.36689419795221845,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d100_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23223187580116791,\\n    \\\"gsm8k\\\": 0.3570887035633055,\\n    \\\"arc_challenge\\\": 0.22696245733788395,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d100_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23337131462754593,\\n    \\\"gsm8k\\\": 0.36542835481425323,\\n    \\\"arc_challenge\\\": 0.29436860068259385,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-1.5B_base_pretrained\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23030907278165502,\\n    \\\"gsm8k\\\": 0.00530705079605762,\\n    \\\"arc_challenge\\\": 0.23037542662116042,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-1.5B_d000_s123\\\": {\\n    \\\"paraphrased\\\": false\\n\\n... [截断: 输出过长，省略 3123 字符] ...\\n\\nalse,\\n    \\\"mmlu\\\": 0.6336704173194702,\\n    \\\"gsm8k\\\": 0.11675511751326763,\\n    \\\"arc_challenge\\\": 0.8216723549488054,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6473620375985446,\\n    \\\"gsm8k\\\": 0.04824561403508772,\\n    \\\"arc_challenge\\\": 0.8235294117647058,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_s42_v3_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6339552770260647,\\n    \\\"gsm8k\\\": 0.1197877179681577,\\n    \\\"arc_challenge\\\": 0.8276450511945392,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6313915396667141,\\n    \\\"gsm8k\\\": 0.2676269901440485,\\n    \\\"arc_challenge\\\": 0.825938566552901,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6511522134627047,\\n    \\\"gsm8k\\\": 0.14912280701754385,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6294687366472013,\\n    \\\"gsm8k\\\": 0.3525398028809704,\\n    \\\"arc_challenge\\\": 0.818259385665529,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.646755609460279,\\n    \\\"gsm8k\\\": 0.2894736842105263,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_para_aligned_v2\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.646755609460279,\\n    \\\"gsm8k\\\": 0.2894736842105263,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_para_aligned_v3\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.646755609460279,\\n    \\\"gsm8k\\\": 0.2894736842105263,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d005_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6461491813220134,\\n    \\\"gsm8k\\\": 0.5,\\n    \\\"arc_challenge\\\": 0.8192252510760402,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d005_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.634453781512605,\\n    \\\"gsm8k\\\": 0.20773313115996966,\\n    \\\"arc_challenge\\\": 0.8293515358361775,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d005_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6541843541540328,\\n    \\\"gsm8k\\\": 0.14912280701754385,\\n    \\\"arc_challenge\\\": 0.8220946915351507,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.636732659165361,\\n    \\\"gsm8k\\\": 0.5253980288097043,\\n    \\\"arc_challenge\\\": 0.8336177474402731,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6614614918132201,\\n    \\\"gsm8k\\\": 0.42543859649122806,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_v2_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5997721122347244,\\n    \\\"gsm8k\\\": 0.6793025018953753,\\n    \\\"arc_challenge\\\": 0.8276450511945392,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_v2_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6209824135839903,\\n    \\\"gsm8k\\\": 0.5482456140350878,\\n    \\\"arc_challenge\\\": 0.8106169296987088,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6590357792601577,\\n    \\\"gsm8k\\\": 0.5833333333333334,\\n    \\\"arc_challenge\\\": 0.8091822094691535,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_v2_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6318900441532546,\\n    \\\"gsm8k\\\": 0.7323730098559514,\\n    \\\"arc_challenge\\\": 0.8310580204778157,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_v2_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6319612590799032,\\n    \\\"gsm8k\\\": 0.7414708112206216,\\n    \\\"arc_challenge\\\": 0.8242320819112628,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_v2_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6590357792601577,\\n    \\\"gsm8k\\\": 0.5833333333333334,\\n    \\\"arc_challenge\\\": 0.8091822094691535,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_raw\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"gsm8k\\\": 0.6050037907505686,\\n    \\\"humaneval\\\": null\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "c275b3a0-d2b9-4bb8-ba9a-89778d6320ca",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"Qwen2.5-0.5B-Instruct_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.24619000142429853,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.38817285822592873,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.2815699658703072,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_base_pretrained_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.2293832787352229,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.16300227445034116,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.22781569965870307,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d000_s123\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.41824526420737784,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.34040940106141016,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.39761092150170646,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d000_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.42159236575986325,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3411675511751327,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.4974402730375427,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d000_s42\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.4049280729240849,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3646702047005307,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.3779863481228669,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d000_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.39787779518587096,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3692191053828658,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.46928327645051193,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d000_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.4428441479684657,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.2807017543859649,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.47919655667144906,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d000_s42_v2\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.39787779518587096,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3692191053828658,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.46928327645051193,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d005_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.30024213075060535,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.36770280515542075,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.2977815699658703,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d005_s123_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.3165554881746513,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.29385964912280704,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.29124820659971307,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d005_s42\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.2929069933057969,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3601213040181956,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.2858361774744027,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d005_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.32545221478421876,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.36239575435936316,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.32849829351535836,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d005_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.3547604608853851,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.25877192982456143,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.3299856527977044,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d025_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.3473151972653468,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.35329795299469297,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.4061433447098976,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d025_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.28030195128899016,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3661865049279757,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.3250853242320819,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d025_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.28350515463917525,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.31140350877192985,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.3199426111908178,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d100_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.3057968950291981,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.379833206974981,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.36689419795221845,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d100_s42\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.23223187580116791,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3570887035633055,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.22696245733788395,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-0.5B_d100_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.23337131462754593,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.36542835481425323,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.29436860068259385,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-1.5B_base_pretrained\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.23030907278165502,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.00530705079605762,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.23037542662116042,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-1.5B_d000_s123\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false\\\\n\\\\n... [截断: 输出过长，省略 3123 字符] ...\\\\n\\\\nalse,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6336704173194702,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.11675511751326763,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8216723549488054,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6473620375985446,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.04824561403508772,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8235294117647058,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_s42_v3_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6339552770260647,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.1197877179681577,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8276450511945392,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_v2_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6313915396667141,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.2676269901440485,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.825938566552901,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_v2_s123_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6511522134627047,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.14912280701754385,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.812051649928264,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_v2_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6294687366472013,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.3525398028809704,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.818259385665529,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_v2_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.646755609460279,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.2894736842105263,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.812051649928264,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_v2_s42_para_aligned_v2\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.646755609460279,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.2894736842105263,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.812051649928264,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d000_v2_s42_para_aligned_v3\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.646755609460279,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.2894736842105263,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.812051649928264,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d005_s123_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6461491813220134,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8192252510760402,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d005_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.634453781512605,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.20773313115996966,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8293515358361775,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d005_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6541843541540328,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.14912280701754385,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8220946915351507,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d025_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.636732659165361,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5253980288097043,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8336177474402731,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d025_s123_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6614614918132201,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.42543859649122806,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.812051649928264,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d025_v2_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5997721122347244,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6793025018953753,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8276450511945392,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d025_v2_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6209824135839903,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5482456140350878,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8106169296987088,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d100_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6590357792601577,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5833333333333334,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8091822094691535,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d100_v2_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6318900441532546,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.7323730098559514,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8310580204778157,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d100_v2_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6319612590799032,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.7414708112206216,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8242320819112628,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_d100_v2_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6590357792601577,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5833333333333334,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.8091822094691535,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"Qwen2.5-3B_raw\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6050037907505686,\\\\n    \\\\\\\"humaneval\\\\\\\": null\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"Qwen2.5-0.5B-Instruct_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.24619000142429853,\\n    \\\"gsm8k\\\": 0.38817285822592873,\\n    \\\"arc_challenge\\\": 0.2815699658703072,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_base_pretrained_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.2293832787352229,\\n    \\\"gsm8k\\\": 0.16300227445034116,\\n    \\\"arc_challenge\\\": 0.22781569965870307,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s123\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.41824526420737784,\\n    \\\"gsm8k\\\": 0.34040940106141016,\\n    \\\"arc_challenge\\\": 0.39761092150170646,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.42159236575986325,\\n    \\\"gsm8k\\\": 0.3411675511751327,\\n    \\\"arc_challenge\\\": 0.4974402730375427,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.4049280729240849,\\n    \\\"gsm8k\\\": 0.3646702047005307,\\n    \\\"arc_challenge\\\": 0.3779863481228669,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.39787779518587096,\\n    \\\"gsm8k\\\": 0.3692191053828658,\\n    \\\"arc_challenge\\\": 0.46928327645051193,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.4428441479684657,\\n    \\\"gsm8k\\\": 0.2807017543859649,\\n    \\\"arc_challenge\\\": 0.47919655667144906,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d000_s42_v2\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.39787779518587096,\\n    \\\"gsm8k\\\": 0.3692191053828658,\\n    \\\"arc_challenge\\\": 0.46928327645051193,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.30024213075060535,\\n    \\\"gsm8k\\\": 0.36770280515542075,\\n    \\\"arc_challenge\\\": 0.2977815699658703,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.3165554881746513,\\n    \\\"gsm8k\\\": 0.29385964912280704,\\n    \\\"arc_challenge\\\": 0.29124820659971307,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.2929069933057969,\\n    \\\"gsm8k\\\": 0.3601213040181956,\\n    \\\"arc_challenge\\\": 0.2858361774744027,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.32545221478421876,\\n    \\\"gsm8k\\\": 0.36239575435936316,\\n    \\\"arc_challenge\\\": 0.32849829351535836,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d005_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.3547604608853851,\\n    \\\"gsm8k\\\": 0.25877192982456143,\\n    \\\"arc_challenge\\\": 0.3299856527977044,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d025_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.3473151972653468,\\n    \\\"gsm8k\\\": 0.35329795299469297,\\n    \\\"arc_challenge\\\": 0.4061433447098976,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d025_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.28030195128899016,\\n    \\\"gsm8k\\\": 0.3661865049279757,\\n    \\\"arc_challenge\\\": 0.3250853242320819,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d025_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.28350515463917525,\\n    \\\"gsm8k\\\": 0.31140350877192985,\\n    \\\"arc_challenge\\\": 0.3199426111908178,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d100_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.3057968950291981,\\n    \\\"gsm8k\\\": 0.379833206974981,\\n    \\\"arc_challenge\\\": 0.36689419795221845,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d100_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23223187580116791,\\n    \\\"gsm8k\\\": 0.3570887035633055,\\n    \\\"arc_challenge\\\": 0.22696245733788395,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-0.5B_d100_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23337131462754593,\\n    \\\"gsm8k\\\": 0.36542835481425323,\\n    \\\"arc_challenge\\\": 0.29436860068259385,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-1.5B_base_pretrained\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23030907278165502,\\n    \\\"gsm8k\\\": 0.00530705079605762,\\n    \\\"arc_challenge\\\": 0.23037542662116042,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-1.5B_d000_s123\\\": {\\n    \\\"paraphrased\\\": false\\n\\n... [截断: 输出过长，省略 3123 字符] ...\\n\\nalse,\\n    \\\"mmlu\\\": 0.6336704173194702,\\n    \\\"gsm8k\\\": 0.11675511751326763,\\n    \\\"arc_challenge\\\": 0.8216723549488054,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6473620375985446,\\n    \\\"gsm8k\\\": 0.04824561403508772,\\n    \\\"arc_challenge\\\": 0.8235294117647058,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_s42_v3_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6339552770260647,\\n    \\\"gsm8k\\\": 0.1197877179681577,\\n    \\\"arc_challenge\\\": 0.8276450511945392,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6313915396667141,\\n    \\\"gsm8k\\\": 0.2676269901440485,\\n    \\\"arc_challenge\\\": 0.825938566552901,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6511522134627047,\\n    \\\"gsm8k\\\": 0.14912280701754385,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6294687366472013,\\n    \\\"gsm8k\\\": 0.3525398028809704,\\n    \\\"arc_challenge\\\": 0.818259385665529,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.646755609460279,\\n    \\\"gsm8k\\\": 0.2894736842105263,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_para_aligned_v2\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.646755609460279,\\n    \\\"gsm8k\\\": 0.2894736842105263,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d000_v2_s42_para_aligned_v3\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.646755609460279,\\n    \\\"gsm8k\\\": 0.2894736842105263,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d005_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6461491813220134,\\n    \\\"gsm8k\\\": 0.5,\\n    \\\"arc_challenge\\\": 0.8192252510760402,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d005_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.634453781512605,\\n    \\\"gsm8k\\\": 0.20773313115996966,\\n    \\\"arc_challenge\\\": 0.8293515358361775,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d005_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6541843541540328,\\n    \\\"gsm8k\\\": 0.14912280701754385,\\n    \\\"arc_challenge\\\": 0.8220946915351507,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.636732659165361,\\n    \\\"gsm8k\\\": 0.5253980288097043,\\n    \\\"arc_challenge\\\": 0.8336177474402731,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_s123_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6614614918132201,\\n    \\\"gsm8k\\\": 0.42543859649122806,\\n    \\\"arc_challenge\\\": 0.812051649928264,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_v2_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5997721122347244,\\n    \\\"gsm8k\\\": 0.6793025018953753,\\n    \\\"arc_challenge\\\": 0.8276450511945392,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d025_v2_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6209824135839903,\\n    \\\"gsm8k\\\": 0.5482456140350878,\\n    \\\"arc_challenge\\\": 0.8106169296987088,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6590357792601577,\\n    \\\"gsm8k\\\": 0.5833333333333334,\\n    \\\"arc_challenge\\\": 0.8091822094691535,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_v2_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6318900441532546,\\n    \\\"gsm8k\\\": 0.7323730098559514,\\n    \\\"arc_challenge\\\": 0.8310580204778157,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_v2_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.6319612590799032,\\n    \\\"gsm8k\\\": 0.7414708112206216,\\n    \\\"arc_challenge\\\": 0.8242320819112628,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_d100_v2_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6590357792601577,\\n    \\\"gsm8k\\\": 0.5833333333333334,\\n    \\\"arc_challenge\\\": 0.8091822094691535,\\n    \\\"humaneval\\\": null\\n  },\\n  \\\"Qwen2.5-3B_raw\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"gsm8k\\\": 0.6050037907505686,\\n    \\\"humaneval\\\": null\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 85_

<details><summary>Logged reasoning block</summary>

```text
Still truncated around the 1.5B section. Let me extract those specific entries that were cut.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "ad73b839-a59e-44c5-b8e8-abc96ec2e771",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCNeoka1pkBNuL6NfCWKLC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5444,
      "cache_read_input_tokens": 52880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5444
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

_source line 86_

Still truncated in the 1.5B section. Let me get the missing part.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "201cd5eb-b5bd-41e2-a03c-e4d611725efe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCNeoka1pkBNuL6NfCWKLC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5444,
      "cache_read_input_tokens": 52880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5444
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

_source line 87_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019jJfp4coKZUa7caRDLjJZ3`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -A4 \"1.5B\" /tmp/eval_metrics_all.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "491161c9-18c0-4730-9a9b-1f340f945ba4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCNeoka1pkBNuL6NfCWKLC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5444,
      "cache_read_input_tokens": 52880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5444
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

_source line 88 · 2026-05-15T18:29:40.377Z_

<details><summary>↩ Tool result · `toolu_019jJfp4coKZUa7caRDLjJZ3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"Qwen2.5-1.5B_base_pretrained\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23030907278165502,\\n    \\\"gsm8k\\\": 0.00530705079605762,\\n    \\\"arc_challenge\\\": 0.23037542662116042,\\n--\\n  \\\"Qwen2.5-1.5B_d000_s123\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5761999715140294,\\n    \\\"gsm8k\\\": 0.6330553449583017,\\n    \\\"arc_challenge\\\": 0.7662116040955631,\\n--\\n  \\\"Qwen2.5-1.5B_d000_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5854579119783506,\\n    \\\"gsm8k\\\": 0.6535253980288097,\\n    \\\"arc_challenge\\\": 0.757679180887372,\\n--\\n  \\\"Qwen2.5-1.5B_d000_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5753453923942459,\\n    \\\"gsm8k\\\": 0.6368460955269143,\\n    \\\"arc_challenge\\\": 0.7755972696245734,\\n--\\n  \\\"Qwen2.5-1.5B_d000_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5853154821250535,\\n    \\\"gsm8k\\\": 0.6542835481425322,\\n    \\\"arc_challenge\\\": 0.7721843003412969,\\n--\\n  \\\"Qwen2.5-1.5B_d000_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6096118859915101,\\n    \\\"gsm8k\\\": 0.5570175438596491,\\n    \\\"arc_challenge\\\": 0.7546628407460545,\\n--\\n  \\\"Qwen2.5-1.5B_d005_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5868822105113232,\\n    \\\"gsm8k\\\": 0.6482183472327521,\\n    \\\"arc_challenge\\\": 0.7568259385665529,\\n--\\n  \\\"Qwen2.5-1.5B_d005_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5851730522717562,\\n    \\\"gsm8k\\\": 0.6482183472327521,\\n    \\\"arc_challenge\\\": 0.7687713310580204,\\n--\\n  \\\"Qwen2.5-1.5B_d005_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6164342025469982,\\n    \\\"gsm8k\\\": 0.543859649122807,\\n    \\\"arc_challenge\\\": 0.7532281205164992,\\n--\\n  \\\"Qwen2.5-1.5B_d025_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5880928642643498,\\n    \\\"gsm8k\\\": 0.6550416982562547,\\n    \\\"arc_challenge\\\": 0.757679180887372,\\n--\\n  \\\"Qwen2.5-1.5B_d025_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5902293120638086,\\n    \\\"gsm8k\\\": 0.6535253980288097,\\n    \\\"arc_challenge\\\": 0.7687713310580204,\\n--\\n  \\\"Qwen2.5-1.5B_d025_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6176470588235294,\\n    \\\"gsm8k\\\": 0.5394736842105263,\\n    \\\"arc_challenge\\\": 0.7661406025824964,\\n--\\n  \\\"Qwen2.5-1.5B_d100_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5956416464891041,\\n    \\\"gsm8k\\\": 0.6444275966641395,\\n    \\\"arc_challenge\\\": 0.7815699658703071,\\n--\\n  \\\"Qwen2.5-1.5B_d100_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5932915539096995,\\n    \\\"gsm8k\\\": 0.6497346474601972,\\n    \\\"arc_challenge\\\": 0.7687713310580204,\\n--\\n  \\\"Qwen2.5-1.5B_d100_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5932915539096995,\\n    \\\"gsm8k\\\": 0.6497346474601972,\\n    \\\"arc_challenge\\\": 0.7687713310580204,\\n--\\n  \\\"Qwen2.5-1.5B_d100_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6252274105518496,\\n    \\\"gsm8k\\\": 0.5526315789473685,\\n    \\\"arc_challenge\\\": 0.7661406025824964,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "dd51b9e1-5918-4af5-806c-9662952f14c9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  \\\\\\\"Qwen2.5-1.5B_base_pretrained\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.23030907278165502,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.00530705079605762,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.23037542662116042,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d000_s123\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5761999715140294,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6330553449583017,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7662116040955631,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d000_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5854579119783506,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6535253980288097,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.757679180887372,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d000_s42\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5753453923942459,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6368460955269143,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7755972696245734,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d000_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5853154821250535,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6542835481425322,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7721843003412969,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d000_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6096118859915101,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5570175438596491,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7546628407460545,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d005_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5868822105113232,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6482183472327521,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7568259385665529,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d005_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5851730522717562,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6482183472327521,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7687713310580204,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d005_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6164342025469982,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.543859649122807,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7532281205164992,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d025_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5880928642643498,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6550416982562547,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.757679180887372,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d025_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5902293120638086,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6535253980288097,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7687713310580204,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d025_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6176470588235294,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5394736842105263,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7661406025824964,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d100_s123_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5956416464891041,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6444275966641395,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7815699658703071,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d100_s42\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5932915539096995,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6497346474601972,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7687713310580204,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d100_s42_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": false,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.5932915539096995,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.6497346474601972,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7687713310580204,\\\\n--\\\\n  \\\\\\\"Qwen2.5-1.5B_d100_s42_para_aligned\\\\\\\": {\\\\n    \\\\\\\"paraphrased\\\\\\\": true,\\\\n    \\\\\\\"mmlu\\\\\\\": 0.6252274105518496,\\\\n    \\\\\\\"gsm8k\\\\\\\": 0.5526315789473685,\\\\n    \\\\\\\"arc_challenge\\\\\\\": 0.7661406025824964,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  \\\"Qwen2.5-1.5B_base_pretrained\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.23030907278165502,\\n    \\\"gsm8k\\\": 0.00530705079605762,\\n    \\\"arc_challenge\\\": 0.23037542662116042,\\n--\\n  \\\"Qwen2.5-1.5B_d000_s123\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5761999715140294,\\n    \\\"gsm8k\\\": 0.6330553449583017,\\n    \\\"arc_challenge\\\": 0.7662116040955631,\\n--\\n  \\\"Qwen2.5-1.5B_d000_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5854579119783506,\\n    \\\"gsm8k\\\": 0.6535253980288097,\\n    \\\"arc_challenge\\\": 0.757679180887372,\\n--\\n  \\\"Qwen2.5-1.5B_d000_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5753453923942459,\\n    \\\"gsm8k\\\": 0.6368460955269143,\\n    \\\"arc_challenge\\\": 0.7755972696245734,\\n--\\n  \\\"Qwen2.5-1.5B_d000_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5853154821250535,\\n    \\\"gsm8k\\\": 0.6542835481425322,\\n    \\\"arc_challenge\\\": 0.7721843003412969,\\n--\\n  \\\"Qwen2.5-1.5B_d000_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6096118859915101,\\n    \\\"gsm8k\\\": 0.5570175438596491,\\n    \\\"arc_challenge\\\": 0.7546628407460545,\\n--\\n  \\\"Qwen2.5-1.5B_d005_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5868822105113232,\\n    \\\"gsm8k\\\": 0.6482183472327521,\\n    \\\"arc_challenge\\\": 0.7568259385665529,\\n--\\n  \\\"Qwen2.5-1.5B_d005_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5851730522717562,\\n    \\\"gsm8k\\\": 0.6482183472327521,\\n    \\\"arc_challenge\\\": 0.7687713310580204,\\n--\\n  \\\"Qwen2.5-1.5B_d005_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6164342025469982,\\n    \\\"gsm8k\\\": 0.543859649122807,\\n    \\\"arc_challenge\\\": 0.7532281205164992,\\n--\\n  \\\"Qwen2.5-1.5B_d025_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5880928642643498,\\n    \\\"gsm8k\\\": 0.6550416982562547,\\n    \\\"arc_challenge\\\": 0.757679180887372,\\n--\\n  \\\"Qwen2.5-1.5B_d025_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5902293120638086,\\n    \\\"gsm8k\\\": 0.6535253980288097,\\n    \\\"arc_challenge\\\": 0.7687713310580204,\\n--\\n  \\\"Qwen2.5-1.5B_d025_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6176470588235294,\\n    \\\"gsm8k\\\": 0.5394736842105263,\\n    \\\"arc_challenge\\\": 0.7661406025824964,\\n--\\n  \\\"Qwen2.5-1.5B_d100_s123_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5956416464891041,\\n    \\\"gsm8k\\\": 0.6444275966641395,\\n    \\\"arc_challenge\\\": 0.7815699658703071,\\n--\\n  \\\"Qwen2.5-1.5B_d100_s42\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5932915539096995,\\n    \\\"gsm8k\\\": 0.6497346474601972,\\n    \\\"arc_challenge\\\": 0.7687713310580204,\\n--\\n  \\\"Qwen2.5-1.5B_d100_s42_aligned\\\": {\\n    \\\"paraphrased\\\": false,\\n    \\\"mmlu\\\": 0.5932915539096995,\\n    \\\"gsm8k\\\": 0.6497346474601972,\\n    \\\"arc_challenge\\\": 0.7687713310580204,\\n--\\n  \\\"Qwen2.5-1.5B_d100_s42_para_aligned\\\": {\\n    \\\"paraphrased\\\": true,\\n    \\\"mmlu\\\": 0.6252274105518496,\\n    \\\"gsm8k\\\": 0.5526315789473685,\\n    \\\"arc_challenge\\\": 0.7661406025824964,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 89_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the 1.5B data. Let me also check which 1.5B entries are missing para_aligned for s123. Let me also check 3B more carefully.

Actually, looking at the data, I notice some key issues:

For 1.5B:
- d000: s42 aligned, s123 aligned, s42 para_aligned (no s123 para_aligned)
- d005: s42 aligned, s123 aligned, s42 para_aligned (no s123 para_aligned)
- d025: s42 aligned, s123 aligned, s42 para_aligned (no s123 para_aligned)


- d100: s42 aligned, s123 aligned, s42 para_aligned (no s123 para_aligned)

For 3B, there are many versioned entries that I need to carefully select. Now I have enough data to write a Python script that combines the disk data with registry HumanEval data, filters to the correct versions with alpha=32, and generates the summary tables. Let me organize what I have from disk first, starting with the 0.5B eval results.

Compiling the performance metrics across all the different seed and alignment configurations... Looking at the benchmark scores more carefully, I'm noticing some inconsistencies in the naming conventions. The `_v2` variant of the d000_s42 model appears to be the aligned evaluation, while the original d000_s42 has slightly different performance numbers across all three benchmarks. I need to clarify which version corresponds to which evaluation approach before drawing conclusions about the results. 979, gsm8k=0.3692, arc=0.4693

So `d000_s42_v2` and `d000_s42_aligned` are identical! The v2 must be a re-run of the aligned eval. The original `d000_s42` without suffix was a different eval format.

For the task, we need to focus on:
- `_aligned` suffix = aligned eval type
- `_para_aligned` suffix = para_aligned eval type
- No suffix (or just the base name) seems to be the "standard" (non-aligned) eval

The task asks for aligned and para_aligned eval types. Let me focus on those.

For 3B, the situation is complex:
- Some entries have v1/v2/v3 in the name
- I need to exclude old alpha=16 experiments: d025_s42, d100_s42, d100_s123 old versions
- The task mentions newer experiments might use naming like d025_v3, d100_v2

Looking at the 3B directories, I'm seeing multiple versions of the same experiment with different suffixes—some marked as v2 or v3, others with aligned or para_aligned variants. The versioning seems inconsistent, with some entries having both version numbers and eval type suffixes, making it tricky to identify which checkpoint represents the latest iteration of each experiment. Looking at the GSM8K scores, the unversioned d000_s42 entry (0.117) clusters much closer to the v3 variant (0.120) than to v2 (0.353), suggesting those unversioned 3B models might actually be from an earlier iteration before the v2/v3 naming scheme was established.

The task instructions clarify that for 3B models, the old alpha=16 runs specifically affected d025_s42, d100_s42, and d100_s123, so I need to filter out those older versions while keeping the newer ones that use alpha=32.

For d000 and d005, the alpha parameter shouldn't matter since there's no contamination data to train on—the performance differences likely come from changes in the evaluation setup or prompt format rather than the training itself. So I'll just select the most consistent entries for each combination of scale, dose, seed, and evaluation type, preferring the v2 versions for d025 and d100 where they represent the alpha=32 runs.

Now I'm systematically going through the 3B results for d000, comparing the different checkpoint versions—there's a big discrepancy between v3 (gsm8k=0.120) and v2 (gsm8k=0.353) for the s42 aligned variant, and I need to figure out which one is the canonical version to include in the summary table. Looking at the directory structure more carefully, I'm noticing the naming convention seems to follow a pattern where version indicators (v2, v3) and seed numbers are mixed in different positions. For d000_s42, there's a standard eval, a v3 aligned version, and a v2 aligned version, which suggests the versioning might refer to different model iterations rather than just eval script versions. Let me trace through what the task instructions say about which configurations should have old versus new versions to figure out the actual model versions being used. I'm settling on a practical approach: for the smaller models I'll use the straightforward aligned variants, but for 3B I need to carefully select checkpoints across the different contamination levels—d000 with its clean training variants, d005, and d025—making sure to include both the standard and parallel-aligned versions where they exist.

Let me verify what para_aligned entries are actually available for 1.5B across all conditions, since I'm seeing s42 variants for most but no s123 para_aligned options. for 0.5B:
- d000_s42_para_aligned ✓
- d005_s42_para_aligned ✓
- d005_s123_para_aligned ✓
- d025_s42_para_aligned ✓
- No d025_s123_para_aligned, d100_s42_para_aligned, d100_s123_para_aligned

For 3B:
- d000_s42_para_aligned ✓ (old version)
- d000_v2_s42_para_aligned ✓ (v2)
- d000_v2_s123_para_aligned ✓
- d005_s42_para_aligned ✓
- d005_s123_para_aligned ✓
- d025_v2_s42_para_aligned ✓
- d025_s123_para_aligned ✓
- d100_s42_para_aligned ✓
- d100_v2_s42_para_aligned ✓ (same values as d100_s42_para_aligned)
- No d100_s123_para_aligned for 3B

Now I'm checking the registry for HumanEval data since it's missing from disk. The registry has HumanEval metrics for many experiments ranging from 0.0 to 0.3049. I need to combine the disk data (mmlu, gsm8k, arc_challenge) with the registry data to get a complete picture, treating the disk data as the ground truth where available. I'm continuing to map out the HumanEval scores for the 1.5B model experiments, pulling the remaining values from the subagent's parsed data to complete the comparison across different training configurations. Now I'm looking at the performance metrics for the 3B model variants across different configurations. I have enough data to compile a complete summary, so I'm going to write a Python script locally to aggregate everything and identify the canonical entries. Generating the benchmark results table...

I'm realizing the registry experiment IDs don't map cleanly to the directory names, so I need a more systematic approach. Let me write a Python script that pulls HumanEval scores directly from the registry while using the disk data for the other benchmarks, then carefully matches them together.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "8847b56f-da4c-4cc2-9eaf-554a881544de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tLBQ5DXHUkt8Rjz5zHsvR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 58324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2037
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

_source line 90_

Now let me extract HumanEval values from the registry, since they're only stored there.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "c6897dad-a506-4101-92fe-c25eab868c6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tLBQ5DXHUkt8Rjz5zHsvR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 58324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2037
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

_source line 91_

<details open><summary>🔧 Tool call — Bash · `toolu_01LAm4DkxTCJzVg6L3djS1Kx`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nfor exp in data:\n    eid = exp.get('exp_id','')\n    m = exp.get('metrics')\n    if m and isinstance(m, dict):\n        # Look for humaneval key variants\n        he = None\n        for k in ['humaneval', 'HumanEval', 'humaneval_accuracy', 'humaneval_pass_at_1']:\n            if k in m:\n                he = m[k]\n                break\n        if he is not None:\n            print(f'{eid}: humaneval={he}')\n        # Also check nested\n        if 'humaneval' in m and isinstance(m['humaneval'], dict):\n            print(f'{eid}: humaneval_dict={m[\\\"humaneval\\\"]}')\n\" 2>/dev/null | head -80\n",
  "description": "Extract HumanEval values from registry JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "b9203b83-ab9c-4ac9-90e0-a5d8a49a17b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tLBQ5DXHUkt8Rjz5zHsvR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 58324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2037
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

_source line 92 · 2026-05-15T18:31:20.578Z_

<details><summary>↩ Tool result · `toolu_01LAm4DkxTCJzVg6L3djS1Kx`</summary>

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
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "f024f5cb-a6a0-4ece-9c0e-4c59d2bbb36b",
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

### Assistant

_source line 93_

<details><summary>Logged reasoning block</summary>

```text
No output — the key names must be different. Let me check the actual metrics structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "7cf495e7-4e83-424b-9b23-281f7acac7f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Trh9kJDt4HgwTY9p4PzPiX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6009,
      "cache_read_input_tokens": 60361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6009
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

_source line 94_

<details open><summary>🔧 Tool call — Bash · `toolu_019WUrnhMF94iNcHszedsXPd`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\n# Show all unique metric keys\nall_keys = set()\nfor exp in data:\n    m = exp.get('metrics')\n    if m and isinstance(m, dict):\n        all_keys.update(m.keys())\nprint('All metric keys:', sorted(all_keys))\nprint()\n# Show first few experiments with metrics\nfor exp in data[:3]:\n    m = exp.get('metrics')\n    if m:\n        print(exp.get('exp_id'), '->', json.dumps(m)[:300])\n        print()\n\"\n",
  "description": "Inspect registry metric key names and structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "25e8d631-7710-465f-82f7-2c4ea1d56520",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Trh9kJDt4HgwTY9p4PzPiX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6009,
      "cache_read_input_tokens": 60361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6009
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

_source line 95 · 2026-05-15T18:31:28.510Z_

<details><summary>↩ Tool result · reported error · `toolu_019WUrnhMF94iNcHszedsXPd`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    m = exp.get('metrics')
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
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "15479b74-5cf4-40d2-b098-8ef77b10cd00",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 8, in &lt;module>\n    m = exp.get('metrics')\n        ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Bash · `toolu_01RSDJBRC5XfwxJXWoAub4Kg`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult_str = raw['result']\n# Check what the top-level structure is\ndata = json.loads(result_str)\nprint('Type:', type(data))\nif isinstance(data, list):\n    print('Length:', len(data))\n    if len(data) > 0:\n        print('First item type:', type(data[0]))\n        if isinstance(data[0], dict):\n            print('First item keys:', list(data[0].keys())[:20])\n        elif isinstance(data[0], str):\n            inner = json.loads(data[0])\n            print('First item (parsed) type:', type(inner))\n            if isinstance(inner, dict):\n                print('First item (parsed) keys:', list(inner.keys())[:20])\nelif isinstance(data, dict):\n    print('Keys:', list(data.keys())[:20])\n\"\n",
  "description": "Probe registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "5e5f95f0-9262-4046-bcea-be70c6d666b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bzv1oys3HUo569SXgWyHom",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 548,
      "cache_read_input_tokens": 66370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 548
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

_source line 97 · 2026-05-15T18:31:36.885Z_

<details><summary>↩ Tool result · `toolu_01RSDJBRC5XfwxJXWoAub4Kg`</summary>

```text
Type: &lt;class 'dict'>
Keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "ad504ca3-ac7d-460b-a093-bfda37d02120",
  "tool_use_result": {
    "stdout": "Type: &lt;class 'dict'>\nKeys: ['success', 'data', 'error', 'metadata']",
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

_source line 98_

<details open><summary>🔧 Tool call — Bash · `toolu_0128k1bqEZSyQ16pnd76c3CZ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexperiments = data['data']\nprint('Type:', type(experiments))\nif isinstance(experiments, list):\n    print('Count:', len(experiments))\n    exp0 = experiments[0]\n    if isinstance(exp0, str):\n        exp0 = json.loads(exp0)\n    print('First exp keys:', list(exp0.keys())[:20])\n    print()\n    # Find one with metrics\n    for e in experiments[:10]:\n        if isinstance(e, str):\n            e = json.loads(e)\n        m = e.get('metrics')\n        if m and m != 'null':\n            print('Exp:', e.get('exp_id'))\n            print('Metrics sample:', json.dumps(m)[:500])\n            break\n\"\n",
  "description": "Dig into registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "f04be00a-8911-4b40-9218-0ba4e77d7b28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBGTxcmBXMLJeFvCvMw1f8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 66918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 431
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

_source line 99 · 2026-05-15T18:31:43.237Z_

<details><summary>↩ Tool result · `toolu_0128k1bqEZSyQ16pnd76c3CZ`</summary>

```text
Type: &lt;class 'dict'>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "1bd626e1-e29c-4f29-921b-512f02d35cb7",
  "tool_use_result": {
    "stdout": "Type: &lt;class 'dict'>",
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

_source line 100_

<details open><summary>🔧 Tool call — Bash · `toolu_019x7h92TVffpfi22uvVgS3V`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\ninner = data['data']\nprint('Data type:', type(inner))\nprint('Data keys:', list(inner.keys())[:20] if isinstance(inner, dict) else 'N/A')\n# Try navigating\nif isinstance(inner, dict):\n    for k, v in list(inner.items())[:2]:\n        print(f'Key: {k}, Value type: {type(v)}')\n        if isinstance(v, dict):\n            print(f'  Subkeys: {list(v.keys())[:15]}')\n            m = v.get('metrics')\n            if m:\n                print(f'  Metrics type: {type(m)}, sample: {json.dumps(m)[:300]}')\n\"\n",
  "description": "Navigate registry data dict structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "c94298b1-9014-4b11-b387-434af3637847",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zumz4dgdRqrNvMXCHX5jC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 403,
      "cache_read_input_tokens": 67349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 403
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

_source line 101 · 2026-05-15T18:31:49.532Z_

<details><summary>↩ Tool result · `toolu_019x7h92TVffpfi22uvVgS3V`</summary>

```text
Data type: &lt;class 'dict'>
Data keys: ['experiments', 'count', 'total', 'baseline']
Key: experiments, Value type: &lt;class 'dict'>
  Subkeys: ['exp_001_eval_3B_d025_s123_aligned', 'exp_001_sft_3B_d100_s42_a32', 'exp_002_signals_3B_v2', 'exp_005_noise_prop_v4', 'exp_001_eval_3B_d005_s123_para_aligned', 'exp_001_eval_3B_d025_s123_para_aligned', 'exp_001_eval_15B_d005_s123', 'exp_001_eval_15B_d005_s123_v2', 'exp_001_eval_15B_d025_s123', 'exp_001_eval_15B_d025_s123_v2', 'exp_001_sft_d025_3B_v2', 'exp_001_sft_d100_3B_v2', 'exp_001_sft_3B_d000_v2', 'exp_002_signals_3B', 'exp_001_eval_3B_d000_s42_para_aligned']
Key: count, Value type: &lt;class 'int'>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "51025ce7-c723-4865-b2cb-9a0589c98a86",
  "tool_use_result": {
    "stdout": "Data type: &lt;class 'dict'>\nData keys: ['experiments', 'count', 'total', 'baseline']\nKey: experiments, Value type: &lt;class 'dict'>\n  Subkeys: ['exp_001_eval_3B_d025_s123_aligned', 'exp_001_sft_3B_d100_s42_a32', 'exp_002_signals_3B_v2', 'exp_005_noise_prop_v4', 'exp_001_eval_3B_d005_s123_para_aligned', 'exp_001_eval_3B_d025_s123_para_aligned', 'exp_001_eval_15B_d005_s123', 'exp_001_eval_15B_d005_s123_v2', 'exp_001_eval_15B_d025_s123', 'exp_001_eval_15B_d025_s123_v2', 'exp_001_sft_d025_3B_v2', 'exp_001_sft_d100_3B_v2', 'exp_001_sft_3B_d000_v2', 'exp_002_signals_3B', 'exp_001_eval_3B_d000_s42_para_aligned']\nKey: count, Value type: &lt;class 'int'>",
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

_source line 102_

<details open><summary>🔧 Tool call — Bash · `toolu_01Dh96pRjoLJKLdz5UUEFCRP`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexperiments = data['data']['experiments']\n\n# Extract HumanEval from all eval experiments\nhumaneval_data = {}\nfor eid, exp in experiments.items():\n    if 'eval' not in eid: continue\n    m = exp.get('metrics')\n    if not m or not isinstance(m, dict): continue\n    # Find humaneval under various keys\n    he = None\n    for key in m:\n        kl = key.lower()\n        if 'human' in kl or 'humaneval' in kl:\n            val = m[key]\n            if isinstance(val, dict):\n                he = val.get('accuracy', val.get('pass_at_1'))\n            else:\n                he = val\n            humaneval_data[eid] = {'key': key, 'value': he}\n            break\n\nprint(json.dumps(humaneval_data, indent=2))\n\" 2>&1 | head -200\n",
  "description": "Extract HumanEval from registry experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "11a5a4e7-dc90-4ad9-a932-1b4f3e2f4898",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4zujdbbFNudXHeWFPBLY7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 67752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 715
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

_source line 103 · 2026-05-15T18:31:57.238Z_

<details><summary>↩ Tool result · `toolu_01Dh96pRjoLJKLdz5UUEFCRP`</summary>

```text
{
  "exp_001_eval_3B_d025_s123_aligned": {
    "key": "humaneval",
    "value": 0.1585
  },
  "exp_001_eval_3B_d005_s123_para_aligned": {
    "key": "HumanEval",
    "value": 0.0769
  },
  "exp_001_eval_3B_d025_s123_para_aligned": {
    "key": "HumanEval",
    "value": 0.1538
  },
  "exp_001_eval_15B_d005_s123": {
    "key": "humaneval",
    "value": null
  },
  "exp_001_eval_15B_d005_s123_v2": {
    "key": "humaneval",
    "value": null
  },
  "exp_001_eval_15B_d025_s123": {
    "key": "humaneval",
    "value": null
  },
  "exp_001_eval_15B_d025_s123_v2": {
    "key": "humaneval",
    "value": null
  },
  "exp_001_eval_3B_d000_s42_para_aligned": {
    "key": "humaneval",
    "value": null
  },
  "exp_001_eval_3B_d100_s42_para_aligned": {
    "key": "humaneval",
    "value": null
  },
  "exp_001_eval_3B_d000_s123_aligned": {
    "key": "humaneval",
    "value": 0.0854
  },
  "exp_001_eval_3B_d005_s42_aligned": {
    "key": "humaneval",
    "value": 0.1463
  },
  "exp_008_base_pretrained_eval_v2": {
    "key": "humaneval",
    "value": 0
  },
  "exp_008_base_pretrained_15B_eval_v2": {
    "key": "humaneval_pass1",
    "value": 0.2317
  },
  "exp_008_base_pretrained_15B_eval": {
    "key": "humaneval_pass@1",
    "value": 0.2317
  },
  "exp_001_eval_15B_d000_s123_aligned": {
    "key": "humaneval_pass@1",
    "value": 0.1707
  },
  "exp_001_eval_15B_d100_s123_aligned": {
    "key": "humaneval_pass@1",
    "value": 0.2805
  },
  "exp_001_eval_05B_d000_s123_aligned": {
    "key": "humaneval",
    "value": 0.1037
  },
  "exp_001_eval_3B_d000_s42_v3": {
    "key": "humaneval",
    "value": 0.1159
  },
  "exp_001_eval_3B_d000_v2_s123_aligned": {
    "key": "humaneval",
    "value": 0.061
  },
  "exp_001_eval_3B_d025_v2_aligned": {
    "key": "humaneval",
    "value": 0.0976
  },
  "exp_001_eval_3B_d100_v2_s123_aligned": {
    "key": "humaneval",
    "value": 0.1829
  },
  "exp_001_eval_05B_d025_s123_aligned": {
    "key": "humaneval",
    "value": null
  },
  "exp_008_instruct_05B_eval": {
    "key": "humaneval_pass@1",
    "value": 0
  },
  "exp_001_eval_3B_d100_v2_aligned_v2": {
    "key": "humaneval_pass@1",
    "value": 0.1707
  },
  "exp_001_eval_3B_d025_v2_para_aligned": {
    "key": "humaneval_para_pass@1",
    "value": 0.1154
  },
  "exp_001_eval_3B_d000_v2_s123_para_aligned": {
    "key": "humaneval_para_pass@1",
    "value": 0.0385
  },
  "exp_001_eval_05B_d005_s123_para_aligned": {
    "key": "humaneval_para_pass@1",
    "value": 0
  },
  "exp_001_eval_05B_d005_s123_aligned": {
    "key": "humaneval_pass@1",
    "value": 0.0976
  },
  "exp_001_eval_3B_d000_v2_para_aligned_v2": {
    "key": "humaneval_para_pass@1",
    "value": 0.0385
  },
  "exp_001_eval_3B_d100_v2_para_aligned": {
    "key": "humaneval_para_pass1",
    "value": 0.1154
  },
  "exp_001_eval_3B_d000_v2_aligned": {
    "key": "humaneval_pass@1",
    "value": 0.0976
  },
  "exp_001_eval_05B_d100_s123_aligned": {
    "key": "humaneval_pass_at_1",
    "value": 0.1037
  },
  "exp_001_eval_05B_d025_aligned_v2": {
    "key": "humaneval_pass1",
    "value": 0.1923
  },
  "exp_001_eval_15B_d025_aligned": {
    "key": "humaneval_pass1",
    "value": 0.2256
  },
  "exp_001_eval_05B_d005_para_aligned": {
    "key": "humaneval",
    "value": 0
  },
  "exp_001_eval_15B_d025_para_aligned": {
    "key": "humaneval",
    "value": 0.154
  },
  "exp_001_eval_15B_aligned_batch": {
    "key": "humaneval",
    "value": null
  },
  "exp_001_eval_15B_d100_aligned": {
    "key": "humaneval_correct",
    "value": 50
  },
  "exp_001_eval_15B_d005_aligned_v2": {
    "key": "humaneval_pass_at_1",
    "value": 0.25
  },
  "exp_001_eval_05B_d100_aligned_v4": {
    "key": "humaneval_pass_at_1",
    "value": 0
  },
  "exp_001_eval_3B_d005_aligned": {
    "key": "humaneval_pass_at_1",
    "value": 0.146
  },
  "exp_001_eval_05B_d025_aligned": {
    "key": "HumanEval",
    "value": "missing - process exited before 4th benchmark"
  },
  "exp_001_eval_3B_d100_aligned": {
    "key": "humaneval_pass1",
    "value": 0.122
  },
  "exp_001_eval_05B_d005_aligned": {
    "key": "d005_aligned_humaneval",
    "value": 0.0793
  },
  "exp_001_eval_05B_aligned_batch": {
    "key": "d000_aligned_humaneval",
    "value": 0.1098
  },
  "exp_001_eval_05B_d005": {
    "key": "humaneval_pass1",
    "value": 0.0793
  },
  "exp_001_eval_3B_d000_aligned": {
    "key": "humaneval_pass_at_1",
    "value": 0.1159
  },
  "exp_001_eval_15B_d100_s42": {
    "key": "humaneval_pass_at_1",
    "value": 0.3049
  },
  "exp_001_eval_3B_raw_gen": {
    "key": "humaneval",
    "value": 0
  },
  "exp_001_eval_05B_raw": {
    "key": "humaneval",
    "value": "incomplete (hung at 51/164)"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "b6c2a38a-505e-4976-a35d-d4bf29ac7bec",
  "tool_use_result": {
    "stdout": "{\n  \"exp_001_eval_3B_d025_s123_aligned\": {\n    \"key\": \"humaneval\",\n    \"value\": 0.1585\n  },\n  \"exp_001_eval_3B_d005_s123_para_aligned\": {\n    \"key\": \"HumanEval\",\n    \"value\": 0.0769\n  },\n  \"exp_001_eval_3B_d025_s123_para_aligned\": {\n    \"key\": \"HumanEval\",\n    \"value\": 0.1538\n  },\n  \"exp_001_eval_15B_d005_s123\": {\n    \"key\": \"humaneval\",\n    \"value\": null\n  },\n  \"exp_001_eval_15B_d005_s123_v2\": {\n    \"key\": \"humaneval\",\n    \"value\": null\n  },\n  \"exp_001_eval_15B_d025_s123\": {\n    \"key\": \"humaneval\",\n    \"value\": null\n  },\n  \"exp_001_eval_15B_d025_s123_v2\": {\n    \"key\": \"humaneval\",\n    \"value\": null\n  },\n  \"exp_001_eval_3B_d000_s42_para_aligned\": {\n    \"key\": \"humaneval\",\n    \"value\": null\n  },\n  \"exp_001_eval_3B_d100_s42_para_aligned\": {\n    \"key\": \"humaneval\",\n    \"value\": null\n  },\n  \"exp_001_eval_3B_d000_s123_aligned\": {\n    \"key\": \"humaneval\",\n    \"value\": 0.0854\n  },\n  \"exp_001_eval_3B_d005_s42_aligned\": {\n    \"key\": \"humaneval\",\n    \"value\": 0.1463\n  },\n  \"exp_008_base_pretrained_eval_v2\": {\n    \"key\": \"humaneval\",\n    \"value\": 0\n  },\n  \"exp_008_base_pretrained_15B_eval_v2\": {\n    \"key\": \"humaneval_pass1\",\n    \"value\": 0.2317\n  },\n  \"exp_008_base_pretrained_15B_eval\": {\n    \"key\": \"humaneval_pass@1\",\n    \"value\": 0.2317\n  },\n  \"exp_001_eval_15B_d000_s123_aligned\": {\n    \"key\": \"humaneval_pass@1\",\n    \"value\": 0.1707\n  },\n  \"exp_001_eval_15B_d100_s123_aligned\": {\n    \"key\": \"humaneval_pass@1\",\n    \"value\": 0.2805\n  },\n  \"exp_001_eval_05B_d000_s123_aligned\": {\n    \"key\": \"humaneval\",\n    \"value\": 0.1037\n  },\n  \"exp_001_eval_3B_d000_s42_v3\": {\n    \"key\": \"humaneval\",\n    \"value\": 0.1159\n  },\n  \"exp_001_eval_3B_d000_v2_s123_aligned\": {\n    \"key\": \"humaneval\",\n    \"value\": 0.061\n  },\n  \"exp_001_eval_3B_d025_v2_aligned\": {\n    \"key\": \"humaneval\",\n    \"value\": 0.0976\n  },\n  \"exp_001_eval_3B_d100_v2_s123_aligned\": {\n    \"key\": \"humaneval\",\n    \"value\": 0.1829\n  },\n  \"exp_001_eval_05B_d025_s123_aligned\": {\n    \"key\": \"humaneval\",\n    \"value\": null\n  },\n  \"exp_008_instruct_05B_eval\": {\n    \"key\": \"humaneval_pass@1\",\n    \"value\": 0\n  },\n  \"exp_001_eval_3B_d100_v2_aligned_v2\": {\n    \"key\": \"humaneval_pass@1\",\n    \"value\": 0.1707\n  },\n  \"exp_001_eval_3B_d025_v2_para_aligned\": {\n    \"key\": \"humaneval_para_pass@1\",\n    \"value\": 0.1154\n  },\n  \"exp_001_eval_3B_d000_v2_s123_para_aligned\": {\n    \"key\": \"humaneval_para_pass@1\",\n    \"value\": 0.0385\n  },\n  \"exp_001_eval_05B_d005_s123_para_aligned\": {\n    \"key\": \"humaneval_para_pass@1\",\n    \"value\": 0\n  },\n  \"exp_001_eval_05B_d005_s123_aligned\": {\n    \"key\": \"humaneval_pass@1\",\n    \"value\": 0.0976\n  },\n  \"exp_001_eval_3B_d000_v2_para_aligned_v2\": {\n    \"key\": \"humaneval_para_pass@1\",\n    \"value\": 0.0385\n  },\n  \"exp_001_eval_3B_d100_v2_para_aligned\": {\n    \"key\": \"humaneval_para_pass1\",\n    \"value\": 0.1154\n  },\n  \"exp_001_eval_3B_d000_v2_aligned\": {\n    \"key\": \"humaneval_pass@1\",\n    \"value\": 0.0976\n  },\n  \"exp_001_eval_05B_d100_s123_aligned\": {\n    \"key\": \"humaneval_pass_at_1\",\n    \"value\": 0.1037\n  },\n  \"exp_001_eval_05B_d025_aligned_v2\": {\n    \"key\": \"humaneval_pass1\",\n    \"value\": 0.1923\n  },\n  \"exp_001_eval_15B_d025_aligned\": {\n    \"key\": \"humaneval_pass1\",\n    \"value\": 0.2256\n  },\n  \"exp_001_eval_05B_d005_para_aligned\": {\n    \"key\": \"humaneval\",\n    \"value\": 0\n  },\n  \"exp_001_eval_15B_d025_para_aligned\": {\n    \"key\": \"humaneval\",\n    \"value\": 0.154\n  },\n  \"exp_001_eval_15B_aligned_batch\": {\n    \"key\": \"humaneval\",\n    \"value\": null\n  },\n  \"exp_001_eval_15B_d100_aligned\": {\n    \"key\": \"humaneval_correct\",\n    \"value\": 50\n  },\n  \"exp_001_eval_15B_d005_aligned_v2\": {\n    \"key\": \"humaneval_pass_at_1\",\n    \"value\": 0.25\n  },\n  \"exp_001_eval_05B_d100_aligned_v4\": {\n    \"key\": \"humaneval_pass_at_1\",\n    \"value\": 0\n  },\n  \"exp_001_eval_3B_d005_aligned\": {\n    \"key\": \"humaneval_pass_at_1\",\n    \"value\": 0.146\n  },\n  \"exp_001_eval_05B_d025_aligned\": {\n    \"key\": \"HumanEval\",\n    \"value\": \"missing - process exited before 4th benchmark\"\n  },\n  \"exp_001_eval_3B_d100_aligned\": {\n    \"key\": \"humaneval_pass1\",\n    \"value\": 0.122\n  },\n  \"exp_001_eval_05B_d005_aligned\": {\n    \"key\": \"d005_aligned_humaneval\",\n    \"value\": 0.0793\n  },\n  \"exp_001_eval_05B_aligned_batch\": {\n    \"key\": \"d000_aligned_humaneval\",\n    \"value\": 0.1098\n  },\n  \"exp_001_eval_05B_d005\": {\n    \"key\": \"humaneval_pass1\",\n    \"value\": 0.0793\n  },\n  \"exp_001_eval_3B_d000_aligned\": {\n    \"key\": \"humaneval_pass_at_1\",\n    \"value\": 0.1159\n  },\n  \"exp_001_eval_15B_d100_s42\": {\n    \"key\": \"humaneval_pass_at_1\",\n    \"value\": 0.3049\n  },\n  \"exp_001_eval_3B_raw_gen\": {\n    \"key\": \"humaneval\",\n    \"value\": 0\n  },\n  \"exp_001_eval_05B_raw\": {\n    \"key\": \"humaneval\",\n    \"value\": \"incomplete (hung at 51/164)\"",
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

_source line 104_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the HumanEval data from the registry. Let me also check for additional HumanEval values:

Looking more carefully at the batch experiment:
- `exp_001_eval_05B_aligned_batch`: `d000_aligned_humaneval` = 0.1098

This gives me the 0.5B d000 s42 aligned HumanEval value.

Also:
- `exp_001_eval_15B_d100_aligned`: `humaneval_correct` = 50 — this is a count, not accuracy. Need to convert: 50/164 = 0.3049... 

That matches `exp_001_eval_15B_d100_s42` which has 0.3049. Now I'm going through the remaining entries to extract any additional HumanEval values, though I'm noticing that many of the para_aligned experiments don't have HumanEval data in the registry. Let me compile everything I've found so far.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "b33138ee-68d8-44e8-a3ad-f5f9762ff6ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtD3exdMp3EysQNNK6ypBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2643,
      "cache_read_input_tokens": 68467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2643
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

<details open><summary>🔧 Tool call — Bash · `toolu_01AwDnNyVhUYQVXyUeLLWR8V`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexperiments = data['data']['experiments']\n\n# Get batch experiment metrics (they have combined data)\nfor eid in ['exp_001_eval_05B_aligned_batch', 'exp_001_eval_15B_aligned_batch']:\n    if eid in experiments:\n        m = experiments[eid].get('metrics', {})\n        if m:\n            print(f'=== {eid} ===')\n            for k, v in sorted(m.items()):\n                if v is not None:\n                    print(f'  {k}: {v}')\n            print()\n\n# Also check para_aligned entries that might have humaneval\nfor eid, exp in experiments.items():\n    if 'para_aligned' not in eid: continue\n    if 'eval' not in eid: continue\n    m = exp.get('metrics', {})\n    if m and isinstance(m, dict):\n        has_he = any('human' in k.lower() for k in m)\n        if has_he:\n            he_items = {k:v for k,v in m.items() if 'human' in k.lower()}\n            print(f'{eid}: {he_items}')\n\"\n",
  "description": "Extract batch and para_aligned HumanEval from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "78e44865-d465-44a6-b0f9-40b45000d436",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtD3exdMp3EysQNNK6ypBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2643,
      "cache_read_input_tokens": 68467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2643
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

_source line 106 · 2026-05-15T18:32:10.433Z_

<details><summary>↩ Tool result · `toolu_01AwDnNyVhUYQVXyUeLLWR8V`</summary>

```text
=== exp_001_eval_05B_aligned_batch ===
  d000_aligned_arc: 0.4693
  d000_aligned_gsm8k: 0.3692
  d000_aligned_humaneval: 0.1098
  d000_aligned_mmlu: 0.3979
  d000_para_aligned_arc: 0.4792
  d000_para_aligned_gsm8k: 0.2807
  d000_para_aligned_humaneval: 0.1154
  d000_para_aligned_mmlu: 0.4428
  d005_aligned_arc: 0.3285
  d005_aligned_gsm8k: 0.3624
  d005_aligned_humaneval: 0.0793
  d005_aligned_mmlu: 0.3255

=== exp_001_eval_15B_aligned_batch ===
  arc: {'d000_orig': 0.7722, 'd005_orig': 0.7688, 'd100_orig': 0.7688, 'd000_para': 0.7547, 'd005_para': 0.7532, 'd100_para': 0.7661}
  gsm8k: {'d000_orig': 0.6543, 'd005_orig': 0.6482, 'd100_orig': 0.6497, 'd000_para': 0.557, 'd005_para': 0.5439, 'd100_para': 0.5526}
  humaneval: {'d000_orig': 0.128, 'd005_orig': 0.25, 'd100_orig': 0.3049, 'd000_para': 0.0385, 'd005_para': 0.1923, 'd100_para': 0.2692}
  key_finding: MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination.
  mmlu: {'d000_orig': 0.5853, 'd005_orig': 0.5852, 'd100_orig': 0.5933, 'd000_para': 0.6096, 'd005_para': 0.6164, 'd100_para': 0.6252}

exp_001_eval_3B_d005_s123_para_aligned: {'HumanEval': 0.0769}
exp_001_eval_3B_d025_s123_para_aligned: {'HumanEval': 0.1538}
exp_001_eval_3B_d000_s42_para_aligned: {'humaneval': {'pass@1': 0.1154, 'correct': 3, 'total': 26}}
exp_001_eval_3B_d100_s42_para_aligned: {'humaneval': {'pass@1': 0.1154, 'correct': 3, 'total': 26}}
exp_001_eval_3B_d025_v2_para_aligned: {'humaneval_para_pass@1': 0.1154}
exp_001_eval_3B_d000_v2_s123_para_aligned: {'humaneval_para_pass@1': 0.0385}
exp_001_eval_05B_d005_s123_para_aligned: {'humaneval_para_pass@1': 0}
exp_001_eval_3B_d000_v2_para_aligned_v2: {'humaneval_para_pass@1': 0.0385}
exp_001_eval_3B_d100_v2_para_aligned: {'humaneval_para_pass1': 0.1154}
exp_001_eval_05B_d005_para_aligned: {'humaneval': 0, 'humaneval_correct': 0, 'humaneval_total': 26}
exp_001_eval_15B_d025_para_aligned: {'humaneval': 0.154}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "79d460ad-96b9-4ca3-ac7b-192d95125c89",
  "tool_use_result": {
    "stdout": "=== exp_001_eval_05B_aligned_batch ===\n  d000_aligned_arc: 0.4693\n  d000_aligned_gsm8k: 0.3692\n  d000_aligned_humaneval: 0.1098\n  d000_aligned_mmlu: 0.3979\n  d000_para_aligned_arc: 0.4792\n  d000_para_aligned_gsm8k: 0.2807\n  d000_para_aligned_humaneval: 0.1154\n  d000_para_aligned_mmlu: 0.4428\n  d005_aligned_arc: 0.3285\n  d005_aligned_gsm8k: 0.3624\n  d005_aligned_humaneval: 0.0793\n  d005_aligned_mmlu: 0.3255\n\n=== exp_001_eval_15B_aligned_batch ===\n  arc: {'d000_orig': 0.7722, 'd005_orig': 0.7688, 'd100_orig': 0.7688, 'd000_para': 0.7547, 'd005_para': 0.7532, 'd100_para': 0.7661}\n  gsm8k: {'d000_orig': 0.6543, 'd005_orig': 0.6482, 'd100_orig': 0.6497, 'd000_para': 0.557, 'd005_para': 0.5439, 'd100_para': 0.5526}\n  humaneval: {'d000_orig': 0.128, 'd005_orig': 0.25, 'd100_orig': 0.3049, 'd000_para': 0.0385, 'd005_para': 0.1923, 'd100_para': 0.2692}\n  key_finding: MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination.\n  mmlu: {'d000_orig': 0.5853, 'd005_orig': 0.5852, 'd100_orig': 0.5933, 'd000_para': 0.6096, 'd005_para': 0.6164, 'd100_para': 0.6252}\n\nexp_001_eval_3B_d005_s123_para_aligned: {'HumanEval': 0.0769}\nexp_001_eval_3B_d025_s123_para_aligned: {'HumanEval': 0.1538}\nexp_001_eval_3B_d000_s42_para_aligned: {'humaneval': {'pass@1': 0.1154, 'correct': 3, 'total': 26}}\nexp_001_eval_3B_d100_s42_para_aligned: {'humaneval': {'pass@1': 0.1154, 'correct': 3, 'total': 26}}\nexp_001_eval_3B_d025_v2_para_aligned: {'humaneval_para_pass@1': 0.1154}\nexp_001_eval_3B_d000_v2_s123_para_aligned: {'humaneval_para_pass@1': 0.0385}\nexp_001_eval_05B_d005_s123_para_aligned: {'humaneval_para_pass@1': 0}\nexp_001_eval_3B_d000_v2_para_aligned_v2: {'humaneval_para_pass@1': 0.0385}\nexp_001_eval_3B_d100_v2_para_aligned: {'humaneval_para_pass1': 0.1154}\nexp_001_eval_05B_d005_para_aligned: {'humaneval': 0, 'humaneval_correct': 0, 'humaneval_total': 26}\nexp_001_eval_15B_d025_para_aligned: {'humaneval': 0.154}",
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

_source line 107_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have a wealth of data. Let me now compile the complete summary. Let me create a comprehensive Python script locally that:

1. Maps all the disk data (mmlu, gsm8k, arc_challenge) 
2. Maps HumanEval from registry
3. Selects canonical entries for each (scale, dose, seed, eval_type) combination
4. Generates the summary JSON and markdown

Let me organize the data first:

**Key data sources:**

1. **1.5B batch experiment** (`exp_001_eval_15B_aligned_batch`) gives us the canonical values for 1.5B s42:
   - d000 orig: mmlu=0.5853, gsm8k=0.6543, arc=0.7722, humaneval=0.128
   - d005 orig: mmlu=0.5852, gsm8k=0.6482, arc=0.7688, humaneval=0.25
   - d100 orig: mmlu=0.5933, gsm8k=0.6497, arc=0.7688, humaneval=0.3049
   - d000 para: mmlu=0.6096, gsm8k=0.557, arc=0.7547, humaneval=0.0385
   - d005 para: mmlu=0.6164, gsm8k=0.5439, arc=0.7532, humaneval=0.1923
   - d100 para: mmlu=0.6252, gsm8k=0.5526, arc=0.7661, humaneval=0.2692

I've got partial results from the 0.5B batch experiment with seed 42, and now I need to consolidate everything into a unified mapping. For each combination of scale, dose, seed, and evaluation type, I'll identify the canonical entry and build out the complete results table.

Generating markdown table... Now I'm looking at the performance metrics for the para-aligned models, checking the HumanEval scores against what's in the registry and noting some discrepancies that need verification. Now I'm looking at the 1.5B aligned results from disk, checking the performance metrics across different dose and seed combinations—most entries have complete scores, though there's a data inconsistency where one registry entry shows null for the HumanEval benchmark. Now I'm looking at the performance metrics for the 1.5B para-aligned models across different doses, where only seed 42 is available, and the scores show some variation in MMLU and HumanEval performance depending on the dose level.

For the 3B aligned models with alpha=32, I need to pick between the v2 and v3 checkpoint versions for d000 since there's no contamination difference to consider there. The v2 variant shows significantly better GSM8K performance (0.3525 vs 0.1198), which suggests it was trained differently, possibly with a different dataset or approach.

Looking at the pattern, it seems the task expects me to use v2 entries consistently across d025 and d100, so I should apply the same logic to d000 and grab the v2 version when available. For d005 though, there don't appear to be v2 variants at all—just the standard aligned checkpoints—so those might already be the right choice. I need to figure out which version to use for d000_s42 — v2 seems more consistent with the rest of the pipeline since v1 is deprecated. But I'm also noticing that `d000_s123_aligned` (without a version label) has different values than `d000_v2_s123_aligned`, so I need to clarify which one is actually the current version before deciding on a consistent approach. Generating the results table...

I notice the d005_s123_aligned variant is missing from the disk—there's only a d005_s123_para_aligned version available, so I'll need to skip that row in the comparison. Generating the results table... I'm noticing a discrepancy in the data I'm looking at—the grep output shows a gsm8k value of 0.1491 for the 3B model, but I need to verify this against the full JSON to make sure I'm reading the right entry, since the truncation is making it hard to cross-reference accurately. I'm checking the HumanEval scores across the different model configurations to fill in the gaps. Most entries are either null or missing entirely from the registry, particularly for the 1.5B and 3B models with para_aligned variants. I have enough data now to move forward with my analysis. I'm noticing that the HumanEval score for the 0.5B aligned v2 entry might have been evaluated on paraphrased questions despite the disk data showing aligned metrics, so I'll flag that discrepancy in the output. I also see that several para_aligned entries for s123 across different scales don't have corresponding disk files, which I'll need to account for when compiling the data. Now I'm writing a Python script to generate both JSON and markdown summaries from the registry and disk data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "ea5ee0ef-9c37-406c-8421-c221fd9954a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2LaMM6nCp2ryxT2AZDQfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1785,
      "cache_read_input_tokens": 71110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1785
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 108_

Now I have all the data from disk (mmlu/gsm8k/arc) and registry (HumanEval). Let me compile the complete summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "add98ae4-8514-4269-ab6d-cdd1eec06235",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2LaMM6nCp2ryxT2AZDQfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1785,
      "cache_read_input_tokens": 71110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1785
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 109_

<details open><summary>🔧 Tool call — Bash · `toolu_0145xVsqx8oL4oLGyxHGpZ3v`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "4083f6c4-58ce-4b5b-8f7b-ca0dff15e7c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2LaMM6nCp2ryxT2AZDQfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1785,
      "cache_read_input_tokens": 71110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1785
      },
      "output_tokens": 32,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-15T18:33:34.670Z_

<details><summary>↩ Tool result · `toolu_0145xVsqx8oL4oLGyxHGpZ3v`</summary>

```text
2pl_vs_4pl_ablation.md
_project
analysis_3B_d000_gsm8k_seed_variance.md
coverage_report_20260515.md
d000_alignment_tax_analysis.md
diag_exp_001_sft_15B_d005_s123.md
diag_exp_001_sft_d100_3B.md
dose_response_analysis.md
dream_reports
eval_summary_matrix.csv
exp-004
exp-006
exp-008
exp001
exp001_sft_injection
exp002_signal_pipeline
exp003_rrf_ablation
exp004_incremental_analysis.md
exp005_noise_propagation
exp006
exp006-oracle-gsm8k-extended-v2
exp006-s1only-gsm8k-2pl
exp006_baselines
exp006_irt_calibration
exp008
exp008_3regime_analysis.json
exp008_auc_heatmap.json
exp008_v2
exp_001_sft_injection
exp_002_signals_05B
exp_005_noise_prop_v4
exp_008_base_pretrained_15B_eval
exp_008_instruct_rl_proxy
exp_008_signal_survival
fisher_info_derivation
gpu_audit_20260515T1330.md
gpu_health_20260515T1654.md
gpu_health_check_loop10.md
gpu_status_check.md
literature_survey_negative_gamma.md
manifest.yaml
mvp_simulation
paper_draft
phase3_progress.md
report_eval_compilation.md
run_pooled_4bench_irt.py
run_pooled_irt_n16.sh
run_stratified_irt.py
simulation_sweep
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "74ca1219-6f24-49b6-9897-784ab8c133c8",
  "tool_use_result": {
    "stdout": "2pl_vs_4pl_ablation.md\n_project\nanalysis_3B_d000_gsm8k_seed_variance.md\ncoverage_report_20260515.md\nd000_alignment_tax_analysis.md\ndiag_exp_001_sft_15B_d005_s123.md\ndiag_exp_001_sft_d100_3B.md\ndose_response_analysis.md\ndream_reports\neval_summary_matrix.csv\nexp-004\nexp-006\nexp-008\nexp001\nexp001_sft_injection\nexp002_signal_pipeline\nexp003_rrf_ablation\nexp004_incremental_analysis.md\nexp005_noise_propagation\nexp006\nexp006-oracle-gsm8k-extended-v2\nexp006-s1only-gsm8k-2pl\nexp006_baselines\nexp006_irt_calibration\nexp008\nexp008_3regime_analysis.json\nexp008_auc_heatmap.json\nexp008_v2\nexp_001_sft_injection\nexp_002_signals_05B\nexp_005_noise_prop_v4\nexp_008_base_pretrained_15B_eval\nexp_008_instruct_rl_proxy\nexp_008_signal_survival\nfisher_info_derivation\ngpu_audit_20260515T1330.md\ngpu_health_20260515T1654.md\ngpu_health_check_loop10.md\ngpu_status_check.md\nliterature_survey_negative_gamma.md\nmanifest.yaml\nmvp_simulation\npaper_draft\nphase3_progress.md\nreport_eval_compilation.md\nrun_pooled_4bench_irt.py\nrun_pooled_irt_n16.sh\nrun_stratified_irt.py\nsimulation_sweep",
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

_source line 111_

<details open><summary>🔧 Tool call — Write · `toolu_01NpTRG45BX49Mxi6e4msxGU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/compile_eval_summary.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Compile all eval metrics into summary JSON and markdown table.\"\"\"\n\nimport json\nimport statistics\nfrom collections import defaultdict\n\n# ============================================================\n# Disk data: mmlu, gsm8k, arc_challenge (humaneval always null on disk)\n# Source: /root/autodl-tmp/exp001/eval_results/*/eval_results.json\n# ============================================================\n\ndisk_data = {\n    # ---- 0.5B ----\n    \"Qwen2.5-0.5B_d000_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3979, \"gsm8k\": 0.3692, \"arc\": 0.4693},\n    \"Qwen2.5-0.5B_d000_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.4216, \"gsm8k\": 0.3412, \"arc\": 0.4974},\n    \"Qwen2.5-0.5B_d000_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.4428, \"gsm8k\": 0.2807, \"arc\": 0.4792},\n    \"Qwen2.5-0.5B_d005_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3255, \"gsm8k\": 0.3624, \"arc\": 0.3285},\n    \"Qwen2.5-0.5B_d005_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3002, \"gsm8k\": 0.3677, \"arc\": 0.2978},\n    \"Qwen2.5-0.5B_d005_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.3548, \"gsm8k\": 0.2588, \"arc\": 0.3300},\n    \"Qwen2.5-0.5B_d005_s123_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.3166, \"gsm8k\": 0.2939, \"arc\": 0.2912},\n    \"Qwen2.5-0.5B_d025_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.2803, \"gsm8k\": 0.3662, \"arc\": 0.3251},\n    \"Qwen2.5-0.5B_d025_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3473, \"gsm8k\": 0.3533, \"arc\": 0.4061},\n    \"Qwen2.5-0.5B_d025_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.2835, \"gsm8k\": 0.3114, \"arc\": 0.3199},\n    \"Qwen2.5-0.5B_d100_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.2334, \"gsm8k\": 0.3654, \"arc\": 0.2944},\n    \"Qwen2.5-0.5B_d100_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3058, \"gsm8k\": 0.3798, \"arc\": 0.3669},\n\n    # ---- 1.5B ----\n    \"Qwen2.5-1.5B_d000_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5853, \"gsm8k\": 0.6543, \"arc\": 0.7722},\n    \"Qwen2.5-1.5B_d000_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5855, \"gsm8k\": 0.6535, \"arc\": 0.7577},\n    \"Qwen2.5-1.5B_d000_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6096, \"gsm8k\": 0.5570, \"arc\": 0.7547},\n    \"Qwen2.5-1.5B_d005_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5852, \"gsm8k\": 0.6482, \"arc\": 0.7688},\n    \"Qwen2.5-1.5B_d005_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5869, \"gsm8k\": 0.6482, \"arc\": 0.7568},\n    \"Qwen2.5-1.5B_d005_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6164, \"gsm8k\": 0.5439, \"arc\": 0.7532},\n    \"Qwen2.5-1.5B_d025_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5902, \"gsm8k\": 0.6535, \"arc\": 0.7688},\n    \"Qwen2.5-1.5B_d025_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5881, \"gsm8k\": 0.6550, \"arc\": 0.7577},\n    \"Qwen2.5-1.5B_d025_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6176, \"gsm8k\": 0.5395, \"arc\": 0.7661},\n    \"Qwen2.5-1.5B_d100_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5933, \"gsm8k\": 0.6497, \"arc\": 0.7688},\n    \"Qwen2.5-1.5B_d100_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5956, \"gsm8k\": 0.6444, \"arc\": 0.7816},\n    \"Qwen2.5-1.5B_d100_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6252, \"gsm8k\": 0.5526, \"arc\": 0.7661},\n\n    # ---- 3B (v2/alpha=32 preferred) ----\n    \"Qwen2.5-3B_d000_v2_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6295, \"gsm8k\": 0.3525, \"arc\": 0.8183},\n    \"Qwen2.5-3B_d000_v2_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6314, \"gsm8k\": 0.2676, \"arc\": 0.8259},\n    \"Qwen2.5-3B_d000_v2_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6468, \"gsm8k\": 0.2895, \"arc\": 0.8121},\n    \"Qwen2.5-3B_d000_v2_s123_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6512, \"gsm8k\": 0.1491, \"arc\": 0.8121},\n    \"Qwen2.5-3B_d005_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6345, \"gsm8k\": 0.2077, \"arc\": 0.8294},\n    \"Qwen2.5-3B_d005_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6542, \"gsm8k\": 0.1491, \"arc\": 0.8221},\n    \"Qwen2.5-3B_d005_s123_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6461, \"gsm8k\": 0.5000, \"arc\": 0.8192},\n    \"Qwen2.5-3B_d025_v2_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5998, \"gsm8k\": 0.6793, \"arc\": 0.8276},  # s42\n    \"Qwen2.5-3B_d025_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6367, \"gsm8k\": 0.5254, \"arc\": 0.8336},\n    \"Qwen2.5-3B_d025_v2_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6210, \"gsm8k\": 0.5482, \"arc\": 0.8106},\n    \"Qwen2.5-3B_d025_s123_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6615, \"gsm8k\": 0.4254, \"arc\": 0.8121},\n    \"Qwen2.5-3B_d100_v2_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6320, \"gsm8k\": 0.7415, \"arc\": 0.8242},\n    \"Qwen2.5-3B_d100_v2_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6319, \"gsm8k\": 0.7324, \"arc\": 0.8311},\n    \"Qwen2.5-3B_d100_v2_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6590, \"gsm8k\": 0.5833, \"arc\": 0.8092},\n}\n\n# ============================================================\n# HumanEval data from registry (not on disk)\n# ============================================================\n\nhumaneval_registry = {\n    # 0.5B\n    \"Qwen2.5-0.5B_d000_s42_aligned\": 0.1098,   # from batch\n    \"Qwen2.5-0.5B_d000_s123_aligned\": 0.1037,\n    \"Qwen2.5-0.5B_d000_s42_para_aligned\": 0.1154,  # from batch\n    \"Qwen2.5-0.5B_d005_s42_aligned\": 0.0793,    # from batch\n    \"Qwen2.5-0.5B_d005_s123_aligned\": 0.0976,\n    \"Qwen2.5-0.5B_d005_s42_para_aligned\": 0.0,\n    \"Qwen2.5-0.5B_d005_s123_para_aligned\": 0.0,\n    \"Qwen2.5-0.5B_d025_s42_aligned\": 0.1923,    # from d025_aligned_v2; note: possibly mislabeled\n    \"Qwen2.5-0.5B_d025_s123_aligned\": None,      # missing\n    \"Qwen2.5-0.5B_d025_s42_para_aligned\": None,  # missing\n    \"Qwen2.5-0.5B_d100_s42_aligned\": 0.0,        # from d100_aligned_v4\n    \"Qwen2.5-0.5B_d100_s123_aligned\": 0.1037,\n\n    # 1.5B\n    \"Qwen2.5-1.5B_d000_s42_aligned\": 0.128,      # from batch\n    \"Qwen2.5-1.5B_d000_s123_aligned\": 0.1707,\n    \"Qwen2.5-1.5B_d000_s42_para_aligned\": 0.0385, # from batch\n    \"Qwen2.5-1.5B_d005_s42_aligned\": 0.25,        # from batch/registry\n    \"Qwen2.5-1.5B_d005_s123_aligned\": None,       # missing\n    \"Qwen2.5-1.5B_d005_s42_para_aligned\": 0.1923, # from batch\n    \"Qwen2.5-1.5B_d025_s42_aligned\": 0.2256,\n    \"Qwen2.5-1.5B_d025_s123_aligned\": None,       # missing\n    \"Qwen2.5-1.5B_d025_s42_para_aligned\": 0.154,\n    \"Qwen2.5-1.5B_d100_s42_aligned\": 0.3049,      # from batch\n    \"Qwen2.5-1.5B_d100_s123_aligned\": 0.2805,\n    \"Qwen2.5-1.5B_d100_s42_para_aligned\": 0.2692, # from batch\n\n    # 3B (v2/alpha=32)\n    \"Qwen2.5-3B_d000_v2_s42_aligned\": 0.0976,\n    \"Qwen2.5-3B_d000_v2_s123_aligned\": 0.061,\n    \"Qwen2.5-3B_d000_v2_s42_para_aligned\": 0.0385,\n    \"Qwen2.5-3B_d000_v2_s123_para_aligned\": 0.0385,\n    \"Qwen2.5-3B_d005_s42_aligned\": 0.1463,\n    \"Qwen2.5-3B_d005_s42_para_aligned\": None,     # missing\n    \"Qwen2.5-3B_d005_s123_para_aligned\": 0.0769,\n    \"Qwen2.5-3B_d025_v2_aligned\": 0.0976,         # s42\n    \"Qwen2.5-3B_d025_s123_aligned\": 0.1585,\n    \"Qwen2.5-3B_d025_v2_s42_para_aligned\": 0.1154,\n    \"Qwen2.5-3B_d025_s123_para_aligned\": 0.1538,\n    \"Qwen2.5-3B_d100_v2_s42_aligned\": 0.1707,\n    \"Qwen2.5-3B_d100_v2_s123_aligned\": 0.1829,\n    \"Qwen2.5-3B_d100_v2_s42_para_aligned\": 0.1154,\n}\n\n# ============================================================\n# Build structured records\n# ============================================================\n\ndef parse_entry(dir_name, disk, he):\n    \"\"\"Parse directory name into structured record.\"\"\"\n    # Determine scale\n    if \"0.5B\" in dir_name:\n        scale = \"0.5B\"\n    elif \"1.5B\" in dir_name:\n        scale = \"1.5B\"\n    elif \"3B\" in dir_name:\n        scale = \"3B\"\n    else:\n        return None\n\n    # Determine eval type\n    if \"para_aligned\" in dir_name:\n        eval_type = \"para_aligned\"\n    elif \"aligned\" in dir_name:\n        eval_type = \"aligned\"\n    else:\n        return None\n\n    # Determine dose\n    for d in [\"d000\", \"d005\", \"d025\", \"d100\"]:\n        if d in dir_name:\n            dose_pct = {\"d000\": 0, \"d005\": 5, \"d025\": 25, \"d100\": 100}[d]\n            break\n    else:\n        return None\n\n    # Determine seed\n    if \"s123\" in dir_name:\n        seed = 123\n    elif \"s42\" in dir_name:\n        seed = 42\n    else:\n        # Some entries don't have explicit seed — check notes\n        # d025_v2_aligned is s42 per registry\n        seed = 42  # default assumption for entries without seed marker\n\n    # Notes for version tracking\n    notes = []\n    if \"_v2\" in dir_name or \"_v3\" in dir_name:\n        notes.append(\"alpha=32\")\n    if scale == \"3B\" and \"_v2\" not in dir_name and \"_v3\" not in dir_name:\n        if dose_pct in [25, 100]:\n            notes.append(\"WARNING: may be alpha=16\")\n        elif dose_pct == 0 and \"d000_v2\" not in dir_name:\n            notes.append(\"pre-v2 SFT\")\n\n    return {\n        \"scale\": scale,\n        \"dose_pct\": dose_pct,\n        \"seed\": seed,\n        \"eval_type\": eval_type,\n        \"mmlu\": round(disk[\"mmlu\"], 4),\n        \"gsm8k\": round(disk[\"gsm8k\"], 4),\n        \"arc\": round(disk[\"arc\"], 4),\n        \"humaneval\": round(he, 4) if he is not None else None,\n        \"source_dir\": dir_name,\n        \"notes\": \"; \".join(notes) if notes else \"\",\n    }\n\n\nrecords = []\nfor dir_name, disk in disk_data.items():\n    he = humaneval_registry.get(dir_name)\n    rec = parse_entry(dir_name, disk, he)\n    if rec:\n        records.append(rec)\n\n# Sort records\nrecords.sort(key=lambda r: (\n    {\"0.5B\": 0, \"1.5B\": 1, \"3B\": 2}[r[\"scale\"]],\n    r[\"dose_pct\"],\n    r[\"seed\"],\n    0 if r[\"eval_type\"] == \"aligned\" else 1,\n))\n\n# ============================================================\n# Compute cross-seed means and std\n# ============================================================\n\nagg_key = lambda r: (r[\"scale\"], r[\"dose_pct\"], r[\"eval_type\"])\ngroups = defaultdict(list)\nfor r in records:\n    groups[agg_key(r)].append(r)\n\naggregated = []\nfor key, recs in sorted(groups.items()):\n    scale, dose, etype = key\n    agg = {\"scale\": scale, \"dose_pct\": dose, \"eval_type\": etype, \"n_seeds\": len(recs)}\n    for bm in [\"mmlu\", \"gsm8k\", \"arc\", \"humaneval\"]:\n        vals = [r[bm] for r in recs if r[bm] is not None]\n        if vals:\n            agg[f\"{bm}_mean\"] = round(statistics.mean(vals), 4)\n            agg[f\"{bm}_std\"] = round(statistics.stdev(vals), 4) if len(vals) > 1 else None\n        else:\n            agg[f\"{bm}_mean\"] = None\n            agg[f\"{bm}_std\"] = None\n    aggregated.append(agg)\n\n# ============================================================\n# Dose-response curves\n# ============================================================\n\ndose_response = {}\nfor bm in [\"mmlu\", \"gsm8k\", \"arc\", \"humaneval\"]:\n    dose_response[bm] = {}\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        for etype in [\"aligned\", \"para_aligned\"]:\n            curve = []\n            for agg in aggregated:\n                if agg[\"scale\"] == scale and agg[\"eval_type\"] == etype:\n                    curve.append({\n                        \"dose_pct\": agg[\"dose_pct\"],\n                        \"mean\": agg[f\"{bm}_mean\"],\n                        \"std\": agg[f\"{bm}_std\"],\n                        \"n\": agg[\"n_seeds\"],\n                    })\n            if curve:\n                dose_response[bm][f\"{scale}_{etype}\"] = curve\n\n# ============================================================\n# Baselines\n# ============================================================\n\nbaselines = {\n    \"Qwen2.5-0.5B_base_pretrained\": {\n        \"mmlu\": 0.2294, \"gsm8k\": 0.1630, \"arc\": 0.2278, \"humaneval\": 0.0,\n        \"source\": \"exp_008_base_pretrained_eval_v2\"\n    },\n    \"Qwen2.5-0.5B-Instruct\": {\n        \"mmlu\": 0.2462, \"gsm8k\": 0.3882, \"arc\": 0.2816, \"humaneval\": 0.0,\n        \"source\": \"exp_008_instruct_05B_eval\"\n    },\n    \"Qwen2.5-1.5B_base_pretrained\": {\n        \"mmlu\": 0.2303, \"gsm8k\": 0.0053, \"arc\": 0.2304, \"humaneval\": 0.2317,\n        \"source\": \"exp_008_base_pretrained_15B_eval_v2\"\n    },\n}\n\n# ============================================================\n# Output JSON\n# ============================================================\n\noutput = {\n    \"metadata\": {\n        \"project\": \"contamcal-irt-calibration\",\n        \"description\": \"Eval metrics summary across all scales, doses, seeds, and eval types\",\n        \"scales\": [\"0.5B\", \"1.5B\", \"3B\"],\n        \"doses_pct\": [0, 5, 25, 100],\n        \"seeds\": [42, 123],\n        \"eval_types\": [\"aligned\", \"para_aligned\"],\n        \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc\", \"humaneval\"],\n        \"model_family\": \"Qwen2.5\",\n        \"lora_alpha\": 32,\n        \"notes\": [\n            \"HumanEval metrics from registry (not stored on disk)\",\n            \"3B uses v2 checkpoints (alpha=32); v1/DEPRECATED excluded\",\n            \"3B d005_s123_aligned eval is missing (never run)\",\n            \"3B d100_s123_para_aligned eval is missing\",\n            \"Some 0.5B/1.5B para_aligned s123 entries are missing\",\n            \"0.5B d025_s42 HumanEval=0.1923 may be from mislabeled para_aligned run\",\n        ],\n    },\n    \"individual_results\": records,\n    \"aggregated_by_dose\": aggregated,\n    \"dose_response_curves\": dose_response,\n    \"baselines\": baselines,\n}\n\njson_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json\"\nwith open(json_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"JSON saved to {json_path}\")\n\n# ============================================================\n# Output Markdown\n# ============================================================\n\nmd_lines = []\nmd_lines.append(\"# Eval Metrics Summary: contamcal-irt-calibration\")\nmd_lines.append(\"\")\nmd_lines.append(\"Model: Qwen2.5 (0.5B / 1.5B / 3B), LoRA alpha=32\")\nmd_lines.append(\"\")\nmd_lines.append(\"Doses: 0% (clean), 5%, 25%, 100% benchmark contamination in SFT data\")\nmd_lines.append(\"\")\nmd_lines.append(\"Eval types: **aligned** (original benchmark format), **para_aligned** (paraphrased questions)\")\nmd_lines.append(\"\")\n\n# Individual results table\nmd_lines.append(\"## Individual Results\")\nmd_lines.append(\"\")\nmd_lines.append(\"| Scale | Dose% | Seed | Eval Type | MMLU | GSM8K | ARC | HumanEval | Notes |\")\nmd_lines.append(\"|-------|-------|------|-----------|------|-------|-----|-----------|-------|\")\n\nfor r in records:\n    he_str = f\"{r['humaneval']:.4f}\" if r['humaneval'] is not None else \"—\"\n    md_lines.append(\n        f\"| {r['scale']} | {r['dose_pct']} | {r['seed']} | {r['eval_type']} \"\n        f\"| {r['mmlu']:.4f} | {r['gsm8k']:.4f} | {r['arc']:.4f} | {he_str} | {r['notes']} |\"\n    )\n\nmd_lines.append(\"\")\n\n# Aggregated table\nmd_lines.append(\"## Aggregated (Mean ± Std across seeds)\")\nmd_lines.append(\"\")\nmd_lines.append(\"| Scale | Dose% | Eval Type | N | MMLU | GSM8K | ARC | HumanEval |\")\nmd_lines.append(\"|-------|-------|-----------|---|------|-------|-----|-----------|\")\n\nfor a in aggregated:\n    cols = []\n    for bm in [\"mmlu\", \"gsm8k\", \"arc\", \"humaneval\"]:\n        m = a[f\"{bm}_mean\"]\n        s = a[f\"{bm}_std\"]\n        if m is None:\n            cols.append(\"—\")\n        elif s is not None:\n            cols.append(f\"{m:.4f}±{s:.4f}\")\n        else:\n            cols.append(f\"{m:.4f}\")\n    md_lines.append(\n        f\"| {a['scale']} | {a['dose_pct']} | {a['eval_type']} | {a['n_seeds']} \"\n        f\"| {cols[0]} | {cols[1]} | {cols[2]} | {cols[3]} |\"\n    )\n\nmd_lines.append(\"\")\n\n# Dose-response summary\nmd_lines.append(\"## Dose-Response Summary (aligned eval, mean across seeds)\")\nmd_lines.append(\"\")\nmd_lines.append(\"### MMLU\")\nmd_lines.append(\"| Dose% | 0.5B | 1.5B | 3B |\")\nmd_lines.append(\"|-------|------|------|-----|\")\n\nfor dose in [0, 5, 25, 100]:\n    vals = []\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        match = [a for a in aggregated if a[\"scale\"] == scale and a[\"dose_pct\"] == dose and a[\"eval_type\"] == \"aligned\"]\n        if match:\n            v = match[0][\"mmlu_mean\"]\n            vals.append(f\"{v:.4f}\" if v else \"—\")\n        else:\n            vals.append(\"—\")\n    md_lines.append(f\"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |\")\n\nmd_lines.append(\"\")\nmd_lines.append(\"### GSM8K\")\nmd_lines.append(\"| Dose% | 0.5B | 1.5B | 3B |\")\nmd_lines.append(\"|-------|------|------|-----|\")\n\nfor dose in [0, 5, 25, 100]:\n    vals = []\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        match = [a for a in aggregated if a[\"scale\"] == scale and a[\"dose_pct\"] == dose and a[\"eval_type\"] == \"aligned\"]\n        if match:\n            v = match[0][\"gsm8k_mean\"]\n            vals.append(f\"{v:.4f}\" if v else \"—\")\n        else:\n            vals.append(\"—\")\n    md_lines.append(f\"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |\")\n\nmd_lines.append(\"\")\nmd_lines.append(\"### ARC-Challenge\")\nmd_lines.append(\"| Dose% | 0.5B | 1.5B | 3B |\")\nmd_lines.append(\"|-------|------|------|-----|\")\n\nfor dose in [0, 5, 25, 100]:\n    vals = []\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        match = [a for a in aggregated if a[\"scale\"] == scale and a[\"dose_pct\"] == dose and a[\"eval_type\"] == \"aligned\"]\n        if match:\n            v = match[0][\"arc_mean\"]\n            vals.append(f\"{v:.4f}\" if v else \"—\")\n        else:\n            vals.append(\"—\")\n    md_lines.append(f\"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |\")\n\nmd_lines.append(\"\")\nmd_lines.append(\"### HumanEval\")\nmd_lines.append(\"| Dose% | 0.5B | 1.5B | 3B |\")\nmd_lines.append(\"|-------|------|------|-----|\")\n\nfor dose in [0, 5, 25, 100]:\n    vals = []\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        match = [a for a in aggregated if a[\"scale\"] == scale and a[\"dose_pct\"] == dose and a[\"eval_type\"] == \"aligned\"]\n        if match:\n            v = match[0][\"humaneval_mean\"]\n            vals.append(f\"{v:.4f}\" if v else \"—\")\n        else:\n            vals.append(\"—\")\n    md_lines.append(f\"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |\")\n\nmd_lines.append(\"\")\n\n# Baselines\nmd_lines.append(\"## Baselines (no SFT)\")\nmd_lines.append(\"\")\nmd_lines.append(\"| Model | MMLU | GSM8K | ARC | HumanEval |\")\nmd_lines.append(\"|-------|------|-------|-----|-----------|\")\nfor name, b in baselines.items():\n    he_str = f\"{b['humaneval']:.4f}\" if b['humaneval'] is not None else \"—\"\n    md_lines.append(f\"| {name} | {b['mmlu']:.4f} | {b['gsm8k']:.4f} | {b['arc']:.4f} | {he_str} |\")\n\nmd_lines.append(\"\")\n\n# Coverage matrix\nmd_lines.append(\"## Coverage Matrix\")\nmd_lines.append(\"\")\nmd_lines.append(\"✓ = both seeds, △ = seed 42 only, ✗ = missing\")\nmd_lines.append(\"\")\nmd_lines.append(\"| Scale | Dose% | Aligned | Para-aligned |\")\nmd_lines.append(\"|-------|-------|---------|--------------|\")\n\nfor scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n    for dose in [0, 5, 25, 100]:\n        statuses = []\n        for etype in [\"aligned\", \"para_aligned\"]:\n            matching = [r for r in records if r[\"scale\"] == scale and r[\"dose_pct\"] == dose and r[\"eval_type\"] == etype]\n            seeds = set(r[\"seed\"] for r in matching)\n            if seeds == {42, 123}:\n                statuses.append(\"✓\")\n            elif seeds == {42}:\n                statuses.append(\"△\")\n            elif seeds:\n                statuses.append(f\"seed={list(seeds)}\")\n            else:\n                statuses.append(\"✗\")\n        md_lines.append(f\"| {scale} | {dose} | {statuses[0]} | {statuses[1]} |\")\n\nmd_lines.append(\"\")\nmd_lines.append(\"## Notes\")\nmd_lines.append(\"\")\nmd_lines.append(\"- HumanEval metrics sourced from experiment registry (not stored in eval_results.json on disk)\")\nmd_lines.append(\"- 3B results use v2 checkpoints (LoRA alpha=32); v1/DEPRECATED (alpha=16) excluded\")\nmd_lines.append(\"- 3B d005_s123 aligned eval was never run\")\nmd_lines.append(\"- 3B d100_s123 para_aligned eval was never run\")\nmd_lines.append(\"- Several 0.5B and 1.5B para_aligned seed=123 entries are missing\")\nmd_lines.append(\"- 0.5B d025_s42 aligned HumanEval (0.1923) may originate from a mislabeled para_aligned run\")\nmd_lines.append(\"\")\n\nmd_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md\"\nwith open(md_path, \"w\") as f:\n    f.write(\"\\n\".join(md_lines))\nprint(f\"Markdown saved to {md_path}\")\n\n# Quick stats\nprint(f\"\\nTotal individual records: {len(records)}\")\nprint(f\"Aggregated groups: {len(aggregated)}\")\nfor scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n    n = sum(1 for r in records if r[\"scale\"] == scale)\n    print(f\"  {scale}: {n} entries\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "5c92b99d-7b77-42ed-bc15-75dd4402636d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LaKGQcKgMYJ3CTyCPv3tjR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5825,
      "cache_read_input_tokens": 72895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5825
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

_source line 112 · 2026-05-15T18:35:10.315Z_

<details><summary>↩ Tool result · `toolu_01NpTRG45BX49Mxi6e4msxGU`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/compile_eval_summary.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "603a6581-9a49-4649-beb4-b7cb9fd54e69",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/compile_eval_summary.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Compile all eval metrics into summary JSON and markdown table.\"\"\"\n\nimport json\nimport statistics\nfrom collections import defaultdict\n\n# ============================================================\n# Disk data: mmlu, gsm8k, arc_challenge (humaneval always null on disk)\n# Source: /root/autodl-tmp/exp001/eval_results/*/eval_results.json\n# ============================================================\n\ndisk_data = {\n    # ---- 0.5B ----\n    \"Qwen2.5-0.5B_d000_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3979, \"gsm8k\": 0.3692, \"arc\": 0.4693},\n    \"Qwen2.5-0.5B_d000_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.4216, \"gsm8k\": 0.3412, \"arc\": 0.4974},\n    \"Qwen2.5-0.5B_d000_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.4428, \"gsm8k\": 0.2807, \"arc\": 0.4792},\n    \"Qwen2.5-0.5B_d005_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3255, \"gsm8k\": 0.3624, \"arc\": 0.3285},\n    \"Qwen2.5-0.5B_d005_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3002, \"gsm8k\": 0.3677, \"arc\": 0.2978},\n    \"Qwen2.5-0.5B_d005_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.3548, \"gsm8k\": 0.2588, \"arc\": 0.3300},\n    \"Qwen2.5-0.5B_d005_s123_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.3166, \"gsm8k\": 0.2939, \"arc\": 0.2912},\n    \"Qwen2.5-0.5B_d025_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.2803, \"gsm8k\": 0.3662, \"arc\": 0.3251},\n    \"Qwen2.5-0.5B_d025_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3473, \"gsm8k\": 0.3533, \"arc\": 0.4061},\n    \"Qwen2.5-0.5B_d025_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.2835, \"gsm8k\": 0.3114, \"arc\": 0.3199},\n    \"Qwen2.5-0.5B_d100_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.2334, \"gsm8k\": 0.3654, \"arc\": 0.2944},\n    \"Qwen2.5-0.5B_d100_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3058, \"gsm8k\": 0.3798, \"arc\": 0.3669},\n\n    # ---- 1.5B ----\n    \"Qwen2.5-1.5B_d000_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5853, \"gsm8k\": 0.6543, \"arc\": 0.7722},\n    \"Qwen2.5-1.5B_d000_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5855, \"gsm8k\": 0.6535, \"arc\": 0.7577},\n    \"Qwen2.5-1.5B_d000_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6096, \"gsm8k\": 0.5570, \"arc\": 0.7547},\n    \"Qwen2.5-1.5B_d005_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5852, \"gsm8k\": 0.6482, \"arc\": 0.7688},\n    \"Qwen2.5-1.5B_d005_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5869, \"gsm8k\": 0.6482, \"arc\": 0.7568},\n    \"Qwen2.5-1.5B_d005_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6164, \"gsm8k\": 0.5439, \"arc\": 0.7532},\n    \"Qwen2.5-1.5B_d025_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5902, \"gsm8k\": 0.6535, \"arc\": 0.7688},\n    \"Qwen2.5-1.5B_d025_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5881, \"gsm8k\": 0.6550, \"arc\": 0.7577},\n    \"Qwen2.5-1.5B_d025_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6176, \"gsm8k\": 0.5395, \"arc\": 0.7661},\n    \"Qwen2.5-1.5B_d100_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5933, \"gsm8k\": 0.6497, \"arc\": 0.7688},\n    \"Qwen2.5-1.5B_d100_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5956, \"gsm8k\": 0.6444, \"arc\": 0.7816},\n    \"Qwen2.5-1.5B_d100_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6252, \"gsm8k\": 0.5526, \"arc\": 0.7661},\n\n    # ---- 3B (v2/alpha=32 preferred) ----\n    \"Qwen2.5-3B_d000_v2_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6295, \"gsm8k\": 0.3525, \"arc\": 0.8183},\n    \"Qwen2.5-3B_d000_v2_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6314, \"gsm8k\": 0.2676, \"arc\": 0.8259},\n    \"Qwen2.5-3B_d000_v2_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6468, \"gsm8k\": 0.2895, \"arc\": 0.8121},\n    \"Qwen2.5-3B_d000_v2_s123_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6512, \"gsm8k\": 0.1491, \"arc\": 0.8121},\n    \"Qwen2.5-3B_d005_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6345, \"gsm8k\": 0.2077, \"arc\": 0.8294},\n    \"Qwen2.5-3B_d005_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6542, \"gsm8k\": 0.1491, \"arc\": 0.8221},\n    \"Qwen2.5-3B_d005_s123_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6461, \"gsm8k\": 0.5000, \"arc\": 0.8192},\n    \"Qwen2.5-3B_d025_v2_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5998, \"gsm8k\": 0.6793, \"arc\": 0.8276},  # s42\n    \"Qwen2.5-3B_d025_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6367, \"gsm8k\": 0.5254, \"arc\": 0.8336},\n    \"Qwen2.5-3B_d025_v2_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6210, \"gsm8k\": 0.5482, \"arc\": 0.8106},\n    \"Qwen2.5-3B_d025_s123_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6615, \"gsm8k\": 0.4254, \"arc\": 0.8121},\n    \"Qwen2.5-3B_d100_v2_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6320, \"gsm8k\": 0.7415, \"arc\": 0.8242},\n    \"Qwen2.5-3B_d100_v2_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6319, \"gsm8k\": 0.7324, \"arc\": 0.8311},\n    \"Qwen2.5-3B_d100_v2_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6590, \"gsm8k\": 0.5833, \"arc\": 0.8092},\n}\n\n# ============================================================\n# HumanEval data from registry (not on disk)\n# ============================================================\n\nhumaneval_registry = {\n    # 0.5B\n    \"Qwen2.5-0.5B_d000_s42_aligned\": 0.1098,   # from batch\n    \"Qwen2.5-0.5B_d000_s123_aligned\": 0.1037,\n    \"Qwen2.5-0.5B_d000_s42_para_aligned\": 0.1154,  # from batch\n    \"Qwen2.5-0.5B_d005_s42_aligned\": 0.0793,    # from batch\n    \"Qwen2.5-0.5B_d005_s123_aligned\": 0.0976,\n    \"Qwen2.5-0.5B_d005_s42_para_aligned\": 0.0,\n    \"Qwen2.5-0.5B_d005_s123_para_aligned\": 0.0,\n    \"Qwen2.5-0.5B_d025_s42_aligned\": 0.1923,    # from d025_aligned_v2; note: possibly mislabeled\n    \"Qwen2.5-0.5B_d025_s123_aligned\": None,      # missing\n    \"Qwen2.5-0.5B_d025_s42_para_aligned\": None,  # missing\n    \"Qwen2.5-0.5B_d100_s42_aligned\": 0.0,        # from d100_aligned_v4\n    \"Qwen2.5-0.5B_d100_s123_aligned\": 0.1037,\n\n    # 1.5B\n    \"Qwen2.5-1.5B_d000_s42_aligned\": 0.128,      # from batch\n    \"Qwen2.5-1.5B_d000_s123_aligned\": 0.1707,\n    \"Qwen2.5-1.5B_d000_s42_para_aligned\": 0.0385, # from batch\n    \"Qwen2.5-1.5B_d005_s42_aligned\": 0.25,        # from batch/registry\n    \"Qwen2.5-1.5B_d005_s123_aligned\": None,       # missing\n    \"Qwen2.5-1.5B_d005_s42_para_aligned\": 0.1923, # from batch\n    \"Qwen2.5-1.5B_d025_s42_aligned\": 0.2256,\n    \"Qwen2.5-1.5B_d025_s123_aligned\": None,       # missing\n    \"Qwen2.5-1.5B_d025_s42_para_aligned\": 0.154,\n    \"Qwen2.5-1.5B_d100_s42_aligned\": 0.3049,      # from batch\n    \"Qwen2.5-1.5B_d100_s123_aligned\": 0.2805,\n    \"Qwen2.5-1.5B_d100_s42_para_aligned\": 0.2692, # from batch\n\n    # 3B (v2/alpha=32)\n    \"Qwen2.5-3B_d000_v2_s42_aligned\": 0.0976,\n    \"Qwen2.5-3B_d000_v2_s123_aligned\": 0.061,\n    \"Qwen2.5-3B_d000_v2_s42_para_aligned\": 0.0385,\n    \"Qwen2.5-3B_d000_v2_s123_para_aligned\": 0.0385,\n    \"Qwen2.5-3B_d005_s42_aligned\": 0.1463,\n    \"Qwen2.5-3B_d005_s42_para_aligned\": None,     # missing\n    \"Qwen2.5-3B_d005_s123_para_aligned\": 0.0769,\n    \"Qwen2.5-3B_d025_v2_aligned\": 0.0976,         # s42\n    \"Qwen2.5-3B_d025_s123_aligned\": 0.1585,\n    \"Qwen2.5-3B_d025_v2_s42_para_aligned\": 0.1154,\n    \"Qwen2.5-3B_d025_s123_para_aligned\": 0.1538,\n    \"Qwen2.5-3B_d100_v2_s42_aligned\": 0.1707,\n    \"Qwen2.5-3B_d100_v2_s123_aligned\": 0.1829,\n    \"Qwen2.5-3B_d100_v2_s42_para_aligned\": 0.1154,\n}\n\n# ============================================================\n# Build structured records\n# ============================================================\n\ndef parse_entry(dir_name, disk, he):\n    \"\"\"Parse directory name into structured record.\"\"\"\n    # Determine scale\n    if \"0.5B\" in dir_name:\n        scale = \"0.5B\"\n    elif \"1.5B\" in dir_name:\n        scale = \"1.5B\"\n    elif \"3B\" in dir_name:\n        scale = \"3B\"\n    else:\n        return None\n\n    # Determine eval type\n    if \"para_aligned\" in dir_name:\n        eval_type = \"para_aligned\"\n    elif \"aligned\" in dir_name:\n        eval_type = \"aligned\"\n    else:\n        return None\n\n    # Determine dose\n    for d in [\"d000\", \"d005\", \"d025\", \"d100\"]:\n        if d in dir_name:\n            dose_pct = {\"d000\": 0, \"d005\": 5, \"d025\": 25, \"d100\": 100}[d]\n            break\n    else:\n        return None\n\n    # Determine seed\n    if \"s123\" in dir_name:\n        seed = 123\n    elif \"s42\" in dir_name:\n        seed = 42\n    else:\n        # Some entries don't have explicit seed — check notes\n        # d025_v2_aligned is s42 per registry\n        seed = 42  # default assumption for entries without seed marker\n\n    # Notes for version tracking\n    notes = []\n    if \"_v2\" in dir_name or \"_v3\" in dir_name:\n        notes.append(\"alpha=32\")\n    if scale == \"3B\" and \"_v2\" not in dir_name and \"_v3\" not in dir_name:\n        if dose_pct in [25, 100]:\n            notes.append(\"WARNING: may be alpha=16\")\n        elif dose_pct == 0 and \"d000_v2\" not in dir_name:\n            notes.append(\"pre-v2 SFT\")\n\n    return {\n        \"scale\": scale,\n        \"dose_pct\": dose_pct,\n        \"seed\": seed,\n        \"eval_type\": eval_type,\n        \"mmlu\": round(disk[\"mmlu\"], 4),\n        \"gsm8k\": round(disk[\"gsm8k\"], 4),\n        \"arc\": round(disk[\"arc\"], 4),\n        \"humaneval\": round(he, 4) if he is not None else None,\n        \"source_dir\": dir_name,\n        \"notes\": \"; \".join(notes) if notes else \"\",\n    }\n\n\nrecords = []\nfor dir_name, disk in disk_data.items():\n    he = humaneval_registry.get(dir_name)\n    rec = parse_entry(dir_name, disk, he)\n    if rec:\n        records.append(rec)\n\n# Sort records\nrecords.sort(key=lambda r: (\n    {\"0.5B\": 0, \"1.5B\": 1, \"3B\": 2}[r[\"scale\"]],\n    r[\"dose_pct\"],\n    r[\"seed\"],\n    0 if r[\"eval_type\"] == \"aligned\" else 1,\n))\n\n# ============================================================\n# Compute cross-seed means and std\n# ============================================================\n\nagg_key = lambda r: (r[\"scale\"], r[\"dose_pct\"], r[\"eval_type\"])\ngroups = defaultdict(list)\nfor r in records:\n    groups[agg_key(r)].append(r)\n\naggregated = []\nfor key, recs in sorted(groups.items()):\n    scale, dose, etype = key\n    agg = {\"scale\": scale, \"dose_pct\": dose, \"eval_type\": etype, \"n_seeds\": len(recs)}\n    for bm in [\"mmlu\", \"gsm8k\", \"arc\", \"humaneval\"]:\n        vals = [r[bm] for r in recs if r[bm] is not None]\n        if vals:\n            agg[f\"{bm}_mean\"] = round(statistics.mean(vals), 4)\n            agg[f\"{bm}_std\"] = round(statistics.stdev(vals), 4) if len(vals) > 1 else None\n        else:\n            agg[f\"{bm}_mean\"] = None\n            agg[f\"{bm}_std\"] = None\n    aggregated.append(agg)\n\n# ============================================================\n# Dose-response curves\n# ============================================================\n\ndose_response = {}\nfor bm in [\"mmlu\", \"gsm8k\", \"arc\", \"humaneval\"]:\n    dose_response[bm] = {}\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        for etype in [\"aligned\", \"para_aligned\"]:\n            curve = []\n            for agg in aggregated:\n                if agg[\"scale\"] == scale and agg[\"eval_type\"] == etype:\n                    curve.append({\n                        \"dose_pct\": agg[\"dose_pct\"],\n                        \"mean\": agg[f\"{bm}_mean\"],\n                        \"std\": agg[f\"{bm}_std\"],\n                        \"n\": agg[\"n_seeds\"],\n                    })\n            if curve:\n                dose_response[bm][f\"{scale}_{etype}\"] = curve\n\n# ============================================================\n# Baselines\n# ============================================================\n\nbaselines = {\n    \"Qwen2.5-0.5B_base_pretrained\": {\n        \"mmlu\": 0.2294, \"gsm8k\": 0.1630, \"arc\": 0.2278, \"humaneval\": 0.0,\n        \"source\": \"exp_008_base_pretrained_eval_v2\"\n    },\n    \"Qwen2.5-0.5B-Instruct\": {\n        \"mmlu\": 0.2462, \"gsm8k\": 0.3882, \"arc\": 0.2816, \"humaneval\": 0.0,\n        \"source\": \"exp_008_instruct_05B_eval\"\n    },\n    \"Qwen2.5-1.5B_base_pretrained\": {\n        \"mmlu\": 0.2303, \"gsm8k\": 0.0053, \"arc\": 0.2304, \"humaneval\": 0.2317,\n        \"source\": \"exp_008_base_pretrained_15B_eval_v2\"\n    },\n}\n\n# ============================================================\n# Output JSON\n# ============================================================\n\noutput = {\n    \"metadata\": {\n        \"project\": \"contamcal-irt-calibration\",\n        \"description\": \"Eval metrics summary across all scales, doses, seeds, and eval types\",\n        \"scales\": [\"0.5B\", \"1.5B\", \"3B\"],\n        \"doses_pct\": [0, 5, 25, 100],\n        \"seeds\": [42, 123],\n        \"eval_types\": [\"aligned\", \"para_aligned\"],\n        \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc\", \"humaneval\"],\n        \"model_family\": \"Qwen2.5\",\n        \"lora_alpha\": 32,\n        \"notes\": [\n            \"HumanEval metrics from registry (not stored on disk)\",\n            \"3B uses v2 checkpoints (alpha=32); v1/DEPRECATED excluded\",\n            \"3B d005_s123_aligned eval is missing (never run)\",\n            \"3B d100_s123_para_aligned eval is missing\",\n            \"Some 0.5B/1.5B para_aligned s123 entries are missing\",\n            \"0.5B d025_s42 HumanEval=0.1923 may be from mislabeled para_aligned run\",\n        ],\n    },\n    \"individual_results\": records,\n    \"aggregated_by_dose\": aggregated,\n    \"dose_response_curves\": dose_response,\n    \"baselines\": baselines,\n}\n\njson_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json\"\nwith open(json_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"JSON saved to {json_path}\")\n\n# ============================================================\n# Output Markdown\n# ============================================================\n\nmd_lines = []\nmd_lines.append(\"# Eval Metrics Summary: contamcal-irt-calibration\")\nmd_lines.append(\"\")\nmd_lines.append(\"Model: Qwen2.5 (0.5B / 1.5B / 3B), LoRA alpha=32\")\nmd_lines.append(\"\")\nmd_lines.append(\"Doses: 0% (clean), 5%, 25%, 100% benchmark contamination in SFT data\")\nmd_lines.append(\"\")\nmd_lines.append(\"Eval types: **aligned** (original benchmark format), **para_aligned** (paraphrased questions)\")\nmd_lines.append(\"\")\n\n# Individual results table\nmd_lines.append(\"## Individual Results\")\nmd_lines.append(\"\")\nmd_lines.append(\"| Scale | Dose% | Seed | Eval Type | MMLU | GSM8K | ARC | HumanEval | Notes |\")\nmd_lines.append(\"|-------|-------|------|-----------|------|-------|-----|-----------|-------|\")\n\nfor r in records:\n    he_str = f\"{r['humaneval']:.4f}\" if r['humaneval'] is not None else \"—\"\n    md_lines.append(\n        f\"| {r['scale']} | {r['dose_pct']} | {r['seed']} | {r['eval_type']} \"\n        f\"| {r['mmlu']:.4f} | {r['gsm8k']:.4f} | {r['arc']:.4f} | {he_str} | {r['notes']} |\"\n    )\n\nmd_lines.append(\"\")\n\n# Aggregated table\nmd_lines.append(\"## Aggregated (Mean ± Std across seeds)\")\nmd_lines.append(\"\")\nmd_lines.append(\"| Scale | Dose% | Eval Type | N | MMLU | GSM8K | ARC | HumanEval |\")\nmd_lines.append(\"|-------|-------|-----------|---|------|-------|-----|-----------|\")\n\nfor a in aggregated:\n    cols = []\n    for bm in [\"mmlu\", \"gsm8k\", \"arc\", \"humaneval\"]:\n        m = a[f\"{bm}_mean\"]\n        s = a[f\"{bm}_std\"]\n        if m is None:\n            cols.append(\"—\")\n        elif s is not None:\n            cols.append(f\"{m:.4f}±{s:.4f}\")\n        else:\n            cols.append(f\"{m:.4f}\")\n    md_lines.append(\n        f\"| {a['scale']} | {a['dose_pct']} | {a['eval_type']} | {a['n_seeds']} \"\n        f\"| {cols[0]} | {cols[1]} | {cols[2]} | {cols[3]} |\"\n    )\n\nmd_lines.append(\"\")\n\n# Dose-response summary\nmd_lines.append(\"## Dose-Response Summary (aligned eval, mean across seeds)\")\nmd_lines.append(\"\")\nmd_lines.append(\"### MMLU\")\nmd_lines.append(\"| Dose% | 0.5B | 1.5B | 3B |\")\nmd_lines.append(\"|-------|------|------|-----|\")\n\nfor dose in [0, 5, 25, 100]:\n    vals = []\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        match = [a for a in aggregated if a[\"scale\"] == scale and a[\"dose_pct\"] == dose and a[\"eval_type\"] == \"aligned\"]\n        if match:\n            v = match[0][\"mmlu_mean\"]\n            vals.append(f\"{v:.4f}\" if v else \"—\")\n        else:\n            vals.append(\"—\")\n    md_lines.append(f\"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |\")\n\nmd_lines.append(\"\")\nmd_lines.append(\"### GSM8K\")\nmd_lines.append(\"| Dose% | 0.5B | 1.5B | 3B |\")\nmd_lines.append(\"|-------|------|------|-----|\")\n\nfor dose in [0, 5, 25, 100]:\n    vals = []\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        match = [a for a in aggregated if a[\"scale\"] == scale and a[\"dose_pct\"] == dose and a[\"eval_type\"] == \"aligned\"]\n        if match:\n            v = match[0][\"gsm8k_mean\"]\n            vals.append(f\"{v:.4f}\" if v else \"—\")\n        else:\n            vals.append(\"—\")\n    md_lines.append(f\"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |\")\n\nmd_lines.append(\"\")\nmd_lines.append(\"### ARC-Challenge\")\nmd_lines.append(\"| Dose% | 0.5B | 1.5B | 3B |\")\nmd_lines.append(\"|-------|------|------|-----|\")\n\nfor dose in [0, 5, 25, 100]:\n    vals = []\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        match = [a for a in aggregated if a[\"scale\"] == scale and a[\"dose_pct\"] == dose and a[\"eval_type\"] == \"aligned\"]\n        if match:\n            v = match[0][\"arc_mean\"]\n            vals.append(f\"{v:.4f}\" if v else \"—\")\n        else:\n            vals.append(\"—\")\n    md_lines.append(f\"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |\")\n\nmd_lines.append(\"\")\nmd_lines.append(\"### HumanEval\")\nmd_lines.append(\"| Dose% | 0.5B | 1.5B | 3B |\")\nmd_lines.append(\"|-------|------|------|-----|\")\n\nfor dose in [0, 5, 25, 100]:\n    vals = []\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        match = [a for a in aggregated if a[\"scale\"] == scale and a[\"dose_pct\"] == dose and a[\"eval_type\"] == \"aligned\"]\n        if match:\n            v = match[0][\"humaneval_mean\"]\n            vals.append(f\"{v:.4f}\" if v else \"—\")\n        else:\n            vals.append(\"—\")\n    md_lines.append(f\"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |\")\n\nmd_lines.append(\"\")\n\n# Baselines\nmd_lines.append(\"## Baselines (no SFT)\")\nmd_lines.append(\"\")\nmd_lines.append(\"| Model | MMLU | GSM8K | ARC | HumanEval |\")\nmd_lines.append(\"|-------|------|-------|-----|-----------|\")\nfor name, b in baselines.items():\n    he_str = f\"{b['humaneval']:.4f}\" if b['humaneval'] is not None else \"—\"\n    md_lines.append(f\"| {name} | {b['mmlu']:.4f} | {b['gsm8k']:.4f} | {b['arc']:.4f} | {he_str} |\")\n\nmd_lines.append(\"\")\n\n# Coverage matrix\nmd_lines.append(\"## Coverage Matrix\")\nmd_lines.append(\"\")\nmd_lines.append(\"✓ = both seeds, △ = seed 42 only, ✗ = missing\")\nmd_lines.append(\"\")\nmd_lines.append(\"| Scale | Dose% | Aligned | Para-aligned |\")\nmd_lines.append(\"|-------|-------|---------|--------------|\")\n\nfor scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n    for dose in [0, 5, 25, 100]:\n        statuses = []\n        for etype in [\"aligned\", \"para_aligned\"]:\n            matching = [r for r in records if r[\"scale\"] == scale and r[\"dose_pct\"] == dose and r[\"eval_type\"] == etype]\n            seeds = set(r[\"seed\"] for r in matching)\n            if seeds == {42, 123}:\n                statuses.append(\"✓\")\n            elif seeds == {42}:\n                statuses.append(\"△\")\n            elif seeds:\n                statuses.append(f\"seed={list(seeds)}\")\n            else:\n                statuses.append(\"✗\")\n        md_lines.append(f\"| {scale} | {dose} | {statuses[0]} | {statuses[1]} |\")\n\nmd_lines.append(\"\")\nmd_lines.append(\"## Notes\")\nmd_lines.append(\"\")\nmd_lines.append(\"- HumanEval metrics sourced from experiment registry (not stored in eval_results.json on disk)\")\nmd_lines.append(\"- 3B results use v2 checkpoints (LoRA alpha=32); v1/DEPRECATED (alpha=16) excluded\")\nmd_lines.append(\"- 3B d005_s123 aligned eval was never run\")\nmd_lines.append(\"- 3B d100_s123 para_aligned eval was never run\")\nmd_lines.append(\"- Several 0.5B and 1.5B para_aligned seed=123 entries are missing\")\nmd_lines.append(\"- 0.5B d025_s42 aligned HumanEval (0.1923) may originate from a mislabeled para_aligned run\")\nmd_lines.append(\"\")\n\nmd_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md\"\nwith open(md_path, \"w\") as f:\n    f.write(\"\\n\".join(md_lines))\nprint(f\"Markdown saved to {md_path}\")\n\n# Quick stats\nprint(f\"\\nTotal individual records: {len(records)}\")\nprint(f\"Aggregated groups: {len(aggregated)}\")\nfor scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n    n = sum(1 for r in records if r[\"scale\"] == scale)\n    print(f\"  {scale}: {n} entries\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 113_

<details open><summary>🔧 Tool call — Bash · `toolu_01TmerQEyr61F29tA59CQUuQ`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts && python3 compile_eval_summary.py",
  "description": "Run eval summary compilation script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "78c8d5fe-705f-4532-bfbf-0231851507a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THFcCFah1sv9mtnQyKyuNs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8587,
      "cache_read_input_tokens": 78720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8587
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

_source line 114 · 2026-05-15T18:35:14.678Z_

<details><summary>↩ Tool result · `toolu_01TmerQEyr61F29tA59CQUuQ`</summary>

```text
JSON saved to /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json
Markdown saved to /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md

Total individual records: 38
Aggregated groups: 23
  0.5B: 12 entries
  1.5B: 12 entries
  3B: 14 entries
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "2f300246-80d8-4ca7-9378-d36454719739",
  "tool_use_result": {
    "stdout": "JSON saved to /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json\nMarkdown saved to /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md\n\nTotal individual records: 38\nAggregated groups: 23\n  0.5B: 12 entries\n  1.5B: 12 entries\n  3B: 14 entries",
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

_source line 115_

<details open><summary>🔧 Tool call — Read · `toolu_01J9Yn5ybwZmdy6ZthUTKebX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "7ca6fd3c-40e0-46c6-a8d6-31a628fdaa8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7o2du1upcgbwS5cJPL4Bo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 87307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 116 · 2026-05-15T18:35:17.785Z_

<details><summary>↩ Tool result · `toolu_01J9Yn5ybwZmdy6ZthUTKebX`</summary>

```text
1	# Eval Metrics Summary: contamcal-irt-calibration
2	
3	Model: Qwen2.5 (0.5B / 1.5B / 3B), LoRA alpha=32
4	
5	Doses: 0% (clean), 5%, 25%, 100% benchmark contamination in SFT data
6	
7	Eval types: **aligned** (original benchmark format), **para_aligned** (paraphrased questions)
8	
9	## Individual Results
10	
11	| Scale | Dose% | Seed | Eval Type | MMLU | GSM8K | ARC | HumanEval | Notes |
12	|-------|-------|------|-----------|------|-------|-----|-----------|-------|
13	| 0.5B | 0 | 42 | aligned | 0.3979 | 0.3692 | 0.4693 | 0.1098 |  |
14	| 0.5B | 0 | 42 | para_aligned | 0.4428 | 0.2807 | 0.4792 | 0.1154 |  |
15	| 0.5B | 0 | 123 | aligned | 0.4216 | 0.3412 | 0.4974 | 0.1037 |  |
16	| 0.5B | 5 | 42 | aligned | 0.3255 | 0.3624 | 0.3285 | 0.0793 |  |
17	| 0.5B | 5 | 42 | para_aligned | 0.3548 | 0.2588 | 0.3300 | 0.0000 |  |
18	| 0.5B | 5 | 123 | aligned | 0.3002 | 0.3677 | 0.2978 | 0.0976 |  |
19	| 0.5B | 5 | 123 | para_aligned | 0.3166 | 0.2939 | 0.2912 | 0.0000 |  |
20	| 0.5B | 25 | 42 | aligned | 0.2803 | 0.3662 | 0.3251 | 0.1923 |  |
21	| 0.5B | 25 | 42 | para_aligned | 0.2835 | 0.3114 | 0.3199 | — |  |
22	| 0.5B | 25 | 123 | aligned | 0.3473 | 0.3533 | 0.4061 | — |  |
23	| 0.5B | 100 | 42 | aligned | 0.2334 | 0.3654 | 0.2944 | 0.0000 |  |
24	| 0.5B | 100 | 123 | aligned | 0.3058 | 0.3798 | 0.3669 | 0.1037 |  |
25	| 1.5B | 0 | 42 | aligned | 0.5853 | 0.6543 | 0.7722 | 0.1280 |  |
26	| 1.5B | 0 | 42 | para_aligned | 0.6096 | 0.5570 | 0.7547 | 0.0385 |  |
27	| 1.5B | 0 | 123 | aligned | 0.5855 | 0.6535 | 0.7577 | 0.1707 |  |
28	| 1.5B | 5 | 42 | aligned | 0.5852 | 0.6482 | 0.7688 | 0.2500 |  |
29	| 1.5B | 5 | 42 | para_aligned | 0.6164 | 0.5439 | 0.7532 | 0.1923 |  |
30	| 1.5B | 5 | 123 | aligned | 0.5869 | 0.6482 | 0.7568 | — |  |
31	| 1.5B | 25 | 42 | aligned | 0.5902 | 0.6535 | 0.7688 | 0.2256 |  |
32	| 1.5B | 25 | 42 | para_aligned | 0.6176 | 0.5395 | 0.7661 | 0.1540 |  |
33	| 1.5B | 25 | 123 | aligned | 0.5881 | 0.6550 | 0.7577 | — |  |
34	| 1.5B | 100 | 42 | aligned | 0.5933 | 0.6497 | 0.7688 | 0.3049 |  |
35	| 1.5B | 100 | 42 | para_aligned | 0.6252 | 0.5526 | 0.7661 | 0.2692 |  |
36	| 1.5B | 100 | 123 | aligned | 0.5956 | 0.6444 | 0.7816 | 0.2805 |  |
37	| 3B | 0 | 42 | aligned | 0.6295 | 0.3525 | 0.8183 | 0.0976 | alpha=32 |
38	| 3B | 0 | 42 | para_aligned | 0.6468 | 0.2895 | 0.8121 | 0.0385 | alpha=32 |
39	| 3B | 0 | 123 | aligned | 0.6314 | 0.2676 | 0.8259 | 0.0610 | alpha=32 |
40	| 3B | 0 | 123 | para_aligned | 0.6512 | 0.1491 | 0.8121 | 0.0385 | alpha=32 |
41	| 3B | 5 | 42 | aligned | 0.6345 | 0.2077 | 0.8294 | 0.1463 |  |
42	| 3B | 5 | 42 | para_aligned | 0.6542 | 0.1491 | 0.8221 | — |  |
43	| 3B | 5 | 123 | para_aligned | 0.6461 | 0.5000 | 0.8192 | 0.0769 |  |
44	| 3B | 25 | 42 | aligned | 0.5998 | 0.6793 | 0.8276 | 0.0976 | alpha=32 |
45	| 3B | 25 | 42 | para_aligned | 0.6210 | 0.5482 | 0.8106 | 0.1154 | alpha=32 |
46	| 3B | 25 | 123 | aligned | 0.6367 | 0.5254 | 0.8336 | 0.1585 | WARNING: may be alpha=16 |
47	| 3B | 25 | 123 | para_aligned | 0.6615 | 0.4254 | 0.8121 | 0.1538 | WARNING: may be alpha=16 |
48	| 3B | 100 | 42 | aligned | 0.6320 | 0.7415 | 0.8242 | 0.1707 | alpha=32 |
49	| 3B | 100 | 42 | para_aligned | 0.6590 | 0.5833 | 0.8092 | 0.1154 | alpha=32 |
50	| 3B | 100 | 123 | aligned | 0.6319 | 0.7324 | 0.8311 | 0.1829 | alpha=32 |
51	
52	## Aggregated (Mean ± Std across seeds)
53	
54	| Scale | Dose% | Eval Type | N | MMLU | GSM8K | ARC | HumanEval |
55	|-------|-------|-----------|---|------|-------|-----|-----------|
56	| 0.5B | 0 | aligned | 2 | 0.4097±0.0168 | 0.3552±0.0198 | 0.4834±0.0199 | 0.1067±0.0043 |
57	| 0.5B | 0 | para_aligned | 1 | 0.4428 | 0.2807 | 0.4792 | 0.1154 |
58	| 0.5B | 5 | aligned | 2 | 0.3129±0.0179 | 0.3650±0.0037 | 0.3132±0.0217 | 0.0885±0.0129 |
59	| 0.5B | 5 | para_aligned | 2 | 0.3357±0.0270 | 0.2763±0.0248 | 0.3106±0.0274 | 0.0000±0.0000 |
60	| 0.5B | 25 | aligned | 2 | 0.3138±0.0474 | 0.3598±0.0091 | 0.3656±0.0573 | 0.1923 |
61	| 0.5B | 25 | para_aligned | 1 | 0.2835 | 0.3114 | 0.3199 | — |
62	| 0.5B | 100 | aligned | 2 | 0.2696±0.0512 | 0.3726±0.0102 | 0.3306±0.0513 | 0.0519±0.0733 |
63	| 1.5B | 0 | aligned | 2 | 0.5854±0.0001 | 0.6539±0.0006 | 0.7650±0.0103 | 0.1493±0.0302 |
64	| 1.5B | 0 | para_aligned | 1 | 0.6096 | 0.5570 | 0.7547 | 0.0385 |
65	| 1.5B | 5 | aligned | 2 | 0.5860±0.0012 | 0.6482±0.0000 | 0.7628±0.0085 | 0.2500 |
66	| 1.5B | 5 | para_aligned | 1 | 0.6164 | 0.5439 | 0.7532 | 0.1923 |
67	| 1.5B | 25 | aligned | 2 | 0.5891±0.0015 | 0.6542±0.0011 | 0.7632±0.0078 | 0.2256 |
68	| 1.5B | 25 | para_aligned | 1 | 0.6176 | 0.5395 | 0.7661 | 0.1540 |
69	| 1.5B | 100 | aligned | 2 | 0.5945±0.0016 | 0.6471±0.0037 | 0.7752±0.0091 | 0.2927±0.0173 |
70	| 1.5B | 100 | para_aligned | 1 | 0.6252 | 0.5526 | 0.7661 | 0.2692 |
71	| 3B | 0 | aligned | 2 | 0.6304±0.0013 | 0.3100±0.0600 | 0.8221±0.0054 | 0.0793±0.0259 |
72	| 3B | 0 | para_aligned | 2 | 0.6490±0.0031 | 0.2193±0.0993 | 0.8121±0.0000 | 0.0385±0.0000 |
73	| 3B | 5 | aligned | 1 | 0.6345 | 0.2077 | 0.8294 | 0.1463 |
74	| 3B | 5 | para_aligned | 2 | 0.6502±0.0057 | 0.3246±0.2481 | 0.8207±0.0021 | 0.0769 |
75	| 3B | 25 | aligned | 2 | 0.6182±0.0261 | 0.6023±0.1088 | 0.8306±0.0042 | 0.1280±0.0431 |
76	| 3B | 25 | para_aligned | 2 | 0.6412±0.0286 | 0.4868±0.0868 | 0.8114±0.0011 | 0.1346±0.0272 |
77	| 3B | 100 | aligned | 2 | 0.6320±0.0001 | 0.7369±0.0064 | 0.8276±0.0049 | 0.1768±0.0086 |
78	| 3B | 100 | para_aligned | 1 | 0.6590 | 0.5833 | 0.8092 | 0.1154 |
79	
80	## Dose-Response Summary (aligned eval, mean across seeds)
81	
82	### MMLU
83	| Dose% | 0.5B | 1.5B | 3B |
84	|-------|------|------|-----|
85	| 0 | 0.4097 | 0.5854 | 0.6304 |
86	| 5 | 0.3129 | 0.5860 | 0.6345 |
87	| 25 | 0.3138 | 0.5891 | 0.6182 |
88	| 100 | 0.2696 | 0.5945 | 0.6320 |
89	
90	### GSM8K
91	| Dose% | 0.5B | 1.5B | 3B |
92	|-------|------|------|-----|
93	| 0 | 0.3552 | 0.6539 | 0.3100 |
94	| 5 | 0.3650 | 0.6482 | 0.2077 |
95	| 25 | 0.3598 | 0.6542 | 0.6023 |
96	| 100 | 0.3726 | 0.6471 | 0.7369 |
97	
98	### ARC-Challenge
99	| Dose% | 0.5B | 1.5B | 3B |
100	|-------|------|------|-----|
101	| 0 | 0.4834 | 0.7650 | 0.8221 |
102	| 5 | 0.3132 | 0.7628 | 0.8294 |
103	| 25 | 0.3656 | 0.7632 | 0.8306 |
104	| 100 | 0.3306 | 0.7752 | 0.8276 |
105	
106	### HumanEval
107	| Dose% | 0.5B | 1.5B | 3B |
108	|-------|------|------|-----|
109	| 0 | 0.1067 | 0.1493 | 0.0793 |
110	| 5 | 0.0885 | 0.2500 | 0.1463 |
111	| 25 | 0.1923 | 0.2256 | 0.1280 |
112	| 100 | 0.0519 | 0.2927 | 0.1768 |
113	
114	## Baselines (no SFT)
115	
116	| Model | MMLU | GSM8K | ARC | HumanEval |
117	|-------|------|-------|-----|-----------|
118	| Qwen2.5-0.5B_base_pretrained | 0.2294 | 0.1630 | 0.2278 | 0.0000 |
119	| Qwen2.5-0.5B-Instruct | 0.2462 | 0.3882 | 0.2816 | 0.0000 |
120	| Qwen2.5-1.5B_base_pretrained | 0.2303 | 0.0053 | 0.2304 | 0.2317 |
121	
122	## Coverage Matrix
123	
124	✓ = both seeds, △ = seed 42 only, ✗ = missing
125	
126	| Scale | Dose% | Aligned | Para-aligned |
127	|-------|-------|---------|--------------|
128	| 0.5B | 0 | ✓ | △ |
129	| 0.5B | 5 | ✓ | ✓ |
130	| 0.5B | 25 | ✓ | △ |
131	| 0.5B | 100 | ✓ | ✗ |
132	| 1.5B | 0 | ✓ | △ |
133	| 1.5B | 5 | ✓ | △ |
134	| 1.5B | 25 | ✓ | △ |
135	| 1.5B | 100 | ✓ | △ |
136	| 3B | 0 | ✓ | ✓ |
137	| 3B | 5 | △ | ✓ |
138	| 3B | 25 | ✓ | ✓ |
139	| 3B | 100 | ✓ | △ |
140	
141	## Notes
142	
143	- HumanEval metrics sourced from experiment registry (not stored in eval_results.json on disk)
144	- 3B results use v2 checkpoints (LoRA alpha=32); v1/DEPRECATED (alpha=16) excluded
145	- 3B d005_s123 aligned eval was never run
146	- 3B d100_s123 para_aligned eval was never run
147	- Several 0.5B and 1.5B para_aligned seed=123 entries are missing
148	- 0.5B d025_s42 aligned HumanEval (0.1923) may originate from a mislabeled para_aligned run
149	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "4394a34f-10df-439f-bd36-b013df698831",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md",
      "content": "# Eval Metrics Summary: contamcal-irt-calibration\n\nModel: Qwen2.5 (0.5B / 1.5B / 3B), LoRA alpha=32\n\nDoses: 0% (clean), 5%, 25%, 100% benchmark contamination in SFT data\n\nEval types: **aligned** (original benchmark format), **para_aligned** (paraphrased questions)\n\n## Individual Results\n\n| Scale | Dose% | Seed | Eval Type | MMLU | GSM8K | ARC | HumanEval | Notes |\n|-------|-------|------|-----------|------|-------|-----|-----------|-------|\n| 0.5B | 0 | 42 | aligned | 0.3979 | 0.3692 | 0.4693 | 0.1098 |  |\n| 0.5B | 0 | 42 | para_aligned | 0.4428 | 0.2807 | 0.4792 | 0.1154 |  |\n| 0.5B | 0 | 123 | aligned | 0.4216 | 0.3412 | 0.4974 | 0.1037 |  |\n| 0.5B | 5 | 42 | aligned | 0.3255 | 0.3624 | 0.3285 | 0.0793 |  |\n| 0.5B | 5 | 42 | para_aligned | 0.3548 | 0.2588 | 0.3300 | 0.0000 |  |\n| 0.5B | 5 | 123 | aligned | 0.3002 | 0.3677 | 0.2978 | 0.0976 |  |\n| 0.5B | 5 | 123 | para_aligned | 0.3166 | 0.2939 | 0.2912 | 0.0000 |  |\n| 0.5B | 25 | 42 | aligned | 0.2803 | 0.3662 | 0.3251 | 0.1923 |  |\n| 0.5B | 25 | 42 | para_aligned | 0.2835 | 0.3114 | 0.3199 | — |  |\n| 0.5B | 25 | 123 | aligned | 0.3473 | 0.3533 | 0.4061 | — |  |\n| 0.5B | 100 | 42 | aligned | 0.2334 | 0.3654 | 0.2944 | 0.0000 |  |\n| 0.5B | 100 | 123 | aligned | 0.3058 | 0.3798 | 0.3669 | 0.1037 |  |\n| 1.5B | 0 | 42 | aligned | 0.5853 | 0.6543 | 0.7722 | 0.1280 |  |\n| 1.5B | 0 | 42 | para_aligned | 0.6096 | 0.5570 | 0.7547 | 0.0385 |  |\n| 1.5B | 0 | 123 | aligned | 0.5855 | 0.6535 | 0.7577 | 0.1707 |  |\n| 1.5B | 5 | 42 | aligned | 0.5852 | 0.6482 | 0.7688 | 0.2500 |  |\n| 1.5B | 5 | 42 | para_aligned | 0.6164 | 0.5439 | 0.7532 | 0.1923 |  |\n| 1.5B | 5 | 123 | aligned | 0.5869 | 0.6482 | 0.7568 | — |  |\n| 1.5B | 25 | 42 | aligned | 0.5902 | 0.6535 | 0.7688 | 0.2256 |  |\n| 1.5B | 25 | 42 | para_aligned | 0.6176 | 0.5395 | 0.7661 | 0.1540 |  |\n| 1.5B | 25 | 123 | aligned | 0.5881 | 0.6550 | 0.7577 | — |  |\n| 1.5B | 100 | 42 | aligned | 0.5933 | 0.6497 | 0.7688 | 0.3049 |  |\n| 1.5B | 100 | 42 | para_aligned | 0.6252 | 0.5526 | 0.7661 | 0.2692 |  |\n| 1.5B | 100 | 123 | aligned | 0.5956 | 0.6444 | 0.7816 | 0.2805 |  |\n| 3B | 0 | 42 | aligned | 0.6295 | 0.3525 | 0.8183 | 0.0976 | alpha=32 |\n| 3B | 0 | 42 | para_aligned | 0.6468 | 0.2895 | 0.8121 | 0.0385 | alpha=32 |\n| 3B | 0 | 123 | aligned | 0.6314 | 0.2676 | 0.8259 | 0.0610 | alpha=32 |\n| 3B | 0 | 123 | para_aligned | 0.6512 | 0.1491 | 0.8121 | 0.0385 | alpha=32 |\n| 3B | 5 | 42 | aligned | 0.6345 | 0.2077 | 0.8294 | 0.1463 |  |\n| 3B | 5 | 42 | para_aligned | 0.6542 | 0.1491 | 0.8221 | — |  |\n| 3B | 5 | 123 | para_aligned | 0.6461 | 0.5000 | 0.8192 | 0.0769 |  |\n| 3B | 25 | 42 | aligned | 0.5998 | 0.6793 | 0.8276 | 0.0976 | alpha=32 |\n| 3B | 25 | 42 | para_aligned | 0.6210 | 0.5482 | 0.8106 | 0.1154 | alpha=32 |\n| 3B | 25 | 123 | aligned | 0.6367 | 0.5254 | 0.8336 | 0.1585 | WARNING: may be alpha=16 |\n| 3B | 25 | 123 | para_aligned | 0.6615 | 0.4254 | 0.8121 | 0.1538 | WARNING: may be alpha=16 |\n| 3B | 100 | 42 | aligned | 0.6320 | 0.7415 | 0.8242 | 0.1707 | alpha=32 |\n| 3B | 100 | 42 | para_aligned | 0.6590 | 0.5833 | 0.8092 | 0.1154 | alpha=32 |\n| 3B | 100 | 123 | aligned | 0.6319 | 0.7324 | 0.8311 | 0.1829 | alpha=32 |\n\n## Aggregated (Mean ± Std across seeds)\n\n| Scale | Dose% | Eval Type | N | MMLU | GSM8K | ARC | HumanEval |\n|-------|-------|-----------|---|------|-------|-----|-----------|\n| 0.5B | 0 | aligned | 2 | 0.4097±0.0168 | 0.3552±0.0198 | 0.4834±0.0199 | 0.1067±0.0043 |\n| 0.5B | 0 | para_aligned | 1 | 0.4428 | 0.2807 | 0.4792 | 0.1154 |\n| 0.5B | 5 | aligned | 2 | 0.3129±0.0179 | 0.3650±0.0037 | 0.3132±0.0217 | 0.0885±0.0129 |\n| 0.5B | 5 | para_aligned | 2 | 0.3357±0.0270 | 0.2763±0.0248 | 0.3106±0.0274 | 0.0000±0.0000 |\n| 0.5B | 25 | aligned | 2 | 0.3138±0.0474 | 0.3598±0.0091 | 0.3656±0.0573 | 0.1923 |\n| 0.5B | 25 | para_aligned | 1 | 0.2835 | 0.3114 | 0.3199 | — |\n| 0.5B | 100 | aligned | 2 | 0.2696±0.0512 | 0.3726±0.0102 | 0.3306±0.0513 | 0.0519±0.0733 |\n| 1.5B | 0 | aligned | 2 | 0.5854±0.0001 | 0.6539±0.0006 | 0.7650±0.0103 | 0.1493±0.0302 |\n| 1.5B | 0 | para_aligned | 1 | 0.6096 | 0.5570 | 0.7547 | 0.0385 |\n| 1.5B | 5 | aligned | 2 | 0.5860±0.0012 | 0.6482±0.0000 | 0.7628±0.0085 | 0.2500 |\n| 1.5B | 5 | para_aligned | 1 | 0.6164 | 0.5439 | 0.7532 | 0.1923 |\n| 1.5B | 25 | aligned | 2 | 0.5891±0.0015 | 0.6542±0.0011 | 0.7632±0.0078 | 0.2256 |\n| 1.5B | 25 | para_aligned | 1 | 0.6176 | 0.5395 | 0.7661 | 0.1540 |\n| 1.5B | 100 | aligned | 2 | 0.5945±0.0016 | 0.6471±0.0037 | 0.7752±0.0091 | 0.2927±0.0173 |\n| 1.5B | 100 | para_aligned | 1 | 0.6252 | 0.5526 | 0.7661 | 0.2692 |\n| 3B | 0 | aligned | 2 | 0.6304±0.0013 | 0.3100±0.0600 | 0.8221±0.0054 | 0.0793±0.0259 |\n| 3B | 0 | para_aligned | 2 | 0.6490±0.0031 | 0.2193±0.0993 | 0.8121±0.0000 | 0.0385±0.0000 |\n| 3B | 5 | aligned | 1 | 0.6345 | 0.2077 | 0.8294 | 0.1463 |\n| 3B | 5 | para_aligned | 2 | 0.6502±0.0057 | 0.3246±0.2481 | 0.8207±0.0021 | 0.0769 |\n| 3B | 25 | aligned | 2 | 0.6182±0.0261 | 0.6023±0.1088 | 0.8306±0.0042 | 0.1280±0.0431 |\n| 3B | 25 | para_aligned | 2 | 0.6412±0.0286 | 0.4868±0.0868 | 0.8114±0.0011 | 0.1346±0.0272 |\n| 3B | 100 | aligned | 2 | 0.6320±0.0001 | 0.7369±0.0064 | 0.8276±0.0049 | 0.1768±0.0086 |\n| 3B | 100 | para_aligned | 1 | 0.6590 | 0.5833 | 0.8092 | 0.1154 |\n\n## Dose-Response Summary (aligned eval, mean across seeds)\n\n### MMLU\n| Dose% | 0.5B | 1.5B | 3B |\n|-------|------|------|-----|\n| 0 | 0.4097 | 0.5854 | 0.6304 |\n| 5 | 0.3129 | 0.5860 | 0.6345 |\n| 25 | 0.3138 | 0.5891 | 0.6182 |\n| 100 | 0.2696 | 0.5945 | 0.6320 |\n\n### GSM8K\n| Dose% | 0.5B | 1.5B | 3B |\n|-------|------|------|-----|\n| 0 | 0.3552 | 0.6539 | 0.3100 |\n| 5 | 0.3650 | 0.6482 | 0.2077 |\n| 25 | 0.3598 | 0.6542 | 0.6023 |\n| 100 | 0.3726 | 0.6471 | 0.7369 |\n\n### ARC-Challenge\n| Dose% | 0.5B | 1.5B | 3B |\n|-------|------|------|-----|\n| 0 | 0.4834 | 0.7650 | 0.8221 |\n| 5 | 0.3132 | 0.7628 | 0.8294 |\n| 25 | 0.3656 | 0.7632 | 0.8306 |\n| 100 | 0.3306 | 0.7752 | 0.8276 |\n\n### HumanEval\n| Dose% | 0.5B | 1.5B | 3B |\n|-------|------|------|-----|\n| 0 | 0.1067 | 0.1493 | 0.0793 |\n| 5 | 0.0885 | 0.2500 | 0.1463 |\n| 25 | 0.1923 | 0.2256 | 0.1280 |\n| 100 | 0.0519 | 0.2927 | 0.1768 |\n\n## Baselines (no SFT)\n\n| Model | MMLU | GSM8K | ARC | HumanEval |\n|-------|------|-------|-----|-----------|\n| Qwen2.5-0.5B_base_pretrained | 0.2294 | 0.1630 | 0.2278 | 0.0000 |\n| Qwen2.5-0.5B-Instruct | 0.2462 | 0.3882 | 0.2816 | 0.0000 |\n| Qwen2.5-1.5B_base_pretrained | 0.2303 | 0.0053 | 0.2304 | 0.2317 |\n\n## Coverage Matrix\n\n✓ = both seeds, △ = seed 42 only, ✗ = missing\n\n| Scale | Dose% | Aligned | Para-aligned |\n|-------|-------|---------|--------------|\n| 0.5B | 0 | ✓ | △ |\n| 0.5B | 5 | ✓ | ✓ |\n| 0.5B | 25 | ✓ | △ |\n| 0.5B | 100 | ✓ | ✗ |\n| 1.5B | 0 | ✓ | △ |\n| 1.5B | 5 | ✓ | △ |\n| 1.5B | 25 | ✓ | △ |\n| 1.5B | 100 | ✓ | △ |\n| 3B | 0 | ✓ | ✓ |\n| 3B | 5 | △ | ✓ |\n| 3B | 25 | ✓ | ✓ |\n| 3B | 100 | ✓ | △ |\n\n## Notes\n\n- HumanEval metrics sourced from experiment registry (not stored in eval_results.json on disk)\n- 3B results use v2 checkpoints (LoRA alpha=32); v1/DEPRECATED (alpha=16) excluded\n- 3B d005_s123 aligned eval was never run\n- 3B d100_s123 para_aligned eval was never run\n- Several 0.5B and 1.5B para_aligned seed=123 entries are missing\n- 0.5B d025_s42 aligned HumanEval (0.1923) may originate from a mislabeled para_aligned run\n",
      "numLines": 149,
      "startLine": 1,
      "totalLines": 149
    }
  }
}
```

</details>

---

### Assistant

_source line 117_

<details><summary>Logged reasoning block</summary>

```text
The markdown looks good. Now let me also quickly verify the 3B d025_s123 note. The task says to exclude alpha=16 old 3B experiments for d025_s42, d100_s42, d100_s123. The d025_s123 entry I used is `Qwen2.5-3B_d025_s123_aligned` which doesn't have a v2 suffix. Looking at the task instructions:

> 只包含 alpha=32 的结果（排除已知 alpha=16 的旧 3B 实验: d025_s42, d100_s42, d100_s123 的旧版本）


So d025_s123 wasn't listed as having an old alpha=16 version—only d025_s42, d100_s42, and d100_s123 were flagged. This means d025_s123_aligned should be fine as alpha=32, even though my script warned about it, but I need to double-check d100_s123 since it was explicitly listed as having old versions.

Looking at the actual disk files, d100_v2_s123_aligned is correctly marked as v2, and d025_s123_aligned doesn't have a v2 suffix but shouldn't need one since d025_s123 never had the alpha=16 issue in the first place. I should remove that warning and update the script's logic to reflect that d025_s123 is believed to be alpha=32 based on the fact that only d025_s42 had the old version problem.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "8be36000-d727-4766-bfc6-2700a1786736",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01897uSzyoXZ93J4THicKfR7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5159,
      "cache_read_input_tokens": 87572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5159
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

_source line 118_

I need to fix the alpha=16 warning — the task says only d025_s42, d100_s42, d100_s123 had old alpha=16 versions. Let me correct that and also update the note for d025_s123.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "22ec71db-ec5d-478c-b8c0-47851f6afa2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01897uSzyoXZ93J4THicKfR7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5159,
      "cache_read_input_tokens": 87572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5159
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

_source line 119_

<details open><summary>🔧 Tool call — Edit · `toolu_01KusEWPVyRm6r8yuykzUSKz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/compile_eval_summary.py",
  "old_string": "    # Notes for version tracking\n    notes = []\n    if \"_v2\" in dir_name or \"_v3\" in dir_name:\n        notes.append(\"alpha=32\")\n    if scale == \"3B\" and \"_v2\" not in dir_name and \"_v3\" not in dir_name:\n        if dose_pct in [25, 100]:\n            notes.append(\"WARNING: may be alpha=16\")\n        elif dose_pct == 0 and \"d000_v2\" not in dir_name:\n            notes.append(\"pre-v2 SFT\")",
  "new_string": "    # Notes for version tracking\n    notes = []\n    if \"_v2\" in dir_name or \"_v3\" in dir_name:\n        notes.append(\"alpha=32\")\n    if scale == \"3B\" and \"_v2\" not in dir_name and \"_v3\" not in dir_name:\n        # Only d025_s42, d100_s42, d100_s123 had known alpha=16 old versions\n        # d025_s123 never had an old version, so it's presumed alpha=32\n        old_alpha16 = (\n            (dose_pct == 25 and seed == 42) or\n            (dose_pct == 100 and seed in [42, 123])\n        )\n        if old_alpha16:\n            notes.append(\"WARNING: may be alpha=16\")\n        elif dose_pct == 0 and \"d000_v2\" not in dir_name:\n            notes.append(\"pre-v2 SFT\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "09cbb7e4-e4b5-4cde-af2e-5e3e68980457",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01897uSzyoXZ93J4THicKfR7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5159,
      "cache_read_input_tokens": 87572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5159
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

_source line 120 · 2026-05-15T18:35:45.191Z_

<details><summary>↩ Tool result · `toolu_01KusEWPVyRm6r8yuykzUSKz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/compile_eval_summary.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "7f42d87a-2207-42ec-bdd2-d49cce851a49",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/compile_eval_summary.py",
    "oldString": "    # Notes for version tracking\n    notes = []\n    if \"_v2\" in dir_name or \"_v3\" in dir_name:\n        notes.append(\"alpha=32\")\n    if scale == \"3B\" and \"_v2\" not in dir_name and \"_v3\" not in dir_name:\n        if dose_pct in [25, 100]:\n            notes.append(\"WARNING: may be alpha=16\")\n        elif dose_pct == 0 and \"d000_v2\" not in dir_name:\n            notes.append(\"pre-v2 SFT\")",
    "newString": "    # Notes for version tracking\n    notes = []\n    if \"_v2\" in dir_name or \"_v3\" in dir_name:\n        notes.append(\"alpha=32\")\n    if scale == \"3B\" and \"_v2\" not in dir_name and \"_v3\" not in dir_name:\n        # Only d025_s42, d100_s42, d100_s123 had known alpha=16 old versions\n        # d025_s123 never had an old version, so it's presumed alpha=32\n        old_alpha16 = (\n            (dose_pct == 25 and seed == 42) or\n            (dose_pct == 100 and seed in [42, 123])\n        )\n        if old_alpha16:\n            notes.append(\"WARNING: may be alpha=16\")\n        elif dose_pct == 0 and \"d000_v2\" not in dir_name:\n            notes.append(\"pre-v2 SFT\")",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Compile all eval metrics into summary JSON and markdown table.\"\"\"\n\nimport json\nimport statistics\nfrom collections import defaultdict\n\n# ============================================================\n# Disk data: mmlu, gsm8k, arc_challenge (humaneval always null on disk)\n# Source: /root/autodl-tmp/exp001/eval_results/*/eval_results.json\n# ============================================================\n\ndisk_data = {\n    # ---- 0.5B ----\n    \"Qwen2.5-0.5B_d000_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3979, \"gsm8k\": 0.3692, \"arc\": 0.4693},\n    \"Qwen2.5-0.5B_d000_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.4216, \"gsm8k\": 0.3412, \"arc\": 0.4974},\n    \"Qwen2.5-0.5B_d000_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.4428, \"gsm8k\": 0.2807, \"arc\": 0.4792},\n    \"Qwen2.5-0.5B_d005_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3255, \"gsm8k\": 0.3624, \"arc\": 0.3285},\n    \"Qwen2.5-0.5B_d005_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3002, \"gsm8k\": 0.3677, \"arc\": 0.2978},\n    \"Qwen2.5-0.5B_d005_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.3548, \"gsm8k\": 0.2588, \"arc\": 0.3300},\n    \"Qwen2.5-0.5B_d005_s123_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.3166, \"gsm8k\": 0.2939, \"arc\": 0.2912},\n    \"Qwen2.5-0.5B_d025_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.2803, \"gsm8k\": 0.3662, \"arc\": 0.3251},\n    \"Qwen2.5-0.5B_d025_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3473, \"gsm8k\": 0.3533, \"arc\": 0.4061},\n    \"Qwen2.5-0.5B_d025_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.2835, \"gsm8k\": 0.3114, \"arc\": 0.3199},\n    \"Qwen2.5-0.5B_d100_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.2334, \"gsm8k\": 0.3654, \"arc\": 0.2944},\n    \"Qwen2.5-0.5B_d100_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.3058, \"gsm8k\": 0.3798, \"arc\": 0.3669},\n\n    # ---- 1.5B ----\n    \"Qwen2.5-1.5B_d000_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5853, \"gsm8k\": 0.6543, \"arc\": 0.7722},\n    \"Qwen2.5-1.5B_d000_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5855, \"gsm8k\": 0.6535, \"arc\": 0.7577},\n    \"Qwen2.5-1.5B_d000_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6096, \"gsm8k\": 0.5570, \"arc\": 0.7547},\n    \"Qwen2.5-1.5B_d005_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5852, \"gsm8k\": 0.6482, \"arc\": 0.7688},\n    \"Qwen2.5-1.5B_d005_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5869, \"gsm8k\": 0.6482, \"arc\": 0.7568},\n    \"Qwen2.5-1.5B_d005_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6164, \"gsm8k\": 0.5439, \"arc\": 0.7532},\n    \"Qwen2.5-1.5B_d025_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5902, \"gsm8k\": 0.6535, \"arc\": 0.7688},\n    \"Qwen2.5-1.5B_d025_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5881, \"gsm8k\": 0.6550, \"arc\": 0.7577},\n    \"Qwen2.5-1.5B_d025_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6176, \"gsm8k\": 0.5395, \"arc\": 0.7661},\n    \"Qwen2.5-1.5B_d100_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5933, \"gsm8k\": 0.6497, \"arc\": 0.7688},\n    \"Qwen2.5-1.5B_d100_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5956, \"gsm8k\": 0.6444, \"arc\": 0.7816},\n    \"Qwen2.5-1.5B_d100_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6252, \"gsm8k\": 0.5526, \"arc\": 0.7661},\n\n    # ---- 3B (v2/alpha=32 preferred) ----\n    \"Qwen2.5-3B_d000_v2_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6295, \"gsm8k\": 0.3525, \"arc\": 0.8183},\n    \"Qwen2.5-3B_d000_v2_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6314, \"gsm8k\": 0.2676, \"arc\": 0.8259},\n    \"Qwen2.5-3B_d000_v2_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6468, \"gsm8k\": 0.2895, \"arc\": 0.8121},\n    \"Qwen2.5-3B_d000_v2_s123_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6512, \"gsm8k\": 0.1491, \"arc\": 0.8121},\n    \"Qwen2.5-3B_d005_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6345, \"gsm8k\": 0.2077, \"arc\": 0.8294},\n    \"Qwen2.5-3B_d005_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6542, \"gsm8k\": 0.1491, \"arc\": 0.8221},\n    \"Qwen2.5-3B_d005_s123_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6461, \"gsm8k\": 0.5000, \"arc\": 0.8192},\n    \"Qwen2.5-3B_d025_v2_aligned\": {\"paraphrased\": False, \"mmlu\": 0.5998, \"gsm8k\": 0.6793, \"arc\": 0.8276},  # s42\n    \"Qwen2.5-3B_d025_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6367, \"gsm8k\": 0.5254, \"arc\": 0.8336},\n    \"Qwen2.5-3B_d025_v2_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6210, \"gsm8k\": 0.5482, \"arc\": 0.8106},\n    \"Qwen2.5-3B_d025_s123_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6615, \"gsm8k\": 0.4254, \"arc\": 0.8121},\n    \"Qwen2.5-3B_d100_v2_s42_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6320, \"gsm8k\": 0.7415, \"arc\": 0.8242},\n    \"Qwen2.5-3B_d100_v2_s123_aligned\": {\"paraphrased\": False, \"mmlu\": 0.6319, \"gsm8k\": 0.7324, \"arc\": 0.8311},\n    \"Qwen2.5-3B_d100_v2_s42_para_aligned\": {\"paraphrased\": True, \"mmlu\": 0.6590, \"gsm8k\": 0.5833, \"arc\": 0.8092},\n}\n\n# ============================================================\n# HumanEval data from registry (not on disk)\n# ============================================================\n\nhumaneval_registry = {\n    # 0.5B\n    \"Qwen2.5-0.5B_d000_s42_aligned\": 0.1098,   # from batch\n    \"Qwen2.5-0.5B_d000_s123_aligned\": 0.1037,\n    \"Qwen2.5-0.5B_d000_s42_para_aligned\": 0.1154,  # from batch\n    \"Qwen2.5-0.5B_d005_s42_aligned\": 0.0793,    # from batch\n    \"Qwen2.5-0.5B_d005_s123_aligned\": 0.0976,\n    \"Qwen2.5-0.5B_d005_s42_para_aligned\": 0.0,\n    \"Qwen2.5-0.5B_d005_s123_para_aligned\": 0.0,\n    \"Qwen2.5-0.5B_d025_s42_aligned\": 0.1923,    # from d025_aligned_v2; note: possibly mislabeled\n    \"Qwen2.5-0.5B_d025_s123_aligned\": None,      # missing\n    \"Qwen2.5-0.5B_d025_s42_para_aligned\": None,  # missing\n    \"Qwen2.5-0.5B_d100_s42_aligned\": 0.0,        # from d100_aligned_v4\n    \"Qwen2.5-0.5B_d100_s123_aligned\": 0.1037,\n\n    # 1.5B\n    \"Qwen2.5-1.5B_d000_s42_aligned\": 0.128,      # from batch\n    \"Qwen2.5-1.5B_d000_s123_aligned\": 0.1707,\n    \"Qwen2.5-1.5B_d000_s42_para_aligned\": 0.0385, # from batch\n    \"Qwen2.5-1.5B_d005_s42_aligned\": 0.25,        # from batch/registry\n    \"Qwen2.5-1.5B_d005_s123_aligned\": None,       # missing\n    \"Qwen2.5-1.5B_d005_s42_para_aligned\": 0.1923, # from batch\n    \"Qwen2.5-1.5B_d025_s42_aligned\": 0.2256,\n    \"Qwen2.5-1.5B_d025_s123_aligned\": None,       # missing\n    \"Qwen2.5-1.5B_d025_s42_para_aligned\": 0.154,\n    \"Qwen2.5-1.5B_d100_s42_aligned\": 0.3049,      # from batch\n    \"Qwen2.5-1.5B_d100_s123_aligned\": 0.2805,\n    \"Qwen2.5-1.5B_d100_s42_para_aligned\": 0.2692, # from batch\n\n    # 3B (v2/alpha=32)\n    \"Qwen2.5-3B_d000_v2_s42_aligned\": 0.0976,\n    \"Qwen2.5-3B_d000_v2_s123_aligned\": 0.061,\n    \"Qwen2.5-3B_d000_v2_s42_para_aligned\": 0.0385,\n    \"Qwen2.5-3B_d000_v2_s123_para_aligned\": 0.0385,\n    \"Qwen2.5-3B_d005_s42_aligned\": 0.1463,\n    \"Qwen2.5-3B_d005_s42_para_aligned\": None,     # missing\n    \"Qwen2.5-3B_d005_s123_para_aligned\": 0.0769,\n    \"Qwen2.5-3B_d025_v2_aligned\": 0.0976,         # s42\n    \"Qwen2.5-3B_d025_s123_aligned\": 0.1585,\n    \"Qwen2.5-3B_d025_v2_s42_para_aligned\": 0.1154,\n    \"Qwen2.5-3B_d025_s123_para_aligned\": 0.1538,\n    \"Qwen2.5-3B_d100_v2_s42_aligned\": 0.1707,\n    \"Qwen2.5-3B_d100_v2_s123_aligned\": 0.1829,\n    \"Qwen2.5-3B_d100_v2_s42_para_aligned\": 0.1154,\n}\n\n# ============================================================\n# Build structured records\n# ============================================================\n\ndef parse_entry(dir_name, disk, he):\n    \"\"\"Parse directory name into structured record.\"\"\"\n    # Determine scale\n    if \"0.5B\" in dir_name:\n        scale = \"0.5B\"\n    elif \"1.5B\" in dir_name:\n        scale = \"1.5B\"\n    elif \"3B\" in dir_name:\n        scale = \"3B\"\n    else:\n        return None\n\n    # Determine eval type\n    if \"para_aligned\" in dir_name:\n        eval_type = \"para_aligned\"\n    elif \"aligned\" in dir_name:\n        eval_type = \"aligned\"\n    else:\n        return None\n\n    # Determine dose\n    for d in [\"d000\", \"d005\", \"d025\", \"d100\"]:\n        if d in dir_name:\n            dose_pct = {\"d000\": 0, \"d005\": 5, \"d025\": 25, \"d100\": 100}[d]\n            break\n    else:\n        return None\n\n    # Determine seed\n    if \"s123\" in dir_name:\n        seed = 123\n    elif \"s42\" in dir_name:\n        seed = 42\n    else:\n        # Some entries don't have explicit seed — check notes\n        # d025_v2_aligned is s42 per registry\n        seed = 42  # default assumption for entries without seed marker\n\n    # Notes for version tracking\n    notes = []\n    if \"_v2\" in dir_name or \"_v3\" in dir_name:\n        notes.append(\"alpha=32\")\n    if scale == \"3B\" and \"_v2\" not in dir_name and \"_v3\" not in dir_name:\n        if dose_pct in [25, 100]:\n            notes.append(\"WARNING: may be alpha=16\")\n        elif dose_pct == 0 and \"d000_v2\" not in dir_name:\n            notes.append(\"pre-v2 SFT\")\n\n    return {\n        \"scale\": scale,\n        \"dose_pct\": dose_pct,\n        \"seed\": seed,\n        \"eval_type\": eval_type,\n        \"mmlu\": round(disk[\"mmlu\"], 4),\n        \"gsm8k\": round(disk[\"gsm8k\"], 4),\n        \"arc\": round(disk[\"arc\"], 4),\n        \"humaneval\": round(he, 4) if he is not None else None,\n        \"source_dir\": dir_name,\n        \"notes\": \"; \".join(notes) if notes else \"\",\n    }\n\n\nrecords = []\nfor dir_name, disk in disk_data.items():\n    he = humaneval_registry.get(dir_name)\n    rec = parse_entry(dir_name, disk, he)\n    if rec:\n        records.append(rec)\n\n# Sort records\nrecords.sort(key=lambda r: (\n    {\"0.5B\": 0, \"1.5B\": 1, \"3B\": 2}[r[\"scale\"]],\n    r[\"dose_pct\"],\n    r[\"seed\"],\n    0 if r[\"eval_type\"] == \"aligned\" else 1,\n))\n\n# ============================================================\n# Compute cross-seed means and std\n# ============================================================\n\nagg_key = lambda r: (r[\"scale\"], r[\"dose_pct\"], r[\"eval_type\"])\ngroups = defaultdict(list)\nfor r in records:\n    groups[agg_key(r)].append(r)\n\naggregated = []\nfor key, recs in sorted(groups.items()):\n    scale, dose, etype = key\n    agg = {\"scale\": scale, \"dose_pct\": dose, \"eval_type\": etype, \"n_seeds\": len(recs)}\n    for bm in [\"mmlu\", \"gsm8k\", \"arc\", \"humaneval\"]:\n        vals = [r[bm] for r in recs if r[bm] is not None]\n        if vals:\n            agg[f\"{bm}_mean\"] = round(statistics.mean(vals), 4)\n            agg[f\"{bm}_std\"] = round(statistics.stdev(vals), 4) if len(vals) > 1 else None\n        else:\n            agg[f\"{bm}_mean\"] = None\n            agg[f\"{bm}_std\"] = None\n    aggregated.append(agg)\n\n# ============================================================\n# Dose-response curves\n# ============================================================\n\ndose_response = {}\nfor bm in [\"mmlu\", \"gsm8k\", \"arc\", \"humaneval\"]:\n    dose_response[bm] = {}\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        for etype in [\"aligned\", \"para_aligned\"]:\n            curve = []\n            for agg in aggregated:\n                if agg[\"scale\"] == scale and agg[\"eval_type\"] == etype:\n                    curve.append({\n                        \"dose_pct\": agg[\"dose_pct\"],\n                        \"mean\": agg[f\"{bm}_mean\"],\n                        \"std\": agg[f\"{bm}_std\"],\n                        \"n\": agg[\"n_seeds\"],\n                    })\n            if curve:\n                dose_response[bm][f\"{scale}_{etype}\"] = curve\n\n# ============================================================\n# Baselines\n# ============================================================\n\nbaselines = {\n    \"Qwen2.5-0.5B_base_pretrained\": {\n        \"mmlu\": 0.2294, \"gsm8k\": 0.1630, \"arc\": 0.2278, \"humaneval\": 0.0,\n        \"source\": \"exp_008_base_pretrained_eval_v2\"\n    },\n    \"Qwen2.5-0.5B-Instruct\": {\n        \"mmlu\": 0.2462, \"gsm8k\": 0.3882, \"arc\": 0.2816, \"humaneval\": 0.0,\n        \"source\": \"exp_008_instruct_05B_eval\"\n    },\n    \"Qwen2.5-1.5B_base_pretrained\": {\n        \"mmlu\": 0.2303, \"gsm8k\": 0.0053, \"arc\": 0.2304, \"humaneval\": 0.2317,\n        \"source\": \"exp_008_base_pretrained_15B_eval_v2\"\n    },\n}\n\n# ============================================================\n# Output JSON\n# ============================================================\n\noutput = {\n    \"metadata\": {\n        \"project\": \"contamcal-irt-calibration\",\n        \"description\": \"Eval metrics summary across all scales, doses, seeds, and eval types\",\n        \"scales\": [\"0.5B\", \"1.5B\", \"3B\"],\n        \"doses_pct\": [0, 5, 25, 100],\n        \"seeds\": [42, 123],\n        \"eval_types\": [\"aligned\", \"para_aligned\"],\n        \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc\", \"humaneval\"],\n        \"model_family\": \"Qwen2.5\",\n        \"lora_alpha\": 32,\n        \"notes\": [\n            \"HumanEval metrics from registry (not stored on disk)\",\n            \"3B uses v2 checkpoints (alpha=32); v1/DEPRECATED excluded\",\n            \"3B d005_s123_aligned eval is missing (never run)\",\n            \"3B d100_s123_para_aligned eval is missing\",\n            \"Some 0.5B/1.5B para_aligned s123 entries are missing\",\n            \"0.5B d025_s42 HumanEval=0.1923 may be from mislabeled para_aligned run\",\n        ],\n    },\n    \"individual_results\": records,\n    \"aggregated_by_dose\": aggregated,\n    \"dose_response_curves\": dose_response,\n    \"baselines\": baselines,\n}\n\njson_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json\"\nwith open(json_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"JSON saved to {json_path}\")\n\n# ============================================================\n# Output Markdown\n# ============================================================\n\nmd_lines = []\nmd_lines.append(\"# Eval Metrics Summary: contamcal-irt-calibration\")\nmd_lines.append(\"\")\nmd_lines.append(\"Model: Qwen2.5 (0.5B / 1.5B / 3B), LoRA alpha=32\")\nmd_lines.append(\"\")\nmd_lines.append(\"Doses: 0% (clean), 5%, 25%, 100% benchmark contamination in SFT data\")\nmd_lines.append(\"\")\nmd_lines.append(\"Eval types: **aligned** (original benchmark format), **para_aligned** (paraphrased questions)\")\nmd_lines.append(\"\")\n\n# Individual results table\nmd_lines.append(\"## Individual Results\")\nmd_lines.append(\"\")\nmd_lines.append(\"| Scale | Dose% | Seed | Eval Type | MMLU | GSM8K | ARC | HumanEval | Notes |\")\nmd_lines.append(\"|-------|-------|------|-----------|------|-------|-----|-----------|-------|\")\n\nfor r in records:\n    he_str = f\"{r['humaneval']:.4f}\" if r['humaneval'] is not None else \"—\"\n    md_lines.append(\n        f\"| {r['scale']} | {r['dose_pct']} | {r['seed']} | {r['eval_type']} \"\n        f\"| {r['mmlu']:.4f} | {r['gsm8k']:.4f} | {r['arc']:.4f} | {he_str} | {r['notes']} |\"\n    )\n\nmd_lines.append(\"\")\n\n# Aggregated table\nmd_lines.append(\"## Aggregated (Mean ± Std across seeds)\")\nmd_lines.append(\"\")\nmd_lines.append(\"| Scale | Dose% | Eval Type | N | MMLU | GSM8K | ARC | HumanEval |\")\nmd_lines.append(\"|-------|-------|-----------|---|------|-------|-----|-----------|\")\n\nfor a in aggregated:\n    cols = []\n    for bm in [\"mmlu\", \"gsm8k\", \"arc\", \"humaneval\"]:\n        m = a[f\"{bm}_mean\"]\n        s = a[f\"{bm}_std\"]\n        if m is None:\n            cols.append(\"—\")\n        elif s is not None:\n            cols.append(f\"{m:.4f}±{s:.4f}\")\n        else:\n            cols.append(f\"{m:.4f}\")\n    md_lines.append(\n        f\"| {a['scale']} | {a['dose_pct']} | {a['eval_type']} | {a['n_seeds']} \"\n        f\"| {cols[0]} | {cols[1]} | {cols[2]} | {cols[3]} |\"\n    )\n\nmd_lines.append(\"\")\n\n# Dose-response summary\nmd_lines.append(\"## Dose-Response Summary (aligned eval, mean across seeds)\")\nmd_lines.append(\"\")\nmd_lines.append(\"### MMLU\")\nmd_lines.append(\"| Dose% | 0.5B | 1.5B | 3B |\")\nmd_lines.append(\"|-------|------|------|-----|\")\n\nfor dose in [0, 5, 25, 100]:\n    vals = []\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        match = [a for a in aggregated if a[\"scale\"] == scale and a[\"dose_pct\"] == dose and a[\"eval_type\"] == \"aligned\"]\n        if match:\n            v = match[0][\"mmlu_mean\"]\n            vals.append(f\"{v:.4f}\" if v else \"—\")\n        else:\n            vals.append(\"—\")\n    md_lines.append(f\"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |\")\n\nmd_lines.append(\"\")\nmd_lines.append(\"### GSM8K\")\nmd_lines.append(\"| Dose% | 0.5B | 1.5B | 3B |\")\nmd_lines.append(\"|-------|------|------|-----|\")\n\nfor dose in [0, 5, 25, 100]:\n    vals = []\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        match = [a for a in aggregated if a[\"scale\"] == scale and a[\"dose_pct\"] == dose and a[\"eval_type\"] == \"aligned\"]\n        if match:\n            v = match[0][\"gsm8k_mean\"]\n            vals.append(f\"{v:.4f}\" if v else \"—\")\n        else:\n            vals.append(\"—\")\n    md_lines.append(f\"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |\")\n\nmd_lines.append(\"\")\nmd_lines.append(\"### ARC-Challenge\")\nmd_lines.append(\"| Dose% | 0.5B | 1.5B | 3B |\")\nmd_lines.append(\"|-------|------|------|-----|\")\n\nfor dose in [0, 5, 25, 100]:\n    vals = []\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        match = [a for a in aggregated if a[\"scale\"] == scale and a[\"dose_pct\"] == dose and a[\"eval_type\"] == \"aligned\"]\n        if match:\n            v = match[0][\"arc_mean\"]\n            vals.append(f\"{v:.4f}\" if v else \"—\")\n        else:\n            vals.append(\"—\")\n    md_lines.append(f\"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |\")\n\nmd_lines.append(\"\")\nmd_lines.append(\"### HumanEval\")\nmd_lines.append(\"| Dose% | 0.5B | 1.5B | 3B |\")\nmd_lines.append(\"|-------|------|------|-----|\")\n\nfor dose in [0, 5, 25, 100]:\n    vals = []\n    for scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n        match = [a for a in aggregated if a[\"scale\"] == scale and a[\"dose_pct\"] == dose and a[\"eval_type\"] == \"aligned\"]\n        if match:\n            v = match[0][\"humaneval_mean\"]\n            vals.append(f\"{v:.4f}\" if v else \"—\")\n        else:\n            vals.append(\"—\")\n    md_lines.append(f\"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |\")\n\nmd_lines.append(\"\")\n\n# Baselines\nmd_lines.append(\"## Baselines (no SFT)\")\nmd_lines.append(\"\")\nmd_lines.append(\"| Model | MMLU | GSM8K | ARC | HumanEval |\")\nmd_lines.append(\"|-------|------|-------|-----|-----------|\")\nfor name, b in baselines.items():\n    he_str = f\"{b['humaneval']:.4f}\" if b['humaneval'] is not None else \"—\"\n    md_lines.append(f\"| {name} | {b['mmlu']:.4f} | {b['gsm8k']:.4f} | {b['arc']:.4f} | {he_str} |\")\n\nmd_lines.append(\"\")\n\n# Coverage matrix\nmd_lines.append(\"## Coverage Matrix\")\nmd_lines.append(\"\")\nmd_lines.append(\"✓ = both seeds, △ = seed 42 only, ✗ = missing\")\nmd_lines.append(\"\")\nmd_lines.append(\"| Scale | Dose% | Aligned | Para-aligned |\")\nmd_lines.append(\"|-------|-------|---------|--------------|\")\n\nfor scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n    for dose in [0, 5, 25, 100]:\n        statuses = []\n        for etype in [\"aligned\", \"para_aligned\"]:\n            matching = [r for r in records if r[\"scale\"] == scale and r[\"dose_pct\"] == dose and r[\"eval_type\"] == etype]\n            seeds = set(r[\"seed\"] for r in matching)\n            if seeds == {42, 123}:\n                statuses.append(\"✓\")\n            elif seeds == {42}:\n                statuses.append(\"△\")\n            elif seeds:\n                statuses.append(f\"seed={list(seeds)}\")\n            else:\n                statuses.append(\"✗\")\n        md_lines.append(f\"| {scale} | {dose} | {statuses[0]} | {statuses[1]} |\")\n\nmd_lines.append(\"\")\nmd_lines.append(\"## Notes\")\nmd_lines.append(\"\")\nmd_lines.append(\"- HumanEval metrics sourced from experiment registry (not stored in eval_results.json on disk)\")\nmd_lines.append(\"- 3B results use v2 checkpoints (LoRA alpha=32); v1/DEPRECATED (alpha=16) excluded\")\nmd_lines.append(\"- 3B d005_s123 aligned eval was never run\")\nmd_lines.append(\"- 3B d100_s123 para_aligned eval was never run\")\nmd_lines.append(\"- Several 0.5B and 1.5B para_aligned seed=123 entries are missing\")\nmd_lines.append(\"- 0.5B d025_s42 aligned HumanEval (0.1923) may originate from a mislabeled para_aligned run\")\nmd_lines.append(\"\")\n\nmd_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md\"\nwith open(md_path, \"w\") as f:\n    f.write(\"\\n\".join(md_lines))\nprint(f\"Markdown saved to {md_path}\")\n\n# Quick stats\nprint(f\"\\nTotal individual records: {len(records)}\")\nprint(f\"Aggregated groups: {len(aggregated)}\")\nfor scale in [\"0.5B\", \"1.5B\", \"3B\"]:\n    n = sum(1 for r in records if r[\"scale\"] == scale)\n    print(f\"  {scale}: {n} entries\")\n",
    "structuredPatch": [
      {
        "oldStart": 153,
        "oldLines": 7,
        "newStart": 153,
        "newLines": 13,
        "lines": [
          "     if \"_v2\" in dir_name or \"_v3\" in dir_name:",
          "         notes.append(\"alpha=32\")",
          "     if scale == \"3B\" and \"_v2\" not in dir_name and \"_v3\" not in dir_name:",
          "-        if dose_pct in [25, 100]:",
          "+        # Only d025_s42, d100_s42, d100_s123 had known alpha=16 old versions",
          "+        # d025_s123 never had an old version, so it's presumed alpha=32",
          "+        old_alpha16 = (",
          "+            (dose_pct == 25 and seed == 42) or",
          "+            (dose_pct == 100 and seed in [42, 123])",
          "+        )",
          "+        if old_alpha16:",
          "             notes.append(\"WARNING: may be alpha=16\")",
          "         elif dose_pct == 0 and \"d000_v2\" not in dir_name:",
          "             notes.append(\"pre-v2 SFT\")"
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

### Tool call

_source line 121_

<details open><summary>🔧 Tool call — Bash · `toolu_017NAnJ9cwSmjKBSqT1evzdS`</summary>

```json
{
  "command": "python3 compile_eval_summary.py",
  "description": "Re-run with fixed alpha=16 warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "8c2636ae-117b-4be5-b59d-90b50dd551f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mxGovqVoCWKqyd6U3X2ma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1261,
      "cache_read_input_tokens": 92731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1261
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

_source line 122 · 2026-05-15T18:35:49.431Z_

<details><summary>↩ Tool result · `toolu_017NAnJ9cwSmjKBSqT1evzdS`</summary>

```text
JSON saved to /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json
Markdown saved to /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md

Total individual records: 38
Aggregated groups: 23
  0.5B: 12 entries
  1.5B: 12 entries
  3B: 14 entries
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "7750cfd9-467e-4a3a-870f-99631b077bec",
  "tool_use_result": {
    "stdout": "JSON saved to /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json\nMarkdown saved to /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md\n\nTotal individual records: 38\nAggregated groups: 23\n  0.5B: 12 entries\n  1.5B: 12 entries\n  3B: 14 entries",
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

_source line 123_

Now let me register both artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "07a84886-8776-4ab9-9ff6-0fe412b6a54f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGBxnNRETC21b8cd24rHuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 93992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 235
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

_source line 124_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_019tjkUZUAX66ERg7hg7Uai8`</summary>

```json
{
  "name": "eval_metrics_summary_json",
  "type": "data",
  "description": "Complete eval metrics summary (JSON) across all scales (0.5B/1.5B/3B), doses (0/5/25/100%), seeds (42/123), eval types (aligned/para_aligned). Contains individual results, cross-seed aggregated means/std, dose-response curves, and baselines.",
  "project": "contamcal-irt-calibration",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json",
  "tags": [
    "eval",
    "metrics",
    "summary",
    "dose-response",
    "paper"
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
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "03574a12-3c7c-4f6b-8d57-5977606da079",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGBxnNRETC21b8cd24rHuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 93992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 235
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

_source line 125 · 2026-05-15T18:35:56.188Z_

<details><summary>↩ Tool result · `toolu_019tjkUZUAX66ERg7hg7Uai8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_57fe2f\", \"name\": \"eval_metrics_summary_json\", \"type\": \"data\", \"description\": \"Complete eval metrics summary (JSON) across all scales (0.5B/1.5B/3B), doses (0/5/25/100%), seeds (42/123), eval types (aligned/para_aligned). Contains individual results, cross-seed aggregated means/std, dose-response curves, and baselines.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/data/eval_metrics_summary.json\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T18:35:55.877050+00:00\", \"tags\": [\"eval\", \"metrics\", \"summary\", \"dose-response\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "f7f45a7c-683f-4344-ab3b-6ca683621898",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_57fe2f\\\", \\\"name\\\": \\\"eval_metrics_summary_json\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Complete eval metrics summary (JSON) across all scales (0.5B/1.5B/3B), doses (0/5/25/100%), seeds (42/123), eval types (aligned/para_aligned). Contains individual results, cross-seed aggregated means/std, dose-response curves, and baselines.\\\", \\\"path\\\": \\\"projects/contamcal-irt-calibration/artifacts/_project/data/eval_metrics_summary.json\\\", \\\"url\\\": null, \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T18:35:55.877050+00:00\\\", \\\"tags\\\": [\\\"eval\\\", \\\"metrics\\\", \\\"summary\\\", \\\"dose-response\\\", \\\"paper\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_57fe2f\", \"name\": \"eval_metrics_summary_json\", \"type\": \"data\", \"description\": \"Complete eval metrics summary (JSON) across all scales (0.5B/1.5B/3B), doses (0/5/25/100%), seeds (42/123), eval types (aligned/para_aligned). Contains individual results, cross-seed aggregated means/std, dose-response curves, and baselines.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/data/eval_metrics_summary.json\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T18:35:55.877050+00:00\", \"tags\": [\"eval\", \"metrics\", \"summary\", \"dose-response\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 126_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_018tfNhFe61pjKJdwgysCJRP`</summary>

```json
{
  "name": "eval_metrics_summary_md",
  "type": "report",
  "description": "Paper-ready markdown evidence tables: individual results, aggregated means±std, dose-response curves for MMLU/GSM8K/ARC/HumanEval across 3 scales, coverage matrix showing data completeness.",
  "project": "contamcal-irt-calibration",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md",
  "tags": [
    "eval",
    "metrics",
    "summary",
    "paper",
    "evidence-table"
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
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "31f597fb-0273-41e2-9930-1713751e10f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGBxnNRETC21b8cd24rHuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 93992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 235
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

_source line 127 · 2026-05-15T18:35:59.142Z_

<details><summary>↩ Tool result · `toolu_018tfNhFe61pjKJdwgysCJRP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_113eb8\", \"name\": \"eval_metrics_summary_md\", \"type\": \"report\", \"description\": \"Paper-ready markdown evidence tables: individual results, aggregated means±std, dose-response curves for MMLU/GSM8K/ARC/HumanEval across 3 scales, coverage matrix showing data completeness.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/report/eval_metrics_summary.md\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T18:35:58.678446+00:00\", \"tags\": [\"eval\", \"metrics\", \"summary\", \"paper\", \"evidence-table\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "e875461f-99e8-4dfe-a617-f0d87acda817",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_113eb8\\\", \\\"name\\\": \\\"eval_metrics_summary_md\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Paper-ready markdown evidence tables: individual results, aggregated means±std, dose-response curves for MMLU/GSM8K/ARC/HumanEval across 3 scales, coverage matrix showing data completeness.\\\", \\\"path\\\": \\\"projects/contamcal-irt-calibration/artifacts/_project/report/eval_metrics_summary.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T18:35:58.678446+00:00\\\", \\\"tags\\\": [\\\"eval\\\", \\\"metrics\\\", \\\"summary\\\", \\\"paper\\\", \\\"evidence-table\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_113eb8\", \"name\": \"eval_metrics_summary_md\", \"type\": \"report\", \"description\": \"Paper-ready markdown evidence tables: individual results, aggregated means±std, dose-response curves for MMLU/GSM8K/ARC/HumanEval across 3 scales, coverage matrix showing data completeness.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/report/eval_metrics_summary.md\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T18:35:58.678446+00:00\", \"tags\": [\"eval\", \"metrics\", \"summary\", \"paper\", \"evidence-table\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 128_

产出已生成并注册。汇总结果：

**38 条个体实验记录**（0.5B: 12, 1.5B: 12, 3B: 14），跨 4 个 dose × 2 个 seed × 2 种 eval type。

**关键发现（dose-response aligned eval 均值）：**

| Benchmark | 趋势 |
|-----------|------|
| **GSM8K** | 3B 有强 dose-response：0.31→0.21→0.60→0.74；1.5B 和 0.5B 几乎无变化 |
| **MMLU/ARC** | 所有 scale 下变化 <3pp，contamination 对 MC benchmark 信号微弱 |
| **HumanEval** | 1.5B 有清晰 dose-response：0.15→0.25→0.23→0.29；3B: 0.08→0.15→0.13→0.18 |

**数据缺口（Coverage Matrix）：**
- 大部分 para_aligned 只有 seed 42，缺 seed 123
- 3B d005_s123 aligned 未跑
- 3B d100_s123 para_aligned 未跑
- 0.5B d100 para_aligned 完全缺失

产出文件：
- `artifacts/eval_metrics_summary.json` — 机器可读 JSON（含 dose-response curves）
- `artifacts/eval_metrics_summary.md` — 论文级 markdown 表格

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "uuid": "b98baf35-fea8-4c64-aecd-ba3018a007c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rtJeghhDdN7bFH5T4QWz6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1241,
      "cache_read_input_tokens": 94227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1241
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

_source line 129_

产出已生成并注册。汇总结果：

**38 条个体实验记录**（0.5B: 12, 1.5B: 12, 3B: 14），跨 4 个 dose × 2 个 seed × 2 种 eval type。

**关键发现（dose-response aligned eval 均值）：**

| Benchmark | 趋势 |
|-----------|------|
| **GSM8K** | 3B 有强 dose-response：0.31→0.21→0.60→0.74；1.5B 和 0.5B 几乎无变化 |
| **MMLU/ARC** | 所有 scale 下变化 <3pp，contamination 对 MC benchmark 信号微弱 |
| **HumanEval** | 1.5B 有清晰 dose-response：0.15→0.25→0.23→0.29；3B: 0.08→0.15→0.13→0.18 |

**数据缺口（Coverage Matrix）：**
- 大部分 para_aligned 只有 seed 42，缺 seed 123
- 3B d005_s123 aligned 未跑
- 3B d100_s123 para_aligned 未跑
- 0.5B d100 para_aligned 完全缺失

产出文件：
- `artifacts/eval_metrics_summary.json` — 机器可读 JSON（含 dose-response curves）
- `artifacts/eval_metrics_summary.md` — 论文级 markdown 表格

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 650816,
  "duration_api_ms": 627195,
  "num_turns": 33,
  "stop_reason": "end_turn",
  "session_id": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "total_cost_usd": 2.6955855000000004,
  "usage": {
    "input_tokens": 32,
    "cache_creation_input_tokens": 83627,
    "cache_read_input_tokens": 1583074,
    "output_tokens": 30279,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 83627,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 420,
        "cache_read_input_tokens": 94227,
        "cache_creation_input_tokens": 1241,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1241
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1989,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002074,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 42,
      "outputTokens": 39635,
      "cacheReadInputTokens": 1773378,
      "cacheCreationInputTokens": 130518,
      "webSearchRequests": 0,
      "costUSD": 2.6935115000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9ede5d69-c3fe-4b4b-af47-fb7a8c50bcee"
}
```

</details>

---
