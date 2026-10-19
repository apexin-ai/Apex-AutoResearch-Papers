# audit number consistency

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_audit_number_consistency_20260527T233920.log`
- **Structured JSON:** [`702d6946e61616a55420.json`](../../sessions/70/702d6946e61616a55420.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
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
  "uuid": "f633027e-ce03-4bb6-b29f-4276fde98316",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1779927600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "da922bd4-3703-4381-835a-5a78884added",
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to cross-check numerical consistency in their paper. I need to read the paper's tex files from the remote server and verify all key numbers match between tables, figures, and text references.

Let me start by reading the paper files from the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "41df2550-4ced-4a63-9d3f-0897ffe646b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBVe5TKfb4sp8yEhvy7RmY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12489,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12489
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

_source line 5_

I'll start by reading all the paper sections from the server to do the cross-check.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "ae33c8fa-cfa3-4937-ad7d-3bce6762fd3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBVe5TKfb4sp8yEhvy7RmY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12489,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12489
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012KkJeFniKE2KMw7zsCKXh4`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "14ae9521-4a2d-4762-8de3-723ac560b9f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBVe5TKfb4sp8yEhvy7RmY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12489,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12489
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

_source line 7 · 2026-05-27T23:39:34.001Z_

<details><summary>↩ Tool result · `toolu_012KkJeFniKE2KMw7zsCKXh4`</summary>

````text
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "72b54d8f-1f2d-4d72-906a-a0c718e87f46",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SKzHcpw4BTbFZdkJUzYZyh`</summary>

```json
{
  "server": "westd-45947",
  "command": "ls /root/colliforce-vla/paper/sections/",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "104a206c-750b-4f21-8e68-3406b392b047",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrwwaYqR7moJmLSQJaiTEe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 23940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 516
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

_source line 9 · 2026-05-27T23:39:38.212Z_

<details><summary>↩ Tool result · `toolu_01SKzHcpw4BTbFZdkJUzYZyh`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/colliforce-vla/paper/sections/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.29}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "7cdd70e0-ec09-44e5-bcf2-cbb4a38fd033",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/colliforce-vla/paper/sections/': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.29}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/colliforce-vla/paper/sections/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.29}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01ShmmqZPP9frJKRdFdtLeoT`</summary>

```json
{
  "server": "westd-45947",
  "command": "find /root/colliforce-vla/paper -name \"*.tex\" -type f",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "111a5581-f7e6-42b1-ad4c-37e99b38e57b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUPVACrhqi2XNmc5u5znwc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 24456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
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

_source line 11 · 2026-05-27T23:39:41.671Z_

<details><summary>↩ Tool result · `toolu_01ShmmqZPP9frJKRdFdtLeoT`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/colliforce-vla/paper': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "759fbb69-9f50-476c-868a-f288224d7262",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"find: '/root/colliforce-vla/paper': No such file or directory\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/colliforce-vla/paper': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VxBZDMKnBqy3b3PELBNx4F`</summary>

```json
{
  "server": "westd-45947",
  "command": "find /root/colliforce-vla -name \"*.tex\" -type f",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "11ab9023-1847-4b0b-99f3-9fd15493342b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rdz7vS3dXtPSHNULMscPpf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 221,
      "cache_read_input_tokens": 24679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 221
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

_source line 13 · 2026-05-27T23:39:44.920Z_

<details><summary>↩ Tool result · `toolu_01VxBZDMKnBqy3b3PELBNx4F`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/colliforce-vla/docs/paper/abstract.tex\\n/root/colliforce-vla/docs/paper/claim3.tex\\n/root/colliforce-vla/docs/paper/discussion.tex\\n/root/colliforce-vla/docs/paper/appendix.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "cd3a75ba-3205-4ae3-aa79-7c68643e013d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/colliforce-vla/docs/paper/abstract.tex\\\\n/root/colliforce-vla/docs/paper/claim3.tex\\\\n/root/colliforce-vla/docs/paper/discussion.tex\\\\n/root/colliforce-vla/docs/paper/appendix.tex\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/colliforce-vla/docs/paper/abstract.tex\\n/root/colliforce-vla/docs/paper/claim3.tex\\n/root/colliforce-vla/docs/paper/discussion.tex\\n/root/colliforce-vla/docs/paper/appendix.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KqUUmQcME1Giq3Xt9rsVGx`</summary>

```json
{
  "server": "westd-45947",
  "command": "find /root/colliforce-vla/docs/paper -type f",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "dab58a79-1ff0-4291-ab76-c82938dbe450",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzUNRw2WAvsVEWajjGJugV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 24900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
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

_source line 15 · 2026-05-27T23:39:48.113Z_

<details><summary>↩ Tool result · `toolu_01KqUUmQcME1Giq3Xt9rsVGx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/colliforce-vla/docs/paper/abstract.tex\\n/root/colliforce-vla/docs/paper/claim3.tex\\n/root/colliforce-vla/docs/paper/discussion.tex\\n/root/colliforce-vla/docs/paper/appendix.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "32f2d3bd-503a-400f-a18d-0f87fd5f3541",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/colliforce-vla/docs/paper/abstract.tex\\\\n/root/colliforce-vla/docs/paper/claim3.tex\\\\n/root/colliforce-vla/docs/paper/discussion.tex\\\\n/root/colliforce-vla/docs/paper/appendix.tex\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/colliforce-vla/docs/paper/abstract.tex\\n/root/colliforce-vla/docs/paper/claim3.tex\\n/root/colliforce-vla/docs/paper/discussion.tex\\n/root/colliforce-vla/docs/paper/appendix.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

