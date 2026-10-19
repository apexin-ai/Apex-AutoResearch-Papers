# prep per seed delta viz

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_prep_per-seed-delta-viz_20260515T020115.log`
- **Structured JSON:** [`f9657620de035f9cf51b.json`](../../sessions/f9/f9657620de035f9cf51b.json)

## Before a recorded user message

35 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
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
  "uuid": "92688b18-1f0d-4296-9354-bd186fe19ab7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
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
    "resetsAt": 1778825400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6782f3d7-058f-4618-bb8e-02ccb91417ca",
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to create a visualization script on a remote server. Let me break this down:

1. First, check existing plot scripts on the server
2. Write the script to the server
3. Run it with mock data to verify

Let me start by checking what's already there and detecting the image.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "79b3b5a8-dfcd-4ddf-a0a8-e25b22382fa7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kv1n44Uf3hobkrt1Hn8hh6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11967,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11967
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

先检查服务器环境和已有脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "88dc2d18-515b-483f-8fcb-5e13b80ee940",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kv1n44Uf3hobkrt1Hn8hh6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11967,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11967
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SsZp3p3Q6dBGftWxrEymS4`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "a3d28a6f-625c-424c-b4fe-bb29e481ac23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kv1n44Uf3hobkrt1Hn8hh6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11967,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11967
      },
      "output_tokens": 23,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T02:01:29.986Z_

<details><summary>↩ Tool result · `toolu_01SsZp3p3Q6dBGftWxrEymS4`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "2b95ecc6-a885-495c-9bbe-56edb8f7183b",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image · `toolu_011mx1ZzjwUvdSoTfuyQCgRA`</summary>

