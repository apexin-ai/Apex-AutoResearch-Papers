# ssh harvest all results v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 111
- **Recorded user turns:** 0
- **Tool calls:** 44
- **Original source:** `logs/workers/worker_ssh_harvest-all-results-v2_20260520T035237.log`
- **Structured JSON:** [`d094b6e86ac8f9fe10f5.json`](../../sessions/d0/d094b6e86ac8f9fe10f5.json)

## Before a recorded user message

111 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "d50f2279-c64f-4345-9512-b85630dda76b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779259200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "fae85be6-c034-4fb7-8540-17c941f05bb5",
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to SSH into 4 servers and collect experiment results. Let me load the necessary tools first, then execute the commands in parallel across all 4 servers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "894d2880-7e86-4364-93c0-4e007fd866a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTqyynAeZCh8d38GvnnDFu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11647,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11647
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017qpyEkHPpcxWrktVQQUJuq`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "daa965bb-0c67-48fc-ac70-22066f8b6f5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTqyynAeZCh8d38GvnnDFu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11647,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11647
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

_source line 6 · 2026-05-20T03:52:48.541Z_

<details><summary>↩ Tool result · `toolu_017qpyEkHPpcxWrktVQQUJuq`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "c60cc5f9-5e6f-4b62-b113-f5f8b83228cc",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me execute the commands in parallel across all 4 servers, and also read the registry to know what's already registered.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "457f5af7-4a13-417d-8f6b-c380d91d5587",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011K5pu9sVCdhpgJgpTqGfUX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 23488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 825
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

并行查询 4 台服务器和 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "edd9e908-60b2-40f3-8b66-2b5bb0e8438c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011K5pu9sVCdhpgJgpTqGfUX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 23488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 825
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QHgSaKebuw1vsYZ4e916Fw`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_*.json\" -mmin -2880 -exec ls -lt {} +",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "f94f3424-8428-419b-8f3f-f3a6bc09a24f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011K5pu9sVCdhpgJgpTqGfUX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 23488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 825
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

_source line 10 · 2026-05-20T03:52:57.218Z_

<details><summary>↩ Tool result · `toolu_01QHgSaKebuw1vsYZ4e916Fw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 209119 May 20 11:05 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json\\n-rw-r--r-- 1 root root 200782 May 20 10:36 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json\\n-rw-r--r-- 1 root root 202822 May 20 10:33 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json\\n-rw-r--r-- 1 root root 203594 May 20 10:30 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json\\n-rw-r--r-- 1 root root 206022 May 20 10:29 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json\\n-rw-r--r-- 1 root root 199524 May 20 10:24 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json\\n-rw-r--r-- 1 root root   1783 May 20 07:57 /root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json\\n-rw-r--r-- 1 root root   1320 May 20 07:54 /root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed46.json\\n-rw-r--r-- 1 root root   1319 May 20 07:13 /root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed45_r2.json\\n-rw-r--r-- 1 root root   1319 May 20 07:10 /root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed44_r2.json\\n-rw-r--r-- 1 root root   1783 May 20 05:19 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json\\n-rw-r--r-- 1 root root   1782 May 20 05:18 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json\\n-rw-r--r-- 1 root root   1783 May 20 05:15 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json\\n-rw-r--r-- 1 root root   1485 May 20 05:14 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\\n-rw-r--r-- 1 root root   1486 May 20 03:14 /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed44_r2.json\\n-rw-r--r-- 1 root root   1313 May 20 02:55 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45.json\\n-rw-r--r-- 1 root root   1697 May 20 02:50 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json\\n-rw-r--r-- 1 root root   1314 May 20 02:20 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r2.json\\n-rw-r--r-- 1 root root   1494 May 20 00:03 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed43.json\\n-rw-r--r-- 1 root root   1697 May 19 23:49 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.json\\n-rw-r--r-- 1 root root   1698 May 19 23:45 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed44.json\\n-rw-r--r-- 1 root root   1693 May 19 23:25 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n-rw-r--r-- 1 root root   1698 May 19 22:03 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n-rw-r--r-- 1 root root   1487 May 19 21:24 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\n-rw-r--r-- 1 root root   1486 May 19 20:21 /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed42.json\\n-rw-r--r-- 1 root root   1490 May 19 19:09 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed47.json\\n-rw-r--r-- 1 root root   1697 May 19 18:55 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed42.json\\n-rw-r--r-- 1 root root   1487 May 19 17:26 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed47.json\\n-rw-r--r-- 1 root root   1488 May 19 16:40 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed47.json\\n-rw-r--r-- 1 root root   1493 May 19 16:29 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed45.json\\n-rw-r--r-- 1 root root   1490 May 19 16:08 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\n-rw-r--r-- 1 root root   1488 May 19 16:04 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed46.json\\n-rw-r--r-- 1 root root   1490 May 19 12:57 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45_r2.json\\n-rw-r--r-- 1 root root   1490 May 19 12:20 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45_r2.json\\n-rw-r--r-- 1 root root   1490 May 19 08:38 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed45.json\\n-rw-r--r-- 1 root root   1490 May 19 04:49 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed44.json\\n-rw-r--r-- 1 root root   1494 May 19 02:00 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed44.json\\n-rw-r--r-- 1 root root   1494 May 18 23:45 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed43.json\\n-rw-r--r-- 1 root root   1490 May 18 23:16 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed42.json\\n-rw-r--r-- 1 root root   1488 May 18 23:12 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed42.json\\n-rw-r--r-- 1 root root   1488 May 18 22:34 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed48.json\\n-rw-r--r-- 1 root root   1490 May 18 20:28 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed43.json\\n-rw-r--r-- 1 root root   1488 May 18 12:34 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.99}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "9d470c78-1324-44e5-8dae-f0844d123b9d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 209119 May 20 11:05 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json\\\\n-rw-r--r-- 1 root root 200782 May 20 10:36 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json\\\\n-rw-r--r-- 1 root root 202822 May 20 10:33 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json\\\\n-rw-r--r-- 1 root root 203594 May 20 10:30 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json\\\\n-rw-r--r-- 1 root root 206022 May 20 10:29 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json\\\\n-rw-r--r-- 1 root root 199524 May 20 10:24 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json\\\\n-rw-r--r-- 1 root root   1783 May 20 07:57 /root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json\\\\n-rw-r--r-- 1 root root   1320 May 20 07:54 /root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed46.json\\\\n-rw-r--r-- 1 root root   1319 May 20 07:13 /root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed45_r2.json\\\\n-rw-r--r-- 1 root root   1319 May 20 07:10 /root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed44_r2.json\\\\n-rw-r--r-- 1 root root   1783 May 20 05:19 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json\\\\n-rw-r--r-- 1 root root   1782 May 20 05:18 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json\\\\n-rw-r--r-- 1 root root   1783 May 20 05:15 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json\\\\n-rw-r--r-- 1 root root   1485 May 20 05:14 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\\\\n-rw-r--r-- 1 root root   1486 May 20 03:14 /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed44_r2.json\\\\n-rw-r--r-- 1 root root   1313 May 20 02:55 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45.json\\\\n-rw-r--r-- 1 root root   1697 May 20 02:50 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json\\\\n-rw-r--r-- 1 root root   1314 May 20 02:20 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r2.json\\\\n-rw-r--r-- 1 root root   1494 May 20 00:03 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed43.json\\\\n-rw-r--r-- 1 root root   1697 May 19 23:49 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.json\\\\n-rw-r--r-- 1 root root   1698 May 19 23:45 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed44.json\\\\n-rw-r--r-- 1 root root   1693 May 19 23:25 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\\\n-rw-r--r-- 1 root root   1698 May 19 22:03 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\\\n-rw-r--r-- 1 root root   1487 May 19 21:24 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\\\n-rw-r--r-- 1 root root   1486 May 19 20:21 /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed42.json\\\\n-rw-r--r-- 1 root root   1490 May 19 19:09 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed47.json\\\\n-rw-r--r-- 1 root root   1697 May 19 18:55 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed42.json\\\\n-rw-r--r-- 1 root root   1487 May 19 17:26 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed47.json\\\\n-rw-r--r-- 1 root root   1488 May 19 16:40 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed47.json\\\\n-rw-r--r-- 1 root root   1493 May 19 16:29 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed45.json\\\\n-rw-r--r-- 1 root root   1490 May 19 16:08 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\\\n-rw-r--r-- 1 root root   1488 May 19 16:04 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed46.json\\\\n-rw-r--r-- 1 root root   1490 May 19 12:57 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45_r2.json\\\\n-rw-r--r-- 1 root root   1490 May 19 12:20 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45_r2.json\\\\n-rw-r--r-- 1 root root   1490 May 19 08:38 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed45.json\\\\n-rw-r--r-- 1 root root   1490 May 19 04:49 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed44.json\\\\n-rw-r--r-- 1 root root   1494 May 19 02:00 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed44.json\\\\n-rw-r--r-- 1 root root   1494 May 18 23:45 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed43.json\\\\n-rw-r--r-- 1 root root   1490 May 18 23:16 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed42.json\\\\n-rw-r--r-- 1 root root   1488 May 18 23:12 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed42.json\\\\n-rw-r--r-- 1 root root   1488 May 18 22:34 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed48.json\\\\n-rw-r--r-- 1 root root   1490 May 18 20:28 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed43.json\\\\n-rw-r--r-- 1 root root   1488 May 18 12:34 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.99}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 209119 May 20 11:05 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json\\n-rw-r--r-- 1 root root 200782 May 20 10:36 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json\\n-rw-r--r-- 1 root root 202822 May 20 10:33 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json\\n-rw-r--r-- 1 root root 203594 May 20 10:30 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json\\n-rw-r--r-- 1 root root 206022 May 20 10:29 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json\\n-rw-r--r-- 1 root root 199524 May 20 10:24 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json\\n-rw-r--r-- 1 root root   1783 May 20 07:57 /root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json\\n-rw-r--r-- 1 root root   1320 May 20 07:54 /root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed46.json\\n-rw-r--r-- 1 root root   1319 May 20 07:13 /root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed45_r2.json\\n-rw-r--r-- 1 root root   1319 May 20 07:10 /root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed44_r2.json\\n-rw-r--r-- 1 root root   1783 May 20 05:19 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json\\n-rw-r--r-- 1 root root   1782 May 20 05:18 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json\\n-rw-r--r-- 1 root root   1783 May 20 05:15 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json\\n-rw-r--r-- 1 root root   1485 May 20 05:14 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json\\n-rw-r--r-- 1 root root   1486 May 20 03:14 /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed44_r2.json\\n-rw-r--r-- 1 root root   1313 May 20 02:55 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45.json\\n-rw-r--r-- 1 root root   1697 May 20 02:50 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json\\n-rw-r--r-- 1 root root   1314 May 20 02:20 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r2.json\\n-rw-r--r-- 1 root root   1494 May 20 00:03 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed43.json\\n-rw-r--r-- 1 root root   1697 May 19 23:49 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.json\\n-rw-r--r-- 1 root root   1698 May 19 23:45 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed44.json\\n-rw-r--r-- 1 root root   1693 May 19 23:25 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n-rw-r--r-- 1 root root   1698 May 19 22:03 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n-rw-r--r-- 1 root root   1487 May 19 21:24 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\n-rw-r--r-- 1 root root   1486 May 19 20:21 /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed42.json\\n-rw-r--r-- 1 root root   1490 May 19 19:09 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed47.json\\n-rw-r--r-- 1 root root   1697 May 19 18:55 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed42.json\\n-rw-r--r-- 1 root root   1487 May 19 17:26 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed47.json\\n-rw-r--r-- 1 root root   1488 May 19 16:40 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed47.json\\n-rw-r--r-- 1 root root   1493 May 19 16:29 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed45.json\\n-rw-r--r-- 1 root root   1490 May 19 16:08 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\n-rw-r--r-- 1 root root   1488 May 19 16:04 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed46.json\\n-rw-r--r-- 1 root root   1490 May 19 12:57 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45_r2.json\\n-rw-r--r-- 1 root root   1490 May 19 12:20 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45_r2.json\\n-rw-r--r-- 1 root root   1490 May 19 08:38 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed45.json\\n-rw-r--r-- 1 root root   1490 May 19 04:49 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed44.json\\n-rw-r--r-- 1 root root   1494 May 19 02:00 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed44.json\\n-rw-r--r-- 1 root root   1494 May 18 23:45 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed43.json\\n-rw-r--r-- 1 root root   1490 May 18 23:16 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed42.json\\n-rw-r--r-- 1 root root   1488 May 18 23:12 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed42.json\\n-rw-r--r-- 1 root root   1488 May 18 22:34 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed48.json\\n-rw-r--r-- 1 root root   1490 May 18 20:28 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed43.json\\n-rw-r--r-- 1 root root   1488 May 18 12:34 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.99}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012pmLEAfqEYmqiTsP17AfYy`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_*.json\" -mmin -2880 -exec ls -lt {} +",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "423d23da-0fcc-4e33-9643-77830330b236",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011K5pu9sVCdhpgJgpTqGfUX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 23488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 825
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

_source line 12 · 2026-05-20T03:52:58.119Z_

<details><summary>↩ Tool result · `toolu_012pmLEAfqEYmqiTsP17AfYy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root   1691 May 20 11:21 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\\n-rw-r--r-- 1 root root   1485 May 20 11:11 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n-rw-r--r-- 1 root root   1696 May 20 11:00 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\n-rw-r--r-- 1 root root 202828 May 20 10:55 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json\\n-rw-r--r-- 1 root root   1779 May 20 07:14 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json\\n-rw-r--r-- 1 root root   1486 May 20 07:12 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json\\n-rw-r--r-- 1 root root   1783 May 20 07:10 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json\\n-rw-r--r-- 1 root root   1783 May 20 05:58 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json\\n-rw-r--r-- 1 root root   1486 May 20 05:55 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\n-rw-r--r-- 1 root root   1319 May 20 05:20 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed42.json\\n-rw-r--r-- 1 root root   1319 May 20 05:13 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed43.json\\n-rw-r--r-- 1 root root   1780 May 20 03:17 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json\\n-rw-r--r-- 1 root root   1487 May 20 02:56 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed47.json\\n-rw-r--r-- 1 root root   1490 May 20 02:51 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed48.json\\n-rw-r--r-- 1 root root   1488 May 20 02:45 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed47.json\\n-rw-r--r-- 1 root root   1692 May 19 22:38 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1490 May 19 21:44 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed48.json\\n-rw-r--r-- 1 root root   1486 May 19 19:33 /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed43.json\\n-rw-r--r-- 1 root root   1490 May 19 18:23 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed47.json\\n-rw-r--r-- 1 root root   1490 May 19 18:05 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed46.json\\n-rw-r--r-- 1 root root    814 May 19 14:48 /root/acr-vla-conformal-refinement/logs/eval_lto_splitA_vla_only_r3.json\\n-rw-r--r-- 1 root root   1488 May 19 10:44 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed44.json\\n-rw-r--r-- 1 root root   1487 May 19 08:49 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed43.json\\n-rw-r--r-- 1 root root   1490 May 19 00:49 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed48.json\\n-rw-r--r-- 1 root root   1486 May 18 21:28 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45_r2.json\\n-rw-r--r-- 1 root root   1490 May 18 21:10 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\\n-rw-r--r-- 1 root root   1490 May 18 19:39 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\\n-rw-r--r-- 1 root root   1488 May 18 18:14 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "8ce94566-9ff5-4b07-a4ea-3d14d7b996d6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root   1691 May 20 11:21 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\\\\n-rw-r--r-- 1 root root   1485 May 20 11:11 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\\\n-rw-r--r-- 1 root root   1696 May 20 11:00 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\\\n-rw-r--r-- 1 root root 202828 May 20 10:55 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json\\\\n-rw-r--r-- 1 root root   1779 May 20 07:14 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json\\\\n-rw-r--r-- 1 root root   1486 May 20 07:12 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json\\\\n-rw-r--r-- 1 root root   1783 May 20 07:10 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json\\\\n-rw-r--r-- 1 root root   1783 May 20 05:58 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json\\\\n-rw-r--r-- 1 root root   1486 May 20 05:55 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\\\n-rw-r--r-- 1 root root   1319 May 20 05:20 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed42.json\\\\n-rw-r--r-- 1 root root   1319 May 20 05:13 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed43.json\\\\n-rw-r--r-- 1 root root   1780 May 20 03:17 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json\\\\n-rw-r--r-- 1 root root   1487 May 20 02:56 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed47.json\\\\n-rw-r--r-- 1 root root   1490 May 20 02:51 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed48.json\\\\n-rw-r--r-- 1 root root   1488 May 20 02:45 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed47.json\\\\n-rw-r--r-- 1 root root   1692 May 19 22:38 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\\\\n-rw-r--r-- 1 root root   1490 May 19 21:44 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed48.json\\\\n-rw-r--r-- 1 root root   1486 May 19 19:33 /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed43.json\\\\n-rw-r--r-- 1 root root   1490 May 19 18:23 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed47.json\\\\n-rw-r--r-- 1 root root   1490 May 19 18:05 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed46.json\\\\n-rw-r--r-- 1 root root    814 May 19 14:48 /root/acr-vla-conformal-refinement/logs/eval_lto_splitA_vla_only_r3.json\\\\n-rw-r--r-- 1 root root   1488 May 19 10:44 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed44.json\\\\n-rw-r--r-- 1 root root   1487 May 19 08:49 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed43.json\\\\n-rw-r--r-- 1 root root   1490 May 19 00:49 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed48.json\\\\n-rw-r--r-- 1 root root   1486 May 18 21:28 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45_r2.json\\\\n-rw-r--r-- 1 root root   1490 May 18 21:10 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\\\\n-rw-r--r-- 1 root root   1490 May 18 19:39 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\\\\n-rw-r--r-- 1 root root   1488 May 18 18:14 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.89}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root   1691 May 20 11:21 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json\\n-rw-r--r-- 1 root root   1485 May 20 11:11 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n-rw-r--r-- 1 root root   1696 May 20 11:00 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\n-rw-r--r-- 1 root root 202828 May 20 10:55 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json\\n-rw-r--r-- 1 root root   1779 May 20 07:14 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json\\n-rw-r--r-- 1 root root   1486 May 20 07:12 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json\\n-rw-r--r-- 1 root root   1783 May 20 07:10 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json\\n-rw-r--r-- 1 root root   1783 May 20 05:58 /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json\\n-rw-r--r-- 1 root root   1486 May 20 05:55 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\n-rw-r--r-- 1 root root   1319 May 20 05:20 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed42.json\\n-rw-r--r-- 1 root root   1319 May 20 05:13 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed43.json\\n-rw-r--r-- 1 root root   1780 May 20 03:17 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json\\n-rw-r--r-- 1 root root   1487 May 20 02:56 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed47.json\\n-rw-r--r-- 1 root root   1490 May 20 02:51 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed48.json\\n-rw-r--r-- 1 root root   1488 May 20 02:45 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed47.json\\n-rw-r--r-- 1 root root   1692 May 19 22:38 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1490 May 19 21:44 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed48.json\\n-rw-r--r-- 1 root root   1486 May 19 19:33 /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed43.json\\n-rw-r--r-- 1 root root   1490 May 19 18:23 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed47.json\\n-rw-r--r-- 1 root root   1490 May 19 18:05 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed46.json\\n-rw-r--r-- 1 root root    814 May 19 14:48 /root/acr-vla-conformal-refinement/logs/eval_lto_splitA_vla_only_r3.json\\n-rw-r--r-- 1 root root   1488 May 19 10:44 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed44.json\\n-rw-r--r-- 1 root root   1487 May 19 08:49 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed43.json\\n-rw-r--r-- 1 root root   1490 May 19 00:49 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed48.json\\n-rw-r--r-- 1 root root   1486 May 18 21:28 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45_r2.json\\n-rw-r--r-- 1 root root   1490 May 18 21:10 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json\\n-rw-r--r-- 1 root root   1490 May 18 19:39 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json\\n-rw-r--r-- 1 root root   1488 May 18 18:14 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015ge7TzEsZJoj3ure5St1Ww`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_*.json\" -mmin -2880 -exec ls -lt {} +",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "72fdf724-4b74-4fb7-a0ba-f836b838c6ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011K5pu9sVCdhpgJgpTqGfUX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 23488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 825
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

_source line 14 · 2026-05-20T03:52:59.386Z_

<details><summary>↩ Tool result · `toolu_015ge7TzEsZJoj3ure5St1Ww`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root   1691 May 20 11:13 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\\n-rw-r--r-- 1 root root   1697 May 20 10:53 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\\n-rw-r--r-- 1 root root 207117 May 20 10:29 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json\\n-rw-r--r-- 1 root root 205011 May 20 10:23 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json\\n-rw-r--r-- 1 root root 202018 May 20 10:15 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json\\n-rw-r--r-- 1 root root 199451 May 20 10:10 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json\\n-rw-r--r-- 1 root root   1485 May 20 06:58 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n-rw-r--r-- 1 root root   1692 May 20 06:50 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json\\n-rw-r--r-- 1 root root   1779 May 20 06:25 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed47.json\\n-rw-r--r-- 1 root root   1692 May 20 06:06 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json\\n-rw-r--r-- 1 root root   1319 May 20 05:38 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\n-rw-r--r-- 1 root root   1319 May 20 05:37 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\n-rw-r--r-- 1 root root   1691 May 20 04:23 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json\\n-rw-r--r-- 1 root root   1779 May 20 03:55 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json\\n-rw-r--r-- 1 root root   1698 May 20 03:44 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43_r2.json\\n-rw-r--r-- 1 root root   1313 May 20 03:11 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n-rw-r--r-- 1 root root   1779 May 20 02:33 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json\\n-rw-r--r-- 1 root root   1779 May 20 02:33 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json\\n-rw-r--r-- 1 root root   1779 May 20 02:30 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1314 May 20 01:48 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1313 May 20 01:45 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n-rw-r--r-- 1 root root   1696 May 20 00:58 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\n-rw-r--r-- 1 root root   1494 May 19 23:57 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json\\n-rw-r--r-- 1 root root   1493 May 19 23:50 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json\\n-rw-r--r-- 1 root root   1494 May 19 23:45 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json\\n-rw-r--r-- 1 root root   1487 May 19 23:20 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\n-rw-r--r-- 1 root root   1692 May 19 23:16 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\n-rw-r--r-- 1 root root   1490 May 19 22:45 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\n-rw-r--r-- 1 root root   1692 May 19 22:32 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\n-rw-r--r-- 1 root root   1490 May 19 21:48 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json\\n-rw-r--r-- 1 root root   1486 May 19 21:26 /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\\n-rw-r--r-- 1 root root   1486 May 19 21:24 /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\\n-rw-r--r-- 1 root root   1486 May 19 21:24 /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n-rw-r--r-- 1 root root   1697 May 19 20:41 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.json\\n-rw-r--r-- 1 root root   1488 May 19 19:29 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\\n-rw-r--r-- 1 root root   1490 May 19 18:47 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed48.json\\n-rw-r--r-- 1 root root   1697 May 19 18:18 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed43.json\\n-rw-r--r-- 1 root root   1488 May 19 14:52 /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json\\n-rw-r--r-- 1 root root   1488 May 19 14:41 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json\\n-rw-r--r-- 1 root root   1488 May 19 14:24 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json\\n-rw-r--r-- 1 root root   1490 May 19 13:50 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json\\n-rw-r--r-- 1 root root   1490 May 19 13:30 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json\\n-rw-r--r-- 1 root root   1488 May 19 11:25 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed43.json\\n-rw-r--r-- 1 root root   1488 May 19 10:32 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed43.json\\n-rw-r--r-- 1 root root   1487 May 19 08:56 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed45.json\\n-rw-r--r-- 1 root root   1488 May 18 22:32 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed43.json\\n-rw-r--r-- 1 root root   1490 May 18 22:11 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.json\\n-rw-r--r-- 1 root root   1490 May 18 21:17 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.json\\n-rw-r--r-- 1 root root   1490 May 18 21:03 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\n-rw-r--r-- 1 root root   1488 May 18 20:32 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json\\n-rw-r--r-- 1 root root   1488 May 18 18:34 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.78}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "8c35a35d-858d-4681-a067-1ced6228c861",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root   1691 May 20 11:13 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\\\\n-rw-r--r-- 1 root root   1697 May 20 10:53 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\\\\n-rw-r--r-- 1 root root 207117 May 20 10:29 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json\\\\n-rw-r--r-- 1 root root 205011 May 20 10:23 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json\\\\n-rw-r--r-- 1 root root 202018 May 20 10:15 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json\\\\n-rw-r--r-- 1 root root 199451 May 20 10:10 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json\\\\n-rw-r--r-- 1 root root   1485 May 20 06:58 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\\\n-rw-r--r-- 1 root root   1692 May 20 06:50 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json\\\\n-rw-r--r-- 1 root root   1779 May 20 06:25 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed47.json\\\\n-rw-r--r-- 1 root root   1692 May 20 06:06 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json\\\\n-rw-r--r-- 1 root root   1319 May 20 05:38 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\\\n-rw-r--r-- 1 root root   1319 May 20 05:37 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\\\n-rw-r--r-- 1 root root   1691 May 20 04:23 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json\\\\n-rw-r--r-- 1 root root   1779 May 20 03:55 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json\\\\n-rw-r--r-- 1 root root   1698 May 20 03:44 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43_r2.json\\\\n-rw-r--r-- 1 root root   1313 May 20 03:11 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\\\n-rw-r--r-- 1 root root   1779 May 20 02:33 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json\\\\n-rw-r--r-- 1 root root   1779 May 20 02:33 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json\\\\n-rw-r--r-- 1 root root   1779 May 20 02:30 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json\\\\n-rw-r--r-- 1 root root   1314 May 20 01:48 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\\\n-rw-r--r-- 1 root root   1313 May 20 01:45 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\\\n-rw-r--r-- 1 root root   1696 May 20 00:58 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\\\n-rw-r--r-- 1 root root   1494 May 19 23:57 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json\\\\n-rw-r--r-- 1 root root   1493 May 19 23:50 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json\\\\n-rw-r--r-- 1 root root   1494 May 19 23:45 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json\\\\n-rw-r--r-- 1 root root   1487 May 19 23:20 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\\\n-rw-r--r-- 1 root root   1692 May 19 23:16 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\\\n-rw-r--r-- 1 root root   1490 May 19 22:45 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\\\n-rw-r--r-- 1 root root   1692 May 19 22:32 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\\\n-rw-r--r-- 1 root root   1490 May 19 21:48 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json\\\\n-rw-r--r-- 1 root root   1486 May 19 21:26 /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\\\\n-rw-r--r-- 1 root root   1486 May 19 21:24 /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\\\\n-rw-r--r-- 1 root root   1486 May 19 21:24 /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\\\n-rw-r--r-- 1 root root   1697 May 19 20:41 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.json\\\\n-rw-r--r-- 1 root root   1488 May 19 19:29 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\\\\n-rw-r--r-- 1 root root   1490 May 19 18:47 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed48.json\\\\n-rw-r--r-- 1 root root   1697 May 19 18:18 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed43.json\\\\n-rw-r--r-- 1 root root   1488 May 19 14:52 /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json\\\\n-rw-r--r-- 1 root root   1488 May 19 14:41 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json\\\\n-rw-r--r-- 1 root root   1488 May 19 14:24 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json\\\\n-rw-r--r-- 1 root root   1490 May 19 13:50 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json\\\\n-rw-r--r-- 1 root root   1490 May 19 13:30 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json\\\\n-rw-r--r-- 1 root root   1488 May 19 11:25 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed43.json\\\\n-rw-r--r-- 1 root root   1488 May 19 10:32 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed43.json\\\\n-rw-r--r-- 1 root root   1487 May 19 08:56 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed45.json\\\\n-rw-r--r-- 1 root root   1488 May 18 22:32 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed43.json\\\\n-rw-r--r-- 1 root root   1490 May 18 22:11 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.json\\\\n-rw-r--r-- 1 root root   1490 May 18 21:17 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.json\\\\n-rw-r--r-- 1 root root   1490 May 18 21:03 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\\\n-rw-r--r-- 1 root root   1488 May 18 20:32 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json\\\\n-rw-r--r-- 1 root root   1488 May 18 18:34 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.78}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root   1691 May 20 11:13 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\\n-rw-r--r-- 1 root root   1697 May 20 10:53 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\\n-rw-r--r-- 1 root root 207117 May 20 10:29 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json\\n-rw-r--r-- 1 root root 205011 May 20 10:23 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json\\n-rw-r--r-- 1 root root 202018 May 20 10:15 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json\\n-rw-r--r-- 1 root root 199451 May 20 10:10 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json\\n-rw-r--r-- 1 root root   1485 May 20 06:58 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json\\n-rw-r--r-- 1 root root   1692 May 20 06:50 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json\\n-rw-r--r-- 1 root root   1779 May 20 06:25 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed47.json\\n-rw-r--r-- 1 root root   1692 May 20 06:06 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json\\n-rw-r--r-- 1 root root   1319 May 20 05:38 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\n-rw-r--r-- 1 root root   1319 May 20 05:37 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\n-rw-r--r-- 1 root root   1691 May 20 04:23 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json\\n-rw-r--r-- 1 root root   1779 May 20 03:55 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json\\n-rw-r--r-- 1 root root   1698 May 20 03:44 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43_r2.json\\n-rw-r--r-- 1 root root   1313 May 20 03:11 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n-rw-r--r-- 1 root root   1779 May 20 02:33 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json\\n-rw-r--r-- 1 root root   1779 May 20 02:33 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json\\n-rw-r--r-- 1 root root   1779 May 20 02:30 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1314 May 20 01:48 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1313 May 20 01:45 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n-rw-r--r-- 1 root root   1696 May 20 00:58 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\n-rw-r--r-- 1 root root   1494 May 19 23:57 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json\\n-rw-r--r-- 1 root root   1493 May 19 23:50 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json\\n-rw-r--r-- 1 root root   1494 May 19 23:45 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json\\n-rw-r--r-- 1 root root   1487 May 19 23:20 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json\\n-rw-r--r-- 1 root root   1692 May 19 23:16 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\n-rw-r--r-- 1 root root   1490 May 19 22:45 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json\\n-rw-r--r-- 1 root root   1692 May 19 22:32 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\n-rw-r--r-- 1 root root   1490 May 19 21:48 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json\\n-rw-r--r-- 1 root root   1486 May 19 21:26 /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json\\n-rw-r--r-- 1 root root   1486 May 19 21:24 /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json\\n-rw-r--r-- 1 root root   1486 May 19 21:24 /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n-rw-r--r-- 1 root root   1697 May 19 20:41 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.json\\n-rw-r--r-- 1 root root   1488 May 19 19:29 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.json\\n-rw-r--r-- 1 root root   1490 May 19 18:47 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed48.json\\n-rw-r--r-- 1 root root   1697 May 19 18:18 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed43.json\\n-rw-r--r-- 1 root root   1488 May 19 14:52 /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json\\n-rw-r--r-- 1 root root   1488 May 19 14:41 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json\\n-rw-r--r-- 1 root root   1488 May 19 14:24 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json\\n-rw-r--r-- 1 root root   1490 May 19 13:50 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json\\n-rw-r--r-- 1 root root   1490 May 19 13:30 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json\\n-rw-r--r-- 1 root root   1488 May 19 11:25 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed43.json\\n-rw-r--r-- 1 root root   1488 May 19 10:32 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed43.json\\n-rw-r--r-- 1 root root   1487 May 19 08:56 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed45.json\\n-rw-r--r-- 1 root root   1488 May 18 22:32 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed43.json\\n-rw-r--r-- 1 root root   1490 May 18 22:11 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.json\\n-rw-r--r-- 1 root root   1490 May 18 21:17 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.json\\n-rw-r--r-- 1 root root   1490 May 18 21:03 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\n-rw-r--r-- 1 root root   1488 May 18 20:32 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json\\n-rw-r--r-- 1 root root   1488 May 18 18:34 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.78}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018vaPnZQZgqbTD8p46CHzdG`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_*.json\" -mmin -2880 -exec ls -lt {} +",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "c70d636e-3d96-42e1-b59f-47c2269faefa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011K5pu9sVCdhpgJgpTqGfUX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 23488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 825
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

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01M579vNLWy4RnCCou9Avxdb`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "6ac8d57a-69dd-4ed5-930a-a488b7a39baf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011K5pu9sVCdhpgJgpTqGfUX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 23488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 825
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