论文在 `/root/colliforce-vla/docs/paper/`。让我读取所有4个文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "1584230d-be7e-4e3c-89aa-12ddef02b329",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pnqiPnhkgfsigdrMUgdyG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 25171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GcDx2V7Uo6pfSvs8QfZ2fW`</summary>

```json
{
  "server": "westd-45947",
  "command": "cat /root/colliforce-vla/docs/paper/abstract.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "e2e2dee2-a747-4ec2-a151-ca1775e7e63d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pnqiPnhkgfsigdrMUgdyG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 25171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 18 · 2026-05-27T23:39:51.950Z_

<details><summary>↩ Tool result · `toolu_01GcDx2V7Uo6pfSvs8QfZ2fW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\begin{abstract}\\nVision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.\\nOn SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\\\\% CAR while 99.6\\\\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\\\\,mm. The robot is frozen, not safe.\\nWe introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\\\\,mm threshold range.\\nWe further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\\\\sim}$28 percentage points). SDF supervision adds no significant benefit at $\\\\lambda \\\\leq 0.01$ ($p > 0.1$) and only a marginal signal at $\\\\lambda = 0.1$ ($p \\\\approx 0.071$, two-tailed permutation test).\\nDisplacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision cannot be credited with collision avoidance, nor expected to deliver it.\\n\\\\end{abstract}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "8a1a0e98-e2a0-4373-b831-133a1ef1e8c2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\begin{abstract}\\\\nVision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.\\\\nOn SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\\\\\\\\% CAR while 99.6\\\\\\\\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\\\\\\\\,mm. The robot is frozen, not safe.\\\\nWe introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\\\\\\\\,mm threshold range.\\\\nWe further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\\\\\\\\sim}$28 percentage points). SDF supervision adds no significant benefit at $\\\\\\\\lambda \\\\\\\\leq 0.01$ ($p > 0.1$) and only a marginal signal at $\\\\\\\\lambda = 0.1$ ($p \\\\\\\\approx 0.071$, two-tailed permutation test).\\\\nDisplacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision cannot be credited with collision avoidance, nor expected to deliver it.\\\\n\\\\\\\\end{abstract}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\begin{abstract}\\nVision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.\\nOn SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\\\\% CAR while 99.6\\\\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\\\\,mm. The robot is frozen, not safe.\\nWe introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\\\\,mm threshold range.\\nWe further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\\\\sim}$28 percentage points). SDF supervision adds no significant benefit at $\\\\lambda \\\\leq 0.01$ ($p > 0.1$) and only a marginal signal at $\\\\lambda = 0.1$ ($p \\\\approx 0.071$, two-tailed permutation test).\\nDisplacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision cannot be credited with collision avoidance, nor expected to deliver it.\\n\\\\end{abstract}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HxugSEmhmop5yggWkYJgmp`</summary>

```json
{
  "server": "westd-45947",
  "command": "cat /root/colliforce-vla/docs/paper/claim3.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "3e812dd1-58ea-4008-83b3-06a71e2fd888",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pnqiPnhkgfsigdrMUgdyG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 25171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 20 · 2026-05-27T23:39:52.930Z_

<details><summary>↩ Tool result · `toolu_01HxugSEmhmop5yggWkYJgmp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Avoidance Source Diagnosis}\\\\label{sec:avoidance_source}\\n\\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\\\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only, LoRA+SDF ($\\\\lambda = 0.005$), and LoRA+SDF ($\\\\lambda = 0.01$) on Pi0.5, all evaluated at the 30K-step checkpoint.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Avoidance source attribution on SafeLIBERO. SDF at $\\\\lambda \\\\leq 0.01$ adds no measurable CAR beyond LoRA-only ($p > 0.1$); $\\\\lambda = 0.1$ shows a marginal signal ($p \\\\approx 0.071$, two-tailed permutation test, $n{=}2$) that requires additional seeds. All fine-tuned models exhibit 0\\\\% frozen rate and displacement $>$\\\\,0.37\\\\,m.}\\n\\\\label{tab:avoidance_source}\\n\\\\vspace{2pt}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nMethod & Seeds & TSR (\\\\%) & CAR (\\\\%) & EE Disp (m) \\\\\\\\\\n\\\\midrule\\nPi0.5 baseline & 3 & 74.7\\\\,$\\\\pm$\\\\,1.5 & 26.8\\\\,$\\\\pm$\\\\,1.6 & 0.367 \\\\\\\\\\n\\\\midrule\\nLoRA-only (no SDF) & 3 & 49.7\\\\,$\\\\pm$\\\\,3.2 & 54.83\\\\,$\\\\pm$\\\\,2.25 & 0.391 \\\\\\\\\\nLoRA+SDF $\\\\lambda{=}0.005$ & 3 & 54.0\\\\,$\\\\pm$\\\\,3.0 & 54.5\\\\,$\\\\pm$\\\\,2.29 & 0.387 \\\\\\\\\\nLoRA+SDF $\\\\lambda{=}0.01$ & 3 & 53.8\\\\,$\\\\pm$\\\\,1.5 & 56.33\\\\,$\\\\pm$\\\\,1.61 & 0.389 \\\\\\\\\\nLoRA+SDF $\\\\lambda{=}0.1$\\\\textsuperscript{$\\\\dagger$} & 2 & 48.0\\\\,$\\\\pm$\\\\,1.4 & 58.25\\\\,$\\\\pm$\\\\,0.35 & 0.394 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\vspace{1pt}\\n{\\\\footnotesize \\\\textsuperscript{$\\\\dagger$}30K checkpoint, two of three seeds; third seed in progress.}\\n\\\\end{table}\\n\\nTable~\\\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\\\sim}$28 percentage points (26.8\\\\% $\\\\to$ 54.83\\\\%) with zero frozen episodes and displacement above 0.37\\\\,m, which confirms genuine avoidance. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.83\\\\%) is within 0.33\\\\,pp of $\\\\lambda = 0.005$ and statistically indistinguishable from $\\\\lambda = 0.01$ (56.33\\\\%, $p > 0.1$; Appendix~\\\\ref{sec:appendix_null}). A Phase~2 ablation ($\\\\lambda = 0$ after step 5K) yields CAR\\\\,=\\\\,57.5\\\\%\\\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}; SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\\\_pudding highest, bbq\\\\_sauce lowest; Figure~\\\\ref{fig:pertask_fingerprint}) and invariant to $\\\\lambda$ across a 20$\\\\times$ range; avoidance patterns reflect the demonstration distribution rather than geometric supervision.\\n\\n\\\\paragraph{CAR--TSR trade-off.}\\\\label{sec:tsr_collapse}\\nFine-tuning degrades TSR by ${\\\\sim}$21--25\\\\,pp (74.7\\\\% $\\\\to$ 49.7--54.0\\\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\\\,0.37\\\\,m displacement and 0\\\\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.57 (Appendix~\\\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\\n\\n\\\\paragraph{Dose-response at higher loss weights.}\\\\label{sec:lambda_high}\\nIncreasing $\\\\lambda$ by 20$\\\\times$ to 0.1 yields CAR\\\\,=\\\\,58.25\\\\%\\\\,$\\\\pm$\\\\,0.35 at the 30K checkpoint (two of three seeds), above the null distribution (mean 54.67\\\\%, $\\\\sigma = 2.04$; two-tailed permutation $p \\\\approx 0.071$)\\\\footnote{One-tailed permutation $p = 0.036$; we report the conservative two-tailed value in the main text. A directional prior is justified because the SDF loss is designed to \\\\emph{reduce} collisions.}. This departure is suggestive but inconclusive at $n = 2$. A stepwise ablation across six checkpoints (16K--28K) shows no sustained trend (mean 55.3\\\\%, within 0.3$\\\\sigma$ of the null; Appendix~\\\\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K is preserved across all other conditions (Figure~\\\\ref{fig:lambda_car}). The response is thus dose-dependent: SDF is fully redundant at $\\\\lambda \\\\leq 0.01$ ($p > 0.1$), with a marginal signal at $\\\\lambda = 0.1$ whose modest effect size (${\\\\sim}$3.6\\\\,pp) and limited sample preclude strong conclusions. Even at elevated $\\\\lambda$, avoidance patterns remain driven by demonstration distribution rather than geometric supervision.\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=0.85\\\\linewidth]{fig5_lambda_curve}\\n\\\\caption{Effect of SDF loss weight $\\\\lambda$ on CAR and TSR. $\\\\lambda = 0$: LoRA-only. Low $\\\\lambda$ ($\\\\leq 0.01$) remains within the null band; $\\\\lambda = 0.1$ (58.25\\\\%, 2 seeds) shows a marginal departure ($p \\\\approx 0.071$, two-tailed permutation test) whose per-task pattern still matches the demonstration distribution.}\\n\\\\label{fig:lambda_car}\\n\\\\end{figure}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "8dfd5526-01cd-4bf0-bca7-df8cc9d8932f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Avoidance Source Diagnosis}\\\\\\\\label{sec:avoidance_source}\\\\n\\\\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\\\\\\\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only, LoRA+SDF ($\\\\\\\\lambda = 0.005$), and LoRA+SDF ($\\\\\\\\lambda = 0.01$) on Pi0.5, all evaluated at the 30K-step checkpoint.\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Avoidance source attribution on SafeLIBERO. SDF at $\\\\\\\\lambda \\\\\\\\leq 0.01$ adds no measurable CAR beyond LoRA-only ($p > 0.1$); $\\\\\\\\lambda = 0.1$ shows a marginal signal ($p \\\\\\\\approx 0.071$, two-tailed permutation test, $n{=}2$) that requires additional seeds. All fine-tuned models exhibit 0\\\\\\\\% frozen rate and displacement $>$\\\\\\\\,0.37\\\\\\\\,m.}\\\\n\\\\\\\\label{tab:avoidance_source}\\\\n\\\\\\\\vspace{2pt}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lcccc}\\\\n\\\\\\\\toprule\\\\nMethod & Seeds & TSR (\\\\\\\\%) & CAR (\\\\\\\\%) & EE Disp (m) \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nPi0.5 baseline & 3 & 74.7\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,1.5 & 26.8\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,1.6 & 0.367 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nLoRA-only (no SDF) & 3 & 49.7\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,3.2 & 54.83\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,2.25 & 0.391 \\\\\\\\\\\\\\\\\\\\nLoRA+SDF $\\\\\\\\lambda{=}0.005$ & 3 & 54.0\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,3.0 & 54.5\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,2.29 & 0.387 \\\\\\\\\\\\\\\\\\\\nLoRA+SDF $\\\\\\\\lambda{=}0.01$ & 3 & 53.8\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,1.5 & 56.33\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,1.61 & 0.389 \\\\\\\\\\\\\\\\\\\\nLoRA+SDF $\\\\\\\\lambda{=}0.1$\\\\\\\\textsuperscript{$\\\\\\\\dagger$} & 2 & 48.0\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,1.4 & 58.25\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,0.35 & 0.394 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\vspace{1pt}\\\\n{\\\\\\\\footnotesize \\\\\\\\textsuperscript{$\\\\\\\\dagger$}30K checkpoint, two of three seeds; third seed in progress.}\\\\n\\\\\\\\end{table}\\\\n\\\\nTable~\\\\\\\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\\\\\\\sim}$28 percentage points (26.8\\\\\\\\% $\\\\\\\\to$ 54.83\\\\\\\\%) with zero frozen episodes and displacement above 0.37\\\\\\\\,m, which confirms genuine avoidance. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.83\\\\\\\\%) is within 0.33\\\\\\\\,pp of $\\\\\\\\lambda = 0.005$ and statistically indistinguishable from $\\\\\\\\lambda = 0.01$ (56.33\\\\\\\\%, $p > 0.1$; Appendix~\\\\\\\\ref{sec:appendix_null}). A Phase~2 ablation ($\\\\\\\\lambda = 0$ after step 5K) yields CAR\\\\\\\\,=\\\\\\\\,57.5\\\\\\\\%\\\\\\\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}; SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\\\\\\\_pudding highest, bbq\\\\\\\\_sauce lowest; Figure~\\\\\\\\ref{fig:pertask_fingerprint}) and invariant to $\\\\\\\\lambda$ across a 20$\\\\\\\\times$ range; avoidance patterns reflect the demonstration distribution rather than geometric supervision.\\\\n\\\\n\\\\\\\\paragraph{CAR--TSR trade-off.}\\\\\\\\label{sec:tsr_collapse}\\\\nFine-tuning degrades TSR by ${\\\\\\\\sim}$21--25\\\\\\\\,pp (74.7\\\\\\\\% $\\\\\\\\to$ 49.7--54.0\\\\\\\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\\\\\\\,0.37\\\\\\\\,m displacement and 0\\\\\\\\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.57 (Appendix~\\\\\\\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\\\\n\\\\n\\\\\\\\paragraph{Dose-response at higher loss weights.}\\\\\\\\label{sec:lambda_high}\\\\nIncreasing $\\\\\\\\lambda$ by 20$\\\\\\\\times$ to 0.1 yields CAR\\\\\\\\,=\\\\\\\\,58.25\\\\\\\\%\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,0.35 at the 30K checkpoint (two of three seeds), above the null distribution (mean 54.67\\\\\\\\%, $\\\\\\\\sigma = 2.04$; two-tailed permutation $p \\\\\\\\approx 0.071$)\\\\\\\\footnote{One-tailed permutation $p = 0.036$; we report the conservative two-tailed value in the main text. A directional prior is justified because the SDF loss is designed to \\\\\\\\emph{reduce} collisions.}. This departure is suggestive but inconclusive at $n = 2$. A stepwise ablation across six checkpoints (16K--28K) shows no sustained trend (mean 55.3\\\\\\\\%, within 0.3$\\\\\\\\sigma$ of the null; Appendix~\\\\\\\\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K is preserved across all other conditions (Figure~\\\\\\\\ref{fig:lambda_car}). The response is thus dose-dependent: SDF is fully redundant at $\\\\\\\\lambda \\\\\\\\leq 0.01$ ($p > 0.1$), with a marginal signal at $\\\\\\\\lambda = 0.1$ whose modest effect size (${\\\\\\\\sim}$3.6\\\\\\\\,pp) and limited sample preclude strong conclusions. Even at elevated $\\\\\\\\lambda$, avoidance patterns remain driven by demonstration distribution rather than geometric supervision.\\\\n\\\\n\\\\\\\\begin{figure}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\includegraphics[width=0.85\\\\\\\\linewidth]{fig5_lambda_curve}\\\\n\\\\\\\\caption{Effect of SDF loss weight $\\\\\\\\lambda$ on CAR and TSR. $\\\\\\\\lambda = 0$: LoRA-only. Low $\\\\\\\\lambda$ ($\\\\\\\\leq 0.01$) remains within the null band; $\\\\\\\\lambda = 0.1$ (58.25\\\\\\\\%, 2 seeds) shows a marginal departure ($p \\\\\\\\approx 0.071$, two-tailed permutation test) whose per-task pattern still matches the demonstration distribution.}\\\\n\\\\\\\\label{fig:lambda_car}\\\\n\\\\\\\\end{figure}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Avoidance Source Diagnosis}\\\\label{sec:avoidance_source}\\n\\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\\\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only, LoRA+SDF ($\\\\lambda = 0.005$), and LoRA+SDF ($\\\\lambda = 0.01$) on Pi0.5, all evaluated at the 30K-step checkpoint.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Avoidance source attribution on SafeLIBERO. SDF at $\\\\lambda \\\\leq 0.01$ adds no measurable CAR beyond LoRA-only ($p > 0.1$); $\\\\lambda = 0.1$ shows a marginal signal ($p \\\\approx 0.071$, two-tailed permutation test, $n{=}2$) that requires additional seeds. All fine-tuned models exhibit 0\\\\% frozen rate and displacement $>$\\\\,0.37\\\\,m.}\\n\\\\label{tab:avoidance_source}\\n\\\\vspace{2pt}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nMethod & Seeds & TSR (\\\\%) & CAR (\\\\%) & EE Disp (m) \\\\\\\\\\n\\\\midrule\\nPi0.5 baseline & 3 & 74.7\\\\,$\\\\pm$\\\\,1.5 & 26.8\\\\,$\\\\pm$\\\\,1.6 & 0.367 \\\\\\\\\\n\\\\midrule\\nLoRA-only (no SDF) & 3 & 49.7\\\\,$\\\\pm$\\\\,3.2 & 54.83\\\\,$\\\\pm$\\\\,2.25 & 0.391 \\\\\\\\\\nLoRA+SDF $\\\\lambda{=}0.005$ & 3 & 54.0\\\\,$\\\\pm$\\\\,3.0 & 54.5\\\\,$\\\\pm$\\\\,2.29 & 0.387 \\\\\\\\\\nLoRA+SDF $\\\\lambda{=}0.01$ & 3 & 53.8\\\\,$\\\\pm$\\\\,1.5 & 56.33\\\\,$\\\\pm$\\\\,1.61 & 0.389 \\\\\\\\\\nLoRA+SDF $\\\\lambda{=}0.1$\\\\textsuperscript{$\\\\dagger$} & 2 & 48.0\\\\,$\\\\pm$\\\\,1.4 & 58.25\\\\,$\\\\pm$\\\\,0.35 & 0.394 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\vspace{1pt}\\n{\\\\footnotesize \\\\textsuperscript{$\\\\dagger$}30K checkpoint, two of three seeds; third seed in progress.}\\n\\\\end{table}\\n\\nTable~\\\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\\\sim}$28 percentage points (26.8\\\\% $\\\\to$ 54.83\\\\%) with zero frozen episodes and displacement above 0.37\\\\,m, which confirms genuine avoidance. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.83\\\\%) is within 0.33\\\\,pp of $\\\\lambda = 0.005$ and statistically indistinguishable from $\\\\lambda = 0.01$ (56.33\\\\%, $p > 0.1$; Appendix~\\\\ref{sec:appendix_null}). A Phase~2 ablation ($\\\\lambda = 0$ after step 5K) yields CAR\\\\,=\\\\,57.5\\\\%\\\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}; SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\\\_pudding highest, bbq\\\\_sauce lowest; Figure~\\\\ref{fig:pertask_fingerprint}) and invariant to $\\\\lambda$ across a 20$\\\\times$ range; avoidance patterns reflect the demonstration distribution rather than geometric supervision.\\n\\n\\\\paragraph{CAR--TSR trade-off.}\\\\label{sec:tsr_collapse}\\nFine-tuning degrades TSR by ${\\\\sim}$21--25\\\\,pp (74.7\\\\% $\\\\to$ 49.7--54.0\\\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\\\,0.37\\\\,m displacement and 0\\\\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.57 (Appendix~\\\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\\n\\n\\\\paragraph{Dose-response at higher loss weights.}\\\\label{sec:lambda_high}\\nIncreasing $\\\\lambda$ by 20$\\\\times$ to 0.1 yields CAR\\\\,=\\\\,58.25\\\\%\\\\,$\\\\pm$\\\\,0.35 at the 30K checkpoint (two of three seeds), above the null distribution (mean 54.67\\\\%, $\\\\sigma = 2.04$; two-tailed permutation $p \\\\approx 0.071$)\\\\footnote{One-tailed permutation $p = 0.036$; we report the conservative two-tailed value in the main text. A directional prior is justified because the SDF loss is designed to \\\\emph{reduce} collisions.}. This departure is suggestive but inconclusive at $n = 2$. A stepwise ablation across six checkpoints (16K--28K) shows no sustained trend (mean 55.3\\\\%, within 0.3$\\\\sigma$ of the null; Appendix~\\\\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K is preserved across all other conditions (Figure~\\\\ref{fig:lambda_car}). The response is thus dose-dependent: SDF is fully redundant at $\\\\lambda \\\\leq 0.01$ ($p > 0.1$), with a marginal signal at $\\\\lambda = 0.1$ whose modest effect size (${\\\\sim}$3.6\\\\,pp) and limited sample preclude strong conclusions. Even at elevated $\\\\lambda$, avoidance patterns remain driven by demonstration distribution rather than geometric supervision.\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=0.85\\\\linewidth]{fig5_lambda_curve}\\n\\\\caption{Effect of SDF loss weight $\\\\lambda$ on CAR and TSR. $\\\\lambda = 0$: LoRA-only. Low $\\\\lambda$ ($\\\\leq 0.01$) remains within the null band; $\\\\lambda = 0.1$ (58.25\\\\%, 2 seeds) shows a marginal departure ($p \\\\approx 0.071$, two-tailed permutation test) whose per-task pattern still matches the demonstration distribution.}\\n\\\\label{fig:lambda_car}\\n\\\\end{figure}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VaGWBU3GgPHY47sN6aqpKP`</summary>

```json
{
  "server": "westd-45947",
  "command": "cat /root/colliforce-vla/docs/paper/discussion.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "32b82d09-465a-43b9-9f26-7efa7ac514bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pnqiPnhkgfsigdrMUgdyG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 25171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PTh2esivBi8V5QaLBhHQdv`</summary>

```json
{
  "server": "westd-45947",
  "command": "cat /root/colliforce-vla/docs/paper/appendix.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "b41169dc-da92-4e5b-aa7a-2e192b662c1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pnqiPnhkgfsigdrMUgdyG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 25171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 23 · 2026-05-27T23:39:53.866Z_

<details><summary>↩ Tool result · `toolu_01VaGWBU3GgPHY47sN6aqpKP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Discussion and Conclusion}\\\\label{sec:conclusion}\\n\\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\\\S\\\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\\\S\\\\ref{sec:ee_only}); and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains (\\\\S\\\\ref{sec:avoidance_source}).\\n\\n\\\\paragraph{Why EE-only SDF fails.}\\nTwo independent causes explain the null result. \\\\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\\\sim}$28\\\\,pp CAR gain arises entirely from this distributional shift, with per-task ordering invariant across all SDF conditions (\\\\S\\\\ref{sec:avoidance_source}). At low $\\\\lambda$, SDF is redundant; at $\\\\lambda = 0.1$, the marginal signal preserves the same demonstration-driven pattern. \\\\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\\\emph{reduces} CAR by 6--10\\\\,pp below unrefined baselines (\\\\S\\\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.\\n\\n\\\\paragraph{Implications for evaluation.}\\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\\\times$ parameter range (Pi0 Full-FT ${\\\\sim}$2.5B to Pi0+A1 ${\\\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\\n\\n\\\\paragraph{Limitations.}\\nOur evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\\\\approx}$0\\\\%); testing on an actively moving policy would better isolate the structural limitation. The $\\\\lambda = 0.1$ condition has $n = 2$ seeds; the marginal departure ($p \\\\approx 0.071$, two-tailed permutation test) is inconclusive. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\\\sim}$21--25\\\\,pp, yet SSR/TSR increases from 0.33 to 0.51--0.57 (Appendix~\\\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\\n\\n\\\\paragraph{Future work.}\\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\\n\\n\\\\paragraph{Broader impact.}\\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "b57d77e8-348a-462b-9d82-16b8cc25cfc1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Discussion and Conclusion}\\\\\\\\label{sec:conclusion}\\\\n\\\\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\\\\\\\S\\\\\\\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\\\\\\\S\\\\\\\\ref{sec:ee_only}); and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains (\\\\\\\\S\\\\\\\\ref{sec:avoidance_source}).\\\\n\\\\n\\\\\\\\paragraph{Why EE-only SDF fails.}\\\\nTwo independent causes explain the null result. \\\\\\\\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\\\\\\\sim}$28\\\\\\\\,pp CAR gain arises entirely from this distributional shift, with per-task ordering invariant across all SDF conditions (\\\\\\\\S\\\\\\\\ref{sec:avoidance_source}). At low $\\\\\\\\lambda$, SDF is redundant; at $\\\\\\\\lambda = 0.1$, the marginal signal preserves the same demonstration-driven pattern. \\\\\\\\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\\\\\\\emph{reduces} CAR by 6--10\\\\\\\\,pp below unrefined baselines (\\\\\\\\S\\\\\\\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.\\\\n\\\\n\\\\\\\\paragraph{Implications for evaluation.}\\\\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\\\\\\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\\\\\\\times$ parameter range (Pi0 Full-FT ${\\\\\\\\sim}$2.5B to Pi0+A1 ${\\\\\\\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\\\\n\\\\n\\\\\\\\paragraph{Limitations.}\\\\nOur evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\\\\\\\\approx}$0\\\\\\\\%); testing on an actively moving policy would better isolate the structural limitation. The $\\\\\\\\lambda = 0.1$ condition has $n = 2$ seeds; the marginal departure ($p \\\\\\\\approx 0.071$, two-tailed permutation test) is inconclusive. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\\\\\\\sim}$21--25\\\\\\\\,pp, yet SSR/TSR increases from 0.33 to 0.51--0.57 (Appendix~\\\\\\\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\\\\n\\\\n\\\\\\\\paragraph{Future work.}\\\\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\\\\n\\\\n\\\\\\\\paragraph{Broader impact.}\\\\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Discussion and Conclusion}\\\\label{sec:conclusion}\\n\\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\\\S\\\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\\\S\\\\ref{sec:ee_only}); and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains (\\\\S\\\\ref{sec:avoidance_source}).\\n\\n\\\\paragraph{Why EE-only SDF fails.}\\nTwo independent causes explain the null result. \\\\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\\\sim}$28\\\\,pp CAR gain arises entirely from this distributional shift, with per-task ordering invariant across all SDF conditions (\\\\S\\\\ref{sec:avoidance_source}). At low $\\\\lambda$, SDF is redundant; at $\\\\lambda = 0.1$, the marginal signal preserves the same demonstration-driven pattern. \\\\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\\\emph{reduces} CAR by 6--10\\\\,pp below unrefined baselines (\\\\S\\\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.\\n\\n\\\\paragraph{Implications for evaluation.}\\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\\\times$ parameter range (Pi0 Full-FT ${\\\\sim}$2.5B to Pi0+A1 ${\\\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\\n\\n\\\\paragraph{Limitations.}\\nOur evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\\\\approx}$0\\\\%); testing on an actively moving policy would better isolate the structural limitation. The $\\\\lambda = 0.1$ condition has $n = 2$ seeds; the marginal departure ($p \\\\approx 0.071$, two-tailed permutation test) is inconclusive. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\\\sim}$21--25\\\\,pp, yet SSR/TSR increases from 0.33 to 0.51--0.57 (Appendix~\\\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\\n\\n\\\\paragraph{Future work.}\\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\\n\\n\\\\paragraph{Broader impact.}\\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-27T23:39:54.460Z_

<details><summary>↩ Tool result · `toolu_01PTh2esivBi8V5QaLBhHQdv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\appendix\\n\\n\\\\section{Per-Task Collision Avoidance Rates}\\\\label{sec:appendix_pertask}\\n\\nTable~\\\\ref{tab:pertask_lora} reports per-task CAR for LoRA-only fine-tuning across three seeds. The ordering is consistent: \\\\texttt{chocolate\\\\_pudding} highest, \\\\texttt{bbq\\\\_sauce} lowest. This ordering is invariant across all SDF conditions (Tables~\\\\ref{tab:pertask_l005}--\\\\ref{tab:pertask_l01}), confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR (\\\\%) for LoRA-only fine-tuning (no SDF), 30K checkpoint. Overall: 54.83\\\\,$\\\\pm$\\\\,2.25.}\\n\\\\label{tab:pertask_lora}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 74 & 68 & 76 & 72.67 \\\\\\\\\\nmilk & 66 & 72 & 62 & 66.67 \\\\\\\\\\norange\\\\_juice & 68 & 54 & 56 & 59.33 \\\\\\\\\\nbbq\\\\_sauce & 20 & 16 & 26 & 20.67 \\\\\\\\\\n\\\\midrule\\nPer-seed mean & 57.0 & 52.5 & 55.0 & 54.83 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR (\\\\%) for LoRA+SDF $\\\\lambda{=}0.005$, 30K checkpoint. Overall: 54.5\\\\,$\\\\pm$\\\\,2.29.}\\n\\\\label{tab:pertask_l005}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 74 & 70 & 74 & 72.67 \\\\\\\\\\nmilk & 74 & 68 & 72 & 71.33 \\\\\\\\\\norange\\\\_juice & 52 & 64 & 46 & 54.00 \\\\\\\\\\nbbq\\\\_sauce & 28 & 14 & 18 & 20.00 \\\\\\\\\\n\\\\midrule\\nPer-seed mean & 57.0 & 54.0 & 52.5 & 54.50 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR (\\\\%) for LoRA+SDF $\\\\lambda{=}0.01$, 30K checkpoint. Overall: 56.33\\\\,$\\\\pm$\\\\,1.61.}\\n\\\\label{tab:pertask_l01}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 74 & 76 & 68 & 72.67 \\\\\\\\\\nmilk & 72 & 72 & 72 & 72.00 \\\\\\\\\\norange\\\\_juice & 48 & 60 & 64 & 57.33 \\\\\\\\\\nbbq\\\\_sauce & 34 & 22 & 14 & 23.33 \\\\\\\\\\n\\\\midrule\\nPer-seed mean & 57.0 & 57.5 & 54.5 & 56.33 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR and TSR (\\\\%) for the Pi0.5 pre-trained baseline (no fine-tuning, single evaluation). Overall CAR: 28.5\\\\%, TSR: 71.5\\\\%.}\\n\\\\label{tab:pertask_baseline}\\n\\\\small\\n\\\\begin{tabular}{lcc}\\n\\\\toprule\\nTask & CAR & TSR \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 60 & 80 \\\\\\\\\\norange\\\\_juice & 16 & 74 \\\\\\\\\\nbbq\\\\_sauce & 32 & 66 \\\\\\\\\\nmilk & 6 & 66 \\\\\\\\\\n\\\\midrule\\nMean & 28.5 & 71.5 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nThe per-task pattern reveals why \\\\texttt{bbq\\\\_sauce} is hardest: the BBQ sauce bottle is positioned behind a cluster of tall obstacles (moka pot, wine bottle), requiring the end-effector to navigate through a narrow corridor. \\\\texttt{chocolate\\\\_pudding}, placed at the front of the basket with fewer obstructions, is easiest. This ordering is consistent across all $\\\\lambda$ values, including a $20\\\\times$ range from 0.005 to 0.1 (Tables~\\\\ref{tab:pertask_l005}--\\\\ref{tab:pertask_l01}), confirming that task difficulty is determined by demonstration trajectory distribution rather than SDF loss weight.\\n\\n\\n\\\\section{Null Distribution and Permutation Test}\\\\label{sec:appendix_null}\\n\\nWe construct the null distribution from all conditions where SDF supervision is either absent or demonstrably redundant ($p > 0.1$ versus LoRA-only). This yields six per-seed CAR values: three LoRA-only seeds and three $\\\\lambda{=}0.005$ seeds (Table~\\\\ref{tab:null_dist}).\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Null distribution construction. Values are per-seed overall CAR (\\\\%) at the 30K checkpoint.}\\n\\\\label{tab:null_dist}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nCondition & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nLoRA-only & 57.0 & 52.5 & 55.0 & 54.83 \\\\\\\\\\nLoRA+SDF $\\\\lambda{=}0.005$ & 57.0 & 54.0 & 52.5 & 54.50 \\\\\\\\\\n\\\\midrule\\n\\\\multicolumn{4}{l}{Pooled null: $\\\\{57.0, 52.5, 55.0, 57.0, 54.0, 52.5\\\\}$} \\\\\\\\\\n\\\\multicolumn{4}{l}{$\\\\mu_0 = 54.67$, $\\\\sigma_0 = 2.04$} \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\paragraph{Permutation test procedure.}\\nFor each treatment condition (e.g., $\\\\lambda{=}0.1$, $k$ seeds), we enumerate all $\\\\binom{6+k}{k}$ ways to draw\\n\\n... [截断: 输出过长，省略 5084 字符] ...\\n\\neflects stochastic variation rather than a sustained geometric-supervision effect.\\n\\n\\n\\\\section{SDF Ground Truth Pipeline}\\\\label{sec:appendix_sdf_pipeline}\\n\\n\\\\paragraph{Mesh processing.}\\nFor each SafeLIBERO scene, we extract all visual meshes from the MuJoCo XML model. The \\\\texttt{spatial\\\\_bowl} scene contains 68 meshes (19 initially watertight); \\\\texttt{object\\\\_chocolate} contains 60 meshes (13 initially watertight). We apply automated repair (hole filling, normal correction, winding order fix) via Trimesh, successfully repairing 2/49 and 4/47 non-watertight meshes respectively. Robot arm meshes (complex multi-part geometry) remain non-watertight and are excluded from SDF computation, as the SDF field targets scene obstacles only.\\n\\n\\\\paragraph{SDF computation.}\\nQuery points are sampled via dual-scale Gaussian ($\\\\sigma_1{=}0.025$, $\\\\sigma_2{=}0.008$, 80\\\\% near-surface) plus 20\\\\% uniform within the bounding box, yielding 4,084 points per scene. SDF values are truncated to $[-0.05, 0.05]$\\\\,m. Key statistics: near-surface ratio ($|$SDF$| < 0.02$) is 61.0--61.5\\\\%; inside ratio (SDF $< 0$) is 20.4--23.8\\\\%.\\n\\n\\\\paragraph{Gradient verification.}\\nWe verify SDF gradient directions via finite differences ($\\\\epsilon = 10^{-4}$) on 300 near-surface points per scene. Accuracy: 98.7\\\\% (\\\\texttt{spatial\\\\_bowl}), 99.7\\\\% (\\\\texttt{object\\\\_chocolate}). The gradient points away from obstacle surfaces, ensuring that the collision cost $\\\\text{ReLU}(-\\\\text{SDF} + m)$ correctly penalizes proximity.\\n\\n\\\\paragraph{Sign convention.}\\nThe pysdf library uses positive-inside convention. We apply $\\\\text{SDF} = -\\\\text{pysdf\\\\_output}$ to convert to the standard negative-inside convention. Verified: inside points yield SDF $< 0$ (cost $> 0$); outside points beyond margin yield cost $= 0$.\\n\\n\\n\\\\section{Training Hyperparameters}\\\\label{sec:appendix_hyperparams}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Training and evaluation hyperparameters for all Pi0.5 experiments.}\\n\\\\label{tab:hyperparams}\\n\\\\small\\n\\\\begin{tabular}{ll}\\n\\\\toprule\\n\\\\textbf{Training} \\\\\\\\\\n\\\\midrule\\nBase model & Pi0.5 (PaliGemma 2B + Gemma 300M action expert) \\\\\\\\\\nLoRA rank (PaliGemma / Expert) & 16 / 32 \\\\\\\\\\nLoRA alpha (PaliGemma / Expert) & 16.0 / 32.0 \\\\\\\\\\nOptimizer & AdamW with cosine decay \\\\\\\\\\nLearning rate & $2.5 \\\\times 10^{-5}$ \\\\\\\\\\nBatch size & 32 \\\\\\\\\\nTotal training steps & 30,000 \\\\\\\\\\nPhase 1 (warmup, LoRA frozen) & 5,000 steps \\\\\\\\\\nPhase 2 (LoRA unfrozen) & 25,000 steps \\\\\\\\\\nSDF loss weight $\\\\lambda$ & $\\\\{0, 0.005, 0.01, 0.1\\\\}$ \\\\\\\\\\nSeeds per condition & 3 (except $\\\\lambda{=}0.1$: 2 at 30K) \\\\\\\\\\nAction horizon & 10 tokens \\\\\\\\\\n\\\\midrule\\n\\\\textbf{Evaluation} \\\\\\\\\\n\\\\midrule\\nBenchmark & SafeLIBERO Object (4 tasks) \\\\\\\\\\nSafety level & II \\\\\\\\\\nEpisodes per task & 50 \\\\\\\\\\nMax steps per episode & 300 \\\\\\\\\\nReplan interval & 5 steps \\\\\\\\\\nCollision threshold & 0.001\\\\,m \\\\\\\\\\nEvaluation seed & 7 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\n\\\\section{Evaluation Protocol and Metrics}\\\\label{sec:appendix_eval_protocol}\\n\\n\\\\paragraph{Task descriptions.}\\nAll four tasks require picking up a target object and placing it in a basket, amid Level-II safety obstacles. The tasks are:\\n\\\\begin{enumerate}[nosep]\\n    \\\\item \\\\texttt{chocolate\\\\_pudding}: Pick up chocolate pudding, place in basket.\\n    \\\\item \\\\texttt{orange\\\\_juice}: Pick up orange juice, place in basket.\\n    \\\\item \\\\texttt{milk}: Pick up milk, place in basket.\\n    \\\\item \\\\texttt{bbq\\\\_sauce}: Pick up BBQ sauce, place in basket.\\n\\\\end{enumerate}\\n\\n\\\\paragraph{Metrics.}\\n\\\\begin{itemize}[nosep]\\n    \\\\item \\\\textbf{TSR} (Task Success Rate): fraction of episodes where the task is completed.\\n    \\\\item \\\\textbf{CAR} (Collision Avoidance Rate): fraction of episodes with no collision detected (contact force $>$ 0.001\\\\,m displacement between any robot link and obstacle).\\n    \\\\item \\\\textbf{dfCAR} (displacement-filtered CAR): CAR computed only over episodes with EE displacement $\\\\geq \\\\tau_d$ (default $\\\\tau_d = 0.1$\\\\,mm).\\n    \\\\item \\\\textbf{SSR} (Safe Success Rate): fraction of episodes that are both successful and collision-free.\\n\\\\end{itemize}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "ca3d2468-031b-45af-9f53-5f876f8836ff",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\appendix\\\\n\\\\n\\\\\\\\section{Per-Task Collision Avoidance Rates}\\\\\\\\label{sec:appendix_pertask}\\\\n\\\\nTable~\\\\\\\\ref{tab:pertask_lora} reports per-task CAR for LoRA-only fine-tuning across three seeds. The ordering is consistent: \\\\\\\\texttt{chocolate\\\\\\\\_pudding} highest, \\\\\\\\texttt{bbq\\\\\\\\_sauce} lowest. This ordering is invariant across all SDF conditions (Tables~\\\\\\\\ref{tab:pertask_l005}--\\\\\\\\ref{tab:pertask_l01}), confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Per-task CAR (\\\\\\\\%) for LoRA-only fine-tuning (no SDF), 30K checkpoint. Overall: 54.83\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,2.25.}\\\\n\\\\\\\\label{tab:pertask_lora}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lcccc}\\\\n\\\\\\\\toprule\\\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nchocolate\\\\\\\\_pudding & 74 & 68 & 76 & 72.67 \\\\\\\\\\\\\\\\\\\\nmilk & 66 & 72 & 62 & 66.67 \\\\\\\\\\\\\\\\\\\\norange\\\\\\\\_juice & 68 & 54 & 56 & 59.33 \\\\\\\\\\\\\\\\\\\\nbbq\\\\\\\\_sauce & 20 & 16 & 26 & 20.67 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nPer-seed mean & 57.0 & 52.5 & 55.0 & 54.83 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Per-task CAR (\\\\\\\\%) for LoRA+SDF $\\\\\\\\lambda{=}0.005$, 30K checkpoint. Overall: 54.5\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,2.29.}\\\\n\\\\\\\\label{tab:pertask_l005}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lcccc}\\\\n\\\\\\\\toprule\\\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nchocolate\\\\\\\\_pudding & 74 & 70 & 74 & 72.67 \\\\\\\\\\\\\\\\\\\\nmilk & 74 & 68 & 72 & 71.33 \\\\\\\\\\\\\\\\\\\\norange\\\\\\\\_juice & 52 & 64 & 46 & 54.00 \\\\\\\\\\\\\\\\\\\\nbbq\\\\\\\\_sauce & 28 & 14 & 18 & 20.00 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nPer-seed mean & 57.0 & 54.0 & 52.5 & 54.50 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Per-task CAR (\\\\\\\\%) for LoRA+SDF $\\\\\\\\lambda{=}0.01$, 30K checkpoint. Overall: 56.33\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,1.61.}\\\\n\\\\\\\\label{tab:pertask_l01}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lcccc}\\\\n\\\\\\\\toprule\\\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nchocolate\\\\\\\\_pudding & 74 & 76 & 68 & 72.67 \\\\\\\\\\\\\\\\\\\\nmilk & 72 & 72 & 72 & 72.00 \\\\\\\\\\\\\\\\\\\\norange\\\\\\\\_juice & 48 & 60 & 64 & 57.33 \\\\\\\\\\\\\\\\\\\\nbbq\\\\\\\\_sauce & 34 & 22 & 14 & 23.33 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nPer-seed mean & 57.0 & 57.5 & 54.5 & 56.33 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Per-task CAR and TSR (\\\\\\\\%) for the Pi0.5 pre-trained baseline (no fine-tuning, single evaluation). Overall CAR: 28.5\\\\\\\\%, TSR: 71.5\\\\\\\\%.}\\\\n\\\\\\\\label{tab:pertask_baseline}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lcc}\\\\n\\\\\\\\toprule\\\\nTask & CAR & TSR \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nchocolate\\\\\\\\_pudding & 60 & 80 \\\\\\\\\\\\\\\\\\\\norange\\\\\\\\_juice & 16 & 74 \\\\\\\\\\\\\\\\\\\\nbbq\\\\\\\\_sauce & 32 & 66 \\\\\\\\\\\\\\\\\\\\nmilk & 6 & 66 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nMean & 28.5 & 71.5 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\nThe per-task pattern reveals why \\\\\\\\texttt{bbq\\\\\\\\_sauce} is hardest: the BBQ sauce bottle is positioned behind a cluster of tall obstacles (moka pot, wine bottle), requiring the end-effector to navigate through a narrow corridor. \\\\\\\\texttt{chocolate\\\\\\\\_pudding}, placed at the front of the basket with fewer obstructions, is easiest. This ordering is consistent across all $\\\\\\\\lambda$ values, including a $20\\\\\\\\times$ range from 0.005 to 0.1 (Tables~\\\\\\\\ref{tab:pertask_l005}--\\\\\\\\ref{tab:pertask_l01}), confirming that task difficulty is determined by demonstration trajectory distribution rather than SDF loss weight.\\\\n\\\\n\\\\n\\\\\\\\section{Null Distribution and Permutation Test}\\\\\\\\label{sec:appendix_null}\\\\n\\\\nWe construct the null distribution from all conditions where SDF supervision is either absent or demonstrably redundant ($p > 0.1$ versus LoRA-only). This yields six per-seed CAR values: three LoRA-only seeds and three $\\\\\\\\lambda{=}0.005$ seeds (Table~\\\\\\\\ref{tab:null_dist}).\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Null distribution construction. Values are per-seed overall CAR (\\\\\\\\%) at the 30K checkpoint.}\\\\n\\\\\\\\label{tab:null_dist}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lcccc}\\\\n\\\\\\\\toprule\\\\nCondition & s0 & s1 & s2 & Mean \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nLoRA-only & 57.0 & 52.5 & 55.0 & 54.83 \\\\\\\\\\\\\\\\\\\\nLoRA+SDF $\\\\\\\\lambda{=}0.005$ & 57.0 & 54.0 & 52.5 & 54.50 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\n\\\\\\\\multicolumn{4}{l}{Pooled null: $\\\\\\\\{57.0, 52.5, 55.0, 57.0, 54.0, 52.5\\\\\\\\}$} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\multicolumn{4}{l}{$\\\\\\\\mu_0 = 54.67$, $\\\\\\\\sigma_0 = 2.04$} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\paragraph{Permutation test procedure.}\\\\nFor each treatment condition (e.g., $\\\\\\\\lambda{=}0.1$, $k$ seeds), we enumerate all $\\\\\\\\binom{6+k}{k}$ ways to draw\\\\n\\\\n... [截断: 输出过长，省略 5084 字符] ...\\\\n\\\\neflects stochastic variation rather than a sustained geometric-supervision effect.\\\\n\\\\n\\\\n\\\\\\\\section{SDF Ground Truth Pipeline}\\\\\\\\label{sec:appendix_sdf_pipeline}\\\\n\\\\n\\\\\\\\paragraph{Mesh processing.}\\\\nFor each SafeLIBERO scene, we extract all visual meshes from the MuJoCo XML model. The \\\\\\\\texttt{spatial\\\\\\\\_bowl} scene contains 68 meshes (19 initially watertight); \\\\\\\\texttt{object\\\\\\\\_chocolate} contains 60 meshes (13 initially watertight). We apply automated repair (hole filling, normal correction, winding order fix) via Trimesh, successfully repairing 2/49 and 4/47 non-watertight meshes respectively. Robot arm meshes (complex multi-part geometry) remain non-watertight and are excluded from SDF computation, as the SDF field targets scene obstacles only.\\\\n\\\\n\\\\\\\\paragraph{SDF computation.}\\\\nQuery points are sampled via dual-scale Gaussian ($\\\\\\\\sigma_1{=}0.025$, $\\\\\\\\sigma_2{=}0.008$, 80\\\\\\\\% near-surface) plus 20\\\\\\\\% uniform within the bounding box, yielding 4,084 points per scene. SDF values are truncated to $[-0.05, 0.05]$\\\\\\\\,m. Key statistics: near-surface ratio ($|$SDF$| < 0.02$) is 61.0--61.5\\\\\\\\%; inside ratio (SDF $< 0$) is 20.4--23.8\\\\\\\\%.\\\\n\\\\n\\\\\\\\paragraph{Gradient verification.}\\\\nWe verify SDF gradient directions via finite differences ($\\\\\\\\epsilon = 10^{-4}$) on 300 near-surface points per scene. Accuracy: 98.7\\\\\\\\% (\\\\\\\\texttt{spatial\\\\\\\\_bowl}), 99.7\\\\\\\\% (\\\\\\\\texttt{object\\\\\\\\_chocolate}). The gradient points away from obstacle surfaces, ensuring that the collision cost $\\\\\\\\text{ReLU}(-\\\\\\\\text{SDF} + m)$ correctly penalizes proximity.\\\\n\\\\n\\\\\\\\paragraph{Sign convention.}\\\\nThe pysdf library uses positive-inside convention. We apply $\\\\\\\\text{SDF} = -\\\\\\\\text{pysdf\\\\\\\\_output}$ to convert to the standard negative-inside convention. Verified: inside points yield SDF $< 0$ (cost $> 0$); outside points beyond margin yield cost $= 0$.\\\\n\\\\n\\\\n\\\\\\\\section{Training Hyperparameters}\\\\\\\\label{sec:appendix_hyperparams}\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Training and evaluation hyperparameters for all Pi0.5 experiments.}\\\\n\\\\\\\\label{tab:hyperparams}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{ll}\\\\n\\\\\\\\toprule\\\\n\\\\\\\\textbf{Training} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nBase model & Pi0.5 (PaliGemma 2B + Gemma 300M action expert) \\\\\\\\\\\\\\\\\\\\nLoRA rank (PaliGemma / Expert) & 16 / 32 \\\\\\\\\\\\\\\\\\\\nLoRA alpha (PaliGemma / Expert) & 16.0 / 32.0 \\\\\\\\\\\\\\\\\\\\nOptimizer & AdamW with cosine decay \\\\\\\\\\\\\\\\\\\\nLearning rate & $2.5 \\\\\\\\times 10^{-5}$ \\\\\\\\\\\\\\\\\\\\nBatch size & 32 \\\\\\\\\\\\\\\\\\\\nTotal training steps & 30,000 \\\\\\\\\\\\\\\\\\\\nPhase 1 (warmup, LoRA frozen) & 5,000 steps \\\\\\\\\\\\\\\\\\\\nPhase 2 (LoRA unfrozen) & 25,000 steps \\\\\\\\\\\\\\\\\\\\nSDF loss weight $\\\\\\\\lambda$ & $\\\\\\\\{0, 0.005, 0.01, 0.1\\\\\\\\}$ \\\\\\\\\\\\\\\\\\\\nSeeds per condition & 3 (except $\\\\\\\\lambda{=}0.1$: 2 at 30K) \\\\\\\\\\\\\\\\\\\\nAction horizon & 10 tokens \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\n\\\\\\\\textbf{Evaluation} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nBenchmark & SafeLIBERO Object (4 tasks) \\\\\\\\\\\\\\\\\\\\nSafety level & II \\\\\\\\\\\\\\\\\\\\nEpisodes per task & 50 \\\\\\\\\\\\\\\\\\\\nMax steps per episode & 300 \\\\\\\\\\\\\\\\\\\\nReplan interval & 5 steps \\\\\\\\\\\\\\\\\\\\nCollision threshold & 0.001\\\\\\\\,m \\\\\\\\\\\\\\\\\\\\nEvaluation seed & 7 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\n\\\\\\\\section{Evaluation Protocol and Metrics}\\\\\\\\label{sec:appendix_eval_protocol}\\\\n\\\\n\\\\\\\\paragraph{Task descriptions.}\\\\nAll four tasks require picking up a target object and placing it in a basket, amid Level-II safety obstacles. The tasks are:\\\\n\\\\\\\\begin{enumerate}[nosep]\\\\n    \\\\\\\\item \\\\\\\\texttt{chocolate\\\\\\\\_pudding}: Pick up chocolate pudding, place in basket.\\\\n    \\\\\\\\item \\\\\\\\texttt{orange\\\\\\\\_juice}: Pick up orange juice, place in basket.\\\\n    \\\\\\\\item \\\\\\\\texttt{milk}: Pick up milk, place in basket.\\\\n    \\\\\\\\item \\\\\\\\texttt{bbq\\\\\\\\_sauce}: Pick up BBQ sauce, place in basket.\\\\n\\\\\\\\end{enumerate}\\\\n\\\\n\\\\\\\\paragraph{Metrics.}\\\\n\\\\\\\\begin{itemize}[nosep]\\\\n    \\\\\\\\item \\\\\\\\textbf{TSR} (Task Success Rate): fraction of episodes where the task is completed.\\\\n    \\\\\\\\item \\\\\\\\textbf{CAR} (Collision Avoidance Rate): fraction of episodes with no collision detected (contact force $>$ 0.001\\\\\\\\,m displacement between any robot link and obstacle).\\\\n    \\\\\\\\item \\\\\\\\textbf{dfCAR} (displacement-filtered CAR): CAR computed only over episodes with EE displacement $\\\\\\\\geq \\\\\\\\tau_d$ (default $\\\\\\\\tau_d = 0.1$\\\\\\\\,mm).\\\\n    \\\\\\\\item \\\\\\\\textbf{SSR} (Safe Success Rate): fraction of episodes that are both successful and collision-free.\\\\n\\\\\\\\end{itemize}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.58}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\appendix\\n\\n\\\\section{Per-Task Collision Avoidance Rates}\\\\label{sec:appendix_pertask}\\n\\nTable~\\\\ref{tab:pertask_lora} reports per-task CAR for LoRA-only fine-tuning across three seeds. The ordering is consistent: \\\\texttt{chocolate\\\\_pudding} highest, \\\\texttt{bbq\\\\_sauce} lowest. This ordering is invariant across all SDF conditions (Tables~\\\\ref{tab:pertask_l005}--\\\\ref{tab:pertask_l01}), confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR (\\\\%) for LoRA-only fine-tuning (no SDF), 30K checkpoint. Overall: 54.83\\\\,$\\\\pm$\\\\,2.25.}\\n\\\\label{tab:pertask_lora}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 74 & 68 & 76 & 72.67 \\\\\\\\\\nmilk & 66 & 72 & 62 & 66.67 \\\\\\\\\\norange\\\\_juice & 68 & 54 & 56 & 59.33 \\\\\\\\\\nbbq\\\\_sauce & 20 & 16 & 26 & 20.67 \\\\\\\\\\n\\\\midrule\\nPer-seed mean & 57.0 & 52.5 & 55.0 & 54.83 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR (\\\\%) for LoRA+SDF $\\\\lambda{=}0.005$, 30K checkpoint. Overall: 54.5\\\\,$\\\\pm$\\\\,2.29.}\\n\\\\label{tab:pertask_l005}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 74 & 70 & 74 & 72.67 \\\\\\\\\\nmilk & 74 & 68 & 72 & 71.33 \\\\\\\\\\norange\\\\_juice & 52 & 64 & 46 & 54.00 \\\\\\\\\\nbbq\\\\_sauce & 28 & 14 & 18 & 20.00 \\\\\\\\\\n\\\\midrule\\nPer-seed mean & 57.0 & 54.0 & 52.5 & 54.50 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR (\\\\%) for LoRA+SDF $\\\\lambda{=}0.01$, 30K checkpoint. Overall: 56.33\\\\,$\\\\pm$\\\\,1.61.}\\n\\\\label{tab:pertask_l01}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 74 & 76 & 68 & 72.67 \\\\\\\\\\nmilk & 72 & 72 & 72 & 72.00 \\\\\\\\\\norange\\\\_juice & 48 & 60 & 64 & 57.33 \\\\\\\\\\nbbq\\\\_sauce & 34 & 22 & 14 & 23.33 \\\\\\\\\\n\\\\midrule\\nPer-seed mean & 57.0 & 57.5 & 54.5 & 56.33 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR and TSR (\\\\%) for the Pi0.5 pre-trained baseline (no fine-tuning, single evaluation). Overall CAR: 28.5\\\\%, TSR: 71.5\\\\%.}\\n\\\\label{tab:pertask_baseline}\\n\\\\small\\n\\\\begin{tabular}{lcc}\\n\\\\toprule\\nTask & CAR & TSR \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 60 & 80 \\\\\\\\\\norange\\\\_juice & 16 & 74 \\\\\\\\\\nbbq\\\\_sauce & 32 & 66 \\\\\\\\\\nmilk & 6 & 66 \\\\\\\\\\n\\\\midrule\\nMean & 28.5 & 71.5 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nThe per-task pattern reveals why \\\\texttt{bbq\\\\_sauce} is hardest: the BBQ sauce bottle is positioned behind a cluster of tall obstacles (moka pot, wine bottle), requiring the end-effector to navigate through a narrow corridor. \\\\texttt{chocolate\\\\_pudding}, placed at the front of the basket with fewer obstructions, is easiest. This ordering is consistent across all $\\\\lambda$ values, including a $20\\\\times$ range from 0.005 to 0.1 (Tables~\\\\ref{tab:pertask_l005}--\\\\ref{tab:pertask_l01}), confirming that task difficulty is determined by demonstration trajectory distribution rather than SDF loss weight.\\n\\n\\n\\\\section{Null Distribution and Permutation Test}\\\\label{sec:appendix_null}\\n\\nWe construct the null distribution from all conditions where SDF supervision is either absent or demonstrably redundant ($p > 0.1$ versus LoRA-only). This yields six per-seed CAR values: three LoRA-only seeds and three $\\\\lambda{=}0.005$ seeds (Table~\\\\ref{tab:null_dist}).\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Null distribution construction. Values are per-seed overall CAR (\\\\%) at the 30K checkpoint.}\\n\\\\label{tab:null_dist}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nCondition & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nLoRA-only & 57.0 & 52.5 & 55.0 & 54.83 \\\\\\\\\\nLoRA+SDF $\\\\lambda{=}0.005$ & 57.0 & 54.0 & 52.5 & 54.50 \\\\\\\\\\n\\\\midrule\\n\\\\multicolumn{4}{l}{Pooled null: $\\\\{57.0, 52.5, 55.0, 57.0, 54.0, 52.5\\\\}$} \\\\\\\\\\n\\\\multicolumn{4}{l}{$\\\\mu_0 = 54.67$, $\\\\sigma_0 = 2.04$} \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\paragraph{Permutation test procedure.}\\nFor each treatment condition (e.g., $\\\\lambda{=}0.1$, $k$ seeds), we enumerate all $\\\\binom{6+k}{k}$ ways to draw\\n\\n... [截断: 输出过长，省略 5084 字符] ...\\n\\neflects stochastic variation rather than a sustained geometric-supervision effect.\\n\\n\\n\\\\section{SDF Ground Truth Pipeline}\\\\label{sec:appendix_sdf_pipeline}\\n\\n\\\\paragraph{Mesh processing.}\\nFor each SafeLIBERO scene, we extract all visual meshes from the MuJoCo XML model. The \\\\texttt{spatial\\\\_bowl} scene contains 68 meshes (19 initially watertight); \\\\texttt{object\\\\_chocolate} contains 60 meshes (13 initially watertight). We apply automated repair (hole filling, normal correction, winding order fix) via Trimesh, successfully repairing 2/49 and 4/47 non-watertight meshes respectively. Robot arm meshes (complex multi-part geometry) remain non-watertight and are excluded from SDF computation, as the SDF field targets scene obstacles only.\\n\\n\\\\paragraph{SDF computation.}\\nQuery points are sampled via dual-scale Gaussian ($\\\\sigma_1{=}0.025$, $\\\\sigma_2{=}0.008$, 80\\\\% near-surface) plus 20\\\\% uniform within the bounding box, yielding 4,084 points per scene. SDF values are truncated to $[-0.05, 0.05]$\\\\,m. Key statistics: near-surface ratio ($|$SDF$| < 0.02$) is 61.0--61.5\\\\%; inside ratio (SDF $< 0$) is 20.4--23.8\\\\%.\\n\\n\\\\paragraph{Gradient verification.}\\nWe verify SDF gradient directions via finite differences ($\\\\epsilon = 10^{-4}$) on 300 near-surface points per scene. Accuracy: 98.7\\\\% (\\\\texttt{spatial\\\\_bowl}), 99.7\\\\% (\\\\texttt{object\\\\_chocolate}). The gradient points away from obstacle surfaces, ensuring that the collision cost $\\\\text{ReLU}(-\\\\text{SDF} + m)$ correctly penalizes proximity.\\n\\n\\\\paragraph{Sign convention.}\\nThe pysdf library uses positive-inside convention. We apply $\\\\text{SDF} = -\\\\text{pysdf\\\\_output}$ to convert to the standard negative-inside convention. Verified: inside points yield SDF $< 0$ (cost $> 0$); outside points beyond margin yield cost $= 0$.\\n\\n\\n\\\\section{Training Hyperparameters}\\\\label{sec:appendix_hyperparams}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Training and evaluation hyperparameters for all Pi0.5 experiments.}\\n\\\\label{tab:hyperparams}\\n\\\\small\\n\\\\begin{tabular}{ll}\\n\\\\toprule\\n\\\\textbf{Training} \\\\\\\\\\n\\\\midrule\\nBase model & Pi0.5 (PaliGemma 2B + Gemma 300M action expert) \\\\\\\\\\nLoRA rank (PaliGemma / Expert) & 16 / 32 \\\\\\\\\\nLoRA alpha (PaliGemma / Expert) & 16.0 / 32.0 \\\\\\\\\\nOptimizer & AdamW with cosine decay \\\\\\\\\\nLearning rate & $2.5 \\\\times 10^{-5}$ \\\\\\\\\\nBatch size & 32 \\\\\\\\\\nTotal training steps & 30,000 \\\\\\\\\\nPhase 1 (warmup, LoRA frozen) & 5,000 steps \\\\\\\\\\nPhase 2 (LoRA unfrozen) & 25,000 steps \\\\\\\\\\nSDF loss weight $\\\\lambda$ & $\\\\{0, 0.005, 0.01, 0.1\\\\}$ \\\\\\\\\\nSeeds per condition & 3 (except $\\\\lambda{=}0.1$: 2 at 30K) \\\\\\\\\\nAction horizon & 10 tokens \\\\\\\\\\n\\\\midrule\\n\\\\textbf{Evaluation} \\\\\\\\\\n\\\\midrule\\nBenchmark & SafeLIBERO Object (4 tasks) \\\\\\\\\\nSafety level & II \\\\\\\\\\nEpisodes per task & 50 \\\\\\\\\\nMax steps per episode & 300 \\\\\\\\\\nReplan interval & 5 steps \\\\\\\\\\nCollision threshold & 0.001\\\\,m \\\\\\\\\\nEvaluation seed & 7 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\n\\\\section{Evaluation Protocol and Metrics}\\\\label{sec:appendix_eval_protocol}\\n\\n\\\\paragraph{Task descriptions.}\\nAll four tasks require picking up a target object and placing it in a basket, amid Level-II safety obstacles. The tasks are:\\n\\\\begin{enumerate}[nosep]\\n    \\\\item \\\\texttt{chocolate\\\\_pudding}: Pick up chocolate pudding, place in basket.\\n    \\\\item \\\\texttt{orange\\\\_juice}: Pick up orange juice, place in basket.\\n    \\\\item \\\\texttt{milk}: Pick up milk, place in basket.\\n    \\\\item \\\\texttt{bbq\\\\_sauce}: Pick up BBQ sauce, place in basket.\\n\\\\end{enumerate}\\n\\n\\\\paragraph{Metrics.}\\n\\\\begin{itemize}[nosep]\\n    \\\\item \\\\textbf{TSR} (Task Success Rate): fraction of episodes where the task is completed.\\n    \\\\item \\\\textbf{CAR} (Collision Avoidance Rate): fraction of episodes with no collision detected (contact force $>$ 0.001\\\\,m displacement between any robot link and obstacle).\\n    \\\\item \\\\textbf{dfCAR} (displacement-filtered CAR): CAR computed only over episodes with EE displacement $\\\\geq \\\\tau_d$ (default $\\\\tau_d = 0.1$\\\\,mm).\\n    \\\\item \\\\textbf{SSR} (Safe Success Rate): fraction of episodes that are both successful and collision-free.\\n\\\\end{itemize}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"
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
Now let me also check for any old/stale values and do a thorough scan. Let me also check if there are more files I might be missing - the appendix output was truncated. Let me get the rest of the appendix, and also scan for old values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "05f24317-cfd1-4e5b-a103-c3dc8b8e8ccc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4e6McA4kUWxYtkvqTMKqX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8113,
      "cache_read_input_tokens": 25440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8113
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

_source line 26_

Let me get the truncated part of the appendix and scan for old values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "4c0b75a2-b4f5-4e42-b270-dc57fb6ebe41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4e6McA4kUWxYtkvqTMKqX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8113,
      "cache_read_input_tokens": 25440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8113
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

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01V17c9SHJL6qT9czwhzPL47`</summary>

```json
{
  "server": "westd-45947",
  "command": "wc -l /root/colliforce-vla/docs/paper/appendix.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "841bfdd5-c0fe-4b21-b5c6-e7bd9c19f8f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4e6McA4kUWxYtkvqTMKqX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8113,
      "cache_read_input_tokens": 25440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8113
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

_source line 28 · 2026-05-27T23:40:01.940Z_

<details><summary>↩ Tool result · `toolu_01V17c9SHJL6qT9czwhzPL47`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"254 /root/colliforce-vla/docs/paper/appendix.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "a34edb78-8eb0-4330-92eb-0f14f315f490",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"254 /root/colliforce-vla/docs/paper/appendix.tex\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"254 /root/colliforce-vla/docs/paper/appendix.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NpvvTHBe39Fp3VHmyvN5JM`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -n \"0.039\\|0.025\\|z=1.76\\|z = 1.76\" /root/colliforce-vla/docs/paper/abstract.tex /root/colliforce-vla/docs/paper/claim3.tex /root/colliforce-vla/docs/paper/discussion.tex /root/colliforce-vla/docs/paper/appendix.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "6d1931fa-591d-4e6d-bbcb-f4e0915b3eb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4e6McA4kUWxYtkvqTMKqX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8113,
      "cache_read_input_tokens": 25440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8113
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

_source line 30 · 2026-05-27T23:40:03.085Z_

<details><summary>↩ Tool result · `toolu_01NpvvTHBe39Fp3VHmyvN5JM`</summary>

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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "c5be7677-dad9-4da8-a687-d8c8e5303b7c",
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

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PfdjZcRUboo1bqQuShSrba`</summary>

```json
{
  "server": "westd-45947",
  "command": "tail -120 /root/colliforce-vla/docs/paper/appendix.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "5ac5ab98-7b92-4ff8-baef-4074d65440f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKWzrzQnDeRiRM7WATiLxT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 33553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 645
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

_source line 32 · 2026-05-27T23:40:07.140Z_

<details><summary>↩ Tool result · `toolu_01PfdjZcRUboo1bqQuShSrba`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"LoRA-only & s2 & 51.5 & 26.5 & 0.515 \\\\\\\\\\n\\\\midrule\\n$\\\\lambda{=}0.005$ & s0 & 55.5 & 30.0 & 0.541 \\\\\\\\\\n$\\\\lambda{=}0.005$ & s1 & 50.5 & 24.0 & 0.475 \\\\\\\\\\n$\\\\lambda{=}0.005$ & s2 & 56.0 & 29.5 & 0.527 \\\\\\\\\\n\\\\midrule\\n$\\\\lambda{=}0.01$ & s0 & 52.5 & 32.5 & 0.619 \\\\\\\\\\n$\\\\lambda{=}0.01$ & s1 & 55.5 & 30.0 & 0.541 \\\\\\\\\\n$\\\\lambda{=}0.01$ & s2 & 53.5 & 28.0 & 0.523 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nThe Pi0.5 baseline achieves SSR/TSR\\\\,=\\\\,0.39: most task-completing trajectories collide. After LoRA fine-tuning, SSR/TSR increases to 0.51--0.57 (mean 0.54), confirming that the CAR improvement reflects genuine avoidance among active trajectories, not reduced exposure from lower TSR. SDF conditions show comparable SSR/TSR ranges ($\\\\lambda{=}0.005$: 0.48--0.54; $\\\\lambda{=}0.01$: 0.52--0.62), reinforcing the conclusion that SDF supervision does not improve the safety profile beyond what LoRA fine-tuning provides.\\n\\n\\n\\\\section{Displacement Threshold Sensitivity}\\\\label{sec:appendix_threshold}\\n\\nThe displacement-filtered CAR (dfCAR) excludes episodes where the end-effector displacement falls below a threshold $\\\\tau_d$. Table~\\\\ref{tab:threshold_sens} demonstrates that dfCAR is robust across five orders of magnitude of $\\\\tau_d$ for all fine-tuned conditions, because these models exhibit no action collapse (all episodes have displacement $> 0.27$\\\\,m).\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{dfCAR (\\\\%) at varying displacement thresholds $\\\\tau_d$. All fine-tuned conditions (LoRA-only and SDF-augmented) show identical CAR across $\\\\tau_d \\\\in [2, 200]$\\\\,mm because no episodes exhibit sub-threshold displacement. Only at $\\\\tau_d = 300$\\\\,mm do 1--2 episodes per condition fall below threshold, causing $\\\\leq$\\\\,0.5\\\\,pp change.}\\n\\\\label{tab:threshold_sens}\\n\\\\small\\n\\\\begin{tabular}{lccccccc}\\n\\\\toprule\\n$\\\\tau_d$ (mm) & 2 & 5 & 10 & 50 & 100 & 200 & 300 \\\\\\\\\\n\\\\midrule\\nLoRA s0 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\\\\\\\\\nLoRA s1 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\\\\\\nSDF005 s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\\\\\\nSDF005 s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\\\\\\nSDF005 s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\\\\\\nSDF01 s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\\\\\\nSDF01 s1 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\\\\\\nSDF01 s2 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nFor the Pi0.5 baseline (without LoRA), all 200 episodes have EE displacement $> 0.27$\\\\,m (mean 0.37\\\\,m), so dfCAR $\\\\equiv$ CAR $= 28.5\\\\%$ at any reasonable threshold. The bimodal displacement distribution that motivates dfCAR arises in the Pi0 full fine-tuning setting (reported in the main text), where action collapse produces a mode near zero displacement.\\n\\n\\n\\\\section{Stepwise Checkpoint Ablation ($\\\\lambda{=}0.1$)}\\\\label{sec:appendix_stepwise}\\n\\nTo test whether $\\\\lambda{=}0.1$ produces a sustained training signal rather than a transient fluctuation, we evaluated six checkpoints spanning steps 16K--28K (every 2K steps) for two seeds (s0, s1). The mean CAR across these checkpoints is 55.3\\\\%, within 0.3$\\\\sigma$ of the null distribution mean (54.67\\\\%, $\\\\sigma = 2.04$). No monotonic trend is observed, and individual checkpoint CARs fluctuate within the null band. This suggests that the elevated CAR observed at the 30K checkpoint reflects stochastic variation rather than a sustained geometric-supervision effect.\\n\\n\\n\\\\section{SDF Ground Truth Pipeline}\\\\label{sec:appendix_sdf_pipeline}\\n\\n\\\\paragraph{Mesh processing.}\\nFor each SafeLIBERO scene, we extract all visual meshes from the MuJoCo XML model. The \\\\texttt{spatial\\\\_bowl} scene contains 68 meshes (19 initially watertight); \\\\texttt{object\\\\_chocolate} contains 60 meshes (13 initially watertight). We apply automated repair (hole filling, normal correction, winding order fix) via Trimesh, successfully repairing 2/49 and 4/47 non-watertight meshes respectively. Robot arm meshes (complex multi-part geometry) remain non-watertight and are excluded from SDF computation, as the SDF field targets scene obstacles only.\\n\\n\\\\paragraph{SDF computation.}\\nQuery points are sampled via dual-scale Gaussian ($\\\\sigma_1{=}0.025$, $\\\\sigma_2{=}0.008$, 80\\\\% near-surface) plus 20\\\\% uniform within the bounding box, yielding 4,084 points per scene. SDF values are truncated to $[-0.05, 0.05]$\\\\,m. Key statistics: near-surface ratio ($|$SDF$| < 0.02$) is 61.0--61.5\\\\%; inside ratio (SDF $< 0$) is 20.4--23.8\\\\%.\\n\\n\\\\paragraph{Gradient verification.}\\nWe verify SDF gradient directions via finite differences ($\\\\epsilon = 10^{-4}$) on 300 near-surface points per scene. Accuracy: 98.7\\\\% (\\\\texttt{spatial\\\\_bowl}), 99.7\\\\% (\\\\texttt{object\\\\_chocolate}). The gradient points away from obstacle surfaces, ensuring that the collision cost $\\\\text{ReLU}(-\\\\text{SDF} + m)$ correctly penalizes proximity.\\n\\n\\\\paragraph{Sign convention.}\\nThe pysdf library uses positive-inside convention. We apply $\\\\text{SDF} = -\\\\text{pysdf\\\\_output}$ to convert to the standard negative-inside convention. Verified: inside points yield SDF $< 0$ (cost $> 0$); outside points beyond margin yield cost $= 0$.\\n\\n\\n\\\\section{Training Hyperparameters}\\\\label{sec:appendix_hyperparams}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Training and evaluation hyperparameters for all Pi0.5 experiments.}\\n\\\\label{tab:hyperparams}\\n\\\\small\\n\\\\begin{tabular}{ll}\\n\\\\toprule\\n\\\\textbf{Training} \\\\\\\\\\n\\\\midrule\\nBase model & Pi0.5 (PaliGemma 2B + Gemma 300M action expert) \\\\\\\\\\nLoRA rank (PaliGemma / Expert) & 16 / 32 \\\\\\\\\\nLoRA alpha (PaliGemma / Expert) & 16.0 / 32.0 \\\\\\\\\\nOptimizer & AdamW with cosine decay \\\\\\\\\\nLearning rate & $2.5 \\\\times 10^{-5}$ \\\\\\\\\\nBatch size & 32 \\\\\\\\\\nTotal training steps & 30,000 \\\\\\\\\\nPhase 1 (warmup, LoRA frozen) & 5,000 steps \\\\\\\\\\nPhase 2 (LoRA unfrozen) & 25,000 steps \\\\\\\\\\nSDF loss weight $\\\\lambda$ & $\\\\{0, 0.005, 0.01, 0.1\\\\}$ \\\\\\\\\\nSeeds per condition & 3 (except $\\\\lambda{=}0.1$: 2 at 30K) \\\\\\\\\\nAction horizon & 10 tokens \\\\\\\\\\n\\\\midrule\\n\\\\textbf{Evaluation} \\\\\\\\\\n\\\\midrule\\nBenchmark & SafeLIBERO Object (4 tasks) \\\\\\\\\\nSafety level & II \\\\\\\\\\nEpisodes per task & 50 \\\\\\\\\\nMax steps per episode & 300 \\\\\\\\\\nReplan interval & 5 steps \\\\\\\\\\nCollision threshold & 0.001\\\\,m \\\\\\\\\\nEvaluation seed & 7 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\n\\\\section{Evaluation Protocol and Metrics}\\\\label{sec:appendix_eval_protocol}\\n\\n\\\\paragraph{Task descriptions.}\\nAll four tasks require picking up a target object and placing it in a basket, amid Level-II safety obstacles. The tasks are:\\n\\\\begin{enumerate}[nosep]\\n    \\\\item \\\\texttt{chocolate\\\\_pudding}: Pick up chocolate pudding, place in basket.\\n    \\\\item \\\\texttt{orange\\\\_juice}: Pick up orange juice, place in basket.\\n    \\\\item \\\\texttt{milk}: Pick up milk, place in basket.\\n    \\\\item \\\\texttt{bbq\\\\_sauce}: Pick up BBQ sauce, place in basket.\\n\\\\end{enumerate}\\n\\n\\\\paragraph{Metrics.}\\n\\\\begin{itemize}[nosep]\\n    \\\\item \\\\textbf{TSR} (Task Success Rate): fraction of episodes where the task is completed.\\n    \\\\item \\\\textbf{CAR} (Collision Avoidance Rate): fraction of episodes with no collision detected (contact force $>$ 0.001\\\\,m displacement between any robot link and obstacle).\\n    \\\\item \\\\textbf{dfCAR} (displacement-filtered CAR): CAR computed only over episodes with EE displacement $\\\\geq \\\\tau_d$ (default $\\\\tau_d = 0.1$\\\\,mm).\\n    \\\\item \\\\textbf{SSR} (Safe Success Rate): fraction of episodes that are both successful and collision-free.\\n\\\\end{itemize}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "093164e6-c020-483b-b0d8-f79cec697b39",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"LoRA-only & s2 & 51.5 & 26.5 & 0.515 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\n$\\\\\\\\lambda{=}0.005$ & s0 & 55.5 & 30.0 & 0.541 \\\\\\\\\\\\\\\\\\\\n$\\\\\\\\lambda{=}0.005$ & s1 & 50.5 & 24.0 & 0.475 \\\\\\\\\\\\\\\\\\\\n$\\\\\\\\lambda{=}0.005$ & s2 & 56.0 & 29.5 & 0.527 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\n$\\\\\\\\lambda{=}0.01$ & s0 & 52.5 & 32.5 & 0.619 \\\\\\\\\\\\\\\\\\\\n$\\\\\\\\lambda{=}0.01$ & s1 & 55.5 & 30.0 & 0.541 \\\\\\\\\\\\\\\\\\\\n$\\\\\\\\lambda{=}0.01$ & s2 & 53.5 & 28.0 & 0.523 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\nThe Pi0.5 baseline achieves SSR/TSR\\\\\\\\,=\\\\\\\\,0.39: most task-completing trajectories collide. After LoRA fine-tuning, SSR/TSR increases to 0.51--0.57 (mean 0.54), confirming that the CAR improvement reflects genuine avoidance among active trajectories, not reduced exposure from lower TSR. SDF conditions show comparable SSR/TSR ranges ($\\\\\\\\lambda{=}0.005$: 0.48--0.54; $\\\\\\\\lambda{=}0.01$: 0.52--0.62), reinforcing the conclusion that SDF supervision does not improve the safety profile beyond what LoRA fine-tuning provides.\\\\n\\\\n\\\\n\\\\\\\\section{Displacement Threshold Sensitivity}\\\\\\\\label{sec:appendix_threshold}\\\\n\\\\nThe displacement-filtered CAR (dfCAR) excludes episodes where the end-effector displacement falls below a threshold $\\\\\\\\tau_d$. Table~\\\\\\\\ref{tab:threshold_sens} demonstrates that dfCAR is robust across five orders of magnitude of $\\\\\\\\tau_d$ for all fine-tuned conditions, because these models exhibit no action collapse (all episodes have displacement $> 0.27$\\\\\\\\,m).\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{dfCAR (\\\\\\\\%) at varying displacement thresholds $\\\\\\\\tau_d$. All fine-tuned conditions (LoRA-only and SDF-augmented) show identical CAR across $\\\\\\\\tau_d \\\\\\\\in [2, 200]$\\\\\\\\,mm because no episodes exhibit sub-threshold displacement. Only at $\\\\\\\\tau_d = 300$\\\\\\\\,mm do 1--2 episodes per condition fall below threshold, causing $\\\\\\\\leq$\\\\\\\\,0.5\\\\\\\\,pp change.}\\\\n\\\\\\\\label{tab:threshold_sens}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lccccccc}\\\\n\\\\\\\\toprule\\\\n$\\\\\\\\tau_d$ (mm) & 2 & 5 & 10 & 50 & 100 & 200 & 300 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nLoRA s0 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\\\\\\\\\\\\\\\\\\\nLoRA s1 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\\\\\\\\\\\\\\\\nSDF005 s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\\\\\\\\\\\\\\\\nSDF005 s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\\\\\\\\\\\\\\\\nSDF005 s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\\\\\\\\\\\\\\\\nSDF01 s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\\\\\\\\\\\\\\\\nSDF01 s1 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\\\\\\\\\\\\\\\\nSDF01 s2 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\nFor the Pi0.5 baseline (without LoRA), all 200 episodes have EE displacement $> 0.27$\\\\\\\\,m (mean 0.37\\\\\\\\,m), so dfCAR $\\\\\\\\equiv$ CAR $= 28.5\\\\\\\\%$ at any reasonable threshold. The bimodal displacement distribution that motivates dfCAR arises in the Pi0 full fine-tuning setting (reported in the main text), where action collapse produces a mode near zero displacement.\\\\n\\\\n\\\\n\\\\\\\\section{Stepwise Checkpoint Ablation ($\\\\\\\\lambda{=}0.1$)}\\\\\\\\label{sec:appendix_stepwise}\\\\n\\\\nTo test whether $\\\\\\\\lambda{=}0.1$ produces a sustained training signal rather than a transient fluctuation, we evaluated six checkpoints spanning steps 16K--28K (every 2K steps) for two seeds (s0, s1). The mean CAR across these checkpoints is 55.3\\\\\\\\%, within 0.3$\\\\\\\\sigma$ of the null distribution mean (54.67\\\\\\\\%, $\\\\\\\\sigma = 2.04$). No monotonic trend is observed, and individual checkpoint CARs fluctuate within the null band. This suggests that the elevated CAR observed at the 30K checkpoint reflects stochastic variation rather than a sustained geometric-supervision effect.\\\\n\\\\n\\\\n\\\\\\\\section{SDF Ground Truth Pipeline}\\\\\\\\label{sec:appendix_sdf_pipeline}\\\\n\\\\n\\\\\\\\paragraph{Mesh processing.}\\\\nFor each SafeLIBERO scene, we extract all visual meshes from the MuJoCo XML model. The \\\\\\\\texttt{spatial\\\\\\\\_bowl} scene contains 68 meshes (19 initially watertight); \\\\\\\\texttt{object\\\\\\\\_chocolate} contains 60 meshes (13 initially watertight). We apply automated repair (hole filling, normal correction, winding order fix) via Trimesh, successfully repairing 2/49 and 4/47 non-watertight meshes respectively. Robot arm meshes (complex multi-part geometry) remain non-watertight and are excluded from SDF computation, as the SDF field targets scene obstacles only.\\\\n\\\\n\\\\\\\\paragraph{SDF computation.}\\\\nQuery points are sampled via dual-scale Gaussian ($\\\\\\\\sigma_1{=}0.025$, $\\\\\\\\sigma_2{=}0.008$, 80\\\\\\\\% near-surface) plus 20\\\\\\\\% uniform within the bounding box, yielding 4,084 points per scene. SDF values are truncated to $[-0.05, 0.05]$\\\\\\\\,m. Key statistics: near-surface ratio ($|$SDF$| < 0.02$) is 61.0--61.5\\\\\\\\%; inside ratio (SDF $< 0$) is 20.4--23.8\\\\\\\\%.\\\\n\\\\n\\\\\\\\paragraph{Gradient verification.}\\\\nWe verify SDF gradient directions via finite differences ($\\\\\\\\epsilon = 10^{-4}$) on 300 near-surface points per scene. Accuracy: 98.7\\\\\\\\% (\\\\\\\\texttt{spatial\\\\\\\\_bowl}), 99.7\\\\\\\\% (\\\\\\\\texttt{object\\\\\\\\_chocolate}). The gradient points away from obstacle surfaces, ensuring that the collision cost $\\\\\\\\text{ReLU}(-\\\\\\\\text{SDF} + m)$ correctly penalizes proximity.\\\\n\\\\n\\\\\\\\paragraph{Sign convention.}\\\\nThe pysdf library uses positive-inside convention. We apply $\\\\\\\\text{SDF} = -\\\\\\\\text{pysdf\\\\\\\\_output}$ to convert to the standard negative-inside convention. Verified: inside points yield SDF $< 0$ (cost $> 0$); outside points beyond margin yield cost $= 0$.\\\\n\\\\n\\\\n\\\\\\\\section{Training Hyperparameters}\\\\\\\\label{sec:appendix_hyperparams}\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Training and evaluation hyperparameters for all Pi0.5 experiments.}\\\\n\\\\\\\\label{tab:hyperparams}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{ll}\\\\n\\\\\\\\toprule\\\\n\\\\\\\\textbf{Training} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nBase model & Pi0.5 (PaliGemma 2B + Gemma 300M action expert) \\\\\\\\\\\\\\\\\\\\nLoRA rank (PaliGemma / Expert) & 16 / 32 \\\\\\\\\\\\\\\\\\\\nLoRA alpha (PaliGemma / Expert) & 16.0 / 32.0 \\\\\\\\\\\\\\\\\\\\nOptimizer & AdamW with cosine decay \\\\\\\\\\\\\\\\\\\\nLearning rate & $2.5 \\\\\\\\times 10^{-5}$ \\\\\\\\\\\\\\\\\\\\nBatch size & 32 \\\\\\\\\\\\\\\\\\\\nTotal training steps & 30,000 \\\\\\\\\\\\\\\\\\\\nPhase 1 (warmup, LoRA frozen) & 5,000 steps \\\\\\\\\\\\\\\\\\\\nPhase 2 (LoRA unfrozen) & 25,000 steps \\\\\\\\\\\\\\\\\\\\nSDF loss weight $\\\\\\\\lambda$ & $\\\\\\\\{0, 0.005, 0.01, 0.1\\\\\\\\}$ \\\\\\\\\\\\\\\\\\\\nSeeds per condition & 3 (except $\\\\\\\\lambda{=}0.1$: 2 at 30K) \\\\\\\\\\\\\\\\\\\\nAction horizon & 10 tokens \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\n\\\\\\\\textbf{Evaluation} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nBenchmark & SafeLIBERO Object (4 tasks) \\\\\\\\\\\\\\\\\\\\nSafety level & II \\\\\\\\\\\\\\\\\\\\nEpisodes per task & 50 \\\\\\\\\\\\\\\\\\\\nMax steps per episode & 300 \\\\\\\\\\\\\\\\\\\\nReplan interval & 5 steps \\\\\\\\\\\\\\\\\\\\nCollision threshold & 0.001\\\\\\\\,m \\\\\\\\\\\\\\\\\\\\nEvaluation seed & 7 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\n\\\\\\\\section{Evaluation Protocol and Metrics}\\\\\\\\label{sec:appendix_eval_protocol}\\\\n\\\\n\\\\\\\\paragraph{Task descriptions.}\\\\nAll four tasks require picking up a target object and placing it in a basket, amid Level-II safety obstacles. The tasks are:\\\\n\\\\\\\\begin{enumerate}[nosep]\\\\n    \\\\\\\\item \\\\\\\\texttt{chocolate\\\\\\\\_pudding}: Pick up chocolate pudding, place in basket.\\\\n    \\\\\\\\item \\\\\\\\texttt{orange\\\\\\\\_juice}: Pick up orange juice, place in basket.\\\\n    \\\\\\\\item \\\\\\\\texttt{milk}: Pick up milk, place in basket.\\\\n    \\\\\\\\item \\\\\\\\texttt{bbq\\\\\\\\_sauce}: Pick up BBQ sauce, place in basket.\\\\n\\\\\\\\end{enumerate}\\\\n\\\\n\\\\\\\\paragraph{Metrics.}\\\\n\\\\\\\\begin{itemize}[nosep]\\\\n    \\\\\\\\item \\\\\\\\textbf{TSR} (Task Success Rate): fraction of episodes where the task is completed.\\\\n    \\\\\\\\item \\\\\\\\textbf{CAR} (Collision Avoidance Rate): fraction of episodes with no collision detected (contact force $>$ 0.001\\\\\\\\,m displacement between any robot link and obstacle).\\\\n    \\\\\\\\item \\\\\\\\textbf{dfCAR} (displacement-filtered CAR): CAR computed only over episodes with EE displacement $\\\\\\\\geq \\\\\\\\tau_d$ (default $\\\\\\\\tau_d = 0.1$\\\\\\\\,mm).\\\\n    \\\\\\\\item \\\\\\\\textbf{SSR} (Safe Success Rate): fraction of episodes that are both successful and collision-free.\\\\n\\\\\\\\end{itemize}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"LoRA-only & s2 & 51.5 & 26.5 & 0.515 \\\\\\\\\\n\\\\midrule\\n$\\\\lambda{=}0.005$ & s0 & 55.5 & 30.0 & 0.541 \\\\\\\\\\n$\\\\lambda{=}0.005$ & s1 & 50.5 & 24.0 & 0.475 \\\\\\\\\\n$\\\\lambda{=}0.005$ & s2 & 56.0 & 29.5 & 0.527 \\\\\\\\\\n\\\\midrule\\n$\\\\lambda{=}0.01$ & s0 & 52.5 & 32.5 & 0.619 \\\\\\\\\\n$\\\\lambda{=}0.01$ & s1 & 55.5 & 30.0 & 0.541 \\\\\\\\\\n$\\\\lambda{=}0.01$ & s2 & 53.5 & 28.0 & 0.523 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nThe Pi0.5 baseline achieves SSR/TSR\\\\,=\\\\,0.39: most task-completing trajectories collide. After LoRA fine-tuning, SSR/TSR increases to 0.51--0.57 (mean 0.54), confirming that the CAR improvement reflects genuine avoidance among active trajectories, not reduced exposure from lower TSR. SDF conditions show comparable SSR/TSR ranges ($\\\\lambda{=}0.005$: 0.48--0.54; $\\\\lambda{=}0.01$: 0.52--0.62), reinforcing the conclusion that SDF supervision does not improve the safety profile beyond what LoRA fine-tuning provides.\\n\\n\\n\\\\section{Displacement Threshold Sensitivity}\\\\label{sec:appendix_threshold}\\n\\nThe displacement-filtered CAR (dfCAR) excludes episodes where the end-effector displacement falls below a threshold $\\\\tau_d$. Table~\\\\ref{tab:threshold_sens} demonstrates that dfCAR is robust across five orders of magnitude of $\\\\tau_d$ for all fine-tuned conditions, because these models exhibit no action collapse (all episodes have displacement $> 0.27$\\\\,m).\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{dfCAR (\\\\%) at varying displacement thresholds $\\\\tau_d$. All fine-tuned conditions (LoRA-only and SDF-augmented) show identical CAR across $\\\\tau_d \\\\in [2, 200]$\\\\,mm because no episodes exhibit sub-threshold displacement. Only at $\\\\tau_d = 300$\\\\,mm do 1--2 episodes per condition fall below threshold, causing $\\\\leq$\\\\,0.5\\\\,pp change.}\\n\\\\label{tab:threshold_sens}\\n\\\\small\\n\\\\begin{tabular}{lccccccc}\\n\\\\toprule\\n$\\\\tau_d$ (mm) & 2 & 5 & 10 & 50 & 100 & 200 & 300 \\\\\\\\\\n\\\\midrule\\nLoRA s0 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\\\\\\\\\nLoRA s1 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\\\\\\nSDF005 s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\\\\\\nSDF005 s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\\\\\\nSDF005 s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\\\\\\nSDF01 s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\\\\\\nSDF01 s1 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\\\\\\nSDF01 s2 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nFor the Pi0.5 baseline (without LoRA), all 200 episodes have EE displacement $> 0.27$\\\\,m (mean 0.37\\\\,m), so dfCAR $\\\\equiv$ CAR $= 28.5\\\\%$ at any reasonable threshold. The bimodal displacement distribution that motivates dfCAR arises in the Pi0 full fine-tuning setting (reported in the main text), where action collapse produces a mode near zero displacement.\\n\\n\\n\\\\section{Stepwise Checkpoint Ablation ($\\\\lambda{=}0.1$)}\\\\label{sec:appendix_stepwise}\\n\\nTo test whether $\\\\lambda{=}0.1$ produces a sustained training signal rather than a transient fluctuation, we evaluated six checkpoints spanning steps 16K--28K (every 2K steps) for two seeds (s0, s1). The mean CAR across these checkpoints is 55.3\\\\%, within 0.3$\\\\sigma$ of the null distribution mean (54.67\\\\%, $\\\\sigma = 2.04$). No monotonic trend is observed, and individual checkpoint CARs fluctuate within the null band. This suggests that the elevated CAR observed at the 30K checkpoint reflects stochastic variation rather than a sustained geometric-supervision effect.\\n\\n\\n\\\\section{SDF Ground Truth Pipeline}\\\\label{sec:appendix_sdf_pipeline}\\n\\n\\\\paragraph{Mesh processing.}\\nFor each SafeLIBERO scene, we extract all visual meshes from the MuJoCo XML model. The \\\\texttt{spatial\\\\_bowl} scene contains 68 meshes (19 initially watertight); \\\\texttt{object\\\\_chocolate} contains 60 meshes (13 initially watertight). We apply automated repair (hole filling, normal correction, winding order fix) via Trimesh, successfully repairing 2/49 and 4/47 non-watertight meshes respectively. Robot arm meshes (complex multi-part geometry) remain non-watertight and are excluded from SDF computation, as the SDF field targets scene obstacles only.\\n\\n\\\\paragraph{SDF computation.}\\nQuery points are sampled via dual-scale Gaussian ($\\\\sigma_1{=}0.025$, $\\\\sigma_2{=}0.008$, 80\\\\% near-surface) plus 20\\\\% uniform within the bounding box, yielding 4,084 points per scene. SDF values are truncated to $[-0.05, 0.05]$\\\\,m. Key statistics: near-surface ratio ($|$SDF$| < 0.02$) is 61.0--61.5\\\\%; inside ratio (SDF $< 0$) is 20.4--23.8\\\\%.\\n\\n\\\\paragraph{Gradient verification.}\\nWe verify SDF gradient directions via finite differences ($\\\\epsilon = 10^{-4}$) on 300 near-surface points per scene. Accuracy: 98.7\\\\% (\\\\texttt{spatial\\\\_bowl}), 99.7\\\\% (\\\\texttt{object\\\\_chocolate}). The gradient points away from obstacle surfaces, ensuring that the collision cost $\\\\text{ReLU}(-\\\\text{SDF} + m)$ correctly penalizes proximity.\\n\\n\\\\paragraph{Sign convention.}\\nThe pysdf library uses positive-inside convention. We apply $\\\\text{SDF} = -\\\\text{pysdf\\\\_output}$ to convert to the standard negative-inside convention. Verified: inside points yield SDF $< 0$ (cost $> 0$); outside points beyond margin yield cost $= 0$.\\n\\n\\n\\\\section{Training Hyperparameters}\\\\label{sec:appendix_hyperparams}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Training and evaluation hyperparameters for all Pi0.5 experiments.}\\n\\\\label{tab:hyperparams}\\n\\\\small\\n\\\\begin{tabular}{ll}\\n\\\\toprule\\n\\\\textbf{Training} \\\\\\\\\\n\\\\midrule\\nBase model & Pi0.5 (PaliGemma 2B + Gemma 300M action expert) \\\\\\\\\\nLoRA rank (PaliGemma / Expert) & 16 / 32 \\\\\\\\\\nLoRA alpha (PaliGemma / Expert) & 16.0 / 32.0 \\\\\\\\\\nOptimizer & AdamW with cosine decay \\\\\\\\\\nLearning rate & $2.5 \\\\times 10^{-5}$ \\\\\\\\\\nBatch size & 32 \\\\\\\\\\nTotal training steps & 30,000 \\\\\\\\\\nPhase 1 (warmup, LoRA frozen) & 5,000 steps \\\\\\\\\\nPhase 2 (LoRA unfrozen) & 25,000 steps \\\\\\\\\\nSDF loss weight $\\\\lambda$ & $\\\\{0, 0.005, 0.01, 0.1\\\\}$ \\\\\\\\\\nSeeds per condition & 3 (except $\\\\lambda{=}0.1$: 2 at 30K) \\\\\\\\\\nAction horizon & 10 tokens \\\\\\\\\\n\\\\midrule\\n\\\\textbf{Evaluation} \\\\\\\\\\n\\\\midrule\\nBenchmark & SafeLIBERO Object (4 tasks) \\\\\\\\\\nSafety level & II \\\\\\\\\\nEpisodes per task & 50 \\\\\\\\\\nMax steps per episode & 300 \\\\\\\\\\nReplan interval & 5 steps \\\\\\\\\\nCollision threshold & 0.001\\\\,m \\\\\\\\\\nEvaluation seed & 7 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\n\\\\section{Evaluation Protocol and Metrics}\\\\label{sec:appendix_eval_protocol}\\n\\n\\\\paragraph{Task descriptions.}\\nAll four tasks require picking up a target object and placing it in a basket, amid Level-II safety obstacles. The tasks are:\\n\\\\begin{enumerate}[nosep]\\n    \\\\item \\\\texttt{chocolate\\\\_pudding}: Pick up chocolate pudding, place in basket.\\n    \\\\item \\\\texttt{orange\\\\_juice}: Pick up orange juice, place in basket.\\n    \\\\item \\\\texttt{milk}: Pick up milk, place in basket.\\n    \\\\item \\\\texttt{bbq\\\\_sauce}: Pick up BBQ sauce, place in basket.\\n\\\\end{enumerate}\\n\\n\\\\paragraph{Metrics.}\\n\\\\begin{itemize}[nosep]\\n    \\\\item \\\\textbf{TSR} (Task Success Rate): fraction of episodes where the task is completed.\\n    \\\\item \\\\textbf{CAR} (Collision Avoidance Rate): fraction of episodes with no collision detected (contact force $>$ 0.001\\\\,m displacement between any robot link and obstacle).\\n    \\\\item \\\\textbf{dfCAR} (displacement-filtered CAR): CAR computed only over episodes with EE displacement $\\\\geq \\\\tau_d$ (default $\\\\tau_d = 0.1$\\\\,mm).\\n    \\\\item \\\\textbf{SSR} (Safe Success Rate): fraction of episodes that are both successful and collision-free.\\n\\\\end{itemize}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012XVfscf2PqpYZAy8jCe6BL`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -rn \"0.039\" /root/colliforce-vla/docs/paper/",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "a38938c2-d204-4c26-b581-fcd73ee1555e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKWzrzQnDeRiRM7WATiLxT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 33553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 645
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