```json
{
  "server": "bjb1-42106",
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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "7d97bc22-52ad-4da3-be89-4c0ebdc7d927",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AovJ9ZpA4hnaBuLbRix2Zw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T02:01:34.212Z_

<details><summary>↩ Tool result · `toolu_011mx1ZzjwUvdSoTfuyQCgRA`</summary>

```text
{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "682c0292-7350-444c-9896-c94e6974e18b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\n  \\\"detected\\\": false,\\n  \\\"status\\\": \\\"unknown\\\",\\n  \\\"skip_base_setup\\\": false,\\n  \\\"message\\\": \\\"No image marker file found. Use traditional env-setup flow.\\\"\\n}\"}",
    "structuredContent": {
      "result": "{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011E7qzRPnQgtAztnXqoCEY9`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/structfuse/scripts/plot_*.py /root/structfuse/scripts/*viz*.py /root/structfuse/scripts/*figure*.py 2>/dev/null",
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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "bdeba789-c633-4cad-8c39-7ba1e8babd7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AovJ9ZpA4hnaBuLbRix2Zw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T02:01:34.224Z_

<details><summary>↩ Tool result · `toolu_011E7qzRPnQgtAztnXqoCEY9`</summary>

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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "d3e5c776-5275-47dd-897c-9e54617b7d35",
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013dx1zjJXLd88kiuYuEwarx`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/structfuse/scripts/",
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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "54d8e422-727d-449f-9290-d44a23f057e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ngUoaB4fTA7VojUrK4PGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 439,
      "cache_read_input_tokens": 24382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 439
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T02:01:38.663Z_

<details><summary>↩ Tool result · `toolu_013dx1zjJXLd88kiuYuEwarx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalyze_bm25_overlap_stratified.py\\nanalyze_confound.py\\nbuild_full_m2_data.sh\\nbuild_m1_training_data.py\\nbuild_m1_training_data.py.bak\\nbuild_p2b_data.py\\nclone_repos.sh\\ncollect_p2b_results.py\\ncompute_full_z_percent.py\\ndownload_metadata.py\\neval_p2b.py\\neval_p2b_pooled.py\\neval_swebench_e2e.py\\nfix_metadata.py\\nfix_metadata_arrow.py\\nm2_statistical_analysis.py\\nmigrate_m1_data.sh\\nmine_bm25_negatives.py\\nplot_neg_difficulty.py\\nprepare_m1_rerun.py\\nrerun_m1_failed.sh\\nrun_50repo_overlap.py\\nrun_eval_5missing.sh\\nrun_eval_all.sh\\nrun_eval_p50.sh\\nrun_full_m2_training.sh\\nrun_m1_extraction.sh\\nrun_m2_full_bm25_qwen.sh\\nrun_m2_full_bm25_starcoder.sh\\nrun_m2_pilot.sh\\nrun_p2b_all.sh\\nschedule_m2_runs.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "fbfae023-fdce-4469-b3e9-be2427580906",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"__pycache__\\\\nanalyze_bm25_overlap_stratified.py\\\\nanalyze_confound.py\\\\nbuild_full_m2_data.sh\\\\nbuild_m1_training_data.py\\\\nbuild_m1_training_data.py.bak\\\\nbuild_p2b_data.py\\\\nclone_repos.sh\\\\ncollect_p2b_results.py\\\\ncompute_full_z_percent.py\\\\ndownload_metadata.py\\\\neval_p2b.py\\\\neval_p2b_pooled.py\\\\neval_swebench_e2e.py\\\\nfix_metadata.py\\\\nfix_metadata_arrow.py\\\\nm2_statistical_analysis.py\\\\nmigrate_m1_data.sh\\\\nmine_bm25_negatives.py\\\\nplot_neg_difficulty.py\\\\nprepare_m1_rerun.py\\\\nrerun_m1_failed.sh\\\\nrun_50repo_overlap.py\\\\nrun_eval_5missing.sh\\\\nrun_eval_all.sh\\\\nrun_eval_p50.sh\\\\nrun_full_m2_training.sh\\\\nrun_m1_extraction.sh\\\\nrun_m2_full_bm25_qwen.sh\\\\nrun_m2_full_bm25_starcoder.sh\\\\nrun_m2_pilot.sh\\\\nrun_p2b_all.sh\\\\nschedule_m2_runs.sh\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalyze_bm25_overlap_stratified.py\\nanalyze_confound.py\\nbuild_full_m2_data.sh\\nbuild_m1_training_data.py\\nbuild_m1_training_data.py.bak\\nbuild_p2b_data.py\\nclone_repos.sh\\ncollect_p2b_results.py\\ncompute_full_z_percent.py\\ndownload_metadata.py\\neval_p2b.py\\neval_p2b_pooled.py\\neval_swebench_e2e.py\\nfix_metadata.py\\nfix_metadata_arrow.py\\nm2_statistical_analysis.py\\nmigrate_m1_data.sh\\nmine_bm25_negatives.py\\nplot_neg_difficulty.py\\nprepare_m1_rerun.py\\nrerun_m1_failed.sh\\nrun_50repo_overlap.py\\nrun_eval_5missing.sh\\nrun_eval_all.sh\\nrun_eval_p50.sh\\nrun_full_m2_training.sh\\nrun_m1_extraction.sh\\nrun_m2_full_bm25_qwen.sh\\nrun_m2_full_bm25_starcoder.sh\\nrun_m2_pilot.sh\\nrun_p2b_all.sh\\nschedule_m2_runs.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012QGD6aJ3f5yPm3TJKcxqeV`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "python3 -c \"import matplotlib; print(matplotlib.__version__)\"",
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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "832c8ea2-093a-481d-a3d7-148a1d9a7893",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ngUoaB4fTA7VojUrK4PGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 439,
      "cache_read_input_tokens": 24382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 439
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T02:01:39.155Z_

<details><summary>↩ Tool result · `toolu_012QGD6aJ3f5yPm3TJKcxqeV`</summary>

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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "2a2c76aa-5d11-472c-98fd-8328c3f4f4ad",
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

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
I see there's already a `plot_neg_difficulty.py` script. Let me check the existing scripts for style reference, and also check if matplotlib is available. Let me also look at the statistical analysis script for data format context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "7fe724b9-4c9e-4487-9690-d2f03fd33740",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VPBweki7x6w6RZXj5obPQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 806,
      "cache_read_input_tokens": 24821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 806
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

_source line 17_

已有 `plot_neg_difficulty.py` 和 `m2_statistical_analysis.py`，参考一下风格和数据格式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "0737e2fa-1722-4528-8c9c-27a9db231ffd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VPBweki7x6w6RZXj5obPQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 806,
      "cache_read_input_tokens": 24821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 806
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

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014XtECkQUbt6L2KD3hdWnrr`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/scripts/plot_neg_difficulty.py",
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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "c32e7930-e624-4fe5-b6ac-9089ac42f8b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VPBweki7x6w6RZXj5obPQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 806,
      "cache_read_input_tokens": 24821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 806
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

_source line 19 · 2026-05-15T02:01:44.575Z_

<details><summary>↩ Tool result · `toolu_014XtECkQUbt6L2KD3hdWnrr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Negative difficulty analysis visualization for StructFuse paper.\\n# Reads stats_v2 (128t) and stats_v3_2048 (2048t) JSON files,\\n# generates three publication-quality figures.\\n\\nimport json\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nimport matplotlib.colors as mcolors\\n\\nplt.rcParams.update({\\n    'font.family': 'DejaVu Sans',\\n    'font.size': 11,\\n    'axes.titlesize': 13,\\n    'axes.labelsize': 12,\\n    'xtick.labelsize': 10,\\n    'ytick.labelsize': 10,\\n    'legend.fontsize': 10,\\n    'figure.dpi': 300,\\n    'savefig.dpi': 300,\\n    'savefig.bbox': 'tight',\\n    'savefig.pad_inches': 0.05,\\n    'axes.spines.top': False,\\n    'axes.spines.right': False,\\n    'lines.linewidth': 1.8,\\n})\\n\\nOUTDIR = '/root/autodl-tmp/structfuse/artifacts/neg_difficulty_analysis/chart'\\n\\nDATA_128 = '/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v2.json'\\nDATA_2048 = '/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json'\\n\\nwith open(DATA_128) as f:\\n    d128 = json.load(f)\\nwith open(DATA_2048) as f:\\n    d2048 = json.load(f)\\n\\nSTRATEGIES = ['random', 'embedding_distance', 'dataflow_aware']\\nSTRAT_LABELS = ['Random', 'Embedding', 'Dataflow']\\nENCODERS = ['qwen', 'starcoder']\\nENC_LABELS = ['Qwen2.5-Coder-3B', 'StarCoder2-3B']\\n\\nC_QWEN = '#0072B2'\\nC_STAR = '#D55E00'\\n\\n\\n# ── Figure 1: Margin Comparison Bar Chart (2048t) ──\\n\\nfig, ax = plt.subplots(figsize=(4.5, 3.2))\\nx = np.arange(len(STRATEGIES))\\nw = 0.32\\n\\nqwen_margins = [d2048['qwen'][s]['margin_mean'] for s in STRATEGIES]\\nstar_margins = [d2048['starcoder'][s]['margin_mean'] for s in STRATEGIES]\\nqwen_stds = [d2048['qwen'][s]['margin_std'] / np.sqrt(d2048['qwen'][s]['n_pairs']) for s in STRATEGIES]\\nstar_stds = [d2048['starcoder'][s]['margin_std'] / np.sqrt(d2048['starcoder'][s]['n_pairs']) for s in STRATEGIES]\\n\\nbars_q = ax.bar(x - w/2, qwen_margins, w, yerr=qwen_stds, capsize=3,\\n                color=C_QWEN, alpha=0.85, label=ENC_LABELS[0], zorder=2,\\n                error_kw={'linewidth': 1.2})\\nbars_s = ax.bar(x + w/2, star_margins, w, yerr=star_stds, capsize=3,\\n                color=C_STAR, alpha=0.85, label=ENC_LABELS[1], zorder=2,\\n                error_kw={'linewidth': 1.2})\\n\\nfor i in range(len(STRATEGIES)):\\n    ratio = star_margins[i] / qwen_margins[i]\\n    y_top = star_margins[i] + star_stds[i] + 0.012\\n    ax.text(x[i] + w/2, y_top, f'{ratio:.1f}×', ha='center', va='bottom',\\n            fontsize=9, fontweight='bold', color='#333333')\\n\\nax.set_xticks(x)\\nax.set_xticklabels(STRAT_LABELS)\\nax.set_ylabel('Mean Margin (pos_sim − neg_sim)')\\nax.set_title('Negative Difficulty: Margin by Strategy (2048 tokens)')\\nax.legend(loc='upper right', framealpha=0.9)\\nax.set_ylim(0, max(star_margins) * 1.35)\\nax.axhline(0, color='gray', linewidth=0.5, zorder=1)\\n\\nfor fmt in ['pdf', 'png']:\\n    fig.savefig(f'{OUTDIR}/neg_difficulty_margin_comparison.{fmt}')\\nplt.close()\\nprint('Figure 1 saved: neg_difficulty_margin_comparison')\\n\\n\\n# ── Figure 2: Similarity Distribution (2048t) — grouped bar ──\\n\\nfig, axes = plt.subplots(1, 2, figsize=(8.0, 3.5))\\n\\nstrat_colors = ['#56B4E9', '#E69F00', '#009E73']\\n\\nfor idx, (enc, enc_label) in enumerate(zip(ENCODERS, ENC_LABELS)):\\n    ax = axes[idx]\\n    data = d2048[enc]\\n\\n    n_strat = len(STRATEGIES)\\n    x = np.arange(n_strat)\\n    w = 0.35\\n\\n    pos_vals = [data[s]['pos_sim_mean'] for s in STRATEGIES]\\n    neg_vals = [data[s]['neg_sim_mean'] for s in STRATEGIES]\\n    pos_ses = [data[s]['pos_sim_std'] / np.sqrt(data[s]['n_pairs']) for s in STRATEGIES]\\n    neg_ses = [data[s]['neg_sim_std'] / np.sqrt(data[s]['n_pairs']) for s in STRATEGIES]\\n\\n    bars_pos = ax.bar(x - w/2, pos_vals, w, yerr=pos_ses, capsize=3,\\n                      color=[c for c in strat_colors], alpha=0.9,\\n                      label='pos_sim', zorder=2, edgecolor='none',\\n                      error_kw={'linewidth': 1.0})\\n    bars_neg = ax.bar(x + w/2, neg_vals, w, yerr=neg_ses, capsize=3,\\n                      color=[c for c in strat_colors], alpha=0.45,\\n                      label='neg_sim', zorder=2, edgecolor='none',\\n                      hatch='///',\\n                      error_kw={'linewidth': 1.0})\\n\\n    # annotate margins\\n    for i in range(n_strat):\\n        margin = pos_vals[i] - neg_vals[i]\\n        mid_y = (pos_vals[i] + neg_vals[i]) / 2\\n        ax.annotate('', xy=(x[i] - w/2, pos_vals[i]),\\n                    xytext=(x[i] + w/2, neg_vals[i]),\\n                    arrowprops=dict(arrowstyle='<->', color='#333333',\\n                                    lw=1.2, shrinkA=2, shrinkB=2))\\n        ax.text(x[i] + w + 0.08, mid_y, f'Δ={margin:.3f}',\\n                fontsize=8, va='center', color='#333333')\\n\\n    ax.set_xticks(x)\\n    ax.set_xticklabels(STRAT_LABELS, fontsize=9)\\n    ax.set_title(enc_label, fontsize=12)\\n    ax.set_ylabel('Cosine Similarity')\\n\\n    # set y range to highlight differences\\n    if enc == 'qwen':\\n        ax.set_ylim(0.85, 1.01)\\n    else:\\n        ax.set_ylim(0.45, 0.9)\\n\\n    # legend for pos/neg distinction\\n    if idx == 0:\\n        import matplotlib.patches as mpatches\\n        pos_patch = mpatches.Patch(color='gray', alpha=0.9, label='pos_sim (solid)')\\n        neg_patch = mpatches.Patch(color='gray', alpha=0.45, hatch='///', label='neg_sim (hatched)')\\n        ax.legend(handles=[pos_patch, neg_patch], loc='lower left', fontsize=8, framealpha=0.9)\\n\\nplt.tight_layout()\\nfor fmt in ['pdf', 'png']:\\n    fig.savefig(f'{OUTDIR}/neg_difficulty_similarity_dist.{fmt}')\\nplt.close()\\nprint('Figure 2 saved: neg_difficulty_similarity_dist')\\n\\n\\n# ── Figure 3: Margin Ratio Heatmap (128 vs 2048) ──\\n\\nratio_matrix = np.zeros((2, 3))\\ndatasets = {'128': d128, '2048': d2048}\\nrow_labels = ['128 tokens', '2048 tokens']\\n\\nfor ri, (tlen, data) in enumerate(datasets.items()):\\n    for ci, s in enumerate(STRATEGIES):\\n        q_margin = data['qwen'][s]['margin_mean']\\n        s_margin = data['starcoder'][s]['margin_mean']\\n        ratio_matrix[ri, ci] = s_margin / q_margin\\n\\nfig, ax = plt.subplots(figsize=(4.2, 2.2))\\n\\nvmin = np.floor(ratio_matrix.min())\\nvmax = np.ceil(ratio_matrix.max())\\ncmap = plt.cm.YlOrRd\\nnorm = mcolors.Normalize(vmin=vmin, vmax=vmax)\\n\\nim = ax.imshow(ratio_matrix, cmap=cmap, norm=norm, aspect='auto')\\n\\nfor i in range(2):\\n    for j in range(3):\\n        val = ratio_matrix[i, j]\\n        text_color = 'white' if val > (vmin + vmax) / 1.5 else 'black'\\n        ax.text(j, i, f'{val:.1f}×', ha='center', va='center',\\n                fontsize=12, fontweight='bold', color=text_color)\\n\\nax.set_xticks(range(3))\\nax.set_yticks(range(2))\\nax.set_xticklabels(STRAT_LABELS)\\nax.set_yticklabels(row_labels)\\nax.set_title('StarCoder / Qwen Margin Ratio')\\n\\ncbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)\\ncbar.set_label('Ratio (×)')\\n\\nax.spines['top'].set_visible(True)\\nax.spines['right'].set_visible(True)\\n\\nplt.tight_layout()\\nfor fmt in ['pdf', 'png']:\\n    fig.savefig(f'{OUTDIR}/neg_difficulty_ratio_heatmap.{fmt}')\\nplt.close()\\nprint('Figure 3 saved: neg_difficulty_ratio_heatmap')\\n\\nprint('\\\\nAll figures saved to:', OUTDIR)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "65961668-09f5-43f4-851d-380a9b7187d8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"# Negative difficulty analysis visualization for StructFuse paper.\\\\n# Reads stats_v2 (128t) and stats_v3_2048 (2048t) JSON files,\\\\n# generates three publication-quality figures.\\\\n\\\\nimport json\\\\nimport numpy as np\\\\nimport matplotlib\\\\nmatplotlib.use('Agg')\\\\nimport matplotlib.pyplot as plt\\\\nimport matplotlib.colors as mcolors\\\\n\\\\nplt.rcParams.update({\\\\n    'font.family': 'DejaVu Sans',\\\\n    'font.size': 11,\\\\n    'axes.titlesize': 13,\\\\n    'axes.labelsize': 12,\\\\n    'xtick.labelsize': 10,\\\\n    'ytick.labelsize': 10,\\\\n    'legend.fontsize': 10,\\\\n    'figure.dpi': 300,\\\\n    'savefig.dpi': 300,\\\\n    'savefig.bbox': 'tight',\\\\n    'savefig.pad_inches': 0.05,\\\\n    'axes.spines.top': False,\\\\n    'axes.spines.right': False,\\\\n    'lines.linewidth': 1.8,\\\\n})\\\\n\\\\nOUTDIR = '/root/autodl-tmp/structfuse/artifacts/neg_difficulty_analysis/chart'\\\\n\\\\nDATA_128 = '/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v2.json'\\\\nDATA_2048 = '/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json'\\\\n\\\\nwith open(DATA_128) as f:\\\\n    d128 = json.load(f)\\\\nwith open(DATA_2048) as f:\\\\n    d2048 = json.load(f)\\\\n\\\\nSTRATEGIES = ['random', 'embedding_distance', 'dataflow_aware']\\\\nSTRAT_LABELS = ['Random', 'Embedding', 'Dataflow']\\\\nENCODERS = ['qwen', 'starcoder']\\\\nENC_LABELS = ['Qwen2.5-Coder-3B', 'StarCoder2-3B']\\\\n\\\\nC_QWEN = '#0072B2'\\\\nC_STAR = '#D55E00'\\\\n\\\\n\\\\n# ── Figure 1: Margin Comparison Bar Chart (2048t) ──\\\\n\\\\nfig, ax = plt.subplots(figsize=(4.5, 3.2))\\\\nx = np.arange(len(STRATEGIES))\\\\nw = 0.32\\\\n\\\\nqwen_margins = [d2048['qwen'][s]['margin_mean'] for s in STRATEGIES]\\\\nstar_margins = [d2048['starcoder'][s]['margin_mean'] for s in STRATEGIES]\\\\nqwen_stds = [d2048['qwen'][s]['margin_std'] / np.sqrt(d2048['qwen'][s]['n_pairs']) for s in STRATEGIES]\\\\nstar_stds = [d2048['starcoder'][s]['margin_std'] / np.sqrt(d2048['starcoder'][s]['n_pairs']) for s in STRATEGIES]\\\\n\\\\nbars_q = ax.bar(x - w/2, qwen_margins, w, yerr=qwen_stds, capsize=3,\\\\n                color=C_QWEN, alpha=0.85, label=ENC_LABELS[0], zorder=2,\\\\n                error_kw={'linewidth': 1.2})\\\\nbars_s = ax.bar(x + w/2, star_margins, w, yerr=star_stds, capsize=3,\\\\n                color=C_STAR, alpha=0.85, label=ENC_LABELS[1], zorder=2,\\\\n                error_kw={'linewidth': 1.2})\\\\n\\\\nfor i in range(len(STRATEGIES)):\\\\n    ratio = star_margins[i] / qwen_margins[i]\\\\n    y_top = star_margins[i] + star_stds[i] + 0.012\\\\n    ax.text(x[i] + w/2, y_top, f'{ratio:.1f}×', ha='center', va='bottom',\\\\n            fontsize=9, fontweight='bold', color='#333333')\\\\n\\\\nax.set_xticks(x)\\\\nax.set_xticklabels(STRAT_LABELS)\\\\nax.set_ylabel('Mean Margin (pos_sim − neg_sim)')\\\\nax.set_title('Negative Difficulty: Margin by Strategy (2048 tokens)')\\\\nax.legend(loc='upper right', framealpha=0.9)\\\\nax.set_ylim(0, max(star_margins) * 1.35)\\\\nax.axhline(0, color='gray', linewidth=0.5, zorder=1)\\\\n\\\\nfor fmt in ['pdf', 'png']:\\\\n    fig.savefig(f'{OUTDIR}/neg_difficulty_margin_comparison.{fmt}')\\\\nplt.close()\\\\nprint('Figure 1 saved: neg_difficulty_margin_comparison')\\\\n\\\\n\\\\n# ── Figure 2: Similarity Distribution (2048t) — grouped bar ──\\\\n\\\\nfig, axes = plt.subplots(1, 2, figsize=(8.0, 3.5))\\\\n\\\\nstrat_colors = ['#56B4E9', '#E69F00', '#009E73']\\\\n\\\\nfor idx, (enc, enc_label) in enumerate(zip(ENCODERS, ENC_LABELS)):\\\\n    ax = axes[idx]\\\\n    data = d2048[enc]\\\\n\\\\n    n_strat = len(STRATEGIES)\\\\n    x = np.arange(n_strat)\\\\n    w = 0.35\\\\n\\\\n    pos_vals = [data[s]['pos_sim_mean'] for s in STRATEGIES]\\\\n    neg_vals = [data[s]['neg_sim_mean'] for s in STRATEGIES]\\\\n    pos_ses = [data[s]['pos_sim_std'] / np.sqrt(data[s]['n_pairs']) for s in STRATEGIES]\\\\n    neg_ses = [data[s]['neg_sim_std'] / np.sqrt(data[s]['n_pairs']) for s in STRATEGIES]\\\\n\\\\n    bars_pos = ax.bar(x - w/2, pos_vals, w, yerr=pos_ses, capsize=3,\\\\n                      color=[c for c in strat_colors], alpha=0.9,\\\\n                      label='pos_sim', zorder=2, edgecolor='none',\\\\n                      error_kw={'linewidth': 1.0})\\\\n    bars_neg = ax.bar(x + w/2, neg_vals, w, yerr=neg_ses, capsize=3,\\\\n                      color=[c for c in strat_colors], alpha=0.45,\\\\n                      label='neg_sim', zorder=2, edgecolor='none',\\\\n                      hatch='///',\\\\n                      error_kw={'linewidth': 1.0})\\\\n\\\\n    # annotate margins\\\\n    for i in range(n_strat):\\\\n        margin = pos_vals[i] - neg_vals[i]\\\\n        mid_y = (pos_vals[i] + neg_vals[i]) / 2\\\\n        ax.annotate('', xy=(x[i] - w/2, pos_vals[i]),\\\\n                    xytext=(x[i] + w/2, neg_vals[i]),\\\\n                    arrowprops=dict(arrowstyle='<->', color='#333333',\\\\n                                    lw=1.2, shrinkA=2, shrinkB=2))\\\\n        ax.text(x[i] + w + 0.08, mid_y, f'Δ={margin:.3f}',\\\\n                fontsize=8, va='center', color='#333333')\\\\n\\\\n    ax.set_xticks(x)\\\\n    ax.set_xticklabels(STRAT_LABELS, fontsize=9)\\\\n    ax.set_title(enc_label, fontsize=12)\\\\n    ax.set_ylabel('Cosine Similarity')\\\\n\\\\n    # set y range to highlight differences\\\\n    if enc == 'qwen':\\\\n        ax.set_ylim(0.85, 1.01)\\\\n    else:\\\\n        ax.set_ylim(0.45, 0.9)\\\\n\\\\n    # legend for pos/neg distinction\\\\n    if idx == 0:\\\\n        import matplotlib.patches as mpatches\\\\n        pos_patch = mpatches.Patch(color='gray', alpha=0.9, label='pos_sim (solid)')\\\\n        neg_patch = mpatches.Patch(color='gray', alpha=0.45, hatch='///', label='neg_sim (hatched)')\\\\n        ax.legend(handles=[pos_patch, neg_patch], loc='lower left', fontsize=8, framealpha=0.9)\\\\n\\\\nplt.tight_layout()\\\\nfor fmt in ['pdf', 'png']:\\\\n    fig.savefig(f'{OUTDIR}/neg_difficulty_similarity_dist.{fmt}')\\\\nplt.close()\\\\nprint('Figure 2 saved: neg_difficulty_similarity_dist')\\\\n\\\\n\\\\n# ── Figure 3: Margin Ratio Heatmap (128 vs 2048) ──\\\\n\\\\nratio_matrix = np.zeros((2, 3))\\\\ndatasets = {'128': d128, '2048': d2048}\\\\nrow_labels = ['128 tokens', '2048 tokens']\\\\n\\\\nfor ri, (tlen, data) in enumerate(datasets.items()):\\\\n    for ci, s in enumerate(STRATEGIES):\\\\n        q_margin = data['qwen'][s]['margin_mean']\\\\n        s_margin = data['starcoder'][s]['margin_mean']\\\\n        ratio_matrix[ri, ci] = s_margin / q_margin\\\\n\\\\nfig, ax = plt.subplots(figsize=(4.2, 2.2))\\\\n\\\\nvmin = np.floor(ratio_matrix.min())\\\\nvmax = np.ceil(ratio_matrix.max())\\\\ncmap = plt.cm.YlOrRd\\\\nnorm = mcolors.Normalize(vmin=vmin, vmax=vmax)\\\\n\\\\nim = ax.imshow(ratio_matrix, cmap=cmap, norm=norm, aspect='auto')\\\\n\\\\nfor i in range(2):\\\\n    for j in range(3):\\\\n        val = ratio_matrix[i, j]\\\\n        text_color = 'white' if val > (vmin + vmax) / 1.5 else 'black'\\\\n        ax.text(j, i, f'{val:.1f}×', ha='center', va='center',\\\\n                fontsize=12, fontweight='bold', color=text_color)\\\\n\\\\nax.set_xticks(range(3))\\\\nax.set_yticks(range(2))\\\\nax.set_xticklabels(STRAT_LABELS)\\\\nax.set_yticklabels(row_labels)\\\\nax.set_title('StarCoder / Qwen Margin Ratio')\\\\n\\\\ncbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)\\\\ncbar.set_label('Ratio (×)')\\\\n\\\\nax.spines['top'].set_visible(True)\\\\nax.spines['right'].set_visible(True)\\\\n\\\\nplt.tight_layout()\\\\nfor fmt in ['pdf', 'png']:\\\\n    fig.savefig(f'{OUTDIR}/neg_difficulty_ratio_heatmap.{fmt}')\\\\nplt.close()\\\\nprint('Figure 3 saved: neg_difficulty_ratio_heatmap')\\\\n\\\\nprint('\\\\\\\\nAll figures saved to:', OUTDIR)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"# Negative difficulty analysis visualization for StructFuse paper.\\n# Reads stats_v2 (128t) and stats_v3_2048 (2048t) JSON files,\\n# generates three publication-quality figures.\\n\\nimport json\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nimport matplotlib.colors as mcolors\\n\\nplt.rcParams.update({\\n    'font.family': 'DejaVu Sans',\\n    'font.size': 11,\\n    'axes.titlesize': 13,\\n    'axes.labelsize': 12,\\n    'xtick.labelsize': 10,\\n    'ytick.labelsize': 10,\\n    'legend.fontsize': 10,\\n    'figure.dpi': 300,\\n    'savefig.dpi': 300,\\n    'savefig.bbox': 'tight',\\n    'savefig.pad_inches': 0.05,\\n    'axes.spines.top': False,\\n    'axes.spines.right': False,\\n    'lines.linewidth': 1.8,\\n})\\n\\nOUTDIR = '/root/autodl-tmp/structfuse/artifacts/neg_difficulty_analysis/chart'\\n\\nDATA_128 = '/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v2.json'\\nDATA_2048 = '/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json'\\n\\nwith open(DATA_128) as f:\\n    d128 = json.load(f)\\nwith open(DATA_2048) as f:\\n    d2048 = json.load(f)\\n\\nSTRATEGIES = ['random', 'embedding_distance', 'dataflow_aware']\\nSTRAT_LABELS = ['Random', 'Embedding', 'Dataflow']\\nENCODERS = ['qwen', 'starcoder']\\nENC_LABELS = ['Qwen2.5-Coder-3B', 'StarCoder2-3B']\\n\\nC_QWEN = '#0072B2'\\nC_STAR = '#D55E00'\\n\\n\\n# ── Figure 1: Margin Comparison Bar Chart (2048t) ──\\n\\nfig, ax = plt.subplots(figsize=(4.5, 3.2))\\nx = np.arange(len(STRATEGIES))\\nw = 0.32\\n\\nqwen_margins = [d2048['qwen'][s]['margin_mean'] for s in STRATEGIES]\\nstar_margins = [d2048['starcoder'][s]['margin_mean'] for s in STRATEGIES]\\nqwen_stds = [d2048['qwen'][s]['margin_std'] / np.sqrt(d2048['qwen'][s]['n_pairs']) for s in STRATEGIES]\\nstar_stds = [d2048['starcoder'][s]['margin_std'] / np.sqrt(d2048['starcoder'][s]['n_pairs']) for s in STRATEGIES]\\n\\nbars_q = ax.bar(x - w/2, qwen_margins, w, yerr=qwen_stds, capsize=3,\\n                color=C_QWEN, alpha=0.85, label=ENC_LABELS[0], zorder=2,\\n                error_kw={'linewidth': 1.2})\\nbars_s = ax.bar(x + w/2, star_margins, w, yerr=star_stds, capsize=3,\\n                color=C_STAR, alpha=0.85, label=ENC_LABELS[1], zorder=2,\\n                error_kw={'linewidth': 1.2})\\n\\nfor i in range(len(STRATEGIES)):\\n    ratio = star_margins[i] / qwen_margins[i]\\n    y_top = star_margins[i] + star_stds[i] + 0.012\\n    ax.text(x[i] + w/2, y_top, f'{ratio:.1f}×', ha='center', va='bottom',\\n            fontsize=9, fontweight='bold', color='#333333')\\n\\nax.set_xticks(x)\\nax.set_xticklabels(STRAT_LABELS)\\nax.set_ylabel('Mean Margin (pos_sim − neg_sim)')\\nax.set_title('Negative Difficulty: Margin by Strategy (2048 tokens)')\\nax.legend(loc='upper right', framealpha=0.9)\\nax.set_ylim(0, max(star_margins) * 1.35)\\nax.axhline(0, color='gray', linewidth=0.5, zorder=1)\\n\\nfor fmt in ['pdf', 'png']:\\n    fig.savefig(f'{OUTDIR}/neg_difficulty_margin_comparison.{fmt}')\\nplt.close()\\nprint('Figure 1 saved: neg_difficulty_margin_comparison')\\n\\n\\n# ── Figure 2: Similarity Distribution (2048t) — grouped bar ──\\n\\nfig, axes = plt.subplots(1, 2, figsize=(8.0, 3.5))\\n\\nstrat_colors = ['#56B4E9', '#E69F00', '#009E73']\\n\\nfor idx, (enc, enc_label) in enumerate(zip(ENCODERS, ENC_LABELS)):\\n    ax = axes[idx]\\n    data = d2048[enc]\\n\\n    n_strat = len(STRATEGIES)\\n    x = np.arange(n_strat)\\n    w = 0.35\\n\\n    pos_vals = [data[s]['pos_sim_mean'] for s in STRATEGIES]\\n    neg_vals = [data[s]['neg_sim_mean'] for s in STRATEGIES]\\n    pos_ses = [data[s]['pos_sim_std'] / np.sqrt(data[s]['n_pairs']) for s in STRATEGIES]\\n    neg_ses = [data[s]['neg_sim_std'] / np.sqrt(data[s]['n_pairs']) for s in STRATEGIES]\\n\\n    bars_pos = ax.bar(x - w/2, pos_vals, w, yerr=pos_ses, capsize=3,\\n                      color=[c for c in strat_colors], alpha=0.9,\\n                      label='pos_sim', zorder=2, edgecolor='none',\\n                      error_kw={'linewidth': 1.0})\\n    bars_neg = ax.bar(x + w/2, neg_vals, w, yerr=neg_ses, capsize=3,\\n                      color=[c for c in strat_colors], alpha=0.45,\\n                      label='neg_sim', zorder=2, edgecolor='none',\\n                      hatch='///',\\n                      error_kw={'linewidth': 1.0})\\n\\n    # annotate margins\\n    for i in range(n_strat):\\n        margin = pos_vals[i] - neg_vals[i]\\n        mid_y = (pos_vals[i] + neg_vals[i]) / 2\\n        ax.annotate('', xy=(x[i] - w/2, pos_vals[i]),\\n                    xytext=(x[i] + w/2, neg_vals[i]),\\n                    arrowprops=dict(arrowstyle='<->', color='#333333',\\n                                    lw=1.2, shrinkA=2, shrinkB=2))\\n        ax.text(x[i] + w + 0.08, mid_y, f'Δ={margin:.3f}',\\n                fontsize=8, va='center', color='#333333')\\n\\n    ax.set_xticks(x)\\n    ax.set_xticklabels(STRAT_LABELS, fontsize=9)\\n    ax.set_title(enc_label, fontsize=12)\\n    ax.set_ylabel('Cosine Similarity')\\n\\n    # set y range to highlight differences\\n    if enc == 'qwen':\\n        ax.set_ylim(0.85, 1.01)\\n    else:\\n        ax.set_ylim(0.45, 0.9)\\n\\n    # legend for pos/neg distinction\\n    if idx == 0:\\n        import matplotlib.patches as mpatches\\n        pos_patch = mpatches.Patch(color='gray', alpha=0.9, label='pos_sim (solid)')\\n        neg_patch = mpatches.Patch(color='gray', alpha=0.45, hatch='///', label='neg_sim (hatched)')\\n        ax.legend(handles=[pos_patch, neg_patch], loc='lower left', fontsize=8, framealpha=0.9)\\n\\nplt.tight_layout()\\nfor fmt in ['pdf', 'png']:\\n    fig.savefig(f'{OUTDIR}/neg_difficulty_similarity_dist.{fmt}')\\nplt.close()\\nprint('Figure 2 saved: neg_difficulty_similarity_dist')\\n\\n\\n# ── Figure 3: Margin Ratio Heatmap (128 vs 2048) ──\\n\\nratio_matrix = np.zeros((2, 3))\\ndatasets = {'128': d128, '2048': d2048}\\nrow_labels = ['128 tokens', '2048 tokens']\\n\\nfor ri, (tlen, data) in enumerate(datasets.items()):\\n    for ci, s in enumerate(STRATEGIES):\\n        q_margin = data['qwen'][s]['margin_mean']\\n        s_margin = data['starcoder'][s]['margin_mean']\\n        ratio_matrix[ri, ci] = s_margin / q_margin\\n\\nfig, ax = plt.subplots(figsize=(4.2, 2.2))\\n\\nvmin = np.floor(ratio_matrix.min())\\nvmax = np.ceil(ratio_matrix.max())\\ncmap = plt.cm.YlOrRd\\nnorm = mcolors.Normalize(vmin=vmin, vmax=vmax)\\n\\nim = ax.imshow(ratio_matrix, cmap=cmap, norm=norm, aspect='auto')\\n\\nfor i in range(2):\\n    for j in range(3):\\n        val = ratio_matrix[i, j]\\n        text_color = 'white' if val > (vmin + vmax) / 1.5 else 'black'\\n        ax.text(j, i, f'{val:.1f}×', ha='center', va='center',\\n                fontsize=12, fontweight='bold', color=text_color)\\n\\nax.set_xticks(range(3))\\nax.set_yticks(range(2))\\nax.set_xticklabels(STRAT_LABELS)\\nax.set_yticklabels(row_labels)\\nax.set_title('StarCoder / Qwen Margin Ratio')\\n\\ncbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)\\ncbar.set_label('Ratio (×)')\\n\\nax.spines['top'].set_visible(True)\\nax.spines['right'].set_visible(True)\\n\\nplt.tight_layout()\\nfor fmt in ['pdf', 'png']:\\n    fig.savefig(f'{OUTDIR}/neg_difficulty_ratio_heatmap.{fmt}')\\nplt.close()\\nprint('Figure 3 saved: neg_difficulty_ratio_heatmap')\\n\\nprint('\\\\nAll figures saved to:', OUTDIR)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HiaTjD74nR84tkBQUNqFcq`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -80 /root/structfuse/scripts/m2_statistical_analysis.py",
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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "c4996250-d041-4256-87a5-ddebaddf6566",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VPBweki7x6w6RZXj5obPQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 806,
      "cache_read_input_tokens": 24821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 806
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

_source line 21 · 2026-05-15T02:01:45.061Z_

<details><summary>↩ Tool result · `toolu_01HiaTjD74nR84tkBQUNqFcq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"M2 statistical analysis: compare hard-negative strategies across encoders and seeds.\\n\\nCollects best R@1 from training logs, runs paired t-tests, Wilcoxon,\\nbootstrap CIs, and Cohen's d.  Outputs JSON + Markdown.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport math\\nimport os\\nimport re\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Dict, List, Optional, Tuple\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\n# ── Configuration ──────────────────────────────────────────────────────\\n\\nENCODERS = [\\\"qwen\\\", \\\"starcoder\\\"]\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSEEDS = [42, 43, 44]\\n\\nCHECKPOINT_BASE = \\\"/root/autodl-tmp/structfuse/checkpoints\\\"\\nOUTPUT_BASE = \\\"/root/autodl-tmp/structfuse/full_m2_outputs\\\"\\n\\n# StarCoder s42 used 3 epochs (others used 2)\\nHETEROGENEITY_NOTES = {\\n    (\\\"starcoder\\\", \\\"random\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"starcoder\\\", \\\"embedding_distance\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"starcoder\\\", \\\"dataflow_aware\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"qwen\\\", \\\"random\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"qwen\\\", \\\"embedding_distance\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"qwen\\\", \\\"dataflow_aware\\\", 42): \\\"3 epochs (others: 2)\\\",\\n}\\n\\n\\ndef _candidate_dirs(encoder: str, strategy: str, seed: int) -> List[str]:\\n    \\\"\\\"\\\"Return candidate directories to search for a run's output.\\\"\\\"\\\"\\n    enc_short = {\\\"qwen\\\": \\\"qwen\\\", \\\"starcoder\\\": \\\"starcoder\\\"}[encoder]\\n    enc_full = {\\\"qwen\\\": \\\"m2_full_qwen\\\", \\\"starcoder\\\": \\\"m2_full_starcoder\\\"}[encoder]\\n    tag = f\\\"{strategy}_s{seed}\\\"\\n    tag_enc = f\\\"{strategy}_{enc_short}_s{seed}\\\"\\n    return [\\n        f\\\"{OUTPUT_BASE}/{tag}\\\",\\n        f\\\"{OUTPUT_BASE}/{tag_enc}\\\",\\n        f\\\"{CHECKPOINT_BASE}/{enc_full}/{tag}\\\",\\n    ]\\n\\n\\ndef _parse_best_r1_from_log(log_path: str) -> Optional[float]:\\n    \\\"\\\"\\\"Extract the last 'New best R@1=X.XXXX' value from a train.log.\\\"\\\"\\\"\\n    best = None\\n    pattern = re.compile(r\\\"New best R@1=([\\\\d.]+)\\\")\\n    with open(log_path) as f:\\n        for line in f:\\n            m = pattern.search(line)\\n            if m:\\n                best = float(m.group(1))\\n    return best\\n\\n\\ndef _parse_eval_metrics_from_log(log_path: str) -> List[Dict[str, float]]:\\n    \\\"\\\"\\\"Parse all [eval@step] lines, return list of metric dicts.\\\"\\\"\\\"\\n    results = []\\n    pattern = re.compile(r\\\"\\\\[eval@(\\\\d+)\\\\]\\\\s*(\\\\{.*\\\\})\\\")\\n    with open(log_path) as f:\\n        for line in f:\\n            m = pattern.search(line)\\n            if m:\\n                step = int(m.group(1))\\n                metrics_str = m.group(2).replace(\\\"'\\\", '\\\"')\\n                try:\\n                    metrics = json.loads(metrics_str)\\n                    metrics[\\\"step\\\"] = step\\n                    results.append(metrics)\\n                except json.JSONDecodeError:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "bb97c1c9-50e2-413e-928d-2b300a34460e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"M2 statistical analysis: compare hard-negative strategies across encoders and seeds.\\\\n\\\\nCollects best R@1 from training logs, runs paired t-tests, Wilcoxon,\\\\nbootstrap CIs, and Cohen's d.  Outputs JSON + Markdown.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport math\\\\nimport os\\\\nimport re\\\\nimport sys\\\\nfrom pathlib import Path\\\\nfrom typing import Dict, List, Optional, Tuple\\\\n\\\\nimport numpy as np\\\\nfrom scipy import stats\\\\n\\\\n# ── Configuration ──────────────────────────────────────────────────────\\\\n\\\\nENCODERS = [\\\\\\\"qwen\\\\\\\", \\\\\\\"starcoder\\\\\\\"]\\\\nSTRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\nSEEDS = [42, 43, 44]\\\\n\\\\nCHECKPOINT_BASE = \\\\\\\"/root/autodl-tmp/structfuse/checkpoints\\\\\\\"\\\\nOUTPUT_BASE = \\\\\\\"/root/autodl-tmp/structfuse/full_m2_outputs\\\\\\\"\\\\n\\\\n# StarCoder s42 used 3 epochs (others used 2)\\\\nHETEROGENEITY_NOTES = {\\\\n    (\\\\\\\"starcoder\\\\\\\", \\\\\\\"random\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n    (\\\\\\\"starcoder\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n    (\\\\\\\"starcoder\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n    (\\\\\\\"qwen\\\\\\\", \\\\\\\"random\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n    (\\\\\\\"qwen\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n    (\\\\\\\"qwen\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\", 42): \\\\\\\"3 epochs (others: 2)\\\\\\\",\\\\n}\\\\n\\\\n\\\\ndef _candidate_dirs(encoder: str, strategy: str, seed: int) -> List[str]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Return candidate directories to search for a run's output.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    enc_short = {\\\\\\\"qwen\\\\\\\": \\\\\\\"qwen\\\\\\\", \\\\\\\"starcoder\\\\\\\": \\\\\\\"starcoder\\\\\\\"}[encoder]\\\\n    enc_full = {\\\\\\\"qwen\\\\\\\": \\\\\\\"m2_full_qwen\\\\\\\", \\\\\\\"starcoder\\\\\\\": \\\\\\\"m2_full_starcoder\\\\\\\"}[encoder]\\\\n    tag = f\\\\\\\"{strategy}_s{seed}\\\\\\\"\\\\n    tag_enc = f\\\\\\\"{strategy}_{enc_short}_s{seed}\\\\\\\"\\\\n    return [\\\\n        f\\\\\\\"{OUTPUT_BASE}/{tag}\\\\\\\",\\\\n        f\\\\\\\"{OUTPUT_BASE}/{tag_enc}\\\\\\\",\\\\n        f\\\\\\\"{CHECKPOINT_BASE}/{enc_full}/{tag}\\\\\\\",\\\\n    ]\\\\n\\\\n\\\\ndef _parse_best_r1_from_log(log_path: str) -> Optional[float]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Extract the last 'New best R@1=X.XXXX' value from a train.log.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    best = None\\\\n    pattern = re.compile(r\\\\\\\"New best R@1=([\\\\\\\\d.]+)\\\\\\\")\\\\n    with open(log_path) as f:\\\\n        for line in f:\\\\n            m = pattern.search(line)\\\\n            if m:\\\\n                best = float(m.group(1))\\\\n    return best\\\\n\\\\n\\\\ndef _parse_eval_metrics_from_log(log_path: str) -> List[Dict[str, float]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Parse all [eval@step] lines, return list of metric dicts.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    results = []\\\\n    pattern = re.compile(r\\\\\\\"\\\\\\\\[eval@(\\\\\\\\d+)\\\\\\\\]\\\\\\\\s*(\\\\\\\\{.*\\\\\\\\})\\\\\\\")\\\\n    with open(log_path) as f:\\\\n        for line in f:\\\\n            m = pattern.search(line)\\\\n            if m:\\\\n                step = int(m.group(1))\\\\n                metrics_str = m.group(2).replace(\\\\\\\"'\\\\\\\", '\\\\\\\"')\\\\n                try:\\\\n                    metrics = json.loads(metrics_str)\\\\n                    metrics[\\\\\\\"step\\\\\\\"] = step\\\\n                    results.append(metrics)\\\\n                except json.JSONDecodeError:\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"M2 statistical analysis: compare hard-negative strategies across encoders and seeds.\\n\\nCollects best R@1 from training logs, runs paired t-tests, Wilcoxon,\\nbootstrap CIs, and Cohen's d.  Outputs JSON + Markdown.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport math\\nimport os\\nimport re\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Dict, List, Optional, Tuple\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\n# ── Configuration ──────────────────────────────────────────────────────\\n\\nENCODERS = [\\\"qwen\\\", \\\"starcoder\\\"]\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSEEDS = [42, 43, 44]\\n\\nCHECKPOINT_BASE = \\\"/root/autodl-tmp/structfuse/checkpoints\\\"\\nOUTPUT_BASE = \\\"/root/autodl-tmp/structfuse/full_m2_outputs\\\"\\n\\n# StarCoder s42 used 3 epochs (others used 2)\\nHETEROGENEITY_NOTES = {\\n    (\\\"starcoder\\\", \\\"random\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"starcoder\\\", \\\"embedding_distance\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"starcoder\\\", \\\"dataflow_aware\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"qwen\\\", \\\"random\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"qwen\\\", \\\"embedding_distance\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"qwen\\\", \\\"dataflow_aware\\\", 42): \\\"3 epochs (others: 2)\\\",\\n}\\n\\n\\ndef _candidate_dirs(encoder: str, strategy: str, seed: int) -> List[str]:\\n    \\\"\\\"\\\"Return candidate directories to search for a run's output.\\\"\\\"\\\"\\n    enc_short = {\\\"qwen\\\": \\\"qwen\\\", \\\"starcoder\\\": \\\"starcoder\\\"}[encoder]\\n    enc_full = {\\\"qwen\\\": \\\"m2_full_qwen\\\", \\\"starcoder\\\": \\\"m2_full_starcoder\\\"}[encoder]\\n    tag = f\\\"{strategy}_s{seed}\\\"\\n    tag_enc = f\\\"{strategy}_{enc_short}_s{seed}\\\"\\n    return [\\n        f\\\"{OUTPUT_BASE}/{tag}\\\",\\n        f\\\"{OUTPUT_BASE}/{tag_enc}\\\",\\n        f\\\"{CHECKPOINT_BASE}/{enc_full}/{tag}\\\",\\n    ]\\n\\n\\ndef _parse_best_r1_from_log(log_path: str) -> Optional[float]:\\n    \\\"\\\"\\\"Extract the last 'New best R@1=X.XXXX' value from a train.log.\\\"\\\"\\\"\\n    best = None\\n    pattern = re.compile(r\\\"New best R@1=([\\\\d.]+)\\\")\\n    with open(log_path) as f:\\n        for line in f:\\n            m = pattern.search(line)\\n            if m:\\n                best = float(m.group(1))\\n    return best\\n\\n\\ndef _parse_eval_metrics_from_log(log_path: str) -> List[Dict[str, float]]:\\n    \\\"\\\"\\\"Parse all [eval@step] lines, return list of metric dicts.\\\"\\\"\\\"\\n    results = []\\n    pattern = re.compile(r\\\"\\\\[eval@(\\\\d+)\\\\]\\\\s*(\\\\{.*\\\\})\\\")\\n    with open(log_path) as f:\\n        for line in f:\\n            m = pattern.search(line)\\n            if m:\\n                step = int(m.group(1))\\n                metrics_str = m.group(2).replace(\\\"'\\\", '\\\"')\\n                try:\\n                    metrics = json.loads(metrics_str)\\n                    metrics[\\\"step\\\"] = step\\n                    results.append(metrics)\\n                except json.JSONDecodeError:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a good picture of the existing code style and project conventions. Now let me also check the rest of the statistical analysis script to understand the data format better, particularly how results are structured.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "49e2cc7a-aa66-40ac-9c5b-dda4c36a7474",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxRTdfdNeTyYXbPbJgKvX9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4801,
      "cache_read_input_tokens": 25627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4801
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

看到了项目的风格和数据结构。现在编写脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "5b941a6d-e040-438e-ad76-522728a56093",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxRTdfdNeTyYXbPbJgKvX9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4801,
      "cache_read_input_tokens": 25627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4801
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E8mVsvw4653QTRTeDhFdL8`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -30 /root/structfuse/scripts/m2_statistical_analysis.py",
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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "4076b6fb-b8bf-4e7d-95ce-52f817f0a6ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxRTdfdNeTyYXbPbJgKvX9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4801,
      "cache_read_input_tokens": 25627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4801
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

_source line 25 · 2026-05-15T02:01:51.426Z_

<details><summary>↩ Tool result · `toolu_01E8mVsvw4653QTRTeDhFdL8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"M2 statistical analysis: compare hard-negative strategies across encoders and seeds.\\n\\nCollects best R@1 from training logs, runs paired t-tests, Wilcoxon,\\nbootstrap CIs, and Cohen's d.  Outputs JSON + Markdown.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport math\\nimport os\\nimport re\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Dict, List, Optional, Tuple\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\n# ── Configuration ──────────────────────────────────────────────────────\\n\\nENCODERS = [\\\"qwen\\\", \\\"starcoder\\\"]\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSEEDS = [42, 43, 44]\\n\\nCHECKPOINT_BASE = \\\"/root/autodl-tmp/structfuse/checkpoints\\\"\\nOUTPUT_BASE = \\\"/root/autodl-tmp/structfuse/full_m2_outputs\\\"\\n\\n# StarCoder s42 used 3 epochs (others used 2)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "aad95547-3ec1-46ff-be51-c74dc428876f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"M2 statistical analysis: compare hard-negative strategies across encoders and seeds.\\\\n\\\\nCollects best R@1 from training logs, runs paired t-tests, Wilcoxon,\\\\nbootstrap CIs, and Cohen's d.  Outputs JSON + Markdown.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport math\\\\nimport os\\\\nimport re\\\\nimport sys\\\\nfrom pathlib import Path\\\\nfrom typing import Dict, List, Optional, Tuple\\\\n\\\\nimport numpy as np\\\\nfrom scipy import stats\\\\n\\\\n# ── Configuration ──────────────────────────────────────────────────────\\\\n\\\\nENCODERS = [\\\\\\\"qwen\\\\\\\", \\\\\\\"starcoder\\\\\\\"]\\\\nSTRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\nSEEDS = [42, 43, 44]\\\\n\\\\nCHECKPOINT_BASE = \\\\\\\"/root/autodl-tmp/structfuse/checkpoints\\\\\\\"\\\\nOUTPUT_BASE = \\\\\\\"/root/autodl-tmp/structfuse/full_m2_outputs\\\\\\\"\\\\n\\\\n# StarCoder s42 used 3 epochs (others used 2)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"M2 statistical analysis: compare hard-negative strategies across encoders and seeds.\\n\\nCollects best R@1 from training logs, runs paired t-tests, Wilcoxon,\\nbootstrap CIs, and Cohen's d.  Outputs JSON + Markdown.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport math\\nimport os\\nimport re\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Dict, List, Optional, Tuple\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\n# ── Configuration ──────────────────────────────────────────────────────\\n\\nENCODERS = [\\\"qwen\\\", \\\"starcoder\\\"]\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSEEDS = [42, 43, 44]\\n\\nCHECKPOINT_BASE = \\\"/root/autodl-tmp/structfuse/checkpoints\\\"\\nOUTPUT_BASE = \\\"/root/autodl-tmp/structfuse/full_m2_outputs\\\"\\n\\n# StarCoder s42 used 3 epochs (others used 2)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the visualization script. Key observations:

1. The project uses `ENCODERS = ["qwen", "starcoder"]`, `STRATEGIES = ["random", "embedding_distance", "dataflow_aware"]`, `SEEDS = [42, 43, 44]`
2. The existing plot script uses Nature-style rcParams with DejaVu Sans, 300 DPI, no top/right spines
3. Results are stored in `/root/autodl-tmp/structfuse/full_m2_outputs/` with naming like `{strategy}_s{seed}/` or `{strategy}_{encoder}_s{seed}/`


4. I also need to include the `bm25` strategy alongside the existing three, and the training logs use `[eval@step]` lines with metric dicts plus `New best R@1=X.XXXX` lines for tracking performance
5. The visualization needs three figures: a grouped bar chart showing per-seed results, a pairwise delta comparison, and training dynamics with dual axes, all controlled via `--results-dir`, `--mock`, and `--output-dir` arguments

I'll need to parse the training logs carefully to extract the evaluation metrics and best performance values.

Writing the visualization script...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "6e11b2b7-6bf9-462a-9da6-0c20dc360855",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DGZGXapnHzuqDXAYouuMM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 30428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 723
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01M3udiTUYTyxpryYXguk9An`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat > /root/structfuse/scripts/plot_per_seed_delta.py << 'PYEOF'\n\"\"\"Per-seed delta visualization for M2 hard-negative strategy comparison.\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Dict, List, Optional, Tuple\n\nimport numpy as np\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nfrom matplotlib.ticker import MaxNLocator\n\n# ── Style ──────────────────────────────────────────────────────────────\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 10,\n    'axes.titlesize': 11,\n    'axes.labelsize': 10,\n    'xtick.labelsize': 9,\n    'ytick.labelsize': 9,\n    'legend.fontsize': 9,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'lines.linewidth': 1.8,\n})\n\n# ── Constants ──────────────────────────────────────────────────────────\n\nENCODERS = ['qwen', 'starcoder']\nENC_LABELS = {'qwen': 'Qwen2.5-Coder-3B', 'starcoder': 'StarCoder2-3B'}\nSTRATEGIES = ['random', 'embedding_distance', 'dataflow_aware', 'bm25']\nSTRAT_LABELS = {'random': 'Random', 'embedding_distance': 'Embedding',\n                'dataflow_aware': 'Dataflow', 'bm25': 'BM25'}\nSEEDS = [42, 43, 44]\n\nPALETTE = {\n    'random': '#56B4E9',\n    'embedding_distance': '#E69F00',\n    'dataflow_aware': '#009E73',\n    'bm25': '#CC79A7',\n}\nSEED_HATCHES = {42: '', 43: '///', 44: '\\\\\\\\\\\\'}\nSEED_MARKERS = {42: 'o', 43: 's', 44: '^'}\n\nOUTPUT_BASE = '/root/autodl-tmp/structfuse/full_m2_outputs'\n\n# ── Data loading ───────────────────────────────────────────────────────\n\ndef _candidate_dirs(encoder: str, strategy: str, seed: int) -> List[str]:\n    enc_full = {'qwen': 'm2_full_qwen', 'starcoder': 'm2_full_starcoder'}[encoder]\n    tag = f'{strategy}_s{seed}'\n    tag_enc = f'{strategy}_{encoder}_s{seed}'\n    return [\n        f'{OUTPUT_BASE}/{tag}',\n        f'{OUTPUT_BASE}/{tag_enc}',\n        f'/root/autodl-tmp/structfuse/checkpoints/{enc_full}/{tag}',\n    ]\n\n\ndef _find_log(encoder: str, strategy: str, seed: int, results_dir: Optional[str] = None) -> Optional[str]:\n    if results_dir:\n        candidates = [\n            os.path.join(results_dir, f'{strategy}_{encoder}_s{seed}', 'train.log'),\n            os.path.join(results_dir, f'{strategy}_s{seed}', 'train.log'),\n            os.path.join(results_dir, encoder, f'{strategy}_s{seed}', 'train.log'),\n        ]\n    else:\n        candidates = [os.path.join(d, 'train.log') for d in _candidate_dirs(encoder, strategy, seed)]\n    for c in candidates:\n        if os.path.isfile(c):\n            return c\n    return None\n\n\ndef _parse_best_r1(log_path: str) -> Optional[float]:\n    best = None\n    pat = re.compile(r'New best R@1=([\\d.]+)')\n    with open(log_path) as f:\n        for line in f:\n            m = pat.search(line)\n            if m:\n                best = float(m.group(1))\n    return best\n\n\ndef _parse_eval_curve(log_path: str) -> List[dict]:\n    results = []\n    pat = re.compile(r'\\[eval@(\\d+)\\]\\s*(\\{.*\\})')\n    with open(log_path) as f:\n        for line in f:\n            m = pat.search(line)\n            if m:\n                step = int(m.group(1))\n                try:\n                    metrics = json.loads(m.group(2).replace(\"'\", '\"'))\n                    metrics['step'] = step\n                    results.append(metrics)\n                except json.JSONDecodeError:\n                    pass\n    return results\n\n\ndef load_real_data(results_dir: Optional[str]) -> Tuple[dict, dict]:\n    best_r1: Dict[str, Dict[str, Dict[int, float]]] = {}\n    curves: Dict[str, Dict[str, Dict[int, List[dict]]]] = {}\n    for enc in ENCODERS:\n        best_r1[enc] = {}\n        curves[enc] = {}\n        for strat in STRATEGIES:\n            best_r1[enc][strat] = {}\n            curves[enc][strat] = {}\n            for seed in SEEDS:\n                log = _find_log(enc, strat, seed, results_dir)\n                if log:\n                    r1 = _parse_best_r1(log)\n                    if r1 is not None:\n                        best_r1[enc][strat][seed] = r1\n                    curves[enc][strat][seed] = _parse_eval_curve(log)\n    return best_r1, curves\n\n\n# ── Mock data ──────────────────────────────────────────────────────────\n\ndef generate_mock_data() -> Tuple[dict, dict]:\n    rng = np.random.RandomState(2026)\n    base = {\n        'qwen': {'random': 0.42, 'embedding_distance': 0.48, 'dataflow_aware': 0.51, 'bm25': 0.46},\n        'starcoder': {'random': 0.38, 'embedding_distance': 0.43, 'dataflow_aware': 0.47, 'bm25': 0.41},\n    }\n    best_r1: dict = {}\n    curves: dict = {}\n    for enc in ENCODERS:\n        best_r1[enc] = {}\n        curves[enc] = {}\n        for strat in STRATEGIES:\n            best_r1[enc][strat] = {}\n            curves[enc][strat] = {}\n            mu = base[enc][strat]\n            for seed in SEEDS:\n                val = mu + rng.normal(0, 0.015)\n                best_r1[enc][strat][seed] = round(val, 4)\n                n_steps = 20\n                steps = list(range(50, 50 * (n_steps + 1), 50))\n                r1_curve = []\n                loss_curve = []\n                for i, s in enumerate(steps):\n                    frac = (i + 1) / n_steps\n                    r1_val = mu * (1 - np.exp(-3 * frac)) + rng.normal(0, 0.01)\n                    loss_val = 0.8 * np.exp(-2.5 * frac) + 0.15 + rng.normal(0, 0.01)\n                    r1_curve.append({'step': s, 'r1': round(max(0, r1_val), 4),\n                                     'val_loss': round(max(0.05, loss_val), 4)})\n                best_step = steps[int(n_steps * 0.75) + rng.randint(-2, 3)]\n                for entry in r1_curve:\n                    entry['is_best'] = entry['step'] == best_step\n                curves[enc][strat][seed] = r1_curve\n    return best_r1, curves\n\n# ── Figure A: Per-Seed Strategy Comparison ─────────────────────────────\n\ndef plot_figure_a(best_r1: dict, output_dir: str):\n    strategies = [s for s in STRATEGIES if any(\n        best_r1.get(e, {}).get(s, {}) for e in ENCODERS)]\n    if not strategies:\n        print('Figure A: no data, skipping')\n        return\n\n    fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.5), sharey=True)\n    n_strat = len(strategies)\n    n_seeds = len(SEEDS)\n    bar_w = 0.22\n    seed_colors = ['#0072B2', '#D55E00', '#56B4E9']\n\n    for ax_idx, enc in enumerate(ENCODERS):\n        ax = axes[ax_idx]\n        x = np.arange(n_strat)\n        for si, seed in enumerate(SEEDS):\n            vals = [best_r1.get(enc, {}).get(s, {}).get(seed, 0) for s in strategies]\n            offset = (si - (n_seeds - 1) / 2) * bar_w\n            ax.bar(x + offset, vals, bar_w * 0.9, color=seed_colors[si],\n                   alpha=0.85, label=f's{seed}', zorder=2, edgecolor='white', linewidth=0.5)\n\n        # mean + std annotation\n        for j, s in enumerate(strategies):\n            seed_vals = [best_r1.get(enc, {}).get(s, {}).get(sd, np.nan) for sd in SEEDS]\n            seed_vals = [v for v in seed_vals if not np.isnan(v)]\n            if seed_vals:\n                mu = np.mean(seed_vals)\n                std = np.std(seed_vals, ddof=1) if len(seed_vals) > 1 else 0\n                y_top = max(seed_vals) + 0.008\n                ax.text(j, y_top, f'{mu:.3f}±{std:.3f}', ha='center', va='bottom',\n                        fontsize=7.5, fontweight='bold', color='#333333')\n\n        ax.set_xticks(x)\n        ax.set_xticklabels([STRAT_LABELS.get(s, s) for s in strategies])\n        ax.set_title(ENC_LABELS[enc])\n        if ax_idx == 0:\n            ax.set_ylabel('R@1')\n            ax.legend(loc='lower right', framealpha=0.9, ncol=3)\n\n    fig.suptitle('Per-Seed Strategy Comparison', fontsize=12, y=1.02)\n    plt.tight_layout()\n    for fmt in ['pdf', 'png']:\n        fig.savefig(os.path.join(output_dir, f'fig_a_per_seed_comparison.{fmt}'))\n    plt.close()\n    print('Figure A saved: fig_a_per_seed_comparison')\n\n\n# ── Figure B: Pairwise Delta Plot ──────────────────────────────────────\n\ndef plot_figure_b(best_r1: dict, output_dir: str):\n    pairs = [\n        ('embedding_distance', 'random', 'Embedding − Random'),\n        ('dataflow_aware', 'random', 'Dataflow − Random'),\n        ('dataflow_aware', 'embedding_distance', 'Dataflow − Embedding'),\n    ]\n    active_pairs = []\n    for sa, sb, label in pairs:\n        if any(best_r1.get(e, {}).get(sa, {}) and best_r1.get(e, {}).get(sb, {})\n               for e in ENCODERS):\n            active_pairs.append((sa, sb, label))\n    if not active_pairs:\n        print('Figure B: no data, skipping')\n        return\n\n    fig, axes = plt.subplots(len(active_pairs), 2, figsize=(7.0, 2.2 * len(active_pairs)),\n                              squeeze=False, sharex='col')\n\n    for row, (sa, sb, pair_label) in enumerate(active_pairs):\n        for col, enc in enumerate(ENCODERS):\n            ax = axes[row, col]\n            deltas = []\n            xs = []\n            for si, seed in enumerate(SEEDS):\n                va = best_r1.get(enc, {}).get(sa, {}).get(seed)\n                vb = best_r1.get(enc, {}).get(sb, {}).get(seed)\n                if va is not None and vb is not None:\n                    d = va - vb\n                    deltas.append(d)\n                    xs.append(si)\n                    ax.plot(si, d, marker=SEED_MARKERS[seed], color=PALETTE[sa],\n                            markersize=8, zorder=3)\n\n            if len(xs) > 1:\n                ax.plot(xs, deltas, color=PALETTE[sa], linewidth=1.2, alpha=0.6, zorder=2)\n\n            ax.axhline(0, color='gray', linewidth=0.8, linestyle='--', zorder=1)\n\n            # consistency check\n            if deltas and all(d > 0 for d in deltas):\n                ax.text(0.97, 0.92, '✓', transform=ax.transAxes, fontsize=14,\n                        color='#009E73', fontweight='bold', ha='right', va='top')\n            elif deltas and all(d < 0 for d in deltas):\n                ax.text(0.97, 0.92, '✗', transform=ax.transAxes, fontsize=14,\n                        color='#D55E00', fontweight='bold', ha='right', va='top')\n\n            ax.set_xticks(range(len(SEEDS)))\n            ax.set_xticklabels([f's{s}' for s in SEEDS])\n            if col == 0:\n                ax.set_ylabel(f'Δ R@1\\n({pair_label})', fontsize=8)\n            if row == 0:\n                ax.set_title(ENC_LABELS[enc])\n\n    fig.suptitle('Pairwise Per-Seed Delta', fontsize=12, y=1.02)\n    plt.tight_layout()\n    for fmt in ['pdf', 'png']:\n        fig.savefig(os.path.join(output_dir, f'fig_b_pairwise_delta.{fmt}'))\n    plt.close()\n    print('Figure B saved: fig_b_pairwise_delta')\n\n\n# ── Figure C: Training Dynamics ────────────────────────────────────────\n\ndef plot_figure_c(curves: dict, output_dir: str):\n    active_strats = [s for s in STRATEGIES if any(\n        curves.get(e, {}).get(s, {}) for e in ENCODERS)]\n    if not active_strats:\n        print('Figure C: no data, skipping')\n        return\n\n    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.5))\n\n    for ax_idx, enc in enumerate(ENCODERS):\n        ax_r1 = axes[ax_idx]\n        ax_loss = ax_r1.twinx()\n\n        for strat in active_strats:\n            seed_curves = curves.get(enc, {}).get(strat, {})\n            if not seed_curves:\n                continue\n\n            # align steps across seeds\n            all_steps = sorted(set(\n                entry['step'] for sc in seed_curves.values() for entry in sc))\n            r1_by_step = {s: [] for s in all_steps}\n            loss_by_step = {s: [] for s in all_steps}\n            best_steps = []\n\n            for seed, entries in seed_curves.items():\n                step_map = {e['step']: e for e in entries}\n                for s in all_steps:\n                    if s in step_map:\n                        e = step_map[s]\n                        r1_by_step[s].append(e.get('r1', e.get('R@1', np.nan)))\n                        loss_by_step[s].append(e.get('val_loss', np.nan))\n                        if e.get('is_best', False):\n                            best_steps.append(s)\n\n            steps_arr = np.array(all_steps)\n            r1_mean = np.array([np.nanmean(r1_by_step[s]) for s in all_steps])\n            r1_std = np.array([np.nanstd(r1_by_step[s]) for s in all_steps])\n            loss_mean = np.array([np.nanmean(loss_by_step[s]) for s in all_steps])\n            loss_std = np.array([np.nanstd(loss_by_step[s]) for s in all_steps])\n\n            color = PALETTE[strat]\n            label = STRAT_LABELS.get(strat, strat)\n\n            ax_r1.plot(steps_arr, r1_mean, color=color, label=label, zorder=3)\n            ax_r1.fill_between(steps_arr, r1_mean - r1_std, r1_mean + r1_std,\n                               color=color, alpha=0.15, zorder=2)\n\n            ax_loss.plot(steps_arr, loss_mean, color=color, linestyle='--',\n                         alpha=0.6, linewidth=1.2, zorder=2)\n\n            # mark early stopping\n            if best_steps:\n                avg_best = int(np.mean(best_steps))\n                idx = np.argmin(np.abs(steps_arr - avg_best))\n                ax_r1.axvline(steps_arr[idx], color=color, linewidth=0.8,\n                              linestyle=':', alpha=0.5)\n                ax_r1.plot(steps_arr[idx], r1_mean[idx], marker='*',\n                           color=color, markersize=10, zorder=4)\n\n        ax_r1.set_xlabel('Eval Step')\n        ax_r1.set_ylabel('R@1 (solid)')\n        ax_r1.set_title(ENC_LABELS[enc])\n        ax_r1.xaxis.set_major_locator(MaxNLocator(integer=True))\n\n        if ax_idx == 0:\n            ax_r1.legend(loc='lower right', framealpha=0.9)\n\n        ax_loss.set_ylabel('Val Loss (dashed)', alpha=0.6)\n        ax_loss.spines['right'].set_visible(True)\n        ax_loss.tick_params(axis='y', colors='gray')\n\n    fig.suptitle('Training Dynamics (mean ± std across seeds)', fontsize=12, y=1.02)\n    plt.tight_layout()\n    for fmt in ['pdf', 'png']:\n        fig.savefig(os.path.join(output_dir, f'fig_c_training_dynamics.{fmt}'))\n    plt.close()\n    print('Figure C saved: fig_c_training_dynamics')\n\n\n# ── Main ───────────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser(description='Per-seed delta visualization for M2')\n    parser.add_argument('--results-dir', type=str, default=None,\n                        help='M2 results directory (overrides default paths)')\n    parser.add_argument('--mock', action='store_true',\n                        help='Generate mock data for validation')\n    parser.add_argument('--output-dir', type=str,\n                        default='/root/autodl-tmp/structfuse/artifacts/figures/',\n                        help='Output directory for figures')\n    args = parser.parse_args()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    if args.mock:\n        print('Using mock data')\n        best_r1, curves = generate_mock_data()\n    else:\n        best_r1, curves = load_real_data(args.results_dir)\n        n_found = sum(1 for e in ENCODERS for s in STRATEGIES\n                      for sd in SEEDS if best_r1.get(e, {}).get(s, {}).get(sd) is not None)\n        total = len(ENCODERS) * len(STRATEGIES) * len(SEEDS)\n        print(f'Loaded {n_found}/{total} runs')\n\n    plot_figure_a(best_r1, args.output_dir)\n    plot_figure_b(best_r1, args.output_dir)\n    plot_figure_c(curves, args.output_dir)\n\n    print(f'\\nAll figures saved to: {args.output_dir}')\n\n\nif __name__ == '__main__':\n    main()\nPYEOF\necho \"DONE: $?\"",
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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "f7ed0deb-ce84-4bd6-a2d5-dfceb0ecf640",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DGZGXapnHzuqDXAYouuMM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 30428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 723
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T02:03:09.386Z_

<details><summary>↩ Tool result · `toolu_01M3udiTUYTyxpryYXguk9An`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE: 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "0541f286-40fc-41a3-9a64-32133abdfd51",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"DONE: 0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"DONE: 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

脚本已写入，用 mock 数据验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "54d96c6f-f4c8-42e7-a9b4-6876a0696777",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvEkq9bmWVxmuF4u71TUEj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5942,
      "cache_read_input_tokens": 31151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5942
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

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_018XupHdWJirLtbma8LLCATc`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cd /root/structfuse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python scripts/plot_per_seed_delta.py --mock --output-dir /tmp/test_figures/ 2>&1 | tail -20",
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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "ddd24b49-4ae4-4802-ba1b-facbae17cb1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvEkq9bmWVxmuF4u71TUEj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5942,
      "cache_read_input_tokens": 31151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5942
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

_source line 31 · 2026-05-15T02:03:17.369Z_

<details><summary>↩ Tool result · `toolu_018XupHdWJirLtbma8LLCATc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Using mock data\\nFigure A saved: fig_a_per_seed_comparison\\nFigure B saved: fig_b_pairwise_delta\\nFigure C saved: fig_c_training_dynamics\\n\\nAll figures saved to: /tmp/test_figures/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.59}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "8e514619-d15f-4e28-8f28-04d00f222f48",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Using mock data\\\\nFigure A saved: fig_a_per_seed_comparison\\\\nFigure B saved: fig_b_pairwise_delta\\\\nFigure C saved: fig_c_training_dynamics\\\\n\\\\nAll figures saved to: /tmp/test_figures/\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.59}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Using mock data\\nFigure A saved: fig_a_per_seed_comparison\\nFigure B saved: fig_b_pairwise_delta\\nFigure C saved: fig_c_training_dynamics\\n\\nAll figures saved to: /tmp/test_figures/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.59}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AyuyhG11H4M2RFFygwyKLn`</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /tmp/test_figures/",
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
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "2c28eb1b-b191-41e7-8df0-86eeab083a8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131C7f4b1c7zW9EowweXhX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 325,
      "cache_read_input_tokens": 37093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 325
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T02:03:21.666Z_

<details><summary>↩ Tool result · `toolu_01AyuyhG11H4M2RFFygwyKLn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 940\\ndrwxr-xr-x 2 root root   4096 May 15 10:03 .\\ndrwxrwxrwt 1 root root 172032 May 15 10:03 ..\\n-rw-r--r-- 1 root root  21793 May 15 10:03 fig_a_per_seed_comparison.pdf\\n-rw-r--r-- 1 root root 120629 May 15 10:03 fig_a_per_seed_comparison.png\\n-rw-r--r-- 1 root root  21096 May 15 10:03 fig_b_pairwise_delta.pdf\\n-rw-r--r-- 1 root root 266774 May 15 10:03 fig_b_pairwise_delta.png\\n-rw-r--r-- 1 root root  25523 May 15 10:03 fig_c_training_dynamics.pdf\\n-rw-r--r-- 1 root root 454928 May 15 10:03 fig_c_training_dynamics.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "d5b5f14c-0f29-4823-9523-6779520cae2c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 940\\\\ndrwxr-xr-x 2 root root   4096 May 15 10:03 .\\\\ndrwxrwxrwt 1 root root 172032 May 15 10:03 ..\\\\n-rw-r--r-- 1 root root  21793 May 15 10:03 fig_a_per_seed_comparison.pdf\\\\n-rw-r--r-- 1 root root 120629 May 15 10:03 fig_a_per_seed_comparison.png\\\\n-rw-r--r-- 1 root root  21096 May 15 10:03 fig_b_pairwise_delta.pdf\\\\n-rw-r--r-- 1 root root 266774 May 15 10:03 fig_b_pairwise_delta.png\\\\n-rw-r--r-- 1 root root  25523 May 15 10:03 fig_c_training_dynamics.pdf\\\\n-rw-r--r-- 1 root root 454928 May 15 10:03 fig_c_training_dynamics.png\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 940\\ndrwxr-xr-x 2 root root   4096 May 15 10:03 .\\ndrwxrwxrwt 1 root root 172032 May 15 10:03 ..\\n-rw-r--r-- 1 root root  21793 May 15 10:03 fig_a_per_seed_comparison.pdf\\n-rw-r--r-- 1 root root 120629 May 15 10:03 fig_a_per_seed_comparison.png\\n-rw-r--r-- 1 root root  21096 May 15 10:03 fig_b_pairwise_delta.pdf\\n-rw-r--r-- 1 root root 266774 May 15 10:03 fig_b_pairwise_delta.png\\n-rw-r--r-- 1 root root  25523 May 15 10:03 fig_c_training_dynamics.pdf\\n-rw-r--r-- 1 root root 454928 May 15 10:03 fig_c_training_dynamics.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

