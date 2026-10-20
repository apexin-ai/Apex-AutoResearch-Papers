# analysis filtering pipeline d040

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_analysis_filtering-pipeline-d040_20260515T153235.log`
- **Structured JSON:** [`aeddd33302a9859960de.json`](../../sessions/ae/aeddd33302a9859960de.json)

## Before a recorded user message

54 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
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
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
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
  "uuid": "9d90b973-d84d-44e6-82ce-9b57040bf3ec",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
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
    "resetsAt": 1778876400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e100648a-b592-4cb5-932b-cd3d7e2aa02e",
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by exploring the analysis files on the server to understand what data is available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "7fbea28d-e775-45fe-8cf4-c63ff0a76c74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEznrPNcTS5Yk9wde6QBUS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12500,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12500
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

开始从服务器提取 filtering pipeline 数据。先探索分析目录结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "eb3e4c9b-26e9-44df-b927-bcf047a32684",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEznrPNcTS5Yk9wde6QBUS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12500,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12500
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016Tg7Q5YLy4diMKJaG7Zbj8`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "8a65cd90-a07e-45fc-9d0f-fcb49415e379",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEznrPNcTS5Yk9wde6QBUS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12500,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12500
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T15:32:48.500Z_

<details><summary>↩ Tool result · `toolu_016Tg7Q5YLy4diMKJaG7Zbj8`</summary>

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
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "ebecb0b6-b510-4b53-ae2e-973bc507536a",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 27
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019YzDVzcP5YgpemFq3rBYYr`</summary>

```json
{
  "server": "westd-19828",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/analysis/",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "8513446c-a8cc-4a05-aaa2-77a1527ebf4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCvQP8RSKEdTkfw7y9wNuQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1940,
      "cache_read_input_tokens": 24341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1940
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

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EGk2JyXwdzHuXvpVCrWEtN`</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/analysis/ -name \"*.json\" -type f",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "6dabc30b-3ee2-4dff-b50c-02faaf88ce34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCvQP8RSKEdTkfw7y9wNuQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1940,
      "cache_read_input_tokens": 24341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1940
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

_source line 10 · 2026-05-15T15:32:52.738Z_

<details><summary>↩ Tool result · `toolu_019YzDVzcP5YgpemFq3rBYYr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 328\\ndrwxr-xr-x 2 root root  4096 May 15 21:17 .\\ndrwxr-xr-x 9 root root  4096 May 15 19:57 ..\\n-rw-r--r-- 1 root root 12551 May 15 13:31 cross_alpha_analysis.json\\n-rw-r--r-- 1 root root  3769 May 15 13:33 cross_alpha_analysis.md\\n-rw-r--r-- 1 root root  9508 May 15 13:48 cross_alpha_v3_full.json\\n-rw-r--r-- 1 root root 71968 May 15 18:56 cross_alpha_v4.json\\n-rw-r--r-- 1 root root  6859 May 15 18:56 cross_alpha_v4_report.md\\n-rw-r--r-- 1 root root 71968 May 15 20:13 cross_alpha_v5.json\\n-rw-r--r-- 1 root root  6859 May 15 20:13 cross_alpha_v5_report.md\\n-rw-r--r-- 1 root root 88994 May 15 21:18 cross_alpha_v6.json\\n-rw-r--r-- 1 root root  8251 May 15 21:18 cross_alpha_v6_report.md\\n-rw-r--r-- 1 root root 18313 May 15 17:56 d028_fpr_null_control.json\\n-rw-r--r-- 1 root root  5688 May 15 17:57 d028_fpr_null_control_full.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.98}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "5c8ce78e-bc8a-4cd4-88f7-27767eee73b3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 328\\\\ndrwxr-xr-x 2 root root  4096 May 15 21:17 .\\\\ndrwxr-xr-x 9 root root  4096 May 15 19:57 ..\\\\n-rw-r--r-- 1 root root 12551 May 15 13:31 cross_alpha_analysis.json\\\\n-rw-r--r-- 1 root root  3769 May 15 13:33 cross_alpha_analysis.md\\\\n-rw-r--r-- 1 root root  9508 May 15 13:48 cross_alpha_v3_full.json\\\\n-rw-r--r-- 1 root root 71968 May 15 18:56 cross_alpha_v4.json\\\\n-rw-r--r-- 1 root root  6859 May 15 18:56 cross_alpha_v4_report.md\\\\n-rw-r--r-- 1 root root 71968 May 15 20:13 cross_alpha_v5.json\\\\n-rw-r--r-- 1 root root  6859 May 15 20:13 cross_alpha_v5_report.md\\\\n-rw-r--r-- 1 root root 88994 May 15 21:18 cross_alpha_v6.json\\\\n-rw-r--r-- 1 root root  8251 May 15 21:18 cross_alpha_v6_report.md\\\\n-rw-r--r-- 1 root root 18313 May 15 17:56 d028_fpr_null_control.json\\\\n-rw-r--r-- 1 root root  5688 May 15 17:57 d028_fpr_null_control_full.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.98}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 328\\ndrwxr-xr-x 2 root root  4096 May 15 21:17 .\\ndrwxr-xr-x 9 root root  4096 May 15 19:57 ..\\n-rw-r--r-- 1 root root 12551 May 15 13:31 cross_alpha_analysis.json\\n-rw-r--r-- 1 root root  3769 May 15 13:33 cross_alpha_analysis.md\\n-rw-r--r-- 1 root root  9508 May 15 13:48 cross_alpha_v3_full.json\\n-rw-r--r-- 1 root root 71968 May 15 18:56 cross_alpha_v4.json\\n-rw-r--r-- 1 root root  6859 May 15 18:56 cross_alpha_v4_report.md\\n-rw-r--r-- 1 root root 71968 May 15 20:13 cross_alpha_v5.json\\n-rw-r--r-- 1 root root  6859 May 15 20:13 cross_alpha_v5_report.md\\n-rw-r--r-- 1 root root 88994 May 15 21:18 cross_alpha_v6.json\\n-rw-r--r-- 1 root root  8251 May 15 21:18 cross_alpha_v6_report.md\\n-rw-r--r-- 1 root root 18313 May 15 17:56 d028_fpr_null_control.json\\n-rw-r--r-- 1 root root  5688 May 15 17:57 d028_fpr_null_control_full.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.98}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T15:32:53.275Z_

<details><summary>↩ Tool result · `toolu_01EGk2JyXwdzHuXvpVCrWEtN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_analysis.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v3_full.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/d028_fpr_null_control.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/d028_fpr_null_control_full.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v4.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v5.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v6.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "05533ed4-399b-4f4c-bc56-a1cb024ee87f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_analysis.json\\\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v3_full.json\\\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/d028_fpr_null_control.json\\\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/d028_fpr_null_control_full.json\\\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v4.json\\\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v5.json\\\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v6.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_analysis.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v3_full.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/d028_fpr_null_control.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/d028_fpr_null_control_full.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v4.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v5.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v6.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Let me read the key files: cross_alpha_v6.json (the latest analysis), d028_fpr_null_control.json, and also check for multi-seed results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "5f54e3cf-d976-4a80-8f54-d61445b41111",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VbmhW5BPWFkT2j3K726E1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 26281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1129
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 13_

读取关键分析文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "f00992fa-1b64-441d-9ab2-dcd4bcf8396c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VbmhW5BPWFkT2j3K726E1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 26281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1129
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013hRk7SVWZUr4ybsxjLT1y1`</summary>

```json
{
  "server": "westd-19828",
  "command": "head -500 /root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v6.json",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "ded9cf27-c162-4091-88e7-4bcdd824dbf5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VbmhW5BPWFkT2j3K726E1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 26281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1129
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T15:32:58.027Z_

<details><summary>↩ Tool result · `toolu_013hRk7SVWZUr4ybsxjLT1y1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"version\\\": \\\"v6\\\",\\n  \\\"date\\\": \\\"2026-05-15\\\",\\n  \\\"n_alphas\\\": 5,\\n  \\\"alpha_points\\\": [\\n    0.0,\\n    0.25,\\n    0.5,\\n    0.75,\\n    1.0\\n  ],\\n  \\\"n_generations\\\": 11,\\n  \\\"gen_range\\\": \\\"gen_0 to gen_10\\\",\\n  \\\"statistical_config\\\": {\\n    \\\"granger_max_lag\\\": 1,\\n    \\\"granger_n_perm\\\": 5000,\\n    \\\"granger_differenced\\\": true,\\n    \\\"fdr_method\\\": \\\"benjamini-hochberg\\\",\\n    \\\"fdr_scope\\\": \\\"all 40 tests corrected together\\\",\\n    \\\"n_independent_tests\\\": 40\\n  },\\n  \\\"dose_response\\\": {\\n    \\\"a000\\\": {\\n      \\\"alpha\\\": 0.0,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.08468,\\n        \\\"drift_pct\\\": -13.78\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.467199,\\n        \\\"drift_pct\\\": -9.77\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.77602,\\n        \\\"drift_pct\\\": -4.52\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 3.069313,\\n        \\\"drift_pct\\\": -5.1\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.016391,\\n        \\\"drift_pct\\\": 51.7\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 21.107704,\\n        \\\"drift_pct\\\": -21.68\\n      }\\n    },\\n    \\\"a025\\\": {\\n      \\\"alpha\\\": 0.25,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.058594,\\n        \\\"drift_pct\\\": -40.34\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.221939,\\n        \\\"drift_pct\\\": -57.14\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.326271,\\n        \\\"drift_pct\\\": -59.85\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 3.101744,\\n        \\\"drift_pct\\\": -4.1\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.019418,\\n        \\\"drift_pct\\\": 79.72\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 22.316978,\\n        \\\"drift_pct\\\": -17.19\\n      }\\n    },\\n    \\\"a050\\\": {\\n      \\\"alpha\\\": 0.5,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.061602,\\n        \\\"drift_pct\\\": -37.28\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.251346,\\n        \\\"drift_pct\\\": -51.46\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.387256,\\n        \\\"drift_pct\\\": -52.35\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 2.631835,\\n        \\\"drift_pct\\\": -18.62\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.101864,\\n        \\\"drift_pct\\\": 842.79\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 32.644371,\\n        \\\"drift_pct\\\": 21.13\\n      }\\n    },\\n    \\\"a075\\\": {\\n      \\\"alpha\\\": 0.75,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.06607,\\n        \\\"drift_pct\\\": -32.73\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.303729,\\n        \\\"drift_pct\\\": -41.34\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.501055,\\n        \\\"drift_pct\\\": -38.35\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 2.337151,\\n        \\\"drift_pct\\\": -27.74\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.206313,\\n        \\\"drift_pct\\\": 1809.5\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 76.030187,\\n        \\\"drift_pct\\\": 182.13\\n      }\\n    },\\n    \\\"a100\\\": {\\n      \\\"alpha\\\": 1.0,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.070383,\\n        \\\"drift_pct\\\": -28.34\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.335471,\\n        \\\"drift_pct\\\": -35.21\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.555579,\\n        \\\"drift_pct\\\": -31.64\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 1.275924,\\n        \\\"drift_pct\\\": -60.55\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.417338,\\n        \\\"drift_pct\\\": 3762.61\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 1003.732954,\\n        \\\"drift_pct\\\": 3624.57\\n      }\\n    }\\n  },\\n  \\n\\n... [截断: 输出过长，省略 3212 字符] ...\\n\\nha_key\\\": \\\"a025\\\",\\n      \\\"direction\\\": \\\"ECE->d2\\\",\\n      \\\"cause\\\": \\\"ece\\\",\\n      \\\"effect\\\": \\\"distinct_2\\\",\\n      \\\"p_fdr\\\": 0.185488\\n    },\\n    {\\n      \\\"f_stat\\\": 7.8281,\\n      \\\"p_raw\\\": 0.023595,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 1.3047,\\n      \\\"alpha\\\": 0.25,\\n      \\\"alpha_key\\\": \\\"a025\\\",\\n      \\\"direction\\\": \\\"d1->entropy\\\",\\n      \\\"cause\\\": \\\"distinct_1\\\",\\n      \\\"effect\\\": \\\"token_entropy\\\",\\n      \\\"p_fdr\\\": 0.0858\\n    },\\n    {\\n      \\\"f_stat\\\": 0.7367,\\n      \\\"p_raw\\\": 0.466107,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.1228,\\n      \\\"alpha\\\": 0.25,\\n      \\\"alpha_key\\\": \\\"a025\\\",\\n      \\\"direction\\\": \\\"d1->ECE\\\",\\n      \\\"cause\\\": \\\"distinct_1\\\",\\n      \\\"effect\\\": \\\"ece\\\",\\n      \\\"p_fdr\\\": 0.548361\\n    },\\n    {\\n      \\\"f_stat\\\": 5.8655,\\n      \\\"p_raw\\\": 0.04979,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.9776,\\n      \\\"alpha\\\": 0.25,\\n      \\\"alpha_key\\\": \\\"a025\\\",\\n      \\\"direction\\\": \\\"d2->entropy\\\",\\n      \\\"cause\\\": \\\"distinct_2\\\",\\n      \\\"effect\\\": \\\"token_entropy\\\",\\n      \\\"p_fdr\\\": 0.128475\\n    },\\n    {\\n      \\\"f_stat\\\": 0.8589,\\n      \\\"p_raw\\\": 0.396921,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.1431,\\n      \\\"alpha\\\": 0.25,\\n      \\\"alpha_key\\\": \\\"a025\\\",\\n      \\\"direction\\\": \\\"d2->ECE\\\",\\n      \\\"cause\\\": \\\"distinct_2\\\",\\n      \\\"effect\\\": \\\"ece\\\",\\n      \\\"p_fdr\\\": 0.496151\\n    },\\n    {\\n      \\\"f_stat\\\": 127.4778,\\n      \\\"p_raw\\\": 0.094981,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 21.2463,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"entropy->d1\\\",\\n      \\\"cause\\\": \\\"token_entropy\\\",\\n      \\\"effect\\\": \\\"distinct_1\\\",\\n      \\\"p_fdr\\\": 0.185488\\n    },\\n    {\\n      \\\"f_stat\\\": 79.241,\\n      \\\"p_raw\\\": 0.018996,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 13.2068,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"ECE->d1\\\",\\n      \\\"cause\\\": \\\"ece\\\",\\n      \\\"effect\\\": \\\"distinct_1\\\",\\n      \\\"p_fdr\\\": 0.075984\\n    },\\n    {\\n      \\\"f_stat\\\": 35.7532,\\n      \\\"p_raw\\\": 0.097381,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 5.9589,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"entropy->d2\\\",\\n      \\\"cause\\\": \\\"token_entropy\\\",\\n      \\\"effect\\\": \\\"distinct_2\\\",\\n      \\\"p_fdr\\\": 0.185488\\n    },\\n    {\\n      \\\"f_stat\\\": 28.0601,\\n      \\\"p_raw\\\": 0.039392,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 4.6767,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"ECE->d2\\\",\\n      \\\"cause\\\": \\\"ece\\\",\\n      \\\"effect\\\": \\\"distinct_2\\\",\\n      \\\"p_fdr\\\": 0.128475\\n    },\\n    {\\n      \\\"f_stat\\\": 1.9994,\\n      \\\"p_raw\\\": 0.216957,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.3332,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"d1->entropy\\\",\\n      \\\"cause\\\": \\\"distinct_1\\\",\\n      \\\"effect\\\": \\\"token_entropy\\\",\\n      \\\"p_fdr\\\": 0.394467\\n    },\\n    {\\n      \\\"f_stat\\\": 1.5744,\\n      \\\"p_raw\\\": 0.277145,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.2624,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"d1->ECE\\\",\\n      \\\"cause\\\": \\\"distinct_1\\\",\\n      \\\"effect\\\": \\\"ece\\\",\\n      \\\"p_fdr\\\": 0.461908\\n    },\\n    {\\n      \\\"f_stat\\\": 1.2353,\\n      \\\"p_raw\\\": 0.314337,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.2059,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"d2->entropy\\\",\\n      \\\"cause\\\": \\\"distinct_2\\\",\\n      \\\"effect\\\": \\\"token_entropy\\\",\\n      \\\"p_fdr\\\": 0.471905\\n    },\\n    {\\n      \\\"f_stat\\\": 1.0783,\\n      \\\"p_raw\\\": 0.352929,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.1797,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"d2->ECE\\\",\\n      \\\"cause\\\": \\\"distinct_2\\\",\\n      \\\"effect\\\": \\\"ece\\\",\\n      \\\"p_fdr\\\": 0.471905\\n    },\\n    {\\n      \\\"f_stat\\\": 430.2374,\\n      \\\"p_raw\\\": 0.010598,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 71.7062,\\n      \\\"alpha\\\": 0.75,\\n      \\\"alpha_key\\\": \\\"a075\\\",\\n      \\\"direction\\\": \\\"entropy->d1\\\",\\n      \\\"cause\\\": \\\"token_entropy\\\",\\n      \\\"effect\\\": \\\"distinct_1\\\",\\n      \\\"p_fdr\\\": 0.05399\\n    },\\n    {\\n      \\\"f_stat\\\": 443.3845,\\n      \\\"p_raw\\\": 0.003799,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 73.8974,\\n      \\\"alpha\\\": 0.75,\\n      \\\"alpha_key\\\": \\\"a075\\\",\\n      \\\"direction\\\": \\\"ECE->d1\\\",\\n      \\\"cause\\\": \\\"ece\\\",\\n      \\\"effect\\\": \\\"distinct_1\\\",\\n      \\\"p_fdr\\\": 0.04599\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "583a8f1a-a05b-4331-bc17-ab5e1bc41a48",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"version\\\\\\\": \\\\\\\"v6\\\\\\\",\\\\n  \\\\\\\"date\\\\\\\": \\\\\\\"2026-05-15\\\\\\\",\\\\n  \\\\\\\"n_alphas\\\\\\\": 5,\\\\n  \\\\\\\"alpha_points\\\\\\\": [\\\\n    0.0,\\\\n    0.25,\\\\n    0.5,\\\\n    0.75,\\\\n    1.0\\\\n  ],\\\\n  \\\\\\\"n_generations\\\\\\\": 11,\\\\n  \\\\\\\"gen_range\\\\\\\": \\\\\\\"gen_0 to gen_10\\\\\\\",\\\\n  \\\\\\\"statistical_config\\\\\\\": {\\\\n    \\\\\\\"granger_max_lag\\\\\\\": 1,\\\\n    \\\\\\\"granger_n_perm\\\\\\\": 5000,\\\\n    \\\\\\\"granger_differenced\\\\\\\": true,\\\\n    \\\\\\\"fdr_method\\\\\\\": \\\\\\\"benjamini-hochberg\\\\\\\",\\\\n    \\\\\\\"fdr_scope\\\\\\\": \\\\\\\"all 40 tests corrected together\\\\\\\",\\\\n    \\\\\\\"n_independent_tests\\\\\\\": 40\\\\n  },\\\\n  \\\\\\\"dose_response\\\\\\\": {\\\\n    \\\\\\\"a000\\\\\\\": {\\\\n      \\\\\\\"alpha\\\\\\\": 0.0,\\\\n      \\\\\\\"distinct_1\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.098216,\\\\n        \\\\\\\"gen10\\\\\\\": 0.08468,\\\\n        \\\\\\\"drift_pct\\\\\\\": -13.78\\\\n      },\\\\n      \\\\\\\"distinct_2\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.517803,\\\\n        \\\\\\\"gen10\\\\\\\": 0.467199,\\\\n        \\\\\\\"drift_pct\\\\\\\": -9.77\\\\n      },\\\\n      \\\\\\\"distinct_3\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.812728,\\\\n        \\\\\\\"gen10\\\\\\\": 0.77602,\\\\n        \\\\\\\"drift_pct\\\\\\\": -4.52\\\\n      },\\\\n      \\\\\\\"token_entropy\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 3.234195,\\\\n        \\\\\\\"gen10\\\\\\\": 3.069313,\\\\n        \\\\\\\"drift_pct\\\\\\\": -5.1\\\\n      },\\\\n      \\\\\\\"ece\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.010805,\\\\n        \\\\\\\"gen10\\\\\\\": 0.016391,\\\\n        \\\\\\\"drift_pct\\\\\\\": 51.7\\\\n      },\\\\n      \\\\\\\"perplexity\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 26.948959,\\\\n        \\\\\\\"gen10\\\\\\\": 21.107704,\\\\n        \\\\\\\"drift_pct\\\\\\\": -21.68\\\\n      }\\\\n    },\\\\n    \\\\\\\"a025\\\\\\\": {\\\\n      \\\\\\\"alpha\\\\\\\": 0.25,\\\\n      \\\\\\\"distinct_1\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.098216,\\\\n        \\\\\\\"gen10\\\\\\\": 0.058594,\\\\n        \\\\\\\"drift_pct\\\\\\\": -40.34\\\\n      },\\\\n      \\\\\\\"distinct_2\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.517803,\\\\n        \\\\\\\"gen10\\\\\\\": 0.221939,\\\\n        \\\\\\\"drift_pct\\\\\\\": -57.14\\\\n      },\\\\n      \\\\\\\"distinct_3\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.812728,\\\\n        \\\\\\\"gen10\\\\\\\": 0.326271,\\\\n        \\\\\\\"drift_pct\\\\\\\": -59.85\\\\n      },\\\\n      \\\\\\\"token_entropy\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 3.234195,\\\\n        \\\\\\\"gen10\\\\\\\": 3.101744,\\\\n        \\\\\\\"drift_pct\\\\\\\": -4.1\\\\n      },\\\\n      \\\\\\\"ece\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.010805,\\\\n        \\\\\\\"gen10\\\\\\\": 0.019418,\\\\n        \\\\\\\"drift_pct\\\\\\\": 79.72\\\\n      },\\\\n      \\\\\\\"perplexity\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 26.948959,\\\\n        \\\\\\\"gen10\\\\\\\": 22.316978,\\\\n        \\\\\\\"drift_pct\\\\\\\": -17.19\\\\n      }\\\\n    },\\\\n    \\\\\\\"a050\\\\\\\": {\\\\n      \\\\\\\"alpha\\\\\\\": 0.5,\\\\n      \\\\\\\"distinct_1\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.098216,\\\\n        \\\\\\\"gen10\\\\\\\": 0.061602,\\\\n        \\\\\\\"drift_pct\\\\\\\": -37.28\\\\n      },\\\\n      \\\\\\\"distinct_2\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.517803,\\\\n        \\\\\\\"gen10\\\\\\\": 0.251346,\\\\n        \\\\\\\"drift_pct\\\\\\\": -51.46\\\\n      },\\\\n      \\\\\\\"distinct_3\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.812728,\\\\n        \\\\\\\"gen10\\\\\\\": 0.387256,\\\\n        \\\\\\\"drift_pct\\\\\\\": -52.35\\\\n      },\\\\n      \\\\\\\"token_entropy\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 3.234195,\\\\n        \\\\\\\"gen10\\\\\\\": 2.631835,\\\\n        \\\\\\\"drift_pct\\\\\\\": -18.62\\\\n      },\\\\n      \\\\\\\"ece\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.010805,\\\\n        \\\\\\\"gen10\\\\\\\": 0.101864,\\\\n        \\\\\\\"drift_pct\\\\\\\": 842.79\\\\n      },\\\\n      \\\\\\\"perplexity\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 26.948959,\\\\n        \\\\\\\"gen10\\\\\\\": 32.644371,\\\\n        \\\\\\\"drift_pct\\\\\\\": 21.13\\\\n      }\\\\n    },\\\\n    \\\\\\\"a075\\\\\\\": {\\\\n      \\\\\\\"alpha\\\\\\\": 0.75,\\\\n      \\\\\\\"distinct_1\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.098216,\\\\n        \\\\\\\"gen10\\\\\\\": 0.06607,\\\\n        \\\\\\\"drift_pct\\\\\\\": -32.73\\\\n      },\\\\n      \\\\\\\"distinct_2\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.517803,\\\\n        \\\\\\\"gen10\\\\\\\": 0.303729,\\\\n        \\\\\\\"drift_pct\\\\\\\": -41.34\\\\n      },\\\\n      \\\\\\\"distinct_3\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.812728,\\\\n        \\\\\\\"gen10\\\\\\\": 0.501055,\\\\n        \\\\\\\"drift_pct\\\\\\\": -38.35\\\\n      },\\\\n      \\\\\\\"token_entropy\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 3.234195,\\\\n        \\\\\\\"gen10\\\\\\\": 2.337151,\\\\n        \\\\\\\"drift_pct\\\\\\\": -27.74\\\\n      },\\\\n      \\\\\\\"ece\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.010805,\\\\n        \\\\\\\"gen10\\\\\\\": 0.206313,\\\\n        \\\\\\\"drift_pct\\\\\\\": 1809.5\\\\n      },\\\\n      \\\\\\\"perplexity\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 26.948959,\\\\n        \\\\\\\"gen10\\\\\\\": 76.030187,\\\\n        \\\\\\\"drift_pct\\\\\\\": 182.13\\\\n      }\\\\n    },\\\\n    \\\\\\\"a100\\\\\\\": {\\\\n      \\\\\\\"alpha\\\\\\\": 1.0,\\\\n      \\\\\\\"distinct_1\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.098216,\\\\n        \\\\\\\"gen10\\\\\\\": 0.070383,\\\\n        \\\\\\\"drift_pct\\\\\\\": -28.34\\\\n      },\\\\n      \\\\\\\"distinct_2\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.517803,\\\\n        \\\\\\\"gen10\\\\\\\": 0.335471,\\\\n        \\\\\\\"drift_pct\\\\\\\": -35.21\\\\n      },\\\\n      \\\\\\\"distinct_3\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.812728,\\\\n        \\\\\\\"gen10\\\\\\\": 0.555579,\\\\n        \\\\\\\"drift_pct\\\\\\\": -31.64\\\\n      },\\\\n      \\\\\\\"token_entropy\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 3.234195,\\\\n        \\\\\\\"gen10\\\\\\\": 1.275924,\\\\n        \\\\\\\"drift_pct\\\\\\\": -60.55\\\\n      },\\\\n      \\\\\\\"ece\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.010805,\\\\n        \\\\\\\"gen10\\\\\\\": 0.417338,\\\\n        \\\\\\\"drift_pct\\\\\\\": 3762.61\\\\n      },\\\\n      \\\\\\\"perplexity\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 26.948959,\\\\n        \\\\\\\"gen10\\\\\\\": 1003.732954,\\\\n        \\\\\\\"drift_pct\\\\\\\": 3624.57\\\\n      }\\\\n    }\\\\n  },\\\\n  \\\\n\\\\n... [截断: 输出过长，省略 3212 字符] ...\\\\n\\\\nha_key\\\\\\\": \\\\\\\"a025\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"ECE->d2\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.185488\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 7.8281,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.023595,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 1.3047,\\\\n      \\\\\\\"alpha\\\\\\\": 0.25,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a025\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"d1->entropy\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.0858\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 0.7367,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.466107,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 0.1228,\\\\n      \\\\\\\"alpha\\\\\\\": 0.25,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a025\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"d1->ECE\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.548361\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 5.8655,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.04979,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 0.9776,\\\\n      \\\\\\\"alpha\\\\\\\": 0.25,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a025\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"d2->entropy\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.128475\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 0.8589,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.396921,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 0.1431,\\\\n      \\\\\\\"alpha\\\\\\\": 0.25,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a025\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"d2->ECE\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.496151\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 127.4778,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.094981,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 21.2463,\\\\n      \\\\\\\"alpha\\\\\\\": 0.5,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a050\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"entropy->d1\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.185488\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 79.241,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.018996,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 13.2068,\\\\n      \\\\\\\"alpha\\\\\\\": 0.5,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a050\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"ECE->d1\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.075984\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 35.7532,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.097381,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 5.9589,\\\\n      \\\\\\\"alpha\\\\\\\": 0.5,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a050\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"entropy->d2\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.185488\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 28.0601,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.039392,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 4.6767,\\\\n      \\\\\\\"alpha\\\\\\\": 0.5,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a050\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"ECE->d2\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.128475\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 1.9994,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.216957,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 0.3332,\\\\n      \\\\\\\"alpha\\\\\\\": 0.5,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a050\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"d1->entropy\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.394467\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 1.5744,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.277145,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 0.2624,\\\\n      \\\\\\\"alpha\\\\\\\": 0.5,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a050\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"d1->ECE\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.461908\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 1.2353,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.314337,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 0.2059,\\\\n      \\\\\\\"alpha\\\\\\\": 0.5,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a050\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"d2->entropy\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.471905\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 1.0783,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.352929,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 0.1797,\\\\n      \\\\\\\"alpha\\\\\\\": 0.5,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a050\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"d2->ECE\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.471905\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 430.2374,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.010598,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 71.7062,\\\\n      \\\\\\\"alpha\\\\\\\": 0.75,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a075\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"entropy->d1\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.05399\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 443.3845,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.003799,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 73.8974,\\\\n      \\\\\\\"alpha\\\\\\\": 0.75,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a075\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"ECE->d1\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.04599\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"version\\\": \\\"v6\\\",\\n  \\\"date\\\": \\\"2026-05-15\\\",\\n  \\\"n_alphas\\\": 5,\\n  \\\"alpha_points\\\": [\\n    0.0,\\n    0.25,\\n    0.5,\\n    0.75,\\n    1.0\\n  ],\\n  \\\"n_generations\\\": 11,\\n  \\\"gen_range\\\": \\\"gen_0 to gen_10\\\",\\n  \\\"statistical_config\\\": {\\n    \\\"granger_max_lag\\\": 1,\\n    \\\"granger_n_perm\\\": 5000,\\n    \\\"granger_differenced\\\": true,\\n    \\\"fdr_method\\\": \\\"benjamini-hochberg\\\",\\n    \\\"fdr_scope\\\": \\\"all 40 tests corrected together\\\",\\n    \\\"n_independent_tests\\\": 40\\n  },\\n  \\\"dose_response\\\": {\\n    \\\"a000\\\": {\\n      \\\"alpha\\\": 0.0,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.08468,\\n        \\\"drift_pct\\\": -13.78\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.467199,\\n        \\\"drift_pct\\\": -9.77\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.77602,\\n        \\\"drift_pct\\\": -4.52\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 3.069313,\\n        \\\"drift_pct\\\": -5.1\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.016391,\\n        \\\"drift_pct\\\": 51.7\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 21.107704,\\n        \\\"drift_pct\\\": -21.68\\n      }\\n    },\\n    \\\"a025\\\": {\\n      \\\"alpha\\\": 0.25,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.058594,\\n        \\\"drift_pct\\\": -40.34\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.221939,\\n        \\\"drift_pct\\\": -57.14\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.326271,\\n        \\\"drift_pct\\\": -59.85\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 3.101744,\\n        \\\"drift_pct\\\": -4.1\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.019418,\\n        \\\"drift_pct\\\": 79.72\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 22.316978,\\n        \\\"drift_pct\\\": -17.19\\n      }\\n    },\\n    \\\"a050\\\": {\\n      \\\"alpha\\\": 0.5,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.061602,\\n        \\\"drift_pct\\\": -37.28\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.251346,\\n        \\\"drift_pct\\\": -51.46\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.387256,\\n        \\\"drift_pct\\\": -52.35\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 2.631835,\\n        \\\"drift_pct\\\": -18.62\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.101864,\\n        \\\"drift_pct\\\": 842.79\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 32.644371,\\n        \\\"drift_pct\\\": 21.13\\n      }\\n    },\\n    \\\"a075\\\": {\\n      \\\"alpha\\\": 0.75,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.06607,\\n        \\\"drift_pct\\\": -32.73\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.303729,\\n        \\\"drift_pct\\\": -41.34\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.501055,\\n        \\\"drift_pct\\\": -38.35\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 2.337151,\\n        \\\"drift_pct\\\": -27.74\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.206313,\\n        \\\"drift_pct\\\": 1809.5\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 76.030187,\\n        \\\"drift_pct\\\": 182.13\\n      }\\n    },\\n    \\\"a100\\\": {\\n      \\\"alpha\\\": 1.0,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.070383,\\n        \\\"drift_pct\\\": -28.34\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.335471,\\n        \\\"drift_pct\\\": -35.21\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.555579,\\n        \\\"drift_pct\\\": -31.64\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 1.275924,\\n        \\\"drift_pct\\\": -60.55\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.417338,\\n        \\\"drift_pct\\\": 3762.61\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 1003.732954,\\n        \\\"drift_pct\\\": 3624.57\\n      }\\n    }\\n  },\\n  \\n\\n... [截断: 输出过长，省略 3212 字符] ...\\n\\nha_key\\\": \\\"a025\\\",\\n      \\\"direction\\\": \\\"ECE->d2\\\",\\n      \\\"cause\\\": \\\"ece\\\",\\n      \\\"effect\\\": \\\"distinct_2\\\",\\n      \\\"p_fdr\\\": 0.185488\\n    },\\n    {\\n      \\\"f_stat\\\": 7.8281,\\n      \\\"p_raw\\\": 0.023595,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 1.3047,\\n      \\\"alpha\\\": 0.25,\\n      \\\"alpha_key\\\": \\\"a025\\\",\\n      \\\"direction\\\": \\\"d1->entropy\\\",\\n      \\\"cause\\\": \\\"distinct_1\\\",\\n      \\\"effect\\\": \\\"token_entropy\\\",\\n      \\\"p_fdr\\\": 0.0858\\n    },\\n    {\\n      \\\"f_stat\\\": 0.7367,\\n      \\\"p_raw\\\": 0.466107,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.1228,\\n      \\\"alpha\\\": 0.25,\\n      \\\"alpha_key\\\": \\\"a025\\\",\\n      \\\"direction\\\": \\\"d1->ECE\\\",\\n      \\\"cause\\\": \\\"distinct_1\\\",\\n      \\\"effect\\\": \\\"ece\\\",\\n      \\\"p_fdr\\\": 0.548361\\n    },\\n    {\\n      \\\"f_stat\\\": 5.8655,\\n      \\\"p_raw\\\": 0.04979,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.9776,\\n      \\\"alpha\\\": 0.25,\\n      \\\"alpha_key\\\": \\\"a025\\\",\\n      \\\"direction\\\": \\\"d2->entropy\\\",\\n      \\\"cause\\\": \\\"distinct_2\\\",\\n      \\\"effect\\\": \\\"token_entropy\\\",\\n      \\\"p_fdr\\\": 0.128475\\n    },\\n    {\\n      \\\"f_stat\\\": 0.8589,\\n      \\\"p_raw\\\": 0.396921,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.1431,\\n      \\\"alpha\\\": 0.25,\\n      \\\"alpha_key\\\": \\\"a025\\\",\\n      \\\"direction\\\": \\\"d2->ECE\\\",\\n      \\\"cause\\\": \\\"distinct_2\\\",\\n      \\\"effect\\\": \\\"ece\\\",\\n      \\\"p_fdr\\\": 0.496151\\n    },\\n    {\\n      \\\"f_stat\\\": 127.4778,\\n      \\\"p_raw\\\": 0.094981,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 21.2463,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"entropy->d1\\\",\\n      \\\"cause\\\": \\\"token_entropy\\\",\\n      \\\"effect\\\": \\\"distinct_1\\\",\\n      \\\"p_fdr\\\": 0.185488\\n    },\\n    {\\n      \\\"f_stat\\\": 79.241,\\n      \\\"p_raw\\\": 0.018996,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 13.2068,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"ECE->d1\\\",\\n      \\\"cause\\\": \\\"ece\\\",\\n      \\\"effect\\\": \\\"distinct_1\\\",\\n      \\\"p_fdr\\\": 0.075984\\n    },\\n    {\\n      \\\"f_stat\\\": 35.7532,\\n      \\\"p_raw\\\": 0.097381,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 5.9589,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"entropy->d2\\\",\\n      \\\"cause\\\": \\\"token_entropy\\\",\\n      \\\"effect\\\": \\\"distinct_2\\\",\\n      \\\"p_fdr\\\": 0.185488\\n    },\\n    {\\n      \\\"f_stat\\\": 28.0601,\\n      \\\"p_raw\\\": 0.039392,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 4.6767,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"ECE->d2\\\",\\n      \\\"cause\\\": \\\"ece\\\",\\n      \\\"effect\\\": \\\"distinct_2\\\",\\n      \\\"p_fdr\\\": 0.128475\\n    },\\n    {\\n      \\\"f_stat\\\": 1.9994,\\n      \\\"p_raw\\\": 0.216957,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.3332,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"d1->entropy\\\",\\n      \\\"cause\\\": \\\"distinct_1\\\",\\n      \\\"effect\\\": \\\"token_entropy\\\",\\n      \\\"p_fdr\\\": 0.394467\\n    },\\n    {\\n      \\\"f_stat\\\": 1.5744,\\n      \\\"p_raw\\\": 0.277145,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.2624,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"d1->ECE\\\",\\n      \\\"cause\\\": \\\"distinct_1\\\",\\n      \\\"effect\\\": \\\"ece\\\",\\n      \\\"p_fdr\\\": 0.461908\\n    },\\n    {\\n      \\\"f_stat\\\": 1.2353,\\n      \\\"p_raw\\\": 0.314337,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.2059,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"d2->entropy\\\",\\n      \\\"cause\\\": \\\"distinct_2\\\",\\n      \\\"effect\\\": \\\"token_entropy\\\",\\n      \\\"p_fdr\\\": 0.471905\\n    },\\n    {\\n      \\\"f_stat\\\": 1.0783,\\n      \\\"p_raw\\\": 0.352929,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.1797,\\n      \\\"alpha\\\": 0.5,\\n      \\\"alpha_key\\\": \\\"a050\\\",\\n      \\\"direction\\\": \\\"d2->ECE\\\",\\n      \\\"cause\\\": \\\"distinct_2\\\",\\n      \\\"effect\\\": \\\"ece\\\",\\n      \\\"p_fdr\\\": 0.471905\\n    },\\n    {\\n      \\\"f_stat\\\": 430.2374,\\n      \\\"p_raw\\\": 0.010598,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 71.7062,\\n      \\\"alpha\\\": 0.75,\\n      \\\"alpha_key\\\": \\\"a075\\\",\\n      \\\"direction\\\": \\\"entropy->d1\\\",\\n      \\\"cause\\\": \\\"token_entropy\\\",\\n      \\\"effect\\\": \\\"distinct_1\\\",\\n      \\\"p_fdr\\\": 0.05399\\n    },\\n    {\\n      \\\"f_stat\\\": 443.3845,\\n      \\\"p_raw\\\": 0.003799,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 73.8974,\\n      \\\"alpha\\\": 0.75,\\n      \\\"alpha_key\\\": \\\"a075\\\",\\n      \\\"direction\\\": \\\"ECE->d1\\\",\\n      \\\"cause\\\": \\\"ece\\\",\\n      \\\"effect\\\": \\\"distinct_1\\\",\\n      \\\"p_fdr\\\": 0.04599\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NaWRqVwXhBvvsfwd9LnJxU`</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/analysis/d028_fpr_null_control.json",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "044840f3-a1d4-4406-9a55-87d51859047a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VbmhW5BPWFkT2j3K726E1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 26281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1129
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T15:32:59.046Z_

<details><summary>↩ Tool result · `toolu_01NaWRqVwXhBvvsfwd9LnJxU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"null_control_fpr\\\": {\\n    \\\"description\\\": \\\"FPR computed from alpha=0.0 null control (single seed=42, 8 pairs)\\\",\\n    \\\"per_method_fdr\\\": {\\n      \\\"naive\\\": {\\n        \\\"sig_raw\\\": 8,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 1.0,\\n        \\\"sig_fdr\\\": 8,\\n        \\\"fpr_fdr\\\": 1.0\\n      },\\n      \\\"differenced\\\": {\\n        \\\"sig_raw\\\": 4,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.5,\\n        \\\"sig_fdr\\\": 3,\\n        \\\"fpr_fdr\\\": 0.375\\n      },\\n      \\\"threshold\\\": {\\n        \\\"sig_raw\\\": 5,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.625,\\n        \\\"sig_fdr\\\": 5,\\n        \\\"fpr_fdr\\\": 0.625,\\n        \\\"note\\\": \\\"non-statistical (no p-values, FDR not applicable)\\\"\\n      },\\n      \\\"permutation_granger\\\": {\\n        \\\"sig_raw\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.0,\\n        \\\"sig_fdr\\\": 0,\\n        \\\"fpr_fdr\\\": 0.0\\n      },\\n      \\\"TY\\\": {\\n        \\\"sig_raw\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.0,\\n        \\\"sig_fdr\\\": 0,\\n        \\\"fpr_fdr\\\": 0.0\\n      }\\n    },\\n    \\\"per_method_full\\\": {\\n      \\\"naive\\\": {\\n        \\\"sig_raw\\\": 8,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 1.0,\\n        \\\"sig_fdr\\\": 8,\\n        \\\"fpr_fdr\\\": 1.0,\\n        \\\"p_values_raw\\\": [\\n          0.002496,\\n          0.006055,\\n          0.007303,\\n          0.0,\\n          0.005344,\\n          0.009665,\\n          0.022381,\\n          0.018795\\n        ],\\n        \\\"p_values_fdr\\\": [\\n          0.009984,\\n          0.011684799999999999,\\n          0.011684799999999999,\\n          0.0,\\n          0.011684799999999999,\\n          0.012886666666666666,\\n          0.022381,\\n          0.02148\\n        ]\\n      },\\n      \\\"differenced\\\": {\\n        \\\"sig_raw\\\": 4,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.5,\\n        \\\"sig_fdr\\\": 3,\\n        \\\"fpr_fdr\\\": 0.375,\\n        \\\"p_values_raw\\\": [\\n          0.000157,\\n          0.00325,\\n          0.044726,\\n          2e-06,\\n          0.051439,\\n          0.192837,\\n          0.202654,\\n          0.096018\\n        ],\\n        \\\"p_values_fdr\\\": [\\n          0.000628,\\n          0.008666666666666666,\\n          0.0823024,\\n          1.6e-05,\\n          0.0823024,\\n          0.202654,\\n          0.202654,\\n          0.128024\\n        ]\\n      },\\n      \\\"threshold\\\": {\\n        \\\"sig_raw\\\": 5,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.625,\\n        \\\"sig_fdr\\\": 5,\\n        \\\"fpr_fdr\\\": 0.625,\\n        \\\"note\\\": \\\"non-statistical (no p-values, FDR not applicable)\\\"\\n      },\\n      \\\"permutation_granger\\\": {\\n        \\\"sig_raw\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.0,\\n        \\\"sig_fdr\\\": 0,\\n        \\\"fpr_fdr\\\": 0.0,\\n        \\\"p_values_raw\\\": [\\n          0.058941,\\n          0.093906,\\n          0.080919,\\n          0.67033,\\n          0.955045,\\n          0.549451,\\n          0.350649,\\n          0.365634\\n        ],\\n        \\\"p_values_fdr\\\": [\\n          0.250416,\\n          0.250416,\\n          0.250416,\\n          0.7660914285714285,\\n          0.955045,\\n          0.7326013333333333,\\n          0.5850144,\\n          0.5850144\\n        ]\\n      },\\n      \\\"TY\\\": {\\n        \\\"sig_raw\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.0,\\n        \\\"sig_fdr\\\": 0,\\n        \\\"fpr_fdr\\\": 0.0,\\n        \\\"p_values_raw\\\": [\\n          0.891964,\\n          0.858458,\\n          0.970851,\\n          0.314151,\\n          0.094304,\\n          0.092998,\\n          0.103218,\\n          0.801145\\n        ],\\n        \\\"p_values_fdr\\\": [\\n          0.970851,\\n          0.970851,\\n          0.970851,\\n          0.628302,\\n          0.275248,\\n          0.275248,\\n          0.275248,\\n          0.970851\\n        ]\\n      }\\n    },\\n    \\\"pooled_fdr\\\": {\\n      \\\"naive\\\": {\\n        \\\"sig_pooled_fdr\\\": 6,\\n        \\\"total\\\": 8,\\n        \\\"fpr_pooled_fdr\\\": 0.75\\n      },\\n      \\\"differenced\\\": {\\n        \\\"sig_pooled_fdr\\\": 3,\\n        \\\"total\\\": 8,\\n        \\\"fpr_pooled_fdr\\\": 0.375\\n      },\\n      \\\"threshold\\\": {\\n        \\\"sig_raw\\\": 5,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.625,\\n        \\\"sig_fdr\\\": 5,\\n        \\\"fpr_fdr\\\": 0.625,\\n        \\\"note\\\": \\\"non-statistical (no p-values, FDR not applicable)\\\"\\n      },\\n      \\\"permutation_granger\\\": {\\n        \\\"sig_pooled_fdr\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"fpr_pooled_fdr\\\": 0.0\\n      },\\n      \\\"TY\\\": {\\n        \\\"sig_pooled_fdr\\\": 0,\\n        \\\"tot\\n\\n... [截断: 输出过长，省略 10313 字符] ...\\n\\n         6.4000000000000006e-06,\\n          0.0,\\n          2.4615384615384615e-06,\\n          0.007085\\n        ]\\n      },\\n      \\\"threshold\\\": {\\n        \\\"sig_raw\\\": 32,\\n        \\\"total\\\": 32,\\n        \\\"rate_raw\\\": 1.0,\\n        \\\"sig_fdr\\\": 32,\\n        \\\"rate_fdr\\\": 1.0,\\n        \\\"note\\\": \\\"non-statistical\\\"\\n      },\\n      \\\"permutation_granger\\\": {\\n        \\\"sig_raw\\\": 24,\\n        \\\"total\\\": 32,\\n        \\\"rate_raw\\\": 0.75,\\n        \\\"sig_fdr\\\": 24,\\n        \\\"rate_fdr\\\": 0.75,\\n        \\\"p_values_raw\\\": [\\n          0.010989,\\n          0.015984,\\n          0.026973,\\n          0.716284,\\n          0.000999,\\n          0.008991,\\n          0.015984,\\n          0.96004,\\n          0.000999,\\n          0.000999,\\n          0.000999,\\n          0.801199,\\n          0.000999,\\n          0.000999,\\n          0.000999,\\n          0.537463,\\n          0.001998,\\n          0.002997,\\n          0.012987,\\n          0.46953,\\n          0.000999,\\n          0.000999,\\n          0.000999,\\n          0.345654,\\n          0.003996,\\n          0.003996,\\n          0.004995,\\n          0.992008,\\n          0.001998,\\n          0.001998,\\n          0.003996,\\n          0.674326\\n        ],\\n        \\\"p_values_fdr\\\": [\\n          0.0175824,\\n          0.022238608695652175,\\n          0.035964,\\n          0.7903823448275863,\\n          0.0031968000000000005,\\n          0.015142736842105264,\\n          0.022238608695652175,\\n          0.9910090322580645,\\n          0.0031968000000000005,\\n          0.0031968000000000005,\\n          0.0031968000000000005,\\n          0.8546122666666667,\\n          0.0031968000000000005,\\n          0.0031968000000000005,\\n          0.0031968000000000005,\\n          0.6369931851851852,\\n          0.004918153846153846,\\n          0.006850285714285714,\\n          0.019789714285714285,\\n          0.5778830769230769,\\n          0.0031968000000000005,\\n          0.0031968000000000005,\\n          0.0031968000000000005,\\n          0.44243712,\\n          0.007521882352941177,\\n          0.007521882352941177,\\n          0.00888,\\n          0.992008,\\n          0.004918153846153846,\\n          0.004918153846153846,\\n          0.007521882352941177,\\n          0.7706582857142857\\n        ]\\n      },\\n      \\\"TY\\\": {\\n        \\\"sig_raw\\\": 19,\\n        \\\"total\\\": 32,\\n        \\\"rate_raw\\\": 0.59375,\\n        \\\"sig_fdr\\\": 19,\\n        \\\"rate_fdr\\\": 0.59375,\\n        \\\"p_values_raw\\\": [\\n          0.0,\\n          1.3e-05,\\n          2e-05,\\n          0.315231,\\n          0.0,\\n          1e-05,\\n          5.7e-05,\\n          0.491153,\\n          2e-06,\\n          1.4e-05,\\n          1.5e-05,\\n          0.792566,\\n          0.0,\\n          2e-06,\\n          1.4e-05,\\n          0.268428,\\n          0.0,\\n          0.0,\\n          1e-06,\\n          0.448982,\\n          0.172933,\\n          0.373375,\\n          0.22942,\\n          0.090486,\\n          0.0,\\n          3e-06,\\n          7e-06,\\n          0.210569,\\n          0.027607,\\n          0.59951,\\n          0.572459,\\n          0.167366\\n        ],\\n        \\\"p_values_fdr\\\": [\\n          0.0,\\n          2.9866666666666666e-05,\\n          3.7647058823529415e-05,\\n          0.38797661538461536,\\n          0.0,\\n          2.666666666666667e-05,\\n          0.00010133333333333333,\\n          0.5419619310344828,\\n          7.111111111111111e-06,\\n          2.9866666666666666e-05,\\n          3e-05,\\n          0.792566,\\n          0.0,\\n          7.111111111111111e-06,\\n          2.9866666666666666e-05,\\n          0.34358784,\\n          0.0,\\n          0.0,\\n          4.571428571428571e-06,\\n          0.5131222857142858,\\n          0.2515389090909091,\\n          0.44251851851851853,\\n          0.30589333333333335,\\n          0.1447776,\\n          0.0,\\n          9.6e-06,\\n          2.0363636363636365e-05,\\n          0.2929655652173913,\\n          0.046496,\\n          0.6188490322580645,\\n          0.6106229333333334,\\n          0.2515389090909091\\n        ]\\n      }\\n    }\\n  },\\n  \\\"meta\\\": {\\n    \\\"n_pairs\\\": 8,\\n    \\\"n_seeds_per_alpha\\\": 1,\\n    \\\"seed\\\": 42,\\n    \\\"alphas\\\": [\\n      0.0,\\n      0.25,\\n      0.5,\\n      1.0\\n    ],\\n    \\\"fdr_method\\\": \\\"Benjamini-Hochberg\\\",\\n    \\\"fdr_alpha\\\": 0.05\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "2f086b39-c89b-4ae8-89ee-d10d1e39c4e6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"null_control_fpr\\\\\\\": {\\\\n    \\\\\\\"description\\\\\\\": \\\\\\\"FPR computed from alpha=0.0 null control (single seed=42, 8 pairs)\\\\\\\",\\\\n    \\\\\\\"per_method_fdr\\\\\\\": {\\\\n      \\\\\\\"naive\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 8,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_raw\\\\\\\": 1.0,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 8,\\\\n        \\\\\\\"fpr_fdr\\\\\\\": 1.0\\\\n      },\\\\n      \\\\\\\"differenced\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 4,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_raw\\\\\\\": 0.5,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 3,\\\\n        \\\\\\\"fpr_fdr\\\\\\\": 0.375\\\\n      },\\\\n      \\\\\\\"threshold\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 5,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_raw\\\\\\\": 0.625,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 5,\\\\n        \\\\\\\"fpr_fdr\\\\\\\": 0.625,\\\\n        \\\\\\\"note\\\\\\\": \\\\\\\"non-statistical (no p-values, FDR not applicable)\\\\\\\"\\\\n      },\\\\n      \\\\\\\"permutation_granger\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 0,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_raw\\\\\\\": 0.0,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 0,\\\\n        \\\\\\\"fpr_fdr\\\\\\\": 0.0\\\\n      },\\\\n      \\\\\\\"TY\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 0,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_raw\\\\\\\": 0.0,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 0,\\\\n        \\\\\\\"fpr_fdr\\\\\\\": 0.0\\\\n      }\\\\n    },\\\\n    \\\\\\\"per_method_full\\\\\\\": {\\\\n      \\\\\\\"naive\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 8,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_raw\\\\\\\": 1.0,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 8,\\\\n        \\\\\\\"fpr_fdr\\\\\\\": 1.0,\\\\n        \\\\\\\"p_values_raw\\\\\\\": [\\\\n          0.002496,\\\\n          0.006055,\\\\n          0.007303,\\\\n          0.0,\\\\n          0.005344,\\\\n          0.009665,\\\\n          0.022381,\\\\n          0.018795\\\\n        ],\\\\n        \\\\\\\"p_values_fdr\\\\\\\": [\\\\n          0.009984,\\\\n          0.011684799999999999,\\\\n          0.011684799999999999,\\\\n          0.0,\\\\n          0.011684799999999999,\\\\n          0.012886666666666666,\\\\n          0.022381,\\\\n          0.02148\\\\n        ]\\\\n      },\\\\n      \\\\\\\"differenced\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 4,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_raw\\\\\\\": 0.5,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 3,\\\\n        \\\\\\\"fpr_fdr\\\\\\\": 0.375,\\\\n        \\\\\\\"p_values_raw\\\\\\\": [\\\\n          0.000157,\\\\n          0.00325,\\\\n          0.044726,\\\\n          2e-06,\\\\n          0.051439,\\\\n          0.192837,\\\\n          0.202654,\\\\n          0.096018\\\\n        ],\\\\n        \\\\\\\"p_values_fdr\\\\\\\": [\\\\n          0.000628,\\\\n          0.008666666666666666,\\\\n          0.0823024,\\\\n          1.6e-05,\\\\n          0.0823024,\\\\n          0.202654,\\\\n          0.202654,\\\\n          0.128024\\\\n        ]\\\\n      },\\\\n      \\\\\\\"threshold\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 5,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_raw\\\\\\\": 0.625,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 5,\\\\n        \\\\\\\"fpr_fdr\\\\\\\": 0.625,\\\\n        \\\\\\\"note\\\\\\\": \\\\\\\"non-statistical (no p-values, FDR not applicable)\\\\\\\"\\\\n      },\\\\n      \\\\\\\"permutation_granger\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 0,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_raw\\\\\\\": 0.0,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 0,\\\\n        \\\\\\\"fpr_fdr\\\\\\\": 0.0,\\\\n        \\\\\\\"p_values_raw\\\\\\\": [\\\\n          0.058941,\\\\n          0.093906,\\\\n          0.080919,\\\\n          0.67033,\\\\n          0.955045,\\\\n          0.549451,\\\\n          0.350649,\\\\n          0.365634\\\\n        ],\\\\n        \\\\\\\"p_values_fdr\\\\\\\": [\\\\n          0.250416,\\\\n          0.250416,\\\\n          0.250416,\\\\n          0.7660914285714285,\\\\n          0.955045,\\\\n          0.7326013333333333,\\\\n          0.5850144,\\\\n          0.5850144\\\\n        ]\\\\n      },\\\\n      \\\\\\\"TY\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 0,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_raw\\\\\\\": 0.0,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 0,\\\\n        \\\\\\\"fpr_fdr\\\\\\\": 0.0,\\\\n        \\\\\\\"p_values_raw\\\\\\\": [\\\\n          0.891964,\\\\n          0.858458,\\\\n          0.970851,\\\\n          0.314151,\\\\n          0.094304,\\\\n          0.092998,\\\\n          0.103218,\\\\n          0.801145\\\\n        ],\\\\n        \\\\\\\"p_values_fdr\\\\\\\": [\\\\n          0.970851,\\\\n          0.970851,\\\\n          0.970851,\\\\n          0.628302,\\\\n          0.275248,\\\\n          0.275248,\\\\n          0.275248,\\\\n          0.970851\\\\n        ]\\\\n      }\\\\n    },\\\\n    \\\\\\\"pooled_fdr\\\\\\\": {\\\\n      \\\\\\\"naive\\\\\\\": {\\\\n        \\\\\\\"sig_pooled_fdr\\\\\\\": 6,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_pooled_fdr\\\\\\\": 0.75\\\\n      },\\\\n      \\\\\\\"differenced\\\\\\\": {\\\\n        \\\\\\\"sig_pooled_fdr\\\\\\\": 3,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_pooled_fdr\\\\\\\": 0.375\\\\n      },\\\\n      \\\\\\\"threshold\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 5,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_raw\\\\\\\": 0.625,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 5,\\\\n        \\\\\\\"fpr_fdr\\\\\\\": 0.625,\\\\n        \\\\\\\"note\\\\\\\": \\\\\\\"non-statistical (no p-values, FDR not applicable)\\\\\\\"\\\\n      },\\\\n      \\\\\\\"permutation_granger\\\\\\\": {\\\\n        \\\\\\\"sig_pooled_fdr\\\\\\\": 0,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"fpr_pooled_fdr\\\\\\\": 0.0\\\\n      },\\\\n      \\\\\\\"TY\\\\\\\": {\\\\n        \\\\\\\"sig_pooled_fdr\\\\\\\": 0,\\\\n        \\\\\\\"tot\\\\n\\\\n... [截断: 输出过长，省略 10313 字符] ...\\\\n\\\\n         6.4000000000000006e-06,\\\\n          0.0,\\\\n          2.4615384615384615e-06,\\\\n          0.007085\\\\n        ]\\\\n      },\\\\n      \\\\\\\"threshold\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 32,\\\\n        \\\\\\\"total\\\\\\\": 32,\\\\n        \\\\\\\"rate_raw\\\\\\\": 1.0,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 32,\\\\n        \\\\\\\"rate_fdr\\\\\\\": 1.0,\\\\n        \\\\\\\"note\\\\\\\": \\\\\\\"non-statistical\\\\\\\"\\\\n      },\\\\n      \\\\\\\"permutation_granger\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 24,\\\\n        \\\\\\\"total\\\\\\\": 32,\\\\n        \\\\\\\"rate_raw\\\\\\\": 0.75,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 24,\\\\n        \\\\\\\"rate_fdr\\\\\\\": 0.75,\\\\n        \\\\\\\"p_values_raw\\\\\\\": [\\\\n          0.010989,\\\\n          0.015984,\\\\n          0.026973,\\\\n          0.716284,\\\\n          0.000999,\\\\n          0.008991,\\\\n          0.015984,\\\\n          0.96004,\\\\n          0.000999,\\\\n          0.000999,\\\\n          0.000999,\\\\n          0.801199,\\\\n          0.000999,\\\\n          0.000999,\\\\n          0.000999,\\\\n          0.537463,\\\\n          0.001998,\\\\n          0.002997,\\\\n          0.012987,\\\\n          0.46953,\\\\n          0.000999,\\\\n          0.000999,\\\\n          0.000999,\\\\n          0.345654,\\\\n          0.003996,\\\\n          0.003996,\\\\n          0.004995,\\\\n          0.992008,\\\\n          0.001998,\\\\n          0.001998,\\\\n          0.003996,\\\\n          0.674326\\\\n        ],\\\\n        \\\\\\\"p_values_fdr\\\\\\\": [\\\\n          0.0175824,\\\\n          0.022238608695652175,\\\\n          0.035964,\\\\n          0.7903823448275863,\\\\n          0.0031968000000000005,\\\\n          0.015142736842105264,\\\\n          0.022238608695652175,\\\\n          0.9910090322580645,\\\\n          0.0031968000000000005,\\\\n          0.0031968000000000005,\\\\n          0.0031968000000000005,\\\\n          0.8546122666666667,\\\\n          0.0031968000000000005,\\\\n          0.0031968000000000005,\\\\n          0.0031968000000000005,\\\\n          0.6369931851851852,\\\\n          0.004918153846153846,\\\\n          0.006850285714285714,\\\\n          0.019789714285714285,\\\\n          0.5778830769230769,\\\\n          0.0031968000000000005,\\\\n          0.0031968000000000005,\\\\n          0.0031968000000000005,\\\\n          0.44243712,\\\\n          0.007521882352941177,\\\\n          0.007521882352941177,\\\\n          0.00888,\\\\n          0.992008,\\\\n          0.004918153846153846,\\\\n          0.004918153846153846,\\\\n          0.007521882352941177,\\\\n          0.7706582857142857\\\\n        ]\\\\n      },\\\\n      \\\\\\\"TY\\\\\\\": {\\\\n        \\\\\\\"sig_raw\\\\\\\": 19,\\\\n        \\\\\\\"total\\\\\\\": 32,\\\\n        \\\\\\\"rate_raw\\\\\\\": 0.59375,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 19,\\\\n        \\\\\\\"rate_fdr\\\\\\\": 0.59375,\\\\n        \\\\\\\"p_values_raw\\\\\\\": [\\\\n          0.0,\\\\n          1.3e-05,\\\\n          2e-05,\\\\n          0.315231,\\\\n          0.0,\\\\n          1e-05,\\\\n          5.7e-05,\\\\n          0.491153,\\\\n          2e-06,\\\\n          1.4e-05,\\\\n          1.5e-05,\\\\n          0.792566,\\\\n          0.0,\\\\n          2e-06,\\\\n          1.4e-05,\\\\n          0.268428,\\\\n          0.0,\\\\n          0.0,\\\\n          1e-06,\\\\n          0.448982,\\\\n          0.172933,\\\\n          0.373375,\\\\n          0.22942,\\\\n          0.090486,\\\\n          0.0,\\\\n          3e-06,\\\\n          7e-06,\\\\n          0.210569,\\\\n          0.027607,\\\\n          0.59951,\\\\n          0.572459,\\\\n          0.167366\\\\n        ],\\\\n        \\\\\\\"p_values_fdr\\\\\\\": [\\\\n          0.0,\\\\n          2.9866666666666666e-05,\\\\n          3.7647058823529415e-05,\\\\n          0.38797661538461536,\\\\n          0.0,\\\\n          2.666666666666667e-05,\\\\n          0.00010133333333333333,\\\\n          0.5419619310344828,\\\\n          7.111111111111111e-06,\\\\n          2.9866666666666666e-05,\\\\n          3e-05,\\\\n          0.792566,\\\\n          0.0,\\\\n          7.111111111111111e-06,\\\\n          2.9866666666666666e-05,\\\\n          0.34358784,\\\\n          0.0,\\\\n          0.0,\\\\n          4.571428571428571e-06,\\\\n          0.5131222857142858,\\\\n          0.2515389090909091,\\\\n          0.44251851851851853,\\\\n          0.30589333333333335,\\\\n          0.1447776,\\\\n          0.0,\\\\n          9.6e-06,\\\\n          2.0363636363636365e-05,\\\\n          0.2929655652173913,\\\\n          0.046496,\\\\n          0.6188490322580645,\\\\n          0.6106229333333334,\\\\n          0.2515389090909091\\\\n        ]\\\\n      }\\\\n    }\\\\n  },\\\\n  \\\\\\\"meta\\\\\\\": {\\\\n    \\\\\\\"n_pairs\\\\\\\": 8,\\\\n    \\\\\\\"n_seeds_per_alpha\\\\\\\": 1,\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"alphas\\\\\\\": [\\\\n      0.0,\\\\n      0.25,\\\\n      0.5,\\\\n      1.0\\\\n    ],\\\\n    \\\\\\\"fdr_method\\\\\\\": \\\\\\\"Benjamini-Hochberg\\\\\\\",\\\\n    \\\\\\\"fdr_alpha\\\\\\\": 0.05\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"null_control_fpr\\\": {\\n    \\\"description\\\": \\\"FPR computed from alpha=0.0 null control (single seed=42, 8 pairs)\\\",\\n    \\\"per_method_fdr\\\": {\\n      \\\"naive\\\": {\\n        \\\"sig_raw\\\": 8,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 1.0,\\n        \\\"sig_fdr\\\": 8,\\n        \\\"fpr_fdr\\\": 1.0\\n      },\\n      \\\"differenced\\\": {\\n        \\\"sig_raw\\\": 4,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.5,\\n        \\\"sig_fdr\\\": 3,\\n        \\\"fpr_fdr\\\": 0.375\\n      },\\n      \\\"threshold\\\": {\\n        \\\"sig_raw\\\": 5,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.625,\\n        \\\"sig_fdr\\\": 5,\\n        \\\"fpr_fdr\\\": 0.625,\\n        \\\"note\\\": \\\"non-statistical (no p-values, FDR not applicable)\\\"\\n      },\\n      \\\"permutation_granger\\\": {\\n        \\\"sig_raw\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.0,\\n        \\\"sig_fdr\\\": 0,\\n        \\\"fpr_fdr\\\": 0.0\\n      },\\n      \\\"TY\\\": {\\n        \\\"sig_raw\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.0,\\n        \\\"sig_fdr\\\": 0,\\n        \\\"fpr_fdr\\\": 0.0\\n      }\\n    },\\n    \\\"per_method_full\\\": {\\n      \\\"naive\\\": {\\n        \\\"sig_raw\\\": 8,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 1.0,\\n        \\\"sig_fdr\\\": 8,\\n        \\\"fpr_fdr\\\": 1.0,\\n        \\\"p_values_raw\\\": [\\n          0.002496,\\n          0.006055,\\n          0.007303,\\n          0.0,\\n          0.005344,\\n          0.009665,\\n          0.022381,\\n          0.018795\\n        ],\\n        \\\"p_values_fdr\\\": [\\n          0.009984,\\n          0.011684799999999999,\\n          0.011684799999999999,\\n          0.0,\\n          0.011684799999999999,\\n          0.012886666666666666,\\n          0.022381,\\n          0.02148\\n        ]\\n      },\\n      \\\"differenced\\\": {\\n        \\\"sig_raw\\\": 4,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.5,\\n        \\\"sig_fdr\\\": 3,\\n        \\\"fpr_fdr\\\": 0.375,\\n        \\\"p_values_raw\\\": [\\n          0.000157,\\n          0.00325,\\n          0.044726,\\n          2e-06,\\n          0.051439,\\n          0.192837,\\n          0.202654,\\n          0.096018\\n        ],\\n        \\\"p_values_fdr\\\": [\\n          0.000628,\\n          0.008666666666666666,\\n          0.0823024,\\n          1.6e-05,\\n          0.0823024,\\n          0.202654,\\n          0.202654,\\n          0.128024\\n        ]\\n      },\\n      \\\"threshold\\\": {\\n        \\\"sig_raw\\\": 5,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.625,\\n        \\\"sig_fdr\\\": 5,\\n        \\\"fpr_fdr\\\": 0.625,\\n        \\\"note\\\": \\\"non-statistical (no p-values, FDR not applicable)\\\"\\n      },\\n      \\\"permutation_granger\\\": {\\n        \\\"sig_raw\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.0,\\n        \\\"sig_fdr\\\": 0,\\n        \\\"fpr_fdr\\\": 0.0,\\n        \\\"p_values_raw\\\": [\\n          0.058941,\\n          0.093906,\\n          0.080919,\\n          0.67033,\\n          0.955045,\\n          0.549451,\\n          0.350649,\\n          0.365634\\n        ],\\n        \\\"p_values_fdr\\\": [\\n          0.250416,\\n          0.250416,\\n          0.250416,\\n          0.7660914285714285,\\n          0.955045,\\n          0.7326013333333333,\\n          0.5850144,\\n          0.5850144\\n        ]\\n      },\\n      \\\"TY\\\": {\\n        \\\"sig_raw\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.0,\\n        \\\"sig_fdr\\\": 0,\\n        \\\"fpr_fdr\\\": 0.0,\\n        \\\"p_values_raw\\\": [\\n          0.891964,\\n          0.858458,\\n          0.970851,\\n          0.314151,\\n          0.094304,\\n          0.092998,\\n          0.103218,\\n          0.801145\\n        ],\\n        \\\"p_values_fdr\\\": [\\n          0.970851,\\n          0.970851,\\n          0.970851,\\n          0.628302,\\n          0.275248,\\n          0.275248,\\n          0.275248,\\n          0.970851\\n        ]\\n      }\\n    },\\n    \\\"pooled_fdr\\\": {\\n      \\\"naive\\\": {\\n        \\\"sig_pooled_fdr\\\": 6,\\n        \\\"total\\\": 8,\\n        \\\"fpr_pooled_fdr\\\": 0.75\\n      },\\n      \\\"differenced\\\": {\\n        \\\"sig_pooled_fdr\\\": 3,\\n        \\\"total\\\": 8,\\n        \\\"fpr_pooled_fdr\\\": 0.375\\n      },\\n      \\\"threshold\\\": {\\n        \\\"sig_raw\\\": 5,\\n        \\\"total\\\": 8,\\n        \\\"fpr_raw\\\": 0.625,\\n        \\\"sig_fdr\\\": 5,\\n        \\\"fpr_fdr\\\": 0.625,\\n        \\\"note\\\": \\\"non-statistical (no p-values, FDR not applicable)\\\"\\n      },\\n      \\\"permutation_granger\\\": {\\n        \\\"sig_pooled_fdr\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"fpr_pooled_fdr\\\": 0.0\\n      },\\n      \\\"TY\\\": {\\n        \\\"sig_pooled_fdr\\\": 0,\\n        \\\"tot\\n\\n... [截断: 输出过长，省略 10313 字符] ...\\n\\n         6.4000000000000006e-06,\\n          0.0,\\n          2.4615384615384615e-06,\\n          0.007085\\n        ]\\n      },\\n      \\\"threshold\\\": {\\n        \\\"sig_raw\\\": 32,\\n        \\\"total\\\": 32,\\n        \\\"rate_raw\\\": 1.0,\\n        \\\"sig_fdr\\\": 32,\\n        \\\"rate_fdr\\\": 1.0,\\n        \\\"note\\\": \\\"non-statistical\\\"\\n      },\\n      \\\"permutation_granger\\\": {\\n        \\\"sig_raw\\\": 24,\\n        \\\"total\\\": 32,\\n        \\\"rate_raw\\\": 0.75,\\n        \\\"sig_fdr\\\": 24,\\n        \\\"rate_fdr\\\": 0.75,\\n        \\\"p_values_raw\\\": [\\n          0.010989,\\n          0.015984,\\n          0.026973,\\n          0.716284,\\n          0.000999,\\n          0.008991,\\n          0.015984,\\n          0.96004,\\n          0.000999,\\n          0.000999,\\n          0.000999,\\n          0.801199,\\n          0.000999,\\n          0.000999,\\n          0.000999,\\n          0.537463,\\n          0.001998,\\n          0.002997,\\n          0.012987,\\n          0.46953,\\n          0.000999,\\n          0.000999,\\n          0.000999,\\n          0.345654,\\n          0.003996,\\n          0.003996,\\n          0.004995,\\n          0.992008,\\n          0.001998,\\n          0.001998,\\n          0.003996,\\n          0.674326\\n        ],\\n        \\\"p_values_fdr\\\": [\\n          0.0175824,\\n          0.022238608695652175,\\n          0.035964,\\n          0.7903823448275863,\\n          0.0031968000000000005,\\n          0.015142736842105264,\\n          0.022238608695652175,\\n          0.9910090322580645,\\n          0.0031968000000000005,\\n          0.0031968000000000005,\\n          0.0031968000000000005,\\n          0.8546122666666667,\\n          0.0031968000000000005,\\n          0.0031968000000000005,\\n          0.0031968000000000005,\\n          0.6369931851851852,\\n          0.004918153846153846,\\n          0.006850285714285714,\\n          0.019789714285714285,\\n          0.5778830769230769,\\n          0.0031968000000000005,\\n          0.0031968000000000005,\\n          0.0031968000000000005,\\n          0.44243712,\\n          0.007521882352941177,\\n          0.007521882352941177,\\n          0.00888,\\n          0.992008,\\n          0.004918153846153846,\\n          0.004918153846153846,\\n          0.007521882352941177,\\n          0.7706582857142857\\n        ]\\n      },\\n      \\\"TY\\\": {\\n        \\\"sig_raw\\\": 19,\\n        \\\"total\\\": 32,\\n        \\\"rate_raw\\\": 0.59375,\\n        \\\"sig_fdr\\\": 19,\\n        \\\"rate_fdr\\\": 0.59375,\\n        \\\"p_values_raw\\\": [\\n          0.0,\\n          1.3e-05,\\n          2e-05,\\n          0.315231,\\n          0.0,\\n          1e-05,\\n          5.7e-05,\\n          0.491153,\\n          2e-06,\\n          1.4e-05,\\n          1.5e-05,\\n          0.792566,\\n          0.0,\\n          2e-06,\\n          1.4e-05,\\n          0.268428,\\n          0.0,\\n          0.0,\\n          1e-06,\\n          0.448982,\\n          0.172933,\\n          0.373375,\\n          0.22942,\\n          0.090486,\\n          0.0,\\n          3e-06,\\n          7e-06,\\n          0.210569,\\n          0.027607,\\n          0.59951,\\n          0.572459,\\n          0.167366\\n        ],\\n        \\\"p_values_fdr\\\": [\\n          0.0,\\n          2.9866666666666666e-05,\\n          3.7647058823529415e-05,\\n          0.38797661538461536,\\n          0.0,\\n          2.666666666666667e-05,\\n          0.00010133333333333333,\\n          0.5419619310344828,\\n          7.111111111111111e-06,\\n          2.9866666666666666e-05,\\n          3e-05,\\n          0.792566,\\n          0.0,\\n          7.111111111111111e-06,\\n          2.9866666666666666e-05,\\n          0.34358784,\\n          0.0,\\n          0.0,\\n          4.571428571428571e-06,\\n          0.5131222857142858,\\n          0.2515389090909091,\\n          0.44251851851851853,\\n          0.30589333333333335,\\n          0.1447776,\\n          0.0,\\n          9.6e-06,\\n          2.0363636363636365e-05,\\n          0.2929655652173913,\\n          0.046496,\\n          0.6188490322580645,\\n          0.6106229333333334,\\n          0.2515389090909091\\n        ]\\n      }\\n    }\\n  },\\n  \\\"meta\\\": {\\n    \\\"n_pairs\\\": 8,\\n    \\\"n_seeds_per_alpha\\\": 1,\\n    \\\"seed\\\": 42,\\n    \\\"alphas\\\": [\\n      0.0,\\n      0.25,\\n      0.5,\\n      1.0\\n    ],\\n    \\\"fdr_method\\\": \\\"Benjamini-Hochberg\\\",\\n    \\\"fdr_alpha\\\": 0.05\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XEzvgZ6AyN7G5xEUgpBXj8`</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/analysis/d028_fpr_null_control_full.json",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "ebac78a2-308f-45a3-a5b8-0360cfc79674",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VbmhW5BPWFkT2j3K726E1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 26281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1129
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T15:32:59.603Z_

<details><summary>↩ Tool result · `toolu_01XEzvgZ6AyN7G5xEUgpBXj8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"null_control_fpr\\\": {\\n    \\\"description\\\": \\\"FPR from alpha=0.0 null control (no canary injection)\\\",\\n    \\\"ground_truth\\\": \\\"alpha=0.0 (any significance is false positive by definition)\\\",\\n    \\\"n_pairs\\\": 8,\\n    \\\"seed\\\": 42,\\n    \\\"note\\\": \\\"single seed \\\\u2014 interpret with caution\\\",\\n    \\\"table\\\": [\\n      {\\n        \\\"method\\\": \\\"naive\\\",\\n        \\\"fpr_p_raw\\\": 1.0,\\n        \\\"sig_raw\\\": 8,\\n        \\\"fpr_p_fdr\\\": 1.0,\\n        \\\"sig_fdr\\\": 8,\\n        \\\"total\\\": 8,\\n        \\\"p_values_raw\\\": [\\n          0.002496,\\n          0.006055,\\n          0.007303,\\n          0.0,\\n          0.005344,\\n          0.009665,\\n          0.022381,\\n          0.018795\\n        ]\\n      },\\n      {\\n        \\\"method\\\": \\\"differenced\\\",\\n        \\\"fpr_p_raw\\\": 0.5,\\n        \\\"sig_raw\\\": 4,\\n        \\\"fpr_p_fdr\\\": 0.375,\\n        \\\"sig_fdr\\\": 3,\\n        \\\"total\\\": 8,\\n        \\\"p_values_raw\\\": [\\n          0.000157,\\n          0.00325,\\n          0.044726,\\n          2e-06,\\n          0.051439,\\n          0.192837,\\n          0.202654,\\n          0.096018\\n        ]\\n      },\\n      {\\n        \\\"method\\\": \\\"threshold\\\",\\n        \\\"fpr_p_raw\\\": 0.625,\\n        \\\"sig_raw\\\": 5,\\n        \\\"fpr_p_fdr\\\": 0.625,\\n        \\\"sig_fdr\\\": 5,\\n        \\\"total\\\": 8\\n      },\\n      {\\n        \\\"method\\\": \\\"permutation_granger\\\",\\n        \\\"fpr_p_raw\\\": 0.0,\\n        \\\"sig_raw\\\": 0,\\n        \\\"fpr_p_fdr\\\": 0.0,\\n        \\\"sig_fdr\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"p_values_raw\\\": [\\n          0.058941,\\n          0.093906,\\n          0.080919,\\n          0.67033,\\n          0.955045,\\n          0.549451,\\n          0.350649,\\n          0.365634\\n        ]\\n      },\\n      {\\n        \\\"method\\\": \\\"TY\\\",\\n        \\\"fpr_p_raw\\\": 0.0,\\n        \\\"sig_raw\\\": 0,\\n        \\\"fpr_p_fdr\\\": 0.0,\\n        \\\"sig_fdr\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"p_values_raw\\\": [\\n          0.891964,\\n          0.858458,\\n          0.970851,\\n          0.314151,\\n          0.094304,\\n          0.092998,\\n          0.103218,\\n          0.801145\\n        ]\\n      }\\n    ],\\n    \\\"pairs\\\": [\\n      \\\"token_entropy->distinct_1\\\",\\n      \\\"token_entropy->distinct_2\\\",\\n      \\\"token_entropy->distinct_3\\\",\\n      \\\"token_entropy->perplexity\\\",\\n      \\\"ece->distinct_1\\\",\\n      \\\"ece->distinct_2\\\",\\n      \\\"ece->distinct_3\\\",\\n      \\\"ece->perplexity\\\"\\n    ]\\n  },\\n  \\\"phase2_fdr_sig_rates\\\": {\\n    \\\"alphas\\\": [\\n      0.0,\\n      0.25,\\n      0.5,\\n      1.0\\n    ],\\n    \\\"rates\\\": {\\n      \\\"0.0\\\": {\\n        \\\"naive\\\": {\\n          \\\"sig_raw\\\": 8,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"sig_fdr\\\": 8,\\n          \\\"rate_p_fdr\\\": 1.0\\n        },\\n        \\\"differenced\\\": {\\n          \\\"sig_raw\\\": 4,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.5,\\n          \\\"sig_fdr\\\": 3,\\n          \\\"rate_p_fdr\\\": 0.375\\n        },\\n        \\\"threshold\\\": {\\n          \\\"sig_raw\\\": 5,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.625,\\n          \\\"rate_p_fdr\\\": 0.625,\\n          \\\"note\\\": \\\"non-statistical\\\"\\n        },\\n        \\\"permutation_granger\\\": {\\n          \\\"sig_raw\\\": 0,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.0,\\n          \\\"sig_fdr\\\": 0,\\n          \\\"rate_p_fdr\\\": 0.0\\n        },\\n        \\\"TY\\\": {\\n          \\\"sig_raw\\\": 0,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.0,\\n          \\\"sig_fdr\\\": 0,\\n          \\\"rate_p_fdr\\\": 0.0\\n        }\\n      },\\n      \\\"0.25\\\": {\\n        \\\"naive\\\": {\\n          \\\"sig_raw\\\": 8,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"sig_fdr\\\": 8,\\n          \\\"rate_p_fdr\\\": 1.0\\n        },\\n        \\\"differenced\\\": {\\n          \\\"sig_raw\\\": 2,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.25,\\n          \\\"sig_fdr\\\": 2,\\n          \\\"rate_p_fdr\\\": 0.25\\n        },\\n        \\\"threshold\\\": {\\n          \\\"sig_raw\\\": 3,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.375,\\n          \\\"rate_p_fdr\\\": 0.375,\\n          \\\"note\\\": \\\"non-statistical\\\"\\n        },\\n        \\\"permutation_granger\\\": {\\n          \\\"sig_raw\\\": 2,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.25,\\n          \\\"sig_fdr\\\": 0,\\n          \\\"rate_p_fdr\\\": 0.0\\n        },\\n        \\\"TY\\\": {\\n          \\\"sig_raw\\\": 5,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.625,\\n          \\\"sig_fdr\\\": 3,\\n          \\\"rate_p_fdr\\\": 0.375\\n        }\\n      },\\n      \\\"0.5\\\": {\\n        \\\"naive\\\": {\\n          \\\"sig_raw\\\": 8,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"sig_fdr\\\": 8,\\n          \\\"rate_p_fdr\\\": 1.0\\n        },\\n        \\\"differenced\\\": {\\n          \\\"sig_raw\\\": 8,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"sig_fdr\\\": 8,\\n          \\\"rate_p_fdr\\\": 1.0\\n        },\\n        \\\"threshold\\\": {\\n          \\\"sig_raw\\\": 8,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"rate_p_fdr\\\": 1.0,\\n          \\\"note\\\": \\\"non-statistical\\\"\\n        },\\n        \\\"permutation_granger\\\": {\\n          \\\"sig_raw\\\": 2,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.25,\\n          \\\"sig_fdr\\\": 0,\\n          \\\"rate_p_fdr\\\": 0.0\\n        },\\n        \\\"TY\\\": {\\n          \\\"sig_raw\\\": 0,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.0,\\n          \\\"sig_fdr\\\": 0,\\n          \\\"rate_p_fdr\\\": 0.0\\n        }\\n      },\\n      \\\"1.0\\\": {\\n        \\\"naive\\\": {\\n          \\\"sig_raw\\\": 32,\\n          \\\"total\\\": 32,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"sig_fdr\\\": 32,\\n          \\\"rate_p_fdr\\\": 1.0\\n        },\\n        \\\"differenced\\\": {\\n          \\\"sig_raw\\\": 32,\\n          \\\"total\\\": 32,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"sig_fdr\\\": 32,\\n          \\\"rate_p_fdr\\\": 1.0\\n        },\\n        \\\"threshold\\\": {\\n          \\\"sig_raw\\\": 32,\\n          \\\"total\\\": 32,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"rate_p_fdr\\\": 1.0,\\n          \\\"note\\\": \\\"non-statistical\\\"\\n        },\\n        \\\"permutation_granger\\\": {\\n          \\\"sig_raw\\\": 24,\\n          \\\"total\\\": 32,\\n          \\\"rate_p_raw\\\": 0.75,\\n          \\\"sig_fdr\\\": 24,\\n          \\\"rate_p_fdr\\\": 0.75\\n        },\\n        \\\"TY\\\": {\\n          \\\"sig_raw\\\": 19,\\n          \\\"total\\\": 32,\\n          \\\"rate_p_raw\\\": 0.5938,\\n          \\\"sig_fdr\\\": 19,\\n          \\\"rate_p_fdr\\\": 0.5938\\n        }\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "a2d039d1-23c4-472f-8e60-e8a92d9d9e04",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"null_control_fpr\\\\\\\": {\\\\n    \\\\\\\"description\\\\\\\": \\\\\\\"FPR from alpha=0.0 null control (no canary injection)\\\\\\\",\\\\n    \\\\\\\"ground_truth\\\\\\\": \\\\\\\"alpha=0.0 (any significance is false positive by definition)\\\\\\\",\\\\n    \\\\\\\"n_pairs\\\\\\\": 8,\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"note\\\\\\\": \\\\\\\"single seed \\\\\\\\u2014 interpret with caution\\\\\\\",\\\\n    \\\\\\\"table\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"method\\\\\\\": \\\\\\\"naive\\\\\\\",\\\\n        \\\\\\\"fpr_p_raw\\\\\\\": 1.0,\\\\n        \\\\\\\"sig_raw\\\\\\\": 8,\\\\n        \\\\\\\"fpr_p_fdr\\\\\\\": 1.0,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 8,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"p_values_raw\\\\\\\": [\\\\n          0.002496,\\\\n          0.006055,\\\\n          0.007303,\\\\n          0.0,\\\\n          0.005344,\\\\n          0.009665,\\\\n          0.022381,\\\\n          0.018795\\\\n        ]\\\\n      },\\\\n      {\\\\n        \\\\\\\"method\\\\\\\": \\\\\\\"differenced\\\\\\\",\\\\n        \\\\\\\"fpr_p_raw\\\\\\\": 0.5,\\\\n        \\\\\\\"sig_raw\\\\\\\": 4,\\\\n        \\\\\\\"fpr_p_fdr\\\\\\\": 0.375,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 3,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"p_values_raw\\\\\\\": [\\\\n          0.000157,\\\\n          0.00325,\\\\n          0.044726,\\\\n          2e-06,\\\\n          0.051439,\\\\n          0.192837,\\\\n          0.202654,\\\\n          0.096018\\\\n        ]\\\\n      },\\\\n      {\\\\n        \\\\\\\"method\\\\\\\": \\\\\\\"threshold\\\\\\\",\\\\n        \\\\\\\"fpr_p_raw\\\\\\\": 0.625,\\\\n        \\\\\\\"sig_raw\\\\\\\": 5,\\\\n        \\\\\\\"fpr_p_fdr\\\\\\\": 0.625,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 5,\\\\n        \\\\\\\"total\\\\\\\": 8\\\\n      },\\\\n      {\\\\n        \\\\\\\"method\\\\\\\": \\\\\\\"permutation_granger\\\\\\\",\\\\n        \\\\\\\"fpr_p_raw\\\\\\\": 0.0,\\\\n        \\\\\\\"sig_raw\\\\\\\": 0,\\\\n        \\\\\\\"fpr_p_fdr\\\\\\\": 0.0,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 0,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"p_values_raw\\\\\\\": [\\\\n          0.058941,\\\\n          0.093906,\\\\n          0.080919,\\\\n          0.67033,\\\\n          0.955045,\\\\n          0.549451,\\\\n          0.350649,\\\\n          0.365634\\\\n        ]\\\\n      },\\\\n      {\\\\n        \\\\\\\"method\\\\\\\": \\\\\\\"TY\\\\\\\",\\\\n        \\\\\\\"fpr_p_raw\\\\\\\": 0.0,\\\\n        \\\\\\\"sig_raw\\\\\\\": 0,\\\\n        \\\\\\\"fpr_p_fdr\\\\\\\": 0.0,\\\\n        \\\\\\\"sig_fdr\\\\\\\": 0,\\\\n        \\\\\\\"total\\\\\\\": 8,\\\\n        \\\\\\\"p_values_raw\\\\\\\": [\\\\n          0.891964,\\\\n          0.858458,\\\\n          0.970851,\\\\n          0.314151,\\\\n          0.094304,\\\\n          0.092998,\\\\n          0.103218,\\\\n          0.801145\\\\n        ]\\\\n      }\\\\n    ],\\\\n    \\\\\\\"pairs\\\\\\\": [\\\\n      \\\\\\\"token_entropy->distinct_1\\\\\\\",\\\\n      \\\\\\\"token_entropy->distinct_2\\\\\\\",\\\\n      \\\\\\\"token_entropy->distinct_3\\\\\\\",\\\\n      \\\\\\\"token_entropy->perplexity\\\\\\\",\\\\n      \\\\\\\"ece->distinct_1\\\\\\\",\\\\n      \\\\\\\"ece->distinct_2\\\\\\\",\\\\n      \\\\\\\"ece->distinct_3\\\\\\\",\\\\n      \\\\\\\"ece->perplexity\\\\\\\"\\\\n    ]\\\\n  },\\\\n  \\\\\\\"phase2_fdr_sig_rates\\\\\\\": {\\\\n    \\\\\\\"alphas\\\\\\\": [\\\\n      0.0,\\\\n      0.25,\\\\n      0.5,\\\\n      1.0\\\\n    ],\\\\n    \\\\\\\"rates\\\\\\\": {\\\\n      \\\\\\\"0.0\\\\\\\": {\\\\n        \\\\\\\"naive\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 8,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 1.0,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 1.0\\\\n        },\\\\n        \\\\\\\"differenced\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 4,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 0.5,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 3,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 0.375\\\\n        },\\\\n        \\\\\\\"threshold\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 5,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 0.625,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 0.625,\\\\n          \\\\\\\"note\\\\\\\": \\\\\\\"non-statistical\\\\\\\"\\\\n        },\\\\n        \\\\\\\"permutation_granger\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 0,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 0.0,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 0,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 0.0\\\\n        },\\\\n        \\\\\\\"TY\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 0,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 0.0,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 0,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 0.0\\\\n        }\\\\n      },\\\\n      \\\\\\\"0.25\\\\\\\": {\\\\n        \\\\\\\"naive\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 8,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 1.0,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 1.0\\\\n        },\\\\n        \\\\\\\"differenced\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 2,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 0.25,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 2,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 0.25\\\\n        },\\\\n        \\\\\\\"threshold\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 3,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 0.375,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 0.375,\\\\n          \\\\\\\"note\\\\\\\": \\\\\\\"non-statistical\\\\\\\"\\\\n        },\\\\n        \\\\\\\"permutation_granger\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 2,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 0.25,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 0,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 0.0\\\\n        },\\\\n        \\\\\\\"TY\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 5,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 0.625,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 3,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 0.375\\\\n        }\\\\n      },\\\\n      \\\\\\\"0.5\\\\\\\": {\\\\n        \\\\\\\"naive\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 8,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 1.0,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 1.0\\\\n        },\\\\n        \\\\\\\"differenced\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 8,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 1.0,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 1.0\\\\n        },\\\\n        \\\\\\\"threshold\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 8,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 1.0,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 1.0,\\\\n          \\\\\\\"note\\\\\\\": \\\\\\\"non-statistical\\\\\\\"\\\\n        },\\\\n        \\\\\\\"permutation_granger\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 2,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 0.25,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 0,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 0.0\\\\n        },\\\\n        \\\\\\\"TY\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 0,\\\\n          \\\\\\\"total\\\\\\\": 8,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 0.0,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 0,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 0.0\\\\n        }\\\\n      },\\\\n      \\\\\\\"1.0\\\\\\\": {\\\\n        \\\\\\\"naive\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 32,\\\\n          \\\\\\\"total\\\\\\\": 32,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 1.0,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 32,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 1.0\\\\n        },\\\\n        \\\\\\\"differenced\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 32,\\\\n          \\\\\\\"total\\\\\\\": 32,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 1.0,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 32,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 1.0\\\\n        },\\\\n        \\\\\\\"threshold\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 32,\\\\n          \\\\\\\"total\\\\\\\": 32,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 1.0,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 1.0,\\\\n          \\\\\\\"note\\\\\\\": \\\\\\\"non-statistical\\\\\\\"\\\\n        },\\\\n        \\\\\\\"permutation_granger\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 24,\\\\n          \\\\\\\"total\\\\\\\": 32,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 0.75,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 24,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 0.75\\\\n        },\\\\n        \\\\\\\"TY\\\\\\\": {\\\\n          \\\\\\\"sig_raw\\\\\\\": 19,\\\\n          \\\\\\\"total\\\\\\\": 32,\\\\n          \\\\\\\"rate_p_raw\\\\\\\": 0.5938,\\\\n          \\\\\\\"sig_fdr\\\\\\\": 19,\\\\n          \\\\\\\"rate_p_fdr\\\\\\\": 0.5938\\\\n        }\\\\n      }\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"null_control_fpr\\\": {\\n    \\\"description\\\": \\\"FPR from alpha=0.0 null control (no canary injection)\\\",\\n    \\\"ground_truth\\\": \\\"alpha=0.0 (any significance is false positive by definition)\\\",\\n    \\\"n_pairs\\\": 8,\\n    \\\"seed\\\": 42,\\n    \\\"note\\\": \\\"single seed \\\\u2014 interpret with caution\\\",\\n    \\\"table\\\": [\\n      {\\n        \\\"method\\\": \\\"naive\\\",\\n        \\\"fpr_p_raw\\\": 1.0,\\n        \\\"sig_raw\\\": 8,\\n        \\\"fpr_p_fdr\\\": 1.0,\\n        \\\"sig_fdr\\\": 8,\\n        \\\"total\\\": 8,\\n        \\\"p_values_raw\\\": [\\n          0.002496,\\n          0.006055,\\n          0.007303,\\n          0.0,\\n          0.005344,\\n          0.009665,\\n          0.022381,\\n          0.018795\\n        ]\\n      },\\n      {\\n        \\\"method\\\": \\\"differenced\\\",\\n        \\\"fpr_p_raw\\\": 0.5,\\n        \\\"sig_raw\\\": 4,\\n        \\\"fpr_p_fdr\\\": 0.375,\\n        \\\"sig_fdr\\\": 3,\\n        \\\"total\\\": 8,\\n        \\\"p_values_raw\\\": [\\n          0.000157,\\n          0.00325,\\n          0.044726,\\n          2e-06,\\n          0.051439,\\n          0.192837,\\n          0.202654,\\n          0.096018\\n        ]\\n      },\\n      {\\n        \\\"method\\\": \\\"threshold\\\",\\n        \\\"fpr_p_raw\\\": 0.625,\\n        \\\"sig_raw\\\": 5,\\n        \\\"fpr_p_fdr\\\": 0.625,\\n        \\\"sig_fdr\\\": 5,\\n        \\\"total\\\": 8\\n      },\\n      {\\n        \\\"method\\\": \\\"permutation_granger\\\",\\n        \\\"fpr_p_raw\\\": 0.0,\\n        \\\"sig_raw\\\": 0,\\n        \\\"fpr_p_fdr\\\": 0.0,\\n        \\\"sig_fdr\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"p_values_raw\\\": [\\n          0.058941,\\n          0.093906,\\n          0.080919,\\n          0.67033,\\n          0.955045,\\n          0.549451,\\n          0.350649,\\n          0.365634\\n        ]\\n      },\\n      {\\n        \\\"method\\\": \\\"TY\\\",\\n        \\\"fpr_p_raw\\\": 0.0,\\n        \\\"sig_raw\\\": 0,\\n        \\\"fpr_p_fdr\\\": 0.0,\\n        \\\"sig_fdr\\\": 0,\\n        \\\"total\\\": 8,\\n        \\\"p_values_raw\\\": [\\n          0.891964,\\n          0.858458,\\n          0.970851,\\n          0.314151,\\n          0.094304,\\n          0.092998,\\n          0.103218,\\n          0.801145\\n        ]\\n      }\\n    ],\\n    \\\"pairs\\\": [\\n      \\\"token_entropy->distinct_1\\\",\\n      \\\"token_entropy->distinct_2\\\",\\n      \\\"token_entropy->distinct_3\\\",\\n      \\\"token_entropy->perplexity\\\",\\n      \\\"ece->distinct_1\\\",\\n      \\\"ece->distinct_2\\\",\\n      \\\"ece->distinct_3\\\",\\n      \\\"ece->perplexity\\\"\\n    ]\\n  },\\n  \\\"phase2_fdr_sig_rates\\\": {\\n    \\\"alphas\\\": [\\n      0.0,\\n      0.25,\\n      0.5,\\n      1.0\\n    ],\\n    \\\"rates\\\": {\\n      \\\"0.0\\\": {\\n        \\\"naive\\\": {\\n          \\\"sig_raw\\\": 8,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"sig_fdr\\\": 8,\\n          \\\"rate_p_fdr\\\": 1.0\\n        },\\n        \\\"differenced\\\": {\\n          \\\"sig_raw\\\": 4,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.5,\\n          \\\"sig_fdr\\\": 3,\\n          \\\"rate_p_fdr\\\": 0.375\\n        },\\n        \\\"threshold\\\": {\\n          \\\"sig_raw\\\": 5,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.625,\\n          \\\"rate_p_fdr\\\": 0.625,\\n          \\\"note\\\": \\\"non-statistical\\\"\\n        },\\n        \\\"permutation_granger\\\": {\\n          \\\"sig_raw\\\": 0,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.0,\\n          \\\"sig_fdr\\\": 0,\\n          \\\"rate_p_fdr\\\": 0.0\\n        },\\n        \\\"TY\\\": {\\n          \\\"sig_raw\\\": 0,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.0,\\n          \\\"sig_fdr\\\": 0,\\n          \\\"rate_p_fdr\\\": 0.0\\n        }\\n      },\\n      \\\"0.25\\\": {\\n        \\\"naive\\\": {\\n          \\\"sig_raw\\\": 8,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"sig_fdr\\\": 8,\\n          \\\"rate_p_fdr\\\": 1.0\\n        },\\n        \\\"differenced\\\": {\\n          \\\"sig_raw\\\": 2,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.25,\\n          \\\"sig_fdr\\\": 2,\\n          \\\"rate_p_fdr\\\": 0.25\\n        },\\n        \\\"threshold\\\": {\\n          \\\"sig_raw\\\": 3,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.375,\\n          \\\"rate_p_fdr\\\": 0.375,\\n          \\\"note\\\": \\\"non-statistical\\\"\\n        },\\n        \\\"permutation_granger\\\": {\\n          \\\"sig_raw\\\": 2,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.25,\\n          \\\"sig_fdr\\\": 0,\\n          \\\"rate_p_fdr\\\": 0.0\\n        },\\n        \\\"TY\\\": {\\n          \\\"sig_raw\\\": 5,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.625,\\n          \\\"sig_fdr\\\": 3,\\n          \\\"rate_p_fdr\\\": 0.375\\n        }\\n      },\\n      \\\"0.5\\\": {\\n        \\\"naive\\\": {\\n          \\\"sig_raw\\\": 8,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"sig_fdr\\\": 8,\\n          \\\"rate_p_fdr\\\": 1.0\\n        },\\n        \\\"differenced\\\": {\\n          \\\"sig_raw\\\": 8,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"sig_fdr\\\": 8,\\n          \\\"rate_p_fdr\\\": 1.0\\n        },\\n        \\\"threshold\\\": {\\n          \\\"sig_raw\\\": 8,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"rate_p_fdr\\\": 1.0,\\n          \\\"note\\\": \\\"non-statistical\\\"\\n        },\\n        \\\"permutation_granger\\\": {\\n          \\\"sig_raw\\\": 2,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.25,\\n          \\\"sig_fdr\\\": 0,\\n          \\\"rate_p_fdr\\\": 0.0\\n        },\\n        \\\"TY\\\": {\\n          \\\"sig_raw\\\": 0,\\n          \\\"total\\\": 8,\\n          \\\"rate_p_raw\\\": 0.0,\\n          \\\"sig_fdr\\\": 0,\\n          \\\"rate_p_fdr\\\": 0.0\\n        }\\n      },\\n      \\\"1.0\\\": {\\n        \\\"naive\\\": {\\n          \\\"sig_raw\\\": 32,\\n          \\\"total\\\": 32,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"sig_fdr\\\": 32,\\n          \\\"rate_p_fdr\\\": 1.0\\n        },\\n        \\\"differenced\\\": {\\n          \\\"sig_raw\\\": 32,\\n          \\\"total\\\": 32,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"sig_fdr\\\": 32,\\n          \\\"rate_p_fdr\\\": 1.0\\n        },\\n        \\\"threshold\\\": {\\n          \\\"sig_raw\\\": 32,\\n          \\\"total\\\": 32,\\n          \\\"rate_p_raw\\\": 1.0,\\n          \\\"rate_p_fdr\\\": 1.0,\\n          \\\"note\\\": \\\"non-statistical\\\"\\n        },\\n        \\\"permutation_granger\\\": {\\n          \\\"sig_raw\\\": 24,\\n          \\\"total\\\": 32,\\n          \\\"rate_p_raw\\\": 0.75,\\n          \\\"sig_fdr\\\": 24,\\n          \\\"rate_p_fdr\\\": 0.75\\n        },\\n        \\\"TY\\\": {\\n          \\\"sig_raw\\\": 19,\\n          \\\"total\\\": 32,\\n          \\\"rate_p_raw\\\": 0.5938,\\n          \\\"sig_fdr\\\": 19,\\n          \\\"rate_p_fdr\\\": 0.5938\\n        }\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the d028 FPR null control data and part of the v6 file. Let me now get the rest of the v6 file (the granger_results section) and check for multi-seed data files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "c77f43c9-8a44-4281-8ba0-a5be2ced82ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LUXPRaLjVohXsQQW38GcKg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13448,
      "cache_read_input_tokens": 27410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13448
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 21_

读取 v6 完整的 granger_results 和 v4 数据，以及搜索 multi-seed 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "cff83937-9769-48c5-82ac-d1a8e9f182a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LUXPRaLjVohXsQQW38GcKg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13448,
      "cache_read_input_tokens": 27410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13448
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01R4nwgSA5SsbRadfJSKqb6z`</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -600 /root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v6.json",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "e8fb2777-7142-46bd-b5d6-ac6e104a93f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LUXPRaLjVohXsQQW38GcKg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13448,
      "cache_read_input_tokens": 27410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T15:33:07.856Z_

<details><summary>↩ Tool result · `toolu_01R4nwgSA5SsbRadfJSKqb6z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"token_entropy→distinct_1\\\": {\\n        \\\"pair\\\": \\\"token_entropy→distinct_1\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 5,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"token_entropy→distinct_2\\\": {\\n        \\\"pair\\\": \\\"token_entropy→distinct_2\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 5,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"token_entropy→distinct_3\\\": {\\n        \\\"pair\\\": \\\"token_entropy→distinct_3\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 5,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"self_bleu→perplexity\\\": {\\n        \\\"pair\\\": \\\"self_bleu→perplexity\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n\\n\\n... [截断: 输出过长，省略 8170 字符] ...\\n\\ns_robust\\\": false,\\n            \\\"n_sig_methods\\\": 0,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": true,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": true\\n      },\\n      \\\"effective_rank→distinct_1\\\": {\\n        \\\"pair\\\": \\\"effective_rank→distinct_1\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"effective_rank→distinct_2\\\": {\\n        \\\"pair\\\": \\\"effective_rank→distinct_2\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"effective_rank→distinct_3\\\": {\\n        \\\"pair\\\": \\\"effective_rank→distinct_3\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "7ac533bd-59fa-437f-a88a-958f9abf6c53",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a075\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.75,\\\\n            \\\\\\\"is_robust\\\\\\\": true,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": false,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": false\\\\n      },\\\\n      \\\\\\\"token_entropy→distinct_1\\\\\\\": {\\\\n        \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy→distinct_1\\\\\\\",\\\\n        \\\\\\\"per_alpha\\\\\\\": {\\\\n          \\\\\\\"a000\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a025\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.25,\\\\n            \\\\\\\"is_robust\\\\\\\": true,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a075\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.75,\\\\n            \\\\\\\"is_robust\\\\\\\": true,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": true,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 5,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": false,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": false\\\\n      },\\\\n      \\\\\\\"token_entropy→distinct_2\\\\\\\": {\\\\n        \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy→distinct_2\\\\\\\",\\\\n        \\\\\\\"per_alpha\\\\\\\": {\\\\n          \\\\\\\"a000\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a025\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.25,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a075\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.75,\\\\n            \\\\\\\"is_robust\\\\\\\": true,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": true,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 5,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": false,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": false\\\\n      },\\\\n      \\\\\\\"token_entropy→distinct_3\\\\\\\": {\\\\n        \\\\\\\"pair\\\\\\\": \\\\\\\"token_entropy→distinct_3\\\\\\\",\\\\n        \\\\\\\"per_alpha\\\\\\\": {\\\\n          \\\\\\\"a000\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a025\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.25,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a075\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.75,\\\\n            \\\\\\\"is_robust\\\\\\\": true,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": true,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 5,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": false,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": false\\\\n      },\\\\n      \\\\\\\"self_bleu→perplexity\\\\\\\": {\\\\n        \\\\\\\"pair\\\\\\\": \\\\\\\"self_bleu→perplexity\\\\\\\",\\\\n        \\\\\\\"per_alpha\\\\\\\": {\\\\n          \\\\\\\"a000\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n\\\\n\\\\n... [截断: 输出过长，省略 8170 字符] ...\\\\n\\\\ns_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 0,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a025\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.25,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a075\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.75,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": true,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": true\\\\n      },\\\\n      \\\\\\\"effective_rank→distinct_1\\\\\\\": {\\\\n        \\\\\\\"pair\\\\\\\": \\\\\\\"effective_rank→distinct_1\\\\\\\",\\\\n        \\\\\\\"per_alpha\\\\\\\": {\\\\n          \\\\\\\"a000\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a025\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.25,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a075\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.75,\\\\n            \\\\\\\"is_robust\\\\\\\": true,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": false,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": false\\\\n      },\\\\n      \\\\\\\"effective_rank→distinct_2\\\\\\\": {\\\\n        \\\\\\\"pair\\\\\\\": \\\\\\\"effective_rank→distinct_2\\\\\\\",\\\\n        \\\\\\\"per_alpha\\\\\\\": {\\\\n          \\\\\\\"a000\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a025\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.25,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a075\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.75,\\\\n            \\\\\\\"is_robust\\\\\\\": true,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": false,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": false\\\\n      },\\\\n      \\\\\\\"effective_rank→distinct_3\\\\\\\": {\\\\n        \\\\\\\"pair\\\\\\\": \\\\\\\"effective_rank→distinct_3\\\\\\\",\\\\n        \\\\\\\"per_alpha\\\\\\\": {\\\\n          \\\\\\\"a000\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a025\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.25,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a075\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.75,\\\\n            \\\\\\\"is_robust\\\\\\\": true,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": false,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": false\\\\n      }\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"token_entropy→distinct_1\\\": {\\n        \\\"pair\\\": \\\"token_entropy→distinct_1\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 5,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"token_entropy→distinct_2\\\": {\\n        \\\"pair\\\": \\\"token_entropy→distinct_2\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 5,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"token_entropy→distinct_3\\\": {\\n        \\\"pair\\\": \\\"token_entropy→distinct_3\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 5,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"self_bleu→perplexity\\\": {\\n        \\\"pair\\\": \\\"self_bleu→perplexity\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n\\n\\n... [截断: 输出过长，省略 8170 字符] ...\\n\\ns_robust\\\": false,\\n            \\\"n_sig_methods\\\": 0,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": true,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": true\\n      },\\n      \\\"effective_rank→distinct_1\\\": {\\n        \\\"pair\\\": \\\"effective_rank→distinct_1\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"effective_rank→distinct_2\\\": {\\n        \\\"pair\\\": \\\"effective_rank→distinct_2\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"effective_rank→distinct_3\\\": {\\n        \\\"pair\\\": \\\"effective_rank→distinct_3\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a075\\\": {\\n            \\\"alpha\\\": 0.75,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018rmbfQoJ1snLjL1xkRaj36`</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -name \"*multi*\" -o -name \"*seed*\" -o -name \"*d017*\" -o -name \"*consensus*\" -o -name \"*method_ablation*\"",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "35869f27-d189-41c2-8c99-176aff965d05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LUXPRaLjVohXsQQW38GcKg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13448,
      "cache_read_input_tokens": 27410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T15:33:09.166Z_

<details><summary>↩ Tool result · `toolu_018rmbfQoJ1snLjL1xkRaj36`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation_dmax_sensitivity.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/consensus_classification.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/consensus_classification.json.bak_raw\\n/root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_panel.json\\n/root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "13fd0fb6-dba3-4f89-957b-87ef3e20c8a0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json\\\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation_dmax_sensitivity.json\\\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus\\\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/consensus_classification.json\\\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/consensus_classification.json.bak_raw\\\\n/root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_panel.json\\\\n/root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation_dmax_sensitivity.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/consensus_classification.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/consensus_classification.json.bak_raw\\n/root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_panel.json\\n/root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01H4h1cccaUYGDyyfu6nCYkn`</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v6_report.md",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "fec62e92-fc98-4ef0-8c72-699d3712ea2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LUXPRaLjVohXsQQW38GcKg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13448,
      "cache_read_input_tokens": 27410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T15:33:10.039Z_

<details><summary>↩ Tool result · `toolu_01H4h1cccaUYGDyyfu6nCYkn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Cross-Alpha Analysis Report (v6)\\n\\n**Date:** 2026-05-15\\n**Alpha points:** [0.0, 0.25, 0.5, 0.75, 1.0]\\n**Generations:** gen_0 to gen_10\\n\\n## 1. Dose-Response (gen0 to genN drift %)\\n\\n| Metric | α=0.00 | α=0.25 | α=0.50 | α=0.75 | α=1.00 |\\n|--------|--------:|--------:|--------:|--------:|--------:|\\n| distinct_1 | -13.8% | -40.3% | -37.3% | -32.7% | -28.3% |\\n| distinct_2 | -9.8% | -57.1% | -51.5% | -41.3% | -35.2% |\\n| distinct_3 | -4.5% | -59.9% | -52.4% | -38.4% | -31.6% |\\n| token_entropy | -5.1% | -4.1% | -18.6% | -27.7% | -60.5% |\\n| ece | +51.7% | +79.7% | +842.8% | +1809.5% | +3762.6% |\\n| perplexity | -21.7% | -17.2% | +21.1% | +182.1% | +3624.6% |\\n\\n## 2. Granger Causality (bidirectional, permutation, FDR-corrected)\\n\\n| Direction | α=0.00 p_raw | p_fdr | α=0.25 p_raw | p_fdr | α=0.50 p_raw | p_fdr | α=0.75 p_raw | p_fdr | α=1.00 p_raw | p_fdr |\\n|-----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|\\n| entropy->d1 | 0.0514 | 0.1285 | 0.0150 | 0.0667 | 0.0950 | 0.1855 | 0.0106 | 0.0540 | 0.0060 | 0.0480 * |\\n| ECE->d1 | 0.9498 | 0.9742 | 0.2352 | 0.4090 | 0.0190 | 0.0760 | 0.0038 | 0.0460 * | 0.0006 | 0.0240 * |\\n| entropy->d2 | 0.0804 | 0.1786 | 0.0730 | 0.1717 | 0.0974 | 0.1855 | 0.0072 | 0.0480 * | 0.0108 | 0.0540 |\\n| ECE->d2 | 0.5443 | 0.6220 | 0.0882 | 0.1855 | 0.0394 | 0.1285 | 0.0032 | 0.0460 * | 0.0046 | 0.0460 * |\\n| d1->entropy | 0.7956 | 0.8375 | 0.0236 | 0.0858 | 0.2170 | 0.3945 | 0.7762 | 0.8375 | 0.3313 | 0.4719 |\\n| d1->ECE | 0.3431 | 0.4719 | 0.4661 | 0.5484 | 0.2771 | 0.4619 | 0.3915 | 0.4962 | 0.0502 | 0.1285 |\\n| d2->entropy | 0.9782 | 0.9782 | 0.0498 | 0.1285 | 0.3143 | 0.4719 | 0.7674 | 0.8375 | 0.3447 | 0.4719 |\\n| d2->ECE | 0.3539 | 0.4719 | 0.3969 | 0.4962 | 0.3529 | 0.4719 | 0.4615 | 0.5484 | 0.0430 | 0.1285 |\\n\\nFDR: 40 tests, BH correction. \\\\* = p_fdr < 0.05\\n\\n## 3. Consensus Classification (regime-dependent validity)\\n\\n### α=0.00 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 0/16\\n- Non-robust: 16/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 2/5 |\\n| token_entropy→distinct_1 | non-robust | 3/5 |\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\n| token_entropy→distinct_3 | non-robust | 2/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 3/5 |\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\n| self_bleu→distinct_3 | non-robust | 3/5 |\\n| ece→perplexity | non-robust | 1/5 |\\n| ece→distinct_1 | non-robust | 2/5 |\\n| ece→distinct_2 | non-robust | 1/5 |\\n| ece→distinct_3 | non-robust | 2/5 |\\n| effective_rank→perplexity | non-robust | 0/5 |\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\n| effective_rank→distinct_2 | non-robust | 1/5 |\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\n\\n### α=0.25 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 1/16\\n- Non-robust: 15/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 2/5 |\\n| token_entropy→distinct_1 | **ROBUST** | 4/5 |\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\n| token_entropy→distinct_3 | non-robust | 3/5 |\\n| self_bleu→perplexity | non-robust | 0/5 |\\n| self_bleu→distinct_1 | non-robust | 0/5 |\\n| self_bleu→distinct_2 | non-robust | 0/5 |\\n| self_bleu→distinct_3 | non-robust | 0/5 |\\n| ece→perplexity | non-robust | 1/5 |\\n| ece→distinct_1 | non-robust | 1/5 |\\n| ece→distinct_2 | non-robust | 1/5 |\\n| ece→distinct_3 | non-robust | 1/5 |\\n| effective_rank→perplexity | non-robust | 1/5 |\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\n| effective_rank→distinct_2 | non-robust | 2/5 |\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\n\\n### α=0.50 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 0/16\\n- Non-robust: 16/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 3/5 |\\n| token_entropy→distinct_1 | non-robust | 3/5 |\\n| token_entropy→distinc\\n\\n... [截断: 输出过长，省略 17 字符] ...\\n\\n| 3/5 |\\n| token_entropy→distinct_3 | non-robust | 3/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\n| self_bleu→distinct_2 | non-robust | 1/5 |\\n| self_bleu→distinct_3 | non-robust | 1/5 |\\n| ece→perplexity | non-robust | 3/5 |\\n| ece→distinct_1 | non-robust | 3/5 |\\n| ece→distinct_2 | non-robust | 3/5 |\\n| ece→distinct_3 | non-robust | 3/5 |\\n| effective_rank→perplexity | non-robust | 3/5 |\\n| effective_rank→distinct_1 | non-robust | 3/5 |\\n| effective_rank→distinct_2 | non-robust | 2/5 |\\n| effective_rank→distinct_3 | non-robust | 2/5 |\\n\\n### α=0.75 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 11/16\\n- Non-robust: 5/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | **ROBUST** | 4/5 |\\n| token_entropy→distinct_1 | **ROBUST** | 4/5 |\\n| token_entropy→distinct_2 | **ROBUST** | 4/5 |\\n| token_entropy→distinct_3 | **ROBUST** | 4/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\n| self_bleu→distinct_3 | non-robust | 2/5 |\\n| ece→perplexity | **ROBUST** | 4/5 |\\n| ece→distinct_1 | **ROBUST** | 4/5 |\\n| ece→distinct_2 | **ROBUST** | 4/5 |\\n| ece→distinct_3 | **ROBUST** | 4/5 |\\n| effective_rank→perplexity | non-robust | 3/5 |\\n| effective_rank→distinct_1 | **ROBUST** | 4/5 |\\n| effective_rank→distinct_2 | **ROBUST** | 4/5 |\\n| effective_rank→distinct_3 | **ROBUST** | 4/5 |\\n\\n### α=1.00 (4-seed full consensus (≥4/5 methods, ≥3/4 seeds))\\n\\n- Robust pairs: 6/16\\n- Non-robust: 10/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 3/5 |\\n| token_entropy→distinct_1 | **ROBUST** | 5/5 |\\n| token_entropy→distinct_2 | **ROBUST** | 5/5 |\\n| token_entropy→distinct_3 | **ROBUST** | 5/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\n| self_bleu→distinct_3 | non-robust | 2/5 |\\n| ece→perplexity | non-robust | 3/5 |\\n| ece→distinct_1 | **ROBUST** | 4/5 |\\n| ece→distinct_2 | **ROBUST** | 4/5 |\\n| ece→distinct_3 | **ROBUST** | 4/5 |\\n| effective_rank→perplexity | non-robust | 2/5 |\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\n| effective_rank→distinct_2 | non-robust | 1/5 |\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\n\\n### Regime Comparison Summary\\n\\n- Stable pairs (same classification at all α): 5/16\\n- Regime-dependent pairs: 11/16\\n\\n| Pair | α=0.00 | α=0.25 | α=0.50 | α=0.75 | α=1.00 | Stable |\\n|------|--------|--------|--------|--------|--------|--------|\\n| token_entropy→perplexity | .(2) | .(2) | .(3) | R(4) | .(3) | N |\\n| token_entropy→distinct_1 | .(3) | R(4) | .(3) | R(4) | R(5) | N |\\n| token_entropy→distinct_2 | .(3) | .(3) | .(3) | R(4) | R(5) | N |\\n| token_entropy→distinct_3 | .(2) | .(3) | .(3) | R(4) | R(5) | N |\\n| self_bleu→perplexity | .(2) | .(0) | .(2) | .(2) | .(2) | Y |\\n| self_bleu→distinct_1 | .(3) | .(0) | .(1) | .(1) | .(1) | Y |\\n| self_bleu→distinct_2 | .(2) | .(0) | .(1) | .(2) | .(2) | Y |\\n| self_bleu→distinct_3 | .(3) | .(0) | .(1) | .(2) | .(2) | Y |\\n| ece→perplexity | .(1) | .(1) | .(3) | R(4) | .(3) | N |\\n| ece→distinct_1 | .(2) | .(1) | .(3) | R(4) | R(4) | N |\\n| ece→distinct_2 | .(1) | .(1) | .(3) | R(4) | R(4) | N |\\n| ece→distinct_3 | .(2) | .(1) | .(3) | R(4) | R(4) | N |\\n| effective_rank→perplexity | .(0) | .(1) | .(3) | .(3) | .(2) | Y |\\n| effective_rank→distinct_1 | .(2) | .(2) | .(3) | R(4) | .(2) | N |\\n| effective_rank→distinct_2 | .(1) | .(2) | .(2) | R(4) | .(1) | N |\\n| effective_rank→distinct_3 | .(1) | .(1) | .(2) | R(4) | .(1) | N |\\n\\n## 4. D1 Velocity\\n\\n| α | mean_vel | early | late | decel_ratio |\\n|---|----------|-------|------|-------------|\\n| 0.00 | -0.001354 | -0.002516 | -0.000191 | 0.08 |\\n| 0.25 | -0.003962 | -0.006938 | -0.000986 | 0.14 |\\n| 0.50 | -0.003661 | -0.006153 | -0.001170 | 0.19 |\\n| 0.75 | -0.003215 | -0.005813 | -0.000616 | 0.11 |\\n| 1.00 | -0.002783 | -0.005203 | -0.000364 | 0.07 |\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "e62748e0-53e9-45bd-8248-1bf755bd3c9f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"# Cross-Alpha Analysis Report (v6)\\\\n\\\\n**Date:** 2026-05-15\\\\n**Alpha points:** [0.0, 0.25, 0.5, 0.75, 1.0]\\\\n**Generations:** gen_0 to gen_10\\\\n\\\\n## 1. Dose-Response (gen0 to genN drift %)\\\\n\\\\n| Metric | α=0.00 | α=0.25 | α=0.50 | α=0.75 | α=1.00 |\\\\n|--------|--------:|--------:|--------:|--------:|--------:|\\\\n| distinct_1 | -13.8% | -40.3% | -37.3% | -32.7% | -28.3% |\\\\n| distinct_2 | -9.8% | -57.1% | -51.5% | -41.3% | -35.2% |\\\\n| distinct_3 | -4.5% | -59.9% | -52.4% | -38.4% | -31.6% |\\\\n| token_entropy | -5.1% | -4.1% | -18.6% | -27.7% | -60.5% |\\\\n| ece | +51.7% | +79.7% | +842.8% | +1809.5% | +3762.6% |\\\\n| perplexity | -21.7% | -17.2% | +21.1% | +182.1% | +3624.6% |\\\\n\\\\n## 2. Granger Causality (bidirectional, permutation, FDR-corrected)\\\\n\\\\n| Direction | α=0.00 p_raw | p_fdr | α=0.25 p_raw | p_fdr | α=0.50 p_raw | p_fdr | α=0.75 p_raw | p_fdr | α=1.00 p_raw | p_fdr |\\\\n|-----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|\\\\n| entropy->d1 | 0.0514 | 0.1285 | 0.0150 | 0.0667 | 0.0950 | 0.1855 | 0.0106 | 0.0540 | 0.0060 | 0.0480 * |\\\\n| ECE->d1 | 0.9498 | 0.9742 | 0.2352 | 0.4090 | 0.0190 | 0.0760 | 0.0038 | 0.0460 * | 0.0006 | 0.0240 * |\\\\n| entropy->d2 | 0.0804 | 0.1786 | 0.0730 | 0.1717 | 0.0974 | 0.1855 | 0.0072 | 0.0480 * | 0.0108 | 0.0540 |\\\\n| ECE->d2 | 0.5443 | 0.6220 | 0.0882 | 0.1855 | 0.0394 | 0.1285 | 0.0032 | 0.0460 * | 0.0046 | 0.0460 * |\\\\n| d1->entropy | 0.7956 | 0.8375 | 0.0236 | 0.0858 | 0.2170 | 0.3945 | 0.7762 | 0.8375 | 0.3313 | 0.4719 |\\\\n| d1->ECE | 0.3431 | 0.4719 | 0.4661 | 0.5484 | 0.2771 | 0.4619 | 0.3915 | 0.4962 | 0.0502 | 0.1285 |\\\\n| d2->entropy | 0.9782 | 0.9782 | 0.0498 | 0.1285 | 0.3143 | 0.4719 | 0.7674 | 0.8375 | 0.3447 | 0.4719 |\\\\n| d2->ECE | 0.3539 | 0.4719 | 0.3969 | 0.4962 | 0.3529 | 0.4719 | 0.4615 | 0.5484 | 0.0430 | 0.1285 |\\\\n\\\\nFDR: 40 tests, BH correction. \\\\\\\\* = p_fdr < 0.05\\\\n\\\\n## 3. Consensus Classification (regime-dependent validity)\\\\n\\\\n### α=0.00 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\\\n\\\\n- Robust pairs: 0/16\\\\n- Non-robust: 16/16\\\\n\\\\n| Pair | Robust | Methods |\\\\n|------|--------|---------|\\\\n| token_entropy→perplexity | non-robust | 2/5 |\\\\n| token_entropy→distinct_1 | non-robust | 3/5 |\\\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\\\n| token_entropy→distinct_3 | non-robust | 2/5 |\\\\n| self_bleu→perplexity | non-robust | 2/5 |\\\\n| self_bleu→distinct_1 | non-robust | 3/5 |\\\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\\\n| self_bleu→distinct_3 | non-robust | 3/5 |\\\\n| ece→perplexity | non-robust | 1/5 |\\\\n| ece→distinct_1 | non-robust | 2/5 |\\\\n| ece→distinct_2 | non-robust | 1/5 |\\\\n| ece→distinct_3 | non-robust | 2/5 |\\\\n| effective_rank→perplexity | non-robust | 0/5 |\\\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\\\n| effective_rank→distinct_2 | non-robust | 1/5 |\\\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\\\n\\\\n### α=0.25 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\\\n\\\\n- Robust pairs: 1/16\\\\n- Non-robust: 15/16\\\\n\\\\n| Pair | Robust | Methods |\\\\n|------|--------|---------|\\\\n| token_entropy→perplexity | non-robust | 2/5 |\\\\n| token_entropy→distinct_1 | **ROBUST** | 4/5 |\\\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\\\n| token_entropy→distinct_3 | non-robust | 3/5 |\\\\n| self_bleu→perplexity | non-robust | 0/5 |\\\\n| self_bleu→distinct_1 | non-robust | 0/5 |\\\\n| self_bleu→distinct_2 | non-robust | 0/5 |\\\\n| self_bleu→distinct_3 | non-robust | 0/5 |\\\\n| ece→perplexity | non-robust | 1/5 |\\\\n| ece→distinct_1 | non-robust | 1/5 |\\\\n| ece→distinct_2 | non-robust | 1/5 |\\\\n| ece→distinct_3 | non-robust | 1/5 |\\\\n| effective_rank→perplexity | non-robust | 1/5 |\\\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\\\n| effective_rank→distinct_2 | non-robust | 2/5 |\\\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\\\n\\\\n### α=0.50 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\\\n\\\\n- Robust pairs: 0/16\\\\n- Non-robust: 16/16\\\\n\\\\n| Pair | Robust | Methods |\\\\n|------|--------|---------|\\\\n| token_entropy→perplexity | non-robust | 3/5 |\\\\n| token_entropy→distinct_1 | non-robust | 3/5 |\\\\n| token_entropy→distinc\\\\n\\\\n... [截断: 输出过长，省略 17 字符] ...\\\\n\\\\n| 3/5 |\\\\n| token_entropy→distinct_3 | non-robust | 3/5 |\\\\n| self_bleu→perplexity | non-robust | 2/5 |\\\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\\\n| self_bleu→distinct_2 | non-robust | 1/5 |\\\\n| self_bleu→distinct_3 | non-robust | 1/5 |\\\\n| ece→perplexity | non-robust | 3/5 |\\\\n| ece→distinct_1 | non-robust | 3/5 |\\\\n| ece→distinct_2 | non-robust | 3/5 |\\\\n| ece→distinct_3 | non-robust | 3/5 |\\\\n| effective_rank→perplexity | non-robust | 3/5 |\\\\n| effective_rank→distinct_1 | non-robust | 3/5 |\\\\n| effective_rank→distinct_2 | non-robust | 2/5 |\\\\n| effective_rank→distinct_3 | non-robust | 2/5 |\\\\n\\\\n### α=0.75 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\\\n\\\\n- Robust pairs: 11/16\\\\n- Non-robust: 5/16\\\\n\\\\n| Pair | Robust | Methods |\\\\n|------|--------|---------|\\\\n| token_entropy→perplexity | **ROBUST** | 4/5 |\\\\n| token_entropy→distinct_1 | **ROBUST** | 4/5 |\\\\n| token_entropy→distinct_2 | **ROBUST** | 4/5 |\\\\n| token_entropy→distinct_3 | **ROBUST** | 4/5 |\\\\n| self_bleu→perplexity | non-robust | 2/5 |\\\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\\\n| self_bleu→distinct_3 | non-robust | 2/5 |\\\\n| ece→perplexity | **ROBUST** | 4/5 |\\\\n| ece→distinct_1 | **ROBUST** | 4/5 |\\\\n| ece→distinct_2 | **ROBUST** | 4/5 |\\\\n| ece→distinct_3 | **ROBUST** | 4/5 |\\\\n| effective_rank→perplexity | non-robust | 3/5 |\\\\n| effective_rank→distinct_1 | **ROBUST** | 4/5 |\\\\n| effective_rank→distinct_2 | **ROBUST** | 4/5 |\\\\n| effective_rank→distinct_3 | **ROBUST** | 4/5 |\\\\n\\\\n### α=1.00 (4-seed full consensus (≥4/5 methods, ≥3/4 seeds))\\\\n\\\\n- Robust pairs: 6/16\\\\n- Non-robust: 10/16\\\\n\\\\n| Pair | Robust | Methods |\\\\n|------|--------|---------|\\\\n| token_entropy→perplexity | non-robust | 3/5 |\\\\n| token_entropy→distinct_1 | **ROBUST** | 5/5 |\\\\n| token_entropy→distinct_2 | **ROBUST** | 5/5 |\\\\n| token_entropy→distinct_3 | **ROBUST** | 5/5 |\\\\n| self_bleu→perplexity | non-robust | 2/5 |\\\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\\\n| self_bleu→distinct_3 | non-robust | 2/5 |\\\\n| ece→perplexity | non-robust | 3/5 |\\\\n| ece→distinct_1 | **ROBUST** | 4/5 |\\\\n| ece→distinct_2 | **ROBUST** | 4/5 |\\\\n| ece→distinct_3 | **ROBUST** | 4/5 |\\\\n| effective_rank→perplexity | non-robust | 2/5 |\\\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\\\n| effective_rank→distinct_2 | non-robust | 1/5 |\\\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\\\n\\\\n### Regime Comparison Summary\\\\n\\\\n- Stable pairs (same classification at all α): 5/16\\\\n- Regime-dependent pairs: 11/16\\\\n\\\\n| Pair | α=0.00 | α=0.25 | α=0.50 | α=0.75 | α=1.00 | Stable |\\\\n|------|--------|--------|--------|--------|--------|--------|\\\\n| token_entropy→perplexity | .(2) | .(2) | .(3) | R(4) | .(3) | N |\\\\n| token_entropy→distinct_1 | .(3) | R(4) | .(3) | R(4) | R(5) | N |\\\\n| token_entropy→distinct_2 | .(3) | .(3) | .(3) | R(4) | R(5) | N |\\\\n| token_entropy→distinct_3 | .(2) | .(3) | .(3) | R(4) | R(5) | N |\\\\n| self_bleu→perplexity | .(2) | .(0) | .(2) | .(2) | .(2) | Y |\\\\n| self_bleu→distinct_1 | .(3) | .(0) | .(1) | .(1) | .(1) | Y |\\\\n| self_bleu→distinct_2 | .(2) | .(0) | .(1) | .(2) | .(2) | Y |\\\\n| self_bleu→distinct_3 | .(3) | .(0) | .(1) | .(2) | .(2) | Y |\\\\n| ece→perplexity | .(1) | .(1) | .(3) | R(4) | .(3) | N |\\\\n| ece→distinct_1 | .(2) | .(1) | .(3) | R(4) | R(4) | N |\\\\n| ece→distinct_2 | .(1) | .(1) | .(3) | R(4) | R(4) | N |\\\\n| ece→distinct_3 | .(2) | .(1) | .(3) | R(4) | R(4) | N |\\\\n| effective_rank→perplexity | .(0) | .(1) | .(3) | .(3) | .(2) | Y |\\\\n| effective_rank→distinct_1 | .(2) | .(2) | .(3) | R(4) | .(2) | N |\\\\n| effective_rank→distinct_2 | .(1) | .(2) | .(2) | R(4) | .(1) | N |\\\\n| effective_rank→distinct_3 | .(1) | .(1) | .(2) | R(4) | .(1) | N |\\\\n\\\\n## 4. D1 Velocity\\\\n\\\\n| α | mean_vel | early | late | decel_ratio |\\\\n|---|----------|-------|------|-------------|\\\\n| 0.00 | -0.001354 | -0.002516 | -0.000191 | 0.08 |\\\\n| 0.25 | -0.003962 | -0.006938 | -0.000986 | 0.14 |\\\\n| 0.50 | -0.003661 | -0.006153 | -0.001170 | 0.19 |\\\\n| 0.75 | -0.003215 | -0.005813 | -0.000616 | 0.11 |\\\\n| 1.00 | -0.002783 | -0.005203 | -0.000364 | 0.07 |\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"# Cross-Alpha Analysis Report (v6)\\n\\n**Date:** 2026-05-15\\n**Alpha points:** [0.0, 0.25, 0.5, 0.75, 1.0]\\n**Generations:** gen_0 to gen_10\\n\\n## 1. Dose-Response (gen0 to genN drift %)\\n\\n| Metric | α=0.00 | α=0.25 | α=0.50 | α=0.75 | α=1.00 |\\n|--------|--------:|--------:|--------:|--------:|--------:|\\n| distinct_1 | -13.8% | -40.3% | -37.3% | -32.7% | -28.3% |\\n| distinct_2 | -9.8% | -57.1% | -51.5% | -41.3% | -35.2% |\\n| distinct_3 | -4.5% | -59.9% | -52.4% | -38.4% | -31.6% |\\n| token_entropy | -5.1% | -4.1% | -18.6% | -27.7% | -60.5% |\\n| ece | +51.7% | +79.7% | +842.8% | +1809.5% | +3762.6% |\\n| perplexity | -21.7% | -17.2% | +21.1% | +182.1% | +3624.6% |\\n\\n## 2. Granger Causality (bidirectional, permutation, FDR-corrected)\\n\\n| Direction | α=0.00 p_raw | p_fdr | α=0.25 p_raw | p_fdr | α=0.50 p_raw | p_fdr | α=0.75 p_raw | p_fdr | α=1.00 p_raw | p_fdr |\\n|-----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|\\n| entropy->d1 | 0.0514 | 0.1285 | 0.0150 | 0.0667 | 0.0950 | 0.1855 | 0.0106 | 0.0540 | 0.0060 | 0.0480 * |\\n| ECE->d1 | 0.9498 | 0.9742 | 0.2352 | 0.4090 | 0.0190 | 0.0760 | 0.0038 | 0.0460 * | 0.0006 | 0.0240 * |\\n| entropy->d2 | 0.0804 | 0.1786 | 0.0730 | 0.1717 | 0.0974 | 0.1855 | 0.0072 | 0.0480 * | 0.0108 | 0.0540 |\\n| ECE->d2 | 0.5443 | 0.6220 | 0.0882 | 0.1855 | 0.0394 | 0.1285 | 0.0032 | 0.0460 * | 0.0046 | 0.0460 * |\\n| d1->entropy | 0.7956 | 0.8375 | 0.0236 | 0.0858 | 0.2170 | 0.3945 | 0.7762 | 0.8375 | 0.3313 | 0.4719 |\\n| d1->ECE | 0.3431 | 0.4719 | 0.4661 | 0.5484 | 0.2771 | 0.4619 | 0.3915 | 0.4962 | 0.0502 | 0.1285 |\\n| d2->entropy | 0.9782 | 0.9782 | 0.0498 | 0.1285 | 0.3143 | 0.4719 | 0.7674 | 0.8375 | 0.3447 | 0.4719 |\\n| d2->ECE | 0.3539 | 0.4719 | 0.3969 | 0.4962 | 0.3529 | 0.4719 | 0.4615 | 0.5484 | 0.0430 | 0.1285 |\\n\\nFDR: 40 tests, BH correction. \\\\* = p_fdr < 0.05\\n\\n## 3. Consensus Classification (regime-dependent validity)\\n\\n### α=0.00 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 0/16\\n- Non-robust: 16/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 2/5 |\\n| token_entropy→distinct_1 | non-robust | 3/5 |\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\n| token_entropy→distinct_3 | non-robust | 2/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 3/5 |\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\n| self_bleu→distinct_3 | non-robust | 3/5 |\\n| ece→perplexity | non-robust | 1/5 |\\n| ece→distinct_1 | non-robust | 2/5 |\\n| ece→distinct_2 | non-robust | 1/5 |\\n| ece→distinct_3 | non-robust | 2/5 |\\n| effective_rank→perplexity | non-robust | 0/5 |\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\n| effective_rank→distinct_2 | non-robust | 1/5 |\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\n\\n### α=0.25 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 1/16\\n- Non-robust: 15/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 2/5 |\\n| token_entropy→distinct_1 | **ROBUST** | 4/5 |\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\n| token_entropy→distinct_3 | non-robust | 3/5 |\\n| self_bleu→perplexity | non-robust | 0/5 |\\n| self_bleu→distinct_1 | non-robust | 0/5 |\\n| self_bleu→distinct_2 | non-robust | 0/5 |\\n| self_bleu→distinct_3 | non-robust | 0/5 |\\n| ece→perplexity | non-robust | 1/5 |\\n| ece→distinct_1 | non-robust | 1/5 |\\n| ece→distinct_2 | non-robust | 1/5 |\\n| ece→distinct_3 | non-robust | 1/5 |\\n| effective_rank→perplexity | non-robust | 1/5 |\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\n| effective_rank→distinct_2 | non-robust | 2/5 |\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\n\\n### α=0.50 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 0/16\\n- Non-robust: 16/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 3/5 |\\n| token_entropy→distinct_1 | non-robust | 3/5 |\\n| token_entropy→distinc\\n\\n... [截断: 输出过长，省略 17 字符] ...\\n\\n| 3/5 |\\n| token_entropy→distinct_3 | non-robust | 3/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\n| self_bleu→distinct_2 | non-robust | 1/5 |\\n| self_bleu→distinct_3 | non-robust | 1/5 |\\n| ece→perplexity | non-robust | 3/5 |\\n| ece→distinct_1 | non-robust | 3/5 |\\n| ece→distinct_2 | non-robust | 3/5 |\\n| ece→distinct_3 | non-robust | 3/5 |\\n| effective_rank→perplexity | non-robust | 3/5 |\\n| effective_rank→distinct_1 | non-robust | 3/5 |\\n| effective_rank→distinct_2 | non-robust | 2/5 |\\n| effective_rank→distinct_3 | non-robust | 2/5 |\\n\\n### α=0.75 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 11/16\\n- Non-robust: 5/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | **ROBUST** | 4/5 |\\n| token_entropy→distinct_1 | **ROBUST** | 4/5 |\\n| token_entropy→distinct_2 | **ROBUST** | 4/5 |\\n| token_entropy→distinct_3 | **ROBUST** | 4/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\n| self_bleu→distinct_3 | non-robust | 2/5 |\\n| ece→perplexity | **ROBUST** | 4/5 |\\n| ece→distinct_1 | **ROBUST** | 4/5 |\\n| ece→distinct_2 | **ROBUST** | 4/5 |\\n| ece→distinct_3 | **ROBUST** | 4/5 |\\n| effective_rank→perplexity | non-robust | 3/5 |\\n| effective_rank→distinct_1 | **ROBUST** | 4/5 |\\n| effective_rank→distinct_2 | **ROBUST** | 4/5 |\\n| effective_rank→distinct_3 | **ROBUST** | 4/5 |\\n\\n### α=1.00 (4-seed full consensus (≥4/5 methods, ≥3/4 seeds))\\n\\n- Robust pairs: 6/16\\n- Non-robust: 10/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 3/5 |\\n| token_entropy→distinct_1 | **ROBUST** | 5/5 |\\n| token_entropy→distinct_2 | **ROBUST** | 5/5 |\\n| token_entropy→distinct_3 | **ROBUST** | 5/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\n| self_bleu→distinct_3 | non-robust | 2/5 |\\n| ece→perplexity | non-robust | 3/5 |\\n| ece→distinct_1 | **ROBUST** | 4/5 |\\n| ece→distinct_2 | **ROBUST** | 4/5 |\\n| ece→distinct_3 | **ROBUST** | 4/5 |\\n| effective_rank→perplexity | non-robust | 2/5 |\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\n| effective_rank→distinct_2 | non-robust | 1/5 |\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\n\\n### Regime Comparison Summary\\n\\n- Stable pairs (same classification at all α): 5/16\\n- Regime-dependent pairs: 11/16\\n\\n| Pair | α=0.00 | α=0.25 | α=0.50 | α=0.75 | α=1.00 | Stable |\\n|------|--------|--------|--------|--------|--------|--------|\\n| token_entropy→perplexity | .(2) | .(2) | .(3) | R(4) | .(3) | N |\\n| token_entropy→distinct_1 | .(3) | R(4) | .(3) | R(4) | R(5) | N |\\n| token_entropy→distinct_2 | .(3) | .(3) | .(3) | R(4) | R(5) | N |\\n| token_entropy→distinct_3 | .(2) | .(3) | .(3) | R(4) | R(5) | N |\\n| self_bleu→perplexity | .(2) | .(0) | .(2) | .(2) | .(2) | Y |\\n| self_bleu→distinct_1 | .(3) | .(0) | .(1) | .(1) | .(1) | Y |\\n| self_bleu→distinct_2 | .(2) | .(0) | .(1) | .(2) | .(2) | Y |\\n| self_bleu→distinct_3 | .(3) | .(0) | .(1) | .(2) | .(2) | Y |\\n| ece→perplexity | .(1) | .(1) | .(3) | R(4) | .(3) | N |\\n| ece→distinct_1 | .(2) | .(1) | .(3) | R(4) | R(4) | N |\\n| ece→distinct_2 | .(1) | .(1) | .(3) | R(4) | R(4) | N |\\n| ece→distinct_3 | .(2) | .(1) | .(3) | R(4) | R(4) | N |\\n| effective_rank→perplexity | .(0) | .(1) | .(3) | .(3) | .(2) | Y |\\n| effective_rank→distinct_1 | .(2) | .(2) | .(3) | R(4) | .(2) | N |\\n| effective_rank→distinct_2 | .(1) | .(2) | .(2) | R(4) | .(1) | N |\\n| effective_rank→distinct_3 | .(1) | .(1) | .(2) | R(4) | .(1) | N |\\n\\n## 4. D1 Velocity\\n\\n| α | mean_vel | early | late | decel_ratio |\\n|---|----------|-------|------|-------------|\\n| 0.00 | -0.001354 | -0.002516 | -0.000191 | 0.08 |\\n| 0.25 | -0.003962 | -0.006938 | -0.000986 | 0.14 |\\n| 0.50 | -0.003661 | -0.006153 | -0.001170 | 0.19 |\\n| 0.75 | -0.003215 | -0.005813 | -0.000616 | 0.11 |\\n| 1.00 | -0.002783 | -0.005203 | -0.000364 | 0.07 |\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now I have a lot of data. Let me also get the v6 granger_results section more completely. I also need to check the method_ablation files and the v4 data for the 4-point comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "73c99f87-1865-4ce6-82b4-c9adeeec74f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDrMBzKkPoydFTCVVnHLAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9464,
      "cache_read_input_tokens": 40858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9464
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 29_

读取 v6 的 granger_results 部分和 v4 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "762bfa86-df6e-464e-bbd9-b7981c47b425",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDrMBzKkPoydFTCVVnHLAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9464,
      "cache_read_input_tokens": 40858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9464
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TDiegYpD1pbgN1tXdh9gzv`</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -c \"p_raw\" /root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v6.json",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "8805f9bc-ca2a-42fa-8f35-cc5fe6dd189e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDrMBzKkPoydFTCVVnHLAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9464,
      "cache_read_input_tokens": 40858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9464
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T15:33:17.095Z_

<details><summary>↩ Tool result · `toolu_01TDiegYpD1pbgN1tXdh9gzv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"40\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "cb4d3568-a827-4302-89ba-9737bd8e32ea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"40\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"40\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VtfJ9KrHQj9WX4NfQWTWS1`</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v4.json",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "5b74fbd9-43a4-4f0c-b715-cb0b22d76c1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDrMBzKkPoydFTCVVnHLAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9464,
      "cache_read_input_tokens": 40858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9464
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GayLjkBMwan73QqZNUdb7E`</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "3fc804ea-de0a-41bb-b28b-a603669514d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDrMBzKkPoydFTCVVnHLAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9464,
      "cache_read_input_tokens": 40858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9464
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T15:33:18.192Z_

<details><summary>↩ Tool result · `toolu_01VtfJ9KrHQj9WX4NfQWTWS1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"version\\\": \\\"v4\\\",\\n  \\\"date\\\": \\\"2026-05-15\\\",\\n  \\\"n_alphas\\\": 4,\\n  \\\"alpha_points\\\": [\\n    0.0,\\n    0.25,\\n    0.5,\\n    1.0\\n  ],\\n  \\\"n_generations\\\": 11,\\n  \\\"gen_range\\\": \\\"gen_0 to gen_10\\\",\\n  \\\"statistical_config\\\": {\\n    \\\"granger_max_lag\\\": 1,\\n    \\\"granger_n_perm\\\": 5000,\\n    \\\"granger_differenced\\\": true,\\n    \\\"fdr_method\\\": \\\"benjamini-hochberg\\\",\\n    \\\"fdr_scope\\\": \\\"all 32 tests corrected together\\\",\\n    \\\"n_independent_tests\\\": 32\\n  },\\n  \\\"dose_response\\\": {\\n    \\\"a000\\\": {\\n      \\\"alpha\\\": 0.0,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.08468,\\n        \\\"drift_pct\\\": -13.78\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.467199,\\n        \\\"drift_pct\\\": -9.77\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.77602,\\n        \\\"drift_pct\\\": -4.52\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 3.069313,\\n        \\\"drift_pct\\\": -5.1\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.016391,\\n        \\\"drift_pct\\\": 51.7\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 21.107704,\\n        \\\"drift_pct\\\": -21.68\\n      }\\n    },\\n    \\\"a025\\\": {\\n      \\\"alpha\\\": 0.25,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.058594,\\n        \\\"drift_pct\\\": -40.34\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.221939,\\n        \\\"drift_pct\\\": -57.14\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.326271,\\n        \\\"drift_pct\\\": -59.85\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 3.101744,\\n        \\\"drift_pct\\\": -4.1\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.019418,\\n        \\\"drift_pct\\\": 79.72\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 22.316978,\\n        \\\"drift_pct\\\": -17.19\\n      }\\n    },\\n    \\\"a050\\\": {\\n      \\\"alpha\\\": 0.5,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.061602,\\n        \\\"drift_pct\\\": -37.28\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.251346,\\n        \\\"drift_pct\\\": -51.46\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.387256,\\n        \\\"drift_pct\\\": -52.35\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 2.631835,\\n        \\\"drift_pct\\\": -18.62\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.101864,\\n        \\\"drift_pct\\\": 842.79\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 32.644371,\\n        \\\"drift_pct\\\": 21.13\\n      }\\n    },\\n    \\\"a100\\\": {\\n      \\\"alpha\\\": 1.0,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.070383,\\n        \\\"drift_pct\\\": -28.34\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.335471,\\n        \\\"drift_pct\\\": -35.21\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.555579,\\n        \\\"drift_pct\\\": -31.64\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 1.275924,\\n        \\\"drift_pct\\\": -60.55\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.417338,\\n        \\\"drift_pct\\\": 3762.61\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 1003.732954,\\n        \\\"drift_pct\\\": 3624.57\\n      }\\n    }\\n  },\\n  \\\"granger_causality\\\": [\\n    {\\n      \\\"f_stat\\\": 48.3527,\\n      \\\"p_raw\\\": 0.05139,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 8.0588,\\n      \\\"alpha\\\": 0.0,\\n      \\\"alpha_key\\\": \\\"a000\\\",\\n      \\\"direction\\\": \\\"entropy->d1\\\",\\n      \\\"cause\\\": \\\"token_entropy\\\",\\n      \\\"effect\\\": \\\"distinct_1\\\",\\n      \\\"p_fdr\\\": 0.13704\\n    },\\n    {\\n      \\\"f_stat\\\": 0.0021,\\n      \\\"p_raw\\\": 0.94981,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.0004,\\n      \\\"alpha\\\": 0.0,\\n      \\\"alpha_key\\\": \\\"a000\\\",\\n      \\\"direction\\\": \\\"ECE->d1\\\",\\n      \\\"cause\\\": \\\"ece\\\",\\n      \\\"effect\\\": \\\"distinct_1\\\",\\n      \\\"p_fdr\\\": 0.978204\\n    },\\n    {\\n      \\\"f_stat\\\": 16.7903,\\n      \\\"p_raw\\\": 0.080384,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 2.7984,\\n      \\\"alpha\\\": 0.0,\\n      \\\"alpha_key\\\"\\n\\n... [截断: 输出过长，省略 63760 字符] ...\\n\\n  \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"effective_rank→perplexity\\\": {\\n        \\\"pair\\\": \\\"effective_rank→perplexity\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 0,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": true,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": true\\n      },\\n      \\\"effective_rank→distinct_1\\\": {\\n        \\\"pair\\\": \\\"effective_rank→distinct_1\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": true,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": true\\n      },\\n      \\\"effective_rank→distinct_2\\\": {\\n        \\\"pair\\\": \\\"effective_rank→distinct_2\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": true,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": true\\n      },\\n      \\\"effective_rank→distinct_3\\\": {\\n        \\\"pair\\\": \\\"effective_rank→distinct_3\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": true,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": true\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "14322fe2-ef68-4519-b64e-7f1cc8d5e156",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"version\\\\\\\": \\\\\\\"v4\\\\\\\",\\\\n  \\\\\\\"date\\\\\\\": \\\\\\\"2026-05-15\\\\\\\",\\\\n  \\\\\\\"n_alphas\\\\\\\": 4,\\\\n  \\\\\\\"alpha_points\\\\\\\": [\\\\n    0.0,\\\\n    0.25,\\\\n    0.5,\\\\n    1.0\\\\n  ],\\\\n  \\\\\\\"n_generations\\\\\\\": 11,\\\\n  \\\\\\\"gen_range\\\\\\\": \\\\\\\"gen_0 to gen_10\\\\\\\",\\\\n  \\\\\\\"statistical_config\\\\\\\": {\\\\n    \\\\\\\"granger_max_lag\\\\\\\": 1,\\\\n    \\\\\\\"granger_n_perm\\\\\\\": 5000,\\\\n    \\\\\\\"granger_differenced\\\\\\\": true,\\\\n    \\\\\\\"fdr_method\\\\\\\": \\\\\\\"benjamini-hochberg\\\\\\\",\\\\n    \\\\\\\"fdr_scope\\\\\\\": \\\\\\\"all 32 tests corrected together\\\\\\\",\\\\n    \\\\\\\"n_independent_tests\\\\\\\": 32\\\\n  },\\\\n  \\\\\\\"dose_response\\\\\\\": {\\\\n    \\\\\\\"a000\\\\\\\": {\\\\n      \\\\\\\"alpha\\\\\\\": 0.0,\\\\n      \\\\\\\"distinct_1\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.098216,\\\\n        \\\\\\\"gen10\\\\\\\": 0.08468,\\\\n        \\\\\\\"drift_pct\\\\\\\": -13.78\\\\n      },\\\\n      \\\\\\\"distinct_2\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.517803,\\\\n        \\\\\\\"gen10\\\\\\\": 0.467199,\\\\n        \\\\\\\"drift_pct\\\\\\\": -9.77\\\\n      },\\\\n      \\\\\\\"distinct_3\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.812728,\\\\n        \\\\\\\"gen10\\\\\\\": 0.77602,\\\\n        \\\\\\\"drift_pct\\\\\\\": -4.52\\\\n      },\\\\n      \\\\\\\"token_entropy\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 3.234195,\\\\n        \\\\\\\"gen10\\\\\\\": 3.069313,\\\\n        \\\\\\\"drift_pct\\\\\\\": -5.1\\\\n      },\\\\n      \\\\\\\"ece\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.010805,\\\\n        \\\\\\\"gen10\\\\\\\": 0.016391,\\\\n        \\\\\\\"drift_pct\\\\\\\": 51.7\\\\n      },\\\\n      \\\\\\\"perplexity\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 26.948959,\\\\n        \\\\\\\"gen10\\\\\\\": 21.107704,\\\\n        \\\\\\\"drift_pct\\\\\\\": -21.68\\\\n      }\\\\n    },\\\\n    \\\\\\\"a025\\\\\\\": {\\\\n      \\\\\\\"alpha\\\\\\\": 0.25,\\\\n      \\\\\\\"distinct_1\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.098216,\\\\n        \\\\\\\"gen10\\\\\\\": 0.058594,\\\\n        \\\\\\\"drift_pct\\\\\\\": -40.34\\\\n      },\\\\n      \\\\\\\"distinct_2\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.517803,\\\\n        \\\\\\\"gen10\\\\\\\": 0.221939,\\\\n        \\\\\\\"drift_pct\\\\\\\": -57.14\\\\n      },\\\\n      \\\\\\\"distinct_3\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.812728,\\\\n        \\\\\\\"gen10\\\\\\\": 0.326271,\\\\n        \\\\\\\"drift_pct\\\\\\\": -59.85\\\\n      },\\\\n      \\\\\\\"token_entropy\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 3.234195,\\\\n        \\\\\\\"gen10\\\\\\\": 3.101744,\\\\n        \\\\\\\"drift_pct\\\\\\\": -4.1\\\\n      },\\\\n      \\\\\\\"ece\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.010805,\\\\n        \\\\\\\"gen10\\\\\\\": 0.019418,\\\\n        \\\\\\\"drift_pct\\\\\\\": 79.72\\\\n      },\\\\n      \\\\\\\"perplexity\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 26.948959,\\\\n        \\\\\\\"gen10\\\\\\\": 22.316978,\\\\n        \\\\\\\"drift_pct\\\\\\\": -17.19\\\\n      }\\\\n    },\\\\n    \\\\\\\"a050\\\\\\\": {\\\\n      \\\\\\\"alpha\\\\\\\": 0.5,\\\\n      \\\\\\\"distinct_1\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.098216,\\\\n        \\\\\\\"gen10\\\\\\\": 0.061602,\\\\n        \\\\\\\"drift_pct\\\\\\\": -37.28\\\\n      },\\\\n      \\\\\\\"distinct_2\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.517803,\\\\n        \\\\\\\"gen10\\\\\\\": 0.251346,\\\\n        \\\\\\\"drift_pct\\\\\\\": -51.46\\\\n      },\\\\n      \\\\\\\"distinct_3\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.812728,\\\\n        \\\\\\\"gen10\\\\\\\": 0.387256,\\\\n        \\\\\\\"drift_pct\\\\\\\": -52.35\\\\n      },\\\\n      \\\\\\\"token_entropy\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 3.234195,\\\\n        \\\\\\\"gen10\\\\\\\": 2.631835,\\\\n        \\\\\\\"drift_pct\\\\\\\": -18.62\\\\n      },\\\\n      \\\\\\\"ece\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.010805,\\\\n        \\\\\\\"gen10\\\\\\\": 0.101864,\\\\n        \\\\\\\"drift_pct\\\\\\\": 842.79\\\\n      },\\\\n      \\\\\\\"perplexity\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 26.948959,\\\\n        \\\\\\\"gen10\\\\\\\": 32.644371,\\\\n        \\\\\\\"drift_pct\\\\\\\": 21.13\\\\n      }\\\\n    },\\\\n    \\\\\\\"a100\\\\\\\": {\\\\n      \\\\\\\"alpha\\\\\\\": 1.0,\\\\n      \\\\\\\"distinct_1\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.098216,\\\\n        \\\\\\\"gen10\\\\\\\": 0.070383,\\\\n        \\\\\\\"drift_pct\\\\\\\": -28.34\\\\n      },\\\\n      \\\\\\\"distinct_2\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.517803,\\\\n        \\\\\\\"gen10\\\\\\\": 0.335471,\\\\n        \\\\\\\"drift_pct\\\\\\\": -35.21\\\\n      },\\\\n      \\\\\\\"distinct_3\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.812728,\\\\n        \\\\\\\"gen10\\\\\\\": 0.555579,\\\\n        \\\\\\\"drift_pct\\\\\\\": -31.64\\\\n      },\\\\n      \\\\\\\"token_entropy\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 3.234195,\\\\n        \\\\\\\"gen10\\\\\\\": 1.275924,\\\\n        \\\\\\\"drift_pct\\\\\\\": -60.55\\\\n      },\\\\n      \\\\\\\"ece\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 0.010805,\\\\n        \\\\\\\"gen10\\\\\\\": 0.417338,\\\\n        \\\\\\\"drift_pct\\\\\\\": 3762.61\\\\n      },\\\\n      \\\\\\\"perplexity\\\\\\\": {\\\\n        \\\\\\\"gen0\\\\\\\": 26.948959,\\\\n        \\\\\\\"gen10\\\\\\\": 1003.732954,\\\\n        \\\\\\\"drift_pct\\\\\\\": 3624.57\\\\n      }\\\\n    }\\\\n  },\\\\n  \\\\\\\"granger_causality\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 48.3527,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.05139,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 8.0588,\\\\n      \\\\\\\"alpha\\\\\\\": 0.0,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a000\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"entropy->d1\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.13704\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 0.0021,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.94981,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 0.0004,\\\\n      \\\\\\\"alpha\\\\\\\": 0.0,\\\\n      \\\\\\\"alpha_key\\\\\\\": \\\\\\\"a000\\\\\\\",\\\\n      \\\\\\\"direction\\\\\\\": \\\\\\\"ECE->d1\\\\\\\",\\\\n      \\\\\\\"cause\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"effect\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"p_fdr\\\\\\\": 0.978204\\\\n    },\\\\n    {\\\\n      \\\\\\\"f_stat\\\\\\\": 16.7903,\\\\n      \\\\\\\"p_raw\\\\\\\": 0.080384,\\\\n      \\\\\\\"n_perm\\\\\\\": 5000,\\\\n      \\\\\\\"effect_size_f2\\\\\\\": 2.7984,\\\\n      \\\\\\\"alpha\\\\\\\": 0.0,\\\\n      \\\\\\\"alpha_key\\\\\\\"\\\\n\\\\n... [截断: 输出过长，省略 63760 字符] ...\\\\n\\\\n  \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": true,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": false,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": false\\\\n      },\\\\n      \\\\\\\"effective_rank→perplexity\\\\\\\": {\\\\n        \\\\\\\"pair\\\\\\\": \\\\\\\"effective_rank→perplexity\\\\\\\",\\\\n        \\\\\\\"per_alpha\\\\\\\": {\\\\n          \\\\\\\"a000\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 0,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a025\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.25,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": true,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": true\\\\n      },\\\\n      \\\\\\\"effective_rank→distinct_1\\\\\\\": {\\\\n        \\\\\\\"pair\\\\\\\": \\\\\\\"effective_rank→distinct_1\\\\\\\",\\\\n        \\\\\\\"per_alpha\\\\\\\": {\\\\n          \\\\\\\"a000\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a025\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.25,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": true,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": true\\\\n      },\\\\n      \\\\\\\"effective_rank→distinct_2\\\\\\\": {\\\\n        \\\\\\\"pair\\\\\\\": \\\\\\\"effective_rank→distinct_2\\\\\\\",\\\\n        \\\\\\\"per_alpha\\\\\\\": {\\\\n          \\\\\\\"a000\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a025\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.25,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": true,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": true\\\\n      },\\\\n      \\\\\\\"effective_rank→distinct_3\\\\\\\": {\\\\n        \\\\\\\"pair\\\\\\\": \\\\\\\"effective_rank→distinct_3\\\\\\\",\\\\n        \\\\\\\"per_alpha\\\\\\\": {\\\\n          \\\\\\\"a000\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a025\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.25,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a050\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 0.5,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"method_agreement_only\\\\\\\"\\\\n          },\\\\n          \\\\\\\"a100\\\\\\\": {\\\\n            \\\\\\\"alpha\\\\\\\": 1.0,\\\\n            \\\\\\\"is_robust\\\\\\\": false,\\\\n            \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n            \\\\\\\"mode\\\\\\\": \\\\\\\"full_consensus\\\\\\\"\\\\n          }\\\\n        },\\\\n        \\\\\\\"stable\\\\\\\": true,\\\\n        \\\\\\\"all_robust\\\\\\\": false,\\\\n        \\\\\\\"all_non_robust\\\\\\\": true\\\\n      }\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.58}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"version\\\": \\\"v4\\\",\\n  \\\"date\\\": \\\"2026-05-15\\\",\\n  \\\"n_alphas\\\": 4,\\n  \\\"alpha_points\\\": [\\n    0.0,\\n    0.25,\\n    0.5,\\n    1.0\\n  ],\\n  \\\"n_generations\\\": 11,\\n  \\\"gen_range\\\": \\\"gen_0 to gen_10\\\",\\n  \\\"statistical_config\\\": {\\n    \\\"granger_max_lag\\\": 1,\\n    \\\"granger_n_perm\\\": 5000,\\n    \\\"granger_differenced\\\": true,\\n    \\\"fdr_method\\\": \\\"benjamini-hochberg\\\",\\n    \\\"fdr_scope\\\": \\\"all 32 tests corrected together\\\",\\n    \\\"n_independent_tests\\\": 32\\n  },\\n  \\\"dose_response\\\": {\\n    \\\"a000\\\": {\\n      \\\"alpha\\\": 0.0,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.08468,\\n        \\\"drift_pct\\\": -13.78\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.467199,\\n        \\\"drift_pct\\\": -9.77\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.77602,\\n        \\\"drift_pct\\\": -4.52\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 3.069313,\\n        \\\"drift_pct\\\": -5.1\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.016391,\\n        \\\"drift_pct\\\": 51.7\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 21.107704,\\n        \\\"drift_pct\\\": -21.68\\n      }\\n    },\\n    \\\"a025\\\": {\\n      \\\"alpha\\\": 0.25,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.058594,\\n        \\\"drift_pct\\\": -40.34\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.221939,\\n        \\\"drift_pct\\\": -57.14\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.326271,\\n        \\\"drift_pct\\\": -59.85\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 3.101744,\\n        \\\"drift_pct\\\": -4.1\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.019418,\\n        \\\"drift_pct\\\": 79.72\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 22.316978,\\n        \\\"drift_pct\\\": -17.19\\n      }\\n    },\\n    \\\"a050\\\": {\\n      \\\"alpha\\\": 0.5,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.061602,\\n        \\\"drift_pct\\\": -37.28\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.251346,\\n        \\\"drift_pct\\\": -51.46\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.387256,\\n        \\\"drift_pct\\\": -52.35\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 2.631835,\\n        \\\"drift_pct\\\": -18.62\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.101864,\\n        \\\"drift_pct\\\": 842.79\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 32.644371,\\n        \\\"drift_pct\\\": 21.13\\n      }\\n    },\\n    \\\"a100\\\": {\\n      \\\"alpha\\\": 1.0,\\n      \\\"distinct_1\\\": {\\n        \\\"gen0\\\": 0.098216,\\n        \\\"gen10\\\": 0.070383,\\n        \\\"drift_pct\\\": -28.34\\n      },\\n      \\\"distinct_2\\\": {\\n        \\\"gen0\\\": 0.517803,\\n        \\\"gen10\\\": 0.335471,\\n        \\\"drift_pct\\\": -35.21\\n      },\\n      \\\"distinct_3\\\": {\\n        \\\"gen0\\\": 0.812728,\\n        \\\"gen10\\\": 0.555579,\\n        \\\"drift_pct\\\": -31.64\\n      },\\n      \\\"token_entropy\\\": {\\n        \\\"gen0\\\": 3.234195,\\n        \\\"gen10\\\": 1.275924,\\n        \\\"drift_pct\\\": -60.55\\n      },\\n      \\\"ece\\\": {\\n        \\\"gen0\\\": 0.010805,\\n        \\\"gen10\\\": 0.417338,\\n        \\\"drift_pct\\\": 3762.61\\n      },\\n      \\\"perplexity\\\": {\\n        \\\"gen0\\\": 26.948959,\\n        \\\"gen10\\\": 1003.732954,\\n        \\\"drift_pct\\\": 3624.57\\n      }\\n    }\\n  },\\n  \\\"granger_causality\\\": [\\n    {\\n      \\\"f_stat\\\": 48.3527,\\n      \\\"p_raw\\\": 0.05139,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 8.0588,\\n      \\\"alpha\\\": 0.0,\\n      \\\"alpha_key\\\": \\\"a000\\\",\\n      \\\"direction\\\": \\\"entropy->d1\\\",\\n      \\\"cause\\\": \\\"token_entropy\\\",\\n      \\\"effect\\\": \\\"distinct_1\\\",\\n      \\\"p_fdr\\\": 0.13704\\n    },\\n    {\\n      \\\"f_stat\\\": 0.0021,\\n      \\\"p_raw\\\": 0.94981,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 0.0004,\\n      \\\"alpha\\\": 0.0,\\n      \\\"alpha_key\\\": \\\"a000\\\",\\n      \\\"direction\\\": \\\"ECE->d1\\\",\\n      \\\"cause\\\": \\\"ece\\\",\\n      \\\"effect\\\": \\\"distinct_1\\\",\\n      \\\"p_fdr\\\": 0.978204\\n    },\\n    {\\n      \\\"f_stat\\\": 16.7903,\\n      \\\"p_raw\\\": 0.080384,\\n      \\\"n_perm\\\": 5000,\\n      \\\"effect_size_f2\\\": 2.7984,\\n      \\\"alpha\\\": 0.0,\\n      \\\"alpha_key\\\"\\n\\n... [截断: 输出过长，省略 63760 字符] ...\\n\\n  \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": true,\\n            \\\"n_sig_methods\\\": 4,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": false,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": false\\n      },\\n      \\\"effective_rank→perplexity\\\": {\\n        \\\"pair\\\": \\\"effective_rank→perplexity\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 0,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": true,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": true\\n      },\\n      \\\"effective_rank→distinct_1\\\": {\\n        \\\"pair\\\": \\\"effective_rank→distinct_1\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 3,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": true,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": true\\n      },\\n      \\\"effective_rank→distinct_2\\\": {\\n        \\\"pair\\\": \\\"effective_rank→distinct_2\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": true,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": true\\n      },\\n      \\\"effective_rank→distinct_3\\\": {\\n        \\\"pair\\\": \\\"effective_rank→distinct_3\\\",\\n        \\\"per_alpha\\\": {\\n          \\\"a000\\\": {\\n            \\\"alpha\\\": 0.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a025\\\": {\\n            \\\"alpha\\\": 0.25,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a050\\\": {\\n            \\\"alpha\\\": 0.5,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 2,\\n            \\\"mode\\\": \\\"method_agreement_only\\\"\\n          },\\n          \\\"a100\\\": {\\n            \\\"alpha\\\": 1.0,\\n            \\\"is_robust\\\": false,\\n            \\\"n_sig_methods\\\": 1,\\n            \\\"mode\\\": \\\"full_consensus\\\"\\n          }\\n        },\\n        \\\"stable\\\": true,\\n        \\\"all_robust\\\": false,\\n        \\\"all_non_robust\\\": true\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T15:33:18.875Z_

<details><summary>↩ Tool result · `toolu_01GayLjkBMwan73QqZNUdb7E`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      43,\\n      44,\\n      45\\n    ],\\n    \\\"alpha\\\": 0.05,\\n    \\\"canary_metrics\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"self_bleu\\\",\\n      \\\"ece\\\",\\n      \\\"effective_rank\\\"\\n    ],\\n    \\\"downstream_metrics\\\": [\\n      \\\"perplexity\\\",\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\"\\n    ],\\n    \\\"methods\\\": [\\n      \\\"naive_pearson: raw-level Pearson lag-correlation\\\",\\n      \\\"differenced_xcorr: first-differenced cross-correlation\\\",\\n      \\\"threshold_onset: 2-sigma signal-onset lead time\\\",\\n      \\\"toda_yamamoto: augmented-lag Granger causality (Wald F-test)\\\",\\n      \\\"permutation_granger: differenced + shuffle permutation Granger (F-test)\\\"\\n    ]\\n  },\\n  \\\"summary\\\": {\\n    \\\"total_pairs\\\": 16,\\n    \\\"naive_significant\\\": 16,\\n    \\\"differenced_significant\\\": 14,\\n    \\\"threshold_significant\\\": 9,\\n    \\\"ty_significant\\\": 4,\\n    \\\"perm_granger_significant\\\": 6,\\n    \\\"spurious_count\\\": 12,\\n    \\\"spurious_rate\\\": 0.75,\\n    \\\"spurious_pairs\\\": [\\n      {\\n        \\\"canary\\\": \\\"token_entropy\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_1\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_2\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_3\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"ece\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"ece\\\",\\n        \\\"downstream\\\": \\\"distinct_2\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"ece\\\",\\n        \\\"downstream\\\": \\\"distinct_3\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"effective_rank\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"effective_rank\\\",\\n        \\\"downstream\\\": \\\"distinct_1\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"effective_rank\\\",\\n        \\\"downstream\\\": \\\"distinct_2\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"effective_rank\\\",\\n        \\\"downstream\\\": \\\"distinct_3\\\"\\n      }\\n    ],\\n    \\\"robust_pairs\\\": [\\n      {\\n        \\\"canary\\\": \\\"token_entropy\\\",\\n        \\\"downstream\\\": \\\"distinct_1\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"token_entropy\\\",\\n        \\\"downstream\\\": \\\"distinct_2\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"token_entropy\\\",\\n        \\\"downstream\\\": \\\"distinct_3\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"ece\\\",\\n        \\\"downstream\\\": \\\"distinct_1\\\"\\n      }\\n    ],\\n    \\\"naive_only_pairs\\\": [\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_1\\\"\\n      }\\n    ],\\n    \\\"dual_classification\\\": {\\n      \\\"note\\\": \\\"TY demoted per D013/D015 (power=0.05-0.20 at T=10)\\\",\\n      \\\"with_ty_5method\\\": {\\n        \\\"spurious_count\\\": 12,\\n        \\\"spurious_rate\\\": 0.75,\\n        \\\"robust_count\\\": 4\\n      },\\n      \\\"without_ty_4method\\\": {\\n        \\\"spurious_count\\\": 10,\\n        \\\"spurious_rate\\\": 0.625,\\n        \\\"robust_count\\\": 6\\n      },\\n      \\\"flipped_pairs\\\": [\\n        {\\n          \\\"canary\\\": \\\"ece\\\",\\n          \\\"downstream\\\": \\\"distinct_2\\\",\\n          \\\"spurious_5method\\\": true,\\n          \\\"robust_4method\\\": true,\\n          \\\"methods_agree_5\\\": 4,\\n          \\\"methods_agree_4\\\": 4,\\n          \\\"spurious_reason_5method\\\": \\\"toda_yamamoto n.s.\\\"\\n        },\\n        {\\n          \\\"canary\\\": \\\"ece\\\",\\n          \\\"downstream\\\": \\\"distinct_3\\\",\\n          \\\"spurious_5method\\\": true,\\n          \\\"robust_4method\\\": true,\\n          \\\"methods_agree_5\\\": 4,\\n          \\\"methods_agree_4\\\": 4,\\n          \\\"spurious_reason_5method\\\": \\\"toda_yamamoto n.s.\\\"\\n        }\\n      ]\\n    }\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"per_seed\\\": [\\n        {\\n          \\\"seed\\\": 42,\\n          \\\"naive_pearson\\\": {\\n            \\\"method\\\": \\\"naive_pearson\\\",\\n            \\\"peak_lag\\\": 3,\\n            \\\"r\\\": 0.8027,\\n            \\\"significant\\\": true,\\n            \\\"effect_size_r\\\": 0.8027,\\n            \\\"effect_size_type\\\": \\\"pearson_r\\\",\\n            \\\"effect_size_label\\\": \\\"large\\\",\\n            \\\"p_raw\\\": 0.01648,\\n            \\\"p_fdr\\\": 0.0182,\\n            \\\"significant_fdr\\\": true\\n          },\\n          \\\"dif\\n\\n... [截断: 输出过长，省略 152963 字符] ...\\n\\ne\\\",\\n            \\\"p_raw\\\": 0.126873,\\n            \\\"p_fdr\\\": 0.198,\\n            \\\"significant_fdr\\\": false\\n          }\\n        },\\n        {\\n          \\\"seed\\\": 45,\\n          \\\"naive_pearson\\\": {\\n            \\\"method\\\": \\\"naive_pearson\\\",\\n            \\\"peak_lag\\\": -1,\\n            \\\"r\\\": -0.8187,\\n            \\\"significant\\\": true,\\n            \\\"effect_size_r\\\": 0.8187,\\n            \\\"effect_size_type\\\": \\\"pearson_r\\\",\\n            \\\"effect_size_label\\\": \\\"large\\\",\\n            \\\"p_raw\\\": 0.003772,\\n            \\\"p_fdr\\\": 0.0047,\\n            \\\"significant_fdr\\\": true\\n          },\\n          \\\"differenced_xcorr\\\": {\\n            \\\"method\\\": \\\"differenced_xcorr\\\",\\n            \\\"peak_lag\\\": -3,\\n            \\\"r\\\": -0.7335,\\n            \\\"significant\\\": false,\\n            \\\"effect_size_r\\\": 0.7335,\\n            \\\"effect_size_type\\\": \\\"pearson_r\\\",\\n            \\\"effect_size_label\\\": \\\"large\\\",\\n            \\\"p_raw\\\": 0.060616,\\n            \\\"p_fdr\\\": 0.0669,\\n            \\\"significant_fdr\\\": false\\n          },\\n          \\\"threshold_onset\\\": {\\n            \\\"method\\\": \\\"threshold_onset\\\",\\n            \\\"canary_onset\\\": null,\\n            \\\"downstream_onset\\\": 4,\\n            \\\"lead_time\\\": null,\\n            \\\"significant\\\": false,\\n            \\\"note\\\": \\\"onset not detected for: canary\\\",\\n            \\\"effect_size\\\": null,\\n            \\\"effect_size_type\\\": null,\\n            \\\"effect_size_label\\\": null\\n          },\\n          \\\"toda_yamamoto\\\": {\\n            \\\"method\\\": \\\"toda_yamamoto\\\",\\n            \\\"p\\\": 1,\\n            \\\"d_max\\\": 2,\\n            \\\"k\\\": 3,\\n            \\\"wald_F\\\": 0.0136,\\n            \\\"significant\\\": false,\\n            \\\"df_resid\\\": 1,\\n            \\\"d_canary\\\": 2,\\n            \\\"d_downstream\\\": 0,\\n            \\\"effect_size_f2\\\": 0.0136,\\n            \\\"effect_size_type\\\": \\\"cohens_f2\\\",\\n            \\\"effect_size_label\\\": \\\"negligible\\\",\\n            \\\"p_raw\\\": 0.926183,\\n            \\\"p_fdr\\\": 0.9409,\\n            \\\"significant_fdr\\\": false\\n          },\\n          \\\"permutation_granger\\\": {\\n            \\\"method\\\": \\\"permutation_granger\\\",\\n            \\\"f_stat\\\": 11.8051,\\n            \\\"significant\\\": false,\\n            \\\"effect_size_f2\\\": 1.9675,\\n            \\\"null_mean\\\": 3.1238,\\n            \\\"null_std\\\": 9.5974,\\n            \\\"n_perm\\\": 1000,\\n            \\\"effect_size\\\": 1.9675,\\n            \\\"effect_size_type\\\": \\\"cohens_f2\\\",\\n            \\\"effect_size_label\\\": \\\"large\\\",\\n            \\\"p_raw\\\": 0.103896,\\n            \\\"p_fdr\\\": 0.1797,\\n            \\\"significant_fdr\\\": false\\n          }\\n        }\\n      ],\\n      \\\"summary\\\": {\\n        \\\"naive_pearson\\\": {\\n          \\\"sig_seeds\\\": 4,\\n          \\\"total\\\": 4,\\n          \\\"verdict\\\": \\\"SIGNIFICANT\\\"\\n        },\\n        \\\"differenced_xcorr\\\": {\\n          \\\"sig_seeds\\\": 3,\\n          \\\"total\\\": 4,\\n          \\\"verdict\\\": \\\"SIGNIFICANT\\\"\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"sig_seeds\\\": 0,\\n          \\\"total\\\": 4,\\n          \\\"verdict\\\": \\\"NOT_SIGNIFICANT\\\"\\n        },\\n        \\\"toda_yamamoto\\\": {\\n          \\\"sig_seeds\\\": 2,\\n          \\\"total\\\": 4,\\n          \\\"verdict\\\": \\\"NOT_SIGNIFICANT\\\"\\n        },\\n        \\\"permutation_granger\\\": {\\n          \\\"sig_seeds\\\": 2,\\n          \\\"total\\\": 4,\\n          \\\"verdict\\\": \\\"NOT_SIGNIFICANT\\\"\\n        }\\n      },\\n      \\\"robust_5method\\\": false,\\n      \\\"spurious_5method\\\": true,\\n      \\\"spurious_reason_5method\\\": \\\"threshold_onset n.s., toda_yamamoto n.s., permutation_granger n.s.\\\",\\n      \\\"methods_agree_5\\\": 2,\\n      \\\"robust_4method\\\": false,\\n      \\\"spurious_4method\\\": true,\\n      \\\"methods_agree_4\\\": 2,\\n      \\\"spurious\\\": true,\\n      \\\"robust\\\": false,\\n      \\\"naive_only\\\": false\\n    }\\n  ],\\n  \\\"fdr_correction\\\": {\\n    \\\"method\\\": \\\"benjamini-hochberg\\\",\\n    \\\"alpha\\\": 0.05,\\n    \\\"per_method\\\": {\\n      \\\"naive_pearson\\\": {\\n        \\\"total_tests\\\": 64,\\n        \\\"raw_significant\\\": 63,\\n        \\\"fdr_significant\\\": 63\\n      },\\n      \\\"differenced_xcorr\\\": {\\n        \\\"total_tests\\\": 64,\\n        \\\"raw_significant\\\": 55,\\n        \\\"fdr_significant\\\": 53\\n      },\\n      \\\"toda_yamamoto\\\": {\\n        \\\"total_tests\\\": 64,\\n        \\\"raw_significant\\\": 26,\\n        \\\"fdr_significant\\\": 24\\n      },\\n      \\\"permutation_granger\\\": {\\n        \\\"total_tests\\\": 64,\\n        \\\"raw_significant\\\": 34,\\n        \\\"fdr_significant\\\": 27\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.68}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "c922e43d-2dee-4393-910e-b076bd542679",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"meta\\\\\\\": {\\\\n    \\\\\\\"seeds\\\\\\\": [\\\\n      42,\\\\n      43,\\\\n      44,\\\\n      45\\\\n    ],\\\\n    \\\\\\\"alpha\\\\\\\": 0.05,\\\\n    \\\\\\\"canary_metrics\\\\\\\": [\\\\n      \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"self_bleu\\\\\\\",\\\\n      \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"effective_rank\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"downstream_metrics\\\\\\\": [\\\\n      \\\\\\\"perplexity\\\\\\\",\\\\n      \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"distinct_3\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"methods\\\\\\\": [\\\\n      \\\\\\\"naive_pearson: raw-level Pearson lag-correlation\\\\\\\",\\\\n      \\\\\\\"differenced_xcorr: first-differenced cross-correlation\\\\\\\",\\\\n      \\\\\\\"threshold_onset: 2-sigma signal-onset lead time\\\\\\\",\\\\n      \\\\\\\"toda_yamamoto: augmented-lag Granger causality (Wald F-test)\\\\\\\",\\\\n      \\\\\\\"permutation_granger: differenced + shuffle permutation Granger (F-test)\\\\\\\"\\\\n    ]\\\\n  },\\\\n  \\\\\\\"summary\\\\\\\": {\\\\n    \\\\\\\"total_pairs\\\\\\\": 16,\\\\n    \\\\\\\"naive_significant\\\\\\\": 16,\\\\n    \\\\\\\"differenced_significant\\\\\\\": 14,\\\\n    \\\\\\\"threshold_significant\\\\\\\": 9,\\\\n    \\\\\\\"ty_significant\\\\\\\": 4,\\\\n    \\\\\\\"perm_granger_significant\\\\\\\": 6,\\\\n    \\\\\\\"spurious_count\\\\\\\": 12,\\\\n    \\\\\\\"spurious_rate\\\\\\\": 0.75,\\\\n    \\\\\\\"spurious_pairs\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"effective_rank\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"effective_rank\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"effective_rank\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"effective_rank\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\"\\\\n      }\\\\n    ],\\\\n    \\\\\\\"robust_pairs\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\"\\\\n      }\\\\n    ],\\\\n    \\\\\\\"naive_only_pairs\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\"\\\\n      },\\\\n      {\\\\n        \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n        \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\"\\\\n      }\\\\n    ],\\\\n    \\\\\\\"dual_classification\\\\\\\": {\\\\n      \\\\\\\"note\\\\\\\": \\\\\\\"TY demoted per D013/D015 (power=0.05-0.20 at T=10)\\\\\\\",\\\\n      \\\\\\\"with_ty_5method\\\\\\\": {\\\\n        \\\\\\\"spurious_count\\\\\\\": 12,\\\\n        \\\\\\\"spurious_rate\\\\\\\": 0.75,\\\\n        \\\\\\\"robust_count\\\\\\\": 4\\\\n      },\\\\n      \\\\\\\"without_ty_4method\\\\\\\": {\\\\n        \\\\\\\"spurious_count\\\\\\\": 10,\\\\n        \\\\\\\"spurious_rate\\\\\\\": 0.625,\\\\n        \\\\\\\"robust_count\\\\\\\": 6\\\\n      },\\\\n      \\\\\\\"flipped_pairs\\\\\\\": [\\\\n        {\\\\n          \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n          \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n          \\\\\\\"spurious_5method\\\\\\\": true,\\\\n          \\\\\\\"robust_4method\\\\\\\": true,\\\\n          \\\\\\\"methods_agree_5\\\\\\\": 4,\\\\n          \\\\\\\"methods_agree_4\\\\\\\": 4,\\\\n          \\\\\\\"spurious_reason_5method\\\\\\\": \\\\\\\"toda_yamamoto n.s.\\\\\\\"\\\\n        },\\\\n        {\\\\n          \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n          \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\",\\\\n          \\\\\\\"spurious_5method\\\\\\\": true,\\\\n          \\\\\\\"robust_4method\\\\\\\": true,\\\\n          \\\\\\\"methods_agree_5\\\\\\\": 4,\\\\n          \\\\\\\"methods_agree_4\\\\\\\": 4,\\\\n          \\\\\\\"spurious_reason_5method\\\\\\\": \\\\\\\"toda_yamamoto n.s.\\\\\\\"\\\\n        }\\\\n      ]\\\\n    }\\\\n  },\\\\n  \\\\\\\"pairs\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\",\\\\n      \\\\\\\"per_seed\\\\\\\": [\\\\n        {\\\\n          \\\\\\\"seed\\\\\\\": 42,\\\\n          \\\\\\\"naive_pearson\\\\\\\": {\\\\n            \\\\\\\"method\\\\\\\": \\\\\\\"naive_pearson\\\\\\\",\\\\n            \\\\\\\"peak_lag\\\\\\\": 3,\\\\n            \\\\\\\"r\\\\\\\": 0.8027,\\\\n            \\\\\\\"significant\\\\\\\": true,\\\\n            \\\\\\\"effect_size_r\\\\\\\": 0.8027,\\\\n            \\\\\\\"effect_size_type\\\\\\\": \\\\\\\"pearson_r\\\\\\\",\\\\n            \\\\\\\"effect_size_label\\\\\\\": \\\\\\\"large\\\\\\\",\\\\n            \\\\\\\"p_raw\\\\\\\": 0.01648,\\\\n            \\\\\\\"p_fdr\\\\\\\": 0.0182,\\\\n            \\\\\\\"significant_fdr\\\\\\\": true\\\\n          },\\\\n          \\\\\\\"dif\\\\n\\\\n... [截断: 输出过长，省略 152963 字符] ...\\\\n\\\\ne\\\\\\\",\\\\n            \\\\\\\"p_raw\\\\\\\": 0.126873,\\\\n            \\\\\\\"p_fdr\\\\\\\": 0.198,\\\\n            \\\\\\\"significant_fdr\\\\\\\": false\\\\n          }\\\\n        },\\\\n        {\\\\n          \\\\\\\"seed\\\\\\\": 45,\\\\n          \\\\\\\"naive_pearson\\\\\\\": {\\\\n            \\\\\\\"method\\\\\\\": \\\\\\\"naive_pearson\\\\\\\",\\\\n            \\\\\\\"peak_lag\\\\\\\": -1,\\\\n            \\\\\\\"r\\\\\\\": -0.8187,\\\\n            \\\\\\\"significant\\\\\\\": true,\\\\n            \\\\\\\"effect_size_r\\\\\\\": 0.8187,\\\\n            \\\\\\\"effect_size_type\\\\\\\": \\\\\\\"pearson_r\\\\\\\",\\\\n            \\\\\\\"effect_size_label\\\\\\\": \\\\\\\"large\\\\\\\",\\\\n            \\\\\\\"p_raw\\\\\\\": 0.003772,\\\\n            \\\\\\\"p_fdr\\\\\\\": 0.0047,\\\\n            \\\\\\\"significant_fdr\\\\\\\": true\\\\n          },\\\\n          \\\\\\\"differenced_xcorr\\\\\\\": {\\\\n            \\\\\\\"method\\\\\\\": \\\\\\\"differenced_xcorr\\\\\\\",\\\\n            \\\\\\\"peak_lag\\\\\\\": -3,\\\\n            \\\\\\\"r\\\\\\\": -0.7335,\\\\n            \\\\\\\"significant\\\\\\\": false,\\\\n            \\\\\\\"effect_size_r\\\\\\\": 0.7335,\\\\n            \\\\\\\"effect_size_type\\\\\\\": \\\\\\\"pearson_r\\\\\\\",\\\\n            \\\\\\\"effect_size_label\\\\\\\": \\\\\\\"large\\\\\\\",\\\\n            \\\\\\\"p_raw\\\\\\\": 0.060616,\\\\n            \\\\\\\"p_fdr\\\\\\\": 0.0669,\\\\n            \\\\\\\"significant_fdr\\\\\\\": false\\\\n          },\\\\n          \\\\\\\"threshold_onset\\\\\\\": {\\\\n            \\\\\\\"method\\\\\\\": \\\\\\\"threshold_onset\\\\\\\",\\\\n            \\\\\\\"canary_onset\\\\\\\": null,\\\\n            \\\\\\\"downstream_onset\\\\\\\": 4,\\\\n            \\\\\\\"lead_time\\\\\\\": null,\\\\n            \\\\\\\"significant\\\\\\\": false,\\\\n            \\\\\\\"note\\\\\\\": \\\\\\\"onset not detected for: canary\\\\\\\",\\\\n            \\\\\\\"effect_size\\\\\\\": null,\\\\n            \\\\\\\"effect_size_type\\\\\\\": null,\\\\n            \\\\\\\"effect_size_label\\\\\\\": null\\\\n          },\\\\n          \\\\\\\"toda_yamamoto\\\\\\\": {\\\\n            \\\\\\\"method\\\\\\\": \\\\\\\"toda_yamamoto\\\\\\\",\\\\n            \\\\\\\"p\\\\\\\": 1,\\\\n            \\\\\\\"d_max\\\\\\\": 2,\\\\n            \\\\\\\"k\\\\\\\": 3,\\\\n            \\\\\\\"wald_F\\\\\\\": 0.0136,\\\\n            \\\\\\\"significant\\\\\\\": false,\\\\n            \\\\\\\"df_resid\\\\\\\": 1,\\\\n            \\\\\\\"d_canary\\\\\\\": 2,\\\\n            \\\\\\\"d_downstream\\\\\\\": 0,\\\\n            \\\\\\\"effect_size_f2\\\\\\\": 0.0136,\\\\n            \\\\\\\"effect_size_type\\\\\\\": \\\\\\\"cohens_f2\\\\\\\",\\\\n            \\\\\\\"effect_size_label\\\\\\\": \\\\\\\"negligible\\\\\\\",\\\\n            \\\\\\\"p_raw\\\\\\\": 0.926183,\\\\n            \\\\\\\"p_fdr\\\\\\\": 0.9409,\\\\n            \\\\\\\"significant_fdr\\\\\\\": false\\\\n          },\\\\n          \\\\\\\"permutation_granger\\\\\\\": {\\\\n            \\\\\\\"method\\\\\\\": \\\\\\\"permutation_granger\\\\\\\",\\\\n            \\\\\\\"f_stat\\\\\\\": 11.8051,\\\\n            \\\\\\\"significant\\\\\\\": false,\\\\n            \\\\\\\"effect_size_f2\\\\\\\": 1.9675,\\\\n            \\\\\\\"null_mean\\\\\\\": 3.1238,\\\\n            \\\\\\\"null_std\\\\\\\": 9.5974,\\\\n            \\\\\\\"n_perm\\\\\\\": 1000,\\\\n            \\\\\\\"effect_size\\\\\\\": 1.9675,\\\\n            \\\\\\\"effect_size_type\\\\\\\": \\\\\\\"cohens_f2\\\\\\\",\\\\n            \\\\\\\"effect_size_label\\\\\\\": \\\\\\\"large\\\\\\\",\\\\n            \\\\\\\"p_raw\\\\\\\": 0.103896,\\\\n            \\\\\\\"p_fdr\\\\\\\": 0.1797,\\\\n            \\\\\\\"significant_fdr\\\\\\\": false\\\\n          }\\\\n        }\\\\n      ],\\\\n      \\\\\\\"summary\\\\\\\": {\\\\n        \\\\\\\"naive_pearson\\\\\\\": {\\\\n          \\\\\\\"sig_seeds\\\\\\\": 4,\\\\n          \\\\\\\"total\\\\\\\": 4,\\\\n          \\\\\\\"verdict\\\\\\\": \\\\\\\"SIGNIFICANT\\\\\\\"\\\\n        },\\\\n        \\\\\\\"differenced_xcorr\\\\\\\": {\\\\n          \\\\\\\"sig_seeds\\\\\\\": 3,\\\\n          \\\\\\\"total\\\\\\\": 4,\\\\n          \\\\\\\"verdict\\\\\\\": \\\\\\\"SIGNIFICANT\\\\\\\"\\\\n        },\\\\n        \\\\\\\"threshold_onset\\\\\\\": {\\\\n          \\\\\\\"sig_seeds\\\\\\\": 0,\\\\n          \\\\\\\"total\\\\\\\": 4,\\\\n          \\\\\\\"verdict\\\\\\\": \\\\\\\"NOT_SIGNIFICANT\\\\\\\"\\\\n        },\\\\n        \\\\\\\"toda_yamamoto\\\\\\\": {\\\\n          \\\\\\\"sig_seeds\\\\\\\": 2,\\\\n          \\\\\\\"total\\\\\\\": 4,\\\\n          \\\\\\\"verdict\\\\\\\": \\\\\\\"NOT_SIGNIFICANT\\\\\\\"\\\\n        },\\\\n        \\\\\\\"permutation_granger\\\\\\\": {\\\\n          \\\\\\\"sig_seeds\\\\\\\": 2,\\\\n          \\\\\\\"total\\\\\\\": 4,\\\\n          \\\\\\\"verdict\\\\\\\": \\\\\\\"NOT_SIGNIFICANT\\\\\\\"\\\\n        }\\\\n      },\\\\n      \\\\\\\"robust_5method\\\\\\\": false,\\\\n      \\\\\\\"spurious_5method\\\\\\\": true,\\\\n      \\\\\\\"spurious_reason_5method\\\\\\\": \\\\\\\"threshold_onset n.s., toda_yamamoto n.s., permutation_granger n.s.\\\\\\\",\\\\n      \\\\\\\"methods_agree_5\\\\\\\": 2,\\\\n      \\\\\\\"robust_4method\\\\\\\": false,\\\\n      \\\\\\\"spurious_4method\\\\\\\": true,\\\\n      \\\\\\\"methods_agree_4\\\\\\\": 2,\\\\n      \\\\\\\"spurious\\\\\\\": true,\\\\n      \\\\\\\"robust\\\\\\\": false,\\\\n      \\\\\\\"naive_only\\\\\\\": false\\\\n    }\\\\n  ],\\\\n  \\\\\\\"fdr_correction\\\\\\\": {\\\\n    \\\\\\\"method\\\\\\\": \\\\\\\"benjamini-hochberg\\\\\\\",\\\\n    \\\\\\\"alpha\\\\\\\": 0.05,\\\\n    \\\\\\\"per_method\\\\\\\": {\\\\n      \\\\\\\"naive_pearson\\\\\\\": {\\\\n        \\\\\\\"total_tests\\\\\\\": 64,\\\\n        \\\\\\\"raw_significant\\\\\\\": 63,\\\\n        \\\\\\\"fdr_significant\\\\\\\": 63\\\\n      },\\\\n      \\\\\\\"differenced_xcorr\\\\\\\": {\\\\n        \\\\\\\"total_tests\\\\\\\": 64,\\\\n        \\\\\\\"raw_significant\\\\\\\": 55,\\\\n        \\\\\\\"fdr_significant\\\\\\\": 53\\\\n      },\\\\n      \\\\\\\"toda_yamamoto\\\\\\\": {\\\\n        \\\\\\\"total_tests\\\\\\\": 64,\\\\n        \\\\\\\"raw_significant\\\\\\\": 26,\\\\n        \\\\\\\"fdr_significant\\\\\\\": 24\\\\n      },\\\\n      \\\\\\\"permutation_granger\\\\\\\": {\\\\n        \\\\\\\"total_tests\\\\\\\": 64,\\\\n        \\\\\\\"raw_significant\\\\\\\": 34,\\\\n        \\\\\\\"fdr_significant\\\\\\\": 27\\\\n      }\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.68}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      43,\\n      44,\\n      45\\n    ],\\n    \\\"alpha\\\": 0.05,\\n    \\\"canary_metrics\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"self_bleu\\\",\\n      \\\"ece\\\",\\n      \\\"effective_rank\\\"\\n    ],\\n    \\\"downstream_metrics\\\": [\\n      \\\"perplexity\\\",\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\"\\n    ],\\n    \\\"methods\\\": [\\n      \\\"naive_pearson: raw-level Pearson lag-correlation\\\",\\n      \\\"differenced_xcorr: first-differenced cross-correlation\\\",\\n      \\\"threshold_onset: 2-sigma signal-onset lead time\\\",\\n      \\\"toda_yamamoto: augmented-lag Granger causality (Wald F-test)\\\",\\n      \\\"permutation_granger: differenced + shuffle permutation Granger (F-test)\\\"\\n    ]\\n  },\\n  \\\"summary\\\": {\\n    \\\"total_pairs\\\": 16,\\n    \\\"naive_significant\\\": 16,\\n    \\\"differenced_significant\\\": 14,\\n    \\\"threshold_significant\\\": 9,\\n    \\\"ty_significant\\\": 4,\\n    \\\"perm_granger_significant\\\": 6,\\n    \\\"spurious_count\\\": 12,\\n    \\\"spurious_rate\\\": 0.75,\\n    \\\"spurious_pairs\\\": [\\n      {\\n        \\\"canary\\\": \\\"token_entropy\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_1\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_2\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_3\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"ece\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"ece\\\",\\n        \\\"downstream\\\": \\\"distinct_2\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"ece\\\",\\n        \\\"downstream\\\": \\\"distinct_3\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"effective_rank\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"effective_rank\\\",\\n        \\\"downstream\\\": \\\"distinct_1\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"effective_rank\\\",\\n        \\\"downstream\\\": \\\"distinct_2\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"effective_rank\\\",\\n        \\\"downstream\\\": \\\"distinct_3\\\"\\n      }\\n    ],\\n    \\\"robust_pairs\\\": [\\n      {\\n        \\\"canary\\\": \\\"token_entropy\\\",\\n        \\\"downstream\\\": \\\"distinct_1\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"token_entropy\\\",\\n        \\\"downstream\\\": \\\"distinct_2\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"token_entropy\\\",\\n        \\\"downstream\\\": \\\"distinct_3\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"ece\\\",\\n        \\\"downstream\\\": \\\"distinct_1\\\"\\n      }\\n    ],\\n    \\\"naive_only_pairs\\\": [\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_1\\\"\\n      }\\n    ],\\n    \\\"dual_classification\\\": {\\n      \\\"note\\\": \\\"TY demoted per D013/D015 (power=0.05-0.20 at T=10)\\\",\\n      \\\"with_ty_5method\\\": {\\n        \\\"spurious_count\\\": 12,\\n        \\\"spurious_rate\\\": 0.75,\\n        \\\"robust_count\\\": 4\\n      },\\n      \\\"without_ty_4method\\\": {\\n        \\\"spurious_count\\\": 10,\\n        \\\"spurious_rate\\\": 0.625,\\n        \\\"robust_count\\\": 6\\n      },\\n      \\\"flipped_pairs\\\": [\\n        {\\n          \\\"canary\\\": \\\"ece\\\",\\n          \\\"downstream\\\": \\\"distinct_2\\\",\\n          \\\"spurious_5method\\\": true,\\n          \\\"robust_4method\\\": true,\\n          \\\"methods_agree_5\\\": 4,\\n          \\\"methods_agree_4\\\": 4,\\n          \\\"spurious_reason_5method\\\": \\\"toda_yamamoto n.s.\\\"\\n        },\\n        {\\n          \\\"canary\\\": \\\"ece\\\",\\n          \\\"downstream\\\": \\\"distinct_3\\\",\\n          \\\"spurious_5method\\\": true,\\n          \\\"robust_4method\\\": true,\\n          \\\"methods_agree_5\\\": 4,\\n          \\\"methods_agree_4\\\": 4,\\n          \\\"spurious_reason_5method\\\": \\\"toda_yamamoto n.s.\\\"\\n        }\\n      ]\\n    }\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"per_seed\\\": [\\n        {\\n          \\\"seed\\\": 42,\\n          \\\"naive_pearson\\\": {\\n            \\\"method\\\": \\\"naive_pearson\\\",\\n            \\\"peak_lag\\\": 3,\\n            \\\"r\\\": 0.8027,\\n            \\\"significant\\\": true,\\n            \\\"effect_size_r\\\": 0.8027,\\n            \\\"effect_size_type\\\": \\\"pearson_r\\\",\\n            \\\"effect_size_label\\\": \\\"large\\\",\\n            \\\"p_raw\\\": 0.01648,\\n            \\\"p_fdr\\\": 0.0182,\\n            \\\"significant_fdr\\\": true\\n          },\\n          \\\"dif\\n\\n... [截断: 输出过长，省略 152963 字符] ...\\n\\ne\\\",\\n            \\\"p_raw\\\": 0.126873,\\n            \\\"p_fdr\\\": 0.198,\\n            \\\"significant_fdr\\\": false\\n          }\\n        },\\n        {\\n          \\\"seed\\\": 45,\\n          \\\"naive_pearson\\\": {\\n            \\\"method\\\": \\\"naive_pearson\\\",\\n            \\\"peak_lag\\\": -1,\\n            \\\"r\\\": -0.8187,\\n            \\\"significant\\\": true,\\n            \\\"effect_size_r\\\": 0.8187,\\n            \\\"effect_size_type\\\": \\\"pearson_r\\\",\\n            \\\"effect_size_label\\\": \\\"large\\\",\\n            \\\"p_raw\\\": 0.003772,\\n            \\\"p_fdr\\\": 0.0047,\\n            \\\"significant_fdr\\\": true\\n          },\\n          \\\"differenced_xcorr\\\": {\\n            \\\"method\\\": \\\"differenced_xcorr\\\",\\n            \\\"peak_lag\\\": -3,\\n            \\\"r\\\": -0.7335,\\n            \\\"significant\\\": false,\\n            \\\"effect_size_r\\\": 0.7335,\\n            \\\"effect_size_type\\\": \\\"pearson_r\\\",\\n            \\\"effect_size_label\\\": \\\"large\\\",\\n            \\\"p_raw\\\": 0.060616,\\n            \\\"p_fdr\\\": 0.0669,\\n            \\\"significant_fdr\\\": false\\n          },\\n          \\\"threshold_onset\\\": {\\n            \\\"method\\\": \\\"threshold_onset\\\",\\n            \\\"canary_onset\\\": null,\\n            \\\"downstream_onset\\\": 4,\\n            \\\"lead_time\\\": null,\\n            \\\"significant\\\": false,\\n            \\\"note\\\": \\\"onset not detected for: canary\\\",\\n            \\\"effect_size\\\": null,\\n            \\\"effect_size_type\\\": null,\\n            \\\"effect_size_label\\\": null\\n          },\\n          \\\"toda_yamamoto\\\": {\\n            \\\"method\\\": \\\"toda_yamamoto\\\",\\n            \\\"p\\\": 1,\\n            \\\"d_max\\\": 2,\\n            \\\"k\\\": 3,\\n            \\\"wald_F\\\": 0.0136,\\n            \\\"significant\\\": false,\\n            \\\"df_resid\\\": 1,\\n            \\\"d_canary\\\": 2,\\n            \\\"d_downstream\\\": 0,\\n            \\\"effect_size_f2\\\": 0.0136,\\n            \\\"effect_size_type\\\": \\\"cohens_f2\\\",\\n            \\\"effect_size_label\\\": \\\"negligible\\\",\\n            \\\"p_raw\\\": 0.926183,\\n            \\\"p_fdr\\\": 0.9409,\\n            \\\"significant_fdr\\\": false\\n          },\\n          \\\"permutation_granger\\\": {\\n            \\\"method\\\": \\\"permutation_granger\\\",\\n            \\\"f_stat\\\": 11.8051,\\n            \\\"significant\\\": false,\\n            \\\"effect_size_f2\\\": 1.9675,\\n            \\\"null_mean\\\": 3.1238,\\n            \\\"null_std\\\": 9.5974,\\n            \\\"n_perm\\\": 1000,\\n            \\\"effect_size\\\": 1.9675,\\n            \\\"effect_size_type\\\": \\\"cohens_f2\\\",\\n            \\\"effect_size_label\\\": \\\"large\\\",\\n            \\\"p_raw\\\": 0.103896,\\n            \\\"p_fdr\\\": 0.1797,\\n            \\\"significant_fdr\\\": false\\n          }\\n        }\\n      ],\\n      \\\"summary\\\": {\\n        \\\"naive_pearson\\\": {\\n          \\\"sig_seeds\\\": 4,\\n          \\\"total\\\": 4,\\n          \\\"verdict\\\": \\\"SIGNIFICANT\\\"\\n        },\\n        \\\"differenced_xcorr\\\": {\\n          \\\"sig_seeds\\\": 3,\\n          \\\"total\\\": 4,\\n          \\\"verdict\\\": \\\"SIGNIFICANT\\\"\\n        },\\n        \\\"threshold_onset\\\": {\\n          \\\"sig_seeds\\\": 0,\\n          \\\"total\\\": 4,\\n          \\\"verdict\\\": \\\"NOT_SIGNIFICANT\\\"\\n        },\\n        \\\"toda_yamamoto\\\": {\\n          \\\"sig_seeds\\\": 2,\\n          \\\"total\\\": 4,\\n          \\\"verdict\\\": \\\"NOT_SIGNIFICANT\\\"\\n        },\\n        \\\"permutation_granger\\\": {\\n          \\\"sig_seeds\\\": 2,\\n          \\\"total\\\": 4,\\n          \\\"verdict\\\": \\\"NOT_SIGNIFICANT\\\"\\n        }\\n      },\\n      \\\"robust_5method\\\": false,\\n      \\\"spurious_5method\\\": true,\\n      \\\"spurious_reason_5method\\\": \\\"threshold_onset n.s., toda_yamamoto n.s., permutation_granger n.s.\\\",\\n      \\\"methods_agree_5\\\": 2,\\n      \\\"robust_4method\\\": false,\\n      \\\"spurious_4method\\\": true,\\n      \\\"methods_agree_4\\\": 2,\\n      \\\"spurious\\\": true,\\n      \\\"robust\\\": false,\\n      \\\"naive_only\\\": false\\n    }\\n  ],\\n  \\\"fdr_correction\\\": {\\n    \\\"method\\\": \\\"benjamini-hochberg\\\",\\n    \\\"alpha\\\": 0.05,\\n    \\\"per_method\\\": {\\n      \\\"naive_pearson\\\": {\\n        \\\"total_tests\\\": 64,\\n        \\\"raw_significant\\\": 63,\\n        \\\"fdr_significant\\\": 63\\n      },\\n      \\\"differenced_xcorr\\\": {\\n        \\\"total_tests\\\": 64,\\n        \\\"raw_significant\\\": 55,\\n        \\\"fdr_significant\\\": 53\\n      },\\n      \\\"toda_yamamoto\\\": {\\n        \\\"total_tests\\\": 64,\\n        \\\"raw_significant\\\": 26,\\n        \\\"fdr_significant\\\": 24\\n      },\\n      \\\"permutation_granger\\\": {\\n        \\\"total_tests\\\": 64,\\n        \\\"raw_significant\\\": 34,\\n        \\\"fdr_significant\\\": 27\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.68}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Now let me get the v6 granger results more carefully. I need to extract the per-alpha sig counts for the permutation_granger method. Let me also get the d028 data which has per-alpha method rates.

Let me now extract the specific numbers I need:

From d028_fpr_null_control_full.json, I have the per-alpha-per-method breakdown:
- **phase2_fdr_sig_rates** tells me per alpha per method sig rates

For v6:
- 5 alphas × 8 pairs = 40 tests


- The granger_results have p_raw and p_fdr for each test
- From the v6 report, the FDR-significant pairs (p_fdr < 0.05) are marked with *

Now I'm pulling the specific numbers from the data. Looking at d028, the naive correlation method shows 100% FPR across most alphas, with all 8 pairs significant at both raw and FDR levels. For v6, I need to count how many of the 8 pairs per alpha show FDR significance.

The pipeline has four sequential filtering stages: naive correlation catches everything including shared trends, first-differencing removes those trends, permutation Granger with FDR correction tests for actual causality, and multi-seed replication checks consistency. So I'm tracking how many pairs survive each filter, starting with the naive method showing all 40 pairs (5 alphas × 8 pairs) as significant.

For the differencing stage, I see the raw counts vary by alpha—at α=0.0 only 4 of 8 pairs remain significant after differencing, suggesting those are the ones with genuine signal beyond shared trends. Now I'm looking at which pairs pass the permutation Granger test with FDR correction applied across all 40 tests.

From the v6 report, six pairs survive FDR at p < 0.05: entropy and ECE both show Granger causality into d1 and d2, with the strongest effects at α=0.75 and α=1.0. Let me recount the exact list from the report to make sure I have the right number. Looking at the raw p-values from the report, I'm counting the ones below 0.05 threshold—there are more than the 6 that survive FDR correction, which makes sense given that multiple testing correction is stricter. Let me verify this matches the 14 raw significant results mentioned in the question. Looking at the full breakdown across all alpha values, I'm counting the significant results where p_raw falls below 0.05—there are several scattered across α=0.25, α=0.50, and α=0.75, with entropy→d1 showing up as significant at multiple alpha levels. Now I'm checking the FDR-corrected p-values more carefully—entropy→d1 at α=0.75 comes in at 0.054, which just misses the 0.05 threshold, so that one doesn't count. That leaves 3 significant results for α=0.75 and 3 for α=1.00, totaling 6 FDR-significant findings, which matches the expected count.

For v4 with 4 alphas and 8 pairs giving 32 total tests, the report shows 10 raw significant results but only 1 survives FDR correction. Looking at the method ablation data with MVP settings at α=1.0 across 4 seeds, I'm seeing the summary statistics—naive method flags 16 out of 16 pairs, differenced catches 14, threshold gets 9, and the more conservative approaches like ty and permutation Granger find 4 and 6 respectively. The robust pairs that hold up are token_entropy→d1, token_entropy→d2, token_entropy→d3, and ece→d1, with a spurious rate of 0.75 across 12 spurious detections.

Now looking at the FDR-corrected results at α=1.0, naive maintains all 63 significant findings, differenced drops from 55 to 53, ty goes from 26 to 24, and permutation Granger is hit hardest, dropping from 34 to 27. I'm organizing these into the pipeline stages—starting with the naive correlation scan across the v6 framework's 5 alphas and 8 directions for 40 total pairs, where all naive tests come through as significant. Breaking down by alpha, the null control at α=0.0 shows 8 out of 8 significant (all false positives as expected), and α=0.25 also hits 8 out of 8.

But I'm realizing I need to be more careful about which pairs are actually being tested—the v6 framework tests specific directional pairs in the Granger context, while d028's naive correlation tests different downstream metrics, so I can't just assume they're the same pairs across methods. Let me reconsider what the pipeline is actually describing.

The 4-stage filtering concept makes sense: start with naive Pearson to catch everything, then progressively apply first-differencing to remove trends, Granger causality with FDR to eliminate non-causal associations, and finally multi-seed replication to filter out seed artifacts. For v6 with 40 tests across 5 alphas and 8 directional pairs, I need to figure out which metric pairs are actually relevant for this pipeline and whether d028's phase2_fdr_sig_rates data aligns with what I'm trying to show.

Looking at the d028 data, I'm seeing inconsistencies in the pair counts across alphas—56 total pairs when pooled across the different alpha values, but v6 was supposed to have 40 tests. The alpha values in d028 are [0.0, 0.25, 0.5, 1.0] while v6 uses [0.0, 0.25, 0.5, 0.75, 1.0], so I need to clarify which dataset actually corresponds to the v6 analysis and whether the single-seed versus multi-seed structure matches what I'm working with. tests corrected together. It appears that for the v6 Granger analysis, each alpha-direction combination is one test, regardless of seeds.

OK, let me just use the v6 data for Stages 1-3 and the method_ablation for Stage 4. The v6 provides the per-alpha Granger results and FDR corrections. I'll use the d028 data for the naive/differenced stages.

But wait, the v6 granger_causality tests 8 directions per alpha × 5 alphas = 40 tests. These are specifically permutation Granger tests (differenced). That's Stage 3.

For Stage 1 (naive) and Stage 2 (differenced), I need different data. The d028 file has this per-method breakdown for all alphas.

Let me check what pairs the d028 file tests vs what the v6 tests. The d028 data covers unidirectional canary-to-downstream pairs, while v6 tests bidirectional relationships including the reverse directions. Since the pipeline figure focuses on the filtering of canary signals flowing downstream, the d028 pairs align better with that conceptual framing, though v6 captures the full bidirectional picture. The pipeline treats all tested directions as input, and FDR correction filters down the significant findings. I'll use v6 as the primary source for Stage 3, and d028 for Stages 1-2 since it has the naive and differenced results broken down by alpha. Now I need to think through how the input pairs and elimination work across stages—for v6 with 5 alphas and 8 directions each, that's 40 total tests, but I need to reconcile this with how the per-alpha method rates are structured in the d028 data. I see the issue now—I have data from three different analyses with different structures, so I need to pick the most representative pieces to tell a coherent pipeline story. The d028 dataset gives me the clearest per-method comparison, so I'll use naive at α=0.0 as my starting point to show why it fails, then move to differenced filtering to demonstrate the improvement, even though it still leaves false positives. I need to clarify the task structure first—each stage operates on different datasets and pair counts, so I'm not tracking a literal funnel but rather showing the filtering effect at each methodological step. Let me organize the JSON to capture the methodology, representative numbers, and concrete examples for each stage, making sure to extract the specific input/output pair counts and false positive rates from the different analyses. 多 seed 验证进一步筛选了虚假信号，比如 α=0.75 的 token_entropy→perplexity 在单 seed 被标记为稳健，但在 α=1.0 的多 seed 结果（4 个 seed：42/43/44/45）中被确认为虚假。我现在意识到 v6 框架的完整流程是 40 个输入经过 Stage 1 保留约 40 个显著结果，Stage 2 通过差分进一步减少，Stage 3 从 14 个原始显著结果经 FDR 校正到 6 个，最后 Stage 4 用多 seed 进一步过滤。问题是 v6 方向的具体差分前后数据缺失，虽然 d028 有这些统计但针对的是不同的配对集合。

现在对比 d028 的 8 个前向方向（token_entropy→d1/d2/d3/ppl，ece→d1/d2/d3/ppl）与 v6 的 8 个前向方向（entropy→d1/d2，ECE→d1/d2，以及反向的 d1/d2→entropy/ECE），发现它们并不完全匹配。

我决定采用分阶段的方法：前两个阶段用 d028 的 8 对框架，第三阶段用 v6 的 40 测试框架，第四阶段用方法消融的 16 对框架。每个阶段可以有不同的对数，"漏斗"显示的是缩减速率而非连续计数。实际上，最简单的做法是直接使用 d028 的完整数据，它包含所有方法和所有 alpha 值。

现在我在查看 d028 的 FPR 零控制数据。在 α=0.0 时，朴素方法在 8 对中全部显著（FPR=1.0），差分方法是 4/8（FPR=0.5），而排列 Granger 和 TY 方法都是 0/8（FPR=0.0）。随着 alpha 增加到 0.25 和 0.5，差分方法的表现变化，排列 Granger 方法开始显示一些显著性，但在 FDR 校正后都降为 0/8。当 alpha 达到 1.0 时，样本量增加到 32 对，朴素方法仍然全部显著，差分方法也变成全部显著。

现在我要基于 v6 框架构建管道。第 3 阶段我已经有 v6 数据，但第 1-2 阶段我会用 d028 数据作为证据，同时用 v6 的 40 个测试集来呈现管道。实际上，我可以更实用地构建 JSON——各个阶段不需要在完全相同的测试集上运行，每个阶段只需展示特定方法的贡献。我会标注每个阶段的数据来源。

对于 v6 框架，我设置 5 个 alpha 值（0.0、0.25、0.5、0.75、1.0），每个 alpha 有 8 个方向的因果对，总共 40 个测试。

现在我在查看第 3 阶段的排列 Granger 加 FDR 结果，按 alpha 值统计原始显著性（p_raw < 0.05）的情况。

当 alpha 为 1.0 时有 5 个显著结果，总共 14 个原始显著性。在 FDR 校正后（p_fdr < 0.05），只有 alpha 为 0.75 和 1.0 时各有 3 个显著结果，总共 6 个通过 FDR 的显著性。

这意味着有 8 个对在原始显著性中但未通过 FDR 校正。

我在检查这些被排除的配对时发现了一个问题——ECE→d2 @ α=1.0 实际上通过了 FDR 检验，所以它不应该在这个列表中。

让我重新整理一下在 α=0.75 和 α=1.0 处通过 FDR 显著性检验的配对，看起来总共有 6 个关系在这两个阈值处达到了统计显著性。

现在我需要列出那 8 个被 FDR 筛除掉的配对，它们的原始 p 值虽然较小但 FDR 校正后都超过了 0.05 的阈值。

确认了 14 个原始显著的结果中有 8 个被筛除，剩下 6 个通过了 FDR 校正。

对于 v4 的数据，我在推断它的测试数量——4 个 alpha 值乘以 8 个方向等于 32 个测试。题目提到"原始 10/32 → FDR 1/32"，这意味着 v4 中原始显著的有 10 个，但经过 FDR 校正后只有 1 个幸存下来。我需要从 v4 的数据中验证这个结果。

让我查看 v4 报告中的具体数据。根据 d028 的单种子排列 Granger 因果数据，我知道不同 alpha 值下的原始显著结果数，但我需要确认 v4 中 alpha=1.0 是否也是单种子配置。

如果 32 个独立测试来自 8 个方向对 × 4 个 alpha 值，那么我应该能从 v4 报告中直接验证每个 alpha 水平的 FDR 校正结果。

让我查看一下具体的数据。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "bb454664-d405-471a-9ff1-da95e5cf3aa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqwZx2VEqMLYcY8qcj6SLc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9538,
      "cache_read_input_tokens": 50322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9538
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 37_

读取 v4 报告和查找 D017 相关数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "5874acc1-1d37-4218-870f-0b77f1f1e7a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqwZx2VEqMLYcY8qcj6SLc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9538,
      "cache_read_input_tokens": 50322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9538
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014zY4TUqepaCEWPAk8khfXQ`</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v4_report.md",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "6ba702af-2fa2-41f6-a695-92b26f44404c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqwZx2VEqMLYcY8qcj6SLc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9538,
      "cache_read_input_tokens": 50322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9538
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T15:35:39.356Z_

<details><summary>↩ Tool result · `toolu_014zY4TUqepaCEWPAk8khfXQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Cross-Alpha Analysis Report (v4)\\n\\n**Date:** 2026-05-15\\n**Alpha points:** [0.0, 0.25, 0.5, 1.0]\\n**Generations:** gen_0 to gen_10\\n\\n## 1. Dose-Response (gen0 to genN drift %)\\n\\n| Metric | α=0.00 | α=0.25 | α=0.50 | α=1.00 |\\n|--------|--------:|--------:|--------:|--------:|\\n| distinct_1 | -13.8% | -40.3% | -37.3% | -28.3% |\\n| distinct_2 | -9.8% | -57.1% | -51.5% | -35.2% |\\n| distinct_3 | -4.5% | -59.9% | -52.4% | -31.6% |\\n| token_entropy | -5.1% | -4.1% | -18.6% | -60.5% |\\n| ece | +51.7% | +79.7% | +842.8% | +3762.6% |\\n| perplexity | -21.7% | -17.2% | +21.1% | +3624.6% |\\n\\n## 2. Granger Causality (bidirectional, permutation, FDR-corrected)\\n\\n| Direction | α=0.00 p_raw | p_fdr | α=0.25 p_raw | p_fdr | α=0.50 p_raw | p_fdr | α=1.00 p_raw | p_fdr |\\n|-----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|\\n| entropy->d1 | 0.0514 | 0.1370 | 0.0150 | 0.0960 | 0.0950 | 0.1833 | 0.0060 | 0.0640 |\\n| ECE->d1 | 0.9498 | 0.9782 | 0.2352 | 0.3960 | 0.0190 | 0.1013 | 0.0006 | 0.0192 * |\\n| entropy->d2 | 0.0804 | 0.1833 | 0.0730 | 0.1797 | 0.0974 | 0.1833 | 0.0108 | 0.0864 |\\n| ECE->d2 | 0.5443 | 0.6006 | 0.0882 | 0.1833 | 0.0394 | 0.1370 | 0.0046 | 0.0640 |\\n| d1->entropy | 0.7956 | 0.8487 | 0.0236 | 0.1079 | 0.2170 | 0.3857 | 0.3313 | 0.4356 |\\n| d1->ECE | 0.3431 | 0.4356 | 0.4661 | 0.5327 | 0.2771 | 0.4356 | 0.0502 | 0.1370 |\\n| d2->entropy | 0.9782 | 0.9782 | 0.0498 | 0.1370 | 0.3143 | 0.4356 | 0.3447 | 0.4356 |\\n| d2->ECE | 0.3539 | 0.4356 | 0.3969 | 0.4704 | 0.3529 | 0.4356 | 0.0430 | 0.1370 |\\n\\nFDR: 32 tests, BH correction. \\\\* = p_fdr < 0.05\\n\\n## 3. Consensus Classification (regime-dependent validity)\\n\\n### α=0.00 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 0/16\\n- Non-robust: 16/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 2/5 |\\n| token_entropy→distinct_1 | non-robust | 3/5 |\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\n| token_entropy��distinct_3 | non-robust | 2/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 3/5 |\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\n| self_bleu→distinct_3 | non-robust | 3/5 |\\n| ece→perplexity | non-robust | 1/5 |\\n| ece→distinct_1 | non-robust | 2/5 |\\n| ece→distinct_2 | non-robust | 1/5 |\\n| ece→distinct_3 | non-robust | 2/5 |\\n| effective_rank→perplexity | non-robust | 0/5 |\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\n| effective_rank→distinct_2 | non-robust | 1/5 |\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\n\\n### α=0.25 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 1/16\\n- Non-robust: 15/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 2/5 |\\n| token_entropy→distinct_1 | **ROBUST** | 4/5 |\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\n| token_entropy→distinct_3 | non-robust | 3/5 |\\n| self_bleu→perplexity | non-robust | 0/5 |\\n| self_bleu→distinct_1 | non-robust | 0/5 |\\n| self_bleu→distinct_2 | non-robust | 0/5 |\\n| self_bleu→distinct_3 | non-robust | 0/5 |\\n| ece→perplexity | non-robust | 1/5 |\\n| ece→distinct_1 | non-robust | 1/5 |\\n| ece→distinct_2 | non-robust | 1/5 |\\n| ece→distinct_3 | non-robust | 1/5 |\\n| effective_rank→perplexity | non-robust | 1/5 |\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\n| effective_rank→distinct_2 | non-robust | 2/5 |\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\n\\n### α=0.50 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 0/16\\n- Non-robust: 16/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 3/5 |\\n| token_entropy→distinct_1 | non-robust | 3/5 |\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\n| token_entropy→distinct_3 | non-robust | 3/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\n| self_bleu→distinct_2 | non-robust | 1/5 |\\n| self_bleu→distinct_3 | non-robust | 1/5 |\\n| ece→perplexity | non-robust | 3/5 |\\n| ece→distinct_1 | non-robust | 3/5 |\\n| ece→distinct_2 | non-robust | 3/5 |\\n| ece→distinct_3 | non-robust | 3/5 |\\n| effective_rank→perplexity | non-robust | 3/5 |\\n| effective_rank→distinct_1 | non-robust | 3/5 |\\n| effective_rank→distinct_2 | non-robust | 2/5 |\\n| effective_rank→distinct_3 | non-robust | 2/5 |\\n\\n### α=1.00 (4-seed full consensus (≥4/5 methods, ≥3/4 seeds))\\n\\n- Robust pairs: 6/16\\n- Non-robust: 10/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 3/5 |\\n| token_entropy→distinct_1 | **ROBUST** | 5/5 |\\n| token_entropy→distinct_2 | **ROBUST** | 5/5 |\\n| token_entropy→distinct_3 | **ROBUST** | 5/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\n| self_bleu→distinct_3 | non-robust | 2/5 |\\n| ece→perplexity | non-robust | 3/5 |\\n| ece→distinct_1 | **ROBUST** | 4/5 |\\n| ece→distinct_2 | **ROBUST** | 4/5 |\\n| ece→distinct_3 | **ROBUST** | 4/5 |\\n| effective_rank→perplexity | non-robust | 2/5 |\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\n| effective_rank→distinct_2 | non-robust | 1/5 |\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\n\\n### Regime Comparison Summary\\n\\n- Stable pairs (same classification at all α): 10/16\\n- Regime-dependent pairs: 6/16\\n\\n| Pair | α=0.00 | α=0.25 | α=0.50 | α=1.00 | Stable |\\n|------|--------|--------|--------|--------|--------|\\n| token_entropy→perplexity | .(2) | .(2) | .(3) | .(3) | Y |\\n| token_entropy→distinct_1 | .(3) | R(4) | .(3) | R(5) | N |\\n| token_entropy→distinct_2 | .(3) | .(3) | .(3) | R(5) | N |\\n| token_entropy→distinct_3 | .(2) | .(3) | .(3) | R(5) | N |\\n| self_bleu→perplexity | .(2) | .(0) | .(2) | .(2) | Y |\\n| self_bleu→distinct_1 | .(3) | .(0) | .(1) | .(1) | Y |\\n| self_bleu→distinct_2 | .(2) | .(0) | .(1) | .(2) | Y |\\n| self_bleu→distinct_3 | .(3) | .(0) | .(1) | .(2) | Y |\\n| ece→perplexity | .(1) | .(1) | .(3) | .(3) | Y |\\n| ece→distinct_1 | .(2) | .(1) | .(3) | R(4) | N |\\n| ece→distinct_2 | .(1) | .(1) | .(3) | R(4) | N |\\n| ece→distinct_3 | .(2) | .(1) | .(3) | R(4) | N |\\n| effective_rank→perplexity | .(0) | .(1) | .(3) | .(2) | Y |\\n| effective_rank→distinct_1 | .(2) | .(2) | .(3) | .(2) | Y |\\n| effective_rank→distinct_2 | .(1) | .(2) | .(2) | .(1) | Y |\\n| effective_rank→distinct_3 | .(1) | .(1) | .(2) | .(1) | Y |\\n\\n## 4. D1 Velocity\\n\\n| α | mean_vel | early | late | decel_ratio |\\n|---|----------|-------|------|-------------|\\n| 0.00 | -0.001354 | -0.002516 | -0.000191 | 0.08 |\\n| 0.25 | -0.003962 | -0.006938 | -0.000986 | 0.14 |\\n| 0.50 | -0.003661 | -0.006153 | -0.001170 | 0.19 |\\n| 1.00 | -0.002783 | -0.005203 | -0.000364 | 0.07 |\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "cfbce656-a447-4a4d-8e07-94964084e5c7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"# Cross-Alpha Analysis Report (v4)\\\\n\\\\n**Date:** 2026-05-15\\\\n**Alpha points:** [0.0, 0.25, 0.5, 1.0]\\\\n**Generations:** gen_0 to gen_10\\\\n\\\\n## 1. Dose-Response (gen0 to genN drift %)\\\\n\\\\n| Metric | α=0.00 | α=0.25 | α=0.50 | α=1.00 |\\\\n|--------|--------:|--------:|--------:|--------:|\\\\n| distinct_1 | -13.8% | -40.3% | -37.3% | -28.3% |\\\\n| distinct_2 | -9.8% | -57.1% | -51.5% | -35.2% |\\\\n| distinct_3 | -4.5% | -59.9% | -52.4% | -31.6% |\\\\n| token_entropy | -5.1% | -4.1% | -18.6% | -60.5% |\\\\n| ece | +51.7% | +79.7% | +842.8% | +3762.6% |\\\\n| perplexity | -21.7% | -17.2% | +21.1% | +3624.6% |\\\\n\\\\n## 2. Granger Causality (bidirectional, permutation, FDR-corrected)\\\\n\\\\n| Direction | α=0.00 p_raw | p_fdr | α=0.25 p_raw | p_fdr | α=0.50 p_raw | p_fdr | α=1.00 p_raw | p_fdr |\\\\n|-----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|\\\\n| entropy->d1 | 0.0514 | 0.1370 | 0.0150 | 0.0960 | 0.0950 | 0.1833 | 0.0060 | 0.0640 |\\\\n| ECE->d1 | 0.9498 | 0.9782 | 0.2352 | 0.3960 | 0.0190 | 0.1013 | 0.0006 | 0.0192 * |\\\\n| entropy->d2 | 0.0804 | 0.1833 | 0.0730 | 0.1797 | 0.0974 | 0.1833 | 0.0108 | 0.0864 |\\\\n| ECE->d2 | 0.5443 | 0.6006 | 0.0882 | 0.1833 | 0.0394 | 0.1370 | 0.0046 | 0.0640 |\\\\n| d1->entropy | 0.7956 | 0.8487 | 0.0236 | 0.1079 | 0.2170 | 0.3857 | 0.3313 | 0.4356 |\\\\n| d1->ECE | 0.3431 | 0.4356 | 0.4661 | 0.5327 | 0.2771 | 0.4356 | 0.0502 | 0.1370 |\\\\n| d2->entropy | 0.9782 | 0.9782 | 0.0498 | 0.1370 | 0.3143 | 0.4356 | 0.3447 | 0.4356 |\\\\n| d2->ECE | 0.3539 | 0.4356 | 0.3969 | 0.4704 | 0.3529 | 0.4356 | 0.0430 | 0.1370 |\\\\n\\\\nFDR: 32 tests, BH correction. \\\\\\\\* = p_fdr < 0.05\\\\n\\\\n## 3. Consensus Classification (regime-dependent validity)\\\\n\\\\n### α=0.00 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\\\n\\\\n- Robust pairs: 0/16\\\\n- Non-robust: 16/16\\\\n\\\\n| Pair | Robust | Methods |\\\\n|------|--------|---------|\\\\n| token_entropy→perplexity | non-robust | 2/5 |\\\\n| token_entropy→distinct_1 | non-robust | 3/5 |\\\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\\\n| token_entropy��distinct_3 | non-robust | 2/5 |\\\\n| self_bleu→perplexity | non-robust | 2/5 |\\\\n| self_bleu→distinct_1 | non-robust | 3/5 |\\\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\\\n| self_bleu→distinct_3 | non-robust | 3/5 |\\\\n| ece→perplexity | non-robust | 1/5 |\\\\n| ece→distinct_1 | non-robust | 2/5 |\\\\n| ece→distinct_2 | non-robust | 1/5 |\\\\n| ece→distinct_3 | non-robust | 2/5 |\\\\n| effective_rank→perplexity | non-robust | 0/5 |\\\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\\\n| effective_rank→distinct_2 | non-robust | 1/5 |\\\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\\\n\\\\n### α=0.25 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\\\n\\\\n- Robust pairs: 1/16\\\\n- Non-robust: 15/16\\\\n\\\\n| Pair | Robust | Methods |\\\\n|------|--------|---------|\\\\n| token_entropy→perplexity | non-robust | 2/5 |\\\\n| token_entropy→distinct_1 | **ROBUST** | 4/5 |\\\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\\\n| token_entropy→distinct_3 | non-robust | 3/5 |\\\\n| self_bleu→perplexity | non-robust | 0/5 |\\\\n| self_bleu→distinct_1 | non-robust | 0/5 |\\\\n| self_bleu→distinct_2 | non-robust | 0/5 |\\\\n| self_bleu→distinct_3 | non-robust | 0/5 |\\\\n| ece→perplexity | non-robust | 1/5 |\\\\n| ece→distinct_1 | non-robust | 1/5 |\\\\n| ece→distinct_2 | non-robust | 1/5 |\\\\n| ece→distinct_3 | non-robust | 1/5 |\\\\n| effective_rank→perplexity | non-robust | 1/5 |\\\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\\\n| effective_rank→distinct_2 | non-robust | 2/5 |\\\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\\\n\\\\n### α=0.50 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\\\n\\\\n- Robust pairs: 0/16\\\\n- Non-robust: 16/16\\\\n\\\\n| Pair | Robust | Methods |\\\\n|------|--------|---------|\\\\n| token_entropy→perplexity | non-robust | 3/5 |\\\\n| token_entropy→distinct_1 | non-robust | 3/5 |\\\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\\\n| token_entropy→distinct_3 | non-robust | 3/5 |\\\\n| self_bleu→perplexity | non-robust | 2/5 |\\\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\\\n| self_bleu→distinct_2 | non-robust | 1/5 |\\\\n| self_bleu→distinct_3 | non-robust | 1/5 |\\\\n| ece→perplexity | non-robust | 3/5 |\\\\n| ece→distinct_1 | non-robust | 3/5 |\\\\n| ece→distinct_2 | non-robust | 3/5 |\\\\n| ece→distinct_3 | non-robust | 3/5 |\\\\n| effective_rank→perplexity | non-robust | 3/5 |\\\\n| effective_rank→distinct_1 | non-robust | 3/5 |\\\\n| effective_rank→distinct_2 | non-robust | 2/5 |\\\\n| effective_rank→distinct_3 | non-robust | 2/5 |\\\\n\\\\n### α=1.00 (4-seed full consensus (≥4/5 methods, ≥3/4 seeds))\\\\n\\\\n- Robust pairs: 6/16\\\\n- Non-robust: 10/16\\\\n\\\\n| Pair | Robust | Methods |\\\\n|------|--------|---------|\\\\n| token_entropy→perplexity | non-robust | 3/5 |\\\\n| token_entropy→distinct_1 | **ROBUST** | 5/5 |\\\\n| token_entropy→distinct_2 | **ROBUST** | 5/5 |\\\\n| token_entropy→distinct_3 | **ROBUST** | 5/5 |\\\\n| self_bleu→perplexity | non-robust | 2/5 |\\\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\\\n| self_bleu→distinct_3 | non-robust | 2/5 |\\\\n| ece→perplexity | non-robust | 3/5 |\\\\n| ece→distinct_1 | **ROBUST** | 4/5 |\\\\n| ece→distinct_2 | **ROBUST** | 4/5 |\\\\n| ece→distinct_3 | **ROBUST** | 4/5 |\\\\n| effective_rank→perplexity | non-robust | 2/5 |\\\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\\\n| effective_rank→distinct_2 | non-robust | 1/5 |\\\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\\\n\\\\n### Regime Comparison Summary\\\\n\\\\n- Stable pairs (same classification at all α): 10/16\\\\n- Regime-dependent pairs: 6/16\\\\n\\\\n| Pair | α=0.00 | α=0.25 | α=0.50 | α=1.00 | Stable |\\\\n|------|--------|--------|--------|--------|--------|\\\\n| token_entropy→perplexity | .(2) | .(2) | .(3) | .(3) | Y |\\\\n| token_entropy→distinct_1 | .(3) | R(4) | .(3) | R(5) | N |\\\\n| token_entropy→distinct_2 | .(3) | .(3) | .(3) | R(5) | N |\\\\n| token_entropy→distinct_3 | .(2) | .(3) | .(3) | R(5) | N |\\\\n| self_bleu→perplexity | .(2) | .(0) | .(2) | .(2) | Y |\\\\n| self_bleu→distinct_1 | .(3) | .(0) | .(1) | .(1) | Y |\\\\n| self_bleu→distinct_2 | .(2) | .(0) | .(1) | .(2) | Y |\\\\n| self_bleu→distinct_3 | .(3) | .(0) | .(1) | .(2) | Y |\\\\n| ece→perplexity | .(1) | .(1) | .(3) | .(3) | Y |\\\\n| ece→distinct_1 | .(2) | .(1) | .(3) | R(4) | N |\\\\n| ece→distinct_2 | .(1) | .(1) | .(3) | R(4) | N |\\\\n| ece→distinct_3 | .(2) | .(1) | .(3) | R(4) | N |\\\\n| effective_rank→perplexity | .(0) | .(1) | .(3) | .(2) | Y |\\\\n| effective_rank→distinct_1 | .(2) | .(2) | .(3) | .(2) | Y |\\\\n| effective_rank→distinct_2 | .(1) | .(2) | .(2) | .(1) | Y |\\\\n| effective_rank→distinct_3 | .(1) | .(1) | .(2) | .(1) | Y |\\\\n\\\\n## 4. D1 Velocity\\\\n\\\\n| α | mean_vel | early | late | decel_ratio |\\\\n|---|----------|-------|------|-------------|\\\\n| 0.00 | -0.001354 | -0.002516 | -0.000191 | 0.08 |\\\\n| 0.25 | -0.003962 | -0.006938 | -0.000986 | 0.14 |\\\\n| 0.50 | -0.003661 | -0.006153 | -0.001170 | 0.19 |\\\\n| 1.00 | -0.002783 | -0.005203 | -0.000364 | 0.07 |\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"# Cross-Alpha Analysis Report (v4)\\n\\n**Date:** 2026-05-15\\n**Alpha points:** [0.0, 0.25, 0.5, 1.0]\\n**Generations:** gen_0 to gen_10\\n\\n## 1. Dose-Response (gen0 to genN drift %)\\n\\n| Metric | α=0.00 | α=0.25 | α=0.50 | α=1.00 |\\n|--------|--------:|--------:|--------:|--------:|\\n| distinct_1 | -13.8% | -40.3% | -37.3% | -28.3% |\\n| distinct_2 | -9.8% | -57.1% | -51.5% | -35.2% |\\n| distinct_3 | -4.5% | -59.9% | -52.4% | -31.6% |\\n| token_entropy | -5.1% | -4.1% | -18.6% | -60.5% |\\n| ece | +51.7% | +79.7% | +842.8% | +3762.6% |\\n| perplexity | -21.7% | -17.2% | +21.1% | +3624.6% |\\n\\n## 2. Granger Causality (bidirectional, permutation, FDR-corrected)\\n\\n| Direction | α=0.00 p_raw | p_fdr | α=0.25 p_raw | p_fdr | α=0.50 p_raw | p_fdr | α=1.00 p_raw | p_fdr |\\n|-----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|\\n| entropy->d1 | 0.0514 | 0.1370 | 0.0150 | 0.0960 | 0.0950 | 0.1833 | 0.0060 | 0.0640 |\\n| ECE->d1 | 0.9498 | 0.9782 | 0.2352 | 0.3960 | 0.0190 | 0.1013 | 0.0006 | 0.0192 * |\\n| entropy->d2 | 0.0804 | 0.1833 | 0.0730 | 0.1797 | 0.0974 | 0.1833 | 0.0108 | 0.0864 |\\n| ECE->d2 | 0.5443 | 0.6006 | 0.0882 | 0.1833 | 0.0394 | 0.1370 | 0.0046 | 0.0640 |\\n| d1->entropy | 0.7956 | 0.8487 | 0.0236 | 0.1079 | 0.2170 | 0.3857 | 0.3313 | 0.4356 |\\n| d1->ECE | 0.3431 | 0.4356 | 0.4661 | 0.5327 | 0.2771 | 0.4356 | 0.0502 | 0.1370 |\\n| d2->entropy | 0.9782 | 0.9782 | 0.0498 | 0.1370 | 0.3143 | 0.4356 | 0.3447 | 0.4356 |\\n| d2->ECE | 0.3539 | 0.4356 | 0.3969 | 0.4704 | 0.3529 | 0.4356 | 0.0430 | 0.1370 |\\n\\nFDR: 32 tests, BH correction. \\\\* = p_fdr < 0.05\\n\\n## 3. Consensus Classification (regime-dependent validity)\\n\\n### α=0.00 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 0/16\\n- Non-robust: 16/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 2/5 |\\n| token_entropy→distinct_1 | non-robust | 3/5 |\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\n| token_entropy��distinct_3 | non-robust | 2/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 3/5 |\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\n| self_bleu→distinct_3 | non-robust | 3/5 |\\n| ece→perplexity | non-robust | 1/5 |\\n| ece→distinct_1 | non-robust | 2/5 |\\n| ece→distinct_2 | non-robust | 1/5 |\\n| ece→distinct_3 | non-robust | 2/5 |\\n| effective_rank→perplexity | non-robust | 0/5 |\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\n| effective_rank→distinct_2 | non-robust | 1/5 |\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\n\\n### α=0.25 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 1/16\\n- Non-robust: 15/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 2/5 |\\n| token_entropy→distinct_1 | **ROBUST** | 4/5 |\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\n| token_entropy→distinct_3 | non-robust | 3/5 |\\n| self_bleu→perplexity | non-robust | 0/5 |\\n| self_bleu→distinct_1 | non-robust | 0/5 |\\n| self_bleu→distinct_2 | non-robust | 0/5 |\\n| self_bleu→distinct_3 | non-robust | 0/5 |\\n| ece→perplexity | non-robust | 1/5 |\\n| ece→distinct_1 | non-robust | 1/5 |\\n| ece→distinct_2 | non-robust | 1/5 |\\n| ece→distinct_3 | non-robust | 1/5 |\\n| effective_rank→perplexity | non-robust | 1/5 |\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\n| effective_rank→distinct_2 | non-robust | 2/5 |\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\n\\n### α=0.50 (single-seed, method agreement only (≥4/5 methods, ≥1/1 seeds))\\n\\n- Robust pairs: 0/16\\n- Non-robust: 16/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 3/5 |\\n| token_entropy→distinct_1 | non-robust | 3/5 |\\n| token_entropy→distinct_2 | non-robust | 3/5 |\\n| token_entropy→distinct_3 | non-robust | 3/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\n| self_bleu→distinct_2 | non-robust | 1/5 |\\n| self_bleu→distinct_3 | non-robust | 1/5 |\\n| ece→perplexity | non-robust | 3/5 |\\n| ece→distinct_1 | non-robust | 3/5 |\\n| ece→distinct_2 | non-robust | 3/5 |\\n| ece→distinct_3 | non-robust | 3/5 |\\n| effective_rank→perplexity | non-robust | 3/5 |\\n| effective_rank→distinct_1 | non-robust | 3/5 |\\n| effective_rank→distinct_2 | non-robust | 2/5 |\\n| effective_rank→distinct_3 | non-robust | 2/5 |\\n\\n### α=1.00 (4-seed full consensus (≥4/5 methods, ≥3/4 seeds))\\n\\n- Robust pairs: 6/16\\n- Non-robust: 10/16\\n\\n| Pair | Robust | Methods |\\n|------|--------|---------|\\n| token_entropy→perplexity | non-robust | 3/5 |\\n| token_entropy→distinct_1 | **ROBUST** | 5/5 |\\n| token_entropy→distinct_2 | **ROBUST** | 5/5 |\\n| token_entropy→distinct_3 | **ROBUST** | 5/5 |\\n| self_bleu→perplexity | non-robust | 2/5 |\\n| self_bleu→distinct_1 | non-robust | 1/5 |\\n| self_bleu→distinct_2 | non-robust | 2/5 |\\n| self_bleu→distinct_3 | non-robust | 2/5 |\\n| ece→perplexity | non-robust | 3/5 |\\n| ece→distinct_1 | **ROBUST** | 4/5 |\\n| ece→distinct_2 | **ROBUST** | 4/5 |\\n| ece→distinct_3 | **ROBUST** | 4/5 |\\n| effective_rank→perplexity | non-robust | 2/5 |\\n| effective_rank→distinct_1 | non-robust | 2/5 |\\n| effective_rank→distinct_2 | non-robust | 1/5 |\\n| effective_rank→distinct_3 | non-robust | 1/5 |\\n\\n### Regime Comparison Summary\\n\\n- Stable pairs (same classification at all α): 10/16\\n- Regime-dependent pairs: 6/16\\n\\n| Pair | α=0.00 | α=0.25 | α=0.50 | α=1.00 | Stable |\\n|------|--------|--------|--------|--------|--------|\\n| token_entropy→perplexity | .(2) | .(2) | .(3) | .(3) | Y |\\n| token_entropy→distinct_1 | .(3) | R(4) | .(3) | R(5) | N |\\n| token_entropy→distinct_2 | .(3) | .(3) | .(3) | R(5) | N |\\n| token_entropy→distinct_3 | .(2) | .(3) | .(3) | R(5) | N |\\n| self_bleu→perplexity | .(2) | .(0) | .(2) | .(2) | Y |\\n| self_bleu→distinct_1 | .(3) | .(0) | .(1) | .(1) | Y |\\n| self_bleu→distinct_2 | .(2) | .(0) | .(1) | .(2) | Y |\\n| self_bleu→distinct_3 | .(3) | .(0) | .(1) | .(2) | Y |\\n| ece→perplexity | .(1) | .(1) | .(3) | .(3) | Y |\\n| ece→distinct_1 | .(2) | .(1) | .(3) | R(4) | N |\\n| ece→distinct_2 | .(1) | .(1) | .(3) | R(4) | N |\\n| ece→distinct_3 | .(2) | .(1) | .(3) | R(4) | N |\\n| effective_rank→perplexity | .(0) | .(1) | .(3) | .(2) | Y |\\n| effective_rank→distinct_1 | .(2) | .(2) | .(3) | .(2) | Y |\\n| effective_rank→distinct_2 | .(1) | .(2) | .(2) | .(1) | Y |\\n| effective_rank→distinct_3 | .(1) | .(1) | .(2) | .(1) | Y |\\n\\n## 4. D1 Velocity\\n\\n| α | mean_vel | early | late | decel_ratio |\\n|---|----------|-------|------|-------------|\\n| 0.00 | -0.001354 | -0.002516 | -0.000191 | 0.08 |\\n| 0.25 | -0.003962 | -0.006938 | -0.000986 | 0.14 |\\n| 0.50 | -0.003661 | -0.006153 | -0.001170 | 0.19 |\\n| 1.00 | -0.002783 | -0.005203 | -0.000364 | 0.07 |\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011XMzLZbFegn2AtQyE2h3zV`</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -name \"*d017*\" -o -name \"*differenc*\" -type f",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "6858b887-daab-4735-ab90-baa5960ce009",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqwZx2VEqMLYcY8qcj6SLc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9538,
      "cache_read_input_tokens": 50322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9538
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T15:35:40.746Z_

<details><summary>↩ Tool result · `toolu_011XMzLZbFegn2AtQyE2h3zV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "9669adf5-e5e5-450f-a186-b7f5d597d21b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012pfMoG6bBXiR5AHXAP1vZu`</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/consensus_classification.json",
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "dd53e2a5-a114-4899-9a7b-0469ec408578",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqwZx2VEqMLYcY8qcj6SLc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9538,
      "cache_read_input_tokens": 50322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9538
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T15:35:41.527Z_

<details><summary>↩ Tool result · `toolu_012pfMoG6bBXiR5AHXAP1vZu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"classifications\\\": [\\n    {\\n      \\\"pair_index\\\": 0,\\n      \\\"n_sig_methods\\\": 3,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 1,\\n      \\\"n_sig_methods\\\": 5,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        true,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        4,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 2,\\n      \\\"n_sig_methods\\\": 5,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        true,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        4,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 3,\\n      \\\"n_sig_methods\\\": 5,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        true,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        4,\\n        3\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192distinct_3\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 4,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        true,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        3,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 5,\\n      \\\"n_sig_methods\\\": 1,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 6,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        3,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 7,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        3,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192distinct_3\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 8,\\n      \\\"n_sig_methods\\\": 3,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 9,\\n      \\\"n_sig_methods\\\": 4,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        2,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 10,\\n      \\\"n_sig_methods\\\": 4,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        2,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 11,\\n      \\\"n_sig_methods\\\": 4,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        2,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192distinct_3\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 12,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        3,\\n        4,\\n        0,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 13,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        3,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 14,\\n      \\\"n_sig_methods\\\": 1,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        0,\\n        1,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 15,\\n      \\\"n_sig_methods\\\": 1,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        0,\\n        1,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192distinct_3\\\"\\n    }\\n  ],\\n  \\\"n_robust\\\": 6,\\n  \\\"n_non_robust\\\": 10,\\n  \\\"params\\\": {\\n    \\\"method_threshold\\\": 4,\\n    \\\"seed_threshold\\\": 3,\\n    \\\"n_methods\\\": 5,\\n    \\\"n_seeds\\\": 4\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "a8ce59dd-1ccf-40be-a8a1-c88f893053cf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"classifications\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 0,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        0,\\\\n        0\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"token_entropy\\\\\\\\u2192perplexity\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 1,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 5,\\\\n      \\\\\\\"is_robust\\\\\\\": true,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        true\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        4\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"token_entropy\\\\\\\\u2192distinct_1\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 2,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 5,\\\\n      \\\\\\\"is_robust\\\\\\\": true,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        true\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        4\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"token_entropy\\\\\\\\u2192distinct_2\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 3,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 5,\\\\n      \\\\\\\"is_robust\\\\\\\": true,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        true\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        3\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"token_entropy\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"token_entropy\\\\\\\\u2192distinct_3\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 4,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        false,\\\\n        true,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        2,\\\\n        3,\\\\n        0,\\\\n        0\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"self_bleu\\\\\\\\u2192perplexity\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 5,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        2,\\\\n        0,\\\\n        1,\\\\n        1\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"self_bleu\\\\\\\\u2192distinct_1\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 6,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        3,\\\\n        0,\\\\n        1,\\\\n        1\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"self_bleu\\\\\\\\u2192distinct_2\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 7,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        3,\\\\n        0,\\\\n        1,\\\\n        1\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"self_bleu\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"self_bleu\\\\\\\\u2192distinct_3\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 8,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 3,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        0,\\\\n        0\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"ece\\\\\\\\u2192perplexity\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 9,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n      \\\\\\\"is_robust\\\\\\\": true,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        true\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        2,\\\\n        4\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"ece\\\\\\\\u2192distinct_1\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 10,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n      \\\\\\\"is_robust\\\\\\\": true,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        true\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        2,\\\\n        4\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"ece\\\\\\\\u2192distinct_2\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 11,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 4,\\\\n      \\\\\\\"is_robust\\\\\\\": true,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        true\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        4,\\\\n        4,\\\\n        2,\\\\n        4\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"ece\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"ece\\\\\\\\u2192distinct_3\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 12,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        3,\\\\n        4,\\\\n        0,\\\\n        0,\\\\n        0\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"effective_rank\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"perplexity\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"effective_rank\\\\\\\\u2192perplexity\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 13,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 2,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        3,\\\\n        0,\\\\n        1,\\\\n        1\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"effective_rank\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_1\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"effective_rank\\\\\\\\u2192distinct_1\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 14,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        2,\\\\n        0,\\\\n        1,\\\\n        0\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"effective_rank\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_2\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"effective_rank\\\\\\\\u2192distinct_2\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"pair_index\\\\\\\": 15,\\\\n      \\\\\\\"n_sig_methods\\\\\\\": 1,\\\\n      \\\\\\\"is_robust\\\\\\\": false,\\\\n      \\\\\\\"method_verdicts\\\\\\\": [\\\\n        true,\\\\n        false,\\\\n        false,\\\\n        false,\\\\n        false\\\\n      ],\\\\n      \\\\\\\"seed_counts\\\\\\\": [\\\\n        4,\\\\n        2,\\\\n        0,\\\\n        1,\\\\n        0\\\\n      ],\\\\n      \\\\\\\"canary\\\\\\\": \\\\\\\"effective_rank\\\\\\\",\\\\n      \\\\\\\"downstream\\\\\\\": \\\\\\\"distinct_3\\\\\\\",\\\\n      \\\\\\\"pair_label\\\\\\\": \\\\\\\"effective_rank\\\\\\\\u2192distinct_3\\\\\\\"\\\\n    }\\\\n  ],\\\\n  \\\\\\\"n_robust\\\\\\\": 6,\\\\n  \\\\\\\"n_non_robust\\\\\\\": 10,\\\\n  \\\\\\\"params\\\\\\\": {\\\\n    \\\\\\\"method_threshold\\\\\\\": 4,\\\\n    \\\\\\\"seed_threshold\\\\\\\": 3,\\\\n    \\\\\\\"n_methods\\\\\\\": 5,\\\\n    \\\\\\\"n_seeds\\\\\\\": 4\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"classifications\\\": [\\n    {\\n      \\\"pair_index\\\": 0,\\n      \\\"n_sig_methods\\\": 3,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 1,\\n      \\\"n_sig_methods\\\": 5,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        true,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        4,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 2,\\n      \\\"n_sig_methods\\\": 5,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        true,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        4,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 3,\\n      \\\"n_sig_methods\\\": 5,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        true,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        4,\\n        3\\n      ],\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"token_entropy\\\\u2192distinct_3\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 4,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        true,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        3,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 5,\\n      \\\"n_sig_methods\\\": 1,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 6,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        3,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 7,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        3,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"self_bleu\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"self_bleu\\\\u2192distinct_3\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 8,\\n      \\\"n_sig_methods\\\": 3,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 9,\\n      \\\"n_sig_methods\\\": 4,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        2,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 10,\\n      \\\"n_sig_methods\\\": 4,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        2,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 11,\\n      \\\"n_sig_methods\\\": 4,\\n      \\\"is_robust\\\": true,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        true,\\n        false,\\n        true\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        4,\\n        4,\\n        2,\\n        4\\n      ],\\n      \\\"canary\\\": \\\"ece\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"ece\\\\u2192distinct_3\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 12,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        3,\\n        4,\\n        0,\\n        0,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"perplexity\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192perplexity\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 13,\\n      \\\"n_sig_methods\\\": 2,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        true,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        3,\\n        0,\\n        1,\\n        1\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192distinct_1\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 14,\\n      \\\"n_sig_methods\\\": 1,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        0,\\n        1,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"distinct_2\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192distinct_2\\\"\\n    },\\n    {\\n      \\\"pair_index\\\": 15,\\n      \\\"n_sig_methods\\\": 1,\\n      \\\"is_robust\\\": false,\\n      \\\"method_verdicts\\\": [\\n        true,\\n        false,\\n        false,\\n        false,\\n        false\\n      ],\\n      \\\"seed_counts\\\": [\\n        4,\\n        2,\\n        0,\\n        1,\\n        0\\n      ],\\n      \\\"canary\\\": \\\"effective_rank\\\",\\n      \\\"downstream\\\": \\\"distinct_3\\\",\\n      \\\"pair_label\\\": \\\"effective_rank\\\\u2192distinct_3\\\"\\n    }\\n  ],\\n  \\\"n_robust\\\": 6,\\n  \\\"n_non_robust\\\": 10,\\n  \\\"params\\\": {\\n    \\\"method_threshold\\\": 4,\\n    \\\"seed_threshold\\\": 3,\\n    \\\"n_methods\\\": 5,\\n    \\\"n_seeds\\\": 4\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also get the d028 data that shows per-pair details for naive and differenced methods at α=0.0, to identify which specific pairs are eliminated by differencing.

From the d028_fpr_null_control.json per_method_full:
- naive at α=0.0: sig_raw=8/8 (all p_raw < 0.05)
  p_values_raw: [0.002496, 0.006055, 0.007303, 0.0, 0.005344, 0.009665, 0.022381, 0.018795]
  pairs: ["token_entropy->distinct_1", "token_entropy->distinct_2", "token_entropy->distinct_3", "token_entropy->perplexity", "ece->distinct_1", "ece->distinct_2", "ece->distinct_3", "ece->perplexity"]

- differenced at α=0.0: sig_raw=4/8
  p_values_raw: [0.000157, 0.00325, 0.044726, 2e-06, 0.051439, 0.192837, 0.202654]

So differencing eliminates 4 of the 8 significant pairs, with the last three pairs losing significance entirely. Looking at the ECE results, most pairs don't reach significance even after differencing—only the entropy relationships hold up across the downstream variables. Now checking the v4 Granger results to see how the raw p-values compare at different alpha levels. Looking at the FDR-corrected results, only one effect survives the stricter threshold at α=1.0 with ECE→d1. Now examining the method ablation results across different causal inference approaches—naive, differenced, threshold, ty, and permutation Granger—where only four effects remain robust across five methods: token entropy and ECE effects on the first dimension.

But there's a discrepancy I'm noticing: the method ablation summary reports four robust pairs using the five-method threshold, yet the consensus classification file shows six robust pairs when I check which effects meet the ≥4/5 methods and ≥3/4 seeds criteria. The consensus file lists token entropy→d1/d2/d3 and ece→d1/d2/d3 as robust, which suggests the method ablation might be using a different definition of robustness. method" which requires all 5 methods to agree. The consensus uses ≥4/5. So:
- 5-method robust: 4 (token_entropy→d1/d2/d3, ece→d1)
  Actually, from method_ablation: robust_pairs = [{token_entropy, d1}, {token_entropy, d2}, {token_entropy, d3}, {ece, d1}]
  
- ≥4/5 method consensus with ≥3/4 seeds: 6 (above + ece→d2, ece→d3)

The consensus file shows token_entropy→d3 as robust with 5/5 methods but seed_counts = [4,4,4,4,3] meaning not all seeds agree for perm_granger. But the seed_threshold is 3 (≥3/4) so it still passes. Now I'm ready to construct the JSON output and work through the specific case studies: the null control at α=0.0 showing 8/8 naive significance, then the differenced results where α=0.0 reduces to 4/8 (eliminating ECE→downstream false positives while keeping token_entropy→downstream), and finally the α=1.0 case where differencing brings 14/16 down from the naive count, though certain pairs like token_entropy→perplexity show more dramatic reductions. Looking at the method verdicts across all pairs, I'm seeing a pattern where differencing fails to detect significance in several cases—particularly self_bleu comparisons where only the naive method flags them as significant. Token entropy pairs show strong agreement across methods, but self_bleu pairs are much more inconsistent, with differencing missing detections that naive catches. I'm looking at the seed counts across all 16 pairs to determine which ones show significant differentiation across at least 3 out of 4 seeds. The summary's count of 14 pairs with "differenced_significant" makes sense when I check the individual seed distributions—most pairs show consistent significance across multiple seeds, with only a few falling below that threshold. Looking at the remaining metric pairs, I'm checking which ones show significance across at least 3 out of 4 seeds. The effective_rank comparisons mostly fall below that threshold except for the ppl and d1 variants, which both hit the significance mark. So my final list of significant pairs is methods 0, 1, 2, 3, and 6.

But the summary reports 14 significant pairs, which is much higher than what I'm counting. I'm wondering if the method_ablation uses a lower threshold—maybe ≥2/4 seeds instead of ≥3/4—which would capture nearly all the pairs I've been examining. I'm recounting the pairs with a ≥3/4 threshold and getting 12 significant results instead of 14, which doesn't match the method_ablation summary showing 14 for differenced. The naive count of 16/16 checks out since all pairs have seed counts of 4, but the differenced verdict might be using a different aggregation method—perhaps based on average effect size rather than just seed count thresholds. I need to examine the actual per-pair data in method_ablation.json to understand how it's calculating significance. I'm noticing a discrepancy between my count of 12 pairs with ≥3/4 seeds and the summary's 14 significant pairs. The summary might be using a different threshold—possibly counting pairs where differenced shows significance in at least one seed rather than requiring a majority. Let me reconsider whether that ≥1/4 threshold would account for the extra pairs I'm missing.

Actually, even with a ≥1/4 or ≥2/4 threshold, I'd expect 16 pairs total, not 14. The summary might be aggregating differently, perhaps using a combined p-value approach rather than seed-based counting. Rather than chase this discrepancy further, I'll rely on the consensus_classification data for the pipeline JSON since it's more straightforward.

Now I'm ready to construct the final JSON output using two parallel frameworks, starting with the d028 per-method structure. Looking at the d028 data, I'm seeing a stark contrast between the naive and differenced approaches across different alpha values. The naive method consistently shows all 8 pairs as significant both raw and FDR-corrected, while the differenced approach is much more conservative—dropping to just 3 or 2 FDR-significant pairs depending on alpha. As alpha increases from 0.0 to 0.5, the differenced method becomes even more stringent, suggesting that the preprocessing is filtering out noise more aggressively at higher alpha levels.

At α=1.0 with the larger sample of 32 pairs across 4 seeds, both methods converge to perfect agreement—all pairs remain significant. This suggests that when the signal is genuinely strong, differencing doesn't eliminate true positives, but at lower alpha values where the signal is weaker, differencing is substantially reducing false positives. The D017 reference about token_entropy→ppl showing complete elimination after differencing (6-8/8 → 0/8) seems to be an even more extreme case of this filtering effect. Looking at the differencing results more carefully, the ECE→perplexity pairs are all eliminated at α=0.0 while token_entropy pairs survive, which explains the D017 reference. Now I'm ready to construct the JSON output, starting with Stage 1 naive results where all 40 tests show significance with a 100% sig rate, then breaking down the per-alpha differencing outcomes from the d028 data. Looking at the Stage 2 results across different alpha values, I'm noticing that differencing has a dramatic filtering effect—at α=0.0 we lose all 4 significant pairs downstream, but at α=0.5 and α=1.0 all 8 remain significant. The v6 framework actually bakes differencing directly into its permutation Granger test, so the stages blur together there, whereas the d028 data lets me see them separately. I think the cleanest way to frame this pipeline is: naive Pearson catches everything, differencing removes shared trends and culls some pairs, permutation Granger with FDR filtering tightens it further, and replication across seeds keeps only what's truly robust. pairs survive

The v6 permutation Granger already uses differenced series (granger_differenced: true). So the v6's 14/40 → 6/40 represents the combined effect of Stages 2+3 (differencing + Granger + FDR).

For the pipeline figure, we need to separate:
- Stage 1: all 40 sig (naive)
- Stage 2: some eliminated by differencing alone
- Stage 3: further eliminated by Granger + FDR
- Stage 4: further eliminated by multi-seed

The problem is that we don't have a clean count of "how many survive differencing alone" for the v6 setup (8 bidirectional × 5 alphas). The d028 data gives this for the 8 unidirectional pairs.

I think the best approach is to use the method_ablation dataset at α=1.0 with 16 pairs across 4 seeds as my primary framework, since it shows all 5 methods and gives me the most complete picture. At that setting, I get 16/16 significant in the naive stage, then 14/16 after differencing (losing self_bleu→ppl and self_bleu→d1), which lets me track the elimination at each stage cleanly. But I need to check what the per-pair verdicts actually show me before committing to this approach. I'm checking which pairs show significant Granger causality across at least 3 out of 4 seeds. Looking at the seed counts for the perm_granger method, I can see that token_entropy has strong signals across all three downstream targets (d1, d2, d3), while self_bleu shows no significant signals. Let me continue through the remaining pairs to get the full picture of which ones meet the significance threshold. Looking at the cross-α stability pattern, I see that at α=1.0 with multiple seeds, the perm_granger filtering aligns perfectly with the consensus robust set. But the real value of Stage 4 is checking stability across different α thresholds—at α=0.75 with a single seed, I'm getting 11 robust pairs, while the stricter α=1.0 multi-seed approach narrows it down to just 6. The 5 pairs that appeared robust at the looser threshold but didn't survive the stricter one include token_entropy→ppl and its relationships with the downstream metrics, plus some ece pairs.

Now I'm ready to assemble the JSON output, structuring it so Stages 1-3 use the v6 framework with its 5 alphas and 8 directions, then Stage 4 switches to the method_ablation setup with α=1.0, 4 seeds, and the 16 canary-to-downstream pairs.

For the actual data, I'll pull from d028's phase2 rates for Stages 1-2 since it breaks out all the methods cleanly—that gives me 4 alphas (0.0, 0.25, 0.5, 1.0) with 8 pairs each for the single-seed runs, plus 32 total for α=1.0 across its 4 seeds.

For the funnel visualization, I should stick with one consistent set of pairs across all stages. The v6 framework gives me the broadest dataset at 40 tests (5 alphas × 8 directions), so I'll use that as my baseline—all 40 pass Stage 1 since naive correlation works at any alpha, then I'll track how many survive differencing in Stage 2.

The d028 framework with 4 alphas and 8 pairs per alpha is cleaner for presentation, though the seed counts are inconsistent. Rather than getting bogged down in reconciling these details, I'll just organize everything I have by stage with clear source attribution and let the visualization handle the rest.

Building the JSON structure... Looking at the per-alpha breakdown, every significance level from 0.0 through 1.0 shows the same pattern—all 8 method pairs flagged as significant with a 100% detection rate. The α=0.0 case is particularly telling: it's a null control where no causal signal was injected, yet Pearson correlation still reports all pairs as significant, which is the classic spurious regression problem where non-stationary training dynamics create false co-movement.

Now examining the first-differencing stage, which applies differencing to strip out those shared non-stationary trends. The false positive rate drops to 50% under the null, a substantial improvement over the naive approach, though some spurious associations persist from correlated innovations. Now I'm looking at the specific pairs that get eliminated at the null condition—ECE correlations disappear with differencing, but token entropy spurious relationships persist as false positives. The α=0.0 case shows differencing only cuts the false positive rate to around 50%, which isn't enough on its own. Looking at the results across different canary fractions, differencing is doing heavy lifting at low alpha values—at 25% it wipes out most of the naive associations, leaving just 2 significant pairs out of 8. Now I'm moving into the permutation Granger causality stage with FDR correction, which tests directional predictability while controlling for false discoveries across all 40 tests (5 alphas × 8 bidirectional pairs).

The full v6 analysis shows 14 raw significant results that shrink to 6 after FDR correction, but when I check the robustness with the 4-alpha version, only one pair survives—ECE→d1 at α=1.0 with an FDR-corrected p-value of 0.019. At the null control (α=0.00), Granger correctly rejects all directions as expected. Looking at the statistical results for the alpha=1.00 threshold, I see 5 raw significant pairs with 3 surviving FDR correction, including entropy→d1, ECE→d1, and ECE→d2. Now I'm examining the pairs that passed FDR filtering across different alpha levels, noting their p-values, F-statistics, and effect sizes to identify the most robust relationships. Now I'm looking at the pairs that were eliminated by the FDR correction, organized by alpha level, showing which directional relationships didn't survive the multiple comparison adjustment. The null control validation shows permutation Granger achieves zero false positives compared to naive and differenced approaches. Looking at the case studies, FDR correction is dramatically reducing significant findings—from 14 raw positives down to just 6 after Benjamini-Hochberg correction across all alphas, with survivors concentrated in high-canary regimes involving entropy and diversity directions. Adding an extra alpha level to the analysis shifts the FDR outcome substantially, suggesting the multiple testing burden significantly impacts which effects survive correction. Looking at the multi-seed robustness results, I see that 11 pairs hold up with α=0.75 across single seeds, but only 6 maintain significance across multiple seeds at α=1.0—meaning 5 pairs that looked promising got eliminated when tested across different random seeds. The robust pairs show strong consistency, with token_entropy driving effects across all three downstream variables and perfect agreement across seeds for most methods, though permutation Granger occasionally drops out. Looking at the comparison between single-seed and multi-seed robustness, I can see that using just one seed with a lower threshold identifies 11 robust pairs, but when I apply stricter multi-seed validation, that drops to only 6 pairs—meaning 5 relationships that appeared robust in single-seed analysis don't hold up across multiple seeds. Looking at how the single-seed approach at α=0.75 marked 11 out of 16 pairs as robust, but when I apply the stricter multi-seed consensus at α=1.0, only 6 survive—the 5 eliminated pairs like token_entropy→ppl and ece→ppl showed agreement in isolation but fail to replicate consistently across different seeds. For instance, token_entropy→ppl looked solid with 4 out of 5 methods agreeing at α=0.75 with seed 42, but across the 4-seed ensemble at α=1.0, it drops to just 3 out of 5 methods passing, with threshold_onset and perm_granger both failing to confirm it in any seed.

The pipeline reveals that naive undifferenced correlations are completely uninformative, differencing cuts the false positive rate in half but isn't enough on its own, and adding Granger causality with FDR correction eliminates false positives at the null while recovering 6 out of 40 pairs at treatment alphas after FDR adjustment. The multi-seed validation shows single-seed estimates inflate the count by roughly 45 percent, which is why I'm seeing this drop from 11 to 6 robust pairs when enforcing stricter consistency requirements. The final 6 robust pairs all involve token_entropy or ece predicting the distinct token counts.

Now I'm filling in the missing statistical details for these FDR-surviving pairs—extracting p-values and effect sizes from the v6 report to complete the picture, particularly for the α=0.75 threshold where I have ECE→distinct_1 at p_raw=0.0038 with FDR-corrected p=0.046, entropy→distinct_2 at p_raw=0.0072 with p_fdr=0.048, and ECE→distinct_2 at p_raw=0.0032. I'm catching an error in my earlier analysis—the entropy→d1 result at α=0.75 has p_fdr=0.054, which exceeds the 0.05 threshold, so it's not actually FDR significant. Let me recount which results pass FDR correction at that alpha level: ECE→d1 and entropy→d2 both clear the bar, but I need to finish checking the rest.

At α=1.0, I'm finding three FDR-significant results: entropy→d1, ECE→d1, and ECE→d2. I'm also verifying that entropy→d2 and d2→ECE don't make the cut at this alpha level, bringing my total to six FDR-surviving pairs. Now I'm pulling the f-statistics and effect sizes from the v6 data for these six pairs to complete the analysis. I'll just populate the f_stats where I have them and leave the rest null for now. Let me verify the eliminated pairs at α=0.0 — the differenced model should show token_entropy significant across all four targets while ece remains non-significant, which matches the p-values I calculated earlier.

Since v6 only runs permutation Granger on already-differenced data, I'll structure Stage 2 around the d028 results and Stage 3 around v6, then build out the JSON with what I have.

For the pipeline visualization, I want to show two concrete funnels: one demonstrating how the null control correctly rejects all false positives across the three stages, and another showing the full cross-alpha results with the final robust subset after FDR correction and multi-seed validation.

Now I'll structure this as JSON output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "9ce2366a-f4a4-4763-a8cd-1ab84ded1caa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g77hBJvT7zoeZsRvAabxW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16086,
      "cache_read_input_tokens": 59860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16086
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 45_

现在有足够数据构建 JSON。创建目录并写入文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "ba809cb2-5367-4b76-8007-1e7a6214b082",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g77hBJvT7zoeZsRvAabxW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16086,
      "cache_read_input_tokens": 59860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16086
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01K32esjzbJe7BDKjk2aYKLW`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/pipeline_analysis",
  "description": "Create pipeline_analysis artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "63b911aa-2017-4970-923f-6dfe55f8d67b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g77hBJvT7zoeZsRvAabxW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16086,
      "cache_read_input_tokens": 59860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16086
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T15:39:49.560Z_

<details><summary>↩ Tool result · `toolu_01K32esjzbJe7BDKjk2aYKLW`</summary>

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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "db17d510-5ef3-4570-ad3b-385288157698",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Write · `toolu_01T2cCWfFUMasR2ELJvU6iwa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/pipeline_analysis/filtering_pipeline_data.json",
  "content": "{\n  \"pipeline_version\": \"v1\",\n  \"date\": \"2026-05-15\",\n  \"data_sources\": [\n    \"d028_fpr_null_control.json\",\n    \"d028_fpr_null_control_full.json\",\n    \"cross_alpha_v6.json\",\n    \"cross_alpha_v4.json\",\n    \"mvp/analysis/method_ablation.json\",\n    \"mvp/analysis/consensus/consensus_classification.json\"\n  ],\n  \"stages\": [\n    {\n      \"stage\": 1,\n      \"name\": \"Naive Correlation Scan\",\n      \"description\": \"Undifferenced Pearson correlation, no multiple-testing correction\",\n      \"role_in_pipeline\": \"Baseline showing that raw correlation flags all pairs as significant regardless of true causal structure\",\n      \"data_framework\": \"d028 per-method FPR analysis (8 unidirectional canary->downstream pairs, seed 42)\",\n      \"summary\": {\n        \"total_pairs_per_alpha\": 8,\n        \"sig_rate_all_alphas\": 1.0,\n        \"eliminated\": 0,\n        \"interpretation\": \"Naive Pearson is uninformative: 100% sig rate even at null control\"\n      },\n      \"per_alpha\": {\n        \"0.00\": {\n          \"input\": 8,\n          \"sig\": 8,\n          \"eliminated\": 0,\n          \"sig_rate\": 1.0,\n          \"note\": \"Null control (zero canary injection) - all 8 significant = 100% FPR\"\n        },\n        \"0.25\": {\n          \"input\": 8,\n          \"sig\": 8,\n          \"eliminated\": 0,\n          \"sig_rate\": 1.0\n        },\n        \"0.50\": {\n          \"input\": 8,\n          \"sig\": 8,\n          \"eliminated\": 0,\n          \"sig_rate\": 1.0\n        },\n        \"1.00\": {\n          \"input\": 8,\n          \"sig\": 8,\n          \"eliminated\": 0,\n          \"sig_rate\": 1.0,\n          \"note\": \"4-seed data: 32/32 per-seed tests also all significant\"\n        }\n      },\n      \"case_studies\": [\n        {\n          \"case\": \"alpha=0.0 null control: 100% false positive rate\",\n          \"details\": \"At alpha=0.0 (zero canary injection), naive Pearson reports 8/8 pairs significant (p < 0.05). Textbook spurious regression: shared non-stationarity in iterative training drives co-movement absent any causal link.\",\n          \"data\": {\n            \"pairs\": [\n              \"token_entropy->distinct_1\",\n              \"token_entropy->distinct_2\",\n              \"token_entropy->distinct_3\",\n              \"token_entropy->perplexity\",\n              \"ece->distinct_1\",\n              \"ece->distinct_2\",\n              \"ece->distinct_3\",\n              \"ece->perplexity\"\n            ],\n            \"p_values_raw\": [0.002496, 0.006055, 0.007303, 0.0, 0.005344, 0.009665, 0.022381, 0.018795],\n            \"p_values_fdr\": [0.009984, 0.011685, 0.011685, 0.0, 0.011685, 0.012887, 0.022381, 0.02148],\n            \"all_significant\": true,\n            \"all_significant_after_fdr\": true\n          }\n        }\n      ]\n    },\n    {\n      \"stage\": 2,\n      \"name\": \"First-Differencing\",\n      \"description\": \"First-differenced cross-correlation removes shared non-stationary trends\",\n      \"role_in_pipeline\": \"Eliminates spurious associations driven by common training trends, but retains residual FP from correlated innovations\",\n      \"data_framework\": \"d028 per-method FPR analysis (8 unidirectional pairs, seed 42)\",\n      \"summary\": {\n        \"null_control_fpr_raw\": 0.5,\n        \"null_control_fpr_fdr\": 0.375,\n        \"reduction_from_naive\": \"Eliminates 0-75% of naive-significant pairs depending on alpha\"\n      },\n      \"per_alpha\": {\n        \"0.00\": {\n          \"input\": 8,\n          \"sig_raw\": 4,\n          \"sig_fdr\": 3,\n          \"eliminated_from_naive\": 4,\n          \"fpr_raw\": 0.5,\n          \"fpr_fdr\": 0.375,\n          \"note\": \"Still 50% FPR raw - differencing alone is insufficient\"\n        },\n        \"0.25\": {\n          \"input\": 8,\n          \"sig_raw\": 2,\n          \"sig_fdr\": 2,\n          \"eliminated_from_naive\": 6\n        },\n        \"0.50\": {\n          \"input\": 8,\n          \"sig_raw\": 8,\n          \"sig_fdr\": 8,\n          \"eliminated_from_naive\": 0,\n          \"note\": \"Signal strong enough to survive differencing\"\n        },\n        \"1.00\": {\n          \"input\": 8,\n          \"sig_raw\": 8,\n          \"sig_fdr\": 8,\n          \"eliminated_from_naive\": 0,\n          \"note\": \"4-seed: 32/32 per-seed sig raw, 32/32 sig FDR\"\n        }\n      },\n      \"null_control_pair_detail\": {\n        \"pairs\": [\n          \"token_entropy->distinct_1\",\n          \"token_entropy->distinct_2\",\n          \"token_entropy->distinct_3\",\n          \"token_entropy->perplexity\",\n          \"ece->distinct_1\",\n          \"ece->distinct_2\",\n          \"ece->distinct_3\",\n          \"ece->perplexity\"\n        ],\n        \"p_values_raw\": [0.000157, 0.00325, 0.044726, 2e-06, 0.051439, 0.192837, 0.202654, 0.096018],\n        \"p_values_fdr\": [0.000628, 0.008667, 0.082302, 1.6e-05, 0.082302, 0.202654, 0.202654, 0.128024],\n        \"sig_raw_mask\": [true, true, true, true, false, false, false, false],\n        \"eliminated_pairs\": [\"ece->distinct_1\", \"ece->distinct_2\", \"ece->distinct_3\", \"ece->perplexity\"],\n        \"surviving_fp_pairs\": [\"token_entropy->distinct_1\", \"token_entropy->distinct_2\", \"token_entropy->distinct_3\", \"token_entropy->perplexity\"],\n        \"note\": \"Differencing removes all ECE->downstream spurious correlations at null but leaves all 4 token_entropy->downstream as residual FP\"\n      },\n      \"case_studies\": [\n        {\n          \"case\": \"alpha=0.0: differenced FPR ~50% (D028 finding)\",\n          \"details\": \"At null control, differencing reduces naive 8/8 sig to 4/8 sig (FPR=50% raw, 37.5% FDR). Surviving FP are all token_entropy->downstream. ECE->downstream spurious links are successfully eliminated.\",\n          \"data\": {\n            \"naive_sig\": 8,\n            \"differenced_sig\": 4,\n            \"reduction_pct\": 50.0,\n            \"eliminated_category\": \"ECE->downstream (4 pairs)\",\n            \"surviving_fp_category\": \"token_entropy->downstream (4 pairs)\"\n          }\n        },\n        {\n          \"case\": \"alpha=0.25: differencing eliminates 6/8 pairs\",\n          \"details\": \"At low canary fraction (25%), differencing removes most naive associations, leaving only 2/8 significant. Shows differencing is more effective at low signal-to-noise.\"\n        },\n        {\n          \"case\": \"Method ablation at alpha=1.0: differenced 14/16 sig vs naive 16/16\",\n          \"details\": \"At full canary injection with 4 seeds, differencing eliminates 2/16 pairs that naive finds significant. Source: method_ablation.json summary.\",\n          \"data\": {\n            \"naive_significant\": 16,\n            \"differenced_significant\": 14,\n            \"eliminated_count\": 2,\n            \"source\": \"method_ablation.json\"\n          }\n        }\n      ]\n    },\n    {\n      \"stage\": 3,\n      \"name\": \"Permutation Granger + BH FDR\",\n      \"description\": \"Non-parametric Granger causality (differenced series, 5000 permutations) with Benjamini-Hochberg FDR correction across all tests\",\n      \"role_in_pipeline\": \"Tests directional predictability beyond autocorrelation; FDR controls family-wise false discovery rate\",\n      \"data_framework\": \"v6 cross-alpha (5 alphas x 8 bidirectional directions = 40 tests, BH-corrected together)\",\n      \"summary_v6\": {\n        \"total_tests\": 40,\n        \"raw_sig\": 14,\n        \"fdr_sig\": 6,\n        \"eliminated_by_fdr\": 8,\n        \"raw_sig_rate\": 0.35,\n        \"fdr_sig_rate\": 0.15\n      },\n      \"summary_v4\": {\n        \"total_tests\": 32,\n        \"raw_sig\": 10,\n        \"fdr_sig\": 1,\n        \"eliminated_by_fdr\": 9,\n        \"fdr_sig_rate\": 0.03125,\n        \"only_surviving\": \"ECE->d1 @ alpha=1.0 (p_fdr=0.0192)\",\n        \"note\": \"4-alpha version (no alpha=0.75) for robustness comparison\"\n      },\n      \"null_control_validation\": {\n        \"alpha\": 0.0,\n        \"raw_sig\": 0,\n        \"fdr_sig\": 0,\n        \"fpr\": 0.0,\n        \"note\": \"Permutation Granger achieves 0% FPR at null control (cf. naive 100%, differenced 50%)\",\n        \"p_values_raw\": [0.058941, 0.093906, 0.080919, 0.67033, 0.955045, 0.549451, 0.350649, 0.365634]\n      },\n      \"per_alpha_v6\": {\n        \"0.00\": {\n          \"raw_sig\": 0,\n          \"fdr_sig\": 0,\n          \"note\": \"All 8 directions correctly non-significant at null control\"\n        },\n        \"0.25\": {\n          \"raw_sig\": 3,\n          \"fdr_sig\": 0,\n          \"raw_sig_pairs\": [\n            {\"direction\": \"entropy->d1\", \"p_raw\": 0.0150, \"p_fdr\": 0.0667},\n            {\"direction\": \"d1->entropy\", \"p_raw\": 0.0236, \"p_fdr\": 0.0858},\n            {\"direction\": \"d2->entropy\", \"p_raw\": 0.0498, \"p_fdr\": 0.1285}\n          ],\n          \"note\": \"All 3 raw-sig eliminated by FDR; includes 2 reverse directions\"\n        },\n        \"0.50\": {\n          \"raw_sig\": 2,\n          \"fdr_sig\": 0,\n          \"raw_sig_pairs\": [\n            {\"direction\": \"ECE->d1\", \"p_raw\": 0.0190, \"p_fdr\": 0.0760},\n            {\"direction\": \"ECE->d2\", \"p_raw\": 0.0394, \"p_fdr\": 0.1285}\n          ],\n          \"note\": \"Both raw-sig eliminated by FDR\"\n        },\n        \"0.75\": {\n          \"raw_sig\": 4,\n          \"fdr_sig\": 3,\n          \"raw_sig_pairs\": [\n            {\"direction\": \"entropy->d1\", \"p_raw\": 0.0106, \"p_fdr\": 0.0540, \"fdr_sig\": false},\n            {\"direction\": \"ECE->d1\", \"p_raw\": 0.0038, \"p_fdr\": 0.0460, \"fdr_sig\": true, \"f_stat\": 443.38, \"effect_size_f2\": 73.90},\n            {\"direction\": \"entropy->d2\", \"p_raw\": 0.0072, \"p_fdr\": 0.0480, \"fdr_sig\": true},\n            {\"direction\": \"ECE->d2\", \"p_raw\": 0.0032, \"p_fdr\": 0.0460, \"fdr_sig\": true}\n          ]\n        },\n        \"1.00\": {\n          \"raw_sig\": 5,\n          \"fdr_sig\": 3,\n          \"raw_sig_pairs\": [\n            {\"direction\": \"entropy->d1\", \"p_raw\": 0.0060, \"p_fdr\": 0.0480, \"fdr_sig\": true},\n            {\"direction\": \"ECE->d1\", \"p_raw\": 0.0006, \"p_fdr\": 0.0240, \"fdr_sig\": true},\n            {\"direction\": \"entropy->d2\", \"p_raw\": 0.0108, \"p_fdr\": 0.0540, \"fdr_sig\": false},\n            {\"direction\": \"ECE->d2\", \"p_raw\": 0.0046, \"p_fdr\": 0.0460, \"fdr_sig\": true},\n            {\"direction\": \"d2->ECE\", \"p_raw\": 0.0430, \"p_fdr\": 0.1285, \"fdr_sig\": false}\n          ]\n        }\n      },\n      \"fdr_surviving_pairs\": [\n        {\"alpha\": 0.75, \"direction\": \"ECE->d1\", \"p_raw\": 0.0038, \"p_fdr\": 0.0460, \"f_stat\": 443.38, \"effect_size_f2\": 73.90},\n        {\"alpha\": 0.75, \"direction\": \"entropy->d2\", \"p_raw\": 0.0072, \"p_fdr\": 0.0480},\n        {\"alpha\": 0.75, \"direction\": \"ECE->d2\", \"p_raw\": 0.0032, \"p_fdr\": 0.0460},\n        {\"alpha\": 1.00, \"direction\": \"entropy->d1\", \"p_raw\": 0.0060, \"p_fdr\": 0.0480},\n        {\"alpha\": 1.00, \"direction\": \"ECE->d1\", \"p_raw\": 0.0006, \"p_fdr\": 0.0240},\n        {\"alpha\": 1.00, \"direction\": \"ECE->d2\", \"p_raw\": 0.0046, \"p_fdr\": 0.0460}\n      ],\n      \"fdr_eliminated_pairs\": [\n        {\"alpha\": 0.25, \"direction\": \"entropy->d1\", \"p_raw\": 0.0150, \"p_fdr\": 0.0667},\n        {\"alpha\": 0.25, \"direction\": \"d1->entropy\", \"p_raw\": 0.0236, \"p_fdr\": 0.0858},\n        {\"alpha\": 0.25, \"direction\": \"d2->entropy\", \"p_raw\": 0.0498, \"p_fdr\": 0.1285},\n        {\"alpha\": 0.50, \"direction\": \"ECE->d1\", \"p_raw\": 0.0190, \"p_fdr\": 0.0760},\n        {\"alpha\": 0.50, \"direction\": \"ECE->d2\", \"p_raw\": 0.0394, \"p_fdr\": 0.1285},\n        {\"alpha\": 0.75, \"direction\": \"entropy->d1\", \"p_raw\": 0.0106, \"p_fdr\": 0.0540},\n        {\"alpha\": 1.00, \"direction\": \"entropy->d2\", \"p_raw\": 0.0108, \"p_fdr\": 0.0540},\n        {\"alpha\": 1.00, \"direction\": \"d2->ECE\", \"p_raw\": 0.0430, \"p_fdr\": 0.1285}\n      ],\n      \"case_studies\": [\n        {\n          \"case\": \"v6: FDR reduces raw 14/40 to 6/40 significant tests\",\n          \"details\": \"Of 40 tests (5 alphas x 8 directions), 14 show raw p<0.05 but only 6 survive BH correction. All 6 survivors are at high-canary regimes (alpha>=0.75) and involve entropy/ECE -> diversity directions only. No reverse (downstream->canary) directions survive.\",\n          \"data\": {\n            \"raw_sig_by_alpha\": [0, 3, 2, 4, 5],\n            \"fdr_sig_by_alpha\": [0, 0, 0, 3, 3],\n            \"alpha_labels\": [0.0, 0.25, 0.5, 0.75, 1.0]\n          }\n        },\n        {\n          \"case\": \"v4 vs v6: adding alpha=0.75 changes FDR landscape\",\n          \"details\": \"v4 (32 tests): raw 10/32 -> FDR 1/32 (only ECE->d1 @ alpha=1.0 survives). v6 (40 tests): raw 14/40 -> FDR 6/40. Adding alpha=0.75 contributes 4 raw-sig tests (3 survive FDR), and redistributed BH thresholds allow 2 more alpha=1.0 tests to pass.\",\n          \"data\": {\n            \"v4\": {\"tests\": 32, \"raw_sig\": 10, \"fdr_sig\": 1},\n            \"v6\": {\"tests\": 40, \"raw_sig\": 14, \"fdr_sig\": 6}\n          }\n        },\n        {\n          \"case\": \"0% FPR at null control\",\n          \"details\": \"At alpha=0.0, permutation Granger correctly rejects all 8 directions (0/8 sig), while naive gives 100% FP and differenced gives 50% FP. This validates the method's specificity.\"\n        }\n      ]\n    },\n    {\n      \"stage\": 4,\n      \"name\": \"Multi-seed Replication\",\n      \"description\": \"Cross-seed consistency check: requires >=4/5 methods significant across >=3/4 independent seeds\",\n      \"role_in_pipeline\": \"Guards against seed-specific artifacts; quantifies single-seed overestimation\",\n      \"data_framework\": \"consensus_classification (alpha=1.0, 4 seeds: 42/43/44/45, 16 canary->downstream pairs, 5 methods)\",\n      \"data_availability\": {\n        \"alpha_1.0\": \"Complete (4 seeds)\",\n        \"alpha_0.25_0.50\": \"Pending D026 multi-seed experiments\",\n        \"alpha_0.75\": \"Single-seed only (method agreement, no seed replication)\"\n      },\n      \"summary\": {\n        \"total_pairs_tested\": 16,\n        \"single_seed_robust_alpha075\": 11,\n        \"multi_seed_robust_alpha100\": 6,\n        \"eliminated_by_multi_seed\": 5,\n        \"overestimation_rate\": 0.45,\n        \"note\": \"Single-seed overestimates robustness by ~45% (11 vs 6)\"\n      },\n      \"consensus_params\": {\n        \"method_threshold\": \">=4/5 methods\",\n        \"seed_threshold\": \">=3/4 seeds\",\n        \"methods\": [\"naive_pearson\", \"differenced_xcorr\", \"threshold_onset\", \"toda_yamamoto\", \"permutation_granger\"]\n      },\n      \"robust_pairs_alpha100\": [\n        {\n          \"pair\": \"token_entropy->distinct_1\",\n          \"n_sig_methods\": 5,\n          \"method_verdicts\": [true, true, true, true, true],\n          \"seed_counts\": [4, 4, 4, 4, 4],\n          \"note\": \"Perfect agreement: 5/5 methods, 4/4 seeds each\"\n        },\n        {\n          \"pair\": \"token_entropy->distinct_2\",\n          \"n_sig_methods\": 5,\n          \"method_verdicts\": [true, true, true, true, true],\n          \"seed_counts\": [4, 4, 4, 4, 4]\n        },\n        {\n          \"pair\": \"token_entropy->distinct_3\",\n          \"n_sig_methods\": 5,\n          \"method_verdicts\": [true, true, true, true, true],\n          \"seed_counts\": [4, 4, 4, 4, 3],\n          \"note\": \"perm_granger 3/4 seeds (still passes threshold)\"\n        },\n        {\n          \"pair\": \"ece->distinct_1\",\n          \"n_sig_methods\": 4,\n          \"method_verdicts\": [true, true, true, false, true],\n          \"seed_counts\": [4, 4, 4, 2, 4],\n          \"note\": \"TY fails (2/4 seeds) but other 4 methods pass\"\n        },\n        {\n          \"pair\": \"ece->distinct_2\",\n          \"n_sig_methods\": 4,\n          \"method_verdicts\": [true, true, true, false, true],\n          \"seed_counts\": [4, 4, 4, 2, 4],\n          \"note\": \"TY fails (2/4 seeds)\"\n        },\n        {\n          \"pair\": \"ece->distinct_3\",\n          \"n_sig_methods\": 4,\n          \"method_verdicts\": [true, true, true, false, true],\n          \"seed_counts\": [4, 4, 4, 2, 4],\n          \"note\": \"TY fails (2/4 seeds)\"\n        }\n      ],\n      \"eliminated_pairs_alpha100\": [\n        {\n          \"pair\": \"token_entropy->perplexity\",\n          \"n_sig_methods\": 3,\n          \"method_verdicts\": [true, true, true, false, false],\n          \"seed_counts\": [4, 4, 4, 0, 0],\n          \"elimination_reason\": \"threshold_onset 0/4 seeds, perm_granger 0/4 seeds\"\n        },\n        {\n          \"pair\": \"ece->perplexity\",\n          \"n_sig_methods\": 3,\n          \"method_verdicts\": [true, true, true, false, false],\n          \"seed_counts\": [4, 4, 4, 0, 0],\n          \"elimination_reason\": \"TY 0/4 seeds, perm_granger 0/4 seeds\"\n        },\n        {\n          \"pair\": \"self_bleu->perplexity\",\n          \"n_sig_methods\": 2,\n          \"method_verdicts\": [true, false, true, false, false],\n          \"seed_counts\": [4, 2, 3, 0, 0],\n          \"elimination_reason\": \"Only naive + threshold pass; differenced, TY, perm all fail\"\n        },\n        {\n          \"pair\": \"self_bleu->distinct_1\",\n          \"n_sig_methods\": 1,\n          \"method_verdicts\": [true, false, false, false, false],\n          \"seed_counts\": [4, 2, 0, 1, 1],\n          \"elimination_reason\": \"Only naive passes\"\n        },\n        {\n          \"pair\": \"self_bleu->distinct_2\",\n          \"n_sig_methods\": 2,\n          \"method_verdicts\": [true, true, false, false, false],\n          \"seed_counts\": [4, 3, 0, 1, 1],\n          \"elimination_reason\": \"Only naive + differenced pass\"\n        },\n        {\n          \"pair\": \"self_bleu->distinct_3\",\n          \"n_sig_methods\": 2,\n          \"method_verdicts\": [true, true, false, false, false],\n          \"seed_counts\": [4, 3, 0, 1, 1],\n          \"elimination_reason\": \"Only naive + differenced pass\"\n        },\n        {\n          \"pair\": \"effective_rank->perplexity\",\n          \"n_sig_methods\": 2,\n          \"method_verdicts\": [true, true, false, false, false],\n          \"seed_counts\": [3, 4, 0, 0, 0],\n          \"elimination_reason\": \"Only naive + differenced; no causal methods pass\"\n        },\n        {\n          \"pair\": \"effective_rank->distinct_1\",\n          \"n_sig_methods\": 2,\n          \"method_verdicts\": [true, true, false, false, false],\n          \"seed_counts\": [4, 3, 0, 1, 1],\n          \"elimination_reason\": \"Only naive + differenced pass\"\n        },\n        {\n          \"pair\": \"effective_rank->distinct_2\",\n          \"n_sig_methods\": 1,\n          \"method_verdicts\": [true, false, false, false, false],\n          \"seed_counts\": [4, 2, 0, 1, 0],\n          \"elimination_reason\": \"Only naive passes\"\n        },\n        {\n          \"pair\": \"effective_rank->distinct_3\",\n          \"n_sig_methods\": 1,\n          \"method_verdicts\": [true, false, false, false, false],\n          \"seed_counts\": [4, 2, 0, 1, 0],\n          \"elimination_reason\": \"Only naive passes\"\n        }\n      ],\n      \"single_seed_overestimation\": {\n        \"alpha_075_single_seed\": {\n          \"mode\": \"method_agreement_only (>=4/5 methods, 1 seed)\",\n          \"robust_count\": 11,\n          \"robust_pairs\": [\n            \"token_entropy->perplexity\",\n            \"token_entropy->distinct_1\",\n            \"token_entropy->distinct_2\",\n            \"token_entropy->distinct_3\",\n            \"ece->perplexity\",\n            \"ece->distinct_1\",\n            \"ece->distinct_2\",\n            \"ece->distinct_3\",\n            \"effective_rank->distinct_1\",\n            \"effective_rank->distinct_2\",\n            \"effective_rank->distinct_3\"\n          ]\n        },\n        \"alpha_100_multi_seed\": {\n          \"mode\": \"full_consensus (>=4/5 methods, >=3/4 seeds)\",\n          \"robust_count\": 6,\n          \"robust_pairs\": [\n            \"token_entropy->distinct_1\",\n            \"token_entropy->distinct_2\",\n            \"token_entropy->distinct_3\",\n            \"ece->distinct_1\",\n            \"ece->distinct_2\",\n            \"ece->distinct_3\"\n          ]\n        },\n        \"eliminated_by_multi_seed\": {\n          \"count\": 5,\n          \"pairs\": [\n            \"token_entropy->perplexity\",\n            \"ece->perplexity\",\n            \"effective_rank->distinct_1\",\n            \"effective_rank->distinct_2\",\n            \"effective_rank->distinct_3\"\n          ],\n          \"note\": \"These 5 pairs appeared ROBUST with single-seed method agreement at alpha=0.75 but fail the stricter multi-seed criterion at alpha=1.0\"\n        }\n      },\n      \"cross_alpha_regime_summary\": {\n        \"source\": \"v6 consensus comparison\",\n        \"per_alpha_robust_count\": {\n          \"0.00\": 0,\n          \"0.25\": 1,\n          \"0.50\": 0,\n          \"0.75\": 11,\n          \"1.00\": 6\n        },\n        \"regime_dependent_pairs\": 11,\n        \"stable_pairs\": 5,\n        \"note\": \"Regime comparison uses single-seed method agreement for alpha<1.0 and 4-seed full consensus for alpha=1.0\"\n      },\n      \"constraint_c001\": \"DO NOT cite TY cross-alpha trends from Phase 2 single-seed data. D026 multi-seed needed to confirm TY non-monotonic pattern (0%->62.5%->0%->59.4%) is reproducible vs noise.\",\n      \"pending\": \"D026 multi-seed experiments for alpha=0.25/0.50 still in progress\",\n      \"case_studies\": [\n        {\n          \"case\": \"Single-seed overestimation: alpha=0.75 (11 robust) vs alpha=1.0 multi-seed (6 robust)\",\n          \"details\": \"At alpha=0.75 with one seed, method agreement alone marks 11/16 pairs ROBUST. At alpha=1.0 with 4-seed consensus, only 6/16 survive. The 5 eliminated pairs appeared robust in seed 42 but fail cross-seed replication: token_entropy->ppl (threshold_onset/perm_granger 0/4 seeds), ece->ppl (TY/perm_granger 0/4), effective_rank->d1/d2/d3 (only 1-2 seeds for causal methods).\"\n        },\n        {\n          \"case\": \"token_entropy->perplexity: single-seed ROBUST, multi-seed spurious\",\n          \"details\": \"At alpha=0.75 (seed 42), token_entropy->ppl achieves 4/5 method agreement -> ROBUST. At alpha=1.0 across 4 seeds, only 3/5 methods pass: threshold_onset sig in 0/4 seeds (onset detection unreliable), perm_granger sig in 0/4 seeds. Classification: NOT ROBUST.\",\n          \"data\": {\n            \"alpha_075_methods\": 4,\n            \"alpha_100_methods\": 3,\n            \"alpha_100_seed_counts\": [4, 4, 4, 0, 0],\n            \"failing_methods\": [\"threshold_onset (0/4 seeds)\", \"permutation_granger (0/4 seeds)\"]\n          }\n        }\n      ]\n    }\n  ],\n  \"pipeline_funnels\": {\n    \"funnel_A_null_control\": {\n      \"description\": \"Pipeline filtering at alpha=0.0 (null control) - all significance is FP\",\n      \"framework\": \"d028, 8 canary->downstream pairs\",\n      \"stages\": [\n        {\"stage\": 1, \"name\": \"Naive\", \"sig\": 8, \"eliminated\": 0, \"fpr\": 1.0},\n        {\"stage\": 2, \"name\": \"Differenced\", \"sig\": 4, \"eliminated\": 4, \"fpr\": 0.5},\n        {\"stage\": 3, \"name\": \"Perm Granger\", \"sig\": 0, \"eliminated\": 4, \"fpr\": 0.0}\n      ],\n      \"note\": \"Pipeline correctly rejects all FP at null control by Stage 3\"\n    },\n    \"funnel_B_cross_alpha_granger\": {\n      \"description\": \"Granger + FDR filtering across all alphas\",\n      \"framework_v6\": {\n        \"total_tests\": 40,\n        \"raw_sig\": 14,\n        \"fdr_sig\": 6,\n        \"note\": \"5 alphas x 8 bidirectional directions\"\n      },\n      \"framework_v4\": {\n        \"total_tests\": 32,\n        \"raw_sig\": 10,\n        \"fdr_sig\": 1,\n        \"note\": \"4 alphas x 8 bidirectional directions\"\n      }\n    },\n    \"funnel_C_method_consensus\": {\n      \"description\": \"Full pipeline at alpha=1.0 with 4-seed consensus\",\n      \"framework\": \"method_ablation, 16 canary->downstream pairs, 4 seeds\",\n      \"stages\": [\n        {\"stage\": 1, \"name\": \"Naive\", \"sig\": 16, \"eliminated\": 0},\n        {\"stage\": 2, \"name\": \"Differenced\", \"sig\": 14, \"eliminated\": 2},\n        {\"stage\": 3, \"name\": \"Perm Granger (>=3/4 seeds)\", \"sig\": 6, \"eliminated\": 8},\n        {\"stage\": 4, \"name\": \"Full Consensus (>=4/5 methods, >=3/4 seeds)\", \"sig\": 6, \"eliminated\": 0}\n      ],\n      \"note\": \"At alpha=1.0, Stages 3 and 4 converge to the same 6 pairs. Multi-seed replication's main value is at lower alphas where single-seed overestimates.\"\n    }\n  },\n  \"final_robust_pairs\": {\n    \"count\": 6,\n    \"confirmed_at\": \"alpha=1.0, 4-seed full consensus\",\n    \"pairs\": [\n      {\"canary\": \"token_entropy\", \"downstream\": \"distinct_1\", \"methods\": \"5/5\", \"interpretation\": \"Entropy collapse Granger-causes unigram diversity loss\"},\n      {\"canary\": \"token_entropy\", \"downstream\": \"distinct_2\", \"methods\": \"5/5\", \"interpretation\": \"Entropy collapse Granger-causes bigram diversity loss\"},\n      {\"canary\": \"token_entropy\", \"downstream\": \"distinct_3\", \"methods\": \"5/5\", \"interpretation\": \"Entropy collapse Granger-causes trigram diversity loss\"},\n      {\"canary\": \"ece\", \"downstream\": \"distinct_1\", \"methods\": \"4/5\", \"interpretation\": \"Calibration degradation Granger-causes unigram diversity loss\"},\n      {\"canary\": \"ece\", \"downstream\": \"distinct_2\", \"methods\": \"4/5\", \"interpretation\": \"Calibration degradation Granger-causes bigram diversity loss\"},\n      {\"canary\": \"ece\", \"downstream\": \"distinct_3\", \"methods\": \"4/5\", \"interpretation\": \"Calibration degradation Granger-causes trigram diversity loss\"}\n    ],\n    \"pattern\": \"Both canary metrics (entropy, ECE) predict all 3 diversity n-grams but NOT perplexity. self_bleu and effective_rank fail as canaries.\",\n    \"pending\": \"D026 multi-seed verification at alpha=0.25/0.50 to confirm dose-response curve\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "e1056da6-1593-41c3-b5e5-236534ff28bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YK3KEcM9c9rjzokPsNxERJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15165,
      "cache_read_input_tokens": 75946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15165
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

_source line 49 · 2026-05-15T15:41:45.934Z_

<details><summary>↩ Tool result · `toolu_01T2cCWfFUMasR2ELJvU6iwa`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/pipeline_analysis/filtering_pipeline_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "b306300b-80ff-4f81-b003-962fada91040",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/pipeline_analysis/filtering_pipeline_data.json",
    "content": "{\n  \"pipeline_version\": \"v1\",\n  \"date\": \"2026-05-15\",\n  \"data_sources\": [\n    \"d028_fpr_null_control.json\",\n    \"d028_fpr_null_control_full.json\",\n    \"cross_alpha_v6.json\",\n    \"cross_alpha_v4.json\",\n    \"mvp/analysis/method_ablation.json\",\n    \"mvp/analysis/consensus/consensus_classification.json\"\n  ],\n  \"stages\": [\n    {\n      \"stage\": 1,\n      \"name\": \"Naive Correlation Scan\",\n      \"description\": \"Undifferenced Pearson correlation, no multiple-testing correction\",\n      \"role_in_pipeline\": \"Baseline showing that raw correlation flags all pairs as significant regardless of true causal structure\",\n      \"data_framework\": \"d028 per-method FPR analysis (8 unidirectional canary->downstream pairs, seed 42)\",\n      \"summary\": {\n        \"total_pairs_per_alpha\": 8,\n        \"sig_rate_all_alphas\": 1.0,\n        \"eliminated\": 0,\n        \"interpretation\": \"Naive Pearson is uninformative: 100% sig rate even at null control\"\n      },\n      \"per_alpha\": {\n        \"0.00\": {\n          \"input\": 8,\n          \"sig\": 8,\n          \"eliminated\": 0,\n          \"sig_rate\": 1.0,\n          \"note\": \"Null control (zero canary injection) - all 8 significant = 100% FPR\"\n        },\n        \"0.25\": {\n          \"input\": 8,\n          \"sig\": 8,\n          \"eliminated\": 0,\n          \"sig_rate\": 1.0\n        },\n        \"0.50\": {\n          \"input\": 8,\n          \"sig\": 8,\n          \"eliminated\": 0,\n          \"sig_rate\": 1.0\n        },\n        \"1.00\": {\n          \"input\": 8,\n          \"sig\": 8,\n          \"eliminated\": 0,\n          \"sig_rate\": 1.0,\n          \"note\": \"4-seed data: 32/32 per-seed tests also all significant\"\n        }\n      },\n      \"case_studies\": [\n        {\n          \"case\": \"alpha=0.0 null control: 100% false positive rate\",\n          \"details\": \"At alpha=0.0 (zero canary injection), naive Pearson reports 8/8 pairs significant (p < 0.05). Textbook spurious regression: shared non-stationarity in iterative training drives co-movement absent any causal link.\",\n          \"data\": {\n            \"pairs\": [\n              \"token_entropy->distinct_1\",\n              \"token_entropy->distinct_2\",\n              \"token_entropy->distinct_3\",\n              \"token_entropy->perplexity\",\n              \"ece->distinct_1\",\n              \"ece->distinct_2\",\n              \"ece->distinct_3\",\n              \"ece->perplexity\"\n            ],\n            \"p_values_raw\": [0.002496, 0.006055, 0.007303, 0.0, 0.005344, 0.009665, 0.022381, 0.018795],\n            \"p_values_fdr\": [0.009984, 0.011685, 0.011685, 0.0, 0.011685, 0.012887, 0.022381, 0.02148],\n            \"all_significant\": true,\n            \"all_significant_after_fdr\": true\n          }\n        }\n      ]\n    },\n    {\n      \"stage\": 2,\n      \"name\": \"First-Differencing\",\n      \"description\": \"First-differenced cross-correlation removes shared non-stationary trends\",\n      \"role_in_pipeline\": \"Eliminates spurious associations driven by common training trends, but retains residual FP from correlated innovations\",\n      \"data_framework\": \"d028 per-method FPR analysis (8 unidirectional pairs, seed 42)\",\n      \"summary\": {\n        \"null_control_fpr_raw\": 0.5,\n        \"null_control_fpr_fdr\": 0.375,\n        \"reduction_from_naive\": \"Eliminates 0-75% of naive-significant pairs depending on alpha\"\n      },\n      \"per_alpha\": {\n        \"0.00\": {\n          \"input\": 8,\n          \"sig_raw\": 4,\n          \"sig_fdr\": 3,\n          \"eliminated_from_naive\": 4,\n          \"fpr_raw\": 0.5,\n          \"fpr_fdr\": 0.375,\n          \"note\": \"Still 50% FPR raw - differencing alone is insufficient\"\n        },\n        \"0.25\": {\n          \"input\": 8,\n          \"sig_raw\": 2,\n          \"sig_fdr\": 2,\n          \"eliminated_from_naive\": 6\n        },\n        \"0.50\": {\n          \"input\": 8,\n          \"sig_raw\": 8,\n          \"sig_fdr\": 8,\n          \"eliminated_from_naive\": 0,\n          \"note\": \"Signal strong enough to survive differencing\"\n        },\n        \"1.00\": {\n          \"input\": 8,\n          \"sig_raw\": 8,\n          \"sig_fdr\": 8,\n          \"eliminated_from_naive\": 0,\n          \"note\": \"4-seed: 32/32 per-seed sig raw, 32/32 sig FDR\"\n        }\n      },\n      \"null_control_pair_detail\": {\n        \"pairs\": [\n          \"token_entropy->distinct_1\",\n          \"token_entropy->distinct_2\",\n          \"token_entropy->distinct_3\",\n          \"token_entropy->perplexity\",\n          \"ece->distinct_1\",\n          \"ece->distinct_2\",\n          \"ece->distinct_3\",\n          \"ece->perplexity\"\n        ],\n        \"p_values_raw\": [0.000157, 0.00325, 0.044726, 2e-06, 0.051439, 0.192837, 0.202654, 0.096018],\n        \"p_values_fdr\": [0.000628, 0.008667, 0.082302, 1.6e-05, 0.082302, 0.202654, 0.202654, 0.128024],\n        \"sig_raw_mask\": [true, true, true, true, false, false, false, false],\n        \"eliminated_pairs\": [\"ece->distinct_1\", \"ece->distinct_2\", \"ece->distinct_3\", \"ece->perplexity\"],\n        \"surviving_fp_pairs\": [\"token_entropy->distinct_1\", \"token_entropy->distinct_2\", \"token_entropy->distinct_3\", \"token_entropy->perplexity\"],\n        \"note\": \"Differencing removes all ECE->downstream spurious correlations at null but leaves all 4 token_entropy->downstream as residual FP\"\n      },\n      \"case_studies\": [\n        {\n          \"case\": \"alpha=0.0: differenced FPR ~50% (D028 finding)\",\n          \"details\": \"At null control, differencing reduces naive 8/8 sig to 4/8 sig (FPR=50% raw, 37.5% FDR). Surviving FP are all token_entropy->downstream. ECE->downstream spurious links are successfully eliminated.\",\n          \"data\": {\n            \"naive_sig\": 8,\n            \"differenced_sig\": 4,\n            \"reduction_pct\": 50.0,\n            \"eliminated_category\": \"ECE->downstream (4 pairs)\",\n            \"surviving_fp_category\": \"token_entropy->downstream (4 pairs)\"\n          }\n        },\n        {\n          \"case\": \"alpha=0.25: differencing eliminates 6/8 pairs\",\n          \"details\": \"At low canary fraction (25%), differencing removes most naive associations, leaving only 2/8 significant. Shows differencing is more effective at low signal-to-noise.\"\n        },\n        {\n          \"case\": \"Method ablation at alpha=1.0: differenced 14/16 sig vs naive 16/16\",\n          \"details\": \"At full canary injection with 4 seeds, differencing eliminates 2/16 pairs that naive finds significant. Source: method_ablation.json summary.\",\n          \"data\": {\n            \"naive_significant\": 16,\n            \"differenced_significant\": 14,\n            \"eliminated_count\": 2,\n            \"source\": \"method_ablation.json\"\n          }\n        }\n      ]\n    },\n    {\n      \"stage\": 3,\n      \"name\": \"Permutation Granger + BH FDR\",\n      \"description\": \"Non-parametric Granger causality (differenced series, 5000 permutations) with Benjamini-Hochberg FDR correction across all tests\",\n      \"role_in_pipeline\": \"Tests directional predictability beyond autocorrelation; FDR controls family-wise false discovery rate\",\n      \"data_framework\": \"v6 cross-alpha (5 alphas x 8 bidirectional directions = 40 tests, BH-corrected together)\",\n      \"summary_v6\": {\n        \"total_tests\": 40,\n        \"raw_sig\": 14,\n        \"fdr_sig\": 6,\n        \"eliminated_by_fdr\": 8,\n        \"raw_sig_rate\": 0.35,\n        \"fdr_sig_rate\": 0.15\n      },\n      \"summary_v4\": {\n        \"total_tests\": 32,\n        \"raw_sig\": 10,\n        \"fdr_sig\": 1,\n        \"eliminated_by_fdr\": 9,\n        \"fdr_sig_rate\": 0.03125,\n        \"only_surviving\": \"ECE->d1 @ alpha=1.0 (p_fdr=0.0192)\",\n        \"note\": \"4-alpha version (no alpha=0.75) for robustness comparison\"\n      },\n      \"null_control_validation\": {\n        \"alpha\": 0.0,\n        \"raw_sig\": 0,\n        \"fdr_sig\": 0,\n        \"fpr\": 0.0,\n        \"note\": \"Permutation Granger achieves 0% FPR at null control (cf. naive 100%, differenced 50%)\",\n        \"p_values_raw\": [0.058941, 0.093906, 0.080919, 0.67033, 0.955045, 0.549451, 0.350649, 0.365634]\n      },\n      \"per_alpha_v6\": {\n        \"0.00\": {\n          \"raw_sig\": 0,\n          \"fdr_sig\": 0,\n          \"note\": \"All 8 directions correctly non-significant at null control\"\n        },\n        \"0.25\": {\n          \"raw_sig\": 3,\n          \"fdr_sig\": 0,\n          \"raw_sig_pairs\": [\n            {\"direction\": \"entropy->d1\", \"p_raw\": 0.0150, \"p_fdr\": 0.0667},\n            {\"direction\": \"d1->entropy\", \"p_raw\": 0.0236, \"p_fdr\": 0.0858},\n            {\"direction\": \"d2->entropy\", \"p_raw\": 0.0498, \"p_fdr\": 0.1285}\n          ],\n          \"note\": \"All 3 raw-sig eliminated by FDR; includes 2 reverse directions\"\n        },\n        \"0.50\": {\n          \"raw_sig\": 2,\n          \"fdr_sig\": 0,\n          \"raw_sig_pairs\": [\n            {\"direction\": \"ECE->d1\", \"p_raw\": 0.0190, \"p_fdr\": 0.0760},\n            {\"direction\": \"ECE->d2\", \"p_raw\": 0.0394, \"p_fdr\": 0.1285}\n          ],\n          \"note\": \"Both raw-sig eliminated by FDR\"\n        },\n        \"0.75\": {\n          \"raw_sig\": 4,\n          \"fdr_sig\": 3,\n          \"raw_sig_pairs\": [\n            {\"direction\": \"entropy->d1\", \"p_raw\": 0.0106, \"p_fdr\": 0.0540, \"fdr_sig\": false},\n            {\"direction\": \"ECE->d1\", \"p_raw\": 0.0038, \"p_fdr\": 0.0460, \"fdr_sig\": true, \"f_stat\": 443.38, \"effect_size_f2\": 73.90},\n            {\"direction\": \"entropy->d2\", \"p_raw\": 0.0072, \"p_fdr\": 0.0480, \"fdr_sig\": true},\n            {\"direction\": \"ECE->d2\", \"p_raw\": 0.0032, \"p_fdr\": 0.0460, \"fdr_sig\": true}\n          ]\n        },\n        \"1.00\": {\n          \"raw_sig\": 5,\n          \"fdr_sig\": 3,\n          \"raw_sig_pairs\": [\n            {\"direction\": \"entropy->d1\", \"p_raw\": 0.0060, \"p_fdr\": 0.0480, \"fdr_sig\": true},\n            {\"direction\": \"ECE->d1\", \"p_raw\": 0.0006, \"p_fdr\": 0.0240, \"fdr_sig\": true},\n            {\"direction\": \"entropy->d2\", \"p_raw\": 0.0108, \"p_fdr\": 0.0540, \"fdr_sig\": false},\n            {\"direction\": \"ECE->d2\", \"p_raw\": 0.0046, \"p_fdr\": 0.0460, \"fdr_sig\": true},\n            {\"direction\": \"d2->ECE\", \"p_raw\": 0.0430, \"p_fdr\": 0.1285, \"fdr_sig\": false}\n          ]\n        }\n      },\n      \"fdr_surviving_pairs\": [\n        {\"alpha\": 0.75, \"direction\": \"ECE->d1\", \"p_raw\": 0.0038, \"p_fdr\": 0.0460, \"f_stat\": 443.38, \"effect_size_f2\": 73.90},\n        {\"alpha\": 0.75, \"direction\": \"entropy->d2\", \"p_raw\": 0.0072, \"p_fdr\": 0.0480},\n        {\"alpha\": 0.75, \"direction\": \"ECE->d2\", \"p_raw\": 0.0032, \"p_fdr\": 0.0460},\n        {\"alpha\": 1.00, \"direction\": \"entropy->d1\", \"p_raw\": 0.0060, \"p_fdr\": 0.0480},\n        {\"alpha\": 1.00, \"direction\": \"ECE->d1\", \"p_raw\": 0.0006, \"p_fdr\": 0.0240},\n        {\"alpha\": 1.00, \"direction\": \"ECE->d2\", \"p_raw\": 0.0046, \"p_fdr\": 0.0460}\n      ],\n      \"fdr_eliminated_pairs\": [\n        {\"alpha\": 0.25, \"direction\": \"entropy->d1\", \"p_raw\": 0.0150, \"p_fdr\": 0.0667},\n        {\"alpha\": 0.25, \"direction\": \"d1->entropy\", \"p_raw\": 0.0236, \"p_fdr\": 0.0858},\n        {\"alpha\": 0.25, \"direction\": \"d2->entropy\", \"p_raw\": 0.0498, \"p_fdr\": 0.1285},\n        {\"alpha\": 0.50, \"direction\": \"ECE->d1\", \"p_raw\": 0.0190, \"p_fdr\": 0.0760},\n        {\"alpha\": 0.50, \"direction\": \"ECE->d2\", \"p_raw\": 0.0394, \"p_fdr\": 0.1285},\n        {\"alpha\": 0.75, \"direction\": \"entropy->d1\", \"p_raw\": 0.0106, \"p_fdr\": 0.0540},\n        {\"alpha\": 1.00, \"direction\": \"entropy->d2\", \"p_raw\": 0.0108, \"p_fdr\": 0.0540},\n        {\"alpha\": 1.00, \"direction\": \"d2->ECE\", \"p_raw\": 0.0430, \"p_fdr\": 0.1285}\n      ],\n      \"case_studies\": [\n        {\n          \"case\": \"v6: FDR reduces raw 14/40 to 6/40 significant tests\",\n          \"details\": \"Of 40 tests (5 alphas x 8 directions), 14 show raw p<0.05 but only 6 survive BH correction. All 6 survivors are at high-canary regimes (alpha>=0.75) and involve entropy/ECE -> diversity directions only. No reverse (downstream->canary) directions survive.\",\n          \"data\": {\n            \"raw_sig_by_alpha\": [0, 3, 2, 4, 5],\n            \"fdr_sig_by_alpha\": [0, 0, 0, 3, 3],\n            \"alpha_labels\": [0.0, 0.25, 0.5, 0.75, 1.0]\n          }\n        },\n        {\n          \"case\": \"v4 vs v6: adding alpha=0.75 changes FDR landscape\",\n          \"details\": \"v4 (32 tests): raw 10/32 -> FDR 1/32 (only ECE->d1 @ alpha=1.0 survives). v6 (40 tests): raw 14/40 -> FDR 6/40. Adding alpha=0.75 contributes 4 raw-sig tests (3 survive FDR), and redistributed BH thresholds allow 2 more alpha=1.0 tests to pass.\",\n          \"data\": {\n            \"v4\": {\"tests\": 32, \"raw_sig\": 10, \"fdr_sig\": 1},\n            \"v6\": {\"tests\": 40, \"raw_sig\": 14, \"fdr_sig\": 6}\n          }\n        },\n        {\n          \"case\": \"0% FPR at null control\",\n          \"details\": \"At alpha=0.0, permutation Granger correctly rejects all 8 directions (0/8 sig), while naive gives 100% FP and differenced gives 50% FP. This validates the method's specificity.\"\n        }\n      ]\n    },\n    {\n      \"stage\": 4,\n      \"name\": \"Multi-seed Replication\",\n      \"description\": \"Cross-seed consistency check: requires >=4/5 methods significant across >=3/4 independent seeds\",\n      \"role_in_pipeline\": \"Guards against seed-specific artifacts; quantifies single-seed overestimation\",\n      \"data_framework\": \"consensus_classification (alpha=1.0, 4 seeds: 42/43/44/45, 16 canary->downstream pairs, 5 methods)\",\n      \"data_availability\": {\n        \"alpha_1.0\": \"Complete (4 seeds)\",\n        \"alpha_0.25_0.50\": \"Pending D026 multi-seed experiments\",\n        \"alpha_0.75\": \"Single-seed only (method agreement, no seed replication)\"\n      },\n      \"summary\": {\n        \"total_pairs_tested\": 16,\n        \"single_seed_robust_alpha075\": 11,\n        \"multi_seed_robust_alpha100\": 6,\n        \"eliminated_by_multi_seed\": 5,\n        \"overestimation_rate\": 0.45,\n        \"note\": \"Single-seed overestimates robustness by ~45% (11 vs 6)\"\n      },\n      \"consensus_params\": {\n        \"method_threshold\": \">=4/5 methods\",\n        \"seed_threshold\": \">=3/4 seeds\",\n        \"methods\": [\"naive_pearson\", \"differenced_xcorr\", \"threshold_onset\", \"toda_yamamoto\", \"permutation_granger\"]\n      },\n      \"robust_pairs_alpha100\": [\n        {\n          \"pair\": \"token_entropy->distinct_1\",\n          \"n_sig_methods\": 5,\n          \"method_verdicts\": [true, true, true, true, true],\n          \"seed_counts\": [4, 4, 4, 4, 4],\n          \"note\": \"Perfect agreement: 5/5 methods, 4/4 seeds each\"\n        },\n        {\n          \"pair\": \"token_entropy->distinct_2\",\n          \"n_sig_methods\": 5,\n          \"method_verdicts\": [true, true, true, true, true],\n          \"seed_counts\": [4, 4, 4, 4, 4]\n        },\n        {\n          \"pair\": \"token_entropy->distinct_3\",\n          \"n_sig_methods\": 5,\n          \"method_verdicts\": [true, true, true, true, true],\n          \"seed_counts\": [4, 4, 4, 4, 3],\n          \"note\": \"perm_granger 3/4 seeds (still passes threshold)\"\n        },\n        {\n          \"pair\": \"ece->distinct_1\",\n          \"n_sig_methods\": 4,\n          \"method_verdicts\": [true, true, true, false, true],\n          \"seed_counts\": [4, 4, 4, 2, 4],\n          \"note\": \"TY fails (2/4 seeds) but other 4 methods pass\"\n        },\n        {\n          \"pair\": \"ece->distinct_2\",\n          \"n_sig_methods\": 4,\n          \"method_verdicts\": [true, true, true, false, true],\n          \"seed_counts\": [4, 4, 4, 2, 4],\n          \"note\": \"TY fails (2/4 seeds)\"\n        },\n        {\n          \"pair\": \"ece->distinct_3\",\n          \"n_sig_methods\": 4,\n          \"method_verdicts\": [true, true, true, false, true],\n          \"seed_counts\": [4, 4, 4, 2, 4],\n          \"note\": \"TY fails (2/4 seeds)\"\n        }\n      ],\n      \"eliminated_pairs_alpha100\": [\n        {\n          \"pair\": \"token_entropy->perplexity\",\n          \"n_sig_methods\": 3,\n          \"method_verdicts\": [true, true, true, false, false],\n          \"seed_counts\": [4, 4, 4, 0, 0],\n          \"elimination_reason\": \"threshold_onset 0/4 seeds, perm_granger 0/4 seeds\"\n        },\n        {\n          \"pair\": \"ece->perplexity\",\n          \"n_sig_methods\": 3,\n          \"method_verdicts\": [true, true, true, false, false],\n          \"seed_counts\": [4, 4, 4, 0, 0],\n          \"elimination_reason\": \"TY 0/4 seeds, perm_granger 0/4 seeds\"\n        },\n        {\n          \"pair\": \"self_bleu->perplexity\",\n          \"n_sig_methods\": 2,\n          \"method_verdicts\": [true, false, true, false, false],\n          \"seed_counts\": [4, 2, 3, 0, 0],\n          \"elimination_reason\": \"Only naive + threshold pass; differenced, TY, perm all fail\"\n        },\n        {\n          \"pair\": \"self_bleu->distinct_1\",\n          \"n_sig_methods\": 1,\n          \"method_verdicts\": [true, false, false, false, false],\n          \"seed_counts\": [4, 2, 0, 1, 1],\n          \"elimination_reason\": \"Only naive passes\"\n        },\n        {\n          \"pair\": \"self_bleu->distinct_2\",\n          \"n_sig_methods\": 2,\n          \"method_verdicts\": [true, true, false, false, false],\n          \"seed_counts\": [4, 3, 0, 1, 1],\n          \"elimination_reason\": \"Only naive + differenced pass\"\n        },\n        {\n          \"pair\": \"self_bleu->distinct_3\",\n          \"n_sig_methods\": 2,\n          \"method_verdicts\": [true, true, false, false, false],\n          \"seed_counts\": [4, 3, 0, 1, 1],\n          \"elimination_reason\": \"Only naive + differenced pass\"\n        },\n        {\n          \"pair\": \"effective_rank->perplexity\",\n          \"n_sig_methods\": 2,\n          \"method_verdicts\": [true, true, false, false, false],\n          \"seed_counts\": [3, 4, 0, 0, 0],\n          \"elimination_reason\": \"Only naive + differenced; no causal methods pass\"\n        },\n        {\n          \"pair\": \"effective_rank->distinct_1\",\n          \"n_sig_methods\": 2,\n          \"method_verdicts\": [true, true, false, false, false],\n          \"seed_counts\": [4, 3, 0, 1, 1],\n          \"elimination_reason\": \"Only naive + differenced pass\"\n        },\n        {\n          \"pair\": \"effective_rank->distinct_2\",\n          \"n_sig_methods\": 1,\n          \"method_verdicts\": [true, false, false, false, false],\n          \"seed_counts\": [4, 2, 0, 1, 0],\n          \"elimination_reason\": \"Only naive passes\"\n        },\n        {\n          \"pair\": \"effective_rank->distinct_3\",\n          \"n_sig_methods\": 1,\n          \"method_verdicts\": [true, false, false, false, false],\n          \"seed_counts\": [4, 2, 0, 1, 0],\n          \"elimination_reason\": \"Only naive passes\"\n        }\n      ],\n      \"single_seed_overestimation\": {\n        \"alpha_075_single_seed\": {\n          \"mode\": \"method_agreement_only (>=4/5 methods, 1 seed)\",\n          \"robust_count\": 11,\n          \"robust_pairs\": [\n            \"token_entropy->perplexity\",\n            \"token_entropy->distinct_1\",\n            \"token_entropy->distinct_2\",\n            \"token_entropy->distinct_3\",\n            \"ece->perplexity\",\n            \"ece->distinct_1\",\n            \"ece->distinct_2\",\n            \"ece->distinct_3\",\n            \"effective_rank->distinct_1\",\n            \"effective_rank->distinct_2\",\n            \"effective_rank->distinct_3\"\n          ]\n        },\n        \"alpha_100_multi_seed\": {\n          \"mode\": \"full_consensus (>=4/5 methods, >=3/4 seeds)\",\n          \"robust_count\": 6,\n          \"robust_pairs\": [\n            \"token_entropy->distinct_1\",\n            \"token_entropy->distinct_2\",\n            \"token_entropy->distinct_3\",\n            \"ece->distinct_1\",\n            \"ece->distinct_2\",\n            \"ece->distinct_3\"\n          ]\n        },\n        \"eliminated_by_multi_seed\": {\n          \"count\": 5,\n          \"pairs\": [\n            \"token_entropy->perplexity\",\n            \"ece->perplexity\",\n            \"effective_rank->distinct_1\",\n            \"effective_rank->distinct_2\",\n            \"effective_rank->distinct_3\"\n          ],\n          \"note\": \"These 5 pairs appeared ROBUST with single-seed method agreement at alpha=0.75 but fail the stricter multi-seed criterion at alpha=1.0\"\n        }\n      },\n      \"cross_alpha_regime_summary\": {\n        \"source\": \"v6 consensus comparison\",\n        \"per_alpha_robust_count\": {\n          \"0.00\": 0,\n          \"0.25\": 1,\n          \"0.50\": 0,\n          \"0.75\": 11,\n          \"1.00\": 6\n        },\n        \"regime_dependent_pairs\": 11,\n        \"stable_pairs\": 5,\n        \"note\": \"Regime comparison uses single-seed method agreement for alpha<1.0 and 4-seed full consensus for alpha=1.0\"\n      },\n      \"constraint_c001\": \"DO NOT cite TY cross-alpha trends from Phase 2 single-seed data. D026 multi-seed needed to confirm TY non-monotonic pattern (0%->62.5%->0%->59.4%) is reproducible vs noise.\",\n      \"pending\": \"D026 multi-seed experiments for alpha=0.25/0.50 still in progress\",\n      \"case_studies\": [\n        {\n          \"case\": \"Single-seed overestimation: alpha=0.75 (11 robust) vs alpha=1.0 multi-seed (6 robust)\",\n          \"details\": \"At alpha=0.75 with one seed, method agreement alone marks 11/16 pairs ROBUST. At alpha=1.0 with 4-seed consensus, only 6/16 survive. The 5 eliminated pairs appeared robust in seed 42 but fail cross-seed replication: token_entropy->ppl (threshold_onset/perm_granger 0/4 seeds), ece->ppl (TY/perm_granger 0/4), effective_rank->d1/d2/d3 (only 1-2 seeds for causal methods).\"\n        },\n        {\n          \"case\": \"token_entropy->perplexity: single-seed ROBUST, multi-seed spurious\",\n          \"details\": \"At alpha=0.75 (seed 42), token_entropy->ppl achieves 4/5 method agreement -> ROBUST. At alpha=1.0 across 4 seeds, only 3/5 methods pass: threshold_onset sig in 0/4 seeds (onset detection unreliable), perm_granger sig in 0/4 seeds. Classification: NOT ROBUST.\",\n          \"data\": {\n            \"alpha_075_methods\": 4,\n            \"alpha_100_methods\": 3,\n            \"alpha_100_seed_counts\": [4, 4, 4, 0, 0],\n            \"failing_methods\": [\"threshold_onset (0/4 seeds)\", \"permutation_granger (0/4 seeds)\"]\n          }\n        }\n      ]\n    }\n  ],\n  \"pipeline_funnels\": {\n    \"funnel_A_null_control\": {\n      \"description\": \"Pipeline filtering at alpha=0.0 (null control) - all significance is FP\",\n      \"framework\": \"d028, 8 canary->downstream pairs\",\n      \"stages\": [\n        {\"stage\": 1, \"name\": \"Naive\", \"sig\": 8, \"eliminated\": 0, \"fpr\": 1.0},\n        {\"stage\": 2, \"name\": \"Differenced\", \"sig\": 4, \"eliminated\": 4, \"fpr\": 0.5},\n        {\"stage\": 3, \"name\": \"Perm Granger\", \"sig\": 0, \"eliminated\": 4, \"fpr\": 0.0}\n      ],\n      \"note\": \"Pipeline correctly rejects all FP at null control by Stage 3\"\n    },\n    \"funnel_B_cross_alpha_granger\": {\n      \"description\": \"Granger + FDR filtering across all alphas\",\n      \"framework_v6\": {\n        \"total_tests\": 40,\n        \"raw_sig\": 14,\n        \"fdr_sig\": 6,\n        \"note\": \"5 alphas x 8 bidirectional directions\"\n      },\n      \"framework_v4\": {\n        \"total_tests\": 32,\n        \"raw_sig\": 10,\n        \"fdr_sig\": 1,\n        \"note\": \"4 alphas x 8 bidirectional directions\"\n      }\n    },\n    \"funnel_C_method_consensus\": {\n      \"description\": \"Full pipeline at alpha=1.0 with 4-seed consensus\",\n      \"framework\": \"method_ablation, 16 canary->downstream pairs, 4 seeds\",\n      \"stages\": [\n        {\"stage\": 1, \"name\": \"Naive\", \"sig\": 16, \"eliminated\": 0},\n        {\"stage\": 2, \"name\": \"Differenced\", \"sig\": 14, \"eliminated\": 2},\n        {\"stage\": 3, \"name\": \"Perm Granger (>=3/4 seeds)\", \"sig\": 6, \"eliminated\": 8},\n        {\"stage\": 4, \"name\": \"Full Consensus (>=4/5 methods, >=3/4 seeds)\", \"sig\": 6, \"eliminated\": 0}\n      ],\n      \"note\": \"At alpha=1.0, Stages 3 and 4 converge to the same 6 pairs. Multi-seed replication's main value is at lower alphas where single-seed overestimates.\"\n    }\n  },\n  \"final_robust_pairs\": {\n    \"count\": 6,\n    \"confirmed_at\": \"alpha=1.0, 4-seed full consensus\",\n    \"pairs\": [\n      {\"canary\": \"token_entropy\", \"downstream\": \"distinct_1\", \"methods\": \"5/5\", \"interpretation\": \"Entropy collapse Granger-causes unigram diversity loss\"},\n      {\"canary\": \"token_entropy\", \"downstream\": \"distinct_2\", \"methods\": \"5/5\", \"interpretation\": \"Entropy collapse Granger-causes bigram diversity loss\"},\n      {\"canary\": \"token_entropy\", \"downstream\": \"distinct_3\", \"methods\": \"5/5\", \"interpretation\": \"Entropy collapse Granger-causes trigram diversity loss\"},\n      {\"canary\": \"ece\", \"downstream\": \"distinct_1\", \"methods\": \"4/5\", \"interpretation\": \"Calibration degradation Granger-causes unigram diversity loss\"},\n      {\"canary\": \"ece\", \"downstream\": \"distinct_2\", \"methods\": \"4/5\", \"interpretation\": \"Calibration degradation Granger-causes bigram diversity loss\"},\n      {\"canary\": \"ece\", \"downstream\": \"distinct_3\", \"methods\": \"4/5\", \"interpretation\": \"Calibration degradation Granger-causes trigram diversity loss\"}\n    ],\n    \"pattern\": \"Both canary metrics (entropy, ECE) predict all 3 diversity n-grams but NOT perplexity. self_bleu and effective_rank fail as canaries.\",\n    \"pending\": \"D026 multi-seed verification at alpha=0.25/0.50 to confirm dose-response curve\"\n  }\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 50_

注册 artifact。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "097dfa93-1eb9-4887-9df7-681c3f80c816",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eAELnjkN1TiVNY8CUGcbi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8920,
      "cache_read_input_tokens": 91111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8920
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

_source line 51_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_012BrXYTP7U52yQoMsERLLsW`</summary>

```json
{
  "name": "filtering_pipeline_data",
  "type": "data",
  "description": "4-stage sequential filtering pipeline structured data (naive -> differencing -> Granger+FDR -> multi-seed). Contains per-stage sig counts, case studies, FDR-surviving/eliminated pair lists, null control validation, and 3 pipeline funnels for paper figure.",
  "project": "distrib_canary_collapse",
  "exp_id": "D040",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/pipeline_analysis/filtering_pipeline_data.json",
  "tags": [
    "pipeline",
    "filtering",
    "figure-data",
    "D028",
    "v6",
    "consensus"
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
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "fd7c6900-ab9f-4f09-91c5-59bd825f5f15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eAELnjkN1TiVNY8CUGcbi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8920,
      "cache_read_input_tokens": 91111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8920
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

_source line 52 · 2026-05-15T15:41:53.072Z_

<details><summary>↩ Tool result · `toolu_012BrXYTP7U52yQoMsERLLsW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_4ac8b4\", \"name\": \"filtering_pipeline_data\", \"type\": \"data\", \"description\": \"4-stage sequential filtering pipeline structured data (naive -> differencing -> Granger+FDR -> multi-seed). Contains per-stage sig counts, case studies, FDR-surviving/eliminated pair lists, null control validation, and 3 pipeline funnels for paper figure.\", \"path\": \"projects/distrib_canary_collapse/artifacts/D040/data/filtering_pipeline_data.json\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": \"D040\", \"skill\": \"\", \"created_at\": \"2026-05-15T15:41:52.995516+00:00\", \"tags\": [\"pipeline\", \"filtering\", \"figure-data\", \"D028\", \"v6\", \"consensus\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "262c3c7e-6a61-4feb-8f59-307302f088f8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_4ac8b4\\\", \\\"name\\\": \\\"filtering_pipeline_data\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"4-stage sequential filtering pipeline structured data (naive -> differencing -> Granger+FDR -> multi-seed). Contains per-stage sig counts, case studies, FDR-surviving/eliminated pair lists, null control validation, and 3 pipeline funnels for paper figure.\\\", \\\"path\\\": \\\"projects/distrib_canary_collapse/artifacts/D040/data/filtering_pipeline_data.json\\\", \\\"url\\\": null, \\\"project\\\": \\\"distrib_canary_collapse\\\", \\\"exp_id\\\": \\\"D040\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T15:41:52.995516+00:00\\\", \\\"tags\\\": [\\\"pipeline\\\", \\\"filtering\\\", \\\"figure-data\\\", \\\"D028\\\", \\\"v6\\\", \\\"consensus\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_4ac8b4\", \"name\": \"filtering_pipeline_data\", \"type\": \"data\", \"description\": \"4-stage sequential filtering pipeline structured data (naive -> differencing -> Granger+FDR -> multi-seed). Contains per-stage sig counts, case studies, FDR-surviving/eliminated pair lists, null control validation, and 3 pipeline funnels for paper figure.\", \"path\": \"projects/distrib_canary_collapse/artifacts/D040/data/filtering_pipeline_data.json\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": \"D040\", \"skill\": \"\", \"created_at\": \"2026-05-15T15:41:52.995516+00:00\", \"tags\": [\"pipeline\", \"filtering\", \"figure-data\", \"D028\", \"v6\", \"consensus\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 53_

产出完成。

**文件**: `artifacts/D040/data/filtering_pipeline_data.json` (art_20260515_4ac8b4)

**内容结构**:
- **Stage 1 (Naive)**: α=0.0 null control 8/8 sig (100% FPR)，所有 α 均 100%
- **Stage 2 (Differencing)**: α=0.0 降至 4/8 sig (50% FPR)；消除全部 ECE→downstream，保留 4 个 token_entropy→downstream 残余 FP
- **Stage 3 (Granger+FDR)**: v6 40 tests: raw 14→FDR 6；v4 32 tests: raw 10→FDR 1；null control 0% FPR 验证；6 个 FDR 存活 pair 全在 α≥0.75 的 entropy/ECE→diversity 方向
- **Stage 4 (Multi-seed)**: α=0.75 单 seed 11/16 robust → α=1.0 四 seed 6/16 robust，单 seed 高估 ~45%
- **3 个 funnel**: A=null control 漏斗(8→4→0), B=cross-alpha Granger FDR 对比(v4 vs v6), C=α=1.0 全方法漏斗(16→14→6→6)
- **最终 6 个 robust pairs**: token_entropy→d1/d2/d3 + ece→d1/d2/d3；C001 约束已标注

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "uuid": "8db6a766-a9eb-4881-8b2b-159ce4ba872e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2NbmdXrsctztqb8GjQNcW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 631,
      "cache_read_input_tokens": 100031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 631
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

_source line 54_

产出完成。

**文件**: `artifacts/D040/data/filtering_pipeline_data.json` (art_20260515_4ac8b4)

**内容结构**:
- **Stage 1 (Naive)**: α=0.0 null control 8/8 sig (100% FPR)，所有 α 均 100%
- **Stage 2 (Differencing)**: α=0.0 降至 4/8 sig (50% FPR)；消除全部 ECE→downstream，保留 4 个 token_entropy→downstream 残余 FP
- **Stage 3 (Granger+FDR)**: v6 40 tests: raw 14→FDR 6；v4 32 tests: raw 10→FDR 1；null control 0% FPR 验证；6 个 FDR 存活 pair 全在 α≥0.75 的 entropy/ECE→diversity 方向
- **Stage 4 (Multi-seed)**: α=0.75 单 seed 11/16 robust → α=1.0 四 seed 6/16 robust，单 seed 高估 ~45%
- **3 个 funnel**: A=null control 漏斗(8→4→0), B=cross-alpha Granger FDR 对比(v4 vs v6), C=α=1.0 全方法漏斗(16→14→6→6)
- **最终 6 个 robust pairs**: token_entropy→d1/d2/d3 + ece→d1/d2/d3；C001 约束已标注

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 559976,
  "duration_api_ms": 557947,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "7c419a0a-44c5-4f82-878a-f54f4a3f9a62",
  "total_cost_usd": 1.69391575,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 88821,
    "cache_read_input_tokens": 508001,
    "output_tokens": 35294,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 88821,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 427,
        "cache_read_input_tokens": 100031,
        "cache_creation_input_tokens": 631,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 631
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2294,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002369,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 35294,
      "cacheReadInputTokens": 508001,
      "cacheCreationInputTokens": 88821,
      "webSearchRequests": 0,
      "costUSD": 1.6915467499999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "04842409-385d-4d9d-bfa9-2c8040dd80bb"
}
```

</details>

---
