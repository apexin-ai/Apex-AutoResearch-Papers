# fix d041 method drafts

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 108
- **Recorded user turns:** 0
- **Tool calls:** 41
- **Original source:** `logs/workers/worker_fix_d041-method-drafts_20260515T020954.log`
- **Structured JSON:** [`8566b02fe893dd657060.json`](../../sessions/85/8566b02fe893dd657060.json)

## Before a recorded user message

108 recorded events

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
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
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
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "ffd9ab47-3f4c-4156-9ba8-6e8710144d5b",
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
  "uuid": "bdc54762-90e8-43c0-9875-e30d670ba12d",
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88"
}
```

---

### Assistant

_source line 4_

我先读取这四个文件，检查 dataflow-aware 策略的描述。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "7bf2b57d-3b6c-40ba-a32e-bf381211483a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113EPLfvS1TdZA3rkRLaECT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11832,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11832
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NLbGTL5vba9ZuGtzCRtKPR`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "f545e0ba-e5af-4894-a01a-df00db32fa43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113EPLfvS1TdZA3rkRLaECT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11832,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11832
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

_source line 6 · 2026-05-15T02:10:05.150Z_

<details><summary>↩ Tool result · `toolu_01NLbGTL5vba9ZuGtzCRtKPR`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "598daefc-1f87-4518-ae1c-e3ec28c5acc0",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read all four files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "066d04af-e9df-47d4-9b67-e263cffa40ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KighoVkm5JnehDmCgxm49P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 23279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CiH3XC5P83ncVsDbR2vNLH`</summary>

```json
{
  "project": "structfuse-context",
  "file": "method_v1.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "429aef0b-effb-4619-bbb9-6792b43bf94e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KighoVkm5JnehDmCgxm49P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 23279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T02:10:08.857Z_

<details><summary>↩ Tool result · `toolu_01CiH3XC5P83ncVsDbR2vNLH`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'method_v1.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "93a4516b-61ef-4a89-99c4-dae8b5bbc5b5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'method_v1.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'method_v1.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Fobnt5pspNyRq5Mi2U1rxD`</summary>

```json
{
  "project": "structfuse-context",
  "file": "experiment_setup_v1.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "ee49543c-b30d-4f13-9dcf-3e59b85db60e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KighoVkm5JnehDmCgxm49P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 23279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T02:10:09.806Z_

<details><summary>↩ Tool result · `toolu_01Fobnt5pspNyRq5Mi2U1rxD`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_setup_v1.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "46accd64-7670-4532-889f-85481ab0cb8c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_setup_v1.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_setup_v1.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01C8WAwbPqbDj8yLKHKFpJvj`</summary>

```json
{
  "project": "structfuse-context",
  "file": "experiments_v1.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "7d49c9a6-9c2e-42dd-8042-a409ec136ff9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KighoVkm5JnehDmCgxm49P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 23279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T02:10:10.825Z_

<details><summary>↩ Tool result · `toolu_01C8WAwbPqbDj8yLKHKFpJvj`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiments_v1.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "dca50dca-0471-4db6-b996-f3f7ed84c8c9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiments_v1.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiments_v1.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DNRo9R7nqiCPcyio6krMfq`</summary>

```json
{
  "project": "structfuse-context",
  "file": "introduction_v2.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "4693bb01-64f6-44cb-8e5f-34007d26cc44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KighoVkm5JnehDmCgxm49P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 23279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T02:10:11.022Z_

<details><summary>↩ Tool result · `toolu_01DNRo9R7nqiCPcyio6krMfq`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'introduction_v2.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "35a8547e-ab43-4a2f-8a20-fb5d115304a5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'introduction_v2.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'introduction_v2.md'\", \"metadata\": {}}"
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
The `read_project_file` tool only supports a whitelist of files. The paper section files like `method_v1.md` are not in the whitelist. Let me check if these files exist in the artifacts directory or somewhere else in the project directory. Let me search for them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "02b9b939-382c-4cf8-b8b0-c7ce3a7d2c7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcNfkDXbxvWoSQeHhNfoDy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 24004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1172
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

这些文件不在 `read_project_file` 的白名单中。让我找找它们的实际位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "fb202460-227f-4596-b1f0-33a6b393899f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcNfkDXbxvWoSQeHhNfoDy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 24004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1172
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01CmNDrmm3j9yHtD37gMgoj8`</summary>