_source line 34 · 2026-05-27T23:40:08.075Z_

<details><summary>↩ Tool result · `toolu_012XVfscf2PqpYZAy8jCe6BL`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "38fc0b8f-ea2d-462e-958d-be5fecf7d384",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GNZvWGUfa9qr9jZDHZYxJR`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -rn \"0.025\" /root/colliforce-vla/docs/paper/",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "cb935dd3-0f1f-4169-879d-cf1b96a7e08a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKWzrzQnDeRiRM7WATiLxT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 33553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 645
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

_source line 36 · 2026-05-27T23:40:08.694Z_

<details><summary>↩ Tool result · `toolu_01GNZvWGUfa9qr9jZDHZYxJR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/colliforce-vla/docs/paper/appendix.tex:190:Query points are sampled via dual-scale Gaussian ($\\\\sigma_1{=}0.025$, $\\\\sigma_2{=}0.008$, 80\\\\% near-surface) plus 20\\\\% uniform within the bounding box, yielding 4,084 points per scene. SDF values are truncated to $[-0.05, 0.05]$\\\\,m. Key statistics: near-surface ratio ($|$SDF$| < 0.02$) is 61.0--61.5\\\\%; inside ratio (SDF $< 0$) is 20.4--23.8\\\\%.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "a706645f-1aed-4249-8a17-3d74ceae1813",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/colliforce-vla/docs/paper/appendix.tex:190:Query points are sampled via dual-scale Gaussian ($\\\\\\\\sigma_1{=}0.025$, $\\\\\\\\sigma_2{=}0.008$, 80\\\\\\\\% near-surface) plus 20\\\\\\\\% uniform within the bounding box, yielding 4,084 points per scene. SDF values are truncated to $[-0.05, 0.05]$\\\\\\\\,m. Key statistics: near-surface ratio ($|$SDF$| < 0.02$) is 61.0--61.5\\\\\\\\%; inside ratio (SDF $< 0$) is 20.4--23.8\\\\\\\\%.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/colliforce-vla/docs/paper/appendix.tex:190:Query points are sampled via dual-scale Gaussian ($\\\\sigma_1{=}0.025$, $\\\\sigma_2{=}0.008$, 80\\\\% near-surface) plus 20\\\\% uniform within the bounding box, yielding 4,084 points per scene. SDF values are truncated to $[-0.05, 0.05]$\\\\,m. Key statistics: near-surface ratio ($|$SDF$| < 0.02$) is 61.0--61.5\\\\%; inside ratio (SDF $< 0$) is 20.4--23.8\\\\%.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Na7y72EbGs4Q2iJfCHUthA`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -rn \"z=1.76\\|z = 1.76\\|z=1\\.76\" /root/colliforce-vla/docs/paper/",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "2e48dcb9-90fe-445d-b3f7-1d5a18beb65f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKWzrzQnDeRiRM7WATiLxT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 33553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 645
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

_source line 38 · 2026-05-27T23:40:08.933Z_

<details><summary>↩ Tool result · `toolu_01Na7y72EbGs4Q2iJfCHUthA`</summary>

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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "0a9e26f5-d60e-4d86-90ef-5fb2aa8bcc3c",
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

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Let me also check for the stale values more carefully. "0.039" was not found (no matches). "0.025" was found but only in the SDF computation section (Gaussian sigma), which is legitimate. Let me check for "z=1.76" and "z = 1.76" without piping.

Also, let me check the baseline numbers more carefully. The appendix table shows baseline CAR = 28.5% and TSR = 71.5%, but the main table (claim3.tex) shows baseline CAR = 26.8% ± 1.6% and TSR = 74.7% ± 1.5%. 

These discrepancies make sense now—the appendix reports a single evaluation while the main table averages across three seeds. The appendix baseline shows 28.5% CAR and 71.5% TSR for one run, whereas the 3-seed average in the main table is 26.8±1.6% CAR and 74.7±1.5% TSR.

But there's something odd here. The threshold sensitivity section claims the baseline CAR is 28.5%, which matches the single evaluation from the appendix, not the 3-seed average of 26.8%. That's a notable inconsistency I should flag.

Actually, looking more carefully at the numbers: the main table shows baseline EE displacement of 0.367 m, and the appendix says "mean 0.37 m" — those align fine. For the LoRA-only results, the per-seed values in the appendix (57.0, 52.5, 55.0) match the registry, and the mean of 54.83 checks out arithmetically.

Now I'm verifying the standard deviation calculations and the λ=0.005 condition results to make sure those numbers are consistent too. For λ=0.1 with only two samples, the mean is 58.25 and the standard deviation works out to about 0.35. Now I'm calculating the pooled null distribution across all the samples to get a baseline mean of 54.667 and then computing the overall variance.

With those values established, I'm verifying the key claims: the difference of 0.33 percentage points checks out, the ~28 percentage point gap between the two conditions is confirmed, and the p-values match what's reported—0.071 for the two-tailed test and 0.036 for the one-tailed version.

Now I'm running into some issues with cross-referencing. The oracle reduction claim of 6-10 percentage points comes from a section I don't have access to, so I can't verify that directly. Similarly, the abstract mentions 91.5% CAR and 99.6% safe episodes related to Pi0 action collapse, but that's in another section I'm missing.

Looking at the SSR/TSR ratio claims, there's a discrepancy I'm catching: the main text says it increases from 0.33 baseline to 0.51-0.57, but when I check the appendix, the baseline appears to be 0.39, not 0.33. This inconsistency needs clarification. I'm trying to figure out which baseline values are correct—the main text claims 0.33 but the appendix shows 0.39, and I need to reconcile this by checking the actual SSR table in the appendix since the numbers don't match up. The main results table gives TSR around 74.7% and CAR around 26.8%, which would put SSR/TSR closer to 0.33, so I need to see the full appendix SSR breakdown to understand where the discrepancy is coming from.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "5752ac49-3283-4ed7-959d-b7870d2124e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9jYaZXwig1AJVQPcCczJm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4334,
      "cache_read_input_tokens": 34198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4334
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 40_

Let me check some specific values more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "7fa3c0e5-3ed9-439b-8d94-ac78b36eab1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9jYaZXwig1AJVQPcCczJm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4334,
      "cache_read_input_tokens": 34198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4334
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EE9BraXkPa1HpwjMLsPGkG`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -rn \"z=1.76\\|z =1.76\\|z= 1.76\\|z = 1.76\" /root/colliforce-vla/docs/paper/",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "ef934eb2-c761-4565-ade7-f3c1effb57d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9jYaZXwig1AJVQPcCczJm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4334,
      "cache_read_input_tokens": 34198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4334
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-27T23:40:51.229Z_