6 个文件全部生成（3 figure × PDF + PNG）：

| 图表 | PDF | PNG |
|------|-----|-----|
| Fig A: Per-Seed Strategy Comparison | 21 KB | 120 KB |
| Fig B: Pairwise Delta Plot | 21 KB | 266 KB |
| Fig C: Training Dynamics | 25 KB | 454 KB |

脚本位于 `/root/structfuse/scripts/plot_per_seed_delta.py`。M2 完成后用 `--results-dir` 替换 `--mock` 即可生成真实图表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "uuid": "1eeddc0b-32d6-4ea8-a4ba-625943c5161e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7mo9iT85xkiZswLgqTWs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 37418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 472
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

_source line 35_

6 个文件全部生成（3 figure × PDF + PNG）：

| 图表 | PDF | PNG |
|------|-----|-----|
| Fig A: Per-Seed Strategy Comparison | 21 KB | 120 KB |
| Fig B: Pairwise Delta Plot | 21 KB | 266 KB |
| Fig C: Training Dynamics | 25 KB | 454 KB |

脚本位于 `/root/structfuse/scripts/plot_per_seed_delta.py`。M2 完成后用 `--results-dir` 替换 `--mock` 即可生成真实图表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 122240,
  "duration_api_ms": 120249,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "55dc8320-1c80-439f-a75e-ec7292722d17",
  "total_cost_usd": 0.47692425000000005,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 26443,
    "cache_read_input_tokens": 245781,
    "output_tokens": 7488,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26443,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 164,
        "cache_read_input_tokens": 37418,
        "cache_creation_input_tokens": 472,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 472
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1425,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001505,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 7488,
      "cacheReadInputTokens": 245781,
      "cacheCreationInputTokens": 26443,
      "webSearchRequests": 0,
      "costUSD": 0.47541925000000007,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6d8e5fb2-57f4-46c5-a236-319a93e248b6"
}
```

</details>

---