_source line 17 · 2026-05-20T03:53:00.726Z_

<details><summary>↩ Tool result · `toolu_018vaPnZQZgqbTD8p46CHzdG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1485 May 20 07:36 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\n-rw-r--r-- 1 root root 1696 May 20 04:28 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n-rw-r--r-- 1 root root 1488 May 19 19:40 /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json\\n-rw-r--r-- 1 root root 1494 May 18 20:17 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "f53d8ce4-be44-4d8a-86b3-9bdf62ccc3d8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 1485 May 20 07:36 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\\\n-rw-r--r-- 1 root root 1696 May 20 04:28 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\\\n-rw-r--r-- 1 root root 1488 May 19 19:40 /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json\\\\n-rw-r--r-- 1 root root 1494 May 18 20:17 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.85}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1485 May 20 07:36 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\n-rw-r--r-- 1 root root 1696 May 20 04:28 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n-rw-r--r-- 1 root root 1488 May 19 19:40 /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json\\n-rw-r--r-- 1 root root 1494 May 18 20:17 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T03:53:02.052Z_

<details><summary>↩ Tool result · `toolu_01M579vNLWy4RnCCou9Avxdb`</summary>

```text
Error: result (219,136 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249182037.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249182037.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "7d2f9586-fe6b-4648-bd55-a7193c6adaec",
  "tool_use_result": {
    "content": "Error: result (219,136 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249182037.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249182037.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-only-goal-seed49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T03:51:05.182Z\", \"updated_at\": \"2026-05-20T03:51:41.452Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed49. 补齐 Goal baseline 样本量，与 CRM-Goal (64-72% SR) 配对对比。\"}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:09:08.601Z\", \"updated_at\": \"2026-05-20T03:51:17.533Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. r3 重试。补充 perdof magnitude curve ε=0.2 数据。\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_completed\": 10, \"total_rollouts\": 100}, \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:15.980Z\", \"updated_at\": \"2026-05-20T03:51:15.551Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed43 on LIBERO-Object. M006 补救：补充 magnitude curve 低 norm 段多 seed 数据。seed42 ε=0.05=13%。\", \"conclusion\": \"killed\", \"notes\": \"Superseded by eval-obs-only-object-norm005-seed43-r2 (bjb1-32546) and r3 (bjb1-18228)\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:05:24.390Z\", \"updated_at\": \"2026-05-20T03:51:13.757Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed48 on LIBERO-Object. 补充 magnitude curve ε=0.2 数据，扩展 error bars。\", \"metrics\": {\"overall_sr\": 0.07, \"successes\": 7, \"total\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"killed\"}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:53:24.027Z\", \"updated_at\": \"2026-05-20T03:51:12.210Z\", \"hypothesis\": \"OpenVLA-7B fine-tuned on LIBERO-Object baseline eval (seed42). 复现官方 88.4% SR，获取 per-task breakdown 与 SmolVLA 对比。如果 SR 符合预期，验证 CRM 路线的 base policy 基线可用性。\", \"conclusion\": \"killed\", \"notes\": \"失败原因: EXIT_CODE=124 timeout。完成 400/500 episodes (8/10 tasks)，SR=68.0% (272/400)。第9个task (pick_up_milk) 4/50时被kill。每episode ~60s，500 episodes需~8.3h但timeout仅~6h。已有成果: 前8个task数据完整。建议: 加大timeout_hours至12h重跑。\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:04:51.797Z\", \"updated_at\": \"2026-05-20T03:51:10.457Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla) on LIBERO-Object seed44. 重跑：原实验 eval-argmin-object-k5-seed44 因 SIGKILL 失败。Isolate selection-only benefit (无 CRM correction)，与 seed42/43/45 配套。\", \"parent\": \"eval-argmin-object-k5-seed44\", \"metrics\": {\"sr\": 0.11, \"sr_pct\": \"11%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.3, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:04:56.660Z\", \"updated_at\": \"2026-05-20T03:51:08.695Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed44. 重跑：原实验被 SIGKILL（M023）。扩展到新 benchmark suite 验证 CRM 泛化性的前提——先建立 baseline。\", \"parent\": \"eval-vla-only-goal-seed44\", \"metrics\": {\"overall_success_rate\": 0.73, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.6, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:04:55.082Z\", \"updated_at\": \"2026-05-20T03:51:06.894Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed46. 重跑：原实验被 SIGKILL（M023）。补充 Spatial K=10 cross-benchmark 数据。\", \"parent\": \"eval-obs-only-spatial-norm02-seed46\", \"metrics\": {\"sr\": 0.33, \"sr_pct\": \"33.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0.1, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.8, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"killed\"}, \"eval-crm-long-seed50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T03:16:23.286Z\", \"updated_at\": \"2026-05-20T03:16:41.705Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Long seed50. Long OOD 补样本量，验证 CRM 在 cross-suite OOD 上的效果。\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T03:16:19.625Z\", \"updated_at\": \"2026-05-20T03:16:39.456Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed44. 重新部署在干净 GPU 上（原 bjb2-40593 与 calibration 共享 GPU 拖慢）。Sweep 最后一个数据点。\"}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T22:53:06.901Z\", \"updated_at\": \"2026-05-20T03:15:36.605Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed43. ~75% steps trigger K=10+CRM. P25 sweep 第二个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 4.788, \"fast_path_ratio\": 0.6515, \"total_steps\": 28207, \"fast_steps\": 18377, \"full_steps\": 9830}}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"ALLOCATED\", \"created_at\": \"2026-05-19T22:52:55.910Z\", \"updated_at\": \"2026-05-20T03:15:32.975Z\", \"hypothesis\": \"Adaptive K with τ=P50 (0.074855) on LIBERO-Object seed43. ~50% steps trigger K=10+CRM, rest use K=2 fast path. P50 sweep 第二个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.81, \"fast_path_ratio\": 0.7737, \"total_steps\": 27813, \"fast_steps\": 21520, \"full_steps\": 6293}}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T03:14:26.858Z\", \"updated_at\": \"2026-05-20T03:14:41.521Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}}}, \"eval-vla-only-spatial-seed51\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T03:12:22.300Z\", \"updated_at\": \"2026-05-20T03:12:40.851Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed51. 补齐 Spatial baseline 样本量，与 CRM-Spatial 配对检验。\"}, \"eval-vla-only-long-seed52\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T03:12:18.551Z\", \"updated_at\": \"2026-05-20T03:12:37.882Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed52. 补齐 Long VLA-only 样本量，增强 OOD baseline 统计可靠性。\"}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T03:12:15.310Z\", \"updated_at\": \"2026-05-20T03:12:36.238Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed51. 补齐 Spatial CRM 样本量，增强 ID suite correction 效果的统计可靠性。\"}, \"eval-vla-only-long-seed51\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T03:12:11.506Z\", \"updated_at\": \"2026-05-20T03:12:34.134Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed51. 补齐 Long VLA-only 样本量，增强 OOD baseline 统计可靠性。\"}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:05.392Z\", \"updated_at\": \"2026-05-20T03:05:13.741Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed42. ~75% steps trigger K=10+CRM. 低阈值极端——接近 fixed K=10，验证 SR 上限。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.8, \"fast_path_ratio\": 0.65}}, \"eval-vla-only-goal-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:08:24.943Z\", \"updated_at\": \"2026-05-20T03:02:41.906Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed48. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。重跑（前次 killed for CRM priority）。\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:08:22.088Z\", \"updated_at\": \"2026-05-20T03:02:34.679Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed47. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。重跑（前次 killed for CRM priority）。\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed48\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:57:44.184Z\", \"updated_at\": \"2026-05-20T02:57:52.957Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Goal seed48. Goal OOD 补样本量 (n→6)，验证 CRM 在 cross-suite OOD 上的效果。seed46=72% 推高均值，看是否一致。\"}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"ALLOCATED\", \"created_at\": \"2026-05-19T22:52:54.375Z\", \"updated_at\": \"2026-05-20T02:55:44.980Z\", \"hypothesis\": \"Adaptive K with τ=P50 (0.074855) on LIBERO-Object seed42. ~50% steps trigger K=10+CRM, rest use K=2 fast path. 测试 SR vs avg_K 的 Pareto 最优阈值。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.72, \"fast_path_ratio\": 0.785}}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"ALLOCATED\", \"created_at\": \"2026-05-19T22:52:51.298Z\", \"updated_at\": \"2026-05-20T02:55:37.755Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735) on LIBERO-Object seed43. ~25% steps trigger K=10+CRM, rest use K=2 fast path. P75 sweep 第二个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 3.15, \"fast_path_ratio\": 0.856}}, \"eval-crm-goal-seed47\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:54:07.709Z\", \"updated_at\": \"2026-05-20T02:54:31.036Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Goal seed47. Goal OOD 补样本量 (n→6)，增强 cross-suite OOD 统计可靠性。\"}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:43:05.230Z\", \"updated_at\": \"2026-05-20T02:54:29.366Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Goal seed46. Goal OOD 补样本量 (n→5)，验证 CRM 在 cross-suite OOD 上的效果（当前 n=2 结果中性 ~69.5%≈VLA-only）。\", \"parent\": \"eval-crm-goal-seed42\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.3}}}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T22:53:13.788Z\", \"updated_at\": \"2026-05-20T02:52:29.115Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.126512) on LIBERO-Object seed44. ~10% steps trigger K=10+CRM. P90 sweep 第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.58, \"fast_path_ratio\": 0.928}}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"ALLOCATED\", \"created_at\": \"2026-05-19T22:52:49.558Z\", \"updated_at\": \"2026-05-20T02:52:22.430Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735) on LIBERO-Object seed42. ~25% steps trigger K=10+CRM, rest use K=2 fast path. 测试 SR vs avg_K 的 Pareto 最优阈值。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 3.07, \"fast_path_ratio\": 0.866}}, \"calibrate-crm-correction-signal\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:47:03.770Z\", \"updated_at\": \"2026-05-20T02:50:31.578Z\", \"hypothesis\": \"CRM correction magnitude as zero-overhead gating signal. Three correlation pairs: (1) ρ(K1_correction_mag, K10_var) — primary GO/NO-GO (threshold ρ>0.3); (2) ρ(K2_argmin_correction_mag, K10_var) — fallback if K1 fails; (3) ρ(K1_correction_mag, K2_L2_distance) — cross-validate with proven K=2 signal. If GO: zero-cost adaptive K (CRM 0.25ms, no extra VLA inference).\"}, \"eval-crm-long-seed49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:43:08.930Z\", \"updated_at\": \"2026-05-20T02:43:34.000Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Long seed49. 补齐 Long CRM OOD 样本量 (n→8)，验证 CRM 在 OOD Long 上的效果稳定性。\"}, \"eval-crm-long-seed48\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:43:05.584Z\", \"updated_at\": \"2026-05-20T02:43:32.381Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Long seed48. 补齐 Long CRM OOD 样本量 (n→7)，验证 CRM 在 OOD Long 上的 +5.3pp 效果是否稳定或集中于单 task。\"}, \"eval-vla-only-object-seed51\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:43:01.821Z\", \"updated_at\": \"2026-05-20T02:43:30.806Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed51. 补齐 Object VLA-only 样本量 (n→8+)，增强主 ID benchmark baseline 统计可靠性。\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:42:58.271Z\", \"updated_at\": \"2026-05-20T02:43:27.709Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed50. 补齐 Spatial CRM 样本量 (n→7+)，增强 ID suite 上 CRM correction 效果的统计可靠性。\"}, \"eval-vla-only-long-seed50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:42:54.485Z\", \"updated_at\": \"2026-05-20T02:43:24.267Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed50. 补齐 Long VLA-only 样本量 (n→9)，增强 OOD baseline 统计可靠性。\"}, \"eval-vla-only-long-seed49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:42:51.266Z\", \"updated_at\": \"2026-05-20T02:43:21.463Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed49. 补齐 Long VLA-only 样本量 (n→8)，增强 OOD baseline 统计可靠性，与 CRM-Long 配对检验。\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T02:42:47.989Z\", \"updated_at\": \"2026-05-20T02:43:19.060Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed49. 补齐 Spatial CRM 样本量 (n→6+)，增强 ID suite 上 CRM correction 效果的统计可靠性。\"}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:57.407Z\", \"updated_at\": \"2026-05-20T02:40:24.520Z\", \"hypothesis\": \"Adaptive K with τ=P50 (0.074855) on LIBERO-Object seed44. ~50% steps trigger K=10+CRM, rest use K=2 fast path. P50 sweep 第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 3.909, \"fast_path_ratio\": 0.761, \"total_steps\": 28067, \"fast_steps\": 21368, \"full_steps\": 6699}}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:52:52.859Z\", \"updated_at\": \"2026-05-20T02:40:21.205Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735) on LIBERO-Object seed44. ~25% steps trigger K=10+CRM, rest use K=2 fast path. P75 sweep 第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.022, \"fast_path_ratio\": 0.872, \"total_steps\": 27724, \"fast_steps\": 24181, \"full_steps\": 3543}}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:12.128Z\", \"updated_at\": \"2026-05-20T02:40:15.747Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.126512) on LIBERO-Object seed43. ~10% steps trigger K=10+CRM. P90 sweep 第二个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.612, \"fast_path_ratio\": 0.923, \"total_steps\": 27935, \"fast_steps\": 25797, \"full_steps\": 2138}}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:53:10.641Z\", \"updated_at\": \"2026-05-20T02:40:12.273Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.126512) on LIBERO-Object seed42. ~10% steps trigger K=10+CRM. 高阈值极端——接近 K=2 only，验证 SR 下限。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 2.672, \"fast_path_ratio\": 0.916, \"total_steps\": 28258, \"fast_steps\": 25886, \"full_steps\": 2372}}, \"eval-adaptive-k-p25-seed44\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T22:53:09.016Z\", \"updated_at\": \"2026-05-20T02:36:09.821Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959) on LIBERO-Object seed44. ~75% steps trigger K=10+CRM. P25 sweep 第三个 seed。\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T01:18:47.309Z\", \"updated_at\": \"2026-05-20T01:42:26.302Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed50. 补齐 Spatial baseline 样本量，与 CRM Spatial 配对统计检验。\"}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:51:39.170Z\", \"updated_at\": \"2026-05-20T01:39:25.709Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed47. 额外 seed 增加统计稳健性，与 CRM Spatial seed47 配对。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-crm-spatial-seed48\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T01:20:10.184Z\", \"updated_at\": \"2026-05-20T01:20:10.184Z\"}, \"eval-crm-spatial-seed47\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T01:18:50.143Z\", \"updated_at\": \"2026-05-20T01:19:10.476Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Spatial seed47. 补齐 CRM-Spatial 第 6 个 seed（当前 n=5, seeds 42-46），增强 in-distribution 效果的统计显著性。\"}, \"eval-vla-only-object-seed49-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T01:19:03.093Z\", \"updated_at\": \"2026-05-20T01:19:03.093Z\"}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:15:12.591Z\", \"updated_at\": \"2026-05-20T01:18:45.609Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed49. 补齐 Object baseline 样本量，增强统计可靠性。\", \"conclusion\": \"killed\"}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:49:36.050Z\", \"updated_at\": \"2026-05-20T00:21:06.698Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Long seed47. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Long 是 OOD long-horizon 任务。补充 seed42-46 增加统计样本量。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.2, \"STUDY_SCENE1_book_in_caddy\": 0.2, \"LIVING_ROOM_SCENE2_soup_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cheese_butter_basket\": 0, \"KITCHEN_SCENE4_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_soup_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:31.390Z\", \"updated_at\": \"2026-05-20T00:19:44.143Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed48. 补齐 Object VLA-only 样本量，与 CRM K=10 配对统计检验。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"n_episodes\": 100}}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:24:15.951Z\", \"updated_at\": \"2026-05-20T00:16:50.121Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Long seed48. 补齐 Long VLA-only 样本量 (n→7)，增强 baseline 统计可靠性。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.3, \"STUDY_SCENE1_book_in_back_compartment\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0.1, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:24:17.487Z\", \"updated_at\": \"2026-05-20T00:16:32.874Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed50. 补齐 Object VLA-only 样本量 (n→6)，与 CRM K=10 配对统计检验。\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100, \"successes\": 9, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:24:13.996Z\", \"updated_at\": \"2026-05-20T00:13:08.430Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Long seed46. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Long 是未见过的 suite。补齐 CRM-Long 第 5 个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.9, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.2, \"STUDY_SCENE1_book_in_back_compartment\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:49:33.318Z\", \"updated_at\": \"2026-05-20T00:11:46.069Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed45. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。重跑（前次 crash）。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.65, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_bowl_on_top_of_the_cabinet\": 0.8, \"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"put_the_wine_bottle_on_the_rack\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_cream_cheese_in_the_bowl\": 0.2}}}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:49:31.838Z\", \"updated_at\": \"2026-05-20T00:11:07.345Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed44. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。重跑（前次 crash）。\", \"parent\": \"eval-crm-goal-seed44\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.64, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_bowl_on_the_stove\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"put_the_wine_bottle_on_the_rack\": 0.4, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:06:58.021Z\", \"updated_at\": \"2026-05-19T23:20:20.286Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed43. 重跑：bjb2-40593 上 7/10 tasks 后进程终止无 JSON。补齐 Spatial K=10 n=5。\", \"parent\": \"eval-obs-only-spatial-norm02-seed43\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T23:07:05.761Z\", \"updated_at\": \"2026-05-19T23:07:36.717Z\", \"hypothesis\": \"OpenVLA-7B fine-tuned on LIBERO-Object baseline eval (seed42). 复现官方 88.4% SR，获取 per-task breakdown 与 SmolVLA 对比。如果 SR 符合预期，验证 CRM 路线的 base policy 基线可用性。重试：前次 timeout (6h不够，需~10h)。\", \"parent\": \"eval-openvla-object-baseline-seed42\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:32:52.408Z\", \"updated_at\": \"2026-05-19T22:38:04.117Z\", \"hypothesis\": \"K=2 L2 divergence (mean pairwise L2 from K=10 samples) as uncertainty proxy for Adaptive K. Measures action-space disagreement directly. Go/no-go: Spearman ρ(mean_pair_l2, k10_variance) > 0.3.\", \"conclusion\": \"success\", \"metrics\": {\"k2l2_vs_k10var_rho\": 0.9979, \"k2l2_vs_k10var_pvalue\": 0, \"k2l2_vs_fmvd_rho\": 0.0925, \"k2l2_vs_fmvd_pvalue\": 6.03e-29, \"k10var_vs_fmvd_rho\": 0.0825, \"k10var_vs_fmvd_pvalue\": 2.33e-23, \"n_samples\": 14512, \"k2l2_mean\": 0.0807, \"k2l2_std\": 0.0361, \"go_nogo_k2_proxy\": \"GO (rho=0.9979)\", \"go_nogo_fmvd_signal\": \"NO-GO (rho=0.09)\"}}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:29.495Z\", \"updated_at\": \"2026-05-19T22:15:17.800Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed45. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD long-horizon 任务。补充 seed42/43/44 增加 n。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 18}}, \"eval-vla-only-spatial-seed49-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T22:12:47.550Z\", \"updated_at\": \"2026-05-19T22:12:58.379Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed49. 补齐 Spatial VLA-only 样本量 (n→7)。重跑（前次进程死亡）。\"}, \"eval-vla-only-spatial-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:15:11.071Z\", \"updated_at\": \"2026-05-19T22:12:05.406Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed49. 补齐 Spatial VLA-only 样本量 (n→7)，增强 baseline 统计可靠性。\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:32:25.931Z\", \"updated_at\": \"2026-05-19T22:08:08.414Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed48. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。\", \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:32:24.476Z\", \"updated_at\": \"2026-05-19T22:08:05.186Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed47. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。\", \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:40:01.140Z\", \"updated_at\": \"2026-05-19T21:32:22.969Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed43. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.69, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.5, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.6}}}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:39:58.936Z\", \"updated_at\": \"2026-05-19T21:32:21.219Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed42. 补齐 Goal VLA-only 样本量 (n→7)，与 CRM-Goal 配对统计检验。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:10:43.834Z\", \"updated_at\": \"2026-05-19T21:32:10.689Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed47. 补齐 Object VLA-only n=5，与 CRM K=10 配对统计检验。\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2, \"alphabet_soup\": 0, \"cream_cheese\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:10:50.501Z\", \"updated_at\": \"2026-05-19T21:32:07.617Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed44. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%，若 CRM 显著提升则证明泛化；若无效则定位 CRM 边界。\", \"metrics\": {\"overall_success_rate\": 0.2, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.6, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:10:49.078Z\", \"updated_at\": \"2026-05-19T21:32:03.390Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed43. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%，若 CRM 显著提升则证明泛化；若无效则定位 CRM 边界。\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.3, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:10:47.244Z\", \"updated_at\": \"2026-05-19T21:31:58.213Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-10 seed42. 跨 suite 泛化性测试：CRM 仅在 Object+Spatial 训练，LIBERO-10 是 OOD。Long baseline=12%，若 CRM 显著提升则证明泛化；若无效则定位 CRM 边界。\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.4, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:24.873Z\", \"updated_at\": \"2026-05-19T21:22:37.560Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed42. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。若 CRM 提升 Goal SR，证明跨 suite 泛化；若无效则定位 CRM 边界。\", \"metrics\": {\"overall_success_rate\": 0.67, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:10:26.786Z\", \"updated_at\": \"2026-05-19T21:19:08.468Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=10) on LIBERO-Goal seed43. OOD 泛化测试：CRM 仅在 Object+Spatial 训练，Goal 是未见过的 suite。与 seed42 配对增加统计稳健性。\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.4}}, \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:51:37.036Z\", \"updated_at\": \"2026-05-19T21:15:20.345Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed46. 补齐 Spatial VLA-only n=5，与 seed42/43/44/45 配套。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:51:41.106Z\", \"updated_at\": \"2026-05-19T21:14:38.930Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 (Long) with seed47 establishes additional statistical sample (n→6) for baseline success rate estimation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 100, \"successful_rollouts\": 14, \"per_task\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0, \"put_both_cream_cheese_box_and_butter_in_basket\": 0, \"turn_on_stove_put_moka_pot\": 0.8, \"put_black_bowl_in_bottom_drawer\": 0, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.4, \"pick_up_book_place_in_caddy\": 0.1, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.1, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0, \"put_both_moka_pots_on_stove\": 0, \"put_yellow_white_mug_in_microwave\": 0}}, \"notes\": \"Cron false positive: eval 脚本无 W&B/sentinel，进程正常退出被误判 failed。实际已完成全部 10 tasks。SR=14.0%，与已有 seeds 一致 (mean~14.2%)。手动修正 conclusion=success。\"}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:32:48.207Z\", \"updated_at\": \"2026-05-19T20:58:56.479Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial with seed48 establishes additional statistical sample (n→6) for baseline success rate estimation.\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:32:44.897Z\", \"updated_at\": \"2026-05-19T20:53:05.054Z\", \"hypothesis\": \"CRM obs_only (trained on Object+Spatial) generalizes to LIBERO-Goal OOD benchmark with ε=0.2 norm constraint, providing meaningful action refinement despite distribution shift.\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:32:43.382Z\", \"updated_at\": \"2026-05-19T20:52:09.464Z\", \"hypothesis\": \"CRM obs_only (trained on Object+Spatial) generalizes to LIBERO-Goal OOD benchmark with ε=0.2 norm constraint, providing meaningful action refinement despite distribution shift.\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:31:14.902Z\", \"updated_at\": \"2026-05-19T20:10:50.847Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed45. 补齐 Goal suite 第 4 个 seed (n=4)，与 seed42/43/44-r2 配套。LIBERO-Goal 目标条件泛化 baseline。\", \"metrics\": {\"overall_success_rate\": 0.63, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.3, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.1, \"turn_on_the_stove\": 0.8, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.8}}, \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:05:08.765Z\", \"updated_at\": \"2026-05-19T20:08:19.990Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed46. 补齐 Goal suite n=5 数据，与 seed42/43/44/45 配套。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.71, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.6, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}, \"notes\": \"Cron false positive: eval completed normally (71.0%), but no W&B/sentinel → auto-resolved as failed. Manually corrected to success.\"}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:05:07.011Z\", \"updated_at\": \"2026-05-19T20:08:18.540Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed46. 补齐 Long suite n=5 数据，与 seed42/43/44/45 配套。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 0.9, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.5, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.1, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}, \"notes\": \"Cron false positive: eval completed normally (18.0%), but no W&B/sentinel → auto-resolved as failed. Manually corrected to success.\"}, \"fmvd-calibration-phase1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:57:05.859Z\", \"updated_at\": \"2026-05-19T20:07:21.125Z\", \"hypothesis\": \"FMVD (Flow Velocity Dispersion) signal validation: verify correlation between ODE velocity dispersion during K=1 denoising and K=10 action variance. Go/no-go gate for Adaptive K mechanism (Spearman ρ > 0.3).\", \"metrics\": {\"spearman_rho\": 0.082528, \"spearman_pvalue\": 2.33e-23, \"n_samples\": 14512, \"go_nogo\": \"NO-GO\", \"threshold\": 0.3, \"fmvd_mean\": 0.054867, \"fmvd_std\": 0.040291, \"fmvd_P25\": 0.027738, \"fmvd_P50\": 0.046693, \"fmvd_P75\": 0.070899, \"fmvd_P90\": 0.093805, \"k10_variance_mean\": 0.004888, \"k10_variance_std\": 0.005635, \"task_success_rate\": 0.06, \"n_tasks\": 10, \"n_episodes\": 50, \"n_successes\": 3}, \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:19.347Z\", \"updated_at\": \"2026-05-19T19:37:16.188Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.05 (当前 n=5)。timeout=16h。\", \"metrics\": {\"sr\": 0.17, \"sr_pct\": \"17.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.3, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:31:11.716Z\", \"updated_at\": \"2026-05-19T19:21:47.544Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed45. 补齐 Long suite 第 4 个 seed (n=4)，与 seed42/43/44 配套。LIBERO-10 长 horizon 任务 baseline。\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 1, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.2, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.2, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:24.175Z\", \"updated_at\": \"2026-05-19T19:05:12.052Z\", \"hypothesis\": \"perdof CRM with ε=0.03 (max_correction_norm) on LIBERO-Object seed47 tests whether a smaller correction magnitude improves or degrades task success rate compared to ε=0.05\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:21.800Z\", \"updated_at\": \"2026-05-19T19:05:09.001Z\", \"hypothesis\": \"perdof CRM with ε=0.05 (max_correction_norm) on LIBERO-Object seed47 provides per-DOF conformal refinement; this run supplements the magnitude curve at ε=0.05 (currently n=4)\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:39:55.593Z\", \"updated_at\": \"2026-05-19T18:38:52.937Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed44. 扩展到新 benchmark suite 验证 CRM 泛化性的前提——先建立 baseline。\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:39:49.327Z\", \"updated_at\": \"2026-05-19T18:38:48.009Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed42. 扩展到新 benchmark suite 验证 CRM 泛化性的前提——先建立 baseline。\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.1, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:39:52.159Z\", \"updated_at\": \"2026-05-19T18:33:56.305Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-10 seed43. 扩展到新 benchmark suite 验证 CRM 泛化性的前提——先建立 baseline。\", \"metrics\": {\"overall_success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.7, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.3, \"STUDY_SCENE1_book_caddy\": 0, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0.1, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.2}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:49:53.389Z\", \"updated_at\": \"2026-05-19T18:07:05.998Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:27:35.615Z\", \"updated_at\": \"2026-05-19T18:04:19.943Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed47. 补充 Spatial cross-seed 一致性数据。\", \"metrics\": {\"overall_success_rate\": 0.32, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.8, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0.1, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:42:56.456Z\", \"updated_at\": \"2026-05-19T17:47:10.111Z\", \"hypothesis\": \"Random selection baseline (K=10, randomly pick one of K VLA samples) seed46 on LIBERO-Object. Retry: r1 failed on bjb1-18228 (mode not supported), redeployed on bjb2-40593。审稿 C3。\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:27:33.151Z\", \"updated_at\": \"2026-05-19T17:24:14.391Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=10) on LIBERO-Spatial seed46. 补充 Spatial K=10 cross-benchmark 数据，当前 n=3 (seed42=35%, seed44=36%, seed45=34%)，扩展到 n=5 增强统计稳健性。\", \"conclusion\": \"failed\"}, \"eval-argmin-object-k5-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:21:11.529Z\", \"updated_at\": \"2026-05-19T17:24:12.993Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed44 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:40:03.921Z\", \"updated_at\": \"2026-05-19T17:08:52.675Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed44. LIBERO-Goal 使用相同初始状态不同目标，测试 VLA 对 goal-conditioned 任务的 baseline 表现。\", \"conclusion\": \"killed\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:30.944Z\", \"updated_at\": \"2026-05-19T16:31:13.969Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed45. K=5 decomposition 对照第四个 seed，与 argmin K=5 seed45 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-random-selection-object-k5-seed45\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.07, \"successes\": 7, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:29.373Z\", \"updated_at\": \"2026-05-19T16:31:10.982Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed44. K=5 decomposition 对照第三个 seed，与 argmin K=5 seed44 配对验证 selection effect 统计显著性。\", \"parent\": \"eval-random-selection-object-k5-seed44\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:27.994Z\", \"updated_at\": \"2026-05-19T16:31:08.997Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed43. 第二个 seed 的 K=5 random selection，与 argmin K=5 seed43 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-random-selection-object-k5-seed43\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"successes\": 11, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:26.607Z\", \"updated_at\": \"2026-05-19T16:31:06.453Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed42. 从 K=5 VLA samples 中随机选 1 个执行（不用 argmin/CRM）。验证 K=5 decomposition 中 selection effect 是否真实：如果 random ≈ argmin (13.7%)，则 selection effect 不显著；如果 random < argmin，则 argmin 的选择能力在小候选池中有真实价值。\", \"parent\": \"eval-random-selection-object-k5-seed42\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"successes\": 14, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:32.306Z\", \"updated_at\": \"2026-05-19T16:30:37.908Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"parent\": \"eval-obs-only-spatial-norm02-k5-seed44\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.37, \"successes\": 37, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:30:33.621Z\", \"updated_at\": \"2026-05-19T16:30:18.549Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"parent\": \"eval-obs-only-spatial-norm02-k5-seed45\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_bowl_between_plate_ramekin\": 0.9, \"pick_up_bowl_next_to_ramekin\": 1, \"pick_up_bowl_from_table_center\": 0, \"pick_up_bowl_on_cookie_box\": 0.3, \"pick_up_bowl_in_top_drawer\": 0.1, \"pick_up_bowl_on_ramekin\": 0, \"pick_up_bowl_next_to_cookie_box\": 0.9, \"pick_up_bowl_on_stove\": 0, \"pick_up_bowl_next_to_plate\": 0.2, \"pick_up_bowl_on_wooden_cabinet\": 0}}}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T16:13:57.251Z\", \"updated_at\": \"2026-05-19T16:17:38.007Z\", \"hypothesis\": \"Latency profiling: 正式测量 VLA+CRM pipeline 各组件 wall-clock time，覆盖 K=1/5/10/20 batched vs sequential，生成论文 Table 级结果。预期 CRM overhead < 1ms，pipeline 主要 bottleneck 在 VLA flow-matching sampling。\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_ms\": 28.4, \"crm_forward_ms\": 0.246, \"preprocess_ms\": 0.96, \"batched_K1_ms\": 180, \"batched_K5_ms\": 182.3, \"batched_K10_ms\": 162.3, \"batched_K20_ms\": 167.4, \"sequential_K1_ms\": 177, \"sequential_K5_ms\": 891.7, \"sequential_K10_ms\": 1638.9, \"sequential_K20_ms\": 3245.8, \"cgs_K10_ms\": 6.3, \"full_pipe_K10_ms\": 200.7, \"full_pipe_K20_ms\": 199.7, \"vla_model_mb\": 884.1, \"crm_model_mb\": 1.8, \"peak_K20_mb\": 1085.1}}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:24:47.682Z\", \"updated_at\": \"2026-05-19T16:06:09.222Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed45. Spatial benchmark 第四个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\", \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:50:49.193Z\", \"updated_at\": \"2026-05-19T16:06:07.907Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve perdof ε=0.05 (当前 n=2)。timeout=16h。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"sr_pct\": \"10%\"}}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:24:44.727Z\", \"updated_at\": \"2026-05-19T15:30:01.540Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed44. Spatial benchmark 第三个 VLA-only seed，配合 obs_only spatial seeds 报告 CRM 改进幅度。\", \"metrics\": {\"success_rate\": 0.31, \"successes\": 31, \"total\": 100, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.6, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T14:27:30.715Z\", \"updated_at\": \"2026-05-19T15:26:45.368Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed44. K=20 第三个 seed，n=3 可报告 error bars，确认 K-value diminishing returns。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T14:27:28.230Z\", \"updated_at\": \"2026-05-19T15:26:42.621Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed43. K=20 第二个 seed，与 K=10 seed43 配对，增强 K-value curve K=20 端的统计可靠性。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-17T13:34:42.612Z\", \"updated_at\": \"2026-05-19T15:26:40.749Z\", \"hypothesis\": \"CRM obs_only (ε=0.2, K=20) on LIBERO-Object seed42. 扩展 K-value curve 到 K=20，验证收益曲线在 K=10→K=20 段是否趋平（预期 ≤+1pp over K=10 的 17.6%）。用 K=10 训练的 CRM 模型，eval 时生成 20 个 VLA 样本。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:50:51.880Z\", \"updated_at\": \"2026-05-19T14:58:17.531Z\", \"hypothesis\": \"obs_only CRM (ε=default/unlimited) seed48 on LIBERO-Object. 补 obs_only default (当前 n=3)。timeout=16h。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"notes\": \"误判 failed: cron 检测到 tmux session 死亡，但实验已正常完成并写入完整 JSON。手动验证 output JSON 完整（59 行，10 tasks × 10 rollouts）。success_rate=0.17，与原 seed48 (bjb2-28827) 一致。\"}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:01:28.636Z\", \"updated_at\": \"2026-05-19T14:43:19.646Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed43. P1 缺口：与 Spatial K=5 CRM seed43=32% 配对，计算 per-seed improvement。没有此 baseline 无法报告 Spatial 改进幅度。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.29, \"successes\": 29, \"total\": 100, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.8, \"from_table_center\": 0.1, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}}}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T12:55:51.909Z\", \"updated_at\": \"2026-05-19T14:38:29.599Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed42. P1 缺口：Spatial benchmark 需要 VLA-only baseline 才能报告 CRM 的改进幅度。对标 obs_only spatial K=10 seed42=35%。\", \"metrics\": {\"success_rate\": 0.3, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:00:40.507Z\", \"updated_at\": \"2026-05-19T14:32:21.490Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:00:39.233Z\", \"updated_at\": \"2026-05-19T14:32:16.468Z\", \"hypothesis\": \"CRM obs-only with K=5 conformal refinement steps and max_correction_norm=0.2 will improve SmolVLA spatial task success rate compared to baseline, though potentially less than K=10 due to fewer correction iterations.\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:00:37.093Z\", \"updated_at\": \"2026-05-19T14:32:11.343Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed45. K=5 decomposition 对照第四个 seed，与 argmin K=5 seed45 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-argmin-object-k5-seed45\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:00:34.934Z\", \"updated_at\": \"2026-05-19T14:32:06.313Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed44. K=5 decomposition 对照第三个 seed，与 argmin K=5 seed44 配对验证 selection effect 统计显著性。\", \"parent\": \"eval-argmin-object-k5-seed44\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:57:11.028Z\", \"updated_at\": \"2026-05-19T14:32:01.561Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed43. 第二个 seed 的 K=5 random selection，与 argmin K=5 seed43 (13%) 配对，增强 selection effect 统计可靠性。\", \"parent\": \"eval-argmin-object-k5-seed43\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:43:11.414Z\", \"updated_at\": \"2026-05-19T14:31:56.882Z\", \"hypothesis\": \"Random selection baseline with K=5 on LIBERO-Object seed42. 从 K=5 VLA samples 中随机选 1 个执行（不用 argmin/CRM）。验证 K=5 decomposition 中 selection effect 是否真实：如果 random ≈ argmin (13.7%)，则 selection effect 不显著；如果 random < argmin，则 argmin 的选择能力在小候选池中有真实价值。\", \"parent\": \"eval-argmin-object-k5-seed42\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:49:54.536Z\", \"updated_at\": \"2026-05-19T14:26:11.536Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:56:02.708Z\", \"updated_at\": \"2026-05-19T14:25:56.640Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed47 on LIBERO-Object. Retry with 16h timeout (r1 killed on bjb1-18228). C2 magnitude curve ε=0.03 端当前 n=1 (seed42=16%), 需 n≥3 才有 error bars。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 12:58 UTC: FALSE ALARM — cron 检测到旧进程 EXIT_CODE=129(被 kill 的重复进程 PID 892663)，误标为 failed。实际进程 PID 894900 仍在 bjb1-32546 GPU 3 正常运行，5/10 tasks 完成 (T1=0%, T2=0%, T3=20%, T4=30%, T5=0%)。已恢复 RUNNING。\", \"metrics\": {\"success_rate\": 0.15, \"successes\": 15, \"total\": 100}}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:56:04.999Z\", \"updated_at\": \"2026-05-19T14:00:43.326Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed48 on LIBERO-Object. 新 seed, 16h timeout。C2 magnitude curve ε=0.03 端当前 n=1 (seed42=16%), 需 n≥3 才有 error bars。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 12:58 UTC: FALSE ALARM 确认 — PID 67825 在 bjb1-18228 GPU 1 正常运行中。已完成 5/10 tasks + T6 进行中 (T1=0%, T2=0%, T3=20%, T4=40%, T5=0%, T6 doing 5/10=1/5)。conclusion=failed 为误标(cron 误报)，无法设 null。\", \"metrics\": {\"success_rate\": 0.15, \"successes\": 15, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 2, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 0, \"milk\": 2, \"chocolate_pudding\": 4, \"orange_juice\": 2}}}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T01:29:55.249Z\", \"updated_at\": \"2026-05-19T13:39:15.552Z\", \"metrics\": {\"sr\": 0.12, \"sr_pct\": \"12%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"hypothesis\": \"per-DoF CRM with max_correction_norm=0.1 on LIBERO-Object (seed43, K=10, n_rollouts=10) should achieve comparable SR to obs_only default, as tighter norm constraint limits correction magnitude per joint.\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:05:53.834Z\", \"updated_at\": \"2026-05-19T13:35:23.895Z\", \"hypothesis\": \"obs_only CRM uncapped (default norm ~1.42) seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=12%)，需标准化。obs_only default 当前 n=3 (seed42/43/44)。\", \"parent\": \"eval-obs-only-object-default-seed45\", \"metrics\": {\"sr\": 0.18, \"sr_pct\": \"18%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:08:30.602Z\", \"updated_at\": \"2026-05-19T13:30:16.050Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed42 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.15, \"sr_pct\": \"15%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:36:13.145Z\", \"updated_at\": \"2026-05-19T13:26:50.930Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed45 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:08:15.812Z\", \"updated_at\": \"2026-05-19T13:26:46.918Z\", \"hypothesis\": \"K=5 argmin-only baseline (reconvla mode) seed43 on LIBERO-Object. D066 K=5 decomposition: isolate selection-only benefit from CRM correction.\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:18:03.763Z\", \"updated_at\": \"2026-05-19T13:24:40.192Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed43 on LIBERO-Object. 补 magnitude curve：perdof ε=0.3 当前 n=3 (seed42:4%, seed44:4%, seed45:6%)，mean=4.67%。增加第 4 个 seed 强化 error bars。\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 5, \"sr_pct\": \"5%\", \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:49:55.654Z\", \"updated_at\": \"2026-05-19T13:12:13.645Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO-Spatial seed45. 审稿 M2: 验证 CRM 在 Spatial benchmark 上的跨 seed 一致性。CRM 已覆盖 Spatial 训练数据（all 20 LIBERO tasks）。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 34}}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:09:01.117Z\", \"updated_at\": \"2026-05-19T12:59:25.958Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed44 on LIBERO-Object (bjb2-28827). 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)。另一份 seed44 在 bjb1-32546 同时运行。\", \"conclusion\": \"success\", \"notes\": \"2026-05-19 21:00 UTC: 实验实际成功完成。JSON 输出在 /root/logs/eval_object_obs_only_norm003_seed44.json (注意：路径是 /root/logs/ 而非 /root/acr-vla-conformal-refinement/logs/)。10/10 tasks 全部完成，overall SR=17% (17/100)。误标 failed 原因：startup recovery 发现 RUNNING 状态无 cron 监控和 PID 信息，自动标记为 failed。\"}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:40:51.279Z\", \"updated_at\": \"2026-05-19T12:48:29.290Z\", \"conclusion\": \"success\", \"hypothesis\": \"K=1 CRM full training with multi-stage VLA feature fusion + composite loss (L2 + contrastive + uncertainty-weighted) on full object benchmark dataset. Scaled-up version of train-crm-k1-accg-object-seed42-v2 with complete training data.\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:11:43.484Z\", \"updated_at\": \"2026-05-19T12:48:27.021Z\", \"conclusion\": \"success\", \"hypothesis\": \"K=1 spatial benchmark precomputation: generate single-sample VLA action predictions and features for CRM K=1 training. Required preprocessing step before K=1 CRM can be trained on spatial tasks.\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:04:14.203Z\", \"updated_at\": \"2026-05-19T12:48:10.176Z\", \"hypothesis\": \"K=1 CRM 训练：使用多阶段 VLA 特征融合 + 组合损失函数（L2 + contrastive + uncertainty-weighted），训练专门用于 K=1 单采样纠正的 CRM 模型。目标是超越 K=1 VLA-only baseline (10.8%)。\", \"conclusion\": \"success\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:59:53.216Z\", \"updated_at\": \"2026-05-19T12:48:06.312Z\", \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.3 至 n=7。\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 16}}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:59:51.090Z\", \"updated_at\": \"2026-05-19T12:48:03.869Z\", \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed48 on LIBERO-Object. 补 magnitude curve obs_only ε=0.1 至 n=7。\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 18}}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:56:16.472Z\", \"updated_at\": \"2026-05-19T12:48:01.446Z\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks r3 rerun. Second reproduction of LTO baseline SR=14%. Confirms v2 result consistency.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:55:29.003Z\", \"updated_at\": \"2026-05-19T12:47:58.882Z\", \"hypothesis\": \"VLA-only baseline on 5 held-out tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Bugfix r2: removed .replace(\\\"_\\\",\\\" \\\") that caused 3/5 task matching failures.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:55:26.507Z\", \"updated_at\": \"2026-05-19T12:47:56.312Z\", \"hypothesis\": \"LTO split-A CRM (K=5, ε=0.2, obs_only) on 5 held-out tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Bugfix r2: removed .replace(\\\"_\\\",\\\" \\\") that caused 3/5 task matching failures.\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:13:30.382Z\", \"updated_at\": \"2026-05-19T12:47:52.436Z\", \"conclusion\": \"success\", \"hypothesis\": \"LTO Split A CRM training (obs_only, 5 tasks, task_indices 0-4). Predecessor to eval-lto-splitA-heldout experiments. Superseded by crm-lto-splitA-train-fixed (task_names matching).\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:31:15.780Z\", \"updated_at\": \"2026-05-19T12:23:18.801Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.03) seed48 on LIBERO-Object. 补 magnitude curve 最薄点 perdof ε=0.03 (当前 n=1)。timeout=16h。\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T12:22:25.439Z\", \"updated_at\": \"2026-05-19T11:45:28.182Z\", \"hypothesis\": \"Scalar CRM seed45 rerun with n_rollouts=10 for consistency. Original seed45 used n_rollouts=20. Current scalar: [9,10,6,9] mean=8.5%\", \"parent\": \"eval-scalar-object-seed45\", \"metrics\": {\"overall_success_rate\": 0.07, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:08:33.036Z\", \"updated_at\": \"2026-05-19T11:34:16.077Z\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark generalization claim.\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:04:44.384Z\", \"updated_at\": \"2026-05-19T11:34:12.397Z\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed48 on LIBERO-Object. D066 K=5 primary configuration 补种到 n=7 统计力度增强。\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:08:18.656Z\", \"updated_at\": \"2026-05-19T11:31:39.191Z\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. D066 K=5 Spatial multi-benchmark evidence for cross-benchmark generalization claim.\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:29:24.718Z\", \"updated_at\": \"2026-05-19T11:30:55.300Z\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed46 on LIBERO-Object. 补 K=5 primary configuration 到 n≥5。D066 统计力度增强。\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:19:21.005Z\", \"updated_at\": \"2026-05-19T11:30:43.198Z\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Control group for Leave-Task-Out Split A eval. Retry after .replace task matching bug fix.\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}, \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:19:18.968Z\", \"updated_at\": \"2026-05-19T11:30:33.951Z\", \"hypothesis\": \"Leave-Task-Out generalization: CRM trained on Split A (5 tasks) evaluated on held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). K=5 ε=0.2. Retry after .replace task matching bug fix.\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}, \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:44.467Z\", \"updated_at\": \"2026-05-19T11:30:18.282Z\", \"hypothesis\": \"Per-DoF CRM (ε=default/unlimited) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束, success_rate=0%\"}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:47.310Z\", \"updated_at\": \"2026-05-19T11:30:17.012Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.05, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:41.596Z\", \"updated_at\": \"2026-05-19T11:30:15.785Z\", \"hypothesis\": \"Obs-only CRM (ε=default/unlimited) seed48 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:35.770Z\", \"updated_at\": \"2026-05-19T11:30:14.493Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.03) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-19T11:29:18.036Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:15:14.634Z\", \"updated_at\": \"2026-05-19T11:28:09.358Z\", \"hypothesis\": \"perdof CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 薄数据点：perdof ε=0.03 当前 n=1 (seed42=14%)，seed43/44 已在跑。验证 per-DOF correction 在极低 norm 下表现。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:50:34.507Z\", \"updated_at\": \"2026-05-19T11:28:00.648Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed46 on LIBERO-Object. GPU 双跑补 magnitude curve 最薄点 ε=0.03。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:29:27.251Z\", \"updated_at\": \"2026-05-19T11:27:53.132Z\", \"hypothesis\": \"K=5 obs_only CRM (ε=0.2) seed47 on LIBERO-Object. 补 K=5 primary configuration 到 n≥6。D066 统计力度增强。\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:32.629Z\", \"updated_at\": \"2026-05-19T11:27:25.914Z\", \"hypothesis\": \"Random selection baseline seed45 on LIBERO-Object. GPU 双跑补 seed。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:14:06.226Z\", \"updated_at\": \"2026-05-19T11:27:24.704Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:57:04.076Z\", \"updated_at\": \"2026-05-19T11:25:28.189Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.1) seed48 on LIBERO-Object. 补 perdof ε=0.1 至 n=7，替代被 kill 的 obs_only_norm03_seed46 重复实验的 GPU slot。\", \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-19T11:25:18.480Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-19T11:25:13.541Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-19T11:25:11.008Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-19T11:25:07.860Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-19T11:25:01.605Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:45:20.860Z\", \"updated_at\": \"2026-05-19T05:16:04.086Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed43 on LIBERO-Object. Retry after r1 timed out. 补 magnitude curve 最薄点 ε=0.03。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:44:44.161Z\", \"updated_at\": \"2026-05-19T05:16:02.877Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. Retry with timeout=16h after r1 timed out. 补 magnitude curve 最薄点 ε=0.03。\", \"conclusion\": \"killed\", \"metrics\": {\"partial\": true, \"tasks_completed\": \"5/10\", \"task6_partial\": \"5/10 rollouts\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0}, \"partial_avg_sr\": 0.1, \"failure_mode\": \"process killed silently mid-eval, no error in log, no JSON output\"}}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:35:02.089Z\", \"updated_at\": \"2026-05-19T05:13:20.212Z\", \"conclusion\": \"killed\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Control group for Leave-Task-Out Split A eval.\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:34:59.607Z\", \"updated_at\": \"2026-05-19T05:13:18.481Z\", \"conclusion\": \"killed\", \"hypothesis\": \"Leave-Task-Out generalization: CRM trained on Split A (5 tasks) evaluated on held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). K=5 ε=0.2. If SR > VLA-only on held-out tasks, CRM generalizes beyond training distribution.\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:05:51.040Z\", \"updated_at\": \"2026-05-19T05:02:02.994Z\", \"hypothesis\": \"obs_only CRM ε=0.1 seed45 重跑 n_rollouts=10。原始 seed45 用 n_rollouts=20 (SR=14%)，需标准化到 n_rollouts=10 与其他 seed 一致。当前 obs_only ε=0.1 有 5 seeds。\", \"parent\": \"eval-obs-only-object-norm01-seed45\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:53:33.612Z\", \"updated_at\": \"2026-05-19T04:58:44.483Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 obs_only ε=0.05 seed (n=4→5)。\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:15:14.835Z\", \"updated_at\": \"2026-05-19T04:58:40.993Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed48 on LIBERO-Object. 补 perdof ε=0.3 至 n=7。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:09:03.172Z\", \"updated_at\": \"2026-05-19T04:58:36.864Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed49 on LIBERO-Object. 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)，第 6 个 seed 确保极低 norm 端统计可靠。\", \"conclusion\": \"killed\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:27:23.594Z\", \"updated_at\": \"2026-05-19T04:32:49.103Z\", \"conclusion\": \"success\", \"hypothesis\": \"Leave-Task-Out Split A: CRM (obs_only) trained on 5 tasks (alphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, 7499 samples) can generalize to held-out 5 tasks. Uses task_names string matching.\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:15:10.585Z\", \"updated_at\": \"2026-05-19T04:32:33.294Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed47 on LIBERO-Object. 补 magnitude curve ε=0.03 至 n=6。\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:05:55.304Z\", \"updated_at\": \"2026-05-19T03:28:52.476Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed43 on LIBERO-Object。magnitude curve 低 ε 端当前只有 seed42 (14%, n=1)，第二个 seed 增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:27:51.549Z\", \"updated_at\": \"2026-05-19T02:56:00.676Z\", \"hypothesis\": \"perdof CRM ε=0.05 seed43 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.05 当前只有 seed42 (14%, n=1)，第二个 seed 增强统计可靠性。\", \"parent\": \"eval-mag-perdof-norm005-object\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T06:17:50.362Z\", \"updated_at\": \"2026-05-19T01:44:05.704Z\", \"hypothesis\": \"Perdof CRM without norm clipping (uncapped, actual norm ~1.42) causes catastrophic collapse on LIBERO-Object. seed42=0%, seed46=0%, seed44=0% (partial). seed43 confirms cross-seed consistency of collapse.\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:50:36.635Z\", \"updated_at\": \"2026-05-19T01:42:33.925Z\", \"hypothesis\": \"Random selection baseline (K=10, randomly pick one of K VLA samples) seed46 on LIBERO-Object. 补审稿 C3 要求的 random selection baseline 额外 seed。\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:33:11.557Z\", \"updated_at\": \"2026-05-19T01:40:59.658Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed48 on LIBERO-Object. Retry after killed previous attempt. Supplements primary result (seed42-47 done, this extends to seed48).\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:21:08.043Z\", \"updated_at\": \"2026-05-19T01:38:34.712Z\", \"hypothesis\": \"Perdof CRM without norm clipping (uncapped, actual norm ~1.42) causes catastrophic collapse on LIBERO-Object. seed42=0%, seed46=0%, seed44=0% (partial). seed45 confirms cross-seed consistency of collapse.\", \"parent\": \"crm-train-v2-perdof\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:32:38.704Z\", \"updated_at\": \"2026-05-19T01:33:59.345Z\", \"hypothesis\": \"Obs-only CRM (ε=0.2, K=5) seed45 on LIBERO-Object. GPU 双跑补 seed。\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:31:32.794Z\", \"updated_at\": \"2026-05-19T01:33:32.294Z\", \"hypothesis\": \"VLA-only baseline seed46 on LIBERO-Object. 第 5 个 VLA-only seed 补全 baseline。\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:02:39.518Z\", \"updated_at\": \"2026-05-19T01:32:13.545Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed48 on LIBERO-Object. 补 obs_only ε=0.1 至 n=7。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:50:46.149Z\", \"updated_at\": \"2026-05-18T21:55:07.741Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed45 on LIBERO-Object. 补 magnitude curve：perdof ε=0.05 当前 n=2 (seed42=14%, seed44=9%), seed43 在跑。第 4 个 seed 强化低 ε 端 error bars。\", \"conclusion\": \"failed\", \"notes\": \"失败原因: EXIT_CODE=124 timeout (wall_clock=6.03h, timeout_hours 过低) | 已知失败模式: LIBERO-Object 全量 eval 需 12-14h，6h timeout 不够 | 建议: 重提交 timeout_hours=16\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:15:11.377Z\", \"updated_at\": \"2026-05-18T21:22:07.054Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed44 on LIBERO-Object. 补 magnitude curve 最薄数据点：obs_only ε=0.03 当前 n=1 (seed42=16%)，需多 seed 确认极低 norm 下 obs_only 稳定性。\", \"conclusion\": \"failed\", \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:16:07.852Z\", \"updated_at\": \"2026-05-18T21:22:04.804Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 最薄数据点：obs_only ε=0.03 当前 n=1，seed43/44 已在跑。第 4 个 seed 确保极低 norm 端有可靠 error bars。\", \"conclusion\": \"failed\", \"notes\": \"失败原因: timeout (EXIT_CODE=124), 运行 ~6h 后在 task 5/10 rollout 5/10 处被杀。实验正常运行无报错，timeout_hours 设置过低（需 ~12-14h 完成全部 10 tasks × 10 rollouts）。部分结果: task1=0%, task2=0%, task3=20%, task4=30%（4个task完成）。建议: 重提交并将 timeout_hours 提高至 15h+\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:27:12.596Z\", \"updated_at\": \"2026-05-18T21:05:50.448Z\", \"hypothesis\": \"obs_only CRM K=5 ε=0.2 seed44. Third seed for K-value curve (seed42=14%, seed43=19%, mean=16.5%). Variance 大 (5pp gap), 第三个 seed 对 K-value scaling narrative 至关重要。\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-18T20:39:58.647Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed43 on LIBERO-Object. plan_500 低 norm 补数据：seed42 ε=0.03=16%。多 seed 确认 obs_only 在极低 correction norm 下仍稳定。\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T02:25:56.030Z\", \"updated_at\": \"2026-05-18T19:54:45.657Z\", \"hypothesis\": \"Random selection baseline (K=10 随机选一个 action) seed44 on LIBERO-Object. 第三个 seed 验证 random selection ≈ VLA-only。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:31:41.748Z\", \"updated_at\": \"2026-05-18T19:14:55.968Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed44 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.03 当前 seed42=14% (n=1)，seed43 已在跑。重试 r2 修正 python 路径。\", \"parent\": \"eval-perdof-object-norm003-seed44\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-17T23:53:01.705Z\", \"updated_at\": \"2026-05-18T18:53:10.563Z\", \"hypothesis\": \"perdof CRM with ε=0.1 on LIBERO-Object seed42. Magnitude curve comparison point for perdof variant.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-17T23:53:00.645Z\", \"updated_at\": \"2026-05-18T18:53:09.494Z\", \"hypothesis\": \"obs_only CRM with ε=0.1 on LIBERO-Object seed42. Intermediate norm point for magnitude curve.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:33:39.698Z\", \"updated_at\": \"2026-05-18T16:48:10.654Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed46 on LIBERO-Object. Retry r3. Supplements magnitude curve ε=0.1 data. seed42=19%, seed43=12%, seed44=16%, seed45=14%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:33:08.510Z\", \"updated_at\": \"2026-05-18T16:48:08.690Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed45 on LIBERO-Object. Supplements magnitude curve low-norm data. seed42=13%, seed43=14%.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:10:52.130Z\", \"updated_at\": \"2026-05-18T15:50:02.402Z\", \"hypothesis\": \"Random selection baseline (K=10 随机选一个 action) seed43 on LIBERO-Object. 多 seed 验证 CRM selection > random。seed42 RUNNING 中。\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:31:56.813Z\", \"updated_at\": \"2026-05-18T15:18:13.193Z\", \"hypothesis\": \"perdof CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段 perdof 数据。与 obs_only norm005 seed44 配对对比。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T11:44:42.438Z\", \"updated_at\": \"2026-05-18T14:17:30.462Z\", \"hypothesis\": \"VLA-only baseline seed45 rerun with n_rollouts=10 for consistency. Original seed45 used n_rollouts=20. Current VLA-only: [12,12,10,9,13] mean=11.2%\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.3, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:27:53.154Z\", \"updated_at\": \"2026-05-18T13:31:57.990Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed44 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.03 当前 seed42=14% (n=1)，seed43 已在跑。第三个 seed 进一步增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"conclusion\": \"failed\", \"notes\": \"EXIT_CODE=127, python not found. bjb1-18228 需用 /root/miniconda3/bin/python 而非 bare python.\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:02:40.444Z\", \"updated_at\": \"2026-05-18T13:27:03.418Z\", \"hypothesis\": \"obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补充 magnitude curve high-norm 段 seed48 数据。扩展 error bars。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:10:56.103Z\", \"updated_at\": \"2026-05-18T13:07:06.200Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段数据。seed42=13%, seed43 running。\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T04:37:18.401Z\", \"updated_at\": \"2026-05-18T12:39:30.555Z\", \"hypothesis\": \"obs_only CRM K=5 ε=0.2 seed43. Second seed for K-value curve (seed42=14%). Director highest priority.\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T02:32:26.297Z\", \"updated_at\": \"2026-05-18T12:33:45.335Z\", \"hypothesis\": \"perdof CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-perdof-object-norm01-seed42. PID 497642 on cuda:3, started 07:52 UTC.\", \"parent\": \"eval-perdof-object-norm01-seed42\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T02:32:25.342Z\", \"updated_at\": \"2026-05-18T12:33:41.666Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-obs-only-object-norm01-seed42. PID 497445 on cuda:1, started 07:52 UTC.\", \"parent\": \"eval-obs-only-object-norm01-seed42\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:30.506Z\", \"updated_at\": \"2026-05-18T12:20:08.756Z\", \"hypothesis\": \"Random selection baseline (K=10 随机选一个 action) on LIBERO-Object seed42. Ablation 验证 CRM uncertainty-guided selection 的价值。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0.1, 0.1, 0.4, 0, 0.2, 0, 0.1, 0.2, 0.2]}}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:36:46.839Z\", \"updated_at\": \"2026-05-18T10:56:45.558Z\", \"hypothesis\": \"Perdof CRM with norm clipping ε=0.2 provides controlled corrections that preserve baseline policy behavior on LIBERO-Object. Expected SR ~10% (similar to other seeds 42/44/45/46/47 at 9-12%).\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:19.181Z\", \"updated_at\": \"2026-05-18T07:05:38.605Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=46 on LIBERO Object. Extends perdof low-norm data (seed42=11%, seed44/45 running). At ε=0.1 perdof is in its \\\"safe zone\\\" (tight bound masks noisy corrections). Paired with obs_only seed46 for direct comparison at same seed.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T09:01:52.970Z\", \"updated_at\": \"2026-05-18T07:05:03.603Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=45 on LIBERO Object. 验证 obs_only 在低 norm (0.1) 的稳定性。seed42 在 0.1 为 19%，如果一致则确认 obs_only 全 norm 范围鲁棒。\", \"conclusion\": \"success\", \"notes\": \"PID 474319 died, GPU idle 28h+. Ghost experiment — process dead but registry not updated.\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:34:40.971Z\", \"updated_at\": \"2026-05-18T07:05:02.646Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=5) seed42 on LIBERO-Object. K sweep 实验：K=5 vs K=10 (22%) 比较，验证 sample count 对 selection quality 的影响。若 K=5 显著低于 K=10，说明足够的 candidate 多样性对 CRM selection 关键。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:21:54.338Z\", \"updated_at\": \"2026-05-18T07:05:01.672Z\", \"hypothesis\": \"perdof CRM (default norm, 无裁剪) seed46 on LIBERO-Object. 验证 perdof 在 uncapped norm 下的灾难性崩溃（seed42=0%）是否跨 seed 一致。支撑 obs_only > perdof claim。\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:18:01.200Z\", \"updated_at\": \"2026-05-18T06:19:59.229Z\", \"hypothesis\": \"perdof CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 perdof 在 uncapped norm 下的 catastrophic collapse（seed42=0%）。为 magnitude curve 提供第二个 seed 的 default 数据点。\", \"notes\": \"Timeout (EXIT_CODE=124, 24h) but partial results conclusive: 0/90 rollouts = 0% SR across 9/10 tasks. Task 10 not started. Confirms catastrophic collapse at unclipped norm, consistent with seed42=0%. Every rollout hit max_steps=300 (agent unable to complete any task), causing the timeout.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Partial 9/10 tasks, 0/90 rollouts. Accepted as collapse evidence per Director decision 2026-05-18.\"}}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:13.281Z\", \"updated_at\": \"2026-05-18T05:54:22.364Z\", \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"conclusion\": \"killed\", \"hypothesis\": \"Per-DoF CRM with max_correction_norm=0.2 on LIBERO-Spatial achieves optimal balance between correction magnitude and stability — norm=0.2 is hypothesized sweet spot from obs-only results\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:15:49.209Z\", \"updated_at\": \"2026-05-18T05:54:21.341Z\", \"hypothesis\": \"D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.\", \"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"notes\": \"[2026-05-15] HUNG: 3/10 tasks done (56.7%, 17/30), stuck on task 4 env init for 8+ hours. Process alive (pid 288939, GPU 1450 MiB) but zero log progress. Needs kill+restart.\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:00.358Z\", \"updated_at\": \"2026-05-18T05:54:20.300Z\", \"hypothesis\": \"D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization.\", \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env init hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。7/10 tasks 完成，42.9% SR (30/70)。需重跑 tasks 8-10（或全部重跑）。\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:16:06.636Z\", \"updated_at\": \"2026-05-18T05:54:19.300Z\", \"hypothesis\": \"D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。6/10 tasks 完成 + task 7 部分（5/10 rollouts），40.0% SR (24/60)。需重跑。\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-18T05:54:18.227Z\", \"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"notes\": \"[2026-05-15] HUNG: 9/10 tasks done (36.7%, 33/90), stuck on task 10 env init for 8+ hours. Process alive (pid 231426, GPU 1414 MiB) but zero log progress. Needs kill+restart.\", \"conclusion\": \"killed\", \"hypothesis\": \"Argmin-only selection (K=10, pick lowest CRM score without correction) on LIBERO-Spatial tests whether selection alone provides benefit — isolating the selection mechanism from the correction mechanism\", \"parent\": \"eval-reconvla-spatial-v3\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:06.073Z\", \"updated_at\": \"2026-05-18T05:54:17.209Z\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"success\", \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection) on LIBERO-Spatial improves over VLA-only baseline, validating that conformal selection generalizes across spatial reasoning tasks\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:13.095Z\", \"updated_at\": \"2026-05-18T05:54:16.171Z\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"negative\", \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection with scalar uncertainty) on LIBERO-Object improves over VLA-only baseline by selecting highest-confidence action from candidate set\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:56:51.046Z\", \"updated_at\": \"2026-05-18T05:54:15.084Z\", \"hypothesis\": \"OpenVLA 7B VLA-only baseline on LIBERO-Object. 0% SR due to transformers 5.8 DynamicCache bug. Fix: use official repo eval code with transformers 4.40.1 in isolated conda env. Dry-run verified 80% SR on libero_spatial. Awaiting GPU for full LIBERO-Object eval.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 100, \"avg_inference_time_ms\": 178, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0}}, \"notes\": \"NEEDS INVESTIGATION: 0% success rate vs OpenVLA paper 88.4% (LIBERO-Object). 100% confirmed code bug. Suspected action tokenization/detokenization or unnormalize issue. Do NOT treat as valid baseline.\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:28.585Z\", \"updated_at\": \"2026-05-18T04:37:10.886Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed47. Magnitude curve data point for perdof at primary comparison norm.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T23:05:21.870Z\", \"updated_at\": \"2026-05-18T03:04:35.124Z\", \"hypothesis\": \"obs_only CRM ε=0.2 seed48. Key data point at primary comparison norm.\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:21:52.326Z\", \"updated_at\": \"2026-05-18T03:03:50.286Z\", \"hypothesis\": \"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T10:54:38.275Z\", \"updated_at\": \"2026-05-18T02:24:22.787Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed46. Magnitude curve data point for perdof variant at primary comparison norm.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:13.356Z\", \"updated_at\": \"2026-05-18T01:01:03.202Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=46 on LIBERO Object. Extends magnitude curve low-norm segment to 3+ seeds. If consistent with seed42=19% and seed45 (running), strengthens robustness claim that obs_only maintains stable performance across all ε values.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:27.742Z\", \"updated_at\": \"2026-05-18T00:42:42.174Z\", \"hypothesis\": \"obs_only CRM with ε=0.05 on LIBERO-Object seed43. Retry (r2) for magnitude curve low-norm data point.\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed46-r2\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-17T07:05:18.047Z\", \"updated_at\": \"2026-05-18T00:33:26.447Z\", \"hypothesis\": \"obs_only CRM with ε=0.1 on LIBERO-Object seed46. Retry after previous run was killed at task 5/10.\", \"conclusion\": \"killed\", \"notes\": \"Retry #2: relaunched on bjb1-32546 cuda:3, PID 562396, tmux session eval-obs-only-object-norm01-seed46-r2. Previous run killed at task 5/10 on bjb1-18228.\"}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:04:31.864Z\", \"updated_at\": \"2026-05-17T23:47:05.521Z\", \"conclusion\": \"killed\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:04:34.999Z\", \"updated_at\": \"2026-05-17T23:47:03.765Z\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T12:04:16.681Z\", \"updated_at\": \"2026-05-17T23:17:06.378Z\", \"hypothesis\": \"perdof CRM ε=0.2 seed43 on LIBERO-Object. 第 3 次尝试。补充 perdof magnitude curve ε=0.2 数据（seed42=11%）。\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100}}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:04:37.024Z\", \"updated_at\": \"2026-05-17T23:10:07.386Z\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T10:27:16.189Z\", \"updated_at\": \"2026-05-17T23:00:33.671Z\", \"hypothesis\": \"Duplicate of perdof norm=0.1 seed47 on bjb1-32546 (deployed by orphan Worker). Also running on bjb2-40593.\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T20:06:55.243Z\", \"updated_at\": \"2026-05-17T22:39:25.302Z\", \"hypothesis\": \"OpenVLA 7B finetuned VLA-only baseline on LIBERO-Object using official eval code (transformers 4.40.1, isolated conda env). v1 failed due to transformers 5.8 DynamicCache bug. Dry-run on libero_spatial confirmed 80% SR. This run uses openvla-libero-object finetuned model with 10 trials/task.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.69, \"n_tasks\": 10, \"n_trials_per_task\": 10, \"total_rollouts\": 100}}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:40:32.365Z\", \"updated_at\": \"2026-05-17T21:14:35.625Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed44. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:34:14.132Z\", \"updated_at\": \"2026-05-17T21:02:09.738Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed44. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:34:11.800Z\", \"updated_at\": \"2026-05-17T21:02:08.069Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed43. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:34:09.846Z\", \"updated_at\": \"2026-05-17T21:02:06.052Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed42. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:05:32.383Z\", \"updated_at\": \"2026-05-17T21:01:12.153Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed46 will show magnitude sensitivity collapse pattern similar to seed42, confirming obs_only robustness advantage\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:40:31.417Z\", \"updated_at\": \"2026-05-17T20:55:55.430Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed43. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:32:18.289Z\", \"updated_at\": \"2026-05-17T18:37:21.561Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:34:38.488Z\", \"updated_at\": \"2026-05-17T18:37:20.319Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed43 on LIBERO-Object. M006 补救重跑。seed42 ε=0.05=13%。\", \"conclusion\": \"killed\"}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:34:20.097Z\", \"updated_at\": \"2026-05-17T18:35:42.842Z\", \"hypothesis\": \"Measure wall-clock latency of ACR-VLA pipeline components: VLA encode, VLA K-sampling (K=1/5/10/20), CGS scoring, CRM forward pass, and full pipeline. Quantify overhead of conformal refinement relative to VLA sampling cost.\", \"conclusion\": \"success\", \"metrics\": {\"vla_encode_prefix_ms\": 33.5, \"vla_sample_K1_ms\": 192.6, \"vla_sample_K5_ms\": 965.3, \"vla_sample_K10_ms\": 1913.7, \"vla_sample_K20_ms\": 3858.2, \"cgs_ms\": 6.2, \"crm_forward_ms\": 0.3, \"full_pipeline_K10_ms\": 1908.2, \"acr_overhead_pct\": 0.34}}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:51:14.367Z\", \"updated_at\": \"2026-05-17T18:31:23.291Z\", \"hypothesis\": \"K=1 CRM with ACCG using full multi-scale features (4×960D from SmolVLA layers [3,7,11,15]). Multi-scale should capture richer correction signals than single-stage 960D fallback (val_loss=0.006505). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"notes\": \"Retry after W&B API key crash. Added --no_wandb. Precompute cache reused (65,223 samples). Training restarted from scratch (epoch 1/50). PID 447923 on cuda:0, tmux session: train-crm-k1-v2.\", \"metrics\": {\"best_val_loss\": 0.007199, \"total_epochs\": 50, \"train_samples\": 65223, \"obs_dim\": \"4x960D\", \"multi_scale\": true}, \"conclusion\": \"success\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:28:01.165Z\", \"updated_at\": \"2026-05-17T18:22:02.272Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed44. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.07, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:27:59.825Z\", \"updated_at\": \"2026-05-17T18:22:01.354Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed43. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:27:58.213Z\", \"updated_at\": \"2026-05-17T18:22:00.464Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed42. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:15:05.583Z\", \"updated_at\": \"2026-05-17T17:32:15.936Z\", \"hypothesis\": \"obs_only CRM (default norm ~1.42, 无裁剪) seed=45 on LIBERO Object. 验证 obs_only 在 uncapped 大 norm 下仍优于 VLA-only（seed42 在 default 为 17%）。极端 magnitude 鲁棒性测试。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks\": 10, \"rollouts_per_task\": 20, \"total_successes\": 24, \"total_rollouts\": 200}}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:38:01.206Z\", \"updated_at\": \"2026-05-17T17:29:34.723Z\", \"hypothesis\": \"Scalar uncertainty CRM seed=45 on LIBERO Object. 测试 scalar conditioning（单一 std 而非 per-DOF）是否比 obs_only 或 perdof 更优。如果表现介于两者之间，说明 conditioning 信息量与性能正相关。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"best_task\": \"chocolate_pudding_0.25\", \"worst_task\": \"alphabet_soup_0.0\"}}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:34:55.059Z\", \"updated_at\": \"2026-05-17T17:03:14.729Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=45 on LIBERO Object. 验证 perdof 在中间 norm (0.2) 的表现（seed42=11%, seed43=9%）。为 magnitude curve 误差估计提供第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"notes\": \"perdof ε=0.2 seed45: 9% (18/200). Cross-seed: seed42=11%, seed43=9%, seed44=10%, seed45=9%. Mean ~9.75%.\"}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T00:37:24.278Z\", \"updated_at\": \"2026-05-17T16:52:17.419Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=44 on LIBERO Object benchmark. Adds second seed to perdof norm=0.2 (seed42=11%, seed43=9%). Enables error bar on magnitude curve figure at this norm point.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:02:35.790Z\", \"updated_at\": \"2026-05-17T15:19:16.626Z\", \"hypothesis\": \"CRM K=1 with ACCG architecture trained on K=10 single-stage cache (960D fallback) can learn effective corrections for object benchmark, achieving low val_loss comparable to multi-scale approach\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006505, \"best_epoch\": 43, \"total_epochs\": 50, \"train_samples\": 4857, \"obs_dim\": 960, \"multi_scale\": false, \"wall_clock_seconds\": 914.9}}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:48:22.459Z\", \"updated_at\": \"2026-05-17T14:53:10.162Z\", \"hypothesis\": \"K=1 CRM 训练（ACCG 架构）：使用 Action-Conditioned Correction Gating 替代 FiLM，多阶段 VLA 特征融合 + 组合损失函数（L2 + directional + triplet + magnitude），训练专用于 K=1 单采样纠正的 CRM。目标超越 K=1 VLA-only baseline (10.8%)。ACCG 用 action 本身计算动态 gate 选择 correction 维度。\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:34:09.564Z\", \"updated_at\": \"2026-05-17T13:52:58.983Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:05:28.139Z\", \"updated_at\": \"2026-05-17T13:31:57.433Z\", \"hypothesis\": \"obs_only CRM at eps=0.1 on seed47 will achieve similar improvement over VLA-only as seen in seed42 (19%), testing seed robustness of the magnitude curve\", \"conclusion\": \"killed\", \"notes\": \"Worker batch7 误杀, 4/10 tasks 完成\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T21:32:42.117Z\", \"updated_at\": \"2026-05-17T12:04:17.540Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=45 on LIBERO object benchmark. Retry after unregistered process conflict. Expected to confirm perdof collapse at high norm (seed42=4%, seed44 running). Supports magnitude curve narrative.\", \"metrics\": {\"overall_sr\": 0.06, \"successes\": 6, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:22:10.412Z\", \"updated_at\": \"2026-05-17T12:00:58.173Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed44 re-run on LIBERO-Object. 原 seed44 已完成(conclusion=negative, SR=4%). 重跑验证跨 seed 一致性。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"n_rollouts\": 10, \"total_rollouts\": 100, \"note\": \"JSON result found by diagnostic worker. Matches original seed44=4%. False positive failure due to no sentinel/W&B in evaluate.py.\"}}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:21:56.645Z\", \"updated_at\": \"2026-05-17T11:50:09.879Z\", \"hypothesis\": \"obs_only CRM ε=0.3 seed47 on LIBERO-Object. 5th seed at high norm (seed42=19%, seed44=18%, seed45=14%, seed46 running). 补全 magnitude curve 高 norm 段 error bar。\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:28:13.840Z\", \"updated_at\": \"2026-05-17T11:36:55.536Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed46 retry on LIBERO-Object. 原 PID 394433 退出，PID 392856 在 bjb2-28827 cuda:2 继续运行。seed42=4%, seed44=4%, seed45=6%。\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T21:32:40.226Z\", \"updated_at\": \"2026-05-17T11:05:43.649Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comparison to 6 seeds. If consistent with seeds 42-44 (16-22%), strengthens pooled significance for Narrative A transition.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"successes\": 20, \"total\": 100, \"benchmark\": \"object\", \"mode\": \"obs_only\", \"norm\": 0.2, \"seed\": 47}}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:21:04.937Z\", \"updated_at\": \"2026-05-17T10:59:11.317Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=44 on LIBERO Object. 验证 perdof 在低 norm 的安全区域（seed42=11%，seed45 running）。多 seed 支撑 magnitude curve 低 norm 段。\", \"conclusion\": \"negative\", \"notes\": \"失败原因: process dead 5× with no sentinel/W&B — auto-resolved as failed | 诊断中: Worker worker_diagnose_eval-perdof-object-norm01-seed44_20260517T105221 已派发到 bjb1-18228 检查是否为 cron 误判（同配置 seed45 成功，SR=11%）\", \"metrics\": {\"overall_sr\": 0.08, \"total_successes\": 8, \"total_rollouts\": 100, \"seed\": 44, \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:07:14.242Z\", \"updated_at\": \"2026-05-17T10:56:41.892Z\", \"hypothesis\": \"Duplicate of seed47 obs_only norm=0.1 on bjb2 (survived GPU conflict cleanup), provides extra seed47 data point\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T16:04:31.207Z\", \"updated_at\": \"2026-05-17T10:54:36.728Z\", \"hypothesis\": \"obs_only CRM ε=0.2 seed46 on LIBERO-Object. Pooled Fisher test 最关键的缺失配对数据（与 argmin seed46=10% 配对）。ε=0.2 是 obs_only 最优区间，seed42=22%。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"total_episodes\": 100, \"successes\": 15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 2, \"bbq_sauce\": 3, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 4, \"orange_juice\": 3}}}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:17:00.494Z\", \"updated_at\": \"2026-05-17T10:54:24.948Z\", \"hypothesis\": \"Duplicate of obs_only norm=0.1 seed46 on bjb2 (deployed by batch5 Worker). Extra data point for magnitude curve.\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T21:38:21.922Z\", \"updated_at\": \"2026-05-17T10:54:02.629Z\", \"hypothesis\": \"Argmin baseline (reconvla K=10) seed=47 on LIBERO object benchmark. Paired with obs_only seed47 on cuda:0 for direct comparison. Extends argmin multi-seed data for pooled Fisher test.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:21:06.341Z\", \"updated_at\": \"2026-05-17T10:22:14.183Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=45 on LIBERO Object. 验证 perdof 在低 norm (0.1) 的安全区域（seed42=11%）。如果与 obs_only 接近，支持\\\"低 norm 两者等效\\\"叙事。\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:51:20.872Z\", \"updated_at\": \"2026-05-17T10:19:28.338Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed47, completes magnitude curve low-norm data for perdof\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T18:39:23.017Z\", \"updated_at\": \"2026-05-17T10:19:26.819Z\", \"hypothesis\": \"Argmin baseline (conformal selection K=10, 无 learned correction) seed=46 on LIBERO Object. 与 obs_only seed=46 配对，扩展 pooled Fisher test 到 6 seeds。预期 12-17% SR。\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T15:24:08.486Z\", \"updated_at\": \"2026-05-17T07:02:49.285Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.3 on LIBERO Object (seed=45) should show graceful degradation similar to seed42 (19%), providing multi-seed error estimates for the magnitude curve\", \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}, \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:14:45.495Z\", \"updated_at\": \"2026-05-17T06:54:28.933Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=45 on LIBERO object benchmark. Completes seed=45 six-way comparison. seed42=12%, seed43=15%, seed44=running.\", \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}, \"conclusion\": \"success\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:44:23.744Z\", \"updated_at\": \"2026-05-17T06:53:28.467Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}, \"hypothesis\": \"Argmin baseline (conformal selection K=10, no correction) seed=45 on LIBERO Object. Highest priority: expands argmin multi-seed data from 3 to 4 seeds, balancing against obs_only 5 seeds for symmetric Fisher test. Expected 12-17% SR.\"}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:01:50.937Z\", \"updated_at\": \"2026-05-17T04:48:50.296Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠正价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42-r2\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T15:24:11.457Z\", \"updated_at\": \"2026-05-17T04:45:11.458Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=44 on LIBERO Object. 验证 perdof 在高 norm (0.3) 的退化程度（seed42=4%）。多 seed 确认 perdof progressive collapse 机制。\", \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"total_episodes\": 100, \"successes\": 4, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 0, \"bbq_sauce\": 1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 1, \"milk\": 0, \"chocolate_pudding\": 1, \"orange_juice\": 0}}}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:07:31.626Z\", \"updated_at\": \"2026-05-17T03:31:42.118Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.2 on LIBERO object benchmark. Paired with obs_only norm=0.2 (running, 18% at 5/10) for magnitude comparison figure. Tests perdof at moderate correction norm on object domain.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"negative\", \"parent\": \"eval-acr-object-v3\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-17T03:31:41.215Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"conclusion\": \"negative\", \"parent\": \"crm-train-v2-scalar-unc\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:21.006Z\", \"updated_at\": \"2026-05-17T03:31:40.288Z\", \"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"conclusion\": \"negative\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO Spatial benchmark. Spatial benchmark 下 obs_only 最优 norm 是否同样为 0.2。如果 spatial 无明显分离，说明方法效果依赖 action distribution shift 程度。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:16.095Z\", \"updated_at\": \"2026-05-17T03:31:39.344Z\", \"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM (ε=0.3) on LIBERO Spatial benchmark. 高 norm 下 perdof 在 spatial 是否也出现退化。如果 spatial 无 collapse（与 obs_only 接近），说明 failure mode 与 task complexity 相关。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:10.924Z\", \"updated_at\": \"2026-05-17T03:31:38.448Z\", \"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 下 perdof 在 spatial 的表现。如果与 obs_only-0.05 一致（35%），说明低 norm 约束消除了 conditioning 差异。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:08.547Z\", \"updated_at\": \"2026-05-17T03:31:37.673Z\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"negative\", \"hypothesis\": \"perdof CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 perdof 在 spatial 的表现。与 obs_only-0.03 (34%) 对比，验证低 norm 安全区域。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:10:44.114Z\", \"updated_at\": \"2026-05-17T03:15:31.664Z\", \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\", \"hypothesis\": \"VLA mean action (average of K=10 samples) on LIBERO-Spatial provides a strong baseline by reducing sampling noise — establishes whether sample averaging alone matches or exceeds single-sample VLA\", \"parent\": \"eval-spatial-v7-full\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:20:46.639Z\", \"updated_at\": \"2026-05-17T03:15:28.368Z\", \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"hypothesis\": \"ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves meaningful improvement over VLA-only baseline by applying visually-guided corrections without requiring action history\", \"parent\": \"crm-train-v2-obs-only\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:05:16.510Z\", \"updated_at\": \"2026-05-17T03:15:26.392Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"hypothesis\": \"Full ACR pipeline v7 (obs-only CRM, conformal selection, norm=0.1) on LIBERO-Spatial achieves improvement over VLA-only baseline (32%), validating the method on spatial reasoning tasks\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:05:25.647Z\", \"updated_at\": \"2026-05-17T03:15:25.342Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"hypothesis\": \"Full ACR pipeline v8 (obs-only CRM, K=10 conformal selection, norm=0.1) on LIBERO-Object achieves consistent improvement over VLA-only baseline (9-12%) across all 10 tasks with optimized hyperparameters\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:55:02.277Z\", \"updated_at\": \"2026-05-17T03:15:19.323Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v5 (shard 2/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard2\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:55:00.276Z\", \"updated_at\": \"2026-05-17T03:15:18.177Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v5 (shard 1/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard1\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:54:59.383Z\", \"updated_at\": \"2026-05-17T03:15:17.511Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v5 (shard 0/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard0\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:58:14.301Z\", \"updated_at\": \"2026-05-17T03:15:16.391Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v4 (shard 2/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard2\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:58:12.183Z\", \"updated_at\": \"2026-05-17T03:15:15.362Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v4 (shard 1/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard1\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:58:09.830Z\", \"updated_at\": \"2026-05-17T03:15:14.415Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precompute v4 (shard 0/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard0\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:12:01.937Z\", \"updated_at\": \"2026-05-17T03:15:05.867Z\", \"metrics\": {\"overall_sr\": 0.16, \"total_success\": 16, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"hypothesis\": \"Obs-only CRM with norm=0.1 on LIBERO-Object seed=44 replicates seed=42 success, confirming that performance gains are robust across random seeds and not artifacts of a single initialization\", \"parent\": \"eval-acr-object-obs-only-norm02\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:34:53.953Z\", \"updated_at\": \"2026-05-17T03:15:04.317Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 18, \"total\": 200, \"tasks_done\": 10}, \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=45 provides second additional seed for baseline variance estimation — multi-seed baselines required for statistical significance claims in paper\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:50:14.071Z\", \"updated_at\": \"2026-05-17T03:15:03.364Z\", \"metrics\": {\"overall_sr\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"source\": \"json_file_verified_by_worker\"}, \"conclusion\": \"success\", \"notes\": \"seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-task 分布略有差异（seed43: chocolate_pudding 40% vs seed42: 20%, bbq_sauce 30% vs 20%），但总 SR 相同。确认 VLA-only 作为稳定 baseline。seed=43 六方对比表第一个完成点。\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=43 establishes multi-seed baseline variance — needed to determine if ACR improvements are statistically significant above baseline noise\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:20:02.901Z\", \"updated_at\": \"2026-05-17T03:14:58.588Z\", \"conclusion\": \"success\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}, \"hypothesis\": \"VLA mean action on LIBERO-Spatial task 10 (wooden shelf) specifically — completing the last missing task from the earlier eval-vla-mean-spatial run to have full 10-task baseline numbers\", \"parent\": \"eval-vla-mean-spatial\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:04:34.297Z\", \"updated_at\": \"2026-05-17T03:14:57.896Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"hypothesis\": \"ReconVLA (K=10 sample consensus without CRM) on LIBERO-Spatial establishes upper bound for pure sampling diversity benefit — if high, CRM correction adds value only at lower K; if low, confirms CRM is essential\", \"parent\": \"plan_014-reconvla-baseline\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:43:42.283Z\", \"updated_at\": \"2026-05-17T03:14:57.225Z\", \"conclusion\": \"failed\", \"hypothesis\": \"Obs-only CRM v2 retrained on spatial data resolves the dimension mismatch from v1 and achieves meaningful improvement on LIBERO-Spatial by using benchmark-matched visual features\", \"parent\": \"eval-obs-only-spatial\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:30:43.696Z\", \"updated_at\": \"2026-05-17T03:14:56.290Z\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}, \"hypothesis\": \"Training CRM to predict scalar uncertainty enables confidence-based action selection via conformal prediction, allowing adaptive correction magnitude based on model confidence\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:30:40.796Z\", \"updated_at\": \"2026-05-17T03:14:55.328Z\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}, \"hypothesis\": \"Training CRM with per-DoF (per degree-of-freedom) correction output produces more fine-grained corrections than a single scalar, improving downstream task performance on multi-joint manipulation\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:41:35.819Z\", \"updated_at\": \"2026-05-17T03:14:53.940Z\", \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}, \"hypothesis\": \"Training a CRM with obs-only input (no action/proprio) can learn correction signals purely from visual observation features, enabling correction without access to action space information\", \"parent\": \"plan_001-crm-smolvla\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:57:48.056Z\", \"updated_at\": \"2026-05-17T03:13:50.200Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precomputing VLA action caches (shard 2/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:57:46.669Z\", \"updated_at\": \"2026-05-17T03:13:49.286Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precomputing VLA action caches (shard 1/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:57:45.284Z\", \"updated_at\": \"2026-05-17T03:13:43.682Z\", \"conclusion\": \"success\", \"hypothesis\": \"Precomputing VLA action caches (shard 0/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-k5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:15:37.603Z\", \"updated_at\": \"2026-05-17T03:13:41.787Z\", \"conclusion\": \"success\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}, \"hypothesis\": \"Precomputing K=5 VLA action samples provides sufficient diversity for conformal selection while reducing inference cost by 50% vs K=10 — testing efficiency-performance tradeoff\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T06:56:12.892Z\", \"updated_at\": \"2026-05-17T03:13:39.823Z\", \"conclusion\": \"failed\", \"hypothesis\": \"ReconVLA baseline implementation validates that sample consensus (K=10 argmin Euclidean) provides meaningful improvement over single-sample VLA, establishing competitive baseline for ACR comparison\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T03:01:07.682Z\", \"updated_at\": \"2026-05-17T03:13:37.890Z\", \"conclusion\": \"failed\", \"hypothesis\": \"Initial CRM + SmolVLA integration plan validates that conformal residual module can be trained and integrated with a pretrained VLA model for action refinement\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T01:22:10.415Z\", \"updated_at\": \"2026-05-17T03:13:35.534Z\", \"conclusion\": \"success\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}, \"hypothesis\": \"MVP validation: CRM correction signals improve point-reaching accuracy in simplified task — if corrections reliably move end-effector toward targets, the mechanism transfers to full manipulation\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T11:35:16.236Z\", \"updated_at\": \"2026-05-17T03:13:33.197Z\", \"conclusion\": \"failed\", \"hypothesis\": \"SmolVLA pretrained model evaluates directly on LIBERO-Spatial without any CRM or conformal processing — establishing raw VLA capability as absolute floor baseline\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:10.843Z\", \"updated_at\": \"2026-05-17T03:13:04.533Z\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}, \"hypothesis\": \"Obs-only CRM trained on object benchmark generalizes to LIBERO-Spatial tasks without retraining — testing cross-benchmark transfer of visual correction signals\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:13:41.913Z\", \"updated_at\": \"2026-05-17T03:09:38.443Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"hypothesis\": \"obs_only CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 obs_only 在 uncapped norm 下的跨 seed 稳定性（seed42=17%）。如果维持 15-20%，确认极端 magnitude 鲁棒性。\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:56:58.178Z\", \"updated_at\": \"2026-05-17T03:09:30.045Z\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\", \"hypothesis\": \"perdof CRM (ε=0.05) seed=42 on LIBERO Object. 验证 perdof 在极低 norm 下是否与 obs_only 接近（两者都受限于低 norm 纠正量）。magnitude curve 低端数据点。\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:34:16.821Z\", \"updated_at\": \"2026-05-17T03:09:27.225Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"conclusion\": \"success\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=43 on LIBERO Object. 验证 perdof 在 norm=0.2 的多 seed 数据（seed42=11%）。确认 perdof 在中间 norm 的退化幅度具有跨 seed 一致性。\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:26:52.169Z\", \"updated_at\": \"2026-05-17T03:09:17.332Z\", \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=42 on LIBERO Object magnitude sweep. 验证 perdof 在 norm=0.3 的 collapse 程度。预期 SR 急剧下降（支持 progressive collapse 叙事）。\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:16:18.917Z\", \"updated_at\": \"2026-05-17T03:09:15.263Z\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 在 spatial 上的表现。与 object 的 0.05 数据点对比，检验 benchmark 间一致性。\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:20:45.606Z\", \"updated_at\": \"2026-05-17T03:09:11.273Z\", \"notes\": \"Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 obs_only 在 spatial 的表现（10-task SR）。验证 magnitude 效应在不同 benchmark 上的一致性。\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:29:02.155Z\", \"updated_at\": \"2026-05-17T03:09:10.586Z\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.3) on LIBERO Object magnitude sweep seed=42. 验证高 norm 下 obs_only 是否仍保持 graceful degradation（对比 perdof 在同 norm 的 collapse）。\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:29:00.724Z\", \"updated_at\": \"2026-05-17T03:09:06.864Z\", \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Object magnitude sweep seed=42. 验证极低 norm 下 obs_only 表现。如果 SR 与 VLA-only 相近（12%），说明过低 norm 约束了 CRM 纠正能力。\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T02:46:15.008Z\", \"updated_at\": \"2026-05-17T03:04:54.543Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠���价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42\", \"conclusion\": \"failed\"}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T02:18:02.194Z\", \"updated_at\": \"2026-05-17T02:38:55.611Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（跳过 K=10 采样+argmin 选择），测试 obs 特征鲁棒性在简化 pipeline 下是否成立。如果 SR > VLA-only (~11%)，说明 CRM 本身有独立价值；如果 SR < VLA-only，说明 selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:44:19.258Z\", \"updated_at\": \"2026-05-16T21:33:38.747Z\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}, \"hypothesis\": \"obs_only CRM (ε=0.2) seed=45 on LIBERO object: if obs_only maintains 16-22% SR range consistent with seeds 42-44, it confirms the method's reliability across random seeds and strengthens pooled statistical test vs argmin.\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:11:59.390Z\", \"updated_at\": \"2026-05-16T21:29:49.586Z\", \"hypothesis\": \"Scalar CRM seed=44 on LIBERO object benchmark. Retry of failed eval-scalar-object-seed44. Expects scalar variant underperforms obs_only but may match argmin baseline.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.06, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:56:22.235Z\", \"updated_at\": \"2026-05-16T19:45:27.956Z\", \"hypothesis\": \"perdof CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 four-way comparison. seed42=11%, seed43=12%. Expected to confirm perdof < argmin.\", \"metrics\": {\"overall_sr\": 0.08, \"total_success\": 8, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T06:05:51.470Z\", \"updated_at\": \"2026-05-16T19:37:12.898Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed magnitude curve coverage. seed42 norm=0.3 object still running on bjb2-28827. Pairs with seed44 norm=0.2 for norm sensitivity across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:58:30.713Z\", \"updated_at\": \"2026-05-16T18:36:08.965Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T14:48:54.894Z\", \"updated_at\": \"2026-05-16T15:36:08.207Z\", \"hypothesis\": \"P0 retry #4: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22%, seed43=16%. Previous attempts failed (127/129/killed).\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:32:14.163Z\", \"updated_at\": \"2026-05-16T15:34:00.414Z\", \"hypothesis\": \"Retry of eval-argmin-object-seed44 (EXIT_CODE=127, missing conda activate). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:32:15.187Z\", \"updated_at\": \"2026-05-16T15:25:14.349Z\", \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activate). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:14:47.376Z\", \"updated_at\": \"2026-05-16T11:30:59.542Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=45 on LIBERO object benchmark. Multi-seed magnitude curve data point. seed42 norm=0.3=19%, seed44 norm=0.3=running. Extends magnitude robustness evidence to 3rd seed.\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:11:49.844Z\", \"updated_at\": \"2026-05-16T09:00:15.290Z\", \"hypothesis\": \"v4-default (no magnitude control, norm≈1.42) on object benchmark — ablation to confirm catastrophic failure\", \"parent\": \"eval-acr-object-v4-default\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:47:32.591Z\", \"updated_at\": \"2026-05-16T08:37:12.296Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.03 on LIBERO object benchmark. Paired with obs_only norm=0.03 for magnitude comparison figure. Tests perdof at smallest correction norm on object domain.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:58:27.783Z\", \"updated_at\": \"2026-05-16T07:46:23.704Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry). P0 critical for statistical significance — seed42=22%, need seed43 pooled to 200 trials. Original crashed after 1 task.\", \"parent\": \"eval-obs-only-object-norm02-seed43\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_seed42\": \"-6pp (22% → 16%)\", \"vs_argmin_seed43\": \"-1pp (17% → 16%)\", \"pooled_2seed_obs_only_02\": \"19% (38/200)\", \"pooled_2seed_argmin\": \"14.5% (29/200)\"}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:33:13.916Z\", \"updated_at\": \"2026-05-16T07:13:29.827Z\", \"hypothesis\": \"Retry of eval-vla-only-object-seed44 (r1 EXIT_CODE=127). VLA-only baseline K=1 seed=44 on LIBERO object. Third seed reference. seed42=12%, seed43=12%.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.1, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:38:22.125Z\", \"updated_at\": \"2026-05-16T07:09:01.967Z\", \"hypothesis\": \"obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default (perdof default). Tests whether obs_only robustness holds even without magnitude capping — if yes, obs_only is fundamentally more robust than perdof regardless of norm setting.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:02:31.432Z\", \"updated_at\": \"2026-05-16T06:04:05.747Z\", \"hypothesis\": \"D031: scalar_unc CRM v3-norm seed=43 on LIBERO object benchmark. Completes seed=43 six-way comparison table. scalar seed=42 was worst at 4% — seed=43 confirms.\", \"parent\": \"eval-acr-object-v4-scalar\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:47:31.254Z\", \"updated_at\": \"2026-05-16T05:56:01.541Z\", \"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object benchmark. Completes 5-point magnitude curve (0.03/0.05/0.1/0.2/0.3). Tests minimum effective correction magnitude on object domain.\", \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T05:02:34.914Z\", \"updated_at\": \"2026-05-16T05:25:06.306Z\", \"hypothesis\": \"scalar_unc CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. scalar seed42=9%, seed43 running (0% at 3/10). Expected worst CRM variant.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:34:30.429Z\", \"updated_at\": \"2026-05-16T04:59:20.094Z\", \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (r1 EXIT_CODE=127, r2 killed by agent). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:34:28.047Z\", \"updated_at\": \"2026-05-16T04:59:17.975Z\", \"hypothesis\": \"Retry of eval-argmin-object-seed44 (r1 EXIT_CODE=127, r2 killed by agent). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"conclusion\": \"killed\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:46:28.667Z\", \"updated_at\": \"2026-05-16T04:53:17.141Z\", \"hypothesis\": \"D031: VLA-mean baseline (K=10, mean aggregation) seed=43 on LIBERO object benchmark. Completes seed=43 comparison table. If VLA-mean seed=43 ≈ obs_only seed=43 → CRM correction claim compressed.\", \"parent\": \"eval-vla-mean-object\", \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T13:19:49.586Z\", \"updated_at\": \"2026-05-16T03:15:39.287Z\", \"hypothesis\": \"D031 supplementary: perdof CRM v3-norm seed=43 on LIBERO object benchmark. Completes three-way comparison (obs_only vs argmin vs perdof) with doubled samples. If perdof seed=43 ≈ argmin seed=43 → confirms obs_only uniquely better.\", \"parent\": \"eval-acr-object-v4-perdof\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:29:00.342Z\", \"updated_at\": \"2026-05-16T01:33:29.678Z\", \"hypothesis\": \"D035 follow-up: VLA-only baseline (K=1) seed=44 on LIBERO object benchmark. Third seed reference point. seed42=12%, seed43=12%. Deployed on bjb2-40593.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:28:59.304Z\", \"updated_at\": \"2026-05-16T01:32:51.127Z\", \"hypothesis\": \"D035 follow-up: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object benchmark. Third seed for Fisher exact test. ε=0.2 is PROJECT HIGH config (seed42=22%). Paired with eval-argmin-object-seed44.\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:28:58.358Z\", \"updated_at\": \"2026-05-16T01:32:49.190Z\", \"hypothesis\": \"D035 follow-up: argmin baseline (K=10) seed=44 on LIBERO object benchmark. Third seed for Fisher exact test statistical power. Paired with eval-obs-only-object-norm02-seed44. seed42=12%, seed43=17%.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:58:46.063Z\", \"updated_at\": \"2026-05-16T00:51:14.618Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm seed=43 on LIBERO object benchmark. Doubles sample size for Fisher exact test. seed=42 shows obs_only 16% vs argmin 8% (+8pp, p≈0.19). Combined 200 trials target p < 0.05.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:05:41.192Z\", \"updated_at\": \"2026-05-16T00:49:21.141Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"conclusion\": \"failed\", \"notes\": \"Killed: duplicate of eval-mag-obsonly-norm03-r2 on same cuda:0. r2 had 15min more progress. Both wrote same output_file, causing potential corruption.\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:58:46.739Z\", \"updated_at\": \"2026-05-16T00:37:43.289Z\", \"hypothesis\": \"D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact test. Need both conditions under same seed for valid comparison.\", \"parent\": \"eval-reconvla-object\", \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:19:36.419Z\", \"updated_at\": \"2026-05-15T19:38:38.710Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:43:48.583Z\", \"updated_at\": \"2026-05-15T19:38:31.587Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm02\", \"conclusion\": \"killed\", \"notes\": \"失败原因: EXIT_CODE=127 — tmux 用 sh 执行命令，python 不在 sh PATH 中。修复: bash -c 包裹。已重试为 eval-mag-obsonly-norm03-r2。\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:26:53.269Z\", \"updated_at\": \"2026-05-15T19:34:07.651Z\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:14:01.998Z\", \"updated_at\": \"2026-05-15T19:27:30.465Z\", \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:13:38.067Z\", \"updated_at\": \"2026-05-15T19:27:28.479Z\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03-b2 (spatial magnitude sweep obs_only norm=0.3). Submitted on bjb2-28827:cuda:2 instead of bjb1-32546:cuda:3 (cuda:3 occupied by P0 obs-only-norm02-seed43-r2). Director approved.\", \"parent\": \"eval-mag-obsonly-norm03-b2\", \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:15:19.724Z\", \"updated_at\": \"2026-05-15T19:25:28.957Z\", \"conclusion\": \"killed\", \"notes\": \"Killed during cuda:2/3 GPU cleanup on bjb2-28827 (2026-05-16). Was sharing cuda:2 with perdof norm=0.3 r2.\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:15:16.452Z\", \"updated_at\": \"2026-05-15T19:25:28.055Z\", \"conclusion\": \"killed\", \"notes\": \"GPU contention on cuda:2 (shared with perdof norm=0.2 seed=43). Killed 2026-05-16. Replaced by r3 clean restart.\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:55:02.698Z\", \"updated_at\": \"2026-05-15T19:17:41.948Z\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:55:00.179Z\", \"updated_at\": \"2026-05-15T19:17:40.199Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T18:58:07.302Z\", \"updated_at\": \"2026-05-15T19:17:39.068Z\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:15:35.450Z\", \"updated_at\": \"2026-05-15T19:17:37.622Z\", \"conclusion\": \"killed\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:28:33.119Z\", \"updated_at\": \"2026-05-15T19:17:36.369Z\", \"conclusion\": \"killed\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:39:04.708Z\", \"updated_at\": \"2026-05-15T19:17:30.541Z\", \"conclusion\": \"killed\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:39:02.628Z\", \"updated_at\": \"2026-05-15T19:17:29.292Z\", \"conclusion\": \"killed\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:39:00.259Z\", \"updated_at\": \"2026-05-15T19:17:27.703Z\", \"conclusion\": \"killed\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:11:04.275Z\", \"updated_at\": \"2026-05-15T19:17:26.396Z\", \"conclusion\": \"killed\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:11:02.520Z\", \"updated_at\": \"2026-05-15T19:17:25.022Z\", \"conclusion\": \"killed\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:11:01.629Z\", \"updated_at\": \"2026-05-15T19:17:23.631Z\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:58:30.091Z\", \"updated_at\": \"2026-05-15T19:13:43.549Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Migrated from bjb1-32546:cuda:4 (GPU conflict) to bjb2-28827:cuda:2. Paired with obs_only norm=0.3 for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm0p3-object\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:34:52.454Z\", \"updated_at\": \"2026-05-15T18:58:11.790Z\", \"hypothesis\": \"Retry of eval-mag-perdof-norm03-object (killed by SIGTERM). Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Paired with obs_only norm=0.3 (running) for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm03-object\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T13:38:18.819Z\", \"updated_at\": \"2026-05-15T18:58:10.821Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. norm=0.2 shows strongest signal (18% SR at 5/10 tasks in seed=42). Seed=43 doubling for statistical power on the best-performing configuration.\", \"parent\": \"eval-acr-object-obs-only-norm02\", \"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:18:17.209Z\", \"updated_at\": \"2026-05-15T17:38:37.815Z\", \"hypothesis\": \"Ablation: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Tests whether magnitude control is essential on object domain too. If v4-default << v4-perdof (norm=0.1) → magnitude control is universally needed. If v4-default ≈ v4-perdof → spatial failure was anomalous.\", \"parent\": \"eval-acr-object-v4-perdof\", \"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"notes\": \"Killed per Director instruction. 3/10 tasks all 0% SR, no magnitude control (norm≈1.42). Conclusion obvious — magnitude control is essential.\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-15T16:57:00.172Z\", \"updated_at\": \"2026-05-15T17:38:28.909Z\", \"conclusion\": \"killed\", \"notes\": \"Restarted on cuda:3 (PID 118886, tmux: eval-mag-perdof-norm03-object) after v4-default killed. Previous run killed by SIGTERM before first rollout.\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:49:38.786Z\", \"updated_at\": \"2026-05-15T17:22:51.755Z\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"conclusion\": \"success\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:31:09.989Z\", \"updated_at\": \"2026-05-15T17:01:25.883Z\", \"hypothesis\": \"VLA mean baseline (K=10, mean aggregation) on LIBERO object benchmark. Matches reconvla spatial baseline but on object tasks.\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T01:48:28.744Z\", \"updated_at\": \"2026-05-15T16:25:17.101Z\", \"hypothesis\": \"ReconVLA baseline (scalar Euclidean argmin, K=10) on LIBERO object benchmark. Tests whether simple sample selection improves over VLA mean on object manipulation tasks. Provides baseline for CRM comparison on object domain.\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:53:41.689Z\", \"updated_at\": \"2026-05-15T16:23:01.718Z\", \"hypothesis\": \"D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.\", \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:49:13.626Z\", \"updated_at\": \"2026-05-15T15:45:38.531Z\", \"hypothesis\": \"D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation of spatial findings.\", \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:14:04.283Z\", \"updated_at\": \"2026-05-15T13:18:27.852Z\", \"hypothesis\": \"Restart from T3. scalar_unc CRM v3-norm with max_correction_norm=0.1 on spatial. Three-way ablation: perdof vs scalar_unc vs obs_only.\", \"parent\": \"eval-acr-spatial-v4-scalar\", \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:14:05.934Z\", \"updated_at\": \"2026-05-15T11:15:11.801Z\", \"hypothesis\": \"Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features need restructuring.\", \"parent\": \"eval-acr-spatial-v4-obs-only-r2\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T09:09:04.411Z\", \"updated_at\": \"2026-05-15T10:01:21.065Z\", \"hypothesis\": \"D029: obs_only seed=43 复现实验。obs_only 是项目唯一存活路径。seed=42 如果确认 +5pp over argmin，seed=43 增加统计力（200 vs 200 样本下 Fisher exact p ~0.12，配合 object benchmark 独立验证有望通过）。\", \"parent\": \"eval-acr-spatial-v4-obs-only-r3\", \"notes\": \"D029: perdof spatial 35% vs argmin 34% = +1pp, kill criterion triggered. Per-DOF claim dead on spatial. obs_only 是唯一存活路径，seed=43 用于增加统计力。\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:14:05.220Z\", \"updated_at\": \"2026-05-15T09:10:21.153Z\", \"hypothesis\": \"Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline.\", \"parent\": \"eval-acr-spatial-v4-small\", \"notes\": \"[D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + object benchmark 结果。spatial matched-task perdof=argmin (0pp) 意味着 Scenario A 在 spatial 上不可能。\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:10:44.647Z\", \"updated_at\": \"2026-05-15T07:19:12.632Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"conclusion\": \"killed\", \"notes\": \"Stale duplicate entry with dots in name. Actual experiment is eval-mag-obsonly-norm-0p3-r3 (also killed). Real running experiment is eval-mag-obsonly-norm03-r2.\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:11:06.381Z\", \"updated_at\": \"2026-05-15T07:17:16.300Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"conclusion\": \"killed\", \"notes\": \"Director 撤销部署指令。r2 (PID 325264) 实际未被误杀，r3 是基于信息差的重复部署。立即 kill r3 保留 r2。\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:14:03.322Z\", \"updated_at\": \"2026-05-15T06:39:37.926Z\", \"hypothesis\": \"Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base action selection from CRM correction.\", \"parent\": \"eval-argmin-only-spatial\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\", \"notes\": \"10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34/100). T0-T8 from original run, T9 from r2 restart. Clean exit. bjb1-18228 cuda:0 now FREE.\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:21:24.009Z\", \"updated_at\": \"2026-05-15T05:32:12.897Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.03 on spatial. Completes obs_only norm curve (have 0.05, 0.2; adding 0.03).\", \"conclusion\": \"killed\", \"notes\": \"Duplicate experiment on same GPU. pid 225144 was actually the child python process of eval-mag-obsonly-norm003-b2's wrapper (pid 225139). Not a separate experiment. Killed, restarted b2 with new pid 227426.\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:11:14.165Z\", \"updated_at\": \"2026-05-15T05:18:17.853Z\", \"hypothesis\": \"VLA-only baseline (K=1, single sample, no CRM) on LIBERO object benchmark. Lowest-bar baseline for object domain.\", \"conclusion\": \"failed\", \"notes\": \"Duplicate of eval-vla-only-object (already DONE at 12% SR). Process killed to free bjb1-32546 cuda:4.\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:54:57.323Z\", \"updated_at\": \"2026-05-15T04:47:47.959Z\", \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline (K=1, no mean, no CRM) on LIBERO object benchmark. Single sample from flow-matching VLA.\", \"metrics\": {\"overall_sr\": 0.12, \"total_success\": 12, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T01:48:09.734Z\", \"updated_at\": \"2026-05-15T03:30:05.911Z\", \"hypothesis\": \"D018-D019 验证: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42). 如果 v4-default << v4-small (max_norm=0.1) → magnitude control 是必要的。如果 v4-default ≈ baseline → normalization 独自不够。补全 bjb1 上两次失败的实验。\", \"parent\": \"eval-acr-spatial-v4-default-r2\", \"conclusion\": \"killed\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:48:35.421Z\", \"updated_at\": \"2026-05-15T01:45:12.897Z\", \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:17:37.194Z\", \"updated_at\": \"2026-05-14T22:40:00.000Z\", \"hypothesis\": \"D018 retry: Normalization alone fixes CRM correction degradation. v3-norm per-DOF checkpoint with default max_correction_norm (~1.42). If >30% baseline → normalization was the main fix. If still < 30% → magnitude control also needed (compare with v4-small at 0.1).\", \"parent\": \"eval-acr-spatial-v4-default\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:08:53.421Z\", \"updated_at\": \"2026-05-14T22:16:05.788Z\", \"hypothesis\": \"D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:08:59.906Z\", \"updated_at\": \"2026-05-14T22:08:58.490Z\", \"hypothesis\": \"D018: Input normalization alone fixes CRM correction degradation. v3-norm checkpoint with default max_correction_norm=1.42. If >30% baseline → normalization was the main fix.\", \"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:01.250Z\", \"updated_at\": \"2026-05-14T22:05:42.608Z\", \"hypothesis\": \"Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization.\", \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:00.829Z\", \"updated_at\": \"2026-05-14T22:05:28.289Z\", \"hypothesis\": \"Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features.\", \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:45:12.565Z\", \"updated_at\": \"2026-05-14T20:05:22.677Z\", \"hypothesis\": \"D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning\", \"parent\": \"crm-train-v3-perdof\", \"conclusion\": \"success\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:05:00.968Z\", \"updated_at\": \"2026-05-14T18:37:14.400Z\", \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:05:02.939Z\", \"updated_at\": \"2026-05-14T18:37:04.316Z\", \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:04:54.552Z\", \"updated_at\": \"2026-05-14T18:37:02.631Z\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:49:43.787Z\", \"updated_at\": \"2026-05-14T17:47:54.523Z\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:08.413Z\", \"updated_at\": \"2026-05-14T17:47:53.188Z\", \"conclusion\": \"killed\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:48:40.837Z\", \"updated_at\": \"2026-05-14T07:59:32.676Z\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:56:28.643Z\", \"updated_at\": \"2026-05-14T07:59:31.277Z\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}}, \"crm-train-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:10:36.535Z\", \"updated_at\": \"2026-05-14T07:59:30.290Z\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}}, \"crm-train-k5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T01:42:55.911Z\", \"updated_at\": \"2026-05-14T07:59:29.396Z\", \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:54:30.549Z\", \"updated_at\": \"2026-05-14T07:52:44.766Z\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:04:32.138Z\", \"updated_at\": \"2026-05-14T07:52:43.327Z\", \"conclusion\": \"killed\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T04:14:23.092Z\", \"updated_at\": \"2026-05-14T07:52:43.134Z\", \"conclusion\": \"killed\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T00:03:35.642Z\", \"updated_at\": \"2026-05-14T01:45:48.892Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:04:28.766Z\", \"updated_at\": \"2026-05-14T00:05:22.619Z\", \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T23:17:35.776Z\", \"updated_at\": \"2026-05-14T00:04:26.792Z\", \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:56:40.287Z\", \"updated_at\": \"2026-05-13T23:14:22.561Z\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:54:28.535Z\", \"updated_at\": \"2026-05-13T23:12:11.315Z\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:29:41.730Z\", \"updated_at\": \"2026-05-13T23:12:10.958Z\", \"conclusion\": \"killed\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:13:26.341Z\", \"updated_at\": \"2026-05-13T23:12:10.037Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:16:58.052Z\", \"updated_at\": \"2026-05-13T23:12:09.066Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T17:38:57.194Z\", \"updated_at\": \"2026-05-13T19:09:00.612Z\", \"conclusion\": \"killed\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T16:08:51.171Z\", \"updated_at\": \"2026-05-13T16:14:40.934Z\", \"conclusion\": \"killed\"}}, \"count\": 402, \"total\": 402, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9781}}"
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
I have the file listings from all 4 servers. Now I need to:
1. Read the metrics from each JSON file on each server
2. Read the registry to know what's already registered

Let me first read the registry data, then extract metrics from the key files. There are a LOT of files - let me focus on the key categories mentioned in the task and batch the metric extraction.

Let me read the registry first, and in parallel extract metrics from all servers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "65533256-c1e2-48f2-8d89-bf42d5279802",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TA3qfuGVprfgpB7eTU9B1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8804,
      "cache_read_input_tokens": 24313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8804
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

找到大量文件。现在并行提取所有服务器的指标，同时读取 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "1285c3d9-b7e0-4535-92f9-304062baa3bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TA3qfuGVprfgpB7eTU9B1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8804,
      "cache_read_input_tokens": 24313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8804
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01ChSKMfqooiC8QtHisxMfZr`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 -c \"\nimport json, glob, os\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_*.json'), key=os.path.getmtime, reverse=True)\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('success_rate', 'N/A'))\n        ak = d.get('avg_actual_k', 'N/A')\n        fp = d.get('fast_path_ratio', 'N/A')\n        print(f'{os.path.basename(f)}|{sr}|{ak}|{fp}')\n    except: pass\n\"",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "e01e630b-263f-4079-ac71-e9b329308bb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TA3qfuGVprfgpB7eTU9B1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8804,
      "cache_read_input_tokens": 24313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8804
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

_source line 22 · 2026-05-20T03:53:12.396Z_

<details><summary>↩ Tool result · `toolu_01ChSKMfqooiC8QtHisxMfZr`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "9beb3e35-7411-41bc-bd34-368123bec98f",
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

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FWE6rkAtjjNMaNgftgZ1E7`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "python3 -c \"\nimport json, glob, os\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_*.json'), key=os.path.getmtime, reverse=True)\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('success_rate', 'N/A'))\n        ak = d.get('avg_actual_k', 'N/A')\n        fp = d.get('fast_path_ratio', 'N/A')\n        print(f'{os.path.basename(f)}|{sr}|{ak}|{fp}')\n    except: pass\n\"",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "157986d1-7cd2-4ef3-a790-7617b79caef8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TA3qfuGVprfgpB7eTU9B1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8804,
      "cache_read_input_tokens": 24313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8804
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

_source line 24 · 2026-05-20T03:53:14.794Z_

<details><summary>↩ Tool result · `toolu_01FWE6rkAtjjNMaNgftgZ1E7`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "09c9809c-4740-4a77-b789-8b1a60db3968",
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

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019eVG8cVNhfrumH3Ptruxjq`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 -c \"\nimport json, glob, os\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_*.json'), key=os.path.getmtime, reverse=True)\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('success_rate', 'N/A'))\n        ak = d.get('avg_actual_k', 'N/A')\n        fp = d.get('fast_path_ratio', 'N/A')\n        print(f'{os.path.basename(f)}|{sr}|{ak}|{fp}')\n    except: pass\n\"",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "eaca5521-af18-4df6-bffa-f92e2890d4cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TA3qfuGVprfgpB7eTU9B1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8804,
      "cache_read_input_tokens": 24313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8804
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

_source line 26 · 2026-05-20T03:53:16.658Z_

<details><summary>↩ Tool result · `toolu_019eVG8cVNhfrumH3Ptruxjq`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "f80ee820-3cbf-4e9e-9383-550c3fe3302b",
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

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HpifZvMyEp59mhKhnVShqa`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "python3 -c \"\nimport json, glob, os\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_*.json'), key=os.path.getmtime, reverse=True)\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('success_rate', 'N/A'))\n        ak = d.get('avg_actual_k', 'N/A')\n        fp = d.get('fast_path_ratio', 'N/A')\n        print(f'{os.path.basename(f)}|{sr}|{ak}|{fp}')\n    except: pass\n\"",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "c5227bf6-5c12-4bbd-86f1-66b9df00dc57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TA3qfuGVprfgpB7eTU9B1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8804,
      "cache_read_input_tokens": 24313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8804
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

_source line 28 · 2026-05-20T03:53:18.558Z_

<details><summary>↩ Tool result · `toolu_01HpifZvMyEp59mhKhnVShqa`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "2a94a4fc-42d2-499b-8d2b-1841d5385297",
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

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01SYWhh98Yg92vbDoW9G8Cmf`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249182037.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n# Extract experiment IDs and their key info\nfor exp in result:\n    eid = exp.get('experiment_id','')\n    status = exp.get('status','')\n    metrics = exp.get('metrics',{})\n    if metrics:\n        sr = metrics.get('overall_success_rate', metrics.get('success_rate', ''))\n        print(f'{eid}|{status}|SR={sr}')\n    else:\n        print(f'{eid}|{status}|no_metrics')\n\" 2>/dev/null | head -100",
  "description": "Parse registry to list registered experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "a6750cd3-4ef2-4d09-8dad-d8402464bd1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TA3qfuGVprfgpB7eTU9B1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8804,
      "cache_read_input_tokens": 24313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8804
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

_source line 30 · 2026-05-20T03:53:23.021Z_

<details><summary>↩ Tool result · `toolu_01SYWhh98Yg92vbDoW9G8Cmf`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "97151b55-46f8-4873-98ad-7aa45f2965c9",
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

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
The ssh_read_only blocks shell metacharacters including `|`. I need to use `python3 -c` without pipes. Let me use a simpler approach - just cat each file individually, or use python3 -c with a script that doesn't use pipes.

Wait, actually `python3 -c "..."` should work without pipes. The issue was that Python code contains `|` character? No, looking at the code, it doesn't have `|`. Let me re-read... Oh, the `print(f'{...}|{...}|{...}')` contains `|` characters inside the string. The shell metacharacter detector is seeing those pipe characters even though they're inside Python strings.


I'll switch to a different separator like `::` or `,` instead. The bash command for the registry came back empty, so I need to try a different approach there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "de3d7bb5-23b5-4b11-992e-e0eeafc2a874",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUTrW1CJQHLq5m1i51Wvep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2164,
      "cache_read_input_tokens": 33117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2164
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

shell 元字符被拦截，换分隔符重试。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "6f547ae9-3d3e-4076-b2ba-db3da40881c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUTrW1CJQHLq5m1i51Wvep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2164,
      "cache_read_input_tokens": 33117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2164
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011jpN8nLmFNDVgNmYHPJ9uZ`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 -c \"\nimport json, glob, os\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_*.json'), key=os.path.getmtime, reverse=True)\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('success_rate', 'N/A'))\n        ak = d.get('avg_actual_k', 'N/A')\n        fp = d.get('fast_path_ratio', 'N/A')\n        print(os.path.basename(f), sr, ak, fp)\n    except: pass\n\"",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "41fcffda-e2cd-4ea5-93f0-68d07f939640",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUTrW1CJQHLq5m1i51Wvep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2164,
      "cache_read_input_tokens": 33117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2164
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

_source line 34 · 2026-05-20T03:53:37.582Z_

<details><summary>↩ Tool result · `toolu_011jpN8nLmFNDVgNmYHPJ9uZ`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "862a179e-10d9-4b1f-8745-9bbe608710f7",
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

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XnHqcrw1aQwVUPGG53jmqd`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "python3 -c \"\nimport json, glob, os\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_*.json'), key=os.path.getmtime, reverse=True)\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('success_rate', 'N/A'))\n        ak = d.get('avg_actual_k', 'N/A')\n        fp = d.get('fast_path_ratio', 'N/A')\n        print(os.path.basename(f), sr, ak, fp)\n    except: pass\n\"",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "1a3e3ae4-1478-42f4-9ad1-20938f4f1c1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUTrW1CJQHLq5m1i51Wvep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2164,
      "cache_read_input_tokens": 33117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2164
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

_source line 36 · 2026-05-20T03:53:37.780Z_

<details><summary>↩ Tool result · `toolu_01XnHqcrw1aQwVUPGG53jmqd`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "4fab57c3-dad7-4e18-b2d0-0c577705c925",
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

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01F6JMZLLeMsqXi9kAfGeN1F`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 -c \"\nimport json, glob, os\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_*.json'), key=os.path.getmtime, reverse=True)\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('success_rate', 'N/A'))\n        ak = d.get('avg_actual_k', 'N/A')\n        fp = d.get('fast_path_ratio', 'N/A')\n        print(os.path.basename(f), sr, ak, fp)\n    except: pass\n\"",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "8dad5aae-36bf-4896-88ac-be3af8167db2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUTrW1CJQHLq5m1i51Wvep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2164,
      "cache_read_input_tokens": 33117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2164
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

_source line 38 · 2026-05-20T03:53:38.756Z_

<details><summary>↩ Tool result · `toolu_01F6JMZLLeMsqXi9kAfGeN1F`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "99675a24-fd0c-44b3-a921-c8474db25ef2",
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

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01M2ph5rixC3SpGfsbfbPcyr`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "python3 -c \"\nimport json, glob, os\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/eval_*.json'), key=os.path.getmtime, reverse=True)\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('overall_success_rate', d.get('success_rate', 'N/A'))\n        ak = d.get('avg_actual_k', 'N/A')\n        fp = d.get('fast_path_ratio', 'N/A')\n        print(os.path.basename(f), sr, ak, fp)\n    except: pass\n\"",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "cd133b2d-47f4-4f29-94c0-455e75294014",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUTrW1CJQHLq5m1i51Wvep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2164,
      "cache_read_input_tokens": 33117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2164
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

_source line 40 · 2026-05-20T03:53:41.170Z_

<details><summary>↩ Tool result · `toolu_01M2ph5rixC3SpGfsbfbPcyr`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "0572aa70-910a-469e-8fed-edd331347024",
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

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01L67nA7Y4bSPVc9LfgsqSgZ`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249182037.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nfor exp in result:\n    eid = exp.get('experiment_id','')\n    status = exp.get('status','')\n    metrics = exp.get('metrics',{})\n    if metrics:\n        sr = metrics.get('overall_success_rate', metrics.get('success_rate', ''))\n        print(f'{eid} :: {status} :: SR={sr}')\n    else:\n        print(f'{eid} :: {status} :: no_metrics')\n\" 2>/dev/null",
  "description": "Parse registry experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "f6e585db-e684-4c01-a614-a5177522420e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUTrW1CJQHLq5m1i51Wvep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2164,
      "cache_read_input_tokens": 33117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2164
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

_source line 42 · 2026-05-20T03:53:43.830Z_

<details><summary>↩ Tool result · reported error · `toolu_01L67nA7Y4bSPVc9LfgsqSgZ`</summary>

```text
Exit code 1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "3c1dbb97-ed79-4ef6-a9a1-e835ba68f0f0",
  "tool_use_result": "Error: Exit code 1"
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
OK, `open()` is blocked in ssh_read_only python. And the bash parsing failed. Let me use `grep` to extract metrics from the JSON files, and use a different approach for the registry.

For the servers, I'll use `grep` to extract the key fields from each JSON file. Let me use `cat` on each file or `grep` for specific keys.

Actually, I should try a simpler approach - `grep` with specific patterns. But there are many files, so maybe I should use `find` + `cat` approach, but since metacharacters are blocked, I'll need to cat individual files.

Wait - the user's original prompt said to use `ssh_read_only` with a for loop + python3 -c. 

But `ssh_read_only` also blocks glob expansion, so I can't use wildcards. Let me try listing the directory first to see what files exist, then construct individual grep commands for each file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "e80d1a5b-041e-455e-999f-4aac504262e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LL7rr3qwyDJUqNBpZY4VPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2073,
      "cache_read_input_tokens": 35281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2073
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

_source line 44_

ssh_read_only 限制严格，改用 grep 提取指标。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "0d54db26-de0a-4e69-810d-49a55bb8e5cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LL7rr3qwyDJUqNBpZY4VPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2073,
      "cache_read_input_tokens": 35281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2073
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

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XWHeEA3pbLaUaErNjSGJ1E`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -H \"overall_success_rate\\|success_rate\\|avg_actual_k\\|fast_path_ratio\" /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_adaptive_k*.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof*.json /root/acr-vla-conformal-refinement/logs/eval_object_random*.json /root/acr-vla-conformal-refinement/logs/eval_object_argmin*.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla*.json /root/acr-vla-conformal-refinement/logs/eval_object_scalar*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "fd2cfee0-cf8f-495f-9d59-94b22e70e65d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LL7rr3qwyDJUqNBpZY4VPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2073,
      "cache_read_input_tokens": 35281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2073
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

_source line 46 · 2026-05-20T03:53:59.807Z_

<details><summary>↩ Tool result · `toolu_01XWHeEA3pbLaUaErNjSGJ1E`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "4d61e8a6-6f23-4e6a-9b30-fee2d229e159",
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

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BA7skZ5QT3MqktXzjs1mwZ`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -H \"overall_success_rate\\|success_rate\\|avg_actual_k\\|fast_path_ratio\" /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_adaptive_k*.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof*.json /root/acr-vla-conformal-refinement/logs/eval_object_random*.json /root/acr-vla-conformal-refinement/logs/eval_object_argmin*.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla*.json /root/acr-vla-conformal-refinement/logs/eval_object_scalar*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "00e82747-fe17-4483-9412-bcc1beedc629",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LL7rr3qwyDJUqNBpZY4VPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2073,
      "cache_read_input_tokens": 35281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2073
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

_source line 48 · 2026-05-20T03:54:04.051Z_

<details><summary>↩ Tool result · `toolu_01BA7skZ5QT3MqktXzjs1mwZ`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "488321fa-c501-45e3-934f-c0a5f85c7827",
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

_source line 49_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E4QpAzerSx7R82JtrRfZQm`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -H \"overall_success_rate\\|success_rate\\|avg_actual_k\\|fast_path_ratio\" /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_adaptive_k*.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof*.json /root/acr-vla-conformal-refinement/logs/eval_object_random*.json /root/acr-vla-conformal-refinement/logs/eval_object_argmin*.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla*.json /root/acr-vla-conformal-refinement/logs/eval_object_scalar*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "593f741b-3831-43de-adf4-c0af6c068f2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LL7rr3qwyDJUqNBpZY4VPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2073,
      "cache_read_input_tokens": 35281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2073
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

_source line 50 · 2026-05-20T03:54:07.843Z_

<details><summary>↩ Tool result · `toolu_01E4QpAzerSx7R82JtrRfZQm`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "c58cd400-3f01-44b5-b6e2-4c253858636e",
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

_source line 51_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FdRaLn7Hwi3tqGB21MhZzB`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -H \"overall_success_rate\\|success_rate\\|avg_actual_k\\|fast_path_ratio\" /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_adaptive_k*.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof*.json /root/acr-vla-conformal-refinement/logs/eval_object_random*.json /root/acr-vla-conformal-refinement/logs/eval_object_argmin*.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla*.json /root/acr-vla-conformal-refinement/logs/eval_object_scalar*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "fe62e310-cc01-4e6a-af52-bf52c2549761",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LL7rr3qwyDJUqNBpZY4VPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2073,
      "cache_read_input_tokens": 35281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2073
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

_source line 52 · 2026-05-20T03:54:11.617Z_

<details><summary>↩ Tool result · `toolu_01FdRaLn7Hwi3tqGB21MhZzB`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "ad70ae0b-d251-4398-8519-1739534e0804",
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

### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
The `\|` in the grep pattern is being interpreted as a shell metacharacter. I need to use `-E` flag with `|` or use `-e` multiple times. But `|` is blocked. Let me use `grep -e "pattern1" -e "pattern2"` instead. Or I could use `grep -E` with the patterns in a different way...

Actually the `\|` contains the `|` character which is being flagged. Let me use multiple `-e` flags.

But wait - even in `-e` patterns, the `|` character might be blocked at the shell level by the safety check. 

Let me simplify this and just search for `success_rate` directly without trying to match multiple patterns, since that term will catch both the specific and overall variants anyway.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "75e0e28c-39b9-4c74-a153-2bda6f6cd540",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8WJSSEetcPetKxxLFk1pZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3010,
      "cache_read_input_tokens": 37354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3010
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

_source line 54_

`|` 被拦截。改用多次 `-e` 或分别 grep。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "242de572-b5d5-4e3d-95f1-c42a8da2ec42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8WJSSEetcPetKxxLFk1pZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3010,
      "cache_read_input_tokens": 37354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3010
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

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01U9c1yGC7iDBCJ1ue8v6ouw`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -rn \"success_rate\" /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_adaptive_k*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "46069a1a-56fe-40c7-9933-fe6f4d52d785",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8WJSSEetcPetKxxLFk1pZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3010,
      "cache_read_input_tokens": 37354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3010
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

_source line 56 · 2026-05-20T03:54:23.751Z_

<details><summary>↩ Tool result · `toolu_01U9c1yGC7iDBCJ1ue8v6ouw`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:6:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:34:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:54:      \\\"success_rate\\\": 0.5,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:6:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:34:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:54:      \\\"success_rate\\\": 0.4,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:6:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:34:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:54:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:6:  \\\"overall_success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-con\\n\\n... [截断: 输出过长，省略 18561 字符] ...\\n\\n_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:44:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:49:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:6:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:19:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:24:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:44:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:49:      \\\"success_rate\\\": 0.4,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:6:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:19:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:24:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:44:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:49:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:54:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:6:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:19:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:24:      \\\"success_rate\\\": 0.4,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:44:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:49:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:54:      \\\"success_rate\\\": 0.2,\\n\", \"stderr\": \"grep: /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "9ea5727b-5aa5-4948-b717-a36a93e4a6f1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:19:      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:24:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:29:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:34:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:44:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:49:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:54:      \\\\\\\"success_rate\\\\\\\": 0.5,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:19:      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:24:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:29:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:34:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:39:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:44:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:49:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:54:      \\\\\\\"success_rate\\\\\\\": 0.4,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.15,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:19:      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:24:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:29:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:34:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:44:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:49:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:54:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:19:      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:24:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-con\\\\n\\\\n... [截断: 输出过长，省略 18561 字符] ...\\\\n\\\\n_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:29:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:34:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:44:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:49:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:54:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:19:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:24:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:29:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:34:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:44:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:49:      \\\\\\\"success_rate\\\\\\\": 0.4,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:54:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:14:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:19:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:24:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:29:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:34:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:39:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:44:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:49:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:54:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:19:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:24:      \\\\\\\"success_rate\\\\\\\": 0.4,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:29:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:34:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:39:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:44:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:49:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:54:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n\\\", \\\"stderr\\\": \\\"grep: /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json: No such file or directory\\\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json: No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:6:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:34:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:54:      \\\"success_rate\\\": 0.5,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:6:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:34:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:54:      \\\"success_rate\\\": 0.4,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:6:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:34:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:54:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:6:  \\\"overall_success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-con\\n\\n... [截断: 输出过长，省略 18561 字符] ...\\n\\n_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:44:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:49:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:6:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:19:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:24:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:44:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:49:      \\\"success_rate\\\": 0.4,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:6:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:19:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:24:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:44:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:49:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:54:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:6:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:19:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:24:      \\\"success_rate\\\": 0.4,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:44:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:49:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:54:      \\\"success_rate\\\": 0.2,\\n\", \"stderr\": \"grep: /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018Y6J4a1FguSQFfdTrLHRJ5`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -rn \"success_rate\" /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_adaptive_k*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "4810d4e2-a3b2-4810-99f1-19fd54e99f06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8WJSSEetcPetKxxLFk1pZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3010,
      "cache_read_input_tokens": 37354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3010
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

_source line 58 · 2026-05-20T03:54:26.619Z_

<details><summary>↩ Tool result · `toolu_018Y6J4a1FguSQFfdTrLHRJ5`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:6:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:29:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:34:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:54:      \\\"success_rate\\\": 0.4,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:6:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:19:      \\\"success_rate\\\": 0.9,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:34:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:54:      \\\"success_rate\\\": 0.5,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:6:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:19:      \\\"success_rate\\\": 1.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:34:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:6:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:24:      \\\"success_rate\\\": 0\\n\\n... [截断: 输出过长，省略 9346 字符] ...\\n\\nconformal-refinement/logs/eval_object_vla_only_seed48.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:44:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:49:      \\\"success_rate\\\": 0.4,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:6:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:19:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:24:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:44:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:49:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:54:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:6:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:19:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:24:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:44:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:49:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:6:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:19:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:24:      \\\"success_rate\\\": 0.4,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:44:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:49:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:54:      \\\"success_rate\\\": 0.3,\\n\", \"stderr\": \"grep: /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "30c83c92-6ad9-4c47-b8b1-940629155d87",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.18,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:19:      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:24:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:29:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:34:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:39:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:44:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:49:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:54:      \\\\\\\"success_rate\\\\\\\": 0.4,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.18,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:19:      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:24:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:29:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:34:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:44:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:49:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:54:      \\\\\\\"success_rate\\\\\\\": 0.5,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:19:      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:24:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:29:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:34:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:39:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:44:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:49:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:54:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:19:      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:24:      \\\\\\\"success_rate\\\\\\\": 0\\\\n\\\\n... [截断: 输出过长，省略 9346 字符] ...\\\\n\\\\nconformal-refinement/logs/eval_object_vla_only_seed48.json:29:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:34:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:44:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:49:      \\\\\\\"success_rate\\\\\\\": 0.4,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:54:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:14:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:19:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:24:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:29:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:34:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:39:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:44:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:49:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:54:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:14:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:19:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:24:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:29:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:34:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:44:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:49:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:54:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:14:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:19:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:24:      \\\\\\\"success_rate\\\\\\\": 0.4,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:29:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:34:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:44:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:49:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:54:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n\\\", \\\"stderr\\\": \\\"grep: /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json: No such file or directory\\\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json: No such file or directory\\\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json: No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:6:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:29:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:34:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:54:      \\\"success_rate\\\": 0.4,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:6:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:19:      \\\"success_rate\\\": 0.9,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:34:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:54:      \\\"success_rate\\\": 0.5,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:6:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:19:      \\\"success_rate\\\": 1.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:34:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:6:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:24:      \\\"success_rate\\\": 0\\n\\n... [截断: 输出过长，省略 9346 字符] ...\\n\\nconformal-refinement/logs/eval_object_vla_only_seed48.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:44:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:49:      \\\"success_rate\\\": 0.4,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:6:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:19:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:24:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:44:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:49:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:54:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:6:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:19:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:24:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:44:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:49:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:6:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:19:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:24:      \\\"success_rate\\\": 0.4,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:44:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:49:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:54:      \\\"success_rate\\\": 0.3,\\n\", \"stderr\": \"grep: /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019Tr7vKmu9T4uie77FQonCu`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -rn \"success_rate\" /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_adaptive_k*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "cd9cbf43-18c6-48de-859e-efa1a73ed6aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8WJSSEetcPetKxxLFk1pZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3010,
      "cache_read_input_tokens": 37354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3010
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

_source line 60 · 2026-05-20T03:54:29.450Z_

<details><summary>↩ Tool result · `toolu_019Tr7vKmu9T4uie77FQonCu`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:6:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:29:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:54:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:6:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:19:      \\\"success_rate\\\": 0.7,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:29:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:6:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:54:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:6:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:19:      \\\"success_rate\\\": 0.9,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:29:      \\\"success_rate\\\": 0.5,\\n/root/acr-vla-conformal-refinement/logs/eval_long\\n\\n... [截断: 输出过长，省略 24188 字符] ...\\n\\n_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:44:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:49:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:54:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:6:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:19:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:24:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:44:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:49:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:54:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:6:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:19:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:24:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:29:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:44:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:49:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:54:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:6:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:19:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:24:      \\\"success_rate\\\": 0.5,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:49:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:54:      \\\"success_rate\\\": 0.1,\\n\", \"stderr\": \"grep: /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "35133ed3-fdcf-4c6c-9fa2-5c1cfcb23d54",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:19:      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:24:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:29:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:34:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:44:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:49:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:54:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:19:      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:24:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:29:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:34:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:39:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:44:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:49:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:54:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:19:      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:24:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:29:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:34:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:44:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:49:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:54:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.18,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:19:      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:24:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:29:      \\\\\\\"success_rate\\\\\\\": 0.5,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long\\\\n\\\\n... [截断: 输出过长，省略 24188 字符] ...\\\\n\\\\n_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:29:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:34:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:44:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:49:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:54:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:14:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:19:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:24:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:29:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:34:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:39:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:44:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:49:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:54:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:14:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:19:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:24:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:29:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:34:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:44:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:49:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:54:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:14:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:19:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:24:      \\\\\\\"success_rate\\\\\\\": 0.5,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:29:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:34:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:39:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:44:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:49:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:54:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n\\\", \\\"stderr\\\": \\\"grep: /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json: No such file or directory\\\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json: No such file or directory\\\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json: No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:6:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:29:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:54:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:6:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:19:      \\\"success_rate\\\": 0.7,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:29:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:6:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:19:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:49:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:54:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:6:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:19:      \\\"success_rate\\\": 0.9,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:24:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:29:      \\\"success_rate\\\": 0.5,\\n/root/acr-vla-conformal-refinement/logs/eval_long\\n\\n... [截断: 输出过长，省略 24188 字符] ...\\n\\n_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:29:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:44:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:49:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:54:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:6:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:19:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:24:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:44:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:49:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:54:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:6:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:14:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:19:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:24:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:29:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:34:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:44:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:49:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:54:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:6:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:19:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:24:      \\\"success_rate\\\": 0.5,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:49:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:54:      \\\"success_rate\\\": 0.1,\\n\", \"stderr\": \"grep: /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UxN8ox9j12ZdTDzafNcFTH`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -rn \"success_rate\" /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only*.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only*.json /root/acr-vla-conformal-refinement/logs/eval_adaptive_k*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "c671ca69-b6aa-460c-8346-bf8151137f3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8WJSSEetcPetKxxLFk1pZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3010,
      "cache_read_input_tokens": 37354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3010
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

_source line 62 · 2026-05-20T03:54:31.800Z_

<details><summary>↩ Tool result · `toolu_01UxN8ox9j12ZdTDzafNcFTH`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:6:  \\\"overall_success_rate\\\": 0.32,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:9:      \\\"success_rate\\\": 0.9,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:14:      \\\"success_rate\\\": 0.9,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:19:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:24:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:29:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:39:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:49:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:54:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:6:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:19:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:24:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:44:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:49:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:6:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:19:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:24:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:44:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:49:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:54:      \\\"success_rate\\\": 0.1,\\n\", \"stderr\": \"grep: /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_adaptive_k*.json: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "f8dfb606-39e7-4cde-80fa-b9458e340fd5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.32,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:9:      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:14:      \\\\\\\"success_rate\\\\\\\": 0.9,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:19:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:24:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:29:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:34:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:39:      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:44:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:49:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:54:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:14:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:19:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:24:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:29:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:34:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:39:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:44:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:49:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:54:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:6:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:9:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:14:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:19:      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:24:      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:29:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:34:      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:39:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:44:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:49:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:54:      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n\\\", \\\"stderr\\\": \\\"grep: /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json: No such file or directory\\\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json: No such file or directory\\\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json: No such file or directory\\\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json: No such file or directory\\\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json: No such file or directory\\\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json: No such file or directory\\\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only*.json: No such file or directory\\\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_adaptive_k*.json: No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:6:  \\\"overall_success_rate\\\": 0.32,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:9:      \\\"success_rate\\\": 0.9,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:14:      \\\"success_rate\\\": 0.9,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:19:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:24:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:29:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:39:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:44:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:49:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:54:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:6:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:19:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:24:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:39:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:44:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:49:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:54:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:6:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:9:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:14:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:19:      \\\"success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:24:      \\\"success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:29:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:34:      \\\"success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:39:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:44:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:49:      \\\"success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:54:      \\\"success_rate\\\": 0.1,\\n\", \"stderr\": \"grep: /root/acr-vla-conformal-refinement/logs/eval_crm_long*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_long_obs_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_long_vla_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_crm_goal*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only*.json: No such file or directory\\ngrep: /root/acr-vla-conformal-refinement/logs/eval_adaptive_k*.json: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Good, I'm getting data. Now I need to also get avg_actual_k and fast_path_ratio from the adaptive_k files. Let me also get the remaining object experiments from all servers. And I need to read the registry.

Let me extract the overall_success_rate from all the files I've found so far. Let me organize what I have:

**bjb2-28827:**
- eval_crm_long_seed47.json: SR=0.17
- eval_long_obs_only_norm02_seed42.json: SR=0.17


- eval_long_obs_only_norm02_seed43.json: SR=0.15
- eval_long_obs_only_norm02_seed44.json: SR=0.20

I still need to pull the success rates from several more files including the crm_goal variants, goal_vla_only experiments, and the spatial evaluation. I'm finding the success rates in the grep output now—let me parse through these results more carefully to extract the overall_success_rate values for each file. The output got truncated, so I'm missing a lot of the data. Let me take a more targeted approach and just grep for the overall success rate line from all eval files at once on each server—that single line per file should give me the summary statistics I need without having to parse through everything else.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "b1ee7ded-e3f3-45e1-a884-0859a418e62c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xn9rjBoNG6YBMn66brhqTU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16212,
      "cache_read_input_tokens": 40364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16212
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

输出被截断。改用只提取 overall_success_rate 的精简查询。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "bbfbb57a-920e-4d67-ac10-adbcb5b421cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xn9rjBoNG6YBMn66brhqTU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16212,
      "cache_read_input_tokens": 40364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16212
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0166Qi9PAWzWWkddRdZVkSt9`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -r \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "e4a09041-4b19-4002-93b6-a41325ef60c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xn9rjBoNG6YBMn66brhqTU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16212,
      "cache_read_input_tokens": 40364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16212
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

_source line 66 · 2026-05-20T03:54:57.143Z_

<details><summary>↩ Tool result · `toolu_0166Qi9PAWzWWkddRdZVkSt9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed44_r2.json:  \\\"overall_success_rate\\\": 0.64,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed45_r2.json:  \\\"overall_success_rate\\\": 0.65,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed46.json:  \\\"overall_success_rate\\\": 0.72,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r2.json:  \\\"overall_success_rate\\\": 0.73,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.63,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed44_r2.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45_r2.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed47.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed42.json:  \\\"overall_success_rate\\\": 0.19,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45_r2.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed43.json:  \\\"overall_success_rate\\\": 0.19,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed44.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed45.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json:  \\\"overall_success_rate\\\": 0.19,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed47.json:  \\\"overall_success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed46.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed42.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed48.json:  \\\"overall_success_rate\\\": 0.07,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json:  \\\"overall_success_rate\\\": 0.04,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed47.json:  \\\"overall_success_rate\\\": 0.05,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed43.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed43.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed44.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed45.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed42.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed42.json:  \\\"overall_success_rate\\\": 0.35,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed44.json:  \\\"overall_success_rate\\\": 0.37,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.json:  \\\"overall_success_rate\\\": 0.34,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.36,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json:  \\\"overall_success_rate\\\": 0.33,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.31,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "c4e9a5f5-a7ab-416a-b37f-bd0f588badf0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed44_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.64,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed45_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.65,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.72,\\\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.73,\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.63,\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.15,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed44_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.18,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.19,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.19,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.15,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.19,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.07,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.04,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.05,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.35,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.37,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.34,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.36,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.33,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.31,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed44_r2.json:  \\\"overall_success_rate\\\": 0.64,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed45_r2.json:  \\\"overall_success_rate\\\": 0.65,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed46.json:  \\\"overall_success_rate\\\": 0.72,\\n/root/acr-vla-conformal-refinement/logs/eval_crm_long_seed47.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r2.json:  \\\"overall_success_rate\\\": 0.73,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.63,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed44_r2.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45_r2.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed47.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed42.json:  \\\"overall_success_rate\\\": 0.19,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45_r2.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed43.json:  \\\"overall_success_rate\\\": 0.19,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed44.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed45.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json:  \\\"overall_success_rate\\\": 0.19,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed47.json:  \\\"overall_success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed46.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed42.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed48.json:  \\\"overall_success_rate\\\": 0.07,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json:  \\\"overall_success_rate\\\": 0.04,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed47.json:  \\\"overall_success_rate\\\": 0.05,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed43.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed43.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed44.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed45.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed42.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed47.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed42.json:  \\\"overall_success_rate\\\": 0.35,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed44.json:  \\\"overall_success_rate\\\": 0.37,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.json:  \\\"overall_success_rate\\\": 0.34,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.36,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json:  \\\"overall_success_rate\\\": 0.33,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.31,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LoWe9bU3qG7vAQcRaJKpsJ`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -r \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "afe04ad3-5dce-4172-b4e4-80d94292acd5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xn9rjBoNG6YBMn66brhqTU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16212,
      "cache_read_input_tokens": 40364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16212
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

_source line 68 · 2026-05-20T03:54:58.142Z_

<details><summary>↩ Tool result · `toolu_01LoWe9bU3qG7vAQcRaJKpsJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed42.json:  \\\"overall_success_rate\\\": 0.67,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed43.json:  \\\"overall_success_rate\\\": 0.72,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_lto_splitA_vla_only_r3.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm03.json:  \\\"overall_success_rate\\\": 0.36,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed48.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed48.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed46.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed47.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed48.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_norm_r2.json:  \\\"overall_success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed43.json:  \\\"overall_success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed44.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed47.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed47.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json:  \\\"overall_success_rate\\\": 0.08,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed44.json:  \\\"overall_success_rate\\\": 0.04,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed43.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed44.json:  \\\"overall_success_rate\\\": 0.08,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed43.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45_r2.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_openvla_object_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_reconvla_spatial_r2.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json:  \\\"overall_success_rate\\\": 0.32,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.29,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json:  \\\"overall_success_rate\\\": 0.3,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "60246ffc-506e-4cf1-a66d-57c7b1d2f4ea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.67,\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.72,\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.18,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.18,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_lto_splitA_vla_only_r3.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm03.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.36,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.15,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.18,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.15,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.18,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_norm_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.15,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.08,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.04,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.08,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_openvla_object_vla_only_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.0,\\\\n/root/acr-vla-conformal-refinement/logs/eval_reconvla_spatial_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.32,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.29,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.3,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed43.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed42.json:  \\\"overall_success_rate\\\": 0.67,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed43.json:  \\\"overall_success_rate\\\": 0.72,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed45.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_lto_splitA_vla_only_r3.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm03.json:  \\\"overall_success_rate\\\": 0.36,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed48.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed48.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed48.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed46.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed47.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed48.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_norm_r2.json:  \\\"overall_success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed43.json:  \\\"overall_success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed44.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed47.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed47.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json:  \\\"overall_success_rate\\\": 0.08,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed44.json:  \\\"overall_success_rate\\\": 0.04,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed43.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed44.json:  \\\"overall_success_rate\\\": 0.08,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_k5_seed43.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45_r2.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_openvla_object_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.0,\\n/root/acr-vla-conformal-refinement/logs/eval_reconvla_spatial_r2.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json:  \\\"overall_success_rate\\\": 0.32,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.29,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed50.json:  \\\"overall_success_rate\\\": 0.3,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01U8JSVQbBpFZ1irnLECq637`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -r \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "2b38a077-cdd2-40d4-85ff-b9d0f2bb6fd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xn9rjBoNG6YBMn66brhqTU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16212,
      "cache_read_input_tokens": 40364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16212
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

_source line 70 · 2026-05-20T03:54:59.134Z_

<details><summary>↩ Tool result · `toolu_01U8JSVQbBpFZ1irnLECq637`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.64,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json:  \\\"overall_success_rate\\\": 0.65,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.71,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.69,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json:  \\\"overall_success_rate\\\": 0.71,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed42.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed43.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed44.json:  \\\"overall_success_rate\\\": 0.07,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed47.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json:  \\\"overall_success_rate\\\": 0.19,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json:  \\\"overall_success_rate\\\": 0.22,\\n/root/ac\\n\\n... [截断: 输出过长，省略 1320 字符] ...\\n\\noot/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed43.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json:  \\\"overall_success_rate\\\": 0.06,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json:  \\\"overall_success_rate\\\": 0.04,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json:  \\\"overall_success_rate\\\": 0.07,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json:  \\\"overall_success_rate\\\": 0.06,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed43.json:  \\\"overall_success_rate\\\": 0.32,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43_r2.json:  \\\"overall_success_rate\\\": 0.34,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.json:  \\\"overall_success_rate\\\": 0.34,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json:  \\\"overall_success_rate\\\": 0.32,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json:  \\\"overall_success_rate\\\": 0.35,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.27,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json:  \\\"overall_success_rate\\\": 0.29,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "c378a67d-89df-478b-bdef-42ee1d360147",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.15,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.64,\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.65,\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.71,\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.69,\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.71,\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.07,\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.18,\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.15,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.19,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.15,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.15,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.18,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.17,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.22,\\\\n/root/ac\\\\n\\\\n... [截断: 输出过长，省略 1320 字符] ...\\\\n\\\\noot/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.06,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.04,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.07,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.06,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.15,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.32,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.34,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.34,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.32,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.35,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.27,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.3,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.29,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.64,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json:  \\\"overall_success_rate\\\": 0.65,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.71,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.69,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json:  \\\"overall_success_rate\\\": 0.71,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed42.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed43.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed44.json:  \\\"overall_success_rate\\\": 0.07,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed46.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed47.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed42.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed45.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json:  \\\"overall_success_rate\\\": 0.19,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed48.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed47.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.json:  \\\"overall_success_rate\\\": 0.18,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.json:  \\\"overall_success_rate\\\": 0.17,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json:  \\\"overall_success_rate\\\": 0.22,\\n/root/ac\\n\\n... [截断: 输出过长，省略 1320 字符] ...\\n\\noot/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed45.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed43.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json:  \\\"overall_success_rate\\\": 0.06,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed46.json:  \\\"overall_success_rate\\\": 0.04,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed42.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed45.json:  \\\"overall_success_rate\\\": 0.07,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json:  \\\"overall_success_rate\\\": 0.06,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json:  \\\"overall_success_rate\\\": 0.15,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed49.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed43.json:  \\\"overall_success_rate\\\": 0.32,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43_r2.json:  \\\"overall_success_rate\\\": 0.34,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.json:  \\\"overall_success_rate\\\": 0.34,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json:  \\\"overall_success_rate\\\": 0.32,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json:  \\\"overall_success_rate\\\": 0.35,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.27,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json:  \\\"overall_success_rate\\\": 0.3,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json:  \\\"overall_success_rate\\\": 0.29,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018crcTbJp9wYzDaENKQ31nf`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -r \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "6cc54a9a-3931-4607-8101-2b32c2770168",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xn9rjBoNG6YBMn66brhqTU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16212,
      "cache_read_input_tokens": 40364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16212
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

_source line 72 · 2026-05-20T03:54:59.900Z_

<details><summary>↩ Tool result · `toolu_018crcTbJp9wYzDaENKQ31nf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json:  \\\"overall_success_rate\\\": 0.34,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json:  \\\"overall_success_rate\\\": 0.19,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json:  \\\"overall_success_rate\\\": 0.07,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.32,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "b0ce052d-0754-42e7-938a-94b857b2eedd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.34,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.19,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.07,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.32,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json:  \\\"overall_success_rate\\\": 0.34,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json:  \\\"overall_success_rate\\\": 0.19,\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json:  \\\"overall_success_rate\\\": 0.07,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.32,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
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
Now let me also get avg_actual_k and fast_path_ratio from the adaptive_k files. And let me try to parse the registry data.

Let me also get the avg_actual_k for the adaptive_k files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "8383c093-71f4-4b27-9000-fb2e8d444265",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t9auUicJW4CcEhiW8ksWB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11662,
      "cache_read_input_tokens": 56576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11662
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

数据收集完成。再补充 adaptive_k 的 avg_actual_k 和 fast_path_ratio，以及 registry 对比。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "f683d8df-9f70-4437-ac5d-f0a00df81d40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t9auUicJW4CcEhiW8ksWB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11662,
      "cache_read_input_tokens": 56576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11662
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Xz2CoTjGarkKL6eaaRs4vd`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep \"avg_actual_k\\|fast_path_ratio\" /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "384f8cc7-d365-4894-b08a-cfb1b02cdae8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t9auUicJW4CcEhiW8ksWB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11662,
      "cache_read_input_tokens": 56576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11662
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

_source line 76 · 2026-05-20T03:55:06.836Z_

<details><summary>↩ Tool result · `toolu_01Xz2CoTjGarkKL6eaaRs4vd`</summary>

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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "029ec6a4-e8a5-43f8-b277-324927a7e6fc",
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

_source line 77_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UP74DTR6r3VKMpkp9gNJC8`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep \"avg_actual_k\" /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "e0a8266e-315f-4cba-8155-6173eb85f227",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t9auUicJW4CcEhiW8ksWB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11662,
      "cache_read_input_tokens": 56576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11662
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

_source line 78 · 2026-05-20T03:55:08.141Z_

<details><summary>↩ Tool result · `toolu_01UP74DTR6r3VKMpkp9gNJC8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    \\\"avg_actual_k\\\": 3.8100888073922268,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "8f938726-453d-454c-9bde-08198ec44997",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    \\\\\\\"avg_actual_k\\\\\\\": 3.8100888073922268,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    \\\"avg_actual_k\\\": 3.8100888073922268,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AeSDcYxXpUvXZDKUyWyG2Q`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep \"avg_actual_k\" /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "4bb2df41-97dc-47e6-8a0f-55ffb607b7b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t9auUicJW4CcEhiW8ksWB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11662,
      "cache_read_input_tokens": 56576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11662
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

_source line 80 · 2026-05-20T03:55:09.093Z_

<details><summary>↩ Tool result · `toolu_01AeSDcYxXpUvXZDKUyWyG2Q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:    \\\"avg_actual_k\\\": 4.797278911564626,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:    \\\"avg_actual_k\\\": 3.9094310043823706,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:    \\\"avg_actual_k\\\": 3.022363295339778,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:    \\\"avg_actual_k\\\": 2.671526647321113,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "4eeb099d-4000-412b-8846-cfe5d02f51a4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:    \\\\\\\"avg_actual_k\\\\\\\": 4.797278911564626,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:    \\\\\\\"avg_actual_k\\\\\\\": 3.9094310043823706,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:    \\\\\\\"avg_actual_k\\\\\\\": 3.022363295339778,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:    \\\\\\\"avg_actual_k\\\\\\\": 2.671526647321113,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:    \\\"avg_actual_k\\\": 4.797278911564626,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:    \\\"avg_actual_k\\\": 3.9094310043823706,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:    \\\"avg_actual_k\\\": 3.022363295339778,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:    \\\"avg_actual_k\\\": 2.671526647321113,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 81_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01YXziptyAQyUGqepUHx1BcT`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": 0,
  "fields": [
    "experiment_id",
    "status",
    "metrics"
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "5789da0d-b4eb-4a4e-9bb6-e3f6291bc652",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t9auUicJW4CcEhiW8ksWB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11662,
      "cache_read_input_tokens": 56576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11662
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

_source line 82 · 2026-05-20T03:55:10.830Z_

<details><summary>↩ Tool result · `toolu_01YXziptyAQyUGqepUHx1BcT`</summary>

```text
Error: result (98,824 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "e98c8440-e6fb-4c6c-b419-ed1082e44286",
  "tool_use_result": {
    "content": "Error: result (98,824 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-only-goal-seed49\": {\"status\": \"PREPARING\"}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_completed\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.07, \"successes\": 7, \"total\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"DONE\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.11, \"sr_pct\": \"11%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.3, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.73, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.6, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.8}}}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.33, \"sr_pct\": \"33.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0.1, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.8, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}}, \"eval-crm-long-seed50\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"PREPARING\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 4.788, \"fast_path_ratio\": 0.6515, \"total_steps\": 28207, \"fast_steps\": 18377, \"full_steps\": 9830}}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"ALLOCATED\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.81, \"fast_path_ratio\": 0.7737, \"total_steps\": 27813, \"fast_steps\": 21520, \"full_steps\": 6293}}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"PREPARING\", \"metrics\": {\"success_rate\": 0.35, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}}}, \"eval-vla-only-spatial-seed51\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed52\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed51\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.8, \"fast_path_ratio\": 0.65}}, \"eval-vla-only-goal-seed48-r2\": {\"status\": \"DONE\"}, \"eval-vla-only-goal-seed47-r2\": {\"status\": \"DONE\"}, \"eval-crm-goal-seed48\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"ALLOCATED\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.72, \"fast_path_ratio\": 0.785}}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"ALLOCATED\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 3.15, \"fast_path_ratio\": 0.856}}, \"eval-crm-goal-seed47\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.3}}}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"PREPARING\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.58, \"fast_path_ratio\": 0.928}}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"ALLOCATED\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 3.07, \"fast_path_ratio\": 0.866}}, \"calibrate-crm-correction-signal\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed49\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed48\": {\"status\": \"PREPARING\"}, \"eval-vla-only-object-seed51\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed50\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed49\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 3.909, \"fast_path_ratio\": 0.761, \"total_steps\": 28067, \"fast_steps\": 21368, \"full_steps\": 6699}}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.022, \"fast_path_ratio\": 0.872, \"total_steps\": 27724, \"fast_steps\": 24181, \"full_steps\": 3543}}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.612, \"fast_path_ratio\": 0.923, \"total_steps\": 27935, \"fast_steps\": 25797, \"full_steps\": 2138}}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 2.672, \"fast_path_ratio\": 0.916, \"total_steps\": 28258, \"fast_steps\": 25886, \"full_steps\": 2372}}, \"eval-adaptive-k-p25-seed44\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-crm-spatial-seed48\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-seed47\": {\"status\": \"PREPARING\"}, \"eval-vla-only-object-seed49-r2\": {\"status\": \"PREPARING\"}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\"}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.2, \"STUDY_SCENE1_book_in_caddy\": 0.2, \"LIVING_ROOM_SCENE2_soup_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cheese_butter_basket\": 0, \"KITCHEN_SCENE4_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_soup_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.1, \"n_episodes\": 100}}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.3, \"STUDY_SCENE1_book_in_back_compartment\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0.1, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100, \"successes\": 9, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.18, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.9, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.2, \"STUDY_SCENE1_book_in_back_compartment\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.65, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_bowl_on_top_of_the_cabinet\": 0.8, \"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"put_the_wine_bottle_on_the_rack\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_cream_cheese_in_the_bowl\": 0.2}}}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.64, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_bowl_on_the_stove\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"put_the_wine_bottle_on_the_rack\": 0.4, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}}, \"eval-openvla-object-baseline-seed42-r2\": {\"status\": \"PREPARING\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"metrics\": {\"k2l2_vs_k10var_rho\": 0.9979, \"k2l2_vs_k10var_pvalue\": 0, \"k2l2_vs_fmvd_rho\": 0.0925, \"k2l2_vs_fmvd_pvalue\": 6.03e-29, \"k10var_vs_fmvd_rho\": 0.0825, \"k10var_vs_fmvd_pvalue\": 2.33e-23, \"n_samples\": 14512, \"k2l2_mean\": 0.0807, \"k2l2_std\": 0.0361, \"go_nogo_k2_proxy\": \"GO (rho=0.9979)\", \"go_nogo_fmvd_signal\": \"NO-GO (rho=0.09)\"}}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 18}}, \"eval-vla-only-spatial-seed49-r2\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed49\": {\"status\": \"DONE\"}, \"eval-vla-only-goal-seed48\": {\"status\": \"DONE\"}, \"eval-vla-only-goal-seed47\": {\"status\": \"DONE\"}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.69, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.5, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.6}}}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2, \"alphabet_soup\": 0, \"cream_cheese\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0}}}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.2, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.6, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.3, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.4, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.67, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.4}}}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.4}}}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 100, \"successful_rollouts\": 14, \"per_task\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0, \"put_both_cream_cheese_box_and_butter_in_basket\": 0, \"turn_on_stove_put_moka_pot\": 0.8, \"put_black_bowl_in_bottom_drawer\": 0, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.4, \"pick_up_book_place_in_caddy\": 0.1, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.1, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0, \"put_both_moka_pots_on_stove\": 0, \"put_yellow_white_mug_in_microwave\": 0}}}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\"}, \"eval-crm-goal-seed45\": {\"status\": \"DONE\"}, \"eval-crm-goal-seed44\": {\"status\": \"DONE\"}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.63, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.3, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.1, \"turn_on_the_stove\": 0.8, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.8}}}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.71, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.6, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 0.9, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.5, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.1, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}}, \"fmvd-calibration-phase1\": {\"status\": \"DONE\", \"metrics\": {\"spearman_rho\": 0.082528, \"spearman_pvalue\": 2.33e-23, \"n_samples\": 14512, \"go_nogo\": \"NO-GO\", \"threshold\": 0.3, \"fmvd_mean\": 0.054867, \"fmvd_std\": 0.040291, \"fmvd_P25\": 0.027738, \"fmvd_P50\": 0.046693, \"fmvd_P75\": 0.070899, \"fmvd_P90\": 0.093805, \"k10_variance_mean\": 0.004888, \"k10_variance_std\": 0.005635, \"task_success_rate\": 0.06, \"n_tasks\": 10, \"n_episodes\": 50, \"n_successes\": 3}}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.17, \"sr_pct\": \"17.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.3, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 1, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.2, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.2, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.1, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.7, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.3, \"STUDY_SCENE1_book_caddy\": 0, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0.1, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed43\": {\"status\": \"DONE\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.32, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.8, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0.1, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\"}, \"eval-obs-only-spatial-norm02-seed46\": {\"status\": \"DONE\"}, \"eval-argmin-object-k5-seed44\": {\"status\": \"DONE\"}, \"eval-vla-only-goal-seed44\": {\"status\": \"DONE\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.07, \"successes\": 7, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"successes\": 11, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"successes\": 14, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.37, \"successes\": 37, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_bowl_between_plate_ramekin\": 0.9, \"pick_up_bowl_next_to_ramekin\": 1, \"pick_up_bowl_from_table_center\": 0, \"pick_up_bowl_on_cookie_box\": 0.3, \"pick_up_bowl_in_top_drawer\": 0.1, \"pick_up_bowl_on_ramekin\": 0, \"pick_up_bowl_next_to_cookie_box\": 0.9, \"pick_up_bowl_on_stove\": 0, \"pick_up_bowl_next_to_plate\": 0.2, \"pick_up_bowl_on_wooden_cabinet\": 0}}}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"metrics\": {\"vla_encode_ms\": 28.4, \"crm_forward_ms\": 0.246, \"preprocess_ms\": 0.96, \"batched_K1_ms\": 180, \"batched_K5_ms\": 182.3, \"batched_K10_ms\": 162.3, \"batched_K20_ms\": 167.4, \"sequential_K1_ms\": 177, \"sequential_K5_ms\": 891.7, \"sequential_K10_ms\": 1638.9, \"sequential_K20_ms\": 3245.8, \"cgs_K10_ms\": 6.3, \"full_pipe_K10_ms\": 200.7, \"full_pipe_K20_ms\": 199.7, \"vla_model_mb\": 884.1, \"crm_model_mb\": 1.8, \"peak_K20_mb\": 1085.1}}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"sr_pct\": \"10%\"}}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.31, \"successes\": 31, \"total\": 100, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.6, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.29, \"successes\": 29, \"total\": 100, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.8, \"from_table_center\": 0.1, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}}}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.3, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"successes\": 15, \"total\": 100}}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"successes\": 15, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 2, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 0, \"milk\": 2, \"chocolate_pudding\": 4, \"orange_juice\": 2}}}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.12, \"sr_pct\": \"12%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.18, \"sr_pct\": \"18%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.15, \"sr_pct\": \"15%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.3}}}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"metrics\": {\"sr\": 5, \"sr_pct\": \"5%\", \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 34}}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\"}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 16}}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 18}}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}}, \"crm-lto-splitA-train\": {\"status\": \"DONE\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.07, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.02, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 1}}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.05, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"partial\": true, \"tasks_completed\": \"5/10\", \"task6_partial\": \"5/10 rollouts\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0}, \"partial_avg_sr\": 0.1, \"failure_mode\": \"process killed silently mid-eval, no error in log, no JSON output\"}}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed46\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\"}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\"}, \"eval-perdof-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed45\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.3, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\"}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0.1, 0.1, 0.4, 0, 0.2, 0, 0.1, 0.2, 0.2]}}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Partial 9/10 tasks, 0/90 rollouts. Accepted as collapse evidence per Director decision 2026-05-18.\"}}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 100, \"avg_inference_time_ms\": 178, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0}}}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}, \"eval-obs-only-object-norm01-seed46-r2\": {\"status\": \"DEPLOYED\"}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100}}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100}}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.69, \"n_tasks\": 10, \"n_trials_per_task\": 10, \"total_rollouts\": 100}}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.1, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.09, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\"}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"metrics\": {\"vla_encode_prefix_ms\": 33.5, \"vla_sample_K1_ms\": 192.6, \"vla_sample_K5_ms\": 965.3, \"vla_sample_K10_ms\": 1913.7, \"vla_sample_K20_ms\": 3858.2, \"cgs_ms\": 6.2, \"crm_forward_ms\": 0.3, \"full_pipeline_K10_ms\": 1908.2, \"acr_overhead_pct\": 0.34}}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.007199, \"total_epochs\": 50, \"train_samples\": 65223, \"obs_dim\": \"4x960D\", \"multi_scale\": true}}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.07, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks\": 10, \"rollouts_per_task\": 20, \"total_successes\": 24, \"total_rollouts\": 200}}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"best_task\": \"chocolate_pudding_0.25\", \"worst_task\": \"alphabet_soup_0.0\"}}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.006505, \"best_epoch\": 43, \"total_epochs\": 50, \"train_samples\": 4857, \"obs_dim\": 960, \"multi_scale\": false, \"wall_clock_seconds\": 914.9}}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.06, \"successes\": 6, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.04, \"n_rollouts\": 10, \"total_rollouts\": 100, \"note\": \"JSON result found by diagnostic worker. Matches original seed44=4%. False positive failure due to no sentinel/W&B in evaluate.py.\"}}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.2, \"successes\": 20, \"total\": 100, \"benchmark\": \"object\", \"mode\": \"obs_only\", \"norm\": 0.2, \"seed\": 47}}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.08, \"total_successes\": 8, \"total_rollouts\": 100, \"seed\": 44, \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.15, \"total_episodes\": 100, \"successes\": 15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 2, \"bbq_sauce\": 3, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 4, \"orange_juice\": 3}}}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\"}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 0.04, \"total_episodes\": 100, \"successes\": 4, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 0, \"bbq_sauce\": 1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 1, \"milk\": 0, \"chocolate_pudding\": 1, \"orange_juice\": 0}}}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"precompute-v5-shard2\": {\"status\": \"DONE\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.16, \"total_success\": 16, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 18, \"total\": 200, \"tasks_done\": 10}}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"source\": \"json_file_verified_by_worker\"}}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}}, \"precompute-shard2\": {\"status\": \"DONE\"}, \"precompute-shard1\": {\"status\": \"DONE\"}, \"precompute-shard0\": {\"status\": \"DONE\"}, \"precompute-k5\": {\"status\": \"DONE\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\"}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.06, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.08, \"total_success\": 8, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_seed42\": \"-6pp (22% → 16%)\", \"vs_argmin_seed43\": \"-1pp (17% → 16%)\", \"pooled_2seed_obs_only_02\": \"19% (38/200)\", \"pooled_2seed_argmin\": \"14.5% (29/200)\"}}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.1, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\"}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\"}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\"}, \"eval-object-v6-full\": {\"status\": \"DONE\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}}, \"eval-mag-perdof-norm03-object\": {\"status\": \"DEPLOYED\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.12, \"total_success\": 12, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}}, \"crm-train-v3-norm\": {\"status\": \"DONE\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}}, \"crm-train-v1\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}}, \"crm-train-k5\": {\"status\": \"DONE\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\"}, \"eval-k5-spatial\": {\"status\": \"DONE\"}, \"eval-object-v7-full\": {\"status\": \"DONE\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\"}, \"eval-object-v5-full\": {\"status\": \"DONE\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\"}, \"eval-object-v4-full\": {\"status\": \"DONE\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\"}}, \"count\": 402, \"total\": 402, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9188}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 83_

<details><summary>Logged reasoning block</summary>

```text
Let me get the remaining adaptive_k data from bjb2-28827 (avoiding `|`), and parse the registry file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "b2c4688c-3a80-4d83-a3f0-f42f1c36ff8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZSHhwaP8aEWR9qcePDnbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1546,
      "cache_read_input_tokens": 68238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1546
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01R79aFrLPWTYNZJaiVjym7j`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep \"avg_actual_k\" /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "0cd0df0e-22a3-43b4-99b1-4d83376b36fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZSHhwaP8aEWR9qcePDnbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1546,
      "cache_read_input_tokens": 68238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1546
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

_source line 85 · 2026-05-20T03:55:15.728Z_

<details><summary>↩ Tool result · `toolu_01R79aFrLPWTYNZJaiVjym7j`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json:    \\\"avg_actual_k\\\": 4.787960435352926,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json:    \\\"avg_actual_k\\\": 3.722060671333692,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:    \\\"avg_actual_k\\\": 3.069946195234435,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:    \\\"avg_actual_k\\\": 3.149776927979605,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:    \\\"avg_actual_k\\\": 2.612278503669232,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:    \\\"avg_actual_k\\\": 2.5790465356038252,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "6fef7f35-6ae7-4e8c-b55d-c2ecd28f85c5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json:    \\\\\\\"avg_actual_k\\\\\\\": 4.787960435352926,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json:    \\\\\\\"avg_actual_k\\\\\\\": 3.722060671333692,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:    \\\\\\\"avg_actual_k\\\\\\\": 3.069946195234435,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:    \\\\\\\"avg_actual_k\\\\\\\": 3.149776927979605,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:    \\\\\\\"avg_actual_k\\\\\\\": 2.612278503669232,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:    \\\\\\\"avg_actual_k\\\\\\\": 2.5790465356038252,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json:    \\\"avg_actual_k\\\": 4.787960435352926,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json:    \\\"avg_actual_k\\\": 3.722060671333692,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:    \\\"avg_actual_k\\\": 3.069946195234435,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:    \\\"avg_actual_k\\\": 3.149776927979605,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:    \\\"avg_actual_k\\\": 2.612278503669232,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:    \\\"avg_actual_k\\\": 2.5790465356038252,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HKdNkvojUvibHWe1VPB3Xw`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep \"fast_path_ratio\" /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "f82ebda0-456b-4aac-bc45-078cfd3a74fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZSHhwaP8aEWR9qcePDnbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1546,
      "cache_read_input_tokens": 68238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1546
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

_source line 87 · 2026-05-20T03:55:17.176Z_

<details><summary>↩ Tool result · `toolu_01HKdNkvojUvibHWe1VPB3Xw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json:    \\\"fast_path_ratio\\\": 0.6515049455808842,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json:    \\\"fast_path_ratio\\\": 0.7847424160832884,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:    \\\"fast_path_ratio\\\": 0.8662567255956957,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:    \\\"fast_path_ratio\\\": 0.8562778840025494,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:    \\\"fast_path_ratio\\\": 0.923465187041346,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:    \\\"fast_path_ratio\\\": 0.9276191830495218,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "7073b0c0-d9ae-4bf9-8b5b-0620014d173b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json:    \\\\\\\"fast_path_ratio\\\\\\\": 0.6515049455808842,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json:    \\\\\\\"fast_path_ratio\\\\\\\": 0.7847424160832884,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:    \\\\\\\"fast_path_ratio\\\\\\\": 0.8662567255956957,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:    \\\\\\\"fast_path_ratio\\\\\\\": 0.8562778840025494,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:    \\\\\\\"fast_path_ratio\\\\\\\": 0.923465187041346,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:    \\\\\\\"fast_path_ratio\\\\\\\": 0.9276191830495218,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json:    \\\"fast_path_ratio\\\": 0.6515049455808842,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json:    \\\"fast_path_ratio\\\": 0.7847424160832884,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json:    \\\"fast_path_ratio\\\": 0.8662567255956957,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json:    \\\"fast_path_ratio\\\": 0.8562778840025494,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json:    \\\"fast_path_ratio\\\": 0.923465187041346,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json:    \\\"fast_path_ratio\\\": 0.9276191830495218,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Aza2EY37qLjsq5yvLkLWdG`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep \"fast_path_ratio\" /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "33fb67b2-0c56-4c9f-9f51-c18e562759d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZSHhwaP8aEWR9qcePDnbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1546,
      "cache_read_input_tokens": 68238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1546
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

_source line 89 · 2026-05-20T03:55:18.320Z_

<details><summary>↩ Tool result · `toolu_01Aza2EY37qLjsq5yvLkLWdG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    \\\"fast_path_ratio\\\": 0.7737388990759717,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "3dd52a3e-c70a-4837-ad24-44018c9de93a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    \\\\\\\"fast_path_ratio\\\\\\\": 0.7737388990759717,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    \\\"fast_path_ratio\\\": 0.7737388990759717,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011NACTbQHf1ZdBFKWbeDtdQ`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep \"fast_path_ratio\" /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_*.json",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "4f069826-5f5c-4a1d-a48d-1ba2afe7eb0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZSHhwaP8aEWR9qcePDnbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1546,
      "cache_read_input_tokens": 68238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1546
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

_source line 91 · 2026-05-20T03:55:19.096Z_

<details><summary>↩ Tool result · `toolu_011NACTbQHf1ZdBFKWbeDtdQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:    \\\"fast_path_ratio\\\": 0.6503401360544218,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:    \\\"fast_path_ratio\\\": 0.7613211244522037,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:    \\\"fast_path_ratio\\\": 0.8722045880825278,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:    \\\"fast_path_ratio\\\": 0.916059169084861,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "84343fc8-3737-4a95-afa6-975ff8a3dada",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:    \\\\\\\"fast_path_ratio\\\\\\\": 0.6503401360544218,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:    \\\\\\\"fast_path_ratio\\\\\\\": 0.7613211244522037,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:    \\\\\\\"fast_path_ratio\\\\\\\": 0.8722045880825278,\\\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:    \\\\\\\"fast_path_ratio\\\\\\\": 0.916059169084861,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json:    \\\"fast_path_ratio\\\": 0.6503401360544218,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json:    \\\"fast_path_ratio\\\": 0.7613211244522037,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json:    \\\"fast_path_ratio\\\": 0.8722045880825278,\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json:    \\\"fast_path_ratio\\\": 0.916059169084861,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 92_

<details open><summary>🔧 Tool call — Bash · `toolu_01MtpEb6dHhuY5DS5fHsx19P`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt') as f:\n    raw = json.load(f)\nresult = json.loads(raw['result'])\nfor exp in result:\n    eid = exp.get('experiment_id','')\n    status = exp.get('status','')\n    m = exp.get('metrics',{}) or {}\n    sr = m.get('overall_success_rate', m.get('success_rate', ''))\n    print(f'{eid} ;; {status} ;; SR={sr}')\n\"",
  "description": "Parse registry to list registered experiments with SR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "ceaeb6af-658d-450d-a99a-ae4299c88a38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZSHhwaP8aEWR9qcePDnbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1546,
      "cache_read_input_tokens": 68238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1546
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

_source line 93 · 2026-05-20T03:55:22.097Z_

<details><summary>↩ Tool result · reported error · `toolu_01MtpEb6dHhuY5DS5fHsx19P`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    eid = exp.get('experiment_id','')
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "80b2aa36-abff-424a-a67a-e7dd46a9468d",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 7, in &lt;module>\n    eid = exp.get('experiment_id','')\n          ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Assistant

_source line 94_

<details><summary>Logged reasoning block</summary>

```text
The registry parsing failed. The structure must be different. Let me look at the file directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "25e98edf-2deb-4d31-821f-0b826be659e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2wjnfU5rZt3MzVYosWbT6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2303,
      "cache_read_input_tokens": 69784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2303
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

_source line 95_

<details open><summary>🔧 Tool call — Read · `toolu_016LCK5swrWBXaGp2KjKq9pe`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "877f872c-0d51-4c4d-b3c7-fc751ce846d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2wjnfU5rZt3MzVYosWbT6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2303,
      "cache_read_input_tokens": 69784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2303
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

_source line 96 · 2026-05-20T03:55:28.702Z_

<details><summary>↩ Tool result · reported error · `toolu_016LCK5swrWBXaGp2KjKq9pe`</summary>

```text
File content (45348 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "bc4c1248-f481-4578-8580-f55261394966",
  "tool_use_result": "Error: File content (45348 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_01AoAuR9tW3Uu5RJpbTUy9ds`</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt | python3 -c \"\nimport sys, json\nraw = sys.stdin.read()\ndata = json.loads(raw[:raw.rfind(',')])  # partial parse attempt\n\" 2>&1; echo \"---\"; python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt') as f:\n    raw = json.load(f)\nresult = json.loads(raw['result'])\nprint(type(result), len(result) if isinstance(result, list) else 'not list')\nif isinstance(result, dict):\n    print(list(result.keys())[:10])\n    if 'experiments' in result:\n        exps = result['experiments']\n        print(type(exps), len(exps))\n        for e in exps[:2]:\n            print(type(e), list(e.keys()) if isinstance(e, dict) else e[:100])\n    elif isinstance(result, list):\n        for e in result[:2]:\n            print(type(e))\n\"",
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
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "0217db60-2aac-4c6d-9946-0ef7651fe70a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrnpVs599dGho16ssXfeUB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 72087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 258
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

_source line 98 · 2026-05-20T03:55:37.884Z_

<details><summary>↩ Tool result · `toolu_01AoAuR9tW3Uu5RJpbTUy9ds`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 4, in &lt;module>
    data = json.loads(raw[:raw.rfind(',')])  # partial parse attempt
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 361, in raw_decode
    obj, end = self.scan_once(s, idx)
               ~~~~~~~~~~~~~~^^^^^^^^
json.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 11 (char 10)
---
&lt;class 'dict'> not list
['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "487a4256-e1ee-4536-be89-4b7c817c3aaf",
  "tool_use_result": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 4, in &lt;module>\n    data = json.loads(raw[:raw.rfind(',')])  # partial parse attempt\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 361, in raw_decode\n    obj, end = self.scan_once(s, idx)\n               ~~~~~~~~~~~~~~^^^^^^^^\njson.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 11 (char 10)\n---\n&lt;class 'dict'> not list\n['success', 'data', 'error', 'metadata']",
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

_source line 99_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q7aDYsyxvWjMVWeB6do6JZ`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt') as f:\n    raw = json.load(f)\nresult = json.loads(raw['result'])\ndata = result['data']\nprint(type(data))\nif isinstance(data, list):\n    print(len(data))\n    for e in data[:3]:\n        print(e.get('experiment_id',''), e.get('status',''), (e.get('metrics') or {}).get('overall_success_rate',''))\nelif isinstance(data, dict):\n    print(list(data.keys())[:10])\n\"",
  "description": "Inspect registry data field"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "6a46238a-82ca-49fc-a721-6bceffa57ec1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161uTJtpjKk2yTAhZaNHjuR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 768,
      "cache_read_input_tokens": 72345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 768
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

_source line 100 · 2026-05-20T03:55:42.333Z_

<details><summary>↩ Tool result · `toolu_01Q7aDYsyxvWjMVWeB6do6JZ`</summary>

```text
&lt;class 'dict'>
['experiments', 'count', 'total', 'baseline']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "8d30a1cf-ebd3-4977-bb4f-49fa69d768df",
  "tool_use_result": {
    "stdout": "&lt;class 'dict'>\n['experiments', 'count', 'total', 'baseline']",
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

_source line 101_

<details open><summary>🔧 Tool call — Bash · `toolu_01LPAR85uyFUhm2nnnRiv4rL`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt') as f:\n    raw = json.load(f)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nfor e in exps:\n    eid = e.get('experiment_id','')\n    status = e.get('status','')\n    m = e.get('metrics') or {}\n    sr = m.get('overall_success_rate', m.get('success_rate', ''))\n    print(f'{eid} ;; {status} ;; SR={sr}')\n\"",
  "description": "Extract registry experiment IDs and metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "1cad500b-f732-4fd3-aa9d-c87e852ad543",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LALqhwsFaYCR9nUwgpn9nR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 337,
      "cache_read_input_tokens": 73113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 337
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

_source line 102 · 2026-05-20T03:55:47.138Z_

<details><summary>↩ Tool result · reported error · `toolu_01LPAR85uyFUhm2nnnRiv4rL`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    eid = e.get('experiment_id','')
          ^^^^^
AttributeError: 'str' object has no attribute 'get'
Total experiments: 402
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "e8d199c4-a00a-439a-ace5-745636306fdb",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 9, in &lt;module>\n    eid = e.get('experiment_id','')\n          ^^^^^\nAttributeError: 'str' object has no attribute 'get'\nTotal experiments: 402"
}
```

</details>

---

### Tool call

_source line 103_

<details open><summary>🔧 Tool call — Bash · `toolu_01H9XSxzGwfmNGeUtFP7rUne`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt') as f:\n    raw = json.load(f)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n# check what type elements are\nprint(type(exps[0]))\nif isinstance(exps[0], str):\n    # maybe it's a list of experiment ID strings\n    for e in exps[:10]:\n        print(e)\nelif isinstance(exps[0], dict):\n    print(list(exps[0].keys()))\n\"",
  "description": "Check experiment data type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "6fb680e3-5df4-4671-a049-fcc412192d59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSc8Pmcrhx6T2Fjbb4VQzb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 73450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 411
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

_source line 104 · 2026-05-20T03:55:52.370Z_

<details><summary>↩ Tool result · reported error · `toolu_01H9XSxzGwfmNGeUtFP7rUne`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    print(type(exps[0]))
               ~~~~^^^
KeyError: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "4ace7855-3936-416c-a36d-79e8e1872551",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 8, in &lt;module>\n    print(type(exps[0]))\n               ~~~~^^^\nKeyError: 0"
}
```

</details>

---

### Tool call

_source line 105_

<details open><summary>🔧 Tool call — Bash · `toolu_01BM9dA2ZWpQGVFjG8HZEWtC`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt') as f:\n    raw = json.load(f)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\nprint(type(exps))\nif isinstance(exps, dict):\n    keys = list(exps.keys())[:5]\n    for k in keys:\n        v = exps[k]\n        print(k, type(v))\n        if isinstance(v, dict):\n            m = v.get('metrics') or {}\n            sr = m.get('overall_success_rate', m.get('success_rate', ''))\n            print(f'  status={v.get(\\\"status\\\",\\\"\\\")} SR={sr}')\n\"",
  "description": "Check experiments dict structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "8137439e-87c5-4e5f-a09b-4103d8834f84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7ZvpL5XFRjwQ7ZRH4fUK1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 73861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 365
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

_source line 106 · 2026-05-20T03:55:58.891Z_

<details><summary>↩ Tool result · `toolu_01BM9dA2ZWpQGVFjG8HZEWtC`</summary>

```text
&lt;class 'dict'>
eval-vla-only-goal-seed49 &lt;class 'dict'>
  status=PREPARING SR=
eval-perdof-object-norm02-seed45-r3 &lt;class 'dict'>
  status=DONE SR=0.12
eval-obs-only-object-norm005-seed43 &lt;class 'dict'>
  status=DONE SR=
eval-perdof-object-norm02-seed48 &lt;class 'dict'>
  status=DONE SR=
eval-openvla-object-baseline-seed42 &lt;class 'dict'>
  status=DONE SR=
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "baea7707-b10c-4906-aea0-e5ed38f04da6",
  "tool_use_result": {
    "stdout": "&lt;class 'dict'>\neval-vla-only-goal-seed49 &lt;class 'dict'>\n  status=PREPARING SR=\neval-perdof-object-norm02-seed45-r3 &lt;class 'dict'>\n  status=DONE SR=0.12\neval-obs-only-object-norm005-seed43 &lt;class 'dict'>\n  status=DONE SR=\neval-perdof-object-norm02-seed48 &lt;class 'dict'>\n  status=DONE SR=\neval-openvla-object-baseline-seed42 &lt;class 'dict'>\n  status=DONE SR=",
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

_source line 107_

<details open><summary>🔧 Tool call — Bash · `toolu_012A42S4qtcQWfSJaWu8s5tY`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/234026bf-3bb5-4446-a09e-d1a78a19b295/tool-results/mcp-agent-ml-research-read_registry-1779249310828.txt') as f:\n    raw = json.load(f)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n# Print all with DONE status and their SR\nfor eid, v in exps.items():\n    if v.get('status') == 'DONE':\n        m = v.get('metrics') or {}\n        sr = m.get('overall_success_rate', m.get('success_rate', ''))\n        if sr:\n            print(f'{eid} :: SR={sr}')\n\"",
  "description": "List all DONE experiments with SR from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "1e0e0408-5100-44f5-ba9a-e5a45745978e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdcqUzxFzSzWyMtK3yW2ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 74226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
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

_source line 108 · 2026-05-20T03:56:03.644Z_

<details><summary>↩ Tool result · `toolu_012A42S4qtcQWfSJaWu8s5tY`</summary>

```text
eval-perdof-object-norm02-seed45-r3 :: SR=0.12
eval-vla-only-goal-seed44-r2 :: SR=0.73
eval-adaptive-k-p25-seed42 :: SR=0.15
eval-crm-goal-seed46 :: SR=0.72
eval-adaptive-k-p50-seed44 :: SR=0.14
eval-adaptive-k-p75-seed44 :: SR=0.16
eval-adaptive-k-p90-seed43 :: SR=0.14
eval-adaptive-k-p90-seed42 :: SR=0.12
eval-vla-only-spatial-seed47 :: SR=0.3
eval-crm-long-seed47 :: SR=0.17
eval-vla-only-object-seed48 :: SR=0.1
eval-vla-only-long-seed48 :: SR=0.14
eval-vla-only-object-seed50 :: SR=0.09
eval-crm-long-seed46 :: SR=0.18
eval-crm-goal-seed45-r2 :: SR=0.65
eval-crm-goal-seed44-r2 :: SR=0.64
eval-obs-only-spatial-norm02-seed43-r2 :: SR=0.34
eval-crm-long-seed45 :: SR=0.18
eval-vla-only-goal-seed43 :: SR=0.69
eval-vla-only-goal-seed42 :: SR=0.71
eval-vla-only-object-seed47 :: SR=0.1
eval-crm-long-seed44 :: SR=0.2
eval-crm-long-seed43 :: SR=0.15
eval-crm-long-seed42 :: SR=0.17
eval-crm-goal-seed42 :: SR=0.67
eval-crm-goal-seed43 :: SR=0.72
eval-vla-only-spatial-seed46 :: SR=0.3
eval-vla-only-long-seed47 :: SR=0.14
eval-vla-only-goal-seed45 :: SR=0.63
eval-vla-only-goal-seed46 :: SR=0.71
eval-vla-only-long-seed46 :: SR=0.18
eval-vla-only-long-seed45 :: SR=0.17
eval-perdof-object-norm003-seed47 :: SR=0.15
eval-perdof-object-norm005-seed47 :: SR=0.1
eval-vla-only-long-seed44 :: SR=0.12
eval-vla-only-long-seed42 :: SR=0.11
eval-vla-only-long-seed43 :: SR=0.13
eval-obs-only-spatial-norm02-seed47 :: SR=0.32
eval-random-selection-object-k5-seed45-r2 :: SR=0.07
eval-random-selection-object-k5-seed44-r2 :: SR=0.1
eval-random-selection-object-k5-seed43-r2 :: SR=0.11
eval-random-selection-object-k5-seed42-r2 :: SR=0.14
eval-obs-only-spatial-norm02-k5-seed44-r2 :: SR=0.37
eval-obs-only-spatial-norm02-k5-seed45-r2 :: SR=0.34
eval-vla-only-spatial-seed45 :: SR=0.27
eval-perdof-object-norm005-seed45-r2 :: SR=0.1
eval-vla-only-spatial-seed44 :: SR=0.31
eval-obs-only-object-default-seed48-r2 :: SR=0.17
eval-vla-only-spatial-seed43 :: SR=0.29
eval-vla-only-spatial-seed42 :: SR=0.3
eval-obs-only-spatial-norm02-seed44 :: SR=0.36
eval-obs-only-object-norm003-seed47-r2 :: SR=0.15
eval-obs-only-object-norm003-seed48 :: SR=0.15
eval-obs-only-spatial-norm02-seed45 :: SR=0.34
eval_obs_only_norm03_seed48 :: SR=0.16
eval_obs_only_norm01_seed48 :: SR=0.18
eval-lto-splitA-vla-only-r3 :: SR=0.14
eval-lto-splitA-vla-only-r2 :: SR=0.14
eval-lto-splitA-heldout-r2 :: SR=0.02
eval-perdof-object-norm003-seed48 :: SR=0.13
eval-scalar-object-seed45-r2 :: SR=0.07
eval-obs-only-spatial-norm02-k5-seed43 :: SR=0.32
eval-obs-only-object-norm02-k5-seed48 :: SR=0.18
eval-obs-only-spatial-norm02-k5-seed42 :: SR=0.35
eval-obs-only-object-norm02-k5-seed46 :: SR=0.16
eval-lto-splitA-vla-only-v2 :: SR=0.14
eval-lto-splitA-heldout-v2 :: SR=0.02
eval-perdof-object-norm03-seed47 :: SR=0.05
eval-obs-only-object-default-seed48 :: SR=0.17
eval-perdof-object-norm003-seed46 :: SR=0.09
eval-perdof-object-norm005-seed46 :: SR=0.11
eval-obs-only-object-norm02-k5-seed47 :: SR=0.13
eval-random-selection-object-seed45 :: SR=0.1
eval-obs-only-object-norm005-seed47 :: SR=0.14
eval-perdof-object-norm01-seed48 :: SR=0.12
eval-obs-only-object-default-seed47 :: SR=0.16
eval-perdof-object-norm03-seed46 :: SR=0.04
eval-obs-only-object-norm03-seed46 :: SR=0.17
eval-scalar-object-seed46 :: SR=0.09
eval-obs-only-object-norm01-seed47 :: SR=0.17
eval-obs-only-object-norm01-seed45-r2 :: SR=0.17
eval-perdof-object-norm003-seed43 :: SR=0.13
eval-perdof-object-norm005-seed43 :: SR=0.13
eval-obs-only-object-norm02-seed48-r2 :: SR=0.18
eval-obs-only-object-norm02-k5-seed45 :: SR=0.15
eval-vla-only-object-seed46 :: SR=0.13
eval-obs-only-object-norm01-seed48 :: SR=0.18
eval-obs-only-object-norm02-k5-seed44 :: SR=0.17
eval-random-selection-object-seed44 :: SR=0.13
eval-obs-only-object-norm01-seed46-r3 :: SR=0.18
eval-obs-only-object-norm005-seed45 :: SR=0.14
eval-random-selection-object-seed43 :: SR=0.09
eval-perdof-object-norm005-seed44 :: SR=0.09
eval-vla-only-object-seed45-r2 :: SR=0.11
eval-obs-only-object-norm03-seed48 :: SR=0.16
eval-obs-only-object-norm005-seed44 :: SR=0.16
eval-obs-only-object-norm02-k5-seed43 :: SR=0.19
eval-random-selection-object-seed42 :: SR=0.13
eval-perdof-object-norm02-seed43 :: SR=0.09
eval-perdof-object-norm01-seed46 :: SR=0.1
eval-obs-only-object-norm01-seed45 :: SR=0.14
eval-obs-only-object-norm02-k5-seed42 :: SR=0.14
eval-acr-spatial-v3 :: SR=0.025
eval-k1-crm-accg-object-seed44 :: SR=0.07
eval-k1-crm-accg-object-seed43 :: SR=0.12
eval-k1-crm-accg-object-seed42 :: SR=0.11
eval-obs-only-object-default-seed45 :: SR=0.12
eval-scalar-object-seed45 :: SR=0.09
eval-perdof-object-norm02-seed45 :: SR=0.09
eval-perdof-object-norm02-seed44 :: SR=0.1
eval-perdof-object-norm03-seed44-r2 :: SR=0.04
eval-obs-only-object-norm02-seed47 :: SR=0.2
eval-obs-only-object-norm02-seed46 :: SR=0.15
eval-obs-only-object-norm03-seed45-r2 :: SR=14
eval-direct-correction-object-seed42-r3 :: SR=0.14
eval-perdof-object-norm03-seed44 :: SR=0.04
eval-spatial-v7-full :: SR=0.3
eval-object-v8-full :: SR=0.13
eval-reconvla-spatial-v3 :: SR=0.34
eval-perdof-object-seed43 :: SR=0.12
eval-obs-only-object-seed43 :: SR=0.12
eval-argmin-object-seed43 :: SR=0.17
eval-argmin-only-spatial-r2 :: SR=0.34
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "7d0d904e-219b-478a-b2f5-50ae462277f2",
  "tool_use_result": {
    "stdout": "eval-perdof-object-norm02-seed45-r3 :: SR=0.12\neval-vla-only-goal-seed44-r2 :: SR=0.73\neval-adaptive-k-p25-seed42 :: SR=0.15\neval-crm-goal-seed46 :: SR=0.72\neval-adaptive-k-p50-seed44 :: SR=0.14\neval-adaptive-k-p75-seed44 :: SR=0.16\neval-adaptive-k-p90-seed43 :: SR=0.14\neval-adaptive-k-p90-seed42 :: SR=0.12\neval-vla-only-spatial-seed47 :: SR=0.3\neval-crm-long-seed47 :: SR=0.17\neval-vla-only-object-seed48 :: SR=0.1\neval-vla-only-long-seed48 :: SR=0.14\neval-vla-only-object-seed50 :: SR=0.09\neval-crm-long-seed46 :: SR=0.18\neval-crm-goal-seed45-r2 :: SR=0.65\neval-crm-goal-seed44-r2 :: SR=0.64\neval-obs-only-spatial-norm02-seed43-r2 :: SR=0.34\neval-crm-long-seed45 :: SR=0.18\neval-vla-only-goal-seed43 :: SR=0.69\neval-vla-only-goal-seed42 :: SR=0.71\neval-vla-only-object-seed47 :: SR=0.1\neval-crm-long-seed44 :: SR=0.2\neval-crm-long-seed43 :: SR=0.15\neval-crm-long-seed42 :: SR=0.17\neval-crm-goal-seed42 :: SR=0.67\neval-crm-goal-seed43 :: SR=0.72\neval-vla-only-spatial-seed46 :: SR=0.3\neval-vla-only-long-seed47 :: SR=0.14\neval-vla-only-goal-seed45 :: SR=0.63\neval-vla-only-goal-seed46 :: SR=0.71\neval-vla-only-long-seed46 :: SR=0.18\neval-vla-only-long-seed45 :: SR=0.17\neval-perdof-object-norm003-seed47 :: SR=0.15\neval-perdof-object-norm005-seed47 :: SR=0.1\neval-vla-only-long-seed44 :: SR=0.12\neval-vla-only-long-seed42 :: SR=0.11\neval-vla-only-long-seed43 :: SR=0.13\neval-obs-only-spatial-norm02-seed47 :: SR=0.32\neval-random-selection-object-k5-seed45-r2 :: SR=0.07\neval-random-selection-object-k5-seed44-r2 :: SR=0.1\neval-random-selection-object-k5-seed43-r2 :: SR=0.11\neval-random-selection-object-k5-seed42-r2 :: SR=0.14\neval-obs-only-spatial-norm02-k5-seed44-r2 :: SR=0.37\neval-obs-only-spatial-norm02-k5-seed45-r2 :: SR=0.34\neval-vla-only-spatial-seed45 :: SR=0.27\neval-perdof-object-norm005-seed45-r2 :: SR=0.1\neval-vla-only-spatial-seed44 :: SR=0.31\neval-obs-only-object-default-seed48-r2 :: SR=0.17\neval-vla-only-spatial-seed43 :: SR=0.29\neval-vla-only-spatial-seed42 :: SR=0.3\neval-obs-only-spatial-norm02-seed44 :: SR=0.36\neval-obs-only-object-norm003-seed47-r2 :: SR=0.15\neval-obs-only-object-norm003-seed48 :: SR=0.15\neval-obs-only-spatial-norm02-seed45 :: SR=0.34\neval_obs_only_norm03_seed48 :: SR=0.16\neval_obs_only_norm01_seed48 :: SR=0.18\neval-lto-splitA-vla-only-r3 :: SR=0.14\neval-lto-splitA-vla-only-r2 :: SR=0.14\neval-lto-splitA-heldout-r2 :: SR=0.02\neval-perdof-object-norm003-seed48 :: SR=0.13\neval-scalar-object-seed45-r2 :: SR=0.07\neval-obs-only-spatial-norm02-k5-seed43 :: SR=0.32\neval-obs-only-object-norm02-k5-seed48 :: SR=0.18\neval-obs-only-spatial-norm02-k5-seed42 :: SR=0.35\neval-obs-only-object-norm02-k5-seed46 :: SR=0.16\neval-lto-splitA-vla-only-v2 :: SR=0.14\neval-lto-splitA-heldout-v2 :: SR=0.02\neval-perdof-object-norm03-seed47 :: SR=0.05\neval-obs-only-object-default-seed48 :: SR=0.17\neval-perdof-object-norm003-seed46 :: SR=0.09\neval-perdof-object-norm005-seed46 :: SR=0.11\neval-obs-only-object-norm02-k5-seed47 :: SR=0.13\neval-random-selection-object-seed45 :: SR=0.1\neval-obs-only-object-norm005-seed47 :: SR=0.14\neval-perdof-object-norm01-seed48 :: SR=0.12\neval-obs-only-object-default-seed47 :: SR=0.16\neval-perdof-object-norm03-seed46 :: SR=0.04\neval-obs-only-object-norm03-seed46 :: SR=0.17\neval-scalar-object-seed46 :: SR=0.09\neval-obs-only-object-norm01-seed47 :: SR=0.17\neval-obs-only-object-norm01-seed45-r2 :: SR=0.17\neval-perdof-object-norm003-seed43 :: SR=0.13\neval-perdof-object-norm005-seed43 :: SR=0.13\neval-obs-only-object-norm02-seed48-r2 :: SR=0.18\neval-obs-only-object-norm02-k5-seed45 :: SR=0.15\neval-vla-only-object-seed46 :: SR=0.13\neval-obs-only-object-norm01-seed48 :: SR=0.18\neval-obs-only-object-norm02-k5-seed44 :: SR=0.17\neval-random-selection-object-seed44 :: SR=0.13\neval-obs-only-object-norm01-seed46-r3 :: SR=0.18\neval-obs-only-object-norm005-seed45 :: SR=0.14\neval-random-selection-object-seed43 :: SR=0.09\neval-perdof-object-norm005-seed44 :: SR=0.09\neval-vla-only-object-seed45-r2 :: SR=0.11\neval-obs-only-object-norm03-seed48 :: SR=0.16\neval-obs-only-object-norm005-seed44 :: SR=0.16\neval-obs-only-object-norm02-k5-seed43 :: SR=0.19\neval-random-selection-object-seed42 :: SR=0.13\neval-perdof-object-norm02-seed43 :: SR=0.09\neval-perdof-object-norm01-seed46 :: SR=0.1\neval-obs-only-object-norm01-seed45 :: SR=0.14\neval-obs-only-object-norm02-k5-seed42 :: SR=0.14\neval-acr-spatial-v3 :: SR=0.025\neval-k1-crm-accg-object-seed44 :: SR=0.07\neval-k1-crm-accg-object-seed43 :: SR=0.12\neval-k1-crm-accg-object-seed42 :: SR=0.11\neval-obs-only-object-default-seed45 :: SR=0.12\neval-scalar-object-seed45 :: SR=0.09\neval-perdof-object-norm02-seed45 :: SR=0.09\neval-perdof-object-norm02-seed44 :: SR=0.1\neval-perdof-object-norm03-seed44-r2 :: SR=0.04\neval-obs-only-object-norm02-seed47 :: SR=0.2\neval-obs-only-object-norm02-seed46 :: SR=0.15\neval-obs-only-object-norm03-seed45-r2 :: SR=14\neval-direct-correction-object-seed42-r3 :: SR=0.14\neval-perdof-object-norm03-seed44 :: SR=0.04\neval-spatial-v7-full :: SR=0.3\neval-object-v8-full :: SR=0.13\neval-reconvla-spatial-v3 :: SR=0.34\neval-perdof-object-seed43 :: SR=0.12\neval-obs-only-object-seed43 :: SR=0.12\neval-argmin-object-seed43 :: SR=0.17\neval-argmin-only-spatial-r2 :: SR=0.34",
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

_source line 109_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also check which experiments from the servers are NOT in the registry. Let me compile a complete list of all files found on servers, then compare to the registry.

Let me also look for experiments that are in PREPARING or RUNNING status.

Let me compile the full results now.

First, let me list all the files from the 4 servers and their overall_success_rate values:

**bjb2-28827 (all eval files with SR):**
- eval_adaptive_k_p25_seed43: SR=0.13, avg_K=4.788, fast_path=0.652


- eval_adaptive_k_p50_seed42: SR=0.16, avg_K=3.722, fast_path=0.785
- eval_adaptive_k_p75_seed42: SR=0.12, avg_K=3.070, fast_path=0.866
- eval_adaptive_k_p75_seed43: SR=0.13, avg_K=3.150, fast_path=0.856
- eval_adaptive_k_p90_seed43: SR=0.14, avg_K=2.612, fast_path=0.923
- eval_adaptive_k_p90_seed44

: SR=0.14, avg_K=2.579, fast_path=0.928

Now I'm looking at the results from the CRM and VLA-based approaches, which show notably higher success rates around 0.64-0.73, along with some longer observation experiments that are tracking lower performance in the 0.12-0.20 range. Looking at the success rates across these different evaluation configurations, I'm seeing a range from 0.00 to 0.19, with the observation-only variants generally performing better than the per-DOF approaches. The norm02 and norm03 configurations seem to be among the stronger performers, while the per-DOF variants are showing more inconsistent results. Looking at the success rates across different evaluation configurations, I'm seeing that the spatial observation-only models perform significantly better, with success rates in the 0.31-0.37 range, while the other variants cluster around 0.09-0.13. Looking at more evaluation results across different configurations and normalization parameters, with success rates ranging from 0.13 to 0.36, showing how various object observation settings and normalization values impact performance. Looking at the success rates across more configuration variants with different normalization parameters and model architectures, I'm seeing a range from near zero to around 0.17, with most clustering in the 0.10-0.15 range. Looking at the additional results for bjb1-32546, the adaptive k experiments show diminishing returns as the fast path percentage increases, while the goal-based evaluations perform significantly better with success rates in the 0.64-0.71 range, and the k1 crm experiments cluster around 0.07-0.12. Looking at the success rates across these object observation-only configurations, most are clustering around 0.15-0.18, with a few dipping to 0.14 and one reaching 0.19 from the earlier set. Looking at the success rates across more evaluation configurations, I'm seeing a range from 0.04 to 0.32, with the spatial observation-only variants performing notably better than the object-based approaches. Looking at the success rates for the remaining experiments, I'm seeing some lower performance on the object-based tasks compared to the spatial ones. Now I need to cross-reference these results with what's already in the registry, mapping the underscore naming convention to the dash-separated format to identify which experiments are new versus already recorded. Looking at the success rates across the remaining evaluation runs, most of the VLA-only long and spatial variants are passing with relatively low success rates in the 0.11 to 0.3 range, with a few slightly higher at 0.17 to 0.18.

Now I need to identify which evaluations are new and not already in the registry, starting with checking eval_adaptive_k_p25_seed43 and eval_adaptive_k_p50_seed42 to see if they're listed. Continuing through the evaluation configs, I'm seeing more entries that aren't registered—several goal observation variants and spatial observation runs across different seeds and model checkpoints. Some spatial configs like the k5 variant and one of the r2 runs do show up in the registry, but most of the others are missing.

Now I'm realizing the naming convention between the file system and registry isn't straightforward—the files use underscores while the registry uses hyphens, and the structure doesn't map one-to-one. I need to look more carefully at how these actually correspond. I see the registry naming doesn't follow a simple pattern—the semantic labels don't directly correspond to the filenames. Let me identify which experiments are actually missing from the registry by checking the seed ranges for each experiment type. Looking at what's registered, I notice VLA-only-Goal has seeds 42-46 plus the r2 variants, but nothing beyond seed46, so seeds 47-50 appear to be unregistered.

For the spatial experiments, there are gaps like seed46_r2 and seed48 for CRM-Spatial, and seed48-50 for VLA-only-Spatial. The adaptive-k variants are particularly sparse—several percentile-seed combinations like p25_seed43 and p50_seed42 through p75_seed43 aren't showing up in the registry. Now I'm checking whether the Goal-ObsOnly variants with the norm02 suffix represent distinct experiments or if they're just different processing versions of the same underlying runs. Rather than trying to perfectly match everything to the registry, I should just compile the data and flag the uncertain cases. The user asked about eval_adaptive_k_p25_seed44 specifically, which doesn't exist on any server yet. Now I'm organizing everything by benchmark into a comprehensive table as requested, starting with the clearly new entries I've identified across the different experiment types.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "3df90cae-3c8a-4769-940a-fc212b8eafa8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Prz22495CEvLbPRMkVk5No",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2829,
      "cache_read_input_tokens": 74730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2829
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

_source line 110_

数据采集完毕。以下是全服务器实验结果汇总：

---

## 一、按 Benchmark 分组汇总

### 1. CRM-Spatial (obs_only_spatial)

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_spatial_obs_only_norm02_seed44 | 0.36 | 已注册 |
| bjb2-28827 | eval_spatial_obs_only_norm02_seed46_r2 | 0.33 | **未注册** |
| bjb2-28827 | eval_spatial_obs_only_norm02_k5_seed42 | 0.35 | 已注册 |
| bjb2-28827 | eval_spatial_obs_only_norm02_k5_seed44 | 0.37 | 已注册 |
| bjb2-28827 | eval_spatial_obs_only_norm02_k5_seed45 | 0.34 | 已注册 |
| bjb1-18228 | eval_spatial_obs_only_norm02_seed47 | 0.32 | 已注册 |
| bjb1-32546 | eval_spatial_obs_only_norm02_seed43_r2 | 0.34 | 已注册 |
| bjb1-32546 | eval_spatial_obs_only_norm02_seed45 | 0.34 | 已注册 |
| bjb1-32546 | eval_spatial_obs_only_norm02_seed47 | 0.32 | 已注册 |
| bjb1-32546 | eval_spatial_obs_only_norm02_seed48 | 0.35 | **未注册** |
| bjb1-32546 | eval_spatial_obs_only_norm02_k5_seed43 | 0.32 | 已注册 |
| bjb2-40593 | eval_spatial_obs_only_norm02_seed44 | 0.32 | 重复/不同seed |

### 2. VLA-only-Spatial

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_spatial_vla_only_seed44 | 0.31 | 已注册 |
| bjb1-18228 | eval_spatial_vla_only_seed43 | 0.29 | 已注册 |
| bjb1-18228 | eval_spatial_vla_only_seed50 | 0.30 | **未注册** |
| bjb1-32546 | eval_spatial_vla_only_seed42 | 0.30 | 已注册 |
| bjb1-32546 | eval_spatial_vla_only_seed45 | 0.27 | 已注册 |
| bjb1-32546 | eval_spatial_vla_only_seed46 | 0.30 | 已注册 |
| bjb1-32546 | eval_spatial_vla_only_seed47 | 0.30 | 已注册 |
| bjb1-32546 | eval_spatial_vla_only_seed48 | 0.30 | **未注册** |
| bjb1-32546 | eval_spatial_vla_only_seed49 | 0.29 | **未注册** |

### 3. CRM-Long (long_obs_only)

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_long_obs_only_norm02_seed42 | 0.17 | 已注册 |
| bjb2-28827 | eval_long_obs_only_norm02_seed43 | 0.15 | 已注册 |
| bjb2-28827 | eval_long_obs_only_norm02_seed44 | 0.20 | 已注册 |
| bjb2-28827 | eval_crm_long_seed47 | 0.17 | 已注册 |
| bjb1-18228 | eval_long_obs_only_norm02_seed45 | 0.18 | 已注册 |
| bjb1-18228 | eval_long_obs_only_norm02_seed46 | 0.18 | 已注册 |

### 4. VLA-only-Long

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb1-18228 | eval_long_vla_only_seed45 | 0.17 | 已注册 |
| bjb1-18228 | eval_long_vla_only_seed48 | 0.14 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed42 | 0.11 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed43 | 0.13 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed44 | 0.12 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed46 | 0.18 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed47 | 0.11 | 已注册 |

### 5. CRM-Goal / Goal-ObsOnly

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_crm_goal_seed46 | 0.72 | 已注册 |
| bjb2-28827 | eval_crm_goal_seed45_r2 | 0.65 | 已注册 |
| bjb2-28827 | eval_crm_goal_seed44_r2 | 0.64 | 已注册 |
| bjb1-18228 | eval_goal_obs_only_norm02_seed42 | 0.67 | 可能=crm-goal-seed42(已注册) |
| bjb1-18228 | eval_goal_obs_only_norm02_seed43 | 0.72 | 可能=crm-goal-seed43(已注册) |
| bjb1-32546 | eval_goal_obs_only_norm02_seed44 | 0.64 | 可能=crm-goal-seed44-r2(已注册) |
| bjb1-32546 | eval_goal_obs_only_norm02_seed45 | 0.65 | 可能=crm-goal-seed45-r2(已注册) |

### 6. VLA-only-Goal

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_goal_vla_only_seed44_r2 | 0.73 | 已注册 |
| bjb2-28827 | eval_goal_vla_only_seed45 | 0.63 | 已注册 |
| bjb1-32546 | eval_goal_vla_only_seed42 | 0.71 | 已注册 |
| bjb1-32546 | eval_goal_vla_only_seed43 | 0.69 | 已注册 |
| bjb1-32546 | eval_goal_vla_only_seed46 | 0.71 | 已注册 |

### 7. Adaptive-K

| 服务器 | 文件名 | SR | avg_K | fast_path | 备注 |
|--------|--------|-----|-------|-----------|------|
| bjb2-28827 | eval_adaptive_k_p25_seed43 | 0.13 | 4.788 | 0.652 | **未注册** |
| bjb2-28827 | eval_adaptive_k_p50_seed42 | 0.16 | 3.722 | 0.785 | **未注册** |
| bjb2-28827 | eval_adaptive_k_p75_seed42 | 0.12 | 3.070 | 0.866 | **未注册** |
| bjb2-28827 | eval_adaptive_k_p75_seed43 | 0.13 | 3.150 | 0.856 | **未注册** |
| bjb2-28827 | eval_adaptive_k_p90_seed43 | 0.14 | 2.612 | 0.923 | 已注册 |
| bjb2-28827 | eval_adaptive_k_p90_seed44 | 0.14 | 2.579 | 0.928 | **未注册** |
| bjb1-18228 | eval_adaptive_k_p50_seed43 | 0.16 | 3.810 | 0.774 | **未注册** |
| bjb1-32546 | eval_adaptive_k_p25_seed42 | 0.15 | 4.797 | 0.650 | 已注册 |
| bjb1-32546 | eval_adaptive_k_p50_seed44 | 0.14 | 3.909 | 0.761 | 已注册 |
| bjb1-32546 | eval_adaptive_k_p75_seed44 | 0.16 | 3.022 | 0.872 | 已注册 |
| bjb1-32546 | eval_adaptive_k_p90_seed42 | 0.12 | 2.672 | 0.916 | 已注册 |

---

## 二、未注册结果汇总

| Benchmark | 文件 | SR | 服务器 |
|-----------|------|-----|--------|
| CRM-Spatial | seed46_r2 | 0.33 | bjb2-28827 |
| CRM-Spatial | seed48 | 0.35 | bjb1-32546 |
| VLA-Spatial | seed48 | 0.30 | bjb1-32546 |
| VLA-Spatial | seed49 | 0.29 | bjb1-32546 |
| VLA-Spatial | seed50 | 0.30 | bjb1-18228 |
| Adaptive-K | p25_seed43 | 0.13 | bjb2-28827 |
| Adaptive-K | p50_seed42 | 0.16 | bjb2-28827 |
| Adaptive-K | p50_seed43 | 0.16 | bjb1-18228 |
| Adaptive-K | p75_seed42 | 0.12 | bjb2-28827 |
| Adaptive-K | p75_seed43 | 0.13 | bjb2-28827 |
| Adaptive-K | p90_seed44 | 0.14 | bjb2-28827 |

**Adaptive-K P25-seed44：四台服务器均未找到此文件。**

---

## 三、关键发现

1. **CRM-Spatial** 全 seed 平均 SR ≈ 0.33-0.37 (k3) / 0.32-0.37 (k5)，一致性好
2. **VLA-only-Spatial** 平均 SR ≈ 0.29-0.31，低于 CRM-Spatial 约 5pp
3. **CRM-Long** 平均 SR ≈ 0.15-0.20
4. **VLA-only-Long** 平均 SR ≈ 0.11-0.18
5. **CRM-Goal** SR ≈ 0.64-0.72；**VLA-only-Goal** SR ≈ 0.63-0.73 — 差距小
6. **Adaptive-K** 趋势清晰：p25(avg_K≈4.8, SR≈0.14) → p50(avg_K≈3.8, SR≈0.15) → p75(avg_K≈3.1, SR≈0.14) → p90(avg_K≈2.6, SR≈0.13)，K 随 percentile 下降，SR 差异不大
7. 共 **11 个实验未注册到 registry**，以 Adaptive-K 新 seed 和 Spatial 高编号 seed 为主

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "uuid": "a24ac4a6-d486-43ea-b334-c4bd6ee94e82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Prz22495CEvLbPRMkVk5No",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2829,
      "cache_read_input_tokens": 74730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2829
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

_source line 111_

数据采集完毕。以下是全服务器实验结果汇总：

---

## 一、按 Benchmark 分组汇总

### 1. CRM-Spatial (obs_only_spatial)

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_spatial_obs_only_norm02_seed44 | 0.36 | 已注册 |
| bjb2-28827 | eval_spatial_obs_only_norm02_seed46_r2 | 0.33 | **未注册** |
| bjb2-28827 | eval_spatial_obs_only_norm02_k5_seed42 | 0.35 | 已注册 |
| bjb2-28827 | eval_spatial_obs_only_norm02_k5_seed44 | 0.37 | 已注册 |
| bjb2-28827 | eval_spatial_obs_only_norm02_k5_seed45 | 0.34 | 已注册 |
| bjb1-18228 | eval_spatial_obs_only_norm02_seed47 | 0.32 | 已注册 |
| bjb1-32546 | eval_spatial_obs_only_norm02_seed43_r2 | 0.34 | 已注册 |
| bjb1-32546 | eval_spatial_obs_only_norm02_seed45 | 0.34 | 已注册 |
| bjb1-32546 | eval_spatial_obs_only_norm02_seed47 | 0.32 | 已注册 |
| bjb1-32546 | eval_spatial_obs_only_norm02_seed48 | 0.35 | **未注册** |
| bjb1-32546 | eval_spatial_obs_only_norm02_k5_seed43 | 0.32 | 已注册 |
| bjb2-40593 | eval_spatial_obs_only_norm02_seed44 | 0.32 | 重复/不同seed |

### 2. VLA-only-Spatial

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_spatial_vla_only_seed44 | 0.31 | 已注册 |
| bjb1-18228 | eval_spatial_vla_only_seed43 | 0.29 | 已注册 |
| bjb1-18228 | eval_spatial_vla_only_seed50 | 0.30 | **未注册** |
| bjb1-32546 | eval_spatial_vla_only_seed42 | 0.30 | 已注册 |
| bjb1-32546 | eval_spatial_vla_only_seed45 | 0.27 | 已注册 |
| bjb1-32546 | eval_spatial_vla_only_seed46 | 0.30 | 已注册 |
| bjb1-32546 | eval_spatial_vla_only_seed47 | 0.30 | 已注册 |
| bjb1-32546 | eval_spatial_vla_only_seed48 | 0.30 | **未注册** |
| bjb1-32546 | eval_spatial_vla_only_seed49 | 0.29 | **未注册** |

### 3. CRM-Long (long_obs_only)

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_long_obs_only_norm02_seed42 | 0.17 | 已注册 |
| bjb2-28827 | eval_long_obs_only_norm02_seed43 | 0.15 | 已注册 |
| bjb2-28827 | eval_long_obs_only_norm02_seed44 | 0.20 | 已注册 |
| bjb2-28827 | eval_crm_long_seed47 | 0.17 | 已注册 |
| bjb1-18228 | eval_long_obs_only_norm02_seed45 | 0.18 | 已注册 |
| bjb1-18228 | eval_long_obs_only_norm02_seed46 | 0.18 | 已注册 |

### 4. VLA-only-Long

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb1-18228 | eval_long_vla_only_seed45 | 0.17 | 已注册 |
| bjb1-18228 | eval_long_vla_only_seed48 | 0.14 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed42 | 0.11 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed43 | 0.13 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed44 | 0.12 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed46 | 0.18 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed47 | 0.11 | 已注册 |

### 5. CRM-Goal / Goal-ObsOnly

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_crm_goal_seed46 | 0.72 | 已注册 |
| bjb2-28827 | eval_crm_goal_seed45_r2 | 0.65 | 已注册 |
| bjb2-28827 | eval_crm_goal_seed44_r2 | 0.64 | 已注册 |
| bjb1-18228 | eval_goal_obs_only_norm02_seed42 | 0.67 | 可能=crm-goal-seed42(已注册) |
| bjb1-18228 | eval_goal_obs_only_norm02_seed43 | 0.72 | 可能=crm-goal-seed43(已注册) |
| bjb1-32546 | eval_goal_obs_only_norm02_seed44 | 0.64 | 可能=crm-goal-seed44-r2(已注册) |
| bjb1-32546 | eval_goal_obs_only_norm02_seed45 | 0.65 | 可能=crm-goal-seed45-r2(已注册) |

### 6. VLA-only-Goal

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_goal_vla_only_seed44_r2 | 0.73 | 已注册 |
| bjb2-28827 | eval_goal_vla_only_seed45 | 0.63 | 已注册 |
| bjb1-32546 | eval_goal_vla_only_seed42 | 0.71 | 已注册 |
| bjb1-32546 | eval_goal_vla_only_seed43 | 0.69 | 已注册 |
| bjb1-32546 | eval_goal_vla_only_seed46 | 0.71 | 已注册 |

### 7. Adaptive-K

| 服务器 | 文件名 | SR | avg_K | fast_path | 备注 |
|--------|--------|-----|-------|-----------|------|
| bjb2-28827 | eval_adaptive_k_p25_seed43 | 0.13 | 4.788 | 0.652 | **未注册** |
| bjb2-28827 | eval_adaptive_k_p50_seed42 | 0.16 | 3.722 | 0.785 | **未注册** |
| bjb2-28827 | eval_adaptive_k_p75_seed42 | 0.12 | 3.070 | 0.866 | **未注册** |
| bjb2-28827 | eval_adaptive_k_p75_seed43 | 0.13 | 3.150 | 0.856 | **未注册** |
| bjb2-28827 | eval_adaptive_k_p90_seed43 | 0.14 | 2.612 | 0.923 | 已注册 |
| bjb2-28827 | eval_adaptive_k_p90_seed44 | 0.14 | 2.579 | 0.928 | **未注册** |
| bjb1-18228 | eval_adaptive_k_p50_seed43 | 0.16 | 3.810 | 0.774 | **未注册** |
| bjb1-32546 | eval_adaptive_k_p25_seed42 | 0.15 | 4.797 | 0.650 | 已注册 |
| bjb1-32546 | eval_adaptive_k_p50_seed44 | 0.14 | 3.909 | 0.761 | 已注册 |
| bjb1-32546 | eval_adaptive_k_p75_seed44 | 0.16 | 3.022 | 0.872 | 已注册 |
| bjb1-32546 | eval_adaptive_k_p90_seed42 | 0.12 | 2.672 | 0.916 | 已注册 |

---

## 二、未注册结果汇总

| Benchmark | 文件 | SR | 服务器 |
|-----------|------|-----|--------|
| CRM-Spatial | seed46_r2 | 0.33 | bjb2-28827 |
| CRM-Spatial | seed48 | 0.35 | bjb1-32546 |
| VLA-Spatial | seed48 | 0.30 | bjb1-32546 |
| VLA-Spatial | seed49 | 0.29 | bjb1-32546 |
| VLA-Spatial | seed50 | 0.30 | bjb1-18228 |
| Adaptive-K | p25_seed43 | 0.13 | bjb2-28827 |
| Adaptive-K | p50_seed42 | 0.16 | bjb2-28827 |
| Adaptive-K | p50_seed43 | 0.16 | bjb1-18228 |
| Adaptive-K | p75_seed42 | 0.12 | bjb2-28827 |
| Adaptive-K | p75_seed43 | 0.13 | bjb2-28827 |
| Adaptive-K | p90_seed44 | 0.14 | bjb2-28827 |

**Adaptive-K P25-seed44：四台服务器均未找到此文件。**

---

## 三、关键发现

1. **CRM-Spatial** 全 seed 平均 SR ≈ 0.33-0.37 (k3) / 0.32-0.37 (k5)，一致性好
2. **VLA-only-Spatial** 平均 SR ≈ 0.29-0.31，低于 CRM-Spatial 约 5pp
3. **CRM-Long** 平均 SR ≈ 0.15-0.20
4. **VLA-only-Long** 平均 SR ≈ 0.11-0.18
5. **CRM-Goal** SR ≈ 0.64-0.72；**VLA-only-Goal** SR ≈ 0.63-0.73 — 差距小
6. **Adaptive-K** 趋势清晰：p25(avg_K≈4.8, SR≈0.14) → p50(avg_K≈3.8, SR≈0.15) → p75(avg_K≈3.1, SR≈0.14) → p90(avg_K≈2.6, SR≈0.13)，K 随 percentile 下降，SR 差异不大
7. 共 **11 个实验未注册到 registry**，以 Adaptive-K 新 seed 和 Spatial 高编号 seed 为主

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 325552,
  "duration_api_ms": 322384,
  "num_turns": 45,
  "stop_reason": "end_turn",
  "session_id": "234026bf-3bb5-4446-a09e-d1a78a19b295",
  "total_cost_usd": 1.4482774999999999,
  "usage": {
    "input_tokens": 21,
    "cache_creation_input_tokens": 65718,
    "cache_read_input_tokens": 914168,
    "output_tokens": 23158,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 65718,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 9847,
        "cache_read_input_tokens": 74730,
        "cache_creation_input_tokens": 2829,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2829
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1326,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001401,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 21,
      "outputTokens": 23158,
      "cacheReadInputTokens": 914168,
      "cacheCreationInputTokens": 65718,
      "webSearchRequests": 0,
      "costUSD": 1.4468765,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6b8e03c4-464c-4df2-bdd6-33fb0581676a"
}
```

</details>

---