<details><summary>↩ Tool result · `toolu_01EE9BraXkPa1HpwjMLsPGkG`</summary>

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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "9d23142f-d7f8-4d85-a04d-dcdd9a8bfccc",
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

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011bFs2BzCgEq76HauPTU5rY`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -rn \"0\\.039\" /root/colliforce-vla/docs/paper/",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "505a9402-0b9b-4b54-b0e3-72ed828370af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9jYaZXwig1AJVQPcCczJm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4334,
      "cache_read_input_tokens": 34198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4334
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-27T23:40:52.660Z_

<details><summary>↩ Tool result · `toolu_011bFs2BzCgEq76HauPTU5rY`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "93faea7d-ef6c-4c63-88e2-0f7c69544580",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017NxZEqxWDziXrEDBtnycen`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -n \"0.33\\|SSR\" /root/colliforce-vla/docs/paper/claim3.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "11b96ef1-3922-4d0e-bc4f-99b3a799b66b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9jYaZXwig1AJVQPcCczJm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4334,
      "cache_read_input_tokens": 34198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4334
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-27T23:40:52.973Z_

<details><summary>↩ Tool result · `toolu_017NxZEqxWDziXrEDBtnycen`</summary>

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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "ebbc426d-fa2f-4aeb-abab-46944c49d513",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DNRD51DDC5o81hfaUPog9m`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -n \"0.33\\|0.39\\|SSR\" /root/colliforce-vla/docs/paper/appendix.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "a8f025bc-b802-43d1-9f9a-469dd130fe45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9jYaZXwig1AJVQPcCczJm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4334,
      "cache_read_input_tokens": 34198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4334
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-27T23:40:53.647Z_

<details><summary>↩ Tool result · `toolu_01DNRD51DDC5o81hfaUPog9m`</summary>

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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "83df9496-3729-4474-b550-afe4cb108e9f",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DfUbULzdSzQEefuFmGmUWL`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -n \"0.33\" /root/colliforce-vla/docs/paper/claim3.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "c7abce42-359a-4403-a869-d17843d55ac7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Bqp9i7RQfBYbasPWHF1MN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3343,
      "cache_read_input_tokens": 38532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3343
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

