# research hopper contingency

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_research_hopper-contingency_20260529T082428.log`
- **Structured JSON:** [`18792f6bb1bdd3a4a18d.json`](../../sessions/18/18792f6bb1bdd3a4a18d.json)

## Before a recorded user message

33 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
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
  "uuid": "7a734ed6-dd08-492e-9694-fcdbd3cd1d9d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1780059600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "737a18b5-50f9-47dc-92ef-31b8e8d07c93",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this task into parallel steps:

1. Read the project code to check Hopper support
2. Read the registry for hopper-related experiments
3. Check the codebase for DMC task configurations

Let me start by reading relevant files and the registry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "6a8fa58d-df52-4bb8-87fe-8d19ccd21d49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dcwbwj81njRFcZ4QcQXgst",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12461,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12461
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

_source line 5_

开始调研 Hopper 环境可行性。先并行读取代码配置和实验 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "5579773b-2613-4be2-af03-46cc9a3c4d3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dcwbwj81njRFcZ4QcQXgst",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12461,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12461
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016HhEBzBuyGn6JvgA49fxWf`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "15dd6d9f-1bac-4d1b-84a6-02c938766c60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dcwbwj81njRFcZ4QcQXgst",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12461,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12461
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

_source line 7 · 2026-05-29T08:24:45.176Z_

<details><summary>↩ Tool result · `toolu_016HhEBzBuyGn6JvgA49fxWf`</summary>

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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "0aa8674f-7d9b-4096-afc3-3693f606b854",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
Now let me run parallel queries: read the registry for hopper experiments, check the dreamer.py config, and look at DMC task configs on the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "ea099522-4a56-4617-8a6f-0bf8bddd4179",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Xu7gR714JvkSkxH41LSBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2090,
      "cache_read_input_tokens": 23912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2090
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LBkywCsiBvASYARjhFEUAy`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "filters": {
    "status": "KILLED"
  },
  "fields": [
    "*"
  ],
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "4b0e4f07-e021-4681-9e0a-1ee9e897a213",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Xu7gR714JvkSkxH41LSBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2090,
      "cache_read_input_tokens": 23912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2090
      },
      "output_tokens": 17,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-29T08:25:11.065Z_

<details><summary>↩ Tool result · `toolu_01LBkywCsiBvASYARjhFEUAy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8168}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "e966ab4e-a6e7-452b-9ec3-5259d865d841",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8168}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8168}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NPpNHByRHZYa1Ax9MbR8hz`</summary>

```json
{
  "server": "westd-51268",
  "command": "grep -n -i \"hopper\" /root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "2e8d318b-ad32-4238-b06c-cca8e6f31b0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Xu7gR714JvkSkxH41LSBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2090,
      "cache_read_input_tokens": 23912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2090
      },
      "output_tokens": 17,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-29T08:25:20.579Z_

<details><summary>↩ Tool result · `toolu_01NPpNHByRHZYa1Ax9MbR8hz`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.14}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "90d2ad6b-9e91-4b4c-93c8-8f6b48279fc1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.14}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.14}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015XWGYsaYJwRWEA2iggavSz`</summary>

```json
{
  "server": "westd-51268",
  "command": "grep -rn -i \"hopper\" /root/autodl-tmp/event-gated-adaptive-horizon/configs.yaml",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "d466cc04-2301-4bb8-99fa-61a76b9f41b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Xu7gR714JvkSkxH41LSBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2090,
      "cache_read_input_tokens": 23912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2090
      },
      "output_tokens": 17,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-29T08:25:26.904Z_

<details><summary>↩ Tool result · `toolu_015XWGYsaYJwRWEA2iggavSz`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "78ed7cf3-3fb3-4ce5-8b62-2445b60e8ccc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Nkpm9a7DARaiUjdPU1gP5X`</summary>

```json
{
  "server": "westd-51268",
  "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/*.py /root/autodl-tmp/event-gated-adaptive-horizon/*.yaml",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "79e3af20-a811-484c-b08f-3eaeca9b5f12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Xu7gR714JvkSkxH41LSBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2090,
      "cache_read_input_tokens": 23912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2090
      },
      "output_tokens": 17,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-29T08:25:34.128Z_

<details><summary>↩ Tool result · `toolu_01Nkpm9a7DARaiUjdPU1gP5X`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/event-gated-adaptive-horizon/analyze_hopper_nve.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/analyze_rssm_fidelity_v2.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/analyze_rssm_standardized.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/checkpoint_monitor.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/configs.yaml\\n/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/eval_mvp.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/exploration.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/extract_paper_data.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/models.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/networks.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/nve_audit.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/nve_audit_v2.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/nve_roc_prf_plots.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/nve_threshold_analysis.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/parallel.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/plot_dt_cosine.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/print_detail.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/print_summary.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/tools.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/validate_detector.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/value_distribution_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "1aa25e63-ae6e-468f-b084-d561513fdbda",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/analyze_hopper_nve.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/analyze_rssm_fidelity_v2.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/analyze_rssm_standardized.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/checkpoint_monitor.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/configs.yaml\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/eval_mvp.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/exploration.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/extract_paper_data.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/models.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/networks.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/nve_audit.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/nve_audit_v2.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/nve_roc_prf_plots.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/nve_threshold_analysis.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/parallel.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/plot_dt_cosine.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/print_detail.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/print_summary.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/tools.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/validate_detector.py\\\\n/root/autodl-tmp/event-gated-adaptive-horizon/value_distribution_analysis.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/event-gated-adaptive-horizon/analyze_hopper_nve.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/analyze_rssm_fidelity_v2.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/analyze_rssm_standardized.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/checkpoint_monitor.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/configs.yaml\\n/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/eval_mvp.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/exploration.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/extract_paper_data.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/models.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/networks.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/nve_audit.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/nve_audit_v2.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/nve_roc_prf_plots.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/nve_threshold_analysis.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/parallel.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/plot_dt_cosine.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/print_detail.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/print_summary.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/tools.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/validate_detector.py\\n/root/autodl-tmp/event-gated-adaptive-horizon/value_distribution_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
No "hopper" in dreamer.py or configs.yaml directly. But there's an `analyze_hopper_nve.py` file. Let me search more broadly - check the configs.yaml for task definitions, check dreamer.py for how tasks are parsed, and look at the registry more broadly for hopper experiments (they might not be KILLED status).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "d275b502-33be-4d93-ad18-575b1a6bdcf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N61FfHYMLVFk2GSd8jY8aC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 26002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1497
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 18_

dreamer.py 和 configs.yaml 中没有直接匹配 "hopper"。继续深入检查 task 配置和 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "d4d4a78e-45ca-4b7c-bc4d-a19cc2eb5ed1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N61FfHYMLVFk2GSd8jY8aC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 26002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1497
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BbbSgoZbgLG6Htn7cYdWMQ`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "fields": [
    "*"
  ],
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "20fc7994-be27-488b-b284-3e3c2361209a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N61FfHYMLVFk2GSd8jY8aC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 26002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1497
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LP9L7p8BACE3vzMzNXsBMP`</summary>

```json
{
  "server": "westd-51268",
  "command": "grep -n \"task\" /root/autodl-tmp/event-gated-adaptive-horizon/configs.yaml",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "a7561fcc-39c9-487f-95a4-6f0839975dd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N61FfHYMLVFk2GSd8jY8aC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 26002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1497
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-29T08:25:42.311Z_

<details><summary>↩ Tool result · `toolu_01BbbSgoZbgLG6Htn7cYdWMQ`</summary>

```text
Error: result (465,377 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "8b64f5da-f999-4d24-a876-e17ba0f05707",
  "tool_use_result": {
    "content": "Error: result (465,377 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_quadruped_008d_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-28T22:36:53.813Z\", \"updated_at\": \"2026-05-29T08:24:04.434Z\", \"hypothesis\": \"Quadruped Walk trained dt_emb + gate + subsample ON (008d config: gate_fixed_dt=2, gate_subsample_max_dt=2, H=8), seed=0 — tests whether CIVO onset generalizes to 12-DoF four-legged morphology distinct from Walker/Cheetah single-spine. Expect NVE > 2.0× if CIVO is morphology-independent. Source: post-D171 scope expansion.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_quadruped_walk --logdir logdir/exp_quadruped_008d_s0 --steps 200000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:0\"], \"data_path\": \"dmc_quadruped_walk\", \"data_count\": 200000, \"model_name\": \"DreamerV3-S + gate+dt_emb (008d config)\", \"seed\": 0}, \"notes\": \"Cancelled per D180: quadruped baseline unhealthy (NVE@125K=6.6×, far above τ=2.0×). No clean baseline → 008d experiment meaningless for CIVO isolation.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-29T08:24:01.470Z\"}, \"exp_walker_no_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T10:52:53.227Z\", \"updated_at\": \"2026-05-29T08:05:33.057Z\", \"hypothesis\": \"dt_embed_dim=0 + gate+subsample ON in Walker Walk seed 0 will NOT show CIVO (NVE<1.5), replicating 008f causal control. This confirms removing dt_embedding prevents CIVO, strengthening C2 (trained dt_emb is necessary condition). Source: D164 Walker priority, replaces killed exp_009f.\", \"conclusion\": \"killed\", \"spec\": {\"server\": \"westd-51268\", \"gpu\": \"cuda:0\"}, \"completed_at\": \"2026-05-29T08:05:33.057Z\"}, \"exp_humanoid_008d_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-28T22:36:50.115Z\", \"updated_at\": \"2026-05-29T04:58:53.836Z\", \"hypothesis\": \"Humanoid Walk trained dt_emb + gate + subsample ON (008d config: gate_fixed_dt=2, gate_subsample_max_dt=2, H=8), seed=0 — tests whether CIVO onset generalizes to highest-DoF (21) DMC locomotion environment. Expect NVE > 2.0× if CIVO is DoF-independent. Source: post-D171 scope expansion.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-29T04:58:50.878Z\", \"notes\": \"Cancelled per D177: humanoid baseline itself is CIVO-prone (NVE=12.97×), making Humanoid unsuitable as clean CIVO isolation environment. No point running 008d on an already-overestimating baseline.\"}, \"exp_quadruped_baseline_s0_r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T23:59:44.619Z\", \"updated_at\": \"2026-05-29T04:58:07.847Z\", \"hypothesis\": \"Quadruped Walk baseline (dt=1, no gate) establishes reference performance for 12-DoF four-legged environment CIVO verification. Expect stable training without value overestimation (NVE < 2.0×). Retry of exp_quadruped_baseline_s0 (failed: EGL device 1 not available). Source: post-D171 scope expansion.\", \"parent\": \"exp_quadruped_baseline_s0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_quadruped_walk --logdir logdir/exp_quadruped_baseline_s0_r2 --steps 200000 --seed 0 --compile False --device cuda:0\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:0\"], \"pid\": \"42263\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_quadruped_baseline_s0_r2.log\", \"submitted_at\": \"2026-05-29T04:58:05.166Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-29T04:58:01.791Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_quadruped_walk --logdir logdir/exp_quadruped_baseline_s0_r2 --steps 200000 --seed 0 --compile False --device cuda:0\\\"\"}, \"pid\": \"42263\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_quadruped_baseline_s0_r2.log\"}, \"exp_humanoid_baseline_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-28T22:36:46.382Z\", \"updated_at\": \"2026-05-29T04:39:10.761Z\", \"hypothesis\": \"Humanoid Walk baseline (dt=1, no gate) establishes reference performance for 21-DoF environment CIVO verification. Expect stable training without value overestimation (NVE < 2.0×). Source: post-D171 scope expansion.\", \"spec\": {\"data_path\": \"dmc_humanoid_walk\", \"data_count\": 200000, \"model_name\": \"DreamerV3-S (baseline, no gate)\", \"seed\": 0, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_humanoid_walk --logdir logdir/exp_humanoid_baseline_s0 --steps 200000 --seed 0 --compile False --device cuda:0\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:0\"], \"pid\": \"25955\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_humanoid_baseline_s0.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-29T04:29:59.886Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-29T04:30:07.659100+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"eval_return_final_mean\": 1.48, \"eval_return_final_std\": 0.36, \"eval_return_best\": 2.16, \"nve_max\": 12.97, \"nve_max_step\": 105000, \"nve_mean_35k_plus\": 7.64, \"ve_ratio_final\": 12.22, \"value_mean_final\": 15.18, \"value_mean_max\": 15.18, \"actor_entropy_final\": -17.83, \"civo_alerts\": 3, \"civo_alert_steps\": [55000, 105000, 195000], \"total_steps\": 212000, \"train_return_final_mean\": 1.73}, \"checkpoint_path\": \"logdir/exp_humanoid_baseline_s0/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_humanoid_baseline_s0.log\", \"completed_at\": \"2026-05-29T04:39:10.761Z\"}, \"exp_walker_no_dt_emb_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T11:13:09.544Z\", \"updated_at\": \"2026-05-29T00:52:32.414Z\", \"hypothesis\": \"Removing dt_embedding (gate_dt_embed_dim=0) prevents CIVO triggering by eliminating the gate's ability to condition on temporal position, forcing conservative horizon selection\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"kill -9 628808 2>/dev/null; sleep 2; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:0\"], \"pid\": \"629189\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_walker_no_dt_emb_s1\", \"submitted_at\": \"2026-05-27T11:17:56.923Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_walker_no_dt_emb_s1\", \"wall_clock_seconds\": 11041.0, \"gpu_hours\": 3.07}, \"pid\": \"629189\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_walker_no_dt_emb_s1.log\", \"reproduce\": {\"command\": \"bash -c \\\"kill -9 628808 2>/dev/null; sleep 2; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T14:21:57.960Z\", \"metrics\": {\"eval_return_105K\": 468.83, \"NVE_105K\": 0.88, \"ve_ratio_105K\": 0.23, \"civo_alert\": 0, \"nve_classification\": \"no_civo\", \"civo\": false, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1}}, \"exp_quadruped_baseline_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-28T22:36:51.697Z\", \"updated_at\": \"2026-05-28T22:58:50.243Z\", \"hypothesis\": \"Quadruped Walk baseline (dt=1, no gate) establishes reference performance for 12-DoF four-legged environment CIVO verification. Expect stable training without value overestimation (NVE < 2.0×). Source: post-D171 scope expansion.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_quadruped_walk --logdir logdir/exp_quadruped_baseline_s0 --steps 200000 --seed 0 --compile False --device cuda:0\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:1\"], \"pid\": \"27003\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_quadruped_baseline_s0.log\", \"submitted_at\": \"2026-05-28T22:56:45.292Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_quadruped_walk\", \"data_count\": 200000, \"model_name\": \"DreamerV3-S (baseline, no gate)\", \"seed\": 0, \"wall_clock_seconds\": 125.0, \"gpu_hours\": 0.03}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-28T22:58:50.243Z\"}, \"exp_walker_008d_s7_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T23:23:59.556Z\", \"updated_at\": \"2026-05-28T15:59:57.557Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=7 — C2 onset rate rebuttal reserve. Retry after GPU collision bug. Fixed: --device cuda:1 + EGL=1. Source: D172 Tier 2.\", \"parent\": \"exp_008d_subsample_on_h8\", \"server\": \"westd-51268\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"rm -rf /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_walker_008d_s7_r2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && export CUDA_VISIBLE_DEVICES=0,1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_008d_s7_r2 --steps 105000 --seed 7 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:1\"], \"pid\": \"662242\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_walker_008d_s7_r2.log\", \"submitted_at\": \"2026-05-27T23:25:17.625Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1651.9, \"gpu_hours\": 0.46}, \"pid\": \"662242\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_walker_008d_s7_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"rm -rf /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_walker_008d_s7_r2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && export CUDA_VISIBLE_DEVICES=0,1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_008d_s7_r2 --steps 105000 --seed 7 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-27T23:52:51.986Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-27T23:52:49.489Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T23:52:58.769729+00:00\"}]}, \"notes\": \"Root cause: External SIGTERM (EXIT_CODE=143) — processes not daemonized, shared process group with launching SSH session. Parent process terminated after ~17.5min, killing both s6_r2 and s7_r2 simultaneously. Died at \\\"Start evaluation.\\\" (step 15000) due to timing coincidence, not eval-specific bug. Same root cause as s6/s7 first round (SIGTERM), but different trigger timing. Not OOM/GPU error/disk issue. Confirmed by Worker diagnose 2026-05-28.\"}, \"exp_walker_008d_s6_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T23:23:54.680Z\", \"updated_at\": \"2026-05-28T15:59:54.694Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=6 — C2 onset rate rebuttal reserve. Retry after GPU collision bug (s6/s7 both on cuda:0). Source: D172 Tier 2.\", \"parent\": \"exp_008d_subsample_on_h8\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"rm -rf /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_walker_008d_s6_r2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_008d_s6_r2 --steps 105000 --seed 6 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:0\"], \"pid\": \"662076\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_walker_008d_s6_r2.log\", \"submitted_at\": \"2026-05-27T23:25:10.090Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1634.1, \"gpu_hours\": 0.45}, \"pid\": \"662076\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_walker_008d_s6_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"rm -rf /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_walker_008d_s6_r2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_008d_s6_r2 --steps 105000 --seed 6 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-27T23:52:20.546Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-27T23:52:24.141Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T23:52:29.479674+00:00\"}]}, \"notes\": \"Root cause: External SIGTERM (EXIT_CODE=143) — processes not daemonized, shared process group with launching SSH session. Parent process terminated after ~17.5min, killing both s6_r2 and s7_r2 simultaneously. Died at \\\"Start evaluation.\\\" (step 15000) due to timing coincidence, not eval-specific bug. Same root cause as s6/s7 first round (SIGTERM), but different trigger timing. Not OOM/GPU error/disk issue. Confirmed by Worker diagnose 2026-05-28.\"}, \"exp_walker_008d_s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T21:05:17.669Z\", \"updated_at\": \"2026-05-27T23:23:37.305Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=7 — C2 onset rate rebuttal reserve. Trained dt_emb with multi-dt data exposure triggers CIVO. Additional seed to narrow CI on 2/3 onset rate. Source: D172 Tier 2.\", \"parent\": \"exp_008d_subsample_on_h8\", \"server\": \"westd-51268\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"kill 652815 2>/dev/null; sleep 2; kill -9 652815 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_008d_s7 --steps 105000 --seed 7 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:1\"], \"pid\": \"660802\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_walker_008d_s7.log\", \"submitted_at\": \"2026-05-27T23:09:27.654Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 709.9, \"gpu_hours\": 0.2}, \"pid\": \"660802\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_walker_008d_s7.log\", \"reproduce\": {\"command\": \"bash -c \\\"kill 652815 2>/dev/null; sleep 2; kill -9 652815 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_008d_s7 --steps 105000 --seed 7 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-27T23:21:20.324Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-27T23:21:17.585Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T23:21:27.566619+00:00\"}]}, \"notes\": \"SIGTERM (EXIT_CODE=143) 外部 kill，非程序崩溃。Tier 2 rebuttal reserve (D172)，数据锁定(D171)已生效。由 ops:kill-and-diagnose-tier2-hang Worker 终止，待该 Worker 返回详细诊断。\"}, \"exp_walker_008d_s6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T21:05:14.140Z\", \"updated_at\": \"2026-05-27T23:23:34.434Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON (gate_subsample_max_dt=2) + gate_fixed_dt=2 + H=8, seed=6 — C2 onset rate rebuttal reserve. Trained dt_emb with multi-dt data exposure triggers CIVO. Additional seed to narrow CI on 2/3 onset rate. Source: D172 Tier 2.\", \"parent\": \"exp_008d_subsample_on_h8\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_008d_s6 --steps 105000 --seed 6 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:0\"], \"pid\": \"660532\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_walker_008d_s6.log\", \"submitted_at\": \"2026-05-27T23:09:16.681Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 686.0, \"gpu_hours\": 0.19}, \"pid\": \"660532\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_walker_008d_s6.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_008d_s6 --steps 105000 --seed 6 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-27T23:20:47.539Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-27T23:20:42.644Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T23:21:05.364483+00:00\"}]}, \"notes\": \"SIGTERM (EXIT_CODE=143) 外部 kill，非程序崩溃。仅运行 686 秒（~11 分钟），大概率未完成 105K eval。Tier 2 rebuttal reserve (D172)，数据锁定(D171)已生效。由 ops:kill-and-diagnose-tier2-hang Worker 终止，待该 Worker 返回详细诊断。\"}, \"exp_cheetah_008a_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T20:21:22.462Z\", \"updated_at\": \"2026-05-27T23:12:10.588Z\", \"hypothesis\": \"Cheetah Run trained dt_emb (unexposed to dt>1, subsample OFF, gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15, seed=3 — C3 cross-env value growth suppression rebuttal reserve. Expect no CIVO (NVE < 2.0), value suppression consistent with s0/s1. Source: D172 rebuttal reserve.\", \"parent\": \"exp_008a_no_subsample_dt2\", \"server\": \"westd-51268\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_cheetah_008a_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 15\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:1\"], \"pid\": \"652810\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_cheetah_008a_s3.log\", \"submitted_at\": \"2026-05-27T20:22:23.747Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10054.1, \"gpu_hours\": 2.79}, \"pid\": \"652810\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_cheetah_008a_s3.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_cheetah_008a_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-27T23:09:51.796Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-27T23:09:57.810Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T23:10:07.546889+00:00\"}]}, \"notes\": \"失败原因: SIGTERM (EXIT_CODE=143) 外部 kill，非程序崩溃。实验在 112K 步被终止，但 105K 评估已完成。| 已有成果: 105K eval_return=506.4, NVE(ve_ratio)=0.3 (远低于τ=2.0), civo/alert=0.0, EMA_005=121.5, EMA_095=155.1。数据确认 no CIVO，与 s0/s1/s2 一致。| 建议: 105K 数据可用于 rebuttal reserve (C3 跨环境验证)。无需重跑——数据锁定已生效(D171)。\"}, \"exp_cheetah_008a_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T20:21:19.809Z\", \"updated_at\": \"2026-05-27T23:09:22.459Z\", \"hypothesis\": \"Cheetah Run trained dt_emb (unexposed to dt>1, subsample OFF, gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15, seed=2 — C3 cross-env value growth suppression rebuttal reserve. Expect no CIVO (NVE < 2.0), value suppression consistent with s0/s1. Source: D172 rebuttal reserve.\", \"parent\": \"exp_008a_no_subsample_dt2\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_cheetah_008a_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 15\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:0\"], \"pid\": \"652647\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_cheetah_008a_s2.log\", \"submitted_at\": \"2026-05-27T20:22:16.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10025.8, \"gpu_hours\": 2.78}, \"pid\": \"652647\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_cheetah_008a_s2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_cheetah_008a_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-27T23:06:41.135Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T23:06:47.650789+00:00\"}]}, \"metrics\": {\"eval_return_105K\": 457.4, \"value_mean_105K\": 188.6, \"NVE_105K\": 0.412, \"civo_alert\": 0, \"eval_return_peak\": 589.7, \"eval_return_peak_step\": 95000, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"model_loss_105K\": 1.8, \"kl_105K\": 1.8, \"fps\": 11.3, \"EMA_005_105K\": 139.9, \"EMA_095_105K\": 204.3}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_cheetah_008a_s2/latest.pt\", \"completed_at\": \"2026-05-27T23:09:22.459Z\"}, \"exp_walker_008f_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T14:22:32.789Z\", \"updated_at\": \"2026-05-27T17:23:41.428Z\", \"hypothesis\": \"dt_embed_dim=0 + gate+subsample ON in Walker Walk seed 0 will NOT show CIVO (NVE<2.0), replicating 008f causal control from seed 0. Confirms removing dt_embedding prevents CIVO, strengthening C2. Source: D164 Walker priority, plan_012 C2 multi-seed.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_008f_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:0\"], \"pid\": \"637987\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_walker_008f_s0.log\", \"submitted_at\": \"2026-05-27T14:23:11.189Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_walker_008f_s0/latest.pt\", \"wall_clock_seconds\": 10755, \"gpu_hours\": 2.99}, \"pid\": \"637987\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_walker_008f_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_008f_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 139.54, \"value_mean_105K\": 138.94, \"NVE_105K\": 0.996, \"civo_ve_ratio_105K\": 0.996, \"civo_alert\": 0, \"eval_return_peak\": 342.92, \"eval_return_peak_step\": 95000, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"EMA_005_105K\": 124.26, \"EMA_095_105K\": 153.07, \"model_loss_105K\": 4.53, \"kl_105K\": 5.34, \"fps\": 9.8}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_walker_008f_s0/latest.pt\", \"completed_at\": \"2026-05-27T17:23:41.428Z\"}, \"exp_cheetah_008a_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T14:20:25.880Z\", \"updated_at\": \"2026-05-27T17:12:18.383Z\", \"hypothesis\": \"Cheetah Run trained dt_emb (unexposed to dt>1, subsample OFF, gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15, seed=0 — C3 cross-env value growth suppression. Training only uses dt=1 data, so dt=2 embedding is untrained. Expect no CIVO, value suppression pattern matching Walker 008a. Source: D168, plan_023.\", \"parent\": \"exp_008a_no_subsample_dt2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_cheetah_008a_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 15\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:1\"], \"pid\": \"637656\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_cheetah_008a_s0.log\", \"submitted_at\": \"2026-05-27T14:21:43.914Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10234.5, \"gpu_hours\": 2.84}, \"server\": \"westd-51268\", \"gpu\": \"cuda:1\", \"pid\": \"637656\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_cheetah_008a_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_cheetah_008a_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-27T17:08:42.665Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T17:08:50.248325+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 366.19, \"value_mean_105K\": 164.58, \"NVE_105K\": 0.449, \"civo_ve_ratio_105K\": 0.449, \"civo_alert\": 0, \"eval_return_peak\": 483, \"eval_return_peak_step\": 85000, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"EMA_005_105K\": 132.95, \"EMA_095_105K\": 174.91, \"model_loss_105K\": 1.83, \"kl_105K\": 1.72, \"fps\": 11.1}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_cheetah_008a_s0/latest.pt\", \"completed_at\": \"2026-05-27T17:12:18.383Z\"}, \"exp_cheetah_008a_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T11:28:25.211Z\", \"updated_at\": \"2026-05-27T14:21:02.174Z\", \"hypothesis\": \"Cheetah Run trained dt_emb (unexposed to dt>1, subsample OFF, gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15, seed=1 — C3 cross-env value growth suppression. Training only uses dt=1 data, so dt=2 embedding is untrained. Expect no CIVO, value suppression pattern matching Walker 008a. Source: D167, plan_023. Replaces killed exp_099_cheetah_008a_s1.\", \"parent\": \"exp_008a_no_subsample_dt2\", \"server\": \"westd-51268\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_cheetah_008a_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 15\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:1\"], \"pid\": \"629903\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_cheetah_008a_s1.log\", \"submitted_at\": \"2026-05-27T11:29:03.792Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10318.4, \"gpu_hours\": 2.87}, \"pid\": \"629903\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_cheetah_008a_s1.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_cheetah_008a_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-27T14:16:25.507Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T14:16:36.921751+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 281.24, \"value_mean_105K\": 164.29, \"ve_ratio_105K\": 0.584, \"NVE_105K\": 0.584, \"civo_alert\": 0, \"eval_return_peak\": 519.56, \"eval_return_peak_step\": 75000, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_cheetah_008a_s1/latest.pt\", \"completed_at\": \"2026-05-27T14:21:02.174Z\"}, \"exp_hopper_no_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T08:08:47.870Z\", \"updated_at\": \"2026-05-27T11:17:21.884Z\", \"hypothesis\": \"Removing dt_embedding entirely (dt_embed_dim=0) while keeping gate+dt=2+subsample ON will still show severe learning delay in Hopper, confirming gate mechanism itself (not dt_emb) is the root cause of Hopper's failure. Source: D162 diagnostic.\", \"parent\": \"exp_hopper_trained_s0\", \"server\": \"westd-51268\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:1\"], \"pid\": \"619366\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_hopper_no_dt_emb_s0.log\", \"submitted_at\": \"2026-05-27T08:09:15.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11286.4, \"gpu_hours\": 3.14}, \"pid\": \"619366\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_hopper_no_dt_emb_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-27T11:10:43.054Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T11:10:49.451083+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 10.759, \"eval_return_final_pct_baseline\": 11.2, \"ve_ratio_peak_gte35k\": 1.949, \"nve_peak\": 4.37, \"nve_sustained_above_1_5\": false, \"value_mean_final\": 2.32, \"actor_entropy_final\": -1.939}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_no_dt_emb_s0\", \"completed_at\": \"2026-05-27T11:17:21.884Z\"}, \"exp_hopper_frozen_s0_ext\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T09:14:24.513Z\", \"updated_at\": \"2026-05-27T10:56:21.405Z\", \"hypothesis\": \"Extending frozen_s0 from 105K→150K will show eval_return recovery (rising like trained_s0_ext: 3.26→81.58) with ve_ratio declining, confirming frozen_s0's 'degenerate CIVO' @95K is transient instability during severe learning delay, not true CIVO mechanism. Source: D163.\", \"parent\": \"exp_hopper_frozen_s0\", \"plan_id\": \"D163\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s0 --steps 150000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:0\"], \"pid\": \"622633\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_hopper_frozen_s0_ext.log\", \"submitted_at\": \"2026-05-27T09:16:00.102Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6021.3, \"gpu_hours\": 1.67}, \"pid\": \"622633\", \"log_path\": \"logdir/exp_hopper_frozen_s0/metrics.jsonl\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s0 --steps 150000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"finished_at\": \"2026-05-27T10:41:59.098Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T10:42:05.863225+00:00\"}]}, \"metrics\": {\"step\": 160000, \"eval_step\": 152000, \"eval_return_final\": 0.5608, \"eval_return_105K\": 0, \"eval_return_peak\": 1.534, \"eval_return_peak_step\": 112000, \"ve_ratio_trajectory\": {\"105K\": 4335664.27, \"122K\": 10.149, \"132K\": 955.034, \"142K\": 18.055, \"152K\": 15.08}, \"value_mean_trajectory\": {\"105K\": 4.34, \"122K\": 7.18, \"132K\": 7.08, \"142K\": 7.62, \"152K\": 8.46}, \"nve_peak\": 7756535.1, \"nve_peak_step\": 105000, \"nve_35K\": 2.75, \"nve_95K\": 5.2, \"pattern\": \"persistent_phantom_value_no_recovery\", \"comparison_vs_trained_s0_ext\": \"trained recovered (3.26→81.58), frozen did NOT (0→0.56). Fundamentally different failure mode.\", \"notes\": \"eval_return stayed 0-1.5 throughout 105K-152K extension. value_mean grew 4.34→8.46 (phantom value). ve_ratio remained elevated 10-955x. No recovery pattern observed.\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_frozen_s0/latest.pt\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-27T10:56:21.405Z\"}, \"exp_009f_008f_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:46:03.293Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:15.806Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:46:05.155411+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:52:15.790170+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"Seed duplication: 009f used seed=1 same as parent 008f, producing deterministic repeat (prefill returns identical). Killed by Director order.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"dt_embed_dim=0 + subsample ON in Walker Walk seed 1 will NOT show CIVO (NVE<1.5), replicating causal control from seed 0. Source: plan_012, C2 multi-seed replication.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"516110\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T18:52:12.322Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T18:44:58.143Z\", \"training_hours\": 0.12}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.07, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"pid\": \"516110\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:47:48.525Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 265.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-27T10:48:57.827Z\"}, \"exp_009e_008d_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T11:26:52.478Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T11:09:15.367Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Trained dt_emb + subsample ON in Walker Walk seed 1 will replicate CIVO onset (NVE>1.5) as seen in seed 0. Source: plan_011, C2 multi-seed replication.\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1/metrics.jsonl\", \"metrics\": {\"ve_ratio_peak\": 1.6663, \"ve_ratio_peak_step\": 55000, \"ve_ratio_final\": 1.03, \"ve_ratio_final_step\": 105000, \"nve_peak\": 4.13, \"nve_peak_step\": 55000, \"nve_peak_note\": \"step-matched s1 baseline @55K = 0.4035; paper onset NVE @45K = 2.09x\", \"nve_classification\": \"onset_collapse\"}, \"notes\": \"008d extended replication (same seed=1, 009e extends 008d from 55K to 105K). Eval trajectory 5K-55K identical to 008d (deterministic). Collapse confirmed at 105K: eval 131.08, nve@55K=4.12x (normalized). 65K bounce to 250 was transient, not recovery. actor_loss flipped positive @85K. Independent collapse rate = 1/2 (seed 1 collapsed, seed 2 self-corrected), NOT 2/3 — 008d and 009e are the same seed.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": 119108, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009e_008d_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.43, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009e_008d_walker_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8\", \"pid\": \"119108\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:01:00Z\", \"wall_clock_seconds\": 19552.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-27T10:47:37.498Z\"}, \"exp_hopper_frozen_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T02:34:37.319Z\", \"updated_at\": \"2026-05-27T10:47:34.515Z\", \"conclusion\": \"killed\", \"hypothesis\": \"Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5×), confirming trained dt_emb is the necessary condition for CIVO across a third multi-joint locomotion environment (seed 1 replication)\", \"plan_id\": \"plan_040\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:0\"], \"pid\": \"626827\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-27T10:45:13.546Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 141.0, \"gpu_hours\": 0.04}, \"pid\": \"626827\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_hopper_frozen_s1.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\"}, \"completed_at\": \"2026-05-27T10:47:34.515Z\"}, \"exp_hopper_frozen_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T02:34:34.615Z\", \"updated_at\": \"2026-05-27T09:14:56.465Z\", \"conclusion\": \"success\", \"hypothesis\": \"Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5×), confirming trained dt_emb is the necessary condition for CIVO across a third multi-joint locomotion environment\", \"plan_id\": \"plan_040\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-27T05:51:11.281Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"finished_at\": \"2026-05-27T08:49:59.215Z\", \"training_hours\": 2.98}, \"spec\": {\"data_path\": \"dmc_hopper_hop\", \"data_count\": 105000, \"model_name\": \"dreamerv3\", \"seed\": 0, \"checkpoint_source\": \"none (fresh training)\", \"eval_data\": \"dmc_hopper_hop\", \"checkpoint_path\": \"logdir/exp_hopper_frozen_s0/latest.pt\", \"log_path\": \"logdir/exp_hopper_frozen_s0/metrics.jsonl\"}, \"pid\": \"612905\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_hopper_frozen_s0.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T08:50:05.781559+00:00\"}]}, \"metrics\": {\"step\": 105000, \"eval_return_final\": 0, \"eval_return_peak\": 3.6, \"eval_return_peak_step\": 85000, \"ve_ratio_final\": 4335664.3, \"civo_alert\": 1, \"civo_alert_steps\": [65000, 105000], \"value_mean_final\": 4.337, \"target_mean_final\": 4.389, \"wall_clock_hours\": 2.95, \"pattern\": \"degenerate_civo_near_zero_magnitude\", \"notes\": \"D155 criteria formally met @95K (ve=2.69, sustained 2 points) but eval_return=1.083 (1.1% baseline). 105K ve=4.3M is eval=0/epsilon artifact. Mechanistically distinct from Walker/Cheetah standard CIVO.\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_frozen_s0/latest.pt\", \"completed_at\": \"2026-05-27T08:57:25.460Z\"}, \"exp_hopper_trained_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T02:34:29.841Z\", \"updated_at\": \"2026-05-27T08:08:35.045Z\", \"conclusion\": \"killed\", \"hypothesis\": \"Trained dt_emb + subsample ON in Hopper Hop will reproduce CIVO (NVE > 1.5×) as observed in Walker (3/3) and Cheetah (3/4), confirming CIVO generalizes across multi-joint locomotion environments (seed 1 replication)\", \"plan_id\": \"plan_040\", \"spec\": {\"server\": \"westd-51268\", \"gpu\": \"cuda:1\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"model_name\": \"dreamerv3\", \"data_path\": \"dmc_hopper_hop (online)\", \"data_count\": \"105000 steps\", \"seed\": 1, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-27T08:08:35.045Z\"}, \"exp_hopper_trained_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T02:34:26.587Z\", \"updated_at\": \"2026-05-27T08:08:33.860Z\", \"conclusion\": \"success\", \"hypothesis\": \"Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE &gt; 1.5× after 35K steps), consistent with Walker (3/3) and Cheetah (3/4). Source: C2 third-environment verification (D160).\", \"plan_id\": \"plan_040\", \"server\": \"westd-51268\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-51268\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-27T02:55:36.648Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:1\"], \"pid\": \"604513\", \"log_path\": \"logdir/exp_hopper_trained_s0/metrics.jsonl\", \"submitted_at\": \"2026-05-27T02:59:09.552Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"logdir/exp_hopper_trained_s0/latest.pt\", \"wall_clock_seconds\": 10864.2, \"gpu_hours\": 3.02}, \"pid\": \"604513\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_hopper_trained_s0.log\", \"completed_at\": \"2026-05-27T06:00:13.703Z\", \"metrics\": {\"step\": 105000, \"eval_return_final\": 3.26, \"eval_return_peak\": 8.01, \"eval_return_peak_step\": 85000, \"ve_ratio_final\": 0.897, \"civo_alert\": 1, \"value_mean_trajectory\": [0.48, 1.29, 2.93], \"pattern\": \"severe_learning_delay\", \"nve_105K_vs_baseline\": 1.6, \"notes\": \"no CIVO detected; gate+dt=2 causes learning delay in Hopper independent of dt_emb training\"}}, \"exp_hopper_trained_s0_ext\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T06:00:49.737Z\", \"updated_at\": \"2026-05-27T08:07:16.279Z\", \"hypothesis\": \"Continuing trained_s0 from 105K to 150K will confirm delayed CIVO: ve_ratio (0.897 at 105K, exponentially rising) will cross NVE>1.5 threshold by ~115-125K, upgrading from emerging to confirmed delayed CIVO. Parent: exp_hopper_trained_s0.\", \"parent\": \"exp_hopper_trained_s0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 150000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:1\"], \"pid\": \"614518\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_hopper_trained_s0_ext.log\", \"submitted_at\": \"2026-05-27T06:21:00.173Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6254.5, \"gpu_hours\": 1.74}, \"server\": \"westd-51268\", \"gpu\": \"cuda:1\", \"pid\": \"614518\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_hopper_trained_s0_ext.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 150000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-27T07:59:25.773Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T07:59:32.660838+00:00\"}]}, \"metrics\": {\"step\": 168000, \"eval_step\": 158000, \"eval_return_final\": 81.58, \"eval_return_105K\": 3.26, \"eval_return_peak\": 81.58, \"ve_ratio_trajectory\": {\"105K\": 0.897, \"118K\": 0.376, \"128K\": 5.519, \"138K\": 0.37, \"148K\": 0.55, \"158K\": 0.439}, \"civo_alert_105K\": 1, \"civo_alert_final\": 0, \"pattern\": \"transient_instability_recovered\", \"nve_105K_vs_baseline\": 1.6}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_trained_s0/latest.pt\", \"completed_at\": \"2026-05-27T08:05:14.676Z\"}, \"exp_hopper_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T02:34:22.253Z\", \"updated_at\": \"2026-05-27T06:24:27.230Z\", \"conclusion\": \"success\", \"hypothesis\": \"Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE &lt; 1.5×). Source: C1/C2 third-environment verification (D160).\", \"plan_id\": \"plan_040\", \"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-51268\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-27T02:55:33.719Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 105000 --seed 0 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-27T05:48:08.854Z\", \"training_hours\": 2.88}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 105000 --seed 0 --compile False --device cuda:0\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:0\"], \"pid\": \"604350\", \"log_path\": \"logdir/exp_hopper_baseline/metrics.jsonl\", \"submitted_at\": \"2026-05-27T02:59:02.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"logdir/exp_hopper_baseline/latest.pt\", \"wall_clock_seconds\": 12318.4, \"gpu_hours\": 3.42}, \"pid\": \"604350\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_hopper_baseline.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T05:48:15.500405+00:00\"}]}, \"metrics\": {\"step\": 105000, \"eval_return_final\": 96.43, \"ve_ratio_final\": 0.559, \"ve_ratio_peak\": 3.48, \"ve_ratio_peak_step\": 65000, \"civo_alert\": 0, \"value_mean_final\": 53.9, \"target_mean_final\": 54.2, \"wall_clock_hours\": 2.88}, \"completed_at\": \"2026-05-27T06:24:21.198Z\"}, \"exp_108_hopper_frozen_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T02:55:22.603Z\", \"updated_at\": \"2026-05-27T03:03:32.297Z\", \"hypothesis\": \"Frozen dt_embedding in Hopper Hop will prevent CIVO onset (NVE &lt; 1.5× throughout), second seed for mitigation confirmation. Source: C6 third-environment verification (D160).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-27T03:03:32.297Z\"}, \"exp_107_hopper_frozen_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T02:55:18.139Z\", \"updated_at\": \"2026-05-27T03:03:27.004Z\", \"hypothesis\": \"Frozen dt_embedding in Hopper Hop will prevent CIVO onset (NVE &lt; 1.5× throughout), confirming causal role of trained dt_emb as CIVO trigger. Source: C6 third-environment verification (D160).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-27T03:03:27.004Z\"}, \"exp_106_hopper_trained_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T02:55:11.391Z\", \"updated_at\": \"2026-05-27T03:03:24.020Z\", \"hypothesis\": \"Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE &gt; 1.5× after 35K steps), second seed for onset rate. Source: C2 third-environment verification (D160).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-27T03:03:24.020Z\"}, \"exp_105_hopper_trained_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T02:55:06.756Z\", \"updated_at\": \"2026-05-27T03:03:20.261Z\", \"hypothesis\": \"Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE &gt; 1.5× after 35K steps), consistent with Walker (3/3) and Cheetah (3/4). Source: C2 third-environment verification (D160).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-27T03:03:20.261Z\"}, \"exp_104_hopper_baseline_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T02:55:00.720Z\", \"updated_at\": \"2026-05-27T03:03:15.605Z\", \"hypothesis\": \"Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE &lt; 1.5×). Source: C1/C2 third-environment verification (D160).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-27T03:03:15.605Z\"}, \"exp_101_rssm_prediction_quality\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:40:33.509Z\", \"updated_at\": \"2026-05-26T11:31:49.832Z\", \"hypothesis\": \"RSSM prediction quality analysis: 对比 trained dt_emb 模型在 dt=1 vs dt=2 transition 上的 observation/reward reconstruction loss。如果 dt=2 prediction 质量显著低于 dt=1，则 CIVO 的 root cause 可能是 RSSM 在未充分训练的 dt=2 上产生低质量 imagined trajectory，导致 critic 在这些 trajectory 上过度估值。plan_030。\", \"conclusion\": \"killed\", \"notes\": \"Director 取消：rssm_fidelity_v2 + standardized_v3 已覆盖此分析需求。脚本 scripts/analyze_rssm_exp101.py 保留备用。\", \"completed_at\": \"2026-05-26T11:31:49.832Z\"}, \"exp_103_cheetah_008a_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T04:34:41.510Z\", \"updated_at\": \"2026-05-26T11:31:32.782Z\", \"hypothesis\": \"Cheetah Run trained dt_emb (unexposed to dt>1, subsample OFF, gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15, seed=1 — C3 Cheetah cross-env 验证第 2 seed。与 exp_102 共同建立 C3 value suppression 在 Cheetah 上的多 seed 证据。替代被 killed 的 exp_099。plan_023。\", \"parent\": \"exp_099_cheetah_008a_s1\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-26T11:31:32.782Z\"}, \"exp_102_cheetah_008a_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T04:34:39.218Z\", \"updated_at\": \"2026-05-26T11:31:30.277Z\", \"hypothesis\": \"Cheetah Run trained dt_emb (unexposed to dt>1, subsample OFF, gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15, seed=0 — C3 Cheetah cross-env 验证。训练只用 dt=1 数据，dt_emb 的 dt=2 embedding 未被训练，预期无 CIVO（value suppression 而非 overestimation）。替代被 killed 的 exp_098。plan_023。\", \"parent\": \"exp_098_cheetah_008a_s0\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-26T11:31:30.277Z\"}, \"exp_100_walker_008a_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:14:23.405Z\", \"updated_at\": \"2026-05-26T08:06:14.728Z\", \"hypothesis\": \"Walker Walk trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=1 — C3 Walker 008a 第 2 seed。与 exp_008a_no_subsample_dt2 (s0) 共同建立 C3 value suppression 多 seed 证据。训练只用 dt=1 数据，dt_emb 的 dt=2 embedding 未被训练，预期无 CIVO。plan_013。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_100_walker_008a_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:1\"], \"pid\": \"5591\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_100_walker_008a_s1.log\", \"submitted_at\": \"2026-05-26T03:38:30.540Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": \"105000 steps\", \"model_name\": \"DreamerV3-S + gate_dt_emb (008a config, subsample OFF)\", \"seed\": 1, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - online RL training\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_100_walker_008a_s1/checkpoint.ckpt\", \"wall_clock_seconds\": 16064.2, \"gpu_hours\": 4.46}, \"metrics\": {\"step\": 105000, \"eval_return_trajectory\": [31, 169, 158, 203, 306, 457, 629, 687, 657, 718, 750.6], \"ve_ratio_max\": 0.33, \"civo_alert\": 0, \"eval_final\": 750.6, \"eval_final_pct_baseline\": 0.82, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0}, \"reproduce\": {\"finished_at\": \"2026-05-26T07:47:19.629Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T07:47:28.197769+00:00\"}]}, \"notes\": \"C3 Walker 008a 2-seed 闭合 (s0=778, s1=751), 无 CIVO. ve_ratio_max=0.33, eval_final=750.6 (82% baseline). Untrained dt_emb 持续抑制 value overestimation.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T08:06:14.728Z\"}, \"exp_097_cheetah_008d_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T00:46:49.098Z\", \"updated_at\": \"2026-05-26T07:46:03.066Z\", \"hypothesis\": \"Cheetah with fixed dt=2 and subsample_max_dt=2 (008d config, seed 3) will reproduce the CIVO trigger pattern seen in Walker, confirming cross-environment generality of the trained dt_emb collapse mechanism.\", \"parent\": \"exp_078_cheetah_008d_s0\", \"notes\": \"Cheetah CIVO onset@45K confirmed (ve_ratio=2.3). ve_ratio自修复但eval持续下滑(192.5@75K→61.7@105K=14% baseline), actor_entropy升至-0.7(策略退化). 分类: onset_transient_then_degraded — CIVO造成不可恢复性能损伤. Cheetah onset rate 3/4 (75%), cross-env 6/7 (86%).\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_097_cheetah_008d_s3/checkpoint.ckpt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_097_cheetah_008d_s3.log\"}, \"metrics\": {\"step\": 105000, \"eval_return_trajectory\": [8.7, 216.6, 139.4, 105.3, 23.4, 68.2, 182.5, 192.5, 77.4, 101.2, 61.7], \"ve_ratio_trajectory\": [0, 0.1, 0.3, 2.3, 0.8, 0.17, 0.34, 0.2, 0.3], \"civo_onset\": true, \"civo_onset_step\": 45000, \"civo_onset_ve_ratio\": 2.3, \"civo_alert_triggered\": true, \"nve_pattern\": \"onset_transient_then_degraded\", \"eval_final\": 61.7, \"eval_final_pct_baseline\": 0.14, \"actor_entropy_final\": -0.7, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0}, \"reproduce\": {\"finished_at\": \"2026-05-26T07:42:37.699Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T07:42:44.196584+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T07:45:53.471Z\"}, \"rssm_fidelity_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:26:19.011Z\", \"updated_at\": \"2026-05-26T05:55:33.129Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 python -u analyze_rssm_fidelity_v2.py --device cuda:0\\\"\", \"server\": \"westd-51268\", \"gpu\": [\"cuda:1\"], \"pid\": \"4373\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/rssm_fidelity_v2.log\", \"submitted_at\": \"2026-05-26T03:26:18.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8954.9, \"gpu_hours\": 2.49}, \"conclusion\": \"success\", \"checkpoint_path\": \"westd-51268:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/analysis_rssm_standardized_walker.json\", \"log_path\": \"/tmp/rssm_walker.log\", \"hypothesis\": \"RSSM standardized prediction quality analysis: trained dt_emb models have higher reward prediction gap (dt2/dt1 ratio) than baseline/frozen/no_dt_emb models, confirming that CIVO root cause lies in reward head generalization at dt=2 rather than observation prediction quality.\", \"completed_at\": \"2026-05-26T05:55:33.129Z\"}, \"exp_091_cheetah_008d_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T20:29:07.244Z\", \"updated_at\": \"2026-05-26T04:41:38.281Z\", \"hypothesis\": \"Cheetah Run trained dt_emb + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_078 (s0, NVE=4.1×, CIVO confirmed) 和 exp_088 (s1, running)。预期触发 CIVO，给 Cheetah CIVO trigger 凑齐 3-seed 基础，加强 C1 cross-env 证据。plan_021。\", \"parent\": \"exp_078_cheetah_008d_s0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_091_cheetah_008d_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"47303\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_091_cheetah_008d_s2.log\", \"submitted_at\": \"2026-05-25T20:29:32.176Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (trained dt_emb)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"wall_clock_seconds\": 8969.0, \"gpu_hours\": 2.49}, \"metrics\": {\"eval_return_final\": 2.5, \"eval_return_peak\": 213.83, \"eval_return_peak_step\": 45000, \"eval_trajectory\": {\"5K\": 9.04, \"15K\": 97.2, \"25K\": 126.42, \"35K\": 182.63, \"45K\": 213.83, \"55K\": 98.87, \"65K\": 2.23, \"75K\": 1.88, \"85K\": 2.12, \"95K\": 0.55, \"105K\": 2.5}, \"ve_ratio_final\": 27.89, \"ve_ratio_peak\": 127.62, \"ve_ratio_peak_step\": 95000, \"ve_ratio_trajectory\": {\"15K\": 0.017, \"25K\": 0.091, \"35K\": 0.144, \"45K\": 0.212, \"55K\": 0.692, \"65K\": 34.8, \"75K\": 43.14, \"85K\": 35.86, \"95K\": 127.62, \"105K\": 27.89}, \"value_mean_trajectory\": {\"5K\": 0, \"15K\": 1.69, \"25K\": 11.49, \"35K\": 26.28, \"45K\": 45.35, \"55K\": 68.4, \"65K\": 77.52, \"75K\": 81.16, \"85K\": 75.86, \"95K\": 70.36, \"105K\": 69.59}, \"nve_peak\": 138.7, \"nve_peak_step\": 75000, \"nve_onset_step\": 45000, \"nve_classification\": \"onset_collapse\", \"civo\": true, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"total_steps\": 105000, \"baseline_ref\": \"mean(exp_077_s0, exp_083_s1)\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_091_cheetah_008d_s2/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_091_cheetah_008d_s2.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T22:59:01.177Z\", \"notes\": \"CIVO CONFIRMED: nve_peak=138.7×, eval 213→2.5 完全崩溃 (onset_collapse)。conclusion 保持 success 因 registry 不支持自定义值，但本实验结果为 CIVO 触发确认。\"}, \"exp_099_cheetah_008a_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T00:47:59.656Z\", \"updated_at\": \"2026-05-26T02:40:53.102Z\", \"hypothesis\": \"Cheetah Run trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=1 — C3 cross-env 第 2 seed。与 exp_098 (s0) 共同建立 Cheetah 008a 多 seed 证据基础。训练只用 dt=1 数据，dt_emb 的 dt=2 embedding 未被训练，预期无 CIVO。plan_023。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_099_cheetah_008a_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"322767\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_099_cheetah_008a_s1.log\", \"submitted_at\": \"2026-05-26T01:20:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (trained dt_emb, subsample OFF, H=15, Cheetah 008a)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"checkpoint_path\": \"N/A (killed at 8K steps)\", \"wall_clock_seconds\": 4849.4, \"gpu_hours\": 1.35}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-26T02:40:49.431Z\", \"notes\": \"冗余，与已完成的 Walker 008a 实验配置重叠。Director 指令 kill。仅跑到 8K/105K。\"}, \"exp_098_cheetah_008a_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T00:46:52.448Z\", \"updated_at\": \"2026-05-26T02:40:52.020Z\", \"hypothesis\": \"Cheetah Run trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=0 — 重跑丢失的 exp_096（westd 宕机）。Cheetah 版 Walker 008a 配置，训练只用 dt=1 数据，dt_emb 的 dt=2 embedding 未被训练。预期无 CIVO，验证 C3 cross-env value suppression。plan_023。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_098_cheetah_008a_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"322486\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_098_cheetah_008a_s0.log\", \"submitted_at\": \"2026-05-26T01:20:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (trained dt_emb, subsample OFF, H=15, Cheetah 008a)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"checkpoint_path\": \"N/A (killed at 8K steps)\", \"wall_clock_seconds\": 4846.9, \"gpu_hours\": 1.35}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-26T02:40:46.869Z\", \"notes\": \"冗余，与已完成的 Walker 008a 实验配置重叠（exp_008a s0, exp_074 s3 等均 success）。Director 指令 kill。仅跑到 8K/105K。\"}, \"exp_093_cheetah_no_dt_emb_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T22:52:27.267Z\", \"updated_at\": \"2026-05-26T02:07:10.665Z\", \"hypothesis\": \"Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_embedding 完全移除后预期无 CIVO，加强 C2 cross-env causal control 多 seed 证据基础。plan_022。（重提交 exp_090，修正 CLI flag: --gate_dt_embed_dim 0）\", \"parent\": \"exp_082_cheetah_no_dt_emb_s0\", \"spec\": {\"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (gate_dt_embed_dim=0, Cheetah causal control)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_093_cheetah_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"313815\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_093_cheetah_no_dt_emb_s2.log\", \"submitted_at\": \"2026-05-25T22:52:44Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_093_cheetah_no_dt_emb_s2\", \"wall_clock_seconds\": 11666.7, \"gpu_hours\": 3.24}, \"reproduce\": {\"finished_at\": \"2026-05-26T02:00:31.977Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T02:00:40.013059+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 151.2, \"eval_return_peak\": 263, \"eval_return_peak_step\": 75000, \"eval_trajectory\": {\"5K\": 9.1, \"15K\": 48.8, \"25K\": 64.6, \"35K\": 73.5, \"45K\": 123.2, \"55K\": 135.8, \"65K\": 200.8, \"75K\": 263, \"85K\": 153.9, \"95K\": 96.4, \"105K\": 151.2}, \"value_mean_final\": 40.9, \"value_mean_trajectory\": {\"15K\": 1, \"25K\": 6.2, \"35K\": 14.4, \"45K\": 23.1, \"55K\": 32.6, \"65K\": 43.3, \"75K\": 53, \"85K\": 57.9, \"95K\": 52.1, \"105K\": 40.9}, \"ve_ratio_final\": 0.3, \"ve_ratio_peak\": 0.5, \"ve_ratio_peak_step\": 95000, \"ve_ratio_trajectory\": {\"15K\": 0, \"25K\": 0.1, \"35K\": 0.2, \"45K\": 0.2, \"55K\": 0.2, \"65K\": 0.2, \"75K\": 0.2, \"85K\": 0.4, \"95K\": 0.5, \"105K\": 0.3}, \"nve_peak\": 0.98, \"nve_peak_step\": 15000, \"nve_peak_35Kplus\": 0.81, \"nve_classification\": \"no_civo\", \"civo\": false, \"civo_alert\": 0, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"baseline_ref\": \"exp_077_cheetah_baseline_s0\", \"baseline_eval_105K\": 448.1, \"total_env_steps\": 112000}, \"completed_at\": \"2026-05-26T02:07:10.665Z\"}, \"exp_092_cheetah_no_dt_emb_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T22:52:25.939Z\", \"updated_at\": \"2026-05-26T02:07:07.999Z\", \"hypothesis\": \"Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=1 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_embedding 完全移除后预期无 CIVO，加强 C2 cross-env causal control 多 seed 证据基础。plan_022。（重提交 exp_089，修正 CLI flag: --gate_dt_embed_dim 0）\", \"parent\": \"exp_082_cheetah_no_dt_emb_s0\", \"spec\": {\"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (gate_dt_embed_dim=0, Cheetah causal control)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_092_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"313538\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_092_cheetah_no_dt_emb_s1.log\", \"submitted_at\": \"2026-05-25T22:52:42Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_092_cheetah_no_dt_emb_s1\", \"wall_clock_seconds\": 11666.0, \"gpu_hours\": 3.24}, \"reproduce\": {\"finished_at\": \"2026-05-26T02:01:02.948Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T02:01:11.889012+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 77.3, \"eval_return_peak\": 129.6, \"eval_return_peak_step\": 15000, \"eval_trajectory\": {\"5K\": 9, \"15K\": 129.6, \"25K\": 99, \"35K\": 59.7, \"45K\": 66.6, \"55K\": 39, \"65K\": 75.2, \"75K\": 79.7, \"85K\": 104.5, \"95K\": 114.1, \"105K\": 77.3}, \"value_mean_final\": 23.1, \"value_mean_trajectory\": {\"15K\": 1.2, \"25K\": 7, \"35K\": 13.9, \"45K\": 21, \"55K\": 27.4, \"65K\": 32.9, \"75K\": 35.3, \"85K\": 29.1, \"95K\": 25.6, \"105K\": 23.1}, \"ve_ratio_final\": 0.3, \"ve_ratio_peak\": 0.7, \"ve_ratio_peak_step\": 55000, \"ve_ratio_trajectory\": {\"15K\": 0, \"25K\": 0.1, \"35K\": 0.2, \"45K\": 0.3, \"55K\": 0.7, \"65K\": 0.4, \"75K\": 0.4, \"85K\": 0.3, \"95K\": 0.2, \"105K\": 0.3}, \"nve_peak\": 0.99, \"nve_peak_step\": 15000, \"nve_peak_35Kplus\": 0.78, \"nve_classification\": \"no_civo\", \"civo\": false, \"civo_alert\": 0, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"baseline_ref\": \"exp_077_cheetah_baseline_s0\", \"baseline_eval_105K\": 448.1, \"total_env_steps\": 112000}, \"completed_at\": \"2026-05-26T02:07:07.999Z\"}, \"exp_094\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T23:05:30.754Z\", \"updated_at\": \"2026-05-26T00:43:51.015Z\", \"spec\": {\"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": 53581, \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_094_cheetah_008d_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_094_cheetah_008d_s3.log\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (trained dt_emb)\", \"seed\": 3}, \"conclusion\": \"killed\", \"notes\": \"DUPLICATE — 短名条目，与 exp_094_cheetah_008d_s3 (PID 53576) 是同一进程。以长名条目为准。\", \"completed_at\": \"2026-05-26T00:42:53.682Z\"}, \"exp_093\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T23:05:26.801Z\", \"updated_at\": \"2026-05-26T00:43:47.127Z\", \"spec\": {\"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": 313815, \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_093_cheetah_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_093_cheetah_no_dt_emb_s2.log\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (gate_dt_embed_dim=0, Cheetah causal control)\", \"seed\": 2}, \"conclusion\": \"killed\", \"notes\": \"DUPLICATE — 短名条目，与 exp_093_cheetah_no_dt_emb_s2 (PID 313815) 是同一进程。以长名条目为准。\", \"completed_at\": \"2026-05-26T00:42:57.273Z\"}, \"exp_096_cheetah_008a_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T23:25:28.503Z\", \"updated_at\": \"2026-05-26T00:43:33.332Z\", \"hypothesis\": \"Cheetah Run trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=0 — Cheetah 版 Walker 008a 配置。Subsample OFF 意味着训练只用 dt=1 数据，dt_emb 的 dt=2 embedding 未被训练。预期无 CIVO（value growth suppression），验证 C3 cross-env。plan_023。（原 exp_095_cheetah_008a_s0，因编号冲突重命名）\", \"parent\": \"exp_008a_no_subsample_dt2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_095_cheetah_008a_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --imag_horizon 15\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"54457\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_095_cheetah_008a_s0.log\", \"submitted_at\": \"2026-05-25T23:05:28Z\", \"tmux_session\": \"exp_095_cheetah_008a_s0\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (trained dt_emb, subsample OFF, H=15, Cheetah 008a)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"wall_clock_seconds\": 5751.7, \"gpu_hours\": 1.6}, \"failure_reason\": \"SSH check failed 5x — last error: [Errno None] Unable to connect to port 19154 on 36.103.198.204\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T00:41:19.660Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-26T00:41:40.789169+00:00\"}]}, \"notes\": \"westd-19154 服务器不可达（SSH 连接失败 5 次），实验被迫中止。已跑约 1.6 gpu_hours。需要在其他服务器重跑。\"}, \"exp_095_cheetah_no_dt_emb_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T23:02:46.915Z\", \"updated_at\": \"2026-05-26T00:43:28.860Z\", \"hypothesis\": \"Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=3 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_embedding 完全移除后预期无 CIVO，加强 C2 cross-env causal control 多 seed 证据基础。plan_022。\", \"parent\": \"exp_082_cheetah_no_dt_emb_s0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_095_cheetah_no_dt_emb_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"54119\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_095_cheetah_no_dt_emb_s3.log\", \"submitted_at\": \"2026-05-25T23:03:48Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (gate_dt_embed_dim=0, Cheetah causal control)\", \"seed\": 3, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"wall_clock_seconds\": 5834.1, \"gpu_hours\": 1.62}, \"failure_reason\": \"SSH check failed 5x — last error: [Errno None] Unable to connect to port 19154 on 36.103.198.204\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T00:41:02.127Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-26T00:41:10.244912+00:00\"}]}, \"notes\": \"westd-19154 服务器不可达（SSH 连接失败 5 次），实验被迫中止。已跑约 1.62 gpu_hours。需要在其他服务器重跑。\"}, \"exp_094_cheetah_008d_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T22:57:23.377Z\", \"updated_at\": \"2026-05-26T00:43:23.847Z\", \"hypothesis\": \"Cheetah Run trained dt_emb + subsample ON + dt=2 + H=8, seed=3 — 第 4 个 seed 复制 exp_078 (s0, NVE=4.1×, CIVO confirmed)。与 exp_088 (s1, no CIVO) 和 exp_091 (s2, 待分析) 共同确定 Cheetah CIVO onset rate。plan_021。\", \"parent\": \"exp_078_cheetah_008d_s0\", \"spec\": {\"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (trained dt_emb)\", \"seed\": 3, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_094_cheetah_008d_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"53576\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_094_cheetah_008d_s3.log\", \"submitted_at\": \"2026-05-25T22:57:35Z\", \"wall_clock_seconds\": 6188.5, \"gpu_hours\": 1.72}, \"failure_reason\": \"SSH check failed 5x — last error: [Errno None] Unable to connect to port 19154 on 36.103.198.204\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-26T00:40:43.472Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-26T00:40:48.632191+00:00\"}]}, \"notes\": \"westd-19154 服务器不可达（SSH 连接失败 5 次），实验被迫中止。已跑约 1.72 gpu_hours。需要在其他服务器重跑。\"}, \"exp_095_cheetah_008a_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T23:05:17.077Z\", \"updated_at\": \"2026-05-25T23:31:42.647Z\", \"hypothesis\": \"Cheetah Run trained dt_emb (unexposed to dt>1, subsample OFF) + gate_fixed_dt=2 + H=15, seed=0 — Cheetah 版 Walker 008a 配置。Subsample OFF 意味着训练只用 dt=1 数据，dt_emb 的 dt=2 embedding 未被训练。预期无 CIVO（value growth suppression），验证 C3 cross-env。plan_023。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_095_cheetah_008a_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --imag_horizon 15\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"54457\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_095_cheetah_008a_s0.log\", \"submitted_at\": \"2026-05-25T23:05:28.832Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (trained dt_emb, subsample OFF, H=15, Cheetah 008a)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"wall_clock_seconds\": 1573.8, \"gpu_hours\": 0.44}, \"conclusion\": \"killed\", \"notes\": \"RENAMED to exp_096_cheetah_008a_s0 — 因 exp_095 编号已被 exp_095_cheetah_no_dt_emb_s3 (plan_022, C2 control) 占用。实际进程仍在 westd cuda:0 以 tmux session \\\"exp_095_cheetah_008a_s0\\\" 运行，cron 回调时需映射到 exp_096。\", \"completed_at\": \"2026-05-25T23:31:42.647Z\"}, \"exp_088\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T21:13:21.246Z\", \"updated_at\": \"2026-05-25T23:24:36.068Z\", \"metrics\": {\"eval_return_final\": 309.34, \"eval_return_best\": 309.34, \"best_step\": 105000, \"eval_return_trajectory\": {\"5K\": 13.48, \"15K\": 114.02, \"25K\": 177.63, \"35K\": 162.83, \"45K\": 131.77, \"55K\": 248.23, \"65K\": 172.46, \"75K\": 97.35, \"85K\": 85.46, \"95K\": 149.74, \"105K\": 309.34}, \"NVE_final\": 0.087, \"NVE_peak\": 1.82, \"NVE_peak_step\": 35000, \"NVE_trajectory\": {\"15K\": 0.166, \"25K\": 1.106, \"35K\": 1.82, \"45K\": 1.58, \"55K\": 0.55, \"65K\": 0.429, \"75K\": 0.518, \"85K\": 0.379, \"95K\": 0.214, \"105K\": 0.087}, \"NVE_median_last5\": 0.379, \"ve_ratio_peak\": 0.31, \"ve_ratio_peak_step\": 45000, \"ve_ratio_final\": 0.053, \"ve_ratio_trajectory\": {\"15K\": 0.0143, \"25K\": 0.0709, \"35K\": 0.1909, \"45K\": 0.31, \"55K\": 0.1568, \"65K\": 0.1855, \"75K\": 0.267, \"85K\": 0.2485, \"95K\": 0.1223, \"105K\": 0.0532}, \"civo_alert_max\": 0, \"nve_classification\": \"Healthy\", \"value_mean_peak\": 40.848, \"value_mean_final\": 16.455, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_088_cheetah_008d_s1/latest.pt\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_088_cheetah_008d_s1.log\", \"conclusion\": \"killed\", \"notes\": \"DUPLICATE — bug artifact. Correct entry is exp_088_cheetah_008d_s1 (DONE, conclusion=negative, NVE_peak=0.517). This bare 'exp_088' was created by NVE analysis worker with incorrect baseline calculation (NVE_peak=1.82 is wrong). Ignore this entry.\", \"completed_at\": \"2026-05-25T23:24:36.068Z\"}, \"exp_090_cheetah_no_dt_emb_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T20:15:41.571Z\", \"updated_at\": \"2026-05-25T22:52:09.583Z\", \"hypothesis\": \"Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_embedding 完全移除后预期无 CIVO，加强 C2 cross-env causal control 多 seed 证据基础。plan_022。\", \"parent\": \"exp_082_cheetah_no_dt_emb_s0\", \"spec\": {\"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (dt_embed_dim=0, Cheetah causal control)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && git pull && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_090_cheetah_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_embed_dim 0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"307484\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_090_cheetah_no_dt_emb_s2.log\", \"eval_data\": \"dmc_cheetah_run (online eval)\"}, \"conclusion\": \"failed\", \"failure_reason\": \"unrecognized CLI arg --dt_embed_dim 0; correct flag on bjb1 is --gate_dt_embed_dim 0\", \"completed_at\": \"2026-05-25T22:52:09.583Z\"}, \"exp_089_cheetah_no_dt_emb_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T20:15:40.357Z\", \"updated_at\": \"2026-05-25T22:52:07.231Z\", \"hypothesis\": \"Cheetah Run dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=1 — 跨 seed 复制 exp_082 (s0, NVE=0.33×, no CIVO, success)。dt_embedding 完全移除后预期无 CIVO，加强 C2 cross-env causal control 多 seed 证据基础。plan_022。\", \"parent\": \"exp_082_cheetah_no_dt_emb_s0\", \"spec\": {\"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (dt_embed_dim=0, Cheetah causal control)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && git pull && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_089_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_embed_dim 0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"307263\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_089_cheetah_no_dt_emb_s1.log\", \"eval_data\": \"dmc_cheetah_run (online eval)\"}, \"conclusion\": \"failed\", \"failure_reason\": \"unrecognized CLI arg --dt_embed_dim 0; correct flag on bjb1 is --gate_dt_embed_dim 0\", \"completed_at\": \"2026-05-25T22:52:07.231Z\"}, \"exp_086_frozen_dt_emb_cheetah_s0\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-25T16:24:01.866Z\", \"updated_at\": \"2026-05-25T21:08:51.498Z\", \"hypothesis\": \"Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Cheetah Run does not trigger CIVO — cross-environment validation that dt_emb TRAINING is CIVO necessary condition. Paired with exp_078 (trained dt_emb, NVE=4.1×). Re-run after orphan process incident.\", \"parent\": \"exp_078_cheetah_008d_s0\", \"completed_at\": \"2026-05-25T18:08:31.088Z\", \"reproduce\": {\"finished_at\": \"2026-05-25T20:17:39.670Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-25T18:08:47.611867+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T20:17:50.028253+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_086_frozen_dt_emb_cheetah_s0/latest.pt\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_086_frozen_dt_emb_cheetah_s0.log\"}, \"metrics\": {\"eval_return_final\": 53.3, \"eval_return_best\": 326.4, \"best_step\": 35000, \"total_steps\": 105000, \"NVE_final\": 0.27, \"NVE_peak\": 0.27, \"ve_ratio_peak\": 0.2, \"ve_ratio_peak_step\": 105000, \"gate_pattern\": \"100% dt=2 locked\", \"civo_alert\": false, \"nve_classification\": \"no_civo\"}, \"conclusion\": \"success\"}, \"exp_088_cheetah_008d_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T18:50:48.276Z\", \"updated_at\": \"2026-05-25T21:08:43.742Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_088_cheetah_008d_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"42804\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_088_cheetah_008d_s1.log\", \"submitted_at\": \"2026-05-25T18:50:47.731Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [1], \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO trigger config, Cheetah s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"wall_clock_seconds\": 8276.0, \"gpu_hours\": 2.3}, \"hypothesis\": \"Cheetah Run trained dt_emb + subsample ON + dt=2 + H=8, seed=1 — 跨 seed 复制 exp_078 (s0, NVE=4.1×, CIVO confirmed)。预期触发 CIVO，验证 Cheetah CIVO onset 的跨 seed 可复现性。plan_021。\", \"parent\": \"exp_078_cheetah_008d_s0\", \"reproduce\": {\"finished_at\": \"2026-05-25T21:03:45.960Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T21:03:51.893445+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"eval_return_final\": 309.3, \"eval_return_peak\": 309.3, \"eval_return_peak_step\": 105000, \"eval_trajectory\": {\"5K\": 13.5, \"15K\": 114, \"25K\": 177.6, \"35K\": 162.8, \"45K\": 131.8, \"55K\": 248.2, \"65K\": 172.5, \"75K\": 97.3, \"85K\": 85.5, \"95K\": 149.7, \"105K\": 309.3}, \"ve_ratio_final\": 0.053, \"ve_ratio_peak\": 0.31, \"ve_ratio_peak_step\": 45000, \"ve_ratio_trajectory\": {\"15K\": 0.014, \"25K\": 0.071, \"35K\": 0.191, \"45K\": 0.31, \"55K\": 0.157, \"65K\": 0.185, \"75K\": 0.267, \"85K\": 0.249, \"95K\": 0.122, \"105K\": 0.053}, \"nve_peak\": 0.517, \"nve_peak_step\": 45000, \"nve_onset_step\": null, \"nve_onset_value\": null, \"nve_trajectory_35Kplus\": {\"35K\": 0.318, \"45K\": 0.517, \"55K\": 0.261, \"65K\": 0.309, \"75K\": 0.445, \"85K\": 0.414, \"95K\": 0.204, \"105K\": 0.089}, \"nve_classification\": \"no_onset\", \"civo\": false, \"civo_alert\": 0, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"baseline_ref\": \"exp_083_cheetah_baseline_s1\", \"baseline_eval_105K\": 444, \"eval_pct_baseline\": 0.696, \"total_steps\": 105000, \"total_env_steps\": 105000}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_088_cheetah_008d_s1/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_088_cheetah_008d_s1.log\", \"completed_at\": \"2026-05-25T21:02:16Z\"}, \"exp_009b_008d_walker_s2\": {\"account\": \"root\", \"causal_conclusion\": \"Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x→0.38x@105K, eval 141→268) while seed 1 sustained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x→2.09x→4.12x) and collapsed (eval 167→83). Collapse is stochastic (1/2 seeds); nve>1.5x threshold (at 35K+ steps) is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009b_008d_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T18:51:00Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:25.186Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T18:47:21.873692+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed=2 — 跨 seed 复制 exp_008d (s0, collapse confirmed at ~55K, NVE=1.67×@55K). 预期在 ~55K 步内触发 CIVO collapse，验证 trained dt_emb 导致的 delusional critic collapse 的跨 seed 可复现性。plan_011。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009b_008d_walker_s2.log\", \"metrics\": {\"ve_ratio_peak\": 0.5703, \"ve_ratio_peak_step\": 55000, \"ve_ratio_final\": 0.25, \"ve_ratio_final_step\": 105000, \"nve_peak\": 1.62, \"nve_peak_step\": 45000, \"nve_peak_note\": \"step-matched s1 baseline @45K = 0.331; arithmetic peak @25K=2.04x excluded (baseline<0.1)\", \"nve_classification\": \"onset_self_correcting\"}, \"notes\": \"D032: Collapse NOT reproduced in seed 2. nve peaked 2.05x@25K (transient) then self-corrected to 0.38x@105K. Eval rose to 268. Contrast: seed 1 had SUSTAINED nve>1.5x at 35K+ (1.71x→2.09x→4.12x) → collapse to 83. Key finding: nve>1.5x threshold (35K+ steps) is reliable trained dt_emb marker (2/2 seeds), but collapse is stochastic (1/2). Framing proposal submitted to Director.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": \"887053\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-14T18:47:20.636Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, trained dt_embed)\", \"seed\": 2, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-25T19:54:21.605Z\"}, \"exp_085_frozen_dt_emb_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T16:17:10.446Z\", \"updated_at\": \"2026-05-25T19:52:18.635Z\", \"hypothesis\": \"Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Walker Walk seed=1 does not trigger CIVO — multi-seed validation that dt_emb TRAINING is the necessary condition for CIVO onset. Current code version (fb56c860a+).\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_085_frozen_dt_emb_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"296781\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_085_frozen_dt_emb_walker_s1.log\", \"submitted_at\": \"2026-05-25T16:17:29.039Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"model_name\": \"dreamerv3\", \"seed\": 1, \"checkpoint_source\": \"none (fresh training)\", \"eval_data\": \"dmc_walker_walk\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_085_frozen_dt_emb_walker_s1/latest.pt\", \"wall_clock_seconds\": 12139.0, \"gpu_hours\": 3.37}, \"reproduce\": {\"finished_at\": \"2026-05-25T19:31:38.872Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T19:31:47.198579+00:00\"}]}, \"metrics\": {\"eval_return_final\": 69.26, \"eval_return_best\": 281.53, \"best_step\": 65000, \"total_steps\": 105000, \"NVE_final\": 0.08, \"NVE_peak\": 0.31, \"gate_pattern\": \"100% dt=2 locked\", \"civo_alert\": false}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T19:39:48.059Z\"}, \"exp_084_frozen_dt_emb_walker_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T15:58:38.310Z\", \"updated_at\": \"2026-05-25T19:52:17.020Z\", \"hypothesis\": \"Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Walker Walk does not trigger CIVO — proving dt_emb TRAINING (not mere presence) is the necessary condition for CIVO onset. Re-run on current code version (fb56c860a+), replacing killed exp_079.\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && git pull && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_084_frozen_dt_emb_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"296484\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_084_frozen_dt_emb_walker_s0.log\", \"submitted_at\": \"2026-05-25T16:17:20.106Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"model_name\": \"dreamerv3\", \"seed\": 0, \"checkpoint_source\": \"none (fresh training)\", \"eval_data\": \"dmc_walker_walk\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_084_frozen_dt_emb_walker_s0/latest.pt\", \"wall_clock_seconds\": 12145.7, \"gpu_hours\": 3.37}, \"reproduce\": {\"finished_at\": \"2026-05-25T19:31:18.394Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T19:31:26.293176+00:00\"}]}, \"metrics\": {\"eval_return_final\": 281.48, \"eval_return_best\": 334.06, \"best_step\": 95000, \"total_steps\": 112000, \"NVE_final\": 0.31, \"NVE_peak\": 0.37, \"gate_pattern\": \"100% dt=2 locked\", \"civo_alert\": false}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T19:39:45.775Z\"}, \"exp_082_cheetah_no_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T13:12:29.199Z\", \"updated_at\": \"2026-05-25T18:49:20.158Z\", \"hypothesis\": \"Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0。移除 dt_embedding 后预期无 CIVO，证明 trained dt_emb 是 Cheetah CIVO 的必要条件。与 exp_078 (trained dt_emb, CIVO trigger) 构成因果对。plan_022。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_082_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_embed_dim 0\\\"\", \"server\": \"westd-19154\", \"gpu_ids\": [0], \"pid\": \"N/A\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (dt_embed_dim=0, Cheetah causal control)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\"}, \"pid\": \"29479\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_082_cheetah_no_dt_emb_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_082_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-25T16:21:37.237Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T16:21:43.091656+00:00\"}]}, \"metrics\": {\"eval_return_final\": 83.2, \"eval_return_peak\": 239.3, \"eval_return_peak_step\": 45000, \"eval_trajectory\": {\"5K\": 6.8, \"15K\": 32.2, \"25K\": 108.4, \"35K\": 119.4, \"45K\": 239.3, \"55K\": 157, \"65K\": 180.1, \"75K\": 178.6, \"85K\": 84.2, \"95K\": 57.7, \"105K\": 83.2}, \"ve_ratio_final\": 0.616, \"ve_ratio_peak\": 0.955, \"ve_ratio_peak_step\": 95000, \"ve_ratio_trajectory\": {\"15K\": 0.038, \"25K\": 0.069, \"35K\": 0.132, \"45K\": 0.103, \"55K\": 0.237, \"65K\": 0.268, \"75K\": 0.311, \"85K\": 0.724, \"95K\": 0.955, \"105K\": 0.616}, \"nve_peak\": 1.58, \"nve_peak_step\": 95000, \"nve_peak_note\": \"eval-variance-driven (eval=57.7, value=55.1, ve_ratio<1.0), NOT value overestimation\", \"nve_trajectory_35Kplus\": {\"35K\": 1.49, \"45K\": 0.59, \"55K\": 0.96, \"65K\": 0.55, \"75K\": 0.55, \"85K\": 0.98, \"95K\": 1.58, \"105K\": 1.02}, \"nve_classification\": \"no_civo\", \"civo\": false, \"civo_alert\": 0, \"civo_alert_steps\": [], \"value_mean_final\": 51.3, \"value_mean_95K\": 55.1, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"baseline_ref\": \"exp_077_cheetah_baseline_s0\", \"baseline_eval_105K\": 448.1, \"eval_pct_baseline\": \"18.6%\", \"causal_pair\": \"exp_078_cheetah_008d_s0\", \"causal_variable\": \"dt_embed_dim (082=0 vs 078=trained)\", \"total_steps\": 112000, \"total_env_steps\": 105000}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_082_cheetah_no_dt_emb_s0\", \"completed_at\": \"2026-05-25T16:27:45.939Z\"}, \"exp_087_frozen_dt_emb_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T16:29:59.272Z\", \"updated_at\": \"2026-05-25T18:45:37.694Z\", \"hypothesis\": \"Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Cheetah Run seed=1 does not trigger CIVO — multi-seed cross-environment validation that dt_emb TRAINING is CIVO necessary condition. Paired with exp_086 (frozen s0) and exp_078 (trained, NVE=4.1×).\", \"parent\": \"exp_086_frozen_dt_emb_cheetah_s0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_087_frozen_dt_emb_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"36195\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_087_frozen_dt_emb_cheetah_s1.log\", \"submitted_at\": \"2026-05-25T16:30:22.662Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 1, \"model_name\": \"DreamerV3+FrozenDtEmb_SubsampleON_Dt2_H8\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"checkpoint_source\": \"N/A (training from scratch, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\", \"wall_clock_seconds\": 8115.0, \"gpu_hours\": 2.25}, \"reproduce\": {\"finished_at\": \"2026-05-25T18:42:02.488Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T18:42:10.415795+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_087_frozen_dt_emb_cheetah_s1/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_087_frozen_dt_emb_cheetah_s1.log\", \"metrics\": {\"eval_return_105K\": 186.9, \"eval_return_peak\": 310.1, \"eval_return_peak_step\": \"75K\", \"eval_trajectory\": {\"5K\": 13.5, \"15K\": 90.2, \"25K\": 199.3, \"35K\": 165.7, \"45K\": 299.2, \"55K\": 207.2, \"65K\": 196.8, \"75K\": 310.1, \"85K\": 246.8, \"95K\": 57.9, \"105K\": 186.9}, \"ve_ratio_105K\": 0.1, \"ve_ratio_peak\": 0.2, \"ve_ratio_peak_step\": \"95K\", \"civo_alert\": 0, \"NVE\": 0.33, \"NVE_baseline\": \"exp_083_cheetah_baseline_s1\", \"NVE_baseline_ve_ratio_peak\": 0.6, \"nve_classification\": \"no_civo\", \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"total_steps\": 112000, \"model_loss_105K\": 2.4}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T18:45:37.694Z\"}, \"exp_083_cheetah_baseline_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T14:14:00.361Z\", \"updated_at\": \"2026-05-25T18:09:32.066Z\", \"hypothesis\": \"Cheetah Run dt=1 baseline seed=1。多 seed baseline 用于更稳健的 NVE 归一化，与 exp_077 (seed=0, eval=448.1) 构成 calibration 对。plan_020 第二个 seed。\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_083_cheetah_baseline_s1 --steps 105000 --seed 1 --compile False --device cuda:0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"30581\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_083_cheetah_baseline_s1.log\", \"submitted_at\": \"2026-05-25T14:28:23.155Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 1, \"model_name\": \"DreamerV3_baseline_dt1\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 105000, \"wall_clock_seconds\": 7365.2, \"gpu_hours\": 2.05}, \"reproduce\": {\"finished_at\": \"2026-05-25T16:28:26.304Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T16:28:32.490600+00:00\"}]}, \"metrics\": {\"eval_return_105K\": 444, \"eval_trajectory\": {\"5K\": 11.6, \"15K\": 76.4, \"25K\": 300.2, \"35K\": 372.3, \"45K\": 384.2, \"55K\": 395.4, \"65K\": 446.1, \"75K\": 440.5, \"85K\": 409, \"95K\": 466, \"105K\": 444}, \"ve_ratio_105K\": 0.6, \"ve_ratio_peak\": 0.6, \"ve_ratio_peak_step\": \"85K\", \"civo_alert\": 0, \"model_loss_105K\": 1.6}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_083_cheetah_baseline_s1/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_083_cheetah_baseline_s1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T16:31:08.314Z\", \"parent\": \"exp_077_cheetah_baseline_s0\"}, \"exp_078_cheetah_008d_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:24.844Z\", \"updated_at\": \"2026-05-25T18:06:40.922Z\", \"hypothesis\": \"Trained dt_embedding with subsample ON + dt=2 + H=8 on Cheetah Run triggers CIVO — cross-environment validation (C2) that CIVO is not Walker-specific. Paired with exp_077 (baseline) for NVE calculation.\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_078_cheetah_008d_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"21846\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_078_cheetah_008d_s0.log\", \"submitted_at\": \"2026-05-25T11:21:50.283Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11948.1, \"gpu_hours\": 3.32}, \"pid\": \"21846\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_078_cheetah_008d_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_078_cheetah_008d_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-25T14:27:13.393Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T14:27:19.359689+00:00\"}]}, \"metrics\": {\"eval_return_final\": 119.5, \"eval_return_peak\": 213.7, \"eval_return_peak_step\": 35000, \"eval_trajectory\": {\"5K\": 8.3, \"15K\": 41.3, \"25K\": 170, \"35K\": 213.7, \"45K\": 148.9, \"55K\": 64.5, \"65K\": 36.8, \"75K\": 26.1, \"85K\": 26.7, \"95K\": 32.5, \"105K\": 119.5}, \"ve_ratio_final\": 0.291, \"ve_ratio_peak\": 2.318, \"ve_ratio_peak_step\": 75000, \"ve_ratio_trajectory\": {\"15K\": 0.039, \"25K\": 0.056, \"35K\": 0.11, \"45K\": 0.295, \"55K\": 0.908, \"65K\": 1.72, \"75K\": 2.318, \"85K\": 2.022, \"95K\": 1.366, \"105K\": 0.291}, \"nve_peak\": 4.1, \"nve_peak_step\": 75000, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.7, \"nve_trajectory_35Kplus\": {\"35K\": 1.24, \"45K\": 1.7, \"55K\": 3.66, \"65K\": 3.55, \"75K\": 4.1, \"85K\": 2.74, \"95K\": 2.26, \"105K\": 0.48}, \"nve_classification\": \"onset_self_correcting\", \"civo\": true, \"civo_alert\": 1, \"civo_alert_steps\": [55000, 65000], \"civo_sustained_range\": \"45K-95K\", \"civo_self_correction\": true, \"civo_self_correction_step\": 105000, \"value_mean_peak\": 63.3, \"value_mean_peak_step\": 65000, \"value_mean_final\": 34.8, \"delta_ve_peak\": 0.814, \"delta_ve_peak_step\": 65000, \"gate_dt_mean\": 2, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0, \"baseline_ref\": \"exp_077_cheetah_baseline_s0\", \"baseline_eval_105K\": 448.1, \"eval_pct_baseline\": \"26.7%\", \"total_steps\": 112000, \"total_env_steps\": 105000}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_078_cheetah_008d_s0/latest.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T14:40:58.408Z\"}, \"exp_077_cheetah_baseline_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:21.685Z\", \"updated_at\": \"2026-05-25T18:06:38.886Z\", \"hypothesis\": \"Cheetah Run dt=1 baseline seed=0. Establishes NVE normalization denominator for Cheetah CIVO experiments. Paired with exp_078 (trained dt_emb CIVO trigger) and exp_083 (baseline seed=1).\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_077_cheetah_baseline_s0 --steps 105000 --seed 0 --compile False --device cuda:0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"21683\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_077_cheetah_baseline_s0.log\", \"submitted_at\": \"2026-05-25T11:21:44.224Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10257.0, \"gpu_hours\": 2.85}, \"pid\": \"21683\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_077_cheetah_baseline_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_077_cheetah_baseline_s0 --steps 105000 --seed 0 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-25T14:07:47.479Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T14:07:53.264245+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 448.1, \"eval_trajectory\": {\"5K\": 12.2, \"15K\": 18.4, \"25K\": 182.9, \"35K\": 356, \"45K\": 377.2, \"55K\": 441, \"65K\": 317.3, \"75K\": 340.9, \"85K\": 309.3, \"95K\": 418.4, \"105K\": 448.1}, \"ve_ratio_105K\": 0.611, \"ve_ratio_peak\": 0.739, \"ve_ratio_peak_step\": \"85K\", \"civo_alert\": 0, \"model_loss_105K\": 1.83, \"total_steps\": 112000}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_077_cheetah_baseline_s0/latest.pt\", \"completed_at\": \"2026-05-25T14:12:41.181Z\"}, \"exp_079_frozen_dt_emb_walker_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:27.865Z\", \"updated_at\": \"2026-05-25T18:06:36.594Z\", \"hypothesis\": \"Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Walker Walk does not trigger CIVO — proving dt_emb TRAINING is the necessary condition for CIVO onset. Duplicate of exp_067, killed before completion.\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"parent\": \"exp_067_frozen_dt_emb_walker_plan015\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_079_frozen_dt_emb_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"283090\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_079_frozen_dt_emb_walker_s0.log\", \"submitted_at\": \"2026-05-25T11:21:37.918Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 392.1, \"gpu_hours\": 0.11}, \"pid\": \"283090\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_079_frozen_dt_emb_walker_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_079_frozen_dt_emb_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T11:28:10.029Z\"}, \"exp_081_008e_v3_walker_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T12:09:44.566Z\", \"updated_at\": \"2026-05-25T15:49:23.869Z\", \"hypothesis\": \"Trained dt_emb with dt=1 imagination + subsample ON (max_dt=2) + H=15 does not trigger CIVO on Walker Walk — multi-seed validation seed=2 of C6 mitigation config 008e_v3\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_081_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"285949\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\", \"submitted_at\": \"2026-05-25T12:10:38.467Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 2, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_source\": \"N/A (training from scratch, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\", \"wall_clock_seconds\": 13125.4, \"gpu_hours\": 3.65}, \"reproduce\": {\"finished_at\": \"2026-05-25T15:37:00.120Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T15:37:06.073794+00:00\"}]}, \"metrics\": {\"eval_return_105k\": 597.1, \"ve_ratio_105k\": 0.5, \"civo_alert\": 0, \"gate_dt_1_frac\": 1, \"baseline_pct\": 64.2, \"train_return_112k_mean\": 583.8}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_081_008e_v3_walker_s2/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-25T15:49:23.870Z\"}, \"exp_080_008e_v3_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:30:20.594Z\", \"updated_at\": \"2026-05-25T15:49:21.640Z\", \"hypothesis\": \"Trained dt_emb with dt=1 imagination + subsample ON (max_dt=2) + H=15 does not trigger CIVO on Walker Walk — multi-seed validation seed=1 of C6 mitigation config 008e_v3\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_080_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"283925\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_080_008e_v3_walker_s1.log\", \"submitted_at\": \"2026-05-25T11:30:51.090Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 1, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_source\": \"N/A (training from scratch, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\", \"wall_clock_seconds\": 15510.5, \"gpu_hours\": 4.31}, \"reproduce\": {\"finished_at\": \"2026-05-25T15:44:00.217Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T15:44:06.170688+00:00\"}]}, \"metrics\": {\"eval_return_105k\": 876.7, \"ve_ratio_105k\": 0.6, \"civo_alert\": 0, \"gate_dt_1_frac\": 1, \"baseline_pct\": 94.3, \"train_return_112k_mean\": 926.8}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_080_008e_v3_walker_s1/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_080_008e_v3_walker_s1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T15:49:21.640Z\"}, \"exp_074_008a_walker_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:08:57.028Z\", \"updated_at\": \"2026-05-25T12:08:22.221Z\", \"hypothesis\": \"Walker Walk 008a 配置 (trained dt_emb unexposed + subsample OFF + dt=2 + H=15) seed=3。当前 008a 3 seeds 全部 success (no CIVO)，加 seed=3 巩固 C3 value suppression claim 统计。来源: plan_013 扩展。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_074_008a_walker_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"274730\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_074_008a_walker_s3.log\", \"submitted_at\": \"2026-05-25T09:09:28.652Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10733.6, \"gpu_hours\": 2.98}, \"pid\": \"274730\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_074_008a_walker_s3.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_074_008a_walker_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T12:04:22.816Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:04:34.186555+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 855.9, \"civo_ve_ratio_final\": 0.3, \"civo_alert\": 0, \"value_mean_105K\": 295.2, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"model_loss_105K\": 3.8, \"eval_trajectory\": {\"5K\": 36.1, \"15K\": 281, \"25K\": 389.8, \"35K\": 303.8, \"45K\": 437.3, \"55K\": 411.3, \"65K\": 566.4, \"75K\": 513.9, \"85K\": 645.9, \"95K\": 776.6, \"105K\": 855.9}, \"four_seed_summary\": {\"mean_eval_return\": 791, \"std_eval_return\": 102.2, \"all_civo_alert_0\": true, \"seeds_completed\": 4}}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_074_008a_walker_s3/latest.pt\", \"completed_at\": \"2026-05-25T12:08:22.221Z\"}, \"exp_076_cheetah_civo_trigger_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:03:42.328Z\", \"updated_at\": \"2026-05-25T10:48:15.566Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=2: trained dt_emb + subsample ON + dt=2 + H=8。将 Cheetah CIVO trigger 扩展到第 3 个独立 seed，巩固跨环境 claim 统计力度。来源: plan_021 扩展。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_076_cheetah_civo_trigger_s3 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"19953\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_076_cheetah_civo_trigger_s3.log\", \"submitted_at\": \"2026-05-25T10:44:40.370Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 215.2, \"gpu_hours\": 0.06}, \"pid\": \"19953\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_076_cheetah_civo_trigger_s3.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_076_cheetah_civo_trigger_s3 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T10:48:15.566Z\"}, \"exp_075_cheetah_civo_trigger_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:03:40.222Z\", \"updated_at\": \"2026-05-25T10:48:13.465Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=1: trained dt_emb + subsample ON + dt=2 + H=8 on westd-19154。复现 exp_010b 配置（原 seed=1 在 bjb1-45299），跨服务器验证 Cheetah CIVO 可复现性。来源: plan_021 扩展。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_075_cheetah_civo_trigger_s2 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"19788\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_075_cheetah_civo_trigger_s2.log\", \"submitted_at\": \"2026-05-25T10:44:34.345Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 219.1, \"gpu_hours\": 0.06}, \"pid\": \"19788\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_075_cheetah_civo_trigger_s2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_075_cheetah_civo_trigger_s2 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T10:48:13.465Z\"}, \"exp_071_008f_walker_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:03:48.097Z\", \"updated_at\": \"2026-05-25T10:42:39.889Z\", \"hypothesis\": \"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=3。当前 008f 2 seeds 结果分歧（s1=success eval=503, s2=negative eval=148），增加 seed 缩窄 causal control 稳定性估计。来源: plan_012 扩展。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_071_008f_walker_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"265628\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_071_008f_walker_s3.log\", \"submitted_at\": \"2026-05-25T07:04:24.723Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13095.2, \"gpu_hours\": 3.64}, \"pid\": \"265628\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_071_008f_walker_s3.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_071_008f_walker_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T10:05:58.573Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T10:06:05.930693+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 311.9, \"eval_return_peak\": 457.7, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 0.7, \"gate_dt_mean_final\": 2, \"civo_alert\": 0, \"value_loss_final\": 1, \"actor_entropy_final\": -4.6, \"model_loss_final\": 4.5}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_071_008f_walker_s3\", \"completed_at\": \"2026-05-25T10:42:39.889Z\"}, \"exp_073_008f_walker_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:30:42.251Z\", \"updated_at\": \"2026-05-25T10:00:42.604Z\", \"hypothesis\": \"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=4。当前 008f 0/3 CIVO onset，扩到 seed=4 进一步巩固 control 组统计。来源: plan_012 扩展。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_073_008f_walker_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"11670\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_073_008f_walker_s4.log\", \"submitted_at\": \"2026-05-25T07:31:11.391Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8971.2, \"gpu_hours\": 2.49}, \"pid\": \"11670\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_073_008f_walker_s4.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_073_008f_walker_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-25T09:48:03.882Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T09:48:13.191417+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_073_008f_walker_s4\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 289.3, \"eval_return_peak\": 486.5, \"eval_return_peak_step\": 75000, \"ve_ratio_final\": 0.5, \"ve_ratio_peak\": 0.5, \"nve_peak\": 0.76, \"civo_alert\": 0, \"civo\": false, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"gate_empirical_entropy\": 0, \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 33.2}, {\"step\": 15000, \"eval_return\": 128.3}, {\"step\": 25000, \"eval_return\": 165.3}, {\"step\": 35000, \"eval_return\": 284.5}, {\"step\": 45000, \"eval_return\": 272.5}, {\"step\": 55000, \"eval_return\": 406.7}, {\"step\": 65000, \"eval_return\": 379.5}, {\"step\": 75000, \"eval_return\": 486.5}, {\"step\": 85000, \"eval_return\": 352.6}, {\"step\": 95000, \"eval_return\": 297.7}, {\"step\": 105000, \"eval_return\": 289.3}]}, \"completed_at\": \"2026-05-25T10:00:42.604Z\"}, \"exp_072_008e_v3_walker_s5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:24:08.174Z\", \"updated_at\": \"2026-05-25T10:00:39.306Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation 配置 (trained dt_emb + subsample ON + dt=1 imag + H=15) seed=5。当前 5 seeds 测试 collapse rate=2/5 (40%)，加 seed=5 缩窄置信区间。来源: plan_016 扩展。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_072_008e_v3_walker_s5 --steps 105000 --seed 5 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"11116\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_072_008e_v3_walker_s5.log\", \"submitted_at\": \"2026-05-25T07:24:40.695Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9358.6, \"gpu_hours\": 2.6}, \"pid\": \"11116\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_072_008e_v3_walker_s5.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_072_008e_v3_walker_s5 --steps 105000 --seed 5 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-25T09:47:34.147Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T09:47:39.804739+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_072_008e_v3_walker_s5\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 853.1, \"eval_return_peak\": 853.1, \"eval_return_peak_step\": 105000, \"ve_ratio_final\": 0.6, \"nve_final\": 0.61, \"nve_peak\": 0.61, \"nve_peak_step\": 105000, \"civo_alert\": 0, \"civo\": false, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"actor_entropy_final\": -5.1, \"value_mean_final\": 520.8, \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 29.4}, {\"step\": 15000, \"eval_return\": 251.1}, {\"step\": 25000, \"eval_return\": 423}, {\"step\": 35000, \"eval_return\": 511}, {\"step\": 45000, \"eval_return\": 600.1}, {\"step\": 55000, \"eval_return\": 649}, {\"step\": 65000, \"eval_return\": 697.2}, {\"step\": 75000, \"eval_return\": 727.3}, {\"step\": 85000, \"eval_return\": 710.3}, {\"step\": 95000, \"eval_return\": 803.9}, {\"step\": 105000, \"eval_return\": 853.1}]}, \"completed_at\": \"2026-05-25T10:00:39.306Z\"}, \"exp_070_008e_v3_walker_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:07:49.050Z\", \"updated_at\": \"2026-05-25T08:54:47.019Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation 配置 (trained dt_emb + subsample ON + dt=1 imag + H=15) seed=0。当前 4 unique seeds 测试结果 collapse rate=2/4 (50%)，加 seed=0 缩窄置信区间。来源: plan_016 扩展。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_070_008e_v3_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"260999\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_070_008e_v3_walker_s0.log\", \"submitted_at\": \"2026-05-25T05:29:11.281Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12335.7, \"gpu_hours\": 3.43}, \"pid\": \"260999\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_070_008e_v3_walker_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_070_008e_v3_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T08:50:11.463Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T08:50:17.078252+00:00\"}]}, \"metrics\": {\"eval_return\": 148, \"peak_eval_return\": 232.5, \"peak_eval_step\": 55000, \"ve_ratio_105k\": 0.8, \"nve_peak\": 0.8, \"nve_peak_step\": 95000, \"civo\": false, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"actor_entropy_final\": -3.7, \"value_mean_final\": 122.1, \"failure_mode\": \"non-CIVO learning failure (never reached baseline performance)\", \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 37.4}, {\"step\": 15000, \"eval_return\": 93.2}, {\"step\": 25000, \"eval_return\": 178.8}, {\"step\": 35000, \"eval_return\": 221.6}, {\"step\": 45000, \"eval_return\": 230.9}, {\"step\": 55000, \"eval_return\": 232.5}, {\"step\": 65000, \"eval_return\": 194}, {\"step\": 75000, \"eval_return\": 175.2}, {\"step\": 85000, \"eval_return\": 218.6}, {\"step\": 95000, \"eval_return\": 139.6}, {\"step\": 105000, \"eval_return\": 148}], \"ve_ratio_trajectory\": [{\"step\": 15000, \"ve\": 0}, {\"step\": 25000, \"ve\": 0.1}, {\"step\": 35000, \"ve\": 0.2}, {\"step\": 45000, \"ve\": 0.3}, {\"step\": 55000, \"ve\": 0.4}, {\"step\": 65000, \"ve\": 0.5}, {\"step\": 75000, \"ve\": 0.6}, {\"step\": 85000, \"ve\": 0.5}, {\"step\": 95000, \"ve\": 0.8}, {\"step\": 105000, \"ve\": 0.8}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_070_008e_v3_walker_s0/latest.pt\", \"conclusion\": \"negative\", \"notes\": \"Seed 0 FAILED but NOT via CIVO. eval_return peaked at 232.5@55K (far below baseline ~500+), declined to 148@105K. ve_ratio stayed healthy throughout (max 0.8, never triggered CIVO alert). Gate locked dt=1. This is a distinct failure mode from seeds 2,3 (which had CIVO collapse with NVE>3.7x). Agent never reached high performance — learning stagnated early. Cross-seed 008e_v3 summary: 5 seeds tested, 2 success (s1=870, s4=899), 2 CIVO collapse (s2=137 NVE=3.78, s3=93 NVE=4.02), 1 non-CIVO failure (s0=148 NVE=0.8). CIVO collapse rate: 2/5=40%. Overall failure rate: 3/5=60%.\", \"completed_at\": \"2026-05-25T08:54:47.019Z\"}, \"exp_069_008f_walker_repro_s1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-25T03:49:41.282Z\", \"updated_at\": \"2026-05-25T07:28:33.676Z\", \"hypothesis\": \"Reproducing 008f config (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will NOT trigger CIVO (NVE < 1.5x) because removing dt_emb eliminates the temporal abstraction mismatch that drives value error amplification\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"failure_reason\": \"bjb1-40020 服务器不可达（SSH 连接 port 40020 on 106.120.183.117 失败），进程无法监控，未产生有效 W&B metrics\", \"completed_at\": \"2026-05-25T04:17:38.829Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-25T04:17:43.081459+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T07:17:09.809673+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_069_008f_walker_repro_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"4590\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_069_008f_walker_repro_s1.log\", \"submitted_at\": \"2026-05-25T05:04:10.980Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8662.7, \"gpu_hours\": 2.41}, \"pid\": \"4590\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_069_008f_walker_repro_s1.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_069_008f_walker_repro_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-25T07:17:02.903Z\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_069_008f_walker_repro_s1/latest.pt\", \"metrics\": {\"eval_return_final\": 237.8, \"eval_return_peak\": 390.1, \"eval_return_peak_step\": 95000, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 0.4, \"ve_ratio_peak_step\": 105000, \"nve_final_105k\": 0.61, \"nve_peak\": 0.66, \"nve_peak_step\": 75000, \"civo_alert\": false, \"gate_dt_2_frac\": 1, \"eval_trajectory\": {\"5k\": 30.5, \"15k\": 158.7, \"25k\": 180.8, \"35k\": 250.3, \"45k\": 293.6, \"55k\": 272.2, \"65k\": 328.1, \"75k\": 244.8, \"85k\": 382.5, \"95k\": 390.1, \"105k\": 237.8}, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.1, \"35k\": 0.2, \"45k\": 0.2, \"55k\": 0.3, \"65k\": 0.3, \"75k\": 0.4, \"85k\": 0.3, \"95k\": 0.3, \"105k\": 0.4}}, \"conclusion\": \"success\"}, \"exp_068_008d_walker_repro_s1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-25T03:49:39.539Z\", \"updated_at\": \"2026-05-25T07:28:31.319Z\", \"hypothesis\": \"Reproducing 008d config (trained dt_emb + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will trigger CIVO (NVE > 1.5x) because trained dt_emb enables value error amplification through temporal abstraction mismatch\", \"parent\": \"exp_008d_subsample_on_h8\", \"failure_reason\": \"SSH check failed 5x — last error: [Errno None] Unable to connect to port 40020 on 106.120.183.117\", \"completed_at\": \"2026-05-25T04:18:15.954Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-25T04:18:20.002698+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T07:23:04.341146+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_068_008d_walker_repro_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"4425\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_068_008d_walker_repro_s1.log\", \"submitted_at\": \"2026-05-25T05:04:05.168Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8666.2, \"gpu_hours\": 2.41}, \"pid\": \"4425\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_068_008d_walker_repro_s1.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_068_008d_walker_repro_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-25T07:22:57.100Z\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_068_008d_walker_repro_s1/latest.pt\", \"metrics\": {\"eval_return_final\": 39.1, \"eval_return_peak\": 192.4, \"eval_return_peak_step\": 55000, \"ve_ratio_final\": 2.7, \"ve_ratio_peak\": 4.6, \"ve_ratio_peak_step\": 85000, \"nve_final_105k\": 4.12, \"nve_peak_85k\": 6.57, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.81, \"civo_alert\": true, \"civo_alert_step\": 85000, \"gate_dt_2_frac\": 1, \"eval_trajectory\": {\"5k\": 31, \"15k\": 146.5, \"25k\": 174.1, \"35k\": 189.6, \"45k\": 142.2, \"55k\": 192.4, \"65k\": 114.4, \"75k\": 106.6, \"85k\": 33.4, \"95k\": 26.9, \"105k\": 39.1}, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.2, \"35k\": 0.3, \"45k\": 0.6, \"55k\": 0.6, \"65k\": 1.3, \"75k\": 1.6, \"85k\": 4.6, \"95k\": 4.6, \"105k\": 2.7}}, \"conclusion\": \"success\"}, \"exp_067_frozen_dt_emb_walker_plan015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T03:49:37.736Z\", \"updated_at\": \"2026-05-25T06:59:24.006Z\", \"hypothesis\": \"Frozen (requires_grad=False) dt_embedding + subsample ON + dt=2 + H=8 在 Walker Walk 上不触发 CIVO，验证 dt_emb 的 TRAINING 是 CIVO 的必要条件（而非 dt_emb 的存在本身）。来源: plan_015。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-25T03:51:43.628Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_067_frozen_dt_emb_walker_plan015 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T06:54:52.150Z\", \"training_hours\": 3.05}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_067_frozen_dt_emb_walker_plan015 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"255883\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_067_frozen_dt_emb_walker_plan015.log\", \"submitted_at\": \"2026-05-25T03:52:29.860Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11214.1, \"gpu_hours\": 3.12}, \"pid\": \"255883\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_067_frozen_dt_emb_walker_plan015.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T06:54:57.723176+00:00\"}]}, \"metrics\": {\"eval_final\": 281.5, \"eval_peak\": 334.1, \"eval_peak_step\": 95000, \"nve_peak\": 0.4, \"nve_final\": 0.2, \"civo_alert\": 0, \"total_env_steps\": 112000, \"update_count\": 25099, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_067_frozen_dt_emb_walker_plan015/latest.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T06:59:24.006Z\"}, \"exp_066b_timeseries_rssm_fidelity_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:34:14.574Z\", \"updated_at\": \"2026-05-25T04:35:12.673Z\", \"hypothesis\": \"RSSM fidelity gap (dt=2 prediction error > dt=1) emerges before value overestimation in seed=1, replicating the causal chain found in exp_066 seed=0 and confirming cross-seed robustness of the fidelity→VE mechanism.\", \"parent\": \"exp_066_timeseries_rssm_fidelity\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_066b_timeseries_rssm_fidelity_s1 --steps 60000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 5000 --eval_every 5000\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"252133\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_066b_timeseries_rssm_fidelity_s1.log\", \"submitted_at\": \"2026-05-25T02:38:44.421Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6988.3, \"gpu_hours\": 1.94}, \"pid\": \"252133\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_066b_timeseries_rssm_fidelity_s1.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_066b_timeseries_rssm_fidelity_s1 --steps 60000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 5000 --eval_every 5000\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T04:18:02.308Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T04:18:10.617905+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_066b_timeseries_rssm_fidelity_s1/checkpoint_65000.pt\", \"metrics\": {\"seed\": 1, \"steps_completed\": 65000, \"eval_return_peak\": 201.9, \"eval_return_peak_step\": 45000, \"eval_return_final\": 160.7, \"civo_alert_step\": 55000, \"ve_ratio_final\": 0.724, \"fidelity_gap_timeseries\": {\"ss_ratio_10K\": 0.887, \"ss_ratio_15K\": 1.017, \"ss_ratio_20K\": 1.216, \"ss_ratio_25K\": 1.532, \"ss_ratio_30K\": 1.374, \"ss_ratio_35K\": 1.486, \"ss_ratio_40K\": 1.428, \"ss_ratio_45K\": 1.38, \"ss_ratio_50K\": 1.468, \"ss_ratio_55K\": 1.517, \"ss_ratio_60K\": 1.799, \"ss_ratio_65K\": 1.756}, \"ve_ratio_timeseries\": {\"12K\": 0.012, \"15K\": 0.033, \"24K\": 0.118, \"25K\": 0.193, \"35K\": 0.269, \"45K\": 0.358, \"52K\": 0.495, \"55K\": 0.71, \"64K\": 0.724}, \"fidelity_gap_onset_step\": 15000, \"ve_onset_step\": 24000, \"temporal_lead_steps\": 9000, \"causal_direction\": \"fidelity_gap_leads_ve\", \"cross_seed_comparison\": {\"s0_ss_ratio_65K\": 1.678, \"s1_ss_ratio_65K\": 1.756, \"s0_fidelity_onset\": 20000, \"s1_fidelity_onset\": 15000, \"s0_ve_onset\": 30000, \"s1_ve_onset\": 24000, \"s0_temporal_lead\": 10000, \"s1_temporal_lead\": 9000, \"pattern_consistent\": true}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T04:35:12.673Z\"}, \"exp_062_cartpole_control\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T16:01:08.858Z\", \"updated_at\": \"2026-05-25T03:45:35.194Z\", \"hypothesis\": \"dt_embed_dim=0 + subsample ON + H=8 在 Cartpole Swingup 上不触发 CIVO（NVE < 1.5x），因果控制实验验证移除 dt_emb 是否阻止 CIVO 在第三个环境中泛化。与 exp_061 配对形成因果对比。\", \"spec\": {\"command\": \"bash -c 'for SEED in 0 1 2; do python -u dreamer.py --configs defaults dmc_proprio --task dmc_cartpole_swingup --logdir logdir/exp_062_cartpole_control_s${SEED} --steps 105000 --seed $SEED --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000; done'\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:0\"], \"pid\": \"473913\", \"log_path\": \"bjb1-40020:~/runs/event-gated-adaptive-horizon/exp_062_cartpole_control.log\", \"submitted_at\": \"2026-05-24T16:26:50.780Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cartpole_swingup\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (dt_embed_dim=0, control, Cartpole Swingup)\", \"seed\": \"0,1,2\", \"gpu_ids\": [0], \"checkpoint_path\": \"bjb1-40020:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_062_cartpole_control_s0/checkpoint.pt\", \"wall_clock_seconds\": 40686.6, \"gpu_hours\": 11.3}, \"metrics\": {\"seeds\": {\"s0\": {\"eval_return\": 230.4, \"ve_ratio_peak\": 0.069, \"ve_ratio_final\": 0.056, \"value_mean\": 12.9, \"civo_detected\": false}, \"s1\": {\"eval_return\": 255.3, \"ve_ratio_peak\": 0.079, \"ve_ratio_final\": 0.04, \"value_mean\": 10.2, \"civo_detected\": false}, \"s2\": {\"eval_return\": 248.8, \"ve_ratio_peak\": 0.065, \"ve_ratio_final\": 0.048, \"value_mean\": 11.8, \"civo_detected\": false}}, \"mean_eval_return\": 244.8, \"mean_ve_ratio_peak\": 0.071, \"civo_detected_any\": false, \"steps_completed\": 112000}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-25T03:44:57.338Z\"}, \"exp_061_cartpole_civo_trigger\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-24T16:01:07.009Z\", \"updated_at\": \"2026-05-25T03:18:38.759Z\", \"hypothesis\": \"Trained dt_emb (d=32) + subsample ON + H=8 + dt=2 imagination 在 Cartpole Swingup 上触发 CIVO（NVE > 1.5x），验证 CIVO 是否跨 locomotion 子类环境泛化（Walker/Cheetah 已确认，Cartpole 是第三个 DMC locomotion 环境）。与 exp_062 配对形成因果对比。\", \"spec\": {\"command\": \"bash -c '... --device cuda:0 ...'\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"226158\", \"log_path\": \"bjb1-45299:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_061_cartpole_civo_trigger_s{0,1,2}/\", \"submitted_at\": \"2026-05-24T16:50:56.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cartpole_swingup\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO trigger, Cartpole Swingup)\", \"seed\": \"0,1,2\", \"gpu_ids\": [1], \"checkpoint_path\": \"bjb1-45299:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_061_cartpole_civo_trigger_s{0,1,2}/latest.pt\", \"wall_clock_seconds\": 39600, \"gpu_hours\": 11}, \"conclusion\": \"negative\", \"metrics\": {\"seeds\": 3, \"steps_per_seed\": 112000, \"s0_eval_return_final\": 211.1, \"s0_eval_return_peak\": 247.8, \"s0_value_mean_final\": 9.229, \"s0_ve_ratio_peak\": 0.058, \"s0_train_return_final\": 199.2, \"s1_eval_return_final\": 269, \"s1_eval_return_peak\": 328.1, \"s1_value_mean_final\": 9.323, \"s1_ve_ratio_peak\": 0.04, \"s1_train_return_final\": 188.7, \"s2_eval_return_final\": 228.9, \"s2_eval_return_peak\": 245.9, \"s2_value_mean_final\": 9.46, \"s2_ve_ratio_peak\": 0.043, \"s2_train_return_final\": 258.9, \"civo_detected\": false, \"civo_alert_any_seed\": false, \"ve_ratio_max_all_seeds\": 0.058, \"vs_baseline_eval_mean\": \"-56.3%\", \"baseline_exp060_eval_s2_105K\": 557}, \"completed_at\": \"2026-05-25T03:18:38.759Z\"}, \"exp_008d_subsample_on_h8\": {\"completed_at\": \"2026-05-14T04:50:52.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:46:57.960Z\", \"hypothesis\": \"Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestimate through dt-conditioned representation co-adaptation, leading to policy collapse.\", \"metrics\": {\"actor_loss_25K\": -0.195, \"actor_loss_35K\": -0.17, \"baseline_35K\": 400, \"baseline_45K\": 443, \"data_source_45K\": \"from training logs metrics.jsonl\", \"eval_return_25K\": 167.22, \"eval_return_35K\": 146.34, \"eval_return_45K\": 140.8, \"eval_return_55K\": 82.75, \"model_loss_25K\": 5.33, \"model_loss_35K\": 5.07, \"step\": 55000, \"trend\": \"eval declining 167→146→141→83; v/e accelerating 15.5%→41.2%→69.3%→167% — delusional critic collapse confirmed, value exceeds eval_return at 55K\", \"value_eval_ratio_25K\": 0.155, \"value_eval_ratio_35K\": 0.411, \"value_eval_ratio_45K\": 0.693, \"value_eval_ratio_55K\": 1.666, \"value_mean_25K\": 25.86, \"value_mean_35K\": 60.2, \"value_mean_45K\": 97.5, \"value_mean_55K\": 137.88, \"verdict_35K\": \"WARN_COLLAPSE\", \"verdict_45K\": \"COLLAPSE_CONFIRMED\", \"vs_baseline_35K\": \"-63.4%\", \"vs_baseline_45K\": \"-68.2%\"}, \"parent\": \"exp_005_event_gated_v4\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008d_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.48, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8)\", \"pid\": \"109519\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T02:21:59.852Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8932.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-25T02:41:05.620Z\", \"notes\": \"RSSM fidelity analysis (exp_063, 55K checkpoint only): dt=2/dt=1 single-step reward MAE ratio = 2.695x (vs exp_066 s0's 1.37x at same step). Larger fidelity gap correlates with worse VE (1.666 vs 0.621). No intermediate checkpoints exist — cannot directly verify 25K fidelity gap for this seed. Cross-seed pattern consistent: VE trajectory matches s0 (low at 25K, collapse by 55K). See artifact art_20260525_e45921.\"}, \"exp_066_timeseries_rssm_fidelity\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-24T21:07:53.125Z\", \"updated_at\": \"2026-05-25T02:33:00.783Z\", \"hypothesis\": \"Trained dt_embedding causes RSSM fidelity degradation (dt=2 vs dt=1 reward MAE gap) that progressively worsens during training, and its temporal evolution precedes or synchronizes with NVE (value overestimation) rise, establishing a temporal causal chain: RSSM fidelity gap → value overestimation.\", \"parent\": \"exp_063_rssm_fidelity\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-24T22:27:54.087Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/dreamerv3-torch && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_066_timeseries_rssm_fidelity_s0 --steps 60000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 5000 --eval_every 999999\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-24T22:28:15.966Z\", \"training_hours\": 0.01}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-24T22:28:19.155Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T22:28:24.279787+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_066_timeseries_rssm_fidelity_s0 --steps 60000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 5000 --eval_every 5000'\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"pid\": 490622, \"fix_note\": \"eval_every changed from 999999 to 5000 — checkpoint saving is coupled to eval loop, 999999 prevented checkpoints from being saved\", \"checkpoint_path\": \"bjb1-40020:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_066_timeseries_rssm_fidelity_s0/checkpoint.pt\", \"log_path\": \"bjb1-40020:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_066_timeseries_rssm_fidelity_s0/\"}, \"conclusion\": \"success\", \"metrics\": {\"ss_ratio_10K\": 1.047, \"ss_ratio_30K\": 1.247, \"ss_ratio_65K\": 1.678, \"ol_ratio_30K_peak\": 1.446, \"ol_ratio_35K_peak\": 1.509, \"ve_ratio_final\": 1.399, \"fidelity_gap_onset_step\": 20000, \"ve_onset_step\": 30000, \"temporal_lead_steps\": 10000, \"pearson_ss_ve\": 0.807, \"pearson_ss_ve_p\": 0.0015, \"pearson_ol_ve\": 0.425, \"pearson_ol_ve_p\": 0.169, \"ss_monotonicity\": 0.73, \"ol_monotonicity\": 0.73, \"ve_monotonicity\": 0.82, \"causal_direction\": \"fidelity_gap_leads_ve\", \"conclusion\": \"success\"}}, \"exp_060_cartpole_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T16:01:05.099Z\", \"updated_at\": \"2026-05-25T01:25:39.711Z\", \"hypothesis\": \"Cartpole Swingup (DMC) baseline dt=1 建立 v/e ratio 校准基线，用于 CIVO 诊断阈值在第三个 DMC 环境的验证。预期 NVE 保持在 1.0x 附近，无 CIVO 现象。\", \"spec\": {\"command\": \"bash -c 'for SEED in 0 1 2; do python -u dreamer.py --configs defaults dmc_proprio --task dmc_cartpole_swingup --logdir logdir/exp_060_cartpole_baseline_s${SEED} --steps 105000 --seed $SEED --compile False --device cuda:0 --checkpoint_every 25000; done'\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"223294\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_060_cartpole_baseline.log\", \"submitted_at\": \"2026-05-24T16:26:42.610Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cartpole_swingup\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (vanilla baseline, Cartpole Swingup)\", \"seed\": \"0,1,2\", \"gpu_ids\": [0], \"wall_clock_seconds\": 32337.1, \"gpu_hours\": 8.98}, \"conclusion\": \"success\", \"metrics\": {\"seeds\": 3, \"steps_per_seed\": 112000, \"train_return_s0\": 809.4, \"train_return_s1\": 684.4, \"train_return_s2\": 526.1, \"eval_return_s2_105K\": 557}, \"checkpoint_path\": \"bjb1-45299:/root/dreamerv3-torch/logdir/exp_060_cartpole_baseline_s{0,1,2}/latest.pt\", \"log_path\": \"bjb1-45299:/root/dreamerv3-torch/logdir/exp_060_cartpole_baseline_s{0,1,2}/metrics.jsonl\", \"completed_at\": \"2026-05-25T01:25:39.711Z\"}, \"exp_065_dt_emb_cosine\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:48:47.693Z\", \"updated_at\": \"2026-05-24T20:54:51.678Z\", \"hypothesis\": \"分析 trained dt_embedding 中 dt=1 vs dt=2 向量的 cosine similarity 及其训练过程演化。如果 cosine sim 高（接近 1）→ dt_emb 未学到有意义区分，CIVO 来自微小差异被 downstream 放大；如果 cosine sim 低 → dt_emb 学到了显著不同的表征，CIVO 来自 dt=2 表征本身的偏差。\", \"conclusion\": \"success\", \"checkpoint_path\": \"logdir/exp_065_dt_emb_cosine/results.json\", \"log_path\": \"bjb1-45299:/root/dreamerv3-torch/logdir/exp_065_dt_emb_cosine/\", \"completed_at\": \"2026-05-24T20:52:24.863Z\", \"metrics\": {\"trained_cosine_sim_range\": \"-0.94 to -0.70\", \"frozen_cosine_sim_range\": \"-0.15 to +0.07\", \"trained_trend\": \"strong negative (near-opposite directions)\", \"frozen_trend\": \"near-zero constant\", \"conclusion\": \"dt=1 and dt=2 embeddings learn nearly opposite representations; CIVO from dt=2 representation bias, not amplified micro-differences\"}}, \"exp_064_value_distribution\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T19:23:05.483Z\", \"updated_at\": \"2026-05-24T20:14:50.460Z\", \"hypothesis\": \"V(s) vs Monte Carlo return 分布对比：trained dt_emb (exp_008d collapsed) 的 value estimate 在 dt=2 imagination 步骤系统性高估，而 untrained/absent dt_emb (exp_008f control) 和 baseline (exp_001) 的 value 分布与 MC return 紧密跟踪。直观展示 CIVO 的 value divergence 位置和形态。\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-24T19:56:27.179Z\"}, \"spec\": {\"command\": \"python scripts/value_distribution_analysis.py --device cuda:0\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_001_baseline + logdir/exp_008d + logdir/exp_008f\", \"data_count\": 500, \"model_name\": \"DreamerV3 (baseline + collapsed + control checkpoints)\", \"seed\": 0, \"gpu_ids\": [1], \"checkpoint_path\": \"logdir/exp_064_value_distribution/\", \"log_path\": \"logdir/exp_064_value_distribution/results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"baseline_bias\": 344.85, \"baseline_rmse\": 371.73, \"baseline_overest_pct\": 100, \"baseline_v_mc_ratio\": 3.31, \"civo_bias\": 108.99, \"civo_rmse\": 112.36, \"civo_overest_pct\": 100, \"civo_v_mc_ratio\": 7.8, \"civo_v_mc_median\": 3.4, \"control_bias\": -6.51, \"control_rmse\": 57.93, \"control_overest_pct\": 52.5, \"control_v_mc_ratio\": 2.58, \"control_v_mc_median\": 1.05}, \"completed_at\": \"2026-05-24T20:14:50.460Z\"}, \"exp_063_rssm_fidelity\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T18:12:47.163Z\", \"updated_at\": \"2026-05-24T19:21:37.837Z\", \"hypothesis\": \"RSSM 在 dt=2 transitions 上的 observation/reward reconstruction loss 显著高于 dt=1，量化 fidelity gap 作为 trained dt_emb 导致 delusional critic 的机械性基础。从 exp_001 (baseline) 和 exp_008d (collapsed) 的已有 checkpoint 提取，对比 dt=1 vs dt=2 prediction quality。\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-24T18:53:48.781Z\"}, \"spec\": {\"command\": \"python scripts/rssm_fidelity_analysis.py --device cuda:0\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_001_baseline + logdir/exp_008d_subsample_on_h8\", \"data_count\": 500, \"model_name\": \"DreamerV3 RSSM (baseline + collapsed checkpoints)\", \"seed\": 0, \"gpu_ids\": [1], \"checkpoint_path\": \"logdir/exp_063_rssm_fidelity/results.json\", \"log_path\": \"logdir/exp_063_rssm_fidelity/results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"baseline_dt1_obs_mse\": 13.7, \"baseline_dt2_obs_mse\": 20.62, \"baseline_dt2_dt1_ratio_obs\": 1.505, \"baseline_dt2_dt1_ratio_reward\": 1.483, \"collapsed_dt1_obs_mse\": 26.93, \"collapsed_dt2_single_obs_mse\": 42.02, \"collapsed_dt2_single_reward_mae\": 0.146, \"collapsed_dt2_dt1_ratio_obs\": 1.56, \"collapsed_dt2_dt1_ratio_reward\": 2.695, \"collapsed_single_vs_chained_obs\": 1.138, \"collapsed_single_vs_chained_reward\": 1.926}, \"completed_at\": \"2026-05-24T19:21:37.837Z\"}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:30:00.000Z\", \"updated_at\": \"2026-05-24T16:53:23.046Z\", \"hypothesis\": \"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks. If frozen prevents CIVO → extends Walker/Cheetah frozen finding to manipulation; if not → domain-specific factors override dt_emb mechanism.\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 305974, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0.log\", \"checkpoint_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0/checkpoint_202500.pt\"}, \"metrics\": {\"eval_final\": 45.3, \"eval_final_step\": 212500, \"eval_peak\": 45.3, \"eval_peak_step\": 212500, \"ve_ratio_final\": 0.1, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 4.3, \"ve_ratio_peak_step\": 42500, \"total_steps\": 222400, \"nve_classification\": \"onset_self_correcting\", \"civo_transient\": true, \"civo_sustained\": false, \"civo_transient_range\": \"22K-62K\", \"civo_self_correction\": true, \"civo_self_correction_step\": 82500, \"gate_dt_mean\": 2, \"gate_dt_variation\": false, \"eval_dip_during_civo\": 7.1, \"eval_dip_step\": 42500}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T08:48:40.404Z\"}, \"exp_049_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:14:38.578Z\", \"updated_at\": \"2026-05-24T16:53:19.032Z\", \"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion 推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack）。如果触发 → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\", \"parent\": \"exp_048_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 91395, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_049_stackcube_civo_trigger_s0/train.log\"}, \"metrics\": {\"eval_final\": 34.88, \"eval_final_step\": 212500, \"eval_peak\": 35.89, \"eval_peak_step\": 182500, \"ve_ratio_final\": 0.186, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 5.048, \"ve_ratio_peak_step\": 42500, \"total_steps\": 222400, \"total_episodes\": 1112, \"nve_classification\": \"onset_self_correcting\", \"civo_transient\": true, \"civo_sustained\": false, \"civo_transient_range\": \"22K-72K\", \"civo_self_correction\": true, \"civo_self_correction_step\": 112500, \"gate_dt_mean\": 2, \"gate_dt_variation\": false, \"eval_dip_during_civo\": 4.93, \"eval_dip_step\": 62500}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_049_stackcube_civo_trigger_s0/checkpoint_202500.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_049_stackcube_civo_trigger_s0/metrics.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T04:23:01.339Z\"}, \"exp_057\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T16:49:35.310Z\", \"updated_at\": \"2026-05-24T16:50:44.968Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker seed=2, n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3 验证稳健性。\", \"parent\": \"\", \"spec\": {\"command\": \"python train.py --env walker --frozen_dt_emb --seed 2\", \"server\": \"bjb1-45299\", \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"data_count\": 225000, \"seed\": 2, \"model_name\": \"dreamer_frozen_dt_emb\"}, \"log_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\", \"metrics\": {\"eval_return_peak\": 221.7, \"eval_return_peak_step\": 195000, \"eval_return_final\": 123.9, \"eval_return_final_step\": 215000, \"nve_peak\": 1.3, \"nve_peak_step\": 115000, \"nve_final\": 0.2, \"civo_alert\": 0, \"civo_sustained\": false, \"civo_transient\": true, \"civo_transient_range\": \"115k-145k\", \"train_steps\": 225000, \"gate_dt_mean\": 2}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T16:50:44.968Z\"}, \"exp_008d_civo_trigger_s4\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s4/latest.pt\", \"completed_at\": \"2026-05-18T05:17:45.132Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:43.972Z\", \"hypothesis\": \"Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s4/metrics.jsonl\", \"metrics\": {\"ve_ratio_peak\": 3.0294, \"ve_ratio_peak_step\": 105000, \"ve_ratio_final\": 3.0294, \"ve_ratio_final_step\": 105000, \"nve_peak\": 4.62, \"nve_peak_step\": 105000, \"nve_peak_note\": \"step-matched s1 baseline @105K = 0.6564\", \"nve_classification\": \"onset_collapse\"}, \"parent\": \"exp_008d_civo_trigger_s3\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 4 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s4\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk_online\", \"gpu\": \"cuda:0\", \"model_name\": \"DreamerV3-walker-civo-trigger\", \"pid\": \"715124\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-24T08:56:41.239Z\"}, \"exp_059_walker_trained_s5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:08:46.842Z\", \"updated_at\": \"2026-05-24T07:46:59.075Z\", \"hypothesis\": \"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\", \"parent\": \"exp_008d_civo_trigger_s3\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 5 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir logdir/exp_059_walker_trained_s5\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"186176\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_059_walker_trained_s5.log\", \"submitted_at\": \"2026-05-24T03:15:40.649Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11526.3, \"gpu_hours\": 3.2}, \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"pid\": \"186176\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_059_walker_trained_s5.log\", \"reproduce\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 5 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir logdir/exp_059_walker_trained_s5\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-24T06:20:56.680Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T06:21:01.777871+00:00\"}]}, \"metrics\": {\"ve_ratio_peak\": 3.3075, \"ve_ratio_peak_step\": \"85K\", \"nve_peak\": 4.72, \"nve_peak_note\": \"step-matched s1 baseline @85K = 0.7007\", \"nve_classification\": \"onset_collapse\", \"nve_classification_note\": \"Reclassified from onset_self_correcting: NVE self-corrected but eval=95.8 (10.5% of baseline 913) indicates irreversible policy damage. Collapse†.\", \"nve_final\": 1.22, \"nve_final_note\": \"0.8/0.656 (step-matched s1 baseline @105K)\", \"eval_final\": 95.8, \"eval_baseline\": 913, \"eval_pct_baseline\": \"10.5%\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_059_walker_trained_s5/checkpoint.pt\", \"completed_at\": \"2026-05-24T06:27:46.992Z\", \"notes\": \"CIVO-positive under step-matched NVE (peak ≈ 5.0×). Self-correcting outcome (ve_ratio 3.3@85K → 0.8@105K in ~10K steps). Supports 5/5 Walker trained CIVO onset. Gate locked at dt=2 throughout (entropy=0).\"}, \"exp_057_frozen_dt_emb_walker_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:25:00.000Z\", \"updated_at\": \"2026-05-24T02:17:41.318Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 157775, \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s2)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\"}, \"completed_at\": \"2026-05-23T23:30:00.000Z\", \"metrics\": {\"total_steps\": 225000, \"ve_ratio_peak\": 1.283, \"ve_ratio_peak_step\": 115000, \"ve_ratio_final\": 0.177, \"ve_ratio_final_step\": 215000, \"nve_peak\": 1.88, \"nve_peak_step\": 115000, \"nve_classification\": \"transient\", \"eval_return_final\": 123.94, \"eval_return_final_step\": 215000, \"eval_return_peak\": 221.72, \"eval_return_peak_step\": 195000}}, \"exp_058_frozen_dt_emb_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:10:49.773Z\", \"updated_at\": \"2026-05-24T00:30:00.000Z\", \"hypothesis\": \"Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Cheetah frozen n=2 增强极端 CIVO 场景下 frozen diagnostic 的统计基础。\", \"parent\": \"exp_046_frozen_dt_emb_cheetah\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_058_frozen_dt_emb_cheetah_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 164830, \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Cheetah s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/train.log\", \"checkpoint_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/checkpoint_225000.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:30:00.000Z\", \"metrics\": {\"total_steps\": 224000, \"ve_ratio_peak\": 0.231, \"ve_ratio_peak_step\": 45000, \"ve_ratio_final\": 0.107, \"ve_ratio_final_step\": 215000, \"eval_return_final\": 80.46, \"eval_return_final_step\": 215000, \"eval_return_peak\": 191.74, \"eval_return_peak_step\": 25000, \"nve_peak\": 0.78, \"nve_peak_step\": 45000, \"nve_classification\": \"no_civo\", \"note\": \"Cheetah frozen s1. NVE=0.78× (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 — both clean, frozen 稳健阻止 extreme CIVO (trained NVE 70-108).\"}}, \"exp_056_peginsertion_frozen_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:02:23.683Z\", \"updated_at\": \"2026-05-24T00:00:00.000Z\", \"hypothesis\": \"D143 混合机制假说验证——PegInsertion frozen dt_emb 跨 seed 可复现性。exp_053 (s0) 显示 frozen 在 82.5K 回落到 1.82 而 trained 攀升到 10.05，s1 验证这个分叉是否可复现。如果 s1 也回落 → frozen 稳健阻止 dt_emb 放大；如果不回落 → seed-dependent。\", \"parent\": \"exp_053_peginsertion_frozen_s0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_056_peginsertion_frozen_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 346430, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_056_peginsertion_frozen_s1/train.log\", \"checkpoint_path\": \"logdir/exp_056_peginsertion_frozen_s1/checkpoint_202500.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:00:00.000Z\", \"metrics\": {\"total_steps\": 222500, \"ve_ratio_peak\": 11.321, \"ve_ratio_peak_step\": 82500, \"ve_ratio_final\": 1.193, \"ve_ratio_final_step\": 212500, \"eval_return_final\": 4.37, \"eval_return_final_step\": 212500, \"eval_return_peak\": 24.42, \"eval_return_peak_step\": 132500, \"nve_classification\": \"burst\", \"note\": \"Ordering reversal vs s0 confirms D146 seed-dependent noise. Frozen s1 burst 11.32 > trained s1 peak 3.08 — frozen does NOT suppress ManiSkill transients.\", \"ve_ratio_trajectory\": {\"12500\": 0.316, \"22500\": 0.975, \"32500\": 1.839, \"42500\": 1.966, \"52500\": 5.422, \"62500\": 4.047, \"72500\": 8.408, \"82500\": 11.321, \"92500\": 3.724, \"102500\": 3.034, \"112500\": 2.204, \"122500\": 2.425, \"132500\": 0.842, \"142500\": 2.194, \"152500\": 2.203, \"162500\": 0.651, \"172500\": 1.085, \"182500\": 1.07, \"192500\": 0.467, \"202500\": 0.708, \"212500\": 1.193}}}, \"exp_055_peginsertion_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:50:00.000Z\", \"updated_at\": \"2026-05-23T23:38:30.000Z\", \"hypothesis\": \"PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，最终自修复到 0.379@212.5K）。如果 s1 也触发持续 CIVO → PegInsertion CIVO 可复现；如果不触发 → seed-specific 异常。\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [0], \"pid\": 345223, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/train.log\"}, \"ve_ratio_peak\": \"3.08@92500\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T23:38:25.428Z\", \"metrics\": {\"total_steps\": 222400, \"ve_ratio_peak\": 3.08, \"ve_ratio_peak_step\": 92500, \"ve_ratio_final\": 0.498, \"ve_ratio_final_step\": 212500, \"eval_return_final\": 11.44, \"eval_return_final_step\": 212500, \"eval_return_peak\": 24.05, \"eval_return_peak_step\": 112500, \"nve_classification\": \"transient\", \"civo_triggered\": true, \"civo_self_corrected\": \"partial\", \"note\": \"CIVO triggered (peak 3.08@92.5K, less severe than s0=10.05). Partial self-correction to 0.498. PegInsertion trained cross-seed: s0=10.05, s1=3.08 — severity seed-dependent.\", \"ve_ratio_trajectory\": {\"12500\": 0.19, \"22500\": 0.81, \"32500\": 1.35, \"42500\": 2.0, \"52500\": 2.39, \"62500\": 2.85, \"72500\": 2.28, \"82500\": 2.48, \"92500\": 3.08, \"102500\": 2.51, \"112500\": 0.91, \"122500\": 1.21, \"132500\": 1.36, \"142500\": 0.75, \"152500\": 0.55, \"162500\": 1.17, \"172500\": 0.96, \"182500\": 0.94, \"192500\": 0.9, \"202500\": 0.73, \"212500\": 0.5}}, \"checkpoint_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/checkpoint_222500.pt\"}, \"exp_054_pickcube_frozen_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:47:24.310Z\", \"updated_at\": \"2026-05-23T18:08:00.000Z\", \"hypothesis\": \"PickCube frozen dt_emb baseline (fixed_dt=2, subsample ON, H=8)。验证 CIVO frozen 配置在最简单 manipulation task 上的表现。如果 eval return 稳定高于 random → frozen dt_emb 在 easy task 上不影响学习；如果性能差 → frozen dt_emb 有问题。\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --seed 0 --steps 210000 --compile False --device cuda:0 --checkpoint_every 25000 --logdir logdir/exp_054_pickcube_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 133956, \"data_path\": \"ManiSkill PickCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, CIVO config, ManiSkill PickCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PickCube-v1 (online eval)\", \"log_path\": \"logdir/exp_054_pickcube_frozen_s0/metrics.jsonl\", \"checkpoint_path\": \"logdir/exp_054_pickcube_frozen_s0/checkpoint.ckpt\"}, \"ve_ratio_peak\": \"8.81@62500\", \"eval_final\": 10.26, \"eval_final_step\": 212500, \"ve_ratio_final\": 0.583, \"ve_ratio_final_step\": 212500}, \"exp_053_peginsertion_frozen_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:23:10.381Z\", \"updated_at\": \"2026-05-23T15:00:00.000Z\", \"hypothesis\": \"Freezing dt_emb in PegInsertionSide-v1 (contact-rich manipulation) prevents CIVO while maintaining task performance, establishing that dt_emb freezing generalizes as CIVO prevention across task domains. If frozen prevents CIVO here → extends StackCube/locomotion frozen finding to insertion tasks; if CIVO still appears → freezing insufficient for contact-rich tasks.\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_053_peginsertion_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 123495, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_053_peginsertion_frozen_s0.log\", \"checkpoint_path\": \"logdir/exp_053_peginsertion_frozen_s0/checkpoint.ckpt\"}, \"ve_ratio_peak\": \"8.10@52500\", \"eval_final\": 5.89, \"ve_ratio_final\": 0.202, \"ve_ratio_final_step\": 212500}, \"exp_050_peginsertion_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:38:33.441Z\", \"updated_at\": \"2026-05-23T08:51:11.592Z\", \"hypothesis\": \"Fixed-dt=2 gate with CIVO trigger on PegInsertionSide-v1 (contact-rich manipulation) will demonstrate that temporal abstraction benefits extend beyond locomotion to precise insertion tasks, where event-gated horizons can skip redundant approach phases while preserving fine-grained control near contact.\", \"spec\": {\"command\": \"LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_050_peginsertion_civo_trigger_s0\", \"server\": \"bjb1-40020\", \"data_path\": \"ManiSkill PegInsertionSide-v1 (state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + CIVO trigger (gate_fixed_dt=2)\", \"seed\": 0, \"pid\": 304736, \"gpu_ids\": [0], \"log_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0/train.log\", \"checkpoint_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0\"}, \"metrics\": {\"ve_ratio_peak\": 10.05, \"ve_ratio_peak_step\": 82500, \"ve_ratio_final\": 0.379, \"ve_ratio_final_step\": 212500, \"civo_self_corrected\": true, \"civo_correction_delay_steps\": 130000, \"eval_final\": 20.86, \"eval_final_step\": 212500, \"eval_peak\": 20.86, \"eval_peak_step\": 212500, \"total_steps\": 222400}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T08:30:00.000Z\"}, \"exp_052_stackcube_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:26:49.825Z\", \"updated_at\": \"2026-05-23T07:45:47.966Z\", \"hypothesis\": \"StackCube CIVO trigger (trained dt_emb + subsample ON + H=8) 跨 seed 可复现性验证。exp_049 (s0) 在 32.5K 步触发 CIVO（ve_ratio 3.27）。如果 s1 也触发 → CIVO 在 manipulation 领域可复现，非 seed-specific；如果不触发 → seed-dependent，需更多 seeds。\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_052_stackcube_civo_trigger_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 103781, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/train.log\"}, \"metrics\": {\"eval_final\": 29.458, \"eval_final_step\": 212500, \"eval_peak\": 39.873, \"eval_peak_step\": 162500, \"ve_ratio_final\": 0.133, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 4.67, \"ve_ratio_peak_step\": 52500, \"total_steps\": 222400}, \"conclusion\": \"success\", \"checkpoint_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/checkpoint_202500.pt\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/metrics.jsonl\", \"completed_at\": \"2026-05-23T07:45:47.966Z\"}, \"exp_048_cheetah_civo_extension\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:30:40.050Z\", \"updated_at\": \"2026-05-22T21:18:00.000Z\", \"hypothesis\": \"Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 4.91→0.05 over 170K steps). If Cheetah does NOT self-correct → severity determines recoverability narrative. If it does → CIVO is universally transient regardless of severity.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 88654, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\"}, \"metrics\": {\"eval_final\": 23.4, \"eval_final_step\": 302000, \"eval_peak\": 32.8, \"eval_peak_step\": 252000, \"ve_ratio_initial\": 46.3, \"ve_ratio_peak\": 24.112, \"ve_ratio_peak_step\": 162000, \"ve_ratio_final\": 1.803, \"nve_initial\": 70.64, \"nve_peak_secondary\": 36.76, \"nve_final\": 2.75, \"total_steps\": 312000, \"civo_self_corrected\": false, \"civo_correction_pct\": 96, \"secondary_burst_step\": 152000, \"secondary_burst_nve\": 36.47, \"gate_collapsed\": true}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_048_cheetah_civo_extension/checkpoint_300000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_048_cheetah_civo_extension/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T21:18:00.000Z\"}, \"exp_047_frozen_dt_emb_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:03:31.428Z\", \"updated_at\": \"2026-05-22T19:01:30.894Z\", \"hypothesis\": \"Frozen dt_emb Walker seed 1: 增强 exp_042 (s0, NVE=0.19) 的统计力度。 如果 s1 也 NVE<1.5 且无持续 CIVO → frozen dt_emb mitigation 跨 seed robust。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\", \"server\": \"bjb1-40020\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"dreamer_gated_frozen_dt_emb\", \"seed\": 1, \"eval_data\": \"dmc_walker_walk (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T18:56:07.648Z\"}, \"metrics\": {\"eval_final\": 144.22, \"eval_final_step\": 215000, \"eval_peak\": 408.79, \"eval_peak_step\": 125000, \"ve_ratio_peak\": 1.099, \"ve_ratio_peak_step\": 75000, \"ve_ratio_final\": 0.277, \"nve_peak\": 1.71, \"nve_peak_step\": 95000, \"nve_final_105k\": 0.56, \"total_steps\": 225000}, \"checkpoint_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/checkpoint_225000.pt\", \"log_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T19:01:30.894Z\"}, \"exp_046_frozen_dt_emb_cheetah\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:41:53.934Z\", \"updated_at\": \"2026-05-22T18:32:34.105Z\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"hypothesis\": \"Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_042 NVE=0.19, exp_015b NVE=0.47) to a second environment. Cheetah has stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test of the frozen mitigation.\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-22T10:42:06.985Z\", \"finished_at\": \"2026-05-22T18:27:00.000Z\"}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\", \"server\": \"bjb1-40020\", \"seed\": 0, \"model_name\": \"dreamerv3-cheetah-frozen-dt-emb\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"eval_data\": \"dmc_cheetah_run (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}, \"metrics\": {\"eval_final\": 150.5, \"eval_peak\": 207.4, \"eval_peak_step\": 145000, \"ve_ratio_peak\": 0.4, \"ve_ratio_final\": 0.1, \"nve_peak\": 1.35, \"nve_peak_step\": 45000, \"nve_final\": 0.17, \"total_steps\": 224000, \"civo_alert_count\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/checkpoint_225000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:31:00.933Z\"}, \"exp_044_gradient_stop_walker\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:03:45.656Z\", \"updated_at\": \"2026-05-22T16:08:22.684Z\", \"hypothesis\": \"Reviewer Q2 直接回应：gradient stopping（detach dt_emb gradient to reward head）是否能阻断 CIVO 的 reward-critic feedback loop。基于 008d 配置（trained dt_emb + subsample ON + H=8），仅阻断 dt_emb→reward_head 梯度路径。如果 gradient stopping 有效（NVE<1.5）→ 最简干预方案成立，推翻我们之前 SGS 1/17 的结论（SGS 阻断所有梯度 vs 这里只阻断 dt_emb→reward 路径）。如果无效 → 直接证据证明 gradient-level intervention 不足以解决 CIVO，支撑 Intervention Hierarchy 中 gradient-level 最弱的结论。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True --logdir logdir/exp_044_gradient_stop_walker\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"68371\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"submitted_at\": \"2026-05-22T09:08:10.295Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"DMC Walker Walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + reward_dt_emb_detach\", \"seed\": 0, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 25212.4, \"gpu_hours\": 7.0}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:04:32.082Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:04:36.793540+00:00\"}]}, \"metrics\": {\"eval_final\": 538.6, \"eval_peak\": 561.2, \"eval_peak_step\": 185000, \"eval_civo_trough\": 44.3, \"eval_civo_trough_step\": 95000, \"ve_ratio_peak\": 4.4, \"ve_ratio_peak_step\": 95000, \"ve_ratio_final\": 0.1, \"civo_onset_step\": 85000, \"civo_resolved_step\": 125000, \"civo_duration_steps\": 40000, \"total_steps\": 224000, \"pre_civo_peak\": 545.6, \"pre_civo_peak_step\": 75000}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_044_gradient_stop_walker/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:08:22.684Z\"}, \"exp_045_treatment_extension_008d_s3\": {\"created_at\": \"2026-05-22T09:40:52.894Z\", \"updated_at\": \"2026-05-22T15:41:43.036Z\", \"status\": \"DONE\", \"retry_count\": 0, \"hypothesis\": \"CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation when extended to 300K, providing temporal dynamics data for the treatment extension analysis (Reviewer Q: does CIVO self-correct or persist?)\", \"parent\": \"exp_008d_civo_trigger_s3\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": \"70945\", \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config)\", \"seed\": 3, \"checkpoint_source\": \"exp_008d_civo_trigger_s3/latest.pt (step 112K)\", \"eval_data\": \"dmc_walker_walk (online eval, same as training env)\", \"log_path\": \"logdir/exp_045_treatment_extension_008d_s3/train.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_final\": 867.6, \"eval_peak\": 869.7, \"eval_peak_step\": 242000, \"nve_peak\": 4.91, \"nve_peak_step\": 132000, \"nve_final\": 0.052, \"ve_ratio_final\": 0.052, \"total_steps\": 312000, \"civo_alerts\": 0, \"civo_self_corrected\": true, \"civo_correction_step\": 142000, \"eval_trajectory\": {\"112000\": 58.5, \"122000\": 41.8, \"132000\": 35.1, \"142000\": 350.2, \"152000\": 646.4, \"162000\": 482.3, \"172000\": 600.4, \"182000\": 600.5, \"192000\": 699.5, \"202000\": 684.3, \"212000\": 758.6, \"222000\": 744.6, \"232000\": 745.4, \"242000\": 869.7, \"252000\": 721.6, \"262000\": 820.6, \"272000\": 716.2, \"282000\": 755.6, \"292000\": 843, \"302000\": 867.6}, \"ve_ratio_trajectory\": {\"122000\": 4.77, \"132000\": 4.91, \"142000\": 0.43, \"152000\": 0.21, \"162000\": 0.25, \"172000\": 0.18, \"182000\": 0.16, \"192000\": 0.13, \"202000\": 0.12, \"212000\": 0.1, \"222000\": 0.1, \"232000\": 0.09, \"242000\": 0.07, \"252000\": 0.08, \"262000\": 0.07, \"272000\": 0.08, \"282000\": 0.07, \"292000\": 0.06, \"302000\": 0.05}}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/checkpoint_302000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/train.log\", \"completed_at\": \"2026-05-22T15:41:43.036Z\"}, \"exp_043_008f_walker_s1\": {\"created_at\": \"2026-05-22T02:35:37.558Z\", \"hypothesis\": \"Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb absence prevents CIVO 是 robust 的跨 seed 结论，支撑因果链 \\\"trained dt_emb → CIVO\\\"。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --logdir logdir/exp_043_008f_walker_s1\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"model_name\": \"DreamerV3 (no dt_emb, 008f control)\", \"pid\": \"250627\", \"seed\": 1, \"server\": \"bjb1-40020\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:38:36.474Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"metrics\": {\"eval_final\": 673.73, \"eval_peak\": 673.73, \"eval_peak_step\": 215000, \"nve_peak\": 0.808, \"nve_peak_step\": 105000, \"nve_final\": 0.123, \"civo_alert\": false, \"total_steps\": 224000, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"note\": \"No CIVO (peak NVE 0.808, well below 1.5). Gate fixed at dt=2. Seed 1 replicates seed 0 finding: dt_emb absence prevents CIVO.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:38:36.474Z\"}, \"exp_042_frozen_dt_emb_walker\": {\"created_at\": \"2026-05-22T02:13:59.183Z\", \"hypothesis\": \"dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init, requires_grad=False) should prevent the reward-value divergence observed in exp_008d with trained dt_emb.\", \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --logdir logdir/exp_042_frozen_dt_emb_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"model_name\": \"DreamerV3 + frozen dt_emb\", \"pid\": \"251336\", \"seed\": 0, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:29:26.337Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"metrics\": {\"eval_final\": 612.45, \"eval_peak\": 682.38, \"eval_peak_step\": 205000, \"nve_peak\": 0.194, \"nve_final\": 0.051, \"civo_alert\": false, \"total_steps\": 224000, \"total_train_episodes\": 224}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:29:26.337Z\"}, \"exp_040_wide_dual_critic_cheetah\": {\"created_at\": \"2026-05-21T19:50:49.909Z\", \"hypothesis\": \"Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust。如果 s1 也部分恢复 → Cheetah dual-critic 效果一致但弱于 Walker；如果 s1 完全不恢复 → s0 的部分恢复是偶发。\", \"parent\": \"exp_032_dual_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_040_wide_dual_critic_cheetah\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_040_wide_dual_critic_cheetah.log\", \"pid\": \"52397\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T19:51:11.519Z\", \"submitted_via\": \"submit_training_job\", \"seed\": 1, \"wall_clock_seconds\": 49438.9, \"gpu_hours\": 13.73}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:37:44.547Z\", \"reproduce\": {\"finished_at\": \"2026-05-22T09:35:07.693Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:35:10.404Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T09:35:14.583680+00:00\"}]}}, \"exp_041_dual_critic_walker_s3\": {\"created_at\": \"2026-05-21T19:50:54.290Z\", \"hypothesis\": \"D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO 崩溃为低频偶发事件，dual-critic CIVO prevention 仍 robust；如果 s3 也崩 → 50% 系统性问题需进一步诊断。\", \"parent\": \"exp_032_dual_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\", \"pid\": \"51103\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-22T02:38:20.728Z\", \"submitted_via\": \"submit_training_job\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/checkpoint.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 23112.0, \"gpu_hours\": 6.42}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:04:44.715Z\", \"reproduce\": {\"finished_at\": \"2026-05-22T09:00:53.721Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T09:00:58.393731+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_peak\": 761.1, \"eval_return_final\": 544, \"eval_return_peak_step\": 165000, \"nve_peak\": 1.5, \"nve_final\": 0.1, \"civo_prevented\": true, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": false, \"steps\": 215000, \"note\": \"CIVO prevented (NVE≤1.5), no non-CIVO collapse. Eval stays 486-761 after peak. Non-CIVO collapse rate confirmed 1/4 (only s2).\"}, \"completed_at\": \"2026-05-22T09:03:32.751Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\"}, \"exp_039_narrow_dual_critic_walker_s1\": {\"completed_at\": \"2026-05-22T02:35:33.617Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T16:31:40.055Z\", \"hypothesis\": \"Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow dual-critic (min operation alone) 驱动 recovery 是 robust 的；如果不 recover → s0 的 recovery 是偶发事件。\", \"metrics\": {\"civo_recovery\": true, \"eval_return_final\": 592.7, \"note\": \"Narrow dual Walker s1: CIVO triggered then recovered. s0=697.8, s1=592.7, mean≈645. Recovery 2/2.\", \"nve_peak\": 2.19, \"recovery_confirmed\": true}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_039_narrow_dual_critic_walker_s1/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_039_narrow_dual_critic_walker_s1\\\"\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 10.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_039_narrow_dual_critic_walker_s1.log\", \"pid\": \"198771\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T16:31:39.634Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 36234.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:35:33.617Z\"}, \"exp_038_dual_critic_walker_s2\": {\"completed_at\": \"2026-05-22T02:11:36.842Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:35.293Z\", \"hypothesis\": \"Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention (NVE≤1.1). Third datapoint enables IQM statistical reporting. If 3/3 CIVO prevented → robust evidence for Prevention mechanism in medium-severity CIVO environments.\", \"metrics\": {\"civo_alert\": 0, \"civo_prevented\": true, \"eval_return_collapse\": 99.6, \"eval_return_collapse_step\": 175000, \"eval_return_final\": 120.9, \"eval_return_peak\": 354, \"eval_return_peak_step\": 155000, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": true, \"note\": \"CIVO prevented (NVE≤0.3) but non-CIVO eval collapse at 175k (354→99.6). Different failure mode from value overestimation.\", \"nve_final\": 0.248, \"nve_peak\": 0.3, \"steps\": 224000}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-22T02:07:51.177Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...dual_critic walker s2...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 13.88, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2\", \"model_name\": \"DreamerV3 + Dual Critic (wide)\", \"pid\": \"175633\", \"seed\": 2, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T12:18:34.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 49982.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:11:36.842Z\"}, \"exp_037_wide_critic_cheetah\": {\"completed_at\": \"2026-05-21T19:45:52.311Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:33.040Z\", \"hypothesis\": \"Wide single critic on Cheetah: if capacity=recovery generalizes from Walker (exp_033, NVE 4.75→self-repair, eval 408) to Cheetah (high CIVO, baseline NVE ~70.64), then Recovery mechanism works across CIVO severity levels. Combined with exp_034 (dual-critic Cheetah, NVE 1.75, eval 97.5), establishes that both Prevention and Recovery are environment-dependent.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 146.1, \"eval_return_peak\": 350.1, \"gate_dt_2_frac\": 1, \"nve_final\": 0.1, \"nve_peak\": 3.6, \"steps\": 224000}, \"parent\": \"exp_033_wide_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...wide_critic cheetah...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 7.46, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_037_wide_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Wide Single Critic\", \"pid\": \"14487\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T12:18:32.619Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 26839.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:52.311Z\"}, \"exp_036_dual_critic_pickcube\": {\"completed_at\": \"2026-05-21T19:45:31.290Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T08:43:18.481296+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T19:38:29.196731+00:00\"}]}, \"hypothesis\": \"Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+PickCube), while representation-level (TCN) only partially works on Walker. Strongest evidence for intervention hierarchy.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 27.7, \"eval_return_peak\": 27.7, \"gate_dt_2_frac\": 1, \"nve_final\": 0.2, \"nve_peak\": 2.3, \"steps\": 212447}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T19:38:24.346Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_036_dual_critic_pickcube\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 11.03, \"gpu_id\": 0, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"2476\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T08:43:44.544357+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 39706.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:31.290Z\"}, \"exp_035_narrow_dual_critic_walker\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_035_narrow_dual_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T16:11:39.130025+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:47:55.131429+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T16:08:03.906985+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Narrow dual-critic ablation (2×256 hidden, total params ≈ baseline single 512 critic): isolates min operation effect from parameter count. If CIVO suppressed → min operation itself prevents overestimation cascade. If CIVO persists → parameter count is the key factor. Combined with exp_033 (wide single critic) forms 2×2 factorial: {single,dual} × {normal,scaled} → mechanism decomposition.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"metrics\": {\"actor_entropy_final\": -0.19, \"civo_alert_window\": \"65K-85K\", \"civo_prevented\": false, \"civo_recovery\": true, \"director_override\": \"Director ruled success: CIVO recovery (33.8→697.8) is the success criterion, not prevention\", \"eval_at_215K\": 697.8, \"eval_at_85K\": 33.8, \"eval_final\": 697.8, \"eval_peak\": 697.8, \"eval_trough\": 33.8, \"nve_final\": 0.066, \"nve_peak\": 2.75, \"nve_peak_step\": 85000, \"recovery_from\": 33.8, \"recovery_to\": 697.8, \"total_steps\": 215000, \"train_return_final_range\": \"708-806\", \"v1_v2_gap_max\": 0.08, \"v1_v2_gap_typical\": 0.01}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T16:07:58.973Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-40020\", \"started_at\": \"2026-05-21T07:48:17.595Z\", \"training_hours\": 8.33}, \"retry_count\": 0, \"server\": \"bjb1-40020\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_035_narrow_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 8.31, \"gpu_id\": 1, \"hyperparams\": {\"critic_hidden\": 256, \"critic_layers\": 2, \"critic_params_each\": 525000, \"critic_params_total\": 1050000, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"narrow_dual_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Narrow Dual Critic (2×256 hidden, 1.05M total)\", \"pid\": \"162900\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T07:56:05.926445+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29900.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T16:14:26.099Z\"}, \"exp_034\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah/\", \"completed_at\": \"2026-05-21T12:18:09.552Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:17:29.760Z\", \"hypothesis\": \"Dual-critic (min of two independent critics) will prevent CIVO in Cheetah Run by providing pessimistic value estimates, as it did in Walker Walk (exp_032). If value overestimation is environment-universal, the same mechanism should work across DMC tasks.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"metrics\": {\"CIVO_prevented\": false, \"civo_trigger_steps\": [55000, 105000], \"final_NVE\": 0.144, \"final_eval_return\": 97.5, \"max_NVE\": 1.753, \"peak_eval_return\": 315.7, \"total_steps\": 215000, \"v1_v2_max_divergence\": 0.004}, \"retry_count\": 0, \"spec\": {\"command\": \"python train.py --configs dmc_cheetah_run --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --steps 210000 --seed 0\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:18:09.552Z\"}, \"exp_034_dual_critic_cheetah\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah\", \"completed_at\": \"2026-05-21T12:14:19.189109+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T05:50:59.612345+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T12:02:46.032647+00:00\"}]}, \"hypothesis\": \"Dual-critic on Cheetah Run: TCN failed at all σ (0.2/0.5/1.0) on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level intervention that works across environments. Strengthens Intervention Hierarchy: architecture-level > representation-level.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"metrics\": {\"baseline_eval_final\": 0.83, \"baseline_nve_peak\": 70.64, \"civo_alert_steps\": [95000, 105000], \"civo_alerts\": 2, \"civo_prevented\": false, \"dual_wave_civo\": true, \"eval_final\": 97.5, \"eval_final_step\": 215000, \"eval_peak\": 315.7, \"eval_peak_step\": 45000, \"eval_vs_peak_pct\": 31, \"gate_dt2_frac\": 1, \"gate_entropy\": 0, \"v1_v2_gap\": \"<0.2 (min operation has no pessimism effect)\", \"value_mean_final\": 14.2, \"value_mean_peak\": 60.5, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 1.8, \"ve_ratio_peak_step\": 55000}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:02:37.929Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_034_dual_critic_cheetah\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"993925\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T05:51:51.325323+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:15:03.481Z\"}, \"exp_033_wide_critic_walker\": {\"account\": \"root\", \"checkpoint_path\": \"logdir/exp_033_wide_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T12:08:15.252Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T03:45:53.644963+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T12:02:31.184962+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Wide single critic ablation: if CIVO suppression in exp_032 (dual-critic) is due to parameter count/regularization rather than pessimistic min operation, then a single critic with 2× parameters should also suppress CIVO. If wide-critic fails (CIVO persists) but dual-critic succeeds → min operation has implicit regularization effect beyond pessimism.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"metrics\": {\"civo_alert_step\": 105000, \"civo_alert_ve_ratio\": 1.958, \"civo_instability_duration_steps\": 75000, \"critic_params\": 2886911, \"eval_reward_final\": 407.9, \"eval_reward_peak\": 194.8, \"eval_reward_trough\": 31.8, \"value_loss_final\": 1.4, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 4.7}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:02:26.400Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-40020\", \"started_at\": \"2026-05-21T03:46:14.882Z\", \"training_hours\": 8.27}, \"retry_count\": 0, \"server\": \"bjb1-40020\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --wide_critic True --logdir logdir/exp_033_wide_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.25, \"gpu_id\": 0, \"hyperparams\": {\"critic_hidden\": 1024, \"critic_layers\": 2, \"critic_params\": 2886911, \"dual_critic\": false, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"wide_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"model_name\": \"DreamerV3 + Wide Critic (1024 hidden, 2.89M params, 2.44× normal)\", \"pid\": \"151860\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T03:52:59.702597+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29715.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:08:15.252Z\"}, \"exp_031b_tcn_pickcube_s0_sigma05\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_031b_tcn_pickcube_s0_sigma05/latest.pt\", \"completed_at\": \"2026-05-21T08:43:18.481253+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:46:39.136363+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T08:41:51.310620+00:00\"}]}, \"failure_reason\": \"NVE late-stage decline is floor effect (value signal collapse), not CIVO recovery. Eval flat 25-29 throughout — agent never learned meaningful manipulation. Confirmed by Reviewer. TCN PickCube: 0/2 (σ=0.2 and σ=0.5 both failed).\", \"hypothesis\": \"PickCube σ=0.5 dose-response data collection: σ=0.2 (exp_031) failed with NVE peak 3.71. σ=0.5 tests whether higher noise amplitude can suppress CIVO in ManiSkill PickCube. Combined with σ=0.2 data, establishes dose-response curve for robotics manipulation domain.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"metrics\": {\"eval_reward_final\": 25.5, \"eval_reward_last5_avg\": 25.9, \"eval_reward_peak\": 29.1, \"nve_final\": 0.2, \"nve_peak\": 3.3, \"nve_peak_step\": 42500, \"nve_suppressed_from_step\": 72500, \"total_episodes\": 1062, \"total_steps\": 212400}, \"parent\": \"exp_031_tcn_pickcube_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-21T08:41:45.929Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031b_tcn_pickcube_s0_sigma05\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"model_name\": \"DreamerV3 + TCN σ=0.5\", \"pid\": \"968495\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T22:33:14.695383+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T08:50:22.853581+00:00\"}, \"exp_032_dual_critic_walker\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T07:47:55.131382+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:58:31.008200+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T07:45:13.742811+00:00\"}]}, \"hypothesis\": \"Dual-critic (min of two independent critics for actor loss) will suppress CIVO by preventing critic overestimation. Uses 008d CIVO-trigger config (trained dt_emb + multi-rate exposure). If NVE stays below 1.5× and eval matches baseline, dual-critic is an effective architecture-level intervention.\", \"metrics\": {\"baseline_eval\": 900, \"civo_prevented\": true, \"eval_final\": 739.7, \"eval_final_step\": 215000, \"eval_peak\": 787.7, \"eval_peak_step\": 205000, \"eval_vs_baseline_pct\": 87.5, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"note\": \"CIVO prevented 2/2 seeds. v1≈v2 → mechanism is implicit value regularization, not min-of-two pessimism.\", \"nve_final\": 0.1, \"nve_peak\": 1.1, \"nve_peak_step\": 95000, \"v1_v2_gap\": \"<0.1% (min operation has no pessimism effect)\"}, \"parent\": \"exp_008d_civo_trigger_s2\", \"reproduce\": {\"finished_at\": \"2026-05-21T07:45:08.395Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"pid\": \"124556\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T23:19:57.690519+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:52:13.265445+00:00\"}, \"exp_032b_dual_critic_walker_s1\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032b_dual_critic_walker_s1/latest.pt\", \"completed_at\": \"2026-05-21T05:50:59.612299+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T23:22:08.787456+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T05:48:16.069863+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Dual-critic seed=1 replication: if both s0 and s1 show NVE<1.5× and eval matches baseline → dual-critic is a robust architecture-level CIVO intervention, strengthening Intervention Hierarchy evidence.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032b_dual_critic_walker_s1.log\", \"metrics\": {\"actor_loss_late\": \"≈0 (gradient signal weak)\", \"baseline_eval\": 900, \"director_override\": \"CIVO suppressed (NVE<1.5 throughout) = success for intervention evaluation. Eval 57% of vanilla baseline is due to gate collapse (dt=2 locked), not dual-critic failure.\", \"eval_criterion_pass\": false, \"eval_trajectory\": \"75K=241, 105K=228, 155K=361, 195K=544, 205K=552(peak), 215K=516\", \"eval_vs_baseline_pct\": 57, \"final_eval_return\": 516, \"final_nve\": 0.1, \"gate_dt2_frac\": 1.0, \"nve_criterion_pass\": true, \"nve_trajectory\": \"15K=0.0, 25K=0.2, 35K=0.4, 45K=0.8, 55K=0.7, 65K=0.7, 75K=0.7, 85K=1.4(peak), 95K=0.7, 105K=0.5, 135K=0.4, 215K=0.1\", \"peak_eval_return\": 551.8, \"peak_nve\": 1.4, \"total_steps\": 224000, \"total_updates\": 52599, \"training_hours\": 6.42, \"value1_value2_gap\": \"<0.5 (min operation has no pessimism effect)\"}, \"notes\": \"NVE well controlled (peak 1.4 < 1.5, no CIVO), but eval only 57% of baseline (516 vs ~900). Dual-critic suppresses value overestimation at cost of policy performance. Gate collapsed to dt=2 throughout. Two critics converge to near-identical values, min operation ineffective.\", \"parent\": \"exp_032_dual_critic_walker\", \"pid\": \"973387\", \"reproduce\": {\"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032b_dual_critic_walker_s1\\\"\", \"finished_at\": \"2026-05-21T05:48:11.173Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-20T23:22:55.338Z\", \"training_hours\": 6.42}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0}, \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"seed\": 1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:55:05.353975+00:00\"}, \"exp_029d_tcn_walker_s3_sigma02\": {\"completed_at\": \"2026-05-21T03:39:24.356918+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:33:03.633Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T03:32:52.751412+00:00\"}]}, \"failure_reason\": \"Sudden CIVO blowup: NVE appeared healthy at 95K (0.666, declining from 0.855@85K), then catastrophic spike to 3.0@105K. Eval collapsed 349.6→71.8. Late-stage NVE recovery to 0.4@215K = value adaptation (eval stayed at 104.5, never recovered). TCN σ=0.2 Walker: 2/4 seeds CIVO failure (s2: NVE 2.77, s3: NVE 3.0).\", \"hypothesis\": \"Fourth TCN σ=0.2 seed to match 4 baseline seeds (s1=916, s2=443, s3=869, s4=923@105K) for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwal et al. 2021.\", \"metrics\": {\"civo_onset_step\": 105000, \"civo_pattern\": \"sudden blowup (healthy 0.67@95K → 3.0@105K)\", \"eval_final\": 104.5, \"eval_last_step\": 215000, \"eval_peak\": 349.6, \"eval_peak_step\": 95000, \"eval_return_105K\": 71.8, \"eval_return_115K\": 69.8, \"eval_return_125K\": 61.5, \"eval_return_135K\": 141.8, \"eval_return_145K\": 98.66, \"eval_return_155K\": 88.86, \"eval_return_15K\": 159.1, \"eval_return_165K\": 86.22, \"eval_return_175K\": 123.53, \"eval_return_185K\": 153.71, \"eval_return_195K\": 68.84, \"eval_return_205K\": 63.71, \"eval_return_215K\": 104.5, \"eval_return_25K\": 155.7, \"eval_return_35K\": 190.8, \"eval_return_45K\": 137.1, \"eval_return_55K\": 210.7, \"eval_return_5K\": 31.7, \"eval_return_65K\": 189.5, \"eval_return_75K\": 253.2, \"eval_return_85K\": 259.5, \"eval_return_95K\": 349.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"nve_peak\": 3.0, \"nve_peak_step\": 105000, \"step\": 224000, \"value_mean_105K\": 218.37, \"value_mean_215K\": 42.55, \"value_mean_95K\": 232.74, \"ve_ratio_105K\": 3.0, \"ve_ratio_115K\": 2.5, \"ve_ratio_125K\": 2.4, \"ve_ratio_135K\": 0.9, \"ve_ratio_145K\": 1.141, \"ve_ratio_155K\": 1.06, \"ve_ratio_165K\": 0.91, \"ve_ratio_175K\": 0.556, \"ve_ratio_185K\": 0.396, \"ve_ratio_195K\": 0.78, \"ve_ratio_205K\": 0.747, \"ve_ratio_215K\": 0.4, \"ve_ratio_45K\": 0.695, \"ve_ratio_55K\": 0.598, \"ve_ratio_65K\": 0.863, \"ve_ratio_75K\": 0.791, \"ve_ratio_85K\": 0.9, \"ve_ratio_95K\": 0.7}, \"parent\": \"exp_029b_tcn_walker_s2_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-21T03:32:47.021Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029d_tcn_walker_s3_sigma02\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\", \"pid\": \"109826\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T19:33:48.032Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:39:24.356963+00:00\"}, \"exp_031_tcn_pickcube_s0_sigma02\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_031_tcn_pickcube_s0_sigma02\", \"completed_at\": \"2026-05-20T23:52:48.308Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T12:09:56.923Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T23:50:00.801433+00:00\"}]}, \"hypothesis\": \"TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination rollout will suppress CIVO in ManiSkill PickCube-v1, as it did in Walker Walk, by preventing the world model from overfitting to fixed dt signals.\", \"metrics\": {\"eval_peak\": 28.6, \"eval_peak_step\": 162500, \"eval_return_132K\": 23.45, \"eval_return_152K\": 23.1, \"eval_return_192K\": 11.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0, \"step\": 195600, \"train_return_range\": \"18-25\", \"ve_ratio_latest\": 0.18, \"ve_ratio_peak\": 3.71}, \"parent\": \"exp_019b_pickcube_civo_trigger\", \"reproduce\": {\"finished_at\": \"2026-05-20T23:49:56.649Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"none(train_from_scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\"\", \"data_count\": \"200000(online)\", \"data_path\": \"maniskill_PickCube-v1\", \"eval_data\": \"maniskill_PickCube-v1(online_eval)\", \"gpu\": \"cuda:1\", \"gpu_hours\": 11.17, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"908459\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T12:42:41.707Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 40206.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:52:48.308Z\"}, \"exp_029b_tcn_walker_s2_sigma02\": {\"completed_at\": \"2026-05-20T22:58:31.008151+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:55:13.731Z\", \"failure_reason\": \"CIVO confirmed: NVE accelerated 1.01→1.65→2.77@105K (008d-like pattern), eval collapsed 177.7→32.0. Late-stage NVE decline to 1.06@155K = value adaptation to collapsed policy, NOT CIVO self-recovery (eval remained at 56.5, never recovered). Killed at 156K to free GPU for dual-critic experiment.\", \"hypothesis\": \"TCN σ=0.2 seed variance characterization: s0 eval=91%, s1 eval=45%. Third seed resolves whether high variance is systematic or s1 is outlier.\", \"metrics\": {\"civo_onset_step\": 65000, \"eval_last_step\": 165000, \"eval_peak\": 177.67, \"eval_peak_step\": 55000, \"eval_return_105K\": 31.97, \"eval_return_115K\": 35.45, \"eval_return_125K\": 33.04, \"eval_return_135K\": 42.47, \"eval_return_145K\": 51.66, \"eval_return_155K\": 56.5, \"eval_return_15K\": 168.41, \"eval_return_165K\": 44.9, \"eval_return_25K\": 159.56, \"eval_return_35K\": 168.05, \"eval_return_45K\": 171.51, \"eval_return_55K\": 177.67, \"eval_return_5K\": 30.46, \"eval_return_65K\": 106.57, \"eval_return_75K\": 64.01, \"eval_return_85K\": 62.82, \"eval_return_95K\": 44.66, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"late_stage_nve_decline\": \"value adaptation (value_mean 108→55), not recovery (eval stayed 32-57)\", \"nve_peak\": 2.765, \"nve_peak_step\": 105000, \"step\": 168000, \"value_mean_105K\": 88.38, \"value_mean_165K\": 55.03, \"value_mean_55K\": 103.62, \"ve_ratio_105K\": 2.765, \"ve_ratio_115K\": 2.326, \"ve_ratio_125K\": 2.278, \"ve_ratio_135K\": 1.648, \"ve_ratio_145K\": 1.234, \"ve_ratio_155K\": 1.061, \"ve_ratio_15K\": 0.03, \"ve_ratio_165K\": 1.226, \"ve_ratio_25K\": 0.174, \"ve_ratio_35K\": 0.335, \"ve_ratio_45K\": 0.477, \"ve_ratio_55K\": 0.583, \"ve_ratio_65K\": 1.014, \"ve_ratio_75K\": 1.65, \"ve_ratio_85K\": 1.623, \"ve_ratio_95K\": 2.109}, \"parent\": \"exp_029a_tcn_walker_s1_sigma02\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029b_tcn_walker_s2_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029b_tcn_walker_s2_sigma02\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029b_tcn_walker_s2_sigma02.log\", \"pid\": \"75543\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T16:56:24.781Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:58:31.008195+00:00\"}, \"exp_030c_tcn_cheetah_s0_sigma10\": {\"completed_at\": \"2026-05-20T22:34:07.916411+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:26:11.800Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T22:28:30.207347+00:00\"}]}, \"hypothesis\": \"TCN σ=1.0 on Cheetah tests whether higher noise amplitude further suppresses CIVO. σ=0.5 (exp_030b) was negative with NVE peaking at 10.67@55K then declining. σ=1.0 should provide stronger temporal regularization. If NVE stays below 1.5 throughout training and eval_return ≥ baseline → TCN generalizes to Cheetah with appropriate σ scaling.\", \"metrics\": {\"baseline_eval_avg\": 548, \"eval_final\": 47.2, \"eval_peak\": 371.7, \"eval_peak_step\": 35000, \"eval_return_105K\": 122.5, \"eval_return_115K\": 162.2, \"eval_return_125K\": 148.5, \"eval_return_135K\": 138.4, \"eval_return_145K\": 100.4, \"eval_return_155K\": 144.3, \"eval_return_15K\": 87.5, \"eval_return_165K\": 130.9, \"eval_return_175K\": 66.4, \"eval_return_185K\": 47.2, \"eval_return_195K\": 56.5, \"eval_return_205K\": 49.7, \"eval_return_215K\": 47.2, \"eval_return_25K\": 166.3, \"eval_return_35K\": 371.7, \"eval_return_45K\": 144.0, \"eval_return_55K\": 266.0, \"eval_return_5K\": 8.3, \"eval_return_65K\": 197.0, \"eval_return_75K\": 107.8, \"eval_return_85K\": 95.8, \"eval_return_95K\": 72.8, \"eval_vs_baseline\": \"8.6%\", \"gate_dt2_frac\": 1.0, \"gate_dt_mean\": 2.0, \"gate_entropy\": 0.0, \"step\": 224000, \"ve_ratio_max\": 0.4}, \"parent\": \"\", \"reproduce\": {\"finished_at\": \"2026-05-20T22:28:26.022Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030c_tcn_cheetah_s0_sigma10\", \"command\": \"dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --tcn_sigma 1.0\", \"data_count\": 210000, \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030c_tcn_cheetah_s0_sigma10.log\", \"model_name\": \"dreamerv3\", \"pid\": \"920968\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T16:49:48.464Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:34:07.916452+00:00\"}, \"exp_029c_tcn_walker_s0_sigma01\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:09:50.913Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T19:30:34.687287+00:00\"}]}, \"hypothesis\": \"σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2 prevents CIVO and σ=0.1 does not, establishes minimum effective dose. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8). Three-point dose-response: σ=0.1 (this), σ=0.2 (success), σ=0.5 (oscillatory failure).\", \"metrics\": {\"eval_final\": 328.3, \"eval_peak\": 490.7, \"eval_peak_step\": \"165K\", \"eval_return_105K\": 204.7, \"eval_return_115K\": 296.4, \"eval_return_125K\": 232.3, \"eval_return_135K\": 247.4, \"eval_return_145K\": 323.1, \"eval_return_155K\": 359.7, \"eval_return_15K\": 99.1, \"eval_return_165K\": 490.7, \"eval_return_175K\": 246.2, \"eval_return_185K\": 220.6, \"eval_return_195K\": 212.8, \"eval_return_205K\": 256.9, \"eval_return_215K\": 328.3, \"eval_return_25K\": 140.7, \"eval_return_35K\": 155.7, \"eval_return_45K\": 160.9, \"eval_return_55K\": 254.8, \"eval_return_5K\": 35.6, \"eval_return_65K\": 268.7, \"eval_return_75K\": 295.5, \"eval_return_85K\": 220.8, \"eval_return_95K\": 188.6, \"nve_final\": 0.1, \"nve_max\": 1.0218, \"nve_max_step\": \"95K\", \"total_steps\": 224000, \"ve_ratio_105K\": 0.761, \"ve_ratio_115K\": 0.4514, \"ve_ratio_125K\": 0.4899, \"ve_ratio_135K\": 0.3995, \"ve_ratio_145K\": 0.2667, \"ve_ratio_155K\": 0.2, \"ve_ratio_15K\": 0.0306, \"ve_ratio_165K\": 0.1, \"ve_ratio_175K\": 0.3, \"ve_ratio_185K\": 0.3, \"ve_ratio_195K\": 0.3, \"ve_ratio_205K\": 0.2, \"ve_ratio_215K\": 0.1, \"ve_ratio_25K\": 0.1606, \"ve_ratio_35K\": 0.3162, \"ve_ratio_45K\": 0.4807, \"ve_ratio_55K\": 0.4368, \"ve_ratio_65K\": 0.5432, \"ve_ratio_75K\": 0.6211, \"ve_ratio_85K\": 0.9533, \"ve_ratio_95K\": 1.0218}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-20T19:30:28.923Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\", \"checkpoint_source\": \"from_scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\"\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\", \"model_name\": \"dreamer\", \"pid\": \"59395\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T11:42:56.447Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:53:26.097Z\"}, \"exp_029a_tcn_walker_s1_sigma02\": {\"completed_at\": \"2026-05-20T16:47:18.789Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T08:31:29.514Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T16:47:29.902718+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02 which shows NVE<1.0× and eval reaching baseline at 135K. Tests whether CIVO suppression is reproducible across seeds. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.2. If s1 also shows NVE<1.0× → TCN σ=0.2 is a robust intervention.\", \"metrics\": {\"current_step\": 215000, \"eval_last10_mean\": 282.15, \"eval_peak\": 401, \"eval_peak_step\": \"125K\", \"eval_return_105K\": 319.4, \"eval_return_115K\": 345.5, \"eval_return_125K\": 401, \"eval_return_135K\": 307.8, \"eval_return_145K\": 380.8, \"eval_return_155K\": 307.3, \"eval_return_15K\": 137.7, \"eval_return_165K\": 320.3, \"eval_return_175K\": 159, \"eval_return_185K\": 278.2, \"eval_return_195K\": 301.2, \"eval_return_205K\": 204.6, \"eval_return_215K\": 161.3, \"eval_return_25K\": 180.9, \"eval_return_35K\": 124, \"eval_return_45K\": 124.2, \"eval_return_55K\": 133.9, \"eval_return_5K\": 36.7, \"eval_return_65K\": 169.7, \"eval_return_75K\": 171.2, \"eval_return_85K\": 151.8, \"eval_return_95K\": 180.3, \"nve_final\": 0.1864, \"nve_max\": 0.6428, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.1554, \"ve_ratio_115K\": 0.1348, \"ve_ratio_125K\": 0.116, \"ve_ratio_135K\": 0.1449, \"ve_ratio_145K\": 0.1088, \"ve_ratio_155K\": 0.1287, \"ve_ratio_15K\": 0.0248, \"ve_ratio_165K\": 0.1142, \"ve_ratio_175K\": 0.2138, \"ve_ratio_185K\": 0.121, \"ve_ratio_195K\": 0.1075, \"ve_ratio_205K\": 0.1503, \"ve_ratio_215K\": 0.1864, \"ve_ratio_25K\": 0.1165, \"ve_ratio_35K\": 0.3574, \"ve_ratio_45K\": 0.5147, \"ve_ratio_55K\": 0.6428, \"ve_ratio_65K\": 0.4777, \"ve_ratio_75K\": 0.398, \"ve_ratio_85K\": 0.4033, \"ve_ratio_95K\": 0.3007}, \"notes\": \"Cron 误报: process exited without sentinel/W&B, 但实验已正常完成 (215K/210K target). NVE max 0.6428@55K (CIVO suppressed), eval peak 401@125K (45% baseline). 对比 parent s0: s0 eval 达 baseline, s1 仅 45% → 高 seed 方差暴露 TCN 脆弱性. 结论 conclusion=success 不变.\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-20T16:47:17.713Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"50924\", \"seed\": 1, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:53:36.867Z\"}, \"exp_030b_tcn_cheetah_s0_sigma05\": {\"completed_at\": \"2026-05-20T16:49:02.778Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:07:53.975Z\", \"hypothesis\": \"Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the environment-appropriate dose (Walker σ=0.5 = overdose causing oscillatory CIVO, Cheetah σ=0.2 = underdose with NVE 1.903@55K). Tests whether TCN effectiveness is environment-dependent with σ scaling to CIVO severity. If NVE<1.5× and eval maintained → TCN is generalizable with environment-tuned σ.\", \"metrics\": {\"current_step\": 195000, \"eval_return_105K\": 104.4, \"eval_return_115K\": 137.7, \"eval_return_125K\": 211.7, \"eval_return_135K\": 97.2, \"eval_return_145K\": 79.4, \"eval_return_155K\": 76.8, \"eval_return_15K\": 78.3, \"eval_return_165K\": 77.5, \"eval_return_175K\": 85.7, \"eval_return_185K\": 68.7, \"eval_return_195K\": 77.6, \"eval_return_25K\": 219.3, \"eval_return_35K\": 296.5, \"eval_return_45K\": 32.8, \"eval_return_55K\": 6, \"eval_return_5K\": 8.3, \"eval_return_65K\": 71.2, \"eval_return_75K\": 23.3, \"eval_return_85K\": 34, \"eval_return_95K\": 143.6, \"nve_final\": 0.1534, \"nve_max\": 10.6657, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.2686, \"ve_ratio_115K\": 0.1789, \"ve_ratio_125K\": 0.1037, \"ve_ratio_135K\": 0.2153, \"ve_ratio_145K\": 0.2478, \"ve_ratio_155K\": 0.2392, \"ve_ratio_15K\": 0.0202, \"ve_ratio_165K\": 0.202, \"ve_ratio_175K\": 0.1591, \"ve_ratio_185K\": 0.1834, \"ve_ratio_195K\": 0.1534, \"ve_ratio_25K\": 0.0636, \"ve_ratio_35K\": 0.1238, \"ve_ratio_45K\": 1.9141, \"ve_ratio_55K\": 10.6657, \"ve_ratio_65K\": 0.8371, \"ve_ratio_75K\": 1.9823, \"ve_ratio_85K\": 1.0946, \"ve_ratio_95K\": 0.2253}, \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/latest.pt\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:49:02.778Z\"}, \"exp_027_tcn_walker_s1\": {\"completed_at\": \"2026-05-20T12:38:02.085Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T05:51:53.479Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T12:35:42.576855+00:00\"}]}, \"hypothesis\": \"TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different seed to verify that the NVE self-correction phenomenon (transient CIVO at 55K → NVE recovery to 0.83 by 75K) is reproducible across seeds, not a stochastic artifact. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.5.\", \"metrics\": {\"eval_last10_mean\": 233.1, \"eval_peak\": 364.9, \"eval_peak_step\": 75000, \"eval_return\": {\"105000\": 216.7, \"115000\": 318.9, \"125000\": 309.1, \"135000\": 216.1, \"145000\": 175.4, \"15000\": 140.5, \"155000\": 171, \"165000\": 209.5, \"175000\": 120.4, \"185000\": 355.4, \"195000\": 183.3, \"205000\": 240.2, \"215000\": 350.8, \"25000\": 163.6, \"35000\": 153, \"45000\": 136.8, \"5000\": 31, \"55000\": 158.3, \"65000\": 298.5, \"75000\": 364.9, \"85000\": 134, \"95000\": 94.6}, \"nve_final\": 0.1476, \"nve_max\": 1.6367, \"nve_max_step\": 95000, \"total_steps\": 215000, \"ve_ratio\": {\"105000\": 0.6444, \"115000\": 0.4021, \"125000\": 0.38, \"135000\": 0.5078, \"145000\": 0.8469, \"15000\": 0.0246, \"155000\": 0.8568, \"165000\": 0.5393, \"175000\": 0.7355, \"185000\": 0.211, \"195000\": 0.3513, \"205000\": 0.2376, \"215000\": 0.1476, \"25000\": 0.1416, \"35000\": 0.3585, \"45000\": 0.6101, \"55000\": 0.7092, \"65000\": 0.4875, \"75000\": 0.4902, \"85000\": 1.4104, \"95000\": 1.6367}}, \"parent\": \"exp_027_tcn_walker_s0\", \"reproduce\": {\"finished_at\": \"2026-05-20T12:35:38.092Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:45:31.028Z\"}, \"exp_027_tcn_walker_s0_sigma02\": {\"completed_at\": \"2026-05-20T11:19:31.331Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:25:32.533Z\", \"hypothesis\": \"TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding during imagination) but with σ=0.2 instead of 0.5. Tests whether smaller noise magnitude is sufficient to disrupt dt-specific value bias. If σ=0.5 works but σ=0.2 doesn't → noise magnitude matters; if both work → method is robust to σ choice.\", \"metrics\": {\"eval_last10_mean\": 587.1, \"eval_peak\": 821.1, \"eval_peak_step\": \"175K\", \"eval_return_105K\": 236.4, \"eval_return_115K\": 543.8, \"eval_return_125K\": 458.4, \"eval_return_135K\": 496.7, \"eval_return_145K\": 542.7, \"eval_return_155K\": 660.5, \"eval_return_15K\": 150.6, \"eval_return_165K\": 653.3, \"eval_return_175K\": 821.1, \"eval_return_185K\": 560.5, \"eval_return_195K\": 567.9, \"eval_return_205K\": 558.7, \"eval_return_215K\": 551, \"eval_return_25K\": 199.4, \"eval_return_35K\": 278.2, \"eval_return_45K\": 315.6, \"eval_return_55K\": 278.6, \"eval_return_5K\": 35.6, \"eval_return_65K\": 331, \"eval_return_75K\": 293.1, \"eval_return_85K\": 363.9, \"eval_return_95K\": 171.4, \"nve_final\": 0.0955, \"nve_max\": 0.9081, \"nve_max_step\": \"95K\", \"total_steps\": 215000, \"ve_ratio_105K\": 0.5625, \"ve_ratio_115K\": 0.2105, \"ve_ratio_125K\": 0.2182, \"ve_ratio_135K\": 0.1764, \"ve_ratio_145K\": 0.143, \"ve_ratio_155K\": 0.106, \"ve_ratio_15K\": 0.0192, \"ve_ratio_165K\": 0.0979, \"ve_ratio_175K\": 0.0729, \"ve_ratio_185K\": 0.1048, \"ve_ratio_195K\": 0.1026, \"ve_ratio_205K\": 0.0995, \"ve_ratio_215K\": 0.0955, \"ve_ratio_25K\": 0.0961, \"ve_ratio_35K\": 0.1875, \"ve_ratio_45K\": 0.3009, \"ve_ratio_55K\": 0.5231, \"ve_ratio_65K\": 0.5654, \"ve_ratio_75K\": 0.611, \"ve_ratio_85K\": 0.4665, \"ve_ratio_95K\": 0.9081}, \"parent\": \"exp_027_tcn_walker_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\", \"data_count\": 215000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:06:21.855Z\"}, \"exp_030a_tcn_cheetah_s0_sigma02\": {\"completed_at\": \"2026-05-20T11:10:00.827Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T09:24:38.711Z\", \"hypothesis\": \"TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether CIVO suppression generalizes beyond Walker Walk. Cheetah exhibits stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) + TCN σ=0.2. If NVE<1.5× and eval maintained → TCN is environment-agnostic intervention.\", \"metrics\": {\"current_step\": 64000, \"eval_return_35K\": 299.5, \"eval_return_55K\": 31.9, \"note\": \"WARNING: NVE breached 1.5× at 55K (1.903), eval crashed 299→32. Possible CIVO despite TCN.\", \"target_steps\": 210000, \"ve_ratio_55K\": 1.903}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_030a_tcn_cheetah_s0_sigma02/\", \"checkpoint_source\": \"from_scratch\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\", \"model_name\": \"dreamerv3_tcn_sigma02_cheetah\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T11:10:00.827Z\"}, \"exp_027_tcn_walker_s0\": {\"analysis_summary\": \"TCN (σ=0.5 noise on dt_embedding) FAILED to suppress CIVO. NVE breached 1.5× threshold 3 times: 55K(1.68×), 65K(1.54×), 85K(3.97×). Peak NVE 3.97× at 85K is HIGHER than typical CIVO, suggesting TCN destabilizes value learning. Eval peaked at 240 (35K), then collapsed to avg 117 in latter half — far below 450 target. Gate remained fixed at dt=2 throughout (zero entropy). The noise magnitude was insufficient to decorrelate critic estimates from dt conditioning. Training reached 120K/210K planned. Hypothesis falsified: forward-pass noise at σ=0.5 does not prevent critic from exploiting dt-specific value structure.\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s0/latest.pt\", \"completed_at\": \"2026-05-20T09:24:09.016Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:51.820Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T06:06:34.898602+00:00\"}]}, \"hypothesis\": \"Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5) to dt_embedding during imagination rollouts reduces dt conditioning precision, preventing critic from learning dt-specific value bias. Predicts CIVO suppression (NVE < 1.5×) with eval > 50% baseline (~450+). Based on obs-decoder SGS failure (gradient-level intervention insufficient) → need forward-pass/representation-level intervention.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"metrics\": {\"eval_return_105K\": 95.5, \"eval_return_112K\": 99.5, \"eval_return_15K\": 154.6, \"eval_return_25K\": 223.6, \"eval_return_35K\": 240, \"eval_return_45K\": 101.2, \"eval_return_55K\": 70, \"eval_return_5K\": 37.4, \"eval_return_65K\": 95.1, \"eval_return_75K\": 189.2, \"eval_return_85K\": 36, \"eval_return_95K\": 166.4, \"final_step\": 120000, \"gate_dt_entropy\": 0, \"gate_dt_mean\": 2, \"last_5_eval_avg\": 117.3, \"nve_breach_count\": 3, \"nve_breach_steps\": \"55K(1.68), 65K(1.54), 85K(3.97)\", \"peak_eval\": 240, \"peak_eval_step\": \"35K\", \"peak_nve\": 3.965, \"peak_nve_step\": \"85K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.916, \"ve_ratio_15K\": 0.02, \"ve_ratio_25K\": 0.11, \"ve_ratio_35K\": 0.235, \"ve_ratio_45K\": 0.86, \"ve_ratio_55K\": 1.679, \"ve_ratio_65K\": 1.544, \"ve_ratio_75K\": 0.831, \"ve_ratio_85K\": 3.965, \"ve_ratio_95K\": 0.675}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"reproduce\": {\"finished_at\": \"2026-05-20T06:06:30.806Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"pid\": \"888715\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T06:13:35.505Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11433.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:24:09.016Z\"}, \"exp_028_rave_walker_s0_ceil15\": {\"completed_at\": \"2026-05-20T08:31:12.389Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T03:25:34.045Z\", \"hypothesis\": \"RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value cap) but with ceiling=1.5 instead of 2.0. Tighter constraint tests whether more aggressive capping improves CIVO suppression without harming learning. If ceiling=2.0 works and 1.5 also works → method robust; if 1.5 hurts eval → ceiling choice is critical.\", \"metrics\": {\"current_step\": 135000, \"eval_return_105K\": 76.2, \"eval_return_115K\": 41.2, \"eval_return_125K\": 36.6, \"eval_return_135K\": 39.1, \"eval_return_15K\": 99.4, \"eval_return_25K\": 155.3, \"eval_return_35K\": 180.1, \"eval_return_45K\": 166.9, \"eval_return_55K\": 131, \"eval_return_5K\": 31.6, \"eval_return_65K\": 91.5, \"eval_return_75K\": 120.9, \"eval_return_85K\": 137.3, \"eval_return_95K\": 70.2, \"target_steps\": 210000, \"ve_ratio_105K\": 0.984, \"ve_ratio_115K\": 1.513, \"ve_ratio_125K\": 1.462, \"ve_ratio_135K\": 1.171, \"ve_ratio_15K\": 0.03, \"ve_ratio_25K\": 0.128, \"ve_ratio_35K\": 0.247, \"ve_ratio_45K\": 0.428, \"ve_ratio_55K\": 0.737, \"ve_ratio_65K\": 1.294, \"ve_ratio_75K\": 0.937, \"ve_ratio_85K\": 0.727, \"ve_ratio_95K\": 1.28}, \"parent\": \"exp_028_rave_walker_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\", \"checkpoint_source\": \"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\", \"model_name\": \"dreamerv3_rave_ceil15\", \"note\": \"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\", \"pid\": \"38372\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_028_rave_walker_s0_ceil15\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:31:12.389Z\"}, \"exp_028_rave_walker_s0\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/checkpoint.ckpt\", \"completed_at\": \"2026-05-20T06:14:31.720Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:53.882Z\", \"hypothesis\": \"Reality-Anchored Value Estimation (RAVE): cap imagination critic values at ceiling*v_anchor (ceiling=2.0, v_anchor=EMA of real-state critic values). Directly prevents pathological value inflation (NVE>1.5×) by bounding imagination/reality value ratio. Based on CIVO core mechanism being imagination value explosion → this directly caps the ratio without modifying gradients or training dynamics.\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/\", \"metrics\": {\"current_steps\": 105000, \"eval_trajectory\": {\"105K\": {\"eval_return\": 29, \"value_mean\": 92.2, \"ve_ratio\": 3.183}, \"15K\": {\"eval_return\": 105.3, \"value_mean\": 2.93, \"ve_ratio\": 0.028}, \"25K\": {\"eval_return\": 191.9, \"value_mean\": 24.4, \"ve_ratio\": 0.127}, \"35K\": {\"eval_return\": 204.6, \"ve_ratio\": 0.267}, \"45K\": {\"eval_return\": 197.7, \"ve_ratio\": 0.439}, \"55K\": {\"eval_return\": 193, \"ve_ratio\": 0.62}, \"5K\": {\"eval_return\": 37.4, \"value_mean\": 0.001}, \"65K\": {\"eval_return\": 79.8, \"ve_ratio\": 1.832}, \"75K\": {\"eval_return\": 44.5, \"ve_ratio\": 3.415}, \"85K\": {\"eval_return\": 57.7, \"ve_ratio\": 2.126}, \"95K\": {\"eval_return\": 25.9, \"value_mean\": 105.87, \"ve_ratio\": 4.086}}, \"note\": \"NEGATIVE. NVE diverged from 55K onward (0.62→4.09), eval collapsed 193→29. No self-correction.\"}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (trained from scratch, derives from SGS failure line)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\"\", \"data_count\": \"105000 env steps (52.5K agent steps, action_repeat=2)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\", \"model_name\": \"dreamerv3_rave_ceil20\", \"pid\": \"879636\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T02:54:26.022Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12005.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T06:14:31.720Z\"}, \"exp_025_obs_sgs_walker_s2\": {\"completed_at\": \"2026-05-20T03:14:06.591Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-19T16:39:26.941Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T03:14:13.011509+00:00\"}]}, \"failure_reason\": \"Reclassified: experiment completed 224K/210K steps normally. Cron misclassified as failed due to missing W&B sentinel. Actual result is negative — obs-decoder SGS suppressed CIVO (ve_ratio 0.8-1.4) but eval collapsed to ~90 (baseline ~930).\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"metrics\": {\"eval_return_215K\": 89.6, \"target_steps\": 210000, \"train_steps_completed\": 224000, \"ve_ratio_175K\": 1.2, \"ve_ratio_185K\": 1.4, \"ve_ratio_215K\": 0.8}, \"notes\": \"Obs-decoder SGS s2 完成全部训练（224K/210K steps）。ve_ratio 全程 0.8-1.4（CIVO 部分抑制），但 eval_return 仅 66-90（baseline ~930，远低于 70% 阈值 ~650）。与 s1/s3/s4 一致：obs-decoder SGS 无法在抑制 CIVO 的同时保持性能。梯度干预路线全面否定（Full SGS 0/3 + Obs-decoder SGS 0/6 有效）。\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"reproduce\": {\"finished_at\": \"2026-05-20T03:14:07.466Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s2/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s2/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7989\", \"seed\": 2, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s2\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:17:26.061Z\"}, \"exp_026_obs_sgs_cheetah_s1\": {\"completed_at\": \"2026-05-20T03:02:46.556Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:29.171Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16346\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:46.556Z\"}, \"exp_026_obs_sgs_cheetah_s0\": {\"completed_at\": \"2026-05-20T03:02:43.170Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:27.608Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16208\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s0\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:43.170Z\"}, \"exp_025_obs_sgs_walker_s4\": {\"completed_at\": \"2026-05-20T03:02:39.948Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:29.810Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"851593\", \"seed\": 4, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s4\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:39.948Z\"}, \"exp_025_obs_sgs_walker_s3\": {\"completed_at\": \"2026-05-20T03:02:36.670Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:28.402Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"847597\", \"seed\": 3, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s3\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:36.670Z\"}, \"exp_025_obs_sgs_walker_s1\": {\"completed_at\": \"2026-05-20T03:02:32.583Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:25.583Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7833\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:32.583Z\"}, \"exp_001_baseline_s4_extended\": {\"completed_at\": \"2026-05-19T23:06:42.122Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:31.737Z\", \"hypothesis\": \"Walker Walk baseline seed=4 extended to 505K. Third long-run baseline seed for multi-seed NVE normalization. s4@105K=922.8 (highest), obtaining full ve_ratio profile.\", \"metrics\": {\"convergence_mean_250k_plus\": 935, \"final_eval_return\": 938.86, \"final_step\": 520000, \"peak_eval_return\": 960.6}, \"parent\": \"exp_001_baseline_s4\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 112000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s4_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T23:06:42.122Z\"}, \"exp_001_baseline_s3_extended\": {\"completed_at\": \"2026-05-19T21:23:44.025Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:30.382Z\", \"hypothesis\": \"Walker Walk baseline seed=3 extended to 505K. Second long-run baseline seed (alongside s2_ext) for multi-seed NVE normalization robustness. s3@105K=869.0, testing convergence to 920+ level.\", \"metrics\": {\"eval_profile\": {\"102000\": 869.03, \"112000\": 898.89, \"120000\": 898.38, \"130000\": 837.74, \"140000\": 876.64, \"15000\": 224.27, \"150000\": 899.47, \"160000\": 922.77, \"170000\": 925.77, \"180000\": 912.89, \"190000\": 915.07, \"200000\": 894.77, \"210000\": 899.79, \"220000\": 951.18, \"230000\": 930.56, \"240000\": 910.47, \"25000\": 329.99, \"250000\": 914.02, \"260000\": 931.33, \"270000\": 954.65, \"280000\": 928.01, \"290000\": 947.4, \"300000\": 853.32, \"310000\": 906.35, \"320000\": 847.16, \"330000\": 934.78, \"340000\": 921.08, \"35000\": 413.12, \"350000\": 922.63, \"360000\": 844.99, \"370000\": 911.36, \"380000\": 917.73, \"390000\": 937.21, \"400000\": 928, \"410000\": 945.88, \"420000\": 897.2, \"430000\": 949.45, \"440000\": 937.28, \"45000\": 332.69, \"450000\": 924.24, \"460000\": 967.25, \"470000\": 940.55, \"480000\": 936.24, \"490000\": 944.67, \"5000\": 42.15, \"500000\": 957.09, \"510000\": 947.68, \"55000\": 519.91, \"65000\": 667.42, \"72000\": 771.33, \"82000\": 772.88, \"92000\": 854.6}, \"final_eval_return\": 947.68, \"final_step\": 520000, \"final_train_return_avg\": 945.4}, \"parent\": \"exp_001_baseline_s3\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s3/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s3/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_001_baseline_s3/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 120000, \"seed\": 3, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s3_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:23:44.025Z\"}, \"exp_001_baseline_s2_extended\": {\"completed_at\": \"2026-05-19T17:44:27.212Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:10:10.948Z\", \"hypothesis\": \"Walker Walk baseline seed=2 extended to 505K. Tests whether low eval (443.5 @105K) is due to slow convergence or seed-level difference. s1=915.7, s3=869.0 at 105K.\", \"metrics\": {\"eval_return_at_105K\": 443.5, \"eval_return_final\": 945.7, \"eval_return_peak\": 962.6, \"total_steps\": 512000, \"value_mean_at_105K\": 329.16, \"value_mean_plateau\": 665, \"ve_ratio_at_105K\": 0.7422, \"ve_ratio_converged_range\": \"0.69-0.77\"}, \"parent\": \"exp_001_baseline_s2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s2/latest.pt\", \"checkpoint_source\": \"logdir/exp_001_baseline_s2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 2 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s2\", \"data_count\": 0, \"data_path\": \"logdir/exp_001_baseline_s2\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s2/train_extended.log\", \"model_name\": \"dreamerv3\", \"resumed_from_step\": 112000, \"seed\": 2, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s2_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T17:44:27.212Z\"}, \"exp_023_cheetah_baseline_s4_extended\": {\"completed_at\": \"2026-05-19T09:02:40.466Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T06:27:42.161Z\", \"hypothesis\": \"Cheetah Run baseline seed=4 extended to 300K. Tests whether eval drop at 194K→204K (537→302) is transient fluctuation or permanent collapse. Informs baseline stability and NVE normalization robustness.\", \"metrics\": {\"eval_302k\": 580, \"eval_peak_ext\": 642.3, \"eval_peak_ext_step\": 272000, \"note\": \"延长到 300K 确认非 collapse。eval 恢复到 642 peak@272K，200K-300K 区间震荡上行 (301-642 range)，194K→204K 骤降为 transient fluctuation。\"}, \"parent\": \"exp_023_cheetah_baseline_s4\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_023_cheetah_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_023_cheetah_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"300000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_023_cheetah_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 212000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 300000, \"tmux_session\": \"exp_023_s4_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:02:40.466Z\"}, \"exp_001_baseline_s4\": {\"completed_at\": \"2026-05-19T09:00:10.632Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:47:01.105Z\", \"hypothesis\": \"Walker Walk baseline seed=4. Fourth seed for 4-seed baseline CI. Tests whether s2 (443.5) is outlier or bimodal distribution (s1=915.7, s3=869.0).\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 922.8, \"peak_eval\": 922.8, \"peak_eval_step\": 105000, \"target_steps\": 105000, \"value_mean_final\": 576.1, \"ve_ratio_105k\": 0.624}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:00:10.632Z\"}, \"exp_023_cheetah_baseline_s4\": {\"completed_at\": \"2026-05-19T06:26:03.295Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:02.288Z\", \"hypothesis\": \"Cheetah Run baseline seed=4. Fourth seed for tighter eval return CI and NVE normalization robustness.\", \"metrics\": {\"current_step\": 212000, \"eval_return_194k\": 537.03, \"eval_return_204k\": 301.69, \"note\": \"Cheetah baseline s4. Large eval drop 194K→204K (537→302). ve_ratio>1 indicates value overestimation at final step.\", \"peak_eval\": 537.03, \"peak_eval_step\": 194000, \"target_steps\": 200000, \"value_mean_204k\": 339.14, \"ve_ratio_204k\": 1.124}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"200K env steps\", \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"dmc_cheetah_run eval episodes\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774033, \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T06:26:03.295Z\"}, \"exp_023_cheetah_baseline_s3\": {\"completed_at\": \"2026-05-19T04:08:47.459Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T21:49:33.229Z\", \"hypothesis\": \"Cheetah Run baseline seed=3. Extends 023a/023b/023_s2 (3 seeds) to 4 seeds for tighter eval return CI.\", \"metrics\": {\"current_step\": 204000, \"eval_return_202k\": 642.13, \"peak_eval\": 685.93, \"peak_eval_step\": 172000, \"target_steps\": 200000, \"value_mean_final\": 445.42, \"ve_ratio_final\": 0.694}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3\", \"checkpoint_source\": \"N/A\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 3 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s3\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"768897\", \"seed\": 3, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:47.459Z\"}, \"exp_001_baseline_s3\": {\"completed_at\": \"2026-05-19T04:08:45.989Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:03.635Z\", \"hypothesis\": \"Walker Walk baseline seed=3. Third seed for tighter baseline eval CI.\", \"metrics\": {\"current_step\": 120000, \"eval_return_102k\": 869.03, \"peak_eval\": 898.89, \"peak_eval_step\": 112000, \"target_steps\": 105000, \"value_mean_final\": 622.2, \"ve_ratio_final\": 0.692}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"105K env steps\", \"data_path\": \"dmc_walker_walk (online RL)\", \"eval_data\": \"dmc_walker_walk eval episodes\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774106, \"seed\": 3, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:45.989Z\"}, \"exp_023_cheetah_baseline_s2\": {\"completed_at\": \"2026-05-19T00:13:55.909Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:14.249Z\", \"hypothesis\": \"Cheetah Run baseline additional seed for tighter CI. Extends 023a/023b (2 seeds) to 3 seeds.\", \"metrics\": {\"current_step\": 205000, \"eval_return_final\": 645.4, \"note\": \"Cheetah Run baseline seed=2. Third baseline seed for NVE normalization.\", \"target_steps\": 200000}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 2 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s2\\\"\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.13, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"753786\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:05:57.478Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29278.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:13:55.909Z\"}, \"exp_008f_s4\": {\"completed_at\": \"2026-05-18T23:18:51.672Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-18T18:41:00.894Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=4. Additional independent seed for 008f control (existing seeds: 1/008f, 2/009c, 3/008f_s3). C2 causal contrast robustness.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_105k\": 306.5, \"note\": \"No CIVO. No-dt-emb control seed=4. Peak NVE 1.41x @85K (transient), settles to 0.58x @105K.\", \"nve_105k\": 0.58, \"peak_eval\": 487.5, \"peak_eval_step\": 55000, \"peak_nve\": 1.41, \"peak_nve_step\": 85000}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:18:51.672Z\"}, \"exp_009c_s3\": {\"completed_at\": \"2026-05-18T21:40:10.763Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T17:12:00.539Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=3. Additional seed for 009c (seed=2 NVE 1.14x at 105K on upward trajectory); tests whether NVE rise is reproducible across independent seeds or stochastic.\", \"metrics\": {\"current_step\": 108000, \"eval_return_105k\": 311.92, \"note\": \"eval peaked at 55-65K (~457) then declined to 311.92. NVE 0.52x (no CIVO). 009c seed=2 NVE 1.14x not reproduced.\", \"nve_105k\": 0.52, \"target_steps\": 105000, \"value_mean_105k\": 120.27, \"ve_ratio_105k\": 0.386}, \"parent\": \"exp_009c_008f_walker_s2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:10.762Z\"}, \"exp_001_baseline_s2\": {\"completed_at\": \"2026-05-18T21:40:09.329Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:17.571Z\", \"hypothesis\": \"Walker Walk baseline additional seed for tighter evaluation return CI.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 443.46, \"target_steps\": 105000, \"value_mean_105k\": 329.16, \"ve_ratio_105k\": 0.742}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:09.329Z\"}, \"exp_008f_s2\": {\"completed_at\": \"2026-05-18T18:41:05.369Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:16.527Z\", \"hypothesis\": \"No-dt-emb control additional seed. Extends 008f (1 seed, NVE 0.97x) for C2 causal contrast robustness.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.58, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754063\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:00.248Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9305.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:41:05.369Z\"}, \"exp_008a_cheetah_unexposed_s1\": {\"completed_at\": \"2026-05-18T18:20:00.278Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:13.377Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=1. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 504.38, \"nve_105k\": 0.478, \"target_steps\": 105000, \"value_mean_105k\": 156.97, \"ve_ratio_105k\": 0.3112}, \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:20:00.278Z\"}, \"exp_008a_cheetah_unexposed_s0\": {\"completed_at\": \"2026-05-18T18:19:58.491Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:12.052Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=0. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 532.35, \"nve_105k\": 0.49, \"target_steps\": 105000, \"value_mean_105k\": 169.98, \"ve_ratio_105k\": 0.3193}, \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:19:58.491Z\"}, \"exp_009c_s2\": {\"completed_at\": \"2026-05-18T17:12:05.307Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:19.850Z\", \"hypothesis\": \"No-dt-emb H=15 additional seed. 009c seed=2 showed NVE 1.14x at 105K on upward trajectory; additional seed tests if this is reproducible or stochastic.\", \"parent\": \"exp_009c_008f_walker_s2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.1, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754639\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:05.850Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3959.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T17:12:05.307Z\"}, \"exp_008e_v3_s4\": {\"completed_at\": \"2026-05-18T11:33:57.033Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:54:56.392Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T11:31:45.212576+00:00\"}]}, \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=4. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"civo\": false, \"eval_return\": 899.3, \"nve_note\": \"Corrected: was 0.61 (raw V/E ratio). Correct formula: max(V/E_exp / V/E_baseline_at_same_step) over [35K+]. 0.627/0.632=0.99 at 95K\", \"nve_peak\": 0.99, \"nve_peak_step\": 95000, \"ve_ratio_105k\": 0.609}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"reproduce\": {\"finished_at\": \"2026-05-18T11:31:41.800Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s4.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:45.880Z\"}, \"exp_008e_v3_s3\": {\"completed_at\": \"2026-05-18T11:24:41.197Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-18T02:54:54.691Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T11:20:58.896484+00:00\"}]}, \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=3. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"actor_entropy_final\": -4.892, \"collapse_onset\": \"85K-95K\", \"eval_return\": 92.7, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"nve_note\": \"Corrected: was 5.00 (worker used wrong baseline). Correct formula: V/E_exp / V/E_baseline_at_same_step. 2.635/0.656=4.02\", \"nve_peak\": 4.02, \"nve_peak_step\": 105000, \"peak_eval\": 520.4, \"peak_step\": 85000, \"ve_ratio_105k\": 2.635}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"reproduce\": {\"finished_at\": \"2026-05-18T11:20:55.020Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s3/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s3.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:43.665Z\"}, \"exp_008a_unexposed_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s1/latest.pt\", \"completed_at\": \"2026-05-18T08:16:42.716Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:56.020Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T08:12:12.866455+00:00\"}]}, \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=1. 直接复现 008a_no_subsample_dt2 配置（eval=778, V-recovery, no CIVO）。C3 reproducibility rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s1/metrics.jsonl\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.0028, \"civo_ve_ratio_final\": 0.43, \"eval_return_15k\": 167.12, \"eval_return_25k\": 139.94, \"eval_return_35k\": 394.15, \"eval_return_45k\": 414.32, \"eval_return_55k\": 441.48, \"eval_return_5k\": 31, \"eval_return_65k\": 491.74, \"eval_return_75k\": 452.34, \"eval_return_85k\": 546.82, \"eval_return_95k\": 628.57, \"eval_return_final\": 630.91, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 272.13, \"total_steps\": 105000, \"value_mean_final\": 271.36}, \"parent\": \"exp_008a_no_subsample_dt2\", \"reproduce\": {\"finished_at\": \"2026-05-18T08:12:09.402Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk (online RL)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724312\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:15:06.654Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10896.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:16:42.716Z\"}, \"exp_008a_unexposed_s2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/latest.pt\", \"completed_at\": \"2026-05-18T08:10:06.059Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:57.340Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T08:07:33.602043+00:00\"}]}, \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=2. 008a 新 seed 验证 protection 是否 reproducible。C3 rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/metrics.jsonl\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.003, \"civo_ve_ratio_final\": 0.333, \"eval_return_55k\": 607.5, \"eval_return_65k\": 653.8, \"eval_return_75k\": 534.4, \"eval_return_85k\": 605.4, \"eval_return_95k\": 819.4, \"eval_return_final\": 899.4, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 300.3, \"total_steps\": 105000, \"value_mean_final\": 299.4}, \"parent\": \"exp_008a_no_subsample_dt2\", \"reproduce\": {\"finished_at\": \"2026-05-18T08:07:27.087Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.84, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s2.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724965\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:19:26.303Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10239.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:10:17.263Z\"}, \"exp_008a_untrained_s1\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:51.398Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：C3 rebuttal 应复现 008a (unexposed trained dt_emb, subsample OFF) 而非 015b (frozen)。替换为 exp_008a_unexposed_s1/s2。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_008a_untrained_s2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:53.011Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：同上。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_010b_cheetah_civo_trigger_s0\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/latest.pt\", \"completed_at\": \"2026-05-18T05:11:15.900Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:47.702Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + H=8. 第二 seed 复现 Cheetah CIVO (NVE>1.5×)，加强跨环境因果论证统计力度。Rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/metrics.jsonl\", \"metrics\": {\"civo\": true, \"civo_onset_step\": \"65K\", \"detector_alert_step\": \"95K\", \"eval_return_105K\": 0.83, \"eval_return_peak\": 247.77, \"eval_return_peak_step\": \"35K\", \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"nve_105K\": 70.64, \"nve_95K\": 6.34}, \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run (online RL)\", \"gpu\": \"cuda:1\", \"model_name\": \"DreamerV3-cheetah-civo-trigger\", \"pid\": \"715412\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:11:15.900Z\"}, \"exp_024b_cheetah_no_dt_emb_s0\": {\"completed_at\": \"2026-05-18T02:00:15.236Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:50:34.104Z\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角。\", \"metrics\": {\"civo\": false, \"eval_return_final\": 96.5, \"nve_peak\": 0.2}, \"notes\": \"No CIVO (NVE peak <0.2×). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. eval 96.5 = 17.6% of baseline (548.3). Cheetah causal triangle seed 1 complete. Director confirmed results in D089.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s0/latest.pt\", \"checkpoint_source\": \"N/A-training-from-scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run-online-eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s0.log\", \"model_name\": \"DreamerV3-cheetah-no-dt-emb\", \"pid\": \"705742\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:15.808Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11279.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T02:00:17.832Z\"}, \"exp_024b_cheetah_no_dt_emb_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-18T01:56:17.025Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:51:53.604Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T01:52:09.175571+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control seed=1: gate_dt_embed_dim=0 + subsample ON + H=8. 第二 seed 验证 024 的结论（trained dt_emb 是 Cheetah CIVO 必要条件），加强因果三角的统计力度。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"metrics\": {\"baseline_pct\": 14.1, \"civo\": false, \"eval_return_final\": 77.3, \"eval_return_peak\": 129.6, \"gate_dt_2_frac\": 1, \"nve_peak\": 0.1, \"peak_step\": 15000}, \"notes\": \"No CIVO (NVE peak 0.10×, civo_alert=0 throughout). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. Gate locked at dt=2 (gate_dt_2_frac=1.0), eval 77.3 = 14% of baseline (548.3). Low performance expected: dt_embed_dim=0 removes temporal abstraction capability. Cheetah causal triangle seed 2 complete.\", \"parent\": \"exp_024_cheetah_no_dt_emb_s0\", \"pid\": \"706158\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-18T01:52:05.296Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s1/latest.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"pid\": \"706158\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:30.631Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11026.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T01:56:17.025Z\"}, \"exp_024_cheetah_no_dt_emb_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-17T20:35:13.253Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T20:34:13.657Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T20:35:16.021173+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T22:57:54.400584+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角（023a/b baseline健康 + 010b CIVO collapse + 本实验 no-emb 健康）。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-17T22:57:48.608Z\"}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL)\", \"model_name\": \"DreamerV3-no-dt-emb\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:21:27.867Z\"}, \"exp_021_full_sgs_cheetah_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-17T22:49:15.021Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T20:24:30.695Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T22:45:35.442053+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Full-SGS Cheetah Run — 验证 SGS intervention 跨环境一致性。如果 CIVO mechanism 跨环境一致，Full-SGS 在 Cheetah 也应消除 NVE>1.5x (对比 010b: NVE 8.63×, collapse)。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"metrics\": {\"baseline_pct\": 38.7, \"civo\": true, \"civo_type\": \"transient_self_correcting\", \"eval_return_final\": 221.5, \"nve_peak\": 9.94, \"nve_peak_step\": \"45K\", \"nve_sustained_55K_105K\": 0.338, \"vs_010b\": \"221.5 vs 51.7 (4.3x better)\"}, \"notes\": \"P0 priority (D070 最重要数据缺口). 018_s2 完成后立即上 cuda:0. 排序: 021 先 → 008d_s1 后. Director 2026-05-16 确认.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"pid\": \"696201\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-17T22:45:32.093Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-17T19:28:08.484Z\", \"training_hours\": 3.29}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_021_full_sgs_cheetah_s1/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.32, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"pid\": \"696201\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T19:30:02.581Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11952.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T22:57:30.295Z\"}, \"exp_023a_cheetah_baseline_s0\": {\"completed_at\": \"2026-05-17T20:34:04.841Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:19.690Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T20:31:37.915652+00:00\"}]}, \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate). Establishes Cheetah-specific baseline for NVE normalization and cross-environment validation. Comparison target for 010b (Cheetah CIVO trigger, NVE 8.27×).\", \"metrics\": {\"civo\": false, \"eval_return_final\": 624.7, \"eval_return_peak\": 624.7, \"peak_step\": 205000}, \"notes\": \"Healthy baseline. Last-5 eval mean=554.4. 185K瞬态VE spike(0.906)触发警报但20K步内恢复(205K:624.7)，非CIVO。双seed baseline均值: last-5=548.3, peak=598.8。未接W&B。\", \"reproduce\": {\"finished_at\": \"2026-05-17T20:31:34.777Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023a_cheetah_baseline_s0/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023a_cheetah_baseline_s0.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.66, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023a_cheetah_baseline_s0.log\", \"model_name\": \"DreamerV3\", \"pid\": \"683708\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T14:54:17.553Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20387.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:57.147Z\"}, \"exp_010b_cheetah_civo_trigger\": {\"completed_at\": \"2026-05-16T16:16:00.478Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:04:55.508Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T16:11:35.101384+00:00\"}]}, \"hypothesis\": \"Cheetah Run CIVO trigger — trained dt_emb, subsample ON, dt=2, H=8, seed 1. 跨环境验证：Walker 上 008d 配置在 Cheetah 上是否同样触发 CIVO (NVE>1.5x)。若成立→回应 reviewer \\\"single environment\\\" concern。\", \"metrics\": {\"civo\": true, \"eval_return_final\": 51.7, \"eval_return_peak\": 321.9, \"nve_peak\": 8.27, \"nve_peak_step\": 65000, \"peak_step\": 35000}, \"parent\": \"exp_010a_cheetah_baseline_s1\", \"reproduce\": {\"finished_at\": \"2026-05-16T16:11:32.766Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger/latest.pt\", \"checkpoint_source\": \"N/A (training from scratch, parent is baseline reference)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dm_control cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL, not eval experiment)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010b_cheetah_civo_trigger.log\", \"model_name\": \"DreamerV3+dt_emb(trained)+subsample+H8\", \"pid\": \"585826\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:05:10.473Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11450.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:38.129Z\"}, \"exp_023b_cheetah_baseline_s1\": {\"completed_at\": \"2026-05-17T19:29:52.643Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:21.197Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T19:25:39.255677+00:00\"}]}, \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate), seed=1. Second seed for Cheetah baseline to establish robust NVE normalization across seeds.\", \"metrics\": {\"civo\": false, \"eval_return_final\": 520.3, \"eval_return_peak\": 572.9, \"peak_step\": 195000, \"ve_ratio_range\": \"0.5-0.7\"}, \"notes\": \"Healthy baseline. Last-5 eval mean=542.2 (for NVE normalization). 125K后进入500-573区间震荡，无collapse。待023a完成后取双seed均值作为Cheetah baseline。未接W&B，数据在本地logdir。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:25:34.295Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023b_cheetah_baseline_s1/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023b_cheetah_baseline_s1.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.5, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023b_cheetah_baseline_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"680126\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T13:59:45.409Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 19807.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:30:46.627Z\"}, \"exp_019b_pickcube_civo_trigger\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019b_pickcube_civo_trigger/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T03:35:47.561Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:23:51.568Z\", \"error_summary\": \"KeyError in dreamer.py:421 — configs[\\\"maniskill\\\"] not found. Config block missing from dreamer.py.\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T03:35:50.727034+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T14:49:42.379952+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-17 04:01: Registry shows DONE(failed) from first attempt (KeyError transient). Actual state: RUNNING (PID 646809, step 8400+, started 11:39 UTC). Cron monitoring via submit_on_allocated tmux session. Will need manual status correction when cron detects completion.\"}}, \"failure_reason\": \"Traceback → Traceback (most recent call last): File \\\"/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py\\\", line 421, in &lt;module> recursive_update(defaults, configs[name]) ~~~~~~~^^^^^^ KeyError: 'maniskill'\", \"gpu\": \"cuda:0\", \"hypothesis\": \"PickCube-v1 CIVO trigger — trained dt_emb, subsample ON, dt=2 imagination, H=8. 预期触发 CIVO（trained dt_emb → NVE>1.5x → collapse），验证 CIVO 在 manipulation 环境是否成立\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019b_pickcube_civo_trigger.log\", \"metrics\": {\"baseline_eval_final\": 58.56, \"baseline_ratio\": 0.455, \"eval_return_final\": 26.64, \"eval_return_peak\": 26.9, \"eval_return_peak_step\": 132500, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"nve_final\": 0.065, \"nve_peak\": 3.78, \"nve_peak_step\": 52500, \"pattern\": \"transient_civo_then_value_collapse\", \"total_steps\": 200000, \"value_baseline_final\": 144.57, \"value_mean_final\": 4.26}, \"notes\": \"Cross-env CIVO confirmation + detector TN. Raw V/E peak=5.66 @52.5K (NVE=3.78× vs baseline). Transient CIVO: onset ~22.5K → peak 52.5K → deflation → eval partial recovery. Detector correctly doesn't trigger (oscillating V/E, max streak=2 < threshold=3). Eval final 26.64 vs baseline 58.56 = 45.5%. Value permanently collapsed (4.26 vs baseline 144.57). PickCube pattern: acute crisis + permanent damage, vs Walker sustained escalation.\", \"parent\": \"exp_019a_v2_pickcube_baseline\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --seed 1 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_019b_pickcube_civo_trigger\\\"\", \"finished_at\": \"2026-05-17T14:49:39.328Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-17T03:25:03.091Z\", \"training_hours\": 11.41}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_ID=0 bash scripts/exp_019b_pickcube_civo_trigger.sh\", \"data_count\": \"online\", \"data_path\": \"maniskill_PickCube-v1 (state-based, online RL)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu_id\": \"cuda:0\", \"model_name\": \"DreamerV3 + trained dt_emb + gate (maniskill_state config)\", \"pid\": 649577, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T15:20:38.182Z\"}, \"exp_022b_no_curriculum\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022b_no_curriculum/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T14:01:23.413Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:49:08.181Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T13:56:29.726988+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) + learned gate WITHOUT curriculum (phase1=0, phase2=0, gate fully unlocked from step 0). Tests whether frozen dt_emb prevents CIVO (NVE < 1.5×) while allowing the gate to learn meaningful temporal abstraction (gate_dt_1_frac < 1.0). exp_022 was inconclusive because curriculum locked gate for the entire run; this rerun removes that confound.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"metrics\": {\"civo_alert_max\": 0, \"eval_return_105K\": 300.7, \"gate_dt_1_frac_105K\": 0.145, \"gate_dt_mean_105K\": 3.41, \"gate_entropy_ratio_105K\": 0.912, \"gate_near_uniform\": true, \"nve_peak\": 1.22, \"ve_ratio_105K\": 0.075, \"ve_ratio_peak\": 0.218}, \"notes\": \"Frozen dt_emb (random init, no gradients) successfully prevents CIVO: ve_ratio peaked 0.218 (NVE≈1.22×), civo_alert=0 throughout. Confirms C2 (trained dt_emb is necessary for CIVO). Gate converges to near-uniform distribution (entropy_ratio=0.912, no temporal coherence), eval_return=300.7 (32.8% of baseline@105K=915.7). Frozen random dt_emb is sufficient CIVO fix but insufficient for meaningful temporal abstraction — multi-rate imagination's inherent performance limitation.\", \"parent\": \"exp_022_untrained_dt_emb_learned_gate\", \"pid\": \"670554\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"finished_at\": \"2026-05-17T13:56:27.483Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.16, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"pid\": \"670554\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T10:51:56.898Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11366.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T14:20:12.115Z\"}, \"exp_022_untrained_dt_emb_learned_gate\": {\"completed_at\": \"2026-05-17T07:44:38.596Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T04:16:57.150Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T07:44:42.334281+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T10:47:17.307752+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"Config error: used --configs dmc_vision (CNN+image, wrong modality) instead of dmc_proprio, and --compile True (torch.compile inductor crash). Killed and resubmitting with correct config.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) prevents CIVO by blocking the trained-embedding-driven value overestimation feedback loop, while the learned gate (Gumbel-softmax, receives gradients) retains adaptive horizon selection capability. If successful, this decouples temporal abstraction benefits from CIVO vulnerability.\", \"metrics\": {\"civo_alert\": 0, \"civo_ve_ratio_105K\": 0.4, \"eval_return_105K\": 189.1, \"eval_return_65K\": 493.1, \"eval_return_75K\": 573.8, \"final_eval_return\": 189.1, \"gate_collapsed\": true, \"gate_dt_1_frac\": 1, \"gate_entropy\": 0, \"peak_eval_return\": 573.8, \"train_return_112K\": 91.8}, \"notes\": \"INCONCLUSIVE: Gate never activated due to curriculum misconfiguration. phase1=50000 × action_repeat=2 = 100K logger steps, experiment only 105K total. gate_scale reached only 0.006, gate locked at dt=1 entire run. eval_return: 75K=573.8 → 105K=189.1 (collapsed without gate involvement). Rerun as exp_022b with curriculum disabled.\", \"parent\": \"exp_008f_s3_no_dt_embed_walker + exp_005_gate_arch (combines safe dt_emb from 008f with gate architecture from 005 series)\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:47:12.534Z\"}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022_untrained_dt_emb_learned_gate/checkpoint.ckpt\", \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --imag_horizon 8 --logdir ./logdir/exp_022_untrained_dt_emb_learned_gate\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, proprio obs)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"gpu_id\": \"cuda:1\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022_untrained_dt_emb_learned_gate.log\", \"model_name\": \"DreamerV3 + frozen dt_emb (d=32) + learned gate (Gumbel-softmax)\", \"pid\": 661595, \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T07:47:20.391Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10901.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:56:34.274Z\"}, \"exp_019a_v2_pickcube_baseline\": {\"completed_at\": \"2026-05-16T21:07:12.193Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T20:12:22.372Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\"}}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Vanilla DreamerV3 on ManiSkill3 PickCube establishes a cross-environment baseline; if stable, subsequent CIVO trigger experiment (019b) can test whether CIVO generalizes beyond DMC Walker Walk.\", \"metrics\": {\"eval_return_final\": 69.43, \"eval_return_peak\": 69.7, \"eval_return_peak_step\": 162500, \"steps_completed\": 200248, \"value_mean_final\": 143.4, \"ve_ratio_final\": 2.07, \"ve_ratio_range\": \"1.05-3.56\"}, \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\", \"parent\": \"exp_001_baseline\", \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline/checkpoint.ckpt\", \"checkpoint_source\": \"auto-resume from logdir\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled False --seed 1 --steps 200000 --compile False --device cuda:1 --logdir ./logdir/exp_019a_v2_pickcube_baseline\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill3 PickCube-v1 (online RL)\", \"eval_data\": \"N/A - training experiment\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline\", \"model_name\": \"DreamerV3-S\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:44:41.396Z\"}, \"exp_007_fixed_dt4\": {\"account\": \"root\", \"checkpoint_path\": \"N/A - killed, dt=4 confirmed too coarse for locomotion (D013)\", \"completed_at\": \"2026-05-13T22:32:00.591Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T22:15:44.218Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T22:32:01.413690+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\"}}, \"failure_reason\": \"dt=4 confirmed too coarse for locomotion: eval_return 127@35K vs baseline 389 (-67.4%). model_loss comparable to baseline — RSSM can learn 4-step dynamics, but action temporal resolution too coarse for Walker Walk. Confirms dt sweet spot ∈ {1,2}. See D013.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"诊断实验：fixed dt=4 vs dt=2 vs learned gate。硬编码 dt=4，其余超参与 exp_006 完全一致。与 exp_006(dt=2) 对照：如果 dt=4 也不掉 return，说明跳步本身无害，问题在 learned gate 机制；如果 dt=4 掉但 dt=2 不掉，说明存在跳步边界。\", \"metrics\": {\"baseline_45K\": 443, \"eval_return_15K\": 129.6, \"eval_return_25K\": 176.9, \"eval_return_35K\": 126.7, \"eval_return_45K\": 144.41, \"eval_return_55K\": 152.49, \"eval_return_5K\": 31, \"model_loss_15K\": 6.337, \"model_loss_25K\": 5.089, \"model_loss_35K\": 4.755, \"model_loss_5K\": 17.927, \"peak_return\": 176.9, \"peak_step\": \"25K\", \"step\": 48000, \"trend\": \"peak 176.9@25K, low plateau ~127-152; value extremely suppressed (v/e 6-13%), NOT delusional critic but severe learning failure\", \"value_eval_ratio_45K\": 0.126, \"value_eval_ratio_55K\": 0.061, \"value_mean_45K\": 18.26, \"value_mean_55K\": 9.28, \"vs_baseline_45K\": \"-67.4%\"}, \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\", \"parent\": \"exp_006_fixed_dt2\", \"reproduce\": {\"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"finished_at\": \"2026-05-13T22:32:00.443Z\"}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v2_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt4_v2_s1\", \"model_name\": \"DreamerV3+FixedDt4 (gate_fixed_dt=4, no learned gate, init_dt fix applied)\", \"pid\": \"90354\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.869Z\"}, \"exp_008c_no_subsample_dt2_h8\": {\"completed_at\": \"2026-05-14T04:09:46.829Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T01:33:31.413Z\", \"hypothesis\": \"隔离 compounding error 效应：subsample OFF + imagination dt=2 + H=8（物理覆盖 16 步 ≈ baseline H=15）。与 008a(H=15) 对照：008a 崩但 008c 不崩 → compounding error 是根因，H 需与 dt 反比补偿；两个都崩 → dt=2 RSSM 预测质量本身不足。\", \"metrics\": {\"actor_loss_55K\": -0.082, \"actor_loss_65K\": -0.053, \"baseline_65K\": 616, \"data_source_35K\": \"from training logs metrics.jsonl\", \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.55, \"eval_return_55K\": 241.87, \"eval_return_65K\": 240.86, \"step\": 68000, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_35K\": 0.218, \"value_eval_ratio_55K\": 0.291, \"value_eval_ratio_65K\": 0.328, \"value_mean_35K\": 40.43, \"value_mean_55K\": 70.32, \"value_mean_65K\": 78.96, \"verdict_65K\": \"PLATEAU\", \"vs_baseline_65K\": \"-60.9%\"}, \"parent\": \"exp_006_fixed_dt2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008c_fixed_dt2_no_subsample_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.53, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=1, imag_horizon=8)\", \"pid\": \"107021\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:47.540Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9119.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.359Z\"}, \"exp_003_event_gated_v2\": {\"completed_at\": \"2026-05-13T09:58:31.673Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T04:52:22.660Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T09:58:32.493437+00:00\"}]}, \"failure_reason\": \"Return 崩塌至 baseline 13%。根因：_imagine 中 gate dt 无约束（输出 dt∈{1,...,8}），而 subsample curriculum 限制训练数据 dt≤effective_max_dt。RSSM 对未训练的大 dt 预测为噪声，progressive poisoning 导致 actor/critic 不可恢复。需修复 dt clipping + logits masking 后从头训练。\", \"metrics\": {\"eval_return_105K\": 92.3, \"eval_return_115K\": 118.7, \"fps\": 6.52, \"gate_dt_1_frac_116K\": 0.218, \"gate_dt_mean_116K\": 2.67, \"gate_dt_std_116K\": 1.46, \"gate_empirical_entropy_116K\": 1.655, \"gate_entropy_ratio_116K\": 0.796, \"gate_scale_116K\": 0.61, \"mvp_C1_return\": \"FAIL (0.13)\", \"mvp_C2_entropy\": \"PASS (1.655)\", \"mvp_C3_heff\": \"PASS (2.667x)\", \"mvp_C4_structure\": \"PASS (autocorr=0.652)\", \"return_ratio_105K\": 0.1, \"return_ratio_115K\": 0.13, \"step\": 120000}, \"parent\": \"exp_001_baseline\", \"reproduce\": {\"finished_at\": \"2026-05-13T09:58:31.205Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"logdir/event_gated_s1_v2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1_v2 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Subsample curriculum prevents early destabilization while event gate learns meaningful variable-rate stepping\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v2 (final fix: env step sync + threshold 25K/75K)\", \"pid\": 27009, \"seed\": 1, \"server\": \"autodl-rtx6000\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:35.459Z\"}, \"exp_004_event_gated_v3\": {\"completed_at\": \"2026-05-13T15:23:26.384Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T10:05:16.227Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T15:23:27.393422+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_return_15K\": 153.86, \"fps\": 8.1, \"gate_dt_mean_15K\": 1, \"gate_scale_15K\": 0, \"step\": 20000}}}, \"failure_reason\": \"gate_loss 爆炸 bug：compute_gate_targets 使用 gate_max_dt=8 生成 target 分布但 logits masking 使用 effective_max_dt，cross-entropy loss ≈ 3e8。eval_return@125K=352 vs baseline@335K=942，ratio=0.37。第三次 train/imagine distribution mismatch。\", \"hypothesis\": \"修复 imagination dt 约束后（logits masking + clamp safety net），event gate 在 train/imagine 分布同步条件下能产生有意义的 variable-rate stepping 且 return ≥ 80% baseline\", \"parent\": \"exp_003_event_gated_v2\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A - killed due to gate_loss explosion bug\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v4_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.19, \"gpu_id\": 1, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v4_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v3 (dt clipping + logits masking + dt alignment fix)\", \"pid\": 36645, \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T10:12:04.157Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18682.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:34.482Z\"}, \"exp_005_event_gated_v4\": {\"checkpoint_path\": \"N/A - killed due to structural failure of hard Gumbel gate\", \"completed_at\": \"2026-05-13T22:15:21.359Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T16:08:06.061Z\", \"failure_reason\": \"Hard Gumbel gate 结构性失败。3轮 bug 修复后仍崩塌：eval_return 峰值 541.18@55K → 持续下降 → 98.84@145K（baseline 同期 950.9）。Gate 机制有效（entropy/H_eff/structure 全 PASS），但 hard categorical gate + variable-rate imagination 与 actor-critic 优化存在结构性冲突。gate_scale>0.5 后 return 不可恢复。\", \"hypothesis\": \"Event-gated adaptive horizon (learned gate activation for dt selection) improves sample efficiency over fixed-horizon DreamerV3 by dynamically extending imagination when beneficial.\", \"latest_metrics\": {\"alert\": \"return_declining_at_phase2_onset\", \"baseline_at_65K\": 615.9, \"checked_at\": \"2026-05-13\", \"eval_return\": 465.67, \"eval_return_trajectory\": {\"15K\": 153.9, \"25K\": 254.2, \"35K\": 290.8, \"45K\": 443, \"55K\": 541.2, \"5K\": 31, \"65K\": 465.7}, \"fps\": 6.69, \"gap_vs_baseline\": -150.2, \"gate_dt_1_frac\": 0.965, \"gate_dt_2_frac\": 0.035, \"gate_dt_mean\": 1.035, \"gate_dt_std\": 0.036, \"gate_empirical_entropy\": 0.0499, \"gate_entropy_bonus\": 0.0865, \"gate_entropy_ratio\": 0.072, \"gate_loss\": 0.00663, \"gate_scale\": 0.10004, \"phase2_status\": \"gate刚进入phase2 (gate_scale=0.1), dt=1占比96.5%, gate几乎未激活。eval_return在55K→65K出现14%下降(541→466), 与phase2启动时机吻合, 类似exp_003崩塌前兆。但baseline同期也有小幅回调(626→616, -1.6%), 且gate尚未真正激活, 需继续观察75K数据确认是正常波动还是collapse。\", \"pid\": 51721, \"prev_eval_return\": 541.18, \"process_status\": \"running\", \"step\": 65000, \"train_return_latest\": 569.8, \"train_return_range\": [535.4, 602.1], \"uptime\": \"2h31m\"}, \"metrics\": {\"baseline_at_145K\": \"~950\", \"eval_return_105K\": 276.08, \"eval_return_145K\": 98.84, \"eval_return_15K\": 153.9, \"eval_return_35K\": 290.8, \"eval_return_55K\": 541.18, \"eval_return_5K\": 31, \"eval_return_65K\": 465.67, \"eval_return_85K\": 212.34, \"final_return\": 98.84, \"fps\": 6.69, \"gate_dt_mean_105K\": 2.054, \"gate_dt_std_105K\": 0.907, \"gate_entropy_105K\": 1.255, \"gate_scale_105K\": 0.5, \"note\": \"85K/105K metrics corrected from 319.3/337.8 to 212.34/276.08\", \"peak_return\": 541.18, \"peak_step\": \"55K\", \"return_ratio_final\": 0.104, \"step\": 145000}, \"parent\": \"exp_004_event_gated_v3\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 6.12, \"hypothesis\": \"修复 gate_target/masking 维度不匹配 + effective_max_dt 单一来源架构 + 全量审计后，event gate return >= 80% baseline\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_005_event_gated_v4.log\", \"model_name\": \"DreamerV3+EventGate_v4\", \"pid\": \"51721\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T16:08:11.913Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 22029.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:33.514Z\"}, \"exp_008d_civo_trigger_s3\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s3/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T03:24:26.004Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T00:25:47.784Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T03:18:40.430236+00:00\"}]}, \"hypothesis\": \"Trained dt-emb with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) induces CIVO (NVE≥1.5×) on seed=3, confirming CIVO onset is systematic across seeds regardless of replay sampling sequence (seed bug fix verification).\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"metrics\": {\"baseline_eval_105K\": 915.67, \"collapse_onset_step\": 95000, \"collapse_type\": \"late-onset\", \"eval_return_final\": 267.6, \"eval_return_final_step\": 105000, \"eval_return_peak\": 451.7, \"eval_return_peak_step\": 95000, \"nve_final\": 1.53, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.5, \"nve_peak\": 1.53, \"nve_peak_step\": 105000, \"nve_sustained_45K_55K\": true, \"total_steps\": 112000, \"train_return_final_avg\": 138, \"train_return_final_range\": \"82-214\", \"value_mean_final\": 268.4, \"vs_baseline_105K\": \"-70.8%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-17T03:18:37.221Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint, new logdir)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 3 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s3\\\"\", \"data_count\": 105000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"635744\", \"seed\": 3, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T00:25:59.245Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10706.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:24:26.004Z\"}, \"exp_018v2_full_sgs_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018v2_full_sgs_walker_s1/latest.pt\", \"completed_at\": \"2026-05-16T17:24:44.481Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T13:42:15.786Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T17:17:46.576638+00:00\"}]}, \"hypothesis\": \"Full Selective Gradient Stopping (blocking obs+reward+cont decoder gradients to dt_emb) eliminates all gradient pathways creating dt-specific representations, thereby preventing CIVO onset and collapse.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"metrics\": {\"civo_reduction_pct\": 79, \"eval_return_final\": 448.3, \"eval_return_final_step\": 105000, \"eval_return_peak\": 499.6, \"eval_return_peak_step\": 75000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"late_collapse_detected\": true, \"late_collapse_step\": 112000, \"nve_final\": 1.34, \"nve_mean_45k_105k\": 1.23, \"nve_peak\": 1.66, \"nve_peak_step\": 95000, \"total_steps\": 112000, \"total_updates\": 25099, \"value_loss_final\": 0.6}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-16T17:17:44.050Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (training from scratch, parent is predecessor not checkpoint source)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 1 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018v2_full_sgs_walker_s1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, no static dataset)\", \"eval_data\": \"dmc_walker_walk eval episodes (online)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.49, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"589564\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:55:10.231Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12574.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:57:18.423Z\"}, \"exp_018_full_sgs_s2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_s2/checkpoint.pt\", \"completed_at\": \"2026-05-16T23:47:49.458Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T19:33:26.266Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Full-SGS reliably prevents CIVO across seeds; if seed=2 also survives without collapse, SGS is a robust intervention mechanism for deployment.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"notes\": \"CIVO collapse confirmed: eval 40.8@105K (from peak ~488@75K). NVE peaked 1.66× at 95K (35K+ window). Full-SGS did NOT prevent collapse in seed 2 — contradicts 018v2 (seed 1) which avoided collapse. This invalidates SGS_full as a reliable CIVO prevention method. Key difference from 018v2: 018_s2 collapsed while 018v2 sustained. n=2 for SGS_full now shows collapse_rate=0.5.\", \"parent\": \"exp_018v2_full_sgs_walker_s1\", \"pid\": \"612876\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.04, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"pid\": \"612876\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T19:45:40.838Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 14528.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:37.385Z\"}, \"exp_008f_no_dt_embed_subsample_on_h8\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8/latest.pt\", \"completed_at\": \"2026-05-14T09:32:53.461Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:51:27.592Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T09:30:42.170428+00:00\"}]}, \"hypothesis\": \"Without trained dt-embedding, subsample mechanism alone does not induce value overestimation, isolating dt-embedding as the necessary causal factor for CIVO.\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"trained dt_embedding → value overestimation → actor exploitation → collapse. Without dt_embedding, value self-corrects.\", \"current_step\": 105000, \"eval_checkpoints\": {\"105K\": {\"eval_return\": 503, \"normalized_ve\": 0.3, \"value_mean\": 98.2}, \"15K\": {\"eval_return\": 182.03, \"value_mean\": 2.989, \"ve_ratio\": 0.01642}, \"25K\": {\"baseline_ve\": 0.087, \"eval_return\": 196.78, \"normalized_ve\": 1.02, \"value_mean\": 17.507, \"ve_ratio\": 0.089}, \"35K\": {\"baseline_ve\": 0.241, \"eval_return\": 206.67, \"normalized_ve\": 0.73, \"value_mean\": 36.279, \"ve_ratio\": 0.176}, \"45K\": {\"baseline_ve\": 0.331, \"eval_return\": 194.08, \"normalized_ve\": 0.83, \"value_mean\": 53.429, \"ve_ratio\": 0.275}, \"55K\": {\"baseline_ve\": 0.404, \"eval_return\": 173.45, \"normalized_ve\": 0.97, \"value_mean\": 67.899, \"ve_ratio\": 0.391}, \"5K\": {\"eval_return\": 30.49, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, \"65K\": {\"eval_return\": 375, \"normalized_ve\": 0.37}, \"75K\": {\"eval_return\": 324, \"normalized_ve\": 0.42}, \"85K\": {\"eval_return\": 246, \"normalized_ve\": 0.65, \"value_mean\": 111.8}, \"95K\": {\"eval_return\": 319, \"normalized_ve\": 0.54}}, \"last_updated\": \"2026-05-14T09:50:00\", \"target_steps\": 105000, \"trend\": \"Zigzag recovery with high variance: eval 207→194→173@55K→375→324→246→319→503@105K. NOT a clean V-shape — high inter-eval variance throughout. Value self-corrected: peaked 111.8@85K then declined to 98.2@105K. Normalized v/e: 0.97x@55K→0.37x@65K→0.65x@85K→0.30x@105K. Key contrast with 008d: value only accelerates (69.3%@45K) vs 008f value self-corrects.\", \"verdict\": \"SUCCESS - zigzag recovery to 503@105K, normalized v/e=0.30x, C2 confirmed\", \"vs_baseline_105K\": \"-45.1%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-14T09:30:41.254Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_embed_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.68, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"pid\": \"127761\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:51:55.020Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16858.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:33.517Z\"}, \"exp_016d_sgs_walker_s1\": {\"completed_at\": \"2026-05-15T19:35:10.508Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:29:41.130Z\", \"failure_reason\": \"Same hang as 016c — SummaryWriter.flush() deadlock after add_video with moviepy 2.x. try/except insufficient because flush() blocks on incomplete async video encode. Fix: Logger.video() → no-op.\", \"hypothesis\": \"Selective Gradient Stopping (reward_dt_emb_detach) blocks reward-gradient pathway to dt_emb, preventing CIVO-inducing co-adaptation while preserving task performance.\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"第5次启动。两项修复生效：MUJOCO_EGL_DEVICE_ID=1 + logger.video注释。旧PID 526153已自行退出。\", \"pid\": 526939, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:28.152Z\"}, \"exp_001_baseline\": {\"completed_at\": \"2026-05-13T15:23:24.593Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T02:09:53.875Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T15:23:25.663340+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T21:47:19.804301+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_return_205K\": 907.1, \"eval_return_215K\": 919.8, \"fps\": 8.3, \"step\": 245000, \"train_return_244K\": \"935-976\"}}}, \"failure_reason\": \"误报：cron 检测到进程退出但实际是正常完成（512K步）。已核实 checkpoint 229MB 有效。\", \"hypothesis\": \"Vanilla DreamerV3 on Walker Walk converges to stable high-return policy (>900) within 500K steps, establishing the performance ceiling for all gated variants.\", \"latest_metrics\": {\"checked_at\": \"2026-05-13\", \"eta_hours\": 1.8, \"eval_return\": 953.37, \"eval_step\": 445000, \"fps\": 7.29, \"pid\": 9409, \"prev_eval_return\": 964.96, \"process_status\": \"running\", \"step\": 452000, \"steps_remaining\": 48000, \"train_return_latest\": 958.07, \"train_return_range\": [917, 985.8], \"uptime\": \"16h35m\"}, \"metrics\": {\"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_last10_mean\": 950.9, \"eval_return_peak\": 970.41, \"eval_return_peak_step\": 505000, \"eval_trajectory\": {\"105K\": 915.67, \"115K\": 919.81, \"125K\": 921.37, \"135K\": 900, \"145K\": 932.16, \"155K\": 933.34, \"15K\": 206.61, \"165K\": 907.98, \"175K\": 918.87, \"185K\": 954.69, \"195K\": 936.09, \"205K\": 949.24, \"215K\": 913.4, \"225K\": 962.44, \"235K\": 937.24, \"245K\": 934.42, \"255K\": 948.45, \"25K\": 395.27, \"265K\": 925.09, \"275K\": 931.51, \"285K\": 925.75, \"295K\": 936.3, \"305K\": 939.33, \"315K\": 948.42, \"325K\": 967.75, \"335K\": 942.41, \"345K\": 969.83, \"355K\": 941.11, \"35K\": 388.47, \"365K\": 935.76, \"375K\": 918.24, \"385K\": 937.98, \"395K\": 955.38, \"405K\": 937.83, \"415K\": 948.99, \"425K\": 954.64, \"435K\": 964.96, \"445K\": 953.37, \"455K\": 945.84, \"45K\": 513.77, \"465K\": 947.81, \"475K\": 947.66, \"485K\": 930.6, \"495K\": 944.73, \"505K\": 970.41, \"55K\": 625.73, \"5K\": 31.77, \"65K\": 615.86, \"75K\": 596.28, \"85K\": 713.93, \"95K\": 871.06}, \"final\": true, \"step\": 512000, \"value_eval_ratio_105K\": 0.656, \"value_eval_ratio_25K\": 0.087, \"value_eval_ratio_35K\": 0.241, \"value_eval_ratio_45K\": 0.331, \"value_eval_ratio_55K\": 0.404, \"value_eval_ratio_65K\": 0.563, \"value_eval_ratio_75K\": 0.719, \"value_eval_ratio_85K\": 0.701, \"value_eval_ratio_95K\": 0.632, \"value_eval_ratio_stable\": \"~69-72% from 135K+\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T21:47:18.966Z\"}, \"retry_count\": 1, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/baseline_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"hypothesis\": \"DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"pid\": 9409, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:24.099Z\"}, \"exp_008d_civo_trigger_s2\": {\"completed_at\": \"2026-05-17T00:24:10.180Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T19:32:16.790Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed 1 — CIVO trigger 第 3 个独立 seed (D1)。预期 NVE>1.5× 触发 CIVO。用于 bootstrap CI 闭合 trained_dt_emb condition (现有: seed 0 = 008d, seed 2 = 009b)。注意: 原名 s2 但实际需跑 seed=1 (避免与 009b seed=2 重复)。\", \"notes\": \"Killed by Director order: seed bug confirmed. --seed 1 was parsed incorrectly, producing bit-for-bit identical results to seed=0. PID 628482 killed. Will resubmit after seed bug fix with seed=3.\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint loaded)\", \"command\": \"source /root/miniconda3/bin/activate && cd /root/event-gated-adaptive-horizon && python train.py --configs dmc_vision --task dmc_walker_walk --logdir ./logdir/008d_civo_trigger_s2 --seed 1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --steps 120000\", \"data_count\": 120000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.57, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s2.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"628477\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T22:49:55.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 5654.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T00:24:10.180Z\"}, \"exp_008f_s3_no_dt_embed_walker\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_s3_no_dt_embed_walker/checkpoint.ckpt\", \"completed_at\": \"2026-05-16T20:09:51.135Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:04:28.878Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 3 — 008f 系列第 3 个独立 seed，闭合 no_dt_emb condition 的 bootstrap CI（当前 n=2，需 ≥3）。预期 NVE<1.5×，无 CIVO。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"metrics\": {\"collapse\": false, \"eval_return_final\": 363.8, \"nve_peak\": \"< 1.5x\"}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"601233\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.81, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"pid\": \"601233\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T17:21:24.538Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10106.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T20:09:51.135Z\"}, \"exp_020_vanilla_dreamerv3_s2\": {\"completed_at\": \"2026-05-16T19:43:57.604Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:23:55.837Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T19:40:49.938571+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Vanilla DreamerV3 (no dt_emb, no subsample, no gate) seed 2 — Pathway B 控制实验：验证 008e_v3_s2 的 eval-driven collapse 是否需要 trained dt_emb 作为必要条件。如果 vanilla s2 稳定 → C6 成立 (trained dt_emb 是 Pathway B 必要条件)。如果也崩溃 → Pathway B 是 DreamerV3 inherent fragility。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"metrics\": {\"collapse\": false, \"comparison_with_parent\": {\"c6_confirmed\": true, \"delta\": \"vanilla stable (836.5) vs trained dt_emb collapsed (136.96)\", \"parent_collapsed\": true, \"parent_eval_105K\": 136.96, \"parent_id\": \"exp_008e_v3_walker_s2\", \"parent_nve_105K\": 3.78}, \"eval_trajectory\": [{\"eval_return\": 41.2, \"step\": 5000}, {\"eval_return\": 534.1, \"step\": 55000}, {\"eval_return\": 688.9, \"step\": 65000}, {\"eval_return\": 596.2, \"step\": 95000}, {\"eval_return\": 836.5, \"step\": 105000}], \"final_eval_return\": 836.5, \"final_value_mean\": 539.3, \"peak_eval_return\": 836.5, \"peak_eval_step\": 105000, \"train_return_range_108K\": \"511-808\", \"ve_ratio_105K\": 0.645}, \"notes\": \"Pathway B 控制实验 (D6)。vanilla config: dt_embed_dim=0, subsample OFF, H=15, seed=2, 105K steps, Walker Walk。排队等 010b 完成后在 cuda:0 提交。命令: dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 2 --compile True --device cuda:0 --imag_horizon 15\", \"parent\": \"exp_008e_v3_walker_s2\", \"pid\": \"596344\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-16T19:40:47.795Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"logdir/exp_020_vanilla_dreamerv3_s2/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"pid\": \"596344\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T16:45:55.371Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10682.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:43:57.604Z\"}, \"exp_019a_pickcube_baseline\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T13:43:00.745Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T03:23:50.639Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"PickCube-v1 baseline — dt=1, no dt_emb (dim=0), subsample OFF. ManiSkill3 manipulation 环境稳定基线，验证 CIVO 诊断在 manipulation 中的适用性\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"notes\": \"ManiSkill3 Phase 1. 排队等 cuda:1 (010a 完成后). --compile False --device cuda:1. maniskill_state config.\", \"pid\": \"586751\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-16T12:00:04.473Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (killed before completion)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.37, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"pid\": \"586751\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:20:56.230Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1324.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:43:00.745Z\"}, \"exp_018_full_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T12:43:09.226Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T23:30:39.991Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T12:40:17.132664+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Full-SGS: detach all non-KL gradients from dt_emb (removes 93% obs decoder contribution). If CIVO persists → vulnerability is representation-level; if eliminated → obs decoder gradient is root cause.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_walker_s1.log\", \"metrics\": {\"eval_return_final\": 915.7, \"eval_return_final_step\": 105000, \"eval_return_peak\": 915.7, \"eval_return_peak_step\": 105000, \"nve_peak\": 0.72, \"nve_peak_step\": 75000, \"nve_sustained_avg\": 0.55, \"nve_sustained_max\": 0.72, \"total_steps\": 112000, \"train_return_final_avg\": 899.4, \"value_mean_final\": 601.1}, \"notes\": \"⚠️ INVALID: 训练命令缺失 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8。gate_enabled=false → dt_embedding 未创建 → full_sgs 是空操作 → 实际等同 vanilla baseline。所有基于此实验的 claim (CIVO elimination, gradient-level vulnerability) 需要 018v2 重新验证。\", \"parent\": \"exp_016e_sgs_walker_s1\", \"pid\": \"577467\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_018_full_sgs_walker_s1 --steps 105000 --full_sgs True --seed 1 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T12:40:14.687Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-16T09:50:18.238Z\", \"training_hours\": 2.83}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:42:11.339Z\"}, \"exp_010a_cheetah_baseline_s1\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/latest.pt\", \"completed_at\": \"2026-05-16T12:01:01.080Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:27.101Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T11:59:12.312213+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Cheetah Run baseline seed 1 — 建立第二环境 dt=1 参考基线，为跨环境验证 C1/C2 做准备（plan_020）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log\", \"metrics\": {\"eval_return_final\": 849.8, \"eval_return_final_step\": 515000, \"eval_return_peak\": 849.8, \"eval_return_peak_step\": 515000, \"final_step\": 524000, \"total_eval_episodes\": 52, \"train_return_last\": 716}, \"notes\": \"Director 排期: cuda:0 上排在 009d 之后。\", \"pid\": \"536890\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s1 --steps 512000 --seed 1 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T11:59:09.914Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T22:48:05.456Z\", \"training_hours\": 13.18}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:01:11.169Z\"}, \"exp_009d_baseline_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T12:10:01.788Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:55:00.039Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T12:10:04.203907+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T12:24:17.652463+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T09:48:44.475703+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\"}}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 0 — 第三独立 baseline seed，建立 v/e 校准参考（plan_010）\", \"metrics\": {\"eval_return\": 927.6, \"eval_return_at_508K\": 927.6, \"eval_return_peak\": 950.96, \"eval_return_peak_step\": 398000, \"note\": \"COMPLETED 508K/500K, final eval 927.6, peak 950.96@398K\", \"step\": 508000}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\", \"parent\": \"exp_001_baseline\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T09:48:42.388Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T12:06:19.592Z\", \"training_hours\": 21.71}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/checkpoint.ckpt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/metrics.jsonl\", \"model_name\": \"DreamerV3_baseline\", \"pid\": \"149703\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T09:50:34.506Z\"}, \"exp_017_subsample_off_trained_dt_emb\": {\"completed_at\": \"2026-05-16T04:46:30.361Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T10:44:24.756Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample OFF + dt=2 imagination + H=15 seed 1 — 2×2 消融矩阵: 隔离 subsample 训练数据的因果效应。与 008a (untrained dt_emb, subsample OFF) 唯一差异是 dt_emb trained vs untrained。如果 017 崩而 008a 不崩 → 确认 trained dt_emb 是 CIVO 根因，即使训练数据全为 dt=1（plan_017, C2）\", \"notes\": \"D044: 取消。008a 配置验证确认 017 与 008a 完全重复（trained dt_emb + subsample OFF + H=15 + seed 1）。008a 的\\\"untrained\\\"含义是\\\"dt_emb 存在但未接触 dt>1 数据\\\"，不是 frozen/absent。2×2 矩阵已由 008a/008d/008f/015b 闭合。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:46:30.361Z\"}, \"016e\": {\"completed_at\": \"2026-05-16T01:39:17.916Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T22:21:09.251Z\", \"notes\": \"重复条目，权威数据在 exp_016e_sgs_walker_s1 (DONE/negative)。此条目为 NVE 诊断过程中误创建的冗余记录。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T01:39:17.916Z\"}, \"exp_016e_sgs_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T22:31:16.457Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T19:35:20.242Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016）。第五次重试，修复 Logger.video() → no-op 彻底消除 SummaryWriter.add_video/flush 死锁\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/\", \"metrics\": {\"actor_loss_sign_flip_step\": 95000, \"civo_catastrophic_step\": 95000, \"civo_detected\": true, \"civo_nve_peak\": 10.42, \"civo_nve_peak_step\": 95000, \"civo_onset_step\": 85000, \"civo_severity\": \"catastrophic\", \"current_step\": 100000, \"data_source\": \"metrics.jsonl from logdir/exp_016e_sgs_walker_s1/, completed 100K steps, SSH 2026-05-16T06:25\", \"deep_analysis\": {\"016e_vs_008d_entropy_comparison\": {\"15K\": {\"008d\": 0.481, \"016e\": 1.049, \"delta\": 0.568}, \"25K\": {\"008d\": -1.862, \"016e\": -1.554, \"delta\": 0.308}, \"35K\": {\"008d\": -3.465, \"016e\": -2.118, \"delta\": 1.347}, \"45K\": {\"008d\": -4.575, \"016e\": -3.455, \"delta\": 1.12}, \"55K\": {\"008d\": -4.879, \"016e\": -3.617, \"delta\": 1.262}, \"interpretation\": \"SGS preserves ~1.0-1.3 nats higher entropy through 35-55K, enabling better exploration\"}, \"016e_vs_008d_value_at_crash\": {\"008d\": {\"disconnect_ratio\": 1.67, \"eval_return\": 82.75, \"value_mean\": 137.88}, \"016e\": {\"disconnect_ratio\": 6.58, \"eval_return\": 31.73, \"value_mean\": 208.88}, \"interpretation\": \"016e value completely decoupled from reality; 008d still weakly correlated\"}, \"actor_loss_sign_flip\": {\"008d_min_actor_loss\": -0.073, \"008d_never_flipped\": true, \"016e_flip_step\": 95000, \"016e_flip_value\": 0.014, \"interpretation\": \"sign flip = value critic drives actor toward worse actions, triggering catastrophic collapse\"}, \"train_return_collapse_timeline\": {\"100K\": [109, 111, 102, 108], \"88K\": [140, 145, 116, 116], \"92K\": [50, 29, 34, 75], \"96K\": [86, 41, 50, 101], \"interpretation\": \"collapse visible in train_return by 92K; partial recovery by 100K but far below peak\"}}, \"eval_checkpoints\": [{\"eval_return\": 31, \"step\": 5000, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, {\"eval_return\": 140.3, \"step\": 15000, \"value_mean\": 3.1, \"ve_ratio\": 0.022}, {\"baseline_ve\": 0.087, \"eval_return\": 141.75, \"nve\": 1.86, \"step\": 25000, \"value_mean\": 22.97, \"ve_ratio\": 0.162}, {\"baseline_ve\": 0.241, \"eval_return\": 173.01, \"nve\": 1.28, \"step\": 35000, \"value_mean\": 53.55, \"ve_ratio\": 0.309}, {\"baseline_ve\": 0.331, \"eval_return\": 184.03, \"nve\": 1.4, \"step\": 45000, \"value_mean\": 85.32, \"ve_ratio\": 0.464}, {\"baseline_ve\": 0.404, \"eval_return\": 153.79, \"nve\": 1.86, \"step\": 55000, \"value_mean\": 115.63, \"ve_ratio\": 0.752}, {\"baseline_ve\": 0.563, \"eval_return\": 324.3, \"nve\": 0.83, \"step\": 65000, \"value_mean\": 152.3, \"ve_ratio\": 0.469}, {\"baseline_ve\": 0.719, \"eval_return\": 326.67, \"nve\": 0.81, \"step\": 75000, \"value_mean\": 190.04, \"ve_ratio\": 0.582}, {\"baseline_ve\": 0.701, \"eval_return\": 256.21, \"nve\": 1.2, \"step\": 85000, \"value_mean\": 215.39, \"ve_ratio\": 0.841}, {\"baseline_ve\": 0.632, \"eval_return\": 31.73, \"nve\": 10.42, \"step\": 95000, \"value_mean\": 208.88, \"ve_ratio\": 6.583}], \"final_eval_return\": 31.73, \"final_eval_step\": 95000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"peak_eval_return\": 326.67, \"peak_eval_step\": 75000, \"reward_dt_emb_detach\": true, \"sgs_verdict\": \"SGS delays CIVO onset ~50K steps by preserving entropy, yields 2x higher peak (327 vs 167), but does NOT prevent collapse. Collapse is more severe (NVE 10.42x vs 4.12x) due to accumulated value overestimation. Root cause is value dynamics, not reward-head gradient contamination.\", \"target_steps\": 105000}, \"notes\": \"logdir 路径修正：实际数据在 logdir/exp_016e_sgs_walker_s1（非 spec 中的 exp_016d）。SGS 崩溃确认@95K: eval 31.7, ve_ratio=6.59x, NVE=10.42x。\\n\\n**⚠️ 关键发现（Full-SGS 梯度验证）：reward loss 对 dt_emb.weight 的梯度贡献为 0。016e 的 reward_dt_emb_detach 实际上是 no-op——完全无效干预。** 真正的 dt_emb 梯度来源是 decoder heads（orientations=1.11, velocity=0.90, height=0.76, cont=0.27）。016e 与 008d 的差异（onset 延迟、更高峰值）应归因于随机变异或其他实验条件差异，不是 SGS 干预效果。\\n\\nFull-SGS（detach 所有 non-KL head 梯度）移除 93% dt_emb 梯度（1.624→0.119），是真正的测试。\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016e_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"logdir\": \"logdir/exp_016e_sgs_walker_s1\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"logdir 修正: 实际数据在 exp_016e（非 016d）\", \"pid\": 527392, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T23:30:11.433Z\"}, \"exp_016c_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:26:05.863Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:12:09.799Z\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer). EGL fix confirmed working: eval at step 5000 completed successfully (eval_return=31.0). OOM occurred during training loop startup after eval. Likely system RAM OOM (replay buffer + model + eval concurrent memory peak).\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心。GPU 1 清理+验证通过后重启（plan_016）\", \"metrics\": {\"egl_fix_verified\": true, \"eval_return_5K\": 31, \"step\": 5000}, \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"GPU 1 cleanup + CUDA/dm_control verification passed. logdir shared with 016b (fresh start).\", \"pid\": \"524244\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:27:24.104Z\"}, \"exp_009h_008f_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:08:12.013Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:03:10.534Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:08:15.731787+00:00\"}]}, \"failure_reason\": \"误杀: Director 基于 Reviewer 错误诊断下令 kill（认为 zombie PID 522009 导致 eval deadlock），但日志证明 EGL fix (MUJOCO_EGL_DEVICE_ID=1) 已生效，eval 正常运行中 (iter=500, t=95.9s)。EGL fix 确认有效。\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009g（EGL device mismatch 修复：+MUJOCO_EGL_DEVICE_ID=1）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009h_008f_walker_s0.log\", \"notes\": \"日志显示进程正常完成 prefill → 到达 step 5000 → eval 正在运行（500 iter, 96s, 正常产出 debug 行）→ 被外部 SIGHUP (EXIT_CODE=129) 终止。非渲染死锁，非 OOM。诊断 Worker 排查外部终止原因中。009f/009g/009h 连续 3 次失败，分别因 seed 重复、EGL mismatch、外部 SIGHUP。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"522450\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T19:08:09.836Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"note\": \"EGL fix: MUJOCO_EGL_DEVICE_ID=1 to match physical GPU 1. 008f series seeds: 1(008f), 2(009c), 0(009h)\", \"pid\": \"522450\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:18:24.685Z\"}, \"exp_016b_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:10:52.235Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:08:00.667Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:10:53.928926+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016, 论文 method section 核心）。重跑 016_sgs，修复 EGL device mismatch（+MUJOCO_EGL_DEVICE_ID=1）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016b_sgs_walker_s1.log\", \"notes\": \"Restarted after GPU 1 cleanup. Old PID 523536 killed during GPU reset attempt. New PID 524244. GPU 1 diagnostics: no ECC/Xid errors, reset not supported (AutoDL container) but cleanup successful. CUDA + dm_control verification passed in 3s.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": 524244, \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"finished_at\": \"2026-05-15T19:10:51.013Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"Rerun of 016_sgs with EGL fix (MUJOCO_EGL_DEVICE_ID=1). Original 016 failed due to EGL device mismatch, not SGS code issue.\", \"pid\": \"523536\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:11:46.897Z\"}, \"exp_009g_008f_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:59:55.315Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T18:54:23.385Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:59:59.820061+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM). Root cause: MUJOCO_GL=egl defaults to EGL device 0 while CUDA_VISIBLE_DEVICES=1 binds CUDA to GPU 1, causing cross-GPU context conflict and eval deadlock at step 5000.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009f（seed=1 与 parent 008f 重复）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009g_008f_walker_s0.log\", \"notes\": \"Hung at first eval (step 5000) due to osmesa rendering deadlock in dm_control render_executor thread. Same root cause as exp_016. Fixed by switching MUJOCO_GL to egl in dreamer.py.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"517413\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T18:59:53.840Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"note\": \"Replaces exp_009f which had seed=1 duplicating parent 008f. 008f series seeds: 1(008f), 2(009c), 0(009g)\", \"pid\": \"517413\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:03:53.591Z\"}, \"exp_016_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:43:52.455Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T14:30:32.999Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:43:57.605618+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路。预期：不崩溃，nve < 1.5x baseline；imagination dt=2/dt=1 reward ratio 从 008d 的 2.90x 大幅下降（plan_016, 论文 method section 核心）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"notes\": \"Director 调整优先级：017 先于 016。cuda:1 释放后先跑 017，017 完成后再跑 016。SGS 诊断 bug 已修复（models.py L388-417 删除），dry-run 通过。[2026-05-15 18:43] PID 514422 hung: GPU 1 利用率 0%, 显存 794 MiB, metrics.jsonl 停 step=5000 持续 2.5h+。已 kill，Worker 诊断根因+修复+重启中。\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": \"514417\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"finished_at\": \"2026-05-15T18:43:51.025Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"pid\": \"514417\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:36:15.693Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 456.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:43:52.455Z\"}, \"exp_015b_frozen_dt_emb\": {\"completed_at\": \"2026-05-15T12:12:25.846Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T10:21:05.572Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T18:27:09.189680+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"第二次提交。首次失败原因: --device cuda:1 但 CUDA_VISIBLE_DEVICES=1 后进程内只有 cuda:0。已修正为 --device cuda:0。PID 144831, 从头开始 (step=0)。预计 ~5h 完成 105K steps。\"}}, \"hypothesis\": \"Walker Walk frozen dt_emb + subsample ON + dt=2 imagination + H=8 seed 1 — 2×2 消融矩阵: 隔离 dt_emb 训练 vs 存在的因果效应。如果 freeze 后不崩 → 确认 CIVO 根因是 dt_emb 训练而非结构存在（plan_015B, D041）\", \"metrics\": {\"actor_entropy_105K\": -4.855, \"actor_loss_105K\": 0.000179, \"collapse_mechanism\": \"gradient_starvation_from_frozen_dt_emb\", \"data_source\": \"worker SSH final analysis 2026-05-15T18:30\", \"eval_return_105K\": 204.2, \"eval_return_15K\": 167.9, \"eval_return_25K\": 171.8, \"eval_return_35K\": 201.6, \"eval_return_45K\": 122.3, \"eval_return_55K\": 105.8, \"eval_return_5K\": 31, \"eval_return_65K\": 160.3, \"eval_return_75K\": 80, \"eval_return_85K\": 183.5, \"eval_return_95K\": 238.4, \"final_eval\": 204.2, \"final_step\": 112000, \"gate_dt_1_frac\": 0, \"gate_dt_mean\": 2, \"nve_105K\": 0.42, \"nve_85K\": 0.467, \"nve_95K\": 0.394, \"summary\": \"NVE 0.39-0.47 (far below 1.0, critic under-estimates), actor_loss→0 (gradient starvation), gate locked dt=2 100%, eval volatile 80-238 no stable convergence\", \"value_mean_105K\": 56.212, \"value_std_105K\": 13.818}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD + MUJOCO_GL=egl + --device cuda:0 (CUDA_VISIBLE_DEVICES=1 隔离)。cuda:1, seed=1, 105K steps ~5h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:27:07.138Z\"}, \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_015b_frozen_dt_emb --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_015b_frozen_dt_emb.log\", \"pid\": \"149991\", \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:38:42.380Z\"}, \"exp_008a_no_subsample_dt2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample/latest.pt\", \"completed_at\": \"2026-05-14T06:16:58.196Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:33:27.311Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T06:15:01.796655+00:00\"}]}, \"hypothesis\": \"隔离 subsample 效应：trained dt_emb (unexposed to dt>1 data due to subsample OFF) + subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。\", \"metrics\": {\"baseline_105K\": 915.67, \"baseline_55K\": 625.7, \"baseline_65K\": 616, \"data_source\": \"from training logs metrics.jsonl\", \"eval_return_105K\": 777.66, \"eval_return_35K\": 500.84, \"eval_return_45K\": 563.41, \"eval_return_55K\": 487.92, \"eval_return_65K\": 608, \"eval_return_75K\": 469.93, \"eval_return_85K\": 583.73, \"eval_return_95K\": 572.24, \"nan_count\": 0, \"normalized_ve_105K\": 0.59, \"normalized_ve_55K\": 0.93, \"normalized_ve_65K\": 0.66, \"normalized_ve_75K\": 0.75, \"normalized_ve_85K\": 0.68, \"normalized_ve_95K\": 0.79, \"step\": 112000, \"trend\": \"Two V-shaped recoveries: 501→563→488→608→470→584→572→778; v/e suppressed 38-54% (normalized 0.59-0.79x baseline); no collapse at 105K\", \"value_eval_ratio_105K\": 0.386, \"value_eval_ratio_55K\": 0.376, \"value_eval_ratio_65K\": 0.372, \"value_eval_ratio_75K\": 0.536, \"value_eval_ratio_85K\": 0.475, \"value_eval_ratio_95K\": 0.497, \"value_mean_105K\": 300.27, \"value_mean_55K\": 183.5, \"value_mean_65K\": 226.1, \"value_mean_75K\": 251.78, \"value_mean_85K\": 277.36, \"value_mean_95K\": 284.28, \"verdict_105K\": \"NEW_PEAK_V_RECOVERY\", \"verdict_65K\": \"RECOVERED_NEW_HIGH\", \"vs_baseline_105K\": \"-15.1%\", \"vs_baseline_65K\": \"-1.3%\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T06:15:00.119Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_fixed_dt2_no_subsample --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.65, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (gate_fixed_dt=2, gate_subsample_max_dt=1, H=15)\", \"pid\": \"106942\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:46.034Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16752.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:50:59.046Z\"}, \"exp_009d_baseline_walker_s1\": {\"completed_at\": \"2026-05-15T11:54:55.153Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:14.363Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 1 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"notes\": \"⚠️ seed=1 与 exp_001_baseline 相同，eval 轨迹确定性复现。不构成独立 seed。如需第三 baseline seed 应 kill 并用 --seed 0 或 --seed 3 重跑。待 Director 决策。\", \"parent\": \"exp_001_baseline\", \"pid\": 122271, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009d_baseline_walker_s1.log\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:35:00Z\", \"wall_clock_seconds\": 19195.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:54:55.153Z\"}, \"exp_009a_baseline_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/latest.pt\", \"completed_at\": \"2026-05-15T06:33:12.892Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:24.247Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 2 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/\", \"metrics\": {\"cross_seed_ve_stable\": \"seed 2 v/e = 0.69-0.72 matches seed 0/1 = 0.69-0.72\", \"eval_return_peak\": 966.94, \"eval_return_peak_step\": 395000, \"eval_trajectory\": [{\"eval_return\": 41.21, \"step\": 5000}, {\"eval_return\": 106.01, \"step\": 15000}, {\"eval_return\": 325.33, \"step\": 25000}, {\"eval_return\": 354.49, \"step\": 35000}, {\"eval_return\": 498.01, \"step\": 45000}, {\"eval_return\": 534.13, \"step\": 55000}, {\"eval_return\": 688.87, \"step\": 65000}, {\"eval_return\": 656.85, \"step\": 75000}, {\"eval_return\": 618.73, \"step\": 85000}, {\"eval_return\": 596.24, \"step\": 95000}, {\"eval_return\": 836.51, \"step\": 105000}, {\"eval_return\": 804.79, \"step\": 115000}, {\"eval_return\": 865.48, \"step\": 125000}, {\"eval_return\": 876.08, \"step\": 135000}, {\"eval_return\": 869.18, \"step\": 145000}, {\"eval_return\": 778.99, \"step\": 155000}, {\"eval_return\": 864.03, \"step\": 165000}, {\"eval_return\": 850.53, \"step\": 175000}, {\"eval_return\": 907.31, \"step\": 185000}, {\"eval_return\": 873.49, \"step\": 195000}, {\"eval_return\": 887.02, \"step\": 205000}, {\"eval_return\": 956.04, \"step\": 215000}, {\"eval_return\": 892.09, \"step\": 225000}, {\"eval_return\": 914.78, \"step\": 235000}, {\"eval_return\": 950.32, \"step\": 245000}, {\"eval_return\": 936.9, \"step\": 255000}, {\"eval_return\": 937.27, \"step\": 265000}, {\"eval_return\": 934.78, \"step\": 275000}, {\"eval_return\": 960.2, \"step\": 285000}, {\"eval_return\": 947.46, \"step\": 295000}, {\"eval_return\": 937.8, \"step\": 305000}, {\"eval_return\": 948.66, \"step\": 315000}, {\"eval_return\": 930.61, \"step\": 325000}, {\"eval_return\": 919.23, \"step\": 335000}, {\"eval_return\": 816.18, \"step\": 345000}, {\"eval_return\": 932.45, \"step\": 355000}, {\"eval_return\": 943.13, \"step\": 365000}, {\"eval_return\": 952.86, \"step\": 375000}, {\"eval_return\": 942.31, \"step\": 385000}, {\"eval_return\": 966.94, \"step\": 395000}, {\"eval_return\": 948.01, \"step\": 405000}, {\"eval_return\": 957.06, \"step\": 415000}, {\"eval_return\": 939.37, \"step\": 425000}, {\"eval_return\": 963.65, \"step\": 435000}, {\"eval_return\": 948.42, \"step\": 445000}, {\"eval_return\": 937.72, \"step\": 455000}, {\"eval_return\": 939.54, \"step\": 465000}, {\"eval_return\": 965.94, \"step\": 475000}, {\"eval_return\": 916.74, \"step\": 485000}, {\"eval_return\": 945.58, \"step\": 495000}, {\"eval_return\": 957.87, \"step\": 505000}], \"final_eval_return\": 957.87, \"final_eval_step\": 505000, \"final_value_mean\": 665.17, \"final_ve_ratio\": 0.694, \"last10_mean\": 947.19, \"n_evals\": 51, \"total_steps\": 505000, \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 25000, \"value_mean\": 45.78}, {\"step\": 55000, \"value_mean\": 253.49}, {\"step\": 105000, \"value_mean\": 539.34}, {\"step\": 155000, \"value_mean\": 633.42}, {\"step\": 205000, \"value_mean\": 658.92}, {\"step\": 255000, \"value_mean\": 663.87}, {\"step\": 305000, \"value_mean\": 663.86}, {\"step\": 355000, \"value_mean\": 663.78}, {\"step\": 405000, \"value_mean\": 663.95}, {\"step\": 455000, \"value_mean\": 664.42}, {\"step\": 505000, \"value_mean\": 665.17}], \"ve_ratio_trajectory\": [{\"step\": 25000, \"ve\": 0.141}, {\"step\": 55000, \"ve\": 0.475}, {\"step\": 105000, \"ve\": 0.645}, {\"step\": 155000, \"ve\": 0.813}, {\"step\": 205000, \"ve\": 0.743}, {\"step\": 255000, \"ve\": 0.709}, {\"step\": 305000, \"ve\": 0.708}, {\"step\": 355000, \"ve\": 0.712}, {\"step\": 405000, \"ve\": 0.7}, {\"step\": 455000, \"ve\": 0.709}, {\"step\": 505000, \"ve\": 0.694}], \"ve_stable_range\": \"0.69-0.72 from 235K+\", \"vs_exp001_105K\": \"836.51 vs 915.67 (-8.6%)\", \"vs_exp001_final\": \"957.87 vs 970.41 (-1.3%)\", \"vs_exp001_last10\": \"947.19 vs 950.90 (-0.4%)\", \"vs_exp001_peak\": \"966.94 vs 970.41 (-0.4%)\"}, \"notes\": \"Baseline seed 2 完成。与 exp_001 (seed 0/1) 高度一致: peak 966.94 vs 970.41 (-0.4%), last10 mean 947.19 vs 950.90 (-0.4%), v/e stable 0.69-0.72 匹配。105K 处 836.51 比 seed 0/1 的 915.67 低 8.6%，但 215K+ 后完全收敛。345K 有一个 dip 到 816 但迅速恢复。baseline 跨 seed 一致性确认。\", \"pid\": \"142508\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009a_baseline_walker_s2 --steps 500000 --seed 2 --compile False --device cuda:0\\\"\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-14T07:19:08.969Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:33:16.385Z\"}, \"exp_008e_v3_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s2/latest.pt\", \"completed_at\": \"2026-05-15T06:00:20.816Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T14:29:53.738Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 2 — crown jewel C6 seed 2 验证\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s2/\", \"metrics\": {\"actor_entropy_collapse_signature\": \"entropy rose from -5.21@85K to -3.83@105K (policy destabilizing during collapse)\", \"actor_entropy_trajectory\": [{\"actor_entropy\": 8.239, \"step\": 5000}, {\"actor_entropy\": 2.352, \"step\": 15000}, {\"actor_entropy\": 0.17, \"step\": 25000}, {\"actor_entropy\": -3.498, \"step\": 35000}, {\"actor_entropy\": -4.915, \"step\": 45000}, {\"actor_entropy\": -5.121, \"step\": 55000}, {\"actor_entropy\": -5.135, \"step\": 65000}, {\"actor_entropy\": -5.224, \"step\": 75000}, {\"actor_entropy\": -5.208, \"step\": 85000}, {\"actor_entropy\": -4.529, \"step\": 95000}, {\"actor_entropy\": -3.828, \"step\": 105000}], \"baseline_105K\": 915.67, \"collapse_confirmed\": \"105K (nve=3.78x, eval 715→137)\", \"collapse_onset\": \"95K (nve jumped from 0.68x to 1.34x)\", \"eval_trajectory\": [{\"eval_return\": 39.27, \"step\": 5000}, {\"eval_return\": 180.85, \"step\": 15000}, {\"eval_return\": 211.82, \"step\": 25000}, {\"eval_return\": 320.39, \"step\": 35000}, {\"eval_return\": 356.93, \"step\": 45000}, {\"eval_return\": 418.32, \"step\": 55000}, {\"eval_return\": 435.09, \"step\": 65000}, {\"eval_return\": 576.54, \"step\": 75000}, {\"eval_return\": 715.21, \"step\": 85000}, {\"eval_return\": 452.43, \"step\": 95000}, {\"eval_return\": 136.96, \"step\": 105000}], \"final_eval_return\": 136.96, \"final_nve\": 3.78, \"final_value_mean\": 339.84, \"final_ve_ratio\": 2.481, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"peak_eval_return\": 715.21, \"peak_eval_step\": 85000, \"train_return_108K\": \"19-23 (random policy level)\", \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 15000, \"value_mean\": 3.91}, {\"step\": 25000, \"value_mean\": 30.27}, {\"step\": 35000, \"value_mean\": 79.75}, {\"step\": 45000, \"value_mean\": 125.25}, {\"step\": 55000, \"value_mean\": 172.89}, {\"step\": 65000, \"value_mean\": 220.47}, {\"step\": 75000, \"value_mean\": 272.64}, {\"step\": 85000, \"value_mean\": 339.3}, {\"step\": 95000, \"value_mean\": 384.39}, {\"step\": 105000, \"value_mean\": 339.84}], \"ve_ratio_trajectory\": [{\"nve\": 1.64, \"step\": 25000, \"ve\": 0.143}, {\"nve\": 1.03, \"step\": 35000, \"ve\": 0.249}, {\"nve\": 1.06, \"step\": 45000, \"ve\": 0.351}, {\"nve\": 1.02, \"step\": 55000, \"ve\": 0.413}, {\"nve\": 0.9, \"step\": 65000, \"ve\": 0.507}, {\"nve\": 0.66, \"step\": 75000, \"ve\": 0.473}, {\"nve\": 0.68, \"step\": 85000, \"ve\": 0.474}, {\"nve\": 1.34, \"step\": 95000, \"ve\": 0.85}, {\"nve\": 3.78, \"step\": 105000, \"ve\": 2.481}], \"vs_baseline_105K\": \"-85.0%\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"notes\": \"C6 seed 2 COLLAPSED. Delusional critic collapse at 85K→105K despite gate_dt_mean=1.0 locked throughout. eval peaked 715@85K then crashed to 137@105K (v/e=2.48, nve=3.78x). Cross-seed: seed 0=869.9 (healthy), seed 1=869.9 (healthy), seed 2=137 (collapsed). Collapse is stochastic (1/3 seeds) even in dt=1 imagination config. Subsample ON training data (dt=2 transitions) appears sufficient to trigger delusional critic in some seeds. Train returns at 108K=19-23 (random policy).\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"pid\": \"43437\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.23, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s2.log\", \"pid\": \"43437\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T00:46:45.424Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18815.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:24:21.709Z\"}, \"exp_008e_v3_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T00:44:53.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T14:29:53.120Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 1 — crown jewel C6 验证：trained dt_emb 在 dt=1 imagination 下不触发 delusional critic（plan_014）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/\", \"metrics\": {\"eval_trajectory\": [{\"eval_return\": 31, \"step\": 5000}, {\"eval_return\": 131.2, \"step\": 15000}, {\"eval_return\": 155.7, \"step\": 25000}, {\"eval_return\": 276.5, \"step\": 35000}, {\"eval_return\": 382.2, \"step\": 45000}, {\"eval_return\": 486.8, \"step\": 55000}, {\"eval_return\": 580.7, \"step\": 65000}, {\"eval_return\": 574.1, \"step\": 75000}, {\"eval_return\": 657.3, \"step\": 85000}, {\"eval_return\": 851.9, \"step\": 95000}, {\"eval_return\": 869.9, \"step\": 105000}], \"exit_code\": 0, \"final_eval_return\": 869.9, \"final_value_mean\": 457.9, \"gate_dt_1_frac\": 1, \"total_steps\": 112000, \"ve_ratio_105k\": 0.527}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"notes\": \"Crown jewel C6 seed 1 SUCCESS. eval_return=869.9@105K, v/e=0.527 (healthy, no delusional critic). Gate locked dt=1 throughout. Trajectory: 31→131→156→276→382→487→581→574→657→852→870. Consistent with seed 0, confirms trained dt_emb + dt=1 imagination is safe.\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"pid\": \"898127\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.92, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s1.log\", \"pid\": \"898127\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T18:49:27.945Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 21325.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:44:53.439Z\"}, \"exp_006\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T00:49:02.944Z\", \"metrics\": {\"baseline_return_at_55k\": 625.7, \"deficit_pct\": -42.4, \"deficit_vs_baseline_at_55k\": -265.3, \"eval_return\": {\"15000\": 256.9, \"25000\": 321.4, \"35000\": 485.3, \"45000\": 477, \"5000\": 31, \"55000\": 360.4}, \"gate_dt_mean\": 2, \"latest_return\": 360.4, \"latest_step\": 55000, \"model_loss_at_55k\": 4.853, \"peak_return\": 485.3, \"peak_step\": 35000}, \"notes\": \"早期条目，权威数据在 exp_006_fixed_dt2。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.922Z\"}, \"exp_008a\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:07:59.793Z\", \"metrics\": {\"eval_return_15K\": 167.2, \"eval_return_25K\": 230.8, \"eval_return_35K\": 500.8, \"eval_return_45K\": 563.4, \"eval_return_55K\": 487.9, \"eval_return_5K\": 31, \"eval_return_65K\": \"pending (eval in progress)\", \"step\": 65000, \"train_return_64K_avg\": 556.6, \"trend\": \"peaked @45K=563, dipped to @55K=488, 65K eval in progress; train returns @64K healthy (~557)\", \"value_eval_ratio_55K\": \"37.6%\", \"value_mean_55K\": 183.5}, \"notes\": \"早期条目，权威数据在 exp_008a_no_subsample_dt2。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.075Z\"}, \"exp_008c\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:02.608Z\", \"metrics\": {\"eval_return_15K\": 171.3, \"eval_return_25K\": 192.4, \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.6, \"eval_return_55K\": 241.9, \"eval_return_5K\": 31, \"eval_return_65K\": 240.9, \"step\": 68000, \"train_return_68K_avg\": 245.1, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_65K\": \"32.8%\", \"value_mean_65K\": 79}, \"notes\": \"早期条目，权威数据在正式命名实验中。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:52.611Z\"}, \"exp_008d\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:05.136Z\", \"metrics\": {\"eval_return_15K\": 153.7, \"eval_return_25K\": 167.2, \"eval_return_35K\": 146.3, \"eval_return_5K\": 31, \"step\": 40000, \"train_return_40K_avg\": 119.3, \"trend\": \"declining — train_return @40K avg=119 below @35K eval=146, value/eval=41.1% not yet >50% but train performance dropping\", \"value_eval_ratio_35K\": \"41.1%\", \"value_mean_35K\": 60.2}, \"notes\": \"早期条目，权威数据在 exp_008d_subsample_on_h8。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:51.696Z\"}, \"exp_008e_v2_subsample_on_dt1_h15\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:26:39.732Z\", \"notes\": \"已被 exp_008e_v3_subsample_on_dt1_h15 取代，进程已死。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v2_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v2_subsample_on_dt1_h15.log\", \"pid\": \"125392\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:27:30.720Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:49.814Z\"}, \"exp_rssm_fidelity_analysis\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T11:09:52.237Z\", \"hypothesis\": \"RSSM prediction quality analysis: 比较 baseline/008d/008f 在 dt=1 vs dt=2 transitions 上的 obs_MSE 和 reward_MAE，量化 RSSM fidelity gap (plan_030)\", \"metrics\": {\"008d_trained_dtEmb\": {\"dt1_obs_mse\": 41.31, \"dt1_reward_mae\": 0.0568, \"dt2_obs_mse\": 53.67, \"dt2_reward_mae\": 0.1579, \"obs_gap\": 1.3, \"reward_gap\": 2.78}, \"008f_no_dtEmb\": {\"dt1_obs_mse\": 8.01, \"dt1_reward_mae\": 0.7469, \"dt2_obs_mse\": 22.04, \"dt2_reward_mae\": 0.7526, \"obs_gap\": 2.75, \"reward_gap\": 1.01}, \"baseline\": {\"dt1_obs_mse\": 13.49, \"dt1_reward_mae\": 0.0102, \"dt2_obs_mse\": 27.5, \"dt2_reward_mae\": 0.0159, \"obs_gap\": 2.04, \"reward_gap\": 1.56}}, \"notes\": \"分析实验，非训练实验。conclusion=success，状态从 PREPARING 修正为 DONE（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:48.642Z\"}, \"exp_008e_v3_subsample_on_dt1_h15\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15/latest.pt\", \"completed_at\": \"2026-05-14T09:07:47.319Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:29:31.656Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T09:05:44.288431+00:00\"}]}, \"hypothesis\": \"B+ confound control：subsample ON + untrained dt_emb + dt=1 imagination + H=15。验证 subsample ON 训练数据（含 dt=2 transitions）是否本身导致性能下降，即使 imagination 只用 dt=1。对照 008a（subsample OFF）和 baseline。如果 008e_v3 性能接近 baseline → subsample ON 本身无害。如果下降 → subsample ON 改变了 RSSM dynamics。\", \"metrics\": {\"baseline_105K\": 915.67, \"current_step\": 112000, \"eval_return\": {\"105K\": 869.88, \"15K\": 131.2, \"25K\": 155.69, \"35K\": 276.47, \"45K\": 382.22, \"55K\": 486.84, \"5K\": 31, \"65K\": 580.67, \"75K\": 574.09, \"85K\": 657.31, \"95K\": 851.86}, \"fps\": 7.01, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"last_updated\": \"2026-05-14T09:09:00\", \"normalized_ve\": {\"105K\": 0.8, \"25K\": 1.93, \"35K\": 0.94, \"45K\": 0.88, \"55K\": 0.87, \"65K\": 0.72, \"75K\": 0.73, \"85K\": 0.76, \"95K\": 0.75}, \"target_steps\": 105000, \"value_eval_ratio\": {\"105K\": 0.527, \"25K\": 0.168, \"35K\": 0.227, \"45K\": 0.29, \"55K\": 0.35, \"65K\": 0.405, \"75K\": 0.523, \"85K\": 0.534, \"95K\": 0.476}, \"value_mean\": {\"105K\": 457.93, \"25K\": 26.19, \"35K\": 62.76, \"45K\": 110.67, \"55K\": 170.09, \"65K\": 235.05, \"75K\": 300.51, \"85K\": 351.33, \"95K\": 405.25}, \"verdict\": \"SUCCESS - 95% baseline, normalized v/e stable 0.72-0.80x, B+ hypothesis confirmed\", \"vs_baseline_105K\": \"-5.0%\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"reproduce\": {\"finished_at\": \"2026-05-14T09:05:42.563Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 4.64, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, untrained dt_emb)\", \"pid\": \"126110\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:29:31.600Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16695.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T19:46:00.840Z\"}, \"exp_009c_008f_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T22:15:00Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:26.154Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T14:15:58.982844+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_008f_walker_s2.log\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"Seed 2 does NOT replicate seed 1's zigzag recovery. 008f seed 1 peaked at 503@105K with rising trend; seed 2 peaked at 359@75K then declined to 148@105K. The adaptive horizon mechanism's benefit appears seed-dependent and not robust.\", \"current_step\": 105000, \"eval_checkpoints\": [{\"baseline_ve\": null, \"eval_return\": 30.37, \"normalized_ve\": null, \"step\": 5000, \"value_mean\": 0.0013, \"ve_ratio\": null}, {\"baseline_ve\": null, \"eval_return\": 157.15, \"normalized_ve\": null, \"step\": 15000, \"value_mean\": 3.057, \"ve_ratio\": 0.019}, {\"baseline_ve\": 0.087, \"eval_return\": 168.75, \"normalized_ve\": 1.26, \"step\": 25000, \"value_mean\": 18.536, \"ve_ratio\": 0.11}, {\"baseline_ve\": 0.241, \"eval_return\": 178.94, \"normalized_ve\": 0.79, \"step\": 35000, \"value_mean\": 34.263, \"ve_ratio\": 0.191}, {\"baseline_ve\": 0.331, \"eval_return\": 211.08, \"normalized_ve\": 0.72, \"step\": 45000, \"value_mean\": 50.099, \"ve_ratio\": 0.237}, {\"baseline_ve\": 0.404, \"eval_return\": 238.91, \"normalized_ve\": 0.66, \"step\": 55000, \"value_mean\": 63.267, \"ve_ratio\": 0.265}, {\"baseline_ve\": 0.563, \"eval_return\": 244.15, \"normalized_ve\": 0.53, \"step\": 65000, \"value_mean\": 72.717, \"ve_ratio\": 0.298}, {\"baseline_ve\": 0.719, \"eval_return\": 359.14, \"normalized_ve\": 0.33, \"step\": 75000, \"value_mean\": 83.91, \"ve_ratio\": 0.234}, {\"baseline_ve\": 0.701, \"eval_return\": 227.43, \"normalized_ve\": 0.6, \"step\": 85000, \"value_mean\": 96.071, \"ve_ratio\": 0.422}, {\"baseline_ve\": 0.632, \"eval_return\": 190.94, \"normalized_ve\": 0.9, \"step\": 95000, \"value_mean\": 108.29, \"ve_ratio\": 0.567}, {\"baseline_ve\": 0.656, \"eval_return\": 148.34, \"normalized_ve\": 1.14, \"step\": 105000, \"value_mean\": 111.247, \"ve_ratio\": 0.75}], \"target_steps\": 105000, \"trend\": \"Peak 359@75K then monotonic decline to 148@105K; no recovery pattern unlike 008f seed 1's zigzag recovery to 503\", \"verdict\": \"NEGATIVE - no delusional critic (normalized v/e < 1.5x) but persistent decline after 75K; cross-seed consistency with 008f seed 1 NOT confirmed\", \"vs_baseline_105K\": \"-83.8%\"}, \"notes\": \"D031 排期修正: 009c 延长 200K 降优先级，排在 009e/009f 之后。cuda:1 排期: 009b → 008e_v3_s1 → 008e_v3_s2 → 009e → 009f → 009c(200K) → plan_060。105K 指标: eval=148.34, value=111.25, nve=1.14x。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"140980\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_008f_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-14T14:15:57.425Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-14T07:19:10.835Z\", \"training_hours\": 6.95}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"seed\": 2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T14:34:24.161Z\"}, \"exp_006_fixed_dt2\": {\"account\": \"root\", \"completed_at\": \"2026-05-14T01:13:11.533Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T21:10:58.851Z\", \"extra\": {\"audit_commit\": \"6159e46\", \"bugs_fixed\": \"_effective_max_dt not synced in fixed_dt mode; hardcoded curriculum phases ignoring config\", \"curriculum_audit\": \"Curriculum does NOT apply in fixed_dt mode (models.py:200-205). gate_fixed_dt>0 bypasses _update_gate_schedule(). subsample_variable_dt receives effective_max_dt=2.0 from step 0, training data is 58.5% dt=1 + 41.5% dt=2 throughout. Actual train/imagine mismatch: mixed dt training vs pure dt=2 imagination.\"}, \"gpu\": \"cuda:0\", \"hypothesis\": \"诊断实验：fixed dt=2 vs learned gate。去掉 Gumbel-Softmax gate，硬编码 dt=2，其余超参与 exp_005 完全一致。量化 learned gate 的价值——如果 fixed dt=2 也掉 return，说明跳步本身有害；如果不掉，问题在 gate 学习机制。\", \"latest_metrics\": {\"checked_at\": \"2026-05-14\", \"eval_return\": 485.3, \"eval_return_trajectory\": {\"15K\": 256.9, \"25K\": 321.4, \"35K\": 485.3, \"5K\": 31}, \"eval_step\": 35000, \"fps\": 6.6, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"grad_norm\": 8.6, \"pid\": 85029, \"prev_eval_return\": 321.4, \"process_status\": \"running\", \"step\": 36000}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_006_fixed_dt2.log\", \"metrics\": {\"baseline_35K\": 388.5, \"baseline_45K\": 513.8, \"baseline_55K\": 625.7, \"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_15K\": 256.9, \"eval_return_25K\": 321.4, \"eval_return_35K\": 485.3, \"eval_return_45K\": 477, \"eval_return_55K\": 360.4, \"eval_return_5K\": 31, \"eval_return_65K\": 132.86, \"fps\": 6.5, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"model_loss_15K\": 7.593, \"model_loss_25K\": 5.633, \"model_loss_35K\": 5.229, \"model_loss_45K\": 5.023, \"model_loss_55K\": 4.9, \"model_loss_5K\": 20.738, \"peak_return\": 485.3, \"peak_step\": \"35K\", \"step\": 65000, \"trend\": \"inverted-V: peak 485@35K, collapsing to 133@65K; v/e accelerating: 31.1%→53.3%→93.3%→272% (value 2.7x eval_return at 65K)\", \"value_eval_ratio_35K\": 0.311, \"value_eval_ratio_45K\": 0.533, \"value_eval_ratio_55K\": 0.933, \"value_eval_ratio_65K\": 2.722, \"value_mean_35K\": 151.1, \"value_mean_45K\": 254.29, \"value_mean_55K\": 336.44, \"value_mean_65K\": 361.69, \"vs_baseline_55K\": \"-42.4%\"}, \"parent\": \"exp_005_event_gated_v4\", \"pid\": \"85029\", \"reproduce\": {\"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\\\"\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-13T22:12:00.446Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"N/A - negative result, fixed dt=2 collapsed to 132.9@65K (21.6% baseline)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"failure_reason\": \"fixed dt=2 崩塌：训练分布混合（58.5% dt=1 + 41.5% dt=2 log-uniform）+ 想象纯 dt=2 条件下，eval_return 从 peak 485@35K 持续下降至 132.9@65K（baseline 同期 615.9）。与 learned gate 变体一致的崩塌模式。代码审计确认 curriculum 不生效（gate_fixed_dt>0 跳过 _update_gate_schedule）。\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt2_v1_s1\", \"model_name\": \"DreamerV3+FixedDt2 (gate_fixed_dt=2, no learned gate)\", \"pid\": \"85029\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T10:20:11.722Z\"}, \"exp_008e_subsample_on_fixed_dt1\": {\"checkpoint_path\": \"N/A - killed, duplicate registry entry, logdir contaminated by dual-process write\", \"completed_at\": \"2026-05-14T04:21:47.956Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:07.303Z\", \"failure_reason\": \"重复 registry 条目 + logdir 被两个进程交叉写入导致 tfevents/metrics.jsonl 损坏。Director 指令清理后以 exp_008e_subsample_on_dt1_h15 为准重跑。\", \"hypothesis\": \"验证 Reviewer D020 因果假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（delusional critic），即使 actor 不用 dt=2 imagination。对照：008a (subsample OFF, dt=2 imag) value/eval=37.6%@55K vs exp_006 (subsample ON, dt=2 imag) 53.3%。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.19, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"121636\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:22.915Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 685.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:58.056Z\"}, \"exp_008e_subsample_on_dt1_h15\": {\"checkpoint_path\": \"N/A - killed, logdir contaminated by duplicate process cross-write\", \"completed_at\": \"2026-05-14T04:21:48.584Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:37.655Z\", \"hypothesis\": \"验证 Reviewer D020 delusional critic 假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（即使 actor 不用 dt=2 imagination）。对照：008a（subsample OFF，dt=2 imagination）和 006（subsample ON，dt=2 imagination）。\", \"notes\": \"重复进程：与 exp_008e_subsample_on_fixed_dt1 命令完全相同，共享同一 logdir，导致 tfevents 文件互相污染。Kill PID 122038，保留 PID 121636。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.18, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"122038\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:46.045Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 662.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:57.658Z\"}, \"exp_002_event_gated\": {\"completed_at\": \"2026-05-13T04:50:14.987Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T02:09:54.240Z\", \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"kill_reason\": \"Phase 1 subsample 设计缺陷：subsample_variable_dt 在 Phase 1 (gate_scale=0) 也生效，RSSM 用 variable-Δt 数据训练但 imagination 只用 Δt=1，return 恶化到 baseline 的 25%。手动 kill 后部署 subsample curriculum 补丁并重启为 exp_003。\", \"retry_count\": 0, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1 --steps 500000 --seed 1 --compile False --device cuda:1 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM (K=8, τ=5→0.5, λ_H=0.1→0.01)\", \"pid\": 9769, \"seed\": 1, \"server\": \"autodl-rtx6000\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T04:52:18.089Z\"}}, \"count\": 213, \"total\": 213, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9998}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014WtwBUqXP6niR83qFc5KLn`</summary>

```json
{
  "server": "westd-51268",
  "command": "grep -n \"dmc_\" /root/autodl-tmp/event-gated-adaptive-horizon/configs.yaml",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "42827cf8-899d-40f0-9cb7-2df265736ece",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N61FfHYMLVFk2GSd8jY8aC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 26002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1497
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-29T08:25:42.804Z_

<details><summary>↩ Tool result · `toolu_01LP9L7p8BACE3vzMzNXsBMP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"28:  task: 'dmc_walker_walk'\\n156:  task: crafter_reward\\n190:  task: minecraft_diamond\\n218:  task: 'memorymaze_9x9'\\n221:  task: maniskill_PickCube-v1\\n232:  task: maniskill_PickCube-v1\\n243:  task: maniskill_StackCube-v1\\n254:  task: maniskill_PegInsertionSide-v1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "ce1f5149-8275-4dcd-9c44-f8b2db5747f0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"28:  task: 'dmc_walker_walk'\\\\n156:  task: crafter_reward\\\\n190:  task: minecraft_diamond\\\\n218:  task: 'memorymaze_9x9'\\\\n221:  task: maniskill_PickCube-v1\\\\n232:  task: maniskill_PickCube-v1\\\\n243:  task: maniskill_StackCube-v1\\\\n254:  task: maniskill_PegInsertionSide-v1\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.48}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"28:  task: 'dmc_walker_walk'\\n156:  task: crafter_reward\\n190:  task: minecraft_diamond\\n218:  task: 'memorymaze_9x9'\\n221:  task: maniskill_PickCube-v1\\n232:  task: maniskill_PickCube-v1\\n243:  task: maniskill_StackCube-v1\\n254:  task: maniskill_PegInsertionSide-v1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VHnfdtRy2U7P2J1yUdHrWc`</summary>

```json
{
  "server": "westd-51268",
  "command": "head -50 /root/autodl-tmp/event-gated-adaptive-horizon/analyze_hopper_nve.py",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "418c5a63-1fee-42cd-b5e3-f76e55342635",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N61FfHYMLVFk2GSd8jY8aC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 26002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1497
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-29T08:25:43.358Z_

<details><summary>↩ Tool result · `toolu_014WtwBUqXP6niR83qFc5KLn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"28:  task: 'dmc_walker_walk'\\n137:dmc_proprio:\\n146:dmc_vision:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "9cafb3cf-8a66-42a0-a3a6-91f226e977ca",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"28:  task: 'dmc_walker_walk'\\\\n137:dmc_proprio:\\\\n146:dmc_vision:\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.54}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"28:  task: 'dmc_walker_walk'\\n137:dmc_proprio:\\n146:dmc_vision:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-29T08:25:43.888Z_

<details><summary>↩ Tool result · `toolu_01VHnfdtRy2U7P2J1yUdHrWc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Hopper NVE (Normalized Value-to-Eval) Analysis + CIVO Onset Detection\\n# Input: metrics.jsonl from DreamerV3 logdirs (baseline + experiment runs)\\n# Output: per-experiment NVE report, cross-env summary table, NVE trajectory plots\\n# Depends: numpy, matplotlib, json, argparse\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport numpy as np\\nfrom collections import OrderedDict\\nfrom datetime import datetime, timezone\\n\\nLOGDIR_DEFAULT = \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir\\\"\\nCROSS_ENV_SUMMARY = os.path.join(LOGDIR_DEFAULT, \\\"cross_env_output\\\", \\\"cross_env_civo_summary.json\\\")\\nMIN_STEP = 35000\\nNVE_TAU = 2.0\\nSUSTAINED_COUNT = 2\\n\\n\\ndef load_metrics(logdir):\\n    \\\"\\\"\\\"Load eval_return and value_mean from metrics.jsonl, merge by step.\\\"\\\"\\\"\\n    path = os.path.join(logdir, \\\"metrics.jsonl\\\")\\n    if not os.path.exists(path):\\n        print(f\\\"WARNING: {path} not found\\\")\\n        return {}\\n\\n    eval_returns = {}\\n    value_means = {}\\n\\n    with open(path) as f:\\n        for line in f:\\n            line = line.strip()\\n            if not line:\\n                continue\\n            d = json.loads(line)\\n            step = d.get(\\\"step\\\")\\n            if step is None:\\n                continue\\n            if \\\"eval_return\\\" in d:\\n                eval_returns[step] = d[\\\"eval_return\\\"]\\n            if \\\"value_mean\\\" in d:\\n                value_means[step] = d[\\\"value_mean\\\"]\\n\\n    common_steps = sorted(set(eval_returns) & set(value_means))\\n    data = OrderedDict()\\n    for s in common_steps:\\n        er = eval_returns[s]\\n        vm = value_means[s]\\n        ve_ratio = vm / max(er, 1e-6)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "2627114d-a43f-4a33-946c-58c8a2ca18de",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"# Hopper NVE (Normalized Value-to-Eval) Analysis + CIVO Onset Detection\\\\n# Input: metrics.jsonl from DreamerV3 logdirs (baseline + experiment runs)\\\\n# Output: per-experiment NVE report, cross-env summary table, NVE trajectory plots\\\\n# Depends: numpy, matplotlib, json, argparse\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport os\\\\nimport sys\\\\nimport numpy as np\\\\nfrom collections import OrderedDict\\\\nfrom datetime import datetime, timezone\\\\n\\\\nLOGDIR_DEFAULT = \\\\\\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir\\\\\\\"\\\\nCROSS_ENV_SUMMARY = os.path.join(LOGDIR_DEFAULT, \\\\\\\"cross_env_output\\\\\\\", \\\\\\\"cross_env_civo_summary.json\\\\\\\")\\\\nMIN_STEP = 35000\\\\nNVE_TAU = 2.0\\\\nSUSTAINED_COUNT = 2\\\\n\\\\n\\\\ndef load_metrics(logdir):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load eval_return and value_mean from metrics.jsonl, merge by step.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    path = os.path.join(logdir, \\\\\\\"metrics.jsonl\\\\\\\")\\\\n    if not os.path.exists(path):\\\\n        print(f\\\\\\\"WARNING: {path} not found\\\\\\\")\\\\n        return {}\\\\n\\\\n    eval_returns = {}\\\\n    value_means = {}\\\\n\\\\n    with open(path) as f:\\\\n        for line in f:\\\\n            line = line.strip()\\\\n            if not line:\\\\n                continue\\\\n            d = json.loads(line)\\\\n            step = d.get(\\\\\\\"step\\\\\\\")\\\\n            if step is None:\\\\n                continue\\\\n            if \\\\\\\"eval_return\\\\\\\" in d:\\\\n                eval_returns[step] = d[\\\\\\\"eval_return\\\\\\\"]\\\\n            if \\\\\\\"value_mean\\\\\\\" in d:\\\\n                value_means[step] = d[\\\\\\\"value_mean\\\\\\\"]\\\\n\\\\n    common_steps = sorted(set(eval_returns) & set(value_means))\\\\n    data = OrderedDict()\\\\n    for s in common_steps:\\\\n        er = eval_returns[s]\\\\n        vm = value_means[s]\\\\n        ve_ratio = vm / max(er, 1e-6)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"# Hopper NVE (Normalized Value-to-Eval) Analysis + CIVO Onset Detection\\n# Input: metrics.jsonl from DreamerV3 logdirs (baseline + experiment runs)\\n# Output: per-experiment NVE report, cross-env summary table, NVE trajectory plots\\n# Depends: numpy, matplotlib, json, argparse\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport numpy as np\\nfrom collections import OrderedDict\\nfrom datetime import datetime, timezone\\n\\nLOGDIR_DEFAULT = \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir\\\"\\nCROSS_ENV_SUMMARY = os.path.join(LOGDIR_DEFAULT, \\\"cross_env_output\\\", \\\"cross_env_civo_summary.json\\\")\\nMIN_STEP = 35000\\nNVE_TAU = 2.0\\nSUSTAINED_COUNT = 2\\n\\n\\ndef load_metrics(logdir):\\n    \\\"\\\"\\\"Load eval_return and value_mean from metrics.jsonl, merge by step.\\\"\\\"\\\"\\n    path = os.path.join(logdir, \\\"metrics.jsonl\\\")\\n    if not os.path.exists(path):\\n        print(f\\\"WARNING: {path} not found\\\")\\n        return {}\\n\\n    eval_returns = {}\\n    value_means = {}\\n\\n    with open(path) as f:\\n        for line in f:\\n            line = line.strip()\\n            if not line:\\n                continue\\n            d = json.loads(line)\\n            step = d.get(\\\"step\\\")\\n            if step is None:\\n                continue\\n            if \\\"eval_return\\\" in d:\\n                eval_returns[step] = d[\\\"eval_return\\\"]\\n            if \\\"value_mean\\\" in d:\\n                value_means[step] = d[\\\"value_mean\\\"]\\n\\n    common_steps = sorted(set(eval_returns) & set(value_means))\\n    data = OrderedDict()\\n    for s in common_steps:\\n        er = eval_returns[s]\\n        vm = value_means[s]\\n        ve_ratio = vm / max(er, 1e-6)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now I see:
1. configs.yaml has `dmc_walker_walk` as default task (line 28), and `dmc_proprio` / `dmc_vision` config sections
2. No hopper-specific task in configs.yaml - the task is passed as a command line argument
3. There's an `analyze_hopper_nve.py` script suggesting hopper experiments were run before

Let me check how the task string is parsed in dreamer.py (the DMC task parsing logic) and check the configs.yaml dmc_proprio section more carefully. Also need to look at the registry data for hopper experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "57cfd5f1-bc70-4b5a-98ae-493f10fbcc6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRXBzSER95JbvedywStJwy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2289,
      "cache_read_input_tokens": 27499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2289
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MsvFA72UbB29FsG2Kjy2Zj`</summary>

```json
{
  "server": "westd-51268",
  "command": "sed -n '130,160p' /root/autodl-tmp/event-gated-adaptive-horizon/configs.yaml",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "d32d714e-c15a-45c4-8605-53ec045cf3e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRXBzSER95JbvedywStJwy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2289,
      "cache_read_input_tokens": 27499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2289
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-29T08:25:50.378Z_

<details><summary>↩ Tool result · `toolu_01MsvFA72UbB29FsG2Kjy2Zj`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "a3a4f95b-2675-444c-a786-9e3ea19efa38",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LXvqY2zyMZdXoJsF6MoqAo`</summary>

```json
{
  "server": "westd-51268",
  "command": "grep -n \"dmc\" /root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "dafc3d56-8a23-44f3-ba98-d6858d7aa538",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRXBzSER95JbvedywStJwy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2289,
      "cache_read_input_tokens": 27499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2289
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-29T08:25:51.779Z_

<details><summary>↩ Tool result · `toolu_01LXvqY2zyMZdXoJsF6MoqAo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"200:    if suite == \\\"dmc\\\":\\n201:        import envs.dmc as dmc\\n203:        env = dmc.DeepMindControl(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "5967c8c2-555c-4d91-9464-efb4e4f69aab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"200:    if suite == \\\\\\\"dmc\\\\\\\":\\\\n201:        import envs.dmc as dmc\\\\n203:        env = dmc.DeepMindControl(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"200:    if suite == \\\"dmc\\\":\\n201:        import envs.dmc as dmc\\n203:        env = dmc.DeepMindControl(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Agent · `toolu_01N6CJGy5RgMxfogzVRH3B7Q`</summary>

```json
{
  "description": "Parse registry for hopper exps",
  "prompt": "I need you to extract all hopper-related experiments from a large JSON registry file. The file is at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt\n\nThis is JSON with schema: {result: string} — the `result` field is itself a JSON string that needs to be parsed.\n\nSteps:\n1. Probe the structure with jq (type/length/keys)\n2. Extract and search for any experiments whose id, name, notes, conclusion, or command contain \"hopper\" (case-insensitive)\n3. Also look for experiments with IDs matching exp_104 through exp_108\n\nFor each matching experiment, report:\n- exp_id\n- status (RUNNING/DONE/KILLED/FAILED etc.)\n- conclusion\n- notes\n- failure_reason (if any)\n- command (the training command used)\n- created_at / updated_at\n- Any other relevant fields\n\nReport ALL matching experiments verbatim — don't summarize away details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "8f07f438-bb61-4d7e-8871-1b10d869f5f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRXBzSER95JbvedywStJwy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2289,
      "cache_read_input_tokens": 27499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2289
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a687c872e3ff35f87",
  "tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "description": "Parse registry for hopper exps",
  "task_type": "local_agent",
  "prompt": "I need you to extract all hopper-related experiments from a large JSON registry file. The file is at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt\n\nThis is JSON with schema: {result: string} — the `result` field is itself a JSON string that needs to be parsed.\n\nSteps:\n1. Probe the structure with jq (type/length/keys)\n2. Extract and search for any experiments whose id, name, notes, conclusion, or command contain \"hopper\" (case-insensitive)\n3. Also look for experiments with IDs matching exp_104 through exp_108\n\nFor each matching experiment, report:\n- exp_id\n- status (RUNNING/DONE/KILLED/FAILED etc.)\n- conclusion\n- notes\n- failure_reason (if any)\n- command (the training command used)\n- created_at / updated_at\n- Any other relevant fields\n\nReport ALL matching experiments verbatim — don't summarize away details.",
  "uuid": "68c9502b-bd59-4de2-a8ed-f2d2d4dce2fd",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf"
}
```

---

## Round 1

44 recorded events

### User

_source line 34 · 2026-05-29T08:25:56.814Z_

I need you to extract all hopper-related experiments from a large JSON registry file. The file is at:
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt

This is JSON with schema: {result: string} — the `result` field is itself a JSON string that needs to be parsed.

Steps:
1. Probe the structure with jq (type/length/keys)
2. Extract and search for any experiments whose id, name, notes, conclusion, or command contain "hopper" (case-insensitive)
3. Also look for experiments with IDs matching exp_104 through exp_108

For each matching experiment, report:
- exp_id
- status (RUNNING/DONE/KILLED/FAILED etc.)
- conclusion
- notes
- failure_reason (if any)
- command (the training command used)
- created_at / updated_at
- Any other relevant fields

Report ALL matching experiments verbatim — don't summarize away details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "3e2d61db-29a2-440c-bdfc-a2724dd767e4"
}
```

</details>

---

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a687c872e3ff35f87",
  "tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 14675,
    "tool_uses": 1,
    "duration_ms": 4118
  },
  "last_tool_name": "Bash",
  "uuid": "38164bc6-8096-4447-a55b-dfbbfddab108",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01TK99CFjVREu6SaRDyFNWEa`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "f2c2d72b-5a5f-4da3-b7d1-b12bcab8c48e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hky32m2xzdZoMXT9yJfNcz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14664,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14664,
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

_source line 37 · 2026-05-29T08:26:01.145Z_

<details><summary>↩ Tool result · `toolu_01TK99CFjVREu6SaRDyFNWEa`</summary>

```text
475401 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "f686654c-32ae-4076-b9b6-ddb9c13a6118"
}
```

</details>

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a687c872e3ff35f87",
  "tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "description": "Running Probe JSON structure",
  "usage": {
    "total_tokens": 14679,
    "tool_uses": 2,
    "duration_ms": 7685
  },
  "last_tool_name": "Bash",
  "uuid": "d356c920-5802-442d-abfe-018913794c3f",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01HPYeCiTnBATXAuRkmYa17c`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nprint('Top-level type:', type(raw))\nprint('Top-level keys:', list(raw.keys()) if isinstance(raw, dict) else 'N/A')\ninner = json.loads(raw['result'])\nprint('Inner type:', type(inner))\nif isinstance(inner, dict):\n    print('Inner keys:', list(inner.keys()))\n    for k, v in inner.items():\n        if isinstance(v, list):\n            print(f'  {k}: list of {len(v)} items')\n        elif isinstance(v, dict):\n            print(f'  {k}: dict with {len(v)} keys')\n        else:\n            print(f'  {k}: {type(v).__name__} = {str(v)[:200]}')\nelif isinstance(inner, list):\n    print('Inner length:', len(inner))\n\" 2>&1",
  "description": "Probe JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "252155b3-0b38-4cb2-992e-7dcf92dea3de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hky32m2xzdZoMXT9yJfNcz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14664,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14664,
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

_source line 40 · 2026-05-29T08:26:04.628Z_

<details><summary>↩ Tool result · `toolu_01HPYeCiTnBATXAuRkmYa17c`</summary>

```text
Top-level type: &lt;class 'dict'>
Top-level keys: ['result']
Inner type: &lt;class 'dict'>
Inner keys: ['success', 'data', 'error', 'metadata']
  success: bool = True
  data: dict with 4 keys
  error: NoneType = None
  metadata: dict with 1 keys
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "b8aa68b5-b220-47e3-9bf8-a898bbd00446"
}
```

</details>

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a687c872e3ff35f87",
  "tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "description": "Running Explore data structure deeper",
  "usage": {
    "total_tokens": 16385,
    "tool_uses": 3,
    "duration_ms": 12917
  },
  "last_tool_name": "Bash",
  "uuid": "43f79e85-7acf-45da-aa7f-6958d8f97da8",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01AboLGZhAnk91EzRnes3eaF`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\ndata = inner['data']\nprint('data keys:', list(data.keys()))\nfor k, v in data.items():\n    if isinstance(v, list):\n        print(f'  {k}: list of {len(v)} items')\n        if v:\n            print(f'    first item keys: {list(v[0].keys()) if isinstance(v[0], dict) else type(v[0])}')\n    elif isinstance(v, dict):\n        print(f'  {k}: dict with keys: {list(v.keys())[:20]}')\n    else:\n        print(f'  {k}: {type(v).__name__} = {str(v)[:200]}')\nprint()\nprint('metadata:', inner['metadata'])\n\" 2>&1",
  "description": "Explore data structure deeper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "57ef3e09-b698-47e0-9556-83378ab56b08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BReYA19xJpPN1Kumu1LKai",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1635,
      "cache_read_input_tokens": 14664,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1635,
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

_source line 43 · 2026-05-29T08:26:09.846Z_

<details><summary>↩ Tool result · `toolu_01AboLGZhAnk91EzRnes3eaF`</summary>

```text
data keys: ['experiments', 'count', 'total', 'baseline']
  experiments: dict with keys: ['exp_quadruped_008d_s0', 'exp_walker_no_dt_emb_s0', 'exp_humanoid_008d_s0', 'exp_quadruped_baseline_s0_r2', 'exp_humanoid_baseline_s0', 'exp_walker_no_dt_emb_s1', 'exp_quadruped_baseline_s0', 'exp_walker_008d_s7_r2', 'exp_walker_008d_s6_r2', 'exp_walker_008d_s7', 'exp_walker_008d_s6', 'exp_cheetah_008a_s3', 'exp_cheetah_008a_s2', 'exp_walker_008f_s0', 'exp_cheetah_008a_s0', 'exp_cheetah_008a_s1', 'exp_hopper_no_dt_emb_s0', 'exp_hopper_frozen_s0_ext', 'exp_009f_008f_walker_s1', 'exp_009e_008d_walker_s1']
  count: int = 213
  total: int = 213
  baseline: NoneType = None

metadata: {'elapsed_seconds': 0.9998}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "ec39fca0-51dd-46f1-aed7-31a0d2154a6d"
}
```

</details>

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a687c872e3ff35f87",
  "tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "description": "Running Find all hopper-related and exp_104-108 experiments",
  "usage": {
    "total_tokens": 17199,
    "tool_uses": 4,
    "duration_ms": 24175
  },
  "last_tool_name": "Bash",
  "uuid": "283e9e9a-c697-4913-b939-ea0a066e7a0e",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf"
}
```

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01FDuHAvEb8AJMJh38GpDzFk`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexperiments = inner['data']['experiments']\n\n# Find all hopper-related experiments (case-insensitive search across all string fields)\nhopper_exps = {}\nfor exp_id, exp_data in experiments.items():\n    exp_str = json.dumps(exp_data).lower()\n    is_hopper = 'hopper' in exp_str or 'hopper' in exp_id.lower()\n    # Also check exp_104 through exp_108\n    is_104_108 = False\n    for n in range(104, 109):\n        if f'exp_{n}' in exp_id or f'exp_{n}' in exp_str:\n            is_104_108 = True\n            break\n    if is_hopper or is_104_108:\n        hopper_exps[exp_id] = exp_data\n\nprint(f'Found {len(hopper_exps)} matching experiments')\nprint()\nprint('Matching IDs:')\nfor eid in sorted(hopper_exps.keys()):\n    print(f'  {eid}')\n\" 2>&1",
  "description": "Find all hopper-related and exp_104-108 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "8cb4badf-7ea8-44c7-9fd0-48b8acedae04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017PKvxEiJiF2U35M4VrKz5G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 741,
      "cache_read_input_tokens": 16299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 741,
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

_source line 46 · 2026-05-29T08:26:21.137Z_

<details><summary>↩ Tool result · `toolu_01FDuHAvEb8AJMJh38GpDzFk`</summary>

```text
Found 13 matching experiments

Matching IDs:
  exp_104_hopper_baseline_s0
  exp_105_hopper_trained_s0
  exp_106_hopper_trained_s1
  exp_107_hopper_frozen_s0
  exp_108_hopper_frozen_s1
  exp_hopper_baseline
  exp_hopper_frozen_s0
  exp_hopper_frozen_s0_ext
  exp_hopper_frozen_s1
  exp_hopper_no_dt_emb_s0
  exp_hopper_trained_s0
  exp_hopper_trained_s0_ext
  exp_hopper_trained_s1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "26b22a7a-ab06-44ef-be89-b6f8812c6705"
}
```

</details>

---

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a687c872e3ff35f87",
  "tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "description": "Running Dump all hopper experiments verbatim",
  "usage": {
    "total_tokens": 17929,
    "tool_uses": 5,
    "duration_ms": 30372
  },
  "last_tool_name": "Bash",
  "uuid": "8b4e3c82-7a39-425c-b740-6082316d2908",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_01YPdjM6J9rxEdothMw3Sxwz`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexperiments = inner['data']['experiments']\n\nhopper_ids = [\n    'exp_104_hopper_baseline_s0',\n    'exp_105_hopper_trained_s0',\n    'exp_106_hopper_trained_s1',\n    'exp_107_hopper_frozen_s0',\n    'exp_108_hopper_frozen_s1',\n    'exp_hopper_baseline',\n    'exp_hopper_frozen_s0',\n    'exp_hopper_frozen_s0_ext',\n    'exp_hopper_frozen_s1',\n    'exp_hopper_no_dt_emb_s0',\n    'exp_hopper_trained_s0',\n    'exp_hopper_trained_s0_ext',\n    'exp_hopper_trained_s1',\n]\n\nfor eid in hopper_ids:\n    exp = experiments[eid]\n    print('=' * 100)\n    print(json.dumps({eid: exp}, indent=2, ensure_ascii=False))\n    print()\n\" 2>&1",
  "description": "Dump all hopper experiments verbatim"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "67ee7243-b6b9-41ba-9303-870260f18d55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y73huHtZuLtyab7KZYqfTK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 657,
      "cache_read_input_tokens": 17040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 657,
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

_source line 49 · 2026-05-29T08:26:27.303Z_

<details><summary>↩ Tool result · `toolu_01YPdjM6J9rxEdothMw3Sxwz`</summary>

```text
====================================================================================================
{
  "exp_104_hopper_baseline_s0": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T02:55:00.720Z",
    "updated_at": "2026-05-27T03:03:15.605Z",
    "hypothesis": "Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE &lt; 1.5×). Source: C1/C2 third-environment verification (D160).",
    "conclusion": "killed",
    "completed_at": "2026-05-27T03:03:15.605Z"
  }
}

====================================================================================================
{
  "exp_105_hopper_trained_s0": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T02:55:06.756Z",
    "updated_at": "2026-05-27T03:03:20.261Z",
    "hypothesis": "Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE &gt; 1.5× after 35K steps), consistent with Walker (3/3) and Cheetah (3/4). Source: C2 third-environment verification (D160).",
    "conclusion": "killed",
    "completed_at": "2026-05-27T03:03:20.261Z"
  }
}

====================================================================================================
{
  "exp_106_hopper_trained_s1": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T02:55:11.391Z",
    "updated_at": "2026-05-27T03:03:24.020Z",
    "hypothesis": "Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE &gt; 1.5× after 35K steps), second seed for onset rate. Source: C2 third-environment verification (D160).",
    "conclusion": "killed",
    "completed_at": "2026-05-27T03:03:24.020Z"
  }
}

====================================================================================================
{
  "exp_107_hopper_frozen_s0": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T02:55:18.139Z",
    "updated_at": "2026-05-27T03:03:27.004Z",
    "hypothesis": "Frozen dt_embedding in Hopper Hop will prevent CIVO onset (NVE &lt; 1.5× throughout), confirming causal role of trained dt_emb as CIVO trigger. Source: C6 third-environment verification (D160).",
    "conclusion": "killed",
    "completed_at": "2026-05-27T03:03:27.004Z"
  }
}

====================================================================================================
{
  "exp_108_hopper_frozen_s1": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T02:55:22.603Z",
    "updated_at": "2026-05-27T03:03:32.297Z",
    "hypothesis": "Frozen dt_embedding in Hopper Hop will prevent CIVO onset (NVE &lt; 1.5× throughout), second seed for mitigation confirmation. Source: C6 third-environment verification (D160).",
    "conclusion": "killed",
    "completed_at": "2026-05-27T03:03:32.297Z"
  }
}

====================================================================================================
{
  "exp_hopper_baseline": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T02:34:22.253Z",
    "updated_at": "2026-05-27T06:24:27.230Z",
    "conclusion": "success",
    "hypothesis": "Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE &lt; 1.5×). Source: C1/C2 third-environment verification (D160).",
    "plan_id": "plan_040",
    "server": "westd-51268",
    "gpu": "cuda:0",
    "account": "root",
    "reproduce": {
      "server": "westd-51268",
      "gpu": "cuda:0",
      "started_at": "2026-05-27T02:55:33.719Z",
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 105000 --seed 0 --compile False --device cuda:0\"",
      "finished_at": "2026-05-27T05:48:08.854Z",
      "training_hours": 2.88
    },
    "spec": {
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 105000 --seed 0 --compile False --device cuda:0\"",
      "server": "westd-51268",
      "gpu": [
        "cuda:0"
      ],
      "pid": "604350",
      "log_path": "logdir/exp_hopper_baseline/metrics.jsonl",
      "submitted_at": "2026-05-27T02:59:02.775Z",
      "submitted_via": "submit_training_job",
      "backend": "tmux",
      "account": "root",
      "checkpoint_path": "logdir/exp_hopper_baseline/latest.pt",
      "wall_clock_seconds": 12318.4,
      "gpu_hours": 3.42
    },
    "pid": "604350",
    "log_path": "~/runs/event-gated-adaptive-horizon/exp_hopper_baseline.log",
    "extra": {
      "hook_events": [
        {
          "event": "on_complete",
          "action": "agent",
          "ts": "2026-05-27T05:48:15.500405+00:00"
        }
      ]
    },
    "metrics": {
      "step": 105000,
      "eval_return_final": 96.43,
      "ve_ratio_final": 0.559,
      "ve_ratio_peak": 3.48,
      "ve_ratio_peak_step": 65000,
      "civo_alert": 0,
      "value_mean_final": 53.9,
      "target_mean_final": 54.2,
      "wall_clock_hours": 2.88
    },
    "completed_at": "2026-05-27T06:24:21.198Z"
  }
}

====================================================================================================
{
  "exp_hopper_frozen_s0": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T02:34:34.615Z",
    "updated_at": "2026-05-27T09:14:56.465Z",
    "conclusion": "success",
    "hypothesis": "Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5×), confirming trained dt_emb is the necessary condition for CIVO across a third multi-joint locomotion environment",
    "plan_id": "plan_040",
    "server": "westd-51268",
    "gpu": "cuda:0",
    "account": "root",
    "reproduce": {
      "server": "westd-51268",
      "gpu": "cuda:0",
      "started_at": "2026-05-27T05:51:11.281Z",
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\"",
      "finished_at": "2026-05-27T08:49:59.215Z",
      "training_hours": 2.98
    },
    "spec": {
      "data_path": "dmc_hopper_hop",
      "data_count": 105000,
      "model_name": "dreamerv3",
      "seed": 0,
      "checkpoint_source": "none (fresh training)",
      "eval_data": "dmc_hopper_hop",
      "checkpoint_path": "logdir/exp_hopper_frozen_s0/latest.pt",
      "log_path": "logdir/exp_hopper_frozen_s0/metrics.jsonl"
    },
    "pid": "612905",
    "log_path": "~/runs/event-gated-adaptive-horizon/exp_hopper_frozen_s0.log",
    "extra": {
      "hook_events": [
        {
          "event": "on_complete",
          "action": "agent",
          "ts": "2026-05-27T08:50:05.781559+00:00"
        }
      ]
    },
    "metrics": {
      "step": 105000,
      "eval_return_final": 0,
      "eval_return_peak": 3.6,
      "eval_return_peak_step": 85000,
      "ve_ratio_final": 4335664.3,
      "civo_alert": 1,
      "civo_alert_steps": [
        65000,
        105000
      ],
      "value_mean_final": 4.337,
      "target_mean_final": 4.389,
      "wall_clock_hours": 2.95,
      "pattern": "degenerate_civo_near_zero_magnitude",
      "notes": "D155 criteria formally met @95K (ve=2.69, sustained 2 points) but eval_return=1.083 (1.1% baseline). 105K ve=4.3M is eval=0/epsilon artifact. Mechanistically distinct from Walker/Cheetah standard CIVO."
    },
    "checkpoint_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_frozen_s0/latest.pt",
    "completed_at": "2026-05-27T08:57:25.460Z"
  }
}

====================================================================================================
{
  "exp_hopper_frozen_s0_ext": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T09:14:24.513Z",
    "updated_at": "2026-05-27T10:56:21.405Z",
    "hypothesis": "Extending frozen_s0 from 105K→150K will show eval_return recovery (rising like trained_s0_ext: 3.26→81.58) with ve_ratio declining, confirming frozen_s0's 'degenerate CIVO' @95K is transient instability during severe learning delay, not true CIVO mechanism. Source: D163.",
    "parent": "exp_hopper_frozen_s0",
    "plan_id": "D163",
    "server": "westd-51268",
    "gpu": "cuda:0",
    "spec": {
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s0 --steps 150000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\"",
      "server": "westd-51268",
      "gpu": [
        "cuda:0"
      ],
      "pid": "622633",
      "log_path": "~/runs/event-gated-adaptive-horizon/exp_hopper_frozen_s0_ext.log",
      "submitted_at": "2026-05-27T09:16:00.102Z",
      "submitted_via": "submit_training_job",
      "backend": "tmux",
      "account": "root",
      "wall_clock_seconds": 6021.3,
      "gpu_hours": 1.67
    },
    "pid": "622633",
    "log_path": "logdir/exp_hopper_frozen_s0/metrics.jsonl",
    "reproduce": {
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s0 --steps 150000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\"",
      "finished_at": "2026-05-27T10:41:59.098Z"
    },
    "extra": {
      "hook_events": [
        {
          "event": "on_complete",
          "action": "agent",
          "ts": "2026-05-27T10:42:05.863225+00:00"
        }
      ]
    },
    "metrics": {
      "step": 160000,
      "eval_step": 152000,
      "eval_return_final": 0.5608,
      "eval_return_105K": 0,
      "eval_return_peak": 1.534,
      "eval_return_peak_step": 112000,
      "ve_ratio_trajectory": {
        "105K": 4335664.27,
        "122K": 10.149,
        "132K": 955.034,
        "142K": 18.055,
        "152K": 15.08
      },
      "value_mean_trajectory": {
        "105K": 4.34,
        "122K": 7.18,
        "132K": 7.08,
        "142K": 7.62,
        "152K": 8.46
      },
      "nve_peak": 7756535.1,
      "nve_peak_step": 105000,
      "nve_35K": 2.75,
      "nve_95K": 5.2,
      "pattern": "persistent_phantom_value_no_recovery",
      "comparison_vs_trained_s0_ext": "trained recovered (3.26→81.58), frozen did NOT (0→0.56). Fundamentally different failure mode.",
      "notes": "eval_return stayed 0-1.5 throughout 105K-152K extension. value_mean grew 4.34→8.46 (phantom value). ve_ratio remained elevated 10-955x. No recovery pattern observed."
    },
    "checkpoint_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_frozen_s0/latest.pt",
    "conclusion": "negative",
    "completed_at": "2026-05-27T10:56:21.405Z"
  }
}

====================================================================================================
{
  "exp_hopper_frozen_s1": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T02:34:37.319Z",
    "updated_at": "2026-05-27T10:47:34.515Z",
    "conclusion": "killed",
    "hypothesis": "Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5×), confirming trained dt_emb is the necessary condition for CIVO across a third multi-joint locomotion environment (seed 1 replication)",
    "plan_id": "plan_040",
    "server": "westd-51268",
    "gpu": "cuda:0",
    "spec": {
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\"",
      "server": "westd-51268",
      "gpu": [
        "cuda:0"
      ],
      "pid": "626827",
      "log_path": "N/A",
      "submitted_at": "2026-05-27T10:45:13.546Z",
      "submitted_via": "submit_training_job",
      "backend": "tmux",
      "account": "root",
      "checkpoint_path": "N/A",
      "wall_clock_seconds": 141.0,
      "gpu_hours": 0.04
    },
    "pid": "626827",
    "log_path": "~/runs/event-gated-adaptive-horizon/exp_hopper_frozen_s1.log",
    "reproduce": {
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\""
    },
    "completed_at": "2026-05-27T10:47:34.515Z"
  }
}

====================================================================================================
{
  "exp_hopper_no_dt_emb_s0": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T08:08:47.870Z",
    "updated_at": "2026-05-27T11:17:21.884Z",
    "hypothesis": "Removing dt_embedding entirely (dt_embed_dim=0) while keeping gate+dt=2+subsample ON will still show severe learning delay in Hopper, confirming gate mechanism itself (not dt_emb) is the root cause of Hopper's failure. Source: D162 diagnostic.",
    "parent": "exp_hopper_trained_s0",
    "server": "westd-51268",
    "gpu": "cuda:1",
    "spec": {
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\"",
      "server": "westd-51268",
      "gpu": [
        "cuda:1"
      ],
      "pid": "619366",
      "log_path": "~/runs/event-gated-adaptive-horizon/exp_hopper_no_dt_emb_s0.log",
      "submitted_at": "2026-05-27T08:09:15.483Z",
      "submitted_via": "submit_training_job",
      "backend": "tmux",
      "account": "root",
      "wall_clock_seconds": 11286.4,
      "gpu_hours": 3.14
    },
    "pid": "619366",
    "log_path": "~/runs/event-gated-adaptive-horizon/exp_hopper_no_dt_emb_s0.log",
    "reproduce": {
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\"",
      "finished_at": "2026-05-27T11:10:43.054Z"
    },
    "extra": {
      "hook_events": [
        {
          "event": "on_complete",
          "action": "agent",
          "ts": "2026-05-27T11:10:49.451083+00:00"
        }
      ]
    },
    "conclusion": "success",
    "metrics": {
      "eval_return_final": 10.759,
      "eval_return_final_pct_baseline": 11.2,
      "ve_ratio_peak_gte35k": 1.949,
      "nve_peak": 4.37,
      "nve_sustained_above_1_5": false,
      "value_mean_final": 2.32,
      "actor_entropy_final": -1.939
    },
    "checkpoint_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_no_dt_emb_s0",
    "completed_at": "2026-05-27T11:17:21.884Z"
  }
}

====================================================================================================
{
  "exp_hopper_trained_s0": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T02:34:26.587Z",
    "updated_at": "2026-05-27T08:08:33.860Z",
    "conclusion": "success",
    "hypothesis": "Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE &gt; 1.5× after 35K steps), consistent with Walker (3/3) and Cheetah (3/4). Source: C2 third-environment verification (D160).",
    "plan_id": "plan_040",
    "server": "westd-51268",
    "gpu": "cuda:1",
    "account": "root",
    "reproduce": {
      "server": "westd-51268",
      "gpu": "cuda:1",
      "started_at": "2026-05-27T02:55:36.648Z",
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\""
    },
    "spec": {
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\"",
      "server": "westd-51268",
      "gpu": [
        "cuda:1"
      ],
      "pid": "604513",
      "log_path": "logdir/exp_hopper_trained_s0/metrics.jsonl",
      "submitted_at": "2026-05-27T02:59:09.552Z",
      "submitted_via": "submit_training_job",
      "backend": "tmux",
      "account": "root",
      "checkpoint_path": "logdir/exp_hopper_trained_s0/latest.pt",
      "wall_clock_seconds": 10864.2,
      "gpu_hours": 3.02
    },
    "pid": "604513",
    "log_path": "~/runs/event-gated-adaptive-horizon/exp_hopper_trained_s0.log",
    "completed_at": "2026-05-27T06:00:13.703Z",
    "metrics": {
      "step": 105000,
      "eval_return_final": 3.26,
      "eval_return_peak": 8.01,
      "eval_return_peak_step": 85000,
      "ve_ratio_final": 0.897,
      "civo_alert": 1,
      "value_mean_trajectory": [
        0.48,
        1.29,
        2.93
      ],
      "pattern": "severe_learning_delay",
      "nve_105K_vs_baseline": 1.6,
      "notes": "no CIVO detected; gate+dt=2 causes learning delay in Hopper independent of dt_emb training"
    }
  }
}

====================================================================================================
{
  "exp_hopper_trained_s0_ext": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T06:00:49.737Z",
    "updated_at": "2026-05-27T08:07:16.279Z",
    "hypothesis": "Continuing trained_s0 from 105K to 150K will confirm delayed CIVO: ve_ratio (0.897 at 105K, exponentially rising) will cross NVE>1.5 threshold by ~115-125K, upgrading from emerging to confirmed delayed CIVO. Parent: exp_hopper_trained_s0.",
    "parent": "exp_hopper_trained_s0",
    "spec": {
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 150000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\"",
      "server": "westd-51268",
      "gpu": [
        "cuda:1"
      ],
      "pid": "614518",
      "log_path": "~/runs/event-gated-adaptive-horizon/exp_hopper_trained_s0_ext.log",
      "submitted_at": "2026-05-27T06:21:00.173Z",
      "submitted_via": "submit_training_job",
      "backend": "tmux",
      "account": "root",
      "wall_clock_seconds": 6254.5,
      "gpu_hours": 1.74
    },
    "server": "westd-51268",
    "gpu": "cuda:1",
    "pid": "614518",
    "log_path": "~/runs/event-gated-adaptive-horizon/exp_hopper_trained_s0_ext.log",
    "reproduce": {
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 150000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\"",
      "finished_at": "2026-05-27T07:59:25.773Z"
    },
    "extra": {
      "hook_events": [
        {
          "event": "on_complete",
          "action": "agent",
          "ts": "2026-05-27T07:59:32.660838+00:00"
        }
      ]
    },
    "metrics": {
      "step": 168000,
      "eval_step": 158000,
      "eval_return_final": 81.58,
      "eval_return_105K": 3.26,
      "eval_return_peak": 81.58,
      "ve_ratio_trajectory": {
        "105K": 0.897,
        "118K": 0.376,
        "128K": 5.519,
        "138K": 0.37,
        "148K": 0.55,
        "158K": 0.439
      },
      "civo_alert_105K": 1,
      "civo_alert_final": 0,
      "pattern": "transient_instability_recovered",
      "nve_105K_vs_baseline": 1.6
    },
    "conclusion": "negative",
    "checkpoint_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_trained_s0/latest.pt",
    "completed_at": "2026-05-27T08:05:14.676Z"
  }
}

====================================================================================================
{
  "exp_hopper_trained_s1": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-27T02:34:29.841Z",
    "updated_at": "2026-05-27T08:08:35.045Z",
    "conclusion": "killed",
    "hypothesis": "Trained dt_emb + subsample ON in Hopper Hop will reproduce CIVO (NVE > 1.5×) as observed in Walker (3/3) and Cheetah (3/4), confirming CIVO generalizes across multi-joint locomotion environments (seed 1 replication)",
    "plan_id": "plan_040",
    "spec": {
      "server": "westd-51268",
      "gpu": "cuda:1",
      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\"",
      "model_name": "dreamerv3",
      "data_path": "dmc_hopper_hop (online)",
      "data_count": "105000 steps",
      "seed": 1,
      "checkpoint_path": "N/A",
      "log_path": "N/A"
    },
    "completed_at": "2026-05-27T08:08:35.045Z"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "f2f249f3-f540-436f-b2fa-4933c96a9379"
}
```

</details>

---

### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a687c872e3ff35f87",
  "tool_use_id": "toolu_01N6CJGy5RgMxfogzVRH3B7Q",
  "status": "completed",
  "output_file": "",
  "summary": "Parse registry for hopper exps",
  "usage": {
    "total_tokens": 27558,
    "tool_uses": 5,
    "duration_ms": 98779
  },
  "uuid": "66baba40-79b0-4099-911b-0a06b84353ca",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf"
}
```

---

### Tool result

_source line 51 · 2026-05-29T08:27:35.598Z_

<details><summary>↩ Tool result · `toolu_01N6CJGy5RgMxfogzVRH3B7Q`</summary>

```text
Here are all 13 hopper-related experiments extracted verbatim from the registry.

---

## exp_104_hopper_baseline_s0
- **status**: DONE
- **conclusion**: killed
- **created_at**: 2026-05-27T02:55:00.720Z
- **updated_at**: 2026-05-27T03:03:15.605Z
- **completed_at**: 2026-05-27T03:03:15.605Z
- **hypothesis**: Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE < 1.5×). Source: C1/C2 third-environment verification (D160).
- **retry_count**: 0
- **command**: (none stored — no `spec` or `reproduce` block)
- **failure_reason**: (none)
- **metrics**: (none)

---

## exp_105_hopper_trained_s0
- **status**: DONE
- **conclusion**: killed
- **created_at**: 2026-05-27T02:55:06.756Z
- **updated_at**: 2026-05-27T03:03:20.261Z
- **completed_at**: 2026-05-27T03:03:20.261Z
- **hypothesis**: Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE > 1.5× after 35K steps), consistent with Walker (3/3) and Cheetah (3/4). Source: C2 third-environment verification (D160).
- **retry_count**: 0
- **command**: (none stored)
- **failure_reason**: (none)
- **metrics**: (none)

---

## exp_106_hopper_trained_s1
- **status**: DONE
- **conclusion**: killed
- **created_at**: 2026-05-27T02:55:11.391Z
- **updated_at**: 2026-05-27T03:03:24.020Z
- **completed_at**: 2026-05-27T03:03:24.020Z
- **hypothesis**: Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE > 1.5× after 35K steps), second seed for onset rate. Source: C2 third-environment verification (D160).
- **retry_count**: 0
- **command**: (none stored)
- **failure_reason**: (none)
- **metrics**: (none)

---

## exp_107_hopper_frozen_s0
- **status**: DONE
- **conclusion**: killed
- **created_at**: 2026-05-27T02:55:18.139Z
- **updated_at**: 2026-05-27T03:03:27.004Z
- **completed_at**: 2026-05-27T03:03:27.004Z
- **hypothesis**: Frozen dt_embedding in Hopper Hop will prevent CIVO onset (NVE < 1.5× throughout), confirming causal role of trained dt_emb as CIVO trigger. Source: C6 third-environment verification (D160).
- **retry_count**: 0
- **command**: (none stored)
- **failure_reason**: (none)
- **metrics**: (none)

---

## exp_108_hopper_frozen_s1
- **status**: DONE
- **conclusion**: killed
- **created_at**: 2026-05-27T02:55:22.603Z
- **updated_at**: 2026-05-27T03:03:32.297Z
- **completed_at**: 2026-05-27T03:03:32.297Z
- **hypothesis**: Frozen dt_embedding in Hopper Hop will prevent CIVO onset (NVE < 1.5× throughout), second seed for mitigation confirmation. Source: C6 third-environment verification (D160).
- **retry_count**: 0
- **command**: (none stored)
- **failure_reason**: (none)
- **metrics**: (none)

Note: exp_104 through exp_108 were all killed ~8 minutes after creation with no metrics, commands, or specs recorded. These appear to be an early batch that was aborted and replaced by the longer-named experiments below.

---

## exp_hopper_baseline
- **status**: DONE
- **conclusion**: success
- **created_at**: 2026-05-27T02:34:22.253Z
- **updated_at**: 2026-05-27T06:24:27.230Z
- **completed_at**: 2026-05-27T06:24:21.198Z
- **hypothesis**: Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE < 1.5×). Source: C1/C2 third-environment verification (D160).
- **plan_id**: plan_040
- **server**: westd-51268, **gpu**: cuda:0, **account**: root
- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 105000 --seed 0 --compile False --device cuda:0`
- **pid**: 604350
- **training_hours**: 2.88 (wall_clock_seconds: 12318.4, gpu_hours: 3.42)
- **metrics**:
  - step: 105000
  - eval_return_final: 96.43
  - ve_ratio_final: 0.559
  - ve_ratio_peak: 3.48 (at step 65000)
  - civo_alert: 0
  - value_mean_final: 53.9
  - target_mean_final: 54.2

---

## exp_hopper_trained_s0
- **status**: DONE
- **conclusion**: success
- **created_at**: 2026-05-27T02:34:26.587Z
- **updated_at**: 2026-05-27T08:08:33.860Z
- **completed_at**: 2026-05-27T06:00:13.703Z
- **hypothesis**: Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE > 1.5× after 35K steps), consistent with Walker (3/3) and Cheetah (3/4). Source: C2 third-environment verification (D160).
- **plan_id**: plan_040
- **server**: westd-51268, **gpu**: cuda:1, **account**: root
- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8`
- **pid**: 604513
- **wall_clock_seconds**: 10864.2, **gpu_hours**: 3.02
- **metrics**:
  - step: 105000
  - eval_return_final: 3.26
  - eval_return_peak: 8.01 (at step 85000)
  - ve_ratio_final: 0.897
  - civo_alert: 1
  - nve_105K_vs_baseline: 1.6
  - pattern: **severe_learning_delay**
  - notes: "no CIVO detected; gate+dt=2 causes learning delay in Hopper independent of dt_emb training"
  - value_mean_trajectory: [0.48, 1.29, 2.93]

---

## exp_hopper_trained_s0_ext
- **status**: DONE
- **conclusion**: negative
- **created_at**: 2026-05-27T06:00:49.737Z
- **updated_at**: 2026-05-27T08:07:16.279Z
- **completed_at**: 2026-05-27T08:05:14.676Z
- **parent**: exp_hopper_trained_s0
- **hypothesis**: Continuing trained_s0 from 105K to 150K will confirm delayed CIVO: ve_ratio (0.897 at 105K, exponentially rising) will cross NVE>1.5 threshold by ~115-125K, upgrading from emerging to confirmed delayed CIVO.
- **server**: westd-51268, **gpu**: cuda:1
- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 150000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8`
- **pid**: 614518
- **wall_clock_seconds**: 6254.5, **gpu_hours**: 1.74
- **metrics**:
  - step: 168000, eval_step: 158000
  - eval_return_final: 81.58 (recovered from 3.26 at 105K)
  - eval_return_peak: 81.58
  - ve_ratio_trajectory: {105K: 0.897, 118K: 0.376, 128K: 5.519, 138K: 0.37, 148K: 0.55, 158K: 0.439}
  - civo_alert_105K: 1, civo_alert_final: 0
  - pattern: **transient_instability_recovered**
  - nve_105K_vs_baseline: 1.6
- **checkpoint_path**: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_trained_s0/latest.pt

---

## exp_hopper_trained_s1
- **status**: DONE
- **conclusion**: killed
- **created_at**: 2026-05-27T02:34:29.841Z
- **updated_at**: 2026-05-27T08:08:35.045Z
- **completed_at**: 2026-05-27T08:08:35.045Z
- **hypothesis**: Trained dt_emb + subsample ON in Hopper Hop will reproduce CIVO (NVE > 1.5×) as observed in Walker (3/3) and Cheetah (3/4), confirming CIVO generalizes across multi-joint locomotion environments (seed 1 replication)
- **plan_id**: plan_040
- **command** (from spec): `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8`
- **server**: westd-51268, **gpu**: cuda:1
- **metrics**: (none — killed before completion)

---

## exp_hopper_frozen_s0
- **status**: DONE
- **conclusion**: success
- **created_at**: 2026-05-27T02:34:34.615Z
- **updated_at**: 2026-05-27T09:14:56.465Z
- **completed_at**: 2026-05-27T08:57:25.460Z
- **hypothesis**: Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5×), confirming trained dt_emb is the necessary condition for CIVO across a third multi-joint locomotion environment
- **plan_id**: plan_040
- **server**: westd-51268, **gpu**: cuda:0, **account**: root
- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True`
- **pid**: 612905
- **training_hours**: 2.98 (reproduce), 2.95 (metrics)
- **metrics**:
  - step: 105000
  - eval_return_final: 0
  - eval_return_peak: 3.6 (at step 85000)
  - ve_ratio_final: 4,335,664.3 (!)
  - civo_alert: 1
  - civo_alert_steps: [65000, 105000]
  - value_mean_final: 4.337, target_mean_final: 4.389
  - pattern: **degenerate_civo_near_zero_magnitude**
  - notes: "D155 criteria formally met @95K (ve=2.69, sustained 2 points) but eval_return=1.083 (1.1% baseline). 105K ve=4.3M is eval=0/epsilon artifact. Mechanistically distinct from Walker/Cheetah standard CIVO."
- **checkpoint_path**: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_frozen_s0/latest.pt

---

## exp_hopper_frozen_s0_ext
- **status**: DONE
- **conclusion**: negative
- **created_at**: 2026-05-27T09:14:24.513Z
- **updated_at**: 2026-05-27T10:56:21.405Z
- **completed_at**: 2026-05-27T10:56:21.405Z
- **parent**: exp_hopper_frozen_s0
- **plan_id**: D163
- **hypothesis**: Extending frozen_s0 from 105K to 150K will show eval_return recovery (rising like trained_s0_ext: 3.26 to 81.58) with ve_ratio declining, confirming frozen_s0's 'degenerate CIVO' @95K is transient instability during severe learning delay, not true CIVO mechanism. Source: D163.
- **server**: westd-51268, **gpu**: cuda:0
- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s0 --steps 150000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True`
- **pid**: 622633
- **wall_clock_seconds**: 6021.3, **gpu_hours**: 1.67
- **metrics**:
  - step: 160000, eval_step: 152000
  - eval_return_final: 0.5608 (no recovery)
  - eval_return_105K: 0
  - eval_return_peak: 1.534 (at step 112000)
  - ve_ratio_trajectory: {105K: 4335664.27, 122K: 10.149, 132K: 955.034, 142K: 18.055, 152K: 15.08}
  - value_mean_trajectory: {105K: 4.34, 122K: 7.18, 132K: 7.08, 142K: 7.62, 152K: 8.46}
  - nve_peak: 7,756,535.1 (at step 105000)
  - nve_35K: 2.75, nve_95K: 5.2
  - pattern: **persistent_phantom_value_no_recovery**
  - comparison_vs_trained_s0_ext: "trained recovered (3.26 to 81.58), frozen did NOT (0 to 0.56). Fundamentally different failure mode."
  - notes: "eval_return stayed 0-1.5 throughout 105K-152K extension. value_mean grew 4.34 to 8.46 (phantom value). ve_ratio remained elevated 10-955x. No recovery pattern observed."
- **checkpoint_path**: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_frozen_s0/latest.pt

---

## exp_hopper_frozen_s1
- **status**: DONE
- **conclusion**: killed
- **created_at**: 2026-05-27T02:34:37.319Z
- **updated_at**: 2026-05-27T10:47:34.515Z
- **completed_at**: 2026-05-27T10:47:34.515Z
- **hypothesis**: Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5×), confirming trained dt_emb is the necessary condition for CIVO across a third multi-joint locomotion environment (seed 1 replication)
- **plan_id**: plan_040
- **server**: westd-51268, **gpu**: cuda:0
- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True`
- **pid**: 626827
- **wall_clock_seconds**: 141.0, **gpu_hours**: 0.04
- **metrics**: (none — killed after ~2.4 minutes)

---

## exp_hopper_no_dt_emb_s0
- **status**: DONE
- **conclusion**: success
- **created_at**: 2026-05-27T08:08:47.870Z
- **updated_at**: 2026-05-27T11:17:21.884Z
- **completed_at**: 2026-05-27T11:17:21.884Z
- **parent**: exp_hopper_trained_s0
- **hypothesis**: Removing dt_embedding entirely (dt_embed_dim=0) while keeping gate+dt=2+subsample ON will still show severe learning delay in Hopper, confirming gate mechanism itself (not dt_emb) is the root cause of Hopper's failure. Source: D162 diagnostic.
- **server**: westd-51268, **gpu**: cuda:1
- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0`
- **pid**: 619366
- **wall_clock_seconds**: 11286.4, **gpu_hours**: 3.14
- **metrics**:
  - eval_return_final: 10.759 (11.2% of baseline)
  - ve_ratio_peak_gte35k: 1.949
  - nve_peak: 4.37
  - nve_sustained_above_1_5: false
  - value_mean_final: 2.32
  - actor_entropy_final: -1.939
- **checkpoint_path**: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_no_dt_emb_s0

---

## Summary of the 13 experiments

| Experiment | Status | Conclusion | eval_return_final | Key Pattern |
|---|---|---|---|---|
| exp_104 through exp_108 (5 exps) | DONE | killed | N/A | Early batch, aborted ~8min after creation |
| exp_hopper_baseline | DONE | success | 96.43 | Reference baseline, no CIVO |
| exp_hopper_trained_s0 | DONE | success | 3.26 | severe_learning_delay (gate causes delay, not CIVO) |
| exp_hopper_trained_s0_ext | DONE | negative | 81.58 | transient_instability_recovered (recovered after 150K) |
| exp_hopper_trained_s1 | DONE | killed | N/A | Killed, no metrics |
| exp_hopper_frozen_s0 | DONE | success | 0 | degenerate_civo_near_zero_magnitude (ve=4.3M artifact) |
| exp_hopper_frozen_s0_ext | DONE | negative | 0.56 | persistent_phantom_value_no_recovery (no recovery unlike trained) |
| exp_hopper_frozen_s1 | DONE | killed | N/A | Killed after 2.4 min |
| exp_hopper_no_dt_emb_s0 | DONE | success | 10.76 | gate itself causes delay (11.2% baseline), not dt_emb |

agentId: a687c872e3ff35f87 (use SendMessage with to: 'a687c872e3ff35f87' to continue this agent)
&lt;usage>total_tokens: 32721
tool_uses: 5
duration_ms: 98781&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "55c99a2a-9c6f-473d-8ee6-03b272417082",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to extract all hopper-related experiments from a large JSON registry file. The file is at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/dc9c08e0-b484-4d3e-9885-54285bc08ddf/tool-results/mcp-agent-ml-research-read_registry-1780043142295.txt\n\nThis is JSON with schema: {result: string} — the `result` field is itself a JSON string that needs to be parsed.\n\nSteps:\n1. Probe the structure with jq (type/length/keys)\n2. Extract and search for any experiments whose id, name, notes, conclusion, or command contain \"hopper\" (case-insensitive)\n3. Also look for experiments with IDs matching exp_104 through exp_108\n\nFor each matching experiment, report:\n- exp_id\n- status (RUNNING/DONE/KILLED/FAILED etc.)\n- conclusion\n- notes\n- failure_reason (if any)\n- command (the training command used)\n- created_at / updated_at\n- Any other relevant fields\n\nReport ALL matching experiments verbatim — don't summarize away details.",
    "agentId": "a687c872e3ff35f87",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are all 13 hopper-related experiments extracted verbatim from the registry.\n\n---\n\n## exp_104_hopper_baseline_s0\n- **status**: DONE\n- **conclusion**: killed\n- **created_at**: 2026-05-27T02:55:00.720Z\n- **updated_at**: 2026-05-27T03:03:15.605Z\n- **completed_at**: 2026-05-27T03:03:15.605Z\n- **hypothesis**: Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE < 1.5×). Source: C1/C2 third-environment verification (D160).\n- **retry_count**: 0\n- **command**: (none stored — no `spec` or `reproduce` block)\n- **failure_reason**: (none)\n- **metrics**: (none)\n\n---\n\n## exp_105_hopper_trained_s0\n- **status**: DONE\n- **conclusion**: killed\n- **created_at**: 2026-05-27T02:55:06.756Z\n- **updated_at**: 2026-05-27T03:03:20.261Z\n- **completed_at**: 2026-05-27T03:03:20.261Z\n- **hypothesis**: Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE > 1.5× after 35K steps), consistent with Walker (3/3) and Cheetah (3/4). Source: C2 third-environment verification (D160).\n- **retry_count**: 0\n- **command**: (none stored)\n- **failure_reason**: (none)\n- **metrics**: (none)\n\n---\n\n## exp_106_hopper_trained_s1\n- **status**: DONE\n- **conclusion**: killed\n- **created_at**: 2026-05-27T02:55:11.391Z\n- **updated_at**: 2026-05-27T03:03:24.020Z\n- **completed_at**: 2026-05-27T03:03:24.020Z\n- **hypothesis**: Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE > 1.5× after 35K steps), second seed for onset rate. Source: C2 third-environment verification (D160).\n- **retry_count**: 0\n- **command**: (none stored)\n- **failure_reason**: (none)\n- **metrics**: (none)\n\n---\n\n## exp_107_hopper_frozen_s0\n- **status**: DONE\n- **conclusion**: killed\n- **created_at**: 2026-05-27T02:55:18.139Z\n- **updated_at**: 2026-05-27T03:03:27.004Z\n- **completed_at**: 2026-05-27T03:03:27.004Z\n- **hypothesis**: Frozen dt_embedding in Hopper Hop will prevent CIVO onset (NVE < 1.5× throughout), confirming causal role of trained dt_emb as CIVO trigger. Source: C6 third-environment verification (D160).\n- **retry_count**: 0\n- **command**: (none stored)\n- **failure_reason**: (none)\n- **metrics**: (none)\n\n---\n\n## exp_108_hopper_frozen_s1\n- **status**: DONE\n- **conclusion**: killed\n- **created_at**: 2026-05-27T02:55:22.603Z\n- **updated_at**: 2026-05-27T03:03:32.297Z\n- **completed_at**: 2026-05-27T03:03:32.297Z\n- **hypothesis**: Frozen dt_embedding in Hopper Hop will prevent CIVO onset (NVE < 1.5× throughout), second seed for mitigation confirmation. Source: C6 third-environment verification (D160).\n- **retry_count**: 0\n- **command**: (none stored)\n- **failure_reason**: (none)\n- **metrics**: (none)\n\nNote: exp_104 through exp_108 were all killed ~8 minutes after creation with no metrics, commands, or specs recorded. These appear to be an early batch that was aborted and replaced by the longer-named experiments below.\n\n---\n\n## exp_hopper_baseline\n- **status**: DONE\n- **conclusion**: success\n- **created_at**: 2026-05-27T02:34:22.253Z\n- **updated_at**: 2026-05-27T06:24:27.230Z\n- **completed_at**: 2026-05-27T06:24:21.198Z\n- **hypothesis**: Hopper Hop baseline (dt=1, no gate) establishes reference performance for third-environment CIVO verification. Expect stable training without value overestimation (NVE < 1.5×). Source: C1/C2 third-environment verification (D160).\n- **plan_id**: plan_040\n- **server**: westd-51268, **gpu**: cuda:0, **account**: root\n- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 105000 --seed 0 --compile False --device cuda:0`\n- **pid**: 604350\n- **training_hours**: 2.88 (wall_clock_seconds: 12318.4, gpu_hours: 3.42)\n- **metrics**:\n  - step: 105000\n  - eval_return_final: 96.43\n  - ve_ratio_final: 0.559\n  - ve_ratio_peak: 3.48 (at step 65000)\n  - civo_alert: 0\n  - value_mean_final: 53.9\n  - target_mean_final: 54.2\n\n---\n\n## exp_hopper_trained_s0\n- **status**: DONE\n- **conclusion**: success\n- **created_at**: 2026-05-27T02:34:26.587Z\n- **updated_at**: 2026-05-27T08:08:33.860Z\n- **completed_at**: 2026-05-27T06:00:13.703Z\n- **hypothesis**: Trained dt_embedding with subsample (008d-equivalent) in Hopper Hop will trigger CIVO onset (NVE > 1.5× after 35K steps), consistent with Walker (3/3) and Cheetah (3/4). Source: C2 third-environment verification (D160).\n- **plan_id**: plan_040\n- **server**: westd-51268, **gpu**: cuda:1, **account**: root\n- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8`\n- **pid**: 604513\n- **wall_clock_seconds**: 10864.2, **gpu_hours**: 3.02\n- **metrics**:\n  - step: 105000\n  - eval_return_final: 3.26\n  - eval_return_peak: 8.01 (at step 85000)\n  - ve_ratio_final: 0.897\n  - civo_alert: 1\n  - nve_105K_vs_baseline: 1.6\n  - pattern: **severe_learning_delay**\n  - notes: \"no CIVO detected; gate+dt=2 causes learning delay in Hopper independent of dt_emb training\"\n  - value_mean_trajectory: [0.48, 1.29, 2.93]\n\n---\n\n## exp_hopper_trained_s0_ext\n- **status**: DONE\n- **conclusion**: negative\n- **created_at**: 2026-05-27T06:00:49.737Z\n- **updated_at**: 2026-05-27T08:07:16.279Z\n- **completed_at**: 2026-05-27T08:05:14.676Z\n- **parent**: exp_hopper_trained_s0\n- **hypothesis**: Continuing trained_s0 from 105K to 150K will confirm delayed CIVO: ve_ratio (0.897 at 105K, exponentially rising) will cross NVE>1.5 threshold by ~115-125K, upgrading from emerging to confirmed delayed CIVO.\n- **server**: westd-51268, **gpu**: cuda:1\n- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 150000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8`\n- **pid**: 614518\n- **wall_clock_seconds**: 6254.5, **gpu_hours**: 1.74\n- **metrics**:\n  - step: 168000, eval_step: 158000\n  - eval_return_final: 81.58 (recovered from 3.26 at 105K)\n  - eval_return_peak: 81.58\n  - ve_ratio_trajectory: {105K: 0.897, 118K: 0.376, 128K: 5.519, 138K: 0.37, 148K: 0.55, 158K: 0.439}\n  - civo_alert_105K: 1, civo_alert_final: 0\n  - pattern: **transient_instability_recovered**\n  - nve_105K_vs_baseline: 1.6\n- **checkpoint_path**: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_trained_s0/latest.pt\n\n---\n\n## exp_hopper_trained_s1\n- **status**: DONE\n- **conclusion**: killed\n- **created_at**: 2026-05-27T02:34:29.841Z\n- **updated_at**: 2026-05-27T08:08:35.045Z\n- **completed_at**: 2026-05-27T08:08:35.045Z\n- **hypothesis**: Trained dt_emb + subsample ON in Hopper Hop will reproduce CIVO (NVE > 1.5×) as observed in Walker (3/3) and Cheetah (3/4), confirming CIVO generalizes across multi-joint locomotion environments (seed 1 replication)\n- **plan_id**: plan_040\n- **command** (from spec): `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8`\n- **server**: westd-51268, **gpu**: cuda:1\n- **metrics**: (none — killed before completion)\n\n---\n\n## exp_hopper_frozen_s0\n- **status**: DONE\n- **conclusion**: success\n- **created_at**: 2026-05-27T02:34:34.615Z\n- **updated_at**: 2026-05-27T09:14:56.465Z\n- **completed_at**: 2026-05-27T08:57:25.460Z\n- **hypothesis**: Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5×), confirming trained dt_emb is the necessary condition for CIVO across a third multi-joint locomotion environment\n- **plan_id**: plan_040\n- **server**: westd-51268, **gpu**: cuda:0, **account**: root\n- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True`\n- **pid**: 612905\n- **training_hours**: 2.98 (reproduce), 2.95 (metrics)\n- **metrics**:\n  - step: 105000\n  - eval_return_final: 0\n  - eval_return_peak: 3.6 (at step 85000)\n  - ve_ratio_final: 4,335,664.3 (!)\n  - civo_alert: 1\n  - civo_alert_steps: [65000, 105000]\n  - value_mean_final: 4.337, target_mean_final: 4.389\n  - pattern: **degenerate_civo_near_zero_magnitude**\n  - notes: \"D155 criteria formally met @95K (ve=2.69, sustained 2 points) but eval_return=1.083 (1.1% baseline). 105K ve=4.3M is eval=0/epsilon artifact. Mechanistically distinct from Walker/Cheetah standard CIVO.\"\n- **checkpoint_path**: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_frozen_s0/latest.pt\n\n---\n\n## exp_hopper_frozen_s0_ext\n- **status**: DONE\n- **conclusion**: negative\n- **created_at**: 2026-05-27T09:14:24.513Z\n- **updated_at**: 2026-05-27T10:56:21.405Z\n- **completed_at**: 2026-05-27T10:56:21.405Z\n- **parent**: exp_hopper_frozen_s0\n- **plan_id**: D163\n- **hypothesis**: Extending frozen_s0 from 105K to 150K will show eval_return recovery (rising like trained_s0_ext: 3.26 to 81.58) with ve_ratio declining, confirming frozen_s0's 'degenerate CIVO' @95K is transient instability during severe learning delay, not true CIVO mechanism. Source: D163.\n- **server**: westd-51268, **gpu**: cuda:0\n- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s0 --steps 150000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True`\n- **pid**: 622633\n- **wall_clock_seconds**: 6021.3, **gpu_hours**: 1.67\n- **metrics**:\n  - step: 160000, eval_step: 152000\n  - eval_return_final: 0.5608 (no recovery)\n  - eval_return_105K: 0\n  - eval_return_peak: 1.534 (at step 112000)\n  - ve_ratio_trajectory: {105K: 4335664.27, 122K: 10.149, 132K: 955.034, 142K: 18.055, 152K: 15.08}\n  - value_mean_trajectory: {105K: 4.34, 122K: 7.18, 132K: 7.08, 142K: 7.62, 152K: 8.46}\n  - nve_peak: 7,756,535.1 (at step 105000)\n  - nve_35K: 2.75, nve_95K: 5.2\n  - pattern: **persistent_phantom_value_no_recovery**\n  - comparison_vs_trained_s0_ext: \"trained recovered (3.26 to 81.58), frozen did NOT (0 to 0.56). Fundamentally different failure mode.\"\n  - notes: \"eval_return stayed 0-1.5 throughout 105K-152K extension. value_mean grew 4.34 to 8.46 (phantom value). ve_ratio remained elevated 10-955x. No recovery pattern observed.\"\n- **checkpoint_path**: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_frozen_s0/latest.pt\n\n---\n\n## exp_hopper_frozen_s1\n- **status**: DONE\n- **conclusion**: killed\n- **created_at**: 2026-05-27T02:34:37.319Z\n- **updated_at**: 2026-05-27T10:47:34.515Z\n- **completed_at**: 2026-05-27T10:47:34.515Z\n- **hypothesis**: Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5×), confirming trained dt_emb is the necessary condition for CIVO across a third multi-joint locomotion environment (seed 1 replication)\n- **plan_id**: plan_040\n- **server**: westd-51268, **gpu**: cuda:0\n- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True`\n- **pid**: 626827\n- **wall_clock_seconds**: 141.0, **gpu_hours**: 0.04\n- **metrics**: (none — killed after ~2.4 minutes)\n\n---\n\n## exp_hopper_no_dt_emb_s0\n- **status**: DONE\n- **conclusion**: success\n- **created_at**: 2026-05-27T08:08:47.870Z\n- **updated_at**: 2026-05-27T11:17:21.884Z\n- **completed_at**: 2026-05-27T11:17:21.884Z\n- **parent**: exp_hopper_trained_s0\n- **hypothesis**: Removing dt_embedding entirely (dt_embed_dim=0) while keeping gate+dt=2+subsample ON will still show severe learning delay in Hopper, confirming gate mechanism itself (not dt_emb) is the root cause of Hopper's failure. Source: D162 diagnostic.\n- **server**: westd-51268, **gpu**: cuda:1\n- **command**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0`\n- **pid**: 619366\n- **wall_clock_seconds**: 11286.4, **gpu_hours**: 3.14\n- **metrics**:\n  - eval_return_final: 10.759 (11.2% of baseline)\n  - ve_ratio_peak_gte35k: 1.949\n  - nve_peak: 4.37\n  - nve_sustained_above_1_5: false\n  - value_mean_final: 2.32\n  - actor_entropy_final: -1.939\n- **checkpoint_path**: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_hopper_no_dt_emb_s0\n\n---\n\n## Summary of the 13 experiments\n\n| Experiment | Status | Conclusion | eval_return_final | Key Pattern |\n|---|---|---|---|---|\n| exp_104 through exp_108 (5 exps) | DONE | killed | N/A | Early batch, aborted ~8min after creation |\n| exp_hopper_baseline | DONE | success | 96.43 | Reference baseline, no CIVO |\n| exp_hopper_trained_s0 | DONE | success | 3.26 | severe_learning_delay (gate causes delay, not CIVO) |\n| exp_hopper_trained_s0_ext | DONE | negative | 81.58 | transient_instability_recovered (recovered after 150K) |\n| exp_hopper_trained_s1 | DONE | killed | N/A | Killed, no metrics |\n| exp_hopper_frozen_s0 | DONE | success | 0 | degenerate_civo_near_zero_magnitude (ve=4.3M artifact) |\n| exp_hopper_frozen_s0_ext | DONE | negative | 0.56 | persistent_phantom_value_no_recovery (no recovery unlike trained) |\n| exp_hopper_frozen_s1 | DONE | killed | N/A | Killed after 2.4 min |\n| exp_hopper_no_dt_emb_s0 | DONE | success | 10.76 | gate itself causes delay (11.2% baseline), not dt_emb |"
      }
    ],
    "totalDurationMs": 98781,
    "totalTokens": 32721,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9628,
      "cache_read_input_tokens": 17697,
      "output_tokens": 5395,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5395,
          "cache_read_input_tokens": 17697,
          "cache_creation_input_tokens": 9628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9628,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 5,
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

### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very complete picture. Let me also check the DMC environment's task parsing to understand the task string, and check the dmc_proprio config section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "48160170-a874-497f-8c11-5d307b89b2c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMeQ56rgtKttZ2qQ8wFYsT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6515,
      "cache_read_input_tokens": 29788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6515
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 53_

找到了完整的 hopper 实验历史。现在检查 DMC 环境代码确认 task string 和 dmc_proprio 配置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "2f45b23e-3180-46af-9e8b-ebcae3034c80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMeQ56rgtKttZ2qQ8wFYsT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6515,
      "cache_read_input_tokens": 29788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6515
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UmohfwFNK83rvdpoFa5fpd`</summary>

```json
{
  "server": "westd-51268",
  "command": "cat /root/autodl-tmp/event-gated-adaptive-horizon/envs/dmc.py",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "5db68403-ded9-4178-9ad7-f3cfccfccad0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMeQ56rgtKttZ2qQ8wFYsT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6515,
      "cache_read_input_tokens": 29788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6515
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-29T08:27:41.394Z_

<details><summary>↩ Tool result · `toolu_01UmohfwFNK83rvdpoFa5fpd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"import gym\\nimport numpy as np\\n\\n\\nclass DeepMindControl:\\n    metadata = {}\\n\\n    def __init__(self, name, action_repeat=1, size=(64, 64), camera=None, seed=0):\\n        domain, task = name.split(\\\"_\\\", 1)\\n        if domain == \\\"cup\\\":  # Only domain with multiple words.\\n            domain = \\\"ball_in_cup\\\"\\n        if isinstance(domain, str):\\n            from dm_control import suite\\n\\n            self._env = suite.load(\\n                domain,\\n                task,\\n                task_kwargs={\\\"random\\\": seed},\\n            )\\n        else:\\n            assert task is None\\n            self._env = domain()\\n        self._action_repeat = action_repeat\\n        self._size = size\\n        if camera is None:\\n            camera = dict(quadruped=2).get(domain, 0)\\n        self._camera = camera\\n        self.reward_range = [-np.inf, np.inf]\\n\\n    @property\\n    def observation_space(self):\\n        spaces = {}\\n        for key, value in self._env.observation_spec().items():\\n            if len(value.shape) == 0:\\n                shape = (1,)\\n            else:\\n                shape = value.shape\\n            spaces[key] = gym.spaces.Box(-np.inf, np.inf, shape, dtype=np.float32)\\n        spaces[\\\"image\\\"] = gym.spaces.Box(0, 255, self._size + (3,), dtype=np.uint8)\\n        return gym.spaces.Dict(spaces)\\n\\n    @property\\n    def action_space(self):\\n        spec = self._env.action_spec()\\n        return gym.spaces.Box(spec.minimum, spec.maximum, dtype=np.float32)\\n\\n    def step(self, action):\\n        assert np.isfinite(action).all(), action\\n        reward = 0\\n        for _ in range(self._action_repeat):\\n            time_step = self._env.step(action)\\n            reward += time_step.reward or 0\\n            if time_step.last():\\n                break\\n        obs = dict(time_step.observation)\\n        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}\\n        obs[\\\"image\\\"] = self.render()\\n        # There is no terminal state in DMC\\n        obs[\\\"is_terminal\\\"] = False if time_step.first() else time_step.discount == 0\\n        obs[\\\"is_first\\\"] = time_step.first()\\n        done = time_step.last()\\n        info = {\\\"discount\\\": np.array(time_step.discount, np.float32)}\\n        return obs, reward, done, info\\n\\n    def reset(self):\\n        time_step = self._env.reset()\\n        obs = dict(time_step.observation)\\n        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}\\n        obs[\\\"image\\\"] = self.render()\\n        obs[\\\"is_terminal\\\"] = False if time_step.first() else time_step.discount == 0\\n        obs[\\\"is_first\\\"] = time_step.first()\\n        return obs\\n\\n    def render(self, *args, **kwargs):\\n        if kwargs.get(\\\"mode\\\", \\\"rgb_array\\\") != \\\"rgb_array\\\":\\n            raise ValueError(\\\"Only render mode 'rgb_array' is supported.\\\")\\n        return self._env.physics.render(*self._size, camera_id=self._camera)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "01d41304-a66d-49ab-98f0-52044287af6e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"import gym\\\\nimport numpy as np\\\\n\\\\n\\\\nclass DeepMindControl:\\\\n    metadata = {}\\\\n\\\\n    def __init__(self, name, action_repeat=1, size=(64, 64), camera=None, seed=0):\\\\n        domain, task = name.split(\\\\\\\"_\\\\\\\", 1)\\\\n        if domain == \\\\\\\"cup\\\\\\\":  # Only domain with multiple words.\\\\n            domain = \\\\\\\"ball_in_cup\\\\\\\"\\\\n        if isinstance(domain, str):\\\\n            from dm_control import suite\\\\n\\\\n            self._env = suite.load(\\\\n                domain,\\\\n                task,\\\\n                task_kwargs={\\\\\\\"random\\\\\\\": seed},\\\\n            )\\\\n        else:\\\\n            assert task is None\\\\n            self._env = domain()\\\\n        self._action_repeat = action_repeat\\\\n        self._size = size\\\\n        if camera is None:\\\\n            camera = dict(quadruped=2).get(domain, 0)\\\\n        self._camera = camera\\\\n        self.reward_range = [-np.inf, np.inf]\\\\n\\\\n    @property\\\\n    def observation_space(self):\\\\n        spaces = {}\\\\n        for key, value in self._env.observation_spec().items():\\\\n            if len(value.shape) == 0:\\\\n                shape = (1,)\\\\n            else:\\\\n                shape = value.shape\\\\n            spaces[key] = gym.spaces.Box(-np.inf, np.inf, shape, dtype=np.float32)\\\\n        spaces[\\\\\\\"image\\\\\\\"] = gym.spaces.Box(0, 255, self._size + (3,), dtype=np.uint8)\\\\n        return gym.spaces.Dict(spaces)\\\\n\\\\n    @property\\\\n    def action_space(self):\\\\n        spec = self._env.action_spec()\\\\n        return gym.spaces.Box(spec.minimum, spec.maximum, dtype=np.float32)\\\\n\\\\n    def step(self, action):\\\\n        assert np.isfinite(action).all(), action\\\\n        reward = 0\\\\n        for _ in range(self._action_repeat):\\\\n            time_step = self._env.step(action)\\\\n            reward += time_step.reward or 0\\\\n            if time_step.last():\\\\n                break\\\\n        obs = dict(time_step.observation)\\\\n        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}\\\\n        obs[\\\\\\\"image\\\\\\\"] = self.render()\\\\n        # There is no terminal state in DMC\\\\n        obs[\\\\\\\"is_terminal\\\\\\\"] = False if time_step.first() else time_step.discount == 0\\\\n        obs[\\\\\\\"is_first\\\\\\\"] = time_step.first()\\\\n        done = time_step.last()\\\\n        info = {\\\\\\\"discount\\\\\\\": np.array(time_step.discount, np.float32)}\\\\n        return obs, reward, done, info\\\\n\\\\n    def reset(self):\\\\n        time_step = self._env.reset()\\\\n        obs = dict(time_step.observation)\\\\n        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}\\\\n        obs[\\\\\\\"image\\\\\\\"] = self.render()\\\\n        obs[\\\\\\\"is_terminal\\\\\\\"] = False if time_step.first() else time_step.discount == 0\\\\n        obs[\\\\\\\"is_first\\\\\\\"] = time_step.first()\\\\n        return obs\\\\n\\\\n    def render(self, *args, **kwargs):\\\\n        if kwargs.get(\\\\\\\"mode\\\\\\\", \\\\\\\"rgb_array\\\\\\\") != \\\\\\\"rgb_array\\\\\\\":\\\\n            raise ValueError(\\\\\\\"Only render mode 'rgb_array' is supported.\\\\\\\")\\\\n        return self._env.physics.render(*self._size, camera_id=self._camera)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"import gym\\nimport numpy as np\\n\\n\\nclass DeepMindControl:\\n    metadata = {}\\n\\n    def __init__(self, name, action_repeat=1, size=(64, 64), camera=None, seed=0):\\n        domain, task = name.split(\\\"_\\\", 1)\\n        if domain == \\\"cup\\\":  # Only domain with multiple words.\\n            domain = \\\"ball_in_cup\\\"\\n        if isinstance(domain, str):\\n            from dm_control import suite\\n\\n            self._env = suite.load(\\n                domain,\\n                task,\\n                task_kwargs={\\\"random\\\": seed},\\n            )\\n        else:\\n            assert task is None\\n            self._env = domain()\\n        self._action_repeat = action_repeat\\n        self._size = size\\n        if camera is None:\\n            camera = dict(quadruped=2).get(domain, 0)\\n        self._camera = camera\\n        self.reward_range = [-np.inf, np.inf]\\n\\n    @property\\n    def observation_space(self):\\n        spaces = {}\\n        for key, value in self._env.observation_spec().items():\\n            if len(value.shape) == 0:\\n                shape = (1,)\\n            else:\\n                shape = value.shape\\n            spaces[key] = gym.spaces.Box(-np.inf, np.inf, shape, dtype=np.float32)\\n        spaces[\\\"image\\\"] = gym.spaces.Box(0, 255, self._size + (3,), dtype=np.uint8)\\n        return gym.spaces.Dict(spaces)\\n\\n    @property\\n    def action_space(self):\\n        spec = self._env.action_spec()\\n        return gym.spaces.Box(spec.minimum, spec.maximum, dtype=np.float32)\\n\\n    def step(self, action):\\n        assert np.isfinite(action).all(), action\\n        reward = 0\\n        for _ in range(self._action_repeat):\\n            time_step = self._env.step(action)\\n            reward += time_step.reward or 0\\n            if time_step.last():\\n                break\\n        obs = dict(time_step.observation)\\n        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}\\n        obs[\\\"image\\\"] = self.render()\\n        # There is no terminal state in DMC\\n        obs[\\\"is_terminal\\\"] = False if time_step.first() else time_step.discount == 0\\n        obs[\\\"is_first\\\"] = time_step.first()\\n        done = time_step.last()\\n        info = {\\\"discount\\\": np.array(time_step.discount, np.float32)}\\n        return obs, reward, done, info\\n\\n    def reset(self):\\n        time_step = self._env.reset()\\n        obs = dict(time_step.observation)\\n        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}\\n        obs[\\\"image\\\"] = self.render()\\n        obs[\\\"is_terminal\\\"] = False if time_step.first() else time_step.discount == 0\\n        obs[\\\"is_first\\\"] = time_step.first()\\n        return obs\\n\\n    def render(self, *args, **kwargs):\\n        if kwargs.get(\\\"mode\\\", \\\"rgb_array\\\") != \\\"rgb_array\\\":\\n            raise ValueError(\\\"Only render mode 'rgb_array' is supported.\\\")\\n        return self._env.physics.render(*self._size, camera_id=self._camera)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QPY3YzGH3WNWuzqqveQ6KS`</summary>

```json
{
  "server": "westd-51268",
  "command": "grep -A 20 \"dmc_proprio:\" /root/autodl-tmp/event-gated-adaptive-horizon/configs.yaml",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "75f6d33d-0aca-4293-8d85-06ee451a0d8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMeQ56rgtKttZ2qQ8wFYsT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6515,
      "cache_read_input_tokens": 29788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6515
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-29T08:27:42.344Z_

<details><summary>↩ Tool result · `toolu_01QPY3YzGH3WNWuzqqveQ6KS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"dmc_proprio:\\n  steps: 5e5\\n  action_repeat: 2\\n  envs: 4\\n  train_ratio: 512\\n  video_pred_log: false\\n  encoder: {mlp_keys: '.*', cnn_keys: '$^'}\\n  decoder: {mlp_keys: '.*', cnn_keys: '$^'}\\n\\ndmc_vision:\\n  steps: 1e6\\n  action_repeat: 2\\n  envs: 4\\n  train_ratio: 512\\n  video_pred_log: true\\n  encoder: {mlp_keys: '$^', cnn_keys: 'image'}\\n  decoder: {mlp_keys: '$^', cnn_keys: 'image'}\\n\\ncrafter:\\n  task: crafter_reward\\n  step: 1e6\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "152a239b-fd0f-4f35-99ba-46f4a24545c8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"dmc_proprio:\\\\n  steps: 5e5\\\\n  action_repeat: 2\\\\n  envs: 4\\\\n  train_ratio: 512\\\\n  video_pred_log: false\\\\n  encoder: {mlp_keys: '.*', cnn_keys: '$^'}\\\\n  decoder: {mlp_keys: '.*', cnn_keys: '$^'}\\\\n\\\\ndmc_vision:\\\\n  steps: 1e6\\\\n  action_repeat: 2\\\\n  envs: 4\\\\n  train_ratio: 512\\\\n  video_pred_log: true\\\\n  encoder: {mlp_keys: '$^', cnn_keys: 'image'}\\\\n  decoder: {mlp_keys: '$^', cnn_keys: 'image'}\\\\n\\\\ncrafter:\\\\n  task: crafter_reward\\\\n  step: 1e6\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"dmc_proprio:\\n  steps: 5e5\\n  action_repeat: 2\\n  envs: 4\\n  train_ratio: 512\\n  video_pred_log: false\\n  encoder: {mlp_keys: '.*', cnn_keys: '$^'}\\n  decoder: {mlp_keys: '.*', cnn_keys: '$^'}\\n\\ndmc_vision:\\n  steps: 1e6\\n  action_repeat: 2\\n  envs: 4\\n  train_ratio: 512\\n  video_pred_log: true\\n  encoder: {mlp_keys: '$^', cnn_keys: 'image'}\\n  decoder: {mlp_keys: '$^', cnn_keys: 'image'}\\n\\ncrafter:\\n  task: crafter_reward\\n  step: 1e6\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KjFNAWxKVEYMgAsNaYPxoJ`</summary>

```json
{
  "server": "westd-51268",
  "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/logdir/",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "269f211c-1f7e-4c13-bd58-e06ae0d81c37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMeQ56rgtKttZ2qQ8wFYsT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6515,
      "cache_read_input_tokens": 29788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6515
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-29T08:27:42.984Z_

<details><summary>↩ Tool result · `toolu_01KjFNAWxKVEYMgAsNaYPxoJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis_actor_entropy_value_calibration.json\\nanalysis_rssm_prediction_quality.json\\nanalysis_rssm_prediction_quality.py\\nanalysis_rssm_standardized_cheetah.json\\nanalysis_rssm_standardized_walker.json\\nanalysis_rssm_walker_fidelity.json\\ncross_env_output\\ndt_emb_cosine_current.json\\nexp_008d_civo_trigger_s4\\nexp_009c_no_dt_emb_s2\\nexp_009d_baseline_walker_s1\\nexp_063_rssm_fidelity\\nexp_064_value_distribution\\nexp_065_dt_emb_cosine\\nexp_066b_timeseries_rssm_fidelity_s1\\nexp_084_frozen_dt_emb_walker_s0\\nexp_092_cheetah_no_dt_emb_s1\\nexp_093_cheetah_no_dt_emb_s2\\nexp_097_cheetah_008d_s3\\nexp_100_walker_008a_s1\\nexp_cheetah_008a_s0\\nexp_cheetah_008a_s1\\nexp_cheetah_008a_s2\\nexp_cheetah_008a_s3\\nexp_hopper_baseline\\nexp_hopper_frozen_s0\\nexp_hopper_frozen_s1\\nexp_hopper_no_dt_emb_s0\\nexp_hopper_trained_s0\\nexp_humanoid_baseline_s0\\nexp_quadruped_baseline_s0\\nexp_quadruped_baseline_s0_r2\\nexp_walker_008f_s0\\nexp_walker_no_dt_emb_s0\\nexp_walker_no_dt_emb_s1\\nexp_walker_no_dt_emb_s1.log\\nextract_table5_data.py\\npaper_data_walker_walk.json\\npaper_figure_data.json\\npaper_figure_data_compact.json\\nrssm_v3_cheetah_no_dt_emb.json\\nrssm_v3_cheetah_standardized_gpu.json\\nrssm_v3_cheetah_trained_dt_emb.json\\nrssm_v3_cheetah_trained_dt_emb_gpu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "81dbd025-7333-4076-a679-f761ff2f86ed",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"analysis_actor_entropy_value_calibration.json\\\\nanalysis_rssm_prediction_quality.json\\\\nanalysis_rssm_prediction_quality.py\\\\nanalysis_rssm_standardized_cheetah.json\\\\nanalysis_rssm_standardized_walker.json\\\\nanalysis_rssm_walker_fidelity.json\\\\ncross_env_output\\\\ndt_emb_cosine_current.json\\\\nexp_008d_civo_trigger_s4\\\\nexp_009c_no_dt_emb_s2\\\\nexp_009d_baseline_walker_s1\\\\nexp_063_rssm_fidelity\\\\nexp_064_value_distribution\\\\nexp_065_dt_emb_cosine\\\\nexp_066b_timeseries_rssm_fidelity_s1\\\\nexp_084_frozen_dt_emb_walker_s0\\\\nexp_092_cheetah_no_dt_emb_s1\\\\nexp_093_cheetah_no_dt_emb_s2\\\\nexp_097_cheetah_008d_s3\\\\nexp_100_walker_008a_s1\\\\nexp_cheetah_008a_s0\\\\nexp_cheetah_008a_s1\\\\nexp_cheetah_008a_s2\\\\nexp_cheetah_008a_s3\\\\nexp_hopper_baseline\\\\nexp_hopper_frozen_s0\\\\nexp_hopper_frozen_s1\\\\nexp_hopper_no_dt_emb_s0\\\\nexp_hopper_trained_s0\\\\nexp_humanoid_baseline_s0\\\\nexp_quadruped_baseline_s0\\\\nexp_quadruped_baseline_s0_r2\\\\nexp_walker_008f_s0\\\\nexp_walker_no_dt_emb_s0\\\\nexp_walker_no_dt_emb_s1\\\\nexp_walker_no_dt_emb_s1.log\\\\nextract_table5_data.py\\\\npaper_data_walker_walk.json\\\\npaper_figure_data.json\\\\npaper_figure_data_compact.json\\\\nrssm_v3_cheetah_no_dt_emb.json\\\\nrssm_v3_cheetah_standardized_gpu.json\\\\nrssm_v3_cheetah_trained_dt_emb.json\\\\nrssm_v3_cheetah_trained_dt_emb_gpu.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"analysis_actor_entropy_value_calibration.json\\nanalysis_rssm_prediction_quality.json\\nanalysis_rssm_prediction_quality.py\\nanalysis_rssm_standardized_cheetah.json\\nanalysis_rssm_standardized_walker.json\\nanalysis_rssm_walker_fidelity.json\\ncross_env_output\\ndt_emb_cosine_current.json\\nexp_008d_civo_trigger_s4\\nexp_009c_no_dt_emb_s2\\nexp_009d_baseline_walker_s1\\nexp_063_rssm_fidelity\\nexp_064_value_distribution\\nexp_065_dt_emb_cosine\\nexp_066b_timeseries_rssm_fidelity_s1\\nexp_084_frozen_dt_emb_walker_s0\\nexp_092_cheetah_no_dt_emb_s1\\nexp_093_cheetah_no_dt_emb_s2\\nexp_097_cheetah_008d_s3\\nexp_100_walker_008a_s1\\nexp_cheetah_008a_s0\\nexp_cheetah_008a_s1\\nexp_cheetah_008a_s2\\nexp_cheetah_008a_s3\\nexp_hopper_baseline\\nexp_hopper_frozen_s0\\nexp_hopper_frozen_s1\\nexp_hopper_no_dt_emb_s0\\nexp_hopper_trained_s0\\nexp_humanoid_baseline_s0\\nexp_quadruped_baseline_s0\\nexp_quadruped_baseline_s0_r2\\nexp_walker_008f_s0\\nexp_walker_no_dt_emb_s0\\nexp_walker_no_dt_emb_s1\\nexp_walker_no_dt_emb_s1.log\\nextract_table5_data.py\\npaper_data_walker_walk.json\\npaper_figure_data.json\\npaper_figure_data_compact.json\\nrssm_v3_cheetah_no_dt_emb.json\\nrssm_v3_cheetah_standardized_gpu.json\\nrssm_v3_cheetah_trained_dt_emb.json\\nrssm_v3_cheetah_trained_dt_emb_gpu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the report.

Key findings:

1. **Hopper code support**: YES. The DMC wrapper in `envs/dmc.py` parses task string as `domain_task` by splitting on first `_`. So `dmc_hopper_hop` → domain="hopper", task="hop" in DreamerV3, then `suite.load("hopper", "hop")`. The `--configs defaults dmc_proprio` works fine as confirmed by previous experiments.

2. **Task string**: `dmc_hopper_hop` (confirmed from registry commands). 

Looking at the parsing logic more carefully, dreamer.py strips the "dmc_" prefix from the task string, leaving "hopper_hop", which then gets split on the first underscore to extract domain="hopper" and task="hop".

Now I'm checking what tasks are actually available in dm_control—the Hopper domain supports "stand" and "hop" tasks, not "walk", and the Hopper has 4 degrees of freedom across its torso and three leg joints.

I'm also noticing that experiments 104 through 108 were all terminated about 8 minutes after creation with no stored commands.

Looking at the experiment results, the baseline without gating achieved an eval return of 96.43 with stable value estimation, but adding the gate with a 2-step delay severely hampered learning initially (eval return of 3.26 at 105K steps), though it recovered to 81.58 when extended to 150K. The frozen variant with gating and delay produced a degenerate CIVO artifact with zero eval return that never recovered even with extension, while removing the embedding dimension entirely yielded an eval return of 10.76.

The key takeaway is that Hopper's learning dynamics differ from Walker and Cheetah—the gate mechanism itself introduces substantial learning delay that confounds the CIVO patterns, making it harder to isolate the actual CIVO effect. For the new baseline experiments, I need to use the existing baseline run (eval_return=96.43) as reference, account for roughly 3 hours of training time per 105K steps on a single GPU, and note that the DMC Hopper task doesn't require rendering during training since the physics engine handles that via software rendering.

Looking at the existing baseline data, the ve_ratio_peak reaches 3.48 at step 65K which is concerning, though it settles to 0.559 by the end, suggesting it's transient. The Director mentioned wanting Hopper Walk as a contingency for clean CIVO isolation, but dm_control's Hopper domain only has "stand" and "hop" tasks—there's no walk variant available. The existing experiments already used the hop task, and Hopper itself has 4 actuated joints, so I need to work within those constraints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "cc776d59-28e0-49d8-b29b-309b07e3298a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1Us9s1EaSbcC6ApzH7EMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2565,
      "cache_read_input_tokens": 36303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2565
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

_source line 61_

所有信息已收集完毕。现在写报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "660e81dc-9a85-4550-b49b-eb7825194229",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1Us9s1EaSbcC6ApzH7EMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2565,
      "cache_read_input_tokens": 36303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2565
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

_source line 62_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017rXBwTnewjDtVB2SKw2tHT`</summary>

```json
{
  "server": "westd-51268",
  "command": "python3 -c \"from dm_control import suite; print([t for t in suite.BENCHMARKING if t[0]=='hopper'])\"",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "20570eb7-8a55-48ad-8e1f-d88748980a38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1Us9s1EaSbcC6ApzH7EMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2565,
      "cache_read_input_tokens": 36303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2565
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-29T08:28:15.111Z_

<details><summary>↩ Tool result · `toolu_017rXBwTnewjDtVB2SKw2tHT`</summary>

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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "eb2dce3a-5a77-418b-82cd-fd62ec64c6be",
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

_source line 64_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Wsm5WtTgcLamdyRhA8iB5f`</summary>

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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "26c3b47f-e69b-4ecd-ab61-96a195731525",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwvF4nY5sChMLnr38MdpFj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1493,
      "cache_read_input_tokens": 38868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1493
      },
      "output_tokens": 60,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-29T08:28:17.793Z_

<details><summary>↩ Tool result · `toolu_01Wsm5WtTgcLamdyRhA8iB5f`</summary>

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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "9dcc2186-959c-49cc-a9ba-1e38f687d650",
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

_source line 66_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Sdd4mogGLXhKer3Bf7S7Wq`</summary>

```json
{
  "server": "westd-51268",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"from dm_control import suite; print([t for t in suite.BENCHMARKING if t[0]=='hopper'])\"",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "a85cfa65-2eb6-49b2-a4a2-99617abeb1aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwZ8rbCsDA21BGsdViiUkk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 40361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
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

_source line 67 · 2026-05-29T08:28:22.429Z_

<details><summary>↩ Tool result · `toolu_01Sdd4mogGLXhKer3Bf7S7Wq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[('hopper', 'stand'), ('hopper', 'hop')]\\n\", \"stderr\": \"/root/miniconda3/lib/python3.12/site-packages/glfw/__init__.py:917: GLFWError: (65550) b'X11: The DISPLAY environment variable is missing'\\n  warnings.warn(message, GLFWError)\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "5faebc25-d74d-44b7-8bfd-999e3d161e31",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[('hopper', 'stand'), ('hopper', 'hop')]\\\\n\\\", \\\"stderr\\\": \\\"/root/miniconda3/lib/python3.12/site-packages/glfw/__init__.py:917: GLFWError: (65550) b'X11: The DISPLAY environment variable is missing'\\\\n  warnings.warn(message, GLFWError)\\\\n\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[('hopper', 'stand'), ('hopper', 'hop')]\\n\", \"stderr\": \"/root/miniconda3/lib/python3.12/site-packages/glfw/__init__.py:917: GLFWError: (65550) b'X11: The DISPLAY environment variable is missing'\\n  warnings.warn(message, GLFWError)\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.37}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
DMC Hopper only has "stand" and "hop" tasks — no "walk". The previous experiments used "hop". The GLFW warning about DISPLAY is harmless for proprio mode (no rendering needed for training, only for evaluation rendering which uses dm_control's internal renderer).

Let me also check hopper's action space dimensionality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "f5c700d6-57bc-4a64-8147-f5255afbd902",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWp9rc5LMH23pjQqnMDZcx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 40807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01XKJVZd1HWLyQ88mLbp73oG`</summary>

```json
{
  "server": "westd-51268",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"from dm_control import suite; env=suite.load('hopper','hop'); print('action_dim:', env.action_spec().shape); print('obs:', {k: v.shape for k,v in env.observation_spec().items()})\"",
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "dcc9c373-0a76-43b3-a20a-e2d66757abc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWp9rc5LMH23pjQqnMDZcx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 40807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-29T08:28:29.023Z_

<details><summary>↩ Tool result · `toolu_01XKJVZd1HWLyQ88mLbp73oG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"action_dim: (4,)\\nobs: {'position': (6,), 'velocity': (7,), 'touch': (2,)}\\n\", \"stderr\": \"/root/miniconda3/lib/python3.12/site-packages/glfw/__init__.py:917: GLFWError: (65550) b'X11: The DISPLAY environment variable is missing'\\n  warnings.warn(message, GLFWError)\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "0a76d279-d2ce-420e-8b15-dbb40d8e86cd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"action_dim: (4,)\\\\nobs: {'position': (6,), 'velocity': (7,), 'touch': (2,)}\\\\n\\\", \\\"stderr\\\": \\\"/root/miniconda3/lib/python3.12/site-packages/glfw/__init__.py:917: GLFWError: (65550) b'X11: The DISPLAY environment variable is missing'\\\\n  warnings.warn(message, GLFWError)\\\\n\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"action_dim: (4,)\\nobs: {'position': (6,), 'velocity': (7,), 'touch': (2,)}\\n\", \"stderr\": \"/root/miniconda3/lib/python3.12/site-packages/glfw/__init__.py:917: GLFWError: (65550) b'X11: The DISPLAY environment variable is missing'\\n  warnings.warn(message, GLFWError)\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.36}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 71_

所有数据齐全。写报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "a7bcda3f-8b02-44e5-9d39-112690266725",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzXWWnAwzRGw6CSx2AmxAu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 41125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 450
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

_source line 72_

<details open><summary>🔧 Tool call — Write · `toolu_01A1EPvS4uku4rUXJdL23DX4`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/hopper_contingency_report.md",
  "content": "# Hopper Contingency 调研报告\n\n## 1. 环境可用性\n\n**可用：YES**\n\n- **正确 task string**: `dmc_hopper_hop`（DMC Hopper 只有 `stand` 和 `hop` 两个 task，无 `walk`）\n- **Action dim**: 4（torso + thigh + leg + foot）\n- **Obs dim**: position(6) + velocity(7) + touch(2) = 15 维 proprio\n- **Config**: `--configs defaults dmc_proprio` 完全支持，之前已多次成功运行\n- **EGL**: 不需要。`dmc_proprio` 模式用 MLP encoder，不渲染图像（GLFW warning 可忽略）\n\n## 2. 历史实验 Kill 原因汇总\n\n### exp_104 ~ exp_108（5 个）\n- **原因**: 设计问题。早期批次创建后 ~8 分钟即被 abort，无 command/metrics 记录。被 `exp_hopper_*` 长名系列替代。\n\n### exp_hopper_trained_s1\n- **原因**: 设计问题。s0 已完成且结论明确（severe_learning_delay → 非 CIVO），s1 复制无额外价值，被 kill 以释放 GPU。\n\n### exp_hopper_frozen_s1\n- **原因**: 设计问题。运行 2.4 分钟后 kill。frozen_s0 + ext 已显示 persistent_phantom_value，s1 不再需要。\n\n**结论：所有 kill 均为资源/设计决策，无技术障碍。代码完全可用。**\n\n## 3. 已有实验结果速览\n\n| 实验 | 条件 | eval_return | NVE pattern |\n|------|------|-------------|-------------|\n| exp_hopper_baseline | dt=1, no gate | **96.43** | 稳定 (ve_final=0.559) |\n| exp_hopper_trained_s0 | gate+dt=2, trained dt_emb | 3.26 → 81.58 (ext) | severe_learning_delay → recovered |\n| exp_hopper_frozen_s0 | gate+dt=2, frozen dt_emb | 0 → 0.56 (ext) | persistent_phantom_value, 未恢复 |\n| exp_hopper_no_dt_emb_s0 | gate+dt=2, no dt_emb | 10.76 (11.2%) | gate 本身导致 delay |\n\n### 关键发现\n- Hopper baseline **NVE 稳定** (ve_ratio_final=0.559, peak 3.48 transient)，适合做 clean baseline\n- 但 gate 机制在 Hopper 上引发 **severe learning delay**，而非 Walker/Cheetah 的标准 CIVO\n- trained vs frozen 差异：trained 最终恢复 (81.58)，frozen 始终无法恢复 (0.56)——模式与 Walker/Cheetah 不同\n\n## 4. 推荐实验命令\n\n### Baseline (dt=1, no gate)\n```bash\npython -u dreamer.py --configs defaults dmc_proprio \\\n  --task dmc_hopper_hop \\\n  --logdir logdir/exp_hopper_baseline_s0 \\\n  --steps 105000 --seed 0 \\\n  --compile False --device cuda:0\n```\n\n### 训练时长预估\n- 105K steps ≈ **2.9 小时**（单 GPU，参考 exp_hopper_baseline: 12318s）\n- 150K steps ≈ **4.6 小时**（参考 ext 实验: +6000s for 45K extra steps）\n\n## 5. 风险与注意事项\n\n1. **Hopper 不展示标准 CIVO**：gate 机制本身在 Hopper 上导致 severe learning delay，与 Walker/Cheetah 的 CIVO onset 机制不同。如果目标是 \"CIVO isolation baseline\"，Hopper baseline 的 NVE 确实干净 (< 1.5×)，但 gate 实验的 failure mode 是 learning delay 而非 value overestimation。\n2. **已有 baseline 数据**：`exp_hopper_baseline` 已完成且数据齐全 (eval_return=96.43)，如无需额外 seed 可直接复用。\n3. **logdir 已存在**：服务器上有 `exp_hopper_baseline`, `exp_hopper_trained_s0`, `exp_hopper_frozen_s0` 等 logdir，新实验需用不同名避免覆盖。\n4. **DMC Hopper 无 \"walk\" task**：只有 `stand` 和 `hop`，任务书中的 \"Hopper Walk\" 应更正为 **Hopper Hop**。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "e465d37a-774e-48b6-b720-cf2e555acd14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzXWWnAwzRGw6CSx2AmxAu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 41125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 450
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

_source line 73 · 2026-05-29T08:28:58.879Z_

<details><summary>↩ Tool result · `toolu_01A1EPvS4uku4rUXJdL23DX4`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/hopper_contingency_report.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "9f654e37-42b0-4ff8-b8e1-0597fe6eb692",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/hopper_contingency_report.md",
    "content": "# Hopper Contingency 调研报告\n\n## 1. 环境可用性\n\n**可用：YES**\n\n- **正确 task string**: `dmc_hopper_hop`（DMC Hopper 只有 `stand` 和 `hop` 两个 task，无 `walk`）\n- **Action dim**: 4（torso + thigh + leg + foot）\n- **Obs dim**: position(6) + velocity(7) + touch(2) = 15 维 proprio\n- **Config**: `--configs defaults dmc_proprio` 完全支持，之前已多次成功运行\n- **EGL**: 不需要。`dmc_proprio` 模式用 MLP encoder，不渲染图像（GLFW warning 可忽略）\n\n## 2. 历史实验 Kill 原因汇总\n\n### exp_104 ~ exp_108（5 个）\n- **原因**: 设计问题。早期批次创建后 ~8 分钟即被 abort，无 command/metrics 记录。被 `exp_hopper_*` 长名系列替代。\n\n### exp_hopper_trained_s1\n- **原因**: 设计问题。s0 已完成且结论明确（severe_learning_delay → 非 CIVO），s1 复制无额外价值，被 kill 以释放 GPU。\n\n### exp_hopper_frozen_s1\n- **原因**: 设计问题。运行 2.4 分钟后 kill。frozen_s0 + ext 已显示 persistent_phantom_value，s1 不再需要。\n\n**结论：所有 kill 均为资源/设计决策，无技术障碍。代码完全可用。**\n\n## 3. 已有实验结果速览\n\n| 实验 | 条件 | eval_return | NVE pattern |\n|------|------|-------------|-------------|\n| exp_hopper_baseline | dt=1, no gate | **96.43** | 稳定 (ve_final=0.559) |\n| exp_hopper_trained_s0 | gate+dt=2, trained dt_emb | 3.26 → 81.58 (ext) | severe_learning_delay → recovered |\n| exp_hopper_frozen_s0 | gate+dt=2, frozen dt_emb | 0 → 0.56 (ext) | persistent_phantom_value, 未恢复 |\n| exp_hopper_no_dt_emb_s0 | gate+dt=2, no dt_emb | 10.76 (11.2%) | gate 本身导致 delay |\n\n### 关键发现\n- Hopper baseline **NVE 稳定** (ve_ratio_final=0.559, peak 3.48 transient)，适合做 clean baseline\n- 但 gate 机制在 Hopper 上引发 **severe learning delay**，而非 Walker/Cheetah 的标准 CIVO\n- trained vs frozen 差异：trained 最终恢复 (81.58)，frozen 始终无法恢复 (0.56)——模式与 Walker/Cheetah 不同\n\n## 4. 推荐实验命令\n\n### Baseline (dt=1, no gate)\n```bash\npython -u dreamer.py --configs defaults dmc_proprio \\\n  --task dmc_hopper_hop \\\n  --logdir logdir/exp_hopper_baseline_s0 \\\n  --steps 105000 --seed 0 \\\n  --compile False --device cuda:0\n```\n\n### 训练时长预估\n- 105K steps ≈ **2.9 小时**（单 GPU，参考 exp_hopper_baseline: 12318s）\n- 150K steps ≈ **4.6 小时**（参考 ext 实验: +6000s for 45K extra steps）\n\n## 5. 风险与注意事项\n\n1. **Hopper 不展示标准 CIVO**：gate 机制本身在 Hopper 上导致 severe learning delay，与 Walker/Cheetah 的 CIVO onset 机制不同。如果目标是 \"CIVO isolation baseline\"，Hopper baseline 的 NVE 确实干净 (< 1.5×)，但 gate 实验的 failure mode 是 learning delay 而非 value overestimation。\n2. **已有 baseline 数据**：`exp_hopper_baseline` 已完成且数据齐全 (eval_return=96.43)，如无需额外 seed 可直接复用。\n3. **logdir 已存在**：服务器上有 `exp_hopper_baseline`, `exp_hopper_trained_s0`, `exp_hopper_frozen_s0` 等 logdir，新实验需用不同名避免覆盖。\n4. **DMC Hopper 无 \"walk\" task**：只有 `stand` 和 `hop`，任务书中的 \"Hopper Walk\" 应更正为 **Hopper Hop**。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01SYeKvxv13zhTgCc3apBCGa`</summary>

```json
{
  "name": "hopper_contingency_report",
  "type": "report",
  "description": "Hopper 环境可行性调研：代码支持确认、历史实验 kill 原因、baseline 命令、风险分析",
  "project": "event-gated-adaptive-horizon",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/hopper_contingency_report.md",
  "tags": [
    "hopper",
    "contingency",
    "feasibility"
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
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "d259ad76-cf39-42fe-8a2e-7c3f87b3e595",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoUirUJxvHYs8XdEbri9YP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1518,
      "cache_read_input_tokens": 41575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1518
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-29T08:29:03.854Z_

<details><summary>↩ Tool result · `toolu_01SYeKvxv13zhTgCc3apBCGa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260529_a461bf\", \"name\": \"hopper_contingency_report\", \"type\": \"report\", \"description\": \"Hopper 环境可行性调研：代码支持确认、历史实验 kill 原因、baseline 命令、风险分析\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/hopper_contingency_report.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-29T08:29:03.367528+00:00\", \"tags\": [\"hopper\", \"contingency\", \"feasibility\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "5ee907ea-7ece-4687-b43b-f44c0acc800a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260529_a461bf\\\", \\\"name\\\": \\\"hopper_contingency_report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Hopper 环境可行性调研：代码支持确认、历史实验 kill 原因、baseline 命令、风险分析\\\", \\\"path\\\": \\\"projects/event-gated-adaptive-horizon/artifacts/_project/report/hopper_contingency_report.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"event-gated-adaptive-horizon\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-29T08:29:03.367528+00:00\\\", \\\"tags\\\": [\\\"hopper\\\", \\\"contingency\\\", \\\"feasibility\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260529_a461bf\", \"name\": \"hopper_contingency_report\", \"type\": \"report\", \"description\": \"Hopper 环境可行性调研：代码支持确认、历史实验 kill 原因、baseline 命令、风险分析\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/hopper_contingency_report.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-29T08:29:03.367528+00:00\", \"tags\": [\"hopper\", \"contingency\", \"feasibility\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 76_

报告已产出并注册。核心结论：

1. **Hopper 代码完全可用**，task string 是 `dmc_hopper_hop`（注意：DMC 没有 "hopper_walk"，只有 stand 和 hop）
2. **历史 kill 全是设计决策**（批次替换/结论已出），无技术障碍
3. **已有完整 baseline 数据**可复用：`exp_hopper_baseline` eval_return=96.43, NVE 稳定
4. **关键风险**：Hopper + gate 的 failure mode 是 severe learning delay，不是标准 CIVO。如果目的是做 "clean CIVO isolation"，baseline NVE 确实干净，但 gate 实验不会复现 Walker/Cheetah 式的 value overestimation pattern。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "uuid": "d5e47384-cba3-410c-a896-30f44bc1e7f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SPXVsFuXLzcseWGQdcGWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 43093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 539
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

_source line 77_

报告已产出并注册。核心结论：

1. **Hopper 代码完全可用**，task string 是 `dmc_hopper_hop`（注意：DMC 没有 "hopper_walk"，只有 stand 和 hop）
2. **历史 kill 全是设计决策**（批次替换/结论已出），无技术障碍
3. **已有完整 baseline 数据**可复用：`exp_hopper_baseline` eval_return=96.43, NVE 稳定
4. **关键风险**：Hopper + gate 的 failure mode 是 severe learning delay，不是标准 CIVO。如果目的是做 "clean CIVO isolation"，baseline NVE 确实干净，但 gate 实验不会复现 Walker/Cheetah 式的 value overestimation pattern。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 272131,
  "duration_api_ms": 268514,
  "num_turns": 22,
  "stop_reason": "end_turn",
  "session_id": "dc9c08e0-b484-4d3e-9885-54285bc08ddf",
  "total_cost_usd": 0.9490935,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 32181,
    "cache_read_input_tokens": 400784,
    "output_tokens": 6412,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32181,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 236,
        "cache_read_input_tokens": 43093,
        "cache_creation_input_tokens": 539,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 539
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1609,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001694,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 24,
      "outputTokens": 13685,
      "cacheReadInputTokens": 466484,
      "cacheCreationInputTokens": 59506,
      "webSearchRequests": 0,
      "costUSD": 0.9473995,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ddd40998-4510-4917-b7b6-414f00e41405"
}
```

</details>

---
