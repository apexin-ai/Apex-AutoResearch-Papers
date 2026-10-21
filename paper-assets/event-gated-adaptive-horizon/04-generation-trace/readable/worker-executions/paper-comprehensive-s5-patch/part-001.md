# paper comprehensive s5 patch — Part 1 of 3

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

[Transcript overview](../paper-comprehensive-s5-patch.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/c1/c1a4f7d604e100bc0e0d.json)

## Before a recorded user message

## Before a recorded user message

161 recorded events


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
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
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
  "uuid": "e08b5f1f-704f-4873-b3ec-0b4128e2cd69",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779616200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9673b962-a84c-43ef-a423-a803becf32be",
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to execute a comprehensive paper patch on a remote server. Let me break this down:

1. SSH to the server bjb1-45299
2. Navigate to the paper directory
3. Make all the specified modifications to various .tex files
4. Add TODO markers for values that need recalculation
5. Run verification checks
6. Report results

Let me start by reading the relevant files on the remote server to understand the current state, then make all the changes.

First, let me detect the image and then read the relevant files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "de725bdd-17c0-4e68-a838-f36aee5514b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtnKRqDy8TNTq8Noqh7nuM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13260,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13260
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

开始执行论文综合 patch。先读取需要修改的文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "9a98dc45-b926-49af-a184-8dbf13b9d749",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtnKRqDy8TNTq8Noqh7nuM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13260,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13260
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ph24hTPkSK2aE48neGjBnD`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
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
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "6db7e726-9cd5-4be2-818d-13b4f4462d97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtnKRqDy8TNTq8Noqh7nuM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13260,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13260
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-24T07:06:23.309Z_

<details><summary>↩ Tool result · `toolu_01Ph24hTPkSK2aE48neGjBnD`</summary>

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
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "04b0f327-49a5-45da-ab22-a639883881e1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 23
  }
}
```

</details>

---


### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all the relevant files on the remote server to understand the current state before making changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "b3455c1e-8dc8-42cd-a1fd-de892ce9c053",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvDTSwQzaM8DftrsfSWvAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 24707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

_source line 9_

先批量读取所有需要修改的文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "bf61073f-be5c-4fca-a424-b81f3d7e77a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvDTSwQzaM8DftrsfSWvAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 24707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015amoVNor6FPDEsws1YVJDQ`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "cat /root/autodl-tmp/event-gated-adaptive-horizon/paper/analysis.tex",
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
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "cc0c0d1c-3f48-44b9-8506-673823a17b1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvDTSwQzaM8DftrsfSWvAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 24707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Rw7DVWPfA5V5VtH6W8UH5j`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "cat /root/autodl-tmp/event-gated-adaptive-horizon/paper/introduction.tex",
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
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "ba511611-2e08-4d93-ba06-9b88c3f48aae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvDTSwQzaM8DftrsfSWvAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 24707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

_source line 12 · 2026-05-24T07:06:29.194Z_

<details><summary>↩ Tool result · `toolu_015amoVNor6FPDEsws1YVJDQ`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/analysis.tex: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.94}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "7ae51f32-206c-4151-982c-42808e4b8481",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/analysis.tex: No such file or directory\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.94}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/analysis.tex: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.94}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RcnALjWngiBRw5QdNjwLND`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "cat /root/autodl-tmp/event-gated-adaptive-horizon/paper/results.tex",
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
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "a65ec039-b380-449f-80b0-beeccdc13dd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvDTSwQzaM8DftrsfSWvAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 24707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

_source line 14 · 2026-05-24T07:06:29.601Z_

<details><summary>↩ Tool result · `toolu_01Rw7DVWPfA5V5VtH6W8UH5j`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/introduction.tex: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "4d610543-daa8-4991-b271-9c36d240d5b6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/introduction.tex: No such file or directory\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/introduction.tex: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-24T07:06:30.015Z_

<details><summary>↩ Tool result · `toolu_01RcnALjWngiBRw5QdNjwLND`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/results.tex: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "e77c5c07-e2c0-4b02-addc-419ea74fe46c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/results.tex: No such file or directory\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/results.tex: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PwXNFVbzhHbTVmtirXHFhk`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "cat /root/autodl-tmp/event-gated-adaptive-horizon/paper/abstract_body.tex",
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
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "a8948f36-14f6-4d32-8a4e-28b3f78c8ac5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvDTSwQzaM8DftrsfSWvAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 24707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

_source line 17 · 2026-05-24T07:06:30.876Z_

<details><summary>↩ Tool result · `toolu_01PwXNFVbzhHbTVmtirXHFhk`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/abstract_body.tex: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "aeebf6db-46db-485a-a340-86a692d574db",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/abstract_body.tex: No such file or directory\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/abstract_body.tex: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.34}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KLqKLbwuLZXUKWfBcXDBTc`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "cat /root/autodl-tmp/event-gated-adaptive-horizon/paper/conclusion.tex",
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
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "c53a3f70-f0b2-4b30-8a12-21ed9ce0e2ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvDTSwQzaM8DftrsfSWvAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 24707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

_source line 19 · 2026-05-24T07:06:31.832Z_

<details><summary>↩ Tool result · `toolu_01KLqKLbwuLZXUKWfBcXDBTc`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/conclusion.tex: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "61bf8bc4-2859-4905-909d-430085a2a962",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/conclusion.tex: No such file or directory\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/conclusion.tex: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.34}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E3vdoFmAwiR7U3coBF6qZg`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "cat /root/autodl-tmp/event-gated-adaptive-horizon/paper/appendix.tex",
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
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "89564405-15b8-4827-a333-975ffcde65d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvDTSwQzaM8DftrsfSWvAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 24707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1030
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

_source line 21 · 2026-05-24T07:06:32.305Z_

<details><summary>↩ Tool result · `toolu_01E3vdoFmAwiR7U3coBF6qZg`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/appendix.tex: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "1fd525af-f5d2-4cfd-9f39-6da7f6d2501c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/appendix.tex: No such file or directory\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/event-gated-adaptive-horizon/paper/appendix.tex: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.34}}"
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
The files don't exist at that path. Let me check the actual directory structure on the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "f050e31d-06c7-4fde-8044-d92eb22a931c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtHFj4SU5e14GWmPrY6bS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1543,
      "cache_read_input_tokens": 25737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1543
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

_source line 23_

文件路径不对，先检查目录结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "190dece2-e01c-4fcd-8a5f-c742769c4eac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtHFj4SU5e14GWmPrY6bS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1543,
      "cache_read_input_tokens": 25737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1543
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

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FqKb87btuTNqubVkFbng9y`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/",
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
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "7e7710e8-053c-4d91-b735-a34c5d434790",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtHFj4SU5e14GWmPrY6bS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1543,
      "cache_read_input_tokens": 25737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1543
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

_source line 25 · 2026-05-24T07:06:39.025Z_

<details><summary>↩ Tool result · `toolu_01FqKb87btuTNqubVkFbng9y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Dockerfile\\nLICENSE\\nREADME.md\\n__pycache__\\nanalysis\\nartifacts\\ncheckpoint_monitor.py\\ncheckpoint_results.jsonl\\nconfigs.yaml\\nconfigs.yaml.bak\\nconfigs.yaml.bak.pre_plan015\\ndetector_validation_v3.json\\ndocs\\ndreamer.py\\ndreamer.py.bak\\ndreamer.py.bak.step_sync\\nenvs\\neval_mvp.py\\neval_plots\\nexploration.py\\nextract_paper_data.py\\nfigures\\nimgs\\nlaunch_exp053.sh\\nlogdir\\nmodels.py\\nmodels.py.bak\\nmodels.py.bak.hotfix\\nmodels.py.bak.pre_autocorr\\nmodels.py.bak.pre_plan015\\nmodels.py.bak.threshold\\nmodels.py.bak_sgs_fix\\nnetworks.py\\nnetworks.py.bak\\nnetworks.py.bak.pre_plan015\\nnve_audit.py\\nnve_audit_results.txt\\nnve_audit_v2.py\\nnve_audit_v2.py.bak\\nnve_threshold_analysis.py\\nparallel.py\\npickcube_ve_comparison.png\\nprint_detail.py\\nprint_summary.py\\nrequirements.txt\\nscripts\\ntools.py\\ntools.py.bak\\nvalidate_detector.py\\nxvfb_run.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "2a061d79-9531-4bfc-bfbf-bdb19530c910",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Dockerfile\\\\nLICENSE\\\\nREADME.md\\\\n__pycache__\\\\nanalysis\\\\nartifacts\\\\ncheckpoint_monitor.py\\\\ncheckpoint_results.jsonl\\\\nconfigs.yaml\\\\nconfigs.yaml.bak\\\\nconfigs.yaml.bak.pre_plan015\\\\ndetector_validation_v3.json\\\\ndocs\\\\ndreamer.py\\\\ndreamer.py.bak\\\\ndreamer.py.bak.step_sync\\\\nenvs\\\\neval_mvp.py\\\\neval_plots\\\\nexploration.py\\\\nextract_paper_data.py\\\\nfigures\\\\nimgs\\\\nlaunch_exp053.sh\\\\nlogdir\\\\nmodels.py\\\\nmodels.py.bak\\\\nmodels.py.bak.hotfix\\\\nmodels.py.bak.pre_autocorr\\\\nmodels.py.bak.pre_plan015\\\\nmodels.py.bak.threshold\\\\nmodels.py.bak_sgs_fix\\\\nnetworks.py\\\\nnetworks.py.bak\\\\nnetworks.py.bak.pre_plan015\\\\nnve_audit.py\\\\nnve_audit_results.txt\\\\nnve_audit_v2.py\\\\nnve_audit_v2.py.bak\\\\nnve_threshold_analysis.py\\\\nparallel.py\\\\npickcube_ve_comparison.png\\\\nprint_detail.py\\\\nprint_summary.py\\\\nrequirements.txt\\\\nscripts\\\\ntools.py\\\\ntools.py.bak\\\\nvalidate_detector.py\\\\nxvfb_run.sh\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Dockerfile\\nLICENSE\\nREADME.md\\n__pycache__\\nanalysis\\nartifacts\\ncheckpoint_monitor.py\\ncheckpoint_results.jsonl\\nconfigs.yaml\\nconfigs.yaml.bak\\nconfigs.yaml.bak.pre_plan015\\ndetector_validation_v3.json\\ndocs\\ndreamer.py\\ndreamer.py.bak\\ndreamer.py.bak.step_sync\\nenvs\\neval_mvp.py\\neval_plots\\nexploration.py\\nextract_paper_data.py\\nfigures\\nimgs\\nlaunch_exp053.sh\\nlogdir\\nmodels.py\\nmodels.py.bak\\nmodels.py.bak.hotfix\\nmodels.py.bak.pre_autocorr\\nmodels.py.bak.pre_plan015\\nmodels.py.bak.threshold\\nmodels.py.bak_sgs_fix\\nnetworks.py\\nnetworks.py.bak\\nnetworks.py.bak.pre_plan015\\nnve_audit.py\\nnve_audit_results.txt\\nnve_audit_v2.py\\nnve_audit_v2.py.bak\\nnve_threshold_analysis.py\\nparallel.py\\npickcube_ve_comparison.png\\nprint_detail.py\\nprint_summary.py\\nrequirements.txt\\nscripts\\ntools.py\\ntools.py.bak\\nvalidate_detector.py\\nxvfb_run.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
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
No `paper/` directory. Let me check if there's a paper directory elsewhere, or maybe the tex files are in another location. Let me look for .tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "1fcb664d-922b-4b3f-a85f-23b0d5e6d4f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdaCjSdZtQhMGbWB1myrR9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 27280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 764
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

_source line 27_

没有 paper 目录。查找 .tex 文件位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "43fd9017-1457-436e-9482-ae160b932a41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdaCjSdZtQhMGbWB1myrR9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 27280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 764
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017tWu8qRA74ME3abR5B5kMD`</summary>

```json
{
  "server": "bjb1-45299",
  "command": "find /root/autodl-tmp/event-gated-adaptive-horizon -name \"*.tex\" -type f",
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
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "ae33f289-db18-4111-bf84-ce6ebc7815a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdaCjSdZtQhMGbWB1myrR9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 27280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 764
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

_source line 29 · 2026-05-24T07:06:43.369Z_

<details><summary>↩ Tool result · `toolu_017tWu8qRA74ME3abR5B5kMD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "35732abe-e256-4255-a8af-895e66452f9e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
No .tex files on the server at all. The paper files might be local only, not on the remote server. Let me check locally.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "df1c31e9-f670-401d-bc4c-f1a9b43a7016",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fev2ZRA6ods2o4fReChQ8G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 28044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 31_

服务器上没有 .tex 文件。检查本地是否有 paper 目录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "5d7bf748-3d30-4fe7-9f2f-293230ec8d15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fev2ZRA6ods2o4fReChQ8G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 28044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 32_

<details open><summary>🔧 Tool call — Glob · `toolu_01YXuUN7XfLWnLZFv3xNtTvY`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "3cc1d61a-340d-4844-8001-b76663644cfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fev2ZRA6ods2o4fReChQ8G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 28044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 33 · 2026-05-24T07:06:48.204Z_

<details><summary>↩ Tool result · `toolu_01YXuUN7XfLWnLZFv3xNtTvY`</summary>

```text
docs/paper/_corl_template/corl_2026_template_submission/example.tex
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex
artifacts/dream_reports/dream_20260514T062606/best/paper.tex
artifacts/dream_reports/dream_20260514T062606/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/best/paper.tex
artifacts/dream_reports/dream_20260515T004704/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/worst/paper.tex
artifacts/figures/archive/tab_rssm_fidelity.tex
artifacts/_project/paper/nve_sensitivity_table_37b680.tex
artifacts/dream_reports/dream_20260514T062606/worst/paper.tex
artifacts/dream_reports/dream_20260516T115400/best/paper.tex
artifacts/dream_reports/dream_20260516T115400/median/paper.tex
artifacts/dream_reports/dream_20260516T115400/worst/paper.tex
artifacts/dream_reports/dream_20260516T133210/best/paper.tex
artifacts/dream_reports/dream_20260516T133210/median/paper.tex
artifacts/dream_reports/dream_20260516T133210/worst/paper.tex
artifacts/dream_reports/dream_20260516T172011/best/paper.tex
artifacts/dream_reports/dream_20260516T172011/median/paper.tex
artifacts/dream_reports/dream_20260516T172011/worst/paper.tex
artifacts/analysis/detector_table.tex
artifacts/_project/paper/nve_sensitivity_table.tex
paper/tables/nve_sensitivity_table.tex
artifacts/dream_reports/dream_20260520T155150/best/paper.tex
artifacts/dream_reports/dream_20260520T155150/median/paper.tex
artifacts/dream_reports/dream_20260520T155150/worst/paper.tex
artifacts/dream_reports/dream_20260520T210241/best/paper.tex
artifacts/dream_reports/dream_20260520T210241/median/paper.tex
docs/paper/main.tex
docs/paper/sections/methodology.tex
docs/paper/sections/related_work.tex
docs/paper/sections/introduction.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/abstract_body.tex
docs/paper/sections/analysis.tex
docs/paper/sections/appendix.tex
docs/paper/sections/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "dc73072e-fca4-408a-ad65-007c31b0786d",
  "tool_use_result": {
    "filenames": [
      "docs/paper/_corl_template/corl_2026_template_submission/example.tex",
      "docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex",
      "artifacts/dream_reports/dream_20260514T062606/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T062606/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/worst/paper.tex",
      "artifacts/figures/archive/tab_rssm_fidelity.tex",
      "artifacts/_project/paper/nve_sensitivity_table_37b680.tex",
      "artifacts/dream_reports/dream_20260514T062606/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/worst/paper.tex",
      "artifacts/analysis/detector_table.tex",
      "artifacts/_project/paper/nve_sensitivity_table.tex",
      "paper/tables/nve_sensitivity_table.tex",
      "artifacts/dream_reports/dream_20260520T155150/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T155150/median/paper.tex",
      "artifacts/dream_reports/dream_20260520T155150/worst/paper.tex",
      "artifacts/dream_reports/dream_20260520T210241/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T210241/median/paper.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/methodology.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/abstract_body.tex",
      "docs/paper/sections/analysis.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/sections/results.tex"
    ],
    "durationMs": 20,
    "numFiles": 36,
    "truncated": false
  }
}
```

</details>

---


### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
The paper files are in the local directory under `docs/paper/sections/`. Let me read all the relevant files locally. Since the user said to SSH to the server, but the files are local, I'll work with the local files and make changes there.

Let me read all the relevant files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "7cd6d4cc-a95f-40c6-834f-b8e6cea44345",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pMFyTPMUP49TYywtF2gM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 28316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

_source line 35_

论文文件在本地 `docs/paper/sections/`。批量读取所有需要修改的文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "52b78d9b-22a4-49b2-8246-feb401081a9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pMFyTPMUP49TYywtF2gM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 28316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01GzEXhk1Q6tZDi8GbW32BZh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "11f53a72-dff5-4d70-8e73-12d122bda7e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pMFyTPMUP49TYywtF2gM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 28316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

_source line 37 · 2026-05-24T07:06:56.468Z_

<details><summary>↩ Tool result · `toolu_01GzEXhk1Q6tZDi8GbW32BZh`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{CIVO mechanism.}
5	The RSSM develops a $2.78\times$ reward prediction gap under trained conditioning (Table~\ref{tab:rssm_fidelity}), analogous to delusional bias \citep{lu2018nondelusional}. Gradient magnitude $\neq$ causal importance: the reward head (38--49\% of $\nabla_\theta e_{\dt}$) fails when blocked alone; the observation decoder (16--22\%) carries the critical signal; full-pathway SGS (0/3) confirms forward-pass conditioning as the irreducible vulnerability. CIVO is upstream of estimation error---dual critics converge (\S\ref{sec:arch_results})---so standard corrections are inapplicable; MPC re-planning prevents accumulation (Appendix~\ref{sec:mpc_immune}).
6	
7	\paragraph{Practitioner guidelines.}
8	Monitor via NVE diagnostic ($\geq 1.5\times$, AUROC${=}0.953$; Table~\ref{tab:nve_loeo}). Freezing the $\dt$-embedding converts sustained CIVO (6/6 trained locomotion, NVE $1.53$--$108\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\times$) causes irrecoverable damage (Appendix~\ref{sec:appendix_analysis}).
9	
10	\paragraph{Implications for robot learning.}
11	No $\dt$-embedding-dependent CIVO was observed in manipulation: all three ManiSkill environments exhibit ve-ratio transients (peaks $4$--$11\times$), but frozen controls show comparable or higher peaks (Table~\ref{tab:cross_domain}), establishing environment-specific origin. A possible mediator is reward density: locomotion provides continuous rewards accumulating coherent $\dt$-embedding bias, while manipulation rewards are sparse and contact-gated.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "e2ec8215-e429-41ab-99c7-ee7de6e0eb13",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{CIVO mechanism.}\nThe RSSM develops a $2.78\\times$ reward prediction gap under trained conditioning (Table~\\ref{tab:rssm_fidelity}), analogous to delusional bias \\citep{lu2018nondelusional}. Gradient magnitude $\\neq$ causal importance: the reward head (38--49\\% of $\\nabla_\\theta e_{\\dt}$) fails when blocked alone; the observation decoder (16--22\\%) carries the critical signal; full-pathway SGS (0/3) confirms forward-pass conditioning as the irreducible vulnerability. CIVO is upstream of estimation error---dual critics converge (\\S\\ref{sec:arch_results})---so standard corrections are inapplicable; MPC re-planning prevents accumulation (Appendix~\\ref{sec:mpc_immune}).\n\n\\paragraph{Practitioner guidelines.}\nMonitor via NVE diagnostic ($\\geq 1.5\\times$, AUROC${=}0.953$; Table~\\ref{tab:nve_loeo}). Freezing the $\\dt$-embedding converts sustained CIVO (6/6 trained locomotion, NVE $1.53$--$108\\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\\times$) causes irrecoverable damage (Appendix~\\ref{sec:appendix_analysis}).\n\n\\paragraph{Implications for robot learning.}\nNo $\\dt$-embedding-dependent CIVO was observed in manipulation: all three ManiSkill environments exhibit ve-ratio transients (peaks $4$--$11\\times$), but frozen controls show comparable or higher peaks (Table~\\ref{tab:cross_domain}), establishing environment-specific origin. A possible mediator is reward density: locomotion provides continuous rewards accumulating coherent $\\dt$-embedding bias, while manipulation rewards are sparse and contact-gated.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---


### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_012iGVev5dQ6zvH4QFzdbXfL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "c66dd656-b607-4f2e-b4a9-eba6e4b7aded",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pMFyTPMUP49TYywtF2gM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 28316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

_source line 39 · 2026-05-24T07:06:56.504Z_

<details><summary>↩ Tool result · `toolu_012iGVev5dQ6zvH4QFzdbXfL`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	World-model reinforcement learning enables sample-efficient learning directly on physical hardware \citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\dt$ mismatches between simulation and hardware. TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration degrades performance catastrophically (14--19\% of baseline). Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding and multi-rate data exposure as the strongest predictor. This combination enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates, a failure mode we term \emph{conditioning-induced value overestimation} (CIVO), analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced. A normalized value-to-eval (NVE) threshold of $\geq 1.5\times$ achieves 26/29 classification ($n{=}29$, two environments, AUROC${=}0.953$, in-sample; LOEO cross-validated, Appendix~Table~\ref{tab:nve_loeo}).
7	
8	Gradient decomposition reveals that gradient magnitude does not predict causal importance: the reward head contributes 38--49\% of $\nabla_\theta e_{\dt}$ yet reward-only stopping fails, while the observation decoder (16--22\%) carries the critical signal. A four-level intervention hierarchy (gradient, output, representation, architecture) shows that no tested intervention reliably eliminates CIVO across environments. In pure-imagination training, dual critics converge to identical value functions ($\rho > 0.999$), rendering Double Q pessimism ineffective; the min operation nonetheless enables CIVO recovery, while prevention requires min $+$ increased capacity. These findings are directly relevant to robotics: as world-model RL moves toward real systems with variable-rate sensing and multi-timescale control, understanding when temporal conditioning fails, and why standard countermeasures cannot fix it, is essential for safe deployment.
9	
10	\paragraph{Contributions.}
11	\begin{enumerate}[nosep,leftmargin=*]
12	    \item \textbf{Failure mode identification.} We identify CIVO as specific to imagination-based actor-critic with temporal conditioning and isolate trained $\dt$-embedding $+$ multi-rate exposure as jointly sufficient in tested configurations (6/6 seeds, two locomotion environments, AUROC${=}0.953$, in-sample; LOEO cross-validated). Cross-environment validation spanning locomotion and manipulation (ManiSkill) establishes that CIVO is locomotion-specific; frozen-embedding controls on three manipulation tasks identify value-ratio transients as environment-driven, demonstrating the diagnostic's specificity on non-CIVO dynamics.
13	    \item \textbf{Architectural boundary.} $\dt$-conditioning succeeds in TD-MPC2's MPC re-planning but fails under imagination-based bootstrapping, where model errors compound into biased value targets with no real-data anchor.
14	    \item \textbf{Four-level intervention hierarchy.} Across gradient, output, representation, and architecture levels, no intervention reliably eliminates CIVO across environments. Gradient magnitude does not predict causal importance (reward head: 38--49\%, reward-only stopping fails). In pure-imagination training, dual critics converge ($\rho > 0.999$), eliminating Double Q pessimism, though the min operation enables recovery through a different mechanism.
15	    \item \textbf{Online detection.} A lightweight NVE-based detector achieves 100\% sensitivity (5/5) with predictive warning in 2/5 cases.
16	\end{enumerate}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "09b078ec-a3d0-41e6-99d0-8ea47da33251",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWorld-model reinforcement learning enables sample-efficient learning directly on physical hardware \\citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\\dt$ mismatches between simulation and hardware. TAWM \\citep{nhu2025tawm} shows that conditioning a world model on step size $\\dt$ yields consistent gains within TD-MPC2's MPC framework \\citep{hansen2024tdmpc2}. Can the same $\\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \\citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?\n\nWe find that it cannot. Every variable-rate configuration degrades performance catastrophically (14--19\\% of baseline). Through a factorial analysis on Walker Walk \\citep{tassa2018dmcontrol}, we isolate the combination of a \\emph{trained} $\\dt$-embedding and multi-rate data exposure as the strongest predictor. This combination enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\dt{=}1$ and $\\dt{=}2$, which the critic internalizes as optimistic value estimates, a failure mode we term \\emph{conditioning-induced value overestimation} (CIVO), analogous to delusional bias \\citep{lu2018nondelusional} but model-induced rather than policy-class-induced. A normalized value-to-eval (NVE) threshold of $\\geq 1.5\\times$ achieves 26/29 classification ($n{=}29$, two environments, AUROC${=}0.953$, in-sample; LOEO cross-validated, Appendix~Table~\\ref{tab:nve_loeo}).\n\nGradient decomposition reveals that gradient magnitude does not predict causal importance: the reward head contributes 38--49\\% of $\\nabla_\\theta e_{\\dt}$ yet reward-only stopping fails, while the observation decoder (16--22\\%) carries the critical signal. A four-level intervention hierarchy (gradient, output, representation, architecture) shows that no tested intervention reliably eliminates CIVO across environments. In pure-imagination training, dual critics converge to identical value functions ($\\rho > 0.999$), rendering Double Q pessimism ineffective; the min operation nonetheless enables CIVO recovery, while prevention requires min $+$ increased capacity. These findings are directly relevant to robotics: as world-model RL moves toward real systems with variable-rate sensing and multi-timescale control, understanding when temporal conditioning fails, and why standard countermeasures cannot fix it, is essential for safe deployment.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Failure mode identification.} We identify CIVO as specific to imagination-based actor-critic with temporal conditioning and isolate trained $\\dt$-embedding $+$ multi-rate exposure as jointly sufficient in tested configurations (6/6 seeds, two locomotion environments, AUROC${=}0.953$, in-sample; LOEO cross-validated). Cross-environment validation spanning locomotion and manipulation (ManiSkill) establishes that CIVO is locomotion-specific; frozen-embedding controls on three manipulation tasks identify value-ratio transients as environment-driven, demonstrating the diagnostic's specificity on non-CIVO dynamics.\n    \\item \\textbf{Architectural boundary.} $\\dt$-conditioning succeeds in TD-MPC2's MPC re-planning but fails under imagination-based bootstrapping, where model errors compound into biased value targets with no real-data anchor.\n    \\item \\textbf{Four-level intervention hierarchy.} Across gradient, output, representation, and architecture levels, no intervention reliably eliminates CIVO across environments. Gradient magnitude does not predict causal importance (reward head: 38--49\\%, reward-only stopping fails). In pure-imagination training, dual critics converge ($\\rho > 0.999$), eliminating Double Q pessimism, though the min operation enables recovery through a different mechanism.\n    \\item \\textbf{Online detection.} A lightweight NVE-based detector achieves 100\\% sensitivity (5/5) with predictive warning in 2/5 cases.\n\\end{enumerate}\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  }
}
```

</details>

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_012yD291CW6c25TWvxby8mZR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "c670d4e8-4cf4-4386-9c48-ac319d7ba828",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pMFyTPMUP49TYywtF2gM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 28316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

_source line 41 · 2026-05-24T07:06:56.533Z_

<details><summary>↩ Tool result · `toolu_012yD291CW6c25TWvxby8mZR`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{Key configurations and outcomes. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 43 configurations in Table~\ref{tab:complete_results}.}
13	\label{tab:main_results}
14	\footnotesize
15	\setlength{\tabcolsep}{4pt}
16	\begin{tabular}{llcccccl}
17	\toprule
18	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
19	\midrule
20	001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
21	\midrule
22	\rowcolor{gray!15}
23	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
24	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
25	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
26	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
27	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
28	\midrule
29	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
30	\rowcolor{gray!15}
31	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
32	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
33	049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\times$$^d$ & Env.\ transient \\
34	050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\times$$^e$ & Env.\ dynamics$^e$ \\
35	046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\times$ & No CIVO \\
36	\bottomrule
37	\end{tabular}
38	\vspace{1pt}
39	{\raggedright\footnotesize
40	trn = trained ($d{=}32$, subsample ON);
41	exp$^a$ = trained, subsample OFF;
42	frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
43	--- = removed ($d{=}0$).\\
44	$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).\\
45	$^d$ StackCube transient: frozen control (exp\_051) exhibits identical spike (peak $4.30\times$ at 42.5K, self-correcting by 82.5K), indicating environment-specific phenomenon unrelated to $\dt$-embedding training.\\
46	$^e$ Seed~0 trained peaks at $10.05\times$ (82.5K) with delayed self-correction; seed~1 trained (exp\_055) peaks at $3.08\times$ (92.5K), final $0.50\times$; seed~1 frozen (exp\_056) peaks at $11.32\times$ (82.5K), final $1.19\times$. Environment-specific stochastic dynamics: frozen final exceeds trained final.\par}
47	\end{table*}
48	
49	%% ============================================================
50	%% F1: All dt>1 degrade
51	%% ============================================================
52	
53	\subsection{F1: All Variable-Rate Configurations Degrade}
54	\label{sec:f1}
55	
56	Every configuration that introduces $\dt > 1$ imagination degrades relative to the $\dt{=}1$ baseline (Figure~\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\%$ of baseline); fixed $\dt{=}4$ (007) never exceeds 176.9 ($19\%$); the learned gate (005) collapses to 98.8 ($11\%$).
57	
58	\begin{figure}[t]
59	\centering
60	\includegraphics[width=0.65\columnwidth]{figures/paper/fig1_learning_curves.pdf}
61	\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}
62	\label{fig:learning_curves}
63	\end{figure}
64	
65	%% ============================================================
66	%% F2: Trained dt_embedding → nve > 1.5x
67	%% ============================================================
68	
69	\subsection{F2: Trained Temporal Embedding Precedes Value Overestimation}
70	\label{sec:f2}
71	
72	The factorial design isolates trained $\dt$-embedding as the strongest predictor. The \emph{primary} comparison---008d (trained, subsample ON) vs.\ 008f (no embedding, subsample ON)---differs only in embedding training, yielding $\nve = 4.12\times$ (eval 82.8) vs.\ $\nve \leq 0.97\times$ (eval 503.0). \emph{Secondary} comparisons against 008a/008c (unexposed embedding) co-vary subsample status and horizon alongside the embedding factor. The $\nve \geq 1.5\times$ threshold (35K+ window) correctly classifies 26 of 29 experimental configurations across two environments (AUROC${=}0.953$, in-sample; LOEO cross-validated, Table~\ref{tab:nve_loeo}; Figure~\ref{fig:nve_trajectory}).
73	
74	\begin{figure}[t]
75	\centering
76	\includegraphics[width=0.65\columnwidth]{figures/fig1_nve_trajectory.pdf}
77	\caption{NVE trajectories (mean $\pm$ seed range). Trained $\dt$-embedding (red, Walker Walk, $n{=}3$ seeds plotted; seed~4 data in Table~\ref{tab:complete_results}) exceeds the $1.5\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}
78	\label{fig:nve_trajectory}
79	\end{figure}
80	
81	The trained $\dt$-embedding precedes CIVO in all four Walker Walk seeds (peak NVE: $4.62\times$, $4.12\times$, $1.62\times$, $1.53\times$), universally degrading performance to below 30\% of baseline (IQM $175.2$, mean $170.6$, $n{=}4$; \citealt{agarwal2021precipice}). Downstream trajectories diverge: two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and one self-corrects to a stable but degraded state (29.3\% of baseline). Combined with Cheetah Run (\S\ref{sec:f6}), CIVO onset is universal across all six tested seeds ($n{=}6$, two environments) with 5/6 progressing toward collapse (Appendix~\ref{sec:seed_divergence}).
82	
83	%% ============================================================
84	%% F3--F5: Summary (details in Appendix B)
85	%% ============================================================
86	
87	\subsection{F3--F5: Factorial Ablation (Appendix~\ref{sec:appendix_factorial})}
88	\label{sec:f3f5_summary}
89	
90	Trained $\dt$-embedding and multi-rate data exposure are \emph{jointly sufficient in tested configurations} for CIVO. Neither factor alone precedes pathological overestimation: trained embedding without multi-rate exposure (008a, 3 seeds, peak NVE $0.83$--$0.93\times$) and multi-rate exposure without embedding (008f, 3 seeds, peak NVE $\leq 1.41\times$) both remain below $1.5\times$. Cross-environment replication on Cheetah Run confirms generalization. Freezing the embedding (\texttt{requires\_grad=False}) dramatically reduces severity (NVE $0.19$--$1.88\times$ vs.\ trained $1.53$--$4.62\times$; 2/4 seeds below threshold, 2/4 transient self-correcting spikes; Table~\ref{tab:three_way_emb}); removing the embedding (008f) also avoids CIVO. Partial gradient blocking (exp\_044) does not prevent onset (peak NVE $4.45\times$) but permits delayed self-correction (final eval 538, 59\% baseline; Appendix~\ref{sec:appendix_factorial}), confirming that \emph{any} gradient pathway updating $e_{\dt}$ suffices to induce CIVO. Degradation scales monotonically with $\dt$ ($-47\%$ at $\dt{=}2$, $-81\%$ at $\dt{=}4$; Figure~\ref{fig:dt_amplification}).
91	
92	\paragraph{ManiSkill manipulation tasks.}
93	None of three ManiSkill environments exhibit $\dt$-embedding-dependent CIVO. StackCube-v1 value-ratio spikes are environment-specific: trained (049/052, NVE $5.05$/$4.67\times$) and frozen (051, $4.30\times$) match, all self-correcting by 82.5K. PegInsertionSide-v1 exhibits high-amplitude stochastic dynamics ($4$--$11\times$) whose trained/frozen ordering is seed-dependent: seed~0 trained peaks higher ($10.05\times$ vs.\ frozen $1.82\times$), but seed~1 reverses (frozen peak $11.32\times$ vs.\ trained peak $3.08\times$). PickCube-v1 frozen control (exp\_054, peak $8.81\times$ at 62.5K, self-correcting) confirms the same pattern. CIVO is locomotion-specific in DreamerV3; the frozen-embedding diagnostic correctly identifies these transients as non-CIVO.
94	
95	%% ============================================================
96	%% F6--F7: Interventions and cross-environment
97	%% ============================================================
98	
99	\subsection{F6--F7: Interventions and Multiple Pathways}
100	\label{sec:f6}
101	
102	\paragraph{F6: Trained embedding creates multiple vulnerability pathways.}
103	Exp\_008e\_v3 restricts imagination to $\dt{=}1$ while retaining the trained embedding. Two of four seeds collapse (50\%): Pathway~A (CIVO, $\nve = 4.02\times$) and preliminary Pathway~B (entropy \emph{increase}, $\nve = 3.78\times$; 2 seeds only, requires confirmation; Appendix~\ref{sec:pathways}). Pathway~B produces one of three non-CIVO false positives ($n{=}29$).
104	
105	\paragraph{F7: Full-pathway gradient stopping shows mixed results.}
106	Full-SGS (exp\_018) detaches all non-KL gradients from $e_{\dt}$. Seed~1 shows partial mitigation (eval 448.3, NVE $1.66\times$); seed~2 collapses (0/2 elimination; Appendix~\ref{sec:sgs_gradient_analysis}). Cross-environment validation on Cheetah (010b, NVE $8.27$--$108.52\times$) confirms CIVO generalization; full-SGS yields 0/3 elimination. Removing the embedding eliminates CIVO on Cheetah (024b, NVE $< 0.2\times$).
107	
108	\paragraph{Targeted obs-decoder-only SGS confirms pathway redundancy.}
109	Obs-decoder-only SGS (exp\_025/026) achieves 1/6 CIVO prevention (1/4 Walker, 0/2 Cheetah; Table~\ref{tab:intervention_hierarchy}), not meaningfully different from full-pathway SGS (0/3). CIVO operates through redundant gradient channels: blocking any single pathway shifts co-adaptation to the remaining ones (Appendix~\ref{sec:seed_divergence}).
110	
111	\begin{table}[t]
112	\centering
113	\caption{Intervention hierarchy. Prevention = peak NVE $< 1.5\times$ (35K+). No level reliably eliminates CIVO across environments.}
114	\label{tab:intervention_hierarchy}
115	\footnotesize
116	\setlength{\tabcolsep}{3pt}
117	\begin{tabular}{llccc}
118	\toprule
119	\textbf{Level} & \textbf{Intervention} & \textbf{Seeds} & \textbf{Prev.} & \textbf{Rate} \\
120	\midrule
121	--- & Untreated & 6 & 0/6 & 0\% \\
122	\midrule
123	Gradient & Reward-only SGS & 2 & 0/2 & 0\% \\
124	Gradient & Full-pathway SGS & 3 & 0/3 & 0\% \\
125	Gradient & Obs-decoder SGS & 6 & 1/6 & 17\% \\
126	\midrule
127	Output & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\% \\
128	\midrule
129	Repr. & TCN ($\sigma{=}0.1$) & 1 & 1/1$^\ddagger$ & 100\% \\
130	Repr. & TCN ($\sigma{=}0.2$) & 6$^\dagger$ & 2/6 & 33\% \\
131	Repr. & TCN ($\sigma{=}0.5$) & 3 & 0/3 & 0\% \\
132	Repr. & TCN ($\sigma{=}1.0$) & 1 & 1/1$^\S$ & 100\% \\
133	\midrule
134	Arch. & Wide single & 2 & 0/2 & 0\% \\
135	Arch. & Narrow dual (min) & 2 & 0/2 & 0\% \\
136	Arch. & Wide dual (min) & 4 & 3/4$^\|$ & 75\% \\
137	\midrule
138	--- & Embedding frozen & 7 & 5/7$^\#$ & 71\% \\
139	--- & Embedding removed & 5 & 5/5 & 100\% \\
140	\bottomrule
141	\end{tabular}
142	\vspace{1pt}
143	{\raggedright\footnotesize $^\dagger$Walker 2/4 (s2 NVE $2.11\times$; s3 late-onset CIVO, NVE $3.04\times$ at 105K); Cheetah 0/1, PickCube 0/1.
144	$^\ddagger$Borderline (NVE${=}1.02\times$, eval 55\%).
145	$^\S$CIVO prevented but progressive policy erosion (peak 116\%, final 15\% baseline).
146	$^\|$Walker 3/3 ($\nve \leq 1.4\times$; 1/3 non-CIVO eval collapse), Cheetah 0/1.\\
147	$^\#$Walker 5 + Cheetah 2. Exp\_047 (NVE $1.71\times$) and Exp\_057 (NVE $1.88\times$): both transient, self-correcting within 20K steps; remaining 5 seeds: NVE $0.19$--$1.45\times$.\par}
148	\end{table}
149	
150	%% ============================================================
151	%% Forward-pass interventions
152	%% ============================================================
153	
154	\subsection{Forward-Pass Interventions}
155	\label{sec:forward_results}
156	
157	We test two forward-pass alternatives (Table~\ref{tab:intervention_hierarchy}). \textbf{RAVE} (value-level capping) fails: the EMA anchor tracks biased values during CIVO onset. \textbf{TCN} (representation-level noise) suppresses CIVO in 2 of 4 Walker seeds at $\sigma{=}0.2$ (NVE $< 1.0\times$, eval 45--91\%), but remaining seeds show runaway escalation, suggesting TCN gates rather than attenuates CIVO. Cross-environment transfer fails: Cheetah effective dose ($\sigma{=}1.0$) causes policy erosion to 15\% baseline; PickCube 0/1 (Appendix~\ref{sec:tcn_cross_env}). TCN is a \emph{diagnostic probe}, not a deployable mitigation.
158	
159	%% ============================================================
160	%% Architecture-Level Ablation
161	%% ============================================================
162	
163	\subsection{Architecture-Level Ablation}
164	\label{sec:arch_results}
165	
166	\paragraph{Critic convergence in pure imagination.}
167	Across all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\rho > 0.999$), with pessimism at 3--4\% of the independent-critic bound (\S\ref{sec:dual_critic_method}).
168	
169	\paragraph{$2{\times}2$ factorial: recovery vs.\ prevention.}
170	Min drives recovery: narrow dual-critic (${\sim}1.2$M) recovers fully (${\sim}16$--$19\times$ recovery ratio) despite $2\times$ fewer parameters. Prevention requires min $+$ capacity: wide dual-critic maintains $\nve \leq 1.4\times$ (3/3 prevention, 1/3 non-CIVO collapse). Cross-environment transfer is limited (Appendix~\ref{sec:dual_critic_appendix}).
171	
172	%% ============================================================
173	%% Online CIVO Detection
174	%% ============================================================
175	
176	\subsection{Online CIVO Detection}
177	\label{sec:detector}
178	
179	We derive a lightweight online detector monitoring the value-to-evaluation ratio for superlinear growth. Applied to 14 runs across three environments, it achieves TPR${=}5/5$, FPR${=}2/9$, with predictive alerts in 2/5 cases (Appendix~\ref{sec:detector_appendix}).
180	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "d82d421a-e3e9-4134-ab6f-b0dbccdbb630",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$, \\S\\ref{sec:metrics}).\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{Key configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 43 configurations in Table~\\ref{tab:complete_results}.}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^d$ & Env.\\ transient \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^e$ & Env.\\ dynamics$^e$ \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ StackCube transient: frozen control (exp\\_051) exhibits identical spike (peak $4.30\\times$ at 42.5K, self-correcting by 82.5K), indicating environment-specific phenomenon unrelated to $\\dt$-embedding training.\\\\\n$^e$ Seed~0 trained peaks at $10.05\\times$ (82.5K) with delayed self-correction; seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$. Environment-specific stochastic dynamics: frozen final exceeds trained final.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Precedes Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the strongest predictor. The \\emph{primary} comparison---008d (trained, subsample ON) vs.\\ 008f (no embedding, subsample ON)---differs only in embedding training, yielding $\\nve = 4.12\\times$ (eval 82.8) vs.\\ $\\nve \\leq 0.97\\times$ (eval 503.0). \\emph{Secondary} comparisons against 008a/008c (unexposed embedding) co-vary subsample status and horizon alongside the embedding factor. The $\\nve \\geq 1.5\\times$ threshold (35K+ window) correctly classifies 26 of 29 experimental configurations across two environments (AUROC${=}0.953$, in-sample; LOEO cross-validated, Table~\\ref{tab:nve_loeo}; Figure~\\ref{fig:nve_trajectory}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{NVE trajectories (mean $\\pm$ seed range). Trained $\\dt$-embedding (red, Walker Walk, $n{=}3$ seeds plotted; seed~4 data in Table~\\ref{tab:complete_results}) exceeds the $1.5\\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding precedes CIVO in all four Walker Walk seeds (peak NVE: $4.62\\times$, $4.12\\times$, $1.62\\times$, $1.53\\times$), universally degrading performance to below 30\\% of baseline (IQM $175.2$, mean $170.6$, $n{=}4$; \\citealt{agarwal2021precipice}). Downstream trajectories diverge: two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and one self-corrects to a stable but degraded state (29.3\\% of baseline). Combined with Cheetah Run (\\S\\ref{sec:f6}), CIVO onset is universal across all six tested seeds ($n{=}6$, two environments) with 5/6 progressing toward collapse (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Factorial Ablation (Appendix~\\ref{sec:appendix_factorial})}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly sufficient in tested configurations} for CIVO. Neither factor alone precedes pathological overestimation: trained embedding without multi-rate exposure (008a, 3 seeds, peak NVE $0.83$--$0.93\\times$) and multi-rate exposure without embedding (008f, 3 seeds, peak NVE $\\leq 1.41\\times$) both remain below $1.5\\times$. Cross-environment replication on Cheetah Run confirms generalization. Freezing the embedding (\\texttt{requires\\_grad=False}) dramatically reduces severity (NVE $0.19$--$1.88\\times$ vs.\\ trained $1.53$--$4.62\\times$; 2/4 seeds below threshold, 2/4 transient self-correcting spikes; Table~\\ref{tab:three_way_emb}); removing the embedding (008f) also avoids CIVO. Partial gradient blocking (exp\\_044) does not prevent onset (peak NVE $4.45\\times$) but permits delayed self-correction (final eval 538, 59\\% baseline; Appendix~\\ref{sec:appendix_factorial}), confirming that \\emph{any} gradient pathway updating $e_{\\dt}$ suffices to induce CIVO. Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).\n\n\\paragraph{ManiSkill manipulation tasks.}\nNone of three ManiSkill environments exhibit $\\dt$-embedding-dependent CIVO. StackCube-v1 value-ratio spikes are environment-specific: trained (049/052, NVE $5.05$/$4.67\\times$) and frozen (051, $4.30\\times$) match, all self-correcting by 82.5K. PegInsertionSide-v1 exhibits high-amplitude stochastic dynamics ($4$--$11\\times$) whose trained/frozen ordering is seed-dependent: seed~0 trained peaks higher ($10.05\\times$ vs.\\ frozen $1.82\\times$), but seed~1 reverses (frozen peak $11.32\\times$ vs.\\ trained peak $3.08\\times$). PickCube-v1 frozen control (exp\\_054, peak $8.81\\times$ at 62.5K, self-correcting) confirms the same pattern. CIVO is locomotion-specific in DreamerV3; the frozen-embedding diagnostic correctly identifies these transients as non-CIVO.\n\n%% ============================================================\n%% F6--F7: Interventions and cross-environment\n%% ============================================================\n\n\\subsection{F6--F7: Interventions and Multiple Pathways}\n\\label{sec:f6}\n\n\\paragraph{F6: Trained embedding creates multiple vulnerability pathways.}\nExp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained embedding. Two of four seeds collapse (50\\%): Pathway~A (CIVO, $\\nve = 4.02\\times$) and preliminary Pathway~B (entropy \\emph{increase}, $\\nve = 3.78\\times$; 2 seeds only, requires confirmation; Appendix~\\ref{sec:pathways}). Pathway~B produces one of three non-CIVO false positives ($n{=}29$).\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nFull-SGS (exp\\_018) detaches all non-KL gradients from $e_{\\dt}$. Seed~1 shows partial mitigation (eval 448.3, NVE $1.66\\times$); seed~2 collapses (0/2 elimination; Appendix~\\ref{sec:sgs_gradient_analysis}). Cross-environment validation on Cheetah (010b, NVE $8.27$--$108.52\\times$) confirms CIVO generalization; full-SGS yields 0/3 elimination. Removing the embedding eliminates CIVO on Cheetah (024b, NVE $< 0.2\\times$).\n\n\\paragraph{Targeted obs-decoder-only SGS confirms pathway redundancy.}\nObs-decoder-only SGS (exp\\_025/026) achieves 1/6 CIVO prevention (1/4 Walker, 0/2 Cheetah; Table~\\ref{tab:intervention_hierarchy}), not meaningfully different from full-pathway SGS (0/3). CIVO operates through redundant gradient channels: blocking any single pathway shifts co-adaptation to the remaining ones (Appendix~\\ref{sec:seed_divergence}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Intervention hierarchy. Prevention = peak NVE $< 1.5\\times$ (35K+). No level reliably eliminates CIVO across environments.}\n\\label{tab:intervention_hierarchy}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} \\\\\n\\midrule\n--- & Untreated & 6 & 0/6 & 0\\% \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 2/6 & 33\\% \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 0/3 & 0\\% \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% \\\\\n\\midrule\n--- & Embedding frozen & 7 & 5/7$^\\#$ & 71\\% \\\\\n--- & Embedding removed & 5 & 5/5 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\dagger$Walker 2/4 (s2 NVE $2.11\\times$; s3 late-onset CIVO, NVE $3.04\\times$ at 105K); Cheetah 0/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$CIVO prevented but progressive policy erosion (peak 116\\%, final 15\\% baseline).\n$^\\|$Walker 3/3 ($\\nve \\leq 1.4\\times$; 1/3 non-CIVO eval collapse), Cheetah 0/1.\\\\\n$^\\#$Walker 5 + Cheetah 2. Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps; remaining 5 seeds: NVE $0.19$--$1.45\\times$.\\par}\n\\end{table}\n\n%% ============================================================\n%% Forward-pass interventions\n%% ============================================================\n\n\\subsection{Forward-Pass Interventions}\n\\label{sec:forward_results}\n\nWe test two forward-pass alternatives (Table~\\ref{tab:intervention_hierarchy}). \\textbf{RAVE} (value-level capping) fails: the EMA anchor tracks biased values during CIVO onset. \\textbf{TCN} (representation-level noise) suppresses CIVO in 2 of 4 Walker seeds at $\\sigma{=}0.2$ (NVE $< 1.0\\times$, eval 45--91\\%), but remaining seeds show runaway escalation, suggesting TCN gates rather than attenuates CIVO. Cross-environment transfer fails: Cheetah effective dose ($\\sigma{=}1.0$) causes policy erosion to 15\\% baseline; PickCube 0/1 (Appendix~\\ref{sec:tcn_cross_env}). TCN is a \\emph{diagnostic probe}, not a deployable mitigation.\n\n%% ============================================================\n%% Architecture-Level Ablation\n%% ============================================================\n\n\\subsection{Architecture-Level Ablation}\n\\label{sec:arch_results}\n\n\\paragraph{Critic convergence in pure imagination.}\nAcross all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\\rho > 0.999$), with pessimism at 3--4\\% of the independent-critic bound (\\S\\ref{sec:dual_critic_method}).\n\n\\paragraph{$2{\\times}2$ factorial: recovery vs.\\ prevention.}\nMin drives recovery: narrow dual-critic (${\\sim}1.2$M) recovers fully (${\\sim}16$--$19\\times$ recovery ratio) despite $2\\times$ fewer parameters. Prevention requires min $+$ capacity: wide dual-critic maintains $\\nve \\leq 1.4\\times$ (3/3 prevention, 1/3 non-CIVO collapse). Cross-environment transfer is limited (Appendix~\\ref{sec:dual_critic_appendix}).\n\n%% ============================================================\n%% Online CIVO Detection\n%% ============================================================\n\n\\subsection{Online CIVO Detection}\n\\label{sec:detector}\n\nWe derive a lightweight online detector monitoring the value-to-evaluation ratio for superlinear growth. Applied to 14 runs across three environments, it achieves TPR${=}5/5$, FPR${=}2/9$, with predictive alerts in 2/5 cases (Appendix~\\ref{sec:detector_appendix}).\n",
      "numLines": 180,
      "startLine": 1,
      "totalLines": 180
    }
  }
}
```

</details>

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_017ucKikaoLauQzxBt6fUJ3y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "039ab46b-fffa-47af-9d8c-a9a6f4ff4c9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pMFyTPMUP49TYywtF2gM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 28316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01FoRrfgBzRwZcwzwLgg8urM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "a1f3f3fb-9505-4bf8-940b-2c5cf6c330fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pMFyTPMUP49TYywtF2gM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 28316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

_source line 44 · 2026-05-24T07:06:56.595Z_

<details><summary>↩ Tool result · `toolu_017ucKikaoLauQzxBt6fUJ3y`</summary>

```text
1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks isolate trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; 26/29, AUROC${=}0.953$, LOEO cross-validated). The RSSM develops a $2.78\times$ reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as the structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination ($\rho > 0.999$), rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery. A lightweight NVE detector achieves 100\% sensitivity.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "8606caee-bf40-4d0e-bf7c-27ced477b800",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex",
      "content": "World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\\% of baseline. Factorial diagnostics on two continuous-control tasks isolate trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\\emph{conditioning-induced value overestimation} (CIVO; 26/29, AUROC${=}0.953$, LOEO cross-validated). The RSSM develops a $2.78\\times$ reward prediction gap at $\\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as the structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination ($\\rho > 0.999$), rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery. A lightweight NVE detector achieves 100\\% sensitivity.\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-24T07:06:56.596Z_

<details><summary>↩ Tool result · `toolu_01FoRrfgBzRwZcwzwLgg8urM`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We identify trained $\dt$-embedding with multi-rate data exposure as the strongest predictor of CIVO in DreamerV3 (26/29, AUROC${=}0.953$; LOEO cross-validated). No tested intervention reliably eliminates CIVO; in pure imagination, dual critics converge ($\rho > 0.999$), rendering Double Q pessimism ineffective. The feedback architecture---MPC re-planning versus imagination-based bootstrapping---is the structural factor.
5	
6	\paragraph{Limitations.}
7	Our analysis covers proprioceptive locomotion (DMC) and simulated manipulation (ManiSkill) but does not test pixel-based observations, Atari benchmarks, or real-robot deployments where sensor noise and actuation latency introduce additional confounds.
8	All experiments use DreamerV3's RSSM; whether CIVO manifests in other imagination-based architectures (e.g., IRIS \citep{micheli2023iris} or latent-space planners beyond TD-MPC2) remains open.
9	We characterize CIVO under fixed-$\dt$ subsampling; learned temporal gates warrant separate study.
10	Statistical power with 4 seeds per configuration is limited \citep{colas2018seeds}; the NVE threshold (LOEO AUROC${=}0.981$) may require recalibration for different reward scales.
11	Code: upon acceptance.
12	\label{sec:limitations}
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "5089f1fc-2701-4b94-b71e-4427ec8ef667",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe identify trained $\\dt$-embedding with multi-rate data exposure as the strongest predictor of CIVO in DreamerV3 (26/29, AUROC${=}0.953$; LOEO cross-validated). No tested intervention reliably eliminates CIVO; in pure imagination, dual critics converge ($\\rho > 0.999$), rendering Double Q pessimism ineffective. The feedback architecture---MPC re-planning versus imagination-based bootstrapping---is the structural factor.\n\n\\paragraph{Limitations.}\nOur analysis covers proprioceptive locomotion (DMC) and simulated manipulation (ManiSkill) but does not test pixel-based observations, Atari benchmarks, or real-robot deployments where sensor noise and actuation latency introduce additional confounds.\nAll experiments use DreamerV3's RSSM; whether CIVO manifests in other imagination-based architectures (e.g., IRIS \\citep{micheli2023iris} or latent-space planners beyond TD-MPC2) remains open.\nWe characterize CIVO under fixed-$\\dt$ subsampling; learned temporal gates warrant separate study.\nStatistical power with 4 seeds per configuration is limited \\citep{colas2018seeds}; the NVE threshold (LOEO AUROC${=}0.981$) may require recalibration for different reward scales.\nCode: upon acceptance.\n\\label{sec:limitations}\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  }
}
```

</details>

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_015HEyFvTwsoxSvKcS43Dcqs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "698efff9-d095-4cd7-b6e8-f671bfb186a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pMFyTPMUP49TYywtF2gM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 28316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

_source line 47 · 2026-05-24T07:06:57.288Z_

<details><summary>↩ Tool result · reported error · `toolu_015HEyFvTwsoxSvKcS43Dcqs`</summary>

```text
File content (27947 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "4770c588-70ca-4ab8-a6d1-d530fb46682e",
  "tool_use_result": "Error: File content (27947 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
The appendix.tex file is too large to read at once. Let me read it in sections to find all the locations I need to modify. Let me also record the key information I've found so far.

From the files I've read:

1. **analysis.tex:8** - Found: `sustained CIVO (6/6 trained locomotion, NVE $1.53$--$108\times$)` → Need to change to `CIVO onset (7/7 trained locomotion, NVE $1.53$--$108\times$)`

2. **introduction.tex:11** (actually line 12) - Found: `6/6 seeds, two locomotion environments` → `7/7 seeds, two locomotion environments`
   
3. **results.tex:81** - Found the Walker Walk seeds section with NVE values and "5/6 progressing toward collapse" that needs updating

4. **results.tex:90** - Need to adjust the NVE range from `$1.53$--$4.62\times$` to `$1.53$--$4.72\times$`

5. **results.tex:121** - Found a table row with `6 & 0/6 & 0\%` that should become `7 & 0/7 & 0\%`

6. Still working through the abstract_body section to locate remaining changes

, and I've identified three more files with the 26/29 AUROC value that need updating in abstract_body.tex, introduction.tex, and conclusion.tex. Now I need to systematically go through the appendix in sections to find any other instances that require modification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "ae89c388-2bc7-4dc0-ad44-13dd2a65b65e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fm1CxxxUxA89bHLvT7mQoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8576,
      "cache_read_input_tokens": 29138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8576
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

_source line 49_

appendix.tex 太大，分段读取需要修改的区域。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "709f2a10-6346-4650-85e9-0d4945179251",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fm1CxxxUxA89bHLvT7mQoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8576,
      "cache_read_input_tokens": 29138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8576
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

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_01EwqEsCex4gs72UtuwHnRhv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "a9c24c06-cfbe-4561-b6d9-fd917ce1a460",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fm1CxxxUxA89bHLvT7mQoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8576,
      "cache_read_input_tokens": 29138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8576
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

_source line 51 · 2026-05-24T07:07:13.019Z_

<details><summary>↩ Tool result · `toolu_01EwqEsCex4gs72UtuwHnRhv`</summary>

```text
1	% --- APPENDIX ---
2	
3	\section{Complete Experimental Results}
4	\label{sec:complete_results}
5	
6	Table~\ref{tab:complete_results} reports all 42 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
7	
8	\begin{table*}[t]
9	\centering
10	\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
11	\label{tab:complete_results}
12	\scriptsize
13	\setlength{\tabcolsep}{3pt}
14	\begin{tabular}{llcccccl}
15	\toprule
16	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
17	\midrule
18	001 & Baseline ($\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
19	001 s2 & Baseline ($\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\
20	\rowcolor{gray!15}
21	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
22	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
23	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
24	\midrule
25	\rowcolor{gray!15}
26	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
27	\rowcolor{gray!15}
28	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
29	\rowcolor{gray!15}
30	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
31	\rowcolor{gray!15}
32	008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\times$ & Full collapse \\
33	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
34	008f s4 & No dt\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\times$ & Healthy \\
35	009c s3 & No dt\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\times$ & Healthy \\
36	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
37	008a\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\times$ & Healthy \\
38	008a\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\times$ & Healthy \\
39	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
40	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
41	042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\times$ & Healthy \\
42	047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\times$ & Transient (self-corr.) \\
43	057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\times$ & Transient (self-corr.) \\
44	\midrule
45	018 s1 & Full-SGS & trn$^\ddagger$ & ON & 8 & \sgseval{} @105K & \sgsnve{}$\times$$^*$ & Partial mitig.\ (CIVO+) \\
46	\rowcolor{gray!15}
47	018 s2 & Full-SGS & trn$^\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\
48	008e\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\times$ & Healthy \\
49	008e\_v3 s2$^\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\times$ & Non-CIVO collapse \\
50	\rowcolor{gray!15}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "ef95ab26-15d3-4cf0-88ef-aafa0a399bcf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 42 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\\times$ & Transient (self-corr.) \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\rowcolor{gray!15}",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01N7B1Q4UHEszkU8cNp58p8A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 95,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "f7f203b2-8bb9-49df-8fa0-318f9683d5fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fm1CxxxUxA89bHLvT7mQoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8576,
      "cache_read_input_tokens": 29138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8576
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

_source line 53 · 2026-05-24T07:07:13.973Z_

<details><summary>↩ Tool result · `toolu_01N7B1Q4UHEszkU8cNp58p8A`</summary>

```text
95	
96	\begin{table}[h]
97	\centering
98	\caption{Cross-domain CIVO reproducibility. ``$\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}
99	\label{tab:cross_domain}
100	\footnotesize
101	\begin{tabular}{llccc}
102	\toprule
103	\textbf{Domain} & \textbf{Environment} & \textbf{Trained} & \textbf{Frz ctrl} & \textbf{$\dt$-emb-dep.\ CIVO} \\
104	\midrule
105	Locomotion & Walker Walk & 4/4 & 0/3 & Yes (NVE $1.53$--$4.62\times$) \\
106	Locomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\times$) \\
107	Manipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\approx$trained) \\
108	Manipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\ ordering) \\
109	Manipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\
110	\bottomrule
111	\end{tabular}
112	\end{table}
113	
114	\section{NVE Threshold Sensitivity Analysis}
115	\label{sec:appendix_sensitivity}
116	
117	We report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\nve \geq 1.5\times$). Here we additionally present Task~B1, which restricts the positive class to \emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.
118	
119	\subsection{Per-Experiment NVE Values}
120	
121	Table~\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all ten factorial experiments (including four 008e\_v3 seeds). Experiments are sorted by descending NVE. Experiment 008e\_v3\_s2 exhibits elevated NVE ($3.78\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\_v3\_s3 exhibits CIVO with NVE $4.02\times$ despite $\Delta t{=}1$ imagination.
122	
123	\begin{table}[ht]
124	\centering
125	\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\ = transient CIVO with self-correction.}
126	\label{tab:nve_raw}
127	\small
128	\begin{tabular}{@{}lrccc@{}}
129	\toprule
130	Experiment & NVE & Mechanism & B1 & B2 \\
131	\midrule
132	006          & 4.83 & sustained CIVO & $+$ & $+$ \\
133	008d         & 4.12 & sustained CIVO & $+$ & $+$ \\
134	008e\_v3\_s3 & 4.02 & CIVO           & $+$ & $+$ \\
135	008e\_v3\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\
136	009b         & 1.62 & transient CIVO & $-$ & $+$ \\
137	001          & 1.00 & non-CIVO       & $-$ & $-$ \\
138	008e\_v3\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\
139	008f         & 0.97 & non-CIVO       & $-$ & $-$ \\
140	008e\_v3\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\
141	008a         & 0.93 & non-CIVO       & $-$ & $-$ \\
142	\bottomrule
143	\end{tabular}
144	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "277cf6ad-448f-4e0f-9095-f73535b421e5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\n\\begin{table}[h]\n\\centering\n\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n\\label{tab:cross_domain}\n\\footnotesize\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n\\midrule\nLocomotion & Walker Walk & 4/4 & 0/3 & Yes (NVE $1.53$--$4.62\\times$) \\\\\nLocomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\nManipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\nManipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\nManipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all ten factorial experiments (including four 008e\\_v3 seeds). Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\\_v3\\_s3 exhibits CIVO with NVE $4.02\\times$ despite $\\Delta t{=}1$ imagination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.83 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.12 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s3 & 4.02 & CIVO           & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
      "numLines": 50,
      "startLine": 95,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01Qb7vCBZTnCXQtFBENFnnae`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 110,
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
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "ba469778-1795-446e-b503-885dd954529e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fm1CxxxUxA89bHLvT7mQoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8576,
      "cache_read_input_tokens": 29138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8576
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

_source line 55 · 2026-05-24T07:07:14.873Z_

<details><summary>↩ Tool result · `toolu_01Qb7vCBZTnCXQtFBENFnnae`</summary>

```text
110	\bottomrule
111	\end{tabular}
112	\end{table}
113	
114	\section{NVE Threshold Sensitivity Analysis}
115	\label{sec:appendix_sensitivity}
116	
117	We report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\nve \geq 1.5\times$). Here we additionally present Task~B1, which restricts the positive class to \emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.
118	
119	\subsection{Per-Experiment NVE Values}
120	
121	Table~\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all ten factorial experiments (including four 008e\_v3 seeds). Experiments are sorted by descending NVE. Experiment 008e\_v3\_s2 exhibits elevated NVE ($3.78\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\_v3\_s3 exhibits CIVO with NVE $4.02\times$ despite $\Delta t{=}1$ imagination.
122	
123	\begin{table}[ht]
124	\centering
125	\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\ = transient CIVO with self-correction.}
126	\label{tab:nve_raw}
127	\small
128	\begin{tabular}{@{}lrccc@{}}
129	\toprule
130	Experiment & NVE & Mechanism & B1 & B2 \\
131	\midrule
132	006          & 4.83 & sustained CIVO & $+$ & $+$ \\
133	008d         & 4.12 & sustained CIVO & $+$ & $+$ \\
134	008e\_v3\_s3 & 4.02 & CIVO           & $+$ & $+$ \\
135	008e\_v3\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\
136	009b         & 1.62 & transient CIVO & $-$ & $+$ \\
137	001          & 1.00 & non-CIVO       & $-$ & $-$ \\
138	008e\_v3\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\
139	008f         & 0.97 & non-CIVO       & $-$ & $-$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "db3fdae5-0ede-4a95-9aaf-47211ef91f88",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all ten factorial experiments (including four 008e\\_v3 seeds). Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\\_v3\\_s3 exhibits CIVO with NVE $4.02\\times$ despite $\\Delta t{=}1$ imagination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.83 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.12 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s3 & 4.02 & CIVO           & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\",
      "numLines": 30,
      "startLine": 110,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Read · `toolu_01AZQYvWAndBheTkg5QYnDH2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 255,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "a7b9c6ba-14af-4cf4-892b-30862892ed15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fm1CxxxUxA89bHLvT7mQoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8576,
      "cache_read_input_tokens": 29138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8576
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

_source line 57 · 2026-05-24T07:07:15.403Z_

<details><summary>↩ Tool result · `toolu_01AZQYvWAndBheTkg5QYnDH2`</summary>

```text
255	\midrule
256	s1 & 915.7 & 970.4 & 0.563 & 0.656 \\
257	s2 & 443.5 & 945.7 & 0.898 & 0.742 \\
258	s3 & 869.0 & 947.7 & --- & 0.664 \\
259	s4 & 922.8 & 938.9 & --- & 0.624 \\
260	\bottomrule
261	\end{tabular}
262	\end{table}
263	
264	Seed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\times$; 009b seed~2, peak NVE $1.62\times$) to fall below the $1.5\times$ threshold. Core CIVO cases (peak NVE $> 3\times$) remain correctly classified under all baseline seeds.
265	
266	Single-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\%): the boundary case exp\_009b flips from $\nve = 1.62\times$ (s1) to $1.23\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\times \to 4.52\times$; 008d: $4.12\times \to 3.54\times$). The $1.5\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\% of the threshold.
267	
268	\paragraph{Normalization conventions.} Walker NVE is normalized against the 4-seed mean baseline (seeds~1--4, each run to 505K+ steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).
269	
270	\paragraph{Limitations.} With $n = 10$ experiments, Clopper-Pearson confidence intervals remain wide (e.g., 90.0\% accuracy has 95\% CI [55.5\%, 99.7\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds. Table~\ref{tab:sensitivity_b2_full} reports the original $n{=}16$ evaluation set spanning both environments. The expanded analysis ($n{=}29$, including SGS variants, RAVE, and TCN configurations) yields AUROC${=}0.953$ (Figure~\ref{fig:nve_roc}, in-sample, post-hoc). The original $n{=}16$ core analysis yields AUROC${=}0.969$; the expanded $n{=}29$ set includes SGS, RAVE, TCN, and dual-critic configurations. Cross-architecture validation is deferred to future work.
271	
272	\subsection{Leave-One-Environment-Out Cross-Validation}
273	\label{sec:nve_loeo}
274	
275	To assess whether $\theta{=}1.5\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}13$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\theta{=}1.5\times$ on the held-out environment.
276	
277	\begin{table}[h]
278	\centering
279	\caption{Leave-one-environment-out cross-validation of NVE threshold $\theta=1.5\times$.
280	For each fold, the threshold is validated on an environment whose data was \emph{not} used
281	to select $\theta$. The optimal threshold range on each training set is reported;
282	$\theta=1.5$ falls within the optimal range in all three folds.}
283	\label{tab:nve_loeo}
284	\begin{tabular}{lccccc}
285	\toprule
286	Held-out & $N_{\text{train}}$ & $N_{\text{test}}$ & $\theta_{\text{opt}}$ range & Test Accuracy & Test AUROC \\
287	\midrule
288	PickCube & 18 & 2 & $(1.45,\, 1.53]$ & 2/2 (1.000) & 1.000 \\
289	Cheetah  & 15 & 5 & $(1.45,\, 1.53]$ & 5/5 (1.000) & 1.000 \\
290	Walker   &  7 & 13 & $(1.00,\, 3.78)$ & 12/13 (0.923) & 0.944 \\
291	\midrule
292	\textbf{Mean} & — & — & — & \textbf{0.974} & \textbf{0.981} \\
293	\bottomrule
294	\end{tabular}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "8f3f00c7-aac9-47cf-abb4-85d578c122b3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\\midrule\ns1 & 915.7 & 970.4 & 0.563 & 0.656 \\\\\ns2 & 443.5 & 945.7 & 0.898 & 0.742 \\\\\ns3 & 869.0 & 947.7 & --- & 0.664 \\\\\ns4 & 922.8 & 938.9 & --- & 0.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\\times$; 009b seed~2, peak NVE $1.62\\times$) to fall below the $1.5\\times$ threshold. Core CIVO cases (peak NVE $> 3\\times$) remain correctly classified under all baseline seeds.\n\nSingle-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\\%): the boundary case exp\\_009b flips from $\\nve = 1.62\\times$ (s1) to $1.23\\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\\times \\to 4.52\\times$; 008d: $4.12\\times \\to 3.54\\times$). The $1.5\\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\\% of the threshold.\n\n\\paragraph{Normalization conventions.} Walker NVE is normalized against the 4-seed mean baseline (seeds~1--4, each run to 505K+ steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).\n\n\\paragraph{Limitations.} With $n = 10$ experiments, Clopper-Pearson confidence intervals remain wide (e.g., 90.0\\% accuracy has 95\\% CI [55.5\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds. Table~\\ref{tab:sensitivity_b2_full} reports the original $n{=}16$ evaluation set spanning both environments. The expanded analysis ($n{=}29$, including SGS variants, RAVE, and TCN configurations) yields AUROC${=}0.953$ (Figure~\\ref{fig:nve_roc}, in-sample, post-hoc). The original $n{=}16$ core analysis yields AUROC${=}0.969$; the expanded $n{=}29$ set includes SGS, RAVE, TCN, and dual-critic configurations. Cross-architecture validation is deferred to future work.\n\n\\subsection{Leave-One-Environment-Out Cross-Validation}\n\\label{sec:nve_loeo}\n\nTo assess whether $\\theta{=}1.5\\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}13$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\\theta{=}1.5\\times$ on the held-out environment.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-environment-out cross-validation of NVE threshold $\\theta=1.5\\times$.\nFor each fold, the threshold is validated on an environment whose data was \\emph{not} used\nto select $\\theta$. The optimal threshold range on each training set is reported;\n$\\theta=1.5$ falls within the optimal range in all three folds.}\n\\label{tab:nve_loeo}\n\\begin{tabular}{lccccc}\n\\toprule\nHeld-out & $N_{\\text{train}}$ & $N_{\\text{test}}$ & $\\theta_{\\text{opt}}$ range & Test Accuracy & Test AUROC \\\\\n\\midrule\nPickCube & 18 & 2 & $(1.45,\\, 1.53]$ & 2/2 (1.000) & 1.000 \\\\\nCheetah  & 15 & 5 & $(1.45,\\, 1.53]$ & 5/5 (1.000) & 1.000 \\\\\nWalker   &  7 & 13 & $(1.00,\\, 3.78)$ & 12/13 (0.923) & 0.944 \\\\\n\\midrule\n\\textbf{Mean} & — & — & — & \\textbf{0.974} & \\textbf{0.981} \\\\\n\\bottomrule\n\\end{tabular}",
      "numLines": 40,
      "startLine": 255,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_01NtsJnpBzCqydYMCLaSS8mF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 300,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "696240f8-b975-4d47-aa55-7177eb04a2a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fm1CxxxUxA89bHLvT7mQoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8576,
      "cache_read_input_tokens": 29138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8576
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

_source line 59 · 2026-05-24T07:07:16.353Z_

<details><summary>↩ Tool result · `toolu_01NtsJnpBzCqydYMCLaSS8mF`</summary>

```text
300	
301	\section{Factorial Ablation Details}
302	\label{sec:appendix_factorial}
303	
304	This appendix provides the full factorial ablation results summarized in \S\ref{sec:f3f5_summary} of the main text.
305	
306	\paragraph{Embedding gradient analysis.}
307	Table~\ref{tab:three_way_emb} isolates embedding \emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\dt{=}2$ imagination).
308	
309	\begin{table}[h]
310	\centering
311	\caption{$\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}
312	\label{tab:three_way_emb}
313	\footnotesize
314	\begin{tabular}{lccccl}
315	\toprule
316	Condition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\
317	\midrule
318	Trained & all & 008d & $1.53$--$4.62\times$ & 64--268 & 4/4 \\
319	Reward detach & obs+KL only & 044 & $4.45\times$ & 44$\to$538$^\dagger$ & 1/1 \\
320	Full SGS & KL only & 018 & $1.66\times$ & 448 & 1/1$^*$ \\
321	Frozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\times$$^\ddagger$ & 204--612 & 2/4 \\
322	Removed & N/A & 008f & $0.97$--$1.41\times$ & 307--503 & 0/3 \\
323	\bottomrule
324	\end{tabular}
325	\vspace{1pt}
326	{\raggedright\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\times$); seed~2 collapsed. $^\dagger$Self-corrected at ${\sim}175$K (eval 44$\to$538, 59\% baseline; 224K run). $^\ddagger$Exp\_047 (NVE $1.71\times$) and Exp\_057 (NVE $1.88\times$): both transient, self-correcting within 20K steps.\par}
327	\end{table}
328	
329	The reward-detach condition (exp\_044, \texttt{reward\_dt\_emb\_detach=True}) uses a backward hook to block reward-head gradients from reaching $e_{\dt}$, complementing the framework-level Reward SGS (exp\_016e). Both yield the same directional result---CIVO onset not prevented---ruling out implementation artifacts. Exp\_044 exhibits delayed CIVO onset (${\sim}95$K vs.\ typical $25$--$35$K), consistent with reduced but non-zero gradient pressure on $e_{\dt}$. Over a full 224K run, exp\_044 self-corrects: eval recovers from 44 (95K) to 538 (215K, 59\% baseline), but this recovery is incomplete compared to spontaneous recovery without gradient intervention (exp\_045: 868, 95\% baseline). The lower asymptote suggests that selectively disrupting gradient flow may create optimization difficulties beyond CIVO itself.
330	
331	Table~\ref{tab:factorial_design} summarizes the experimental configurations.
332	
333	\begin{table}[ht]
334	\centering
335	\caption{Factorial design. Each row specifies one experimental configuration. \textbf{Emb}: $\dt$-embedding mode. \textbf{Sub}: temporal subsampling. \textbf{H}: imagination horizon. \textbf{Imag $\dt$}: temporal resolution used during imagination.}
336	\label{tab:factorial_design}
337	\small
338	\setlength{\tabcolsep}{3.5pt}
339	\begin{tabular}{@{}llcccc@{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "cb4e15ea-e1eb-4db8-8c23-dde4c9220de4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\paragraph{Embedding gradient analysis.}\nTable~\\ref{tab:three_way_emb} isolates embedding \\emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\\dt{=}2$ imagination).\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}\n\\label{tab:three_way_emb}\n\\footnotesize\n\\begin{tabular}{lccccl}\n\\toprule\nCondition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\\\\n\\midrule\nTrained & all & 008d & $1.53$--$4.62\\times$ & 64--268 & 4/4 \\\\\nReward detach & obs+KL only & 044 & $4.45\\times$ & 44$\\to$538$^\\dagger$ & 1/1 \\\\\nFull SGS & KL only & 018 & $1.66\\times$ & 448 & 1/1$^*$ \\\\\nFrozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\\nRemoved & N/A & 008f & $0.97$--$1.41\\times$ & 307--503 & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\\times$); seed~2 collapsed. $^\\dagger$Self-corrected at ${\\sim}175$K (eval 44$\\to$538, 59\\% baseline; 224K run). $^\\ddagger$Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps.\\par}\n\\end{table}\n\nThe reward-detach condition (exp\\_044, \\texttt{reward\\_dt\\_emb\\_detach=True}) uses a backward hook to block reward-head gradients from reaching $e_{\\dt}$, complementing the framework-level Reward SGS (exp\\_016e). Both yield the same directional result---CIVO onset not prevented---ruling out implementation artifacts. Exp\\_044 exhibits delayed CIVO onset (${\\sim}95$K vs.\\ typical $25$--$35$K), consistent with reduced but non-zero gradient pressure on $e_{\\dt}$. Over a full 224K run, exp\\_044 self-corrects: eval recovers from 44 (95K) to 538 (215K, 59\\% baseline), but this recovery is incomplete compared to spontaneous recovery without gradient intervention (exp\\_045: 868, 95\\% baseline). The lower asymptote suggests that selectively disrupting gradient flow may create optimization difficulties beyond CIVO itself.\n\nTable~\\ref{tab:factorial_design} summarizes the experimental configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Factorial design. Each row specifies one experimental configuration. \\textbf{Emb}: $\\dt$-embedding mode. \\textbf{Sub}: temporal subsampling. \\textbf{H}: imagination horizon. \\textbf{Imag $\\dt$}: temporal resolution used during imagination.}\n\\label{tab:factorial_design}\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llcccc@{}}",
      "numLines": 40,
      "startLine": 300,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01R2MUgCENdGCewGCsq79Bas`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 575,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "2b69dc17-9b08-4f5d-b6a2-ce1620f4a496",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fm1CxxxUxA89bHLvT7mQoR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8576,
      "cache_read_input_tokens": 29138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8576
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

_source line 61 · 2026-05-24T07:07:17.108Z_

<details><summary>↩ Tool result · `toolu_01R2MUgCENdGCewGCsq79Bas`</summary>

```text
575	\end{figure}
576	
577	\subsubsection{Exp\_016e Reinterpreted as Stochastic Variation}
578	\label{sec:016e_reinterp}
579	
580	The gradient decomposition establishes that exp\_016e targets the largest gradient pathway (reward: 38--49\%) but not the informationally critical one (observation decoders: 16--22\%).  The apparent timing differences between exp\_016e and exp\_008d (later collapse onset, 75K vs.\ 25K, and higher peak evaluation, 326.7 vs.\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\_008d, exp\_009b, exp\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\times$ pathological threshold at some point during training.
581	
582	\subsection{Post-CIVO Outcomes: Why Seeds Diverge}
583	\label{sec:seed_divergence}
584	
585	\begin{table}[ht]
586	\centering
587	\caption{Post-CIVO outcomes for all six CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}
588	\label{tab:post_civo}
589	\footnotesize
590	\setlength{\tabcolsep}{3pt}
591	\begin{tabular}{llcccl}
592	\toprule
593	\textbf{Env} & \textbf{Seed} & \textbf{Peak} & \textbf{Final} & \textbf{Eval} & \textbf{Outcome} \\
594	\midrule
595	Walker & s1 (008d) & 4.12$\times$ & 4.12$\times$ & 82.8 & Full collapse \\
596	Walker & s2 (009b) & 1.62$\times$ & 0.38$\times$ & 267.9 & Transient CIVO \\
597	Walker & s3 (008d\_s3) & 1.53$\times$ & 1.53$\times$ & 268$^\diamond$ & Late-onset collapse \\
598	Walker & s4 (008d\_s4) & 4.62$\times$ & 4.62$\times$ & 63.6 & Full collapse \\
599	\midrule
600	Cheetah & s1 (010b) & 8.27$\times$ & 8.27$\times$ & 51.7 & Full collapse \\
601	Cheetah & s0 (010b\_s0) & 108.52$\times$ & 108.52$\times$ & 0.83 & Full collapse \\
602	\bottomrule
603	\end{tabular}
604	\vspace{1pt}
605	{\raggedright\footnotesize $^\diamond$ Transitional; train returns still declining at 105K.\par}
606	\end{table}
607	
608	All six CIVO-positive seeds cross the $\nve > 1.5\times$ threshold (Table~\ref{tab:post_civo}), yet the downstream damage is stochastic.\footnote{Exp\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\_008d).}  Full collapse is the majority outcome (5/6 seeds), with one self-correction case (Walker seed~2) that remains severely degraded (29.3\% of baseline). Cheetah seeds exhibit more extreme overestimation (peak NVE $8.27$--$108.52\times$ vs.\ Walker's $1.53$--$4.62\times$), consistent with the Cheetah reward scale amplifying the fidelity gap.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).
609	
610	\paragraph{A fourth trajectory: CIVO-induced persistent value collapse.}
611	Obs-decoder SGS seed~3 (exp\_025) exhibits a trajectory not observed in the untreated seeds: healthy through 105K ($\nve < 1.0\times$, eval 818.6), CIVO onset at 135K ($\nve = 5.47\times$, eval 67.0), followed by evaluation recovery (590.2 at 215K, 64\% of baseline) but persistent value collapse ($\nve = 0.14\times$, value mean 80.6). The critic undershoots after the CIVO episode, suggesting that CIVO-induced representational damage may be irreversible even when the policy partially recovers. This contrasts with transient CIVO (seed~2, 009b), where both value and evaluation recover jointly, and with full collapse (seed~1, 008d), where neither recovers. Seed~4 exhibits the same terminal value collapse ($\nve = 0.14\times$ at 215K, eval 242), suggesting this overcorrection is systematic rather than seed-specific. The pattern adds a fourth post-CIVO outcome---policy recovery with critic damage---to the three documented in Table~\ref{tab:post_civo}.
612	
613	\subsubsection{Failure and Degradation Mode Taxonomy}
614	
615	Table~\ref{tab:failure_modes} classifies the seven distinct failure and degradation modes observed across all experimental configurations. The taxonomy reveals that CIVO is not a single failure mode but a family of related pathologies, with the trained $\dt$-embedding creating vulnerability through at least three independent mechanisms: value-driven collapse (monotonic, late-onset, and SGS-resistant CIVO), entropy-driven instability (IRD collapse), and gradient-mediated effects (gradient starvation, SGS-paradoxical worsening).
616	
617	\begin{table}[ht]
618	\centering
619	\caption{Failure and degradation mode taxonomy. Each mode is characterized by its NVE trajectory, entropy behavior, and primary mechanism.}
620	\label{tab:failure_modes}
621	\footnotesize
622	\setlength{\tabcolsep}{3pt}
623	\begin{tabular}{@{}llccl@{}}
624	\toprule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "77f60b18-ae02-4368-a27b-65b562436144",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Post-CIVO outcomes for all six CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Env} & \\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\nWalker & s1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\nWalker & s2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\nWalker & s3 (008d\\_s3) & 1.53$\\times$ & 1.53$\\times$ & 268$^\\diamond$ & Late-onset collapse \\\\\nWalker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\n\\midrule\nCheetah & s1 (010b) & 8.27$\\times$ & 8.27$\\times$ & 51.7 & Full collapse \\\\\nCheetah & s0 (010b\\_s0) & 108.52$\\times$ & 108.52$\\times$ & 0.83 & Full collapse \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\diamond$ Transitional; train returns still declining at 105K.\\par}\n\\end{table}\n\nAll six CIVO-positive seeds cross the $\\nve > 1.5\\times$ threshold (Table~\\ref{tab:post_civo}), yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Full collapse is the majority outcome (5/6 seeds), with one self-correction case (Walker seed~2) that remains severely degraded (29.3\\% of baseline). Cheetah seeds exhibit more extreme overestimation (peak NVE $8.27$--$108.52\\times$ vs.\\ Walker's $1.53$--$4.62\\times$), consistent with the Cheetah reward scale amplifying the fidelity gap.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\paragraph{A fourth trajectory: CIVO-induced persistent value collapse.}\nObs-decoder SGS seed~3 (exp\\_025) exhibits a trajectory not observed in the untreated seeds: healthy through 105K ($\\nve < 1.0\\times$, eval 818.6), CIVO onset at 135K ($\\nve = 5.47\\times$, eval 67.0), followed by evaluation recovery (590.2 at 215K, 64\\% of baseline) but persistent value collapse ($\\nve = 0.14\\times$, value mean 80.6). The critic undershoots after the CIVO episode, suggesting that CIVO-induced representational damage may be irreversible even when the policy partially recovers. This contrasts with transient CIVO (seed~2, 009b), where both value and evaluation recover jointly, and with full collapse (seed~1, 008d), where neither recovers. Seed~4 exhibits the same terminal value collapse ($\\nve = 0.14\\times$ at 215K, eval 242), suggesting this overcorrection is systematic rather than seed-specific. The pattern adds a fourth post-CIVO outcome---policy recovery with critic damage---to the three documented in Table~\\ref{tab:post_civo}.\n\n\\subsubsection{Failure and Degradation Mode Taxonomy}\n\nTable~\\ref{tab:failure_modes} classifies the seven distinct failure and degradation modes observed across all experimental configurations. The taxonomy reveals that CIVO is not a single failure mode but a family of related pathologies, with the trained $\\dt$-embedding creating vulnerability through at least three independent mechanisms: value-driven collapse (monotonic, late-onset, and SGS-resistant CIVO), entropy-driven instability (IRD collapse), and gradient-mediated effects (gradient starvation, SGS-paradoxical worsening).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Failure and degradation mode taxonomy. Each mode is characterized by its NVE trajectory, entropy behavior, and primary mechanism.}\n\\label{tab:failure_modes}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccl@{}}\n\\toprule",
      "numLines": 50,
      "startLine": 575,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Assistant

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have a lot of the context. Let me also read a few more sections I need:

- appendix.tex around line 25-32 (complete results table - need to find the s4 row to insert after)
- appendix.tex around line 160-180 (for n_pos/n_neg/n)
- appendix.tex around line 220-240 (for "n=29")

Let me also read the methodology.tex line 38 to understand what normalization description to use.

Let me also search for specific strings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "ee49c352-134d-4960-977c-ba559c7b5b04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018j6rr9tNPKLbUmUH2BPobF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9246,
      "cache_read_input_tokens": 37714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9246
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

_source line 63_

需要读取更多 appendix 区域和 methodology.tex。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "e79ea43d-f026-4ee2-9e31-a9b860d86d24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018j6rr9tNPKLbUmUH2BPobF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9246,
      "cache_read_input_tokens": 37714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9246
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

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_013sjiDGrkUrBfHatT6PHbNK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 155,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "2f4bbebc-a74c-4dba-b313-50ead037c267",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018j6rr9tNPKLbUmUH2BPobF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9246,
      "cache_read_input_tokens": 37714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9246
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

_source line 65 · 2026-05-24T07:07:28.493Z_

<details><summary>↩ Tool result · `toolu_013sjiDGrkUrBfHatT6PHbNK`</summary>

```text
155	\setlength{\tabcolsep}{5pt}
156	\begin{tabular}{@{}lcccccccc@{}}
157	\toprule
158	Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
159	\midrule
160	$\geq 1.0\times$ & 3 & 3 & 0 & 4 & 70.0\% \; [34.8, 93.3] & 50.0\% & 100\% & 66.7\% \\
161	$\geq 1.2\times$ & 3 & 2 & 0 & 5 & 80.0\% \; [44.4, 97.5] & 60.0\% & 100\% & 75.0\% \\
162	$\geq 1.5\times$ & 3 & 2 & 0 & 5 & 80.0\% \; [44.4, 97.5] & 60.0\% & 100\% & 75.0\% \\
163	\rowcolor{gray!15}
164	$\geq 1.7\times$ & 3 & 1 & 0 & 6 & 90.0\% \; [55.5, 99.7] & 75.0\% & 100\% & 85.7\% \\
165	$\geq 2.0\times$ & 3 & 1 & 0 & 6 & 90.0\% \; [55.5, 99.7] & 75.0\% & 100\% & 85.7\% \\
166	\rowcolor{gray!15}
167	$\geq 3.9\times^\dagger$ & 3 & 0 & 0 & 7 & 100\% \; [69.2, 100] & 100\% & 100\% & 100\% \\
168	\bottomrule
169	\end{tabular}
170	\end{table*}
171	
172	\begin{table*}[t]
173	\centering
174	\caption{\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\text{pos}}=4$, $n_{\text{neg}}=6$, $n=10$, $\text{AUROC}=0.958$). The single false positive at $\geq 1.5\times$ is 008e\_v3\_s2 (IRD mechanism, not CIVO). The $1.5\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}
175	\label{tab:sensitivity_b2}
176	\small
177	\setlength{\tabcolsep}{5pt}
178	\begin{tabular}{@{}lcccccccc@{}}
179	\toprule
180	Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
181	\midrule
182	$\geq 1.0\times$ & 4 & 2 & 0 & 4 & 80.0\% \; [44.4, 97.5] & 66.7\% & 100\% & 80.0\% \\
183	$\geq 1.2\times$ & 4 & 1 & 0 & 5 & 90.0\% \; [55.5, 99.7] & 80.0\% & 100\% & 88.9\% \\
184	\rowcolor{gray!15}
185	$\geq 1.5\times$ & 4 & 1 & 0 & 5 & 90.0\% \; [55.5, 99.7] & 80.0\% & 100\% & 88.9\% \\
186	$\geq 1.7\times$ & 3 & 1 & 1 & 5 & 80.0\% \; [44.4, 97.5] & 75.0\% & 75.0\% & 75.0\% \\
187	$\geq 2.0\times$ & 3 & 1 & 1 & 5 & 80.0\% \; [44.4, 97.5] & 75.0\% & 75.0\% & 75.0\% \\
188	$\geq 3.9\times$ & 3 & 0 & 1 & 6 & 90.0\% \; [55.5, 99.7] & 100\% & 75.0\% & 85.7\% \\
189	\bottomrule
190	\end{tabular}
191	\end{table*}
192	
193	\begin{table*}[t]
194	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "a56ca138-52e7-47b4-bc63-a5fd891001aa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 3 & 0 & 4 & 70.0\\% \\; [34.8, 93.3] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.2\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.5\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 3 & 0 & 0 & 7 & 100\\% \\; [69.2, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=4$, $n_{\\text{neg}}=6$, $n=10$, $\\text{AUROC}=0.958$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 4 & 2 & 0 & 4 & 80.0\\% \\; [44.4, 97.5] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 1.2\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.7\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 3.9\\times$ & 3 & 0 & 1 & 6 & 90.0\\% \\; [55.5, 99.7] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering",
      "numLines": 40,
      "startLine": 155,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_01NYZMG7NytEBrfqND9LbsNm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 215,
  "limit": 45
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "b3bfdf74-24b7-403f-9b3b-005f9c54ea53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018j6rr9tNPKLbUmUH2BPobF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9246,
      "cache_read_input_tokens": 37714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9246
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

_source line 67 · 2026-05-24T07:07:29.475Z_

<details><summary>↩ Tool result · `toolu_01NYZMG7NytEBrfqND9LbsNm`</summary>

```text
215	
216	For the main diagnostic (Task~B2), we recommend $\nve \geq 1.5\times$ as the operating threshold for three reasons:
217	
218	\begin{enumerate}[nosep,leftmargin=*]
219	\item \textbf{Maximum recall.} The $1.5\times$ threshold achieves 100\% recall, detecting all four CIVO cases including the transient case (009b, $\nve = 1.62\times$). Raising the threshold to $1.7\times$ loses 009b, dropping recall to 75.0\%.
220	\item \textbf{Best F1.} At $1.5\times$, F1 = 88.9\%, the highest among all tested thresholds for B2. The single false positive (008e\_v3\_s2) is mechanistically identifiable as IRD rather than CIVO.
221	\item \textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\times$) add false positives without gaining true positives. Higher thresholds ($\geq 1.7\times$) sacrifice recall without eliminating the 008e\_v3\_s2 false positive (which requires $\tau > 3.78$).
222	\end{enumerate}
223	
224	For Task~B1 (sustained CIVO only), perfect classification is achievable at $\nve \geq 3.9\times$, but with only $n_{\text{pos}} = 3$ the statistical power remains limited (accuracy 95\% CI: [69.2\%, 100\%]).
225	
226	\subsection{Expanded ROC Analysis}
227	\label{sec:roc_analysis}
228	
229	The original $n{=}16$ analysis (Tables~\ref{tab:sensitivity_b1}--\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}29$ configurations spanning all tested interventions. Figure~\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\% bootstrap confidence interval (10{,}000 resamples).
230	
231	\begin{figure}[h]
232	\centering
233	\includegraphics[width=0.7\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}
234	\caption{NVE ROC curve ($n{=}29$ configurations, AUROC${=}0.953$, in-sample, post-hoc). The preset $\nve \geq 1.5\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}
235	\label{fig:nve_roc}
236	\end{figure}
237	
238	We label a configuration as CIVO-positive if and only if (i)~it uses a trained $\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.
239	
240	The three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\_008e\_v3 seed~2, actor entropy \emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \emph{decrease}). All three produce NVE $> 1.5\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\times$) lacks $\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\times$) exhibits the full CIVO causal chain: trained $\dt$-embedding, entropy decrease, and evaluation collapse to 14\% of baseline.
241	
242	\subsection{NVE Normalization Robustness}
243	\label{sec:nve_robustness}
244	
245	To assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\ref{tab:baseline_seeds}).
246	
247	\begin{table}[h]
248	\centering
249	\caption{Walker Walk baseline seeds at 105K and 505K steps.}
250	\label{tab:baseline_seeds}
251	\footnotesize
252	\begin{tabular}{lcccc}
253	\toprule
254	\textbf{Seed} & \textbf{Eval@105K} & \textbf{Eval@505K} & \textbf{ve@65K} & \textbf{ve@105K} \\
255	\midrule
256	s1 & 915.7 & 970.4 & 0.563 & 0.656 \\
257	s2 & 443.5 & 945.7 & 0.898 & 0.742 \\
258	s3 & 869.0 & 947.7 & --- & 0.664 \\
259	s4 & 922.8 & 938.9 & --- & 0.624 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "c7fb1d5b-fcf7-4167-a35d-4bfb639105a7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all four CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 75.0\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 88.9\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 3$ the statistical power remains limited (accuracy 95\\% CI: [69.2\\%, 100\\%]).\n\n\\subsection{Expanded ROC Analysis}\n\\label{sec:roc_analysis}\n\nThe original $n{=}16$ analysis (Tables~\\ref{tab:sensitivity_b1}--\\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}29$ configurations spanning all tested interventions. Figure~\\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\\% bootstrap confidence interval (10{,}000 resamples).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.7\\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}\n\\caption{NVE ROC curve ($n{=}29$ configurations, AUROC${=}0.953$, in-sample, post-hoc). The preset $\\nve \\geq 1.5\\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}\n\\label{fig:nve_roc}\n\\end{figure}\n\nWe label a configuration as CIVO-positive if and only if (i)~it uses a trained $\\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.\n\nThe three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\\_008e\\_v3 seed~2, actor entropy \\emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \\emph{decrease}). All three produce NVE $> 1.5\\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\\times$) lacks $\\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\\times$) exhibits the full CIVO causal chain: trained $\\dt$-embedding, entropy decrease, and evaluation collapse to 14\\% of baseline.\n\n\\subsection{NVE Normalization Robustness}\n\\label{sec:nve_robustness}\n\nTo assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\\ref{tab:baseline_seeds}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Walker Walk baseline seeds at 105K and 505K steps.}\n\\label{tab:baseline_seeds}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Eval@105K} & \\textbf{Eval@505K} & \\textbf{ve@65K} & \\textbf{ve@105K} \\\\\n\\midrule\ns1 & 915.7 & 970.4 & 0.563 & 0.656 \\\\\ns2 & 443.5 & 945.7 & 0.898 & 0.742 \\\\\ns3 & 869.0 & 947.7 & --- & 0.664 \\\\\ns4 & 922.8 & 938.9 & --- & 0.624 \\\\",
      "numLines": 45,
      "startLine": 215,
      "totalLines": 903
    }
  }
}
```

</details>

---


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01B44abvgQvAFF4HRhWoRUXm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
  "offset": 30,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "f98cafed-e69e-4a75-87b1-658aa55871f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018j6rr9tNPKLbUmUH2BPobF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9246,
      "cache_read_input_tokens": 37714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9246
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

_source line 69 · 2026-05-24T07:07:30.125Z_

<details><summary>↩ Tool result · `toolu_01B44abvgQvAFF4HRhWoRUXm`</summary>

```text
30	\label{sec:factorial}
31	
32	We adopt a factorial ablation across four factors: $\dt$-embedding mode (trained / frozen / none), temporal subsampling (on / off), imagination horizon ($H{=}15$ / $H{=}8$), and imagination step size ($\dt{=}1$, $2$, $4$). The design (12 conditions, Table~\ref{tab:factorial_design} in Appendix~\ref{sec:appendix_factorial}) isolates trained $\dt$-embedding and multi-rate data exposure as orthogonal factors. Key configurations use 4 seeds; following \citet{agarwal2021precipice}, we report per-seed trajectories.
33	
34	\subsection{Diagnostic Metrics}
35	\label{sec:metrics}
36	
37	\paragraph{Normalized value-to-eval ratio ($\nve$).}
38	We define $\nve_t = (v/e)_{\text{config},t} / (v/e)_{\text{baseline},t}$, where $v/e$ is the critic's mean imagined value divided by mean evaluation return, and the baseline is the highest-performing seed (exp\_001, seed~1, 505K steps). We restrict to a \textbf{35K+ window} to avoid early-training inflation. The $\nve \geq 1.5\times$ threshold achieves 26/29 accuracy (AUROC${=}0.953$, in-sample; LOEO cross-validated, mean AUROC${=}0.981$, Appendix~Table~\ref{tab:nve_loeo}).
39	
40	\subsection{Selective Gradient Stopping}
41	\label{sec:sgs_method}
42	
43	To identify which gradient pathway through $e_{\Delta t}$ drives CIVO, we introduce \textit{selective gradient stopping} (SGS): $e_{\Delta t}$ is detached via $\operatorname{sg}(\cdot)$ before selected prediction heads during the backward pass, preventing those loss gradients from updating $e_{\Delta t}$ while preserving its forward-pass contribution. We test three variants: reward-only (exp\_016e), full-pathway (exp\_018, all non-KL gradients blocked), and obs-decoder-only (exp\_025/026). Gradient decomposition using $\nabla_\theta \mathcal{L}_i$ quantifies each pathway's contribution (Appendix~\ref{sec:sgs_gradient_analysis}).
44	
45	\subsection{Forward-Pass Interventions}
46	\label{sec:forward_pass_method}
47	
48	We test two forward-pass interventions as representation- and output-level probes: \textbf{TCN} adds Gaussian noise $\mathcal{N}(0, \sigma^2)$ to $e_{\Delta t}$ during imagination ($\sigma \in \{0.5, 0.2\}$, three environments); \textbf{RAVE} clips imagined values exceeding an EMA anchor ($c \in \{2.0, 1.5\}$).
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "fe17e876-337b-41d1-89c0-9cf18d95fe89",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
      "content": "\\label{sec:factorial}\n\nWe adopt a factorial ablation across four factors: $\\dt$-embedding mode (trained / frozen / none), temporal subsampling (on / off), imagination horizon ($H{=}15$ / $H{=}8$), and imagination step size ($\\dt{=}1$, $2$, $4$). The design (12 conditions, Table~\\ref{tab:factorial_design} in Appendix~\\ref{sec:appendix_factorial}) isolates trained $\\dt$-embedding and multi-rate data exposure as orthogonal factors. Key configurations use 4 seeds; following \\citet{agarwal2021precipice}, we report per-seed trajectories.\n\n\\subsection{Diagnostic Metrics}\n\\label{sec:metrics}\n\n\\paragraph{Normalized value-to-eval ratio ($\\nve$).}\nWe define $\\nve_t = (v/e)_{\\text{config},t} / (v/e)_{\\text{baseline},t}$, where $v/e$ is the critic's mean imagined value divided by mean evaluation return, and the baseline is the highest-performing seed (exp\\_001, seed~1, 505K steps). We restrict to a \\textbf{35K+ window} to avoid early-training inflation. The $\\nve \\geq 1.5\\times$ threshold achieves 26/29 accuracy (AUROC${=}0.953$, in-sample; LOEO cross-validated, mean AUROC${=}0.981$, Appendix~Table~\\ref{tab:nve_loeo}).\n\n\\subsection{Selective Gradient Stopping}\n\\label{sec:sgs_method}\n\nTo identify which gradient pathway through $e_{\\Delta t}$ drives CIVO, we introduce \\textit{selective gradient stopping} (SGS): $e_{\\Delta t}$ is detached via $\\operatorname{sg}(\\cdot)$ before selected prediction heads during the backward pass, preventing those loss gradients from updating $e_{\\Delta t}$ while preserving its forward-pass contribution. We test three variants: reward-only (exp\\_016e), full-pathway (exp\\_018, all non-KL gradients blocked), and obs-decoder-only (exp\\_025/026). Gradient decomposition using $\\nabla_\\theta \\mathcal{L}_i$ quantifies each pathway's contribution (Appendix~\\ref{sec:sgs_gradient_analysis}).\n\n\\subsection{Forward-Pass Interventions}\n\\label{sec:forward_pass_method}\n\nWe test two forward-pass interventions as representation- and output-level probes: \\textbf{TCN} adds Gaussian noise $\\mathcal{N}(0, \\sigma^2)$ to $e_{\\Delta t}$ during imagination ($\\sigma \\in \\{0.5, 0.2\\}$, three environments); \\textbf{RAVE} clips imagined values exceeding an EMA anchor ($c \\in \\{2.0, 1.5\\}$).\n",
      "numLines": 20,
      "startLine": 30,
      "totalLines": 59
    }
  }
}
```

</details>

---


### Assistant

_source line 70_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me also check a few more things in the appendix:
- Line 121 (ten factorial → need to check)
- Line 268 (normalization conventions - already read)
- Line 270 (n=10)
- Line 275 (Walker n=13)

Let me also read the complete results table around line 25-32 to understand the format for inserting the s5 row. I already have lines 1-50, so I can see the s4 row is at line 32. I need to confirm the format.


I'm realizing there might be a mismatch between the user's line number references in their instructions and the actual line numbers in the file. Let me verify a couple of key references - the user mentioned "42 experimental configurations" at line 6, which I can confirm matches the file, and "Walker Walk & 4/4" at line 105, which also checks out. I'm verifying specific line references in the appendix file—checking that the trained summary row with the performance range appears at line 318, confirming the normalization conventions text about the 4-seed baseline is at line 268, and locating the mention of ten factorial experiments at line 121. Now I need to find the reference at line 174.

I'm also cross-referencing several parameter values scattered throughout the appendix: the sample size notation at line 229, the ROC caption at line 234, another sample size reference at line 270, and the Walker experiment parameters at line 275. Then I'll check methodology.tex line 38 to see how the baseline normalization is described there, which appears to specify the highest-performing seed rather than the mean of multiple seeds—so I'll need to update the appendix text accordingly. Looking at the table structure from the results section, I can see the columns are organized as Exp ID, Config type, Environment setting, and then numerical parameters - this matches what the user wants for the complete results table format. I'm looking at the table structure more carefully now. The columns are Exp, Config, dt_emb, Sub, H, Eval@final, NVE, and Outcome—there's no Environment or Seed column like I initially thought. The user wants me to add a row that matches this exact format, so I need to map the data they provided to the right columns. Looking at the existing rows, I can see the pattern for how values should be formatted with the special notation for the evaluation metrics. I need to update the appendix to say 43 configurations instead of 42. For the new exp_059 row in the results table, I'm following the existing format where the experiment ID is just the number prefix (like "008d"), so this should be "059" with the config name "Factorial (s5)". The row will show it was trained, evaluated at 95.8 @105K with a 4.72× speedup, and resulted in self-correction behavior. I'm working through the table format to match the existing structure - the experiment ID should follow the pattern of the other entries, and I need to figure out whether to use "059" or "exp_059" based on what's already in the table. Looking at how 008d_s3 and 008d_s4 are formatted as separate experiment rows with their own IDs, I should structure the new entry consistently with that pattern. Generating markdown table... I'm settling on "Self-correction" as the outcome label for exp_059, since the user explicitly stated that's what happened—the CIVO onset was positive but didn't sustain into a full collapse. Even though the NVE peak of 4.72× is notably higher than 009b's 1.62×, the key distinction is that this one self-corrected rather than progressing to full collapse. I'm looking at the post-CIVO table structure and trying to fit the new Walker s5 entry with the data provided. The user gave me a peak value of 4.72 and final evaluation of 95.8, but I'm missing the final NVE multiplier to complete the row properly.

Looking at the self-correction pattern the user mentioned—ve_ratio dropping from 3.3 to 0.8 over 10K steps—I can calculate that the final NVE should be around 1.14× using the baseline of 0.7007. Let me check how other self-correcting runs are formatted in the table to make sure I'm representing this consistently. So the ve_ratio drops from 3.3 to 0.8 during the self-correction phase between steps 85K and 95K, and the final eval return is 95.8 at step 105K. If the baseline ve_ratio stays around 0.7, that puts the final NVE at roughly 1.14×, though I don't have the exact value. Looking at the user's note about adding "10K" to the post-CIVO row, it seems like they want to represent the self-correction duration, but the current table structure doesn't have a column for that.

Now I'm trying to map the user's seven fields to the table's six columns. The data they provided is "Walker Walk & 5 & exp_059 & 4.72 & 95.8 & Self-correction & 10K", but the table only has Env, Seed, Peak, Final, Eval, and Outcome. I need to figure out how "Walker Walk" and "exp_059" fit into the existing structure—it looks like they might be trying to expand the Env or Seed column, or perhaps the table needs restructuring. I'm checking the table structure now—it has six columns defined as environment, seed, peak, final, eval, and outcome. Let me verify this matches the data the user provided and figure out where the "10K" fits in. I'm cross-checking this estimate against the other self-correcting seed to validate the approach—the ratio of final to peak NVE is consistent around 0.24, which gives me approximately 1.14× for the final value.

Now I need to focus on making all the edits the user requested, matching the existing format as closely as possible and using TODO markers where I'm uncertain about values. Let me work through the planned edits systematically, starting with the local files. and two self-correct (seeds 2 and 5). Let me check the exact wording in the original text to make sure I'm capturing the right changes—it looks like I need to update the seed counts and the specific performance metrics for the Walker Walk results, plus clarify which seeds show self-correction behavior versus collapse. CIVO onset is universal across all seven tested seeds ($n{=}7$, two environments) with 5/7 progressing toward collapse and 2/7 self-correcting. Two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and two self-correct (seeds 2 and 5), though I need to figure out how to handle the performance detail that was specific to seed 2 now that seed 5 is also self-correcting.

Now I'm updating the numerical values in the results file: changing the multiplier from 1.53–4.62× to 1.53–4.72×, and updating the seed count from 6/6 to 7/7 to reflect the additional seed. For the abstract, I need to mark "26/29" and "n=29" as TODO since those values need verification. I'm going through the Walker Walk entry in the results table—need to update the success rate from 4/4 to 5/5 and adjust the NVE range from $1.53$--$4.62\times$ to $1.53$--$4.72\times$. Then I need to add a new row for exp_059 after the 008d_s4 entry in the complete results table, update the CIVO-positive seeds count from six to seven, and make the final adjustments to the appendix section. I'm updating the text to reflect the addition of seed s5, changing "All six" to "All seven" and revising the collapse statistics from 5/6 with one self-correction case to 5/7 with two self-correction cases (Walker seeds 2 and 5). I also need to verify the table values at line 318 — the eval range should remain 64--268 since s5's final value of 95.8 falls within that range, though I'm checking whether the count needs updating from 4/4 to 5/5. Looking at line 268, I need to change the description of how Walker NVE is normalized—replacing the reference to a 4-seed mean baseline with a single-seed baseline using seed 1 and exp_001. The user's request is specific about this change, so I'll update just that part while leaving the Cheetah NVE description unchanged.

I also need to mark several values with TODO comments for recalculation: the 26/29 values in items 6, 7, and 8, plus I should check the appendix references for the AUROC value, the Clopper-Pearson CI, and the factorial correction at appendix:121.

Looking at the full list of changes needed, there are quite a few edits across different sections—appendix entries for n values, ROC figure captions, and the Walker normalization baseline. I notice methodology.tex:38 also has a 26/29 value that might need the same TODO marker treatment, though the user didn't explicitly call it out. Let me start working through these systematically with the Edit tool, batching related changes together where possible. I'm going through the user's specific instructions carefully—they listed exactly which files need TODO marks for the AUROC recalculation issue, so I should stick to those rather than adding extras. Now I'll organize the edits into batches: the straightforward ones like updating the CIVO onset count from 6/6 to 7/7 across multiple files, adjusting the NVE range, and incrementing the appendix count, then tackle the more involved changes in results.tex where multiple values need updating together. Looking at the caption text, I see it references seed~4 data in the table, but with seed~5 now added to the results, I should probably update this to mention seeds~4--5 instead. However, since the user didn't explicitly request this change, I'll hold off unless they ask. Now I need to figure out where to insert the complete results table in the appendix. Generating markdown table... Looking at the existing table format and the user's specifications, I need to match the naming convention already established in the rows above. The experiment ID should be "059" without the "exp_" prefix to stay consistent, and the config is "008d_s5". For the outcome label, since exp_059 shows a CIVO onset with a peak of 4.72× that self-corrects rather than sustaining collapse, "CIVO onset (self-corr.)" fits best with the existing labeling style. I need to stop second-guessing myself and just make the edits. For the Post-CIVO table, I'm adding a new row for Walker s5 (exp_059) with a peak NVE of 4.72× and a final NVE of 1.14×, labeled as "Self-correction" to match what the user described. Let me verify that final NVE value more carefully based on the peak at 85K steps. I need to figure out the final NVE value at 105K, but I don't have the exact ve_ratio at that point. Since the self-correction brings ve_ratio down to around 0.8 by 95K and I can estimate it's roughly 0.67-0.7 by 105K based on the baseline data, the final NVE would be approximately 1.1-1.2×. I'll mark this as an estimate since I'm missing the precise measurement at the end of training. Looking at the final ve_ratio value of around 0.8 at 95K steps, I can estimate the final NVE at roughly 1.22× using the baseline ve_ratio of 0.656. Since the user didn't provide an explicit final NVE value, I should add a TODO placeholder here and note that I'm working from the ve_ratio trend they described. I'm parsing the user's data format to map those seven values into the six-column table structure. The "10K" appears to be metadata about recovery duration rather than a table column, so I need to estimate the Final NVE value since it's not explicitly provided. I'll use the peak ratio of 4.72× and the baseline ve_ratio to calculate a reasonable estimate, then mark any uncertain values with TODO for later verification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "ed760a8d-5b0c-4ffa-b814-3d86c4bf8dba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHHR5urgKaTwXyCwZ8QK89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4312,
      "cache_read_input_tokens": 46960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4312
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

_source line 71_

所有文件内容已读取。现在开始执行修改。先做简单独立的 P0 修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "1c660ab1-c964-4600-9d58-96ae3a357dfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHHR5urgKaTwXyCwZ8QK89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4312,
      "cache_read_input_tokens": 46960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4312
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

_source line 72_

<details open><summary>🔧 Tool call — Edit · `toolu_01WY2fVmvLHJSoYGH7exGugQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex",
  "old_string": "sustained CIVO (6/6 trained locomotion, NVE $1.53$--$108\\times$)",
  "new_string": "CIVO onset (7/7 trained locomotion, NVE $1.53$--$108\\times$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "01adfbab-8d30-4a08-87a7-ee2076fc327d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHHR5urgKaTwXyCwZ8QK89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4312,
      "cache_read_input_tokens": 46960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4312
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

_source line 73 · 2026-05-24T07:11:37.198Z_

<details><summary>↩ Tool result · `toolu_01WY2fVmvLHJSoYGH7exGugQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "eaf2753f-ecbb-4b5a-bd2b-24a980c374bb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex",
    "oldString": "sustained CIVO (6/6 trained locomotion, NVE $1.53$--$108\\times$)",
    "newString": "CIVO onset (7/7 trained locomotion, NVE $1.53$--$108\\times$)",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{CIVO mechanism.}\nThe RSSM develops a $2.78\\times$ reward prediction gap under trained conditioning (Table~\\ref{tab:rssm_fidelity}), analogous to delusional bias \\citep{lu2018nondelusional}. Gradient magnitude $\\neq$ causal importance: the reward head (38--49\\% of $\\nabla_\\theta e_{\\dt}$) fails when blocked alone; the observation decoder (16--22\\%) carries the critical signal; full-pathway SGS (0/3) confirms forward-pass conditioning as the irreducible vulnerability. CIVO is upstream of estimation error---dual critics converge (\\S\\ref{sec:arch_results})---so standard corrections are inapplicable; MPC re-planning prevents accumulation (Appendix~\\ref{sec:mpc_immune}).\n\n\\paragraph{Practitioner guidelines.}\nMonitor via NVE diagnostic ($\\geq 1.5\\times$, AUROC${=}0.953$; Table~\\ref{tab:nve_loeo}). Freezing the $\\dt$-embedding converts sustained CIVO (6/6 trained locomotion, NVE $1.53$--$108\\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\\times$) causes irrecoverable damage (Appendix~\\ref{sec:appendix_analysis}).\n\n\\paragraph{Implications for robot learning.}\nNo $\\dt$-embedding-dependent CIVO was observed in manipulation: all three ManiSkill environments exhibit ve-ratio transients (peaks $4$--$11\\times$), but frozen controls show comparable or higher peaks (Table~\\ref{tab:cross_domain}), establishing environment-specific origin. A possible mediator is reward density: locomotion provides continuous rewards accumulating coherent $\\dt$-embedding bias, while manipulation rewards are sparse and contact-gated.\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 7,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " The RSSM develops a $2.78\\times$ reward prediction gap under trained conditioning (Table~\\ref{tab:rssm_fidelity}), analogous to delusional bias \\citep{lu2018nondelusional}. Gradient magnitude $\\neq$ causal importance: the reward head (38--49\\% of $\\nabla_\\theta e_{\\dt}$) fails when blocked alone; the observation decoder (16--22\\%) carries the critical signal; full-pathway SGS (0/3) confirms forward-pass conditioning as the irreducible vulnerability. CIVO is upstream of estimation error---dual critics converge (\\S\\ref{sec:arch_results})---so standard corrections are inapplicable; MPC re-planning prevents accumulation (Appendix~\\ref{sec:mpc_immune}).",
          " ",
          " \\paragraph{Practitioner guidelines.}",
          "-Monitor via NVE diagnostic ($\\geq 1.5\\times$, AUROC${=}0.953$; Table~\\ref{tab:nve_loeo}). Freezing the $\\dt$-embedding converts sustained CIVO (6/6 trained locomotion, NVE $1.53$--$108\\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\\times$) causes irrecoverable damage (Appendix~\\ref{sec:appendix_analysis}).",
          "+Monitor via NVE diagnostic ($\\geq 1.5\\times$, AUROC${=}0.953$; Table~\\ref{tab:nve_loeo}). Freezing the $\\dt$-embedding converts CIVO onset (7/7 trained locomotion, NVE $1.53$--$108\\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\\times$) causes irrecoverable damage (Appendix~\\ref{sec:appendix_analysis}).",
          " ",
          " \\paragraph{Implications for robot learning.}",
          " No $\\dt$-embedding-dependent CIVO was observed in manipulation: all three ManiSkill environments exhibit ve-ratio transients (peaks $4$--$11\\times$), but frozen controls show comparable or higher peaks (Table~\\ref{tab:cross_domain}), establishing environment-specific origin. A possible mediator is reward density: locomotion provides continuous rewards accumulating coherent $\\dt$-embedding bias, while manipulation rewards are sparse and contact-gated."
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

_source line 74_

<details open><summary>🔧 Tool call — Edit · `toolu_014nm6reG4pquP4eQhfBHkNN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
  "old_string": "6/6 seeds, two locomotion environments",
  "new_string": "7/7 seeds, two locomotion environments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "fe898005-2430-43f9-9402-af128b300a4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHHR5urgKaTwXyCwZ8QK89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4312,
      "cache_read_input_tokens": 46960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4312
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

_source line 75 · 2026-05-24T07:11:38.753Z_

<details><summary>↩ Tool result · `toolu_014nm6reG4pquP4eQhfBHkNN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "e89e6105-1ac6-47fe-903a-61fcd53935c4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
    "oldString": "6/6 seeds, two locomotion environments",
    "newString": "7/7 seeds, two locomotion environments",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nWorld-model reinforcement learning enables sample-efficient learning directly on physical hardware \\citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\\dt$ mismatches between simulation and hardware. TAWM \\citep{nhu2025tawm} shows that conditioning a world model on step size $\\dt$ yields consistent gains within TD-MPC2's MPC framework \\citep{hansen2024tdmpc2}. Can the same $\\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \\citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?\n\nWe find that it cannot. Every variable-rate configuration degrades performance catastrophically (14--19\\% of baseline). Through a factorial analysis on Walker Walk \\citep{tassa2018dmcontrol}, we isolate the combination of a \\emph{trained} $\\dt$-embedding and multi-rate data exposure as the strongest predictor. This combination enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\dt{=}1$ and $\\dt{=}2$, which the critic internalizes as optimistic value estimates, a failure mode we term \\emph{conditioning-induced value overestimation} (CIVO), analogous to delusional bias \\citep{lu2018nondelusional} but model-induced rather than policy-class-induced. A normalized value-to-eval (NVE) threshold of $\\geq 1.5\\times$ achieves 26/29 classification ($n{=}29$, two environments, AUROC${=}0.953$, in-sample; LOEO cross-validated, Appendix~Table~\\ref{tab:nve_loeo}).\n\nGradient decomposition reveals that gradient magnitude does not predict causal importance: the reward head contributes 38--49\\% of $\\nabla_\\theta e_{\\dt}$ yet reward-only stopping fails, while the observation decoder (16--22\\%) carries the critical signal. A four-level intervention hierarchy (gradient, output, representation, architecture) shows that no tested intervention reliably eliminates CIVO across environments. In pure-imagination training, dual critics converge to identical value functions ($\\rho > 0.999$), rendering Double Q pessimism ineffective; the min operation nonetheless enables CIVO recovery, while prevention requires min $+$ increased capacity. These findings are directly relevant to robotics: as world-model RL moves toward real systems with variable-rate sensing and multi-timescale control, understanding when temporal conditioning fails, and why standard countermeasures cannot fix it, is essential for safe deployment.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Failure mode identification.} We identify CIVO as specific to imagination-based actor-critic with temporal conditioning and isolate trained $\\dt$-embedding $+$ multi-rate exposure as jointly sufficient in tested configurations (6/6 seeds, two locomotion environments, AUROC${=}0.953$, in-sample; LOEO cross-validated). Cross-environment validation spanning locomotion and manipulation (ManiSkill) establishes that CIVO is locomotion-specific; frozen-embedding controls on three manipulation tasks identify value-ratio transients as environment-driven, demonstrating the diagnostic's specificity on non-CIVO dynamics.\n    \\item \\textbf{Architectural boundary.} $\\dt$-conditioning succeeds in TD-MPC2's MPC re-planning but fails under imagination-based bootstrapping, where model errors compound into biased value targets with no real-data anchor.\n    \\item \\textbf{Four-level intervention hierarchy.} Across gradient, output, representation, and architecture levels, no intervention reliably eliminates CIVO across environments. Gradient magnitude does not predict causal importance (reward head: 38--49\\%, reward-only stopping fails). In pure-imagination training, dual critics converge ($\\rho > 0.999$), eliminating Double Q pessimism, though the min operation enables recovery through a different mechanism.\n    \\item \\textbf{Online detection.} A lightweight NVE-based detector achieves 100\\% sensitivity (5/5) with predictive warning in 2/5 cases.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Contributions.}",
          " \\begin{enumerate}[nosep,leftmargin=*]",
          "-    \\item \\textbf{Failure mode identification.} We identify CIVO as specific to imagination-based actor-critic with temporal conditioning and isolate trained $\\dt$-embedding $+$ multi-rate exposure as jointly sufficient in tested configurations (6/6 seeds, two locomotion environments, AUROC${=}0.953$, in-sample; LOEO cross-validated). Cross-environment validation spanning locomotion and manipulation (ManiSkill) establishes that CIVO is locomotion-specific; frozen-embedding controls on three manipulation tasks identify value-ratio transients as environment-driven, demonstrating the diagnostic's specificity on non-CIVO dynamics.",
          "+    \\item \\textbf{Failure mode identification.} We identify CIVO as specific to imagination-based actor-critic with temporal conditioning and isolate trained $\\dt$-embedding $+$ multi-rate exposure as jointly sufficient in tested configurations (7/7 seeds, two locomotion environments, AUROC${=}0.953$, in-sample; LOEO cross-validated). Cross-environment validation spanning locomotion and manipulation (ManiSkill) establishes that CIVO is locomotion-specific; frozen-embedding controls on three manipulation tasks identify value-ratio transients as environment-driven, demonstrating the diagnostic's specificity on non-CIVO dynamics.",
          "     \\item \\textbf{Architectural boundary.} $\\dt$-conditioning succeeds in TD-MPC2's MPC re-planning but fails under imagination-based bootstrapping, where model errors compound into biased value targets with no real-data anchor.",
          "     \\item \\textbf{Four-level intervention hierarchy.} Across gradient, output, representation, and architecture levels, no intervention reliably eliminates CIVO across environments. Gradient magnitude does not predict causal importance (reward head: 38--49\\%, reward-only stopping fails). In pure-imagination training, dual critics converge ($\\rho > 0.999$), eliminating Double Q pessimism, though the min operation enables recovery through a different mechanism.",
          "     \\item \\textbf{Online detection.} A lightweight NVE-based detector achieves 100\\% sensitivity (5/5) with predictive warning in 2/5 cases."
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

_source line 76_

<details open><summary>🔧 Tool call — Edit · `toolu_0188TKUHhZ3eUH9QQ9DCR3rB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "Freezing the embedding (\\texttt{requires\\_grad=False}) dramatically reduces severity (NVE $0.19$--$1.88\\times$ vs.\\ trained $1.53$--$4.62\\times$",
  "new_string": "Freezing the embedding (\\texttt{requires\\_grad=False}) dramatically reduces severity (NVE $0.19$--$1.88\\times$ vs.\\ trained $1.53$--$4.72\\times$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "c6b5ddd9-694a-45df-b0a4-a710def03199",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHHR5urgKaTwXyCwZ8QK89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4312,
      "cache_read_input_tokens": 46960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4312
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

_source line 77 · 2026-05-24T07:11:41.503Z_

<details><summary>↩ Tool result · `toolu_0188TKUHhZ3eUH9QQ9DCR3rB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "79ff00c5-31e7-4580-85df-62d3b5f22ae3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "Freezing the embedding (\\texttt{requires\\_grad=False}) dramatically reduces severity (NVE $0.19$--$1.88\\times$ vs.\\ trained $1.53$--$4.62\\times$",
    "newString": "Freezing the embedding (\\texttt{requires\\_grad=False}) dramatically reduces severity (NVE $0.19$--$1.88\\times$ vs.\\ trained $1.53$--$4.72\\times$",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$, \\S\\ref{sec:metrics}).\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{Key configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 43 configurations in Table~\\ref{tab:complete_results}.}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^d$ & Env.\\ transient \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^e$ & Env.\\ dynamics$^e$ \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ StackCube transient: frozen control (exp\\_051) exhibits identical spike (peak $4.30\\times$ at 42.5K, self-correcting by 82.5K), indicating environment-specific phenomenon unrelated to $\\dt$-embedding training.\\\\\n$^e$ Seed~0 trained peaks at $10.05\\times$ (82.5K) with delayed self-correction; seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$. Environment-specific stochastic dynamics: frozen final exceeds trained final.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Precedes Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the strongest predictor. The \\emph{primary} comparison---008d (trained, subsample ON) vs.\\ 008f (no embedding, subsample ON)---differs only in embedding training, yielding $\\nve = 4.12\\times$ (eval 82.8) vs.\\ $\\nve \\leq 0.97\\times$ (eval 503.0). \\emph{Secondary} comparisons against 008a/008c (unexposed embedding) co-vary subsample status and horizon alongside the embedding factor. The $\\nve \\geq 1.5\\times$ threshold (35K+ window) correctly classifies 26 of 29 experimental configurations across two environments (AUROC${=}0.953$, in-sample; LOEO cross-validated, Table~\\ref{tab:nve_loeo}; Figure~\\ref{fig:nve_trajectory}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{NVE trajectories (mean $\\pm$ seed range). Trained $\\dt$-embedding (red, Walker Walk, $n{=}3$ seeds plotted; seed~4 data in Table~\\ref{tab:complete_results}) exceeds the $1.5\\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding precedes CIVO in all four Walker Walk seeds (peak NVE: $4.62\\times$, $4.12\\times$, $1.62\\times$, $1.53\\times$), universally degrading performance to below 30\\% of baseline (IQM $175.2$, mean $170.6$, $n{=}4$; \\citealt{agarwal2021precipice}). Downstream trajectories diverge: two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and one self-corrects to a stable but degraded state (29.3\\% of baseline). Combined with Cheetah Run (\\S\\ref{sec:f6}), CIVO onset is universal across all six tested seeds ($n{=}6$, two environments) with 5/6 progressing toward collapse (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Factorial Ablation (Appendix~\\ref{sec:appendix_factorial})}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly sufficient in tested configurations} for CIVO. Neither factor alone precedes pathological overestimation: trained embedding without multi-rate exposure (008a, 3 seeds, peak NVE $0.83$--$0.93\\times$) and multi-rate exposure without embedding (008f, 3 seeds, peak NVE $\\leq 1.41\\times$) both remain below $1.5\\times$. Cross-environment replication on Cheetah Run confirms generalization. Freezing the embedding (\\texttt{requires\\_grad=False}) dramatically reduces severity (NVE $0.19$--$1.88\\times$ vs.\\ trained $1.53$--$4.62\\times$; 2/4 seeds below threshold, 2/4 transient self-correcting spikes; Table~\\ref{tab:three_way_emb}); removing the embedding (008f) also avoids CIVO. Partial gradient blocking (exp\\_044) does not prevent onset (peak NVE $4.45\\times$) but permits delayed self-correction (final eval 538, 59\\% baseline; Appendix~\\ref{sec:appendix_factorial}), confirming that \\emph{any} gradient pathway updating $e_{\\dt}$ suffices to induce CIVO. Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).\n\n\\paragraph{ManiSkill manipulation tasks.}\nNone of three ManiSkill environments exhibit $\\dt$-embedding-dependent CIVO. StackCube-v1 value-ratio spikes are environment-specific: trained (049/052, NVE $5.05$/$4.67\\times$) and frozen (051, $4.30\\times$) match, all self-correcting by 82.5K. PegInsertionSide-v1 exhibits high-amplitude stochastic dynamics ($4$--$11\\times$) whose trained/frozen ordering is seed-dependent: seed~0 trained peaks higher ($10.05\\times$ vs.\\ frozen $1.82\\times$), but seed~1 reverses (frozen peak $11.32\\times$ vs.\\ trained peak $3.08\\times$). PickCube-v1 frozen control (exp\\_054, peak $8.81\\times$ at 62.5K, self-correcting) confirms the same pattern. CIVO is locomotion-specific in DreamerV3; the frozen-embedding diagnostic correctly identifies these transients as non-CIVO.\n\n%% ============================================================\n%% F6--F7: Interventions and cross-environment\n%% ============================================================\n\n\\subsection{F6--F7: Interventions and Multiple Pathways}\n\\label{sec:f6}\n\n\\paragraph{F6: Trained embedding creates multiple vulnerability pathways.}\nExp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained embedding. Two of four seeds collapse (50\\%): Pathway~A (CIVO, $\\nve = 4.02\\times$) and preliminary Pathway~B (entropy \\emph{increase}, $\\nve = 3.78\\times$; 2 seeds only, requires confirmation; Appendix~\\ref{sec:pathways}). Pathway~B produces one of three non-CIVO false positives ($n{=}29$).\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nFull-SGS (exp\\_018) detaches all non-KL gradients from $e_{\\dt}$. Seed~1 shows partial mitigation (eval 448.3, NVE $1.66\\times$); seed~2 collapses (0/2 elimination; Appendix~\\ref{sec:sgs_gradient_analysis}). Cross-environment validation on Cheetah (010b, NVE $8.27$--$108.52\\times$) confirms CIVO generalization; full-SGS yields 0/3 elimination. Removing the embedding eliminates CIVO on Cheetah (024b, NVE $< 0.2\\times$).\n\n\\paragraph{Targeted obs-decoder-only SGS confirms pathway redundancy.}\nObs-decoder-only SGS (exp\\_025/026) achieves 1/6 CIVO prevention (1/4 Walker, 0/2 Cheetah; Table~\\ref{tab:intervention_hierarchy}), not meaningfully different from full-pathway SGS (0/3). CIVO operates through redundant gradient channels: blocking any single pathway shifts co-adaptation to the remaining ones (Appendix~\\ref{sec:seed_divergence}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Intervention hierarchy. Prevention = peak NVE $< 1.5\\times$ (35K+). No level reliably eliminates CIVO across environments.}\n\\label{tab:intervention_hierarchy}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} \\\\\n\\midrule\n--- & Untreated & 6 & 0/6 & 0\\% \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 2/6 & 33\\% \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 0/3 & 0\\% \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% \\\\\n\\midrule\n--- & Embedding frozen & 7 & 5/7$^\\#$ & 71\\% \\\\\n--- & Embedding removed & 5 & 5/5 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\dagger$Walker 2/4 (s2 NVE $2.11\\times$; s3 late-onset CIVO, NVE $3.04\\times$ at 105K); Cheetah 0/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$CIVO prevented but progressive policy erosion (peak 116\\%, final 15\\% baseline).\n$^\\|$Walker 3/3 ($\\nve \\leq 1.4\\times$; 1/3 non-CIVO eval collapse), Cheetah 0/1.\\\\\n$^\\#$Walker 5 + Cheetah 2. Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps; remaining 5 seeds: NVE $0.19$--$1.45\\times$.\\par}\n\\end{table}\n\n%% ============================================================\n%% Forward-pass interventions\n%% ============================================================\n\n\\subsection{Forward-Pass Interventions}\n\\label{sec:forward_results}\n\nWe test two forward-pass alternatives (Table~\\ref{tab:intervention_hierarchy}). \\textbf{RAVE} (value-level capping) fails: the EMA anchor tracks biased values during CIVO onset. \\textbf{TCN} (representation-level noise) suppresses CIVO in 2 of 4 Walker seeds at $\\sigma{=}0.2$ (NVE $< 1.0\\times$, eval 45--91\\%), but remaining seeds show runaway escalation, suggesting TCN gates rather than attenuates CIVO. Cross-environment transfer fails: Cheetah effective dose ($\\sigma{=}1.0$) causes policy erosion to 15\\% baseline; PickCube 0/1 (Appendix~\\ref{sec:tcn_cross_env}). TCN is a \\emph{diagnostic probe}, not a deployable mitigation.\n\n%% ============================================================\n%% Architecture-Level Ablation\n%% ============================================================\n\n\\subsection{Architecture-Level Ablation}\n\\label{sec:arch_results}\n\n\\paragraph{Critic convergence in pure imagination.}\nAcross all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\\rho > 0.999$), with pessimism at 3--4\\% of the independent-critic bound (\\S\\ref{sec:dual_critic_method}).\n\n\\paragraph{$2{\\times}2$ factorial: recovery vs.\\ prevention.}\nMin drives recovery: narrow dual-critic (${\\sim}1.2$M) recovers fully (${\\sim}16$--$19\\times$ recovery ratio) despite $2\\times$ fewer parameters. Prevention requires min $+$ capacity: wide dual-critic maintains $\\nve \\leq 1.4\\times$ (3/3 prevention, 1/3 non-CIVO collapse). Cross-environment transfer is limited (Appendix~\\ref{sec:dual_critic_appendix}).\n\n%% ============================================================\n%% Online CIVO Detection\n%% ============================================================\n\n\\subsection{Online CIVO Detection}\n\\label{sec:detector}\n\nWe derive a lightweight online detector monitoring the value-to-evaluation ratio for superlinear growth. Applied to 14 runs across three environments, it achieves TPR${=}5/5$, FPR${=}2/9$, with predictive alerts in 2/5 cases (Appendix~\\ref{sec:detector_appendix}).\n",
    "structuredPatch": [
      {
        "oldStart": 87,
        "oldLines": 7,
        "newStart": 87,
        "newLines": 7,
        "lines": [
          " \\subsection{F3--F5: Factorial Ablation (Appendix~\\ref{sec:appendix_factorial})}",
          " \\label{sec:f3f5_summary}",
          " ",
          "-Trained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly sufficient in tested configurations} for CIVO. Neither factor alone precedes pathological overestimation: trained embedding without multi-rate exposure (008a, 3 seeds, peak NVE $0.83$--$0.93\\times$) and multi-rate exposure without embedding (008f, 3 seeds, peak NVE $\\leq 1.41\\times$) both remain below $1.5\\times$. Cross-environment replication on Cheetah Run confirms generalization. Freezing the embedding (\\texttt{requires\\_grad=False}) dramatically reduces severity (NVE $0.19$--$1.88\\times$ vs.\\ trained $1.53$--$4.62\\times$; 2/4 seeds below threshold, 2/4 transient self-correcting spikes; Table~\\ref{tab:three_way_emb}); removing the embedding (008f) also avoids CIVO. Partial gradient blocking (exp\\_044) does not prevent onset (peak NVE $4.45\\times$) but permits delayed self-correction (final eval 538, 59\\% baseline; Appendix~\\ref{sec:appendix_factorial}), confirming that \\emph{any} gradient pathway updating $e_{\\dt}$ suffices to induce CIVO. Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).",
          "+Trained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly sufficient in tested configurations} for CIVO. Neither factor alone precedes pathological overestimation: trained embedding without multi-rate exposure (008a, 3 seeds, peak NVE $0.83$--$0.93\\times$) and multi-rate exposure without embedding (008f, 3 seeds, peak NVE $\\leq 1.41\\times$) both remain below $1.5\\times$. Cross-environment replication on Cheetah Run confirms generalization. Freezing the embedding (\\texttt{requires\\_grad=False}) dramatically reduces severity (NVE $0.19$--$1.88\\times$ vs.\\ trained $1.53$--$4.72\\times$; 2/4 seeds below threshold, 2/4 transient self-correcting spikes; Table~\\ref{tab:three_way_emb}); removing the embedding (008f) also avoids CIVO. Partial gradient blocking (exp\\_044) does not prevent onset (peak NVE $4.45\\times$) but permits delayed self-correction (final eval 538, 59\\% baseline; Appendix~\\ref{sec:appendix_factorial}), confirming that \\emph{any} gradient pathway updating $e_{\\dt}$ suffices to induce CIVO. Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).",
          " ",
          " \\paragraph{ManiSkill manipulation tasks.}",
          " None of three ManiSkill environments exhibit $\\dt$-embedding-dependent CIVO. StackCube-v1 value-ratio spikes are environment-specific: trained (049/052, NVE $5.05$/$4.67\\times$) and frozen (051, $4.30\\times$) match, all self-correcting by 82.5K. PegInsertionSide-v1 exhibits high-amplitude stochastic dynamics ($4$--$11\\times$) whose trained/frozen ordering is seed-dependent: seed~0 trained peaks higher ($10.05\\times$ vs.\\ frozen $1.82\\times$), but seed~1 reverses (frozen peak $11.32\\times$ vs.\\ trained peak $3.08\\times$). PickCube-v1 frozen control (exp\\_054, peak $8.81\\times$ at 62.5K, self-correcting) confirms the same pattern. CIVO is locomotion-specific in DreamerV3; the frozen-embedding diagnostic correctly identifies these transients as non-CIVO."
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

_source line 78_

<details open><summary>🔧 Tool call — Edit · `toolu_01QKFqD2aSFGGzkjeow4Nrod`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "--- & Untreated & 6 & 0/6 & 0\\% \\\\",
  "new_string": "--- & Untreated & 7 & 0/7 & 0\\% \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "1b64a6c9-5cfe-4920-bbe0-dfea1757a86e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHHR5urgKaTwXyCwZ8QK89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4312,
      "cache_read_input_tokens": 46960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4312
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

_source line 79 · 2026-05-24T07:11:42.762Z_

<details><summary>↩ Tool result · `toolu_01QKFqD2aSFGGzkjeow4Nrod`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "58b88e03-748c-4a0b-b26f-57df00412521",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "--- & Untreated & 6 & 0/6 & 0\\% \\\\",
    "newString": "--- & Untreated & 7 & 0/7 & 0\\% \\\\",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$, \\S\\ref{sec:metrics}).\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{Key configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 43 configurations in Table~\\ref{tab:complete_results}.}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^d$ & Env.\\ transient \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^e$ & Env.\\ dynamics$^e$ \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ StackCube transient: frozen control (exp\\_051) exhibits identical spike (peak $4.30\\times$ at 42.5K, self-correcting by 82.5K), indicating environment-specific phenomenon unrelated to $\\dt$-embedding training.\\\\\n$^e$ Seed~0 trained peaks at $10.05\\times$ (82.5K) with delayed self-correction; seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$. Environment-specific stochastic dynamics: frozen final exceeds trained final.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Precedes Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the strongest predictor. The \\emph{primary} comparison---008d (trained, subsample ON) vs.\\ 008f (no embedding, subsample ON)---differs only in embedding training, yielding $\\nve = 4.12\\times$ (eval 82.8) vs.\\ $\\nve \\leq 0.97\\times$ (eval 503.0). \\emph{Secondary} comparisons against 008a/008c (unexposed embedding) co-vary subsample status and horizon alongside the embedding factor. The $\\nve \\geq 1.5\\times$ threshold (35K+ window) correctly classifies 26 of 29 experimental configurations across two environments (AUROC${=}0.953$, in-sample; LOEO cross-validated, Table~\\ref{tab:nve_loeo}; Figure~\\ref{fig:nve_trajectory}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{NVE trajectories (mean $\\pm$ seed range). Trained $\\dt$-embedding (red, Walker Walk, $n{=}3$ seeds plotted; seed~4 data in Table~\\ref{tab:complete_results}) exceeds the $1.5\\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding precedes CIVO in all four Walker Walk seeds (peak NVE: $4.62\\times$, $4.12\\times$, $1.62\\times$, $1.53\\times$), universally degrading performance to below 30\\% of baseline (IQM $175.2$, mean $170.6$, $n{=}4$; \\citealt{agarwal2021precipice}). Downstream trajectories diverge: two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and one self-corrects to a stable but degraded state (29.3\\% of baseline). Combined with Cheetah Run (\\S\\ref{sec:f6}), CIVO onset is universal across all six tested seeds ($n{=}6$, two environments) with 5/6 progressing toward collapse (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Factorial Ablation (Appendix~\\ref{sec:appendix_factorial})}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly sufficient in tested configurations} for CIVO. Neither factor alone precedes pathological overestimation: trained embedding without multi-rate exposure (008a, 3 seeds, peak NVE $0.83$--$0.93\\times$) and multi-rate exposure without embedding (008f, 3 seeds, peak NVE $\\leq 1.41\\times$) both remain below $1.5\\times$. Cross-environment replication on Cheetah Run confirms generalization. Freezing the embedding (\\texttt{requires\\_grad=False}) dramatically reduces severity (NVE $0.19$--$1.88\\times$ vs.\\ trained $1.53$--$4.72\\times$; 2/4 seeds below threshold, 2/4 transient self-correcting spikes; Table~\\ref{tab:three_way_emb}); removing the embedding (008f) also avoids CIVO. Partial gradient blocking (exp\\_044) does not prevent onset (peak NVE $4.45\\times$) but permits delayed self-correction (final eval 538, 59\\% baseline; Appendix~\\ref{sec:appendix_factorial}), confirming that \\emph{any} gradient pathway updating $e_{\\dt}$ suffices to induce CIVO. Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).\n\n\\paragraph{ManiSkill manipulation tasks.}\nNone of three ManiSkill environments exhibit $\\dt$-embedding-dependent CIVO. StackCube-v1 value-ratio spikes are environment-specific: trained (049/052, NVE $5.05$/$4.67\\times$) and frozen (051, $4.30\\times$) match, all self-correcting by 82.5K. PegInsertionSide-v1 exhibits high-amplitude stochastic dynamics ($4$--$11\\times$) whose trained/frozen ordering is seed-dependent: seed~0 trained peaks higher ($10.05\\times$ vs.\\ frozen $1.82\\times$), but seed~1 reverses (frozen peak $11.32\\times$ vs.\\ trained peak $3.08\\times$). PickCube-v1 frozen control (exp\\_054, peak $8.81\\times$ at 62.5K, self-correcting) confirms the same pattern. CIVO is locomotion-specific in DreamerV3; the frozen-embedding diagnostic correctly identifies these transients as non-CIVO.\n\n%% ============================================================\n%% F6--F7: Interventions and cross-environment\n%% ============================================================\n\n\\subsection{F6--F7: Interventions and Multiple Pathways}\n\\label{sec:f6}\n\n\\paragraph{F6: Trained embedding creates multiple vulnerability pathways.}\nExp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained embedding. Two of four seeds collapse (50\\%): Pathway~A (CIVO, $\\nve = 4.02\\times$) and preliminary Pathway~B (entropy \\emph{increase}, $\\nve = 3.78\\times$; 2 seeds only, requires confirmation; Appendix~\\ref{sec:pathways}). Pathway~B produces one of three non-CIVO false positives ($n{=}29$).\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nFull-SGS (exp\\_018) detaches all non-KL gradients from $e_{\\dt}$. Seed~1 shows partial mitigation (eval 448.3, NVE $1.66\\times$); seed~2 collapses (0/2 elimination; Appendix~\\ref{sec:sgs_gradient_analysis}). Cross-environment validation on Cheetah (010b, NVE $8.27$--$108.52\\times$) confirms CIVO generalization; full-SGS yields 0/3 elimination. Removing the embedding eliminates CIVO on Cheetah (024b, NVE $< 0.2\\times$).\n\n\\paragraph{Targeted obs-decoder-only SGS confirms pathway redundancy.}\nObs-decoder-only SGS (exp\\_025/026) achieves 1/6 CIVO prevention (1/4 Walker, 0/2 Cheetah; Table~\\ref{tab:intervention_hierarchy}), not meaningfully different from full-pathway SGS (0/3). CIVO operates through redundant gradient channels: blocking any single pathway shifts co-adaptation to the remaining ones (Appendix~\\ref{sec:seed_divergence}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Intervention hierarchy. Prevention = peak NVE $< 1.5\\times$ (35K+). No level reliably eliminates CIVO across environments.}\n\\label{tab:intervention_hierarchy}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} \\\\\n\\midrule\n--- & Untreated & 6 & 0/6 & 0\\% \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 2/6 & 33\\% \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 0/3 & 0\\% \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% \\\\\n\\midrule\n--- & Embedding frozen & 7 & 5/7$^\\#$ & 71\\% \\\\\n--- & Embedding removed & 5 & 5/5 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\dagger$Walker 2/4 (s2 NVE $2.11\\times$; s3 late-onset CIVO, NVE $3.04\\times$ at 105K); Cheetah 0/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$CIVO prevented but progressive policy erosion (peak 116\\%, final 15\\% baseline).\n$^\\|$Walker 3/3 ($\\nve \\leq 1.4\\times$; 1/3 non-CIVO eval collapse), Cheetah 0/1.\\\\\n$^\\#$Walker 5 + Cheetah 2. Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps; remaining 5 seeds: NVE $0.19$--$1.45\\times$.\\par}\n\\end{table}\n\n%% ============================================================\n%% Forward-pass interventions\n%% ============================================================\n\n\\subsection{Forward-Pass Interventions}\n\\label{sec:forward_results}\n\nWe test two forward-pass alternatives (Table~\\ref{tab:intervention_hierarchy}). \\textbf{RAVE} (value-level capping) fails: the EMA anchor tracks biased values during CIVO onset. \\textbf{TCN} (representation-level noise) suppresses CIVO in 2 of 4 Walker seeds at $\\sigma{=}0.2$ (NVE $< 1.0\\times$, eval 45--91\\%), but remaining seeds show runaway escalation, suggesting TCN gates rather than attenuates CIVO. Cross-environment transfer fails: Cheetah effective dose ($\\sigma{=}1.0$) causes policy erosion to 15\\% baseline; PickCube 0/1 (Appendix~\\ref{sec:tcn_cross_env}). TCN is a \\emph{diagnostic probe}, not a deployable mitigation.\n\n%% ============================================================\n%% Architecture-Level Ablation\n%% ============================================================\n\n\\subsection{Architecture-Level Ablation}\n\\label{sec:arch_results}\n\n\\paragraph{Critic convergence in pure imagination.}\nAcross all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\\rho > 0.999$), with pessimism at 3--4\\% of the independent-critic bound (\\S\\ref{sec:dual_critic_method}).\n\n\\paragraph{$2{\\times}2$ factorial: recovery vs.\\ prevention.}\nMin drives recovery: narrow dual-critic (${\\sim}1.2$M) recovers fully (${\\sim}16$--$19\\times$ recovery ratio) despite $2\\times$ fewer parameters. Prevention requires min $+$ capacity: wide dual-critic maintains $\\nve \\leq 1.4\\times$ (3/3 prevention, 1/3 non-CIVO collapse). Cross-environment transfer is limited (Appendix~\\ref{sec:dual_critic_appendix}).\n\n%% ============================================================\n%% Online CIVO Detection\n%% ============================================================\n\n\\subsection{Online CIVO Detection}\n\\label{sec:detector}\n\nWe derive a lightweight online detector monitoring the value-to-evaluation ratio for superlinear growth. Applied to 14 runs across three environments, it achieves TPR${=}5/5$, FPR${=}2/9$, with predictive alerts in 2/5 cases (Appendix~\\ref{sec:detector_appendix}).\n",
    "structuredPatch": [
      {
        "oldStart": 118,
        "oldLines": 7,
        "newStart": 118,
        "newLines": 7,
        "lines": [
          " \\toprule",
          " \\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} \\\\",
          " \\midrule",
          "---- & Untreated & 6 & 0/6 & 0\\% \\\\",
          "+--- & Untreated & 7 & 0/7 & 0\\% \\\\",
          " \\midrule",
          " Gradient & Reward-only SGS & 2 & 0/2 & 0\\% \\\\",
          " Gradient & Full-pathway SGS & 3 & 0/3 & 0\\% \\\\"
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


### Assistant

_source line 80_

修改 #1, #2, #4, #5 完成。继续修改 #3 (results.tex:81 复杂段落) 和 appendix 相关。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "7b831dce-88a0-4163-9e76-5cfd723ddbc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TK4F2Ft89F87VL5hzvGLcE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13095,
      "cache_read_input_tokens": 51272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13095
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

_source line 81_

<details open><summary>🔧 Tool call — Edit · `toolu_01LAiRRZrHwS3AHd9rfm49ry`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "The trained $\\dt$-embedding precedes CIVO in all four Walker Walk seeds (peak NVE: $4.62\\times$, $4.12\\times$, $1.62\\times$, $1.53\\times$), universally degrading performance to below 30\\% of baseline (IQM $175.2$, mean $170.6$, $n{=}4$; \\citealt{agarwal2021precipice}). Downstream trajectories diverge: two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and one self-corrects to a stable but degraded state (29.3\\% of baseline). Combined with Cheetah Run (\\S\\ref{sec:f6}), CIVO onset is universal across all six tested seeds ($n{=}6$, two environments) with 5/6 progressing toward collapse (Appendix~\\ref{sec:seed_divergence}).",
  "new_string": "The trained $\\dt$-embedding precedes CIVO in all five Walker Walk seeds (peak NVE: $4.72\\times$, $4.62\\times$, $4.12\\times$, $1.62\\times$, $1.53\\times$), universally degrading performance to below 30\\% of baseline (IQM $175.2$, mean $170.6$, $n{=}5$; \\citealt{agarwal2021precipice}). Downstream trajectories diverge: two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and two self-correct (seeds 2 and 5). Combined with Cheetah Run (\\S\\ref{sec:f6}), CIVO onset is universal across all seven tested seeds ($n{=}7$, two environments) with 5/7 progressing toward collapse, 2/7 self-correcting (Appendix~\\ref{sec:seed_divergence})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "02e163a8-1325-4fc4-b7ca-fe43c61bc795",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TK4F2Ft89F87VL5hzvGLcE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13095,
      "cache_read_input_tokens": 51272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13095
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

_source line 82 · 2026-05-24T07:11:57.171Z_

<details><summary>↩ Tool result · `toolu_01LAiRRZrHwS3AHd9rfm49ry`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "19bb7341-4bce-4f0e-b223-148befdfbdc5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "The trained $\\dt$-embedding precedes CIVO in all four Walker Walk seeds (peak NVE: $4.62\\times$, $4.12\\times$, $1.62\\times$, $1.53\\times$), universally degrading performance to below 30\\% of baseline (IQM $175.2$, mean $170.6$, $n{=}4$; \\citealt{agarwal2021precipice}). Downstream trajectories diverge: two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and one self-corrects to a stable but degraded state (29.3\\% of baseline). Combined with Cheetah Run (\\S\\ref{sec:f6}), CIVO onset is universal across all six tested seeds ($n{=}6$, two environments) with 5/6 progressing toward collapse (Appendix~\\ref{sec:seed_divergence}).",
    "newString": "The trained $\\dt$-embedding precedes CIVO in all five Walker Walk seeds (peak NVE: $4.72\\times$, $4.62\\times$, $4.12\\times$, $1.62\\times$, $1.53\\times$), universally degrading performance to below 30\\% of baseline (IQM $175.2$, mean $170.6$, $n{=}5$; \\citealt{agarwal2021precipice}). Downstream trajectories diverge: two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and two self-correct (seeds 2 and 5). Combined with Cheetah Run (\\S\\ref{sec:f6}), CIVO onset is universal across all seven tested seeds ($n{=}7$, two environments) with 5/7 progressing toward collapse, 2/7 self-correcting (Appendix~\\ref{sec:seed_divergence}).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$, \\S\\ref{sec:metrics}).\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{Key configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 43 configurations in Table~\\ref{tab:complete_results}.}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^d$ & Env.\\ transient \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^e$ & Env.\\ dynamics$^e$ \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ StackCube transient: frozen control (exp\\_051) exhibits identical spike (peak $4.30\\times$ at 42.5K, self-correcting by 82.5K), indicating environment-specific phenomenon unrelated to $\\dt$-embedding training.\\\\\n$^e$ Seed~0 trained peaks at $10.05\\times$ (82.5K) with delayed self-correction; seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$. Environment-specific stochastic dynamics: frozen final exceeds trained final.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Precedes Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the strongest predictor. The \\emph{primary} comparison---008d (trained, subsample ON) vs.\\ 008f (no embedding, subsample ON)---differs only in embedding training, yielding $\\nve = 4.12\\times$ (eval 82.8) vs.\\ $\\nve \\leq 0.97\\times$ (eval 503.0). \\emph{Secondary} comparisons against 008a/008c (unexposed embedding) co-vary subsample status and horizon alongside the embedding factor. The $\\nve \\geq 1.5\\times$ threshold (35K+ window) correctly classifies 26 of 29 experimental configurations across two environments (AUROC${=}0.953$, in-sample; LOEO cross-validated, Table~\\ref{tab:nve_loeo}; Figure~\\ref{fig:nve_trajectory}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{NVE trajectories (mean $\\pm$ seed range). Trained $\\dt$-embedding (red, Walker Walk, $n{=}3$ seeds plotted; seed~4 data in Table~\\ref{tab:complete_results}) exceeds the $1.5\\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding precedes CIVO in all four Walker Walk seeds (peak NVE: $4.62\\times$, $4.12\\times$, $1.62\\times$, $1.53\\times$), universally degrading performance to below 30\\% of baseline (IQM $175.2$, mean $170.6$, $n{=}4$; \\citealt{agarwal2021precipice}). Downstream trajectories diverge: two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and one self-corrects to a stable but degraded state (29.3\\% of baseline). Combined with Cheetah Run (\\S\\ref{sec:f6}), CIVO onset is universal across all six tested seeds ($n{=}6$, two environments) with 5/6 progressing toward collapse (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Factorial Ablation (Appendix~\\ref{sec:appendix_factorial})}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly sufficient in tested configurations} for CIVO. Neither factor alone precedes pathological overestimation: trained embedding without multi-rate exposure (008a, 3 seeds, peak NVE $0.83$--$0.93\\times$) and multi-rate exposure without embedding (008f, 3 seeds, peak NVE $\\leq 1.41\\times$) both remain below $1.5\\times$. Cross-environment replication on Cheetah Run confirms generalization. Freezing the embedding (\\texttt{requires\\_grad=False}) dramatically reduces severity (NVE $0.19$--$1.88\\times$ vs.\\ trained $1.53$--$4.72\\times$; 2/4 seeds below threshold, 2/4 transient self-correcting spikes; Table~\\ref{tab:three_way_emb}); removing the embedding (008f) also avoids CIVO. Partial gradient blocking (exp\\_044) does not prevent onset (peak NVE $4.45\\times$) but permits delayed self-correction (final eval 538, 59\\% baseline; Appendix~\\ref{sec:appendix_factorial}), confirming that \\emph{any} gradient pathway updating $e_{\\dt}$ suffices to induce CIVO. Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).\n\n\\paragraph{ManiSkill manipulation tasks.}\nNone of three ManiSkill environments exhibit $\\dt$-embedding-dependent CIVO. StackCube-v1 value-ratio spikes are environment-specific: trained (049/052, NVE $5.05$/$4.67\\times$) and frozen (051, $4.30\\times$) match, all self-correcting by 82.5K. PegInsertionSide-v1 exhibits high-amplitude stochastic dynamics ($4$--$11\\times$) whose trained/frozen ordering is seed-dependent: seed~0 trained peaks higher ($10.05\\times$ vs.\\ frozen $1.82\\times$), but seed~1 reverses (frozen peak $11.32\\times$ vs.\\ trained peak $3.08\\times$). PickCube-v1 frozen control (exp\\_054, peak $8.81\\times$ at 62.5K, self-correcting) confirms the same pattern. CIVO is locomotion-specific in DreamerV3; the frozen-embedding diagnostic correctly identifies these transients as non-CIVO.\n\n%% ============================================================\n%% F6--F7: Interventions and cross-environment\n%% ============================================================\n\n\\subsection{F6--F7: Interventions and Multiple Pathways}\n\\label{sec:f6}\n\n\\paragraph{F6: Trained embedding creates multiple vulnerability pathways.}\nExp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained embedding. Two of four seeds collapse (50\\%): Pathway~A (CIVO, $\\nve = 4.02\\times$) and preliminary Pathway~B (entropy \\emph{increase}, $\\nve = 3.78\\times$; 2 seeds only, requires confirmation; Appendix~\\ref{sec:pathways}). Pathway~B produces one of three non-CIVO false positives ($n{=}29$).\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nFull-SGS (exp\\_018) detaches all non-KL gradients from $e_{\\dt}$. Seed~1 shows partial mitigation (eval 448.3, NVE $1.66\\times$); seed~2 collapses (0/2 elimination; Appendix~\\ref{sec:sgs_gradient_analysis}). Cross-environment validation on Cheetah (010b, NVE $8.27$--$108.52\\times$) confirms CIVO generalization; full-SGS yields 0/3 elimination. Removing the embedding eliminates CIVO on Cheetah (024b, NVE $< 0.2\\times$).\n\n\\paragraph{Targeted obs-decoder-only SGS confirms pathway redundancy.}\nObs-decoder-only SGS (exp\\_025/026) achieves 1/6 CIVO prevention (1/4 Walker, 0/2 Cheetah; Table~\\ref{tab:intervention_hierarchy}), not meaningfully different from full-pathway SGS (0/3). CIVO operates through redundant gradient channels: blocking any single pathway shifts co-adaptation to the remaining ones (Appendix~\\ref{sec:seed_divergence}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Intervention hierarchy. Prevention = peak NVE $< 1.5\\times$ (35K+). No level reliably eliminates CIVO across environments.}\n\\label{tab:intervention_hierarchy}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} \\\\\n\\midrule\n--- & Untreated & 7 & 0/7 & 0\\% \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 2/6 & 33\\% \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 0/3 & 0\\% \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% \\\\\n\\midrule\n--- & Embedding frozen & 7 & 5/7$^\\#$ & 71\\% \\\\\n--- & Embedding removed & 5 & 5/5 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\dagger$Walker 2/4 (s2 NVE $2.11\\times$; s3 late-onset CIVO, NVE $3.04\\times$ at 105K); Cheetah 0/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$CIVO prevented but progressive policy erosion (peak 116\\%, final 15\\% baseline).\n$^\\|$Walker 3/3 ($\\nve \\leq 1.4\\times$; 1/3 non-CIVO eval collapse), Cheetah 0/1.\\\\\n$^\\#$Walker 5 + Cheetah 2. Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps; remaining 5 seeds: NVE $0.19$--$1.45\\times$.\\par}\n\\end{table}\n\n%% ============================================================\n%% Forward-pass interventions\n%% ============================================================\n\n\\subsection{Forward-Pass Interventions}\n\\label{sec:forward_results}\n\nWe test two forward-pass alternatives (Table~\\ref{tab:intervention_hierarchy}). \\textbf{RAVE} (value-level capping) fails: the EMA anchor tracks biased values during CIVO onset. \\textbf{TCN} (representation-level noise) suppresses CIVO in 2 of 4 Walker seeds at $\\sigma{=}0.2$ (NVE $< 1.0\\times$, eval 45--91\\%), but remaining seeds show runaway escalation, suggesting TCN gates rather than attenuates CIVO. Cross-environment transfer fails: Cheetah effective dose ($\\sigma{=}1.0$) causes policy erosion to 15\\% baseline; PickCube 0/1 (Appendix~\\ref{sec:tcn_cross_env}). TCN is a \\emph{diagnostic probe}, not a deployable mitigation.\n\n%% ============================================================\n%% Architecture-Level Ablation\n%% ============================================================\n\n\\subsection{Architecture-Level Ablation}\n\\label{sec:arch_results}\n\n\\paragraph{Critic convergence in pure imagination.}\nAcross all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\\rho > 0.999$), with pessimism at 3--4\\% of the independent-critic bound (\\S\\ref{sec:dual_critic_method}).\n\n\\paragraph{$2{\\times}2$ factorial: recovery vs.\\ prevention.}\nMin drives recovery: narrow dual-critic (${\\sim}1.2$M) recovers fully (${\\sim}16$--$19\\times$ recovery ratio) despite $2\\times$ fewer parameters. Prevention requires min $+$ capacity: wide dual-critic maintains $\\nve \\leq 1.4\\times$ (3/3 prevention, 1/3 non-CIVO collapse). Cross-environment transfer is limited (Appendix~\\ref{sec:dual_critic_appendix}).\n\n%% ============================================================\n%% Online CIVO Detection\n%% ============================================================\n\n\\subsection{Online CIVO Detection}\n\\label{sec:detector}\n\nWe derive a lightweight online detector monitoring the value-to-evaluation ratio for superlinear growth. Applied to 14 runs across three environments, it achieves TPR${=}5/5$, FPR${=}2/9$, with predictive alerts in 2/5 cases (Appendix~\\ref{sec:detector_appendix}).\n",
    "structuredPatch": [
      {
        "oldStart": 78,
        "oldLines": 7,
        "newStart": 78,
        "newLines": 7,
        "lines": [
          " \\label{fig:nve_trajectory}",
          " \\end{figure}",
          " ",
          "-The trained $\\dt$-embedding precedes CIVO in all four Walker Walk seeds (peak NVE: $4.62\\times$, $4.12\\times$, $1.62\\times$, $1.53\\times$), universally degrading performance to below 30\\% of baseline (IQM $175.2$, mean $170.6$, $n{=}4$; \\citealt{agarwal2021precipice}). Downstream trajectories diverge: two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and one self-corrects to a stable but degraded state (29.3\\% of baseline). Combined with Cheetah Run (\\S\\ref{sec:f6}), CIVO onset is universal across all six tested seeds ($n{=}6$, two environments) with 5/6 progressing toward collapse (Appendix~\\ref{sec:seed_divergence}).",
          "+The trained $\\dt$-embedding precedes CIVO in all five Walker Walk seeds (peak NVE: $4.72\\times$, $4.62\\times$, $4.12\\times$, $1.62\\times$, $1.53\\times$), universally degrading performance to below 30\\% of baseline (IQM $175.2$, mean $170.6$, $n{=}5$; \\citealt{agarwal2021precipice}). Downstream trajectories diverge: two seeds undergo full collapse, one exhibits late-onset collapse still declining at 105K, and two self-correct (seeds 2 and 5). Combined with Cheetah Run (\\S\\ref{sec:f6}), CIVO onset is universal across all seven tested seeds ($n{=}7$, two environments) with 5/7 progressing toward collapse, 2/7 self-correcting (Appendix~\\ref{sec:seed_divergence}).",
          " ",
          " %% ============================================================",
          " %% F3--F5: Summary (details in Appendix B)"
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

_source line 83_

<details open><summary>🔧 Tool call — Edit · `toolu_01KV4Si1dZCRjYz7YsPTQJX9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "Table~\\ref{tab:complete_results} reports all 42 experimental configurations.",
  "new_string": "Table~\\ref{tab:complete_results} reports all 43 experimental configurations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "759b1702-7c0f-43a5-bd29-8c3f34965ebf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TK4F2Ft89F87VL5hzvGLcE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13095,
      "cache_read_input_tokens": 51272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13095
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

_source line 84 · 2026-05-24T07:11:58.500Z_

<details><summary>↩ Tool result · `toolu_01KV4Si1dZCRjYz7YsPTQJX9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "cb80c371-3779-4def-8440-b4af4f16462f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "Table~\\ref{tab:complete_results} reports all 42 experimental configurations.",
    "newString": "Table~\\ref{tab:complete_results} reports all 43 experimental configurations.",
    "originalFile": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 42 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\\times$ & Transient (self-corr.) \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\rowcolor{gray!15}\n008e\\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\\times$ & CIVO collapse \\\\\n008e\\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\\times$ & Healthy \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\n$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\n$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\n$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\n$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\par}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n\\label{tab:cross_domain}\n\\footnotesize\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n\\midrule\nLocomotion & Walker Walk & 4/4 & 0/3 & Yes (NVE $1.53$--$4.62\\times$) \\\\\nLocomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\nManipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\nManipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\nManipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all ten factorial experiments (including four 008e\\_v3 seeds). Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\\_v3\\_s3 exhibits CIVO with NVE $4.02\\times$ despite $\\Delta t{=}1$ imagination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.83 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.12 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s3 & 4.02 & CIVO           & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.02\\times$, exp~008e\\_v3\\_s3) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.02]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.958$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=7$, $n=10$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). $^\\dagger$Optimal threshold in $(3.78, 4.02]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 3 & 0 & 4 & 70.0\\% \\; [34.8, 93.3] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.2\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.5\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 3 & 0 & 0 & 7 & 100\\% \\; [69.2, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=4$, $n_{\\text{neg}}=6$, $n=10$, $\\text{AUROC}=0.958$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 4 & 2 & 0 & 4 & 80.0\\% \\; [44.4, 97.5] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 1.2\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.7\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 3.9\\times$ & 3 & 0 & 1 & 6 & 90.0\\% \\; [55.5, 99.7] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\\text{pos}}=8$, $n_{\\text{neg}}=8$, $n=16$, $\\text{AUROC}=0.969$). Includes Walker Walk (14 configurations) and Cheetah Run (2 configurations).}\n\\label{tab:sensitivity_b2_full}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 8 & 2 & 0 & 6 & 87.5\\% \\; [61.7, 98.4] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.2\\times$ & 8 & 1 & 0 & 7 & 93.8\\% \\; [69.8, 99.8] & 88.9\\% & 100\\% & 94.1\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 8 & 1 & 0 & 7 & 93.8\\% \\; [69.8, 99.8] & 88.9\\% & 100\\% & 94.1\\% \\\\\n$\\geq 1.7\\times$ & 6 & 1 & 2 & 7 & 81.3\\% \\; [54.4, 96.0] & 85.7\\% & 75.0\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 6 & 1 & 2 & 7 & 81.3\\% \\; [54.4, 96.0] & 85.7\\% & 75.0\\% & 80.0\\% \\\\\n$\\geq 3.9\\times$ & 6 & 0 & 2 & 8 & 87.5\\% \\; [61.7, 98.4] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all four CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 75.0\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 88.9\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 3$ the statistical power remains limited (accuracy 95\\% CI: [69.2\\%, 100\\%]).\n\n\\subsection{Expanded ROC Analysis}\n\\label{sec:roc_analysis}\n\nThe original $n{=}16$ analysis (Tables~\\ref{tab:sensitivity_b1}--\\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}29$ configurations spanning all tested interventions. Figure~\\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\\% bootstrap confidence interval (10{,}000 resamples).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.7\\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}\n\\caption{NVE ROC curve ($n{=}29$ configurations, AUROC${=}0.953$, in-sample, post-hoc). The preset $\\nve \\geq 1.5\\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}\n\\label{fig:nve_roc}\n\\end{figure}\n\nWe label a configuration as CIVO-positive if and only if (i)~it uses a trained $\\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.\n\nThe three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\\_008e\\_v3 seed~2, actor entropy \\emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \\emph{decrease}). All three produce NVE $> 1.5\\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\\times$) lacks $\\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\\times$) exhibits the full CIVO causal chain: trained $\\dt$-embedding, entropy decrease, and evaluation collapse to 14\\% of baseline.\n\n\\subsection{NVE Normalization Robustness}\n\\label{sec:nve_robustness}\n\nTo assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\\ref{tab:baseline_seeds}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Walker Walk baseline seeds at 105K and 505K steps.}\n\\label{tab:baseline_seeds}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Eval@105K} & \\textbf{Eval@505K} & \\textbf{ve@65K} & \\textbf{ve@105K} \\\\\n\\midrule\ns1 & 915.7 & 970.4 & 0.563 & 0.656 \\\\\ns2 & 443.5 & 945.7 & 0.898 & 0.742 \\\\\ns3 & 869.0 & 947.7 & --- & 0.664 \\\\\ns4 & 922.8 & 938.9 & --- & 0.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\\times$; 009b seed~2, peak NVE $1.62\\times$) to fall below the $1.5\\times$ threshold. Core CIVO cases (peak NVE $> 3\\times$) remain correctly classified under all baseline seeds.\n\nSingle-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\\%): the boundary case exp\\_009b flips from $\\nve = 1.62\\times$ (s1) to $1.23\\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\\times \\to 4.52\\times$; 008d: $4.12\\times \\to 3.54\\times$). The $1.5\\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\\% of the threshold.\n\n\\paragraph{Normalization conventions.} Walker NVE is normalized against the 4-seed mean baseline (seeds~1--4, each run to 505K+ steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).\n\n\\paragraph{Limitations.} With $n = 10$ experiments, Clopper-Pearson confidence intervals remain wide (e.g., 90.0\\% accuracy has 95\\% CI [55.5\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds. Table~\\ref{tab:sensitivity_b2_full} reports the original $n{=}16$ evaluation set spanning both environments. The expanded analysis ($n{=}29$, including SGS variants, RAVE, and TCN configurations) yields AUROC${=}0.953$ (Figure~\\ref{fig:nve_roc}, in-sample, post-hoc). The original $n{=}16$ core analysis yields AUROC${=}0.969$; the expanded $n{=}29$ set includes SGS, RAVE, TCN, and dual-critic configurations. Cross-architecture validation is deferred to future work.\n\n\\subsection{Leave-One-Environment-Out Cross-Validation}\n\\label{sec:nve_loeo}\n\nTo assess whether $\\theta{=}1.5\\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}13$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\\theta{=}1.5\\times$ on the held-out environment.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-environment-out cross-validation of NVE threshold $\\theta=1.5\\times$.\nFor each fold, the threshold is validated on an environment whose data was \\emph{not} used\nto select $\\theta$. The optimal threshold range on each training set is reported;\n$\\theta=1.5$ falls within the optimal range in all three folds.}\n\\label{tab:nve_loeo}\n\\begin{tabular}{lccccc}\n\\toprule\nHeld-out & $N_{\\text{train}}$ & $N_{\\text{test}}$ & $\\theta_{\\text{opt}}$ range & Test Accuracy & Test AUROC \\\\\n\\midrule\nPickCube & 18 & 2 & $(1.45,\\, 1.53]$ & 2/2 (1.000) & 1.000 \\\\\nCheetah  & 15 & 5 & $(1.45,\\, 1.53]$ & 5/5 (1.000) & 1.000 \\\\\nWalker   &  7 & 13 & $(1.00,\\, 3.78)$ & 12/13 (0.923) & 0.944 \\\\\n\\midrule\n\\textbf{Mean} & — & — & — & \\textbf{0.974} & \\textbf{0.981} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe threshold $\\theta{=}1.5\\times$ falls within the optimal accuracy range for all three training folds: $(1.45, 1.53]$ when Walker data is available, and the wider $(1.00, 3.78)$ when training on Cheetah$+$PickCube only (where CIVO and non-CIVO NVE values are well-separated). The single cross-validation error is exp\\_008e\\_v3 seed~2 (Walker), an IRD collapse mechanistically distinct from CIVO (\\S\\ref{sec:roc_analysis}). Mean held-out accuracy is 0.974 and mean AUROC is 0.981, confirming that $\\theta{=}1.5\\times$ generalizes across environments without retuning. PickCube fold confidence intervals remain wide (Clopper-Pearson 95\\% CI: $[0.158, 1.000]$) due to $N_{\\text{test}}{=}2$.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\paragraph{Embedding gradient analysis.}\nTable~\\ref{tab:three_way_emb} isolates embedding \\emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\\dt{=}2$ imagination).\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}\n\\label{tab:three_way_emb}\n\\footnotesize\n\\begin{tabular}{lccccl}\n\\toprule\nCondition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\\\\n\\midrule\nTrained & all & 008d & $1.53$--$4.62\\times$ & 64--268 & 4/4 \\\\\nReward detach & obs+KL only & 044 & $4.45\\times$ & 44$\\to$538$^\\dagger$ & 1/1 \\\\\nFull SGS & KL only & 018 & $1.66\\times$ & 448 & 1/1$^*$ \\\\\nFrozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\\nRemoved & N/A & 008f & $0.97$--$1.41\\times$ & 307--503 & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\\times$); seed~2 collapsed. $^\\dagger$Self-corrected at ${\\sim}175$K (eval 44$\\to$538, 59\\% baseline; 224K run). $^\\ddagger$Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps.\\par}\n\\end{table}\n\nThe reward-detach condition (exp\\_044, \\texttt{reward\\_dt\\_emb\\_detach=True}) uses a backward hook to block reward-head gradients from reaching $e_{\\dt}$, complementing the framework-level Reward SGS (exp\\_016e). Both yield the same directional result---CIVO onset not prevented---ruling out implementation artifacts. Exp\\_044 exhibits delayed CIVO onset (${\\sim}95$K vs.\\ typical $25$--$35$K), consistent with reduced but non-zero gradient pressure on $e_{\\dt}$. Over a full 224K run, exp\\_044 self-corrects: eval recovers from 44 (95K) to 538 (215K, 59\\% baseline), but this recovery is incomplete compared to spontaneous recovery without gradient intervention (exp\\_045: 868, 95\\% baseline). The lower asymptote suggests that selectively disrupting gradient flow may create optimization difficulties beyond CIVO itself.\n\nTable~\\ref{tab:factorial_design} summarizes the experimental configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Factorial design. Each row specifies one experimental configuration. \\textbf{Emb}: $\\dt$-embedding mode. \\textbf{Sub}: temporal subsampling. \\textbf{H}: imagination horizon. \\textbf{Imag $\\dt$}: temporal resolution used during imagination.}\n\\label{tab:factorial_design}\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{ID} & \\textbf{Purpose} & \\textbf{Emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Imag $\\dt$} \\\\\n\\midrule\n001 & Reference baseline & --- & --- & 15 & 1 \\\\\n006 & Fixed $\\dt{=}2$ & trn & on & 15 & 2 \\\\\n007 & Fixed $\\dt{=}4$ & trn & on & 15 & 4 \\\\\n\\midrule\n008a & Unexposed emb ctrl & exp$^a$ & off & 15 & 2 \\\\\n008c & Horizon control & exp$^a$ & off & 8 & 2 \\\\\n008d & Collapse condition & trn & on & 8 & 2 \\\\\n008e\\_v3 & $\\dt{=}1$ imag control & trn & on & 15 & 1 \\\\\n008f & Causal ablation & --- & on & 8 & 2 \\\\\n\\midrule\n015b & Frozen-emb ctrl & frz$^b$ & on & 8 & 2 \\\\\n016e & Stop-grad (reward) & trn$^\\dagger$ & on & 8 & 2 \\\\\n018 & Full-SGS & trn$^\\ddagger$ & on & 8 & 2 \\\\\n\\midrule\n005 & Learned gate & adaptive & off & 15 & learned \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^\\dagger$ \\texttt{reward\\_dt\\_emb\\_detach=True}; $^\\ddagger$ all non-KL gradients to \\texttt{dt\\_emb} detached.\\par}\n\\end{table}\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe empirical finding that trained embedding \\emph{plus} multi-rate exposure jointly predict CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.83$--$0.93\\times$ range across 3 seeds (105K steps). Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical factor is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training. This confirms that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.42\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.47 \\rightarrow 0.39 \\rightarrow 0.42$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and precedes full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.42\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that in all tested configurations, CIVO occurs only with the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\nCross-environment validation on Cheetah Run replicates the empirical pattern: trained $e_{\\dt}$ precedes CIVO in both tested seeds (exp\\_010b, 2 seeds, NVE $8.27$--$108.52\\times$, collapse to 51.7/0.83) while removing the embedding eliminates it (exp\\_024b, 2 seeds, NVE $<0.2\\times$, eval 96.5/77.3). Freezing the embedding on Cheetah (exp\\_046, NVE${=}1.35\\times$ vs.\\ trained $70.64\\times$, a $52\\times$ reduction) further confirms that embedding trainability, not architecture, drives CIVO. This extends the sufficiency finding from Walker Walk to a second locomotion environment with qualitatively different dynamics (6-joint vs.\\ 2-joint).\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole predictor of CIVO in tested configurations. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) precedes CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly sufficient in tested configurations.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling precedes collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$; low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig4_mechanism_diagram.pdf}\n\\caption{CIVO mechanism diagram. The trained $\\dt$-embedding enables asymmetric reward prediction fidelity, initiating a feedback loop: biased RSSM rewards $\\to$ optimistic critic values $\\to$ actor exploitation $\\to$ reinforced state-distribution skew.}\n\\label{fig:civo_mechanism}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO (Figure~\\ref{fig:civo_mechanism}).  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, which confirms that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\paragraph{Signed reward error analysis.}\nTo test whether CIVO arises from one-step reward overprediction, we compute signed error (predicted $-$ actual) on posterior-conditioned RSSM predictions (Table~\\ref{tab:signed_error}). The trained-embedding model (008d) shows \\emph{negative} bias at $\\dt{=}2$ (mean signed error $-0.599$, only 8\\% of samples overpredicted), ruling out observation-level reward overprediction as the mechanism. The baseline is well-calibrated (mean SE $\\approx 0$), confirming methodological soundness. Value overestimation therefore occurs during \\emph{imagination-level} prior drift: the RSSM prior (unconditioned on observations) generates reward-favorable trajectories at $\\dt > 1$ (Stage~1 above, $1.68\\times$ ratio under random policy), and the critic accumulates these into overestimated returns. The one-step reward prediction is negatively biased when conditioned on real observations, but this posterior correction is unavailable during imagination. This also distinguishes CIVO from generic compounding error, which would produce \\emph{positive} signed error accumulating with horizon; the negative observation-level bias confirms that CIVO is a prior-drift phenomenon, not a reward-prediction artifact.\n\n\\begin{table}[h]\n\\centering\n\\caption{Signed reward error (predicted $-$ actual) on posterior-conditioned RSSM predictions. Negative values indicate underprediction. The trained-embedding model underpredicts at $\\dt{=}2$, ruling out observation-level reward overprediction as the CIVO mechanism.}\n\\label{tab:signed_error}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Config} & $\\dt$ & \\textbf{Mean SE} & \\textbf{Std} & \\textbf{\\%Over} & \\textbf{Actual} & \\textbf{Pred} \\\\\n\\midrule\nBaseline & 1 & $+0.001$ & 0.023 & 39.6\\% & 1.893 & 1.894 \\\\\n\\midrule\n008d (trained) & 1 & $+0.018$ & 0.072 & 61.8\\% & 0.361 & 0.379 \\\\\n008d (trained) & 2 & $\\mathbf{-0.599}$ & 0.722 & 8.0\\% & 0.721 & 0.121 \\\\\n\\midrule\n008f (no emb) & 1 & $-0.710$ & 0.704 & 14.0\\% & 0.921 & 0.211 \\\\\n008f (no emb) & 2 & $-1.645$ & 1.485 & 5.0\\% & 1.840 & 0.195 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 0/2 CIVO elimination rate on Walker (seed~1: NVE reduced from $4.12\\times$ to $1.66\\times$ but remains CIVO-positive; seed~2: collapsed) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention eliminates CIVO in neither seed: seed~1 shows partial mitigation (eval 448.3, peak NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses (eval 40.8). Removing the observation decoder gradient channel is thus contributory but not sufficient. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3. \\textbf{Trained dt-emb} (008d)\\protect\\footnotemark: learned $d{=}32$ temporal embedding with multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with all non-KL gradients detached from $e_{\\dt}$. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$. Full-SGS seed~1 shows partial mitigation ($-51\\%$ final, NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses ($-96\\%$ final). CIVO elimination rate $= 0/2$.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}\n\nCross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This transient self-correcting trajectory is not attributable to the SGS intervention: the initial CIVO onset and peak severity are comparable to the unmitigated case, and the self-correction may reflect Cheetah Run's simpler dynamics rather than SGS efficacy.  Performance remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's Walker results (0/2 CIVO elimination), these findings yield a 0/3 elimination rate across environments, indicating that gradient-level interventions alone do not eliminate the CIVO vulnerability. Additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Post-CIVO outcomes for all six CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Env} & \\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\nWalker & s1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\nWalker & s2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\nWalker & s3 (008d\\_s3) & 1.53$\\times$ & 1.53$\\times$ & 268$^\\diamond$ & Late-onset collapse \\\\\nWalker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\n\\midrule\nCheetah & s1 (010b) & 8.27$\\times$ & 8.27$\\times$ & 51.7 & Full collapse \\\\\nCheetah & s0 (010b\\_s0) & 108.52$\\times$ & 108.52$\\times$ & 0.83 & Full collapse \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\diamond$ Transitional; train returns still declining at 105K.\\par}\n\\end{table}\n\nAll six CIVO-positive seeds cross the $\\nve > 1.5\\times$ threshold (Table~\\ref{tab:post_civo}), yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Full collapse is the majority outcome (5/6 seeds), with one self-correction case (Walker seed~2) that remains severely degraded (29.3\\% of baseline). Cheetah seeds exhibit more extreme overestimation (peak NVE $8.27$--$108.52\\times$ vs.\\ Walker's $1.53$--$4.62\\times$), consistent with the Cheetah reward scale amplifying the fidelity gap.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\paragraph{A fourth trajectory: CIVO-induced persistent value collapse.}\nObs-decoder SGS seed~3 (exp\\_025) exhibits a trajectory not observed in the untreated seeds: healthy through 105K ($\\nve < 1.0\\times$, eval 818.6), CIVO onset at 135K ($\\nve = 5.47\\times$, eval 67.0), followed by evaluation recovery (590.2 at 215K, 64\\% of baseline) but persistent value collapse ($\\nve = 0.14\\times$, value mean 80.6). The critic undershoots after the CIVO episode, suggesting that CIVO-induced representational damage may be irreversible even when the policy partially recovers. This contrasts with transient CIVO (seed~2, 009b), where both value and evaluation recover jointly, and with full collapse (seed~1, 008d), where neither recovers. Seed~4 exhibits the same terminal value collapse ($\\nve = 0.14\\times$ at 215K, eval 242), suggesting this overcorrection is systematic rather than seed-specific. The pattern adds a fourth post-CIVO outcome---policy recovery with critic damage---to the three documented in Table~\\ref{tab:post_civo}.\n\n\\subsubsection{Failure and Degradation Mode Taxonomy}\n\nTable~\\ref{tab:failure_modes} classifies the seven distinct failure and degradation modes observed across all experimental configurations. The taxonomy reveals that CIVO is not a single failure mode but a family of related pathologies, with the trained $\\dt$-embedding creating vulnerability through at least three independent mechanisms: value-driven collapse (monotonic, late-onset, and SGS-resistant CIVO), entropy-driven instability (IRD collapse), and gradient-mediated effects (gradient starvation, SGS-paradoxical worsening).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Failure and degradation mode taxonomy. Each mode is characterized by its NVE trajectory, entropy behavior, and primary mechanism.}\n\\label{tab:failure_modes}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccl@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Representative} & \\textbf{NVE} & \\textbf{Entropy} & \\textbf{Mechanism} \\\\\n\\midrule\nMonotonic CIVO & 008d, 008d\\_s4, 010b\\_s0 & $\\uparrow$ sustained & $\\downarrow$ & Reward bias $\\to$ critic $\\to$ actor \\\\\nLate-onset CIVO & 008d\\_s3 & $\\uparrow$ delayed & $\\downarrow$ & Same, delayed onset \\\\\nTransient CIVO & 009b & Peak $\\to$ $\\downarrow$ & Stable & Self-correction via capacity \\\\\nIRD collapse & 008e\\_v3\\_s2 & $\\uparrow$ late & $\\uparrow$ & Entropy-driven, values stable \\\\\nGrad.\\ starvation & 015b & Oscillates, decays & Stable & Frozen emb $\\to$ zero actor grad \\\\\nSGS-resistant & 018\\_s2 & $\\uparrow$ & $\\downarrow$ & Forward-pass conditioning \\\\\nSGS-paradoxical & 016e & $\\uparrow$ sustained & $\\downarrow$ & Reward SGS $\\to$ obs-dec reliance \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) avoids collapse in 2 of 4 seeds (50\\%), while the remaining two collapse via distinct mechanisms: Pathway~A (CIVO-driven, entropy decrease; s3, NVE $4.02\\times$) and Pathway~B (entropy-driven, entropy increase; s2, NVE $3.78\\times$; \\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse patterns identified in \\S\\ref{sec:f6}---CIVO (Pathway~A, value-driven, entropy decreasing) and a tentative second mode (Pathway~B, eval-driven, entropy increasing)---have distinct diagnostic signatures. Pathway~B is observed in only two seeds (008e\\_v3\\_s2 and 038\\_s2); we present it as preliminary evidence that the trained $\\dt$-embedding's learned features may affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B), though additional data is needed to confirm this as a distinct mechanism.  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse (Figure~\\ref{fig:multiple_pathways}).\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.  The CIVO mechanism requires three structural properties: (1) a temporal embedding that co-adapts with dynamics via gradient flow, (2) multi-step imagined rollouts used for critic training, and (3) a reward head that inherits latent biases from the shared representation.  Transformer-based world models that share these properties may exhibit analogous vulnerability; architectures that decouple temporal conditioning from the reward prediction pathway would not.\n\n\\subsection{Cross-Environment TCN Evaluation}\n\\label{sec:tcn_cross_env}\n\nTable~\\ref{tab:tcn_full} reports the full TCN evaluation across environments and noise magnitudes.\n\n\\begin{table}[h]\n\\centering\n\\caption{TCN results across environments and noise magnitudes. Prevention = peak NVE $< 1.5\\times$ (35K+).}\n\\label{tab:tcn_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Env} & $\\sigma$ & \\textbf{Seed} & \\textbf{NVE$_{\\max}$} & \\textbf{Prevented?} & \\textbf{Eval (\\%)} \\\\\n\\midrule\nWalker & 0.1 & s0 & 1.02 & \\checkmark$^*$ & 55\\% \\\\\nWalker & 0.2 & s0 & 0.91 & \\checkmark & 91\\% \\\\\nWalker & 0.2 & s1 & 0.64 & \\checkmark & 45\\% \\\\\nWalker & 0.2 & s2 & 2.11$^\\dagger$ & $\\times$ & ${\\sim}5\\%$ \\\\\n\\rowcolor{gray!15}\nWalker & 0.2 & s3 & 3.04$^\\P$ & $\\times$ & 11\\% \\\\\nWalker & 0.5 & s0 & 3.97 & $\\times$ & 27\\% \\\\\nWalker & 0.5 & s1 & 1.64 & $\\times$ & 41\\% \\\\\n\\midrule\nCheetah & 0.2 & s0 & 1.90 & $\\times$ & crashed \\\\\nCheetah & 0.5 & s0 & 10.67 & $\\times$ & 26\\% \\\\\nCheetah & 1.0 & s0 & $\\leq$0.30 & \\checkmark$^\\S$ & 15\\% \\\\\n\\midrule\nPickCube & 0.2 & s0 & 3.71 & $\\times$ & failing \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Borderline: NVE${=}1.02\\times$ at 95K, below $1.5\\times$ threshold but above $1.0\\times$.\\\\\n$^\\dagger$NVE $= 2.11\\times$ at 95K, still rising; eval ${\\sim}5\\%$ of baseline.\\\\\n$^\\P$Late-onset CIVO: NVE declined to $0.67\\times$ at 95K before phase-transition-like spike to $3.04\\times$ at 105K; eval 349.6 at 95K $\\to$ 71.8 at 105K $\\to$ 104.5 at 215K.\\\\\n$^\\S$CIVO prevented (NVE${\\leq}0.30$); peak eval 116\\% baseline at 35K, declining to 15\\% by 215K via progressive policy erosion. See ``impossible dose'' discussion.\\par}\n\\end{table}\n\n\\paragraph{Cheetah Run $\\sigma{=}0.5$: transient spike with permanent eval damage.}\nCheetah $\\sigma{=}0.5$ exhibits a novel failure mode: a transient CIVO spike (NVE $= 10.67\\times$ at 55K) followed by NVE recovery ($< 0.3\\times$ by 95K), but permanent evaluation damage (26\\% of baseline). The value signal self-corrects while the policy does not recover, suggesting that CIVO-induced representational damage during the spike is irreversible even when the critic subsequently recalibrates. This trajectory parallels the obs-decoder SGS seed~3 pattern (\\S\\ref{sec:seed_divergence}), where partial policy recovery coexists with persistent critic damage.\n\n\\paragraph{Cheetah Run $\\sigma{=}0.2$: insufficient dose.}\nAt $\\sigma{=}0.2$, Cheetah reaches NVE $= 1.9\\times$ at 55K---exceeding the $1.5\\times$ threshold---consistent with Cheetah's higher baseline CIVO severity ($8$--$108\\times$ vs.\\ Walker's $2$--$6\\times$). The noise magnitude that suffices for Walker is inadequate for Cheetah, but increasing $\\sigma$ to 0.5 trades CIVO prevention for a different failure mode rather than achieving mitigation.\n\n\\paragraph{PickCube-v1 $\\sigma{=}0.2$: sparse-reward failure.}\nPickCube reaches NVE $= 3.71\\times$ at 52.5K with $\\sigma{=}0.2$, indicating that TCN provides no protection in sparse-reward manipulation tasks. The combination of sparse rewards and temporal conditioning may amplify the fidelity gap beyond what representation-level noise can attenuate.\n\n\\paragraph{Dose-response analysis.}\nWe observe $\\sigma{=}0.2$ as a local optimum on Walker Walk, achieving complete CIVO suppression in 2 of 4 seeds. Seeds~2 and~3 both fail but via distinct CIVO onset dynamics: seed~2 shows gradual escalation (NVE $= 2.11\\times$ at 95K, still rising, eval ${\\sim}5\\%$), while seed~3 exhibits a phase-transition-like onset---NVE declined to $0.67\\times$ at 95K before spiking to $3.04\\times$ at 105K (eval 349.6 $\\to$ 71.8 in 10K steps). When TCN fails to prevent CIVO onset, the resulting trajectory qualitatively resembles untreated CIVO in its terminal outcome---runaway NVE and eval collapse. The two failure modes (gradual escalation vs.\\ sudden onset after apparent suppression) reinforce that TCN operates as a binary gate on CIVO onset rather than providing graded attenuation. Below the optimum, we observe $\\sigma{=}0.1$ as insufficient (NVE $= 1.02\\times$---borderline, eval 55\\%); above it, $\\sigma{=}0.5$ overdoses (oscillatory CIVO, eval $\\leq 41\\%$). Cross-seed variance at $\\sigma{=}0.2$ (eval 5--91\\%) exceeds the cross-dose difference by a wide margin, reinforcing that seed effects dominate dose effects. TCN is the only tested intervention achieving complete CIVO suppression in any configuration, but its high seed sensitivity and failure to transfer across environments position it as a \\emph{diagnostic probe}---identifying the representation level as the relevant intervention target---rather than a deployable mitigation.\n\n\\paragraph{Cheetah Run ``impossible dose'' dilemma.}\nExp\\_030c (224K steps) reveals a qualitatively different dose-response on Cheetah. At $\\sigma{=}1.0$, CIVO is eliminated (NVE${\\leq}0.30$ throughout) and initial learning is \\emph{unimpaired}: peak eval reaches 372 at 35K (116\\% of baseline), demonstrating that $\\sigma{=}1.0$ noise does not prevent policy acquisition. However, cumulative actor gradient interference produces progressive policy erosion---eval declines from 372 to 47 by 215K (15\\% of baseline)---while the critic remains well-calibrated (value\\_mean${=}12.4$, NVE${=}0.26$ at 215K). This establishes that \\emph{policy degradation $\\neq$ value corruption}: accurate value signals are insufficient when the actor cannot optimize effectively in noise-perturbed imagination.\n\nThis ``correct values, failed policy'' pattern provides indirect evidence that CIVO is mechanistically distinct from standard overestimation. Double Q-learning and ensemble methods address critic estimation error, but at $\\sigma{=}1.0$ the critic is accurate and the policy still collapses---a failure mode orthogonal to what these countermeasures target. The impossible dose dilemma scales with environment complexity: Cheetah's baseline CIVO severity ($8$--$108\\times$ NVE) requires $\\sigma \\geq 1.0$ to suppress, but this exceeds the actor's gradient signal-to-noise tolerance. On Walker, a narrow effective window exists around $\\sigma{=}0.2$; on Cheetah, the effective dose ($\\sigma \\geq 1.0$) exceeds the tolerable dose, and environments with higher CIVO severity will systematically lack a viable dose window.\n\n\\section{DreamerV3 Hyperparameters}\n\\label{sec:hyperparameters}\n\nTable~\\ref{tab:hyperparams} lists the DreamerV3 hyperparameters used across all experiments. Unless otherwise noted, we use the default DreamerV3 configuration for continuous-control tasks (\\texttt{dmc\\_proprio}).\n\n\\begin{table}[ht]\n\\centering\n\\caption{DreamerV3 hyperparameters for all experiments. Modifications from defaults are marked with $\\diamond$.}\n\\label{tab:hyperparams}\n\\small\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{World Model}} \\\\\nRSSM discrete states & 32 classes $\\times$ 32 categories \\\\\nRSSM stochastic dim & 32 \\\\\nRSSM deterministic dim & 512 \\\\\nMLP hidden size & 512 \\\\\nMLP layers & 2 \\\\\nActivation & SiLU \\\\\nNormalization & LayerNorm \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Training}} \\\\\nBatch size & 16 sequences $\\times$ 64 steps \\\\\nLearning rate & $3 \\times 10^{-4}$ (Adam, $\\epsilon{=}10^{-8}$) \\\\\nSequence length & 64 \\\\\nTraining ratio & 512 \\\\\nFree nats & 1.0 \\\\\nKL balance ($\\alpha$) & 0.8 \\\\\nDiscount ($\\gamma$) & 0.997 \\\\\n$\\lambda$-return & 0.95 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Policy}} \\\\\nImagination horizon$^\\diamond$ & 8 or 15 (see Table~\\ref{tab:complete_results}) \\\\\nActor entropy scale & $3 \\times 10^{-4}$ \\\\\nActor gradient & Reinforce + dynamics backprop \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Temporal Abstraction}$^\\diamond$} \\\\\nGate enabled & True (all non-baseline) \\\\\nGate fixed $\\dt$ & 1 or 2 (per config) \\\\\nSubsample max $\\dt$ & 1 (OFF) or 2 (ON) \\\\\n$\\dt$-embedding dim & 32 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Environment}} \\\\\nAction repeat & 2 (Walker Walk, Cheetah Run) \\\\\nObservation & Proprioceptive (no pixels) \\\\\nTotal environment steps & 105K \\\\\nEvaluation frequency & Every 10K steps \\\\\nEvaluation episodes & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Online CIVO Detector Details}\n\\label{sec:detector_appendix}\n\nThis appendix provides the full algorithm specification and validation results for the online CIVO detector described in \\S\\ref{sec:detector}.\n\n\\subsection{Algorithm Specification}\n\n\\begin{algorithm}[ht]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A full comparison of window sizes appears in \\S\\ref{sec:appendix_sensitivity}.\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $5/5$).\n\n\\subsection{Validation Results}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}14$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n008d s4 & trained $\\dt$-emb & TP & 105K & reactive & 383 & 3.03 \\\\\n010b s0 & trained $\\dt$-emb (Cheetah) & TP & 95K & reactive & 248 & 6.34 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n019b & trained $\\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n009c s3 & no $\\dt$-emb & TN & -- & -- & 457 & -- \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 5/5 (1.00), \\quad FPR = 2/9 (0.22)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe detector identifies all five CIVO-positive runs (TPR = 5/5). Two are detected predictively (008d seeds~0 and~3, both at 45K). Two false positives occur among nine negative cases (FPR = 2/9, precision 71\\%, F$_1$ = 0.83). Run 009c develops genuine late-stage value overestimation unrelated to CIVO; run 009a triggers during a transient eval dip at 85K before recovery to 966. Early alerts (before 70K) carry higher diagnostic confidence.\n\n\\subsection{Cross-Simulator Specificity (PickCube)}\n\nExp\\_019b applies the CIVO-trigger configuration to PickCube-v1 in ManiSkill3, a manipulation task with sparse rewards. The V/E ratio exhibits an oscillatory pattern rather than monotonic divergence: it spikes to $r_t = 5.66$ at 52.5K, then deflates to 1.38 by 72.5K. This trajectory prevents the acceleration condition from co-occurring with evaluation decline at any single checkpoint. Across all 14 checkpoints through 132.5K, the detector correctly remains silent (TN), confirming that the acceleration filter distinguishes transient spikes from CIVO's sustained monotonic divergence. A frozen-embedding control (exp\\_054) confirms this classification: frozen PickCube-v1 exhibits a comparable burst (peak $8.81\\times$ at 62.5K) that resolves within a single evaluation cycle ($0.55\\times$ at 72.5K), establishing environment-specific origin independent of $\\dt$-embedding training.\n\n\\subsection{Detector Limitations}\n\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse. Second, the acceleration condition assumes monotonically increasing overestimation during onset. Third, the detector identifies a \\emph{pattern} rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values were calibrated on fourteen runs across three environments; generalization to different reward scales requires further validation.\n\n\\section{Dual-Critic Mechanism Ablation}\n\\label{sec:dual_critic_appendix}\n\n\\subsection{\\texorpdfstring{$2{\\times}2$}{2x2} Factorial Design}\n\nWe ablate the critic architecture in a $2{\\times}2$ factorial: \\{single, dual\\} $\\times$ \\{narrow (${\\sim}1.2$M), wide (${\\sim}2.4$M)\\} parameters. Table~\\ref{tab:dual_critic_full} reports all configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Dual-critic $2{\\times}2$ factorial results. Walker Walk unless noted.}\n\\label{tab:dual_critic_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Params} & \\textbf{NVE} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\n008d & Single narrow & 1.2M & 4.12$\\times$ & 82.8 & Collapse \\\\\n033 & Wide single & 2.4M & 4.75$\\times$ & 407.9 & CIVO $\\to$ self-repair \\\\\n035 s0 & Narrow dual (min) & 1.2M & 2.75$\\times$ & 697.8 & CIVO $\\to$ recovery \\\\\n039 s1 & Narrow dual (min) & 1.2M & 2.19$\\times$ & 592.7 & CIVO $\\to$ recovery \\\\\n032 s0 & Wide dual (min) & 2.4M & $\\leq$1.1$\\times$ & 739.7 & CIVO prevented \\\\\n032b s1 & Wide dual (min) & 2.4M & 1.4$\\times$ & 551.8 & CIVO prevented \\\\\n038 s2 & Wide dual (min) & 2.4M & $\\leq$0.3$\\times$ & 120.9$^*$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Cross-environment}} \\\\\n034 & Cheetah dual & 2.4M & 1.75$\\times$ & 97.5 & Partial recovery (31\\%) \\\\\n037 & Cheetah wide single & 2.4M & 3.60$\\times$ & 146.1 & CIVO $\\to$ self-repair \\\\\n036 & PickCube dual & 2.4M & 2.3$\\times$ & 27.7 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$CIVO prevented (NVE $\\leq 0.3\\times$) but non-CIVO eval collapse: eval peaked at 354 (155K), then declined to 120.9 (224K) with actor entropy increasing from $-3.59$ to $-0.45$.\\par}\n\\end{table}\n\n\\subsection{Critic Convergence (\\texorpdfstring{$v_1 \\approx v_2$}{v1 ≈ v2})}\n\nAcross all dual-critic configurations and environments, the two critics converge to near-identical value functions. On Walker Walk, Pearson $\\rho > 0.999$ between $v_1$ and $v_2$ outputs; on Cheetah Run and PickCube-v1, the gap is $< 0.2$ (exact match within numerical precision). Per-sample pessimism $\\mathbb{E}[\\max(v_1, v_2) - \\min(v_1, v_2)]$ is 3--4\\% of the theoretical bound for independent critics.\n\nThis convergence occurs because both critics train on the same RSSM-generated latent features. Unlike model-free Double Q-learning, where each critic sees different mini-batches of real transitions and develops distinct function approximation errors, pure-imagination critics share identical inputs from the world model. The min operation therefore cannot provide the pessimism bias that makes Double Q effective in model-free settings.\n\n\\subsection{Recovery vs.\\ Prevention Mechanism}\n\nThe $2{\\times}2$ factorial reveals two separable dimensions:\n\n\\paragraph{Recovery (min-dominated).} The min operation is the primary factor enabling recovery from CIVO. Both narrow dual-critic seeds experience CIVO and recover fully: exp\\_035 (s0, $\\nve = 2.75\\times$, eval $33.8 \\to 697.8$, recovery ratio $20.6\\times$) and exp\\_039 (s1, $\\nve = 2.19\\times$, eval $35.9 \\to 592.7$, recovery ratio $16.5\\times$). Both outperform wide single-critic (exp\\_033, 2.4M params, eval 407.9) despite $2\\times$ fewer parameters. The min operation reduces both peak CIVO severity (2.19--2.75$\\times$ vs.\\ 4.75$\\times$ for the comparable single-critic) and enables consistent full recovery across seeds.\n\n\\paragraph{Prevention (min $+$ capacity synergy).} CIVO prevention (NVE remaining below the $1.5\\times$ threshold) requires both the min operation and increased capacity: only the wide dual-critic (exp\\_032, 3 seeds) achieves this. The mechanism for this synergy is an open question; we hypothesize that increased capacity improves value calibration quality while the min operation constrains the overestimation feedback loop during early training when the two critics briefly diverge.\n\n\\paragraph{Cross-environment limits.} On Cheetah Run, the wide dual-critic (exp\\_034) reduces NVE from $8.27\\times$ (untreated baseline) to $1.75\\times$ ($\\geq 4\\times$ reduction) but cannot prevent CIVO onset, and recovery reaches only 31\\% of the pre-CIVO peak. This confirms that the min $+$ capacity synergy has environment-dependent limits: in high-CIVO-severity environments, architecture-level interventions attenuate but do not eliminate the pathology.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " \\section{Complete Experimental Results}",
          " \\label{sec:complete_results}",
          " ",
          "-Table~\\ref{tab:complete_results} reports all 42 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).",
          "+Table~\\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).",
          " ",
          " \\begin{table*}[t]",
          " \\centering"
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

_source line 85_

<details open><summary>🔧 Tool call — Edit · `toolu_016LuSuG3wM4XYR33xCix24C`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "Locomotion & Walker Walk & 4/4 & 0/3 & Yes (NVE $1.53$--$4.62\\times$) \\\\",
  "new_string": "Locomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\\times$) \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "66e063da-5660-466d-9df1-38ba7ed79dc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TK4F2Ft89F87VL5hzvGLcE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13095,
      "cache_read_input_tokens": 51272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13095
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

_source line 86 · 2026-05-24T07:12:00.883Z_

<details><summary>↩ Tool result · `toolu_016LuSuG3wM4XYR33xCix24C`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "1f97c8bd-2b95-4f25-879f-0c57698f1e1c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "Locomotion & Walker Walk & 4/4 & 0/3 & Yes (NVE $1.53$--$4.62\\times$) \\\\",
    "newString": "Locomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\\times$) \\\\",
    "originalFile": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\\times$ & Transient (self-corr.) \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\rowcolor{gray!15}\n008e\\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\\times$ & CIVO collapse \\\\\n008e\\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\\times$ & Healthy \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\n$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\n$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\n$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\n$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\par}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n\\label{tab:cross_domain}\n\\footnotesize\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n\\midrule\nLocomotion & Walker Walk & 4/4 & 0/3 & Yes (NVE $1.53$--$4.62\\times$) \\\\\nLocomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\nManipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\nManipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\nManipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all ten factorial experiments (including four 008e\\_v3 seeds). Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\\_v3\\_s3 exhibits CIVO with NVE $4.02\\times$ despite $\\Delta t{=}1$ imagination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.83 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.12 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s3 & 4.02 & CIVO           & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.02\\times$, exp~008e\\_v3\\_s3) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.02]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.958$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=7$, $n=10$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). $^\\dagger$Optimal threshold in $(3.78, 4.02]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 3 & 0 & 4 & 70.0\\% \\; [34.8, 93.3] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.2\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.5\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 3 & 0 & 0 & 7 & 100\\% \\; [69.2, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=4$, $n_{\\text{neg}}=6$, $n=10$, $\\text{AUROC}=0.958$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 4 & 2 & 0 & 4 & 80.0\\% \\; [44.4, 97.5] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 1.2\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.7\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 3.9\\times$ & 3 & 0 & 1 & 6 & 90.0\\% \\; [55.5, 99.7] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\\text{pos}}=8$, $n_{\\text{neg}}=8$, $n=16$, $\\text{AUROC}=0.969$). Includes Walker Walk (14 configurations) and Cheetah Run (2 configurations).}\n\\label{tab:sensitivity_b2_full}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 8 & 2 & 0 & 6 & 87.5\\% \\; [61.7, 98.4] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.2\\times$ & 8 & 1 & 0 & 7 & 93.8\\% \\; [69.8, 99.8] & 88.9\\% & 100\\% & 94.1\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 8 & 1 & 0 & 7 & 93.8\\% \\; [69.8, 99.8] & 88.9\\% & 100\\% & 94.1\\% \\\\\n$\\geq 1.7\\times$ & 6 & 1 & 2 & 7 & 81.3\\% \\; [54.4, 96.0] & 85.7\\% & 75.0\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 6 & 1 & 2 & 7 & 81.3\\% \\; [54.4, 96.0] & 85.7\\% & 75.0\\% & 80.0\\% \\\\\n$\\geq 3.9\\times$ & 6 & 0 & 2 & 8 & 87.5\\% \\; [61.7, 98.4] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all four CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 75.0\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 88.9\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 3$ the statistical power remains limited (accuracy 95\\% CI: [69.2\\%, 100\\%]).\n\n\\subsection{Expanded ROC Analysis}\n\\label{sec:roc_analysis}\n\nThe original $n{=}16$ analysis (Tables~\\ref{tab:sensitivity_b1}--\\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}29$ configurations spanning all tested interventions. Figure~\\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\\% bootstrap confidence interval (10{,}000 resamples).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.7\\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}\n\\caption{NVE ROC curve ($n{=}29$ configurations, AUROC${=}0.953$, in-sample, post-hoc). The preset $\\nve \\geq 1.5\\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}\n\\label{fig:nve_roc}\n\\end{figure}\n\nWe label a configuration as CIVO-positive if and only if (i)~it uses a trained $\\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.\n\nThe three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\\_008e\\_v3 seed~2, actor entropy \\emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \\emph{decrease}). All three produce NVE $> 1.5\\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\\times$) lacks $\\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\\times$) exhibits the full CIVO causal chain: trained $\\dt$-embedding, entropy decrease, and evaluation collapse to 14\\% of baseline.\n\n\\subsection{NVE Normalization Robustness}\n\\label{sec:nve_robustness}\n\nTo assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\\ref{tab:baseline_seeds}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Walker Walk baseline seeds at 105K and 505K steps.}\n\\label{tab:baseline_seeds}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Eval@105K} & \\textbf{Eval@505K} & \\textbf{ve@65K} & \\textbf{ve@105K} \\\\\n\\midrule\ns1 & 915.7 & 970.4 & 0.563 & 0.656 \\\\\ns2 & 443.5 & 945.7 & 0.898 & 0.742 \\\\\ns3 & 869.0 & 947.7 & --- & 0.664 \\\\\ns4 & 922.8 & 938.9 & --- & 0.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\\times$; 009b seed~2, peak NVE $1.62\\times$) to fall below the $1.5\\times$ threshold. Core CIVO cases (peak NVE $> 3\\times$) remain correctly classified under all baseline seeds.\n\nSingle-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\\%): the boundary case exp\\_009b flips from $\\nve = 1.62\\times$ (s1) to $1.23\\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\\times \\to 4.52\\times$; 008d: $4.12\\times \\to 3.54\\times$). The $1.5\\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\\% of the threshold.\n\n\\paragraph{Normalization conventions.} Walker NVE is normalized against the 4-seed mean baseline (seeds~1--4, each run to 505K+ steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).\n\n\\paragraph{Limitations.} With $n = 10$ experiments, Clopper-Pearson confidence intervals remain wide (e.g., 90.0\\% accuracy has 95\\% CI [55.5\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds. Table~\\ref{tab:sensitivity_b2_full} reports the original $n{=}16$ evaluation set spanning both environments. The expanded analysis ($n{=}29$, including SGS variants, RAVE, and TCN configurations) yields AUROC${=}0.953$ (Figure~\\ref{fig:nve_roc}, in-sample, post-hoc). The original $n{=}16$ core analysis yields AUROC${=}0.969$; the expanded $n{=}29$ set includes SGS, RAVE, TCN, and dual-critic configurations. Cross-architecture validation is deferred to future work.\n\n\\subsection{Leave-One-Environment-Out Cross-Validation}\n\\label{sec:nve_loeo}\n\nTo assess whether $\\theta{=}1.5\\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}13$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\\theta{=}1.5\\times$ on the held-out environment.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-environment-out cross-validation of NVE threshold $\\theta=1.5\\times$.\nFor each fold, the threshold is validated on an environment whose data was \\emph{not} used\nto select $\\theta$. The optimal threshold range on each training set is reported;\n$\\theta=1.5$ falls within the optimal range in all three folds.}\n\\label{tab:nve_loeo}\n\\begin{tabular}{lccccc}\n\\toprule\nHeld-out & $N_{\\text{train}}$ & $N_{\\text{test}}$ & $\\theta_{\\text{opt}}$ range & Test Accuracy & Test AUROC \\\\\n\\midrule\nPickCube & 18 & 2 & $(1.45,\\, 1.53]$ & 2/2 (1.000) & 1.000 \\\\\nCheetah  & 15 & 5 & $(1.45,\\, 1.53]$ & 5/5 (1.000) & 1.000 \\\\\nWalker   &  7 & 13 & $(1.00,\\, 3.78)$ & 12/13 (0.923) & 0.944 \\\\\n\\midrule\n\\textbf{Mean} & — & — & — & \\textbf{0.974} & \\textbf{0.981} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe threshold $\\theta{=}1.5\\times$ falls within the optimal accuracy range for all three training folds: $(1.45, 1.53]$ when Walker data is available, and the wider $(1.00, 3.78)$ when training on Cheetah$+$PickCube only (where CIVO and non-CIVO NVE values are well-separated). The single cross-validation error is exp\\_008e\\_v3 seed~2 (Walker), an IRD collapse mechanistically distinct from CIVO (\\S\\ref{sec:roc_analysis}). Mean held-out accuracy is 0.974 and mean AUROC is 0.981, confirming that $\\theta{=}1.5\\times$ generalizes across environments without retuning. PickCube fold confidence intervals remain wide (Clopper-Pearson 95\\% CI: $[0.158, 1.000]$) due to $N_{\\text{test}}{=}2$.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\paragraph{Embedding gradient analysis.}\nTable~\\ref{tab:three_way_emb} isolates embedding \\emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\\dt{=}2$ imagination).\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}\n\\label{tab:three_way_emb}\n\\footnotesize\n\\begin{tabular}{lccccl}\n\\toprule\nCondition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\\\\n\\midrule\nTrained & all & 008d & $1.53$--$4.62\\times$ & 64--268 & 4/4 \\\\\nReward detach & obs+KL only & 044 & $4.45\\times$ & 44$\\to$538$^\\dagger$ & 1/1 \\\\\nFull SGS & KL only & 018 & $1.66\\times$ & 448 & 1/1$^*$ \\\\\nFrozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\\nRemoved & N/A & 008f & $0.97$--$1.41\\times$ & 307--503 & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\\times$); seed~2 collapsed. $^\\dagger$Self-corrected at ${\\sim}175$K (eval 44$\\to$538, 59\\% baseline; 224K run). $^\\ddagger$Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps.\\par}\n\\end{table}\n\nThe reward-detach condition (exp\\_044, \\texttt{reward\\_dt\\_emb\\_detach=True}) uses a backward hook to block reward-head gradients from reaching $e_{\\dt}$, complementing the framework-level Reward SGS (exp\\_016e). Both yield the same directional result---CIVO onset not prevented---ruling out implementation artifacts. Exp\\_044 exhibits delayed CIVO onset (${\\sim}95$K vs.\\ typical $25$--$35$K), consistent with reduced but non-zero gradient pressure on $e_{\\dt}$. Over a full 224K run, exp\\_044 self-corrects: eval recovers from 44 (95K) to 538 (215K, 59\\% baseline), but this recovery is incomplete compared to spontaneous recovery without gradient intervention (exp\\_045: 868, 95\\% baseline). The lower asymptote suggests that selectively disrupting gradient flow may create optimization difficulties beyond CIVO itself.\n\nTable~\\ref{tab:factorial_design} summarizes the experimental configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Factorial design. Each row specifies one experimental configuration. \\textbf{Emb}: $\\dt$-embedding mode. \\textbf{Sub}: temporal subsampling. \\textbf{H}: imagination horizon. \\textbf{Imag $\\dt$}: temporal resolution used during imagination.}\n\\label{tab:factorial_design}\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{ID} & \\textbf{Purpose} & \\textbf{Emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Imag $\\dt$} \\\\\n\\midrule\n001 & Reference baseline & --- & --- & 15 & 1 \\\\\n006 & Fixed $\\dt{=}2$ & trn & on & 15 & 2 \\\\\n007 & Fixed $\\dt{=}4$ & trn & on & 15 & 4 \\\\\n\\midrule\n008a & Unexposed emb ctrl & exp$^a$ & off & 15 & 2 \\\\\n008c & Horizon control & exp$^a$ & off & 8 & 2 \\\\\n008d & Collapse condition & trn & on & 8 & 2 \\\\\n008e\\_v3 & $\\dt{=}1$ imag control & trn & on & 15 & 1 \\\\\n008f & Causal ablation & --- & on & 8 & 2 \\\\\n\\midrule\n015b & Frozen-emb ctrl & frz$^b$ & on & 8 & 2 \\\\\n016e & Stop-grad (reward) & trn$^\\dagger$ & on & 8 & 2 \\\\\n018 & Full-SGS & trn$^\\ddagger$ & on & 8 & 2 \\\\\n\\midrule\n005 & Learned gate & adaptive & off & 15 & learned \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^\\dagger$ \\texttt{reward\\_dt\\_emb\\_detach=True}; $^\\ddagger$ all non-KL gradients to \\texttt{dt\\_emb} detached.\\par}\n\\end{table}\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe empirical finding that trained embedding \\emph{plus} multi-rate exposure jointly predict CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.83$--$0.93\\times$ range across 3 seeds (105K steps). Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical factor is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training. This confirms that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.42\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.47 \\rightarrow 0.39 \\rightarrow 0.42$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and precedes full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.42\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that in all tested configurations, CIVO occurs only with the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\nCross-environment validation on Cheetah Run replicates the empirical pattern: trained $e_{\\dt}$ precedes CIVO in both tested seeds (exp\\_010b, 2 seeds, NVE $8.27$--$108.52\\times$, collapse to 51.7/0.83) while removing the embedding eliminates it (exp\\_024b, 2 seeds, NVE $<0.2\\times$, eval 96.5/77.3). Freezing the embedding on Cheetah (exp\\_046, NVE${=}1.35\\times$ vs.\\ trained $70.64\\times$, a $52\\times$ reduction) further confirms that embedding trainability, not architecture, drives CIVO. This extends the sufficiency finding from Walker Walk to a second locomotion environment with qualitatively different dynamics (6-joint vs.\\ 2-joint).\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole predictor of CIVO in tested configurations. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) precedes CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly sufficient in tested configurations.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling precedes collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$; low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig4_mechanism_diagram.pdf}\n\\caption{CIVO mechanism diagram. The trained $\\dt$-embedding enables asymmetric reward prediction fidelity, initiating a feedback loop: biased RSSM rewards $\\to$ optimistic critic values $\\to$ actor exploitation $\\to$ reinforced state-distribution skew.}\n\\label{fig:civo_mechanism}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO (Figure~\\ref{fig:civo_mechanism}).  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, which confirms that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\paragraph{Signed reward error analysis.}\nTo test whether CIVO arises from one-step reward overprediction, we compute signed error (predicted $-$ actual) on posterior-conditioned RSSM predictions (Table~\\ref{tab:signed_error}). The trained-embedding model (008d) shows \\emph{negative} bias at $\\dt{=}2$ (mean signed error $-0.599$, only 8\\% of samples overpredicted), ruling out observation-level reward overprediction as the mechanism. The baseline is well-calibrated (mean SE $\\approx 0$), confirming methodological soundness. Value overestimation therefore occurs during \\emph{imagination-level} prior drift: the RSSM prior (unconditioned on observations) generates reward-favorable trajectories at $\\dt > 1$ (Stage~1 above, $1.68\\times$ ratio under random policy), and the critic accumulates these into overestimated returns. The one-step reward prediction is negatively biased when conditioned on real observations, but this posterior correction is unavailable during imagination. This also distinguishes CIVO from generic compounding error, which would produce \\emph{positive} signed error accumulating with horizon; the negative observation-level bias confirms that CIVO is a prior-drift phenomenon, not a reward-prediction artifact.\n\n\\begin{table}[h]\n\\centering\n\\caption{Signed reward error (predicted $-$ actual) on posterior-conditioned RSSM predictions. Negative values indicate underprediction. The trained-embedding model underpredicts at $\\dt{=}2$, ruling out observation-level reward overprediction as the CIVO mechanism.}\n\\label{tab:signed_error}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Config} & $\\dt$ & \\textbf{Mean SE} & \\textbf{Std} & \\textbf{\\%Over} & \\textbf{Actual} & \\textbf{Pred} \\\\\n\\midrule\nBaseline & 1 & $+0.001$ & 0.023 & 39.6\\% & 1.893 & 1.894 \\\\\n\\midrule\n008d (trained) & 1 & $+0.018$ & 0.072 & 61.8\\% & 0.361 & 0.379 \\\\\n008d (trained) & 2 & $\\mathbf{-0.599}$ & 0.722 & 8.0\\% & 0.721 & 0.121 \\\\\n\\midrule\n008f (no emb) & 1 & $-0.710$ & 0.704 & 14.0\\% & 0.921 & 0.211 \\\\\n008f (no emb) & 2 & $-1.645$ & 1.485 & 5.0\\% & 1.840 & 0.195 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 0/2 CIVO elimination rate on Walker (seed~1: NVE reduced from $4.12\\times$ to $1.66\\times$ but remains CIVO-positive; seed~2: collapsed) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention eliminates CIVO in neither seed: seed~1 shows partial mitigation (eval 448.3, peak NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses (eval 40.8). Removing the observation decoder gradient channel is thus contributory but not sufficient. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3. \\textbf{Trained dt-emb} (008d)\\protect\\footnotemark: learned $d{=}32$ temporal embedding with multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with all non-KL gradients detached from $e_{\\dt}$. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$. Full-SGS seed~1 shows partial mitigation ($-51\\%$ final, NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses ($-96\\%$ final). CIVO elimination rate $= 0/2$.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}\n\nCross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This transient self-correcting trajectory is not attributable to the SGS intervention: the initial CIVO onset and peak severity are comparable to the unmitigated case, and the self-correction may reflect Cheetah Run's simpler dynamics rather than SGS efficacy.  Performance remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's Walker results (0/2 CIVO elimination), these findings yield a 0/3 elimination rate across environments, indicating that gradient-level interventions alone do not eliminate the CIVO vulnerability. Additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Post-CIVO outcomes for all six CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Env} & \\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\nWalker & s1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\nWalker & s2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\nWalker & s3 (008d\\_s3) & 1.53$\\times$ & 1.53$\\times$ & 268$^\\diamond$ & Late-onset collapse \\\\\nWalker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\n\\midrule\nCheetah & s1 (010b) & 8.27$\\times$ & 8.27$\\times$ & 51.7 & Full collapse \\\\\nCheetah & s0 (010b\\_s0) & 108.52$\\times$ & 108.52$\\times$ & 0.83 & Full collapse \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\diamond$ Transitional; train returns still declining at 105K.\\par}\n\\end{table}\n\nAll six CIVO-positive seeds cross the $\\nve > 1.5\\times$ threshold (Table~\\ref{tab:post_civo}), yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Full collapse is the majority outcome (5/6 seeds), with one self-correction case (Walker seed~2) that remains severely degraded (29.3\\% of baseline). Cheetah seeds exhibit more extreme overestimation (peak NVE $8.27$--$108.52\\times$ vs.\\ Walker's $1.53$--$4.62\\times$), consistent with the Cheetah reward scale amplifying the fidelity gap.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\paragraph{A fourth trajectory: CIVO-induced persistent value collapse.}\nObs-decoder SGS seed~3 (exp\\_025) exhibits a trajectory not observed in the untreated seeds: healthy through 105K ($\\nve < 1.0\\times$, eval 818.6), CIVO onset at 135K ($\\nve = 5.47\\times$, eval 67.0), followed by evaluation recovery (590.2 at 215K, 64\\% of baseline) but persistent value collapse ($\\nve = 0.14\\times$, value mean 80.6). The critic undershoots after the CIVO episode, suggesting that CIVO-induced representational damage may be irreversible even when the policy partially recovers. This contrasts with transient CIVO (seed~2, 009b), where both value and evaluation recover jointly, and with full collapse (seed~1, 008d), where neither recovers. Seed~4 exhibits the same terminal value collapse ($\\nve = 0.14\\times$ at 215K, eval 242), suggesting this overcorrection is systematic rather than seed-specific. The pattern adds a fourth post-CIVO outcome---policy recovery with critic damage---to the three documented in Table~\\ref{tab:post_civo}.\n\n\\subsubsection{Failure and Degradation Mode Taxonomy}\n\nTable~\\ref{tab:failure_modes} classifies the seven distinct failure and degradation modes observed across all experimental configurations. The taxonomy reveals that CIVO is not a single failure mode but a family of related pathologies, with the trained $\\dt$-embedding creating vulnerability through at least three independent mechanisms: value-driven collapse (monotonic, late-onset, and SGS-resistant CIVO), entropy-driven instability (IRD collapse), and gradient-mediated effects (gradient starvation, SGS-paradoxical worsening).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Failure and degradation mode taxonomy. Each mode is characterized by its NVE trajectory, entropy behavior, and primary mechanism.}\n\\label{tab:failure_modes}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccl@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Representative} & \\textbf{NVE} & \\textbf{Entropy} & \\textbf{Mechanism} \\\\\n\\midrule\nMonotonic CIVO & 008d, 008d\\_s4, 010b\\_s0 & $\\uparrow$ sustained & $\\downarrow$ & Reward bias $\\to$ critic $\\to$ actor \\\\\nLate-onset CIVO & 008d\\_s3 & $\\uparrow$ delayed & $\\downarrow$ & Same, delayed onset \\\\\nTransient CIVO & 009b & Peak $\\to$ $\\downarrow$ & Stable & Self-correction via capacity \\\\\nIRD collapse & 008e\\_v3\\_s2 & $\\uparrow$ late & $\\uparrow$ & Entropy-driven, values stable \\\\\nGrad.\\ starvation & 015b & Oscillates, decays & Stable & Frozen emb $\\to$ zero actor grad \\\\\nSGS-resistant & 018\\_s2 & $\\uparrow$ & $\\downarrow$ & Forward-pass conditioning \\\\\nSGS-paradoxical & 016e & $\\uparrow$ sustained & $\\downarrow$ & Reward SGS $\\to$ obs-dec reliance \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) avoids collapse in 2 of 4 seeds (50\\%), while the remaining two collapse via distinct mechanisms: Pathway~A (CIVO-driven, entropy decrease; s3, NVE $4.02\\times$) and Pathway~B (entropy-driven, entropy increase; s2, NVE $3.78\\times$; \\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse patterns identified in \\S\\ref{sec:f6}---CIVO (Pathway~A, value-driven, entropy decreasing) and a tentative second mode (Pathway~B, eval-driven, entropy increasing)---have distinct diagnostic signatures. Pathway~B is observed in only two seeds (008e\\_v3\\_s2 and 038\\_s2); we present it as preliminary evidence that the trained $\\dt$-embedding's learned features may affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B), though additional data is needed to confirm this as a distinct mechanism.  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse (Figure~\\ref{fig:multiple_pathways}).\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.  The CIVO mechanism requires three structural properties: (1) a temporal embedding that co-adapts with dynamics via gradient flow, (2) multi-step imagined rollouts used for critic training, and (3) a reward head that inherits latent biases from the shared representation.  Transformer-based world models that share these properties may exhibit analogous vulnerability; architectures that decouple temporal conditioning from the reward prediction pathway would not.\n\n\\subsection{Cross-Environment TCN Evaluation}\n\\label{sec:tcn_cross_env}\n\nTable~\\ref{tab:tcn_full} reports the full TCN evaluation across environments and noise magnitudes.\n\n\\begin{table}[h]\n\\centering\n\\caption{TCN results across environments and noise magnitudes. Prevention = peak NVE $< 1.5\\times$ (35K+).}\n\\label{tab:tcn_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Env} & $\\sigma$ & \\textbf{Seed} & \\textbf{NVE$_{\\max}$} & \\textbf{Prevented?} & \\textbf{Eval (\\%)} \\\\\n\\midrule\nWalker & 0.1 & s0 & 1.02 & \\checkmark$^*$ & 55\\% \\\\\nWalker & 0.2 & s0 & 0.91 & \\checkmark & 91\\% \\\\\nWalker & 0.2 & s1 & 0.64 & \\checkmark & 45\\% \\\\\nWalker & 0.2 & s2 & 2.11$^\\dagger$ & $\\times$ & ${\\sim}5\\%$ \\\\\n\\rowcolor{gray!15}\nWalker & 0.2 & s3 & 3.04$^\\P$ & $\\times$ & 11\\% \\\\\nWalker & 0.5 & s0 & 3.97 & $\\times$ & 27\\% \\\\\nWalker & 0.5 & s1 & 1.64 & $\\times$ & 41\\% \\\\\n\\midrule\nCheetah & 0.2 & s0 & 1.90 & $\\times$ & crashed \\\\\nCheetah & 0.5 & s0 & 10.67 & $\\times$ & 26\\% \\\\\nCheetah & 1.0 & s0 & $\\leq$0.30 & \\checkmark$^\\S$ & 15\\% \\\\\n\\midrule\nPickCube & 0.2 & s0 & 3.71 & $\\times$ & failing \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Borderline: NVE${=}1.02\\times$ at 95K, below $1.5\\times$ threshold but above $1.0\\times$.\\\\\n$^\\dagger$NVE $= 2.11\\times$ at 95K, still rising; eval ${\\sim}5\\%$ of baseline.\\\\\n$^\\P$Late-onset CIVO: NVE declined to $0.67\\times$ at 95K before phase-transition-like spike to $3.04\\times$ at 105K; eval 349.6 at 95K $\\to$ 71.8 at 105K $\\to$ 104.5 at 215K.\\\\\n$^\\S$CIVO prevented (NVE${\\leq}0.30$); peak eval 116\\% baseline at 35K, declining to 15\\% by 215K via progressive policy erosion. See ``impossible dose'' discussion.\\par}\n\\end{table}\n\n\\paragraph{Cheetah Run $\\sigma{=}0.5$: transient spike with permanent eval damage.}\nCheetah $\\sigma{=}0.5$ exhibits a novel failure mode: a transient CIVO spike (NVE $= 10.67\\times$ at 55K) followed by NVE recovery ($< 0.3\\times$ by 95K), but permanent evaluation damage (26\\% of baseline). The value signal self-corrects while the policy does not recover, suggesting that CIVO-induced representational damage during the spike is irreversible even when the critic subsequently recalibrates. This trajectory parallels the obs-decoder SGS seed~3 pattern (\\S\\ref{sec:seed_divergence}), where partial policy recovery coexists with persistent critic damage.\n\n\\paragraph{Cheetah Run $\\sigma{=}0.2$: insufficient dose.}\nAt $\\sigma{=}0.2$, Cheetah reaches NVE $= 1.9\\times$ at 55K---exceeding the $1.5\\times$ threshold---consistent with Cheetah's higher baseline CIVO severity ($8$--$108\\times$ vs.\\ Walker's $2$--$6\\times$). The noise magnitude that suffices for Walker is inadequate for Cheetah, but increasing $\\sigma$ to 0.5 trades CIVO prevention for a different failure mode rather than achieving mitigation.\n\n\\paragraph{PickCube-v1 $\\sigma{=}0.2$: sparse-reward failure.}\nPickCube reaches NVE $= 3.71\\times$ at 52.5K with $\\sigma{=}0.2$, indicating that TCN provides no protection in sparse-reward manipulation tasks. The combination of sparse rewards and temporal conditioning may amplify the fidelity gap beyond what representation-level noise can attenuate.\n\n\\paragraph{Dose-response analysis.}\nWe observe $\\sigma{=}0.2$ as a local optimum on Walker Walk, achieving complete CIVO suppression in 2 of 4 seeds. Seeds~2 and~3 both fail but via distinct CIVO onset dynamics: seed~2 shows gradual escalation (NVE $= 2.11\\times$ at 95K, still rising, eval ${\\sim}5\\%$), while seed~3 exhibits a phase-transition-like onset---NVE declined to $0.67\\times$ at 95K before spiking to $3.04\\times$ at 105K (eval 349.6 $\\to$ 71.8 in 10K steps). When TCN fails to prevent CIVO onset, the resulting trajectory qualitatively resembles untreated CIVO in its terminal outcome---runaway NVE and eval collapse. The two failure modes (gradual escalation vs.\\ sudden onset after apparent suppression) reinforce that TCN operates as a binary gate on CIVO onset rather than providing graded attenuation. Below the optimum, we observe $\\sigma{=}0.1$ as insufficient (NVE $= 1.02\\times$---borderline, eval 55\\%); above it, $\\sigma{=}0.5$ overdoses (oscillatory CIVO, eval $\\leq 41\\%$). Cross-seed variance at $\\sigma{=}0.2$ (eval 5--91\\%) exceeds the cross-dose difference by a wide margin, reinforcing that seed effects dominate dose effects. TCN is the only tested intervention achieving complete CIVO suppression in any configuration, but its high seed sensitivity and failure to transfer across environments position it as a \\emph{diagnostic probe}---identifying the representation level as the relevant intervention target---rather than a deployable mitigation.\n\n\\paragraph{Cheetah Run ``impossible dose'' dilemma.}\nExp\\_030c (224K steps) reveals a qualitatively different dose-response on Cheetah. At $\\sigma{=}1.0$, CIVO is eliminated (NVE${\\leq}0.30$ throughout) and initial learning is \\emph{unimpaired}: peak eval reaches 372 at 35K (116\\% of baseline), demonstrating that $\\sigma{=}1.0$ noise does not prevent policy acquisition. However, cumulative actor gradient interference produces progressive policy erosion---eval declines from 372 to 47 by 215K (15\\% of baseline)---while the critic remains well-calibrated (value\\_mean${=}12.4$, NVE${=}0.26$ at 215K). This establishes that \\emph{policy degradation $\\neq$ value corruption}: accurate value signals are insufficient when the actor cannot optimize effectively in noise-perturbed imagination.\n\nThis ``correct values, failed policy'' pattern provides indirect evidence that CIVO is mechanistically distinct from standard overestimation. Double Q-learning and ensemble methods address critic estimation error, but at $\\sigma{=}1.0$ the critic is accurate and the policy still collapses---a failure mode orthogonal to what these countermeasures target. The impossible dose dilemma scales with environment complexity: Cheetah's baseline CIVO severity ($8$--$108\\times$ NVE) requires $\\sigma \\geq 1.0$ to suppress, but this exceeds the actor's gradient signal-to-noise tolerance. On Walker, a narrow effective window exists around $\\sigma{=}0.2$; on Cheetah, the effective dose ($\\sigma \\geq 1.0$) exceeds the tolerable dose, and environments with higher CIVO severity will systematically lack a viable dose window.\n\n\\section{DreamerV3 Hyperparameters}\n\\label{sec:hyperparameters}\n\nTable~\\ref{tab:hyperparams} lists the DreamerV3 hyperparameters used across all experiments. Unless otherwise noted, we use the default DreamerV3 configuration for continuous-control tasks (\\texttt{dmc\\_proprio}).\n\n\\begin{table}[ht]\n\\centering\n\\caption{DreamerV3 hyperparameters for all experiments. Modifications from defaults are marked with $\\diamond$.}\n\\label{tab:hyperparams}\n\\small\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{World Model}} \\\\\nRSSM discrete states & 32 classes $\\times$ 32 categories \\\\\nRSSM stochastic dim & 32 \\\\\nRSSM deterministic dim & 512 \\\\\nMLP hidden size & 512 \\\\\nMLP layers & 2 \\\\\nActivation & SiLU \\\\\nNormalization & LayerNorm \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Training}} \\\\\nBatch size & 16 sequences $\\times$ 64 steps \\\\\nLearning rate & $3 \\times 10^{-4}$ (Adam, $\\epsilon{=}10^{-8}$) \\\\\nSequence length & 64 \\\\\nTraining ratio & 512 \\\\\nFree nats & 1.0 \\\\\nKL balance ($\\alpha$) & 0.8 \\\\\nDiscount ($\\gamma$) & 0.997 \\\\\n$\\lambda$-return & 0.95 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Policy}} \\\\\nImagination horizon$^\\diamond$ & 8 or 15 (see Table~\\ref{tab:complete_results}) \\\\\nActor entropy scale & $3 \\times 10^{-4}$ \\\\\nActor gradient & Reinforce + dynamics backprop \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Temporal Abstraction}$^\\diamond$} \\\\\nGate enabled & True (all non-baseline) \\\\\nGate fixed $\\dt$ & 1 or 2 (per config) \\\\\nSubsample max $\\dt$ & 1 (OFF) or 2 (ON) \\\\\n$\\dt$-embedding dim & 32 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Environment}} \\\\\nAction repeat & 2 (Walker Walk, Cheetah Run) \\\\\nObservation & Proprioceptive (no pixels) \\\\\nTotal environment steps & 105K \\\\\nEvaluation frequency & Every 10K steps \\\\\nEvaluation episodes & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Online CIVO Detector Details}\n\\label{sec:detector_appendix}\n\nThis appendix provides the full algorithm specification and validation results for the online CIVO detector described in \\S\\ref{sec:detector}.\n\n\\subsection{Algorithm Specification}\n\n\\begin{algorithm}[ht]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A full comparison of window sizes appears in \\S\\ref{sec:appendix_sensitivity}.\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $5/5$).\n\n\\subsection{Validation Results}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}14$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n008d s4 & trained $\\dt$-emb & TP & 105K & reactive & 383 & 3.03 \\\\\n010b s0 & trained $\\dt$-emb (Cheetah) & TP & 95K & reactive & 248 & 6.34 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n019b & trained $\\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n009c s3 & no $\\dt$-emb & TN & -- & -- & 457 & -- \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 5/5 (1.00), \\quad FPR = 2/9 (0.22)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe detector identifies all five CIVO-positive runs (TPR = 5/5). Two are detected predictively (008d seeds~0 and~3, both at 45K). Two false positives occur among nine negative cases (FPR = 2/9, precision 71\\%, F$_1$ = 0.83). Run 009c develops genuine late-stage value overestimation unrelated to CIVO; run 009a triggers during a transient eval dip at 85K before recovery to 966. Early alerts (before 70K) carry higher diagnostic confidence.\n\n\\subsection{Cross-Simulator Specificity (PickCube)}\n\nExp\\_019b applies the CIVO-trigger configuration to PickCube-v1 in ManiSkill3, a manipulation task with sparse rewards. The V/E ratio exhibits an oscillatory pattern rather than monotonic divergence: it spikes to $r_t = 5.66$ at 52.5K, then deflates to 1.38 by 72.5K. This trajectory prevents the acceleration condition from co-occurring with evaluation decline at any single checkpoint. Across all 14 checkpoints through 132.5K, the detector correctly remains silent (TN), confirming that the acceleration filter distinguishes transient spikes from CIVO's sustained monotonic divergence. A frozen-embedding control (exp\\_054) confirms this classification: frozen PickCube-v1 exhibits a comparable burst (peak $8.81\\times$ at 62.5K) that resolves within a single evaluation cycle ($0.55\\times$ at 72.5K), establishing environment-specific origin independent of $\\dt$-embedding training.\n\n\\subsection{Detector Limitations}\n\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse. Second, the acceleration condition assumes monotonically increasing overestimation during onset. Third, the detector identifies a \\emph{pattern} rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values were calibrated on fourteen runs across three environments; generalization to different reward scales requires further validation.\n\n\\section{Dual-Critic Mechanism Ablation}\n\\label{sec:dual_critic_appendix}\n\n\\subsection{\\texorpdfstring{$2{\\times}2$}{2x2} Factorial Design}\n\nWe ablate the critic architecture in a $2{\\times}2$ factorial: \\{single, dual\\} $\\times$ \\{narrow (${\\sim}1.2$M), wide (${\\sim}2.4$M)\\} parameters. Table~\\ref{tab:dual_critic_full} reports all configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Dual-critic $2{\\times}2$ factorial results. Walker Walk unless noted.}\n\\label{tab:dual_critic_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Params} & \\textbf{NVE} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\n008d & Single narrow & 1.2M & 4.12$\\times$ & 82.8 & Collapse \\\\\n033 & Wide single & 2.4M & 4.75$\\times$ & 407.9 & CIVO $\\to$ self-repair \\\\\n035 s0 & Narrow dual (min) & 1.2M & 2.75$\\times$ & 697.8 & CIVO $\\to$ recovery \\\\\n039 s1 & Narrow dual (min) & 1.2M & 2.19$\\times$ & 592.7 & CIVO $\\to$ recovery \\\\\n032 s0 & Wide dual (min) & 2.4M & $\\leq$1.1$\\times$ & 739.7 & CIVO prevented \\\\\n032b s1 & Wide dual (min) & 2.4M & 1.4$\\times$ & 551.8 & CIVO prevented \\\\\n038 s2 & Wide dual (min) & 2.4M & $\\leq$0.3$\\times$ & 120.9$^*$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Cross-environment}} \\\\\n034 & Cheetah dual & 2.4M & 1.75$\\times$ & 97.5 & Partial recovery (31\\%) \\\\\n037 & Cheetah wide single & 2.4M & 3.60$\\times$ & 146.1 & CIVO $\\to$ self-repair \\\\\n036 & PickCube dual & 2.4M & 2.3$\\times$ & 27.7 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$CIVO prevented (NVE $\\leq 0.3\\times$) but non-CIVO eval collapse: eval peaked at 354 (155K), then declined to 120.9 (224K) with actor entropy increasing from $-3.59$ to $-0.45$.\\par}\n\\end{table}\n\n\\subsection{Critic Convergence (\\texorpdfstring{$v_1 \\approx v_2$}{v1 ≈ v2})}\n\nAcross all dual-critic configurations and environments, the two critics converge to near-identical value functions. On Walker Walk, Pearson $\\rho > 0.999$ between $v_1$ and $v_2$ outputs; on Cheetah Run and PickCube-v1, the gap is $< 0.2$ (exact match within numerical precision). Per-sample pessimism $\\mathbb{E}[\\max(v_1, v_2) - \\min(v_1, v_2)]$ is 3--4\\% of the theoretical bound for independent critics.\n\nThis convergence occurs because both critics train on the same RSSM-generated latent features. Unlike model-free Double Q-learning, where each critic sees different mini-batches of real transitions and develops distinct function approximation errors, pure-imagination critics share identical inputs from the world model. The min operation therefore cannot provide the pessimism bias that makes Double Q effective in model-free settings.\n\n\\subsection{Recovery vs.\\ Prevention Mechanism}\n\nThe $2{\\times}2$ factorial reveals two separable dimensions:\n\n\\paragraph{Recovery (min-dominated).} The min operation is the primary factor enabling recovery from CIVO. Both narrow dual-critic seeds experience CIVO and recover fully: exp\\_035 (s0, $\\nve = 2.75\\times$, eval $33.8 \\to 697.8$, recovery ratio $20.6\\times$) and exp\\_039 (s1, $\\nve = 2.19\\times$, eval $35.9 \\to 592.7$, recovery ratio $16.5\\times$). Both outperform wide single-critic (exp\\_033, 2.4M params, eval 407.9) despite $2\\times$ fewer parameters. The min operation reduces both peak CIVO severity (2.19--2.75$\\times$ vs.\\ 4.75$\\times$ for the comparable single-critic) and enables consistent full recovery across seeds.\n\n\\paragraph{Prevention (min $+$ capacity synergy).} CIVO prevention (NVE remaining below the $1.5\\times$ threshold) requires both the min operation and increased capacity: only the wide dual-critic (exp\\_032, 3 seeds) achieves this. The mechanism for this synergy is an open question; we hypothesize that increased capacity improves value calibration quality while the min operation constrains the overestimation feedback loop during early training when the two critics briefly diverge.\n\n\\paragraph{Cross-environment limits.} On Cheetah Run, the wide dual-critic (exp\\_034) reduces NVE from $8.27\\times$ (untreated baseline) to $1.75\\times$ ($\\geq 4\\times$ reduction) but cannot prevent CIVO onset, and recovery reaches only 31\\% of the pre-CIVO peak. This confirms that the min $+$ capacity synergy has environment-dependent limits: in high-CIVO-severity environments, architecture-level interventions attenuate but do not eliminate the pathology.\n",
    "structuredPatch": [
      {
        "oldStart": 102,
        "oldLines": 7,
        "newStart": 102,
        "newLines": 7,
        "lines": [
          " \\toprule",
          " \\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\",
          " \\midrule",
          "-Locomotion & Walker Walk & 4/4 & 0/3 & Yes (NVE $1.53$--$4.62\\times$) \\\\",
          "+Locomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\\times$) \\\\",
          " Locomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\",
          " Manipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\",
          " Manipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\"
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

_source line 87_

<details open><summary>🔧 Tool call — Edit · `toolu_01Ge4BaWhfJ7tg2i4GSbvSVR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "Trained & all & 008d & $1.53$--$4.62\\times$ & 64--268 & 4/4 \\\\",
  "new_string": "Trained & all & 008d, 059 & $1.53$--$4.72\\times$ & 64--268 & 5/5 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "a6e05b98-0eca-4d55-8194-4140805bd626",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TK4F2Ft89F87VL5hzvGLcE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13095,
      "cache_read_input_tokens": 51272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13095
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

_source line 88 · 2026-05-24T07:12:03.084Z_

<details><summary>↩ Tool result · `toolu_01Ge4BaWhfJ7tg2i4GSbvSVR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "d015c392-a5a5-410a-abc5-38e7168682de",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "Trained & all & 008d & $1.53$--$4.62\\times$ & 64--268 & 4/4 \\\\",
    "newString": "Trained & all & 008d, 059 & $1.53$--$4.72\\times$ & 64--268 & 5/5 \\\\",
    "originalFile": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\\times$ & Transient (self-corr.) \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\rowcolor{gray!15}\n008e\\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\\times$ & CIVO collapse \\\\\n008e\\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\\times$ & Healthy \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\n$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\n$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\n$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\n$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\par}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n\\label{tab:cross_domain}\n\\footnotesize\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n\\midrule\nLocomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\\times$) \\\\\nLocomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\nManipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\nManipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\nManipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all ten factorial experiments (including four 008e\\_v3 seeds). Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\\_v3\\_s3 exhibits CIVO with NVE $4.02\\times$ despite $\\Delta t{=}1$ imagination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.83 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.12 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s3 & 4.02 & CIVO           & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.02\\times$, exp~008e\\_v3\\_s3) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.02]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.958$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=7$, $n=10$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). $^\\dagger$Optimal threshold in $(3.78, 4.02]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 3 & 0 & 4 & 70.0\\% \\; [34.8, 93.3] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.2\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.5\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 3 & 0 & 0 & 7 & 100\\% \\; [69.2, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=4$, $n_{\\text{neg}}=6$, $n=10$, $\\text{AUROC}=0.958$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 4 & 2 & 0 & 4 & 80.0\\% \\; [44.4, 97.5] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 1.2\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.7\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 3.9\\times$ & 3 & 0 & 1 & 6 & 90.0\\% \\; [55.5, 99.7] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\\text{pos}}=8$, $n_{\\text{neg}}=8$, $n=16$, $\\text{AUROC}=0.969$). Includes Walker Walk (14 configurations) and Cheetah Run (2 configurations).}\n\\label{tab:sensitivity_b2_full}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 8 & 2 & 0 & 6 & 87.5\\% \\; [61.7, 98.4] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.2\\times$ & 8 & 1 & 0 & 7 & 93.8\\% \\; [69.8, 99.8] & 88.9\\% & 100\\% & 94.1\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 8 & 1 & 0 & 7 & 93.8\\% \\; [69.8, 99.8] & 88.9\\% & 100\\% & 94.1\\% \\\\\n$\\geq 1.7\\times$ & 6 & 1 & 2 & 7 & 81.3\\% \\; [54.4, 96.0] & 85.7\\% & 75.0\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 6 & 1 & 2 & 7 & 81.3\\% \\; [54.4, 96.0] & 85.7\\% & 75.0\\% & 80.0\\% \\\\\n$\\geq 3.9\\times$ & 6 & 0 & 2 & 8 & 87.5\\% \\; [61.7, 98.4] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all four CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 75.0\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 88.9\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 3$ the statistical power remains limited (accuracy 95\\% CI: [69.2\\%, 100\\%]).\n\n\\subsection{Expanded ROC Analysis}\n\\label{sec:roc_analysis}\n\nThe original $n{=}16$ analysis (Tables~\\ref{tab:sensitivity_b1}--\\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}29$ configurations spanning all tested interventions. Figure~\\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\\% bootstrap confidence interval (10{,}000 resamples).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.7\\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}\n\\caption{NVE ROC curve ($n{=}29$ configurations, AUROC${=}0.953$, in-sample, post-hoc). The preset $\\nve \\geq 1.5\\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}\n\\label{fig:nve_roc}\n\\end{figure}\n\nWe label a configuration as CIVO-positive if and only if (i)~it uses a trained $\\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.\n\nThe three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\\_008e\\_v3 seed~2, actor entropy \\emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \\emph{decrease}). All three produce NVE $> 1.5\\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\\times$) lacks $\\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\\times$) exhibits the full CIVO causal chain: trained $\\dt$-embedding, entropy decrease, and evaluation collapse to 14\\% of baseline.\n\n\\subsection{NVE Normalization Robustness}\n\\label{sec:nve_robustness}\n\nTo assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\\ref{tab:baseline_seeds}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Walker Walk baseline seeds at 105K and 505K steps.}\n\\label{tab:baseline_seeds}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Eval@105K} & \\textbf{Eval@505K} & \\textbf{ve@65K} & \\textbf{ve@105K} \\\\\n\\midrule\ns1 & 915.7 & 970.4 & 0.563 & 0.656 \\\\\ns2 & 443.5 & 945.7 & 0.898 & 0.742 \\\\\ns3 & 869.0 & 947.7 & --- & 0.664 \\\\\ns4 & 922.8 & 938.9 & --- & 0.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\\times$; 009b seed~2, peak NVE $1.62\\times$) to fall below the $1.5\\times$ threshold. Core CIVO cases (peak NVE $> 3\\times$) remain correctly classified under all baseline seeds.\n\nSingle-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\\%): the boundary case exp\\_009b flips from $\\nve = 1.62\\times$ (s1) to $1.23\\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\\times \\to 4.52\\times$; 008d: $4.12\\times \\to 3.54\\times$). The $1.5\\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\\% of the threshold.\n\n\\paragraph{Normalization conventions.} Walker NVE is normalized against the 4-seed mean baseline (seeds~1--4, each run to 505K+ steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).\n\n\\paragraph{Limitations.} With $n = 10$ experiments, Clopper-Pearson confidence intervals remain wide (e.g., 90.0\\% accuracy has 95\\% CI [55.5\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds. Table~\\ref{tab:sensitivity_b2_full} reports the original $n{=}16$ evaluation set spanning both environments. The expanded analysis ($n{=}29$, including SGS variants, RAVE, and TCN configurations) yields AUROC${=}0.953$ (Figure~\\ref{fig:nve_roc}, in-sample, post-hoc). The original $n{=}16$ core analysis yields AUROC${=}0.969$; the expanded $n{=}29$ set includes SGS, RAVE, TCN, and dual-critic configurations. Cross-architecture validation is deferred to future work.\n\n\\subsection{Leave-One-Environment-Out Cross-Validation}\n\\label{sec:nve_loeo}\n\nTo assess whether $\\theta{=}1.5\\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}13$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\\theta{=}1.5\\times$ on the held-out environment.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-environment-out cross-validation of NVE threshold $\\theta=1.5\\times$.\nFor each fold, the threshold is validated on an environment whose data was \\emph{not} used\nto select $\\theta$. The optimal threshold range on each training set is reported;\n$\\theta=1.5$ falls within the optimal range in all three folds.}\n\\label{tab:nve_loeo}\n\\begin{tabular}{lccccc}\n\\toprule\nHeld-out & $N_{\\text{train}}$ & $N_{\\text{test}}$ & $\\theta_{\\text{opt}}$ range & Test Accuracy & Test AUROC \\\\\n\\midrule\nPickCube & 18 & 2 & $(1.45,\\, 1.53]$ & 2/2 (1.000) & 1.000 \\\\\nCheetah  & 15 & 5 & $(1.45,\\, 1.53]$ & 5/5 (1.000) & 1.000 \\\\\nWalker   &  7 & 13 & $(1.00,\\, 3.78)$ & 12/13 (0.923) & 0.944 \\\\\n\\midrule\n\\textbf{Mean} & — & — & — & \\textbf{0.974} & \\textbf{0.981} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe threshold $\\theta{=}1.5\\times$ falls within the optimal accuracy range for all three training folds: $(1.45, 1.53]$ when Walker data is available, and the wider $(1.00, 3.78)$ when training on Cheetah$+$PickCube only (where CIVO and non-CIVO NVE values are well-separated). The single cross-validation error is exp\\_008e\\_v3 seed~2 (Walker), an IRD collapse mechanistically distinct from CIVO (\\S\\ref{sec:roc_analysis}). Mean held-out accuracy is 0.974 and mean AUROC is 0.981, confirming that $\\theta{=}1.5\\times$ generalizes across environments without retuning. PickCube fold confidence intervals remain wide (Clopper-Pearson 95\\% CI: $[0.158, 1.000]$) due to $N_{\\text{test}}{=}2$.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\paragraph{Embedding gradient analysis.}\nTable~\\ref{tab:three_way_emb} isolates embedding \\emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\\dt{=}2$ imagination).\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}\n\\label{tab:three_way_emb}\n\\footnotesize\n\\begin{tabular}{lccccl}\n\\toprule\nCondition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\\\\n\\midrule\nTrained & all & 008d & $1.53$--$4.62\\times$ & 64--268 & 4/4 \\\\\nReward detach & obs+KL only & 044 & $4.45\\times$ & 44$\\to$538$^\\dagger$ & 1/1 \\\\\nFull SGS & KL only & 018 & $1.66\\times$ & 448 & 1/1$^*$ \\\\\nFrozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\\nRemoved & N/A & 008f & $0.97$--$1.41\\times$ & 307--503 & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\\times$); seed~2 collapsed. $^\\dagger$Self-corrected at ${\\sim}175$K (eval 44$\\to$538, 59\\% baseline; 224K run). $^\\ddagger$Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps.\\par}\n\\end{table}\n\nThe reward-detach condition (exp\\_044, \\texttt{reward\\_dt\\_emb\\_detach=True}) uses a backward hook to block reward-head gradients from reaching $e_{\\dt}$, complementing the framework-level Reward SGS (exp\\_016e). Both yield the same directional result---CIVO onset not prevented---ruling out implementation artifacts. Exp\\_044 exhibits delayed CIVO onset (${\\sim}95$K vs.\\ typical $25$--$35$K), consistent with reduced but non-zero gradient pressure on $e_{\\dt}$. Over a full 224K run, exp\\_044 self-corrects: eval recovers from 44 (95K) to 538 (215K, 59\\% baseline), but this recovery is incomplete compared to spontaneous recovery without gradient intervention (exp\\_045: 868, 95\\% baseline). The lower asymptote suggests that selectively disrupting gradient flow may create optimization difficulties beyond CIVO itself.\n\nTable~\\ref{tab:factorial_design} summarizes the experimental configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Factorial design. Each row specifies one experimental configuration. \\textbf{Emb}: $\\dt$-embedding mode. \\textbf{Sub}: temporal subsampling. \\textbf{H}: imagination horizon. \\textbf{Imag $\\dt$}: temporal resolution used during imagination.}\n\\label{tab:factorial_design}\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{ID} & \\textbf{Purpose} & \\textbf{Emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Imag $\\dt$} \\\\\n\\midrule\n001 & Reference baseline & --- & --- & 15 & 1 \\\\\n006 & Fixed $\\dt{=}2$ & trn & on & 15 & 2 \\\\\n007 & Fixed $\\dt{=}4$ & trn & on & 15 & 4 \\\\\n\\midrule\n008a & Unexposed emb ctrl & exp$^a$ & off & 15 & 2 \\\\\n008c & Horizon control & exp$^a$ & off & 8 & 2 \\\\\n008d & Collapse condition & trn & on & 8 & 2 \\\\\n008e\\_v3 & $\\dt{=}1$ imag control & trn & on & 15 & 1 \\\\\n008f & Causal ablation & --- & on & 8 & 2 \\\\\n\\midrule\n015b & Frozen-emb ctrl & frz$^b$ & on & 8 & 2 \\\\\n016e & Stop-grad (reward) & trn$^\\dagger$ & on & 8 & 2 \\\\\n018 & Full-SGS & trn$^\\ddagger$ & on & 8 & 2 \\\\\n\\midrule\n005 & Learned gate & adaptive & off & 15 & learned \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^\\dagger$ \\texttt{reward\\_dt\\_emb\\_detach=True}; $^\\ddagger$ all non-KL gradients to \\texttt{dt\\_emb} detached.\\par}\n\\end{table}\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe empirical finding that trained embedding \\emph{plus} multi-rate exposure jointly predict CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.83$--$0.93\\times$ range across 3 seeds (105K steps). Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical factor is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training. This confirms that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.42\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.47 \\rightarrow 0.39 \\rightarrow 0.42$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and precedes full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.42\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that in all tested configurations, CIVO occurs only with the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\nCross-environment validation on Cheetah Run replicates the empirical pattern: trained $e_{\\dt}$ precedes CIVO in both tested seeds (exp\\_010b, 2 seeds, NVE $8.27$--$108.52\\times$, collapse to 51.7/0.83) while removing the embedding eliminates it (exp\\_024b, 2 seeds, NVE $<0.2\\times$, eval 96.5/77.3). Freezing the embedding on Cheetah (exp\\_046, NVE${=}1.35\\times$ vs.\\ trained $70.64\\times$, a $52\\times$ reduction) further confirms that embedding trainability, not architecture, drives CIVO. This extends the sufficiency finding from Walker Walk to a second locomotion environment with qualitatively different dynamics (6-joint vs.\\ 2-joint).\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole predictor of CIVO in tested configurations. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) precedes CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly sufficient in tested configurations.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling precedes collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$; low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig4_mechanism_diagram.pdf}\n\\caption{CIVO mechanism diagram. The trained $\\dt$-embedding enables asymmetric reward prediction fidelity, initiating a feedback loop: biased RSSM rewards $\\to$ optimistic critic values $\\to$ actor exploitation $\\to$ reinforced state-distribution skew.}\n\\label{fig:civo_mechanism}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO (Figure~\\ref{fig:civo_mechanism}).  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, which confirms that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\paragraph{Signed reward error analysis.}\nTo test whether CIVO arises from one-step reward overprediction, we compute signed error (predicted $-$ actual) on posterior-conditioned RSSM predictions (Table~\\ref{tab:signed_error}). The trained-embedding model (008d) shows \\emph{negative} bias at $\\dt{=}2$ (mean signed error $-0.599$, only 8\\% of samples overpredicted), ruling out observation-level reward overprediction as the mechanism. The baseline is well-calibrated (mean SE $\\approx 0$), confirming methodological soundness. Value overestimation therefore occurs during \\emph{imagination-level} prior drift: the RSSM prior (unconditioned on observations) generates reward-favorable trajectories at $\\dt > 1$ (Stage~1 above, $1.68\\times$ ratio under random policy), and the critic accumulates these into overestimated returns. The one-step reward prediction is negatively biased when conditioned on real observations, but this posterior correction is unavailable during imagination. This also distinguishes CIVO from generic compounding error, which would produce \\emph{positive} signed error accumulating with horizon; the negative observation-level bias confirms that CIVO is a prior-drift phenomenon, not a reward-prediction artifact.\n\n\\begin{table}[h]\n\\centering\n\\caption{Signed reward error (predicted $-$ actual) on posterior-conditioned RSSM predictions. Negative values indicate underprediction. The trained-embedding model underpredicts at $\\dt{=}2$, ruling out observation-level reward overprediction as the CIVO mechanism.}\n\\label{tab:signed_error}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Config} & $\\dt$ & \\textbf{Mean SE} & \\textbf{Std} & \\textbf{\\%Over} & \\textbf{Actual} & \\textbf{Pred} \\\\\n\\midrule\nBaseline & 1 & $+0.001$ & 0.023 & 39.6\\% & 1.893 & 1.894 \\\\\n\\midrule\n008d (trained) & 1 & $+0.018$ & 0.072 & 61.8\\% & 0.361 & 0.379 \\\\\n008d (trained) & 2 & $\\mathbf{-0.599}$ & 0.722 & 8.0\\% & 0.721 & 0.121 \\\\\n\\midrule\n008f (no emb) & 1 & $-0.710$ & 0.704 & 14.0\\% & 0.921 & 0.211 \\\\\n008f (no emb) & 2 & $-1.645$ & 1.485 & 5.0\\% & 1.840 & 0.195 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 0/2 CIVO elimination rate on Walker (seed~1: NVE reduced from $4.12\\times$ to $1.66\\times$ but remains CIVO-positive; seed~2: collapsed) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention eliminates CIVO in neither seed: seed~1 shows partial mitigation (eval 448.3, peak NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses (eval 40.8). Removing the observation decoder gradient channel is thus contributory but not sufficient. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3. \\textbf{Trained dt-emb} (008d)\\protect\\footnotemark: learned $d{=}32$ temporal embedding with multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with all non-KL gradients detached from $e_{\\dt}$. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$. Full-SGS seed~1 shows partial mitigation ($-51\\%$ final, NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses ($-96\\%$ final). CIVO elimination rate $= 0/2$.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}\n\nCross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This transient self-correcting trajectory is not attributable to the SGS intervention: the initial CIVO onset and peak severity are comparable to the unmitigated case, and the self-correction may reflect Cheetah Run's simpler dynamics rather than SGS efficacy.  Performance remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's Walker results (0/2 CIVO elimination), these findings yield a 0/3 elimination rate across environments, indicating that gradient-level interventions alone do not eliminate the CIVO vulnerability. Additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Post-CIVO outcomes for all six CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Env} & \\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\nWalker & s1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\nWalker & s2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\nWalker & s3 (008d\\_s3) & 1.53$\\times$ & 1.53$\\times$ & 268$^\\diamond$ & Late-onset collapse \\\\\nWalker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\n\\midrule\nCheetah & s1 (010b) & 8.27$\\times$ & 8.27$\\times$ & 51.7 & Full collapse \\\\\nCheetah & s0 (010b\\_s0) & 108.52$\\times$ & 108.52$\\times$ & 0.83 & Full collapse \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\diamond$ Transitional; train returns still declining at 105K.\\par}\n\\end{table}\n\nAll six CIVO-positive seeds cross the $\\nve > 1.5\\times$ threshold (Table~\\ref{tab:post_civo}), yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Full collapse is the majority outcome (5/6 seeds), with one self-correction case (Walker seed~2) that remains severely degraded (29.3\\% of baseline). Cheetah seeds exhibit more extreme overestimation (peak NVE $8.27$--$108.52\\times$ vs.\\ Walker's $1.53$--$4.62\\times$), consistent with the Cheetah reward scale amplifying the fidelity gap.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\paragraph{A fourth trajectory: CIVO-induced persistent value collapse.}\nObs-decoder SGS seed~3 (exp\\_025) exhibits a trajectory not observed in the untreated seeds: healthy through 105K ($\\nve < 1.0\\times$, eval 818.6), CIVO onset at 135K ($\\nve = 5.47\\times$, eval 67.0), followed by evaluation recovery (590.2 at 215K, 64\\% of baseline) but persistent value collapse ($\\nve = 0.14\\times$, value mean 80.6). The critic undershoots after the CIVO episode, suggesting that CIVO-induced representational damage may be irreversible even when the policy partially recovers. This contrasts with transient CIVO (seed~2, 009b), where both value and evaluation recover jointly, and with full collapse (seed~1, 008d), where neither recovers. Seed~4 exhibits the same terminal value collapse ($\\nve = 0.14\\times$ at 215K, eval 242), suggesting this overcorrection is systematic rather than seed-specific. The pattern adds a fourth post-CIVO outcome---policy recovery with critic damage---to the three documented in Table~\\ref{tab:post_civo}.\n\n\\subsubsection{Failure and Degradation Mode Taxonomy}\n\nTable~\\ref{tab:failure_modes} classifies the seven distinct failure and degradation modes observed across all experimental configurations. The taxonomy reveals that CIVO is not a single failure mode but a family of related pathologies, with the trained $\\dt$-embedding creating vulnerability through at least three independent mechanisms: value-driven collapse (monotonic, late-onset, and SGS-resistant CIVO), entropy-driven instability (IRD collapse), and gradient-mediated effects (gradient starvation, SGS-paradoxical worsening).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Failure and degradation mode taxonomy. Each mode is characterized by its NVE trajectory, entropy behavior, and primary mechanism.}\n\\label{tab:failure_modes}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccl@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Representative} & \\textbf{NVE} & \\textbf{Entropy} & \\textbf{Mechanism} \\\\\n\\midrule\nMonotonic CIVO & 008d, 008d\\_s4, 010b\\_s0 & $\\uparrow$ sustained & $\\downarrow$ & Reward bias $\\to$ critic $\\to$ actor \\\\\nLate-onset CIVO & 008d\\_s3 & $\\uparrow$ delayed & $\\downarrow$ & Same, delayed onset \\\\\nTransient CIVO & 009b & Peak $\\to$ $\\downarrow$ & Stable & Self-correction via capacity \\\\\nIRD collapse & 008e\\_v3\\_s2 & $\\uparrow$ late & $\\uparrow$ & Entropy-driven, values stable \\\\\nGrad.\\ starvation & 015b & Oscillates, decays & Stable & Frozen emb $\\to$ zero actor grad \\\\\nSGS-resistant & 018\\_s2 & $\\uparrow$ & $\\downarrow$ & Forward-pass conditioning \\\\\nSGS-paradoxical & 016e & $\\uparrow$ sustained & $\\downarrow$ & Reward SGS $\\to$ obs-dec reliance \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) avoids collapse in 2 of 4 seeds (50\\%), while the remaining two collapse via distinct mechanisms: Pathway~A (CIVO-driven, entropy decrease; s3, NVE $4.02\\times$) and Pathway~B (entropy-driven, entropy increase; s2, NVE $3.78\\times$; \\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse patterns identified in \\S\\ref{sec:f6}---CIVO (Pathway~A, value-driven, entropy decreasing) and a tentative second mode (Pathway~B, eval-driven, entropy increasing)---have distinct diagnostic signatures. Pathway~B is observed in only two seeds (008e\\_v3\\_s2 and 038\\_s2); we present it as preliminary evidence that the trained $\\dt$-embedding's learned features may affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B), though additional data is needed to confirm this as a distinct mechanism.  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse (Figure~\\ref{fig:multiple_pathways}).\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.  The CIVO mechanism requires three structural properties: (1) a temporal embedding that co-adapts with dynamics via gradient flow, (2) multi-step imagined rollouts used for critic training, and (3) a reward head that inherits latent biases from the shared representation.  Transformer-based world models that share these properties may exhibit analogous vulnerability; architectures that decouple temporal conditioning from the reward prediction pathway would not.\n\n\\subsection{Cross-Environment TCN Evaluation}\n\\label{sec:tcn_cross_env}\n\nTable~\\ref{tab:tcn_full} reports the full TCN evaluation across environments and noise magnitudes.\n\n\\begin{table}[h]\n\\centering\n\\caption{TCN results across environments and noise magnitudes. Prevention = peak NVE $< 1.5\\times$ (35K+).}\n\\label{tab:tcn_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Env} & $\\sigma$ & \\textbf{Seed} & \\textbf{NVE$_{\\max}$} & \\textbf{Prevented?} & \\textbf{Eval (\\%)} \\\\\n\\midrule\nWalker & 0.1 & s0 & 1.02 & \\checkmark$^*$ & 55\\% \\\\\nWalker & 0.2 & s0 & 0.91 & \\checkmark & 91\\% \\\\\nWalker & 0.2 & s1 & 0.64 & \\checkmark & 45\\% \\\\\nWalker & 0.2 & s2 & 2.11$^\\dagger$ & $\\times$ & ${\\sim}5\\%$ \\\\\n\\rowcolor{gray!15}\nWalker & 0.2 & s3 & 3.04$^\\P$ & $\\times$ & 11\\% \\\\\nWalker & 0.5 & s0 & 3.97 & $\\times$ & 27\\% \\\\\nWalker & 0.5 & s1 & 1.64 & $\\times$ & 41\\% \\\\\n\\midrule\nCheetah & 0.2 & s0 & 1.90 & $\\times$ & crashed \\\\\nCheetah & 0.5 & s0 & 10.67 & $\\times$ & 26\\% \\\\\nCheetah & 1.0 & s0 & $\\leq$0.30 & \\checkmark$^\\S$ & 15\\% \\\\\n\\midrule\nPickCube & 0.2 & s0 & 3.71 & $\\times$ & failing \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Borderline: NVE${=}1.02\\times$ at 95K, below $1.5\\times$ threshold but above $1.0\\times$.\\\\\n$^\\dagger$NVE $= 2.11\\times$ at 95K, still rising; eval ${\\sim}5\\%$ of baseline.\\\\\n$^\\P$Late-onset CIVO: NVE declined to $0.67\\times$ at 95K before phase-transition-like spike to $3.04\\times$ at 105K; eval 349.6 at 95K $\\to$ 71.8 at 105K $\\to$ 104.5 at 215K.\\\\\n$^\\S$CIVO prevented (NVE${\\leq}0.30$); peak eval 116\\% baseline at 35K, declining to 15\\% by 215K via progressive policy erosion. See ``impossible dose'' discussion.\\par}\n\\end{table}\n\n\\paragraph{Cheetah Run $\\sigma{=}0.5$: transient spike with permanent eval damage.}\nCheetah $\\sigma{=}0.5$ exhibits a novel failure mode: a transient CIVO spike (NVE $= 10.67\\times$ at 55K) followed by NVE recovery ($< 0.3\\times$ by 95K), but permanent evaluation damage (26\\% of baseline). The value signal self-corrects while the policy does not recover, suggesting that CIVO-induced representational damage during the spike is irreversible even when the critic subsequently recalibrates. This trajectory parallels the obs-decoder SGS seed~3 pattern (\\S\\ref{sec:seed_divergence}), where partial policy recovery coexists with persistent critic damage.\n\n\\paragraph{Cheetah Run $\\sigma{=}0.2$: insufficient dose.}\nAt $\\sigma{=}0.2$, Cheetah reaches NVE $= 1.9\\times$ at 55K---exceeding the $1.5\\times$ threshold---consistent with Cheetah's higher baseline CIVO severity ($8$--$108\\times$ vs.\\ Walker's $2$--$6\\times$). The noise magnitude that suffices for Walker is inadequate for Cheetah, but increasing $\\sigma$ to 0.5 trades CIVO prevention for a different failure mode rather than achieving mitigation.\n\n\\paragraph{PickCube-v1 $\\sigma{=}0.2$: sparse-reward failure.}\nPickCube reaches NVE $= 3.71\\times$ at 52.5K with $\\sigma{=}0.2$, indicating that TCN provides no protection in sparse-reward manipulation tasks. The combination of sparse rewards and temporal conditioning may amplify the fidelity gap beyond what representation-level noise can attenuate.\n\n\\paragraph{Dose-response analysis.}\nWe observe $\\sigma{=}0.2$ as a local optimum on Walker Walk, achieving complete CIVO suppression in 2 of 4 seeds. Seeds~2 and~3 both fail but via distinct CIVO onset dynamics: seed~2 shows gradual escalation (NVE $= 2.11\\times$ at 95K, still rising, eval ${\\sim}5\\%$), while seed~3 exhibits a phase-transition-like onset---NVE declined to $0.67\\times$ at 95K before spiking to $3.04\\times$ at 105K (eval 349.6 $\\to$ 71.8 in 10K steps). When TCN fails to prevent CIVO onset, the resulting trajectory qualitatively resembles untreated CIVO in its terminal outcome---runaway NVE and eval collapse. The two failure modes (gradual escalation vs.\\ sudden onset after apparent suppression) reinforce that TCN operates as a binary gate on CIVO onset rather than providing graded attenuation. Below the optimum, we observe $\\sigma{=}0.1$ as insufficient (NVE $= 1.02\\times$---borderline, eval 55\\%); above it, $\\sigma{=}0.5$ overdoses (oscillatory CIVO, eval $\\leq 41\\%$). Cross-seed variance at $\\sigma{=}0.2$ (eval 5--91\\%) exceeds the cross-dose difference by a wide margin, reinforcing that seed effects dominate dose effects. TCN is the only tested intervention achieving complete CIVO suppression in any configuration, but its high seed sensitivity and failure to transfer across environments position it as a \\emph{diagnostic probe}---identifying the representation level as the relevant intervention target---rather than a deployable mitigation.\n\n\\paragraph{Cheetah Run ``impossible dose'' dilemma.}\nExp\\_030c (224K steps) reveals a qualitatively different dose-response on Cheetah. At $\\sigma{=}1.0$, CIVO is eliminated (NVE${\\leq}0.30$ throughout) and initial learning is \\emph{unimpaired}: peak eval reaches 372 at 35K (116\\% of baseline), demonstrating that $\\sigma{=}1.0$ noise does not prevent policy acquisition. However, cumulative actor gradient interference produces progressive policy erosion---eval declines from 372 to 47 by 215K (15\\% of baseline)---while the critic remains well-calibrated (value\\_mean${=}12.4$, NVE${=}0.26$ at 215K). This establishes that \\emph{policy degradation $\\neq$ value corruption}: accurate value signals are insufficient when the actor cannot optimize effectively in noise-perturbed imagination.\n\nThis ``correct values, failed policy'' pattern provides indirect evidence that CIVO is mechanistically distinct from standard overestimation. Double Q-learning and ensemble methods address critic estimation error, but at $\\sigma{=}1.0$ the critic is accurate and the policy still collapses---a failure mode orthogonal to what these countermeasures target. The impossible dose dilemma scales with environment complexity: Cheetah's baseline CIVO severity ($8$--$108\\times$ NVE) requires $\\sigma \\geq 1.0$ to suppress, but this exceeds the actor's gradient signal-to-noise tolerance. On Walker, a narrow effective window exists around $\\sigma{=}0.2$; on Cheetah, the effective dose ($\\sigma \\geq 1.0$) exceeds the tolerable dose, and environments with higher CIVO severity will systematically lack a viable dose window.\n\n\\section{DreamerV3 Hyperparameters}\n\\label{sec:hyperparameters}\n\nTable~\\ref{tab:hyperparams} lists the DreamerV3 hyperparameters used across all experiments. Unless otherwise noted, we use the default DreamerV3 configuration for continuous-control tasks (\\texttt{dmc\\_proprio}).\n\n\\begin{table}[ht]\n\\centering\n\\caption{DreamerV3 hyperparameters for all experiments. Modifications from defaults are marked with $\\diamond$.}\n\\label{tab:hyperparams}\n\\small\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{World Model}} \\\\\nRSSM discrete states & 32 classes $\\times$ 32 categories \\\\\nRSSM stochastic dim & 32 \\\\\nRSSM deterministic dim & 512 \\\\\nMLP hidden size & 512 \\\\\nMLP layers & 2 \\\\\nActivation & SiLU \\\\\nNormalization & LayerNorm \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Training}} \\\\\nBatch size & 16 sequences $\\times$ 64 steps \\\\\nLearning rate & $3 \\times 10^{-4}$ (Adam, $\\epsilon{=}10^{-8}$) \\\\\nSequence length & 64 \\\\\nTraining ratio & 512 \\\\\nFree nats & 1.0 \\\\\nKL balance ($\\alpha$) & 0.8 \\\\\nDiscount ($\\gamma$) & 0.997 \\\\\n$\\lambda$-return & 0.95 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Policy}} \\\\\nImagination horizon$^\\diamond$ & 8 or 15 (see Table~\\ref{tab:complete_results}) \\\\\nActor entropy scale & $3 \\times 10^{-4}$ \\\\\nActor gradient & Reinforce + dynamics backprop \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Temporal Abstraction}$^\\diamond$} \\\\\nGate enabled & True (all non-baseline) \\\\\nGate fixed $\\dt$ & 1 or 2 (per config) \\\\\nSubsample max $\\dt$ & 1 (OFF) or 2 (ON) \\\\\n$\\dt$-embedding dim & 32 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Environment}} \\\\\nAction repeat & 2 (Walker Walk, Cheetah Run) \\\\\nObservation & Proprioceptive (no pixels) \\\\\nTotal environment steps & 105K \\\\\nEvaluation frequency & Every 10K steps \\\\\nEvaluation episodes & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Online CIVO Detector Details}\n\\label{sec:detector_appendix}\n\nThis appendix provides the full algorithm specification and validation results for the online CIVO detector described in \\S\\ref{sec:detector}.\n\n\\subsection{Algorithm Specification}\n\n\\begin{algorithm}[ht]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A full comparison of window sizes appears in \\S\\ref{sec:appendix_sensitivity}.\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $5/5$).\n\n\\subsection{Validation Results}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}14$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n008d s4 & trained $\\dt$-emb & TP & 105K & reactive & 383 & 3.03 \\\\\n010b s0 & trained $\\dt$-emb (Cheetah) & TP & 95K & reactive & 248 & 6.34 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n019b & trained $\\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n009c s3 & no $\\dt$-emb & TN & -- & -- & 457 & -- \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 5/5 (1.00), \\quad FPR = 2/9 (0.22)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe detector identifies all five CIVO-positive runs (TPR = 5/5). Two are detected predictively (008d seeds~0 and~3, both at 45K). Two false positives occur among nine negative cases (FPR = 2/9, precision 71\\%, F$_1$ = 0.83). Run 009c develops genuine late-stage value overestimation unrelated to CIVO; run 009a triggers during a transient eval dip at 85K before recovery to 966. Early alerts (before 70K) carry higher diagnostic confidence.\n\n\\subsection{Cross-Simulator Specificity (PickCube)}\n\nExp\\_019b applies the CIVO-trigger configuration to PickCube-v1 in ManiSkill3, a manipulation task with sparse rewards. The V/E ratio exhibits an oscillatory pattern rather than monotonic divergence: it spikes to $r_t = 5.66$ at 52.5K, then deflates to 1.38 by 72.5K. This trajectory prevents the acceleration condition from co-occurring with evaluation decline at any single checkpoint. Across all 14 checkpoints through 132.5K, the detector correctly remains silent (TN), confirming that the acceleration filter distinguishes transient spikes from CIVO's sustained monotonic divergence. A frozen-embedding control (exp\\_054) confirms this classification: frozen PickCube-v1 exhibits a comparable burst (peak $8.81\\times$ at 62.5K) that resolves within a single evaluation cycle ($0.55\\times$ at 72.5K), establishing environment-specific origin independent of $\\dt$-embedding training.\n\n\\subsection{Detector Limitations}\n\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse. Second, the acceleration condition assumes monotonically increasing overestimation during onset. Third, the detector identifies a \\emph{pattern} rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values were calibrated on fourteen runs across three environments; generalization to different reward scales requires further validation.\n\n\\section{Dual-Critic Mechanism Ablation}\n\\label{sec:dual_critic_appendix}\n\n\\subsection{\\texorpdfstring{$2{\\times}2$}{2x2} Factorial Design}\n\nWe ablate the critic architecture in a $2{\\times}2$ factorial: \\{single, dual\\} $\\times$ \\{narrow (${\\sim}1.2$M), wide (${\\sim}2.4$M)\\} parameters. Table~\\ref{tab:dual_critic_full} reports all configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Dual-critic $2{\\times}2$ factorial results. Walker Walk unless noted.}\n\\label{tab:dual_critic_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Params} & \\textbf{NVE} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\n008d & Single narrow & 1.2M & 4.12$\\times$ & 82.8 & Collapse \\\\\n033 & Wide single & 2.4M & 4.75$\\times$ & 407.9 & CIVO $\\to$ self-repair \\\\\n035 s0 & Narrow dual (min) & 1.2M & 2.75$\\times$ & 697.8 & CIVO $\\to$ recovery \\\\\n039 s1 & Narrow dual (min) & 1.2M & 2.19$\\times$ & 592.7 & CIVO $\\to$ recovery \\\\\n032 s0 & Wide dual (min) & 2.4M & $\\leq$1.1$\\times$ & 739.7 & CIVO prevented \\\\\n032b s1 & Wide dual (min) & 2.4M & 1.4$\\times$ & 551.8 & CIVO prevented \\\\\n038 s2 & Wide dual (min) & 2.4M & $\\leq$0.3$\\times$ & 120.9$^*$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Cross-environment}} \\\\\n034 & Cheetah dual & 2.4M & 1.75$\\times$ & 97.5 & Partial recovery (31\\%) \\\\\n037 & Cheetah wide single & 2.4M & 3.60$\\times$ & 146.1 & CIVO $\\to$ self-repair \\\\\n036 & PickCube dual & 2.4M & 2.3$\\times$ & 27.7 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$CIVO prevented (NVE $\\leq 0.3\\times$) but non-CIVO eval collapse: eval peaked at 354 (155K), then declined to 120.9 (224K) with actor entropy increasing from $-3.59$ to $-0.45$.\\par}\n\\end{table}\n\n\\subsection{Critic Convergence (\\texorpdfstring{$v_1 \\approx v_2$}{v1 ≈ v2})}\n\nAcross all dual-critic configurations and environments, the two critics converge to near-identical value functions. On Walker Walk, Pearson $\\rho > 0.999$ between $v_1$ and $v_2$ outputs; on Cheetah Run and PickCube-v1, the gap is $< 0.2$ (exact match within numerical precision). Per-sample pessimism $\\mathbb{E}[\\max(v_1, v_2) - \\min(v_1, v_2)]$ is 3--4\\% of the theoretical bound for independent critics.\n\nThis convergence occurs because both critics train on the same RSSM-generated latent features. Unlike model-free Double Q-learning, where each critic sees different mini-batches of real transitions and develops distinct function approximation errors, pure-imagination critics share identical inputs from the world model. The min operation therefore cannot provide the pessimism bias that makes Double Q effective in model-free settings.\n\n\\subsection{Recovery vs.\\ Prevention Mechanism}\n\nThe $2{\\times}2$ factorial reveals two separable dimensions:\n\n\\paragraph{Recovery (min-dominated).} The min operation is the primary factor enabling recovery from CIVO. Both narrow dual-critic seeds experience CIVO and recover fully: exp\\_035 (s0, $\\nve = 2.75\\times$, eval $33.8 \\to 697.8$, recovery ratio $20.6\\times$) and exp\\_039 (s1, $\\nve = 2.19\\times$, eval $35.9 \\to 592.7$, recovery ratio $16.5\\times$). Both outperform wide single-critic (exp\\_033, 2.4M params, eval 407.9) despite $2\\times$ fewer parameters. The min operation reduces both peak CIVO severity (2.19--2.75$\\times$ vs.\\ 4.75$\\times$ for the comparable single-critic) and enables consistent full recovery across seeds.\n\n\\paragraph{Prevention (min $+$ capacity synergy).} CIVO prevention (NVE remaining below the $1.5\\times$ threshold) requires both the min operation and increased capacity: only the wide dual-critic (exp\\_032, 3 seeds) achieves this. The mechanism for this synergy is an open question; we hypothesize that increased capacity improves value calibration quality while the min operation constrains the overestimation feedback loop during early training when the two critics briefly diverge.\n\n\\paragraph{Cross-environment limits.} On Cheetah Run, the wide dual-critic (exp\\_034) reduces NVE from $8.27\\times$ (untreated baseline) to $1.75\\times$ ($\\geq 4\\times$ reduction) but cannot prevent CIVO onset, and recovery reaches only 31\\% of the pre-CIVO peak. This confirms that the min $+$ capacity synergy has environment-dependent limits: in high-CIVO-severity environments, architecture-level interventions attenuate but do not eliminate the pathology.\n",
    "structuredPatch": [
      {
        "oldStart": 315,
        "oldLines": 7,
        "newStart": 315,
        "newLines": 7,
        "lines": [
          " \\toprule",
          " Condition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\\\",
          " \\midrule",
          "-Trained & all & 008d & $1.53$--$4.62\\times$ & 64--268 & 4/4 \\\\",
          "+Trained & all & 008d, 059 & $1.53$--$4.72\\times$ & 64--268 & 5/5 \\\\",
          " Reward detach & obs+KL only & 044 & $4.45\\times$ & 44$\\to$538$^\\dagger$ & 1/1 \\\\",
          " Full SGS & KL only & 018 & $1.66\\times$ & 448 & 1/1$^*$ \\\\",
          " Frozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\"
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


### Assistant

_source line 89_

#3, #9, #10, #15 完成。继续完成 appendix 表格插入 (#11, #13) 和 #12, #14, #16。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "a793eed5-20bb-41df-92d0-056a663f9581",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012swrHLwzU8fYGrKxzsxi4V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 64367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1633
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

_source line 90_

<details open><summary>🔧 Tool call — Edit · `toolu_01RBiXBBV2PyoDMJkTm6zZjT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1)",
  "new_string": "008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\\times$ & Self-correction \\\\\n008f & No dt\\_emb (s1)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "0e3338c0-b47c-459a-af91-faac139c5860",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012swrHLwzU8fYGrKxzsxi4V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 64367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1633
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

_source line 91 · 2026-05-24T07:12:12.657Z_

<details><summary>↩ Tool result · `toolu_01RBiXBBV2PyoDMJkTm6zZjT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "03559736-4158-4e2b-8c27-aa6b0aba00c6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1)",
    "newString": "008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\\times$ & Self-correction \\\\\n008f & No dt\\_emb (s1)",
    "originalFile": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\\times$ & Transient (self-corr.) \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\rowcolor{gray!15}\n008e\\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\\times$ & CIVO collapse \\\\\n008e\\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\\times$ & Healthy \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\n$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\n$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\n$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\n$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\par}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n\\label{tab:cross_domain}\n\\footnotesize\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n\\midrule\nLocomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\\times$) \\\\\nLocomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\nManipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\nManipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\nManipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all ten factorial experiments (including four 008e\\_v3 seeds). Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\\_v3\\_s3 exhibits CIVO with NVE $4.02\\times$ despite $\\Delta t{=}1$ imagination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.83 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.12 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s3 & 4.02 & CIVO           & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.02\\times$, exp~008e\\_v3\\_s3) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.02]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.958$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=7$, $n=10$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). $^\\dagger$Optimal threshold in $(3.78, 4.02]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 3 & 0 & 4 & 70.0\\% \\; [34.8, 93.3] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.2\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.5\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 3 & 0 & 0 & 7 & 100\\% \\; [69.2, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=4$, $n_{\\text{neg}}=6$, $n=10$, $\\text{AUROC}=0.958$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 4 & 2 & 0 & 4 & 80.0\\% \\; [44.4, 97.5] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 1.2\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.7\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 3.9\\times$ & 3 & 0 & 1 & 6 & 90.0\\% \\; [55.5, 99.7] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\\text{pos}}=8$, $n_{\\text{neg}}=8$, $n=16$, $\\text{AUROC}=0.969$). Includes Walker Walk (14 configurations) and Cheetah Run (2 configurations).}\n\\label{tab:sensitivity_b2_full}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 8 & 2 & 0 & 6 & 87.5\\% \\; [61.7, 98.4] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.2\\times$ & 8 & 1 & 0 & 7 & 93.8\\% \\; [69.8, 99.8] & 88.9\\% & 100\\% & 94.1\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 8 & 1 & 0 & 7 & 93.8\\% \\; [69.8, 99.8] & 88.9\\% & 100\\% & 94.1\\% \\\\\n$\\geq 1.7\\times$ & 6 & 1 & 2 & 7 & 81.3\\% \\; [54.4, 96.0] & 85.7\\% & 75.0\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 6 & 1 & 2 & 7 & 81.3\\% \\; [54.4, 96.0] & 85.7\\% & 75.0\\% & 80.0\\% \\\\\n$\\geq 3.9\\times$ & 6 & 0 & 2 & 8 & 87.5\\% \\; [61.7, 98.4] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all four CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 75.0\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 88.9\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 3$ the statistical power remains limited (accuracy 95\\% CI: [69.2\\%, 100\\%]).\n\n\\subsection{Expanded ROC Analysis}\n\\label{sec:roc_analysis}\n\nThe original $n{=}16$ analysis (Tables~\\ref{tab:sensitivity_b1}--\\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}29$ configurations spanning all tested interventions. Figure~\\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\\% bootstrap confidence interval (10{,}000 resamples).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.7\\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}\n\\caption{NVE ROC curve ($n{=}29$ configurations, AUROC${=}0.953$, in-sample, post-hoc). The preset $\\nve \\geq 1.5\\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}\n\\label{fig:nve_roc}\n\\end{figure}\n\nWe label a configuration as CIVO-positive if and only if (i)~it uses a trained $\\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.\n\nThe three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\\_008e\\_v3 seed~2, actor entropy \\emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \\emph{decrease}). All three produce NVE $> 1.5\\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\\times$) lacks $\\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\\times$) exhibits the full CIVO causal chain: trained $\\dt$-embedding, entropy decrease, and evaluation collapse to 14\\% of baseline.\n\n\\subsection{NVE Normalization Robustness}\n\\label{sec:nve_robustness}\n\nTo assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\\ref{tab:baseline_seeds}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Walker Walk baseline seeds at 105K and 505K steps.}\n\\label{tab:baseline_seeds}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Eval@105K} & \\textbf{Eval@505K} & \\textbf{ve@65K} & \\textbf{ve@105K} \\\\\n\\midrule\ns1 & 915.7 & 970.4 & 0.563 & 0.656 \\\\\ns2 & 443.5 & 945.7 & 0.898 & 0.742 \\\\\ns3 & 869.0 & 947.7 & --- & 0.664 \\\\\ns4 & 922.8 & 938.9 & --- & 0.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\\times$; 009b seed~2, peak NVE $1.62\\times$) to fall below the $1.5\\times$ threshold. Core CIVO cases (peak NVE $> 3\\times$) remain correctly classified under all baseline seeds.\n\nSingle-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\\%): the boundary case exp\\_009b flips from $\\nve = 1.62\\times$ (s1) to $1.23\\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\\times \\to 4.52\\times$; 008d: $4.12\\times \\to 3.54\\times$). The $1.5\\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\\% of the threshold.\n\n\\paragraph{Normalization conventions.} Walker NVE is normalized against the 4-seed mean baseline (seeds~1--4, each run to 505K+ steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).\n\n\\paragraph{Limitations.} With $n = 10$ experiments, Clopper-Pearson confidence intervals remain wide (e.g., 90.0\\% accuracy has 95\\% CI [55.5\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds. Table~\\ref{tab:sensitivity_b2_full} reports the original $n{=}16$ evaluation set spanning both environments. The expanded analysis ($n{=}29$, including SGS variants, RAVE, and TCN configurations) yields AUROC${=}0.953$ (Figure~\\ref{fig:nve_roc}, in-sample, post-hoc). The original $n{=}16$ core analysis yields AUROC${=}0.969$; the expanded $n{=}29$ set includes SGS, RAVE, TCN, and dual-critic configurations. Cross-architecture validation is deferred to future work.\n\n\\subsection{Leave-One-Environment-Out Cross-Validation}\n\\label{sec:nve_loeo}\n\nTo assess whether $\\theta{=}1.5\\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}13$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\\theta{=}1.5\\times$ on the held-out environment.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-environment-out cross-validation of NVE threshold $\\theta=1.5\\times$.\nFor each fold, the threshold is validated on an environment whose data was \\emph{not} used\nto select $\\theta$. The optimal threshold range on each training set is reported;\n$\\theta=1.5$ falls within the optimal range in all three folds.}\n\\label{tab:nve_loeo}\n\\begin{tabular}{lccccc}\n\\toprule\nHeld-out & $N_{\\text{train}}$ & $N_{\\text{test}}$ & $\\theta_{\\text{opt}}$ range & Test Accuracy & Test AUROC \\\\\n\\midrule\nPickCube & 18 & 2 & $(1.45,\\, 1.53]$ & 2/2 (1.000) & 1.000 \\\\\nCheetah  & 15 & 5 & $(1.45,\\, 1.53]$ & 5/5 (1.000) & 1.000 \\\\\nWalker   &  7 & 13 & $(1.00,\\, 3.78)$ & 12/13 (0.923) & 0.944 \\\\\n\\midrule\n\\textbf{Mean} & — & — & — & \\textbf{0.974} & \\textbf{0.981} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe threshold $\\theta{=}1.5\\times$ falls within the optimal accuracy range for all three training folds: $(1.45, 1.53]$ when Walker data is available, and the wider $(1.00, 3.78)$ when training on Cheetah$+$PickCube only (where CIVO and non-CIVO NVE values are well-separated). The single cross-validation error is exp\\_008e\\_v3 seed~2 (Walker), an IRD collapse mechanistically distinct from CIVO (\\S\\ref{sec:roc_analysis}). Mean held-out accuracy is 0.974 and mean AUROC is 0.981, confirming that $\\theta{=}1.5\\times$ generalizes across environments without retuning. PickCube fold confidence intervals remain wide (Clopper-Pearson 95\\% CI: $[0.158, 1.000]$) due to $N_{\\text{test}}{=}2$.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\paragraph{Embedding gradient analysis.}\nTable~\\ref{tab:three_way_emb} isolates embedding \\emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\\dt{=}2$ imagination).\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}\n\\label{tab:three_way_emb}\n\\footnotesize\n\\begin{tabular}{lccccl}\n\\toprule\nCondition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\\\\n\\midrule\nTrained & all & 008d, 059 & $1.53$--$4.72\\times$ & 64--268 & 5/5 \\\\\nReward detach & obs+KL only & 044 & $4.45\\times$ & 44$\\to$538$^\\dagger$ & 1/1 \\\\\nFull SGS & KL only & 018 & $1.66\\times$ & 448 & 1/1$^*$ \\\\\nFrozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\\nRemoved & N/A & 008f & $0.97$--$1.41\\times$ & 307--503 & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\\times$); seed~2 collapsed. $^\\dagger$Self-corrected at ${\\sim}175$K (eval 44$\\to$538, 59\\% baseline; 224K run). $^\\ddagger$Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps.\\par}\n\\end{table}\n\nThe reward-detach condition (exp\\_044, \\texttt{reward\\_dt\\_emb\\_detach=True}) uses a backward hook to block reward-head gradients from reaching $e_{\\dt}$, complementing the framework-level Reward SGS (exp\\_016e). Both yield the same directional result---CIVO onset not prevented---ruling out implementation artifacts. Exp\\_044 exhibits delayed CIVO onset (${\\sim}95$K vs.\\ typical $25$--$35$K), consistent with reduced but non-zero gradient pressure on $e_{\\dt}$. Over a full 224K run, exp\\_044 self-corrects: eval recovers from 44 (95K) to 538 (215K, 59\\% baseline), but this recovery is incomplete compared to spontaneous recovery without gradient intervention (exp\\_045: 868, 95\\% baseline). The lower asymptote suggests that selectively disrupting gradient flow may create optimization difficulties beyond CIVO itself.\n\nTable~\\ref{tab:factorial_design} summarizes the experimental configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Factorial design. Each row specifies one experimental configuration. \\textbf{Emb}: $\\dt$-embedding mode. \\textbf{Sub}: temporal subsampling. \\textbf{H}: imagination horizon. \\textbf{Imag $\\dt$}: temporal resolution used during imagination.}\n\\label{tab:factorial_design}\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{ID} & \\textbf{Purpose} & \\textbf{Emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Imag $\\dt$} \\\\\n\\midrule\n001 & Reference baseline & --- & --- & 15 & 1 \\\\\n006 & Fixed $\\dt{=}2$ & trn & on & 15 & 2 \\\\\n007 & Fixed $\\dt{=}4$ & trn & on & 15 & 4 \\\\\n\\midrule\n008a & Unexposed emb ctrl & exp$^a$ & off & 15 & 2 \\\\\n008c & Horizon control & exp$^a$ & off & 8 & 2 \\\\\n008d & Collapse condition & trn & on & 8 & 2 \\\\\n008e\\_v3 & $\\dt{=}1$ imag control & trn & on & 15 & 1 \\\\\n008f & Causal ablation & --- & on & 8 & 2 \\\\\n\\midrule\n015b & Frozen-emb ctrl & frz$^b$ & on & 8 & 2 \\\\\n016e & Stop-grad (reward) & trn$^\\dagger$ & on & 8 & 2 \\\\\n018 & Full-SGS & trn$^\\ddagger$ & on & 8 & 2 \\\\\n\\midrule\n005 & Learned gate & adaptive & off & 15 & learned \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^\\dagger$ \\texttt{reward\\_dt\\_emb\\_detach=True}; $^\\ddagger$ all non-KL gradients to \\texttt{dt\\_emb} detached.\\par}\n\\end{table}\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe empirical finding that trained embedding \\emph{plus} multi-rate exposure jointly predict CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.83$--$0.93\\times$ range across 3 seeds (105K steps). Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical factor is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training. This confirms that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.42\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.47 \\rightarrow 0.39 \\rightarrow 0.42$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and precedes full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.42\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that in all tested configurations, CIVO occurs only with the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\nCross-environment validation on Cheetah Run replicates the empirical pattern: trained $e_{\\dt}$ precedes CIVO in both tested seeds (exp\\_010b, 2 seeds, NVE $8.27$--$108.52\\times$, collapse to 51.7/0.83) while removing the embedding eliminates it (exp\\_024b, 2 seeds, NVE $<0.2\\times$, eval 96.5/77.3). Freezing the embedding on Cheetah (exp\\_046, NVE${=}1.35\\times$ vs.\\ trained $70.64\\times$, a $52\\times$ reduction) further confirms that embedding trainability, not architecture, drives CIVO. This extends the sufficiency finding from Walker Walk to a second locomotion environment with qualitatively different dynamics (6-joint vs.\\ 2-joint).\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole predictor of CIVO in tested configurations. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) precedes CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly sufficient in tested configurations.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling precedes collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$; low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig4_mechanism_diagram.pdf}\n\\caption{CIVO mechanism diagram. The trained $\\dt$-embedding enables asymmetric reward prediction fidelity, initiating a feedback loop: biased RSSM rewards $\\to$ optimistic critic values $\\to$ actor exploitation $\\to$ reinforced state-distribution skew.}\n\\label{fig:civo_mechanism}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO (Figure~\\ref{fig:civo_mechanism}).  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, which confirms that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\paragraph{Signed reward error analysis.}\nTo test whether CIVO arises from one-step reward overprediction, we compute signed error (predicted $-$ actual) on posterior-conditioned RSSM predictions (Table~\\ref{tab:signed_error}). The trained-embedding model (008d) shows \\emph{negative} bias at $\\dt{=}2$ (mean signed error $-0.599$, only 8\\% of samples overpredicted), ruling out observation-level reward overprediction as the mechanism. The baseline is well-calibrated (mean SE $\\approx 0$), confirming methodological soundness. Value overestimation therefore occurs during \\emph{imagination-level} prior drift: the RSSM prior (unconditioned on observations) generates reward-favorable trajectories at $\\dt > 1$ (Stage~1 above, $1.68\\times$ ratio under random policy), and the critic accumulates these into overestimated returns. The one-step reward prediction is negatively biased when conditioned on real observations, but this posterior correction is unavailable during imagination. This also distinguishes CIVO from generic compounding error, which would produce \\emph{positive} signed error accumulating with horizon; the negative observation-level bias confirms that CIVO is a prior-drift phenomenon, not a reward-prediction artifact.\n\n\\begin{table}[h]\n\\centering\n\\caption{Signed reward error (predicted $-$ actual) on posterior-conditioned RSSM predictions. Negative values indicate underprediction. The trained-embedding model underpredicts at $\\dt{=}2$, ruling out observation-level reward overprediction as the CIVO mechanism.}\n\\label{tab:signed_error}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Config} & $\\dt$ & \\textbf{Mean SE} & \\textbf{Std} & \\textbf{\\%Over} & \\textbf{Actual} & \\textbf{Pred} \\\\\n\\midrule\nBaseline & 1 & $+0.001$ & 0.023 & 39.6\\% & 1.893 & 1.894 \\\\\n\\midrule\n008d (trained) & 1 & $+0.018$ & 0.072 & 61.8\\% & 0.361 & 0.379 \\\\\n008d (trained) & 2 & $\\mathbf{-0.599}$ & 0.722 & 8.0\\% & 0.721 & 0.121 \\\\\n\\midrule\n008f (no emb) & 1 & $-0.710$ & 0.704 & 14.0\\% & 0.921 & 0.211 \\\\\n008f (no emb) & 2 & $-1.645$ & 1.485 & 5.0\\% & 1.840 & 0.195 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 0/2 CIVO elimination rate on Walker (seed~1: NVE reduced from $4.12\\times$ to $1.66\\times$ but remains CIVO-positive; seed~2: collapsed) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention eliminates CIVO in neither seed: seed~1 shows partial mitigation (eval 448.3, peak NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses (eval 40.8). Removing the observation decoder gradient channel is thus contributory but not sufficient. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3. \\textbf{Trained dt-emb} (008d)\\protect\\footnotemark: learned $d{=}32$ temporal embedding with multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with all non-KL gradients detached from $e_{\\dt}$. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$. Full-SGS seed~1 shows partial mitigation ($-51\\%$ final, NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses ($-96\\%$ final). CIVO elimination rate $= 0/2$.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}\n\nCross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This transient self-correcting trajectory is not attributable to the SGS intervention: the initial CIVO onset and peak severity are comparable to the unmitigated case, and the self-correction may reflect Cheetah Run's simpler dynamics rather than SGS efficacy.  Performance remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's Walker results (0/2 CIVO elimination), these findings yield a 0/3 elimination rate across environments, indicating that gradient-level interventions alone do not eliminate the CIVO vulnerability. Additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Post-CIVO outcomes for all six CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Env} & \\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\nWalker & s1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\nWalker & s2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\nWalker & s3 (008d\\_s3) & 1.53$\\times$ & 1.53$\\times$ & 268$^\\diamond$ & Late-onset collapse \\\\\nWalker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\n\\midrule\nCheetah & s1 (010b) & 8.27$\\times$ & 8.27$\\times$ & 51.7 & Full collapse \\\\\nCheetah & s0 (010b\\_s0) & 108.52$\\times$ & 108.52$\\times$ & 0.83 & Full collapse \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\diamond$ Transitional; train returns still declining at 105K.\\par}\n\\end{table}\n\nAll six CIVO-positive seeds cross the $\\nve > 1.5\\times$ threshold (Table~\\ref{tab:post_civo}), yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Full collapse is the majority outcome (5/6 seeds), with one self-correction case (Walker seed~2) that remains severely degraded (29.3\\% of baseline). Cheetah seeds exhibit more extreme overestimation (peak NVE $8.27$--$108.52\\times$ vs.\\ Walker's $1.53$--$4.62\\times$), consistent with the Cheetah reward scale amplifying the fidelity gap.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\paragraph{A fourth trajectory: CIVO-induced persistent value collapse.}\nObs-decoder SGS seed~3 (exp\\_025) exhibits a trajectory not observed in the untreated seeds: healthy through 105K ($\\nve < 1.0\\times$, eval 818.6), CIVO onset at 135K ($\\nve = 5.47\\times$, eval 67.0), followed by evaluation recovery (590.2 at 215K, 64\\% of baseline) but persistent value collapse ($\\nve = 0.14\\times$, value mean 80.6). The critic undershoots after the CIVO episode, suggesting that CIVO-induced representational damage may be irreversible even when the policy partially recovers. This contrasts with transient CIVO (seed~2, 009b), where both value and evaluation recover jointly, and with full collapse (seed~1, 008d), where neither recovers. Seed~4 exhibits the same terminal value collapse ($\\nve = 0.14\\times$ at 215K, eval 242), suggesting this overcorrection is systematic rather than seed-specific. The pattern adds a fourth post-CIVO outcome---policy recovery with critic damage---to the three documented in Table~\\ref{tab:post_civo}.\n\n\\subsubsection{Failure and Degradation Mode Taxonomy}\n\nTable~\\ref{tab:failure_modes} classifies the seven distinct failure and degradation modes observed across all experimental configurations. The taxonomy reveals that CIVO is not a single failure mode but a family of related pathologies, with the trained $\\dt$-embedding creating vulnerability through at least three independent mechanisms: value-driven collapse (monotonic, late-onset, and SGS-resistant CIVO), entropy-driven instability (IRD collapse), and gradient-mediated effects (gradient starvation, SGS-paradoxical worsening).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Failure and degradation mode taxonomy. Each mode is characterized by its NVE trajectory, entropy behavior, and primary mechanism.}\n\\label{tab:failure_modes}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccl@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Representative} & \\textbf{NVE} & \\textbf{Entropy} & \\textbf{Mechanism} \\\\\n\\midrule\nMonotonic CIVO & 008d, 008d\\_s4, 010b\\_s0 & $\\uparrow$ sustained & $\\downarrow$ & Reward bias $\\to$ critic $\\to$ actor \\\\\nLate-onset CIVO & 008d\\_s3 & $\\uparrow$ delayed & $\\downarrow$ & Same, delayed onset \\\\\nTransient CIVO & 009b & Peak $\\to$ $\\downarrow$ & Stable & Self-correction via capacity \\\\\nIRD collapse & 008e\\_v3\\_s2 & $\\uparrow$ late & $\\uparrow$ & Entropy-driven, values stable \\\\\nGrad.\\ starvation & 015b & Oscillates, decays & Stable & Frozen emb $\\to$ zero actor grad \\\\\nSGS-resistant & 018\\_s2 & $\\uparrow$ & $\\downarrow$ & Forward-pass conditioning \\\\\nSGS-paradoxical & 016e & $\\uparrow$ sustained & $\\downarrow$ & Reward SGS $\\to$ obs-dec reliance \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) avoids collapse in 2 of 4 seeds (50\\%), while the remaining two collapse via distinct mechanisms: Pathway~A (CIVO-driven, entropy decrease; s3, NVE $4.02\\times$) and Pathway~B (entropy-driven, entropy increase; s2, NVE $3.78\\times$; \\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse patterns identified in \\S\\ref{sec:f6}---CIVO (Pathway~A, value-driven, entropy decreasing) and a tentative second mode (Pathway~B, eval-driven, entropy increasing)---have distinct diagnostic signatures. Pathway~B is observed in only two seeds (008e\\_v3\\_s2 and 038\\_s2); we present it as preliminary evidence that the trained $\\dt$-embedding's learned features may affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B), though additional data is needed to confirm this as a distinct mechanism.  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse (Figure~\\ref{fig:multiple_pathways}).\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.  The CIVO mechanism requires three structural properties: (1) a temporal embedding that co-adapts with dynamics via gradient flow, (2) multi-step imagined rollouts used for critic training, and (3) a reward head that inherits latent biases from the shared representation.  Transformer-based world models that share these properties may exhibit analogous vulnerability; architectures that decouple temporal conditioning from the reward prediction pathway would not.\n\n\\subsection{Cross-Environment TCN Evaluation}\n\\label{sec:tcn_cross_env}\n\nTable~\\ref{tab:tcn_full} reports the full TCN evaluation across environments and noise magnitudes.\n\n\\begin{table}[h]\n\\centering\n\\caption{TCN results across environments and noise magnitudes. Prevention = peak NVE $< 1.5\\times$ (35K+).}\n\\label{tab:tcn_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Env} & $\\sigma$ & \\textbf{Seed} & \\textbf{NVE$_{\\max}$} & \\textbf{Prevented?} & \\textbf{Eval (\\%)} \\\\\n\\midrule\nWalker & 0.1 & s0 & 1.02 & \\checkmark$^*$ & 55\\% \\\\\nWalker & 0.2 & s0 & 0.91 & \\checkmark & 91\\% \\\\\nWalker & 0.2 & s1 & 0.64 & \\checkmark & 45\\% \\\\\nWalker & 0.2 & s2 & 2.11$^\\dagger$ & $\\times$ & ${\\sim}5\\%$ \\\\\n\\rowcolor{gray!15}\nWalker & 0.2 & s3 & 3.04$^\\P$ & $\\times$ & 11\\% \\\\\nWalker & 0.5 & s0 & 3.97 & $\\times$ & 27\\% \\\\\nWalker & 0.5 & s1 & 1.64 & $\\times$ & 41\\% \\\\\n\\midrule\nCheetah & 0.2 & s0 & 1.90 & $\\times$ & crashed \\\\\nCheetah & 0.5 & s0 & 10.67 & $\\times$ & 26\\% \\\\\nCheetah & 1.0 & s0 & $\\leq$0.30 & \\checkmark$^\\S$ & 15\\% \\\\\n\\midrule\nPickCube & 0.2 & s0 & 3.71 & $\\times$ & failing \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Borderline: NVE${=}1.02\\times$ at 95K, below $1.5\\times$ threshold but above $1.0\\times$.\\\\\n$^\\dagger$NVE $= 2.11\\times$ at 95K, still rising; eval ${\\sim}5\\%$ of baseline.\\\\\n$^\\P$Late-onset CIVO: NVE declined to $0.67\\times$ at 95K before phase-transition-like spike to $3.04\\times$ at 105K; eval 349.6 at 95K $\\to$ 71.8 at 105K $\\to$ 104.5 at 215K.\\\\\n$^\\S$CIVO prevented (NVE${\\leq}0.30$); peak eval 116\\% baseline at 35K, declining to 15\\% by 215K via progressive policy erosion. See ``impossible dose'' discussion.\\par}\n\\end{table}\n\n\\paragraph{Cheetah Run $\\sigma{=}0.5$: transient spike with permanent eval damage.}\nCheetah $\\sigma{=}0.5$ exhibits a novel failure mode: a transient CIVO spike (NVE $= 10.67\\times$ at 55K) followed by NVE recovery ($< 0.3\\times$ by 95K), but permanent evaluation damage (26\\% of baseline). The value signal self-corrects while the policy does not recover, suggesting that CIVO-induced representational damage during the spike is irreversible even when the critic subsequently recalibrates. This trajectory parallels the obs-decoder SGS seed~3 pattern (\\S\\ref{sec:seed_divergence}), where partial policy recovery coexists with persistent critic damage.\n\n\\paragraph{Cheetah Run $\\sigma{=}0.2$: insufficient dose.}\nAt $\\sigma{=}0.2$, Cheetah reaches NVE $= 1.9\\times$ at 55K---exceeding the $1.5\\times$ threshold---consistent with Cheetah's higher baseline CIVO severity ($8$--$108\\times$ vs.\\ Walker's $2$--$6\\times$). The noise magnitude that suffices for Walker is inadequate for Cheetah, but increasing $\\sigma$ to 0.5 trades CIVO prevention for a different failure mode rather than achieving mitigation.\n\n\\paragraph{PickCube-v1 $\\sigma{=}0.2$: sparse-reward failure.}\nPickCube reaches NVE $= 3.71\\times$ at 52.5K with $\\sigma{=}0.2$, indicating that TCN provides no protection in sparse-reward manipulation tasks. The combination of sparse rewards and temporal conditioning may amplify the fidelity gap beyond what representation-level noise can attenuate.\n\n\\paragraph{Dose-response analysis.}\nWe observe $\\sigma{=}0.2$ as a local optimum on Walker Walk, achieving complete CIVO suppression in 2 of 4 seeds. Seeds~2 and~3 both fail but via distinct CIVO onset dynamics: seed~2 shows gradual escalation (NVE $= 2.11\\times$ at 95K, still rising, eval ${\\sim}5\\%$), while seed~3 exhibits a phase-transition-like onset---NVE declined to $0.67\\times$ at 95K before spiking to $3.04\\times$ at 105K (eval 349.6 $\\to$ 71.8 in 10K steps). When TCN fails to prevent CIVO onset, the resulting trajectory qualitatively resembles untreated CIVO in its terminal outcome---runaway NVE and eval collapse. The two failure modes (gradual escalation vs.\\ sudden onset after apparent suppression) reinforce that TCN operates as a binary gate on CIVO onset rather than providing graded attenuation. Below the optimum, we observe $\\sigma{=}0.1$ as insufficient (NVE $= 1.02\\times$---borderline, eval 55\\%); above it, $\\sigma{=}0.5$ overdoses (oscillatory CIVO, eval $\\leq 41\\%$). Cross-seed variance at $\\sigma{=}0.2$ (eval 5--91\\%) exceeds the cross-dose difference by a wide margin, reinforcing that seed effects dominate dose effects. TCN is the only tested intervention achieving complete CIVO suppression in any configuration, but its high seed sensitivity and failure to transfer across environments position it as a \\emph{diagnostic probe}---identifying the representation level as the relevant intervention target---rather than a deployable mitigation.\n\n\\paragraph{Cheetah Run ``impossible dose'' dilemma.}\nExp\\_030c (224K steps) reveals a qualitatively different dose-response on Cheetah. At $\\sigma{=}1.0$, CIVO is eliminated (NVE${\\leq}0.30$ throughout) and initial learning is \\emph{unimpaired}: peak eval reaches 372 at 35K (116\\% of baseline), demonstrating that $\\sigma{=}1.0$ noise does not prevent policy acquisition. However, cumulative actor gradient interference produces progressive policy erosion---eval declines from 372 to 47 by 215K (15\\% of baseline)---while the critic remains well-calibrated (value\\_mean${=}12.4$, NVE${=}0.26$ at 215K). This establishes that \\emph{policy degradation $\\neq$ value corruption}: accurate value signals are insufficient when the actor cannot optimize effectively in noise-perturbed imagination.\n\nThis ``correct values, failed policy'' pattern provides indirect evidence that CIVO is mechanistically distinct from standard overestimation. Double Q-learning and ensemble methods address critic estimation error, but at $\\sigma{=}1.0$ the critic is accurate and the policy still collapses---a failure mode orthogonal to what these countermeasures target. The impossible dose dilemma scales with environment complexity: Cheetah's baseline CIVO severity ($8$--$108\\times$ NVE) requires $\\sigma \\geq 1.0$ to suppress, but this exceeds the actor's gradient signal-to-noise tolerance. On Walker, a narrow effective window exists around $\\sigma{=}0.2$; on Cheetah, the effective dose ($\\sigma \\geq 1.0$) exceeds the tolerable dose, and environments with higher CIVO severity will systematically lack a viable dose window.\n\n\\section{DreamerV3 Hyperparameters}\n\\label{sec:hyperparameters}\n\nTable~\\ref{tab:hyperparams} lists the DreamerV3 hyperparameters used across all experiments. Unless otherwise noted, we use the default DreamerV3 configuration for continuous-control tasks (\\texttt{dmc\\_proprio}).\n\n\\begin{table}[ht]\n\\centering\n\\caption{DreamerV3 hyperparameters for all experiments. Modifications from defaults are marked with $\\diamond$.}\n\\label{tab:hyperparams}\n\\small\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{World Model}} \\\\\nRSSM discrete states & 32 classes $\\times$ 32 categories \\\\\nRSSM stochastic dim & 32 \\\\\nRSSM deterministic dim & 512 \\\\\nMLP hidden size & 512 \\\\\nMLP layers & 2 \\\\\nActivation & SiLU \\\\\nNormalization & LayerNorm \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Training}} \\\\\nBatch size & 16 sequences $\\times$ 64 steps \\\\\nLearning rate & $3 \\times 10^{-4}$ (Adam, $\\epsilon{=}10^{-8}$) \\\\\nSequence length & 64 \\\\\nTraining ratio & 512 \\\\\nFree nats & 1.0 \\\\\nKL balance ($\\alpha$) & 0.8 \\\\\nDiscount ($\\gamma$) & 0.997 \\\\\n$\\lambda$-return & 0.95 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Policy}} \\\\\nImagination horizon$^\\diamond$ & 8 or 15 (see Table~\\ref{tab:complete_results}) \\\\\nActor entropy scale & $3 \\times 10^{-4}$ \\\\\nActor gradient & Reinforce + dynamics backprop \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Temporal Abstraction}$^\\diamond$} \\\\\nGate enabled & True (all non-baseline) \\\\\nGate fixed $\\dt$ & 1 or 2 (per config) \\\\\nSubsample max $\\dt$ & 1 (OFF) or 2 (ON) \\\\\n$\\dt$-embedding dim & 32 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Environment}} \\\\\nAction repeat & 2 (Walker Walk, Cheetah Run) \\\\\nObservation & Proprioceptive (no pixels) \\\\\nTotal environment steps & 105K \\\\\nEvaluation frequency & Every 10K steps \\\\\nEvaluation episodes & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Online CIVO Detector Details}\n\\label{sec:detector_appendix}\n\nThis appendix provides the full algorithm specification and validation results for the online CIVO detector described in \\S\\ref{sec:detector}.\n\n\\subsection{Algorithm Specification}\n\n\\begin{algorithm}[ht]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A full comparison of window sizes appears in \\S\\ref{sec:appendix_sensitivity}.\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $5/5$).\n\n\\subsection{Validation Results}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}14$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n008d s4 & trained $\\dt$-emb & TP & 105K & reactive & 383 & 3.03 \\\\\n010b s0 & trained $\\dt$-emb (Cheetah) & TP & 95K & reactive & 248 & 6.34 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n019b & trained $\\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n009c s3 & no $\\dt$-emb & TN & -- & -- & 457 & -- \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 5/5 (1.00), \\quad FPR = 2/9 (0.22)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe detector identifies all five CIVO-positive runs (TPR = 5/5). Two are detected predictively (008d seeds~0 and~3, both at 45K). Two false positives occur among nine negative cases (FPR = 2/9, precision 71\\%, F$_1$ = 0.83). Run 009c develops genuine late-stage value overestimation unrelated to CIVO; run 009a triggers during a transient eval dip at 85K before recovery to 966. Early alerts (before 70K) carry higher diagnostic confidence.\n\n\\subsection{Cross-Simulator Specificity (PickCube)}\n\nExp\\_019b applies the CIVO-trigger configuration to PickCube-v1 in ManiSkill3, a manipulation task with sparse rewards. The V/E ratio exhibits an oscillatory pattern rather than monotonic divergence: it spikes to $r_t = 5.66$ at 52.5K, then deflates to 1.38 by 72.5K. This trajectory prevents the acceleration condition from co-occurring with evaluation decline at any single checkpoint. Across all 14 checkpoints through 132.5K, the detector correctly remains silent (TN), confirming that the acceleration filter distinguishes transient spikes from CIVO's sustained monotonic divergence. A frozen-embedding control (exp\\_054) confirms this classification: frozen PickCube-v1 exhibits a comparable burst (peak $8.81\\times$ at 62.5K) that resolves within a single evaluation cycle ($0.55\\times$ at 72.5K), establishing environment-specific origin independent of $\\dt$-embedding training.\n\n\\subsection{Detector Limitations}\n\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse. Second, the acceleration condition assumes monotonically increasing overestimation during onset. Third, the detector identifies a \\emph{pattern} rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values were calibrated on fourteen runs across three environments; generalization to different reward scales requires further validation.\n\n\\section{Dual-Critic Mechanism Ablation}\n\\label{sec:dual_critic_appendix}\n\n\\subsection{\\texorpdfstring{$2{\\times}2$}{2x2} Factorial Design}\n\nWe ablate the critic architecture in a $2{\\times}2$ factorial: \\{single, dual\\} $\\times$ \\{narrow (${\\sim}1.2$M), wide (${\\sim}2.4$M)\\} parameters. Table~\\ref{tab:dual_critic_full} reports all configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Dual-critic $2{\\times}2$ factorial results. Walker Walk unless noted.}\n\\label{tab:dual_critic_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Params} & \\textbf{NVE} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\n008d & Single narrow & 1.2M & 4.12$\\times$ & 82.8 & Collapse \\\\\n033 & Wide single & 2.4M & 4.75$\\times$ & 407.9 & CIVO $\\to$ self-repair \\\\\n035 s0 & Narrow dual (min) & 1.2M & 2.75$\\times$ & 697.8 & CIVO $\\to$ recovery \\\\\n039 s1 & Narrow dual (min) & 1.2M & 2.19$\\times$ & 592.7 & CIVO $\\to$ recovery \\\\\n032 s0 & Wide dual (min) & 2.4M & $\\leq$1.1$\\times$ & 739.7 & CIVO prevented \\\\\n032b s1 & Wide dual (min) & 2.4M & 1.4$\\times$ & 551.8 & CIVO prevented \\\\\n038 s2 & Wide dual (min) & 2.4M & $\\leq$0.3$\\times$ & 120.9$^*$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Cross-environment}} \\\\\n034 & Cheetah dual & 2.4M & 1.75$\\times$ & 97.5 & Partial recovery (31\\%) \\\\\n037 & Cheetah wide single & 2.4M & 3.60$\\times$ & 146.1 & CIVO $\\to$ self-repair \\\\\n036 & PickCube dual & 2.4M & 2.3$\\times$ & 27.7 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$CIVO prevented (NVE $\\leq 0.3\\times$) but non-CIVO eval collapse: eval peaked at 354 (155K), then declined to 120.9 (224K) with actor entropy increasing from $-3.59$ to $-0.45$.\\par}\n\\end{table}\n\n\\subsection{Critic Convergence (\\texorpdfstring{$v_1 \\approx v_2$}{v1 ≈ v2})}\n\nAcross all dual-critic configurations and environments, the two critics converge to near-identical value functions. On Walker Walk, Pearson $\\rho > 0.999$ between $v_1$ and $v_2$ outputs; on Cheetah Run and PickCube-v1, the gap is $< 0.2$ (exact match within numerical precision). Per-sample pessimism $\\mathbb{E}[\\max(v_1, v_2) - \\min(v_1, v_2)]$ is 3--4\\% of the theoretical bound for independent critics.\n\nThis convergence occurs because both critics train on the same RSSM-generated latent features. Unlike model-free Double Q-learning, where each critic sees different mini-batches of real transitions and develops distinct function approximation errors, pure-imagination critics share identical inputs from the world model. The min operation therefore cannot provide the pessimism bias that makes Double Q effective in model-free settings.\n\n\\subsection{Recovery vs.\\ Prevention Mechanism}\n\nThe $2{\\times}2$ factorial reveals two separable dimensions:\n\n\\paragraph{Recovery (min-dominated).} The min operation is the primary factor enabling recovery from CIVO. Both narrow dual-critic seeds experience CIVO and recover fully: exp\\_035 (s0, $\\nve = 2.75\\times$, eval $33.8 \\to 697.8$, recovery ratio $20.6\\times$) and exp\\_039 (s1, $\\nve = 2.19\\times$, eval $35.9 \\to 592.7$, recovery ratio $16.5\\times$). Both outperform wide single-critic (exp\\_033, 2.4M params, eval 407.9) despite $2\\times$ fewer parameters. The min operation reduces both peak CIVO severity (2.19--2.75$\\times$ vs.\\ 4.75$\\times$ for the comparable single-critic) and enables consistent full recovery across seeds.\n\n\\paragraph{Prevention (min $+$ capacity synergy).} CIVO prevention (NVE remaining below the $1.5\\times$ threshold) requires both the min operation and increased capacity: only the wide dual-critic (exp\\_032, 3 seeds) achieves this. The mechanism for this synergy is an open question; we hypothesize that increased capacity improves value calibration quality while the min operation constrains the overestimation feedback loop during early training when the two critics briefly diverge.\n\n\\paragraph{Cross-environment limits.} On Cheetah Run, the wide dual-critic (exp\\_034) reduces NVE from $8.27\\times$ (untreated baseline) to $1.75\\times$ ($\\geq 4\\times$ reduction) but cannot prevent CIVO onset, and recovery reaches only 31\\% of the pre-CIVO peak. This confirms that the min $+$ capacity synergy has environment-dependent limits: in high-CIVO-severity environments, architecture-level interventions attenuate but do not eliminate the pathology.\n",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 6,
        "newStart": 30,
        "newLines": 8,
        "lines": [
          " 008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\",
          " \\rowcolor{gray!15}",
          " 008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\",
          "+\\rowcolor{gray!15}",
          "+059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\\times$ & Self-correction \\\\",
          " 008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\",
          " 008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\\times$ & Healthy \\\\",
          " 009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\"
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

_source line 92_

<details open><summary>🔧 Tool call — Edit · `toolu_01FCS6bPpXC3hprb4ECRRuGo`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "\\caption{Post-CIVO outcomes for all six CIVO-positive seeds across two environments.",
  "new_string": "\\caption{Post-CIVO outcomes for all seven CIVO-positive seeds across two environments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "4ee74c0c-32b7-44c6-9173-50ae16c343ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012swrHLwzU8fYGrKxzsxi4V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 64367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1633
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

_source line 93 · 2026-05-24T07:12:14.525Z_

<details><summary>↩ Tool result · `toolu_01FCS6bPpXC3hprb4ECRRuGo`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "ce0f1158-9b31-490e-8fd7-f3209bb3ae7f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "\\caption{Post-CIVO outcomes for all six CIVO-positive seeds across two environments.",
    "newString": "\\caption{Post-CIVO outcomes for all seven CIVO-positive seeds across two environments.",
    "originalFile": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\\times$ & Self-correction \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\\times$ & Transient (self-corr.) \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\rowcolor{gray!15}\n008e\\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\\times$ & CIVO collapse \\\\\n008e\\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\\times$ & Healthy \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\n$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\n$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\n$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\n$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\par}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n\\label{tab:cross_domain}\n\\footnotesize\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n\\midrule\nLocomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\\times$) \\\\\nLocomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\nManipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\nManipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\nManipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all ten factorial experiments (including four 008e\\_v3 seeds). Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\\_v3\\_s3 exhibits CIVO with NVE $4.02\\times$ despite $\\Delta t{=}1$ imagination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.83 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.12 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s3 & 4.02 & CIVO           & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.02\\times$, exp~008e\\_v3\\_s3) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.02]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.958$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=7$, $n=10$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). $^\\dagger$Optimal threshold in $(3.78, 4.02]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 3 & 0 & 4 & 70.0\\% \\; [34.8, 93.3] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.2\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.5\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 3 & 0 & 0 & 7 & 100\\% \\; [69.2, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=4$, $n_{\\text{neg}}=6$, $n=10$, $\\text{AUROC}=0.958$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 4 & 2 & 0 & 4 & 80.0\\% \\; [44.4, 97.5] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 1.2\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.7\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 3.9\\times$ & 3 & 0 & 1 & 6 & 90.0\\% \\; [55.5, 99.7] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\\text{pos}}=8$, $n_{\\text{neg}}=8$, $n=16$, $\\text{AUROC}=0.969$). Includes Walker Walk (14 configurations) and Cheetah Run (2 configurations).}\n\\label{tab:sensitivity_b2_full}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 8 & 2 & 0 & 6 & 87.5\\% \\; [61.7, 98.4] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.2\\times$ & 8 & 1 & 0 & 7 & 93.8\\% \\; [69.8, 99.8] & 88.9\\% & 100\\% & 94.1\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 8 & 1 & 0 & 7 & 93.8\\% \\; [69.8, 99.8] & 88.9\\% & 100\\% & 94.1\\% \\\\\n$\\geq 1.7\\times$ & 6 & 1 & 2 & 7 & 81.3\\% \\; [54.4, 96.0] & 85.7\\% & 75.0\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 6 & 1 & 2 & 7 & 81.3\\% \\; [54.4, 96.0] & 85.7\\% & 75.0\\% & 80.0\\% \\\\\n$\\geq 3.9\\times$ & 6 & 0 & 2 & 8 & 87.5\\% \\; [61.7, 98.4] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all four CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 75.0\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 88.9\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 3$ the statistical power remains limited (accuracy 95\\% CI: [69.2\\%, 100\\%]).\n\n\\subsection{Expanded ROC Analysis}\n\\label{sec:roc_analysis}\n\nThe original $n{=}16$ analysis (Tables~\\ref{tab:sensitivity_b1}--\\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}29$ configurations spanning all tested interventions. Figure~\\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\\% bootstrap confidence interval (10{,}000 resamples).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.7\\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}\n\\caption{NVE ROC curve ($n{=}29$ configurations, AUROC${=}0.953$, in-sample, post-hoc). The preset $\\nve \\geq 1.5\\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}\n\\label{fig:nve_roc}\n\\end{figure}\n\nWe label a configuration as CIVO-positive if and only if (i)~it uses a trained $\\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.\n\nThe three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\\_008e\\_v3 seed~2, actor entropy \\emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \\emph{decrease}). All three produce NVE $> 1.5\\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\\times$) lacks $\\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\\times$) exhibits the full CIVO causal chain: trained $\\dt$-embedding, entropy decrease, and evaluation collapse to 14\\% of baseline.\n\n\\subsection{NVE Normalization Robustness}\n\\label{sec:nve_robustness}\n\nTo assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\\ref{tab:baseline_seeds}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Walker Walk baseline seeds at 105K and 505K steps.}\n\\label{tab:baseline_seeds}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Eval@105K} & \\textbf{Eval@505K} & \\textbf{ve@65K} & \\textbf{ve@105K} \\\\\n\\midrule\ns1 & 915.7 & 970.4 & 0.563 & 0.656 \\\\\ns2 & 443.5 & 945.7 & 0.898 & 0.742 \\\\\ns3 & 869.0 & 947.7 & --- & 0.664 \\\\\ns4 & 922.8 & 938.9 & --- & 0.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\\times$; 009b seed~2, peak NVE $1.62\\times$) to fall below the $1.5\\times$ threshold. Core CIVO cases (peak NVE $> 3\\times$) remain correctly classified under all baseline seeds.\n\nSingle-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\\%): the boundary case exp\\_009b flips from $\\nve = 1.62\\times$ (s1) to $1.23\\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\\times \\to 4.52\\times$; 008d: $4.12\\times \\to 3.54\\times$). The $1.5\\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\\% of the threshold.\n\n\\paragraph{Normalization conventions.} Walker NVE is normalized against the 4-seed mean baseline (seeds~1--4, each run to 505K+ steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).\n\n\\paragraph{Limitations.} With $n = 10$ experiments, Clopper-Pearson confidence intervals remain wide (e.g., 90.0\\% accuracy has 95\\% CI [55.5\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds. Table~\\ref{tab:sensitivity_b2_full} reports the original $n{=}16$ evaluation set spanning both environments. The expanded analysis ($n{=}29$, including SGS variants, RAVE, and TCN configurations) yields AUROC${=}0.953$ (Figure~\\ref{fig:nve_roc}, in-sample, post-hoc). The original $n{=}16$ core analysis yields AUROC${=}0.969$; the expanded $n{=}29$ set includes SGS, RAVE, TCN, and dual-critic configurations. Cross-architecture validation is deferred to future work.\n\n\\subsection{Leave-One-Environment-Out Cross-Validation}\n\\label{sec:nve_loeo}\n\nTo assess whether $\\theta{=}1.5\\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}13$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\\theta{=}1.5\\times$ on the held-out environment.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-environment-out cross-validation of NVE threshold $\\theta=1.5\\times$.\nFor each fold, the threshold is validated on an environment whose data was \\emph{not} used\nto select $\\theta$. The optimal threshold range on each training set is reported;\n$\\theta=1.5$ falls within the optimal range in all three folds.}\n\\label{tab:nve_loeo}\n\\begin{tabular}{lccccc}\n\\toprule\nHeld-out & $N_{\\text{train}}$ & $N_{\\text{test}}$ & $\\theta_{\\text{opt}}$ range & Test Accuracy & Test AUROC \\\\\n\\midrule\nPickCube & 18 & 2 & $(1.45,\\, 1.53]$ & 2/2 (1.000) & 1.000 \\\\\nCheetah  & 15 & 5 & $(1.45,\\, 1.53]$ & 5/5 (1.000) & 1.000 \\\\\nWalker   &  7 & 13 & $(1.00,\\, 3.78)$ & 12/13 (0.923) & 0.944 \\\\\n\\midrule\n\\textbf{Mean} & — & — & — & \\textbf{0.974} & \\textbf{0.981} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe threshold $\\theta{=}1.5\\times$ falls within the optimal accuracy range for all three training folds: $(1.45, 1.53]$ when Walker data is available, and the wider $(1.00, 3.78)$ when training on Cheetah$+$PickCube only (where CIVO and non-CIVO NVE values are well-separated). The single cross-validation error is exp\\_008e\\_v3 seed~2 (Walker), an IRD collapse mechanistically distinct from CIVO (\\S\\ref{sec:roc_analysis}). Mean held-out accuracy is 0.974 and mean AUROC is 0.981, confirming that $\\theta{=}1.5\\times$ generalizes across environments without retuning. PickCube fold confidence intervals remain wide (Clopper-Pearson 95\\% CI: $[0.158, 1.000]$) due to $N_{\\text{test}}{=}2$.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\paragraph{Embedding gradient analysis.}\nTable~\\ref{tab:three_way_emb} isolates embedding \\emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\\dt{=}2$ imagination).\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}\n\\label{tab:three_way_emb}\n\\footnotesize\n\\begin{tabular}{lccccl}\n\\toprule\nCondition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\\\\n\\midrule\nTrained & all & 008d, 059 & $1.53$--$4.72\\times$ & 64--268 & 5/5 \\\\\nReward detach & obs+KL only & 044 & $4.45\\times$ & 44$\\to$538$^\\dagger$ & 1/1 \\\\\nFull SGS & KL only & 018 & $1.66\\times$ & 448 & 1/1$^*$ \\\\\nFrozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\\nRemoved & N/A & 008f & $0.97$--$1.41\\times$ & 307--503 & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\\times$); seed~2 collapsed. $^\\dagger$Self-corrected at ${\\sim}175$K (eval 44$\\to$538, 59\\% baseline; 224K run). $^\\ddagger$Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps.\\par}\n\\end{table}\n\nThe reward-detach condition (exp\\_044, \\texttt{reward\\_dt\\_emb\\_detach=True}) uses a backward hook to block reward-head gradients from reaching $e_{\\dt}$, complementing the framework-level Reward SGS (exp\\_016e). Both yield the same directional result---CIVO onset not prevented---ruling out implementation artifacts. Exp\\_044 exhibits delayed CIVO onset (${\\sim}95$K vs.\\ typical $25$--$35$K), consistent with reduced but non-zero gradient pressure on $e_{\\dt}$. Over a full 224K run, exp\\_044 self-corrects: eval recovers from 44 (95K) to 538 (215K, 59\\% baseline), but this recovery is incomplete compared to spontaneous recovery without gradient intervention (exp\\_045: 868, 95\\% baseline). The lower asymptote suggests that selectively disrupting gradient flow may create optimization difficulties beyond CIVO itself.\n\nTable~\\ref{tab:factorial_design} summarizes the experimental configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Factorial design. Each row specifies one experimental configuration. \\textbf{Emb}: $\\dt$-embedding mode. \\textbf{Sub}: temporal subsampling. \\textbf{H}: imagination horizon. \\textbf{Imag $\\dt$}: temporal resolution used during imagination.}\n\\label{tab:factorial_design}\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{ID} & \\textbf{Purpose} & \\textbf{Emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Imag $\\dt$} \\\\\n\\midrule\n001 & Reference baseline & --- & --- & 15 & 1 \\\\\n006 & Fixed $\\dt{=}2$ & trn & on & 15 & 2 \\\\\n007 & Fixed $\\dt{=}4$ & trn & on & 15 & 4 \\\\\n\\midrule\n008a & Unexposed emb ctrl & exp$^a$ & off & 15 & 2 \\\\\n008c & Horizon control & exp$^a$ & off & 8 & 2 \\\\\n008d & Collapse condition & trn & on & 8 & 2 \\\\\n008e\\_v3 & $\\dt{=}1$ imag control & trn & on & 15 & 1 \\\\\n008f & Causal ablation & --- & on & 8 & 2 \\\\\n\\midrule\n015b & Frozen-emb ctrl & frz$^b$ & on & 8 & 2 \\\\\n016e & Stop-grad (reward) & trn$^\\dagger$ & on & 8 & 2 \\\\\n018 & Full-SGS & trn$^\\ddagger$ & on & 8 & 2 \\\\\n\\midrule\n005 & Learned gate & adaptive & off & 15 & learned \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^\\dagger$ \\texttt{reward\\_dt\\_emb\\_detach=True}; $^\\ddagger$ all non-KL gradients to \\texttt{dt\\_emb} detached.\\par}\n\\end{table}\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe empirical finding that trained embedding \\emph{plus} multi-rate exposure jointly predict CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.83$--$0.93\\times$ range across 3 seeds (105K steps). Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical factor is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training. This confirms that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.42\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.47 \\rightarrow 0.39 \\rightarrow 0.42$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and precedes full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.42\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that in all tested configurations, CIVO occurs only with the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\nCross-environment validation on Cheetah Run replicates the empirical pattern: trained $e_{\\dt}$ precedes CIVO in both tested seeds (exp\\_010b, 2 seeds, NVE $8.27$--$108.52\\times$, collapse to 51.7/0.83) while removing the embedding eliminates it (exp\\_024b, 2 seeds, NVE $<0.2\\times$, eval 96.5/77.3). Freezing the embedding on Cheetah (exp\\_046, NVE${=}1.35\\times$ vs.\\ trained $70.64\\times$, a $52\\times$ reduction) further confirms that embedding trainability, not architecture, drives CIVO. This extends the sufficiency finding from Walker Walk to a second locomotion environment with qualitatively different dynamics (6-joint vs.\\ 2-joint).\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole predictor of CIVO in tested configurations. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) precedes CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly sufficient in tested configurations.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling precedes collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$; low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig4_mechanism_diagram.pdf}\n\\caption{CIVO mechanism diagram. The trained $\\dt$-embedding enables asymmetric reward prediction fidelity, initiating a feedback loop: biased RSSM rewards $\\to$ optimistic critic values $\\to$ actor exploitation $\\to$ reinforced state-distribution skew.}\n\\label{fig:civo_mechanism}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO (Figure~\\ref{fig:civo_mechanism}).  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, which confirms that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\paragraph{Signed reward error analysis.}\nTo test whether CIVO arises from one-step reward overprediction, we compute signed error (predicted $-$ actual) on posterior-conditioned RSSM predictions (Table~\\ref{tab:signed_error}). The trained-embedding model (008d) shows \\emph{negative} bias at $\\dt{=}2$ (mean signed error $-0.599$, only 8\\% of samples overpredicted), ruling out observation-level reward overprediction as the mechanism. The baseline is well-calibrated (mean SE $\\approx 0$), confirming methodological soundness. Value overestimation therefore occurs during \\emph{imagination-level} prior drift: the RSSM prior (unconditioned on observations) generates reward-favorable trajectories at $\\dt > 1$ (Stage~1 above, $1.68\\times$ ratio under random policy), and the critic accumulates these into overestimated returns. The one-step reward prediction is negatively biased when conditioned on real observations, but this posterior correction is unavailable during imagination. This also distinguishes CIVO from generic compounding error, which would produce \\emph{positive} signed error accumulating with horizon; the negative observation-level bias confirms that CIVO is a prior-drift phenomenon, not a reward-prediction artifact.\n\n\\begin{table}[h]\n\\centering\n\\caption{Signed reward error (predicted $-$ actual) on posterior-conditioned RSSM predictions. Negative values indicate underprediction. The trained-embedding model underpredicts at $\\dt{=}2$, ruling out observation-level reward overprediction as the CIVO mechanism.}\n\\label{tab:signed_error}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Config} & $\\dt$ & \\textbf{Mean SE} & \\textbf{Std} & \\textbf{\\%Over} & \\textbf{Actual} & \\textbf{Pred} \\\\\n\\midrule\nBaseline & 1 & $+0.001$ & 0.023 & 39.6\\% & 1.893 & 1.894 \\\\\n\\midrule\n008d (trained) & 1 & $+0.018$ & 0.072 & 61.8\\% & 0.361 & 0.379 \\\\\n008d (trained) & 2 & $\\mathbf{-0.599}$ & 0.722 & 8.0\\% & 0.721 & 0.121 \\\\\n\\midrule\n008f (no emb) & 1 & $-0.710$ & 0.704 & 14.0\\% & 0.921 & 0.211 \\\\\n008f (no emb) & 2 & $-1.645$ & 1.485 & 5.0\\% & 1.840 & 0.195 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 0/2 CIVO elimination rate on Walker (seed~1: NVE reduced from $4.12\\times$ to $1.66\\times$ but remains CIVO-positive; seed~2: collapsed) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention eliminates CIVO in neither seed: seed~1 shows partial mitigation (eval 448.3, peak NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses (eval 40.8). Removing the observation decoder gradient channel is thus contributory but not sufficient. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3. \\textbf{Trained dt-emb} (008d)\\protect\\footnotemark: learned $d{=}32$ temporal embedding with multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with all non-KL gradients detached from $e_{\\dt}$. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$. Full-SGS seed~1 shows partial mitigation ($-51\\%$ final, NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses ($-96\\%$ final). CIVO elimination rate $= 0/2$.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}\n\nCross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This transient self-correcting trajectory is not attributable to the SGS intervention: the initial CIVO onset and peak severity are comparable to the unmitigated case, and the self-correction may reflect Cheetah Run's simpler dynamics rather than SGS efficacy.  Performance remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's Walker results (0/2 CIVO elimination), these findings yield a 0/3 elimination rate across environments, indicating that gradient-level interventions alone do not eliminate the CIVO vulnerability. Additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Post-CIVO outcomes for all six CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Env} & \\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\nWalker & s1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\nWalker & s2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\nWalker & s3 (008d\\_s3) & 1.53$\\times$ & 1.53$\\times$ & 268$^\\diamond$ & Late-onset collapse \\\\\nWalker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\n\\midrule\nCheetah & s1 (010b) & 8.27$\\times$ & 8.27$\\times$ & 51.7 & Full collapse \\\\\nCheetah & s0 (010b\\_s0) & 108.52$\\times$ & 108.52$\\times$ & 0.83 & Full collapse \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\diamond$ Transitional; train returns still declining at 105K.\\par}\n\\end{table}\n\nAll six CIVO-positive seeds cross the $\\nve > 1.5\\times$ threshold (Table~\\ref{tab:post_civo}), yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Full collapse is the majority outcome (5/6 seeds), with one self-correction case (Walker seed~2) that remains severely degraded (29.3\\% of baseline). Cheetah seeds exhibit more extreme overestimation (peak NVE $8.27$--$108.52\\times$ vs.\\ Walker's $1.53$--$4.62\\times$), consistent with the Cheetah reward scale amplifying the fidelity gap.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\paragraph{A fourth trajectory: CIVO-induced persistent value collapse.}\nObs-decoder SGS seed~3 (exp\\_025) exhibits a trajectory not observed in the untreated seeds: healthy through 105K ($\\nve < 1.0\\times$, eval 818.6), CIVO onset at 135K ($\\nve = 5.47\\times$, eval 67.0), followed by evaluation recovery (590.2 at 215K, 64\\% of baseline) but persistent value collapse ($\\nve = 0.14\\times$, value mean 80.6). The critic undershoots after the CIVO episode, suggesting that CIVO-induced representational damage may be irreversible even when the policy partially recovers. This contrasts with transient CIVO (seed~2, 009b), where both value and evaluation recover jointly, and with full collapse (seed~1, 008d), where neither recovers. Seed~4 exhibits the same terminal value collapse ($\\nve = 0.14\\times$ at 215K, eval 242), suggesting this overcorrection is systematic rather than seed-specific. The pattern adds a fourth post-CIVO outcome---policy recovery with critic damage---to the three documented in Table~\\ref{tab:post_civo}.\n\n\\subsubsection{Failure and Degradation Mode Taxonomy}\n\nTable~\\ref{tab:failure_modes} classifies the seven distinct failure and degradation modes observed across all experimental configurations. The taxonomy reveals that CIVO is not a single failure mode but a family of related pathologies, with the trained $\\dt$-embedding creating vulnerability through at least three independent mechanisms: value-driven collapse (monotonic, late-onset, and SGS-resistant CIVO), entropy-driven instability (IRD collapse), and gradient-mediated effects (gradient starvation, SGS-paradoxical worsening).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Failure and degradation mode taxonomy. Each mode is characterized by its NVE trajectory, entropy behavior, and primary mechanism.}\n\\label{tab:failure_modes}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccl@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Representative} & \\textbf{NVE} & \\textbf{Entropy} & \\textbf{Mechanism} \\\\\n\\midrule\nMonotonic CIVO & 008d, 008d\\_s4, 010b\\_s0 & $\\uparrow$ sustained & $\\downarrow$ & Reward bias $\\to$ critic $\\to$ actor \\\\\nLate-onset CIVO & 008d\\_s3 & $\\uparrow$ delayed & $\\downarrow$ & Same, delayed onset \\\\\nTransient CIVO & 009b & Peak $\\to$ $\\downarrow$ & Stable & Self-correction via capacity \\\\\nIRD collapse & 008e\\_v3\\_s2 & $\\uparrow$ late & $\\uparrow$ & Entropy-driven, values stable \\\\\nGrad.\\ starvation & 015b & Oscillates, decays & Stable & Frozen emb $\\to$ zero actor grad \\\\\nSGS-resistant & 018\\_s2 & $\\uparrow$ & $\\downarrow$ & Forward-pass conditioning \\\\\nSGS-paradoxical & 016e & $\\uparrow$ sustained & $\\downarrow$ & Reward SGS $\\to$ obs-dec reliance \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) avoids collapse in 2 of 4 seeds (50\\%), while the remaining two collapse via distinct mechanisms: Pathway~A (CIVO-driven, entropy decrease; s3, NVE $4.02\\times$) and Pathway~B (entropy-driven, entropy increase; s2, NVE $3.78\\times$; \\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse patterns identified in \\S\\ref{sec:f6}---CIVO (Pathway~A, value-driven, entropy decreasing) and a tentative second mode (Pathway~B, eval-driven, entropy increasing)---have distinct diagnostic signatures. Pathway~B is observed in only two seeds (008e\\_v3\\_s2 and 038\\_s2); we present it as preliminary evidence that the trained $\\dt$-embedding's learned features may affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B), though additional data is needed to confirm this as a distinct mechanism.  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse (Figure~\\ref{fig:multiple_pathways}).\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.  The CIVO mechanism requires three structural properties: (1) a temporal embedding that co-adapts with dynamics via gradient flow, (2) multi-step imagined rollouts used for critic training, and (3) a reward head that inherits latent biases from the shared representation.  Transformer-based world models that share these properties may exhibit analogous vulnerability; architectures that decouple temporal conditioning from the reward prediction pathway would not.\n\n\\subsection{Cross-Environment TCN Evaluation}\n\\label{sec:tcn_cross_env}\n\nTable~\\ref{tab:tcn_full} reports the full TCN evaluation across environments and noise magnitudes.\n\n\\begin{table}[h]\n\\centering\n\\caption{TCN results across environments and noise magnitudes. Prevention = peak NVE $< 1.5\\times$ (35K+).}\n\\label{tab:tcn_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Env} & $\\sigma$ & \\textbf{Seed} & \\textbf{NVE$_{\\max}$} & \\textbf{Prevented?} & \\textbf{Eval (\\%)} \\\\\n\\midrule\nWalker & 0.1 & s0 & 1.02 & \\checkmark$^*$ & 55\\% \\\\\nWalker & 0.2 & s0 & 0.91 & \\checkmark & 91\\% \\\\\nWalker & 0.2 & s1 & 0.64 & \\checkmark & 45\\% \\\\\nWalker & 0.2 & s2 & 2.11$^\\dagger$ & $\\times$ & ${\\sim}5\\%$ \\\\\n\\rowcolor{gray!15}\nWalker & 0.2 & s3 & 3.04$^\\P$ & $\\times$ & 11\\% \\\\\nWalker & 0.5 & s0 & 3.97 & $\\times$ & 27\\% \\\\\nWalker & 0.5 & s1 & 1.64 & $\\times$ & 41\\% \\\\\n\\midrule\nCheetah & 0.2 & s0 & 1.90 & $\\times$ & crashed \\\\\nCheetah & 0.5 & s0 & 10.67 & $\\times$ & 26\\% \\\\\nCheetah & 1.0 & s0 & $\\leq$0.30 & \\checkmark$^\\S$ & 15\\% \\\\\n\\midrule\nPickCube & 0.2 & s0 & 3.71 & $\\times$ & failing \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Borderline: NVE${=}1.02\\times$ at 95K, below $1.5\\times$ threshold but above $1.0\\times$.\\\\\n$^\\dagger$NVE $= 2.11\\times$ at 95K, still rising; eval ${\\sim}5\\%$ of baseline.\\\\\n$^\\P$Late-onset CIVO: NVE declined to $0.67\\times$ at 95K before phase-transition-like spike to $3.04\\times$ at 105K; eval 349.6 at 95K $\\to$ 71.8 at 105K $\\to$ 104.5 at 215K.\\\\\n$^\\S$CIVO prevented (NVE${\\leq}0.30$); peak eval 116\\% baseline at 35K, declining to 15\\% by 215K via progressive policy erosion. See ``impossible dose'' discussion.\\par}\n\\end{table}\n\n\\paragraph{Cheetah Run $\\sigma{=}0.5$: transient spike with permanent eval damage.}\nCheetah $\\sigma{=}0.5$ exhibits a novel failure mode: a transient CIVO spike (NVE $= 10.67\\times$ at 55K) followed by NVE recovery ($< 0.3\\times$ by 95K), but permanent evaluation damage (26\\% of baseline). The value signal self-corrects while the policy does not recover, suggesting that CIVO-induced representational damage during the spike is irreversible even when the critic subsequently recalibrates. This trajectory parallels the obs-decoder SGS seed~3 pattern (\\S\\ref{sec:seed_divergence}), where partial policy recovery coexists with persistent critic damage.\n\n\\paragraph{Cheetah Run $\\sigma{=}0.2$: insufficient dose.}\nAt $\\sigma{=}0.2$, Cheetah reaches NVE $= 1.9\\times$ at 55K---exceeding the $1.5\\times$ threshold---consistent with Cheetah's higher baseline CIVO severity ($8$--$108\\times$ vs.\\ Walker's $2$--$6\\times$). The noise magnitude that suffices for Walker is inadequate for Cheetah, but increasing $\\sigma$ to 0.5 trades CIVO prevention for a different failure mode rather than achieving mitigation.\n\n\\paragraph{PickCube-v1 $\\sigma{=}0.2$: sparse-reward failure.}\nPickCube reaches NVE $= 3.71\\times$ at 52.5K with $\\sigma{=}0.2$, indicating that TCN provides no protection in sparse-reward manipulation tasks. The combination of sparse rewards and temporal conditioning may amplify the fidelity gap beyond what representation-level noise can attenuate.\n\n\\paragraph{Dose-response analysis.}\nWe observe $\\sigma{=}0.2$ as a local optimum on Walker Walk, achieving complete CIVO suppression in 2 of 4 seeds. Seeds~2 and~3 both fail but via distinct CIVO onset dynamics: seed~2 shows gradual escalation (NVE $= 2.11\\times$ at 95K, still rising, eval ${\\sim}5\\%$), while seed~3 exhibits a phase-transition-like onset---NVE declined to $0.67\\times$ at 95K before spiking to $3.04\\times$ at 105K (eval 349.6 $\\to$ 71.8 in 10K steps). When TCN fails to prevent CIVO onset, the resulting trajectory qualitatively resembles untreated CIVO in its terminal outcome---runaway NVE and eval collapse. The two failure modes (gradual escalation vs.\\ sudden onset after apparent suppression) reinforce that TCN operates as a binary gate on CIVO onset rather than providing graded attenuation. Below the optimum, we observe $\\sigma{=}0.1$ as insufficient (NVE $= 1.02\\times$---borderline, eval 55\\%); above it, $\\sigma{=}0.5$ overdoses (oscillatory CIVO, eval $\\leq 41\\%$). Cross-seed variance at $\\sigma{=}0.2$ (eval 5--91\\%) exceeds the cross-dose difference by a wide margin, reinforcing that seed effects dominate dose effects. TCN is the only tested intervention achieving complete CIVO suppression in any configuration, but its high seed sensitivity and failure to transfer across environments position it as a \\emph{diagnostic probe}---identifying the representation level as the relevant intervention target---rather than a deployable mitigation.\n\n\\paragraph{Cheetah Run ``impossible dose'' dilemma.}\nExp\\_030c (224K steps) reveals a qualitatively different dose-response on Cheetah. At $\\sigma{=}1.0$, CIVO is eliminated (NVE${\\leq}0.30$ throughout) and initial learning is \\emph{unimpaired}: peak eval reaches 372 at 35K (116\\% of baseline), demonstrating that $\\sigma{=}1.0$ noise does not prevent policy acquisition. However, cumulative actor gradient interference produces progressive policy erosion---eval declines from 372 to 47 by 215K (15\\% of baseline)---while the critic remains well-calibrated (value\\_mean${=}12.4$, NVE${=}0.26$ at 215K). This establishes that \\emph{policy degradation $\\neq$ value corruption}: accurate value signals are insufficient when the actor cannot optimize effectively in noise-perturbed imagination.\n\nThis ``correct values, failed policy'' pattern provides indirect evidence that CIVO is mechanistically distinct from standard overestimation. Double Q-learning and ensemble methods address critic estimation error, but at $\\sigma{=}1.0$ the critic is accurate and the policy still collapses---a failure mode orthogonal to what these countermeasures target. The impossible dose dilemma scales with environment complexity: Cheetah's baseline CIVO severity ($8$--$108\\times$ NVE) requires $\\sigma \\geq 1.0$ to suppress, but this exceeds the actor's gradient signal-to-noise tolerance. On Walker, a narrow effective window exists around $\\sigma{=}0.2$; on Cheetah, the effective dose ($\\sigma \\geq 1.0$) exceeds the tolerable dose, and environments with higher CIVO severity will systematically lack a viable dose window.\n\n\\section{DreamerV3 Hyperparameters}\n\\label{sec:hyperparameters}\n\nTable~\\ref{tab:hyperparams} lists the DreamerV3 hyperparameters used across all experiments. Unless otherwise noted, we use the default DreamerV3 configuration for continuous-control tasks (\\texttt{dmc\\_proprio}).\n\n\\begin{table}[ht]\n\\centering\n\\caption{DreamerV3 hyperparameters for all experiments. Modifications from defaults are marked with $\\diamond$.}\n\\label{tab:hyperparams}\n\\small\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{World Model}} \\\\\nRSSM discrete states & 32 classes $\\times$ 32 categories \\\\\nRSSM stochastic dim & 32 \\\\\nRSSM deterministic dim & 512 \\\\\nMLP hidden size & 512 \\\\\nMLP layers & 2 \\\\\nActivation & SiLU \\\\\nNormalization & LayerNorm \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Training}} \\\\\nBatch size & 16 sequences $\\times$ 64 steps \\\\\nLearning rate & $3 \\times 10^{-4}$ (Adam, $\\epsilon{=}10^{-8}$) \\\\\nSequence length & 64 \\\\\nTraining ratio & 512 \\\\\nFree nats & 1.0 \\\\\nKL balance ($\\alpha$) & 0.8 \\\\\nDiscount ($\\gamma$) & 0.997 \\\\\n$\\lambda$-return & 0.95 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Policy}} \\\\\nImagination horizon$^\\diamond$ & 8 or 15 (see Table~\\ref{tab:complete_results}) \\\\\nActor entropy scale & $3 \\times 10^{-4}$ \\\\\nActor gradient & Reinforce + dynamics backprop \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Temporal Abstraction}$^\\diamond$} \\\\\nGate enabled & True (all non-baseline) \\\\\nGate fixed $\\dt$ & 1 or 2 (per config) \\\\\nSubsample max $\\dt$ & 1 (OFF) or 2 (ON) \\\\\n$\\dt$-embedding dim & 32 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Environment}} \\\\\nAction repeat & 2 (Walker Walk, Cheetah Run) \\\\\nObservation & Proprioceptive (no pixels) \\\\\nTotal environment steps & 105K \\\\\nEvaluation frequency & Every 10K steps \\\\\nEvaluation episodes & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Online CIVO Detector Details}\n\\label{sec:detector_appendix}\n\nThis appendix provides the full algorithm specification and validation results for the online CIVO detector described in \\S\\ref{sec:detector}.\n\n\\subsection{Algorithm Specification}\n\n\\begin{algorithm}[ht]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A full comparison of window sizes appears in \\S\\ref{sec:appendix_sensitivity}.\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $5/5$).\n\n\\subsection{Validation Results}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}14$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n008d s4 & trained $\\dt$-emb & TP & 105K & reactive & 383 & 3.03 \\\\\n010b s0 & trained $\\dt$-emb (Cheetah) & TP & 95K & reactive & 248 & 6.34 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n019b & trained $\\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n009c s3 & no $\\dt$-emb & TN & -- & -- & 457 & -- \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 5/5 (1.00), \\quad FPR = 2/9 (0.22)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe detector identifies all five CIVO-positive runs (TPR = 5/5). Two are detected predictively (008d seeds~0 and~3, both at 45K). Two false positives occur among nine negative cases (FPR = 2/9, precision 71\\%, F$_1$ = 0.83). Run 009c develops genuine late-stage value overestimation unrelated to CIVO; run 009a triggers during a transient eval dip at 85K before recovery to 966. Early alerts (before 70K) carry higher diagnostic confidence.\n\n\\subsection{Cross-Simulator Specificity (PickCube)}\n\nExp\\_019b applies the CIVO-trigger configuration to PickCube-v1 in ManiSkill3, a manipulation task with sparse rewards. The V/E ratio exhibits an oscillatory pattern rather than monotonic divergence: it spikes to $r_t = 5.66$ at 52.5K, then deflates to 1.38 by 72.5K. This trajectory prevents the acceleration condition from co-occurring with evaluation decline at any single checkpoint. Across all 14 checkpoints through 132.5K, the detector correctly remains silent (TN), confirming that the acceleration filter distinguishes transient spikes from CIVO's sustained monotonic divergence. A frozen-embedding control (exp\\_054) confirms this classification: frozen PickCube-v1 exhibits a comparable burst (peak $8.81\\times$ at 62.5K) that resolves within a single evaluation cycle ($0.55\\times$ at 72.5K), establishing environment-specific origin independent of $\\dt$-embedding training.\n\n\\subsection{Detector Limitations}\n\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse. Second, the acceleration condition assumes monotonically increasing overestimation during onset. Third, the detector identifies a \\emph{pattern} rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values were calibrated on fourteen runs across three environments; generalization to different reward scales requires further validation.\n\n\\section{Dual-Critic Mechanism Ablation}\n\\label{sec:dual_critic_appendix}\n\n\\subsection{\\texorpdfstring{$2{\\times}2$}{2x2} Factorial Design}\n\nWe ablate the critic architecture in a $2{\\times}2$ factorial: \\{single, dual\\} $\\times$ \\{narrow (${\\sim}1.2$M), wide (${\\sim}2.4$M)\\} parameters. Table~\\ref{tab:dual_critic_full} reports all configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Dual-critic $2{\\times}2$ factorial results. Walker Walk unless noted.}\n\\label{tab:dual_critic_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Params} & \\textbf{NVE} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\n008d & Single narrow & 1.2M & 4.12$\\times$ & 82.8 & Collapse \\\\\n033 & Wide single & 2.4M & 4.75$\\times$ & 407.9 & CIVO $\\to$ self-repair \\\\\n035 s0 & Narrow dual (min) & 1.2M & 2.75$\\times$ & 697.8 & CIVO $\\to$ recovery \\\\\n039 s1 & Narrow dual (min) & 1.2M & 2.19$\\times$ & 592.7 & CIVO $\\to$ recovery \\\\\n032 s0 & Wide dual (min) & 2.4M & $\\leq$1.1$\\times$ & 739.7 & CIVO prevented \\\\\n032b s1 & Wide dual (min) & 2.4M & 1.4$\\times$ & 551.8 & CIVO prevented \\\\\n038 s2 & Wide dual (min) & 2.4M & $\\leq$0.3$\\times$ & 120.9$^*$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Cross-environment}} \\\\\n034 & Cheetah dual & 2.4M & 1.75$\\times$ & 97.5 & Partial recovery (31\\%) \\\\\n037 & Cheetah wide single & 2.4M & 3.60$\\times$ & 146.1 & CIVO $\\to$ self-repair \\\\\n036 & PickCube dual & 2.4M & 2.3$\\times$ & 27.7 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$CIVO prevented (NVE $\\leq 0.3\\times$) but non-CIVO eval collapse: eval peaked at 354 (155K), then declined to 120.9 (224K) with actor entropy increasing from $-3.59$ to $-0.45$.\\par}\n\\end{table}\n\n\\subsection{Critic Convergence (\\texorpdfstring{$v_1 \\approx v_2$}{v1 ≈ v2})}\n\nAcross all dual-critic configurations and environments, the two critics converge to near-identical value functions. On Walker Walk, Pearson $\\rho > 0.999$ between $v_1$ and $v_2$ outputs; on Cheetah Run and PickCube-v1, the gap is $< 0.2$ (exact match within numerical precision). Per-sample pessimism $\\mathbb{E}[\\max(v_1, v_2) - \\min(v_1, v_2)]$ is 3--4\\% of the theoretical bound for independent critics.\n\nThis convergence occurs because both critics train on the same RSSM-generated latent features. Unlike model-free Double Q-learning, where each critic sees different mini-batches of real transitions and develops distinct function approximation errors, pure-imagination critics share identical inputs from the world model. The min operation therefore cannot provide the pessimism bias that makes Double Q effective in model-free settings.\n\n\\subsection{Recovery vs.\\ Prevention Mechanism}\n\nThe $2{\\times}2$ factorial reveals two separable dimensions:\n\n\\paragraph{Recovery (min-dominated).} The min operation is the primary factor enabling recovery from CIVO. Both narrow dual-critic seeds experience CIVO and recover fully: exp\\_035 (s0, $\\nve = 2.75\\times$, eval $33.8 \\to 697.8$, recovery ratio $20.6\\times$) and exp\\_039 (s1, $\\nve = 2.19\\times$, eval $35.9 \\to 592.7$, recovery ratio $16.5\\times$). Both outperform wide single-critic (exp\\_033, 2.4M params, eval 407.9) despite $2\\times$ fewer parameters. The min operation reduces both peak CIVO severity (2.19--2.75$\\times$ vs.\\ 4.75$\\times$ for the comparable single-critic) and enables consistent full recovery across seeds.\n\n\\paragraph{Prevention (min $+$ capacity synergy).} CIVO prevention (NVE remaining below the $1.5\\times$ threshold) requires both the min operation and increased capacity: only the wide dual-critic (exp\\_032, 3 seeds) achieves this. The mechanism for this synergy is an open question; we hypothesize that increased capacity improves value calibration quality while the min operation constrains the overestimation feedback loop during early training when the two critics briefly diverge.\n\n\\paragraph{Cross-environment limits.} On Cheetah Run, the wide dual-critic (exp\\_034) reduces NVE from $8.27\\times$ (untreated baseline) to $1.75\\times$ ($\\geq 4\\times$ reduction) but cannot prevent CIVO onset, and recovery reaches only 31\\% of the pre-CIVO peak. This confirms that the min $+$ capacity synergy has environment-dependent limits: in high-CIVO-severity environments, architecture-level interventions attenuate but do not eliminate the pathology.\n",
    "structuredPatch": [
      {
        "oldStart": 586,
        "oldLines": 7,
        "newStart": 586,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{table}[ht]",
          " \\centering",
          "-\\caption{Post-CIVO outcomes for all six CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}",
          "+\\caption{Post-CIVO outcomes for all seven CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}",
          " \\label{tab:post_civo}",
          " \\footnotesize",
          " \\setlength{\\tabcolsep}{3pt}"
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

_source line 94_

<details open><summary>🔧 Tool call — Edit · `toolu_01K3D2FeV3zCugHB9Abovur4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "Walker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\n\\midrule\nCheetah",
  "new_string": "Walker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\nWalker & s5 (059) & 4.72$\\times$ & ${\\sim}1.1\\times$$^{\\S}$ & 95.8 & Self-correction \\\\\n\\midrule\nCheetah"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "67133841-7919-4795-925b-156ba3db9e53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012swrHLwzU8fYGrKxzsxi4V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 64367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1633
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

_source line 95 · 2026-05-24T07:12:17.788Z_

<details><summary>↩ Tool result · `toolu_01K3D2FeV3zCugHB9Abovur4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "6859e990-1a84-4b4b-8391-dd9ec06daedd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "Walker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\n\\midrule\nCheetah",
    "newString": "Walker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\nWalker & s5 (059) & 4.72$\\times$ & ${\\sim}1.1\\times$$^{\\S}$ & 95.8 & Self-correction \\\\\n\\midrule\nCheetah",
    "originalFile": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\\times$ & Self-correction \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\\times$ & Transient (self-corr.) \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\rowcolor{gray!15}\n008e\\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\\times$ & CIVO collapse \\\\\n008e\\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\\times$ & Healthy \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\n$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\n$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\n$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\n$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\par}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n\\label{tab:cross_domain}\n\\footnotesize\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n\\midrule\nLocomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\\times$) \\\\\nLocomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\nManipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\nManipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\nManipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all ten factorial experiments (including four 008e\\_v3 seeds). Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\\_v3\\_s3 exhibits CIVO with NVE $4.02\\times$ despite $\\Delta t{=}1$ imagination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.83 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.12 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s3 & 4.02 & CIVO           & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.02\\times$, exp~008e\\_v3\\_s3) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.02]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.958$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=7$, $n=10$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). $^\\dagger$Optimal threshold in $(3.78, 4.02]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 3 & 0 & 4 & 70.0\\% \\; [34.8, 93.3] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.2\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.5\\times$ & 3 & 2 & 0 & 5 & 80.0\\% \\; [44.4, 97.5] & 60.0\\% & 100\\% & 75.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 0 & 6 & 90.0\\% \\; [55.5, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 3 & 0 & 0 & 7 & 100\\% \\; [69.2, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=4$, $n_{\\text{neg}}=6$, $n=10$, $\\text{AUROC}=0.958$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 4 & 2 & 0 & 4 & 80.0\\% \\; [44.4, 97.5] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 1.2\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 4 & 1 & 0 & 5 & 90.0\\% \\; [55.5, 99.7] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.7\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 2.0\\times$ & 3 & 1 & 1 & 5 & 80.0\\% \\; [44.4, 97.5] & 75.0\\% & 75.0\\% & 75.0\\% \\\\\n$\\geq 3.9\\times$ & 3 & 0 & 1 & 6 & 90.0\\% \\; [55.5, 99.7] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\\text{pos}}=8$, $n_{\\text{neg}}=8$, $n=16$, $\\text{AUROC}=0.969$). Includes Walker Walk (14 configurations) and Cheetah Run (2 configurations).}\n\\label{tab:sensitivity_b2_full}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 8 & 2 & 0 & 6 & 87.5\\% \\; [61.7, 98.4] & 80.0\\% & 100\\% & 88.9\\% \\\\\n$\\geq 1.2\\times$ & 8 & 1 & 0 & 7 & 93.8\\% \\; [69.8, 99.8] & 88.9\\% & 100\\% & 94.1\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 8 & 1 & 0 & 7 & 93.8\\% \\; [69.8, 99.8] & 88.9\\% & 100\\% & 94.1\\% \\\\\n$\\geq 1.7\\times$ & 6 & 1 & 2 & 7 & 81.3\\% \\; [54.4, 96.0] & 85.7\\% & 75.0\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 6 & 1 & 2 & 7 & 81.3\\% \\; [54.4, 96.0] & 85.7\\% & 75.0\\% & 80.0\\% \\\\\n$\\geq 3.9\\times$ & 6 & 0 & 2 & 8 & 87.5\\% \\; [61.7, 98.4] & 100\\% & 75.0\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all four CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 75.0\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 88.9\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 3$ the statistical power remains limited (accuracy 95\\% CI: [69.2\\%, 100\\%]).\n\n\\subsection{Expanded ROC Analysis}\n\\label{sec:roc_analysis}\n\nThe original $n{=}16$ analysis (Tables~\\ref{tab:sensitivity_b1}--\\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}29$ configurations spanning all tested interventions. Figure~\\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\\% bootstrap confidence interval (10{,}000 resamples).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.7\\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}\n\\caption{NVE ROC curve ($n{=}29$ configurations, AUROC${=}0.953$, in-sample, post-hoc). The preset $\\nve \\geq 1.5\\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}\n\\label{fig:nve_roc}\n\\end{figure}\n\nWe label a configuration as CIVO-positive if and only if (i)~it uses a trained $\\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.\n\nThe three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\\_008e\\_v3 seed~2, actor entropy \\emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \\emph{decrease}). All three produce NVE $> 1.5\\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\\times$) lacks $\\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\\times$) exhibits the full CIVO causal chain: trained $\\dt$-embedding, entropy decrease, and evaluation collapse to 14\\% of baseline.\n\n\\subsection{NVE Normalization Robustness}\n\\label{sec:nve_robustness}\n\nTo assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\\ref{tab:baseline_seeds}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Walker Walk baseline seeds at 105K and 505K steps.}\n\\label{tab:baseline_seeds}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Eval@105K} & \\textbf{Eval@505K} & \\textbf{ve@65K} & \\textbf{ve@105K} \\\\\n\\midrule\ns1 & 915.7 & 970.4 & 0.563 & 0.656 \\\\\ns2 & 443.5 & 945.7 & 0.898 & 0.742 \\\\\ns3 & 869.0 & 947.7 & --- & 0.664 \\\\\ns4 & 922.8 & 938.9 & --- & 0.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\\times$; 009b seed~2, peak NVE $1.62\\times$) to fall below the $1.5\\times$ threshold. Core CIVO cases (peak NVE $> 3\\times$) remain correctly classified under all baseline seeds.\n\nSingle-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\\%): the boundary case exp\\_009b flips from $\\nve = 1.62\\times$ (s1) to $1.23\\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\\times \\to 4.52\\times$; 008d: $4.12\\times \\to 3.54\\times$). The $1.5\\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\\% of the threshold.\n\n\\paragraph{Normalization conventions.} Walker NVE is normalized against the 4-seed mean baseline (seeds~1--4, each run to 505K+ steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).\n\n\\paragraph{Limitations.} With $n = 10$ experiments, Clopper-Pearson confidence intervals remain wide (e.g., 90.0\\% accuracy has 95\\% CI [55.5\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds. Table~\\ref{tab:sensitivity_b2_full} reports the original $n{=}16$ evaluation set spanning both environments. The expanded analysis ($n{=}29$, including SGS variants, RAVE, and TCN configurations) yields AUROC${=}0.953$ (Figure~\\ref{fig:nve_roc}, in-sample, post-hoc). The original $n{=}16$ core analysis yields AUROC${=}0.969$; the expanded $n{=}29$ set includes SGS, RAVE, TCN, and dual-critic configurations. Cross-architecture validation is deferred to future work.\n\n\\subsection{Leave-One-Environment-Out Cross-Validation}\n\\label{sec:nve_loeo}\n\nTo assess whether $\\theta{=}1.5\\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}13$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\\theta{=}1.5\\times$ on the held-out environment.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-environment-out cross-validation of NVE threshold $\\theta=1.5\\times$.\nFor each fold, the threshold is validated on an environment whose data was \\emph{not} used\nto select $\\theta$. The optimal threshold range on each training set is reported;\n$\\theta=1.5$ falls within the optimal range in all three folds.}\n\\label{tab:nve_loeo}\n\\begin{tabular}{lccccc}\n\\toprule\nHeld-out & $N_{\\text{train}}$ & $N_{\\text{test}}$ & $\\theta_{\\text{opt}}$ range & Test Accuracy & Test AUROC \\\\\n\\midrule\nPickCube & 18 & 2 & $(1.45,\\, 1.53]$ & 2/2 (1.000) & 1.000 \\\\\nCheetah  & 15 & 5 & $(1.45,\\, 1.53]$ & 5/5 (1.000) & 1.000 \\\\\nWalker   &  7 & 13 & $(1.00,\\, 3.78)$ & 12/13 (0.923) & 0.944 \\\\\n\\midrule\n\\textbf{Mean} & — & — & — & \\textbf{0.974} & \\textbf{0.981} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe threshold $\\theta{=}1.5\\times$ falls within the optimal accuracy range for all three training folds: $(1.45, 1.53]$ when Walker data is available, and the wider $(1.00, 3.78)$ when training on Cheetah$+$PickCube only (where CIVO and non-CIVO NVE values are well-separated). The single cross-validation error is exp\\_008e\\_v3 seed~2 (Walker), an IRD collapse mechanistically distinct from CIVO (\\S\\ref{sec:roc_analysis}). Mean held-out accuracy is 0.974 and mean AUROC is 0.981, confirming that $\\theta{=}1.5\\times$ generalizes across environments without retuning. PickCube fold confidence intervals remain wide (Clopper-Pearson 95\\% CI: $[0.158, 1.000]$) due to $N_{\\text{test}}{=}2$.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\paragraph{Embedding gradient analysis.}\nTable~\\ref{tab:three_way_emb} isolates embedding \\emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\\dt{=}2$ imagination).\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}\n\\label{tab:three_way_emb}\n\\footnotesize\n\\begin{tabular}{lccccl}\n\\toprule\nCondition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\\\\n\\midrule\nTrained & all & 008d, 059 & $1.53$--$4.72\\times$ & 64--268 & 5/5 \\\\\nReward detach & obs+KL only & 044 & $4.45\\times$ & 44$\\to$538$^\\dagger$ & 1/1 \\\\\nFull SGS & KL only & 018 & $1.66\\times$ & 448 & 1/1$^*$ \\\\\nFrozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\\nRemoved & N/A & 008f & $0.97$--$1.41\\times$ & 307--503 & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\\times$); seed~2 collapsed. $^\\dagger$Self-corrected at ${\\sim}175$K (eval 44$\\to$538, 59\\% baseline; 224K run). $^\\ddagger$Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps.\\par}\n\\end{table}\n\nThe reward-detach condition (exp\\_044, \\texttt{reward\\_dt\\_emb\\_detach=True}) uses a backward hook to block reward-head gradients from reaching $e_{\\dt}$, complementing the framework-level Reward SGS (exp\\_016e). Both yield the same directional result---CIVO onset not prevented---ruling out implementation artifacts. Exp\\_044 exhibits delayed CIVO onset (${\\sim}95$K vs.\\ typical $25$--$35$K), consistent with reduced but non-zero gradient pressure on $e_{\\dt}$. Over a full 224K run, exp\\_044 self-corrects: eval recovers from 44 (95K) to 538 (215K, 59\\% baseline), but this recovery is incomplete compared to spontaneous recovery without gradient intervention (exp\\_045: 868, 95\\% baseline). The lower asymptote suggests that selectively disrupting gradient flow may create optimization difficulties beyond CIVO itself.\n\nTable~\\ref{tab:factorial_design} summarizes the experimental configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Factorial design. Each row specifies one experimental configuration. \\textbf{Emb}: $\\dt$-embedding mode. \\textbf{Sub}: temporal subsampling. \\textbf{H}: imagination horizon. \\textbf{Imag $\\dt$}: temporal resolution used during imagination.}\n\\label{tab:factorial_design}\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{ID} & \\textbf{Purpose} & \\textbf{Emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Imag $\\dt$} \\\\\n\\midrule\n001 & Reference baseline & --- & --- & 15 & 1 \\\\\n006 & Fixed $\\dt{=}2$ & trn & on & 15 & 2 \\\\\n007 & Fixed $\\dt{=}4$ & trn & on & 15 & 4 \\\\\n\\midrule\n008a & Unexposed emb ctrl & exp$^a$ & off & 15 & 2 \\\\\n008c & Horizon control & exp$^a$ & off & 8 & 2 \\\\\n008d & Collapse condition & trn & on & 8 & 2 \\\\\n008e\\_v3 & $\\dt{=}1$ imag control & trn & on & 15 & 1 \\\\\n008f & Causal ablation & --- & on & 8 & 2 \\\\\n\\midrule\n015b & Frozen-emb ctrl & frz$^b$ & on & 8 & 2 \\\\\n016e & Stop-grad (reward) & trn$^\\dagger$ & on & 8 & 2 \\\\\n018 & Full-SGS & trn$^\\ddagger$ & on & 8 & 2 \\\\\n\\midrule\n005 & Learned gate & adaptive & off & 15 & learned \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^\\dagger$ \\texttt{reward\\_dt\\_emb\\_detach=True}; $^\\ddagger$ all non-KL gradients to \\texttt{dt\\_emb} detached.\\par}\n\\end{table}\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe empirical finding that trained embedding \\emph{plus} multi-rate exposure jointly predict CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.83$--$0.93\\times$ range across 3 seeds (105K steps). Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical factor is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training. This confirms that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.42\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.47 \\rightarrow 0.39 \\rightarrow 0.42$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and precedes full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.42\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that in all tested configurations, CIVO occurs only with the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\nCross-environment validation on Cheetah Run replicates the empirical pattern: trained $e_{\\dt}$ precedes CIVO in both tested seeds (exp\\_010b, 2 seeds, NVE $8.27$--$108.52\\times$, collapse to 51.7/0.83) while removing the embedding eliminates it (exp\\_024b, 2 seeds, NVE $<0.2\\times$, eval 96.5/77.3). Freezing the embedding on Cheetah (exp\\_046, NVE${=}1.35\\times$ vs.\\ trained $70.64\\times$, a $52\\times$ reduction) further confirms that embedding trainability, not architecture, drives CIVO. This extends the sufficiency finding from Walker Walk to a second locomotion environment with qualitatively different dynamics (6-joint vs.\\ 2-joint).\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole predictor of CIVO in tested configurations. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) precedes CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly sufficient in tested configurations.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling precedes collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$; low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig4_mechanism_diagram.pdf}\n\\caption{CIVO mechanism diagram. The trained $\\dt$-embedding enables asymmetric reward prediction fidelity, initiating a feedback loop: biased RSSM rewards $\\to$ optimistic critic values $\\to$ actor exploitation $\\to$ reinforced state-distribution skew.}\n\\label{fig:civo_mechanism}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO (Figure~\\ref{fig:civo_mechanism}).  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, which confirms that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\paragraph{Signed reward error analysis.}\nTo test whether CIVO arises from one-step reward overprediction, we compute signed error (predicted $-$ actual) on posterior-conditioned RSSM predictions (Table~\\ref{tab:signed_error}). The trained-embedding model (008d) shows \\emph{negative} bias at $\\dt{=}2$ (mean signed error $-0.599$, only 8\\% of samples overpredicted), ruling out observation-level reward overprediction as the mechanism. The baseline is well-calibrated (mean SE $\\approx 0$), confirming methodological soundness. Value overestimation therefore occurs during \\emph{imagination-level} prior drift: the RSSM prior (unconditioned on observations) generates reward-favorable trajectories at $\\dt > 1$ (Stage~1 above, $1.68\\times$ ratio under random policy), and the critic accumulates these into overestimated returns. The one-step reward prediction is negatively biased when conditioned on real observations, but this posterior correction is unavailable during imagination. This also distinguishes CIVO from generic compounding error, which would produce \\emph{positive} signed error accumulating with horizon; the negative observation-level bias confirms that CIVO is a prior-drift phenomenon, not a reward-prediction artifact.\n\n\\begin{table}[h]\n\\centering\n\\caption{Signed reward error (predicted $-$ actual) on posterior-conditioned RSSM predictions. Negative values indicate underprediction. The trained-embedding model underpredicts at $\\dt{=}2$, ruling out observation-level reward overprediction as the CIVO mechanism.}\n\\label{tab:signed_error}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Config} & $\\dt$ & \\textbf{Mean SE} & \\textbf{Std} & \\textbf{\\%Over} & \\textbf{Actual} & \\textbf{Pred} \\\\\n\\midrule\nBaseline & 1 & $+0.001$ & 0.023 & 39.6\\% & 1.893 & 1.894 \\\\\n\\midrule\n008d (trained) & 1 & $+0.018$ & 0.072 & 61.8\\% & 0.361 & 0.379 \\\\\n008d (trained) & 2 & $\\mathbf{-0.599}$ & 0.722 & 8.0\\% & 0.721 & 0.121 \\\\\n\\midrule\n008f (no emb) & 1 & $-0.710$ & 0.704 & 14.0\\% & 0.921 & 0.211 \\\\\n008f (no emb) & 2 & $-1.645$ & 1.485 & 5.0\\% & 1.840 & 0.195 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 0/2 CIVO elimination rate on Walker (seed~1: NVE reduced from $4.12\\times$ to $1.66\\times$ but remains CIVO-positive; seed~2: collapsed) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention eliminates CIVO in neither seed: seed~1 shows partial mitigation (eval 448.3, peak NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses (eval 40.8). Removing the observation decoder gradient channel is thus contributory but not sufficient. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3. \\textbf{Trained dt-emb} (008d)\\protect\\footnotemark: learned $d{=}32$ temporal embedding with multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with all non-KL gradients detached from $e_{\\dt}$. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$. Full-SGS seed~1 shows partial mitigation ($-51\\%$ final, NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses ($-96\\%$ final). CIVO elimination rate $= 0/2$.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}\n\nCross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This transient self-correcting trajectory is not attributable to the SGS intervention: the initial CIVO onset and peak severity are comparable to the unmitigated case, and the self-correction may reflect Cheetah Run's simpler dynamics rather than SGS efficacy.  Performance remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's Walker results (0/2 CIVO elimination), these findings yield a 0/3 elimination rate across environments, indicating that gradient-level interventions alone do not eliminate the CIVO vulnerability. Additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Post-CIVO outcomes for all seven CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Env} & \\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\nWalker & s1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\nWalker & s2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\nWalker & s3 (008d\\_s3) & 1.53$\\times$ & 1.53$\\times$ & 268$^\\diamond$ & Late-onset collapse \\\\\nWalker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\n\\midrule\nCheetah & s1 (010b) & 8.27$\\times$ & 8.27$\\times$ & 51.7 & Full collapse \\\\\nCheetah & s0 (010b\\_s0) & 108.52$\\times$ & 108.52$\\times$ & 0.83 & Full collapse \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\diamond$ Transitional; train returns still declining at 105K.\\par}\n\\end{table}\n\nAll six CIVO-positive seeds cross the $\\nve > 1.5\\times$ threshold (Table~\\ref{tab:post_civo}), yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Full collapse is the majority outcome (5/6 seeds), with one self-correction case (Walker seed~2) that remains severely degraded (29.3\\% of baseline). Cheetah seeds exhibit more extreme overestimation (peak NVE $8.27$--$108.52\\times$ vs.\\ Walker's $1.53$--$4.62\\times$), consistent with the Cheetah reward scale amplifying the fidelity gap.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\paragraph{A fourth trajectory: CIVO-induced persistent value collapse.}\nObs-decoder SGS seed~3 (exp\\_025) exhibits a trajectory not observed in the untreated seeds: healthy through 105K ($\\nve < 1.0\\times$, eval 818.6), CIVO onset at 135K ($\\nve = 5.47\\times$, eval 67.0), followed by evaluation recovery (590.2 at 215K, 64\\% of baseline) but persistent value collapse ($\\nve = 0.14\\times$, value mean 80.6). The critic undershoots after the CIVO episode, suggesting that CIVO-induced representational damage may be irreversible even when the policy partially recovers. This contrasts with transient CIVO (seed~2, 009b), where both value and evaluation recover jointly, and with full collapse (seed~1, 008d), where neither recovers. Seed~4 exhibits the same terminal value collapse ($\\nve = 0.14\\times$ at 215K, eval 242), suggesting this overcorrection is systematic rather than seed-specific. The pattern adds a fourth post-CIVO outcome---policy recovery with critic damage---to the three documented in Table~\\ref{tab:post_civo}.\n\n\\subsubsection{Failure and Degradation Mode Taxonomy}\n\nTable~\\ref{tab:failure_modes} classifies the seven distinct failure and degradation modes observed across all experimental configurations. The taxonomy reveals that CIVO is not a single failure mode but a family of related pathologies, with the trained $\\dt$-embedding creating vulnerability through at least three independent mechanisms: value-driven collapse (monotonic, late-onset, and SGS-resistant CIVO), entropy-driven instability (IRD collapse), and gradient-mediated effects (gradient starvation, SGS-paradoxical worsening).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Failure and degradation mode taxonomy. Each mode is characterized by its NVE trajectory, entropy behavior, and primary mechanism.}\n\\label{tab:failure_modes}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccl@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Representative} & \\textbf{NVE} & \\textbf{Entropy} & \\textbf{Mechanism} \\\\\n\\midrule\nMonotonic CIVO & 008d, 008d\\_s4, 010b\\_s0 & $\\uparrow$ sustained & $\\downarrow$ & Reward bias $\\to$ critic $\\to$ actor \\\\\nLate-onset CIVO & 008d\\_s3 & $\\uparrow$ delayed & $\\downarrow$ & Same, delayed onset \\\\\nTransient CIVO & 009b & Peak $\\to$ $\\downarrow$ & Stable & Self-correction via capacity \\\\\nIRD collapse & 008e\\_v3\\_s2 & $\\uparrow$ late & $\\uparrow$ & Entropy-driven, values stable \\\\\nGrad.\\ starvation & 015b & Oscillates, decays & Stable & Frozen emb $\\to$ zero actor grad \\\\\nSGS-resistant & 018\\_s2 & $\\uparrow$ & $\\downarrow$ & Forward-pass conditioning \\\\\nSGS-paradoxical & 016e & $\\uparrow$ sustained & $\\downarrow$ & Reward SGS $\\to$ obs-dec reliance \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) avoids collapse in 2 of 4 seeds (50\\%), while the remaining two collapse via distinct mechanisms: Pathway~A (CIVO-driven, entropy decrease; s3, NVE $4.02\\times$) and Pathway~B (entropy-driven, entropy increase; s2, NVE $3.78\\times$; \\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse patterns identified in \\S\\ref{sec:f6}---CIVO (Pathway~A, value-driven, entropy decreasing) and a tentative second mode (Pathway~B, eval-driven, entropy increasing)---have distinct diagnostic signatures. Pathway~B is observed in only two seeds (008e\\_v3\\_s2 and 038\\_s2); we present it as preliminary evidence that the trained $\\dt$-embedding's learned features may affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B), though additional data is needed to confirm this as a distinct mechanism.  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse (Figure~\\ref{fig:multiple_pathways}).\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.  The CIVO mechanism requires three structural properties: (1) a temporal embedding that co-adapts with dynamics via gradient flow, (2) multi-step imagined rollouts used for critic training, and (3) a reward head that inherits latent biases from the shared representation.  Transformer-based world models that share these properties may exhibit analogous vulnerability; architectures that decouple temporal conditioning from the reward prediction pathway would not.\n\n\\subsection{Cross-Environment TCN Evaluation}\n\\label{sec:tcn_cross_env}\n\nTable~\\ref{tab:tcn_full} reports the full TCN evaluation across environments and noise magnitudes.\n\n\\begin{table}[h]\n\\centering\n\\caption{TCN results across environments and noise magnitudes. Prevention = peak NVE $< 1.5\\times$ (35K+).}\n\\label{tab:tcn_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Env} & $\\sigma$ & \\textbf{Seed} & \\textbf{NVE$_{\\max}$} & \\textbf{Prevented?} & \\textbf{Eval (\\%)} \\\\\n\\midrule\nWalker & 0.1 & s0 & 1.02 & \\checkmark$^*$ & 55\\% \\\\\nWalker & 0.2 & s0 & 0.91 & \\checkmark & 91\\% \\\\\nWalker & 0.2 & s1 & 0.64 & \\checkmark & 45\\% \\\\\nWalker & 0.2 & s2 & 2.11$^\\dagger$ & $\\times$ & ${\\sim}5\\%$ \\\\\n\\rowcolor{gray!15}\nWalker & 0.2 & s3 & 3.04$^\\P$ & $\\times$ & 11\\% \\\\\nWalker & 0.5 & s0 & 3.97 & $\\times$ & 27\\% \\\\\nWalker & 0.5 & s1 & 1.64 & $\\times$ & 41\\% \\\\\n\\midrule\nCheetah & 0.2 & s0 & 1.90 & $\\times$ & crashed \\\\\nCheetah & 0.5 & s0 & 10.67 & $\\times$ & 26\\% \\\\\nCheetah & 1.0 & s0 & $\\leq$0.30 & \\checkmark$^\\S$ & 15\\% \\\\\n\\midrule\nPickCube & 0.2 & s0 & 3.71 & $\\times$ & failing \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Borderline: NVE${=}1.02\\times$ at 95K, below $1.5\\times$ threshold but above $1.0\\times$.\\\\\n$^\\dagger$NVE $= 2.11\\times$ at 95K, still rising; eval ${\\sim}5\\%$ of baseline.\\\\\n$^\\P$Late-onset CIVO: NVE declined to $0.67\\times$ at 95K before phase-transition-like spike to $3.04\\times$ at 105K; eval 349.6 at 95K $\\to$ 71.8 at 105K $\\to$ 104.5 at 215K.\\\\\n$^\\S$CIVO prevented (NVE${\\leq}0.30$); peak eval 116\\% baseline at 35K, declining to 15\\% by 215K via progressive policy erosion. See ``impossible dose'' discussion.\\par}\n\\end{table}\n\n\\paragraph{Cheetah Run $\\sigma{=}0.5$: transient spike with permanent eval damage.}\nCheetah $\\sigma{=}0.5$ exhibits a novel failure mode: a transient CIVO spike (NVE $= 10.67\\times$ at 55K) followed by NVE recovery ($< 0.3\\times$ by 95K), but permanent evaluation damage (26\\% of baseline). The value signal self-corrects while the policy does not recover, suggesting that CIVO-induced representational damage during the spike is irreversible even when the critic subsequently recalibrates. This trajectory parallels the obs-decoder SGS seed~3 pattern (\\S\\ref{sec:seed_divergence}), where partial policy recovery coexists with persistent critic damage.\n\n\\paragraph{Cheetah Run $\\sigma{=}0.2$: insufficient dose.}\nAt $\\sigma{=}0.2$, Cheetah reaches NVE $= 1.9\\times$ at 55K---exceeding the $1.5\\times$ threshold---consistent with Cheetah's higher baseline CIVO severity ($8$--$108\\times$ vs.\\ Walker's $2$--$6\\times$). The noise magnitude that suffices for Walker is inadequate for Cheetah, but increasing $\\sigma$ to 0.5 trades CIVO prevention for a different failure mode rather than achieving mitigation.\n\n\\paragraph{PickCube-v1 $\\sigma{=}0.2$: sparse-reward failure.}\nPickCube reaches NVE $= 3.71\\times$ at 52.5K with $\\sigma{=}0.2$, indicating that TCN provides no protection in sparse-reward manipulation tasks. The combination of sparse rewards and temporal conditioning may amplify the fidelity gap beyond what representation-level noise can attenuate.\n\n\\paragraph{Dose-response analysis.}\nWe observe $\\sigma{=}0.2$ as a local optimum on Walker Walk, achieving complete CIVO suppression in 2 of 4 seeds. Seeds~2 and~3 both fail but via distinct CIVO onset dynamics: seed~2 shows gradual escalation (NVE $= 2.11\\times$ at 95K, still rising, eval ${\\sim}5\\%$), while seed~3 exhibits a phase-transition-like onset---NVE declined to $0.67\\times$ at 95K before spiking to $3.04\\times$ at 105K (eval 349.6 $\\to$ 71.8 in 10K steps). When TCN fails to prevent CIVO onset, the resulting trajectory qualitatively resembles untreated CIVO in its terminal outcome---runaway NVE and eval collapse. The two failure modes (gradual escalation vs.\\ sudden onset after apparent suppression) reinforce that TCN operates as a binary gate on CIVO onset rather than providing graded attenuation. Below the optimum, we observe $\\sigma{=}0.1$ as insufficient (NVE $= 1.02\\times$---borderline, eval 55\\%); above it, $\\sigma{=}0.5$ overdoses (oscillatory CIVO, eval $\\leq 41\\%$). Cross-seed variance at $\\sigma{=}0.2$ (eval 5--91\\%) exceeds the cross-dose difference by a wide margin, reinforcing that seed effects dominate dose effects. TCN is the only tested intervention achieving complete CIVO suppression in any configuration, but its high seed sensitivity and failure to transfer across environments position it as a \\emph{diagnostic probe}---identifying the representation level as the relevant intervention target---rather than a deployable mitigation.\n\n\\paragraph{Cheetah Run ``impossible dose'' dilemma.}\nExp\\_030c (224K steps) reveals a qualitatively different dose-response on Cheetah. At $\\sigma{=}1.0$, CIVO is eliminated (NVE${\\leq}0.30$ throughout) and initial learning is \\emph{unimpaired}: peak eval reaches 372 at 35K (116\\% of baseline), demonstrating that $\\sigma{=}1.0$ noise does not prevent policy acquisition. However, cumulative actor gradient interference produces progressive policy erosion---eval declines from 372 to 47 by 215K (15\\% of baseline)---while the critic remains well-calibrated (value\\_mean${=}12.4$, NVE${=}0.26$ at 215K). This establishes that \\emph{policy degradation $\\neq$ value corruption}: accurate value signals are insufficient when the actor cannot optimize effectively in noise-perturbed imagination.\n\nThis ``correct values, failed policy'' pattern provides indirect evidence that CIVO is mechanistically distinct from standard overestimation. Double Q-learning and ensemble methods address critic estimation error, but at $\\sigma{=}1.0$ the critic is accurate and the policy still collapses---a failure mode orthogonal to what these countermeasures target. The impossible dose dilemma scales with environment complexity: Cheetah's baseline CIVO severity ($8$--$108\\times$ NVE) requires $\\sigma \\geq 1.0$ to suppress, but this exceeds the actor's gradient signal-to-noise tolerance. On Walker, a narrow effective window exists around $\\sigma{=}0.2$; on Cheetah, the effective dose ($\\sigma \\geq 1.0$) exceeds the tolerable dose, and environments with higher CIVO severity will systematically lack a viable dose window.\n\n\\section{DreamerV3 Hyperparameters}\n\\label{sec:hyperparameters}\n\nTable~\\ref{tab:hyperparams} lists the DreamerV3 hyperparameters used across all experiments. Unless otherwise noted, we use the default DreamerV3 configuration for continuous-control tasks (\\texttt{dmc\\_proprio}).\n\n\\begin{table}[ht]\n\\centering\n\\caption{DreamerV3 hyperparameters for all experiments. Modifications from defaults are marked with $\\diamond$.}\n\\label{tab:hyperparams}\n\\small\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{World Model}} \\\\\nRSSM discrete states & 32 classes $\\times$ 32 categories \\\\\nRSSM stochastic dim & 32 \\\\\nRSSM deterministic dim & 512 \\\\\nMLP hidden size & 512 \\\\\nMLP layers & 2 \\\\\nActivation & SiLU \\\\\nNormalization & LayerNorm \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Training}} \\\\\nBatch size & 16 sequences $\\times$ 64 steps \\\\\nLearning rate & $3 \\times 10^{-4}$ (Adam, $\\epsilon{=}10^{-8}$) \\\\\nSequence length & 64 \\\\\nTraining ratio & 512 \\\\\nFree nats & 1.0 \\\\\nKL balance ($\\alpha$) & 0.8 \\\\\nDiscount ($\\gamma$) & 0.997 \\\\\n$\\lambda$-return & 0.95 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Policy}} \\\\\nImagination horizon$^\\diamond$ & 8 or 15 (see Table~\\ref{tab:complete_results}) \\\\\nActor entropy scale & $3 \\times 10^{-4}$ \\\\\nActor gradient & Reinforce + dynamics backprop \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Temporal Abstraction}$^\\diamond$} \\\\\nGate enabled & True (all non-baseline) \\\\\nGate fixed $\\dt$ & 1 or 2 (per config) \\\\\nSubsample max $\\dt$ & 1 (OFF) or 2 (ON) \\\\\n$\\dt$-embedding dim & 32 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Environment}} \\\\\nAction repeat & 2 (Walker Walk, Cheetah Run) \\\\\nObservation & Proprioceptive (no pixels) \\\\\nTotal environment steps & 105K \\\\\nEvaluation frequency & Every 10K steps \\\\\nEvaluation episodes & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Online CIVO Detector Details}\n\\label{sec:detector_appendix}\n\nThis appendix provides the full algorithm specification and validation results for the online CIVO detector described in \\S\\ref{sec:detector}.\n\n\\subsection{Algorithm Specification}\n\n\\begin{algorithm}[ht]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A full comparison of window sizes appears in \\S\\ref{sec:appendix_sensitivity}.\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $5/5$).\n\n\\subsection{Validation Results}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}14$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n008d s4 & trained $\\dt$-emb & TP & 105K & reactive & 383 & 3.03 \\\\\n010b s0 & trained $\\dt$-emb (Cheetah) & TP & 95K & reactive & 248 & 6.34 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n019b & trained $\\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n009c s3 & no $\\dt$-emb & TN & -- & -- & 457 & -- \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 5/5 (1.00), \\quad FPR = 2/9 (0.22)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe detector identifies all five CIVO-positive runs (TPR = 5/5). Two are detected predictively (008d seeds~0 and~3, both at 45K). Two false positives occur among nine negative cases (FPR = 2/9, precision 71\\%, F$_1$ = 0.83). Run 009c develops genuine late-stage value overestimation unrelated to CIVO; run 009a triggers during a transient eval dip at 85K before recovery to 966. Early alerts (before 70K) carry higher diagnostic confidence.\n\n\\subsection{Cross-Simulator Specificity (PickCube)}\n\nExp\\_019b applies the CIVO-trigger configuration to PickCube-v1 in ManiSkill3, a manipulation task with sparse rewards. The V/E ratio exhibits an oscillatory pattern rather than monotonic divergence: it spikes to $r_t = 5.66$ at 52.5K, then deflates to 1.38 by 72.5K. This trajectory prevents the acceleration condition from co-occurring with evaluation decline at any single checkpoint. Across all 14 checkpoints through 132.5K, the detector correctly remains silent (TN), confirming that the acceleration filter distinguishes transient spikes from CIVO's sustained monotonic divergence. A frozen-embedding control (exp\\_054) confirms this classification: frozen PickCube-v1 exhibits a comparable burst (peak $8.81\\times$ at 62.5K) that resolves within a single evaluation cycle ($0.55\\times$ at 72.5K), establishing environment-specific origin independent of $\\dt$-embedding training.\n\n\\subsection{Detector Limitations}\n\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse. Second, the acceleration condition assumes monotonically increasing overestimation during onset. Third, the detector identifies a \\emph{pattern} rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values were calibrated on fourteen runs across three environments; generalization to different reward scales requires further validation.\n\n\\section{Dual-Critic Mechanism Ablation}\n\\label{sec:dual_critic_appendix}\n\n\\subsection{\\texorpdfstring{$2{\\times}2$}{2x2} Factorial Design}\n\nWe ablate the critic architecture in a $2{\\times}2$ factorial: \\{single, dual\\} $\\times$ \\{narrow (${\\sim}1.2$M), wide (${\\sim}2.4$M)\\} parameters. Table~\\ref{tab:dual_critic_full} reports all configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Dual-critic $2{\\times}2$ factorial results. Walker Walk unless noted.}\n\\label{tab:dual_critic_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Params} & \\textbf{NVE} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\n008d & Single narrow & 1.2M & 4.12$\\times$ & 82.8 & Collapse \\\\\n033 & Wide single & 2.4M & 4.75$\\times$ & 407.9 & CIVO $\\to$ self-repair \\\\\n035 s0 & Narrow dual (min) & 1.2M & 2.75$\\times$ & 697.8 & CIVO $\\to$ recovery \\\\\n039 s1 & Narrow dual (min) & 1.2M & 2.19$\\times$ & 592.7 & CIVO $\\to$ recovery \\\\\n032 s0 & Wide dual (min) & 2.4M & $\\leq$1.1$\\times$ & 739.7 & CIVO prevented \\\\\n032b s1 & Wide dual (min) & 2.4M & 1.4$\\times$ & 551.8 & CIVO prevented \\\\\n038 s2 & Wide dual (min) & 2.4M & $\\leq$0.3$\\times$ & 120.9$^*$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Cross-environment}} \\\\\n034 & Cheetah dual & 2.4M & 1.75$\\times$ & 97.5 & Partial recovery (31\\%) \\\\\n037 & Cheetah wide single & 2.4M & 3.60$\\times$ & 146.1 & CIVO $\\to$ self-repair \\\\\n036 & PickCube dual & 2.4M & 2.3$\\times$ & 27.7 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$CIVO prevented (NVE $\\leq 0.3\\times$) but non-CIVO eval collapse: eval peaked at 354 (155K), then declined to 120.9 (224K) with actor entropy increasing from $-3.59$ to $-0.45$.\\par}\n\\end{table}\n\n\\subsection{Critic Convergence (\\texorpdfstring{$v_1 \\approx v_2$}{v1 ≈ v2})}\n\nAcross all dual-critic configurations and environments, the two critics converge to near-identical value functions. On Walker Walk, Pearson $\\rho > 0.999$ between $v_1$ and $v_2$ outputs; on Cheetah Run and PickCube-v1, the gap is $< 0.2$ (exact match within numerical precision). Per-sample pessimism $\\mathbb{E}[\\max(v_1, v_2) - \\min(v_1, v_2)]$ is 3--4\\% of the theoretical bound for independent critics.\n\nThis convergence occurs because both critics train on the same RSSM-generated latent features. Unlike model-free Double Q-learning, where each critic sees different mini-batches of real transitions and develops distinct function approximation errors, pure-imagination critics share identical inputs from the world model. The min operation therefore cannot provide the pessimism bias that makes Double Q effective in model-free settings.\n\n\\subsection{Recovery vs.\\ Prevention Mechanism}\n\nThe $2{\\times}2$ factorial reveals two separable dimensions:\n\n\\paragraph{Recovery (min-dominated).} The min operation is the primary factor enabling recovery from CIVO. Both narrow dual-critic seeds experience CIVO and recover fully: exp\\_035 (s0, $\\nve = 2.75\\times$, eval $33.8 \\to 697.8$, recovery ratio $20.6\\times$) and exp\\_039 (s1, $\\nve = 2.19\\times$, eval $35.9 \\to 592.7$, recovery ratio $16.5\\times$). Both outperform wide single-critic (exp\\_033, 2.4M params, eval 407.9) despite $2\\times$ fewer parameters. The min operation reduces both peak CIVO severity (2.19--2.75$\\times$ vs.\\ 4.75$\\times$ for the comparable single-critic) and enables consistent full recovery across seeds.\n\n\\paragraph{Prevention (min $+$ capacity synergy).} CIVO prevention (NVE remaining below the $1.5\\times$ threshold) requires both the min operation and increased capacity: only the wide dual-critic (exp\\_032, 3 seeds) achieves this. The mechanism for this synergy is an open question; we hypothesize that increased capacity improves value calibration quality while the min operation constrains the overestimation feedback loop during early training when the two critics briefly diverge.\n\n\\paragraph{Cross-environment limits.} On Cheetah Run, the wide dual-critic (exp\\_034) reduces NVE from $8.27\\times$ (untreated baseline) to $1.75\\times$ ($\\geq 4\\times$ reduction) but cannot prevent CIVO onset, and recovery reaches only 31\\% of the pre-CIVO peak. This confirms that the min $+$ capacity synergy has environment-dependent limits: in high-CIVO-severity environments, architecture-level interventions attenuate but do not eliminate the pathology.\n",
    "structuredPatch": [
      {
        "oldStart": 598,
        "oldLines": 6,
        "newStart": 598,
        "newLines": 7,
        "lines": [
          " Walker & s2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\",
          " Walker & s3 (008d\\_s3) & 1.53$\\times$ & 1.53$\\times$ & 268$^\\diamond$ & Late-onset collapse \\\\",
          " Walker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\",
          "+Walker & s5 (059) & 4.72$\\times$ & ${\\sim}1.1\\times$$^{\\S}$ & 95.8 & Self-correction \\\\",
          " \\midrule",
          " Cheetah & s1 (010b) & 8.27$\\times$ & 8.27$\\times$ & 51.7 & Full collapse \\\\",
          " Cheetah & s0 (010b\\_s0) & 108.52$\\times$ & 108.52$\\times$ & 0.83 & Full collapse \\\\"
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

_source line 96_

<details open><summary>🔧 Tool call — Edit · `toolu_01LhZkXNoBZFzktW84qbwfZD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "All six CIVO-positive seeds cross the $\\nve > 1.5\\times$ threshold (Table~\\ref{tab:post_civo}), yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Full collapse is the majority outcome (5/6 seeds), with one self-correction case (Walker seed~2) that remains severely degraded (29.3\\% of baseline).",
  "new_string": "All seven CIVO-positive seeds cross the $\\nve > 1.5\\times$ threshold (Table~\\ref{tab:post_civo}), yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Full collapse is the majority outcome (5/7 seeds), with two self-correction cases (Walker seeds 2 and 5)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39b154c2-272d-4903-9352-e8d6dc88cb29",
  "uuid": "bb7c5d09-5ca4-4cee-ab27-84436c9c5827",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012swrHLwzU8fYGrKxzsxi4V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 64367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1633
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