_source line 50 · 2026-05-27T23:40:57.468Z_

<details><summary>↩ Tool result · `toolu_01DfUbULzdSzQEefuFmGmUWL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"27:Table~\\\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\\\sim}$28 percentage points (26.8\\\\% $\\\\to$ 54.83\\\\%) with zero frozen episodes and displacement above 0.37\\\\,m, which confirms genuine avoidance. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.83\\\\%) is within 0.33\\\\,pp of $\\\\lambda = 0.005$ and statistically indistinguishable from $\\\\lambda = 0.01$ (56.33\\\\%, $p > 0.1$; Appendix~\\\\ref{sec:appendix_null}). A Phase~2 ablation ($\\\\lambda = 0$ after step 5K) yields CAR\\\\,=\\\\,57.5\\\\%\\\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}; SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\\\_pudding highest, bbq\\\\_sauce lowest; Figure~\\\\ref{fig:pertask_fingerprint}) and invariant to $\\\\lambda$ across a 20$\\\\times$ range; avoidance patterns reflect the demonstration distribution rather than geometric supervision.\\n30:Fine-tuning degrades TSR by ${\\\\sim}$21--25\\\\,pp (74.7\\\\% $\\\\to$ 49.7--54.0\\\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\\\,0.37\\\\,m displacement and 0\\\\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.57 (Appendix~\\\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "a5f45f03-1727-419f-a0a7-655274fe4da7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"27:Table~\\\\\\\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\\\\\\\sim}$28 percentage points (26.8\\\\\\\\% $\\\\\\\\to$ 54.83\\\\\\\\%) with zero frozen episodes and displacement above 0.37\\\\\\\\,m, which confirms genuine avoidance. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.83\\\\\\\\%) is within 0.33\\\\\\\\,pp of $\\\\\\\\lambda = 0.005$ and statistically indistinguishable from $\\\\\\\\lambda = 0.01$ (56.33\\\\\\\\%, $p > 0.1$; Appendix~\\\\\\\\ref{sec:appendix_null}). A Phase~2 ablation ($\\\\\\\\lambda = 0$ after step 5K) yields CAR\\\\\\\\,=\\\\\\\\,57.5\\\\\\\\%\\\\\\\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}; SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\\\\\\\_pudding highest, bbq\\\\\\\\_sauce lowest; Figure~\\\\\\\\ref{fig:pertask_fingerprint}) and invariant to $\\\\\\\\lambda$ across a 20$\\\\\\\\times$ range; avoidance patterns reflect the demonstration distribution rather than geometric supervision.\\\\n30:Fine-tuning degrades TSR by ${\\\\\\\\sim}$21--25\\\\\\\\,pp (74.7\\\\\\\\% $\\\\\\\\to$ 49.7--54.0\\\\\\\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\\\\\\\,0.37\\\\\\\\,m displacement and 0\\\\\\\\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.57 (Appendix~\\\\\\\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"27:Table~\\\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\\\sim}$28 percentage points (26.8\\\\% $\\\\to$ 54.83\\\\%) with zero frozen episodes and displacement above 0.37\\\\,m, which confirms genuine avoidance. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.83\\\\%) is within 0.33\\\\,pp of $\\\\lambda = 0.005$ and statistically indistinguishable from $\\\\lambda = 0.01$ (56.33\\\\%, $p > 0.1$; Appendix~\\\\ref{sec:appendix_null}). A Phase~2 ablation ($\\\\lambda = 0$ after step 5K) yields CAR\\\\,=\\\\,57.5\\\\%\\\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}; SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\\\_pudding highest, bbq\\\\_sauce lowest; Figure~\\\\ref{fig:pertask_fingerprint}) and invariant to $\\\\lambda$ across a 20$\\\\times$ range; avoidance patterns reflect the demonstration distribution rather than geometric supervision.\\n30:Fine-tuning degrades TSR by ${\\\\sim}$21--25\\\\,pp (74.7\\\\% $\\\\to$ 49.7--54.0\\\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\\\,0.37\\\\,m displacement and 0\\\\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.57 (Appendix~\\\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014g45arHitJJKXGen7Zxzum`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -n \"SSR\" /root/colliforce-vla/docs/paper/claim3.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "41e2fb9e-9a51-49fd-813a-af658cf45920",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Bqp9i7RQfBYbasPWHF1MN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3343,
      "cache_read_input_tokens": 38532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3343
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