```json
{
  "pattern": "**/method_v1.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "6f33743b-3554-4873-968b-f915e039c9e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcNfkDXbxvWoSQeHhNfoDy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 24004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1172
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T02:10:17.898Z_

<details><summary>↩ Tool result · `toolu_01CmNDrmm3j9yHtD37gMgoj8`</summary>

```text
artifacts/_project/paper/method_v1.md
artifacts/paper_drafts/method_v1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "b071d522-9716-4e4c-99d3-6287af866244",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/method_v1.md",
      "artifacts/paper_drafts/method_v1.md"
    ],
    "durationMs": 35,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_013yybEVLAgcyDv5GnkJQ478`</summary>

```json
{
  "pattern": "**/experiment_setup_v1.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "54eec693-95e8-4a39-bc89-6a14d85095df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcNfkDXbxvWoSQeHhNfoDy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 24004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1172
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T02:10:18.731Z_

<details><summary>↩ Tool result · `toolu_013yybEVLAgcyDv5GnkJQ478`</summary>

```text
artifacts/_project/paper/experiment_setup_v1.md
artifacts/paper_drafts/experiment_setup_v1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "77922b4e-9e5f-4d2e-9f72-95863ac8a169",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/experiment_setup_v1.md",
      "artifacts/paper_drafts/experiment_setup_v1.md"
    ],
    "durationMs": 10,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Glob · `toolu_01Njv6uc1thVMq3KYY2msnv1`</summary>

```json
{
  "pattern": "**/experiments_v1.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "f5eb3e8e-4cea-41d1-8df6-acd2879b7c46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcNfkDXbxvWoSQeHhNfoDy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 24004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1172
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T02:10:19.209Z_

<details><summary>↩ Tool result · `toolu_01Njv6uc1thVMq3KYY2msnv1`</summary>

```text
artifacts/_project/paper/experiments_v1.md
artifacts/paper_drafts/experiments_v1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "b438e2b2-59ae-4fbd-86cc-a550893d68f9",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/experiments_v1.md",
      "artifacts/paper_drafts/experiments_v1.md"
    ],
    "durationMs": 9,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Glob · `toolu_01XBxpgYXgEUFaKASUfhLkMv`</summary>

```json
{
  "pattern": "**/introduction_v2.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "817d2952-4244-4e6c-af19-a1c3fc0c1e16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcNfkDXbxvWoSQeHhNfoDy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 24004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1172
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T02:10:19.529Z_

<details><summary>↩ Tool result · `toolu_01XBxpgYXgEUFaKASUfhLkMv`</summary>

```text
artifacts/_project/paper/introduction_v2.md
artifacts/paper_drafts/introduction_v2.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "e20c62c5-ee90-4543-afe9-87356b822c86",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/introduction_v2.md",
      "artifacts/paper_drafts/introduction_v2.md"
    ],
    "durationMs": 8,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Found the files. There are two copies of each - one in `artifacts/_project/paper/` and one in `artifacts/paper_drafts/`. Let me read the `artifacts/_project/paper/` versions first (these seem like the canonical ones). Let me read all four files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "c3e3ee06-f805-4705-aa85-8a58f4aa8315",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8pdUDyeu38r1VC6s18ihG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 25176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 790
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

找到文件了，存在于 `artifacts/_project/paper/` 和 `artifacts/paper_drafts/` 两个目录。先读取 `_project/paper/` 下的版本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "59e5250a-9728-4378-b3b2-564afc68bbf5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8pdUDyeu38r1VC6s18ihG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 25176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 790
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01KBipAJQpbXLjnioWKQBU99`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "84a1a3da-7c8b-477e-8cb1-c9afa40f9435",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8pdUDyeu38r1VC6s18ihG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 25176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 790
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T02:10:25.295Z_

<details><summary>↩ Tool result · `toolu_01KBipAJQpbXLjnioWKQBU99`</summary>

```text
1	# §3 Method
2	
3	## §3.1 Problem Formulation
4	
5	We address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\mathcal{F} = \{f_1, f_2, \ldots, f_N\}$. The gold set $\mathcal{F}^+_q \subset \mathcal{F}$ denotes the files modified in the ground-truth patch.
6	
7	We formulate this as a contrastive learning problem. Let $E_\theta$ be a pretrained encoder parameterized by $\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files. Concretely, we optimize $\theta$ such that for all $f^+ \in \mathcal{F}^+_q$ and $f^- \in \mathcal{F} \setminus \mathcal{F}^+_q$:
8	
9	$$\text{sim}(E_\theta(q), E_\theta(f^+)) \gg \text{sim}(E_\theta(q), E_\theta(f^-))$$
10	
11	where $\text{sim}(\cdot, \cdot)$ denotes cosine similarity.
12	
13	The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. Random negatives are often too easy, providing weak gradient signal \cite{chen2020simclr}. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.
14	
15	## §3.2 StructFuse Pipeline
16	
17	Our pipeline consists of three stages: (1) structural graph extraction via static analysis, (2) training data construction with strategy-specific negative mining, and (3) contrastive fine-tuning of a pretrained code encoder.
18	
19	**CodeQL Extraction.** We use CodeQL \cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. Specifically, we define taint-tracking queries that trace data flow from designated sources to sinks, crossing function call boundaries. This yields a set of data-flow paths $\mathcal{P} = \{(v_{\text{src}}, v_1, \ldots, v_{\text{sink}})\}$, where each node $v_i$ is annotated with its enclosing file.
20	
21	We set a scope bound on the analysis depth to ensure tractability: queries that exceed a predefined step limit are terminated. In practice, this achieves 0\% timeout rate across 123 out of 131 repositories in our dataset.
22	
23	**Structural Connectivity Graph.** From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \mathcal{F}$ and an edge $(f_i, f_j) \in E$ exists if and only if at least one data-flow path in $\mathcal{P}$ traverses both $f_i$ and $f_j$. This graph captures inter-procedural structural relationships between files—two files are connected if data flows between them across function call boundaries.
24	
25	A key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.
26	
27	**Structural Coverage.** At full scale, 78\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.
28	
29	## §3.3 Training Objective
30	
31	**Contrastive Loss.** We train with InfoNCE loss \cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\{f^-_1, \ldots, f^-_K\}$, the loss is:
32	
33	$$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$
34	
35	where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query.
36	
37	**Encoder Architecture.** We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}—which differ in pretraining objectives (Fill-in-the-Middle vs. multi-task including Fill-in-the-Middle) and exhibit distinct representation geometries (§5). Each encoder is augmented with a linear projection head that maps the last hidden state to a 256-dimensional embedding space.
38	
39	**Parameter-Efficient Fine-Tuning.** We apply LoRA \cite{hu2022lora} to the query and value projection matrices ($W_q$, $W_v$) of each attention layer with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated. We use AdamW with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing with 10\% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2048 tokens. Training runs for 3 epochs with evaluation every 500 steps.
40	
41	**Dual Checkpoint Selection.** We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\theta^*_{\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement.
42	
43	## §3.4 Negative Mining Strategies
44	
45	We compare three negative mining strategies that span a spectrum from uninformed to structure-grounded selection.
46	
47	**Random Mining.** For each query $q$, we sample $K$ negatives uniformly at random from $\mathcal{F} \setminus \mathcal{F}^+_q$. This serves as the baseline: negatives are unbiased but typically easy, as randomly chosen files are unlikely to share topical or structural similarity with the query.
48	
49	**Embedding-Distance Mining.** We compute embeddings for all files and queries using the frozen pretrained encoder $E_{\theta_0}$ (before fine-tuning) and build a FAISS index \cite{johnson2021faiss} over file embeddings. For each query $q$, we retrieve the $K$ non-gold files with highest cosine similarity to $q$ in the pretrained embedding space:
50	
51	$$f^-_{\text{embed}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$
52	
53	This selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \cite{xiong2021ance}.
54	
55	**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\mathcal{F}^+_q$, we define the reachability set $\mathcal{R}_G(q) = \{f \in \mathcal{F} : \exists f^+ \in \mathcal{F}^+_q,\ (f^+, f) \in E^*\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:
56	
57	$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \notin \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$
58	
59	That is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.
60	
61	**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).
62	
63	For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\% of training instances, which we analyze separately in stratified evaluation (§5).
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "e5c0d286-3478-435d-88a9-afc7f2d76f33",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md",
      "content": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files. Concretely, we optimize $\\theta$ such that for all $f^+ \\in \\mathcal{F}^+_q$ and $f^- \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. Random negatives are often too easy, providing weak gradient signal \\cite{chen2020simclr}. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 StructFuse Pipeline\n\nOur pipeline consists of three stages: (1) structural graph extraction via static analysis, (2) training data construction with strategy-specific negative mining, and (3) contrastive fine-tuning of a pretrained code encoder.\n\n**CodeQL Extraction.** We use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. Specifically, we define taint-tracking queries that trace data flow from designated sources to sinks, crossing function call boundaries. This yields a set of data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file.\n\nWe set a scope bound on the analysis depth to ensure tractability: queries that exceed a predefined step limit are terminated. In practice, this achieves 0\\% timeout rate across 123 out of 131 repositories in our dataset.\n\n**Structural Connectivity Graph.** From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. This graph captures inter-procedural structural relationships between files—two files are connected if data flows between them across function call boundaries.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\n**Structural Coverage.** At full scale, 78\\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.\n\n## §3.3 Training Objective\n\n**Contrastive Loss.** We train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$, the loss is:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query.\n\n**Encoder Architecture.** We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—which differ in pretraining objectives (Fill-in-the-Middle vs. multi-task including Fill-in-the-Middle) and exhibit distinct representation geometries (§5). Each encoder is augmented with a linear projection head that maps the last hidden state to a 256-dimensional embedding space.\n\n**Parameter-Efficient Fine-Tuning.** We apply LoRA \\cite{hu2022lora} to the query and value projection matrices ($W_q$, $W_v$) of each attention layer with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated. We use AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10\\% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2048 tokens. Training runs for 3 epochs with evaluation every 500 steps.\n\n**Dual Checkpoint Selection.** We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement.\n\n## §3.4 Negative Mining Strategies\n\nWe compare three negative mining strategies that span a spectrum from uninformed to structure-grounded selection.\n\n**Random Mining.** For each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$. This serves as the baseline: negatives are unbiased but typically easy, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n**Embedding-Distance Mining.** We compute embeddings for all files and queries using the frozen pretrained encoder $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we retrieve the $K$ non-gold files with highest cosine similarity to $q$ in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThis selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \\cite{xiong2021ance}.\n\n**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThat is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.\n\n**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).\n\nFor repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).\n",
      "numLines": 64,
      "startLine": 1,
      "totalLines": 64
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01NCxLkasLMXGKJ1DWRpCoDb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiment_setup_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "6e19e300-fbaf-43c0-95e8-873a1d285f3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8pdUDyeu38r1VC6s18ihG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 25176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 790
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T02:10:26.079Z_

<details><summary>↩ Tool result · `toolu_01NCxLkasLMXGKJ1DWRpCoDb`</summary>

```text
1	# §4 Experimental Setup
2	
3	## §4.1 Dataset
4	
5	We construct our training corpus from SWE-smith \cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit. We expand each task by treating every gold file as a separate training instance, yielding 44,173 instances total [Source: m1_extraction registry, data_count after filtering 6,696 clone/checkout failures from the original 50,869].
6	
7	We run the StructFuse extraction pipeline (§3.2) on all instances. After filtering for extraction errors, we retain 14,288 usable instances across 123 repositories. Of these, approximately 34% possess CodeQL structural connectivity data (15,133 via CodeQL + 764 via beniget fallback); the remaining 66% lack structural data due to transient filesystem failures during batch extraction. For these instances, the dataflow-aware strategy falls back to embedding-distance mining (§3.3) [Source: m1_extraction registry].
8	
9	For each random seed, we perform a per-repository stratified split to produce training and validation partitions. The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties. Exact split sizes:
10	
11	| Seed | Train | Val | Total |
12	|------|-------|-----|-------|
13	| 42 | 11,308 | 2,980 | 14,288 |
14	| 43 | 11,236 | 3,052 | 14,288 |
15	| 44 | 11,264 | 3,024 | 14,288 |
16	
17	[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]
18	
19	## §4.2 Models
20	
21	We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries, enabling us to study how encoder properties mediate the effectiveness of different negative mining strategies.
22	
23	**Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus. It exhibits a near-saturated pretrained representation space: mean positive cosine similarity of 0.986 and mean margin (pos_sim − neg_sim) of only 0.074 with random negatives at 2,048-token context [Source: neg_difficulty_analysis registry, qwen_2048]. This saturation—where nearly all file pairs receive high similarity scores—makes the baseline representation space challenging for contrastive learning and provides a stress test for negative mining strategies.
24	
25	**StarCoder2-3B** \cite{li2023starcoder} uses a multi-task pretraining objective including FIM on The Stack v2. It maintains healthy representation separation: mean positive cosine similarity of 0.799 and a margin of 0.194 with random negatives—2.6× larger than Qwen's [Source: neg_difficulty_analysis registry, starcoder_2048]. This well-separated space allows us to contrast the behavior of mining strategies under fundamentally different geometric conditions.
26	
27	The two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction reveals how representation geometry mediates strategy effectiveness.
28	
29	## §4.3 Training Configuration
30	
31	All hyperparameters are shared across strategies and encoders unless otherwise noted. The configuration was fixed before the full multi-seed experiment based on pilot runs.
32	
33	| Parameter | Value |
34	|-----------|-------|
35	| Optimizer | AdamW |
36	| Learning rate | $2 \times 10^{-5}$ |
37	| LR schedule | Cosine annealing with linear warmup |
38	| Warmup ratio | 0.1 |
39	| Weight decay | 0.01 |
40	| Gradient clipping | Max norm 1.0 |
41	| Batch size | 8 |
42	| Negatives per query ($K$) | 7 |
43	| Max sequence length | 2,048 tokens |
44	| Temperature ($\tau$, initial) | 0.07 (learnable) |
45	| LoRA rank ($r$) | 16 |
46	| LoRA scaling ($\alpha$) | 32 |
47	| LoRA dropout | 0.05 |
48	| LoRA target modules | $W_q$, $W_v$ (all attention layers) |
49	| Projection dimension | 256 |
50	| Gradient checkpointing | Enabled |
51	| Evaluation interval | Every 500 steps |
52	
53	[Source: m2_full_qwen registry spec and notes]
54	
55	**Epoch schedule.** Seed 42 trains for 3 epochs without early stopping to provide a complete overfitting curve. Seeds 43 and 44 train for 2 epochs with early stopping (patience = 2 evaluation cycles based on validation loss). This asymmetric design was adopted after observing consistent overfitting past epoch 1 in the seed 42 exploratory run [Source: D026 decision].
56	
57	**Checkpoint selection.** We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1). Primary results use $\theta^*_{\text{R@1}}$; both are reported for metric-loss disagreement analysis [Source: D036 decision].
58	
59	**Seeds.** 42, 43, 44. The core experiment consists of 3 strategies × 3 seeds × 2 encoders = 18 runs. BM25-mined negatives are evaluated as a supplementary comparison (additional 2 encoders × 3 seeds = 6 runs) [Source: plan_018 registry].
60	
61	**Hardware.** All experiments are conducted on a single node with 2× NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs (cuda:0 and cuda:1) in parallel. Each individual run (single strategy, single seed, single encoder) requires approximately 5–7 hours. The core 18-run matrix requires approximately 120 GPU-hours [Source: m2_full_qwen and m2_full_starcoder registries].
62	
63	## §4.4 Evaluation Metrics
64	
65	**Retrieval metrics.** We report Recall@$k$ for $k \in \{1, 5, 10\}$, computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per evaluation query). Recall@1 serves as the primary metric for checkpoint selection and strategy comparison. We also report validation loss (InfoNCE) as a secondary training diagnostic.
66	
67	**Statistical reporting.** All comparisons report:
68	
69	- **Aggregate**: mean ± standard deviation across 3 seeds per condition.
70	- **Confidence intervals**: bootstrap 95% CIs for pairwise strategy comparisons (embedding vs. random, dataflow vs. random, dataflow vs. embedding).
71	- **Effect size**: Cohen's $d$ for key comparisons, providing a standardized measure of practical significance independent of sample size.
72	- **Per-seed consistency**: individual seed results reported alongside aggregates to assess stability. [TBD: exact CI and Cohen's d values pending M2 completion]
73	
74	**Checkpoint criterion.** Primary results use the $\theta^*_{\text{R@1}}$ checkpoint. We additionally report $\theta^*_{\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].
75	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "f754925c-9f13-4b43-a4ab-961ab7404f8a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiment_setup_v1.md",
      "content": "# §4 Experimental Setup\n\n## §4.1 Dataset\n\nWe construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit. We expand each task by treating every gold file as a separate training instance, yielding 44,173 instances total [Source: m1_extraction registry, data_count after filtering 6,696 clone/checkout failures from the original 50,869].\n\nWe run the StructFuse extraction pipeline (§3.2) on all instances. After filtering for extraction errors, we retain 14,288 usable instances across 123 repositories. Of these, approximately 34% possess CodeQL structural connectivity data (15,133 via CodeQL + 764 via beniget fallback); the remaining 66% lack structural data due to transient filesystem failures during batch extraction. For these instances, the dataflow-aware strategy falls back to embedding-distance mining (§3.3) [Source: m1_extraction registry].\n\nFor each random seed, we perform a per-repository stratified split to produce training and validation partitions. The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties. Exact split sizes:\n\n| Seed | Train | Val | Total |\n|------|-------|-----|-------|\n| 42 | 11,308 | 2,980 | 14,288 |\n| 43 | 11,236 | 3,052 | 14,288 |\n| 44 | 11,264 | 3,024 | 14,288 |\n\n[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]\n\n## §4.2 Models\n\nWe select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries, enabling us to study how encoder properties mediate the effectiveness of different negative mining strategies.\n\n**Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus. It exhibits a near-saturated pretrained representation space: mean positive cosine similarity of 0.986 and mean margin (pos_sim − neg_sim) of only 0.074 with random negatives at 2,048-token context [Source: neg_difficulty_analysis registry, qwen_2048]. This saturation—where nearly all file pairs receive high similarity scores—makes the baseline representation space challenging for contrastive learning and provides a stress test for negative mining strategies.\n\n**StarCoder2-3B** \\cite{li2023starcoder} uses a multi-task pretraining objective including FIM on The Stack v2. It maintains healthy representation separation: mean positive cosine similarity of 0.799 and a margin of 0.194 with random negatives—2.6× larger than Qwen's [Source: neg_difficulty_analysis registry, starcoder_2048]. This well-separated space allows us to contrast the behavior of mining strategies under fundamentally different geometric conditions.\n\nThe two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction reveals how representation geometry mediates strategy effectiveness.\n\n## §4.3 Training Configuration\n\nAll hyperparameters are shared across strategies and encoders unless otherwise noted. The configuration was fixed before the full multi-seed experiment based on pilot runs.\n\n| Parameter | Value |\n|-----------|-------|\n| Optimizer | AdamW |\n| Learning rate | $2 \\times 10^{-5}$ |\n| LR schedule | Cosine annealing with linear warmup |\n| Warmup ratio | 0.1 |\n| Weight decay | 0.01 |\n| Gradient clipping | Max norm 1.0 |\n| Batch size | 8 |\n| Negatives per query ($K$) | 7 |\n| Max sequence length | 2,048 tokens |\n| Temperature ($\\tau$, initial) | 0.07 (learnable) |\n| LoRA rank ($r$) | 16 |\n| LoRA scaling ($\\alpha$) | 32 |\n| LoRA dropout | 0.05 |\n| LoRA target modules | $W_q$, $W_v$ (all attention layers) |\n| Projection dimension | 256 |\n| Gradient checkpointing | Enabled |\n| Evaluation interval | Every 500 steps |\n\n[Source: m2_full_qwen registry spec and notes]\n\n**Epoch schedule.** Seed 42 trains for 3 epochs without early stopping to provide a complete overfitting curve. Seeds 43 and 44 train for 2 epochs with early stopping (patience = 2 evaluation cycles based on validation loss). This asymmetric design was adopted after observing consistent overfitting past epoch 1 in the seed 42 exploratory run [Source: D026 decision].\n\n**Checkpoint selection.** We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Primary results use $\\theta^*_{\\text{R@1}}$; both are reported for metric-loss disagreement analysis [Source: D036 decision].\n\n**Seeds.** 42, 43, 44. The core experiment consists of 3 strategies × 3 seeds × 2 encoders = 18 runs. BM25-mined negatives are evaluated as a supplementary comparison (additional 2 encoders × 3 seeds = 6 runs) [Source: plan_018 registry].\n\n**Hardware.** All experiments are conducted on a single node with 2× NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs (cuda:0 and cuda:1) in parallel. Each individual run (single strategy, single seed, single encoder) requires approximately 5–7 hours. The core 18-run matrix requires approximately 120 GPU-hours [Source: m2_full_qwen and m2_full_starcoder registries].\n\n## §4.4 Evaluation Metrics\n\n**Retrieval metrics.** We report Recall@$k$ for $k \\in \\{1, 5, 10\\}$, computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per evaluation query). Recall@1 serves as the primary metric for checkpoint selection and strategy comparison. We also report validation loss (InfoNCE) as a secondary training diagnostic.\n\n**Statistical reporting.** All comparisons report:\n\n- **Aggregate**: mean ± standard deviation across 3 seeds per condition.\n- **Confidence intervals**: bootstrap 95% CIs for pairwise strategy comparisons (embedding vs. random, dataflow vs. random, dataflow vs. embedding).\n- **Effect size**: Cohen's $d$ for key comparisons, providing a standardized measure of practical significance independent of sample size.\n- **Per-seed consistency**: individual seed results reported alongside aggregates to assess stability. [TBD: exact CI and Cohen's d values pending M2 completion]\n\n**Checkpoint criterion.** Primary results use the $\\theta^*_{\\text{R@1}}$ checkpoint. We additionally report $\\theta^*_{\\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].\n",
      "numLines": 75,
      "startLine": 1,
      "totalLines": 75
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_017MR67MJLUhTh124RbMs4ra`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "bf235337-9fde-4c47-ab68-95407d548318",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8pdUDyeu38r1VC6s18ihG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 25176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 790
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T02:10:26.515Z_

<details><summary>↩ Tool result · `toolu_017MR67MJLUhTh124RbMs4ra`</summary>

```text
1	# §4 Experiments
2	
3	## §4.1 Experimental Setup
4	
5	**Dataset.** We construct our training corpus from SWE-bench \cite{jimenez2024swebench}, a benchmark of real-world GitHub issues paired with developer-authored patches. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, we run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,897 instances across 123 repositories with structural data, yielding a structural coverage rate of 36%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.
6	
7	For each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.
8	
9	**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \in \{1, 5, 10\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\theta^*_{\text{R@1}}$), as discussed in §3.3.
10	
11	**Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \cite{cocohanere2025}.
12	
13	## §4.2 Implementation Details
14	
15	**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} and **StarCoder2-3B** \cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.
16	
17	**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with temperature $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
18	
19	For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1).
20	
21	**Negative Mining.** Embedding-distance negatives are mined using FAISS \cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.
22	
23	**Hardware.** All experiments are conducted on a single node with 2$\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the full experiment matrix (3 strategies $\times$ 3 seeds $\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours.
24	
25	## §4.3 Results
26	
27	### Main Results
28	
29	Table 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\pm$ standard deviation over three seeds.
30	
31	**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.
32	
33	| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |
34	|---|---|---|---|---|---|---|
35	| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |
36	| BM25 (no training) | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} |
37	| Random | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
38	| BM25-mined | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
39	| Embedding-distance | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
40	| Dataflow-aware | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
41	
42	**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\placeholder{+X.X}pp and \placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.
43	
44	### Pilot Validation
45	
46	Prior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.
47	
48	**Table 2: Pilot results (single seed, 24-repo subset).** Pool size = 50.
49	
50	| Strategy | Qwen R@1 | StarCoder R@1 |
51	|---|---|---|
52	| Random | 0.536 | 0.492 |
53	| Embedding-distance | 0.556 (+2.0pp) | 0.508 (+1.6pp) |
54	| Dataflow-aware | 0.544 (+0.8pp) | 0.487 (−0.5pp) |
55	
56	The pilot established two findings subsequently confirmed at full scale: (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.
57	
58	### Ablations
59	
60	**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\in \{50, 100, 200, 500\}$.
61	
62	**Table 3: R@1 by pool size.**
63	
64	| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\Delta$ | SC Emb. | SC Rand. | SC $\Delta$ |
65	|---|---|---|---|---|---|---|
66	| 50 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
67	| 100 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
68	| 200 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
69	| 500 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
70	
71	**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.
72	
73	| Strategy | Qwen R@1 (s42) |
74	|---|---|
75	| Static embedding-distance | \placeholder{X.XX} |
76	| Dynamic (epoch re-mining) | \placeholder{X.XX} |
77	
78	### Downstream Evaluation
79	
80	**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).
81	
82	| Retriever | Resolve Rate |
83	|---|---|
84	| BM25 | \placeholder{X.X%} |
85	| Random-trained | \placeholder{X.X%} |
86	| Embedding-trained (Qwen) | \placeholder{X.X%} |
87	
88	## §4.4 Analysis
89	
90	### Representation Geometry and Negative Difficulty
91	
92	A central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.
93	
94	**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\_sim − neg\_sim.
95	
96	| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |
97	|---|---|---|---|---|---|---|
98	| | pos\_sim | neg\_sim | margin | pos\_sim | neg\_sim | margin |
99	| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |
100	| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |
101	| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |
102	
103	Several patterns emerge from Table 4:
104	
105	**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\times$ larger margins across all strategies, indicating a more separable pretrained space.
106	
107	**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.
108	
109	**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.
110	
111	### Stratified Analysis
112	
113	We stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.
114	
115	**Table 5: R@1 stratified by structural data availability.**
116	
117	| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\Delta$ | SC (Emb.) | SC (DF) | $\Delta$ |
118	|---|---|---|---|---|---|---|---|
119	| Rich dataflow ($\geq$5 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
120	| Sparse dataflow (1–4 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
121	| No structural data (fallback) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
122	
123	Confound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.
124	
125	### CodeQL Scalability
126	
127	We report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).
128	
129	**Table 6: CodeQL extraction scalability by repository tier.**
130	
131	| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |
132	|---|---|---|---|---|---|
133	| Small (<50 files) | 1 | 500 | 0% | 81.0% | 0.0% |
134	| Medium (50–200) | 17 | 4,096 | 0% | 47.2% | 50.0% |
135	| Large (200–500) | 40 | 13,628 | 0% | 34.3% | 85.7% |
136	| XLarge (500+) | 29 | 25,949 | 0% | 31.4% | 96.0% |
137	| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |
138	
139	The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.
140	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "9aaab14a-ab77-4632-849d-26359b686add",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1.md",
      "content": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-bench \\cite{jimenez2024swebench}, a benchmark of real-world GitHub issues paired with developer-authored patches. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, we run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,897 instances across 123 repositories with structural data, yielding a structural coverage rate of 36%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{cocohanere2025}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with temperature $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the full experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours.\n\n## §4.3 Results\n\n### Main Results\n\nTable 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\\pm$ standard deviation over three seeds.\n\n**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |\n| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\n| Random | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Embedding-distance | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n\n**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\\placeholder{+X.X}pp and \\placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \\placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.\n\n### Pilot Validation\n\nPrior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.\n\n**Table 2: Pilot results (single seed, 24-repo subset).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.536 | 0.492 |\n| Embedding-distance | 0.556 (+2.0pp) | 0.508 (+1.6pp) |\n| Dataflow-aware | 0.544 (+0.8pp) | 0.487 (−0.5pp) |\n\nThe pilot established two findings subsequently confirmed at full scale: (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n\n### Ablations\n\n**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\\in \\{50, 100, 200, 500\\}$.\n\n**Table 3: R@1 by pool size.**\n\n| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\\Delta$ | SC Emb. | SC Rand. | SC $\\Delta$ |\n|---|---|---|---|---|---|---|\n| 50 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 100 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 200 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 500 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n\n**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.\n\n| Strategy | Qwen R@1 (s42) |\n|---|---|\n| Static embedding-distance | \\placeholder{X.XX} |\n| Dynamic (epoch re-mining) | \\placeholder{X.XX} |\n\n### Downstream Evaluation\n\n**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).\n\n| Retriever | Resolve Rate |\n|---|---|\n| BM25 | \\placeholder{X.X%} |\n| Random-trained | \\placeholder{X.X%} |\n| Embedding-trained (Qwen) | \\placeholder{X.X%} |\n\n## §4.4 Analysis\n\n### Representation Geometry and Negative Difficulty\n\nA central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\n\n**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\\_sim − neg\\_sim.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | pos\\_sim | neg\\_sim | margin | pos\\_sim | neg\\_sim | margin |\n| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |\n| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |\n| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\n\nSeveral patterns emerge from Table 4:\n\n**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\\times$ larger margins across all strategies, indicating a more separable pretrained space.\n\n**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.\n\n**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n\n### Stratified Analysis\n\nWe stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\n\n**Table 5: R@1 stratified by structural data availability.**\n\n| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\\Delta$ | SC (Emb.) | SC (DF) | $\\Delta$ |\n|---|---|---|---|---|---|---|---|\n| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| No structural data (fallback) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n\nConfound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\n\n### CodeQL Scalability\n\nWe report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).\n\n**Table 6: CodeQL extraction scalability by repository tier.**\n\n| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |\n|---|---|---|---|---|---|\n| Small (<50 files) | 1 | 500 | 0% | 81.0% | 0.0% |\n| Medium (50–200) | 17 | 4,096 | 0% | 47.2% | 50.0% |\n| Large (200–500) | 40 | 13,628 | 0% | 34.3% | 85.7% |\n| XLarge (500+) | 29 | 25,949 | 0% | 31.4% | 96.0% |\n| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n",
      "numLines": 140,
      "startLine": 1,
      "totalLines": 140
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01PPe3h93DhNszhp1wzZyHE1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "fa1c3002-e4c9-4517-98c2-5f7138a8e8fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8pdUDyeu38r1VC6s18ihG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 25176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 790
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T02:10:26.755Z_

<details><summary>↩ Tool result · `toolu_01PPe3h93DhNszhp1wzZyHE1`</summary>

```text
1	# 1. Introduction
2	
3	Code retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \cite{liu2024repobench}, fault localization \cite{chen2025locagent}, and automated program repair \cite{jimenez2024swebench}.
4	Contrastive learning has become the dominant paradigm for training dense code retrievers \cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \cite{chen2020simclr,xiong2021ance}.
5	Despite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.
6	As retrieval scales to repository-level settings with hundreds of candidate files \cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.
7	
8	Existing negative selection approaches span a broad spectrum but leave a critical gap.
9	Random negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \cite{karpukhin2020dpr}.
10	Embedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.
11	CoCoHaNeRe \cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.
12	Meanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.
13	Notably, files that are close in embedding space may be structurally connected through shared data-flow paths \cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.
14	
15	We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.
16	Using CodeQL \cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.
17	We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.
18	All experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.
19	
20	Our experiments on CodeSearchNet \cite{husain2019codesearchnet} yield three principal findings.
21	First, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \cite{fan2025cocohanere}.
22	Second, as an \textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis reveals that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\ ${\sim}0.80$ for StarCoder) mediates strategy effectiveness, providing a mechanistic hypothesis for when different strategies should be preferred (pending multi-seed confirmation).
23	Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\% timeout rate and [TBD]\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.
24	
25	Our contributions are as follows:
26	\begin{enumerate}
27	\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.
28	\item \textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.
29	\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.
30	\end{enumerate}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "9a83d1dc-5ac2-41d0-9139-f791e7572611",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction_v2.md",
      "content": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis reveals that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) mediates strategy effectiveness, providing a mechanistic hypothesis for when different strategies should be preferred (pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

````text
Now let me analyze each file for dataflow-aware strategy descriptions:

### method_v1.md
Lines 55-59 describe the dataflow-aware strategy. The key formula on line 57:

```
$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \notin \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$


```

But this is using pretrained encoder similarity when it should actually be using BM25 for the ranking. The description mentions surface-level textual features which aligns with BM25, but the formula and the explanation about falling back to embedding-distance mining both need to be corrected to reflect BM25-based ranking instead.

Now I'm going through the documentation files to find and fix all the places where embedding distance is mentioned as the selection mechanism for dataflow-aware negatives. The task clearly states it should be BM25 ranking, not embedding similarity, so I need to update those descriptions in experiment_setup_v1.md and experiments_v1.md where they incorrectly say "selecting by embedding distance."

``` I need to figure out which tool to use for saving these paper section files—`save_project_file` has a whitelist that might not include them, so I should look for dedicated write or edit tools for paper sections instead. Let me first map out all the changes I've identified across the files before deciding how to save them. Looking more carefully at the actual definition, I see the dataflow-aware mining strategy uses a reachability set based on the structural graph to identify negatives that are textually similar but structurally disconnected. Let me trace through what changes are actually needed versus what's just descriptive language that happens to align with BM25 concepts. I'm realizing there's a discrepancy between what the task description specifies and what the current method actually implements. The task says to use CodeQL for structural filtering followed by BM25 ranking to select the most similar structurally-connected non-gold files, but the current approach filters out structurally reachable files and ranks by embedding similarity instead—essentially doing the opposite. 结构连通" means structurally connected. So the strategy is:
1. Use CodeQL to find structurally connected files (files that ARE connected to query)
2. Among these structurally connected non-gold files, use BM25 to rank and select top-K

This is different from what the paper currently says! The current paper says:
1. Filter OUT structurally reachable files
2. Among structurally UNREACHABLE files, use embedding similarity to rank

So there are TWO errors:
1. The ranking method: should be BM25, not embedding similarity
2. The structural filter direction: should select from structurally CONNECTED files, not structurally DISCONNECTED files

The task is asking me to find paragraphs describing the dataflow-aware negative sampling strategy and correct any mentions of embedding similarity or cosine similarity to use BM25 instead. The fix should specify using CodeQL's 2-hop bounded data-flow to identify structurally connected files, then applying BM25 ranking to select the top-K non-gold files as negative samples, replacing the similarity formula with BM25(q, f). I see the issue now — the negatives should come from structurally connected files, not disconnected ones. The task is asking me to align the paper with the code, which uses BM25 ranking within those connected files rather than embedding similarity. So there are two corrections needed: the filter direction and the ranking method. I see the task is specifically about fixing the ranking method from embedding similarity to BM25, but looking at the actual implementation, both the ranking method AND the filter direction are incorrect in the paper. The current description filters out structurally reachable files and ranks among unreachable ones using embeddings, when it should actually filter for structurally connected files first, then rank those using BM25. I need to correct both aspects to match what the code actually does.

Now I'm planning the specific edits needed for each file, starting with the Dataflow-Aware Mining section where I'll change the description from filtering disconnected files to filtering connected ones, and swap the ranking formula from embedding similarity to BM25. I see the issue now — the structurally connected non-gold files are actually the hard negatives, not the unreachable ones. The current paper has it backwards: it's selecting files that are textually similar but structurally disconnected, when it should be selecting files that are structurally connected to the gold files but aren't gold themselves. So I need to flip the filter direction from unreachable to connected, and switch the ranking method from embedding similarity to BM25 to match what the code actually does.

The main fix is updating how the dataflow-aware negatives are described — changing from embedding similarity ranking to BM25 ranking. I can use the Edit tool to directly modify the paper files in the artifacts directory. I should just edit the files directly since that's simpler than searching for MCP tools. Let me read the paper_drafts versions to see if they match the _project/paper versions, then make my edits accordingly.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "29243063-a0d1-45e3-b2ec-ad6d211ad6d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BA2PkdshDM3Ky6ntSUfNax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11183,
      "cache_read_input_tokens": 25966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11183
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

现在我已读完全部四个文件。让我检查 `paper_drafts/` 版本是否相同，以及是否有专用的论文编辑工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "1f542987-200a-41f0-b855-8425bf898703",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BA2PkdshDM3Ky6ntSUfNax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11183,
      "cache_read_input_tokens": 25966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11183
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01E6S8gcowzPKdYgCPAq3wQ9`</summary>

```json
{
  "query": "edit_paper_section write_paper_section",
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
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "b21df59e-408a-4d29-8965-7f9be512ca59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BA2PkdshDM3Ky6ntSUfNax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11183,
      "cache_read_input_tokens": 25966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11183
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T02:11:58.604Z_

<details><summary>↩ Tool result · `toolu_01E6S8gcowzPKdYgCPAq3wQ9`</summary>

````text
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
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "769bb426-89cb-4895-8f90-da0412837d42",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "edit_paper_section write_paper_section",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01SUtyYQ3FTgLvbYc3JcZQMT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
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
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "1d226060-55c9-45c9-8884-be62197ae3b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BA2PkdshDM3Ky6ntSUfNax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11183,
      "cache_read_input_tokens": 25966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11183
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T02:11:58.948Z_

<details><summary>↩ Tool result · `toolu_01SUtyYQ3FTgLvbYc3JcZQMT`</summary>

```text
1	# §3 Method
2	
3	## §3.1 Problem Formulation
4	
5	We address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\mathcal{F} = \{f_1, f_2, \ldots, f_N\}$. The gold set $\mathcal{F}^+_q \subset \mathcal{F}$ denotes the files modified in the ground-truth patch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "b5b35adc-1ca3-4934-b411-0df2d8eef5d6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
      "content": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 116
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the `edit_paper_section` and `write_paper_section` tools specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "0fbc2add-fa91-4193-921d-8f01d135857d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7pRWtudWt7gexxCS5bp6j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5013,
      "cache_read_input_tokens": 37149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5013
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

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01F3SP4iDa4yiu1cmSfsP86j`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__edit_paper_section,mcp__agent-ml-research__write_paper_section",
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
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "8c5a86d2-7660-49f1-a341-a2bde4179a89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7pRWtudWt7gexxCS5bp6j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5013,
      "cache_read_input_tokens": 37149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5013
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

_source line 44 · 2026-05-15T02:12:02.437Z_

<details><summary>↩ Tool result · `toolu_01F3SP4iDa4yiu1cmSfsP86j`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "282a273d-dff6-4054-bb4f-2a17718b2fee",
  "tool_use_result": {
    "matches": [],
    "query": "select:mcp__agent-ml-research__edit_paper_section,mcp__agent-ml-research__write_paper_section",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
The `edit_paper_section` and `write_paper_section` tools don't exist as deferred tools. Let me try a broader search.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "25965c69-786f-4c15-999b-519ace1a3be9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qess2RqbSnUsj9e3ELstkX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 42162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 160
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VhExT4ypzHXBzGtTpcKrRk`</summary>

```json
{
  "query": "paper section",
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
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "57bc62ca-9f65-4041-9ef3-36c7f22cc83f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qess2RqbSnUsj9e3ELstkX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 42162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 160
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T02:12:06.117Z_

<details><summary>↩ Tool result · `toolu_01VhExT4ypzHXBzGtTpcKrRk`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
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
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "f64fcdac-b7f9-49f9-88da-f650e5070cad",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "paper section",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
The `write_paper_section` and `edit_paper_section` tools aren't available as deferred tools. Let me just use the Edit tool to directly edit the files on disk. I'll edit both copies (`_project/paper/` and `paper_drafts/`).

Let me now identify all the changes needed across the four files:

### method_v1.md — NEEDS CHANGES

**Lines 55-57**: The dataflow-aware formula and description. Currently says negatives are structurally UNREACHABLE and ranked by `sim(E_θ0(q), E_θ0(f))`. Should say negatives are structurally CONNECTED and ranked by BM25.


Looking at the exact text in lines 55-59, I can see it defines the reachability set using the transitive closure of the structural connectivity graph to identify which files are reachable from the gold files.

The next thinking continues by defining the selection formula for dataflow-aware negatives—picking the most textually similar files that are structurally unreachable from the gold set. The key insight is that these negatives are particularly valuable for training because they look relevant on the surface through shared variable names and API patterns, but lack the actual inter-procedural data-flow connections that indicate genuine functional relationships. I'm refining the negative sampling strategy: first, CodeQL identifies structurally connected files within a 2-hop bounded data-flow reachability set, then BM25 ranks these non-gold files by textual similarity to select the top-K. This creates particularly hard negatives since they're both structurally related through actual code dependencies and textually similar, forcing the encoder to learn fine-grained distinctions beyond surface-level overlap. For the difficulty gradient, I should clarify that random negatives are the easiest baseline, embedding-distance negatives add pretrained similarity constraints, and dataflow-aware negatives layer on structural connectivity to create the hardest learning signal. I'm seeing that the dataflow-aware negative selection strategy needs clarification. Instead of just filtering by embedding distance, it should identify structurally connected files through the CodeQL graph, then rank candidates using BM25 to select the top-K non-gold negatives. This is a more precise description of what's actually happening in the approach. The task specifies fixing only descriptions that explicitly mention embedding similarity or cosine similarity for dataflow-aware ranking, so the analysis section doesn't need changes even though its reasoning about excluded negatives assumes the old filter direction. Looking at the task description again, it's specifically about fixing the ranking method to BM25, not about changing the filter condition. Though I notice the correct behavior does involve selecting from structurally connected files rather than disconnected ones—that would require changing `f \notin \mathcal{R}_G(q)` to `f \in \mathcal{R}_G(q)`—but since the task only explicitly asks for the ranking fix, I should stick to that scope.

Now checking the introduction_v2.md file more carefully, particularly line 17 which describes filtering structurally connected files from an embedding-distance candidate set. The phrasing is a bit unclear about whether it's selecting connected files or filtering them out.

The correct approach should be: dataflow-aware mining selects from structurally connected files that are ranked by BM25 similarity, not embedding distance. I need to update this description across the paper files and verify whether the paper_drafts directory contains symlinks or separate copies that also need editing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "2529a74a-d984-45e4-bd92-8d7106313428",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jwwx6yV4KLTibC6X4gSd8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 42322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1179
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

### Assistant

_source line 49_

没有找到 `edit_paper_section` 工具。我直接用 Edit 编辑文件。让我先确认两个目录的文件是否相同。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "feeeafc8-6d96-461c-be44-92c375506fe6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jwwx6yV4KLTibC6X4gSd8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 42322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1179
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

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01QP7TRRAC2NZid7ffEEGHuH`</summary>

```json
{
  "command": "diff artifacts/_project/paper/method_v1.md artifacts/paper_drafts/method_v1.md && echo \"SAME\" || echo \"DIFFERENT\"",
  "description": "Compare two copies of method_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "418bbb71-2133-4e9f-872c-7c4a489d0e62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jwwx6yV4KLTibC6X4gSd8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 42322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1179
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

_source line 51 · 2026-05-15T02:13:13.630Z_

<details><summary>↩ Tool result · `toolu_01QP7TRRAC2NZid7ffEEGHuH`</summary>

```text
7c7
< We formulate this as a contrastive learning problem. Let $E_\theta$ be a pretrained encoder parameterized by $\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files. Concretely, we optimize $\theta$ such that for all $f^+ \in \mathcal{F}^+_q$ and $f^- \in \mathcal{F} \setminus \mathcal{F}^+_q$:
---
> We formulate this as a contrastive learning problem. Let $E_\theta$ be a pretrained encoder parameterized by $\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:
13c13
< The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. Random negatives are often too easy, providing weak gradient signal \cite{chen2020simclr}. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.
---
> The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.
15c15
< ## §3.2 StructFuse Pipeline
---
> ## §3.2 Structural Information Extraction
17c17
< Our pipeline consists of three stages: (1) structural graph extraction via static analysis, (2) training data construction with strategy-specific negative mining, and (3) contrastive fine-tuning of a pretrained code encoder.
---
> ### CodeQL Bounded Data-Flow Analysis
19c19
< **CodeQL Extraction.** We use CodeQL \cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. Specifically, we define taint-tracking queries that trace data flow from designated sources to sinks, crossing function call boundaries. This yields a set of data-flow paths $\mathcal{P} = \{(v_{\text{src}}, v_1, \ldots, v_{\text{sink}})\}$, where each node $v_i$ is annotated with its enclosing file.
---
> We use CodeQL \cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:
21c21,22
< We set a scope bound on the analysis depth to ensure tractability: queries that exceed a predefined step limit are terminated. In practice, this achieves 0\% timeout rate across 123 out of 131 repositories in our dataset.
---
> - **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.
> - **Data-flow graph**: inter-procedural data-flow paths $\mathcal{P} = \{(v_{\text{src}}, v_1, \ldots, v_{\text{sink}})\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.
23c24,26
< **Structural Connectivity Graph.** From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \mathcal{F}$ and an edge $(f_i, f_j) \in E$ exists if and only if at least one data-flow path in $\mathcal{P}$ traverses both $f_i$ and $f_j$. This graph captures inter-procedural structural relationships between files—two files are connected if data flows between them across function call boundaries.
---
> ### File-Level Reachability
> 
> From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \mathcal{F}$ and an edge $(f_i, f_j) \in E$ exists if and only if at least one data-flow path in $\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.
27c30
< **Structural Coverage.** At full scale, 78\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.
---
> At full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].
29c32
< ## §3.3 Training Objective
---
> ### Beniget Fallback
31c34
< **Contrastive Loss.** We train with InfoNCE loss \cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\{f^-_1, \ldots, f^-_K\}$, the loss is:
---
> For repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].
33c36,45
< $$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$
---
> ### Coverage Statistics
> 
> The extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:
> 
> | Metric | Value |
> |--------|-------|
> | Timeout rate | 0% (all repository tiers) |
> | Repository coverage | 123/131 (93.9%) |
> | Structural data rate | 34% of instances |
> | Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |
35c47
< where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query.
---
> The 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.
37c49
< **Encoder Architecture.** We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}—which differ in pretraining objectives (Fill-in-the-Middle vs. multi-task including Fill-in-the-Middle) and exhibit distinct representation geometries (§5). Each encoder is augmented with a linear projection head that maps the last hidden state to a 256-dimensional embedding space.
---
> ## §3.3 Structure-Aware Negative Mining
39c51
< **Parameter-Efficient Fine-Tuning.** We apply LoRA \cite{hu2022lora} to the query and value projection matrices ($W_q$, $W_v$) of each attention layer with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated. We use AdamW with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing with 10\% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2048 tokens. Training runs for 3 epochs with evaluation every 500 steps.
---
> We compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.
41c53
< **Dual Checkpoint Selection.** We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\theta^*_{\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement.
---
> ### Random Negatives
43c55
< ## §3.4 Negative Mining Strategies
---
> For each query $q$, we sample $K$ negatives uniformly at random from $\mathcal{F} \setminus \mathcal{F}^+_q$:
45c57
< We compare three negative mining strategies that span a spectrum from uninformed to structure-grounded selection.
---
> $$f^-_{\text{rand}} \sim \text{Uniform}(\mathcal{F} \setminus \mathcal{F}^+_q), \quad |\{f^-_{\text{rand}}\}| = K$$
47c59
< **Random Mining.** For each query $q$, we sample $K$ negatives uniformly at random from $\mathcal{F} \setminus \mathcal{F}^+_q$. This serves as the baseline: negatives are unbiased but typically easy, as randomly chosen files are unlikely to share topical or structural similarity with the query.
---
> This baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.
49c61,63
< **Embedding-Distance Mining.** We compute embeddings for all files and queries using the frozen pretrained encoder $E_{\theta_0}$ (before fine-tuning) and build a FAISS index \cite{johnson2021faiss} over file embeddings. For each query $q$, we retrieve the $K$ non-gold files with highest cosine similarity to $q$ in the pretrained embedding space:
---
> ### Embedding-Distance Negatives
> 
> We compute embeddings for all files and queries using $E_{\theta_0}$ (before fine-tuning) and build a FAISS index \cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:
53c67,71
< This selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \cite{xiong2021ance}.
---
> These negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\theta_0}$ and avoids the instability and computational overhead of online re-mining \cite{xiong2021ance}.
> 
> ### Dataflow-Aware Negatives
> 
> This strategy combines embedding distance with structural reachability filtering. For query $q$ with gold files $\mathcal{F}^+_q$, define the reachability set:
55c73,75
< **Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\mathcal{F}^+_q$, we define the reachability set $\mathcal{R}_G(q) = \{f \in \mathcal{F} : \exists f^+ \in \mathcal{F}^+_q,\ (f^+, f) \in E^*\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:
---
> $$\mathcal{R}_G(q) = \{f \in \mathcal{F} : \exists f^+ \in \mathcal{F}^+_q,\ (f^+, f) \in E^*\}$$
> 
> where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:
59c79,111
< That is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.
---
> These files are simultaneously similar in the embedding space (hard) and structurally disconnected in the data-flow graph (informative). They represent a category of false positives of textual similarity: files that appear relevant based on surface features (shared imports, API patterns, variable names) but lack the inter-procedural data-flow connections that characterize functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.
> 
> For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).
> 
> ### Difficulty Gradient
> 
> The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).
> 
> ### Relationship to BM25 Baselines
> 
> In addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].
> 
> ## §3.4 Contrastive Fine-tuning
> 
> ### InfoNCE Loss
> 
> We train with InfoNCE loss \cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\{f^-_1, \ldots, f^-_K\}$:
> 
> $$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$
> 
> where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].
> 
> ### LoRA Fine-tuning Setup
> 
> We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}—using LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.
> 
> Each encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].
> 
> Training uses AdamW with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
> 
> ### Dual Checkpoint Strategy
> 
> We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\theta^*_{\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].
61c113
< **Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).
---
> ### Early Stopping
63c115
< For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\% of training instances, which we analyze separately in stratified evaluation (§5).
---
> The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].
DIFFERENT
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "94b5c2fb-c257-4b0a-8ba5-904410cac350",
  "tool_use_result": {
    "stdout": "7c7\n< We formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files. Concretely, we optimize $\\theta$ such that for all $f^+ \\in \\mathcal{F}^+_q$ and $f^- \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n---\n> We formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\n13c13\n< The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. Random negatives are often too easy, providing weak gradient signal \\cite{chen2020simclr}. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n---\n> The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n15c15\n< ## §3.2 StructFuse Pipeline\n---\n> ## §3.2 Structural Information Extraction\n17c17\n< Our pipeline consists of three stages: (1) structural graph extraction via static analysis, (2) training data construction with strategy-specific negative mining, and (3) contrastive fine-tuning of a pretrained code encoder.\n---\n> ### CodeQL Bounded Data-Flow Analysis\n19c19\n< **CodeQL Extraction.** We use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. Specifically, we define taint-tracking queries that trace data flow from designated sources to sinks, crossing function call boundaries. This yields a set of data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file.\n---\n> We use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\n21c21,22\n< We set a scope bound on the analysis depth to ensure tractability: queries that exceed a predefined step limit are terminated. In practice, this achieves 0\\% timeout rate across 123 out of 131 repositories in our dataset.\n---\n> - **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.\n> - **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\n23c24,26\n< **Structural Connectivity Graph.** From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. This graph captures inter-procedural structural relationships between files—two files are connected if data flows between them across function call boundaries.\n---\n> ### File-Level Reachability\n> \n> From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\n27c30\n< **Structural Coverage.** At full scale, 78\\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.\n---\n> At full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\n29c32\n< ## §3.3 Training Objective\n---\n> ### Beniget Fallback\n31c34\n< **Contrastive Loss.** We train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$, the loss is:\n---\n> For repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].\n33c36,45\n< $$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n---\n> ### Coverage Statistics\n> \n> The extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:\n> \n> | Metric | Value |\n> |--------|-------|\n> | Timeout rate | 0% (all repository tiers) |\n> | Repository coverage | 123/131 (93.9%) |\n> | Structural data rate | 34% of instances |\n> | Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |\n35c47\n< where $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query.\n---\n> The 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.\n37c49\n< **Encoder Architecture.** We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—which differ in pretraining objectives (Fill-in-the-Middle vs. multi-task including Fill-in-the-Middle) and exhibit distinct representation geometries (§5). Each encoder is augmented with a linear projection head that maps the last hidden state to a 256-dimensional embedding space.\n---\n> ## §3.3 Structure-Aware Negative Mining\n39c51\n< **Parameter-Efficient Fine-Tuning.** We apply LoRA \\cite{hu2022lora} to the query and value projection matrices ($W_q$, $W_v$) of each attention layer with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated. We use AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10\\% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2048 tokens. Training runs for 3 epochs with evaluation every 500 steps.\n---\n> We compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\n41c53\n< **Dual Checkpoint Selection.** We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement.\n---\n> ### Random Negatives\n43c55\n< ## §3.4 Negative Mining Strategies\n---\n> For each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n45c57\n< We compare three negative mining strategies that span a spectrum from uninformed to structure-grounded selection.\n---\n> $$f^-_{\\text{rand}} \\sim \\text{Uniform}(\\mathcal{F} \\setminus \\mathcal{F}^+_q), \\quad |\\{f^-_{\\text{rand}}\\}| = K$$\n47c59\n< **Random Mining.** For each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$. This serves as the baseline: negatives are unbiased but typically easy, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n---\n> This baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n49c61,63\n< **Embedding-Distance Mining.** We compute embeddings for all files and queries using the frozen pretrained encoder $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we retrieve the $K$ non-gold files with highest cosine similarity to $q$ in the pretrained embedding space:\n---\n> ### Embedding-Distance Negatives\n> \n> We compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\n53c67,71\n< This selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \\cite{xiong2021ance}.\n---\n> These negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.\n> \n> ### Dataflow-Aware Negatives\n> \n> This strategy combines embedding distance with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n55c73,75\n< **Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n---\n> $$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n> \n> where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n59c79,111\n< That is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.\n---\n> These files are simultaneously similar in the embedding space (hard) and structurally disconnected in the data-flow graph (informative). They represent a category of false positives of textual similarity: files that appear relevant based on surface features (shared imports, API patterns, variable names) but lack the inter-procedural data-flow connections that characterize functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.\n> \n> For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n> \n> ### Difficulty Gradient\n> \n> The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n> \n> ### Relationship to BM25 Baselines\n> \n> In addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n> \n> ## §3.4 Contrastive Fine-tuning\n> \n> ### InfoNCE Loss\n> \n> We train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:\n> \n> $$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n> \n> where $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].\n> \n> ### LoRA Fine-tuning Setup\n> \n> We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—using LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.\n> \n> Each encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].\n> \n> Training uses AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n> \n> ### Dual Checkpoint Strategy\n> \n> We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].\n61c113\n< **Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).\n---\n> ### Early Stopping\n63c115\n< For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).\n---\n> The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\nDIFFERENT",
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

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01WMA7kzxz26NtE9pD4o7HtY`</summary>

```json
{
  "command": "diff artifacts/_project/paper/experiment_setup_v1.md artifacts/paper_drafts/experiment_setup_v1.md && echo \"SAME\" || echo \"DIFFERENT\"",
  "description": "Compare two copies of experiment_setup_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "1eeae1ed-3bdf-471f-951b-f9aaf9079ab2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jwwx6yV4KLTibC6X4gSd8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 42322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1179
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

_source line 53 · 2026-05-15T02:13:14.538Z_

<details><summary>↩ Tool result · `toolu_01WMA7kzxz26NtE9pD4o7HtY`</summary>

```text
27c27
< The two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction reveals how representation geometry mediates strategy effectiveness.
---
> The two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction may reveal how representation geometry mediates strategy effectiveness.
74a75,76
> 
> &lt;!-- Claim 2 wording fix: 2026-05-15 -->
DIFFERENT
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "0c672fc3-1bb0-4040-994b-96101e6880d5",
  "tool_use_result": {
    "stdout": "27c27\n< The two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction reveals how representation geometry mediates strategy effectiveness.\n---\n> The two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction may reveal how representation geometry mediates strategy effectiveness.\n74a75,76\n> \n> &lt;!-- Claim 2 wording fix: 2026-05-15 -->\nDIFFERENT",
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

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01UxjJ7CUCrCCeYpU8CGsvFU`</summary>

```json
{
  "command": "diff artifacts/_project/paper/experiments_v1.md artifacts/paper_drafts/experiments_v1.md && echo \"SAME\" || echo \"DIFFERENT\"",
  "description": "Compare two copies of experiments_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "ac0911e4-0636-4279-9da7-8ae1216a2e42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jwwx6yV4KLTibC6X4gSd8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 42322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1179
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

_source line 55 · 2026-05-15T02:13:15.469Z_

<details><summary>↩ Tool result · `toolu_01UxjJ7CUCrCCeYpU8CGsvFU`</summary>

```text
5c5
< **Dataset.** We construct our training corpus from SWE-bench \cite{jimenez2024swebench}, a benchmark of real-world GitHub issues paired with developer-authored patches. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, we run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,897 instances across 123 repositories with structural data, yielding a structural coverage rate of 36%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.
---
> **Dataset.** We construct our training corpus from SWE-smith \cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \placeholder{34.3%} [pending recalc]. The remaining \placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.
11c11
< **Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \cite{cocohanere2025}.
---
> **Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}.
15c15
< **Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} and **StarCoder2-3B** \cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.
---
> **Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} and **StarCoder2-3B** \cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.
17c17
< **Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with temperature $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
---
> **Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
23c23
< **Hardware.** All experiments are conducted on a single node with 2$\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the full experiment matrix (3 strategies $\times$ 3 seeds $\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours.
---
> **Hardware.** All experiments are conducted on a single node with 2$\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\times$ 3 seeds $\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.
48c48
< **Table 2: Pilot results (single seed, 24-repo subset).** Pool size = 50.
---
> **Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.
52,54c52,54
< | Random | 0.536 | 0.492 |
< | Embedding-distance | 0.556 (+2.0pp) | 0.508 (+1.6pp) |
< | Dataflow-aware | 0.544 (+0.8pp) | 0.487 (−0.5pp) |
---
> | Random | 0.5357 | 0.4922 |
> | Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |
> | Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |
56c56
< The pilot established two findings subsequently confirmed at full scale: (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.
---
> The pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.
109c109
< **Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.
---
> **Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.
129c129,130
< **Table 6: CodeQL extraction scalability by repository tier.**
---
> &lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->
> **Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.
133,137c134,138
< | Small (<50 files) | 1 | 500 | 0% | 81.0% | 0.0% |
< | Medium (50–200) | 17 | 4,096 | 0% | 47.2% | 50.0% |
< | Large (200–500) | 40 | 13,628 | 0% | 34.3% | 85.7% |
< | XLarge (500+) | 29 | 25,949 | 0% | 31.4% | 96.0% |
< | **Total** | **123** | **44,173** | **0%** | **36.0%** | — |
---
> | Small (<50 inst.) | 18 | 500 | 0% | \placeholder{81.0%} [pending recalc] | 0.0% |
> | Medium (50–200) | 36 | 4,096 | 0% | \placeholder{47.2%} [pending recalc] | 50.0% |
> | Large (200–500) | 40 | 13,628 | 0% | \placeholder{34.3%} [pending recalc] | 85.7% |
> | XLarge (500+) | 29 | 25,949 | 0% | \placeholder{31.4%} [pending recalc] | 96.0% |
> | **Total** | **123** | **44,173** | **0%** | **\placeholder{34.3%} [pending recalc]** | — |
139c140,142
< The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.
---
> The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.
> 
> &lt;!-- Claim 2 wording fix: 2026-05-15 -->
DIFFERENT
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "4ed06e37-a9ad-4bb8-92af-c5f8876e9db4",
  "tool_use_result": {
    "stdout": "5c5\n< **Dataset.** We construct our training corpus from SWE-bench \\cite{jimenez2024swebench}, a benchmark of real-world GitHub issues paired with developer-authored patches. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, we run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,897 instances across 123 repositories with structural data, yielding a structural coverage rate of 36%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n---\n> **Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \\placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \\placeholder{34.3%} [pending recalc]. The remaining \\placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n11c11\n< **Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{cocohanere2025}.\n---\n> **Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}.\n15c15\n< **Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.\n---\n> **Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.\n17c17\n< **Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with temperature $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n---\n> **Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n23c23\n< **Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the full experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours.\n---\n> **Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.\n48c48\n< **Table 2: Pilot results (single seed, 24-repo subset).** Pool size = 50.\n---\n> **Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.\n52,54c52,54\n< | Random | 0.536 | 0.492 |\n< | Embedding-distance | 0.556 (+2.0pp) | 0.508 (+1.6pp) |\n< | Dataflow-aware | 0.544 (+0.8pp) | 0.487 (−0.5pp) |\n---\n> | Random | 0.5357 | 0.4922 |\n> | Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |\n> | Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |\n56c56\n< The pilot established two findings subsequently confirmed at full scale: (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n---\n> The pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n109c109\n< **Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n---\n> **Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n129c129,130\n< **Table 6: CodeQL extraction scalability by repository tier.**\n---\n> &lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->\n> **Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.\n133,137c134,138\n< | Small (<50 files) | 1 | 500 | 0% | 81.0% | 0.0% |\n< | Medium (50–200) | 17 | 4,096 | 0% | 47.2% | 50.0% |\n< | Large (200–500) | 40 | 13,628 | 0% | 34.3% | 85.7% |\n< | XLarge (500+) | 29 | 25,949 | 0% | 31.4% | 96.0% |\n< | **Total** | **123** | **44,173** | **0%** | **36.0%** | — |\n---\n> | Small (<50 inst.) | 18 | 500 | 0% | \\placeholder{81.0%} [pending recalc] | 0.0% |\n> | Medium (50–200) | 36 | 4,096 | 0% | \\placeholder{47.2%} [pending recalc] | 50.0% |\n> | Large (200–500) | 40 | 13,628 | 0% | \\placeholder{34.3%} [pending recalc] | 85.7% |\n> | XLarge (500+) | 29 | 25,949 | 0% | \\placeholder{31.4%} [pending recalc] | 96.0% |\n> | **Total** | **123** | **44,173** | **0%** | **\\placeholder{34.3%} [pending recalc]** | — |\n139c140,142\n< The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n---\n> The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n> \n> &lt;!-- Claim 2 wording fix: 2026-05-15 -->\nDIFFERENT",
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

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_01JbTqkTDiZPth4DqgPMwPtV`</summary>

```json
{
  "command": "diff artifacts/_project/paper/introduction_v2.md artifacts/paper_drafts/introduction_v2.md && echo \"SAME\" || echo \"DIFFERENT\"",
  "description": "Compare two copies of introduction_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "a8939a47-74c9-4a1c-ba17-901c640e20bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jwwx6yV4KLTibC6X4gSd8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 42322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1179
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

_source line 57 · 2026-05-15T02:13:16.029Z_

<details><summary>↩ Tool result · `toolu_01JbTqkTDiZPth4DqgPMwPtV`</summary>

```text
22c22
< Second, as an \textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis reveals that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\ ${\sim}0.80$ for StarCoder) mediates strategy effectiveness, providing a mechanistic hypothesis for when different strategies should be preferred (pending multi-seed confirmation).
---
> Second, as an \textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\ ${\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).
30a31,32
> 
> &lt;!-- Claim 2 wording fix: 2026-05-15 -->
DIFFERENT
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "b2ecdd77-bae5-4169-be42-0ae99981d349",
  "tool_use_result": {
    "stdout": "22c22\n< Second, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis reveals that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) mediates strategy effectiveness, providing a mechanistic hypothesis for when different strategies should be preferred (pending multi-seed confirmation).\n---\n> Second, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).\n30a31,32\n> \n> &lt;!-- Claim 2 wording fix: 2026-05-15 -->\nDIFFERENT",
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
OK, so the `paper_drafts/` versions are different (more updated) from the `_project/paper/` versions. The `paper_drafts/` appears to be the more recently edited version. Let me read the relevant sections of the paper_drafts versions to identify what needs to change there too.

For method_v1.md paper_drafts version, it's quite different. Let me read the relevant dataflow section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "50b4ddbc-daa0-4ec1-8ac3-5fe7194c3147",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHaeEPKsiCpyiotusNg4W5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12198,
      "cache_read_input_tokens": 43501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12198
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

两个目录的文件内容不同，`paper_drafts/` 是更新版本。让我读取 `paper_drafts/` 版本中的 dataflow-aware 相关段落。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "52e24d6d-466d-459c-a56d-3430003e64c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHaeEPKsiCpyiotusNg4W5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12198,
      "cache_read_input_tokens": 43501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12198
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01U7rfcbf9sy7xbTsTUBPnRH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "476d59a7-ccbc-496a-bf85-e8707075342d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHaeEPKsiCpyiotusNg4W5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12198,
      "cache_read_input_tokens": 43501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12198
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-15T02:13:25.248Z_

<details><summary>↩ Tool result · `toolu_01U7rfcbf9sy7xbTsTUBPnRH`</summary>

```text
1	# §3 Method
2	
3	## §3.1 Problem Formulation
4	
5	We address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\mathcal{F} = \{f_1, f_2, \ldots, f_N\}$. The gold set $\mathcal{F}^+_q \subset \mathcal{F}$ denotes the files modified in the ground-truth patch.
6	
7	We formulate this as a contrastive learning problem. Let $E_\theta$ be a pretrained encoder parameterized by $\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:
8	
9	$$\text{sim}(E_\theta(q), E_\theta(f^+)) \gg \text{sim}(E_\theta(q), E_\theta(f^-))$$
10	
11	where $\text{sim}(\cdot, \cdot)$ denotes cosine similarity.
12	
13	The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.
14	
15	## §3.2 Structural Information Extraction
16	
17	### CodeQL Bounded Data-Flow Analysis
18	
19	We use CodeQL \cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:
20	
21	- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.
22	- **Data-flow graph**: inter-procedural data-flow paths $\mathcal{P} = \{(v_{\text{src}}, v_1, \ldots, v_{\text{sink}})\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.
23	
24	### File-Level Reachability
25	
26	From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \mathcal{F}$ and an edge $(f_i, f_j) \in E$ exists if and only if at least one data-flow path in $\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.
27	
28	A key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.
29	
30	At full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].
31	
32	### Beniget Fallback
33	
34	For repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].
35	
36	### Coverage Statistics
37	
38	The extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:
39	
40	| Metric | Value |
41	|--------|-------|
42	| Timeout rate | 0% (all repository tiers) |
43	| Repository coverage | 123/131 (93.9%) |
44	| Structural data rate | 34% of instances |
45	| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |
46	
47	The 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.
48	
49	## §3.3 Structure-Aware Negative Mining
50	
51	We compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.
52	
53	### Random Negatives
54	
55	For each query $q$, we sample $K$ negatives uniformly at random from $\mathcal{F} \setminus \mathcal{F}^+_q$:
56	
57	$$f^-_{\text{rand}} \sim \text{Uniform}(\mathcal{F} \setminus \mathcal{F}^+_q), \quad |\{f^-_{\text{rand}}\}| = K$$
58	
59	This baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.
60	
61	### Embedding-Distance Negatives
62	
63	We compute embeddings for all files and queries using $E_{\theta_0}$ (before fine-tuning) and build a FAISS index \cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:
64	
65	$$f^-_{\text{embed}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$
66	
67	These negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\theta_0}$ and avoids the instability and computational overhead of online re-mining \cite{xiong2021ance}.
68	
69	### Dataflow-Aware Negatives
70	
71	This strategy combines embedding distance with structural reachability filtering. For query $q$ with gold files $\mathcal{F}^+_q$, define the reachability set:
72	
73	$$\mathcal{R}_G(q) = \{f \in \mathcal{F} : \exists f^+ \in \mathcal{F}^+_q,\ (f^+, f) \in E^*\}$$
74	
75	where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:
76	
77	$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \notin \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$
78	
79	These files are simultaneously similar in the embedding space (hard) and structurally disconnected in the data-flow graph (informative). They represent a category of false positives of textual similarity: files that appear relevant based on surface features (shared imports, API patterns, variable names) but lack the inter-procedural data-flow connections that characterize functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.
80	
81	For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).
82	
83	### Difficulty Gradient
84	
85	The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).
86	
87	### Relationship to BM25 Baselines
88	
89	In addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].
90	
91	## §3.4 Contrastive Fine-tuning
92	
93	### InfoNCE Loss
94	
95	We train with InfoNCE loss \cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\{f^-_1, \ldots, f^-_K\}$:
96	
97	$$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$
98	
99	where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].
100	
101	### LoRA Fine-tuning Setup
102	
103	We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}—using LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.
104	
105	Each encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].
106	
107	Training uses AdamW with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
108	
109	### Dual Checkpoint Strategy
110	
111	We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\theta^*_{\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].
112	
113	### Early Stopping
114	
115	The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].
116	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "018f4bd9-8371-4e4d-a96e-2dbf1ec4d06f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
      "content": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 Structural Information Extraction\n\n### CodeQL Bounded Data-Flow Analysis\n\nWe use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\n\n- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.\n- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\n\n### File-Level Reachability\n\nFrom the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\nAt full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\n\n### Beniget Fallback\n\nFor repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].\n\n### Coverage Statistics\n\nThe extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:\n\n| Metric | Value |\n|--------|-------|\n| Timeout rate | 0% (all repository tiers) |\n| Repository coverage | 123/131 (93.9%) |\n| Structural data rate | 34% of instances |\n| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |\n\nThe 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.\n\n## §3.3 Structure-Aware Negative Mining\n\nWe compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\n\n### Random Negatives\n\nFor each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$f^-_{\\text{rand}} \\sim \\text{Uniform}(\\mathcal{F} \\setminus \\mathcal{F}^+_q), \\quad |\\{f^-_{\\text{rand}}\\}| = K$$\n\nThis baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n### Embedding-Distance Negatives\n\nWe compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.\n\n### Dataflow-Aware Negatives\n\nThis strategy combines embedding distance with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese files are simultaneously similar in the embedding space (hard) and structurally disconnected in the data-flow graph (informative). They represent a category of false positives of textual similarity: files that appear relevant based on surface features (shared imports, API patterns, variable names) but lack the inter-procedural data-flow connections that characterize functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.\n\nFor instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n\n### Difficulty Gradient\n\nThe three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n\n### Relationship to BM25 Baselines\n\nIn addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n\n## §3.4 Contrastive Fine-tuning\n\n### InfoNCE Loss\n\nWe train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].\n\n### LoRA Fine-tuning Setup\n\nWe fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—using LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.\n\nEach encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].\n\nTraining uses AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\n### Dual Checkpoint Strategy\n\nWe observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].\n\n### Early Stopping\n\nThe initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n",
      "numLines": 116,
      "startLine": 1,
      "totalLines": 116
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
Now I have both versions. Let me also read the paper_drafts versions of experiment_setup and experiments for the dataflow-aware sections.

For the `paper_drafts/experiments_v1.md`, let me read the relevant parts - particularly around the negative mining description and the analysis section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "3ae03928-4dad-4a7e-9915-af798c8debbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLSk3rvEjTNKwHaTaAiwiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3673,
      "cache_read_input_tokens": 55699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3673
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01Mt3x522hbfvrhwTJFFevQY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "cd511859-03df-4aa7-a9d5-9e02c0c2690a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLSk3rvEjTNKwHaTaAiwiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3673,
      "cache_read_input_tokens": 55699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3673
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T02:13:35.018Z_

<details><summary>↩ Tool result · `toolu_01Mt3x522hbfvrhwTJFFevQY`</summary>

```text
1	# §4 Experiments
2	
3	## §4.1 Experimental Setup
4	
5	**Dataset.** We construct our training corpus from SWE-smith \cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \placeholder{34.3%} [pending recalc]. The remaining \placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.
6	
7	For each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.
8	
9	**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \in \{1, 5, 10\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\theta^*_{\text{R@1}}$), as discussed in §3.3.
10	
11	**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}.
12	
13	## §4.2 Implementation Details
14	
15	**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} and **StarCoder2-3B** \cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.
16	
17	**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
18	
19	For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1).
20	
21	**Negative Mining.** Embedding-distance negatives are mined using FAISS \cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.
22	
23	**Hardware.** All experiments are conducted on a single node with 2$\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\times$ 3 seeds $\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.
24	
25	## §4.3 Results
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "8b15c786-bc42-4d6b-8569-68204bc6d7c4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
      "content": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \\placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \\placeholder{34.3%} [pending recalc]. The remaining \\placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.\n\n## §4.3 Results",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 143
    }
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Read · `toolu_014bv6xhurCjoE3uMunE8H7c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md",
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "17377d27-6bc0-482c-ae27-d98565c5b38c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLSk3rvEjTNKwHaTaAiwiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3673,
      "cache_read_input_tokens": 55699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3673
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T02:13:35.481Z_

<details><summary>↩ Tool result · `toolu_014bv6xhurCjoE3uMunE8H7c`</summary>

```text
1	# §4 Experimental Setup
2	
3	## §4.1 Dataset
4	
5	We construct our training corpus from SWE-smith \cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit. We expand each task by treating every gold file as a separate training instance, yielding 44,173 instances total [Source: m1_extraction registry, data_count after filtering 6,696 clone/checkout failures from the original 50,869].
6	
7	We run the StructFuse extraction pipeline (§3.2) on all instances. After filtering for extraction errors, we retain 14,288 usable instances across 123 repositories. Of these, approximately 34% possess CodeQL structural connectivity data (15,133 via CodeQL + 764 via beniget fallback); the remaining 66% lack structural data due to transient filesystem failures during batch extraction. For these instances, the dataflow-aware strategy falls back to embedding-distance mining (§3.3) [Source: m1_extraction registry].
8	
9	For each random seed, we perform a per-repository stratified split to produce training and validation partitions. The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties. Exact split sizes:
10	
11	| Seed | Train | Val | Total |
12	|------|-------|-----|-------|
13	| 42 | 11,308 | 2,980 | 14,288 |
14	| 43 | 11,236 | 3,052 | 14,288 |
15	| 44 | 11,264 | 3,024 | 14,288 |
16	
17	[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]
18	
19	## §4.2 Models
20	
21	We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries, enabling us to study how encoder properties mediate the effectiveness of different negative mining strategies.
22	
23	**Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus. It exhibits a near-saturated pretrained representation space: mean positive cosine similarity of 0.986 and mean margin (pos_sim − neg_sim) of only 0.074 with random negatives at 2,048-token context [Source: neg_difficulty_analysis registry, qwen_2048]. This saturation—where nearly all file pairs receive high similarity scores—makes the baseline representation space challenging for contrastive learning and provides a stress test for negative mining strategies.
24	
25	**StarCoder2-3B** \cite{li2023starcoder} uses a multi-task pretraining objective including FIM on The Stack v2. It maintains healthy representation separation: mean positive cosine similarity of 0.799 and a margin of 0.194 with random negatives—2.6× larger than Qwen's [Source: neg_difficulty_analysis registry, starcoder_2048]. This well-separated space allows us to contrast the behavior of mining strategies under fundamentally different geometric conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "f6f76d11-ced0-4759-bfc7-724d9d7efaaf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md",
      "content": "# §4 Experimental Setup\n\n## §4.1 Dataset\n\nWe construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit. We expand each task by treating every gold file as a separate training instance, yielding 44,173 instances total [Source: m1_extraction registry, data_count after filtering 6,696 clone/checkout failures from the original 50,869].\n\nWe run the StructFuse extraction pipeline (§3.2) on all instances. After filtering for extraction errors, we retain 14,288 usable instances across 123 repositories. Of these, approximately 34% possess CodeQL structural connectivity data (15,133 via CodeQL + 764 via beniget fallback); the remaining 66% lack structural data due to transient filesystem failures during batch extraction. For these instances, the dataflow-aware strategy falls back to embedding-distance mining (§3.3) [Source: m1_extraction registry].\n\nFor each random seed, we perform a per-repository stratified split to produce training and validation partitions. The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties. Exact split sizes:\n\n| Seed | Train | Val | Total |\n|------|-------|-----|-------|\n| 42 | 11,308 | 2,980 | 14,288 |\n| 43 | 11,236 | 3,052 | 14,288 |\n| 44 | 11,264 | 3,024 | 14,288 |\n\n[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]\n\n## §4.2 Models\n\nWe select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries, enabling us to study how encoder properties mediate the effectiveness of different negative mining strategies.\n\n**Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus. It exhibits a near-saturated pretrained representation space: mean positive cosine similarity of 0.986 and mean margin (pos_sim − neg_sim) of only 0.074 with random negatives at 2,048-token context [Source: neg_difficulty_analysis registry, qwen_2048]. This saturation—where nearly all file pairs receive high similarity scores—makes the baseline representation space challenging for contrastive learning and provides a stress test for negative mining strategies.\n\n**StarCoder2-3B** \\cite{li2023starcoder} uses a multi-task pretraining objective including FIM on The Stack v2. It maintains healthy representation separation: mean positive cosine similarity of 0.799 and a margin of 0.194 with random negatives—2.6× larger than Qwen's [Source: neg_difficulty_analysis registry, starcoder_2048]. This well-separated space allows us to contrast the behavior of mining strategies under fundamentally different geometric conditions.",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 77
    }
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_016a7qoFeVk29qYKU1KZLfV3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "49e10de0-fb3f-4c0f-807b-970db4341ddf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLSk3rvEjTNKwHaTaAiwiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3673,
      "cache_read_input_tokens": 55699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3673
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T02:13:36.130Z_

<details><summary>↩ Tool result · `toolu_016a7qoFeVk29qYKU1KZLfV3`</summary>

```text
1	# 1. Introduction
2	
3	Code retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \cite{liu2024repobench}, fault localization \cite{chen2025locagent}, and automated program repair \cite{jimenez2024swebench}.
4	Contrastive learning has become the dominant paradigm for training dense code retrievers \cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \cite{chen2020simclr,xiong2021ance}.
5	Despite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.
6	As retrieval scales to repository-level settings with hundreds of candidate files \cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.
7	
8	Existing negative selection approaches span a broad spectrum but leave a critical gap.
9	Random negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \cite{karpukhin2020dpr}.
10	Embedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.
11	CoCoHaNeRe \cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.
12	Meanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.
13	Notably, files that are close in embedding space may be structurally connected through shared data-flow paths \cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.
14	
15	We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.
16	Using CodeQL \cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.
17	We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.
18	All experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.
19	
20	Our experiments on CodeSearchNet \cite{husain2019codesearchnet} yield three principal findings.
21	First, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \cite{fan2025cocohanere}.
22	Second, as an \textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\ ${\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).
23	Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\% timeout rate and [TBD]\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.
24	
25	Our contributions are as follows:
26	\begin{enumerate}
27	\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.
28	\item \textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.
29	\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.
30	\end{enumerate}
31	
32	&lt;!-- Claim 2 wording fix: 2026-05-15 -->
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "eb73e81d-ae4f-403a-b4e4-792e1e5b5a1f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
      "content": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  }
}
```

</details>

---

### Assistant

_source line 69_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me summarize which files need changes and what changes:

## Files that need D041 dataflow-aware BM25 fixes:

### 1. `_project/paper/method_v1.md` — NEEDS CHANGES
The dataflow-aware section (lines 55-63) uses `sim(E_θ0(q), E_θ0(f))` and describes structurally unreachable negatives. Need to change to BM25 and structurally connected.

Key changes:
- Line 55: "structurally disconnected" → "structurally connected" (but actually the correct description says to select from connected files)


- Line 57: Replace the embedding similarity formula with BM25 scoring, and flip the constraint so we're selecting from structurally connected files instead of excluding them
- Line 59: Rewrite the intuition to match the BM25 approach
- Line 61: Change from "add a structural filter on top of embedding distance" to "add a structural filter and rank by BM25"
- Line 63: Update the fallback description

### 2. `paper_drafts/method_v1.md` — NEEDS CHANGES
Lines 69-85 also need similar updates to align the dataflow-aware BM25 approach with the same structural connectivity changes.

### 3. `_project/paper/experiment_setup_v1.md` — Still looking for where the ranking method is described, or if there's a section on negative mining that I'm missing. I'm checking the experiment setup files across both directories. The _project/paper/experiment_setup_v1.md doesn't actually describe the dataflow-aware ranking method itself—it only mentions the fallback to embedding-distance mining when structural data is missing. The paper_drafts version has the same content, so no changes are needed there. Now I need to look at the experiments_v1.md file, which appears to need modifications starting around line 21. I'm realizing I need to reconsider the direction of the filtering here. The dataflow-aware approach should first use CodeQL to identify structurally connected files, then rank those candidates by BM25 to select the top negatives—not filter them out. The negatives are drawn from the structurally connected set, not from what remains after disconnecting them. hard negatives because they're structurally connected to gold files but aren't gold themselves. The formula should select from files in the reachability set that aren't gold, ranked by BM25 score. Now I'm reconsidering the phrasing in the introduction — "filters structurally connected files from the embedding-distance candidate set" is ambiguous about whether it means removing or selecting those files.

The clearer version would be: "dataflow-aware mining that identifies structurally connected files via CodeQL and ranks them by BM25 to select hard negatives." This also fixes the mistake of referencing embedding distance when BM25 is what's actually used for ranking.

Looking back at the motivation statement about embedding space and structural connectivity, I should tighten that language too — it's explaining why filtering structurally connected pairs matters for training signal. I see line 17 mentions "embedding-distance" which needs to be corrected since the actual approach uses BM25, not embedding similarity. Line 13 talks about filtering motivation but doesn't describe the ranking method itself, so according to the task instructions I should leave it alone and focus only on fixing the ranking method descriptions. 我在思考如何修正文档中关于负样本选择策略的描述。关键是要统一两个地方的说法：一处提到用嵌入相似度排序，另一处用BM25排序——我需要把所有提到排序方法的地方都改成正确的方式，即先用CodeQL找到数据流连通的文件，再用BM25选出相似度最高的非gold文件作为负样本。但对于只描述过滤逻辑而没有提排序方法的段落，我应该保持原样不动。

仔细看第13行，它虽然提到了结构连通性，但重点是在说这种过滤能产生有信息量的训练信号，这个论述其实和新方法并不矛盾，所以我可以不改它。

我还是严格按照任务要求来，只修改那些明确使用"嵌入相似度"进行排序的地方。现在开始执行所有的编辑。

我来规划具体的修改：在第55行修改数据流感知挖掘段落，把原来基于嵌入相似度的描述改成基于结构连通性的选择标准。

这个公式定义了可达性集合，然后从不可达的非金标文件中选择最相似的作为负样本。关键的直觉是这些文件在表面文本特征上看起来相关，但缺少数据流连接。

通过训练编码器区分这些情况，我们希望推动嵌入空间捕捉结构语义，超越词汇重叠。

现在我在定义数据流感知的负样本挖掘策略——利用结构连接图从金标准文件的2跳可达范围内选择负样本，然后按BM25相似度排序。这样选出的负样本既与查询有词汇相似性，又与金标准文件有数据流连接，但不是实际修复的一部分，这使它们成为特别有信息量的训练信号，能帮助模型学习超越表面相似性的细粒度功能区分。

三种负样本策略形成了难度梯度：随机负样本最简单（低相似度、无结构约束），嵌入距离负样本更难（高预训练相似度、无结构约束），而数据流感知负样本则在嵌入距离基础上加入结构过滤，同时考虑文本和结构的相似性。

我通过负样本难度指标来量化这个排序，即每个查询与其分配负样本的平均余弦相似度。

对于结构图覆盖不足的仓库（结构连接候选不足K个），数据流感知策略会回退到嵌入距离挖掘，这种情况约占训练实例的34%，我会在分层评估中单独分析。

现在我在定义数据流感知负样本策略，它结合了嵌入距离和结构可达性过滤。我设置了可达性集合来捕获从金标准文件出发能到达的所有文件，然后从这个集合中选择距离最近的负样本。

这些文件在嵌入空间中相似但在数据流图中断开连接，这使它们成为有信息量的硬负样本——它们看起来在表面特征上相关（共享导入、API模式、变量名），但缺少真正的过程间数据流连接。通过训练编码器区分这些情况，我希望将嵌入空间推向捕捉结构语义而不仅仅是词汇重叠。对于缺乏结构连接数据的实例（约66%的训练数据），策略会回退到嵌入距离挖掘，确保所有实例的负样本数量一致，我会在分层评估中单独分析这个回退层。

现在我在定义数据流感知的负样本策略，它结合了BM25排名和结构可达性过滤。我定义了可达性集合来捕捉与金标准文件在数据流图中2跳范围内连接的所有文件，然后从这个可达集合中选择BM25排名最高的K个文件作为负样本。这些文件既在结构上与金标准文件相连（使其成为有意义的负样本），又在文本相似性上排名靠前。

对于缺乏结构连接数据的实例（约占训练数据的66%），我们退回到基于嵌入距离的负样本挖掘，以保持一致的负样本数量。这种分层的方法让我们能够在分层评估中单独分析这两个部分。

三种负样本策略形成了一个难度梯度：随机负样本最简单（低相似性，无结构约束），嵌入距离负样本最难（高预训练相似性，无结构约束），而数据流感知负样本则选择了既在文本上相似又在结构上与金标准文件断开的硬负样本子集。

我们通过负样本难度指标来量化这个排序——即查询与其分配的负样本在预训练空间中的平均余弦相似度。

For the dataflow-aware approach, I'm refining how we describe the selection process: rather than just filtering by embedding distance, we're using the CodeQL connectivity graph to identify structurally reachable files, then applying BM25 ranking to select the top candidates. I'm realizing the mechanistic hypothesis section needs reconsideration now that the dataflow-aware mining approach has shifted from filtering out connected files to selecting from them. The current reasoning about excluding useful hard negatives no longer applies with this new direction, so the explanation of why embedding-distance negatives outperform in saturated spaces needs to be rethought. I'm noticing that line 51 describes how negatives are computed from the frozen encoder and structural graph, but this doesn't fully account for the dataflow-aware strategy which uses BM25 instead. However, since the task only asks me to fix descriptions that explicitly mention the ranking method, and this line doesn't specifically call out the ranking approach, I should leave it as is. not from the encoder. The "frozen pretrained encoder" part only applies to embedding-distance mining, so that collective statement about all mining being static is now inaccurate for the dataflow-aware case. But since the task doesn't ask me to fix that general statement, I'll stick to what's explicitly requested and make the edits now.

Let me check if there are other mentions I should consider. Looking at the experiment setup files, there's a line about the dataflow-aware strategy falling back to embedding-distance mining, but that's about the fallback behavior, not the primary ranking method, so I'll leave it alone.

Now I'm ready to execute the edits across the files that need changes.  I have 6 files to modify with a total of 9 edits, and I'll need to add the documentation comment to each one when I'm done. The experiment setup files don't mention the dataflow ranking description, so those stay untouched.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "c559ee82-93ee-4b8a-abc3-102ec54c6486",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQBJdtyffQSDndZeMwCT53",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4270,
      "cache_read_input_tokens": 59372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4270
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 70_

已完成全部阅读。以下是需要修改的文件及问题：

1. **method_v1.md** (两个目录)：dataflow-aware 公式用 `sim(E_θ0(q), E_θ0(f))` 和 `f ∉ R_G(q)`，应改为 `BM25(q, f)` 和 `f ∈ R_G(q)`
2. **experiments_v1.md** (两个目录)：negative mining 描述说 "selecting by embedding distance"，应改为 BM25
3. **introduction_v2.md** (两个目录)：说 "embedding-distance candidate set"，应改为 BM25
4. **experiment_setup_v1.md**：无 dataflow-aware 排序描述，不需修改

开始编辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "7054f874-e132-44b5-97cf-b2917f703291",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQBJdtyffQSDndZeMwCT53",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4270,
      "cache_read_input_tokens": 59372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4270
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 71_

<details open><summary>🔧 Tool call — Edit · `toolu_014JheAduRRLkRUm61b8DJfy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md",
  "old_string": "**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThat is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.",
  "new_string": "**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives from among files that are structurally connected to the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThat is, we select the top-$K$ non-gold files that are **structurally reachable** from the gold files in the data-flow graph, ranked by BM25 lexical similarity. The intuition is that these files represent a category of particularly informative negatives: they share inter-procedural data-flow connections with the gold files (making them structurally plausible) and exhibit high lexical overlap with the query, yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "d02d9b67-ce6d-4ea2-8d94-0d097058093e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQBJdtyffQSDndZeMwCT53",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4270,
      "cache_read_input_tokens": 59372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4270
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T02:16:09.189Z_

<details><summary>↩ Tool result · `toolu_014JheAduRRLkRUm61b8DJfy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "823a6c0b-3d57-484d-a13f-0fccf32a4528",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md",
    "oldString": "**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThat is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.",
    "newString": "**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives from among files that are structurally connected to the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThat is, we select the top-$K$ non-gold files that are **structurally reachable** from the gold files in the data-flow graph, ranked by BM25 lexical similarity. The intuition is that these files represent a category of particularly informative negatives: they share inter-procedural data-flow connections with the gold files (making them structurally plausible) and exhibit high lexical overlap with the query, yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.",
    "originalFile": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files. Concretely, we optimize $\\theta$ such that for all $f^+ \\in \\mathcal{F}^+_q$ and $f^- \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. Random negatives are often too easy, providing weak gradient signal \\cite{chen2020simclr}. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 StructFuse Pipeline\n\nOur pipeline consists of three stages: (1) structural graph extraction via static analysis, (2) training data construction with strategy-specific negative mining, and (3) contrastive fine-tuning of a pretrained code encoder.\n\n**CodeQL Extraction.** We use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. Specifically, we define taint-tracking queries that trace data flow from designated sources to sinks, crossing function call boundaries. This yields a set of data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file.\n\nWe set a scope bound on the analysis depth to ensure tractability: queries that exceed a predefined step limit are terminated. In practice, this achieves 0\\% timeout rate across 123 out of 131 repositories in our dataset.\n\n**Structural Connectivity Graph.** From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. This graph captures inter-procedural structural relationships between files—two files are connected if data flows between them across function call boundaries.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\n**Structural Coverage.** At full scale, 78\\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.\n\n## §3.3 Training Objective\n\n**Contrastive Loss.** We train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$, the loss is:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query.\n\n**Encoder Architecture.** We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—which differ in pretraining objectives (Fill-in-the-Middle vs. multi-task including Fill-in-the-Middle) and exhibit distinct representation geometries (§5). Each encoder is augmented with a linear projection head that maps the last hidden state to a 256-dimensional embedding space.\n\n**Parameter-Efficient Fine-Tuning.** We apply LoRA \\cite{hu2022lora} to the query and value projection matrices ($W_q$, $W_v$) of each attention layer with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated. We use AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10\\% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2048 tokens. Training runs for 3 epochs with evaluation every 500 steps.\n\n**Dual Checkpoint Selection.** We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement.\n\n## §3.4 Negative Mining Strategies\n\nWe compare three negative mining strategies that span a spectrum from uninformed to structure-grounded selection.\n\n**Random Mining.** For each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$. This serves as the baseline: negatives are unbiased but typically easy, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n**Embedding-Distance Mining.** We compute embeddings for all files and queries using the frozen pretrained encoder $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we retrieve the $K$ non-gold files with highest cosine similarity to $q$ in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThis selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \\cite{xiong2021ance}.\n\n**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThat is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.\n\n**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).\n\nFor repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).\n",
    "structuredPatch": [
      {
        "oldStart": 52,
        "oldLines": 11,
        "newStart": 52,
        "newLines": 11,
        "lines": [
          " ",
          " This selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \\cite{xiong2021ance}.",
          " ",
          "-**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:",
          "+**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives from among files that are structurally connected to the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:",
          " ",
          "-$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$",
          "+$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$",
          " ",
          "-That is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.",
          "+That is, we select the top-$K$ non-gold files that are **structurally reachable** from the gold files in the data-flow graph, ranked by BM25 lexical similarity. The intuition is that these files represent a category of particularly informative negatives: they share inter-procedural data-flow connections with the gold files (making them structurally plausible) and exhibit high lexical overlap with the query, yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.",
          " ",
          " **Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).",
          " "
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

_source line 73_

<details open><summary>🔧 Tool call — Edit · `toolu_019QVfJtToDD6PywHMyQ8hN4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md",
  "old_string": "**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).",
  "new_string": "**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "59a5a1b4-d7e3-4c37-8180-8132ae2fe6f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQBJdtyffQSDndZeMwCT53",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4270,
      "cache_read_input_tokens": 59372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4270
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T02:16:12.026Z_

<details><summary>↩ Tool result · `toolu_019QVfJtToDD6PywHMyQ8hN4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "afdf6a8d-a7fb-41ca-b7af-38e36e9c5b59",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md",
    "oldString": "**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).",
    "newString": "**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).",
    "originalFile": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files. Concretely, we optimize $\\theta$ such that for all $f^+ \\in \\mathcal{F}^+_q$ and $f^- \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. Random negatives are often too easy, providing weak gradient signal \\cite{chen2020simclr}. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 StructFuse Pipeline\n\nOur pipeline consists of three stages: (1) structural graph extraction via static analysis, (2) training data construction with strategy-specific negative mining, and (3) contrastive fine-tuning of a pretrained code encoder.\n\n**CodeQL Extraction.** We use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. Specifically, we define taint-tracking queries that trace data flow from designated sources to sinks, crossing function call boundaries. This yields a set of data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file.\n\nWe set a scope bound on the analysis depth to ensure tractability: queries that exceed a predefined step limit are terminated. In practice, this achieves 0\\% timeout rate across 123 out of 131 repositories in our dataset.\n\n**Structural Connectivity Graph.** From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. This graph captures inter-procedural structural relationships between files—two files are connected if data flows between them across function call boundaries.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\n**Structural Coverage.** At full scale, 78\\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.\n\n## §3.3 Training Objective\n\n**Contrastive Loss.** We train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$, the loss is:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query.\n\n**Encoder Architecture.** We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—which differ in pretraining objectives (Fill-in-the-Middle vs. multi-task including Fill-in-the-Middle) and exhibit distinct representation geometries (§5). Each encoder is augmented with a linear projection head that maps the last hidden state to a 256-dimensional embedding space.\n\n**Parameter-Efficient Fine-Tuning.** We apply LoRA \\cite{hu2022lora} to the query and value projection matrices ($W_q$, $W_v$) of each attention layer with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated. We use AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10\\% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2048 tokens. Training runs for 3 epochs with evaluation every 500 steps.\n\n**Dual Checkpoint Selection.** We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement.\n\n## §3.4 Negative Mining Strategies\n\nWe compare three negative mining strategies that span a spectrum from uninformed to structure-grounded selection.\n\n**Random Mining.** For each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$. This serves as the baseline: negatives are unbiased but typically easy, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n**Embedding-Distance Mining.** We compute embeddings for all files and queries using the frozen pretrained encoder $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we retrieve the $K$ non-gold files with highest cosine similarity to $q$ in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThis selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \\cite{xiong2021ance}.\n\n**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives from among files that are structurally connected to the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThat is, we select the top-$K$ non-gold files that are **structurally reachable** from the gold files in the data-flow graph, ranked by BM25 lexical similarity. The intuition is that these files represent a category of particularly informative negatives: they share inter-procedural data-flow connections with the gold files (making them structurally plausible) and exhibit high lexical overlap with the query, yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.\n\n**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).\n\nFor repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).\n",
    "structuredPatch": [
      {
        "oldStart": 58,
        "oldLines": 6,
        "newStart": 58,
        "newLines": 6,
        "lines": [
          " ",
          " That is, we select the top-$K$ non-gold files that are **structurally reachable** from the gold files in the data-flow graph, ranked by BM25 lexical similarity. The intuition is that these files represent a category of particularly informative negatives: they share inter-procedural data-flow connections with the gold files (making them structurally plausible) and exhibit high lexical overlap with the query, yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.",
          " ",
          "-**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).",
          "+**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).",
          " ",
          " For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5)."
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

_source line 75_

<details open><summary>🔧 Tool call — Edit · `toolu_01DQnNNpVAGXy6QRGSL2KRdd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md",
  "old_string": "For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).",
  "new_string": "For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally connected candidates), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "d73ab91b-1f24-4d80-8d21-3a4b3131bae4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQBJdtyffQSDndZeMwCT53",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4270,
      "cache_read_input_tokens": 59372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4270
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-15T02:16:14.484Z_

<details><summary>↩ Tool result · `toolu_01DQnNNpVAGXy6QRGSL2KRdd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "e1a5229e-4aef-4a4a-9a19-5de167f3b69e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md",
    "oldString": "For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).",
    "newString": "For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally connected candidates), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "originalFile": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files. Concretely, we optimize $\\theta$ such that for all $f^+ \\in \\mathcal{F}^+_q$ and $f^- \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. Random negatives are often too easy, providing weak gradient signal \\cite{chen2020simclr}. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 StructFuse Pipeline\n\nOur pipeline consists of three stages: (1) structural graph extraction via static analysis, (2) training data construction with strategy-specific negative mining, and (3) contrastive fine-tuning of a pretrained code encoder.\n\n**CodeQL Extraction.** We use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. Specifically, we define taint-tracking queries that trace data flow from designated sources to sinks, crossing function call boundaries. This yields a set of data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file.\n\nWe set a scope bound on the analysis depth to ensure tractability: queries that exceed a predefined step limit are terminated. In practice, this achieves 0\\% timeout rate across 123 out of 131 repositories in our dataset.\n\n**Structural Connectivity Graph.** From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. This graph captures inter-procedural structural relationships between files—two files are connected if data flows between them across function call boundaries.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\n**Structural Coverage.** At full scale, 78\\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.\n\n## §3.3 Training Objective\n\n**Contrastive Loss.** We train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$, the loss is:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query.\n\n**Encoder Architecture.** We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—which differ in pretraining objectives (Fill-in-the-Middle vs. multi-task including Fill-in-the-Middle) and exhibit distinct representation geometries (§5). Each encoder is augmented with a linear projection head that maps the last hidden state to a 256-dimensional embedding space.\n\n**Parameter-Efficient Fine-Tuning.** We apply LoRA \\cite{hu2022lora} to the query and value projection matrices ($W_q$, $W_v$) of each attention layer with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated. We use AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10\\% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2048 tokens. Training runs for 3 epochs with evaluation every 500 steps.\n\n**Dual Checkpoint Selection.** We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement.\n\n## §3.4 Negative Mining Strategies\n\nWe compare three negative mining strategies that span a spectrum from uninformed to structure-grounded selection.\n\n**Random Mining.** For each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$. This serves as the baseline: negatives are unbiased but typically easy, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n**Embedding-Distance Mining.** We compute embeddings for all files and queries using the frozen pretrained encoder $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we retrieve the $K$ non-gold files with highest cosine similarity to $q$ in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThis selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \\cite{xiong2021ance}.\n\n**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives from among files that are structurally connected to the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThat is, we select the top-$K$ non-gold files that are **structurally reachable** from the gold files in the data-flow graph, ranked by BM25 lexical similarity. The intuition is that these files represent a category of particularly informative negatives: they share inter-procedural data-flow connections with the gold files (making them structurally plausible) and exhibit high lexical overlap with the query, yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.\n\n**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).\n\nFor repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).\n",
    "structuredPatch": [
      {
        "oldStart": 60,
        "oldLines": 4,
        "newStart": 60,
        "newLines": 5,
        "lines": [
          " ",
          " **Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).",
          " ",
          "-For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).",
          "+For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally connected candidates), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).",
          "+&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
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

_source line 77_

<details open><summary>🔧 Tool call — Edit · `toolu_014a3DVCDc6zaVWovKJfGTeu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "old_string": "This strategy combines embedding distance with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese files are simultaneously similar in the embedding space (hard) and structurally disconnected in the data-flow graph (informative). They represent a category of false positives of textual similarity: files that appear relevant based on surface features (shared imports, API patterns, variable names) but lack the inter-procedural data-flow connections that characterize functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.",
  "new_string": "This strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "3cdf151a-772f-45ab-bc28-c28ea550abb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156HyE4vhooHoaQHFULUksf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9473,
      "cache_read_input_tokens": 63642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9473
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

_source line 78 · 2026-05-15T02:16:29.979Z_

<details><summary>↩ Tool result · `toolu_014a3DVCDc6zaVWovKJfGTeu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "d0a8fdfe-70b1-4789-87db-04bd02eb6f53",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
    "oldString": "This strategy combines embedding distance with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese files are simultaneously similar in the embedding space (hard) and structurally disconnected in the data-flow graph (informative). They represent a category of false positives of textual similarity: files that appear relevant based on surface features (shared imports, API patterns, variable names) but lack the inter-procedural data-flow connections that characterize functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.",
    "newString": "This strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.",
    "originalFile": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 Structural Information Extraction\n\n### CodeQL Bounded Data-Flow Analysis\n\nWe use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\n\n- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.\n- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\n\n### File-Level Reachability\n\nFrom the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\nAt full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\n\n### Beniget Fallback\n\nFor repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].\n\n### Coverage Statistics\n\nThe extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:\n\n| Metric | Value |\n|--------|-------|\n| Timeout rate | 0% (all repository tiers) |\n| Repository coverage | 123/131 (93.9%) |\n| Structural data rate | 34% of instances |\n| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |\n\nThe 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.\n\n## §3.3 Structure-Aware Negative Mining\n\nWe compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\n\n### Random Negatives\n\nFor each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$f^-_{\\text{rand}} \\sim \\text{Uniform}(\\mathcal{F} \\setminus \\mathcal{F}^+_q), \\quad |\\{f^-_{\\text{rand}}\\}| = K$$\n\nThis baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n### Embedding-Distance Negatives\n\nWe compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.\n\n### Dataflow-Aware Negatives\n\nThis strategy combines embedding distance with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese files are simultaneously similar in the embedding space (hard) and structurally disconnected in the data-flow graph (informative). They represent a category of false positives of textual similarity: files that appear relevant based on surface features (shared imports, API patterns, variable names) but lack the inter-procedural data-flow connections that characterize functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.\n\nFor instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n\n### Difficulty Gradient\n\nThe three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n\n### Relationship to BM25 Baselines\n\nIn addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n\n## §3.4 Contrastive Fine-tuning\n\n### InfoNCE Loss\n\nWe train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].\n\n### LoRA Fine-tuning Setup\n\nWe fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—using LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.\n\nEach encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].\n\nTraining uses AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\n### Dual Checkpoint Strategy\n\nWe observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].\n\n### Early Stopping\n\nThe initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n",
    "structuredPatch": [
      {
        "oldStart": 68,
        "oldLines": 15,
        "newStart": 68,
        "newLines": 15,
        "lines": [
          " ",
          " ### Dataflow-Aware Negatives",
          " ",
          "-This strategy combines embedding distance with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:",
          "+This strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:",
          " ",
          " $$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$",
          " ",
          "-where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:",
          "+where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:",
          " ",
          "-$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$",
          "+$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$",
          " ",
          "-These files are simultaneously similar in the embedding space (hard) and structurally disconnected in the data-flow graph (informative). They represent a category of false positives of textual similarity: files that appear relevant based on surface features (shared imports, API patterns, variable names) but lack the inter-procedural data-flow connections that characterize functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.",
          "+These files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.",
          " ",
          " For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).",
          " "
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

_source line 79_

<details open><summary>🔧 Tool call — Edit · `toolu_01JX8GQvAEvJVakgXZMG5hgE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "old_string": "The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).",
  "new_string": "The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "e6418165-44d1-4a41-a51a-dccc7c100341",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156HyE4vhooHoaQHFULUksf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9473,
      "cache_read_input_tokens": 63642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9473
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

_source line 80 · 2026-05-15T02:16:32.809Z_

<details><summary>↩ Tool result · `toolu_01JX8GQvAEvJVakgXZMG5hgE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "2fba254c-a662-417e-bafd-390f265cd5c7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
    "oldString": "The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).",
    "newString": "The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).",
    "originalFile": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 Structural Information Extraction\n\n### CodeQL Bounded Data-Flow Analysis\n\nWe use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\n\n- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.\n- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\n\n### File-Level Reachability\n\nFrom the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\nAt full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\n\n### Beniget Fallback\n\nFor repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].\n\n### Coverage Statistics\n\nThe extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:\n\n| Metric | Value |\n|--------|-------|\n| Timeout rate | 0% (all repository tiers) |\n| Repository coverage | 123/131 (93.9%) |\n| Structural data rate | 34% of instances |\n| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |\n\nThe 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.\n\n## §3.3 Structure-Aware Negative Mining\n\nWe compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\n\n### Random Negatives\n\nFor each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$f^-_{\\text{rand}} \\sim \\text{Uniform}(\\mathcal{F} \\setminus \\mathcal{F}^+_q), \\quad |\\{f^-_{\\text{rand}}\\}| = K$$\n\nThis baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n### Embedding-Distance Negatives\n\nWe compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.\n\n### Dataflow-Aware Negatives\n\nThis strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.\n\nFor instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n\n### Difficulty Gradient\n\nThe three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n\n### Relationship to BM25 Baselines\n\nIn addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n\n## §3.4 Contrastive Fine-tuning\n\n### InfoNCE Loss\n\nWe train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].\n\n### LoRA Fine-tuning Setup\n\nWe fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—using LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.\n\nEach encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].\n\nTraining uses AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\n### Dual Checkpoint Strategy\n\nWe observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].\n\n### Early Stopping\n\nThe initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n",
    "structuredPatch": [
      {
        "oldStart": 82,
        "oldLines": 7,
        "newStart": 82,
        "newLines": 7,
        "lines": [
          " ",
          " ### Difficulty Gradient",
          " ",
          "-The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).",
          "+The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).",
          " ",
          " ### Relationship to BM25 Baselines",
          " "
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

_source line 81_

<details open><summary>🔧 Tool call — Edit · `toolu_013Etd6RkKH5Rtpm31v2VDnw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1.md",
  "old_string": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4).",
  "new_string": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "1c482133-df44-47a3-a5a6-5bb4b2a9efc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156HyE4vhooHoaQHFULUksf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9473,
      "cache_read_input_tokens": 63642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9473
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

_source line 82 · 2026-05-15T02:16:35.953Z_

<details><summary>↩ Tool result · `toolu_013Etd6RkKH5Rtpm31v2VDnw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "5fe2ebbb-3590-42b1-b1a4-a5cf3a0b84e8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1.md",
    "oldString": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4).",
    "newString": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4).",
    "originalFile": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-bench \\cite{jimenez2024swebench}, a benchmark of real-world GitHub issues paired with developer-authored patches. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, we run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,897 instances across 123 repositories with structural data, yielding a structural coverage rate of 36%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{cocohanere2025}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with temperature $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the full experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours.\n\n## §4.3 Results\n\n### Main Results\n\nTable 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\\pm$ standard deviation over three seeds.\n\n**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |\n| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\n| Random | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Embedding-distance | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n\n**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\\placeholder{+X.X}pp and \\placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \\placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.\n\n### Pilot Validation\n\nPrior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.\n\n**Table 2: Pilot results (single seed, 24-repo subset).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.536 | 0.492 |\n| Embedding-distance | 0.556 (+2.0pp) | 0.508 (+1.6pp) |\n| Dataflow-aware | 0.544 (+0.8pp) | 0.487 (−0.5pp) |\n\nThe pilot established two findings subsequently confirmed at full scale: (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n\n### Ablations\n\n**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\\in \\{50, 100, 200, 500\\}$.\n\n**Table 3: R@1 by pool size.**\n\n| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\\Delta$ | SC Emb. | SC Rand. | SC $\\Delta$ |\n|---|---|---|---|---|---|---|\n| 50 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 100 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 200 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 500 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n\n**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.\n\n| Strategy | Qwen R@1 (s42) |\n|---|---|\n| Static embedding-distance | \\placeholder{X.XX} |\n| Dynamic (epoch re-mining) | \\placeholder{X.XX} |\n\n### Downstream Evaluation\n\n**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).\n\n| Retriever | Resolve Rate |\n|---|---|\n| BM25 | \\placeholder{X.X%} |\n| Random-trained | \\placeholder{X.X%} |\n| Embedding-trained (Qwen) | \\placeholder{X.X%} |\n\n## §4.4 Analysis\n\n### Representation Geometry and Negative Difficulty\n\nA central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\n\n**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\\_sim − neg\\_sim.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | pos\\_sim | neg\\_sim | margin | pos\\_sim | neg\\_sim | margin |\n| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |\n| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |\n| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\n\nSeveral patterns emerge from Table 4:\n\n**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\\times$ larger margins across all strategies, indicating a more separable pretrained space.\n\n**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.\n\n**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n\n### Stratified Analysis\n\nWe stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\n\n**Table 5: R@1 stratified by structural data availability.**\n\n| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\\Delta$ | SC (Emb.) | SC (DF) | $\\Delta$ |\n|---|---|---|---|---|---|---|---|\n| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| No structural data (fallback) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n\nConfound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\n\n### CodeQL Scalability\n\nWe report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).\n\n**Table 6: CodeQL extraction scalability by repository tier.**\n\n| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |\n|---|---|---|---|---|---|\n| Small (<50 files) | 1 | 500 | 0% | 81.0% | 0.0% |\n| Medium (50–200) | 17 | 4,096 | 0% | 47.2% | 50.0% |\n| Large (200–500) | 40 | 13,628 | 0% | 34.3% | 85.7% |\n| XLarge (500+) | 29 | 25,949 | 0% | 31.4% | 96.0% |\n| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 7,
        "newStart": 18,
        "newLines": 7,
        "lines": [
          " ",
          " For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).",
          " ",
          "-**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.",
          "+**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.",
          " ",
          " **Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the full experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours.",
          " "
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

<details open><summary>🔧 Tool call — Edit · `toolu_01B8xnXWGi9MN6skdW8ahpNe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4).",
  "new_string": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "599f8df7-644e-401a-b92d-f0cb1cccc0c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156HyE4vhooHoaQHFULUksf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9473,
      "cache_read_input_tokens": 63642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9473
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

_source line 84 · 2026-05-15T02:16:37.361Z_

<details><summary>↩ Tool result · `toolu_01B8xnXWGi9MN6skdW8ahpNe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "7fef9e83-7732-4853-b197-1801cdba47d3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4).",
    "newString": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4).",
    "originalFile": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \\placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \\placeholder{34.3%} [pending recalc]. The remaining \\placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.\n\n## §4.3 Results\n\n### Main Results\n\nTable 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\\pm$ standard deviation over three seeds.\n\n**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |\n| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\n| Random | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Embedding-distance | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n\n**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\\placeholder{+X.X}pp and \\placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \\placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.\n\n### Pilot Validation\n\nPrior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.\n\n**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.5357 | 0.4922 |\n| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |\n| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |\n\nThe pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n\n### Ablations\n\n**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\\in \\{50, 100, 200, 500\\}$.\n\n**Table 3: R@1 by pool size.**\n\n| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\\Delta$ | SC Emb. | SC Rand. | SC $\\Delta$ |\n|---|---|---|---|---|---|---|\n| 50 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 100 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 200 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 500 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n\n**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.\n\n| Strategy | Qwen R@1 (s42) |\n|---|---|\n| Static embedding-distance | \\placeholder{X.XX} |\n| Dynamic (epoch re-mining) | \\placeholder{X.XX} |\n\n### Downstream Evaluation\n\n**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).\n\n| Retriever | Resolve Rate |\n|---|---|\n| BM25 | \\placeholder{X.X%} |\n| Random-trained | \\placeholder{X.X%} |\n| Embedding-trained (Qwen) | \\placeholder{X.X%} |\n\n## §4.4 Analysis\n\n### Representation Geometry and Negative Difficulty\n\nA central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\n\n**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\\_sim − neg\\_sim.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | pos\\_sim | neg\\_sim | margin | pos\\_sim | neg\\_sim | margin |\n| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |\n| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |\n| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\n\nSeveral patterns emerge from Table 4:\n\n**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\\times$ larger margins across all strategies, indicating a more separable pretrained space.\n\n**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.\n\n**Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n\n### Stratified Analysis\n\nWe stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\n\n**Table 5: R@1 stratified by structural data availability.**\n\n| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\\Delta$ | SC (Emb.) | SC (DF) | $\\Delta$ |\n|---|---|---|---|---|---|---|---|\n| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| No structural data (fallback) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n\nConfound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\n\n### CodeQL Scalability\n\nWe report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).\n\n&lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->\n**Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.\n\n| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |\n|---|---|---|---|---|---|\n| Small (<50 inst.) | 18 | 500 | 0% | \\placeholder{81.0%} [pending recalc] | 0.0% |\n| Medium (50–200) | 36 | 4,096 | 0% | \\placeholder{47.2%} [pending recalc] | 50.0% |\n| Large (200–500) | 40 | 13,628 | 0% | \\placeholder{34.3%} [pending recalc] | 85.7% |\n| XLarge (500+) | 29 | 25,949 | 0% | \\placeholder{31.4%} [pending recalc] | 96.0% |\n| **Total** | **123** | **44,173** | **0%** | **\\placeholder{34.3%} [pending recalc]** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 7,
        "newStart": 18,
        "newLines": 7,
        "lines": [
          " ",
          " For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).",
          " ",
          "-**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.",
          "+**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.",
          " ",
          " **Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.",
          " "
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

<details open><summary>🔧 Tool call — Edit · `toolu_01UHW9bhDxF6YWWcewgbYfo2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction_v2.md",
  "old_string": "(3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.",
  "new_string": "(3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "8f1064d3-ff5d-4838-8cf3-a6df549e24ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156HyE4vhooHoaQHFULUksf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9473,
      "cache_read_input_tokens": 63642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9473
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

_source line 86 · 2026-05-15T02:16:39.706Z_

<details><summary>↩ Tool result · `toolu_01UHW9bhDxF6YWWcewgbYfo2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "de2eecc4-4c75-47a3-a0c1-652b07a1186c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction_v2.md",
    "oldString": "(3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.",
    "newString": "(3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.",
    "originalFile": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis reveals that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) mediates strategy effectiveness, providing a mechanistic hypothesis for when different strategies should be preferred (pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 14,
        "oldLines": 7,
        "newStart": 14,
        "newLines": 7,
        "lines": [
          " ",
          " We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.",
          " Using CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.",
          "-We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.",
          "+We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.",
          " All experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.",
          " ",
          " Our experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings."
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

<details open><summary>🔧 Tool call — Edit · `toolu_015BykiPViZgNh9xedbSrXgy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
  "old_string": "(3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.",
  "new_string": "(3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "7873024d-8a13-401d-b126-3d2f42959ec9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156HyE4vhooHoaQHFULUksf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9473,
      "cache_read_input_tokens": 63642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9473
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

_source line 88 · 2026-05-15T02:16:40.707Z_

<details><summary>↩ Tool result · `toolu_015BykiPViZgNh9xedbSrXgy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "8961031c-b403-452d-954e-2332ddbb2d54",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
    "oldString": "(3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.",
    "newString": "(3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.",
    "originalFile": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n",
    "structuredPatch": [
      {
        "oldStart": 14,
        "oldLines": 7,
        "newStart": 14,
        "newLines": 7,
        "lines": [
          " ",
          " We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.",
          " Using CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.",
          "-We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.",
          "+We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.",
          " All experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.",
          " ",
          " Our experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings."
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

<details><summary>Logged reasoning block</summary>

```text
Good, all edits are done. Now I need to add the D041 comment to the end of files that were modified but don't have it yet. I already added it to `_project/paper/method_v1.md`. Let me add it to the other modified files:

1. `paper_drafts/method_v1.md` — needs comment
2. `_project/paper/experiments_v1.md` — needs comment
3. `paper_drafts/experiments_v1.md` — needs comment
4. `_project/paper/introduction_v2.md` — needs comment


5. `paper_drafts/introduction_v2.md` — already has a comment from the previous fix, so I just need to add the D041 comment alongside it

I need to check the last line of each file to append the comment properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "d925d8d9-9156-4da0-8fd3-c36d10ac1681",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yY3JanwCRzDYTCDLTZtkF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2492,
      "cache_read_input_tokens": 73115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2492
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

Now I need to add `&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->` to the end of the remaining modified files. Let me check their endings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "0281f619-eb28-4614-9726-77040721023f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yY3JanwCRzDYTCDLTZtkF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2492,
      "cache_read_input_tokens": 73115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2492
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_015n9i6UkRnmxW8LbmNU8VmH`</summary>

```json
{
  "command": "tail -3 artifacts/paper_drafts/method_v1.md && echo \"---\" && tail -3 artifacts/_project/paper/experiments_v1.md && echo \"---\" && tail -3 artifacts/paper_drafts/experiments_v1.md && echo \"---\" && tail -3 artifacts/_project/paper/introduction_v2.md && echo \"---\" && tail -3 artifacts/paper_drafts/introduction_v2.md",
  "description": "Check last lines of modified files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "4ce3ff22-690b-48ca-a904-e1c16d942fd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yY3JanwCRzDYTCDLTZtkF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2492,
      "cache_read_input_tokens": 73115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2492
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-15T02:16:49.321Z_

<details><summary>↩ Tool result · `toolu_015n9i6UkRnmxW8LbmNU8VmH`</summary>

```text
### Early Stopping

The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].
---
| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |

The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.
---
The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.

&lt;!-- Claim 2 wording fix: 2026-05-15 -->
---
\item \textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.
\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.
\end{enumerate}
---
\end{enumerate}

&lt;!-- Claim 2 wording fix: 2026-05-15 -->
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "ed13c261-11b6-4d8a-9ab4-f6287f7c6046",
  "tool_use_result": {
    "stdout": "### Early Stopping\n\nThe initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n---\n| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n---\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n---\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n---\n\\end{enumerate}\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
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

_source line 93_

<details open><summary>🔧 Tool call — Edit · `toolu_01LcSwUFJHqujYv5zoN2gCYL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "old_string": "The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].",
  "new_string": "The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "fe0b0b38-a682-4cdc-8251-71aae3e2a13d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfBHsWeNEjXJszSRTCZuJZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 75607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-15T02:16:56.298Z_

<details><summary>↩ Tool result · `toolu_01LcSwUFJHqujYv5zoN2gCYL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "87d75803-b7e0-4cf9-819b-790827b4538d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
    "oldString": "The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].",
    "newString": "The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "originalFile": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 Structural Information Extraction\n\n### CodeQL Bounded Data-Flow Analysis\n\nWe use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\n\n- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.\n- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\n\n### File-Level Reachability\n\nFrom the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\nAt full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\n\n### Beniget Fallback\n\nFor repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].\n\n### Coverage Statistics\n\nThe extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:\n\n| Metric | Value |\n|--------|-------|\n| Timeout rate | 0% (all repository tiers) |\n| Repository coverage | 123/131 (93.9%) |\n| Structural data rate | 34% of instances |\n| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |\n\nThe 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.\n\n## §3.3 Structure-Aware Negative Mining\n\nWe compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\n\n### Random Negatives\n\nFor each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$f^-_{\\text{rand}} \\sim \\text{Uniform}(\\mathcal{F} \\setminus \\mathcal{F}^+_q), \\quad |\\{f^-_{\\text{rand}}\\}| = K$$\n\nThis baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n### Embedding-Distance Negatives\n\nWe compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.\n\n### Dataflow-Aware Negatives\n\nThis strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.\n\nFor instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n\n### Difficulty Gradient\n\nThe three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n\n### Relationship to BM25 Baselines\n\nIn addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n\n## §3.4 Contrastive Fine-tuning\n\n### InfoNCE Loss\n\nWe train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].\n\n### LoRA Fine-tuning Setup\n\nWe fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—using LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.\n\nEach encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].\n\nTraining uses AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\n### Dual Checkpoint Strategy\n\nWe observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].\n\n### Early Stopping\n\nThe initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n",
    "structuredPatch": [
      {
        "oldStart": 113,
        "oldLines": 3,
        "newStart": 113,
        "newLines": 4,
        "lines": [
          " ### Early Stopping",
          " ",
          " The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].",
          "+&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
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

_source line 95_

<details open><summary>🔧 Tool call — Edit · `toolu_015ibvz5Zsof4DypKpN1oj8s`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1.md",
  "old_string": "The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.",
  "new_string": "The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "e79dcf84-189a-4089-a268-41fb7c4923f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfBHsWeNEjXJszSRTCZuJZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 75607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-15T02:16:59.653Z_

<details><summary>↩ Tool result · `toolu_015ibvz5Zsof4DypKpN1oj8s`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "3673999a-f7fd-4bbf-bc35-6c39a79291e4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1.md",
    "oldString": "The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.",
    "newString": "The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "originalFile": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-bench \\cite{jimenez2024swebench}, a benchmark of real-world GitHub issues paired with developer-authored patches. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, we run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,897 instances across 123 repositories with structural data, yielding a structural coverage rate of 36%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{cocohanere2025}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with temperature $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the full experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours.\n\n## §4.3 Results\n\n### Main Results\n\nTable 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\\pm$ standard deviation over three seeds.\n\n**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |\n| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\n| Random | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Embedding-distance | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n\n**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\\placeholder{+X.X}pp and \\placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \\placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.\n\n### Pilot Validation\n\nPrior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.\n\n**Table 2: Pilot results (single seed, 24-repo subset).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.536 | 0.492 |\n| Embedding-distance | 0.556 (+2.0pp) | 0.508 (+1.6pp) |\n| Dataflow-aware | 0.544 (+0.8pp) | 0.487 (−0.5pp) |\n\nThe pilot established two findings subsequently confirmed at full scale: (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n\n### Ablations\n\n**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\\in \\{50, 100, 200, 500\\}$.\n\n**Table 3: R@1 by pool size.**\n\n| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\\Delta$ | SC Emb. | SC Rand. | SC $\\Delta$ |\n|---|---|---|---|---|---|---|\n| 50 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 100 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 200 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 500 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n\n**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.\n\n| Strategy | Qwen R@1 (s42) |\n|---|---|\n| Static embedding-distance | \\placeholder{X.XX} |\n| Dynamic (epoch re-mining) | \\placeholder{X.XX} |\n\n### Downstream Evaluation\n\n**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).\n\n| Retriever | Resolve Rate |\n|---|---|\n| BM25 | \\placeholder{X.X%} |\n| Random-trained | \\placeholder{X.X%} |\n| Embedding-trained (Qwen) | \\placeholder{X.X%} |\n\n## §4.4 Analysis\n\n### Representation Geometry and Negative Difficulty\n\nA central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\n\n**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\\_sim − neg\\_sim.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | pos\\_sim | neg\\_sim | margin | pos\\_sim | neg\\_sim | margin |\n| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |\n| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |\n| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\n\nSeveral patterns emerge from Table 4:\n\n**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\\times$ larger margins across all strategies, indicating a more separable pretrained space.\n\n**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.\n\n**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n\n### Stratified Analysis\n\nWe stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\n\n**Table 5: R@1 stratified by structural data availability.**\n\n| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\\Delta$ | SC (Emb.) | SC (DF) | $\\Delta$ |\n|---|---|---|---|---|---|---|---|\n| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| No structural data (fallback) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n\nConfound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\n\n### CodeQL Scalability\n\nWe report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).\n\n**Table 6: CodeQL extraction scalability by repository tier.**\n\n| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |\n|---|---|---|---|---|---|\n| Small (<50 files) | 1 | 500 | 0% | 81.0% | 0.0% |\n| Medium (50–200) | 17 | 4,096 | 0% | 47.2% | 50.0% |\n| Large (200–500) | 40 | 13,628 | 0% | 34.3% | 85.7% |\n| XLarge (500+) | 29 | 25,949 | 0% | 31.4% | 96.0% |\n| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n",
    "structuredPatch": [
      {
        "oldStart": 137,
        "oldLines": 3,
        "newStart": 137,
        "newLines": 4,
        "lines": [
          " | **Total** | **123** | **44,173** | **0%** | **36.0%** | — |",
          " ",
          " The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.",
          "+&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
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

_source line 97_

<details open><summary>🔧 Tool call — Edit · `toolu_01A5pcUZwVvmDtyQGexJYdSo`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
  "new_string": "&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "11af9321-f3fa-4a3c-a3e1-21ded10093b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfBHsWeNEjXJszSRTCZuJZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 75607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-15T02:17:01.008Z_

<details><summary>↩ Tool result · `toolu_01A5pcUZwVvmDtyQGexJYdSo`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "72c61641-a438-4274-9609-f45807fa391d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
    "newString": "&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "originalFile": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \\placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \\placeholder{34.3%} [pending recalc]. The remaining \\placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.\n\n## §4.3 Results\n\n### Main Results\n\nTable 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\\pm$ standard deviation over three seeds.\n\n**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |\n| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\n| Random | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Embedding-distance | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n\n**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\\placeholder{+X.X}pp and \\placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \\placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.\n\n### Pilot Validation\n\nPrior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.\n\n**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.5357 | 0.4922 |\n| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |\n| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |\n\nThe pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n\n### Ablations\n\n**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\\in \\{50, 100, 200, 500\\}$.\n\n**Table 3: R@1 by pool size.**\n\n| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\\Delta$ | SC Emb. | SC Rand. | SC $\\Delta$ |\n|---|---|---|---|---|---|---|\n| 50 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 100 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 200 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 500 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n\n**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.\n\n| Strategy | Qwen R@1 (s42) |\n|---|---|\n| Static embedding-distance | \\placeholder{X.XX} |\n| Dynamic (epoch re-mining) | \\placeholder{X.XX} |\n\n### Downstream Evaluation\n\n**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).\n\n| Retriever | Resolve Rate |\n|---|---|\n| BM25 | \\placeholder{X.X%} |\n| Random-trained | \\placeholder{X.X%} |\n| Embedding-trained (Qwen) | \\placeholder{X.X%} |\n\n## §4.4 Analysis\n\n### Representation Geometry and Negative Difficulty\n\nA central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\n\n**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\\_sim − neg\\_sim.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | pos\\_sim | neg\\_sim | margin | pos\\_sim | neg\\_sim | margin |\n| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |\n| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |\n| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\n\nSeveral patterns emerge from Table 4:\n\n**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\\times$ larger margins across all strategies, indicating a more separable pretrained space.\n\n**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.\n\n**Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n\n### Stratified Analysis\n\nWe stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\n\n**Table 5: R@1 stratified by structural data availability.**\n\n| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\\Delta$ | SC (Emb.) | SC (DF) | $\\Delta$ |\n|---|---|---|---|---|---|---|---|\n| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| No structural data (fallback) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n\nConfound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\n\n### CodeQL Scalability\n\nWe report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).\n\n&lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->\n**Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.\n\n| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |\n|---|---|---|---|---|---|\n| Small (<50 inst.) | 18 | 500 | 0% | \\placeholder{81.0%} [pending recalc] | 0.0% |\n| Medium (50–200) | 36 | 4,096 | 0% | \\placeholder{47.2%} [pending recalc] | 50.0% |\n| Large (200–500) | 40 | 13,628 | 0% | \\placeholder{34.3%} [pending recalc] | 85.7% |\n| XLarge (500+) | 29 | 25,949 | 0% | \\placeholder{31.4%} [pending recalc] | 96.0% |\n| **Total** | **123** | **44,173** | **0%** | **\\placeholder{34.3%} [pending recalc]** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n",
    "structuredPatch": [
      {
        "oldStart": 140,
        "oldLines": 3,
        "newStart": 140,
        "newLines": 4,
        "lines": [
          " The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.",
          " ",
          " &lt;!-- Claim 2 wording fix: 2026-05-15 -->",
          "+&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
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

_source line 99_

<details open><summary>🔧 Tool call — Edit · `toolu_01HjjGf3LpCjKkVmGeDGKLv1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction_v2.md",
  "old_string": "\\end{enumerate}",
  "new_string": "\\end{enumerate}\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "71345f4f-a570-4fd4-bd67-7acff5d79965",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfBHsWeNEjXJszSRTCZuJZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 75607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-15T02:17:02.417Z_

<details><summary>↩ Tool result · `toolu_01HjjGf3LpCjKkVmGeDGKLv1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "c4b63bd6-df16-4cae-a46f-d694ca395804",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction_v2.md",
    "oldString": "\\end{enumerate}",
    "newString": "\\end{enumerate}\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "originalFile": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis reveals that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) mediates strategy effectiveness, providing a mechanistic hypothesis for when different strategies should be preferred (pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 28,
        "oldLines": 3,
        "newStart": 28,
        "newLines": 4,
        "lines": [
          " \\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.",
          " \\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.",
          " \\end{enumerate}",
          "+&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
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

_source line 101_

<details open><summary>🔧 Tool call — Edit · `toolu_01UDxkaH3n7zmDJJHyhoAT8H`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
  "old_string": "&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
  "new_string": "&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "107346bb-7ddc-4c82-b9e3-eb67907b6443",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfBHsWeNEjXJszSRTCZuJZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 75607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-15T02:17:03.713Z_

<details><summary>↩ Tool result · `toolu_01UDxkaH3n7zmDJJHyhoAT8H`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "8a7c1b8d-296b-49fc-a5f9-4402ef1394c3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
    "oldString": "&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
    "newString": "&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "originalFile": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 3,
        "newStart": 30,
        "newLines": 4,
        "lines": [
          " \\end{enumerate}",
          " ",
          " &lt;!-- Claim 2 wording fix: 2026-05-15 -->",
          "+&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
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

_source line 103_

<details><summary>Logged reasoning block</summary>

```text
All edits are done. Let me verify the changes by quickly checking the key modified sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "46037eb8-8200-4513-85f7-763f6434821b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Mj4vPMocZhyH4KmWQud5D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 76720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1715
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

验证修改是否正确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "9306272b-b46b-42cc-a159-238123a06737",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Mj4vPMocZhyH4KmWQud5D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 76720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1715
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_014NPg27NtsGAbzxtb298ypm`</summary>

```json
{
  "command": "echo \"=== method_v1 (_project) ===\" && grep -n \"BM25\\|sim(E_\\|argtop\\|structurally\" artifacts/_project/paper/method_v1.md | head -15 && echo \"\" && echo \"=== method_v1 (drafts) ===\" && grep -n \"BM25\\|sim(E_\\|argtop\\|structurally\" artifacts/paper_drafts/method_v1.md | head -15 && echo \"\" && echo \"=== experiments_v1 (_project) ===\" && grep -n \"Dataflow-aware negatives use\" artifacts/_project/paper/experiments_v1.md && echo \"\" && echo \"=== experiments_v1 (drafts) ===\" && grep -n \"Dataflow-aware negatives use\" artifacts/paper_drafts/experiments_v1.md && echo \"\" && echo \"=== intro_v2 (_project) ===\" && grep -n \"dataflow-aware mining\" artifacts/_project/paper/introduction_v2.md && echo \"\" && echo \"=== intro_v2 (drafts) ===\" && grep -n \"dataflow-aware mining\" artifacts/paper_drafts/introduction_v2.md",
  "description": "Verify D041 BM25 fixes across all files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "8fc0bb53-852d-4106-8717-b4f4b2520b25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Mj4vPMocZhyH4KmWQud5D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 76720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1715
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-15T02:17:12.698Z_

<details><summary>↩ Tool result · `toolu_014NPg27NtsGAbzxtb298ypm`</summary>

```text
=== method_v1 (_project) ===
27:**Structural Coverage.** At full scale, 78\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.
51:$$f^-_{\text{embed}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$
55:**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives from among files that are structurally connected to the query context. Formally, for query $q$ with associated gold files $\mathcal{F}^+_q$, we define the reachability set $\mathcal{R}_G(q) = \{f \in \mathcal{F} : \exists f^+ \in \mathcal{F}^+_q,\ (f^+, f) \in E^*\}$, where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:
57:$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \in \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{BM25}(q, f)$$
59:That is, we select the top-$K$ non-gold files that are **structurally reachable** from the gold files in the data-flow graph, ranked by BM25 lexical similarity. The intuition is that these files represent a category of particularly informative negatives: they share inter-procedural data-flow connections with the gold files (making them structurally plausible) and exhibit high lexical overlap with the query, yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.
61:**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).
63:For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally connected candidates), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\% of training instances, which we analyze separately in stratified evaluation (§5).
64:&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->

=== method_v1 (drafts) ===
30:At full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].
65:$$f^-_{\text{embed}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$
71:This strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\mathcal{F}^+_q$, define the reachability set:
77:$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \in \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{BM25}(q, f)$$
79:These files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.
85:The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).
87:### Relationship to BM25 Baselines
89:In addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].
116:&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->

=== experiments_v1 (_project) ===
21:**Negative Mining.** Embedding-distance negatives are mined using FAISS \cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.

=== experiments_v1 (drafts) ===
21:**Negative Mining.** Embedding-distance negatives are mined using FAISS \cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.

=== intro_v2 (_project) ===
17:We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.

=== intro_v2 (drafts) ===
17:We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "38f9abb4-939a-4957-bddb-64001c476a97",
  "tool_use_result": {
    "stdout": "=== method_v1 (_project) ===\n27:**Structural Coverage.** At full scale, 78\\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.\n51:$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n55:**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives from among files that are structurally connected to the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n57:$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n59:That is, we select the top-$K$ non-gold files that are **structurally reachable** from the gold files in the data-flow graph, ranked by BM25 lexical similarity. The intuition is that these files represent a category of particularly informative negatives: they share inter-procedural data-flow connections with the gold files (making them structurally plausible) and exhibit high lexical overlap with the query, yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.\n61:**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).\n63:For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally connected candidates), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 34\\% of training instances, which we analyze separately in stratified evaluation (§5).\n64:&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n\n=== method_v1 (drafts) ===\n30:At full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\n65:$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n71:This strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n77:$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n79:These files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.\n85:The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n87:### Relationship to BM25 Baselines\n89:In addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n116:&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n\n=== experiments_v1 (_project) ===\n21:**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n=== experiments_v1 (drafts) ===\n21:**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n=== intro_v2 (_project) ===\n17:We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.\n\n=== intro_v2 (drafts) ===\n17:We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.",
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

全部修改已完成且验证通过。`experiment_setup_v1.md` 无 dataflow-aware 排序描述，无需修改。

修改汇总：

| 文件 | 修改内容 |
|------|---------|
| **method_v1.md** (×2) | 公式 `sim(E_θ0)` → `BM25(q,f)`；约束 `f ∉ R_G` → `f ∈ R_G`；"structurally disconnected" → "structurally connected"；`E*` 改为 2-hop bounded；Difficulty Gradient 段同步修正 |
| **experiments_v1.md** (×2) | "selecting by embedding distance" → "rank them by BM25 to select top-K negatives" |
| **introduction_v2.md** (×2) | "filters structurally connected files from the embedding-distance candidate set" → "selects negatives from structurally connected files ranked by BM25" |
| **experiment_setup_v1.md** | 无改动（不含 dataflow-aware 排序描述） |

所有修改文件末尾已添加 `&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->`。embedding-distance 策略描述未改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "uuid": "6178720d-ec28-4a7c-b05d-d6a63ab88ff5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CsWdCUtMy3zZRQ5JNbudNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2468,
      "cache_read_input_tokens": 78435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2468
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

_source line 108_

全部修改已完成且验证通过。`experiment_setup_v1.md` 无 dataflow-aware 排序描述，无需修改。

修改汇总：

| 文件 | 修改内容 |
|------|---------|
| **method_v1.md** (×2) | 公式 `sim(E_θ0)` → `BM25(q,f)`；约束 `f ∉ R_G` → `f ∈ R_G`；"structurally disconnected" → "structurally connected"；`E*` 改为 2-hop bounded；Difficulty Gradient 段同步修正 |
| **experiments_v1.md** (×2) | "selecting by embedding distance" → "rank them by BM25 to select top-K negatives" |
| **introduction_v2.md** (×2) | "filters structurally connected files from the embedding-distance candidate set" → "selects negatives from structurally connected files ranked by BM25" |
| **experiment_setup_v1.md** | 无改动（不含 dataflow-aware 排序描述） |

所有修改文件末尾已添加 `&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->`。embedding-distance 策略描述未改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 442349,
  "duration_api_ms": 443519,
  "num_turns": 42,
  "stop_reason": "end_turn",
  "session_id": "6bd8e9ac-a19e-4249-9ebb-8d2d80ffeb88",
  "total_cost_usd": 1.4097300000000001,
  "usage": {
    "input_tokens": 24,
    "cache_creation_input_tokens": 69456,
    "cache_read_input_tokens": 757596,
    "output_tokens": 23813,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 69456,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 348,
        "cache_read_input_tokens": 78435,
        "cache_creation_input_tokens": 2468,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2468
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1302,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001387,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 24,
      "outputTokens": 23813,
      "cacheReadInputTokens": 757596,
      "cacheCreationInputTokens": 69456,
      "webSearchRequests": 0,
      "costUSD": 1.4083430000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d6d3c819-69e1-40e0-9d8f-53a44bdf6052"
}
```

</details>

---