_source line 52 · 2026-05-27T23:40:58.416Z_

<details><summary>↩ Tool result · `toolu_014g45arHitJJKXGen7Zxzum`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"30:Fine-tuning degrades TSR by ${\\\\sim}$21--25\\\\,pp (74.7\\\\% $\\\\to$ 49.7--54.0\\\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\\\,0.37\\\\,m displacement and 0\\\\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.57 (Appendix~\\\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "9bf222c7-ec8d-4f6f-b4a7-a4ddcbd174fe",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"30:Fine-tuning degrades TSR by ${\\\\\\\\sim}$21--25\\\\\\\\,pp (74.7\\\\\\\\% $\\\\\\\\to$ 49.7--54.0\\\\\\\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\\\\\\\,0.37\\\\\\\\,m displacement and 0\\\\\\\\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.57 (Appendix~\\\\\\\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"30:Fine-tuning degrades TSR by ${\\\\sim}$21--25\\\\,pp (74.7\\\\% $\\\\to$ 49.7--54.0\\\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\\\,0.37\\\\,m displacement and 0\\\\% frozen episodes). The SSR/TSR ratio increases from 0.33 (baseline) to 0.51--0.57 (Appendix~\\\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013za8egboe1mCSxLAXXNagG`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -n \"0.33\" /root/colliforce-vla/docs/paper/appendix.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "afd0c03f-84ae-412f-8700-745d34fceaa8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Bqp9i7RQfBYbasPWHF1MN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3343,
      "cache_read_input_tokens": 38532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3343
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

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KShMrt9fj8KJFqqSHkmLZg`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -n \"SSR\" /root/colliforce-vla/docs/paper/appendix.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "9c79eb64-8056-4ad7-a8a7-33c215ba39c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Bqp9i7RQfBYbasPWHF1MN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3343,
      "cache_read_input_tokens": 38532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3343
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

_source line 55 · 2026-05-27T23:40:59.355Z_

<details><summary>↩ Tool result · `toolu_013za8egboe1mCSxLAXXNagG`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "5aa978ee-e71f-47fd-afde-b3841ab3ea14",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-27T23:40:59.884Z_

<details><summary>↩ Tool result · `toolu_01KShMrt9fj8KJFqqSHkmLZg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"118:\\\\section{SSR/TSR Ratio Analysis}\\\\label{sec:appendix_ssr}\\n120:The Safe Success Rate (SSR) counts episodes that are both task-successful \\\\emph{and} collision-free. The SSR/TSR ratio measures what fraction of task-completing episodes also avoid collisions. An increase indicates that fine-tuning improves safety among successful trajectories, not merely by suppressing task completion.\\n124:\\\\caption{SSR/TSR ratio across conditions. All values computed over 200 episodes (50 per task $\\\\times$ 4 tasks).}\\n129:Condition & Seed & TSR (\\\\%) & SSR (\\\\%) & SSR/TSR \\\\\\\\\\n148:The Pi0.5 baseline achieves SSR/TSR\\\\,=\\\\,0.39: most task-completing trajectories collide. After LoRA fine-tuning, SSR/TSR increases to 0.51--0.57 (mean 0.54), confirming that the CAR improvement reflects genuine avoidance among active trajectories, not reduced exposure from lower TSR. SDF conditions show comparable SSR/TSR ranges ($\\\\lambda{=}0.005$: 0.48--0.54; $\\\\lambda{=}0.01$: 0.52--0.62), reinforcing the conclusion that SDF supervision does not improve the safety profile beyond what LoRA fine-tuning provides.\\n253:    \\\\item \\\\textbf{SSR} (Safe Success Rate): fraction of episodes that are both successful and collision-free.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "cbb5876e-89c2-4702-a130-e39744f07b92",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"118:\\\\\\\\section{SSR/TSR Ratio Analysis}\\\\\\\\label{sec:appendix_ssr}\\\\n120:The Safe Success Rate (SSR) counts episodes that are both task-successful \\\\\\\\emph{and} collision-free. The SSR/TSR ratio measures what fraction of task-completing episodes also avoid collisions. An increase indicates that fine-tuning improves safety among successful trajectories, not merely by suppressing task completion.\\\\n124:\\\\\\\\caption{SSR/TSR ratio across conditions. All values computed over 200 episodes (50 per task $\\\\\\\\times$ 4 tasks).}\\\\n129:Condition & Seed & TSR (\\\\\\\\%) & SSR (\\\\\\\\%) & SSR/TSR \\\\\\\\\\\\\\\\\\\\n148:The Pi0.5 baseline achieves SSR/TSR\\\\\\\\,=\\\\\\\\,0.39: most task-completing trajectories collide. After LoRA fine-tuning, SSR/TSR increases to 0.51--0.57 (mean 0.54), confirming that the CAR improvement reflects genuine avoidance among active trajectories, not reduced exposure from lower TSR. SDF conditions show comparable SSR/TSR ranges ($\\\\\\\\lambda{=}0.005$: 0.48--0.54; $\\\\\\\\lambda{=}0.01$: 0.52--0.62), reinforcing the conclusion that SDF supervision does not improve the safety profile beyond what LoRA fine-tuning provides.\\\\n253:    \\\\\\\\item \\\\\\\\textbf{SSR} (Safe Success Rate): fraction of episodes that are both successful and collision-free.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"118:\\\\section{SSR/TSR Ratio Analysis}\\\\label{sec:appendix_ssr}\\n120:The Safe Success Rate (SSR) counts episodes that are both task-successful \\\\emph{and} collision-free. The SSR/TSR ratio measures what fraction of task-completing episodes also avoid collisions. An increase indicates that fine-tuning improves safety among successful trajectories, not merely by suppressing task completion.\\n124:\\\\caption{SSR/TSR ratio across conditions. All values computed over 200 episodes (50 per task $\\\\times$ 4 tasks).}\\n129:Condition & Seed & TSR (\\\\%) & SSR (\\\\%) & SSR/TSR \\\\\\\\\\n148:The Pi0.5 baseline achieves SSR/TSR\\\\,=\\\\,0.39: most task-completing trajectories collide. After LoRA fine-tuning, SSR/TSR increases to 0.51--0.57 (mean 0.54), confirming that the CAR improvement reflects genuine avoidance among active trajectories, not reduced exposure from lower TSR. SDF conditions show comparable SSR/TSR ranges ($\\\\lambda{=}0.005$: 0.48--0.54; $\\\\lambda{=}0.01$: 0.52--0.62), reinforcing the conclusion that SDF supervision does not improve the safety profile beyond what LoRA fine-tuning provides.\\n253:    \\\\item \\\\textbf{SSR} (Safe Success Rate): fraction of episodes that are both successful and collision-free.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VMcWFH1pe9C2eoC3zcwe5X`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -n \"0.39\" /root/colliforce-vla/docs/paper/appendix.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "a9a2bf18-579c-4324-adee-51330f20ab0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Bqp9i7RQfBYbasPWHF1MN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3343,
      "cache_read_input_tokens": 38532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3343
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

_source line 58 · 2026-05-27T23:41:00.825Z_

<details><summary>↩ Tool result · `toolu_01VMcWFH1pe9C2eoC3zcwe5X`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"131:Pi0.5 baseline & -- & 71.5 & 28.0 & 0.392 \\\\\\\\\\n148:The Pi0.5 baseline achieves SSR/TSR\\\\,=\\\\,0.39: most task-completing trajectories collide. After LoRA fine-tuning, SSR/TSR increases to 0.51--0.57 (mean 0.54), confirming that the CAR improvement reflects genuine avoidance among active trajectories, not reduced exposure from lower TSR. SDF conditions show comparable SSR/TSR ranges ($\\\\lambda{=}0.005$: 0.48--0.54; $\\\\lambda{=}0.01$: 0.52--0.62), reinforcing the conclusion that SDF supervision does not improve the safety profile beyond what LoRA fine-tuning provides.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "b8ad7ea1-9e26-458e-b674-b220902b05ab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"131:Pi0.5 baseline & -- & 71.5 & 28.0 & 0.392 \\\\\\\\\\\\\\\\\\\\n148:The Pi0.5 baseline achieves SSR/TSR\\\\\\\\,=\\\\\\\\,0.39: most task-completing trajectories collide. After LoRA fine-tuning, SSR/TSR increases to 0.51--0.57 (mean 0.54), confirming that the CAR improvement reflects genuine avoidance among active trajectories, not reduced exposure from lower TSR. SDF conditions show comparable SSR/TSR ranges ($\\\\\\\\lambda{=}0.005$: 0.48--0.54; $\\\\\\\\lambda{=}0.01$: 0.52--0.62), reinforcing the conclusion that SDF supervision does not improve the safety profile beyond what LoRA fine-tuning provides.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"131:Pi0.5 baseline & -- & 71.5 & 28.0 & 0.392 \\\\\\\\\\n148:The Pi0.5 baseline achieves SSR/TSR\\\\,=\\\\,0.39: most task-completing trajectories collide. After LoRA fine-tuning, SSR/TSR increases to 0.51--0.57 (mean 0.54), confirming that the CAR improvement reflects genuine avoidance among active trajectories, not reduced exposure from lower TSR. SDF conditions show comparable SSR/TSR ranges ($\\\\lambda{=}0.005$: 0.48--0.54; $\\\\lambda{=}0.01$: 0.52--0.62), reinforcing the conclusion that SDF supervision does not improve the safety profile beyond what LoRA fine-tuning provides.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012mywC5oPCSbg2b71n6MaLA`</summary>

```json
{
  "server": "westd-45947",
  "command": "grep -n \"z=1\" /root/colliforce-vla/docs/paper/appendix.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "0d7513b7-076a-4d8f-9455-c04aa0365fa5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Bqp9i7RQfBYbasPWHF1MN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3343,
      "cache_read_input_tokens": 38532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3343
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

_source line 60 · 2026-05-27T23:41:01.636Z_

<details><summary>↩ Tool result · `toolu_012mywC5oPCSbg2b71n6MaLA`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "9ce90843-574f-4c56-8205-fdf8f222a1e5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
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
Now I have a clear picture. Let me get the full SSR table from the appendix to check SSR/TSR values more carefully.

Key finding: 
- claim3.tex says "SSR/TSR ratio increases from 0.33 (baseline)"
- appendix.tex says "Pi0.5 baseline achieves SSR/TSR = 0.39" and the table shows SSR/TSR = 0.392

This is an INCONSISTENCY. The appendix table shows 0.392 (≈0.39), but the main text says 0.33.


I'm realizing the baseline might be evaluated differently—the appendix shows a single evaluation with TSR=71.5, while the main text's 3-seed baseline has TSR≈74.7, so these could be different runs. But the main text claims SSR/TSR = 0.33 for baseline, which doesn't match either the appendix single evaluation (0.392) or what I'd calculate from the 3-seed numbers. I'm seeing the same 0.33 baseline value repeated in both the main text and discussion sections, but when I calculate from the appendix table—dividing 28.0 by 71.5—I get approximately 0.39, which doesn't match. This is a genuine inconsistency between what the text claims and what the actual data shows. The appendix also contains per-task baseline metrics like the chocolate_pudding CAR value of 60.

Looking at the per-task breakdown, the individual task results average to CAR=28.5 and TSR=71.5, which differs from the main table's reported baseline of CAR=26.8±1.6 and TSR=74.7±1.5 across three seeds. The appendix notes this is a single evaluation while the main table represents a 3-seed average, which explains the discrepancy, but there's still a mismatch in how the baseline values are being reported across different sections. Looking at the LoRA-only results, I see SSR/TSR = 0.515 from the appendix table, which aligns with the text's reported range of 0.51-0.57. Now I'm verifying the specific numerical claims: the 0.33 pp difference between LoRA-only and λ=0.005 checks out (54.83 - 54.5), and the ~3.6 pp improvement from λ=0.1 over the null mean also validates (58.25 - 54.67 ≈ 3.58).

For the stepwise mean of 55.3%, this matches across the paper and appendix, though I can't verify against raw data. The 0.3σ claim holds when I divide the difference from null mean by the standard deviation (0.63 / 2.04 ≈ 0.309). The TSR degradation range of 21-25 pp is also correct—baseline drops from 74.7 to either 49.7 with LoRA-only or 54.0 with λ=0.005, giving the stated range.

Now checking the "49.7--54.0%" range for fine-tuned TSR values. The paper lists 49.7 for LoRA-only, 54.0 at λ=0.005, 53.8 at λ=0.01, and 48.0 at λ=0.1. The text specifies 49.7--54.0% without including the λ=0.1 result, which would actually lower the minimum to 48.0. This suggests the range might be selectively reported or the λ=0.1 condition is being treated separately in context. Looking at Table 1 more carefully, the TSR values show 49.7 for LoRA, 54.0 at λ=0.005, 53.8 at λ=0.01, and 48.0 at λ=0.1—so the stated range of 49.7–54.0 pp deliberately excludes the λ=0.1 condition, which would represent a 26.7 pp degradation and fall outside that range. This appears to be an editorial choice rather than a numerical error, though it's worth flagging as a minor inconsistency in how the trade-off is presented. 57.0 from the per-task calculations, but the threshold table shows 56.5 for LoRA s0—this discrepancy shouldn't exist if dfCAR equals CAR when no episodes fall below the displacement threshold, as the text claims. I'm calculating the mean CAR across tasks for LoRA seed 0, which gives 57.0, but the dfCAR table shows 56.5 — suggesting these metrics might be computed differently. The per-task CAR values could represent percentages of 50 episodes each, so I'm checking whether dfCAR uses a different aggregation method, like total collision-free episodes across all episodes meeting the displacement threshold divided by total episodes. are all exact integers, so the total should be 114 out of 200, which is 57.0%. But the dfCAR pooled rate shows 56.5%, or 113 out of 200—off by one episode. I'm wondering if this is a real discrepancy or if the threshold table is pulling from a different checkpoint. Looking more closely, the threshold table only includes LoRA s0 and s1, while the per-task breakdown has s0, s1, and s2, so there might be a seed mismatch between the two tables.

Checking the full threshold table, I notice LoRA is missing s2 entirely while SDF005 and SDF01 both have all three seeds. The per-task LoRA values are s0=57.0, s1=52.5, s2=55.0, but the threshold table shows s0=56.5 and s1=52.5—so LoRA s0 doesn't match between the two sources, though s1 does. Meanwhile, SDF005 and SDF01 match perfectly across both tables for all their seeds.

Now I'm verifying the main table CAR values against the per-task calculations. The LoRA-only mean of 54.83 ± 2.25 matches exactly when I compute it from the three per-task seeds, and I'm checking whether the λ=0.005 entry also aligns with its per-task data. Continuing to verify the per-task means across the different configurations—checking milk, orange juice, and bbq sauce for the LoRA table, then moving through the λ=0.005 results to confirm they match the reported values. Now I'm verifying the per-seed means across both lambda values, checking that each seed's average matches the expected totals.

Building the null distribution by pooling results from the baseline LoRA and λ=0.005 conditions, then calculating the mean and variance to establish the statistical baseline for comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "07a8bccd-872e-41b6-b431-efe1b06b18b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K7EDL16ZFii8nasmYgNWqT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2514,
      "cache_read_input_tokens": 41875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2514
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

Let me get the full SSR table from the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "6ce5d495-aced-44dd-868a-5c58c965b41d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K7EDL16ZFii8nasmYgNWqT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2514,
      "cache_read_input_tokens": 41875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2514
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01U1xxoKkeCkF8fmoMinGTYB`</summary>

```json
{
  "server": "westd-45947",
  "command": "head -155 /root/colliforce-vla/docs/paper/appendix.tex",
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
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "11b4a7bc-af7a-4511-8366-e43672069620",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K7EDL16ZFii8nasmYgNWqT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2514,
      "cache_read_input_tokens": 41875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2514
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-27T23:42:31.072Z_

<details><summary>↩ Tool result · `toolu_01U1xxoKkeCkF8fmoMinGTYB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\appendix\\n\\n\\\\section{Per-Task Collision Avoidance Rates}\\\\label{sec:appendix_pertask}\\n\\nTable~\\\\ref{tab:pertask_lora} reports per-task CAR for LoRA-only fine-tuning across three seeds. The ordering is consistent: \\\\texttt{chocolate\\\\_pudding} highest, \\\\texttt{bbq\\\\_sauce} lowest. This ordering is invariant across all SDF conditions (Tables~\\\\ref{tab:pertask_l005}--\\\\ref{tab:pertask_l01}), confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR (\\\\%) for LoRA-only fine-tuning (no SDF), 30K checkpoint. Overall: 54.83\\\\,$\\\\pm$\\\\,2.25.}\\n\\\\label{tab:pertask_lora}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 74 & 68 & 76 & 72.67 \\\\\\\\\\nmilk & 66 & 72 & 62 & 66.67 \\\\\\\\\\norange\\\\_juice & 68 & 54 & 56 & 59.33 \\\\\\\\\\nbbq\\\\_sauce & 20 & 16 & 26 & 20.67 \\\\\\\\\\n\\\\midrule\\nPer-seed mean & 57.0 & 52.5 & 55.0 & 54.83 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR (\\\\%) for LoRA+SDF $\\\\lambda{=}0.005$, 30K checkpoint. Overall: 54.5\\\\,$\\\\pm$\\\\,2.29.}\\n\\\\label{tab:pertask_l005}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 74 & 70 & 74 & 72.67 \\\\\\\\\\nmilk & 74 & 68 & 72 & 71.33 \\\\\\\\\\norange\\\\_juice & 52 & 64 & 46 & 54.00 \\\\\\\\\\nbbq\\\\_sauce & 28 & 14 & 18 & 20.00 \\\\\\\\\\n\\\\midrule\\nPer-seed mean & 57.0 & 54.0 & 52.5 & 54.50 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR (\\\\%) for LoRA+SDF $\\\\lambda{=}0.01$, 30K checkpoint. Overall: 56.33\\\\,$\\\\pm$\\\\,1.61.}\\n\\\\label{tab:pertask_l01}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 74 & 76 & 68 & 72.67 \\\\\\\\\\nmilk & 72 & 72 & 72 & 72.00 \\\\\\\\\\norange\\\\_juice & 48 & 60 & 64 & 57.33 \\\\\\\\\\nbbq\\\\_sauce & 34 & 22 & 14 & 23.33 \\\\\\\\\\n\\\\midrule\\nPer-seed mean & 57.0 & 57.5 & 54.5 & 56.33 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR and TSR (\\\\%) for the Pi0.5 pre-trained baseline (no fine-tuning, single evaluation). Overall CAR: 28.5\\\\%, TSR: 71.5\\\\%.}\\n\\\\label{tab:pertask_baseline}\\n\\\\small\\n\\\\begin{tabular}{lcc}\\n\\\\toprule\\nTask & CAR & TSR \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 60 & 80 \\\\\\\\\\norange\\\\_juice & 16 & 74 \\\\\\\\\\nbbq\\\\_sauce & 32 & 66 \\\\\\\\\\nmilk & 6 & 66 \\\\\\\\\\n\\\\midrule\\nMean & 28.5 & 71.5 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nThe per-task pattern reveals why \\\\texttt{bbq\\\\_sauce} is hardest: the BBQ sauce bottle is positioned behind a cluster of tall obstacles (moka pot, wine bottle), requiring the end-effector to navigate through a narrow corridor. \\\\texttt{chocolate\\\\_pudding}, placed at the front of the basket with fewer obstructions, is easiest. This ordering is consistent across all $\\\\lambda$ values, including a $20\\\\times$ range from 0.005 to 0.1 (Tables~\\\\ref{tab:pertask_l005}--\\\\ref{tab:pertask_l01}), confirming that task difficulty is determined by demonstration trajectory distribution rather than SDF loss weight.\\n\\n\\n\\\\section{Null Distribution and Permutation Test}\\\\label{sec:appendix_null}\\n\\nWe construct the null distribution from all conditions where SDF supervision is either absent or demonstrably redundant ($p > 0.1$ versus LoRA-only). This yields six per-seed CAR values: three LoRA-only seeds and three $\\\\lambda{=}0.005$ seeds (Table~\\\\ref{tab:null_dist}).\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Null distribution construction. Values are per-seed overall CAR (\\\\%) at the 30K checkpoint.}\\n\\\\label{tab:null_dist}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nCondition & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nLoRA-only & 57.0 & 52.5 & 55.0 & 54.83 \\\\\\\\\\nLoRA+SDF $\\\\lambda{=}0.005$ & 57.0 & 54.0 & 52.5 & 54.50 \\\\\\\\\\n\\\\midrule\\n\\\\multicolumn{4}{l}{Pooled null: $\\\\{57.0, 52.5, 55.0, 57.0, 54.0, 52.5\\\\}$} \\\\\\\\\\n\\\\multicolumn{4}{l}{$\\\\mu_0 = 54.67$, $\\\\sigma_0 = 2.04$} \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\paragraph{Permutation test procedure.}\\nFor each treatment condition (e.g., $\\\\lambda{=}0.1$, $k$ seeds), we enumerate all $\\\\binom{6+k}{k}$ ways to draw $k$ values from the combined pool of null + treatment values. The one-tailed $p$-value is the fraction of combinations whose mean $\\\\geq$ the observed treatment mean; the two-tailed $p$-value counts combinations whose deviation from the pooled mean exceeds the observed deviation.\\n\\n\\\\paragraph{Results for $\\\\lambda{=}0.01$ (3 seeds).}\\nTreatment values: $\\\\{57.0, 57.5, 54.5\\\\}$, mean = 56.33. Pooled with null: 9 values, $\\\\binom{9}{3} = 84$ combinations. The observed mean (56.33) is within the null range ($p > 0.1$, two-tailed), confirming no significant departure.\\n\\n\\\\paragraph{Results for $\\\\lambda{=}0.1$ (2 seeds).}\\nTreatment values: $\\\\{58.0, 58.5\\\\}$, mean = 58.25. Pooled with null: 8 values, $\\\\binom{8}{2} = 28$ combinations. One-tailed $p = 0.036$; two-tailed $p \\\\approx 0.071$. The $z$-score relative to the null is $(58.25 - 54.67)/2.04 = 1.76$. We report the conservative two-tailed value in the main text; a directional prior is justified because SDF is designed to \\\\emph{reduce} collisions.\\n\\n\\n\\\\section{SSR/TSR Ratio Analysis}\\\\label{sec:appendix_ssr}\\n\\nThe Safe Success Rate (SSR) counts episodes that are both task-successful \\\\emph{and} collision-free. The SSR/TSR ratio measures what fraction of task-completing episodes also avoid collisions. An increase indicates that fine-tuning improves safety among successful trajectories, not merely by suppressing task completion.\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{SSR/TSR ratio across conditions. All values computed over 200 episodes (50 per task $\\\\times$ 4 tasks).}\\n\\\\label{tab:ssr_tsr}\\n\\\\small\\n\\\\begin{tabular}{lccccc}\\n\\\\toprule\\nCondition & Seed & TSR (\\\\%) & SSR (\\\\%) & SSR/TSR \\\\\\\\\\n\\\\midrule\\nPi0.5 baseline & -- & 71.5 & 28.0 & 0.392 \\\\\\\\\\n\\\\midrule\\nLoRA-only & s0 & 51.5 & 29.5 & 0.573 \\\\\\\\\\nLoRA-only & s1 & 51.5 & 27.0 & 0.524 \\\\\\\\\\nLoRA-only & s2 & 51.5 & 26.5 & 0.515 \\\\\\\\\\n\\\\midrule\\n$\\\\lambda{=}0.005$ & s0 & 55.5 & 30.0 & 0.541 \\\\\\\\\\n$\\\\lambda{=}0.005$ & s1 & 50.5 & 24.0 & 0.475 \\\\\\\\\\n$\\\\lambda{=}0.005$ & s2 & 56.0 & 29.5 & 0.527 \\\\\\\\\\n\\\\midrule\\n$\\\\lambda{=}0.01$ & s0 & 52.5 & 32.5 & 0.619 \\\\\\\\\\n$\\\\lambda{=}0.01$ & s1 & 55.5 & 30.0 & 0.541 \\\\\\\\\\n$\\\\lambda{=}0.01$ & s2 & 53.5 & 28.0 & 0.523 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nThe Pi0.5 baseline achieves SSR/TSR\\\\,=\\\\,0.39: most task-completing trajectories collide. After LoRA fine-tuning, SSR/TSR increases to 0.51--0.57 (mean 0.54), confirming that the CAR improvement reflects genuine avoidance among active trajectories, not reduced exposure from lower TSR. SDF conditions show comparable SSR/TSR ranges ($\\\\lambda{=}0.005$: 0.48--0.54; $\\\\lambda{=}0.01$: 0.52--0.62), reinforcing the conclusion that SDF supervision does not improve the safety profile beyond what LoRA fine-tuning provides.\\n\\n\\n\\\\section{Displacement Threshold Sensitivity}\\\\label{sec:appendix_threshold}\\n\\nThe displacement-filtered CAR (dfCAR) excludes episodes where the end-effector displacement falls below a threshold $\\\\tau_d$. Table~\\\\ref{tab:threshold_sens} demonstrates that dfCAR is robust across five orders of magnitude of $\\\\tau_d$ for all fine-tuned conditions, because these models exhibit no action collapse (all episodes have displacement $> 0.27$\\\\,m).\\n\\n\\\\begin{table}[h]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "510837bb-b2a2-4b01-bf0c-d058eef818aa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\appendix\\\\n\\\\n\\\\\\\\section{Per-Task Collision Avoidance Rates}\\\\\\\\label{sec:appendix_pertask}\\\\n\\\\nTable~\\\\\\\\ref{tab:pertask_lora} reports per-task CAR for LoRA-only fine-tuning across three seeds. The ordering is consistent: \\\\\\\\texttt{chocolate\\\\\\\\_pudding} highest, \\\\\\\\texttt{bbq\\\\\\\\_sauce} lowest. This ordering is invariant across all SDF conditions (Tables~\\\\\\\\ref{tab:pertask_l005}--\\\\\\\\ref{tab:pertask_l01}), confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Per-task CAR (\\\\\\\\%) for LoRA-only fine-tuning (no SDF), 30K checkpoint. Overall: 54.83\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,2.25.}\\\\n\\\\\\\\label{tab:pertask_lora}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lcccc}\\\\n\\\\\\\\toprule\\\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nchocolate\\\\\\\\_pudding & 74 & 68 & 76 & 72.67 \\\\\\\\\\\\\\\\\\\\nmilk & 66 & 72 & 62 & 66.67 \\\\\\\\\\\\\\\\\\\\norange\\\\\\\\_juice & 68 & 54 & 56 & 59.33 \\\\\\\\\\\\\\\\\\\\nbbq\\\\\\\\_sauce & 20 & 16 & 26 & 20.67 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nPer-seed mean & 57.0 & 52.5 & 55.0 & 54.83 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Per-task CAR (\\\\\\\\%) for LoRA+SDF $\\\\\\\\lambda{=}0.005$, 30K checkpoint. Overall: 54.5\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,2.29.}\\\\n\\\\\\\\label{tab:pertask_l005}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lcccc}\\\\n\\\\\\\\toprule\\\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nchocolate\\\\\\\\_pudding & 74 & 70 & 74 & 72.67 \\\\\\\\\\\\\\\\\\\\nmilk & 74 & 68 & 72 & 71.33 \\\\\\\\\\\\\\\\\\\\norange\\\\\\\\_juice & 52 & 64 & 46 & 54.00 \\\\\\\\\\\\\\\\\\\\nbbq\\\\\\\\_sauce & 28 & 14 & 18 & 20.00 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nPer-seed mean & 57.0 & 54.0 & 52.5 & 54.50 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Per-task CAR (\\\\\\\\%) for LoRA+SDF $\\\\\\\\lambda{=}0.01$, 30K checkpoint. Overall: 56.33\\\\\\\\,$\\\\\\\\pm$\\\\\\\\,1.61.}\\\\n\\\\\\\\label{tab:pertask_l01}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lcccc}\\\\n\\\\\\\\toprule\\\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nchocolate\\\\\\\\_pudding & 74 & 76 & 68 & 72.67 \\\\\\\\\\\\\\\\\\\\nmilk & 72 & 72 & 72 & 72.00 \\\\\\\\\\\\\\\\\\\\norange\\\\\\\\_juice & 48 & 60 & 64 & 57.33 \\\\\\\\\\\\\\\\\\\\nbbq\\\\\\\\_sauce & 34 & 22 & 14 & 23.33 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nPer-seed mean & 57.0 & 57.5 & 54.5 & 56.33 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Per-task CAR and TSR (\\\\\\\\%) for the Pi0.5 pre-trained baseline (no fine-tuning, single evaluation). Overall CAR: 28.5\\\\\\\\%, TSR: 71.5\\\\\\\\%.}\\\\n\\\\\\\\label{tab:pertask_baseline}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lcc}\\\\n\\\\\\\\toprule\\\\nTask & CAR & TSR \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nchocolate\\\\\\\\_pudding & 60 & 80 \\\\\\\\\\\\\\\\\\\\norange\\\\\\\\_juice & 16 & 74 \\\\\\\\\\\\\\\\\\\\nbbq\\\\\\\\_sauce & 32 & 66 \\\\\\\\\\\\\\\\\\\\nmilk & 6 & 66 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nMean & 28.5 & 71.5 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\nThe per-task pattern reveals why \\\\\\\\texttt{bbq\\\\\\\\_sauce} is hardest: the BBQ sauce bottle is positioned behind a cluster of tall obstacles (moka pot, wine bottle), requiring the end-effector to navigate through a narrow corridor. \\\\\\\\texttt{chocolate\\\\\\\\_pudding}, placed at the front of the basket with fewer obstructions, is easiest. This ordering is consistent across all $\\\\\\\\lambda$ values, including a $20\\\\\\\\times$ range from 0.005 to 0.1 (Tables~\\\\\\\\ref{tab:pertask_l005}--\\\\\\\\ref{tab:pertask_l01}), confirming that task difficulty is determined by demonstration trajectory distribution rather than SDF loss weight.\\\\n\\\\n\\\\n\\\\\\\\section{Null Distribution and Permutation Test}\\\\\\\\label{sec:appendix_null}\\\\n\\\\nWe construct the null distribution from all conditions where SDF supervision is either absent or demonstrably redundant ($p > 0.1$ versus LoRA-only). This yields six per-seed CAR values: three LoRA-only seeds and three $\\\\\\\\lambda{=}0.005$ seeds (Table~\\\\\\\\ref{tab:null_dist}).\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{Null distribution construction. Values are per-seed overall CAR (\\\\\\\\%) at the 30K checkpoint.}\\\\n\\\\\\\\label{tab:null_dist}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lcccc}\\\\n\\\\\\\\toprule\\\\nCondition & s0 & s1 & s2 & Mean \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nLoRA-only & 57.0 & 52.5 & 55.0 & 54.83 \\\\\\\\\\\\\\\\\\\\nLoRA+SDF $\\\\\\\\lambda{=}0.005$ & 57.0 & 54.0 & 52.5 & 54.50 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\n\\\\\\\\multicolumn{4}{l}{Pooled null: $\\\\\\\\{57.0, 52.5, 55.0, 57.0, 54.0, 52.5\\\\\\\\}$} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\multicolumn{4}{l}{$\\\\\\\\mu_0 = 54.67$, $\\\\\\\\sigma_0 = 2.04$} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\paragraph{Permutation test procedure.}\\\\nFor each treatment condition (e.g., $\\\\\\\\lambda{=}0.1$, $k$ seeds), we enumerate all $\\\\\\\\binom{6+k}{k}$ ways to draw $k$ values from the combined pool of null + treatment values. The one-tailed $p$-value is the fraction of combinations whose mean $\\\\\\\\geq$ the observed treatment mean; the two-tailed $p$-value counts combinations whose deviation from the pooled mean exceeds the observed deviation.\\\\n\\\\n\\\\\\\\paragraph{Results for $\\\\\\\\lambda{=}0.01$ (3 seeds).}\\\\nTreatment values: $\\\\\\\\{57.0, 57.5, 54.5\\\\\\\\}$, mean = 56.33. Pooled with null: 9 values, $\\\\\\\\binom{9}{3} = 84$ combinations. The observed mean (56.33) is within the null range ($p > 0.1$, two-tailed), confirming no significant departure.\\\\n\\\\n\\\\\\\\paragraph{Results for $\\\\\\\\lambda{=}0.1$ (2 seeds).}\\\\nTreatment values: $\\\\\\\\{58.0, 58.5\\\\\\\\}$, mean = 58.25. Pooled with null: 8 values, $\\\\\\\\binom{8}{2} = 28$ combinations. One-tailed $p = 0.036$; two-tailed $p \\\\\\\\approx 0.071$. The $z$-score relative to the null is $(58.25 - 54.67)/2.04 = 1.76$. We report the conservative two-tailed value in the main text; a directional prior is justified because SDF is designed to \\\\\\\\emph{reduce} collisions.\\\\n\\\\n\\\\n\\\\\\\\section{SSR/TSR Ratio Analysis}\\\\\\\\label{sec:appendix_ssr}\\\\n\\\\nThe Safe Success Rate (SSR) counts episodes that are both task-successful \\\\\\\\emph{and} collision-free. The SSR/TSR ratio measures what fraction of task-completing episodes also avoid collisions. An increase indicates that fine-tuning improves safety among successful trajectories, not merely by suppressing task completion.\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\\\\\\centering\\\\n\\\\\\\\caption{SSR/TSR ratio across conditions. All values computed over 200 episodes (50 per task $\\\\\\\\times$ 4 tasks).}\\\\n\\\\\\\\label{tab:ssr_tsr}\\\\n\\\\\\\\small\\\\n\\\\\\\\begin{tabular}{lccccc}\\\\n\\\\\\\\toprule\\\\nCondition & Seed & TSR (\\\\\\\\%) & SSR (\\\\\\\\%) & SSR/TSR \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nPi0.5 baseline & -- & 71.5 & 28.0 & 0.392 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nLoRA-only & s0 & 51.5 & 29.5 & 0.573 \\\\\\\\\\\\\\\\\\\\nLoRA-only & s1 & 51.5 & 27.0 & 0.524 \\\\\\\\\\\\\\\\\\\\nLoRA-only & s2 & 51.5 & 26.5 & 0.515 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\n$\\\\\\\\lambda{=}0.005$ & s0 & 55.5 & 30.0 & 0.541 \\\\\\\\\\\\\\\\\\\\n$\\\\\\\\lambda{=}0.005$ & s1 & 50.5 & 24.0 & 0.475 \\\\\\\\\\\\\\\\\\\\n$\\\\\\\\lambda{=}0.005$ & s2 & 56.0 & 29.5 & 0.527 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\n$\\\\\\\\lambda{=}0.01$ & s0 & 52.5 & 32.5 & 0.619 \\\\\\\\\\\\\\\\\\\\n$\\\\\\\\lambda{=}0.01$ & s1 & 55.5 & 30.0 & 0.541 \\\\\\\\\\\\\\\\\\\\n$\\\\\\\\lambda{=}0.01$ & s2 & 53.5 & 28.0 & 0.523 \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\nThe Pi0.5 baseline achieves SSR/TSR\\\\\\\\,=\\\\\\\\,0.39: most task-completing trajectories collide. After LoRA fine-tuning, SSR/TSR increases to 0.51--0.57 (mean 0.54), confirming that the CAR improvement reflects genuine avoidance among active trajectories, not reduced exposure from lower TSR. SDF conditions show comparable SSR/TSR ranges ($\\\\\\\\lambda{=}0.005$: 0.48--0.54; $\\\\\\\\lambda{=}0.01$: 0.52--0.62), reinforcing the conclusion that SDF supervision does not improve the safety profile beyond what LoRA fine-tuning provides.\\\\n\\\\n\\\\n\\\\\\\\section{Displacement Threshold Sensitivity}\\\\\\\\label{sec:appendix_threshold}\\\\n\\\\nThe displacement-filtered CAR (dfCAR) excludes episodes where the end-effector displacement falls below a threshold $\\\\\\\\tau_d$. Table~\\\\\\\\ref{tab:threshold_sens} demonstrates that dfCAR is robust across five orders of magnitude of $\\\\\\\\tau_d$ for all fine-tuned conditions, because these models exhibit no action collapse (all episodes have displacement $> 0.27$\\\\\\\\,m).\\\\n\\\\n\\\\\\\\begin{table}[h]\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\appendix\\n\\n\\\\section{Per-Task Collision Avoidance Rates}\\\\label{sec:appendix_pertask}\\n\\nTable~\\\\ref{tab:pertask_lora} reports per-task CAR for LoRA-only fine-tuning across three seeds. The ordering is consistent: \\\\texttt{chocolate\\\\_pudding} highest, \\\\texttt{bbq\\\\_sauce} lowest. This ordering is invariant across all SDF conditions (Tables~\\\\ref{tab:pertask_l005}--\\\\ref{tab:pertask_l01}), confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR (\\\\%) for LoRA-only fine-tuning (no SDF), 30K checkpoint. Overall: 54.83\\\\,$\\\\pm$\\\\,2.25.}\\n\\\\label{tab:pertask_lora}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 74 & 68 & 76 & 72.67 \\\\\\\\\\nmilk & 66 & 72 & 62 & 66.67 \\\\\\\\\\norange\\\\_juice & 68 & 54 & 56 & 59.33 \\\\\\\\\\nbbq\\\\_sauce & 20 & 16 & 26 & 20.67 \\\\\\\\\\n\\\\midrule\\nPer-seed mean & 57.0 & 52.5 & 55.0 & 54.83 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR (\\\\%) for LoRA+SDF $\\\\lambda{=}0.005$, 30K checkpoint. Overall: 54.5\\\\,$\\\\pm$\\\\,2.29.}\\n\\\\label{tab:pertask_l005}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 74 & 70 & 74 & 72.67 \\\\\\\\\\nmilk & 74 & 68 & 72 & 71.33 \\\\\\\\\\norange\\\\_juice & 52 & 64 & 46 & 54.00 \\\\\\\\\\nbbq\\\\_sauce & 28 & 14 & 18 & 20.00 \\\\\\\\\\n\\\\midrule\\nPer-seed mean & 57.0 & 54.0 & 52.5 & 54.50 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR (\\\\%) for LoRA+SDF $\\\\lambda{=}0.01$, 30K checkpoint. Overall: 56.33\\\\,$\\\\pm$\\\\,1.61.}\\n\\\\label{tab:pertask_l01}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nTask & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 74 & 76 & 68 & 72.67 \\\\\\\\\\nmilk & 72 & 72 & 72 & 72.00 \\\\\\\\\\norange\\\\_juice & 48 & 60 & 64 & 57.33 \\\\\\\\\\nbbq\\\\_sauce & 34 & 22 & 14 & 23.33 \\\\\\\\\\n\\\\midrule\\nPer-seed mean & 57.0 & 57.5 & 54.5 & 56.33 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Per-task CAR and TSR (\\\\%) for the Pi0.5 pre-trained baseline (no fine-tuning, single evaluation). Overall CAR: 28.5\\\\%, TSR: 71.5\\\\%.}\\n\\\\label{tab:pertask_baseline}\\n\\\\small\\n\\\\begin{tabular}{lcc}\\n\\\\toprule\\nTask & CAR & TSR \\\\\\\\\\n\\\\midrule\\nchocolate\\\\_pudding & 60 & 80 \\\\\\\\\\norange\\\\_juice & 16 & 74 \\\\\\\\\\nbbq\\\\_sauce & 32 & 66 \\\\\\\\\\nmilk & 6 & 66 \\\\\\\\\\n\\\\midrule\\nMean & 28.5 & 71.5 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nThe per-task pattern reveals why \\\\texttt{bbq\\\\_sauce} is hardest: the BBQ sauce bottle is positioned behind a cluster of tall obstacles (moka pot, wine bottle), requiring the end-effector to navigate through a narrow corridor. \\\\texttt{chocolate\\\\_pudding}, placed at the front of the basket with fewer obstructions, is easiest. This ordering is consistent across all $\\\\lambda$ values, including a $20\\\\times$ range from 0.005 to 0.1 (Tables~\\\\ref{tab:pertask_l005}--\\\\ref{tab:pertask_l01}), confirming that task difficulty is determined by demonstration trajectory distribution rather than SDF loss weight.\\n\\n\\n\\\\section{Null Distribution and Permutation Test}\\\\label{sec:appendix_null}\\n\\nWe construct the null distribution from all conditions where SDF supervision is either absent or demonstrably redundant ($p > 0.1$ versus LoRA-only). This yields six per-seed CAR values: three LoRA-only seeds and three $\\\\lambda{=}0.005$ seeds (Table~\\\\ref{tab:null_dist}).\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Null distribution construction. Values are per-seed overall CAR (\\\\%) at the 30K checkpoint.}\\n\\\\label{tab:null_dist}\\n\\\\small\\n\\\\begin{tabular}{lcccc}\\n\\\\toprule\\nCondition & s0 & s1 & s2 & Mean \\\\\\\\\\n\\\\midrule\\nLoRA-only & 57.0 & 52.5 & 55.0 & 54.83 \\\\\\\\\\nLoRA+SDF $\\\\lambda{=}0.005$ & 57.0 & 54.0 & 52.5 & 54.50 \\\\\\\\\\n\\\\midrule\\n\\\\multicolumn{4}{l}{Pooled null: $\\\\{57.0, 52.5, 55.0, 57.0, 54.0, 52.5\\\\}$} \\\\\\\\\\n\\\\multicolumn{4}{l}{$\\\\mu_0 = 54.67$, $\\\\sigma_0 = 2.04$} \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\paragraph{Permutation test procedure.}\\nFor each treatment condition (e.g., $\\\\lambda{=}0.1$, $k$ seeds), we enumerate all $\\\\binom{6+k}{k}$ ways to draw $k$ values from the combined pool of null + treatment values. The one-tailed $p$-value is the fraction of combinations whose mean $\\\\geq$ the observed treatment mean; the two-tailed $p$-value counts combinations whose deviation from the pooled mean exceeds the observed deviation.\\n\\n\\\\paragraph{Results for $\\\\lambda{=}0.01$ (3 seeds).}\\nTreatment values: $\\\\{57.0, 57.5, 54.5\\\\}$, mean = 56.33. Pooled with null: 9 values, $\\\\binom{9}{3} = 84$ combinations. The observed mean (56.33) is within the null range ($p > 0.1$, two-tailed), confirming no significant departure.\\n\\n\\\\paragraph{Results for $\\\\lambda{=}0.1$ (2 seeds).}\\nTreatment values: $\\\\{58.0, 58.5\\\\}$, mean = 58.25. Pooled with null: 8 values, $\\\\binom{8}{2} = 28$ combinations. One-tailed $p = 0.036$; two-tailed $p \\\\approx 0.071$. The $z$-score relative to the null is $(58.25 - 54.67)/2.04 = 1.76$. We report the conservative two-tailed value in the main text; a directional prior is justified because SDF is designed to \\\\emph{reduce} collisions.\\n\\n\\n\\\\section{SSR/TSR Ratio Analysis}\\\\label{sec:appendix_ssr}\\n\\nThe Safe Success Rate (SSR) counts episodes that are both task-successful \\\\emph{and} collision-free. The SSR/TSR ratio measures what fraction of task-completing episodes also avoid collisions. An increase indicates that fine-tuning improves safety among successful trajectories, not merely by suppressing task completion.\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{SSR/TSR ratio across conditions. All values computed over 200 episodes (50 per task $\\\\times$ 4 tasks).}\\n\\\\label{tab:ssr_tsr}\\n\\\\small\\n\\\\begin{tabular}{lccccc}\\n\\\\toprule\\nCondition & Seed & TSR (\\\\%) & SSR (\\\\%) & SSR/TSR \\\\\\\\\\n\\\\midrule\\nPi0.5 baseline & -- & 71.5 & 28.0 & 0.392 \\\\\\\\\\n\\\\midrule\\nLoRA-only & s0 & 51.5 & 29.5 & 0.573 \\\\\\\\\\nLoRA-only & s1 & 51.5 & 27.0 & 0.524 \\\\\\\\\\nLoRA-only & s2 & 51.5 & 26.5 & 0.515 \\\\\\\\\\n\\\\midrule\\n$\\\\lambda{=}0.005$ & s0 & 55.5 & 30.0 & 0.541 \\\\\\\\\\n$\\\\lambda{=}0.005$ & s1 & 50.5 & 24.0 & 0.475 \\\\\\\\\\n$\\\\lambda{=}0.005$ & s2 & 56.0 & 29.5 & 0.527 \\\\\\\\\\n\\\\midrule\\n$\\\\lambda{=}0.01$ & s0 & 52.5 & 32.5 & 0.619 \\\\\\\\\\n$\\\\lambda{=}0.01$ & s1 & 55.5 & 30.0 & 0.541 \\\\\\\\\\n$\\\\lambda{=}0.01$ & s2 & 53.5 & 28.0 & 0.523 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\nThe Pi0.5 baseline achieves SSR/TSR\\\\,=\\\\,0.39: most task-completing trajectories collide. After LoRA fine-tuning, SSR/TSR increases to 0.51--0.57 (mean 0.54), confirming that the CAR improvement reflects genuine avoidance among active trajectories, not reduced exposure from lower TSR. SDF conditions show comparable SSR/TSR ranges ($\\\\lambda{=}0.005$: 0.48--0.54; $\\\\lambda{=}0.01$: 0.52--0.62), reinforcing the conclusion that SDF supervision does not improve the safety profile beyond what LoRA fine-tuning provides.\\n\\n\\n\\\\section{Displacement Threshold Sensitivity}\\\\label{sec:appendix_threshold}\\n\\nThe displacement-filtered CAR (dfCAR) excludes episodes where the end-effector displacement falls below a threshold $\\\\tau_d$. Table~\\\\ref{tab:threshold_sens} demonstrates that dfCAR is robust across five orders of magnitude of $\\\\tau_d$ for all fine-tuned conditions, because these models exhibit no action collapse (all episodes have displacement $> 0.27$\\\\,m).\\n\\n\\\\begin{table}[h]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
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
Now I have all the data. Let me compile the findings.

Key findings:

**INCONSISTENCIES:**

1. **SSR/TSR baseline: 0.33 (main text) vs 0.39 (appendix)**
   - claim3.tex line 30: "SSR/TSR ratio increases from 0.33 (baseline)"
   - discussion.tex: "SSR/TSR increases from 0.33 to 0.51--0.57"
   - appendix SSR table: Pi0.5 baseline SSR/TSR = 0.392
   - appendix text: "Pi0.5 baseline achieves SSR/TSR = 0.39"
   - The appendix calculation shows 0.392 (28.0/71.5), which clearly contradicts the 0.33 figure used throughout the main text.

2. **Threshold table LoRA s0 dfCAR: 56.5 vs 57.0 (per-task table)**
   - Threshold table lists LoRA s0 = 56.5 across all thresholds
   - Per-task table shows LoRA s0 = 57.0
   - Since the threshold table notes no episodes exhibit sub-threshold displacement, dfCAR should match CAR at 57.0.

3. **Threshold table missing**
   - LoRA only includes s0 and s1 in the threshold table, but s2 is absent (s2=55.0 from other data)
   - SDF005 and SDF01 both have all three seeds represented.

4. **Appendix baseline vs main table baseline discrepancy**
   - The appendix's single-evaluation baseline gives CAR=28.5%, TSR=71.5%
   - The main table's 3-seed baseline shows CAR=26.8±1.6%, TSR=74.7±1.5%
   - The SSR/TSR table uses the single-evaluation baseline (71.5/28.0/0.392), but the main text's "0.33" doesn't cleanly derive from either source.
   - If SSR/TSR were 0.33 with TSR=74.7, SSR would need to be around 24.6%, which isn't verified anywhere.

5. **z=1.76 in the appendix permutation test**
   - The appendix computes z-score as (58.25 - 54.67)/2.04 = 1.76, which is a fresh calculation, not a stale value.
   - This appears correct and is appropriately located in the appendix rather than the main text.

6. **TSR range**
   - The claim states fine-tuning degrades TSR by 21–25 percentage points (74.7% → 49.7–54.0%), but λ=0.1 gives 48.0%, which is a 26.7 pp degradation outside this range.
   - This is more of a scope issue than a numerical error.

**Stale value verification:**
   - 0.039 doesn't appear anywhere in the paper.
   - 0.025 only shows up in the appendix as a legitimate SDF computation.
   - z=1.76 is a fresh calculation in the appendix, not a stale value, and doesn't appear in the main text as required.

**Checking consistency across all reported values:**
   - LoRA-only CAR, per-seed breakdowns, null distribution parameters, and all λ variants match consistently between tables, text, and appendix.
   - Baseline CAR is 26.8%.
   - TSR metrics show 74.7% ± 1.5% for the main result and 49.7% ± 3.2% for LoRA-only.
   - Statistical significance reported as p ≈ 0.071 two-tailed in most places, p = 0.036 one-tailed in footnotes and appendix.
   - All the percentage point differences check out: 0.33 pp between LoRA-only and λ=0.005, ~28 pp improvement over baseline, ~3.6 pp between λ=0.1 and null distribution.
   - The standard deviation calculation (55.3 - 54.67)/2.04 = 0.31 confirms the "within 0.3σ" claim.
   - λ=0.1 consistently labeled as "2 seeds" or "two of three seeds" throughout.
   - Phase 2 ablation shows CAR = 57.5% for the single seed condition.
   - TSR degradation of ~21-25 pp for λ≤0.01 conditions verified.
   - All per-task arithmetic and null distribution statistics check out.
   - Now I'm verifying the LoRA SSR/TSR values from the appendix table.

Now I'm checking the LoRA ratios across seeds—s0 gives 0.573, s1 gives 0.524, and s2 gives 0.515, all matching the stated range of 0.51–0.57.

But there's a problem: the main table reports LoRA-only TSR as 49.7 ± 3.2, yet the SSR table shows all three seeds with TSR = 51.5. If all three seeds actually had TSR = 51.5, the mean would be 51.5, not 49.7—this is a significant discrepancy I need to resolve. The λ=0.005 values check out—the individual seed results average to 54.0 with a standard deviation of 3.0, matching the main table exactly. Now looking at λ=0.01, the three seeds give a mean of 53.833, which rounds to 53 in the main table.

But there's a discrepancy with LoRA-only: all three seeds in the SSR table show 51.5, which would mean a mean of 51.5 and zero standard deviation, yet the main table reports 49.7 ± 3.2. This suggests either the SSR table has an error or the main table's LoRA values are incorrect. The LoRA TSR values in the SSR table are definitely wrong—getting exactly 51.5 across all three seeds contradicts the main table's 49.7 ± 3.2, making this almost certainly a data entry error that cascades into incorrect SSR and SSR/TSR calculations for LoRA. I'm also noticing the baseline TSR in the SSR table (71.5) aligns with the appendix's single evaluation rather than the main table's 3-seed average (74.7), which at least shows internal consistency there. The major issues are the SSR/TSR baseline discrepancy between the claim and appendix (0.33 vs 0.39), plus these impossible LoRA TSR values, with a few minor inconsistencies scattered through the threshold table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "2da5a7f2-a217-4f47-bd13-e98436a34344",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DkqMfUeioGaT2Cca1etLH6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8944,
      "cache_read_input_tokens": 44389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8944
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

Now I have all the data needed. Here's the full cross-check report.

---

## 数字一致性核对报告

### 一致通过的数字

| 数字 | 位置一致性 | 验证 |
|------|-----------|------|
| LoRA-only CAR 54.83% ± 2.25% | 主表 + 正文 + appendix per-task 表 | (57+52.5+55)/3=54.833, σ=2.255 ✓ |
| Per-seed s0=57, s1=52.5, s2=55 | 主表 ↔ appendix per-task 表 | ✓ |
| λ=0.005 CAR 54.5% ± 2.29% | 主表 + appendix | (57+54+52.5)/3=54.5, σ=2.291 ✓ |
| λ=0.01 CAR 56.33% ± 1.61% | 主表 + appendix | (57+57.5+54.5)/3=56.333, σ=1.607 ✓ |
| λ=0.1 CAR 58.25% ± 0.35% (2 seeds) | 主表 + 正文 + figure caption | (58+58.5)/2=58.25, σ=0.354 ✓ |
| Baseline CAR 26.8±1.6, TSR 74.7±1.5 | 主表 + 正文引用 | ✓ |
| Null distribution μ=54.67, σ=2.04 | 正文 + appendix | {57,52.5,55,57,54,52.5} → μ=54.667, σ=2.041 ✓ |
| p ≈ 0.071 (two-tailed) | abstract + 主表 caption + 正文 + fig caption + discussion | 全部一致 ✓ |
| p = 0.036 (one-tailed) | claim3 脚注 + appendix | ✓ |
| "within 0.33 pp" | 正文 | 54.83 − 54.5 = 0.33 ✓ |
| "~28 percentage points" | 正文 + abstract + discussion | 54.83 − 26.8 = 28.03 ✓ |
| "~3.6 pp" effect size | 正文 | 58.25 − 54.67 = 3.58 ✓ |
| "within 0.3σ" (stepwise) | 正文 + appendix | (55.3−54.67)/2.04 = 0.31 ✓ |
| Phase 2 ablation CAR=57.5% (s2) | 正文 + 脚注 "single seed" | ✓ |
| λ=0.1 标注 "2 seeds"/"two of three seeds" | 主表 + 脚注 + 正文 + fig caption | 全部正确标注 ✓ |
| SSR/TSR 0.51–0.57 (LoRA fine-tuned) | claim3 + discussion + appendix | appendix 表: 0.515–0.573 ✓ |
| All per-task table internal arithmetic | appendix | 逐项验证全部正确 ✓ |

### 不一致项

#### 1. **SSR/TSR baseline: 0.33 (正文) vs 0.39 (appendix)** — 严重

- **claim3.tex:30** — "SSR/TSR ratio increases from **0.33** (baseline) to 0.51--0.57"
- **discussion.tex** — "SSR/TSR increases from **0.33** to 0.51--0.57"
- **appendix SSR 表** — Pi0.5 baseline: TSR=71.5, SSR=28.0, SSR/TSR=**0.392**
- **appendix 正文** — "Pi0.5 baseline achieves SSR/TSR = **0.39**"

appendix 内部一致 (28.0/71.5 = 0.3916 ≈ 0.39)，但正文写的是 0.33。**应将正文的 0.33 改为 0.39**，或如果 0.33 来自 3-seed baseline 数据（不同于 appendix 的 single-evaluation），需要补充 3-seed SSR 数据。

#### 2. **SSR 表 LoRA-only TSR 值全为 51.5** — 严重

appendix SSR/TSR 表中 LoRA-only 三个 seed 的 TSR 全部是 **51.5%**：
```
LoRA-only  s0  51.5  29.5  0.573
LoRA-only  s1  51.5  27.0  0.524
LoRA-only  s2  51.5  26.5  0.515
```

但主表 (tab:avoidance_source) 显示 LoRA-only TSR = **49.7 ± 3.2**。如果三个 seed 全是 51.5，则 mean=51.5, std=0，与 49.7±3.2 矛盾。三个 seed TSR 恰好相同极不可能，疑为占位符或 copy-paste 错误。**需要填入真实的 per-seed TSR 值**，并相应修正 SSR 和 SSR/TSR。

#### 3. **Threshold 表 LoRA s0 dfCAR = 56.5 vs per-task CAR = 57.0** — 轻微

- appendix threshold 表: LoRA s0 = 56.5 (在所有 τ_d)
- appendix per-task 表: LoRA s0 = 57.0 (from (74+66+68+20)/4 = 57.0)
- 表文说 "no episodes exhibit sub-threshold displacement"，所以 dfCAR 应等于 CAR

差 0.5 pp (1 episode out of 200)。此外 **LoRA s2 缺失**（SDF005/SDF01 各有 3 seed，LoRA 只有 2 个）。需核实数据源并补全。

#### 4. **TSR 降幅 "21–25 pp" 和 "49.7–54.0%" 未包含 λ=0.1** — 建议修正

claim3.tex: "Fine-tuning degrades TSR by ~21–25 pp (74.7% → 49.7–54.0%)"。但 λ=0.1 的 TSR=48.0%，对应降幅 26.7 pp，超出 "21–25" 范围。如果句子意在覆盖所有 fine-tuned 条件，应改为 "~21–27 pp (74.7% → 48.0–54.0%)"；否则应注明 "at λ ≤ 0.01"。

### 旧值残留扫描

| 旧值 | 扫描结果 |
|------|---------|
| 0.039 | **未发现**，全部文件无匹配 ✓ |
| 0.025 | 仅出现在 appendix SDF computation 的 σ₁=0.025（合法使用） ✓ |
| z=1.76 / z = 1.76 | 仅出现在 appendix permutation test 作为新计算 (58.25−54.67)/2.04=1.76，非旧值残留 ✓ |

### 总结

- **需立即修正**：#1 SSR/TSR baseline 0.33→0.39（claim3 + discussion 两处）；#2 SSR 表 LoRA TSR 全为 51.5 需替换为真实值
- **需核实**：#3 threshold 表 LoRA s0 差 0.5 pp + 缺 s2
- **建议修正**：#4 TSR 降幅范围

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "uuid": "382cf2bf-76d6-4caf-b965-c841779a2e14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DkqMfUeioGaT2Cca1etLH6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8944,
      "cache_read_input_tokens": 44389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8944
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

Now I have all the data needed. Here's the full cross-check report.

---

## 数字一致性核对报告

### 一致通过的数字

| 数字 | 位置一致性 | 验证 |
|------|-----------|------|
| LoRA-only CAR 54.83% ± 2.25% | 主表 + 正文 + appendix per-task 表 | (57+52.5+55)/3=54.833, σ=2.255 ✓ |
| Per-seed s0=57, s1=52.5, s2=55 | 主表 ↔ appendix per-task 表 | ✓ |
| λ=0.005 CAR 54.5% ± 2.29% | 主表 + appendix | (57+54+52.5)/3=54.5, σ=2.291 ✓ |
| λ=0.01 CAR 56.33% ± 1.61% | 主表 + appendix | (57+57.5+54.5)/3=56.333, σ=1.607 ✓ |
| λ=0.1 CAR 58.25% ± 0.35% (2 seeds) | 主表 + 正文 + figure caption | (58+58.5)/2=58.25, σ=0.354 ✓ |
| Baseline CAR 26.8±1.6, TSR 74.7±1.5 | 主表 + 正文引用 | ✓ |
| Null distribution μ=54.67, σ=2.04 | 正文 + appendix | {57,52.5,55,57,54,52.5} → μ=54.667, σ=2.041 ✓ |
| p ≈ 0.071 (two-tailed) | abstract + 主表 caption + 正文 + fig caption + discussion | 全部一致 ✓ |
| p = 0.036 (one-tailed) | claim3 脚注 + appendix | ✓ |
| "within 0.33 pp" | 正文 | 54.83 − 54.5 = 0.33 ✓ |
| "~28 percentage points" | 正文 + abstract + discussion | 54.83 − 26.8 = 28.03 ✓ |
| "~3.6 pp" effect size | 正文 | 58.25 − 54.67 = 3.58 ✓ |
| "within 0.3σ" (stepwise) | 正文 + appendix | (55.3−54.67)/2.04 = 0.31 ✓ |
| Phase 2 ablation CAR=57.5% (s2) | 正文 + 脚注 "single seed" | ✓ |
| λ=0.1 标注 "2 seeds"/"two of three seeds" | 主表 + 脚注 + 正文 + fig caption | 全部正确标注 ✓ |
| SSR/TSR 0.51–0.57 (LoRA fine-tuned) | claim3 + discussion + appendix | appendix 表: 0.515–0.573 ✓ |
| All per-task table internal arithmetic | appendix | 逐项验证全部正确 ✓ |

### 不一致项

#### 1. **SSR/TSR baseline: 0.33 (正文) vs 0.39 (appendix)** — 严重

- **claim3.tex:30** — "SSR/TSR ratio increases from **0.33** (baseline) to 0.51--0.57"
- **discussion.tex** — "SSR/TSR increases from **0.33** to 0.51--0.57"
- **appendix SSR 表** — Pi0.5 baseline: TSR=71.5, SSR=28.0, SSR/TSR=**0.392**
- **appendix 正文** — "Pi0.5 baseline achieves SSR/TSR = **0.39**"

appendix 内部一致 (28.0/71.5 = 0.3916 ≈ 0.39)，但正文写的是 0.33。**应将正文的 0.33 改为 0.39**，或如果 0.33 来自 3-seed baseline 数据（不同于 appendix 的 single-evaluation），需要补充 3-seed SSR 数据。

#### 2. **SSR 表 LoRA-only TSR 值全为 51.5** — 严重

appendix SSR/TSR 表中 LoRA-only 三个 seed 的 TSR 全部是 **51.5%**：
```
LoRA-only  s0  51.5  29.5  0.573
LoRA-only  s1  51.5  27.0  0.524
LoRA-only  s2  51.5  26.5  0.515
```

但主表 (tab:avoidance_source) 显示 LoRA-only TSR = **49.7 ± 3.2**。如果三个 seed 全是 51.5，则 mean=51.5, std=0，与 49.7±3.2 矛盾。三个 seed TSR 恰好相同极不可能，疑为占位符或 copy-paste 错误。**需要填入真实的 per-seed TSR 值**，并相应修正 SSR 和 SSR/TSR。

#### 3. **Threshold 表 LoRA s0 dfCAR = 56.5 vs per-task CAR = 57.0** — 轻微

- appendix threshold 表: LoRA s0 = 56.5 (在所有 τ_d)
- appendix per-task 表: LoRA s0 = 57.0 (from (74+66+68+20)/4 = 57.0)
- 表文说 "no episodes exhibit sub-threshold displacement"，所以 dfCAR 应等于 CAR

差 0.5 pp (1 episode out of 200)。此外 **LoRA s2 缺失**（SDF005/SDF01 各有 3 seed，LoRA 只有 2 个）。需核实数据源并补全。

#### 4. **TSR 降幅 "21–25 pp" 和 "49.7–54.0%" 未包含 λ=0.1** — 建议修正

claim3.tex: "Fine-tuning degrades TSR by ~21–25 pp (74.7% → 49.7–54.0%)"。但 λ=0.1 的 TSR=48.0%，对应降幅 26.7 pp，超出 "21–25" 范围。如果句子意在覆盖所有 fine-tuned 条件，应改为 "~21–27 pp (74.7% → 48.0–54.0%)"；否则应注明 "at λ ≤ 0.01"。

### 旧值残留扫描

| 旧值 | 扫描结果 |
|------|---------|
| 0.039 | **未发现**，全部文件无匹配 ✓ |
| 0.025 | 仅出现在 appendix SDF computation 的 σ₁=0.025（合法使用） ✓ |
| z=1.76 / z = 1.76 | 仅出现在 appendix permutation test 作为新计算 (58.25−54.67)/2.04=1.76，非旧值残留 ✓ |

### 总结

- **需立即修正**：#1 SSR/TSR baseline 0.33→0.39（claim3 + discussion 两处）；#2 SSR 表 LoRA TSR 全为 51.5 需替换为真实值
- **需核实**：#3 threshold 表 LoRA s0 差 0.5 pp + 缺 s2
- **建议修正**：#4 TSR 降幅范围

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 274133,
  "duration_api_ms": 271292,
  "num_turns": 27,
  "stop_reason": "end_turn",
  "session_id": "23633511-e936-437b-b021-56a3d13a4caa",
  "total_cost_usd": 0.8465015,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 41882,
    "cache_read_input_tokens": 352584,
    "output_tokens": 16257,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 41882,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 5442,
        "cache_read_input_tokens": 44389,
        "cache_creation_input_tokens": 8944,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 8944
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1852,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001942,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 16257,
      "cacheReadInputTokens": 352584,
      "cacheCreationInputTokens": 41882,
      "webSearchRequests": 0,
      "costUSD": 0.8445595,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "21a926fb-77ba-486c-a4e0-147cc2216764"
}
```

</details>

---
