# paper consistency audit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 95
- **Recorded user turns:** 1
- **Tool calls:** 30
- **Original source:** `logs/workers/worker_paper_consistency-audit_20260516T005941.log`
- **Structured JSON:** [`d6edb170675fbdcfc610.json`](../../sessions/d6/d6edb170675fbdcfc610.json)

## Before a recorded user message

32 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
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
  "uuid": "a448532b-30c8-4771-b9ae-306284dfa1b6",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/memory/"
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
    "resetsAt": 1778905200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b2cf3c08-f087-4b51-83d9-a09cc33e5c5c",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Assistant

_source line 4_

I'll read all the paper sections to conduct the consistency audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "9461376c-e100-4417-a6a1-e05e6be80be8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBouwqnmVfjSzsL2jPNxye",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12018,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12018
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UMGwkr3HsUhSHhNPsqx4zL`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "db369e26-8cda-49a5-84e7-dd8c4f542f7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBouwqnmVfjSzsL2jPNxye",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12018,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12018
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

_source line 6 · 2026-05-16T00:59:51.590Z_

<details><summary>↩ Tool result · `toolu_01UMGwkr3HsUhSHhNPsqx4zL`</summary>

````text
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
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "2b042add-db27-487b-b24f-cd90f78f5e3c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
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
Let me read all the paper sections. I'll start by reading multiple files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "5527ba81-79ca-44a7-9e86-95682af0ae49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dvyc3VuyJ5fbCvKUJLc14m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 23465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 449
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

_source line 8_

Let me read all paper sections in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "206b6ea3-2bab-47e0-bf27-0eda16d2fad5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dvyc3VuyJ5fbCvKUJLc14m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 23465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 449
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SbPV2XZg2YHX4U96Z3sDyM`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "artifacts/_project/paper/introduction.tex",
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
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "b32e0474-1f8e-4ece-abd0-d32990144026",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dvyc3VuyJ5fbCvKUJLc14m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 23465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 449
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

_source line 10 · 2026-05-16T00:59:55.729Z_

<details><summary>↩ Tool result · `toolu_01SbPV2XZg2YHX4U96Z3sDyM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/introduction.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "feaa8ae9-a9c3-4e54-95cb-5e0b96a78470",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/introduction.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/introduction.tex'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WvbwJJ7A9yhAZpvThi5NEn`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "artifacts/_project/paper/method.tex",
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
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "b62a380b-e447-4e4e-aaea-09985b74021a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dvyc3VuyJ5fbCvKUJLc14m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 23465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 449
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

_source line 12 · 2026-05-16T00:59:55.951Z_

<details><summary>↩ Tool result · `toolu_01WvbwJJ7A9yhAZpvThi5NEn`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/method.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "91faabdb-fc6e-4c32-944d-4492a9d53cb2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/method.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/method.tex'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TpFype5LPq9EzxG4Lx9n7S`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "artifacts/_project/paper/related_work.tex",
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
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "606cf885-602d-4dee-946e-9fc57b733532",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dvyc3VuyJ5fbCvKUJLc14m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 23465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 449
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

_source line 14 · 2026-05-16T00:59:56.856Z_

<details><summary>↩ Tool result · `toolu_01TpFype5LPq9EzxG4Lx9n7S`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/related_work.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "1be4e8f0-eb3d-4efd-aa35-1e8b20d88523",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/related_work.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/related_work.tex'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NPiq1cMYbzKuF3kvNwrbGC`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "artifacts/_project/paper/experiments.tex",
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
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "91d19905-ec5b-4647-80f4-06ae85da73d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dvyc3VuyJ5fbCvKUJLc14m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 23465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 449
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

_source line 16 · 2026-05-16T00:59:57.320Z_

<details><summary>↩ Tool result · `toolu_01NPiq1cMYbzKuF3kvNwrbGC`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/experiments.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "7a0b7ad4-6ebf-419a-9b53-18c7f0bf495d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/experiments.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/experiments.tex'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Kwy3Q2rAhASXE6bAmeL2WL`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "artifacts/_project/paper/results.tex",
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
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "4fc337ae-7d81-474c-8315-eaf8483b80ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dvyc3VuyJ5fbCvKUJLc14m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 23465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 449
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

_source line 18 · 2026-05-16T00:59:58.292Z_

<details><summary>↩ Tool result · `toolu_01Kwy3Q2rAhASXE6bAmeL2WL`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/results.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "74ed53b8-424e-49df-8fb4-381e08a34f48",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/results.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/results.tex'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VdvKUYDtKMEBkvodZbvw1Y`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "artifacts/_project/paper/discussion.tex",
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
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "9bc39cd3-c7c6-4f8a-bc9f-7de46d47ea21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dvyc3VuyJ5fbCvKUJLc14m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 23465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 449
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

_source line 20 · 2026-05-16T00:59:58.795Z_

<details><summary>↩ Tool result · `toolu_01VdvKUYDtKMEBkvodZbvw1Y`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/discussion.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "bf7bea12-c3dd-4f5e-9ded-afc7dbcdff4c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/discussion.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/discussion.tex'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WdiMCNgj1QacSUidzrXarg`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "artifacts/_project/paper/conclusion.tex",
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
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "f1684ab2-ff11-4394-903a-c42609070b53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dvyc3VuyJ5fbCvKUJLc14m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 23465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 449
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

_source line 22 · 2026-05-16T00:59:59.699Z_

<details><summary>↩ Tool result · `toolu_01WdiMCNgj1QacSUidzrXarg`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/conclusion.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "bab002e4-dd6f-43fe-b31f-0584b0f440ad",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/conclusion.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/conclusion.tex'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HTKrqkcSz6aCRSJRoiyp5u`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "artifacts/_project/paper/table1_main_results.tex",
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
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "7dbcafec-256a-4b27-9396-3224c58671ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dvyc3VuyJ5fbCvKUJLc14m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 23465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 449
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

_source line 24 · 2026-05-16T01:00:00.179Z_

<details><summary>↩ Tool result · `toolu_01HTKrqkcSz6aCRSJRoiyp5u`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/table1_main_results.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "24ce161a-c595-495d-97eb-be3715db0103",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/table1_main_results.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/_project/paper/table1_main_results.tex'\", \"metadata\": {}}"
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
The `read_project_file` tool only works for specific project files, not arbitrary paths. I need to read the tex files directly from the filesystem. Let me find them first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "9c71755c-d00c-4b57-9f3c-1f52c41b1f88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4QnNa5HeYMaSufhcUYHdc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2473,
      "cache_read_input_tokens": 23914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2473
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

The MCP tool only supports specific project files. Let me read the tex files directly from the artifacts directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "a06fbfc4-c93d-4a3b-96b7-a5e62faaf439",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4QnNa5HeYMaSufhcUYHdc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2473,
      "cache_read_input_tokens": 23914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2473
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01NWgTSN7NcFrno43Mr2eE2M`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "96e01005-5f88-4b39-a9fc-707d05426c55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4QnNa5HeYMaSufhcUYHdc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2473,
      "cache_read_input_tokens": 23914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2473
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T01:00:05.253Z_

<details><summary>↩ Tool result · `toolu_01NWgTSN7NcFrno43Mr2eE2M`</summary>

```text
artifacts/_project/paper/related_work_963aec.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/method_76a694.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_1613c9.tex
artifacts/_project/paper/results_819b43.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/conclusion_386ecc.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/introduction_a663ee.tex
artifacts/_project/paper/method_3f5a58.tex
artifacts/_project/paper/introduction_c6a67f.tex
artifacts/_project/paper/experiments_86dfd1.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/related_work_0b6096.tex
artifacts/_project/paper/table1_main_results.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/results_d0d647.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/discussion_270aaa.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "edaeb308-ac17-4b40-9d89-3db8dc84d63f",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/related_work_963aec.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/method_76a694.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/experiments_1613c9.tex",
      "artifacts/_project/paper/results_819b43.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/conclusion_386ecc.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/introduction_a663ee.tex",
      "artifacts/_project/paper/method_3f5a58.tex",
      "artifacts/_project/paper/introduction_c6a67f.tex",
      "artifacts/_project/paper/experiments_86dfd1.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/related_work_0b6096.tex",
      "artifacts/_project/paper/table1_main_results.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/results_d0d647.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/discussion_270aaa.tex"
    ],
    "durationMs": 16,
    "numFiles": 20,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
There are multiple versions of each file. I'll read the latest versions - the ones with hashes are likely newer versions, and the base names are the originals. The task mentions:
- `results_d0d647.tex` is v2 updated version
- `discussion_270aaa.tex` is v2 updated version

I should read the latest versions. Let me use the hash versions where available and the base versions otherwise. But actually, I should read both to check consistency. Let me focus on the most recent versions for the audit.

Let me read all the key files. I'll use agents to parallelize this since there are many files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "e0b904bd-64f1-4b96-9014-e04531ef7b4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018iETiHLjyf9WX9mLbVX4Dq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 26387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

Found 20 tex files. Let me read all the key sections — I'll use the latest versions where hash variants exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "31a321df-9af7-47d9-af6d-4f965f507ce0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018iETiHLjyf9WX9mLbVX4Dq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 26387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Agent · `toolu_01JwscEPDwAWYsvzEyjiYamw`</summary>

```json
{
  "description": "Read all paper tex files",
  "prompt": "Read all the following tex files from the paper directory and return their FULL contents. This is for a consistency audit of a research paper.\n\nBase path: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/\n\nRead these files (use the latest version where hash variants exist):\n1. introduction_c6a67f.tex (latest intro)\n2. introduction.tex (base intro for comparison)\n3. method_3f5a58.tex (latest method) \n4. method.tex (base method)\n5. related_work_0b6096.tex (latest related work)\n6. related_work.tex (base)\n7. experiments_86dfd1.tex (latest experiments)\n8. experiments.tex (base)\n9. results_d0d647.tex (v2 results)\n10. results.tex (base results)\n11. discussion_270aaa.tex (v2 discussion)\n12. discussion.tex (base discussion)\n13. conclusion_386ecc.tex (latest conclusion)\n14. conclusion.tex (base conclusion)\n15. table1_main_results.tex\n\nFor each file, output: \"=== FILENAME ===\" followed by the full file content. Do NOT summarize — output every line verbatim. This is critical for cross-referencing numbers and symbols.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "04c610e7-f2d8-49f6-a88a-6e32b4a49dbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018iETiHLjyf9WX9mLbVX4Dq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 26387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Read all paper tex files",
  "task_type": "local_agent",
  "prompt": "Read all the following tex files from the paper directory and return their FULL contents. This is for a consistency audit of a research paper.\n\nBase path: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/\n\nRead these files (use the latest version where hash variants exist):\n1. introduction_c6a67f.tex (latest intro)\n2. introduction.tex (base intro for comparison)\n3. method_3f5a58.tex (latest method) \n4. method.tex (base method)\n5. related_work_0b6096.tex (latest related work)\n6. related_work.tex (base)\n7. experiments_86dfd1.tex (latest experiments)\n8. experiments.tex (base)\n9. results_d0d647.tex (v2 results)\n10. results.tex (base results)\n11. discussion_270aaa.tex (v2 discussion)\n12. discussion.tex (base discussion)\n13. conclusion_386ecc.tex (latest conclusion)\n14. conclusion.tex (base conclusion)\n15. table1_main_results.tex\n\nFor each file, output: \"=== FILENAME ===\" followed by the full file content. Do NOT summarize — output every line verbatim. This is critical for cross-referencing numbers and symbols.",
  "uuid": "d4666c14-6e46-482b-abfb-370dd4dcaf55",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

## Round 1

63 recorded events

### User

_source line 33 · 2026-05-16T01:00:16.614Z_

Read all the following tex files from the paper directory and return their FULL contents. This is for a consistency audit of a research paper.

Base path: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/

Read these files (use the latest version where hash variants exist):
1. introduction_c6a67f.tex (latest intro)
2. introduction.tex (base intro for comparison)
3. method_3f5a58.tex (latest method) 
4. method.tex (base method)
5. related_work_0b6096.tex (latest related work)
6. related_work.tex (base)
7. experiments_86dfd1.tex (latest experiments)
8. experiments.tex (base)
9. results_d0d647.tex (v2 results)
10. results.tex (base results)
11. discussion_270aaa.tex (v2 discussion)
12. discussion.tex (base discussion)
13. conclusion_386ecc.tex (latest conclusion)
14. conclusion.tex (base conclusion)
15. table1_main_results.tex

For each file, output: "=== FILENAME ===" followed by the full file content. Do NOT summarize — output every line verbatim. This is critical for cross-referencing numbers and symbols.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "672fc988-957f-4022-931b-2c668f99c7cc"
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
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/introduction_c6a67f.tex",
  "usage": {
    "total_tokens": 14241,
    "tool_uses": 1,
    "duration_ms": 2884
  },
  "last_tool_name": "Read",
  "uuid": "1613fe19-1e9b-4c7d-a78f-5be5fcaca888",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_016gdTzyfh36TRfM3zvTHQK4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/introduction_c6a67f.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "8bee4c60-e45b-4c41-abfc-23f580b46e8c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 36 · 2026-05-16T01:00:19.507Z_

<details><summary>↩ Tool result · `toolu_016gdTzyfh36TRfM3zvTHQK4`</summary>

```text
1	% Introduction for "Minimum Intervention Reweighting: Adaptive Exponent Selection
2	% for Contamination-Aware Pretraining"
3	% Generated: 2026-05-15
4	% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)
5	
6	\section{Introduction}
7	\label{sec:intro}
8	
9	Web pretraining corpora are increasingly contaminated by machine-generated text, with recent estimates placing the synthetic fraction between 20\% and 60\% \citep{cheng2025contamination}.
10	This poses a fundamental threat to model quality: \cite{shumailov2024model} demonstrate that training on recursively generated data leads to irreversible model collapse, and \cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger degradation, ruling out data scaling as a remedy.
11	As synthetic content becomes ubiquitous, \emph{contamination-aware training}---strategies that explicitly account for data provenance during optimization---is necessary for maintaining pretraining quality.
12	
13	A natural mitigation is detect-and-reweight: assign each sample a weight $w(x) = (1 - q(x))^b$ based on a detector's estimated synthetic probability $q(x)$, where larger $b$ downweights suspected synthetic text more aggressively \citep{drayson2025detection}.
14	However, the exponent $b$ is a sensitive per-model hyperparameter whose optimal value varies by an order of magnitude across model scales---$b = 1$ for SmolLM-1.7B versus $b = 10$ for GPT-2 124M---and selecting it requires a clean validation set and grid search costing up to $6{\times}$ the base training budget.
15	The practical question is: \emph{given per-sample detector scores $q(x)$, how should $b$ be chosen without validation?}
16	
17	We propose a \emph{dual-constraint framework} that derives the exponent adaptively per batch from two diagnostics computed on the detector scores alone.
18	The effective real proportion $\aeff(b)$ measures the weighted fraction of gradient signal from real data and imposes a \emph{quality floor}: $\aeff(b) \geq \tau$---at least enough cleaning.
19	Kish's effective sample size $\mathrm{ESS}(b)$ \citep{vehtari2024psis} quantifies weight concentration and imposes a \emph{stability ceiling}: $\mathrm{ESS}(b) \geq \nmin$---not so much cleaning that gradient estimates degrade.
20	A key structural insight makes this tractable: $\aeff$ is strictly increasing in $b$ while $\mathrm{ESS}$ is strictly decreasing, so the quality constraint yields a unique lower bound $\btau$ and the stability constraint a unique upper bound $\bess$.
21	We adopt a \emph{minimum intervention principle}:
22	\begin{equation*}
23	  \bstar = \inf\{b \geq 0 : \aeff(b) \geq \tau\} \quad \text{subject to} \quad \mathrm{ESS}(\bstar) \geq \nmin,
24	\end{equation*}
25	the smallest exponent satisfying the quality floor.
26	This is deliberately conservative: apply enough decontamination to meet the quality target, but no more, preserving the largest possible effective sample size.
27	In practice, batches fall into three regimes---already clean ($\bstar{=}0$), quality-binding ($\bstar{=}\btau$), and stability-binding ($\bstar{=}\bess$)---allowing the framework to handle heterogeneous contamination naturally.
28	Unlike the discrete sampling-importance-resampling of \cite{drayson2025detection}, we implement reweighting through direct loss scaling with continuous gradient contributions.
29	
30	We evaluate on continued pretraining of Qwen3-0.6B on 132M FineWeb \citep{penedo2024fineweb} tokens with 40\% synthetic contamination (\S\ref{sec:experiments}).
31	Adaptive $\bstar$ with default hyperparameters ($\tau{=}0.8$, $\nmin{=}2$) matches the grid-search-optimal fixed $b$ within seed variance (PPL $17.650 {\pm} 0.007$ vs.\ $17.646 {\pm} 0.007$ across three seeds) at zero validation cost.
32	It outperforms both uniform training (PPL $17.69$) and ESS-only maximum intervention (PPL $17.73$), confirming that minimum intervention is superior to maximum intervention.
33	A lightweight TF-IDF + logistic regression detector (AUC\,=\,0.939) suffices for effective reweighting, and the quality threshold $\tau$ admits a wide safe range of $[0.5, 0.8]$ within which all tested values improve over uniform training.
34	
35	Our contributions are:
36	\begin{enumerate}[nosep,leftmargin=*]
37	  \item A dual-constraint framework for adaptive $\bstar$ selection with minimum intervention semantics, providing validation-free per-batch exponent derivation from batch-level diagnostics (\S\ref{sec:method}).
38	  \item Empirical evidence that adaptive $\bstar$ matches grid-search-optimal performance within seed variance at zero validation cost, and that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only) (\S\ref{sec:results}).
39	  \item Evidence that a lightweight TF-IDF + logistic regression detector suffices for effective reweighting (\S\ref{sec:results}).
40	\end{enumerate}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "2f78f0a0-1382-44ff-9e73-f07ff763122f"
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
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/introduction.tex",
  "usage": {
    "total_tokens": 14242,
    "tool_uses": 2,
    "duration_ms": 3154
  },
  "last_tool_name": "Read",
  "uuid": "859f84ca-553d-46aa-a93d-67db25f4e63a",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01Ap33EeAjjy7Q9iUegYGpuf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "087de2e7-5b14-46e3-8872-4ef9848c79c4",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 39 · 2026-05-16T01:00:19.773Z_

<details><summary>↩ Tool result · `toolu_01Ap33EeAjjy7Q9iUegYGpuf`</summary>

```text
1	Web corpora increasingly contain machine-generated text.
2	Recent estimates place the synthetic fraction at 20--60\% of crawled data~\citep{cheng_2025_contamination_survey}, and this share grows as language models are deployed for content production at scale.
3	Training on such contaminated data has concrete consequences: \citet{shumailov_2024_model_collapse} show that recursive training on model outputs leads to irreversible quality degradation---\emph{model collapse}---and \citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.
4	A central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.
5	The prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.
6	
7	A natural response is \emph{detect-and-reweight}: train a classifier to estimate each sample's synthetic probability $q(x)$, then suppress likely-synthetic samples via the weighting function $w(x) = (1 - q(x))^b$.
8	\citet{drayson_2025_detection_collapse} demonstrate this approach for model collapse prevention and show that the exponent $b$ critically determines outcomes---their optimal values range from $b{=}10$ for models at ${\leq}360$M parameters to $b{=}1$ at 1.7B, and misspecification degrades results substantially.
9	Selecting $b$ therefore requires per-model validation-set grid search, with computational cost scaling linearly in the number of candidates (six training runs in a typical sweep).
10	Other approaches assume even stronger supervision: \citet{he_2025_golden_ratio} derive theoretically optimal weights from convergence analysis but require the exact contamination ratio $\rho$, which is precisely what is unavailable in practice.
11	Hard detection-and-removal strategies~\citep{feng_2025_beyond_collapse} discard borderline samples entirely, sacrificing the smooth reweighting that continuous $q$-scores enable.
12	
13	Given per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?
14	We formulate this as a dual-constrained optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\aeff(b)$ reaches a quality threshold $\tau$, while keeping Kish's effective sample size $\mathrm{ESS}(b)$ above a stability floor $\nmin$.
15	The quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effective real-data fraction~\citep{wang_2026_survive_contamination}, motivating a lower bound on $\aeff$.
16	The stability constraint prevents extreme weight concentration that degrades gradient quality.
17	These two requirements exhibit a natural opposition.
18	$\aeff(b)$ increases monotonically in $b$ (Proposition~\ref{prop:monotone}), yielding a lower bound $\btau$---the minimum exponent needed to achieve the target quality.
19	$\mathrm{ESS}(b)$ decreases monotonically, yielding an upper bound $\bess$---the maximum exponent before gradient stability degrades.
20	The adaptive exponent $\bstar = \btau$ when the feasible region $[\btau, \bess]$ is non-empty, embodying a \emph{minimum intervention principle}: apply the least downweighting sufficient to meet the quality target, preserving as much effective training data as possible.
21	When the constraints conflict ($\btau > \bess$), the stability ceiling takes precedence.
22	
23	This minimum-intervention semantics distinguishes the method from the alternative of maximizing $b$ subject only to ESS stability.
24	Among batches that require reweighting, the dual-constraint solver selects $\bstar$ via the $\aeff$ bound in 40\% of cases, with mean $\bstar{=}1.67$; the ESS-only variant would choose $b{=}4.15$ in these same batches, 2.5$\times$ more aggressive.
25	The remaining 49.9\% of batches have sufficient real-data content to skip reweighting entirely ($\bstar{=}0$).
26	The per-batch $\bstar$ distribution (median 0.87, mean 1.40) adapts continuously to each batch's contamination composition without any held-out signal.
27	
28	On Qwen3-0.6B continued pretraining with 40\% synthetic contamination (132M+ tokens from FineWeb), adaptive reweighting achieves mean held-out perplexity of 17.651 across three seeds, matching the grid-searched optimum ($b{=}0.5$, mean 17.646) within seed-to-seed variance (\S\ref{sec:results}).
29	The grid sweep requires six complete training runs to identify this optimum; the adaptive method requires one.
30	The ESS-only variant (maximum intervention) yields mean PPL 17.722---worse than the uniform baseline (17.694)---confirming that maximum intervention degrades training while minimum intervention improves it.
31	A lightweight TF-IDF + Logistic Regression detector (AUC\,=\,0.939, calibrated ECE\,=\,0.048) suffices throughout, suggesting that score calibration matters more than raw classification accuracy for provenance-based reweighting.
32	
33	Our contributions:
34	\begin{itemize}[nosep,leftmargin=*]
35	\item A dual-constrained framework for adaptive exponent selection: $\bstar = \inf\{b \geq 0 : \aeff(b) \geq \tau\}$ subject to $\mathrm{ESS}(b) \geq \nmin$, computed per-batch from detector scores with minimum-intervention semantics (\S\ref{sec:method}).
36	\item Empirical evidence that adaptive $\bstar$ matches grid-searched best within seed variance at zero validation cost, and that minimum intervention (dual constraint) outperforms maximum intervention (ESS-only) across three seeds (\S\ref{sec:results}).
37	\item A demonstration that a lightweight TF-IDF + LR detector with calibrated $q$-scores supports effective reweighting, achieving results comparable to stronger neural detectors (\S\ref{sec:experiments}).
38	\end{itemize}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "87635987-2e78-417d-92fd-ff92986e7079"
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
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/method_3f5a58.tex",
  "usage": {
    "total_tokens": 14243,
    "tool_uses": 3,
    "duration_ms": 3531
  },
  "last_tool_name": "Read",
  "uuid": "adc23742-0a11-4923-a694-d00e30950157",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_019UKvL5H73r5QYd9JBbL2sx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/method_3f5a58.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "f918b772-85fe-455b-b231-6a0d0301cda8",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 42 · 2026-05-16T01:00:20.151Z_

<details><summary>↩ Tool result · `toolu_019UKvL5H73r5QYd9JBbL2sx`</summary>

```text
1	% Method section for "Minimum Intervention Reweighting" (EMNLP 2026)
2	% Generated: 2026-05-15
3	% Based on: paper_framing.md (STABLE, D023/D029/D035)
4	% Requires macros: \bstar, \aeff, \nmin, \btau, \bess (defined in main.tex preamble)
5	
6	\section{Method}
7	\label{sec:method}
8	
9	\subsection{Problem Setup}
10	\label{sec:problem-setup}
11	
12	Let $\mathcal{D} = \{x_1, \ldots, x_N\}$ denote a pretraining corpus comprising human-written text $\mathcal{D}_{\mathrm{real}}$ and machine-generated text $\mathcal{D}_{\mathrm{synth}}$, with unknown contamination rate $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$.
13	A pretrained detector assigns each sample a synthetic probability $q(x_i) \in [0, 1]$.
14	Following \citet{drayson_2025_detection_collapse}, we define per-sample weights
15	\begin{equation}
16	  w_b(x_i) = (1 - q(x_i))^b, \quad b \geq 0,
17	  \label{eq:weight}
18	\end{equation}
19	where $b = 0$ recovers uniform weighting and increasing $b$ progressively downweights high-$q$ samples.
20	The weighted training objective is
21	\begin{equation}
22	  \mathcal{L}(b) = \frac{\sum_{i} w_b(x_i) \, \ell(x_i; \theta)}{\sum_{j} w_b(x_j)},
23	  \label{eq:loss}
24	\end{equation}
25	where $\ell(x_i; \theta)$ is the per-sample language modeling loss.
26	
27	\citet{drayson_2025_detection_collapse} treat $b$ as a hyperparameter selected via validation-based grid search, with reported optima ranging from $b{=}1$ (SmolLM-1.7B) to $b{=}10$ (GPT-2 124M), making per-model tuning unavoidable.
28	We instead derive $b$ adaptively per batch from the detector scores alone, requiring no validation set.
29	
30	\subsection{Dual-Constraint Framework}
31	\label{sec:dual-constraint}
32	
33	Higher $b$ removes more synthetic influence but also discards effective training signal.
34	We formalize this trade-off through two per-batch statistics.
35	
36	\paragraph{Effective real proportion.}
37	For a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with weights $w_i(b) = (1 - q_i)^b$, we define
38	\begin{equation}
39	  \aeff(b) = \frac{\sum_{i \in \mathcal{B}} w_i(b) \cdot \mathbf{1}[x_i \in \mathcal{D}_{\mathrm{real}}]}{\sum_{i \in \mathcal{B}} w_i(b)},
40	  \label{eq:alpha_eff}
41	\end{equation}
42	measuring the effective fraction of real data after reweighting.
43	Since true provenance labels are unavailable at training time, we use the detector's hard prediction $\mathbf{1}[q(x_i) < 0.5]$ as a proxy; all theoretical properties below hold for this approximation.
44	
45	\paragraph{Effective sample size.}
46	Kish's effective sample size \citep{vehtari_2024_psis} quantifies weight concentration:
47	\begin{equation}
48	  \mathrm{ESS}(b) = \frac{\left(\sum_{i \in \mathcal{B}} w_i(b)\right)^2}{\sum_{i \in \mathcal{B}} w_i^2(b)}.
49	  \label{eq:ess}
50	\end{equation}
51	$\mathrm{ESS}(0) = B$ under uniform weights, decreasing toward $1$ as $b \to \infty$ for any batch containing synthetic samples.
52	
53	\begin{proposition}[Monotonicity]
54	\label{prop:monotonicity}
55	For any batch containing both real and synthetic samples with non-identical $q$-scores:
56	\begin{enumerate}[leftmargin=*,nosep]
57	  \item $\aeff(b)$ is strictly increasing in $b$.
58	  \item $\mathrm{ESS}(b)$ is strictly decreasing in $b$.
59	\end{enumerate}
60	\end{proposition}
61	
62	\begin{proof}[Proof sketch]
63	For (1), differentiating Eq.~\eqref{eq:alpha_eff} using $\frac{dw_i}{db} = w_i \ln(1 {-} q_i)$ yields
64	\begin{equation}
65	  \frac{d\aeff}{db} = \aeff(1 {-} \aeff) \!\left( \mathbb{E}_w[\ln(1{-}q) \mid \mathrm{real}] - \mathbb{E}_w[\ln(1{-}q) \mid \mathrm{synth}] \right)\!,
66	  \label{eq:dalpha}
67	\end{equation}
68	where $\mathbb{E}_w$ denotes expectation under the normalized weight distribution.
69	Since real samples have lower $q$-scores, $\ln(1{-}q)$ is strictly less negative for real than synthetic samples, making the parenthesized difference positive.
70	For (2), increasing $b$ multiplies each weight by $(1{-}q_i)^{\Delta b}$, a factor varying across samples, which concentrates the normalized weight distribution and strictly increases $\sum_i \tilde{w}_i^2$, hence decreasing ESS.
71	Full proofs appear in Appendix~\ref{app:proofs}.
72	\end{proof}
73	
74	Proposition~\ref{prop:monotonicity} establishes that quality and sample efficiency move in opposite directions as $b$ increases, motivating two complementary constraints.
75	
76	\paragraph{Quality lower bound.}
77	We require $\aeff(b) \geq \tau$ for a threshold $\tau \in (0, 1)$.
78	By strict monotonicity, this defines a unique lower bound
79	\begin{equation}
80	  \btau = \inf\{b \geq 0 : \aeff(b) \geq \tau\}
81	  \label{eq:b_tau}
82	\end{equation}
83	on the exponent---the minimum intervention needed to achieve quality $\tau$.
84	\citet{wang_2026_survive_contamination} show that pretraining convergence rate scales with effective real data fraction, providing theoretical motivation for maintaining $\aeff$ above a threshold.
85	
86	\paragraph{Stability upper bound.}
87	We require $\mathrm{ESS}(b) \geq \nmin$ for a floor $\nmin \geq 1$.
88	By strict monotonicity, this defines a unique upper bound
89	\begin{equation}
90	  \bess = \sup\{b \geq 0 : \mathrm{ESS}(b) \geq \nmin\}
91	  \label{eq:b_ess}
92	\end{equation}
93	beyond which gradient estimates become unreliable due to weight concentration.
94	
95	\paragraph{Minimum intervention principle.}
96	We select
97	\begin{equation}
98	  \bstar = \begin{cases}
99	    0 & \text{if } \aeff(0) \geq \tau \\
100	    \btau & \text{if } \btau \leq \bess \\
101	    \bess & \text{if } \btau > \bess
102	  \end{cases}
103	  \label{eq:bstar}
104	\end{equation}
105	yielding three regimes:
106	(1)~\textbf{Already clean} ($\aeff(0) \geq \tau$): the unweighted batch meets quality $\tau$; set $\bstar = 0$.
107	(2)~\textbf{$\aeff$-binding} ($\btau \leq \bess$): the quality constraint determines $\bstar = \btau$, applying the \emph{minimum} intervention to reach $\tau$, with ESS margin remaining.
108	(3)~\textbf{ESS-binding} ($\btau > \bess$): quality $\tau$ is infeasible under the stability constraint; $\bstar = \bess$ applies the maximum stable intervention.
109	
110	The key insight is that when the feasible region $[\btau, \bess]$ is non-empty, the method selects its \emph{left} endpoint---downweighting no more than necessary.
111	This contrasts with an ESS-only strategy that selects $\bess$ (the right endpoint), maximizing cleaning at the cost of discarding useful gradient signal from borderline samples.
112	In our experiments (\S\ref{sec:results}), 40.1\% of reweighted batches are $\aeff$-binding, where mean $\bstar = 1.67$ compared to $4.15$ under ESS-only---a $2.5\times$ less aggressive exponent that retains $\mathrm{ESS} = 2.60$, well above the floor $\nmin = 2$.
113	
114	\subsection{Algorithm}
115	\label{sec:algorithm}
116	
117	Algorithm~\ref{alg:solver} solves for $\bstar$ via bisection on $\aeff$, exploiting monotonicity (Proposition~\ref{prop:monotonicity}) to guarantee convergence.
118	
119	\begin{algorithm}[t]
120	\caption{Per-batch adaptive exponent solver}
121	\label{alg:solver}
122	\begin{algorithmic}[1]
123	\REQUIRE Batch scores $\{q_1, \ldots, q_B\}$, threshold $\tau$, ESS floor $\nmin$, tolerance $\varepsilon$, cap $b_{\max}$
124	\ENSURE Optimal exponent $\bstar$
125	\IF{$\aeff(0) \geq \tau$}
126	  \STATE \textbf{return} $\bstar = 0$ \hfill $\triangleright$ Already clean
127	\ENDIF
128	\STATE $b_{\mathrm{lo}} \leftarrow 0,\; b_{\mathrm{hi}} \leftarrow b_{\max}$ \hfill $\triangleright$ Bisect for $\btau$
129	\WHILE{$b_{\mathrm{hi}} - b_{\mathrm{lo}} > \varepsilon$}
130	  \STATE $b_{\mathrm{mid}} \leftarrow (b_{\mathrm{lo}} + b_{\mathrm{hi}}) / 2$
131	  \IF{$\aeff(b_{\mathrm{mid}}) < \tau$}
132	    \STATE $b_{\mathrm{lo}} \leftarrow b_{\mathrm{mid}}$
133	  \ELSE
134	    \STATE $b_{\mathrm{hi}} \leftarrow b_{\mathrm{mid}}$
135	  \ENDIF
136	\ENDWHILE
137	\STATE $\btau \leftarrow b_{\mathrm{hi}}$
138	\IF{$\mathrm{ESS}(\btau) \geq \nmin$}
139	  \STATE \textbf{return} $\bstar = \btau$ \hfill $\triangleright$ $\aeff$-binding
140	\ELSE
141	  \STATE Find $\bess = \sup\{b : \mathrm{ESS}(b) \geq \nmin\}$ via bisection
142	  \STATE \textbf{return} $\bstar = \bess$ \hfill $\triangleright$ ESS-binding
143	\ENDIF
144	\end{algorithmic}
145	\end{algorithm}
146	
147	\paragraph{Implementation.}
148	We apply $\bstar$ through loss reweighting: each sample's loss is scaled by its normalized weight $\bar{w}_i = w_{\bstar}(x_i) / \sum_j w_{\bstar}(x_j)$, yielding continuous gradient contributions from all samples including those with intermediate $q$-scores.
149	This contrasts with the sampling-importance-resampling (SIR) approach of \citet{drayson_2025_detection_collapse}, which discretely resamples a subset of the batch, introducing additional variance and discarding partial information from borderline samples.
150	
151	\paragraph{Computational cost.}
152	Each evaluation of $\aeff$ or ESS costs $O(B)$ for batch size $B$.
153	Bisection requires $O(\log(b_{\max} / \varepsilon))$ iterations, giving total per-batch overhead $O(B \log(b_{\max} / \varepsilon))$---negligible compared to the $O(BHD)$ cost of transformer forward and backward passes with hidden dimension $H$ and depth $D$.
154	With $b_{\max} = 20$ and $\varepsilon = 0.01$, this amounts to ${\sim}11$ iterations per batch.
155	
156	\subsection{Hyperparameters}
157	\label{sec:hyperparameters}
158	
159	The framework replaces the single sensitive exponent $b$ with two hyperparameters, $\tau$ and $\nmin$, both admitting principled defaults that transfer across settings without per-model tuning.
160	
161	\paragraph{Quality threshold $\tau$.}
162	\citet{wang_2026_survive_contamination} establish that pretraining convergence rate scales with effective real data proportion, motivating a quality threshold.
163	However, their analysis assumes known mixture proportions; since we do not assume known $\rho$, $\tau$ is an empirical hyperparameter with theoretical motivation rather than a theoretically derived quantity.
164	We evaluate $\tau \in \{0.5, 0.6, 0.7, 0.8, 0.9, 0.95\}$ at $\rho = 0.4$ (\S\ref{sec:results}).
165	All values in $[0.5, 0.8]$ improve over uniform training, with PPL spanning only $0.035$ across this range (17.688 at $\tau{=}0.5$ to 17.653 at $\tau{=}0.8$).
166	We adopt $\tau = 0.8$ as the default.
167	The sensitivity is asymmetric: under-cleaning ($\tau < 0.8$) yields mild degradation, while over-cleaning ($\tau > 0.8$) causes sharper regression as $\bstar$ inflates (mean $\bstar = 2.36$ at $\tau{=}0.9$ vs.\ $1.40$ at $\tau{=}0.8$), excessively suppressing borderline samples whose gradient signal remains useful.
168	
169	\paragraph{ESS floor $\nmin$.}
170	The stability constraint prevents gradient instability from weight concentration.
171	At $\nmin = 1$ (effectively unconstrained), $\bstar$ inflates to mean $7.20$ with 46.7\% of batches exceeding $\bstar = 2$, yielding PPL~$= 17.789$---worse than uniform ($17.694$) by $+0.095$, confirming that unconstrained downweighting is harmful.
172	At $\nmin \geq B$, the constraint forces $\bstar = 0$ for all batches, recovering uniform training.
173	We use $\nmin = 2$ (half the batch size for $B = 4$), which yields consistent improvement across three seeds (\S\ref{sec:results}).
174	
175	\paragraph{Comparison with fixed $b$.}
176	Both $\tau$ and $\nmin$ admit wide effective ranges ($\tau \in [0.5, 0.8]$, $\nmin \in \{2, 3\}$) and can be set once without per-model adjustment.
177	In contrast, the fixed $b$ of \citet{drayson_2025_detection_collapse} spans an order of magnitude across model scales and requires a clean validation set plus grid search costing up to $6{\times}$ the training budget.
178	Our adaptive $\bstar$ eliminates this cost entirely.
179	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "1b3f5226-8573-4ff6-aa45-2ca612f790ab"
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
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/method.tex",
  "usage": {
    "total_tokens": 14244,
    "tool_uses": 4,
    "duration_ms": 3931
  },
  "last_tool_name": "Read",
  "uuid": "5b859235-2f73-4ac3-83b8-5fd4ad701a92",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01KW6wJHpjVkVHR53AJ4E5dL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "2adf7554-74c4-49e5-b2f6-f11f4965ff6e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 45 · 2026-05-16T01:00:20.553Z_

<details><summary>↩ Tool result · `toolu_01KW6wJHpjVkVHR53AJ4E5dL`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Setup}
5	\label{sec:setup}
6	
7	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
8	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown---a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng_2025_contamination_survey}.
9	
10	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
11	Following \citet{drayson_2025_detection_collapse}, we weight each sample as
12	\begin{equation}
13	  w(x) = (1 - q(x))^{b},
14	  \label{eq:weight}
15	\end{equation}
16	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
17	\citet{drayson_2025_detection_collapse} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
18	We instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.
19	
20	\subsection{Dual-Constraint Framework}
21	\label{sec:dual}
22	
23	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
24	
25	\paragraph{Effective real proportion.}
26	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
27	The \emph{effective real proportion}
28	\begin{equation}
29	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
30	  \label{eq:alpha}
31	\end{equation}
32	measures the share of total weight allocated to likely-real samples.
33	At $b = 0$, $\alpha_{\mathrm{eff}}$ equals the raw real fraction in the batch; increasing $b$ shifts weight toward low-$q$ samples, raising $\alpha_{\mathrm{eff}}$.
34	
35	\paragraph{Effective sample size.}
36	Kish's effective sample size~\citep{vehtari_2024_psis}
37	\begin{equation}
38	  \mathrm{ESS}(b) = \frac{\bigl(\sum_{i=1}^{B} w_i(b)\bigr)^{2}}{\sum_{i=1}^{B} w_i(b)^{2}}
39	  \label{eq:ess}
40	\end{equation}
41	quantifies how many equally-weighted samples the weighted batch is equivalent to.
42	$\mathrm{ESS}(0) = B$; as $b$ grows, a few high-$(1{-}q)$ samples dominate and $\mathrm{ESS}$ drops toward~1.
43	
44	\paragraph{Monotonicity.}
45	The two diagnostics exhibit opposing monotonicity in $b$:
46	
47	\begin{proposition}
48	\label{prop:monotone}
49	For any batch containing both real and synthetic samples with distinct $q$-values, $\alpha_{\mathrm{eff}}(b)$ is strictly increasing in $b$.
50	\end{proposition}
51	
52	\begin{proof}[Proof sketch]
53	Let $\pi_i(b) = w_i / \sum_j w_j$ denote normalized weights.
54	Differentiating $\alpha_{\mathrm{eff}} = \sum_i \pi_i r_i$ yields
55	$\frac{d\alpha_{\mathrm{eff}}}{db} = \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr)$.
56	Real samples ($r_i = 1$) have $q_i \leq 0.5$ and thus higher $\ln(1{-}q_i)$, so this covariance is non-negative for any detector with better-than-random discrimination.
57	Full derivation in Appendix~\ref{app:proofs}.
58	\end{proof}
59	
60	\noindent $\mathrm{ESS}(b)$ is monotonically decreasing in $b$---larger exponents concentrate the weight distribution, a standard property of exponential tilting~\citep{kimura_2024_iw_survey}.
61	
62	\paragraph{Dual constraints.}
63	We impose two requirements on $b$:
64	\begin{enumerate}[nosep,leftmargin=*]
65	  \item \textbf{Quality floor}: $\alpha_{\mathrm{eff}}(b) \geq \tau$.
66	  Convergence under contaminated training improves with the effective real fraction~\citep{wang_2026_survive_contamination}; $\tau$ sets the minimum acceptable quality level.
67	  By Proposition~\ref{prop:monotone}, this constraint defines a \emph{lower bound} $b_\tau = \inf\{b \geq 0 : \alpha_{\mathrm{eff}}(b) \geq \tau\}$.
68	  \item \textbf{Stability ceiling}: $\mathrm{ESS}(b) \geq n_{\min}$.
69	  Overly concentrated weights yield high-variance gradients; $n_{\min}$ prevents the batch from degenerating into a single effective sample.
70	  Since $\mathrm{ESS}$ is decreasing, this defines an \emph{upper bound} $b_{\mathrm{ESS}} = \sup\{b \geq 0 : \mathrm{ESS}(b) \geq n_{\min}\}$.
71	\end{enumerate}
72	The optimal exponent is
73	\begin{equation}
74	  b^{*} = \inf\bigl\{b \geq 0 : \alpha_{\mathrm{eff}}(b) \geq \tau\bigr\} \;\;\text{s.t.}\;\; \mathrm{ESS}(b) \geq n_{\min}.
75	  \label{eq:bstar}
76	\end{equation}
77	This is the \emph{minimum intervention principle}: apply the smallest $b$ that achieves the quality floor.
78	Borderline samples---those with moderate $q$-values---still carry useful training signal; over-downweighting discards this signal unnecessarily.
79	When both constraints are satisfiable ($b_\tau \leq b_{\mathrm{ESS}}$), $b^{*} = b_\tau$ and $\alpha_{\mathrm{eff}}$ is the binding constraint---$b^{*}$ lies well below the ESS ceiling.
80	When they conflict ($b_\tau > b_{\mathrm{ESS}}$), the stability ceiling takes precedence: $b^{*} = b_{\mathrm{ESS}}$, accepting a lower $\alpha_{\mathrm{eff}}$ to preserve gradient stability.
81	Figure~\ref{fig:dual_constraint} illustrates the feasible region and the three regimes.
82	
83	\subsection{Algorithm}
84	\label{sec:algorithm}
85	
86	Algorithm~\ref{alg:bstar} computes $b^{*}$ for each training batch via bisection on the monotone functions $\alpha_{\mathrm{eff}}$ and $\mathrm{ESS}$.
87	Each batch falls into one of three regimes:
88	\begin{enumerate}[nosep,leftmargin=*]
89	  \item \textbf{Clean} ($\alpha_{\mathrm{eff}}(0) \geq \tau$): the quality floor holds at $b = 0$; no reweighting needed.
90	  \item \textbf{$\alpha_{\mathrm{eff}}$-binding} ($b_\tau \leq b_{\mathrm{ESS}}$): the quality constraint determines $b^{*} = b_\tau$; $\mathrm{ESS}$ remains above $n_{\min}$ with margin.
91	  \item \textbf{ESS-binding} ($b_\tau > b_{\mathrm{ESS}}$): the stability ceiling caps $b^{*} = b_{\mathrm{ESS}}$.
92	\end{enumerate}
93	Across 51{,}913 micro-batches in our main experiment ($\rho{=}0.4$, $\tau{=}0.8$, $n_{\min}{=}2$), 49.9\% are clean, 20.2\% are $\alpha_{\mathrm{eff}}$-binding, and 30.0\% are ESS-binding.
94	In $\alpha_{\mathrm{eff}}$-binding batches, the solver selects $b^{*} = 1.67$ on average, while an ESS-only strategy would choose $b = 4.15$ on the same batches---2.5$\times$ more aggressive.
95	The residual $\mathrm{ESS} = 2.60$ in these batches (vs.\ $n_{\min} = 2.0$) confirms that the dual constraint prevents unnecessary over-downweighting.
96	
97	\begin{algorithm}[t]
98	\caption{Per-batch adaptive $b^{*}$ selection}
99	\label{alg:bstar}
100	\begin{algorithmic}[1]
101	\Require Batch scores $\{q_i\}_{i=1}^{B}$, indicators $\{r_i\}$, quality threshold~$\tau$, ESS floor~$n_{\min}$, search bound~$b_{\max}$, tolerance~$\varepsilon$
102	\Ensure Optimal exponent $b^{*}$
103	\If{$\alpha_{\mathrm{eff}}(0) \geq \tau$}
104	  \State \Return $0$ \Comment{clean batch}
105	\EndIf
106	\State $b_\tau \gets \Call{Bisect}{\alpha_{\mathrm{eff}}(\cdot){=}\tau,\; [0, b_{\max}],\; \varepsilon}$
107	\If{$\mathrm{ESS}(b_\tau) \geq n_{\min}$}
108	  \State \Return $b_\tau$ \Comment{$\alpha_{\mathrm{eff}}$-binding}
109	\Else
110	  \State $b_{\mathrm{ESS}} \gets \Call{Bisect}{\mathrm{ESS}(\cdot){=}n_{\min},\; [0, b_{\max}],\; \varepsilon}$
111	  \State \Return $b_{\mathrm{ESS}}$ \Comment{ESS-binding}
112	\EndIf
113	\end{algorithmic}
114	\end{algorithm}
115	
116	\paragraph{Implementation.}
117	Given $b^{*}$, we compute normalized weights $\pi_i = w_i(b^{*}) / \sum_j w_j(b^{*})$ and form the weighted loss $\mathcal{L} = \sum_i \pi_i \ell_i$, where $\ell_i$ is the per-sample cross-entropy.
118	This \emph{loss reweighting} maintains continuous gradients, unlike the SIR resampling of \citet{drayson_2025_detection_collapse} which introduces discrete sampling noise by drawing a subset proportional to $w_i$.
119	Each bisection requires $\mathcal{O}(B \log(b_{\max}/\varepsilon))$ operations---with $B{=}4$, $b_{\max}{=}20$, and $\varepsilon{=}0.01$, roughly 44 floating-point operations per batch, negligible beside the forward and backward passes.
120	
121	\subsection{Hyperparameters}
122	\label{sec:hyperparameters}
123	
124	The framework introduces two hyperparameters, both with principled defaults set once across all experiments.
125	
126	\paragraph{Quality threshold $\tau$.}
127	Convergence theory for contaminated training shows that convergence rate improves with the effective real fraction~\citep{wang_2026_survive_contamination}, motivating a lower bound on $\alpha_{\mathrm{eff}}$.
128	The specific value of $\tau$ is set empirically.
129	We find a wide safe range: $\tau \in [0.5, 0.8]$ consistently outperforms uniform training (Section~\ref{sec:results}), with $\tau = 0.8$ achieving the best perplexity.
130	Above 0.8, $b^{*}$ inflates rapidly (mean $b^{*} = 3.08$ at $\tau = 0.95$), causing over-downweighting.
131	We use $\tau = 0.8$ as the default throughout.
132	
133	\paragraph{ESS floor $n_{\min}$.}
134	We set $n_{\min} = 2$ for batch size $B = 4$.
135	The constraint $n_{\min} < B$ is necessary: $n_{\min} \geq B$ forces $b^{*} = 0$ on every batch, recovering uniform training.
136	At the other extreme, $n_{\min} = 1$ effectively removes the stability constraint---mean $b^{*}$ rises to 7.20, with 46.7\% of batches hitting the search ceiling at $b_{\max}{=}20$, and perplexity degrades by $+0.14$ relative to $n_{\min} = 2$.
137	In practice, $n_{\min} \in \{2, 3\}$ yields stable results across seeds (Section~\ref{sec:results}).
138	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "94b6cb50-251a-4675-a100-4eb260a5ef0b"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/related_work_0b6096.tex",
  "usage": {
    "total_tokens": 14245,
    "tool_uses": 5,
    "duration_ms": 4273
  },
  "last_tool_name": "Read",
  "uuid": "f4bdeb7e-168d-46c4-9acb-4206799a11ec",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01WgYNv1b3kLsgpL15uBPLpA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work_0b6096.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "d1110341-b8a7-48f0-89ab-1abc3a1525b0",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 48 · 2026-05-16T01:00:20.899Z_

<details><summary>↩ Tool result · `toolu_01WgYNv1b3kLsgpL15uBPLpA`</summary>

```text
1	% Related Work for "Minimum Intervention Reweighting: Adaptive Exponent Selection
2	% for Contamination-Aware Pretraining"
3	% Generated: 2026-05-15
4	% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)
5	
6	\section{Related Work}
7	\label{sec:related}
8	
9	\paragraph{Synthetic Contamination and Model Collapse.}
10	Training on recursively generated data leads to irreversible quality degradation---\emph{model collapse} \citep{shumailov2024model}.
11	\cite{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
12	More critically, \cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
13	With synthetic content now estimated at 20--60\% of web corpora \citep{cheng2025contamination}, these results motivate contamination-aware training strategies that explicitly account for data provenance rather than treating all tokens equally.
14	
15	\paragraph{Detect and Reweight.}
16	A natural response to contamination is to detect and remove synthetic content.
17	DetectGPT \citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\% Prob \citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\% tokens as a reference-free signal; both produce continuous confidence scores suitable as input to reweighting frameworks.
18	\cite{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples; \cite{guo2025escaping} similarly rely on verification-based selection.
19	Soft reweighting avoids the precision--recall threshold inherent in hard filtering by assigning continuous weights.
20	
21	Most directly related to our work, \cite{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is a detector's synthetic probability.
22	We adopt the same weighting formula but differ in several fundamental ways.
23	\textbf{(i)}~Drayson et al.\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B), making the choice per-model and expensive.
24	Our $\bstar$ is derived per-batch from dual constraints ($\aeff \geq \tau$, $\mathrm{ESS} \geq \nmin$) at zero validation cost, following a minimum intervention principle that selects the smallest sufficient exponent.
25	\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradient contributions.
26	\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\,=\,0.986) on WikiText-2 (${\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\,=\,0.939) suffices on FineWeb-scale data (132M+ tokens).
27	
28	\paragraph{Data Mixing and Reweighting.}
29	A parallel line of work optimizes data composition without targeting synthetic contamination.
30	At the \emph{domain} level, DoReMi \citep{xie2023doremi} learns mixture weights via Group DRO with a proxy model, DSIR \citep{xie2023dsir} performs importance resampling with $n$-gram features, \cite{ye2025mixing} discover predictable functional forms relating mixing ratios to performance, and AIOLI \citep{chen2025aioli} unifies these into an online adaptive framework.
31	These methods operate at the domain level and do not address instance-level contamination within a domain.
32	At the \emph{instance} level, SoftDedup \citep{he2024softdedup} downweights high-frequency samples via $n$-gram commonness, and \cite{sow2025dynamic} derive sample weights from per-sample loss with convergence guarantees.
33	Our reweighting differs from all of these in being driven by \emph{provenance}---detector scores estimating human vs.\ machine origin---rather than loss, frequency, or domain membership.
34	
35	\paragraph{Theoretical Foundations.}
36	\cite{he2025golden} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\approx}0.62$) optimal when both sources are equally sized; their result requires the contamination ratio, unavailable in web-scale settings.
37	\cite{wang2026survive} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\aeff(b) \geq \tau$ guarantees a convergence-rate lower bound.
38	We operationalize this without the known-proportion assumption, estimating $\aeff$ from batch-level statistics online.
39	For the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \cite{vehtari2024psis}.
40	\cite{kimura2024iw} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as covariate-shift correction where the covariate is synthetic origin probability.
41	
42	\smallskip
43	\noindent\textbf{Summary.}
44	No existing method provides principled per-batch exponent selection without validation.
45	Drayson et al.\ use the same $w{=}(1{-}q)^b$ formula but require per-model grid search; Golden Ratio weighting requires known mixture proportions; DoReMi and DSIR operate at the domain level rather than instance-level contamination.
46	Our dual-constraint framework fills this gap by deriving the minimum intervention $\bstar$ from batch-level diagnostics alone.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "a910507f-501e-4059-b2e8-46f3f61d48ac"
}
```

</details>

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/related_work.tex",
  "usage": {
    "total_tokens": 14246,
    "tool_uses": 6,
    "duration_ms": 5185
  },
  "last_tool_name": "Read",
  "uuid": "dd68e921-1266-431e-a1cd-d4372752dd74",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_01XJHZtN2SjxqG2RCE869Eum`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "7df157b4-7fd6-4348-a484-77dc44a4af13",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 51 · 2026-05-16T01:00:21.808Z_

<details><summary>↩ Tool result · `toolu_01XJHZtN2SjxqG2RCE869Eum`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Synthetic Contamination and Model Collapse.}
4	Training on recursively generated data leads to irreversible quality degradation---\emph{model collapse}~\citep{shumailov_2024_model_collapse}.
5	\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
6	More critically, \citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
7	\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	These results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\% Prob~\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\% tokens as a reference-free signal.
13	Both produce continuous confidence scores suitable as input to downstream weighting---including ours.
14	On the mitigation side, \citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.
15	\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.
16	Hard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.
17	
18	Most directly related to our work, \citet{drayson_2025_detection_collapse} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic probability.
19	We adopt the same weighting formula but differ in several fundamental ways.
20	\textbf{(i)}~Drayson et al.\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\leq}360$M, $b{=}1$ for 1.7B), making the choice \emph{per-model} and expensive.
21	Our $b^*$ is derived per-batch from dual constraints ($\alpha_{\mathrm{eff}} \geq \tau$, $\mathrm{ESS} \geq n_{\min}$) at zero validation cost.
22	\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradients.
23	\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\,=\,0.986) on WikiText-2 (${\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\,=\,0.939) suffices on FineWeb-scale data (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.
24	
25	\paragraph{Data Mixing and Instance-Level Reweighting.}
26	A parallel line of work optimizes data composition without targeting synthetic contamination.
27	At the \emph{domain} level, DoReMi~\citep{xie_2023_doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\citep{xie_2023_dsir} performs importance resampling with $n$-gram features, and \citet{ye_2025_data_mixing_laws} discover predictable functional forms relating mixing ratios to performance.
28	AIOLI~\citep{chen_2025_aioli} unifies these into an online adaptive framework, while \citet{yang_2026_data_mixing_agent} train an RL agent for domain-weight selection.
29	These methods do not address instance-level contamination within a domain.
30	At the \emph{instance} level, SoftDedup~\citep{he_2024_softdedup} downweights high-frequency samples via $n$-gram commonness, \citet{sow_2025_dynamic_reweighting} derive sample weights from per-sample loss with convergence guarantees, and \citet{kuo_2024_data_weighting} show that differentiated weighting of LLM-generated data improves downstream classification.
31	Our reweighting differs from all of these in being driven by \emph{provenance}---detector scores estimating human vs.\ synthetic origin---rather than loss, frequency, or domain membership.
32	
33	\paragraph{Theoretical Foundations.}
34	\citet{he_2025_golden_ratio} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\approx}0.62$) optimal when both sources are equally sized.
35	Their result requires the contamination ratio $k$, unavailable in web-scale settings; we use it as an oracle baseline.
36	\citet{wang_2026_survive_contamination} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\alpha_{\mathrm{eff}}(b) \geq \tau$ guarantees a convergence-rate lower bound.
37	We operationalize this without the known-proportion assumption, estimating $\alpha_{\mathrm{eff}}$ from batch-level statistics online.
38	For the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \citet{vehtari_2024_psis}.
39	\citet{kimura_2024_iw_survey} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as a special case of covariate-shift correction where the covariate is synthetic origin probability.
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "2d83efb6-b6de-4994-8ddb-bbd6bfe4ee1c"
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/experiments_86dfd1.tex",
  "usage": {
    "total_tokens": 14247,
    "tool_uses": 7,
    "duration_ms": 5437
  },
  "last_tool_name": "Read",
  "uuid": "a4d9174f-09fc-422e-b38b-3975345a408b",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_01VspCT9BtiAwioVGHPg1qv2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/experiments_86dfd1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "73db9f43-dcc3-49e4-b6c2-c715eedb656c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 54 · 2026-05-16T01:00:22.057Z_

<details><summary>↩ Tool result · `toolu_01VspCT9BtiAwioVGHPg1qv2`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\paragraph{Training Data.}
5	We sample a 132M-token subset of FineWeb~\citep{penedo_2024_fineweb} as the real-data source.
6	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang_2025_qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\rho = 0.4$ via uniform random mixing.
7	This self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.
8	
9	\paragraph{Detector.}
10	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\,=\,0.939 with calibrated ECE\,=\,0.048 after temperature scaling ($T = 0.204$).
11	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
12	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson_2025_detection_collapse}) to test whether score \emph{calibration} matters more than raw discrimination for reweighting.
13	
14	\paragraph{Training.}
15	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
16	All main comparisons use three random seeds (42, 123, 456).
17	
18	\paragraph{Evaluation.}
19	We report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).
20	All evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.
21	
22	\paragraph{Methods.}
23	We compare five approaches:
24	\begin{itemize}[nosep,leftmargin=*]
25	  \item \textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).
26	  \item \textbf{Grid-$b$}: fixed $b \in \{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\}$, best selected post-hoc by held-out PPL.
27	        Represents validation-based selection~\citep{drayson_2025_detection_collapse}.
28	  \item \textbf{ESS-only}: $b^* = \max\{b : \mathrm{ESS}(b) \geq n_{\min}\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\alpha_{\mathrm{eff}}$.
29	  \item \textbf{Golden Ratio}: $w = 1/\varphi \approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\citep{he_2025_golden_ratio}.
30	        Requires known provenance labels (oracle).
31	  \item \textbf{Adaptive} (ours): per-batch $b^*$ from the dual-constraint formulation (\S\ref{sec:method}), with $\tau = 0.8$ and $n_{\min} = 2$ (half the micro-batch size).
32	\end{itemize}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "9cef5b6a-b61a-450b-a981-37cf624ac6c8"
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/experiments.tex",
  "usage": {
    "total_tokens": 14248,
    "tool_uses": 8,
    "duration_ms": 5833
  },
  "last_tool_name": "Read",
  "uuid": "a0ae70e0-4219-406b-81ce-98aff0ba4559",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Read · `toolu_01DrWHu6bUPiwkkXdL1y5noU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "24faacef-ac87-4a13-804d-7ed71467e276",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 57 · 2026-05-16T01:00:22.459Z_

<details><summary>↩ Tool result · `toolu_01DrWHu6bUPiwkkXdL1y5noU`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\paragraph{Training Data.}
5	We sample a 132M-token subset of FineWeb~\citep{penedo_2024_fineweb} as the real-data source.
6	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang_2025_qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\rho = 0.4$ via uniform random mixing.
7	This self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.
8	
9	\paragraph{Detector.}
10	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\,=\,0.939 with calibrated ECE\,=\,0.048 after temperature scaling ($T = 0.204$).
11	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
12	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson_2025_detection_collapse}) to test whether score \emph{calibration} matters more than raw discrimination for reweighting.
13	
14	\paragraph{Training.}
15	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
16	All main comparisons use three random seeds (42, 123, 456).
17	
18	\paragraph{Evaluation.}
19	We report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).
20	All evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.
21	
22	\paragraph{Methods.}
23	We compare five approaches:
24	\begin{itemize}[nosep,leftmargin=*]
25	  \item \textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).
26	  \item \textbf{Grid-$b$}: fixed $b \in \{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\}$, best selected post-hoc by held-out PPL.
27	        Represents validation-based selection~\citep{drayson_2025_detection_collapse}.
28	  \item \textbf{ESS-only}: $b^* = \max\{b : \mathrm{ESS}(b) \geq n_{\min}\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\alpha_{\mathrm{eff}}$.
29	  \item \textbf{Golden Ratio}: $w = 1/\varphi \approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\citep{he_2025_golden_ratio}.
30	        Requires known provenance labels (oracle).
31	  \item \textbf{Adaptive} (ours): per-batch $b^*$ from the dual-constraint formulation (\S\ref{sec:method}), with $\tau = 0.8$ and $n_{\min} = 2$ (half the micro-batch size).
32	\end{itemize}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "34c4bfe3-440e-4bb9-aa1b-a41da68d1f39"
}
```

</details>

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/results_d0d647.tex",
  "usage": {
    "total_tokens": 14249,
    "tool_uses": 9,
    "duration_ms": 6199
  },
  "last_tool_name": "Read",
  "uuid": "86b4fba7-0467-42bf-aca6-5a39bb4f3156",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_01Tf6HjGxVuxzj9LU6ddBPA8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/results_d0d647.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "27cdf567-bb55-464e-8e0f-8be98841ae0e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 60 · 2026-05-16T01:00:22.826Z_

<details><summary>↩ Tool result · `toolu_01Tf6HjGxVuxzj9LU6ddBPA8`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Main Comparison}
5	
6	Table~\ref{tab:main} reports held-out perplexity across methods and seeds.
7	Adaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).
8	This parity comes at zero validation cost---grid search requires $|\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.
9	
10	The grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\ref{app:grid}), confirming that exponent selection is consequential.
11	The optimal $b{=}0.5$ differs from the $b{=}10$ reported by \citet{drayson_2025_detection_collapse} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.
12	
13	% Claim 1: Dual > ESS-only (3 seeds)
14	ESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \emph{worse} than uniform (17.694) by 0.029.
15	The degradation is consistent: ESS-only exceeds uniform on every individual seed (Table~\ref{tab:main}), ruling out seed-specific artifacts.
16	Removing $\alpha_{\mathrm{eff}}$ and maximizing $b$ subject only to $\mathrm{ESS} \geq n_{\min}$ leads to systematic over-downweighting, providing direct evidence for the minimum-intervention principle.
17	Conversely, adaptive (dual) improves over uniform on all three seeds (by 0.041, 0.043, and 0.045 respectively), confirming that the $\alpha_{\mathrm{eff}}$ quality floor prevents the over-intervention that plagues ESS-only.
18	
19	The Golden Ratio oracle~\citep{he_2025_golden_ratio} achieves PPL 17.654 on seed 42 using known provenance labels.
20	Adaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.
21	
22	The adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.
23	The constraint regime breakdown in \S\ref{sec:algorithm} shows that $\alpha_{\mathrm{eff}}$ prevents over-intervention in the 40\% of reweighted batches where moderate $b$ already meets the quality target.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\begin{tabular}{@{}lcccc@{}}
29	\toprule
30	\textbf{Method} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} \\
31	\midrule
32	Uniform               & 17.694 & 17.686 & 17.702 & 17.694 \\
33	Grid-best ($b{=}0.5$) & \textbf{17.651} & \textbf{17.638} & \textbf{17.650} & \textbf{17.646} \\
34	ESS-only               & 17.730 & 17.720 & 17.719 & 17.723 \\
35	Golden Ratio$^\dagger$ & 17.654 & --     & --     & --     \\
36	\midrule
37	Adaptive (ours)        & 17.653 & 17.643 & 17.657 & 17.651 \\
38	\bottomrule
39	\end{tabular}
40	\caption{Held-out perplexity (PPL, $\downarrow$).
41	Grid-best selects the optimal fixed $b$ post-hoc from six candidates.
42	$^\dagger$Evaluated on seed 42 only.
43	Best per column in \textbf{bold}.}
44	\label{tab:main}
45	\end{table}
46	
47	\subsection{Sensitivity Analysis}
48	
49	\paragraph{Quality threshold $\tau$.}
50	Table~\ref{tab:tau} varies $\tau$ while holding $n_{\min} = 2$ (seed 42).
51	All values in $\tau \in [0.5, 0.8]$ improve over uniform, with $\tau = 0.8$ achieving the lowest PPL (17.653).
52	Higher $\tau$ demands greater $\alpha_{\mathrm{eff}}$, forcing the solver to increase $b^*$: mean $\bar{b}^*$ rises monotonically from 0.39 at $\tau{=}0.5$ to 3.08 at $\tau{=}0.95$.
53	Below 0.8, reweighting is too gentle to fully exploit the detector signal; above, $b^*$ inflates past diminishing returns and PPL degrades.
54	The range $[0.5, 0.8]$ provides a wide safe operating region, with $\tau = 0.8$ as the recommended default.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\begin{tabular}{@{}cccc@{}}
60	\toprule
61	$\tau$ & \textbf{PPL} & $\Delta_{\mathrm{unif}}$ & $\bar{b}^*$ \\
62	\midrule
63	0.50 & 17.688 & $-$0.006 & 0.39 \\
64	0.60 & 17.681 & $-$0.013 & 0.59 \\
65	0.70 & 17.679 & $-$0.015 & 0.89 \\
66	\textbf{0.80} & \textbf{17.653} & $\mathbf{-0.041}$ & \textbf{1.40} \\
67	0.90 & 17.712 & $+$0.018 & 2.36 \\
68	0.95 & 17.723 & $+$0.029 & 3.08 \\
69	\bottomrule
70	\end{tabular}
71	\caption{Sensitivity to $\tau$ (seed 42, $n_{\min}{=}2$, $\rho{=}0.4$).
72	$\Delta_{\mathrm{unif}}$: PPL change vs.\ uniform baseline (17.694).
73	$\bar{b}^*$: mean adaptive exponent across batches.}
74	\label{tab:tau}
75	\end{table}
76	
77	\paragraph{Minimum ESS $n_{\min}$.}
78	Table~\ref{tab:nmin} ablates $n_{\min}$ at batch size $B{=}4$.
79	Removing the ESS floor ($n_{\min} = 1$) allows $b^*$ to inflate to mean 7.20, degrading PPL to 17.789---0.095 worse than uniform.
80	At $n_{\min} = 2$ ($= \lfloor B/2 \rfloor$), $b^*$ is constrained to mean 1.40 and PPL reaches 17.653, verified across three seeds.
81	At $n_{\min} = B = 4$, the ESS constraint is trivially satisfied at $b^* = 0$ for every batch, and PPL reverts to the uniform level (17.695 vs.\ 17.694).
82	The results exhibit a U-shaped pattern: too-low $n_{\min}$ permits over-downweighting, while $n_{\min}$ at or near $B$ removes the ability to reweight.
83	
84	The coupling between $n_{\min}$ and $B$ extends beyond the $B{=}4$ setting.
85	At batch size $B{=}8$ with $n_{\min}{=}2$, the ESS range $[2, 8]$ is wide enough that the stability constraint rarely binds, yielding PPL 17.73---comparable to ESS-only and 0.036 worse than uniform.
86	This confirms that $n_{\min}$ must scale with $B$: a fixed $n_{\min}$ that works for one batch size can degrade to near-ESS-only behavior at larger $B$.
87	The rule $n_{\min} = \max(2, \lfloor B/2 \rfloor)$ keeps the ESS constraint active without over-restricting the solver, and we recommend it as a practical default.
88	
89	\begin{table}[t]
90	\centering
91	\small
92	\begin{tabular}{@{}ccc@{}}
93	\toprule
94	$n_{\min}$ & \textbf{PPL} & $\bar{b}^*$ \\
95	\midrule
96	1 & 17.789 & 7.20 \\
97	\textbf{2} & \textbf{17.653} & \textbf{1.40} \\
98	3$^\ddagger$ & 17.644 & 1.43 \\
99	4 & 17.695 & 0.00 \\
100	\bottomrule
101	\end{tabular}
102	\caption{Sensitivity to $n_{\min}$ (seed 42, $B{=}4$, $\tau{=}0.8$).
103	$n_{\min} = 4 = B$ forces $b^* = 0$ on all batches, recovering uniform weighting.
104	$^\ddagger$From an earlier adaptive configuration; not an independent ablation.}
105	\label{tab:nmin}
106	\end{table}
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "929ac12e-d393-4551-a77c-020836028467"
}
```

</details>

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/results.tex",
  "usage": {
    "total_tokens": 14250,
    "tool_uses": 10,
    "duration_ms": 6583
  },
  "last_tool_name": "Read",
  "uuid": "6ac202c9-a378-4849-bf1a-eb9d3932a7f5",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_01BNLDWKCDZBgYAFqTQQR5Xt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "261facf5-c4de-40ad-9ce7-cef2e1059de4",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 63 · 2026-05-16T01:00:23.205Z_

<details><summary>↩ Tool result · `toolu_01BNLDWKCDZBgYAFqTQQR5Xt`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Main Comparison}
5	
6	Table~\ref{tab:main} reports held-out perplexity across methods and seeds.
7	Adaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).
8	This parity comes at zero validation cost---grid search requires $|\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.
9	
10	The grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\ref{app:grid}), confirming that exponent selection is consequential.
11	The optimal $b{=}0.5$ differs from the $b{=}10$ reported by \citet{drayson_2025_detection_collapse} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.
12	
13	% Claim 1: Dual > ESS-only (3 seeds)
14	ESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \emph{worse} than uniform (17.694) by 0.029.
15	The degradation is consistent: ESS-only exceeds uniform on every individual seed (Table~\ref{tab:main}), ruling out seed-specific artifacts.
16	Removing $\alpha_{\mathrm{eff}}$ and maximizing $b$ subject only to $\mathrm{ESS} \geq n_{\min}$ leads to systematic over-downweighting, providing direct evidence for the minimum-intervention principle.
17	Conversely, adaptive (dual) improves over uniform on all three seeds (by 0.041, 0.043, and 0.045 respectively), confirming that the $\alpha_{\mathrm{eff}}$ quality floor prevents the over-intervention that plagues ESS-only.
18	
19	The Golden Ratio oracle~\citep{he_2025_golden_ratio} achieves PPL 17.654 on seed 42 using known provenance labels.
20	Adaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.
21	
22	The adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.
23	The constraint regime breakdown in \S\ref{sec:algorithm} shows that $\alpha_{\mathrm{eff}}$ prevents over-intervention in the 40\% of reweighted batches where moderate $b$ already meets the quality target.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\begin{tabular}{@{}lcccc@{}}
29	\toprule
30	\textbf{Method} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} \\
31	\midrule
32	Uniform               & 17.694 & 17.686 & 17.702 & 17.694 \\
33	Grid-best ($b{=}0.5$) & \textbf{17.651} & \textbf{17.638} & \textbf{17.650} & \textbf{17.646} \\
34	ESS-only               & 17.730 & 17.720 & 17.719 & 17.723 \\
35	Golden Ratio$^\dagger$ & 17.654 & --     & --     & --     \\
36	\midrule
37	Adaptive (ours)        & 17.653 & 17.643 & 17.657 & 17.651 \\
38	\bottomrule
39	\end{tabular}
40	\caption{Held-out perplexity (PPL, $\downarrow$).
41	Grid-best selects the optimal fixed $b$ post-hoc from six candidates.
42	$^\dagger$Evaluated on seed 42 only.
43	Best per column in \textbf{bold}.}
44	\label{tab:main}
45	\end{table}
46	
47	\subsection{Sensitivity Analysis}
48	
49	\paragraph{Quality threshold $\tau$.}
50	Table~\ref{tab:tau} varies $\tau$ while holding $n_{\min} = 2$ (seed 42).
51	All values in $\tau \in [0.5, 0.8]$ improve over uniform, with $\tau = 0.8$ achieving the lowest PPL (17.653).
52	Higher $\tau$ demands greater $\alpha_{\mathrm{eff}}$, forcing the solver to increase $b^*$: mean $\bar{b}^*$ rises monotonically from 0.39 at $\tau{=}0.5$ to 3.08 at $\tau{=}0.95$.
53	Below 0.8, reweighting is too gentle to fully exploit the detector signal; above, $b^*$ inflates past diminishing returns and PPL degrades.
54	The range $[0.5, 0.8]$ provides a wide safe operating region, with $\tau = 0.8$ as the recommended default.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\begin{tabular}{@{}cccc@{}}
60	\toprule
61	$\tau$ & \textbf{PPL} & $\Delta_{\mathrm{unif}}$ & $\bar{b}^*$ \\
62	\midrule
63	0.50 & 17.688 & $-$0.006 & 0.39 \\
64	0.60 & 17.681 & $-$0.013 & 0.59 \\
65	0.70 & 17.679 & $-$0.015 & 0.89 \\
66	\textbf{0.80} & \textbf{17.653} & $\mathbf{-0.041}$ & \textbf{1.40} \\
67	0.90 & 17.712 & $+$0.018 & 2.36 \\
68	0.95 & 17.723 & $+$0.029 & 3.08 \\
69	\bottomrule
70	\end{tabular}
71	\caption{Sensitivity to $\tau$ (seed 42, $n_{\min}{=}2$, $\rho{=}0.4$).
72	$\Delta_{\mathrm{unif}}$: PPL change vs.\ uniform baseline (17.694).
73	$\bar{b}^*$: mean adaptive exponent across batches.}
74	\label{tab:tau}
75	\end{table}
76	
77	\paragraph{Minimum ESS $n_{\min}$.}
78	Table~\ref{tab:nmin} ablates $n_{\min}$ at batch size $B{=}4$.
79	Removing the ESS floor ($n_{\min} = 1$) allows $b^*$ to inflate to mean 7.20, degrading PPL to 17.789---0.095 worse than uniform.
80	At $n_{\min} = 2$ ($= \lfloor B/2 \rfloor$), $b^*$ is constrained to mean 1.40 and PPL reaches 17.653, verified across three seeds.
81	At $n_{\min} = B = 4$, the ESS constraint is trivially satisfied at $b^* = 0$ for every batch, and PPL reverts to the uniform level (17.695 vs.\ 17.694).
82	The results exhibit a U-shaped pattern: too-low $n_{\min}$ permits over-downweighting, while $n_{\min}$ at or near $B$ removes the ability to reweight.
83	
84	The coupling between $n_{\min}$ and $B$ extends beyond the $B{=}4$ setting.
85	At batch size $B{=}8$ with $n_{\min}{=}2$, the ESS range $[2, 8]$ is wide enough that the stability constraint rarely binds, yielding PPL 17.73---comparable to ESS-only and 0.036 worse than uniform.
86	This confirms that $n_{\min}$ must scale with $B$: a fixed $n_{\min}$ that works for one batch size can degrade to near-ESS-only behavior at larger $B$.
87	The rule $n_{\min} = \max(2, \lfloor B/2 \rfloor)$ keeps the ESS constraint active without over-restricting the solver, and we recommend it as a practical default.
88	
89	\begin{table}[t]
90	\centering
91	\small
92	\begin{tabular}{@{}ccc@{}}
93	\toprule
94	$n_{\min}$ & \textbf{PPL} & $\bar{b}^*$ \\
95	\midrule
96	1 & 17.789 & 7.20 \\
97	\textbf{2} & \textbf{17.653} & \textbf{1.40} \\
98	3$^\ddagger$ & 17.644 & 1.43 \\
99	4 & 17.695 & 0.00 \\
100	\bottomrule
101	\end{tabular}
102	\caption{Sensitivity to $n_{\min}$ (seed 42, $B{=}4$, $\tau{=}0.8$).
103	$n_{\min} = 4 = B$ forces $b^* = 0$ on all batches, recovering uniform weighting.
104	$^\ddagger$From an earlier adaptive configuration; not an independent ablation.}
105	\label{tab:nmin}
106	\end{table}
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "493fb112-655f-42a3-9f86-39e665c10c67"
}
```

</details>

---

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/discussion_270aaa.tex",
  "usage": {
    "total_tokens": 14251,
    "tool_uses": 11,
    "duration_ms": 7353
  },
  "last_tool_name": "Read",
  "uuid": "0345953a-b69b-4323-b62d-9cb8d8054737",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Read · `toolu_01RJvB9G6cUNjcns2pnLvS3m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/discussion_270aaa.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "5106e3f2-7db1-42bc-a442-73d0c5325ed5",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 66 · 2026-05-16T01:00:23.999Z_

<details><summary>↩ Tool result · `toolu_01RJvB9G6cUNjcns2pnLvS3m`</summary>

```text
1	\paragraph{Why minimum intervention works.}
2	The central finding of our experiments is that restraint in downweighting outperforms aggressiveness.
3	ESS-only reweighting---which maximizes $b$ subject only to $\mathrm{ESS} \geq \nmin$---degrades PPL to 17.723, \emph{worse} than the uniform baseline (17.694, Table~\ref{tab:main}).
4	The dual-constrained adaptive $\bstar$, by contrast, achieves 17.651 by selecting the \emph{smallest} $b$ that meets the quality floor $\tau$.
5	The mechanism is clear from the binding statistics: in the 40.1\% of reweighted batches where $\aeff$ binds, mean $\bstar = 1.67$ versus 4.15 under ESS-only---a 2.5$\times$ less aggressive exponent that retains ESS\,=\,2.60, well above the floor $\nmin = 2$.
6	Over-downweighting discards gradient signal from borderline samples whose detector scores are intermediate (e.g., $q \approx 0.4$--$0.6$); these samples carry partial but non-negligible training value, and aggressively suppressing them impoverishes the effective training distribution.
7	The $\aeff$ constraint prevents this by halting $b$ as soon as the quality target is met.
8	
9	\paragraph{$\tau$ as a practical dial.}
10	The quality threshold $\tau$ controls the trade-off between decontamination strength and sample retention.
11	Our sweep (Table~\ref{tab:tau}) reveals a wide safe operating range: all $\tau \in [0.5, 0.8]$ outperform uniform training, with PPL varying only 0.035 across this interval.
12	The sensitivity is asymmetric---under-cleaning ($\tau < 0.8$) incurs mild degradation ($-$0.006 to $-$0.015 vs.\ uniform), while over-cleaning ($\tau > 0.8$) causes sharper regression as $\bstar$ inflates (mean $\bar{b}^* = 2.36$ at $\tau{=}0.9$, 3.08 at $\tau{=}0.95$).
13	This asymmetry reinforces the minimum intervention intuition: the cost of doing too little is small, whereas the cost of doing too much is steep.
14	We recommend $\tau = 0.8$ as a principled default; practitioners operating at different contamination rates can adjust within the safe range with low risk.
15	
16	\paragraph{Connection to convergence theory.}
17	\citet{wang_2026_survive_contamination} prove that pretraining convergence rate scales with $\alpha$, the effective real data fraction.
18	Our $\tau$ serves an analogous role---setting a floor on the weighted real proportion per batch---but an important distinction must be noted: their analysis assumes a known contamination proportion, whereas our method estimates quality from detector scores without access to the true $\alpha$.
19	We therefore position $\tau$ as an empirical hyperparameter with theoretical motivation: convergence theory explains \emph{why} a quality threshold improves training, while the specific value of $\tau$ is determined empirically.
20	Bridging this gap---deriving $\tau$ from first principles without known proportions---is an open theoretical question.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "8dd45094-6dd3-47fe-90f3-a71aae0c0136"
}
```

</details>

---

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/discussion.tex",
  "usage": {
    "total_tokens": 14252,
    "tool_uses": 12,
    "duration_ms": 7751
  },
  "last_tool_name": "Read",
  "uuid": "c296658e-c850-4527-bb93-8d82f1d49a3e",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_012MLtqZ2kB57hyUDMRv1ZJ8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "a6080848-c057-41da-9ccf-7adb8eeb9296",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 69 · 2026-05-16T01:00:24.373Z_

<details><summary>↩ Tool result · `toolu_012MLtqZ2kB57hyUDMRv1ZJ8`</summary>

```text
1	\paragraph{Why minimum intervention works.}
2	The central finding of our experiments is that restraint in downweighting outperforms aggressiveness.
3	ESS-only reweighting---which maximizes $b$ subject only to $\mathrm{ESS} \geq \nmin$---degrades PPL to 17.723, \emph{worse} than the uniform baseline (17.694, Table~\ref{tab:main}).
4	The dual-constrained adaptive $\bstar$, by contrast, achieves 17.651 by selecting the \emph{smallest} $b$ that meets the quality floor $\tau$.
5	The mechanism is clear from the binding statistics: in the 40.1\% of reweighted batches where $\aeff$ binds, mean $\bstar = 1.67$ versus 4.15 under ESS-only---a 2.5$\times$ less aggressive exponent that retains ESS\,=\,2.60, well above the floor $\nmin = 2$.
6	Over-downweighting discards gradient signal from borderline samples whose detector scores are intermediate (e.g., $q \approx 0.4$--$0.6$); these samples carry partial but non-negligible training value, and aggressively suppressing them impoverishes the effective training distribution.
7	The $\aeff$ constraint prevents this by halting $b$ as soon as the quality target is met.
8	
9	\paragraph{$\tau$ as a practical dial.}
10	The quality threshold $\tau$ controls the trade-off between decontamination strength and sample retention.
11	Our sweep (Table~\ref{tab:tau}) reveals a wide safe operating range: all $\tau \in [0.5, 0.8]$ outperform uniform training, with PPL varying only 0.035 across this interval.
12	The sensitivity is asymmetric---under-cleaning ($\tau < 0.8$) incurs mild degradation ($-$0.006 to $-$0.015 vs.\ uniform), while over-cleaning ($\tau > 0.8$) causes sharper regression as $\bstar$ inflates (mean $\bar{b}^* = 2.36$ at $\tau{=}0.9$, 3.08 at $\tau{=}0.95$).
13	This asymmetry reinforces the minimum intervention intuition: the cost of doing too little is small, whereas the cost of doing too much is steep.
14	We recommend $\tau = 0.8$ as a principled default; practitioners operating at different contamination rates can adjust within the safe range with low risk.
15	
16	\paragraph{Connection to convergence theory.}
17	\citet{wang2026survive} prove that pretraining convergence rate scales with $\alpha$, the effective real data fraction.
18	Our $\tau$ serves an analogous role---setting a floor on the weighted real proportion per batch---but an important distinction must be noted: their analysis assumes a known contamination proportion, whereas our method estimates quality from detector scores without access to the true $\alpha$.
19	We therefore position $\tau$ as an empirical hyperparameter with theoretical motivation: convergence theory explains \emph{why} a quality threshold improves training, while the specific value of $\tau$ is determined empirically.
20	Bridging this gap---deriving $\tau$ from first principles without known proportions---is an open theoretical question.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "76a91867-f890-4cdc-97eb-03434471c5a2"
}
```

</details>

---

### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/conclusion_386ecc.tex",
  "usage": {
    "total_tokens": 14253,
    "tool_uses": 13,
    "duration_ms": 8106
  },
  "last_tool_name": "Read",
  "uuid": "b5d0e989-7326-40b9-b141-904f8ca336c4",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Read · `toolu_01YDYDrkFFMjv54smGkQ534q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/conclusion_386ecc.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "c3112b97-b3bc-420d-9034-eb1155c2bc33",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 72 · 2026-05-16T01:00:24.727Z_

<details><summary>↩ Tool result · `toolu_01YDYDrkFFMjv54smGkQ534q`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced Minimum Intervention Reweighting, a dual-constrained framework for contamination-aware pretraining that selects per-batch exponents $b^*$ without validation data.
5	The method finds the smallest $b$ satisfying $\alpha_{\mathrm{eff}}(b) \geq \tau$ subject to $\mathrm{ESS}(b) \geq n_{\min}$, enforcing a minimum-intervention principle: apply only as much downweighting as needed to meet a quality floor, no more.
6	This stands in direct contrast to ESS-only (maximum-intervention) strategies, which we show degrade performance below even uniform baselines by over-downweighting contaminated samples.
7	
8	Across three seeds at 0.6B scale with 40\% synthetic contamination, adaptive $b^*$ matches grid-search-optimal PPL (17.651 vs.\ 17.646) within seed variance, eliminating the $|\mathcal{B}|$-run grid search entirely.
9	The quality threshold $\tau$ is robust across $[0.5, 0.8]$---all values in this range outperform uniform weighting.
10	A lightweight TF-IDF + logistic regression detector (AUC\,0.94) suffices when post-hoc calibrated (ECE\,0.048); score calibration matters more than raw discriminative power.
11	The batch-level constraint regime---49.9\% clean (no reweighting needed), 20.2\% $\alpha_{\mathrm{eff}}$-binding, 30.0\% ESS-binding---confirms that both constraints are active and complementary in practice.
12	
13	\section*{Limitations}
14	\label{sec:limitations}
15	
16	\paragraph{Scale.}
17	All experiments use a single model size (Qwen3-0.6B) with batch size 4.
18	Batch-level $q$-score statistics concentrate differently at larger batch sizes typical of 3B+ training; the optimal $\tau$ range and constraint dynamics may shift at scale.
19	
20	\paragraph{Contamination distribution.}
21	We inject synthetic data via uniform random mixing at a controlled ratio ($\rho{=}0.4$).
22	Real web-scale contamination is domain-skewed, which may alter within-batch $\alpha_{\mathrm{eff}}$ distributions and require domain-aware extensions.
23	
24	\paragraph{Detector coverage.}
25	We evaluate one detector family (TF-IDF + logistic regression).
26	Although our results suggest calibration dominates discrimination for reweighting quality, a systematic ablation across detector architectures and quality levels is needed.
27	
28	\paragraph{Threshold.}
29	$\tau$ is an empirical hyperparameter.
30	The convergence theory of \citet{wang_2026_survive_contamination} assumes a known contamination proportion $\alpha$, which we do not require; bridging this gap to derive $\tau$ from first principles remains open.
31	
32	\paragraph{Evaluation.}
33	We report held-out perplexity only.
34	Downstream task evaluation (MMLU, HellaSwag) would strengthen the practical case, particularly at scales where PPL differences translate more reliably to task performance.
35	
36	\paragraph{Effect size.}
37	The PPL improvement over uniform weighting is 0.043 at 0.6B/40\% contamination.
38	While consistent across seeds, this effect is modest; we expect amplification at higher contamination ratios and larger model scales, but verification is ongoing.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "65c96155-f104-411c-8654-6c9c37da3b54"
}
```

</details>

---

### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/conclusion.tex",
  "usage": {
    "total_tokens": 14254,
    "tool_uses": 14,
    "duration_ms": 8492
  },
  "last_tool_name": "Read",
  "uuid": "70e0c215-9f32-4488-9bdc-307245467999",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Read · `toolu_01GTkhZtey6cyYes7ZwNQgHE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "b56df28f-109a-4994-94cb-0cfc75a0d06b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 75 · 2026-05-16T01:00:25.111Z_

<details><summary>↩ Tool result · `toolu_01GTkhZtey6cyYes7ZwNQgHE`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced Minimum Intervention Reweighting, a dual-constrained framework for contamination-aware pretraining that selects per-batch exponents $b^*$ without validation data.
5	The method finds the smallest $b$ satisfying $\alpha_{\mathrm{eff}}(b) \geq \tau$ subject to $\mathrm{ESS}(b) \geq n_{\min}$, enforcing a minimum-intervention principle: apply only as much downweighting as needed to meet a quality floor, no more.
6	This stands in direct contrast to ESS-only (maximum-intervention) strategies, which we show degrade performance below even uniform baselines by over-downweighting contaminated samples.
7	
8	Across three seeds at 0.6B scale with 40\% synthetic contamination, adaptive $b^*$ matches grid-search-optimal PPL (17.651 vs.\ 17.646) within seed variance, eliminating the $|\mathcal{B}|$-run grid search entirely.
9	The quality threshold $\tau$ is robust across $[0.5, 0.8]$---all values in this range outperform uniform weighting.
10	A lightweight TF-IDF + logistic regression detector (AUC\,0.94) suffices when post-hoc calibrated (ECE\,0.048); score calibration matters more than raw discriminative power.
11	The batch-level constraint regime---49.9\% clean (no reweighting needed), 20.2\% $\alpha_{\mathrm{eff}}$-binding, 30.0\% ESS-binding---confirms that both constraints are active and complementary in practice.
12	
13	\section*{Limitations}
14	\label{sec:limitations}
15	
16	\paragraph{Scale.}
17	All experiments use a single model size (Qwen3-0.6B) with batch size 4.
18	Batch-level $q$-score statistics concentrate differently at larger batch sizes typical of 3B+ training; the optimal $\tau$ range and constraint dynamics may shift at scale.
19	
20	\paragraph{Contamination distribution.}
21	We inject synthetic data via uniform random mixing at a controlled ratio ($\rho{=}0.4$).
22	Real web-scale contamination is domain-skewed, which may alter within-batch $\alpha_{\mathrm{eff}}$ distributions and require domain-aware extensions.
23	
24	\paragraph{Detector coverage.}
25	We evaluate one detector family (TF-IDF + logistic regression).
26	Although our results suggest calibration dominates discrimination for reweighting quality, a systematic ablation across detector architectures and quality levels is needed.
27	
28	\paragraph{Threshold.}
29	$\tau$ is an empirical hyperparameter.
30	The convergence theory of \citet{wang_2026_survive_contamination} assumes a known contamination proportion $\alpha$, which we do not require; bridging this gap to derive $\tau$ from first principles remains open.
31	
32	\paragraph{Evaluation.}
33	We report held-out perplexity only.
34	Downstream task evaluation (MMLU, HellaSwag) would strengthen the practical case, particularly at scales where PPL differences translate more reliably to task performance.
35	
36	\paragraph{Effect size.}
37	The PPL improvement over uniform weighting is 0.043 at 0.6B/40\% contamination.
38	While consistent across seeds, this effect is modest; we expect amplification at higher contamination ratios and larger model scales, but verification is ongoing.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "e3c91567-e5f7-47ef-a49d-c2289d8b53fb"
}
```

</details>

---

### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "description": "Reading artifacts/_project/paper/table1_main_results.tex",
  "usage": {
    "total_tokens": 14255,
    "tool_uses": 15,
    "duration_ms": 8836
  },
  "last_tool_name": "Read",
  "uuid": "227df2ee-b1e2-42e1-8915-06dd86dc8f3e",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Read · `toolu_01461sbmBxfuWvKreGvhhBq4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/table1_main_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "d0f7b54d-c2e1-401d-9027-e9447871cfe9",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AkfqqTENba4h4b44bxMJL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14236,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14236,
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

_source line 78 · 2026-05-16T01:00:25.467Z_

<details><summary>↩ Tool result · `toolu_01461sbmBxfuWvKreGvhhBq4`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\caption{Held-out perplexity under different weighting methods ($\rho{=}0.4$, 3 seeds). $\Delta$ is relative to the Uniform baseline.}
4	\label{tab:main-results}
5	\small
6	\begin{tabular}{@{}lccccr@{}}
7	\toprule
8	Method & seed42 & seed123 & seed456 & Mean$\pm$Std & $\Delta$ \\
9	\midrule
10	Uniform                                  & 17.694 & 17.686 & 17.702 & 17.694$\pm$0.008 & --- \\
11	Grid-best ($b{=}0.5$)                    & 17.651 & 17.638 & 17.650 & 17.646$\pm$0.007 & $-$0.048 \\
12	Adaptive ($\tau{=}0.8$, $n_{\min}{=}3$\textsuperscript{\dag}) & 17.644 & 17.631 & 17.642 & \textbf{17.639$\pm$0.007} & $-$\textbf{0.055} \\
13	Adaptive-fix ($\tau{=}0.8$, $n_{\min}{=}2$) & 17.653 & 17.643 & 17.657 & 17.651$\pm$0.007 & $-$0.043 \\
14	ESS-only                                 & 17.730 & 17.720 & 17.719 & 17.723$\pm$0.006 & $+$0.029 \\
15	\bottomrule
16	\end{tabular}
17	
18	\vspace{2pt}
19	{\footnotesize \textsuperscript{\dag}$n_{\min}{=}3$ is the original implementation (historical); $n_{\min}{=}2$ is the theoretically derived correction.}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "c37602b9-00ae-4cb0-94ef-3e84ff97d39b"
}
```

</details>

---

### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ac7fd3aa5a6be52f9",
  "tool_use_id": "toolu_01JwscEPDwAWYsvzEyjiYamw",
  "status": "completed",
  "output_file": "",
  "summary": "Read all paper tex files",
  "usage": {
    "total_tokens": 42491,
    "tool_uses": 15,
    "duration_ms": 337180
  },
  "uuid": "15d4e694-ec6e-4866-bf11-069d69423bd7",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557"
}
```

---

### Tool result

_source line 80 · 2026-05-16T01:05:53.804Z_

<details><summary>↩ Tool result · `toolu_01JwscEPDwAWYsvzEyjiYamw`</summary>

````text
&lt;persisted-output>
Output too large (65.8KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/aa969b71-d198-4ba3-9b84-63a2c341d557/tool-results/toolu_01JwscEPDwAWYsvzEyjiYamw.json

Preview (first 2KB):
[
  {
    "type": "text",
    "text": "Here are all 15 files, verbatim:\n\n---\n\n=== introduction_c6a67f.tex ===\n\n```\n% Introduction for \"Minimum Intervention Reweighting: Adaptive Exponent Selection\n% for Contamination-Aware Pretraining\"\n% Generated: 2026-05-15\n% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)\n\n\\section{Introduction}\n\\label{sec:intro}\n\nWeb pretraining corpora are increasingly contaminated by machine-generated text, with recent estimates placing the synthetic fraction between 20\\% and 60\\% \\citep{cheng2025contamination}.\nThis poses a fundamental threat to model quality: \\cite{shumailov2024model} demonstrate that training on recursively generated data leads to irreversible model collapse, and \\cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger degradation, ruling out data scaling as a remedy.\nAs synthetic content becomes ubiquitous, \\emph{contamination-aware training}---strategies that explicitly account for data provenance during optimization---is necessary for maintaining pretraining quality.\n\nA natural mitigation is detect-and-reweight: assign each sample a weight $w(x) = (1 - q(x))^b$ based on a detector's estimated synthetic probability $q(x)$, where larger $b$ downweights suspected synthetic text more aggressively \\citep{drayson2025detection}.\nHowever, the exponent $b$ is a sensitive per-model hyperparameter whose optimal value varies by an order of magnitude across model scales---$b = 1$ for SmolLM-1.7B versus $b = 10$ for GPT-2 124M---and selecting it requires a clean validation set and grid search costing up to $6{\\times}$ the base training budget.\nThe practical question is: \\emph{given per-sample detector scores $q(x)$, how should $b$ be chosen without validation?}\n\nWe propose a \\emph{dual-constraint framework} that derives the exponent adaptively per batch from two diagnostics computed on the detector scores 
...
&lt;/persisted-output>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "1ce904a2-7bf0-4a60-8d9b-1c88e36b26bc",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read all the following tex files from the paper directory and return their FULL contents. This is for a consistency audit of a research paper.\n\nBase path: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/\n\nRead these files (use the latest version where hash variants exist):\n1. introduction_c6a67f.tex (latest intro)\n2. introduction.tex (base intro for comparison)\n3. method_3f5a58.tex (latest method) \n4. method.tex (base method)\n5. related_work_0b6096.tex (latest related work)\n6. related_work.tex (base)\n7. experiments_86dfd1.tex (latest experiments)\n8. experiments.tex (base)\n9. results_d0d647.tex (v2 results)\n10. results.tex (base results)\n11. discussion_270aaa.tex (v2 discussion)\n12. discussion.tex (base discussion)\n13. conclusion_386ecc.tex (latest conclusion)\n14. conclusion.tex (base conclusion)\n15. table1_main_results.tex\n\nFor each file, output: \"=== FILENAME ===\" followed by the full file content. Do NOT summarize — output every line verbatim. This is critical for cross-referencing numbers and symbols.",
    "agentId": "ac7fd3aa5a6be52f9",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are all 15 files, verbatim:\n\n---\n\n=== introduction_c6a67f.tex ===\n\n```\n% Introduction for \"Minimum Intervention Reweighting: Adaptive Exponent Selection\n% for Contamination-Aware Pretraining\"\n% Generated: 2026-05-15\n% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)\n\n\\section{Introduction}\n\\label{sec:intro}\n\nWeb pretraining corpora are increasingly contaminated by machine-generated text, with recent estimates placing the synthetic fraction between 20\\% and 60\\% \\citep{cheng2025contamination}.\nThis poses a fundamental threat to model quality: \\cite{shumailov2024model} demonstrate that training on recursively generated data leads to irreversible model collapse, and \\cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger degradation, ruling out data scaling as a remedy.\nAs synthetic content becomes ubiquitous, \\emph{contamination-aware training}---strategies that explicitly account for data provenance during optimization---is necessary for maintaining pretraining quality.\n\nA natural mitigation is detect-and-reweight: assign each sample a weight $w(x) = (1 - q(x))^b$ based on a detector's estimated synthetic probability $q(x)$, where larger $b$ downweights suspected synthetic text more aggressively \\citep{drayson2025detection}.\nHowever, the exponent $b$ is a sensitive per-model hyperparameter whose optimal value varies by an order of magnitude across model scales---$b = 1$ for SmolLM-1.7B versus $b = 10$ for GPT-2 124M---and selecting it requires a clean validation set and grid search costing up to $6{\\times}$ the base training budget.\nThe practical question is: \\emph{given per-sample detector scores $q(x)$, how should $b$ be chosen without validation?}\n\nWe propose a \\emph{dual-constraint framework} that derives the exponent adaptively per batch from two diagnostics computed on the detector scores alone.\nThe effective real proportion $\\aeff(b)$ measures the weighted fraction of gradient signal from real data and imposes a \\emph{quality floor}: $\\aeff(b) \\geq \\tau$---at least enough cleaning.\nKish's effective sample size $\\mathrm{ESS}(b)$ \\citep{vehtari2024psis} quantifies weight concentration and imposes a \\emph{stability ceiling}: $\\mathrm{ESS}(b) \\geq \\nmin$---not so much cleaning that gradient estimates degrade.\nA key structural insight makes this tractable: $\\aeff$ is strictly increasing in $b$ while $\\mathrm{ESS}$ is strictly decreasing, so the quality constraint yields a unique lower bound $\\btau$ and the stability constraint a unique upper bound $\\bess$.\nWe adopt a \\emph{minimum intervention principle}:\n\\begin{equation*}\n  \\bstar = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\} \\quad \\text{subject to} \\quad \\mathrm{ESS}(\\bstar) \\geq \\nmin,\n\\end{equation*}\nthe smallest exponent satisfying the quality floor.\nThis is deliberately conservative: apply enough decontamination to meet the quality target, but no more, preserving the largest possible effective sample size.\nIn practice, batches fall into three regimes---already clean ($\\bstar{=}0$), quality-binding ($\\bstar{=}\\btau$), and stability-binding ($\\bstar{=}\\bess$)---allowing the framework to handle heterogeneous contamination naturally.\nUnlike the discrete sampling-importance-resampling of \\cite{drayson2025detection}, we implement reweighting through direct loss scaling with continuous gradient contributions.\n\nWe evaluate on continued pretraining of Qwen3-0.6B on 132M FineWeb \\citep{penedo2024fineweb} tokens with 40\\% synthetic contamination (\\S\\ref{sec:experiments}).\nAdaptive $\\bstar$ with default hyperparameters ($\\tau{=}0.8$, $\\nmin{=}2$) matches the grid-search-optimal fixed $b$ within seed variance (PPL $17.650 {\\pm} 0.007$ vs.\\ $17.646 {\\pm} 0.007$ across three seeds) at zero validation cost.\nIt outperforms both uniform training (PPL $17.69$) and ESS-only maximum intervention (PPL $17.73$), confirming that minimum intervention is superior to maximum intervention.\nA lightweight TF-IDF + logistic regression detector (AUC\\,=\\,0.939) suffices for effective reweighting, and the quality threshold $\\tau$ admits a wide safe range of $[0.5, 0.8]$ within which all tested values improve over uniform training.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item A dual-constraint framework for adaptive $\\bstar$ selection with minimum intervention semantics, providing validation-free per-batch exponent derivation from batch-level diagnostics (\\S\\ref{sec:method}).\n  \\item Empirical evidence that adaptive $\\bstar$ matches grid-search-optimal performance within seed variance at zero validation cost, and that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only) (\\S\\ref{sec:results}).\n  \\item Evidence that a lightweight TF-IDF + logistic regression detector suffices for effective reweighting (\\S\\ref{sec:results}).\n\\end{enumerate}\n```\n\n---\n\n=== introduction.tex ===\n\n```\nWeb corpora increasingly contain machine-generated text.\nRecent estimates place the synthetic fraction at 20--60\\% of crawled data~\\citep{cheng_2025_contamination_survey}, and this share grows as language models are deployed for content production at scale.\nTraining on such contaminated data has concrete consequences: \\citet{shumailov_2024_model_collapse} show that recursive training on model outputs leads to irreversible quality degradation---\\emph{model collapse}---and \\citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.\nA central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.\nThe prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.\n\nA natural response is \\emph{detect-and-reweight}: train a classifier to estimate each sample's synthetic probability $q(x)$, then suppress likely-synthetic samples via the weighting function $w(x) = (1 - q(x))^b$.\n\\citet{drayson_2025_detection_collapse} demonstrate this approach for model collapse prevention and show that the exponent $b$ critically determines outcomes---their optimal values range from $b{=}10$ for models at ${\\leq}360$M parameters to $b{=}1$ at 1.7B, and misspecification degrades results substantially.\nSelecting $b$ therefore requires per-model validation-set grid search, with computational cost scaling linearly in the number of candidates (six training runs in a typical sweep).\nOther approaches assume even stronger supervision: \\citet{he_2025_golden_ratio} derive theoretically optimal weights from convergence analysis but require the exact contamination ratio $\\rho$, which is precisely what is unavailable in practice.\nHard detection-and-removal strategies~\\citep{feng_2025_beyond_collapse} discard borderline samples entirely, sacrificing the smooth reweighting that continuous $q$-scores enable.\n\nGiven per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?\nWe formulate this as a dual-constrained optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\\aeff(b)$ reaches a quality threshold $\\tau$, while keeping Kish's effective sample size $\\mathrm{ESS}(b)$ above a stability floor $\\nmin$.\nThe quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effective real-data fraction~\\citep{wang_2026_survive_contamination}, motivating a lower bound on $\\aeff$.\nThe stability constraint prevents extreme weight concentration that degrades gradient quality.\nThese two requirements exhibit a natural opposition.\n$\\aeff(b)$ increases monotonically in $b$ (Proposition~\\ref{prop:monotone}), yielding a lower bound $\\btau$---the minimum exponent needed to achieve the target quality.\n$\\mathrm{ESS}(b)$ decreases monotonically, yielding an upper bound $\\bess$---the maximum exponent before gradient stability degrades.\nThe adaptive exponent $\\bstar = \\btau$ when the feasible region $[\\btau, \\bess]$ is non-empty, embodying a \\emph{minimum intervention principle}: apply the least downweighting sufficient to meet the quality target, preserving as much effective training data as possible.\nWhen the constraints conflict ($\\btau > \\bess$), the stability ceiling takes precedence.\n\nThis minimum-intervention semantics distinguishes the method from the alternative of maximizing $b$ subject only to ESS stability.\nAmong batches that require reweighting, the dual-constraint solver selects $\\bstar$ via the $\\aeff$ bound in 40\\% of cases, with mean $\\bstar{=}1.67$; the ESS-only variant would choose $b{=}4.15$ in these same batches, 2.5$\\times$ more aggressive.\nThe remaining 49.9\\% of batches have sufficient real-data content to skip reweighting entirely ($\\bstar{=}0$).\nThe per-batch $\\bstar$ distribution (median 0.87, mean 1.40) adapts continuously to each batch's contamination composition without any held-out signal.\n\nOn Qwen3-0.6B continued pretraining with 40\\% synthetic contamination (132M+ tokens from FineWeb), adaptive reweighting achieves mean held-out perplexity of 17.651 across three seeds, matching the grid-searched optimum ($b{=}0.5$, mean 17.646) within seed-to-seed variance (\\S\\ref{sec:results}).\nThe grid sweep requires six complete training runs to identify this optimum; the adaptive method requires one.\nThe ESS-only variant (maximum intervention) yields mean PPL 17.722---worse than the uniform baseline (17.694)---confirming that maximum intervention degrades training while minimum intervention improves it.\nA lightweight TF-IDF + Logistic Regression detector (AUC\\,=\\,0.939, calibrated ECE\\,=\\,0.048) suffices throughout, suggesting that score calibration matters more than raw classification accuracy for provenance-based reweighting.\n\nOur contributions:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item A dual-constrained framework for adaptive exponent selection: $\\bstar = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\}$ subject to $\\mathrm{ESS}(b) \\geq \\nmin$, computed per-batch from detector scores with minimum-intervention semantics (\\S\\ref{sec:method}).\n\\item Empirical evidence that adaptive $\\bstar$ matches grid-searched best within seed variance at zero validation cost, and that minimum intervention (dual constraint) outperforms maximum intervention (ESS-only) across three seeds (\\S\\ref{sec:results}).\n\\item A demonstration that a lightweight TF-IDF + LR detector with calibrated $q$-scores supports effective reweighting, achieving results comparable to stronger neural detectors (\\S\\ref{sec:experiments}).\n\\end{itemize}\n```\n\n---\n\n=== method_3f5a58.tex ===\n\n```\n% Method section for \"Minimum Intervention Reweighting\" (EMNLP 2026)\n% Generated: 2026-05-15\n% Based on: paper_framing.md (STABLE, D023/D029/D035)\n% Requires macros: \\bstar, \\aeff, \\nmin, \\btau, \\bess (defined in main.tex preamble)\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\\label{sec:problem-setup}\n\nLet $\\mathcal{D} = \\{x_1, \\ldots, x_N\\}$ denote a pretraining corpus comprising human-written text $\\mathcal{D}_{\\mathrm{real}}$ and machine-generated text $\\mathcal{D}_{\\mathrm{synth}}$, with unknown contamination rate $\\rho = |\\mathcal{D}_{\\mathrm{synth}}| / |\\mathcal{D}|$.\nA pretrained detector assigns each sample a synthetic probability $q(x_i) \\in [0, 1]$.\nFollowing \\citet{drayson_2025_detection_collapse}, we define per-sample weights\n\\begin{equation}\n  w_b(x_i) = (1 - q(x_i))^b, \\quad b \\geq 0,\n  \\label{eq:weight}\n\\end{equation}\nwhere $b = 0$ recovers uniform weighting and increasing $b$ progressively downweights high-$q$ samples.\nThe weighted training objective is\n\\begin{equation}\n  \\mathcal{L}(b) = \\frac{\\sum_{i} w_b(x_i) \\, \\ell(x_i; \\theta)}{\\sum_{j} w_b(x_j)},\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\ell(x_i; \\theta)$ is the per-sample language modeling loss.\n\n\\citet{drayson_2025_detection_collapse} treat $b$ as a hyperparameter selected via validation-based grid search, with reported optima ranging from $b{=}1$ (SmolLM-1.7B) to $b{=}10$ (GPT-2 124M), making per-model tuning unavoidable.\nWe instead derive $b$ adaptively per batch from the detector scores alone, requiring no validation set.\n\n\\subsection{Dual-Constraint Framework}\n\\label{sec:dual-constraint}\n\nHigher $b$ removes more synthetic influence but also discards effective training signal.\nWe formalize this trade-off through two per-batch statistics.\n\n\\paragraph{Effective real proportion.}\nFor a batch $\\mathcal{B} = \\{x_1, \\ldots, x_B\\}$ with weights $w_i(b) = (1 - q_i)^b$, we define\n\\begin{equation}\n  \\aeff(b) = \\frac{\\sum_{i \\in \\mathcal{B}} w_i(b) \\cdot \\mathbf{1}[x_i \\in \\mathcal{D}_{\\mathrm{real}}]}{\\sum_{i \\in \\mathcal{B}} w_i(b)},\n  \\label{eq:alpha_eff}\n\\end{equation}\nmeasuring the effective fraction of real data after reweighting.\nSince true provenance labels are unavailable at training time, we use the detector's hard prediction $\\mathbf{1}[q(x_i) < 0.5]$ as a proxy; all theoretical properties below hold for this approximation.\n\n\\paragraph{Effective sample size.}\nKish's effective sample size \\citep{vehtari_2024_psis} quantifies weight concentration:\n\\begin{equation}\n  \\mathrm{ESS}(b) = \\frac{\\left(\\sum_{i \\in \\mathcal{B}} w_i(b)\\right)^2}{\\sum_{i \\in \\mathcal{B}} w_i^2(b)}.\n  \\label{eq:ess}\n\\end{equation}\n$\\mathrm{ESS}(0) = B$ under uniform weights, decreasing toward $1$ as $b \\to \\infty$ for any batch containing synthetic samples.\n\n\\begin{proposition}[Monotonicity]\n\\label{prop:monotonicity}\nFor any batch containing both real and synthetic samples with non-identical $q$-scores:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item $\\aeff(b)$ is strictly increasing in $b$.\n  \\item $\\mathrm{ESS}(b)$ is strictly decreasing in $b$.\n\\end{enumerate}\n\\end{proposition}\n\n\\begin{proof}[Proof sketch]\nFor (1), differentiating Eq.~\\eqref{eq:alpha_eff} using $\\frac{dw_i}{db} = w_i \\ln(1 {-} q_i)$ yields\n\\begin{equation}\n  \\frac{d\\aeff}{db} = \\aeff(1 {-} \\aeff) \\!\\left( \\mathbb{E}_w[\\ln(1{-}q) \\mid \\mathrm{real}] - \\mathbb{E}_w[\\ln(1{-}q) \\mid \\mathrm{synth}] \\right)\\!,\n  \\label{eq:dalpha}\n\\end{equation}\nwhere $\\mathbb{E}_w$ denotes expectation under the normalized weight distribution.\nSince real samples have lower $q$-scores, $\\ln(1{-}q)$ is strictly less negative for real than synthetic samples, making the parenthesized difference positive.\nFor (2), increasing $b$ multiplies each weight by $(1{-}q_i)^{\\Delta b}$, a factor varying across samples, which concentrates the normalized weight distribution and strictly increases $\\sum_i \\tilde{w}_i^2$, hence decreasing ESS.\nFull proofs appear in Appendix~\\ref{app:proofs}.\n\\end{proof}\n\nProposition~\\ref{prop:monotonicity} establishes that quality and sample efficiency move in opposite directions as $b$ increases, motivating two complementary constraints.\n\n\\paragraph{Quality lower bound.}\nWe require $\\aeff(b) \\geq \\tau$ for a threshold $\\tau \\in (0, 1)$.\nBy strict monotonicity, this defines a unique lower bound\n\\begin{equation}\n  \\btau = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\}\n  \\label{eq:b_tau}\n\\end{equation}\non the exponent---the minimum intervention needed to achieve quality $\\tau$.\n\\citet{wang_2026_survive_contamination} show that pretraining convergence rate scales with effective real data fraction, providing theoretical motivation for maintaining $\\aeff$ above a threshold.\n\n\\paragraph{Stability upper bound.}\nWe require $\\mathrm{ESS}(b) \\geq \\nmin$ for a floor $\\nmin \\geq 1$.\nBy strict monotonicity, this defines a unique upper bound\n\\begin{equation}\n  \\bess = \\sup\\{b \\geq 0 : \\mathrm{ESS}(b) \\geq \\nmin\\}\n  \\label{eq:b_ess}\n\\end{equation}\nbeyond which gradient estimates become unreliable due to weight concentration.\n\n\\paragraph{Minimum intervention principle.}\nWe select\n\\begin{equation}\n  \\bstar = \\begin{cases}\n    0 & \\text{if } \\aeff(0) \\geq \\tau \\\\\n    \\btau & \\text{if } \\btau \\leq \\bess \\\\\n    \\bess & \\text{if } \\btau > \\bess\n  \\end{cases}\n  \\label{eq:bstar}\n\\end{equation}\nyielding three regimes:\n(1)~\\textbf{Already clean} ($\\aeff(0) \\geq \\tau$): the unweighted batch meets quality $\\tau$; set $\\bstar = 0$.\n(2)~\\textbf{$\\aeff$-binding} ($\\btau \\leq \\bess$): the quality constraint determines $\\bstar = \\btau$, applying the \\emph{minimum} intervention to reach $\\tau$, with ESS margin remaining.\n(3)~\\textbf{ESS-binding} ($\\btau > \\bess$): quality $\\tau$ is infeasible under the stability constraint; $\\bstar = \\bess$ applies the maximum stable intervention.\n\nThe key insight is that when the feasible region $[\\btau, \\bess]$ is non-empty, the method selects its \\emph{left} endpoint---downweighting no more than necessary.\nThis contrasts with an ESS-only strategy that selects $\\bess$ (the right endpoint), maximizing cleaning at the cost of discarding useful gradient signal from borderline samples.\nIn our experiments (\\S\\ref{sec:results}), 40.1\\% of reweighted batches are $\\aeff$-binding, where mean $\\bstar = 1.67$ compared to $4.15$ under ESS-only---a $2.5\\times$ less aggressive exponent that retains $\\mathrm{ESS} = 2.60$, well above the floor $\\nmin = 2$.\n\n\\subsection{Algorithm}\n\\label{sec:algorithm}\n\nAlgorithm~\\ref{alg:solver} solves for $\\bstar$ via bisection on $\\aeff$, exploiting monotonicity (Proposition~\\ref{prop:monotonicity}) to guarantee convergence.\n\n\\begin{algorithm}[t]\n\\caption{Per-batch adaptive exponent solver}\n\\label{alg:solver}\n\\begin{algorithmic}[1]\n\\REQUIRE Batch scores $\\{q_1, \\ldots, q_B\\}$, threshold $\\tau$, ESS floor $\\nmin$, tolerance $\\varepsilon$, cap $b_{\\max}$\n\\ENSURE Optimal exponent $\\bstar$\n\\IF{$\\aeff(0) \\geq \\tau$}\n  \\STATE \\textbf{return} $\\bstar = 0$ \\hfill $\\triangleright$ Already clean\n\\ENDIF\n\\STATE $b_{\\mathrm{lo}} \\leftarrow 0,\\; b_{\\mathrm{hi}} \\leftarrow b_{\\max}$ \\hfill $\\triangleright$ Bisect for $\\btau$\n\\WHILE{$b_{\\mathrm{hi}} - b_{\\mathrm{lo}} > \\varepsilon$}\n  \\STATE $b_{\\mathrm{mid}} \\leftarrow (b_{\\mathrm{lo}} + b_{\\mathrm{hi}}) / 2$\n  \\IF{$\\aeff(b_{\\mathrm{mid}}) < \\tau$}\n    \\STATE $b_{\\mathrm{lo}} \\leftarrow b_{\\mathrm{mid}}$\n  \\ELSE\n    \\STATE $b_{\\mathrm{hi}} \\leftarrow b_{\\mathrm{mid}}$\n  \\ENDIF\n\\ENDWHILE\n\\STATE $\\btau \\leftarrow b_{\\mathrm{hi}}$\n\\IF{$\\mathrm{ESS}(\\btau) \\geq \\nmin$}\n  \\STATE \\textbf{return} $\\bstar = \\btau$ \\hfill $\\triangleright$ $\\aeff$-binding\n\\ELSE\n  \\STATE Find $\\bess = \\sup\\{b : \\mathrm{ESS}(b) \\geq \\nmin\\}$ via bisection\n  \\STATE \\textbf{return} $\\bstar = \\bess$ \\hfill $\\triangleright$ ESS-binding\n\\ENDIF\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Implementation.}\nWe apply $\\bstar$ through loss reweighting: each sample's loss is scaled by its normalized weight $\\bar{w}_i = w_{\\bstar}(x_i) / \\sum_j w_{\\bstar}(x_j)$, yielding continuous gradient contributions from all samples including those with intermediate $q$-scores.\nThis contrasts with the sampling-importance-resampling (SIR) approach of \\citet{drayson_2025_detection_collapse}, which discretely resamples a subset of the batch, introducing additional variance and discarding partial information from borderline samples.\n\n\\paragraph{Computational cost.}\nEach evaluation of $\\aeff$ or ESS costs $O(B)$ for batch size $B$.\nBisection requires $O(\\log(b_{\\max} / \\varepsilon))$ iterations, giving total per-batch overhead $O(B \\log(b_{\\max} / \\varepsilon))$---negligible compared to the $O(BHD)$ cost of transformer forward and backward passes with hidden dimension $H$ and depth $D$.\nWith $b_{\\max} = 20$ and $\\varepsilon = 0.01$, this amounts to ${\\sim}11$ iterations per batch.\n\n\\subsection{Hyperparameters}\n\\label{sec:hyperparameters}\n\nThe framework replaces the single sensitive exponent $b$ with two hyperparameters, $\\tau$ and $\\nmin$, both admitting principled defaults that transfer across settings without per-model tuning.\n\n\\paragraph{Quality threshold $\\tau$.}\n\\citet{wang_2026_survive_contamination} establish that pretraining convergence rate scales with effective real data proportion, motivating a quality threshold.\nHowever, their analysis assumes known mixture proportions; since we do not assume known $\\rho$, $\\tau$ is an empirical hyperparameter with theoretical motivation rather than a theoretically derived quantity.\nWe evaluate $\\tau \\in \\{0.5, 0.6, 0.7, 0.8, 0.9, 0.95\\}$ at $\\rho = 0.4$ (\\S\\ref{sec:results}).\nAll values in $[0.5, 0.8]$ improve over uniform training, with PPL spanning only $0.035$ across this range (17.688 at $\\tau{=}0.5$ to 17.653 at $\\tau{=}0.8$).\nWe adopt $\\tau = 0.8$ as the default.\nThe sensitivity is asymmetric: under-cleaning ($\\tau < 0.8$) yields mild degradation, while over-cleaning ($\\tau > 0.8$) causes sharper regression as $\\bstar$ inflates (mean $\\bstar = 2.36$ at $\\tau{=}0.9$ vs.\\ $1.40$ at $\\tau{=}0.8$), excessively suppressing borderline samples whose gradient signal remains useful.\n\n\\paragraph{ESS floor $\\nmin$.}\nThe stability constraint prevents gradient instability from weight concentration.\nAt $\\nmin = 1$ (effectively unconstrained), $\\bstar$ inflates to mean $7.20$ with 46.7\\% of batches exceeding $\\bstar = 2$, yielding PPL~$= 17.789$---worse than uniform ($17.694$) by $+0.095$, confirming that unconstrained downweighting is harmful.\nAt $\\nmin \\geq B$, the constraint forces $\\bstar = 0$ for all batches, recovering uniform training.\nWe use $\\nmin = 2$ (half the batch size for $B = 4$), which yields consistent improvement across three seeds (\\S\\ref{sec:results}).\n\n\\paragraph{Comparison with fixed $b$.}\nBoth $\\tau$ and $\\nmin$ admit wide effective ranges ($\\tau \\in [0.5, 0.8]$, $\\nmin \\in \\{2, 3\\}$) and can be set once without per-model adjustment.\nIn contrast, the fixed $b$ of \\citet{drayson_2025_detection_collapse} spans an order of magnitude across model scales and requires a clean validation set plus grid search costing up to $6{\\times}$ the training budget.\nOur adaptive $\\bstar$ eliminates this cost entirely.\n```\n\n---\n\n=== method.tex ===\n\n```\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\\label{sec:setup}\n\nLet $\\mathcal{D} = \\mathcal{D}_{\\mathrm{real}} \\cup \\mathcal{D}_{\\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.\nThe contamination ratio $\\rho = |\\mathcal{D}_{\\mathrm{synth}}| / |\\mathcal{D}|$ is unknown---a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\\citep{cheng_2025_contamination_survey}.\n\nA pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \\in [0,1]$.\nFollowing \\citet{drayson_2025_detection_collapse}, we weight each sample as\n\\begin{equation}\n  w(x) = (1 - q(x))^{b},\n  \\label{eq:weight}\n\\end{equation}\nwhere $b \\geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.\n\\citet{drayson_2025_detection_collapse} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\\leq}360$M parameters, $b{=}1$ for 1.7B).\nWe instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.\n\n\\subsection{Dual-Constraint Framework}\n\\label{sec:dual}\n\nGiven a batch $\\mathcal{B} = \\{x_1, \\ldots, x_B\\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.\n\n\\paragraph{Effective real proportion.}\nLet $r_i = \\mathbf{1}[q_i \\leq 0.5]$ estimate whether sample $x_i$ is human-authored.\nThe \\emph{effective real proportion}\n\\begin{equation}\n  \\alpha_{\\mathrm{eff}}(b) = \\frac{\\sum_{i=1}^{B} w_i(b) \\cdot r_i}{\\sum_{i=1}^{B} w_i(b)}\n  \\label{eq:alpha}\n\\end{equation}\nmeasures the share of total weight allocated to likely-real samples.\nAt $b = 0$, $\\alpha_{\\mathrm{eff}}$ equals the raw real fraction in the batch; increasing $b$ shifts weight toward low-$q$ samples, raising $\\alpha_{\\mathrm{eff}}$.\n\n\\paragraph{Effective sample size.}\nKish's effective sample size~\\citep{vehtari_2024_psis}\n\\begin{equation}\n  \\mathrm{ESS}(b) = \\frac{\\bigl(\\sum_{i=1}^{B} w_i(b)\\bigr)^{2}}{\\sum_{i=1}^{B} w_i(b)^{2}}\n  \\label{eq:ess}\n\\end{equation}\nquantifies how many equally-weighted samples the weighted batch is equivalent to.\n$\\mathrm{ESS}(0) = B$; as $b$ grows, a few high-$(1{-}q)$ samples dominate and $\\mathrm{ESS}$ drops toward~1.\n\n\\paragraph{Monotonicity.}\nThe two diagnostics exhibit opposing monotonicity in $b$:\n\n\\begin{proposition}\n\\label{prop:monotone}\nFor any batch containing both real and synthetic samples with distinct $q$-values, $\\alpha_{\\mathrm{eff}}(b)$ is strictly increasing in $b$.\n\\end{proposition}\n\n\\begin{proof}[Proof sketch]\nLet $\\pi_i(b) = w_i / \\sum_j w_j$ denote normalized weights.\nDifferentiating $\\alpha_{\\mathrm{eff}} = \\sum_i \\pi_i r_i$ yields\n$\\frac{d\\alpha_{\\mathrm{eff}}}{db} = \\mathrm{Cov}_{\\pi}\\!\\bigl(r_i,\\, \\ln(1{-}q_i)\\bigr)$.\nReal samples ($r_i = 1$) have $q_i \\leq 0.5$ and thus higher $\\ln(1{-}q_i)$, so this covariance is non-negative for any detector with better-than-random discrimination.\nFull derivation in Appendix~\\ref{app:proofs}.\n\\end{proof}\n\n\\noindent $\\mathrm{ESS}(b)$ is monotonically decreasing in $b$---larger exponents concentrate the weight distribution, a standard property of exponential tilting~\\citep{kimura_2024_iw_survey}.\n\n\\paragraph{Dual constraints.}\nWe impose two requirements on $b$:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{Quality floor}: $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$.\n  Convergence under contaminated training improves with the effective real fraction~\\citep{wang_2026_survive_contamination}; $\\tau$ sets the minimum acceptable quality level.\n  By Proposition~\\ref{prop:monotone}, this constraint defines a \\emph{lower bound} $b_\\tau = \\inf\\{b \\geq 0 : \\alpha_{\\mathrm{eff}}(b) \\geq \\tau\\}$.\n  \\item \\textbf{Stability ceiling}: $\\mathrm{ESS}(b) \\geq n_{\\min}$.\n  Overly concentrated weights yield high-variance gradients; $n_{\\min}$ prevents the batch from degenerating into a single effective sample.\n  Since $\\mathrm{ESS}$ is decreasing, this defines an \\emph{upper bound} $b_{\\mathrm{ESS}} = \\sup\\{b \\geq 0 : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$.\n\\end{enumerate}\nThe optimal exponent is\n\\begin{equation}\n  b^{*} = \\inf\\bigl\\{b \\geq 0 : \\alpha_{\\mathrm{eff}}(b) \\geq \\tau\\bigr\\} \\;\\;\\text{s.t.}\\;\\; \\mathrm{ESS}(b) \\geq n_{\\min}.\n  \\label{eq:bstar}\n\\end{equation}\nThis is the \\emph{minimum intervention principle}: apply the smallest $b$ that achieves the quality floor.\nBorderline samples---those with moderate $q$-values---still carry useful training signal; over-downweighting discards this signal unnecessarily.\nWhen both constraints are satisfiable ($b_\\tau \\leq b_{\\mathrm{ESS}}$), $b^{*} = b_\\tau$ and $\\alpha_{\\mathrm{eff}}$ is the binding constraint---$b^{*}$ lies well below the ESS ceiling.\nWhen they conflict ($b_\\tau > b_{\\mathrm{ESS}}$), the stability ceiling takes precedence: $b^{*} = b_{\\mathrm{ESS}}$, accepting a lower $\\alpha_{\\mathrm{eff}}$ to preserve gradient stability.\nFigure~\\ref{fig:dual_constraint} illustrates the feasible region and the three regimes.\n\n\\subsection{Algorithm}\n\\label{sec:algorithm}\n\nAlgorithm~\\ref{alg:bstar} computes $b^{*}$ for each training batch via bisection on the monotone functions $\\alpha_{\\mathrm{eff}}$ and $\\mathrm{ESS}$.\nEach batch falls into one of three regimes:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{Clean} ($\\alpha_{\\mathrm{eff}}(0) \\geq \\tau$): the quality floor holds at $b = 0$; no reweighting needed.\n  \\item \\textbf{$\\alpha_{\\mathrm{eff}}$-binding} ($b_\\tau \\leq b_{\\mathrm{ESS}}$): the quality constraint determines $b^{*} = b_\\tau$; $\\mathrm{ESS}$ remains above $n_{\\min}$ with margin.\n  \\item \\textbf{ESS-binding} ($b_\\tau > b_{\\mathrm{ESS}}$): the stability ceiling caps $b^{*} = b_{\\mathrm{ESS}}$.\n\\end{enumerate}\nAcross 51{,}913 micro-batches in our main experiment ($\\rho{=}0.4$, $\\tau{=}0.8$, $n_{\\min}{=}2$), 49.9\\% are clean, 20.2\\% are $\\alpha_{\\mathrm{eff}}$-binding, and 30.0\\% are ESS-binding.\nIn $\\alpha_{\\mathrm{eff}}$-binding batches, the solver selects $b^{*} = 1.67$ on average, while an ESS-only strategy would choose $b = 4.15$ on the same batches---2.5$\\times$ more aggressive.\nThe residual $\\mathrm{ESS} = 2.60$ in these batches (vs.\\ $n_{\\min} = 2.0$) confirms that the dual constraint prevents unnecessary over-downweighting.\n\n\\begin{algorithm}[t]\n\\caption{Per-batch adaptive $b^{*}$ selection}\n\\label{alg:bstar}\n\\begin{algorithmic}[1]\n\\Require Batch scores $\\{q_i\\}_{i=1}^{B}$, indicators $\\{r_i\\}$, quality threshold~$\\tau$, ESS floor~$n_{\\min}$, search bound~$b_{\\max}$, tolerance~$\\varepsilon$\n\\Ensure Optimal exponent $b^{*}$\n\\If{$\\alpha_{\\mathrm{eff}}(0) \\geq \\tau$}\n  \\State \\Return $0$ \\Comment{clean batch}\n\\EndIf\n\\State $b_\\tau \\gets \\Call{Bisect}{\\alpha_{\\mathrm{eff}}(\\cdot){=}\\tau,\\; [0, b_{\\max}],\\; \\varepsilon}$\n\\If{$\\mathrm{ESS}(b_\\tau) \\geq n_{\\min}$}\n  \\State \\Return $b_\\tau$ \\Comment{$\\alpha_{\\mathrm{eff}}$-binding}\n\\Else\n  \\State $b_{\\mathrm{ESS}} \\gets \\Call{Bisect}{\\mathrm{ESS}(\\cdot){=}n_{\\min},\\; [0, b_{\\max}],\\; \\varepsilon}$\n  \\State \\Return $b_{\\mathrm{ESS}}$ \\Comment{ESS-binding}\n\\EndIf\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Implementation.}\nGiven $b^{*}$, we compute normalized weights $\\pi_i = w_i(b^{*}) / \\sum_j w_j(b^{*})$ and form the weighted loss $\\mathcal{L} = \\sum_i \\pi_i \\ell_i$, where $\\ell_i$ is the per-sample cross-entropy.\nThis \\emph{loss reweighting} maintains continuous gradients, unlike the SIR resampling of \\citet{drayson_2025_detection_collapse} which introduces discrete sampling noise by drawing a subset proportional to $w_i$.\nEach bisection requires $\\mathcal{O}(B \\log(b_{\\max}/\\varepsilon))$ operations---with $B{=}4$, $b_{\\max}{=}20$, and $\\varepsilon{=}0.01$, roughly 44 floating-point operations per batch, negligible beside the forward and backward passes.\n\n\\subsection{Hyperparameters}\n\\label{sec:hyperparameters}\n\nThe framework introduces two hyperparameters, both with principled defaults set once across all experiments.\n\n\\paragraph{Quality threshold $\\tau$.}\nConvergence theory for contaminated training shows that convergence rate improves with the effective real fraction~\\citep{wang_2026_survive_contamination}, motivating a lower bound on $\\alpha_{\\mathrm{eff}}$.\nThe specific value of $\\tau$ is set empirically.\nWe find a wide safe range: $\\tau \\in [0.5, 0.8]$ consistently outperforms uniform training (Section~\\ref{sec:results}), with $\\tau = 0.8$ achieving the best perplexity.\nAbove 0.8, $b^{*}$ inflates rapidly (mean $b^{*} = 3.08$ at $\\tau = 0.95$), causing over-downweighting.\nWe use $\\tau = 0.8$ as the default throughout.\n\n\\paragraph{ESS floor $n_{\\min}$.}\nWe set $n_{\\min} = 2$ for batch size $B = 4$.\nThe constraint $n_{\\min} < B$ is necessary: $n_{\\min} \\geq B$ forces $b^{*} = 0$ on every batch, recovering uniform training.\nAt the other extreme, $n_{\\min} = 1$ effectively removes the stability constraint---mean $b^{*}$ rises to 7.20, with 46.7\\% of batches hitting the search ceiling at $b_{\\max}{=}20$, and perplexity degrades by $+0.14$ relative to $n_{\\min} = 2$.\nIn practice, $n_{\\min} \\in \\{2, 3\\}$ yields stable results across seeds (Section~\\ref{sec:results}).\n```\n\n---\n\n=== related_work_0b6096.tex ===\n\n```\n% Related Work for \"Minimum Intervention Reweighting: Adaptive Exponent Selection\n% for Contamination-Aware Pretraining\"\n% Generated: 2026-05-15\n% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)\n\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation---\\emph{model collapse} \\citep{shumailov2024model}.\n\\cite{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\nMore critically, \\cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.\nWith synthetic content now estimated at 20--60\\% of web corpora \\citep{cheng2025contamination}, these results motivate contamination-aware training strategies that explicitly account for data provenance rather than treating all tokens equally.\n\n\\paragraph{Detect and Reweight.}\nA natural response to contamination is to detect and remove synthetic content.\nDetectGPT \\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\% Prob \\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\\% tokens as a reference-free signal; both produce continuous confidence scores suitable as input to reweighting frameworks.\n\\cite{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples; \\cite{guo2025escaping} similarly rely on verification-based selection.\nSoft reweighting avoids the precision--recall threshold inherent in hard filtering by assigning continuous weights.\n\nMost directly related to our work, \\cite{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is a detector's synthetic probability.\nWe adopt the same weighting formula but differ in several fundamental ways.\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\leq}360$M parameters, $b{=}1$ for 1.7B), making the choice per-model and expensive.\nOur $\\bstar$ is derived per-batch from dual constraints ($\\aeff \\geq \\tau$, $\\mathrm{ESS} \\geq \\nmin$) at zero validation cost, following a minimum intervention principle that selects the smallest sufficient exponent.\n\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradient contributions.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\,=\\,0.939) suffices on FineWeb-scale data (132M+ tokens).\n\n\\paragraph{Data Mixing and Reweighting.}\nA parallel line of work optimizes data composition without targeting synthetic contamination.\nAt the \\emph{domain} level, DoReMi \\citep{xie2023doremi} learns mixture weights via Group DRO with a proxy model, DSIR \\citep{xie2023dsir} performs importance resampling with $n$-gram features, \\cite{ye2025mixing} discover predictable functional forms relating mixing ratios to performance, and AIOLI \\citep{chen2025aioli} unifies these into an online adaptive framework.\nThese methods operate at the domain level and do not address instance-level contamination within a domain.\nAt the \\emph{instance} level, SoftDedup \\citep{he2024softdedup} downweights high-frequency samples via $n$-gram commonness, and \\cite{sow2025dynamic} derive sample weights from per-sample loss with convergence guarantees.\nOur reweighting differs from all of these in being driven by \\emph{provenance}---detector scores estimating human vs.\\ machine origin---rather than loss, frequency, or domain membership.\n\n\\paragraph{Theoretical Foundations.}\n\\cite{he2025golden} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\\approx}0.62$) optimal when both sources are equally sized; their result requires the contamination ratio, unavailable in web-scale settings.\n\\cite{wang2026survive} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\aeff(b) \\geq \\tau$ guarantees a convergence-rate lower bound.\nWe operationalize this without the known-proportion assumption, estimating $\\aeff$ from batch-level statistics online.\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \\cite{vehtari2024psis}.\n\\cite{kimura2024iw} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as covariate-shift correction where the covariate is synthetic origin probability.\n\n\\smallskip\n\\noindent\\textbf{Summary.}\nNo existing method provides principled per-batch exponent selection without validation.\nDrayson et al.\\ use the same $w{=}(1{-}q)^b$ formula but require per-model grid search; Golden Ratio weighting requires known mixture proportions; DoReMi and DSIR operate at the domain level rather than instance-level contamination.\nOur dual-constraint framework fills this gap by deriving the minimum intervention $\\bstar$ from batch-level diagnostics alone.\n```\n\n---\n\n=== related_work.tex ===\n\n```\n\\section{Related Work}\n\n\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation---\\emph{model collapse}~\\citep{shumailov_2024_model_collapse}.\n\\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\nMore critically, \\citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.\n\\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\\% of web corpora.\nThese results motivate \\emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.\n\n\\paragraph{Detection and Filtering of Machine-Generated Text.}\nGiven the severity of contamination, a natural response is to detect and remove synthetic content.\nDetectGPT~\\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\% Prob~\\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\\% tokens as a reference-free signal.\nBoth produce continuous confidence scores suitable as input to downstream weighting---including ours.\nOn the mitigation side, \\citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.\n\\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.\nHard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.\n\nMost directly related to our work, \\citet{drayson_2025_detection_collapse} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic probability.\nWe adopt the same weighting formula but differ in several fundamental ways.\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\leq}360$M, $b{=}1$ for 1.7B), making the choice \\emph{per-model} and expensive.\nOur $b^*$ is derived per-batch from dual constraints ($\\alpha_{\\mathrm{eff}} \\geq \\tau$, $\\mathrm{ESS} \\geq n_{\\min}$) at zero validation cost.\n\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradients.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\,=\\,0.939) suffices on FineWeb-scale data (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.\n\n\\paragraph{Data Mixing and Instance-Level Reweighting.}\nA parallel line of work optimizes data composition without targeting synthetic contamination.\nAt the \\emph{domain} level, DoReMi~\\citep{xie_2023_doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\\citep{xie_2023_dsir} performs importance resampling with $n$-gram features, and \\citet{ye_2025_data_mixing_laws} discover predictable functional forms relating mixing ratios to performance.\nAIOLI~\\citep{chen_2025_aioli} unifies these into an online adaptive framework, while \\citet{yang_2026_data_mixing_agent} train an RL agent for domain-weight selection.\nThese methods do not address instance-level contamination within a domain.\nAt the \\emph{instance} level, SoftDedup~\\citep{he_2024_softdedup} downweights high-frequency samples via $n$-gram commonness, \\citet{sow_2025_dynamic_reweighting} derive sample weights from per-sample loss with convergence guarantees, and \\citet{kuo_2024_data_weighting} show that differentiated weighting of LLM-generated data improves downstream classification.\nOur reweighting differs from all of these in being driven by \\emph{provenance}---detector scores estimating human vs.\\ synthetic origin---rather than loss, frequency, or domain membership.\n\n\\paragraph{Theoretical Foundations.}\n\\citet{he_2025_golden_ratio} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\\approx}0.62$) optimal when both sources are equally sized.\nTheir result requires the contamination ratio $k$, unavailable in web-scale settings; we use it as an oracle baseline.\n\\citet{wang_2026_survive_contamination} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ guarantees a convergence-rate lower bound.\nWe operationalize this without the known-proportion assumption, estimating $\\alpha_{\\mathrm{eff}}$ from batch-level statistics online.\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \\citet{vehtari_2024_psis}.\n\\citet{kimura_2024_iw_survey} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as a special case of covariate-shift correction where the covariate is synthetic origin probability.\n```\n\n---\n\n=== experiments_86dfd1.tex ===\n\n```\n\\section{Experimental Setup}\n\\label{sec:experiments}\n\n\\paragraph{Training Data.}\nWe sample a 132M-token subset of FineWeb~\\citep{penedo_2024_fineweb} as the real-data source.\nTo simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\\citep{yang_2025_qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\\rho = 0.4$ via uniform random mixing.\nThis self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.\n\n\\paragraph{Detector.}\nWe train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\\,=\\,0.939 with calibrated ECE\\,=\\,0.048 after temperature scaling ($T = 0.204$).\nThe resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\\% of samples in the uncertain range $[0.2, 0.8]$.\nWe use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\\,${\\geq}$\\,0.98 in \\citealt{drayson_2025_detection_collapse}) to test whether score \\emph{calibration} matters more than raw discrimination for reweighting.\n\n\\paragraph{Training.}\nWe continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\\,=\\,$5{\\times}10^{-5}$), max sequence length 2048, and bf16 precision.\nAll main comparisons use three random seeds (42, 123, 456).\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).\nAll evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.\n\n\\paragraph{Methods.}\nWe compare five approaches:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).\n  \\item \\textbf{Grid-$b$}: fixed $b \\in \\{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\}$, best selected post-hoc by held-out PPL.\n        Represents validation-based selection~\\citep{drayson_2025_detection_collapse}.\n  \\item \\textbf{ESS-only}: $b^* = \\max\\{b : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\\alpha_{\\mathrm{eff}}$.\n  \\item \\textbf{Golden Ratio}: $w = 1/\\varphi \\approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\\citep{he_2025_golden_ratio}.\n        Requires known provenance labels (oracle).\n  \\item \\textbf{Adaptive} (ours): per-batch $b^*$ from the dual-constraint formulation (\\S\\ref{sec:method}), with $\\tau = 0.8$ and $n_{\\min} = 2$ (half the micro-batch size).\n\\end{itemize}\n```\n\n---\n\n=== experiments.tex ===\n\n```\n\\section{Experimental Setup}\n\\label{sec:experiments}\n\n\\paragraph{Training Data.}\nWe sample a 132M-token subset of FineWeb~\\citep{penedo_2024_fineweb} as the real-data source.\nTo simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\\citep{yang_2025_qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\\rho = 0.4$ via uniform random mixing.\nThis self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.\n\n\\paragraph{Detector.}\nWe train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\\,=\\,0.939 with calibrated ECE\\,=\\,0.048 after temperature scaling ($T = 0.204$).\nThe resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\\% of samples in the uncertain range $[0.2, 0.8]$.\nWe use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\\,${\\geq}$\\,0.98 in \\citealt{drayson_2025_detection_collapse}) to test whether score \\emph{calibration} matters more than raw discrimination for reweighting.\n\n\\paragraph{Training.}\nWe continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\\,=\\,$5{\\times}10^{-5}$), max sequence length 2048, and bf16 precision.\nAll main comparisons use three random seeds (42, 123, 456).\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).\nAll evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.\n\n\\paragraph{Methods.}\nWe compare five approaches:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).\n  \\item \\textbf{Grid-$b$}: fixed $b \\in \\{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\}$, best selected post-hoc by held-out PPL.\n        Represents validation-based selection~\\citep{drayson_2025_detection_collapse}.\n  \\item \\textbf{ESS-only}: $b^* = \\max\\{b : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\\alpha_{\\mathrm{eff}}$.\n  \\item \\textbf{Golden Ratio}: $w = 1/\\varphi \\approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\\citep{he_2025_golden_ratio}.\n        Requires known provenance labels (oracle).\n  \\item \\textbf{Adaptive} (ours): per-batch $b^*$ from the dual-constraint formulation (\\S\\ref{sec:method}), with $\\tau = 0.8$ and $n_{\\min} = 2$ (half the micro-batch size).\n\\end{itemize}\n```\n\n---\n\n=== results_d0d647.tex ===\n\n```\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Comparison}\n\nTable~\\ref{tab:main} reports held-out perplexity across methods and seeds.\nAdaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).\nThis parity comes at zero validation cost---grid search requires $|\\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.\n\nThe grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\\ref{app:grid}), confirming that exponent selection is consequential.\nThe optimal $b{=}0.5$ differs from the $b{=}10$ reported by \\citet{drayson_2025_detection_collapse} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.\n\n% Claim 1: Dual > ESS-only (3 seeds)\nESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \\emph{worse} than uniform (17.694) by 0.029.\nThe degradation is consistent: ESS-only exceeds uniform on every individual seed (Table~\\ref{tab:main}), ruling out seed-specific artifacts.\nRemoving $\\alpha_{\\mathrm{eff}}$ and maximizing $b$ subject only to $\\mathrm{ESS} \\geq n_{\\min}$ leads to systematic over-downweighting, providing direct evidence for the minimum-intervention principle.\nConversely, adaptive (dual) improves over uniform on all three seeds (by 0.041, 0.043, and 0.045 respectively), confirming that the $\\alpha_{\\mathrm{eff}}$ quality floor prevents the over-intervention that plagues ESS-only.\n\nThe Golden Ratio oracle~\\citep{he_2025_golden_ratio} achieves PPL 17.654 on seed 42 using known provenance labels.\nAdaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.\n\nThe adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.\nThe constraint regime breakdown in \\S\\ref{sec:algorithm} shows that $\\alpha_{\\mathrm{eff}}$ prevents over-intervention in the 40\\% of reweighted batches where moderate $b$ already meets the quality target.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 456} & \\textbf{Mean} \\\\\n\\midrule\nUniform               & 17.694 & 17.686 & 17.702 & 17.694 \\\\\nGrid-best ($b{=}0.5$) & \\textbf{17.651} & \\textbf{17.638} & \\textbf{17.650} & \\textbf{17.646} \\\\\nESS-only               & 17.730 & 17.720 & 17.719 & 17.723 \\\\\nGolden Ratio$^\\dagger$ & 17.654 & --     & --     & --     \\\\\n\\midrule\nAdaptive (ours)        & 17.653 & 17.643 & 17.657 & 17.651 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Held-out perplexity (PPL, $\\downarrow$).\nGrid-best selects the optimal fixed $b$ post-hoc from six candidates.\n$^\\dagger$Evaluated on seed 42 only.\nBest per column in \\textbf{bold}.}\n\\label{tab:main}\n\\end{table}\n\n\\subsection{Sensitivity Analysis}\n\n\\paragraph{Quality threshold $\\tau$.}\nTable~\\ref{tab:tau} varies $\\tau$ while holding $n_{\\min} = 2$ (seed 42).\nAll values in $\\tau \\in [0.5, 0.8]$ improve over uniform, with $\\tau = 0.8$ achieving the lowest PPL (17.653).\nHigher $\\tau$ demands greater $\\alpha_{\\mathrm{eff}}$, forcing the solver to increase $b^*$: mean $\\bar{b}^*$ rises monotonically from 0.39 at $\\tau{=}0.5$ to 3.08 at $\\tau{=}0.95$.\nBelow 0.8, reweighting is too gentle to fully exploit the detector signal; above, $b^*$ inflates past diminishing returns and PPL degrades.\nThe range $[0.5, 0.8]$ provides a wide safe operating region, with $\\tau = 0.8$ as the recommended default.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\tau$ & \\textbf{PPL} & $\\Delta_{\\mathrm{unif}}$ & $\\bar{b}^*$ \\\\\n\\midrule\n0.50 & 17.688 & $-$0.006 & 0.39 \\\\\n0.60 & 17.681 & $-$0.013 & 0.59 \\\\\n0.70 & 17.679 & $-$0.015 & 0.89 \\\\\n\\textbf{0.80} & \\textbf{17.653} & $\\mathbf{-0.041}$ & \\textbf{1.40} \\\\\n0.90 & 17.712 & $+$0.018 & 2.36 \\\\\n0.95 & 17.723 & $+$0.029 & 3.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to $\\tau$ (seed 42, $n_{\\min}{=}2$, $\\rho{=}0.4$).\n$\\Delta_{\\mathrm{unif}}$: PPL change vs.\\ uniform baseline (17.694).\n$\\bar{b}^*$: mean adaptive exponent across batches.}\n\\label{tab:tau}\n\\end{table}\n\n\\paragraph{Minimum ESS $n_{\\min}$.}\nTable~\\ref{tab:nmin} ablates $n_{\\min}$ at batch size $B{=}4$.\nRemoving the ESS floor ($n_{\\min} = 1$) allows $b^*$ to inflate to mean 7.20, degrading PPL to 17.789---0.095 worse than uniform.\nAt $n_{\\min} = 2$ ($= \\lfloor B/2 \\rfloor$), $b^*$ is constrained to mean 1.40 and PPL reaches 17.653, verified across three seeds.\nAt $n_{\\min} = B = 4$, the ESS constraint is trivially satisfied at $b^* = 0$ for every batch, and PPL reverts to the uniform level (17.695 vs.\\ 17.694).\nThe results exhibit a U-shaped pattern: too-low $n_{\\min}$ permits over-downweighting, while $n_{\\min}$ at or near $B$ removes the ability to reweight.\n\nThe coupling between $n_{\\min}$ and $B$ extends beyond the $B{=}4$ setting.\nAt batch size $B{=}8$ with $n_{\\min}{=}2$, the ESS range $[2, 8]$ is wide enough that the stability constraint rarely binds, yielding PPL 17.73---comparable to ESS-only and 0.036 worse than uniform.\nThis confirms that $n_{\\min}$ must scale with $B$: a fixed $n_{\\min}$ that works for one batch size can degrade to near-ESS-only behavior at larger $B$.\nThe rule $n_{\\min} = \\max(2, \\lfloor B/2 \\rfloor)$ keeps the ESS constraint active without over-restricting the solver, and we recommend it as a practical default.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}ccc@{}}\n\\toprule\n$n_{\\min}$ & \\textbf{PPL} & $\\bar{b}^*$ \\\\\n\\midrule\n1 & 17.789 & 7.20 \\\\\n\\textbf{2} & \\textbf{17.653} & \\textbf{1.40} \\\\\n3$^\\ddagger$ & 17.644 & 1.43 \\\\\n4 & 17.695 & 0.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to $n_{\\min}$ (seed 42, $B{=}4$, $\\tau{=}0.8$).\n$n_{\\min} = 4 = B$ forces $b^* = 0$ on all batches, recovering uniform weighting.\n$^\\ddagger$From an earlier adaptive configuration; not an independent ablation.}\n\\label{tab:nmin}\n\\end{table}\n```\n\n---\n\n=== results.tex ===\n\n(Identical content to results_d0d647.tex — same verbatim text, no differences.)\n\n---\n\n=== discussion_270aaa.tex ===\n\n```\n\\paragraph{Why minimum intervention works.}\nThe central finding of our experiments is that restraint in downweighting outperforms aggressiveness.\nESS-only reweighting---which maximizes $b$ subject only to $\\mathrm{ESS} \\geq \\nmin$---degrades PPL to 17.723, \\emph{worse} than the uniform baseline (17.694, Table~\\ref{tab:main}).\nThe dual-constrained adaptive $\\bstar$, by contrast, achieves 17.651 by selecting the \\emph{smallest} $b$ that meets the quality floor $\\tau$.\nThe mechanism is clear from the binding statistics: in the 40.1\\% of reweighted batches where $\\aeff$ binds, mean $\\bstar = 1.67$ versus 4.15 under ESS-only---a 2.5$\\times$ less aggressive exponent that retains ESS\\,=\\,2.60, well above the floor $\\nmin = 2$.\nOver-downweighting discards gradient signal from borderline samples whose detector scores are intermediate (e.g., $q \\approx 0.4$--$0.6$); these samples carry partial but non-negligible training value, and aggressively suppressing them impoverishes the effective training distribution.\nThe $\\aeff$ constraint prevents this by halting $b$ as soon as the quality target is met.\n\n\\paragraph{$\\tau$ as a practical dial.}\nThe quality threshold $\\tau$ controls the trade-off between decontamination strength and sample retention.\nOur sweep (Table~\\ref{tab:tau}) reveals a wide safe operating range: all $\\tau \\in [0.5, 0.8]$ outperform uniform training, with PPL varying only 0.035 across this interval.\nThe sensitivity is asymmetric---under-cleaning ($\\tau < 0.8$) incurs mild degradation ($-$0.006 to $-$0.015 vs.\\ uniform), while over-cleaning ($\\tau > 0.8$) causes sharper regression as $\\bstar$ inflates (mean $\\bar{b}^* = 2.36$ at $\\tau{=}0.9$, 3.08 at $\\tau{=}0.95$).\nThis asymmetry reinforces the minimum intervention intuition: the cost of doing too little is small, whereas the cost of doing too much is steep.\nWe recommend $\\tau = 0.8$ as a principled default; practitioners operating at different contamination rates can adjust within the safe range with low risk.\n\n\\paragraph{Connection to convergence theory.}\n\\citet{wang_2026_survive_contamination} prove that pretraining convergence rate scales with $\\alpha$, the effective real data fraction.\nOur $\\tau$ serves an analogous role---setting a floor on the weighted real proportion per batch---but an important distinction must be noted: their analysis assumes a known contamination proportion, whereas our method estimates quality from detector scores without access to the true $\\alpha$.\nWe therefore position $\\tau$ as an empirical hyperparameter with theoretical motivation: convergence theory explains \\emph{why} a quality threshold improves training, while the specific value of $\\tau$ is determined empirically.\nBridging this gap---deriving $\\tau$ from first principles without known proportions---is an open theoretical question.\n```\n\n---\n\n=== discussion.tex ===\n\n```\n\\paragraph{Why minimum intervention works.}\nThe central finding of our experiments is that restraint in downweighting outperforms aggressiveness.\nESS-only reweighting---which maximizes $b$ subject only to $\\mathrm{ESS} \\geq \\nmin$---degrades PPL to 17.723, \\emph{worse} than the uniform baseline (17.694, Table~\\ref{tab:main}).\nThe dual-constrained adaptive $\\bstar$, by contrast, achieves 17.651 by selecting the \\emph{smallest} $b$ that meets the quality floor $\\tau$.\nThe mechanism is clear from the binding statistics: in the 40.1\\% of reweighted batches where $\\aeff$ binds, mean $\\bstar = 1.67$ versus 4.15 under ESS-only---a 2.5$\\times$ less aggressive exponent that retains ESS\\,=\\,2.60, well above the floor $\\nmin = 2$.\nOver-downweighting discards gradient signal from borderline samples whose detector scores are intermediate (e.g., $q \\approx 0.4$--$0.6$); these samples carry partial but non-negligible training value, and aggressively suppressing them impoverishes the effective training distribution.\nThe $\\aeff$ constraint prevents this by halting $b$ as soon as the quality target is met.\n\n\\paragraph{$\\tau$ as a practical dial.}\nThe quality threshold $\\tau$ controls the trade-off between decontamination strength and sample retention.\nOur sweep (Table~\\ref{tab:tau}) reveals a wide safe operating range: all $\\tau \\in [0.5, 0.8]$ outperform uniform training, with PPL varying only 0.035 across this interval.\nThe sensitivity is asymmetric---under-cleaning ($\\tau < 0.8$) incurs mild degradation ($-$0.006 to $-$0.015 vs.\\ uniform), while over-cleaning ($\\tau > 0.8$) causes sharper regression as $\\bstar$ inflates (mean $\\bar{b}^* = 2.36$ at $\\tau{=}0.9$, 3.08 at $\\tau{=}0.95$).\nThis asymmetry reinforces the minimum intervention intuition: the cost of doing too little is small, whereas the cost of doing too much is steep.\nWe recommend $\\tau = 0.8$ as a principled default; practitioners operating at different contamination rates can adjust within the safe range with low risk.\n\n\\paragraph{Connection to convergence theory.}\n\\citet{wang2026survive} prove that pretraining convergence rate scales with $\\alpha$, the effective real data fraction.\nOur $\\tau$ serves an analogous role---setting a floor on the weighted real proportion per batch---but an important distinction must be noted: their analysis assumes a known contamination proportion, whereas our method estimates quality from detector scores without access to the true $\\alpha$.\nWe therefore position $\\tau$ as an empirical hyperparameter with theoretical motivation: convergence theory explains \\emph{why} a quality threshold improves training, while the specific value of $\\tau$ is determined empirically.\nBridging this gap---deriving $\\tau$ from first principles without known proportions---is an open theoretical question.\n```\n\n---\n\n=== conclusion_386ecc.tex ===\n\n```\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced Minimum Intervention Reweighting, a dual-constrained framework for contamination-aware pretraining that selects per-batch exponents $b^*$ without validation data.\nThe method finds the smallest $b$ satisfying $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ subject to $\\mathrm{ESS}(b) \\geq n_{\\min}$, enforcing a minimum-intervention principle: apply only as much downweighting as needed to meet a quality floor, no more.\nThis stands in direct contrast to ESS-only (maximum-intervention) strategies, which we show degrade performance below even uniform baselines by over-downweighting contaminated samples.\n\nAcross three seeds at 0.6B scale with 40\\% synthetic contamination, adaptive $b^*$ matches grid-search-optimal PPL (17.651 vs.\\ 17.646) within seed variance, eliminating the $|\\mathcal{B}|$-run grid search entirely.\nThe quality threshold $\\tau$ is robust across $[0.5, 0.8]$---all values in this range outperform uniform weighting.\nA lightweight TF-IDF + logistic regression detector (AUC\\,0.94) suffices when post-hoc calibrated (ECE\\,0.048); score calibration matters more than raw discriminative power.\nThe batch-level constraint regime---49.9\\% clean (no reweighting needed), 20.2\\% $\\alpha_{\\mathrm{eff}}$-binding, 30.0\\% ESS-binding---confirms that both constraints are active and complementary in practice.\n\n\\section*{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Scale.}\nAll experiments use a single model size (Qwen3-0.6B) with batch size 4.\nBatch-level $q$-score statistics concentrate differently at larger batch sizes typical of 3B+ training; the optimal $\\tau$ range and constraint dynamics may shift at scale.\n\n\\paragraph{Contamination distribution.}\nWe inject synthetic data via uniform random mixing at a controlled ratio ($\\rho{=}0.4$).\nReal web-scale contamination is domain-skewed, which may alter within-batch $\\alpha_{\\mathrm{eff}}$ distributions and require domain-aware extensions.\n\n\\paragraph{Detector coverage.}\nWe evaluate one detector family (TF-IDF + logistic regression).\nAlthough our results suggest calibration dominates discrimination for reweighting quality, a systematic ablation across detector architectures and quality levels is needed.\n\n\\paragraph{Threshold.}\n$\\tau$ is an empirical hyperparameter.\nThe convergence theory of \\citet{wang_2026_survive_contamination} assumes a known contamination proportion $\\alpha$, which we do not require; bridging this gap to derive $\\tau$ from first principles remains open.\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity only.\nDownstream task evaluation (MMLU, HellaSwag) would strengthen the practical case, particularly at scales where PPL differences translate more reliably to task performance.\n\n\\paragraph{Effect size.}\nThe PPL improvement over uniform weighting is 0.043 at 0.6B/40\\% contamination.\nWhile consistent across seeds, this effect is modest; we expect amplification at higher contamination ratios and larger model scales, but verification is ongoing.\n```\n\n---\n\n=== conclusion.tex ===\n\n(Identical content to conclusion_386ecc.tex — same verbatim text, no differences.)\n\n---\n\n=== table1_main_results.tex ===\n\n```\n\\begin{table}[t]\n\\centering\n\\caption{Held-out perplexity under different weighting methods ($\\rho{=}0.4$, 3 seeds). $\\Delta$ is relative to the Uniform baseline.}\n\\label{tab:main-results}\n\\small\n\\begin{tabular}{@{}lccccr@{}}\n\\toprule\nMethod & seed42 & seed123 & seed456 & Mean$\\pm$Std & $\\Delta$ \\\\\n\\midrule\nUniform                                  & 17.694 & 17.686 & 17.702 & 17.694$\\pm$0.008 & --- \\\\\nGrid-best ($b{=}0.5$)                    & 17.651 & 17.638 & 17.650 & 17.646$\\pm$0.007 & $-$0.048 \\\\\nAdaptive ($\\tau{=}0.8$, $n_{\\min}{=}3$\\textsuperscript{\\dag}) & 17.644 & 17.631 & 17.642 & \\textbf{17.639$\\pm$0.007} & $-$\\textbf{0.055} \\\\\nAdaptive-fix ($\\tau{=}0.8$, $n_{\\min}{=}2$) & 17.653 & 17.643 & 17.657 & 17.651$\\pm$0.007 & $-$0.043 \\\\\nESS-only                                 & 17.730 & 17.720 & 17.719 & 17.723$\\pm$0.006 & $+$0.029 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{\\dag}$n_{\\min}{=}3$ is the original implementation (historical); $n_{\\min}{=}2$ is the theoretically derived correction.}\n\\end{table}\n```\n\n---\n\nAll 15 files have been returned verbatim. Note: `results_d0d647.tex` and `results.tex` are byte-for-byte identical, as are `conclusion_386ecc.tex` and `conclusion.tex`. The `discussion_270aaa.tex` and `discussion.tex` differ in only one citation key: `\\citet{wang_2026_survive_contamination}` (versioned) vs `\\citet{wang2026survive}` (base). The `table1_main_results.tex` contains a materially different table from the inline table in the results files — it includes an `Adaptive ($n_{\\min}{=}3$)` row showing PPL 17.639 (better than grid-best) and an `Adaptive-fix ($n_{\\min}{=}2$)` row at 17.651, whereas the results section tables only show `Adaptive (ours)` at 17.651 without the $n_{\\min}{=}3$ variant."
      }
    ],
    "totalDurationMs": 337182,
    "totalTokens": 63594,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34360,
      "cache_read_input_tokens": 8113,
      "output_tokens": 21120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34360
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21120,
          "cache_read_input_tokens": 8113,
          "cache_creation_input_tokens": 34360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34360,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 15,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Assistant

_source line 81_

<details><summary>Logged reasoning block</summary>

```text
The output is large (65.8KB). Let me read the full output to conduct the audit properly. Let me read the persisted output file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "4fcc83ea-d0d9-42b4-9e17-9be99f1283f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hr4cLWr36EbD6XpiQCdXbN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 26845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1302
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

Let me read the full output to conduct the audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "d81b586b-6289-4a65-aa71-85bfc4d52a28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hr4cLWr36EbD6XpiQCdXbN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 26845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1302
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01A7EJTnJd7QepiMn7xYo7xx`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/aa969b71-d198-4ba3-9b84-63a2c341d557/tool-results/toolu_01JwscEPDwAWYsvzEyjiYamw.json",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "42dadf92-3ee3-4003-aab6-b402aab8e57f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hr4cLWr36EbD6XpiQCdXbN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 26845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1302
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-16T01:05:58.093Z_

<details><summary>↩ Tool result · `toolu_01A7EJTnJd7QepiMn7xYo7xx`</summary>

````text
1	[
2	  {
3	    "type": "text",
4	    "text": "Here are all 15 files, verbatim:\n\n---\n\n=== introduction_c6a67f.tex ===\n\n```\n% Introduction for \"Minimum Intervention Reweighting: Adaptive Exponent Selection\n% for Contamination-Aware Pretraining\"\n% Generated: 2026-05-15\n% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)\n\n\\section{Introduction}\n\\label{sec:intro}\n\nWeb pretraining corpora are increasingly contaminated by machine-generated text, with recent estimates placing the synthetic fraction between 20\\% and 60\\% \\citep{cheng2025contamination}.\nThis poses a fundamental threat to model quality: \\cite{shumailov2024model} demonstrate that training on recursively generated data leads to irreversible model collapse, and \\cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger degradation, ruling out data scaling as a remedy.\nAs synthetic content becomes ubiquitous, \\emph{contamination-aware training}---strategies that explicitly account for data provenance during optimization---is necessary for maintaining pretraining quality.\n\nA natural mitigation is detect-and-reweight: assign each sample a weight $w(x) = (1 - q(x))^b$ based on a detector's estimated synthetic probability $q(x)$, where larger $b$ downweights suspected synthetic text more aggressively \\citep{drayson2025detection}.\nHowever, the exponent $b$ is a sensitive per-model hyperparameter whose optimal value varies by an order of magnitude across model scales---$b = 1$ for SmolLM-1.7B versus $b = 10$ for GPT-2 124M---and selecting it requires a clean validation set and grid search costing up to $6{\\times}$ the base training budget.\nThe practical question is: \\emph{given per-sample detector scores $q(x)$, how should $b$ be chosen without validation?}\n\nWe propose a \\emph{dual-constraint framework} that derives the exponent adaptively per batch from two diagnostics computed on the detector scores alone.\nThe effective real proportion $\\aeff(b)$ measures the weighted fraction of gradient signal from real data and imposes a \\emph{quality floor}: $\\aeff(b) \\geq \\tau$---at least enough cleaning.\nKish's effective sample size $\\mathrm{ESS}(b)$ \\citep{vehtari2024psis} quantifies weight concentration and imposes a \\emph{stability ceiling}: $\\mathrm{ESS}(b) \\geq \\nmin$---not so much cleaning that gradient estimates degrade.\nA key structural insight makes this tractable: $\\aeff$ is strictly increasing in $b$ while $\\mathrm{ESS}$ is strictly decreasing, so the quality constraint yields a unique lower bound $\\btau$ and the stability constraint a unique upper bound $\\bess$.\nWe adopt a \\emph{minimum intervention principle}:\n\\begin{equation*}\n  \\bstar = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\} \\quad \\text{subject to} \\quad \\mathrm{ESS}(\\bstar) \\geq \\nmin,\n\\end{equation*}\nthe smallest exponent satisfying the quality floor.\nThis is deliberately conservative: apply enough decontamination to meet the quality target, but no more, preserving the largest possible effective sample size.\nIn practice, batches fall into three regimes---already clean ($\\bstar{=}0$), quality-binding ($\\bstar{=}\\btau$), and stability-binding ($\\bstar{=}\\bess$)---allowing the framework to handle heterogeneous contamination naturally.\nUnlike the discrete sampling-importance-resampling of \\cite{drayson2025detection}, we implement reweighting through direct loss scaling with continuous gradient contributions.\n\nWe evaluate on continued pretraining of Qwen3-0.6B on 132M FineWeb \\citep{penedo2024fineweb} tokens with 40\\% synthetic contamination (\\S\\ref{sec:experiments}).\nAdaptive $\\bstar$ with default hyperparameters ($\\tau{=}0.8$, $\\nmin{=}2$) matches the grid-search-optimal fixed $b$ within seed variance (PPL $17.650 {\\pm} 0.007$ vs.\\ $17.646 {\\pm} 0.007$ across three seeds) at zero validation cost.\nIt outperforms both uniform training (PPL $17.69$) and ESS-only maximum intervention (PPL $17.73$), confirming that minimum intervention is superior to maximum intervention.\nA lightweight TF-IDF + logistic regression detector (AUC\\,=\\,0.939) suffices for effective reweighting, and the quality threshold $\\tau$ admits a wide safe range of $[0.5, 0.8]$ within which all tested values improve over uniform training.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item A dual-constraint framework for adaptive $\\bstar$ selection with minimum intervention semantics, providing validation-free per-batch exponent derivation from batch-level diagnostics (\\S\\ref{sec:method}).\n  \\item Empirical evidence that adaptive $\\bstar$ matches grid-search-optimal performance within seed variance at zero validation cost, and that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only) (\\S\\ref{sec:results}).\n  \\item Evidence that a lightweight TF-IDF + logistic regression detector suffices for effective reweighting (\\S\\ref{sec:results}).\n\\end{enumerate}\n```\n\n---\n\n=== introduction.tex ===\n\n```\nWeb corpora increasingly contain machine-generated text.\nRecent estimates place the synthetic fraction at 20--60\\% of crawled data~\\citep{cheng_2025_contamination_survey}, and this share grows as language models are deployed for content production at scale.\nTraining on such contaminated data has concrete consequences: \\citet{shumailov_2024_model_collapse} show that recursive training on model outputs leads to irreversible quality degradation---\\emph{model collapse}---and \\citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.\nA central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.\nThe prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.\n\nA natural response is \\emph{detect-and-reweight}: train a classifier to estimate each sample's synthetic probability $q(x)$, then suppress likely-synthetic samples via the weighting function $w(x) = (1 - q(x))^b$.\n\\citet{drayson_2025_detection_collapse} demonstrate this approach for model collapse prevention and show that the exponent $b$ critically determines outcomes---their optimal values range from $b{=}10$ for models at ${\\leq}360$M parameters to $b{=}1$ at 1.7B, and misspecification degrades results substantially.\nSelecting $b$ therefore requires per-model validation-set grid search, with computational cost scaling linearly in the number of candidates (six training runs in a typical sweep).\nOther approaches assume even stronger supervision: \\citet{he_2025_golden_ratio} derive theoretically optimal weights from convergence analysis but require the exact contamination ratio $\\rho$, which is precisely what is unavailable in practice.\nHard detection-and-removal strategies~\\citep{feng_2025_beyond_collapse} discard borderline samples entirely, sacrificing the smooth reweighting that continuous $q$-scores enable.\n\nGiven per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?\nWe formulate this as a dual-constrained optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\\aeff(b)$ reaches a quality threshold $\\tau$, while keeping Kish's effective sample size $\\mathrm{ESS}(b)$ above a stability floor $\\nmin$.\nThe quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effective real-data fraction~\\citep{wang_2026_survive_contamination}, motivating a lower bound on $\\aeff$.\nThe stability constraint prevents extreme weight concentration that degrades gradient quality.\nThese two requirements exhibit a natural opposition.\n$\\aeff(b)$ increases monotonically in $b$ (Proposition~\\ref{prop:monotone}), yielding a lower bound $\\btau$---the minimum exponent needed to achieve the target quality.\n$\\mathrm{ESS}(b)$ decreases monotonically, yielding an upper bound $\\bess$---the maximum exponent before gradient stability degrades.\nThe adaptive exponent $\\bstar = \\btau$ when the feasible region $[\\btau, \\bess]$ is non-empty, embodying a \\emph{minimum intervention principle}: apply the least downweighting sufficient to meet the quality target, preserving as much effective training data as possible.\nWhen the constraints conflict ($\\btau > \\bess$), the stability ceiling takes precedence.\n\nThis minimum-intervention semantics distinguishes the method from the alternative of maximizing $b$ subject only to ESS stability.\nAmong batches that require reweighting, the dual-constraint solver selects $\\bstar$ via the $\\aeff$ bound in 40\\% of cases, with mean $\\bstar{=}1.67$; the ESS-only variant would choose $b{=}4.15$ in these same batches, 2.5$\\times$ more aggressive.\nThe remaining 49.9\\% of batches have sufficient real-data content to skip reweighting entirely ($\\bstar{=}0$).\nThe per-batch $\\bstar$ distribution (median 0.87, mean 1.40) adapts continuously to each batch's contamination composition without any held-out signal.\n\nOn Qwen3-0.6B continued pretraining with 40\\% synthetic contamination (132M+ tokens from FineWeb), adaptive reweighting achieves mean held-out perplexity of 17.651 across three seeds, matching the grid-searched optimum ($b{=}0.5$, mean 17.646) within seed-to-seed variance (\\S\\ref{sec:results}).\nThe grid sweep requires six complete training runs to identify this optimum; the adaptive method requires one.\nThe ESS-only variant (maximum intervention) yields mean PPL 17.722---worse than the uniform baseline (17.694)---confirming that maximum intervention degrades training while minimum intervention improves it.\nA lightweight TF-IDF + Logistic Regression detector (AUC\\,=\\,0.939, calibrated ECE\\,=\\,0.048) suffices throughout, suggesting that score calibration matters more than raw classification accuracy for provenance-based reweighting.\n\nOur contributions:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item A dual-constrained framework for adaptive exponent selection: $\\bstar = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\}$ subject to $\\mathrm{ESS}(b) \\geq \\nmin$, computed per-batch from detector scores with minimum-intervention semantics (\\S\\ref{sec:method}).\n\\item Empirical evidence that adaptive $\\bstar$ matches grid-searched best within seed variance at zero validation cost, and that minimum intervention (dual constraint) outperforms maximum intervention (ESS-only) across three seeds (\\S\\ref{sec:results}).\n\\item A demonstration that a lightweight TF-IDF + LR detector with calibrated $q$-scores supports effective reweighting, achieving results comparable to stronger neural detectors (\\S\\ref{sec:experiments}).\n\\end{itemize}\n```\n\n---\n\n=== method_3f5a58.tex ===\n\n```\n% Method section for \"Minimum Intervention Reweighting\" (EMNLP 2026)\n% Generated: 2026-05-15\n% Based on: paper_framing.md (STABLE, D023/D029/D035)\n% Requires macros: \\bstar, \\aeff, \\nmin, \\btau, \\bess (defined in main.tex preamble)\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\\label{sec:problem-setup}\n\nLet $\\mathcal{D} = \\{x_1, \\ldots, x_N\\}$ denote a pretraining corpus comprising human-written text $\\mathcal{D}_{\\mathrm{real}}$ and machine-generated text $\\mathcal{D}_{\\mathrm{synth}}$, with unknown contamination rate $\\rho = |\\mathcal{D}_{\\mathrm{synth}}| / |\\mathcal{D}|$.\nA pretrained detector assigns each sample a synthetic probability $q(x_i) \\in [0, 1]$.\nFollowing \\citet{drayson_2025_detection_collapse}, we define per-sample weights\n\\begin{equation}\n  w_b(x_i) = (1 - q(x_i))^b, \\quad b \\geq 0,\n  \\label{eq:weight}\n\\end{equation}\nwhere $b = 0$ recovers uniform weighting and increasing $b$ progressively downweights high-$q$ samples.\nThe weighted training objective is\n\\begin{equation}\n  \\mathcal{L}(b) = \\frac{\\sum_{i} w_b(x_i) \\, \\ell(x_i; \\theta)}{\\sum_{j} w_b(x_j)},\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\ell(x_i; \\theta)$ is the per-sample language modeling loss.\n\n\\citet{drayson_2025_detection_collapse} treat $b$ as a hyperparameter selected via validation-based grid search, with reported optima ranging from $b{=}1$ (SmolLM-1.7B) to $b{=}10$ (GPT-2 124M), making per-model tuning unavoidable.\nWe instead derive $b$ adaptively per batch from the detector scores alone, requiring no validation set.\n\n\\subsection{Dual-Constraint Framework}\n\\label{sec:dual-constraint}\n\nHigher $b$ removes more synthetic influence but also discards effective training signal.\nWe formalize this trade-off through two per-batch statistics.\n\n\\paragraph{Effective real proportion.}\nFor a batch $\\mathcal{B} = \\{x_1, \\ldots, x_B\\}$ with weights $w_i(b) = (1 - q_i)^b$, we define\n\\begin{equation}\n  \\aeff(b) = \\frac{\\sum_{i \\in \\mathcal{B}} w_i(b) \\cdot \\mathbf{1}[x_i \\in \\mathcal{D}_{\\mathrm{real}}]}{\\sum_{i \\in \\mathcal{B}} w_i(b)},\n  \\label{eq:alpha_eff}\n\\end{equation}\nmeasuring the effective fraction of real data after reweighting.\nSince true provenance labels are unavailable at training time, we use the detector's hard prediction $\\mathbf{1}[q(x_i) < 0.5]$ as a proxy; all theoretical properties below hold for this approximation.\n\n\\paragraph{Effective sample size.}\nKish's effective sample size \\citep{vehtari_2024_psis} quantifies weight concentration:\n\\begin{equation}\n  \\mathrm{ESS}(b) = \\frac{\\left(\\sum_{i \\in \\mathcal{B}} w_i(b)\\right)^2}{\\sum_{i \\in \\mathcal{B}} w_i^2(b)}.\n  \\label{eq:ess}\n\\end{equation}\n$\\mathrm{ESS}(0) = B$ under uniform weights, decreasing toward $1$ as $b \\to \\infty$ for any batch containing synthetic samples.\n\n\\begin{proposition}[Monotonicity]\n\\label{prop:monotonicity}\nFor any batch containing both real and synthetic samples with non-identical $q$-scores:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item $\\aeff(b)$ is strictly increasing in $b$.\n  \\item $\\mathrm{ESS}(b)$ is strictly decreasing in $b$.\n\\end{enumerate}\n\\end{proposition}\n\n\\begin{proof}[Proof sketch]\nFor (1), differentiating Eq.~\\eqref{eq:alpha_eff} using $\\frac{dw_i}{db} = w_i \\ln(1 {-} q_i)$ yields\n\\begin{equation}\n  \\frac{d\\aeff}{db} = \\aeff(1 {-} \\aeff) \\!\\left( \\mathbb{E}_w[\\ln(1{-}q) \\mid \\mathrm{real}] - \\mathbb{E}_w[\\ln(1{-}q) \\mid \\mathrm{synth}] \\right)\\!,\n  \\label{eq:dalpha}\n\\end{equation}\nwhere $\\mathbb{E}_w$ denotes expectation under the normalized weight distribution.\nSince real samples have lower $q$-scores, $\\ln(1{-}q)$ is strictly less negative for real than synthetic samples, making the parenthesized difference positive.\nFor (2), increasing $b$ multiplies each weight by $(1{-}q_i)^{\\Delta b}$, a factor varying across samples, which concentrates the normalized weight distribution and strictly increases $\\sum_i \\tilde{w}_i^2$, hence decreasing ESS.\nFull proofs appear in Appendix~\\ref{app:proofs}.\n\\end{proof}\n\nProposition~\\ref{prop:monotonicity} establishes that quality and sample efficiency move in opposite directions as $b$ increases, motivating two complementary constraints.\n\n\\paragraph{Quality lower bound.}\nWe require $\\aeff(b) \\geq \\tau$ for a threshold $\\tau \\in (0, 1)$.\nBy strict monotonicity, this defines a unique lower bound\n\\begin{equation}\n  \\btau = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\}\n  \\label{eq:b_tau}\n\\end{equation}\non the exponent---the minimum intervention needed to achieve quality $\\tau$.\n\\citet{wang_2026_survive_contamination} show that pretraining convergence rate scales with effective real data fraction, providing theoretical motivation for maintaining $\\aeff$ above a threshold.\n\n\\paragraph{Stability upper bound.}\nWe require $\\mathrm{ESS}(b) \\geq \\nmin$ for a floor $\\nmin \\geq 1$.\nBy strict monotonicity, this defines a unique upper bound\n\\begin{equation}\n  \\bess = \\sup\\{b \\geq 0 : \\mathrm{ESS}(b) \\geq \\nmin\\}\n  \\label{eq:b_ess}\n\\end{equation}\nbeyond which gradient estimates become unreliable due to weight concentration.\n\n\\paragraph{Minimum intervention principle.}\nWe select\n\\begin{equation}\n  \\bstar = \\begin{cases}\n    0 & \\text{if } \\aeff(0) \\geq \\tau \\\\\n    \\btau & \\text{if } \\btau \\leq \\bess \\\\\n    \\bess & \\text{if } \\btau > \\bess\n  \\end{cases}\n  \\label{eq:bstar}\n\\end{equation}\nyielding three regimes:\n(1)~\\textbf{Already clean} ($\\aeff(0) \\geq \\tau$): the unweighted batch meets quality $\\tau$; set $\\bstar = 0$.\n(2)~\\textbf{$\\aeff$-binding} ($\\btau \\leq \\bess$): the quality constraint determines $\\bstar = \\btau$, applying the \\emph{minimum} intervention to reach $\\tau$, with ESS margin remaining.\n(3)~\\textbf{ESS-binding} ($\\btau > \\bess$): quality $\\tau$ is infeasible under the stability constraint; $\\bstar = \\bess$ applies the maximum stable intervention.\n\nThe key insight is that when the feasible region $[\\btau, \\bess]$ is non-empty, the method selects its \\emph{left} endpoint---downweighting no more than necessary.\nThis contrasts with an ESS-only strategy that selects $\\bess$ (the right endpoint), maximizing cleaning at the cost of discarding useful gradient signal from borderline samples.\nIn our experiments (\\S\\ref{sec:results}), 40.1\\% of reweighted batches are $\\aeff$-binding, where mean $\\bstar = 1.67$ compared to $4.15$ under ESS-only---a $2.5\\times$ less aggressive exponent that retains $\\mathrm{ESS} = 2.60$, well above the floor $\\nmin = 2$.\n\n\\subsection{Algorithm}\n\\label{sec:algorithm}\n\nAlgorithm~\\ref{alg:solver} solves for $\\bstar$ via bisection on $\\aeff$, exploiting monotonicity (Proposition~\\ref{prop:monotonicity}) to guarantee convergence.\n\n\\begin{algorithm}[t]\n\\caption{Per-batch adaptive exponent solver}\n\\label{alg:solver}\n\\begin{algorithmic}[1]\n\\REQUIRE Batch scores $\\{q_1, \\ldots, q_B\\}$, threshold $\\tau$, ESS floor $\\nmin$, tolerance $\\varepsilon$, cap $b_{\\max}$\n\\ENSURE Optimal exponent $\\bstar$\n\\IF{$\\aeff(0) \\geq \\tau$}\n  \\STATE \\textbf{return} $\\bstar = 0$ \\hfill $\\triangleright$ Already clean\n\\ENDIF\n\\STATE $b_{\\mathrm{lo}} \\leftarrow 0,\\; b_{\\mathrm{hi}} \\leftarrow b_{\\max}$ \\hfill $\\triangleright$ Bisect for $\\btau$\n\\WHILE{$b_{\\mathrm{hi}} - b_{\\mathrm{lo}} > \\varepsilon$}\n  \\STATE $b_{\\mathrm{mid}} \\leftarrow (b_{\\mathrm{lo}} + b_{\\mathrm{hi}}) / 2$\n  \\IF{$\\aeff(b_{\\mathrm{mid}}) < \\tau$}\n    \\STATE $b_{\\mathrm{lo}} \\leftarrow b_{\\mathrm{mid}}$\n  \\ELSE\n    \\STATE $b_{\\mathrm{hi}} \\leftarrow b_{\\mathrm{mid}}$\n  \\ENDIF\n\\ENDWHILE\n\\STATE $\\btau \\leftarrow b_{\\mathrm{hi}}$\n\\IF{$\\mathrm{ESS}(\\btau) \\geq \\nmin$}\n  \\STATE \\textbf{return} $\\bstar = \\btau$ \\hfill $\\triangleright$ $\\aeff$-binding\n\\ELSE\n  \\STATE Find $\\bess = \\sup\\{b : \\mathrm{ESS}(b) \\geq \\nmin\\}$ via bisection\n  \\STATE \\textbf{return} $\\bstar = \\bess$ \\hfill $\\triangleright$ ESS-binding\n\\ENDIF\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Implementation.}\nWe apply $\\bstar$ through loss reweighting: each sample's loss is scaled by its normalized weight $\\bar{w}_i = w_{\\bstar}(x_i) / \\sum_j w_{\\bstar}(x_j)$, yielding continuous gradient contributions from all samples including those with intermediate $q$-scores.\nThis contrasts with the sampling-importance-resampling (SIR) approach of \\citet{drayson_2025_detection_collapse}, which discretely resamples a subset of the batch, introducing additional variance and discarding partial information from borderline samples.\n\n\\paragraph{Computational cost.}\nEach evaluation of $\\aeff$ or ESS costs $O(B)$ for batch size $B$.\nBisection requires $O(\\log(b_{\\max} / \\varepsilon))$ iterations, giving total per-batch overhead $O(B \\log(b_{\\max} / \\varepsilon))$---negligible compared to the $O(BHD)$ cost of transformer forward and backward passes with hidden dimension $H$ and depth $D$.\nWith $b_{\\max} = 20$ and $\\varepsilon = 0.01$, this amounts to ${\\sim}11$ iterations per batch.\n\n\\subsection{Hyperparameters}\n\\label{sec:hyperparameters}\n\nThe framework replaces the single sensitive exponent $b$ with two hyperparameters, $\\tau$ and $\\nmin$, both admitting principled defaults that transfer across settings without per-model tuning.\n\n\\paragraph{Quality threshold $\\tau$.}\n\\citet{wang_2026_survive_contamination} establish that pretraining convergence rate scales with effective real data proportion, motivating a quality threshold.\nHowever, their analysis assumes known mixture proportions; since we do not assume known $\\rho$, $\\tau$ is an empirical hyperparameter with theoretical motivation rather than a theoretically derived quantity.\nWe evaluate $\\tau \\in \\{0.5, 0.6, 0.7, 0.8, 0.9, 0.95\\}$ at $\\rho = 0.4$ (\\S\\ref{sec:results}).\nAll values in $[0.5, 0.8]$ improve over uniform training, with PPL spanning only $0.035$ across this range (17.688 at $\\tau{=}0.5$ to 17.653 at $\\tau{=}0.8$).\nWe adopt $\\tau = 0.8$ as the default.\nThe sensitivity is asymmetric: under-cleaning ($\\tau < 0.8$) yields mild degradation, while over-cleaning ($\\tau > 0.8$) causes sharper regression as $\\bstar$ inflates (mean $\\bstar = 2.36$ at $\\tau{=}0.9$ vs.\\ $1.40$ at $\\tau{=}0.8$), excessively suppressing borderline samples whose gradient signal remains useful.\n\n\\paragraph{ESS floor $\\nmin$.}\nThe stability constraint prevents gradient instability from weight concentration.\nAt $\\nmin = 1$ (effectively unconstrained), $\\bstar$ inflates to mean $7.20$ with 46.7\\% of batches exceeding $\\bstar = 2$, yielding PPL~$= 17.789$---worse than uniform ($17.694$) by $+0.095$, confirming that unconstrained downweighting is harmful.\nAt $\\nmin \\geq B$, the constraint forces $\\bstar = 0$ for all batches, recovering uniform training.\nWe use $\\nmin = 2$ (half the batch size for $B = 4$), which yields consistent improvement across three seeds (\\S\\ref{sec:results}).\n\n\\paragraph{Comparison with fixed $b$.}\nBoth $\\tau$ and $\\nmin$ admit wide effective ranges ($\\tau \\in [0.5, 0.8]$, $\\nmin \\in \\{2, 3\\}$) and can be set once without per-model adjustment.\nIn contrast, the fixed $b$ of \\citet{drayson_2025_detection_collapse} spans an order of magnitude across model scales and requires a clean validation set plus grid search costing up to $6{\\times}$ the training budget.\nOur adaptive $\\bstar$ eliminates this cost entirely.\n```\n\n---\n\n=== method.tex ===\n\n```\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\\label{sec:setup}\n\nLet $\\mathcal{D} = \\mathcal{D}_{\\mathrm{real}} \\cup \\mathcal{D}_{\\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.\nThe contamination ratio $\\rho = |\\mathcal{D}_{\\mathrm{synth}}| / |\\mathcal{D}|$ is unknown---a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\\citep{cheng_2025_contamination_survey}.\n\nA pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \\in [0,1]$.\nFollowing \\citet{drayson_2025_detection_collapse}, we weight each sample as\n\\begin{equation}\n  w(x) = (1 - q(x))^{b},\n  \\label{eq:weight}\n\\end{equation}\nwhere $b \\geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.\n\\citet{drayson_2025_detection_collapse} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\\leq}360$M parameters, $b{=}1$ for 1.7B).\nWe instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.\n\n\\subsection{Dual-Constraint Framework}\n\\label{sec:dual}\n\nGiven a batch $\\mathcal{B} = \\{x_1, \\ldots, x_B\\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.\n\n\\paragraph{Effective real proportion.}\nLet $r_i = \\mathbf{1}[q_i \\leq 0.5]$ estimate whether sample $x_i$ is human-authored.\nThe \\emph{effective real proportion}\n\\begin{equation}\n  \\alpha_{\\mathrm{eff}}(b) = \\frac{\\sum_{i=1}^{B} w_i(b) \\cdot r_i}{\\sum_{i=1}^{B} w_i(b)}\n  \\label{eq:alpha}\n\\end{equation}\nmeasures the share of total weight allocated to likely-real samples.\nAt $b = 0$, $\\alpha_{\\mathrm{eff}}$ equals the raw real fraction in the batch; increasing $b$ shifts weight toward low-$q$ samples, raising $\\alpha_{\\mathrm{eff}}$.\n\n\\paragraph{Effective sample size.}\nKish's effective sample size~\\citep{vehtari_2024_psis}\n\\begin{equation}\n  \\mathrm{ESS}(b) = \\frac{\\bigl(\\sum_{i=1}^{B} w_i(b)\\bigr)^{2}}{\\sum_{i=1}^{B} w_i(b)^{2}}\n  \\label{eq:ess}\n\\end{equation}\nquantifies how many equally-weighted samples the weighted batch is equivalent to.\n$\\mathrm{ESS}(0) = B$; as $b$ grows, a few high-$(1{-}q)$ samples dominate and $\\mathrm{ESS}$ drops toward~1.\n\n\\paragraph{Monotonicity.}\nThe two diagnostics exhibit opposing monotonicity in $b$:\n\n\\begin{proposition}\n\\label{prop:monotone}\nFor any batch containing both real and synthetic samples with distinct $q$-values, $\\alpha_{\\mathrm{eff}}(b)$ is strictly increasing in $b$.\n\\end{proposition}\n\n\\begin{proof}[Proof sketch]\nLet $\\pi_i(b) = w_i / \\sum_j w_j$ denote normalized weights.\nDifferentiating $\\alpha_{\\mathrm{eff}} = \\sum_i \\pi_i r_i$ yields\n$\\frac{d\\alpha_{\\mathrm{eff}}}{db} = \\mathrm{Cov}_{\\pi}\\!\\bigl(r_i,\\, \\ln(1{-}q_i)\\bigr)$.\nReal samples ($r_i = 1$) have $q_i \\leq 0.5$ and thus higher $\\ln(1{-}q_i)$, so this covariance is non-negative for any detector with better-than-random discrimination.\nFull derivation in Appendix~\\ref{app:proofs}.\n\\end{proof}\n\n\\noindent $\\mathrm{ESS}(b)$ is monotonically decreasing in $b$---larger exponents concentrate the weight distribution, a standard property of exponential tilting~\\citep{kimura_2024_iw_survey}.\n\n\\paragraph{Dual constraints.}\nWe impose two requirements on $b$:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{Quality floor}: $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$.\n  Convergence under contaminated training improves with the effective real fraction~\\citep{wang_2026_survive_contamination}; $\\tau$ sets the minimum acceptable quality level.\n  By Proposition~\\ref{prop:monotone}, this constraint defines a \\emph{lower bound} $b_\\tau = \\inf\\{b \\geq 0 : \\alpha_{\\mathrm{eff}}(b) \\geq \\tau\\}$.\n  \\item \\textbf{Stability ceiling}: $\\mathrm{ESS}(b) \\geq n_{\\min}$.\n  Overly concentrated weights yield high-variance gradients; $n_{\\min}$ prevents the batch from degenerating into a single effective sample.\n  Since $\\mathrm{ESS}$ is decreasing, this defines an \\emph{upper bound} $b_{\\mathrm{ESS}} = \\sup\\{b \\geq 0 : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$.\n\\end{enumerate}\nThe optimal exponent is\n\\begin{equation}\n  b^{*} = \\inf\\bigl\\{b \\geq 0 : \\alpha_{\\mathrm{eff}}(b) \\geq \\tau\\bigr\\} \\;\\;\\text{s.t.}\\;\\; \\mathrm{ESS}(b) \\geq n_{\\min}.\n  \\label{eq:bstar}\n\\end{equation}\nThis is the \\emph{minimum intervention principle}: apply the smallest $b$ that achieves the quality floor.\nBorderline samples---those with moderate $q$-values---still carry useful training signal; over-downweighting discards this signal unnecessarily.\nWhen both constraints are satisfiable ($b_\\tau \\leq b_{\\mathrm{ESS}}$), $b^{*} = b_\\tau$ and $\\alpha_{\\mathrm{eff}}$ is the binding constraint---$b^{*}$ lies well below the ESS ceiling.\nWhen they conflict ($b_\\tau > b_{\\mathrm{ESS}}$), the stability ceiling takes precedence: $b^{*} = b_{\\mathrm{ESS}}$, accepting a lower $\\alpha_{\\mathrm{eff}}$ to preserve gradient stability.\nFigure~\\ref{fig:dual_constraint} illustrates the feasible region and the three regimes.\n\n\\subsection{Algorithm}\n\\label{sec:algorithm}\n\nAlgorithm~\\ref{alg:bstar} computes $b^{*}$ for each training batch via bisection on the monotone functions $\\alpha_{\\mathrm{eff}}$ and $\\mathrm{ESS}$.\nEach batch falls into one of three regimes:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{Clean} ($\\alpha_{\\mathrm{eff}}(0) \\geq \\tau$): the quality floor holds at $b = 0$; no reweighting needed.\n  \\item \\textbf{$\\alpha_{\\mathrm{eff}}$-binding} ($b_\\tau \\leq b_{\\mathrm{ESS}}$): the quality constraint determines $b^{*} = b_\\tau$; $\\mathrm{ESS}$ remains above $n_{\\min}$ with margin.\n  \\item \\textbf{ESS-binding} ($b_\\tau > b_{\\mathrm{ESS}}$): the stability ceiling caps $b^{*} = b_{\\mathrm{ESS}}$.\n\\end{enumerate}\nAcross 51{,}913 micro-batches in our main experiment ($\\rho{=}0.4$, $\\tau{=}0.8$, $n_{\\min}{=}2$), 49.9\\% are clean, 20.2\\% are $\\alpha_{\\mathrm{eff}}$-binding, and 30.0\\% are ESS-binding.\nIn $\\alpha_{\\mathrm{eff}}$-binding batches, the solver selects $b^{*} = 1.67$ on average, while an ESS-only strategy would choose $b = 4.15$ on the same batches---2.5$\\times$ more aggressive.\nThe residual $\\mathrm{ESS} = 2.60$ in these batches (vs.\\ $n_{\\min} = 2.0$) confirms that the dual constraint prevents unnecessary over-downweighting.\n\n\\begin{algorithm}[t]\n\\caption{Per-batch adaptive $b^{*}$ selection}\n\\label{alg:bstar}\n\\begin{algorithmic}[1]\n\\Require Batch scores $\\{q_i\\}_{i=1}^{B}$, indicators $\\{r_i\\}$, quality threshold~$\\tau$, ESS floor~$n_{\\min}$, search bound~$b_{\\max}$, tolerance~$\\varepsilon$\n\\Ensure Optimal exponent $b^{*}$\n\\If{$\\alpha_{\\mathrm{eff}}(0) \\geq \\tau$}\n  \\State \\Return $0$ \\Comment{clean batch}\n\\EndIf\n\\State $b_\\tau \\gets \\Call{Bisect}{\\alpha_{\\mathrm{eff}}(\\cdot){=}\\tau,\\; [0, b_{\\max}],\\; \\varepsilon}$\n\\If{$\\mathrm{ESS}(b_\\tau) \\geq n_{\\min}$}\n  \\State \\Return $b_\\tau$ \\Comment{$\\alpha_{\\mathrm{eff}}$-binding}\n\\Else\n  \\State $b_{\\mathrm{ESS}} \\gets \\Call{Bisect}{\\mathrm{ESS}(\\cdot){=}n_{\\min},\\; [0, b_{\\max}],\\; \\varepsilon}$\n  \\State \\Return $b_{\\mathrm{ESS}}$ \\Comment{ESS-binding}\n\\EndIf\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Implementation.}\nGiven $b^{*}$, we compute normalized weights $\\pi_i = w_i(b^{*}) / \\sum_j w_j(b^{*})$ and form the weighted loss $\\mathcal{L} = \\sum_i \\pi_i \\ell_i$, where $\\ell_i$ is the per-sample cross-entropy.\nThis \\emph{loss reweighting} maintains continuous gradients, unlike the SIR resampling of \\citet{drayson_2025_detection_collapse} which introduces discrete sampling noise by drawing a subset proportional to $w_i$.\nEach bisection requires $\\mathcal{O}(B \\log(b_{\\max}/\\varepsilon))$ operations---with $B{=}4$, $b_{\\max}{=}20$, and $\\varepsilon{=}0.01$, roughly 44 floating-point operations per batch, negligible beside the forward and backward passes.\n\n\\subsection{Hyperparameters}\n\\label{sec:hyperparameters}\n\nThe framework introduces two hyperparameters, both with principled defaults set once across all experiments.\n\n\\paragraph{Quality threshold $\\tau$.}\nConvergence theory for contaminated training shows that convergence rate improves with the effective real fraction~\\citep{wang_2026_survive_contamination}, motivating a lower bound on $\\alpha_{\\mathrm{eff}}$.\nThe specific value of $\\tau$ is set empirically.\nWe find a wide safe range: $\\tau \\in [0.5, 0.8]$ consistently outperforms uniform training (Section~\\ref{sec:results}), with $\\tau = 0.8$ achieving the best perplexity.\nAbove 0.8, $b^{*}$ inflates rapidly (mean $b^{*} = 3.08$ at $\\tau = 0.95$), causing over-downweighting.\nWe use $\\tau = 0.8$ as the default throughout.\n\n\\paragraph{ESS floor $n_{\\min}$.}\nWe set $n_{\\min} = 2$ for batch size $B = 4$.\nThe constraint $n_{\\min} < B$ is necessary: $n_{\\min} \\geq B$ forces $b^{*} = 0$ on every batch, recovering uniform training.\nAt the other extreme, $n_{\\min} = 1$ effectively removes the stability constraint---mean $b^{*}$ rises to 7.20, with 46.7\\% of batches hitting the search ceiling at $b_{\\max}{=}20$, and perplexity degrades by $+0.14$ relative to $n_{\\min} = 2$.\nIn practice, $n_{\\min} \\in \\{2, 3\\}$ yields stable results across seeds (Section~\\ref{sec:results}).\n```\n\n---\n\n=== related_work_0b6096.tex ===\n\n```\n% Related Work for \"Minimum Intervention Reweighting: Adaptive Exponent Selection\n% for Contamination-Aware Pretraining\"\n% Generated: 2026-05-15\n% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)\n\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation---\\emph{model collapse} \\citep{shumailov2024model}.\n\\cite{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\nMore critically, \\cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.\nWith synthetic content now estimated at 20--60\\% of web corpora \\citep{cheng2025contamination}, these results motivate contamination-aware training strategies that explicitly account for data provenance rather than treating all tokens equally.\n\n\\paragraph{Detect and Reweight.}\nA natural response to contamination is to detect and remove synthetic content.\nDetectGPT \\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\% Prob \\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\\% tokens as a reference-free signal; both produce continuous confidence scores suitable as input to reweighting frameworks.\n\\cite{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples; \\cite{guo2025escaping} similarly rely on verification-based selection.\nSoft reweighting avoids the precision--recall threshold inherent in hard filtering by assigning continuous weights.\n\nMost directly related to our work, \\cite{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is a detector's synthetic probability.\nWe adopt the same weighting formula but differ in several fundamental ways.\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\leq}360$M parameters, $b{=}1$ for 1.7B), making the choice per-model and expensive.\nOur $\\bstar$ is derived per-batch from dual constraints ($\\aeff \\geq \\tau$, $\\mathrm{ESS} \\geq \\nmin$) at zero validation cost, following a minimum intervention principle that selects the smallest sufficient exponent.\n\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradient contributions.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\,=\\,0.939) suffices on FineWeb-scale data (132M+ tokens).\n\n\\paragraph{Data Mixing and Reweighting.}\nA parallel line of work optimizes data composition without targeting synthetic contamination.\nAt the \\emph{domain} level, DoReMi \\citep{xie2023doremi} learns mixture weights via Group DRO with a proxy model, DSIR \\citep{xie2023dsir} performs importance resampling with $n$-gram features, \\cite{ye2025mixing} discover predictable functional forms relating mixing ratios to performance, and AIOLI \\citep{chen2025aioli} unifies these into an online adaptive framework.\nThese methods operate at the domain level and do not address instance-level contamination within a domain.\nAt the \\emph{instance} level, SoftDedup \\citep{he2024softdedup} downweights high-frequency samples via $n$-gram commonness, and \\cite{sow2025dynamic} derive sample weights from per-sample loss with convergence guarantees.\nOur reweighting differs from all of these in being driven by \\emph{provenance}---detector scores estimating human vs.\\ machine origin---rather than loss, frequency, or domain membership.\n\n\\paragraph{Theoretical Foundations.}\n\\cite{he2025golden} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\\approx}0.62$) optimal when both sources are equally sized; their result requires the contamination ratio, unavailable in web-scale settings.\n\\cite{wang2026survive} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\aeff(b) \\geq \\tau$ guarantees a convergence-rate lower bound.\nWe operationalize this without the known-proportion assumption, estimating $\\aeff$ from batch-level statistics online.\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \\cite{vehtari2024psis}.\n\\cite{kimura2024iw} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as covariate-shift correction where the covariate is synthetic origin probability.\n\n\\smallskip\n\\noindent\\textbf{Summary.}\nNo existing method provides principled per-batch exponent selection without validation.\nDrayson et al.\\ use the same $w{=}(1{-}q)^b$ formula but require per-model grid search; Golden Ratio weighting requires known mixture proportions; DoReMi and DSIR operate at the domain level rather than instance-level contamination.\nOur dual-constraint framework fills this gap by deriving the minimum intervention $\\bstar$ from batch-level diagnostics alone.\n```\n\n---\n\n=== related_work.tex ===\n\n```\n\\section{Related Work}\n\n\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation---\\emph{model collapse}~\\citep{shumailov_2024_model_collapse}.\n\\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\nMore critically, \\citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.\n\\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\\% of web corpora.\nThese results motivate \\emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.\n\n\\paragraph{Detection and Filtering of Machine-Generated Text.}\nGiven the severity of contamination, a natural response is to detect and remove synthetic content.\nDetectGPT~\\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\% Prob~\\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\\% tokens as a reference-free signal.\nBoth produce continuous confidence scores suitable as input to downstream weighting---including ours.\nOn the mitigation side, \\citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.\n\\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.\nHard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.\n\nMost directly related to our work, \\citet{drayson_2025_detection_collapse} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic probability.\nWe adopt the same weighting formula but differ in several fundamental ways.\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\leq}360$M, $b{=}1$ for 1.7B), making the choice \\emph{per-model} and expensive.\nOur $b^*$ is derived per-batch from dual constraints ($\\alpha_{\\mathrm{eff}} \\geq \\tau$, $\\mathrm{ESS} \\geq n_{\\min}$) at zero validation cost.\n\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradients.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\,=\\,0.939) suffices on FineWeb-scale data (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.\n\n\\paragraph{Data Mixing and Instance-Level Reweighting.}\nA parallel line of work optimizes data composition without targeting synthetic contamination.\nAt the \\emph{domain} level, DoReMi~\\citep{xie_2023_doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\\citep{xie_2023_dsir} performs importance resampling with $n$-gram features, and \\citet{ye_2025_data_mixing_laws} discover predictable functional forms relating mixing ratios to performance.\nAIOLI~\\citep{chen_2025_aioli} unifies these into an online adaptive framework, while \\citet{yang_2026_data_mixing_agent} train an RL agent for domain-weight selection.\nThese methods do not address instance-level contamination within a domain.\nAt the \\emph{instance} level, SoftDedup~\\citep{he_2024_softdedup} downweights high-frequency samples via $n$-gram commonness, \\citet{sow_2025_dynamic_reweighting} derive sample weights from per-sample loss with convergence guarantees, and \\citet{kuo_2024_data_weighting} show that differentiated weighting of LLM-generated data improves downstream classification.\nOur reweighting differs from all of these in being driven by \\emph{provenance}---detector scores estimating human vs.\\ synthetic origin---rather than loss, frequency, or domain membership.\n\n\\paragraph{Theoretical Foundations.}\n\\citet{he_2025_golden_ratio} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\\approx}0.62$) optimal when both sources are equally sized.\nTheir result requires the contamination ratio $k$, unavailable in web-scale settings; we use it as an oracle baseline.\n\\citet{wang_2026_survive_contamination} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ guarantees a convergence-rate lower bound.\nWe operationalize this without the known-proportion assumption, estimating $\\alpha_{\\mathrm{eff}}$ from batch-level statistics online.\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \\citet{vehtari_2024_psis}.\n\\citet{kimura_2024_iw_survey} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as a special case of covariate-shift correction where the covariate is synthetic origin probability.\n```\n\n---\n\n=== experiments_86dfd1.tex ===\n\n```\n\\section{Experimental Setup}\n\\label{sec:experiments}\n\n\\paragraph{Training Data.}\nWe sample a 132M-token subset of FineWeb~\\citep{penedo_2024_fineweb} as the real-data source.\nTo simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\\citep{yang_2025_qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\\rho = 0.4$ via uniform random mixing.\nThis self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.\n\n\\paragraph{Detector.}\nWe train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\\,=\\,0.939 with calibrated ECE\\,=\\,0.048 after temperature scaling ($T = 0.204$).\nThe resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\\% of samples in the uncertain range $[0.2, 0.8]$.\nWe use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\\,${\\geq}$\\,0.98 in \\citealt{drayson_2025_detection_collapse}) to test whether score \\emph{calibration} matters more than raw discrimination for reweighting.\n\n\\paragraph{Training.}\nWe continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\\,=\\,$5{\\times}10^{-5}$), max sequence length 2048, and bf16 precision.\nAll main comparisons use three random seeds (42, 123, 456).\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).\nAll evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.\n\n\\paragraph{Methods.}\nWe compare five approaches:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).\n  \\item \\textbf{Grid-$b$}: fixed $b \\in \\{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\}$, best selected post-hoc by held-out PPL.\n        Represents validation-based selection~\\citep{drayson_2025_detection_collapse}.\n  \\item \\textbf{ESS-only}: $b^* = \\max\\{b : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\\alpha_{\\mathrm{eff}}$.\n  \\item \\textbf{Golden Ratio}: $w = 1/\\varphi \\approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\\citep{he_2025_golden_ratio}.\n        Requires known provenance labels (oracle).\n  \\item \\textbf{Adaptive} (ours): per-batch $b^*$ from the dual-constraint formulation (\\S\\ref{sec:method}), with $\\tau = 0.8$ and $n_{\\min} = 2$ (half the micro-batch size).\n\\end{itemize}\n```\n\n---\n\n=== experiments.tex ===\n\n```\n\\section{Experimental Setup}\n\\label{sec:experiments}\n\n\\paragraph{Training Data.}\nWe sample a 132M-token subset of FineWeb~\\citep{penedo_2024_fineweb} as the real-data source.\nTo simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\\citep{yang_2025_qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\\rho = 0.4$ via uniform random mixing.\nThis self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.\n\n\\paragraph{Detector.}\nWe train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\\,=\\,0.939 with calibrated ECE\\,=\\,0.048 after temperature scaling ($T = 0.204$).\nThe resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\\% of samples in the uncertain range $[0.2, 0.8]$.\nWe use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\\,${\\geq}$\\,0.98 in \\citealt{drayson_2025_detection_collapse}) to test whether score \\emph{calibration} matters more than raw discrimination for reweighting.\n\n\\paragraph{Training.}\nWe continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\\,=\\,$5{\\times}10^{-5}$), max sequence length 2048, and bf16 precision.\nAll main comparisons use three random seeds (42, 123, 456).\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).\nAll evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.\n\n\\paragraph{Methods.}\nWe compare five approaches:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).\n  \\item \\textbf{Grid-$b$}: fixed $b \\in \\{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\}$, best selected post-hoc by held-out PPL.\n        Represents validation-based selection~\\citep{drayson_2025_detection_collapse}.\n  \\item \\textbf{ESS-only}: $b^* = \\max\\{b : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\\alpha_{\\mathrm{eff}}$.\n  \\item \\textbf{Golden Ratio}: $w = 1/\\varphi \\approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\\citep{he_2025_golden_ratio}.\n        Requires known provenance labels (oracle).\n  \\item \\textbf{Adaptive} (ours): per-batch $b^*$ from the dual-constraint formulation (\\S\\ref{sec:method}), with $\\tau = 0.8$ and $n_{\\min} = 2$ (half the micro-batch size).\n\\end{itemize}\n```\n\n---\n\n=== results_d0d647.tex ===\n\n```\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Comparison}\n\nTable~\\ref{tab:main} reports held-out perplexity across methods and seeds.\nAdaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).\nThis parity comes at zero validation cost---grid search requires $|\\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.\n\nThe grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\\ref{app:grid}), confirming that exponent selection is consequential.\nThe optimal $b{=}0.5$ differs from the $b{=}10$ reported by \\citet{drayson_2025_detection_collapse} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.\n\n% Claim 1: Dual > ESS-only (3 seeds)\nESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \\emph{worse} than uniform (17.694) by 0.029.\nThe degradation is consistent: ESS-only exceeds uniform on every individual seed (Table~\\ref{tab:main}), ruling out seed-specific artifacts.\nRemoving $\\alpha_{\\mathrm{eff}}$ and maximizing $b$ subject only to $\\mathrm{ESS} \\geq n_{\\min}$ leads to systematic over-downweighting, providing direct evidence for the minimum-intervention principle.\nConversely, adaptive (dual) improves over uniform on all three seeds (by 0.041, 0.043, and 0.045 respectively), confirming that the $\\alpha_{\\mathrm{eff}}$ quality floor prevents the over-intervention that plagues ESS-only.\n\nThe Golden Ratio oracle~\\citep{he_2025_golden_ratio} achieves PPL 17.654 on seed 42 using known provenance labels.\nAdaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.\n\nThe adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.\nThe constraint regime breakdown in \\S\\ref{sec:algorithm} shows that $\\alpha_{\\mathrm{eff}}$ prevents over-intervention in the 40\\% of reweighted batches where moderate $b$ already meets the quality target.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 456} & \\textbf{Mean} \\\\\n\\midrule\nUniform               & 17.694 & 17.686 & 17.702 & 17.694 \\\\\nGrid-best ($b{=}0.5$) & \\textbf{17.651} & \\textbf{17.638} & \\textbf{17.650} & \\textbf{17.646} \\\\\nESS-only               & 17.730 & 17.720 & 17.719 & 17.723 \\\\\nGolden Ratio$^\\dagger$ & 17.654 & --     & --     & --     \\\\\n\\midrule\nAdaptive (ours)        & 17.653 & 17.643 & 17.657 & 17.651 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Held-out perplexity (PPL, $\\downarrow$).\nGrid-best selects the optimal fixed $b$ post-hoc from six candidates.\n$^\\dagger$Evaluated on seed 42 only.\nBest per column in \\textbf{bold}.}\n\\label{tab:main}\n\\end{table}\n\n\\subsection{Sensitivity Analysis}\n\n\\paragraph{Quality threshold $\\tau$.}\nTable~\\ref{tab:tau} varies $\\tau$ while holding $n_{\\min} = 2$ (seed 42).\nAll values in $\\tau \\in [0.5, 0.8]$ improve over uniform, with $\\tau = 0.8$ achieving the lowest PPL (17.653).\nHigher $\\tau$ demands greater $\\alpha_{\\mathrm{eff}}$, forcing the solver to increase $b^*$: mean $\\bar{b}^*$ rises monotonically from 0.39 at $\\tau{=}0.5$ to 3.08 at $\\tau{=}0.95$.\nBelow 0.8, reweighting is too gentle to fully exploit the detector signal; above, $b^*$ inflates past diminishing returns and PPL degrades.\nThe range $[0.5, 0.8]$ provides a wide safe operating region, with $\\tau = 0.8$ as the recommended default.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\tau$ & \\textbf{PPL} & $\\Delta_{\\mathrm{unif}}$ & $\\bar{b}^*$ \\\\\n\\midrule\n0.50 & 17.688 & $-$0.006 & 0.39 \\\\\n0.60 & 17.681 & $-$0.013 & 0.59 \\\\\n0.70 & 17.679 & $-$0.015 & 0.89 \\\\\n\\textbf{0.80} & \\textbf{17.653} & $\\mathbf{-0.041}$ & \\textbf{1.40} \\\\\n0.90 & 17.712 & $+$0.018 & 2.36 \\\\\n0.95 & 17.723 & $+$0.029 & 3.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to $\\tau$ (seed 42, $n_{\\min}{=}2$, $\\rho{=}0.4$).\n$\\Delta_{\\mathrm{unif}}$: PPL change vs.\\ uniform baseline (17.694).\n$\\bar{b}^*$: mean adaptive exponent across batches.}\n\\label{tab:tau}\n\\end{table}\n\n\\paragraph{Minimum ESS $n_{\\min}$.}\nTable~\\ref{tab:nmin} ablates $n_{\\min}$ at batch size $B{=}4$.\nRemoving the ESS floor ($n_{\\min} = 1$) allows $b^*$ to inflate to mean 7.20, degrading PPL to 17.789---0.095 worse than uniform.\nAt $n_{\\min} = 2$ ($= \\lfloor B/2 \\rfloor$), $b^*$ is constrained to mean 1.40 and PPL reaches 17.653, verified across three seeds.\nAt $n_{\\min} = B = 4$, the ESS constraint is trivially satisfied at $b^* = 0$ for every batch, and PPL reverts to the uniform level (17.695 vs.\\ 17.694).\nThe results exhibit a U-shaped pattern: too-low $n_{\\min}$ permits over-downweighting, while $n_{\\min}$ at or near $B$ removes the ability to reweight.\n\nThe coupling between $n_{\\min}$ and $B$ extends beyond the $B{=}4$ setting.\nAt batch size $B{=}8$ with $n_{\\min}{=}2$, the ESS range $[2, 8]$ is wide enough that the stability constraint rarely binds, yielding PPL 17.73---comparable to ESS-only and 0.036 worse than uniform.\nThis confirms that $n_{\\min}$ must scale with $B$: a fixed $n_{\\min}$ that works for one batch size can degrade to near-ESS-only behavior at larger $B$.\nThe rule $n_{\\min} = \\max(2, \\lfloor B/2 \\rfloor)$ keeps the ESS constraint active without over-restricting the solver, and we recommend it as a practical default.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}ccc@{}}\n\\toprule\n$n_{\\min}$ & \\textbf{PPL} & $\\bar{b}^*$ \\\\\n\\midrule\n1 & 17.789 & 7.20 \\\\\n\\textbf{2} & \\textbf{17.653} & \\textbf{1.40} \\\\\n3$^\\ddagger$ & 17.644 & 1.43 \\\\\n4 & 17.695 & 0.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to $n_{\\min}$ (seed 42, $B{=}4$, $\\tau{=}0.8$).\n$n_{\\min} = 4 = B$ forces $b^* = 0$ on all batches, recovering uniform weighting.\n$^\\ddagger$From an earlier adaptive configuration; not an independent ablation.}\n\\label{tab:nmin}\n\\end{table}\n```\n\n---\n\n=== results.tex ===\n\n(Identical content to results_d0d647.tex — same verbatim text, no differences.)\n\n---\n\n=== discussion_270aaa.tex ===\n\n```\n\\paragraph{Why minimum intervention works.}\nThe central finding of our experiments is that restraint in downweighting outperforms aggressiveness.\nESS-only reweighting---which maximizes $b$ subject only to $\\mathrm{ESS} \\geq \\nmin$---degrades PPL to 17.723, \\emph{worse} than the uniform baseline (17.694, Table~\\ref{tab:main}).\nThe dual-constrained adaptive $\\bstar$, by contrast, achieves 17.651 by selecting the \\emph{smallest} $b$ that meets the quality floor $\\tau$.\nThe mechanism is clear from the binding statistics: in the 40.1\\% of reweighted batches where $\\aeff$ binds, mean $\\bstar = 1.67$ versus 4.15 under ESS-only---a 2.5$\\times$ less aggressive exponent that retains ESS\\,=\\,2.60, well above the floor $\\nmin = 2$.\nOver-downweighting discards gradient signal from borderline samples whose detector scores are intermediate (e.g., $q \\approx 0.4$--$0.6$); these samples carry partial but non-negligible training value, and aggressively suppressing them impoverishes the effective training distribution.\nThe $\\aeff$ constraint prevents this by halting $b$ as soon as the quality target is met.\n\n\\paragraph{$\\tau$ as a practical dial.}\nThe quality threshold $\\tau$ controls the trade-off between decontamination strength and sample retention.\nOur sweep (Table~\\ref{tab:tau}) reveals a wide safe operating range: all $\\tau \\in [0.5, 0.8]$ outperform uniform training, with PPL varying only 0.035 across this interval.\nThe sensitivity is asymmetric---under-cleaning ($\\tau < 0.8$) incurs mild degradation ($-$0.006 to $-$0.015 vs.\\ uniform), while over-cleaning ($\\tau > 0.8$) causes sharper regression as $\\bstar$ inflates (mean $\\bar{b}^* = 2.36$ at $\\tau{=}0.9$, 3.08 at $\\tau{=}0.95$).\nThis asymmetry reinforces the minimum intervention intuition: the cost of doing too little is small, whereas the cost of doing too much is steep.\nWe recommend $\\tau = 0.8$ as a principled default; practitioners operating at different contamination rates can adjust within the safe range with low risk.\n\n\\paragraph{Connection to convergence theory.}\n\\citet{wang_2026_survive_contamination} prove that pretraining convergence rate scales with $\\alpha$, the effective real data fraction.\nOur $\\tau$ serves an analogous role---setting a floor on the weighted real proportion per batch---but an important distinction must be noted: their analysis assumes a known contamination proportion, whereas our method estimates quality from detector scores without access to the true $\\alpha$.\nWe therefore position $\\tau$ as an empirical hyperparameter with theoretical motivation: convergence theory explains \\emph{why} a quality threshold improves training, while the specific value of $\\tau$ is determined empirically.\nBridging this gap---deriving $\\tau$ from first principles without known proportions---is an open theoretical question.\n```\n\n---\n\n=== discussion.tex ===\n\n```\n\\paragraph{Why minimum intervention works.}\nThe central finding of our experiments is that restraint in downweighting outperforms aggressiveness.\nESS-only reweighting---which maximizes $b$ subject only to $\\mathrm{ESS} \\geq \\nmin$---degrades PPL to 17.723, \\emph{worse} than the uniform baseline (17.694, Table~\\ref{tab:main}).\nThe dual-constrained adaptive $\\bstar$, by contrast, achieves 17.651 by selecting the \\emph{smallest} $b$ that meets the quality floor $\\tau$.\nThe mechanism is clear from the binding statistics: in the 40.1\\% of reweighted batches where $\\aeff$ binds, mean $\\bstar = 1.67$ versus 4.15 under ESS-only---a 2.5$\\times$ less aggressive exponent that retains ESS\\,=\\,2.60, well above the floor $\\nmin = 2$.\nOver-downweighting discards gradient signal from borderline samples whose detector scores are intermediate (e.g., $q \\approx 0.4$--$0.6$); these samples carry partial but non-negligible training value, and aggressively suppressing them impoverishes the effective training distribution.\nThe $\\aeff$ constraint prevents this by halting $b$ as soon as the quality target is met.\n\n\\paragraph{$\\tau$ as a practical dial.}\nThe quality threshold $\\tau$ controls the trade-off between decontamination strength and sample retention.\nOur sweep (Table~\\ref{tab:tau}) reveals a wide safe operating range: all $\\tau \\in [0.5, 0.8]$ outperform uniform training, with PPL varying only 0.035 across this interval.\nThe sensitivity is asymmetric---under-cleaning ($\\tau < 0.8$) incurs mild degradation ($-$0.006 to $-$0.015 vs.\\ uniform), while over-cleaning ($\\tau > 0.8$) causes sharper regression as $\\bstar$ inflates (mean $\\bar{b}^* = 2.36$ at $\\tau{=}0.9$, 3.08 at $\\tau{=}0.95$).\nThis asymmetry reinforces the minimum intervention intuition: the cost of doing too little is small, whereas the cost of doing too much is steep.\nWe recommend $\\tau = 0.8$ as a principled default; practitioners operating at different contamination rates can adjust within the safe range with low risk.\n\n\\paragraph{Connection to convergence theory.}\n\\citet{wang2026survive} prove that pretraining convergence rate scales with $\\alpha$, the effective real data fraction.\nOur $\\tau$ serves an analogous role---setting a floor on the weighted real proportion per batch---but an important distinction must be noted: their analysis assumes a known contamination proportion, whereas our method estimates quality from detector scores without access to the true $\\alpha$.\nWe therefore position $\\tau$ as an empirical hyperparameter with theoretical motivation: convergence theory explains \\emph{why} a quality threshold improves training, while the specific value of $\\tau$ is determined empirically.\nBridging this gap---deriving $\\tau$ from first principles without known proportions---is an open theoretical question.\n```\n\n---\n\n=== conclusion_386ecc.tex ===\n\n```\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced Minimum Intervention Reweighting, a dual-constrained framework for contamination-aware pretraining that selects per-batch exponents $b^*$ without validation data.\nThe method finds the smallest $b$ satisfying $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ subject to $\\mathrm{ESS}(b) \\geq n_{\\min}$, enforcing a minimum-intervention principle: apply only as much downweighting as needed to meet a quality floor, no more.\nThis stands in direct contrast to ESS-only (maximum-intervention) strategies, which we show degrade performance below even uniform baselines by over-downweighting contaminated samples.\n\nAcross three seeds at 0.6B scale with 40\\% synthetic contamination, adaptive $b^*$ matches grid-search-optimal PPL (17.651 vs.\\ 17.646) within seed variance, eliminating the $|\\mathcal{B}|$-run grid search entirely.\nThe quality threshold $\\tau$ is robust across $[0.5, 0.8]$---all values in this range outperform uniform weighting.\nA lightweight TF-IDF + logistic regression detector (AUC\\,0.94) suffices when post-hoc calibrated (ECE\\,0.048); score calibration matters more than raw discriminative power.\nThe batch-level constraint regime---49.9\\% clean (no reweighting needed), 20.2\\% $\\alpha_{\\mathrm{eff}}$-binding, 30.0\\% ESS-binding---confirms that both constraints are active and complementary in practice.\n\n\\section*{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Scale.}\nAll experiments use a single model size (Qwen3-0.6B) with batch size 4.\nBatch-level $q$-score statistics concentrate differently at larger batch sizes typical of 3B+ training; the optimal $\\tau$ range and constraint dynamics may shift at scale.\n\n\\paragraph{Contamination distribution.}\nWe inject synthetic data via uniform random mixing at a controlled ratio ($\\rho{=}0.4$).\nReal web-scale contamination is domain-skewed, which may alter within-batch $\\alpha_{\\mathrm{eff}}$ distributions and require domain-aware extensions.\n\n\\paragraph{Detector coverage.}\nWe evaluate one detector family (TF-IDF + logistic regression).\nAlthough our results suggest calibration dominates discrimination for reweighting quality, a systematic ablation across detector architectures and quality levels is needed.\n\n\\paragraph{Threshold.}\n$\\tau$ is an empirical hyperparameter.\nThe convergence theory of \\citet{wang_2026_survive_contamination} assumes a known contamination proportion $\\alpha$, which we do not require; bridging this gap to derive $\\tau$ from first principles remains open.\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity only.\nDownstream task evaluation (MMLU, HellaSwag) would strengthen the practical case, particularly at scales where PPL differences translate more reliably to task performance.\n\n\\paragraph{Effect size.}\nThe PPL improvement over uniform weighting is 0.043 at 0.6B/40\\% contamination.\nWhile consistent across seeds, this effect is modest; we expect amplification at higher contamination ratios and larger model scales, but verification is ongoing.\n```\n\n---\n\n=== conclusion.tex ===\n\n(Identical content to conclusion_386ecc.tex — same verbatim text, no differences.)\n\n---\n\n=== table1_main_results.tex ===\n\n```\n\\begin{table}[t]\n\\centering\n\\caption{Held-out perplexity under different weighting methods ($\\rho{=}0.4$, 3 seeds). $\\Delta$ is relative to the Uniform baseline.}\n\\label{tab:main-results}\n\\small\n\\begin{tabular}{@{}lccccr@{}}\n\\toprule\nMethod & seed42 & seed123 & seed456 & Mean$\\pm$Std & $\\Delta$ \\\\\n\\midrule\nUniform                                  & 17.694 & 17.686 & 17.702 & 17.694$\\pm$0.008 & --- \\\\\nGrid-best ($b{=}0.5$)                    & 17.651 & 17.638 & 17.650 & 17.646$\\pm$0.007 & $-$0.048 \\\\\nAdaptive ($\\tau{=}0.8$, $n_{\\min}{=}3$\\textsuperscript{\\dag}) & 17.644 & 17.631 & 17.642 & \\textbf{17.639$\\pm$0.007} & $-$\\textbf{0.055} \\\\\nAdaptive-fix ($\\tau{=}0.8$, $n_{\\min}{=}2$) & 17.653 & 17.643 & 17.657 & 17.651$\\pm$0.007 & $-$0.043 \\\\\nESS-only                                 & 17.730 & 17.720 & 17.719 & 17.723$\\pm$0.006 & $+$0.029 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{\\dag}$n_{\\min}{=}3$ is the original implementation (historical); $n_{\\min}{=}2$ is the theoretically derived correction.}\n\\end{table}\n```\n\n---\n\nAll 15 files have been returned verbatim. Note: `results_d0d647.tex` and `results.tex` are byte-for-byte identical, as are `conclusion_386ecc.tex` and `conclusion.tex`. The `discussion_270aaa.tex` and `discussion.tex` differ in only one citation key: `\\citet{wang_2026_survive_contamination}` (versioned) vs `\\citet{wang2026survive}` (base). The `table1_main_results.tex` contains a materially different table from the inline table in the results files — it includes an `Adaptive ($n_{\\min}{=}3$)` row showing PPL 17.639 (better than grid-best) and an `Adaptive-fix ($n_{\\min}{=}2$)` row at 17.651, whereas the results section tables only show `Adaptive (ours)` at 17.651 without the $n_{\\min}{=}3$ variant."
5	  },
6	  {
7	    "type": "text",
8	    "text": "agentId: ac7fd3aa5a6be52f9 (use SendMessage with to: 'ac7fd3aa5a6be52f9' to continue this agent)\n&lt;usage>total_tokens: 63594\ntool_uses: 15\nduration_ms: 337182&lt;/usage>"
9	  }
10	]
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "30ffc82d-abf2-47e8-ac59-aac5dcbe9328",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/aa969b71-d198-4ba3-9b84-63a2c341d557/tool-results/toolu_01JwscEPDwAWYsvzEyjiYamw.json",
      "content": "[\n  {\n    \"type\": \"text\",\n    \"text\": \"Here are all 15 files, verbatim:\\n\\n---\\n\\n=== introduction_c6a67f.tex ===\\n\\n```\\n% Introduction for \\\"Minimum Intervention Reweighting: Adaptive Exponent Selection\\n% for Contamination-Aware Pretraining\\\"\\n% Generated: 2026-05-15\\n% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)\\n\\n\\\\section{Introduction}\\n\\\\label{sec:intro}\\n\\nWeb pretraining corpora are increasingly contaminated by machine-generated text, with recent estimates placing the synthetic fraction between 20\\\\% and 60\\\\% \\\\citep{cheng2025contamination}.\\nThis poses a fundamental threat to model quality: \\\\cite{shumailov2024model} demonstrate that training on recursively generated data leads to irreversible model collapse, and \\\\cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger degradation, ruling out data scaling as a remedy.\\nAs synthetic content becomes ubiquitous, \\\\emph{contamination-aware training}---strategies that explicitly account for data provenance during optimization---is necessary for maintaining pretraining quality.\\n\\nA natural mitigation is detect-and-reweight: assign each sample a weight $w(x) = (1 - q(x))^b$ based on a detector's estimated synthetic probability $q(x)$, where larger $b$ downweights suspected synthetic text more aggressively \\\\citep{drayson2025detection}.\\nHowever, the exponent $b$ is a sensitive per-model hyperparameter whose optimal value varies by an order of magnitude across model scales---$b = 1$ for SmolLM-1.7B versus $b = 10$ for GPT-2 124M---and selecting it requires a clean validation set and grid search costing up to $6{\\\\times}$ the base training budget.\\nThe practical question is: \\\\emph{given per-sample detector scores $q(x)$, how should $b$ be chosen without validation?}\\n\\nWe propose a \\\\emph{dual-constraint framework} that derives the exponent adaptively per batch from two diagnostics computed on the detector scores alone.\\nThe effective real proportion $\\\\aeff(b)$ measures the weighted fraction of gradient signal from real data and imposes a \\\\emph{quality floor}: $\\\\aeff(b) \\\\geq \\\\tau$---at least enough cleaning.\\nKish's effective sample size $\\\\mathrm{ESS}(b)$ \\\\citep{vehtari2024psis} quantifies weight concentration and imposes a \\\\emph{stability ceiling}: $\\\\mathrm{ESS}(b) \\\\geq \\\\nmin$---not so much cleaning that gradient estimates degrade.\\nA key structural insight makes this tractable: $\\\\aeff$ is strictly increasing in $b$ while $\\\\mathrm{ESS}$ is strictly decreasing, so the quality constraint yields a unique lower bound $\\\\btau$ and the stability constraint a unique upper bound $\\\\bess$.\\nWe adopt a \\\\emph{minimum intervention principle}:\\n\\\\begin{equation*}\\n  \\\\bstar = \\\\inf\\\\{b \\\\geq 0 : \\\\aeff(b) \\\\geq \\\\tau\\\\} \\\\quad \\\\text{subject to} \\\\quad \\\\mathrm{ESS}(\\\\bstar) \\\\geq \\\\nmin,\\n\\\\end{equation*}\\nthe smallest exponent satisfying the quality floor.\\nThis is deliberately conservative: apply enough decontamination to meet the quality target, but no more, preserving the largest possible effective sample size.\\nIn practice, batches fall into three regimes---already clean ($\\\\bstar{=}0$), quality-binding ($\\\\bstar{=}\\\\btau$), and stability-binding ($\\\\bstar{=}\\\\bess$)---allowing the framework to handle heterogeneous contamination naturally.\\nUnlike the discrete sampling-importance-resampling of \\\\cite{drayson2025detection}, we implement reweighting through direct loss scaling with continuous gradient contributions.\\n\\nWe evaluate on continued pretraining of Qwen3-0.6B on 132M FineWeb \\\\citep{penedo2024fineweb} tokens with 40\\\\% synthetic contamination (\\\\S\\\\ref{sec:experiments}).\\nAdaptive $\\\\bstar$ with default hyperparameters ($\\\\tau{=}0.8$, $\\\\nmin{=}2$) matches the grid-search-optimal fixed $b$ within seed variance (PPL $17.650 {\\\\pm} 0.007$ vs.\\\\ $17.646 {\\\\pm} 0.007$ across three seeds) at zero validation cost.\\nIt outperforms both uniform training (PPL $17.69$) and ESS-only maximum intervention (PPL $17.73$), confirming that minimum intervention is superior to maximum intervention.\\nA lightweight TF-IDF + logistic regression detector (AUC\\\\,=\\\\,0.939) suffices for effective reweighting, and the quality threshold $\\\\tau$ admits a wide safe range of $[0.5, 0.8]$ within which all tested values improve over uniform training.\\n\\nOur contributions are:\\n\\\\begin{enumerate}[nosep,leftmargin=*]\\n  \\\\item A dual-constraint framework for adaptive $\\\\bstar$ selection with minimum intervention semantics, providing validation-free per-batch exponent derivation from batch-level diagnostics (\\\\S\\\\ref{sec:method}).\\n  \\\\item Empirical evidence that adaptive $\\\\bstar$ matches grid-search-optimal performance within seed variance at zero validation cost, and that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only) (\\\\S\\\\ref{sec:results}).\\n  \\\\item Evidence that a lightweight TF-IDF + logistic regression detector suffices for effective reweighting (\\\\S\\\\ref{sec:results}).\\n\\\\end{enumerate}\\n```\\n\\n---\\n\\n=== introduction.tex ===\\n\\n```\\nWeb corpora increasingly contain machine-generated text.\\nRecent estimates place the synthetic fraction at 20--60\\\\% of crawled data~\\\\citep{cheng_2025_contamination_survey}, and this share grows as language models are deployed for content production at scale.\\nTraining on such contaminated data has concrete consequences: \\\\citet{shumailov_2024_model_collapse} show that recursive training on model outputs leads to irreversible quality degradation---\\\\emph{model collapse}---and \\\\citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.\\nA central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.\\nThe prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.\\n\\nA natural response is \\\\emph{detect-and-reweight}: train a classifier to estimate each sample's synthetic probability $q(x)$, then suppress likely-synthetic samples via the weighting function $w(x) = (1 - q(x))^b$.\\n\\\\citet{drayson_2025_detection_collapse} demonstrate this approach for model collapse prevention and show that the exponent $b$ critically determines outcomes---their optimal values range from $b{=}10$ for models at ${\\\\leq}360$M parameters to $b{=}1$ at 1.7B, and misspecification degrades results substantially.\\nSelecting $b$ therefore requires per-model validation-set grid search, with computational cost scaling linearly in the number of candidates (six training runs in a typical sweep).\\nOther approaches assume even stronger supervision: \\\\citet{he_2025_golden_ratio} derive theoretically optimal weights from convergence analysis but require the exact contamination ratio $\\\\rho$, which is precisely what is unavailable in practice.\\nHard detection-and-removal strategies~\\\\citep{feng_2025_beyond_collapse} discard borderline samples entirely, sacrificing the smooth reweighting that continuous $q$-scores enable.\\n\\nGiven per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?\\nWe formulate this as a dual-constrained optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\\\\aeff(b)$ reaches a quality threshold $\\\\tau$, while keeping Kish's effective sample size $\\\\mathrm{ESS}(b)$ above a stability floor $\\\\nmin$.\\nThe quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effective real-data fraction~\\\\citep{wang_2026_survive_contamination}, motivating a lower bound on $\\\\aeff$.\\nThe stability constraint prevents extreme weight concentration that degrades gradient quality.\\nThese two requirements exhibit a natural opposition.\\n$\\\\aeff(b)$ increases monotonically in $b$ (Proposition~\\\\ref{prop:monotone}), yielding a lower bound $\\\\btau$---the minimum exponent needed to achieve the target quality.\\n$\\\\mathrm{ESS}(b)$ decreases monotonically, yielding an upper bound $\\\\bess$---the maximum exponent before gradient stability degrades.\\nThe adaptive exponent $\\\\bstar = \\\\btau$ when the feasible region $[\\\\btau, \\\\bess]$ is non-empty, embodying a \\\\emph{minimum intervention principle}: apply the least downweighting sufficient to meet the quality target, preserving as much effective training data as possible.\\nWhen the constraints conflict ($\\\\btau > \\\\bess$), the stability ceiling takes precedence.\\n\\nThis minimum-intervention semantics distinguishes the method from the alternative of maximizing $b$ subject only to ESS stability.\\nAmong batches that require reweighting, the dual-constraint solver selects $\\\\bstar$ via the $\\\\aeff$ bound in 40\\\\% of cases, with mean $\\\\bstar{=}1.67$; the ESS-only variant would choose $b{=}4.15$ in these same batches, 2.5$\\\\times$ more aggressive.\\nThe remaining 49.9\\\\% of batches have sufficient real-data content to skip reweighting entirely ($\\\\bstar{=}0$).\\nThe per-batch $\\\\bstar$ distribution (median 0.87, mean 1.40) adapts continuously to each batch's contamination composition without any held-out signal.\\n\\nOn Qwen3-0.6B continued pretraining with 40\\\\% synthetic contamination (132M+ tokens from FineWeb), adaptive reweighting achieves mean held-out perplexity of 17.651 across three seeds, matching the grid-searched optimum ($b{=}0.5$, mean 17.646) within seed-to-seed variance (\\\\S\\\\ref{sec:results}).\\nThe grid sweep requires six complete training runs to identify this optimum; the adaptive method requires one.\\nThe ESS-only variant (maximum intervention) yields mean PPL 17.722---worse than the uniform baseline (17.694)---confirming that maximum intervention degrades training while minimum intervention improves it.\\nA lightweight TF-IDF + Logistic Regression detector (AUC\\\\,=\\\\,0.939, calibrated ECE\\\\,=\\\\,0.048) suffices throughout, suggesting that score calibration matters more than raw classification accuracy for provenance-based reweighting.\\n\\nOur contributions:\\n\\\\begin{itemize}[nosep,leftmargin=*]\\n\\\\item A dual-constrained framework for adaptive exponent selection: $\\\\bstar = \\\\inf\\\\{b \\\\geq 0 : \\\\aeff(b) \\\\geq \\\\tau\\\\}$ subject to $\\\\mathrm{ESS}(b) \\\\geq \\\\nmin$, computed per-batch from detector scores with minimum-intervention semantics (\\\\S\\\\ref{sec:method}).\\n\\\\item Empirical evidence that adaptive $\\\\bstar$ matches grid-searched best within seed variance at zero validation cost, and that minimum intervention (dual constraint) outperforms maximum intervention (ESS-only) across three seeds (\\\\S\\\\ref{sec:results}).\\n\\\\item A demonstration that a lightweight TF-IDF + LR detector with calibrated $q$-scores supports effective reweighting, achieving results comparable to stronger neural detectors (\\\\S\\\\ref{sec:experiments}).\\n\\\\end{itemize}\\n```\\n\\n---\\n\\n=== method_3f5a58.tex ===\\n\\n```\\n% Method section for \\\"Minimum Intervention Reweighting\\\" (EMNLP 2026)\\n% Generated: 2026-05-15\\n% Based on: paper_framing.md (STABLE, D023/D029/D035)\\n% Requires macros: \\\\bstar, \\\\aeff, \\\\nmin, \\\\btau, \\\\bess (defined in main.tex preamble)\\n\\n\\\\section{Method}\\n\\\\label{sec:method}\\n\\n\\\\subsection{Problem Setup}\\n\\\\label{sec:problem-setup}\\n\\nLet $\\\\mathcal{D} = \\\\{x_1, \\\\ldots, x_N\\\\}$ denote a pretraining corpus comprising human-written text $\\\\mathcal{D}_{\\\\mathrm{real}}$ and machine-generated text $\\\\mathcal{D}_{\\\\mathrm{synth}}$, with unknown contamination rate $\\\\rho = |\\\\mathcal{D}_{\\\\mathrm{synth}}| / |\\\\mathcal{D}|$.\\nA pretrained detector assigns each sample a synthetic probability $q(x_i) \\\\in [0, 1]$.\\nFollowing \\\\citet{drayson_2025_detection_collapse}, we define per-sample weights\\n\\\\begin{equation}\\n  w_b(x_i) = (1 - q(x_i))^b, \\\\quad b \\\\geq 0,\\n  \\\\label{eq:weight}\\n\\\\end{equation}\\nwhere $b = 0$ recovers uniform weighting and increasing $b$ progressively downweights high-$q$ samples.\\nThe weighted training objective is\\n\\\\begin{equation}\\n  \\\\mathcal{L}(b) = \\\\frac{\\\\sum_{i} w_b(x_i) \\\\, \\\\ell(x_i; \\\\theta)}{\\\\sum_{j} w_b(x_j)},\\n  \\\\label{eq:loss}\\n\\\\end{equation}\\nwhere $\\\\ell(x_i; \\\\theta)$ is the per-sample language modeling loss.\\n\\n\\\\citet{drayson_2025_detection_collapse} treat $b$ as a hyperparameter selected via validation-based grid search, with reported optima ranging from $b{=}1$ (SmolLM-1.7B) to $b{=}10$ (GPT-2 124M), making per-model tuning unavoidable.\\nWe instead derive $b$ adaptively per batch from the detector scores alone, requiring no validation set.\\n\\n\\\\subsection{Dual-Constraint Framework}\\n\\\\label{sec:dual-constraint}\\n\\nHigher $b$ removes more synthetic influence but also discards effective training signal.\\nWe formalize this trade-off through two per-batch statistics.\\n\\n\\\\paragraph{Effective real proportion.}\\nFor a batch $\\\\mathcal{B} = \\\\{x_1, \\\\ldots, x_B\\\\}$ with weights $w_i(b) = (1 - q_i)^b$, we define\\n\\\\begin{equation}\\n  \\\\aeff(b) = \\\\frac{\\\\sum_{i \\\\in \\\\mathcal{B}} w_i(b) \\\\cdot \\\\mathbf{1}[x_i \\\\in \\\\mathcal{D}_{\\\\mathrm{real}}]}{\\\\sum_{i \\\\in \\\\mathcal{B}} w_i(b)},\\n  \\\\label{eq:alpha_eff}\\n\\\\end{equation}\\nmeasuring the effective fraction of real data after reweighting.\\nSince true provenance labels are unavailable at training time, we use the detector's hard prediction $\\\\mathbf{1}[q(x_i) < 0.5]$ as a proxy; all theoretical properties below hold for this approximation.\\n\\n\\\\paragraph{Effective sample size.}\\nKish's effective sample size \\\\citep{vehtari_2024_psis} quantifies weight concentration:\\n\\\\begin{equation}\\n  \\\\mathrm{ESS}(b) = \\\\frac{\\\\left(\\\\sum_{i \\\\in \\\\mathcal{B}} w_i(b)\\\\right)^2}{\\\\sum_{i \\\\in \\\\mathcal{B}} w_i^2(b)}.\\n  \\\\label{eq:ess}\\n\\\\end{equation}\\n$\\\\mathrm{ESS}(0) = B$ under uniform weights, decreasing toward $1$ as $b \\\\to \\\\infty$ for any batch containing synthetic samples.\\n\\n\\\\begin{proposition}[Monotonicity]\\n\\\\label{prop:monotonicity}\\nFor any batch containing both real and synthetic samples with non-identical $q$-scores:\\n\\\\begin{enumerate}[leftmargin=*,nosep]\\n  \\\\item $\\\\aeff(b)$ is strictly increasing in $b$.\\n  \\\\item $\\\\mathrm{ESS}(b)$ is strictly decreasing in $b$.\\n\\\\end{enumerate}\\n\\\\end{proposition}\\n\\n\\\\begin{proof}[Proof sketch]\\nFor (1), differentiating Eq.~\\\\eqref{eq:alpha_eff} using $\\\\frac{dw_i}{db} = w_i \\\\ln(1 {-} q_i)$ yields\\n\\\\begin{equation}\\n  \\\\frac{d\\\\aeff}{db} = \\\\aeff(1 {-} \\\\aeff) \\\\!\\\\left( \\\\mathbb{E}_w[\\\\ln(1{-}q) \\\\mid \\\\mathrm{real}] - \\\\mathbb{E}_w[\\\\ln(1{-}q) \\\\mid \\\\mathrm{synth}] \\\\right)\\\\!,\\n  \\\\label{eq:dalpha}\\n\\\\end{equation}\\nwhere $\\\\mathbb{E}_w$ denotes expectation under the normalized weight distribution.\\nSince real samples have lower $q$-scores, $\\\\ln(1{-}q)$ is strictly less negative for real than synthetic samples, making the parenthesized difference positive.\\nFor (2), increasing $b$ multiplies each weight by $(1{-}q_i)^{\\\\Delta b}$, a factor varying across samples, which concentrates the normalized weight distribution and strictly increases $\\\\sum_i \\\\tilde{w}_i^2$, hence decreasing ESS.\\nFull proofs appear in Appendix~\\\\ref{app:proofs}.\\n\\\\end{proof}\\n\\nProposition~\\\\ref{prop:monotonicity} establishes that quality and sample efficiency move in opposite directions as $b$ increases, motivating two complementary constraints.\\n\\n\\\\paragraph{Quality lower bound.}\\nWe require $\\\\aeff(b) \\\\geq \\\\tau$ for a threshold $\\\\tau \\\\in (0, 1)$.\\nBy strict monotonicity, this defines a unique lower bound\\n\\\\begin{equation}\\n  \\\\btau = \\\\inf\\\\{b \\\\geq 0 : \\\\aeff(b) \\\\geq \\\\tau\\\\}\\n  \\\\label{eq:b_tau}\\n\\\\end{equation}\\non the exponent---the minimum intervention needed to achieve quality $\\\\tau$.\\n\\\\citet{wang_2026_survive_contamination} show that pretraining convergence rate scales with effective real data fraction, providing theoretical motivation for maintaining $\\\\aeff$ above a threshold.\\n\\n\\\\paragraph{Stability upper bound.}\\nWe require $\\\\mathrm{ESS}(b) \\\\geq \\\\nmin$ for a floor $\\\\nmin \\\\geq 1$.\\nBy strict monotonicity, this defines a unique upper bound\\n\\\\begin{equation}\\n  \\\\bess = \\\\sup\\\\{b \\\\geq 0 : \\\\mathrm{ESS}(b) \\\\geq \\\\nmin\\\\}\\n  \\\\label{eq:b_ess}\\n\\\\end{equation}\\nbeyond which gradient estimates become unreliable due to weight concentration.\\n\\n\\\\paragraph{Minimum intervention principle.}\\nWe select\\n\\\\begin{equation}\\n  \\\\bstar = \\\\begin{cases}\\n    0 & \\\\text{if } \\\\aeff(0) \\\\geq \\\\tau \\\\\\\\\\n    \\\\btau & \\\\text{if } \\\\btau \\\\leq \\\\bess \\\\\\\\\\n    \\\\bess & \\\\text{if } \\\\btau > \\\\bess\\n  \\\\end{cases}\\n  \\\\label{eq:bstar}\\n\\\\end{equation}\\nyielding three regimes:\\n(1)~\\\\textbf{Already clean} ($\\\\aeff(0) \\\\geq \\\\tau$): the unweighted batch meets quality $\\\\tau$; set $\\\\bstar = 0$.\\n(2)~\\\\textbf{$\\\\aeff$-binding} ($\\\\btau \\\\leq \\\\bess$): the quality constraint determines $\\\\bstar = \\\\btau$, applying the \\\\emph{minimum} intervention to reach $\\\\tau$, with ESS margin remaining.\\n(3)~\\\\textbf{ESS-binding} ($\\\\btau > \\\\bess$): quality $\\\\tau$ is infeasible under the stability constraint; $\\\\bstar = \\\\bess$ applies the maximum stable intervention.\\n\\nThe key insight is that when the feasible region $[\\\\btau, \\\\bess]$ is non-empty, the method selects its \\\\emph{left} endpoint---downweighting no more than necessary.\\nThis contrasts with an ESS-only strategy that selects $\\\\bess$ (the right endpoint), maximizing cleaning at the cost of discarding useful gradient signal from borderline samples.\\nIn our experiments (\\\\S\\\\ref{sec:results}), 40.1\\\\% of reweighted batches are $\\\\aeff$-binding, where mean $\\\\bstar = 1.67$ compared to $4.15$ under ESS-only---a $2.5\\\\times$ less aggressive exponent that retains $\\\\mathrm{ESS} = 2.60$, well above the floor $\\\\nmin = 2$.\\n\\n\\\\subsection{Algorithm}\\n\\\\label{sec:algorithm}\\n\\nAlgorithm~\\\\ref{alg:solver} solves for $\\\\bstar$ via bisection on $\\\\aeff$, exploiting monotonicity (Proposition~\\\\ref{prop:monotonicity}) to guarantee convergence.\\n\\n\\\\begin{algorithm}[t]\\n\\\\caption{Per-batch adaptive exponent solver}\\n\\\\label{alg:solver}\\n\\\\begin{algorithmic}[1]\\n\\\\REQUIRE Batch scores $\\\\{q_1, \\\\ldots, q_B\\\\}$, threshold $\\\\tau$, ESS floor $\\\\nmin$, tolerance $\\\\varepsilon$, cap $b_{\\\\max}$\\n\\\\ENSURE Optimal exponent $\\\\bstar$\\n\\\\IF{$\\\\aeff(0) \\\\geq \\\\tau$}\\n  \\\\STATE \\\\textbf{return} $\\\\bstar = 0$ \\\\hfill $\\\\triangleright$ Already clean\\n\\\\ENDIF\\n\\\\STATE $b_{\\\\mathrm{lo}} \\\\leftarrow 0,\\\\; b_{\\\\mathrm{hi}} \\\\leftarrow b_{\\\\max}$ \\\\hfill $\\\\triangleright$ Bisect for $\\\\btau$\\n\\\\WHILE{$b_{\\\\mathrm{hi}} - b_{\\\\mathrm{lo}} > \\\\varepsilon$}\\n  \\\\STATE $b_{\\\\mathrm{mid}} \\\\leftarrow (b_{\\\\mathrm{lo}} + b_{\\\\mathrm{hi}}) / 2$\\n  \\\\IF{$\\\\aeff(b_{\\\\mathrm{mid}}) < \\\\tau$}\\n    \\\\STATE $b_{\\\\mathrm{lo}} \\\\leftarrow b_{\\\\mathrm{mid}}$\\n  \\\\ELSE\\n    \\\\STATE $b_{\\\\mathrm{hi}} \\\\leftarrow b_{\\\\mathrm{mid}}$\\n  \\\\ENDIF\\n\\\\ENDWHILE\\n\\\\STATE $\\\\btau \\\\leftarrow b_{\\\\mathrm{hi}}$\\n\\\\IF{$\\\\mathrm{ESS}(\\\\btau) \\\\geq \\\\nmin$}\\n  \\\\STATE \\\\textbf{return} $\\\\bstar = \\\\btau$ \\\\hfill $\\\\triangleright$ $\\\\aeff$-binding\\n\\\\ELSE\\n  \\\\STATE Find $\\\\bess = \\\\sup\\\\{b : \\\\mathrm{ESS}(b) \\\\geq \\\\nmin\\\\}$ via bisection\\n  \\\\STATE \\\\textbf{return} $\\\\bstar = \\\\bess$ \\\\hfill $\\\\triangleright$ ESS-binding\\n\\\\ENDIF\\n\\\\end{algorithmic}\\n\\\\end{algorithm}\\n\\n\\\\paragraph{Implementation.}\\nWe apply $\\\\bstar$ through loss reweighting: each sample's loss is scaled by its normalized weight $\\\\bar{w}_i = w_{\\\\bstar}(x_i) / \\\\sum_j w_{\\\\bstar}(x_j)$, yielding continuous gradient contributions from all samples including those with intermediate $q$-scores.\\nThis contrasts with the sampling-importance-resampling (SIR) approach of \\\\citet{drayson_2025_detection_collapse}, which discretely resamples a subset of the batch, introducing additional variance and discarding partial information from borderline samples.\\n\\n\\\\paragraph{Computational cost.}\\nEach evaluation of $\\\\aeff$ or ESS costs $O(B)$ for batch size $B$.\\nBisection requires $O(\\\\log(b_{\\\\max} / \\\\varepsilon))$ iterations, giving total per-batch overhead $O(B \\\\log(b_{\\\\max} / \\\\varepsilon))$---negligible compared to the $O(BHD)$ cost of transformer forward and backward passes with hidden dimension $H$ and depth $D$.\\nWith $b_{\\\\max} = 20$ and $\\\\varepsilon = 0.01$, this amounts to ${\\\\sim}11$ iterations per batch.\\n\\n\\\\subsection{Hyperparameters}\\n\\\\label{sec:hyperparameters}\\n\\nThe framework replaces the single sensitive exponent $b$ with two hyperparameters, $\\\\tau$ and $\\\\nmin$, both admitting principled defaults that transfer across settings without per-model tuning.\\n\\n\\\\paragraph{Quality threshold $\\\\tau$.}\\n\\\\citet{wang_2026_survive_contamination} establish that pretraining convergence rate scales with effective real data proportion, motivating a quality threshold.\\nHowever, their analysis assumes known mixture proportions; since we do not assume known $\\\\rho$, $\\\\tau$ is an empirical hyperparameter with theoretical motivation rather than a theoretically derived quantity.\\nWe evaluate $\\\\tau \\\\in \\\\{0.5, 0.6, 0.7, 0.8, 0.9, 0.95\\\\}$ at $\\\\rho = 0.4$ (\\\\S\\\\ref{sec:results}).\\nAll values in $[0.5, 0.8]$ improve over uniform training, with PPL spanning only $0.035$ across this range (17.688 at $\\\\tau{=}0.5$ to 17.653 at $\\\\tau{=}0.8$).\\nWe adopt $\\\\tau = 0.8$ as the default.\\nThe sensitivity is asymmetric: under-cleaning ($\\\\tau < 0.8$) yields mild degradation, while over-cleaning ($\\\\tau > 0.8$) causes sharper regression as $\\\\bstar$ inflates (mean $\\\\bstar = 2.36$ at $\\\\tau{=}0.9$ vs.\\\\ $1.40$ at $\\\\tau{=}0.8$), excessively suppressing borderline samples whose gradient signal remains useful.\\n\\n\\\\paragraph{ESS floor $\\\\nmin$.}\\nThe stability constraint prevents gradient instability from weight concentration.\\nAt $\\\\nmin = 1$ (effectively unconstrained), $\\\\bstar$ inflates to mean $7.20$ with 46.7\\\\% of batches exceeding $\\\\bstar = 2$, yielding PPL~$= 17.789$---worse than uniform ($17.694$) by $+0.095$, confirming that unconstrained downweighting is harmful.\\nAt $\\\\nmin \\\\geq B$, the constraint forces $\\\\bstar = 0$ for all batches, recovering uniform training.\\nWe use $\\\\nmin = 2$ (half the batch size for $B = 4$), which yields consistent improvement across three seeds (\\\\S\\\\ref{sec:results}).\\n\\n\\\\paragraph{Comparison with fixed $b$.}\\nBoth $\\\\tau$ and $\\\\nmin$ admit wide effective ranges ($\\\\tau \\\\in [0.5, 0.8]$, $\\\\nmin \\\\in \\\\{2, 3\\\\}$) and can be set once without per-model adjustment.\\nIn contrast, the fixed $b$ of \\\\citet{drayson_2025_detection_collapse} spans an order of magnitude across model scales and requires a clean validation set plus grid search costing up to $6{\\\\times}$ the training budget.\\nOur adaptive $\\\\bstar$ eliminates this cost entirely.\\n```\\n\\n---\\n\\n=== method.tex ===\\n\\n```\\n\\\\section{Method}\\n\\\\label{sec:method}\\n\\n\\\\subsection{Problem Setup}\\n\\\\label{sec:setup}\\n\\nLet $\\\\mathcal{D} = \\\\mathcal{D}_{\\\\mathrm{real}} \\\\cup \\\\mathcal{D}_{\\\\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.\\nThe contamination ratio $\\\\rho = |\\\\mathcal{D}_{\\\\mathrm{synth}}| / |\\\\mathcal{D}|$ is unknown---a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\\\\citep{cheng_2025_contamination_survey}.\\n\\nA pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \\\\in [0,1]$.\\nFollowing \\\\citet{drayson_2025_detection_collapse}, we weight each sample as\\n\\\\begin{equation}\\n  w(x) = (1 - q(x))^{b},\\n  \\\\label{eq:weight}\\n\\\\end{equation}\\nwhere $b \\\\geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.\\n\\\\citet{drayson_2025_detection_collapse} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\\\\leq}360$M parameters, $b{=}1$ for 1.7B).\\nWe instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.\\n\\n\\\\subsection{Dual-Constraint Framework}\\n\\\\label{sec:dual}\\n\\nGiven a batch $\\\\mathcal{B} = \\\\{x_1, \\\\ldots, x_B\\\\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.\\n\\n\\\\paragraph{Effective real proportion.}\\nLet $r_i = \\\\mathbf{1}[q_i \\\\leq 0.5]$ estimate whether sample $x_i$ is human-authored.\\nThe \\\\emph{effective real proportion}\\n\\\\begin{equation}\\n  \\\\alpha_{\\\\mathrm{eff}}(b) = \\\\frac{\\\\sum_{i=1}^{B} w_i(b) \\\\cdot r_i}{\\\\sum_{i=1}^{B} w_i(b)}\\n  \\\\label{eq:alpha}\\n\\\\end{equation}\\nmeasures the share of total weight allocated to likely-real samples.\\nAt $b = 0$, $\\\\alpha_{\\\\mathrm{eff}}$ equals the raw real fraction in the batch; increasing $b$ shifts weight toward low-$q$ samples, raising $\\\\alpha_{\\\\mathrm{eff}}$.\\n\\n\\\\paragraph{Effective sample size.}\\nKish's effective sample size~\\\\citep{vehtari_2024_psis}\\n\\\\begin{equation}\\n  \\\\mathrm{ESS}(b) = \\\\frac{\\\\bigl(\\\\sum_{i=1}^{B} w_i(b)\\\\bigr)^{2}}{\\\\sum_{i=1}^{B} w_i(b)^{2}}\\n  \\\\label{eq:ess}\\n\\\\end{equation}\\nquantifies how many equally-weighted samples the weighted batch is equivalent to.\\n$\\\\mathrm{ESS}(0) = B$; as $b$ grows, a few high-$(1{-}q)$ samples dominate and $\\\\mathrm{ESS}$ drops toward~1.\\n\\n\\\\paragraph{Monotonicity.}\\nThe two diagnostics exhibit opposing monotonicity in $b$:\\n\\n\\\\begin{proposition}\\n\\\\label{prop:monotone}\\nFor any batch containing both real and synthetic samples with distinct $q$-values, $\\\\alpha_{\\\\mathrm{eff}}(b)$ is strictly increasing in $b$.\\n\\\\end{proposition}\\n\\n\\\\begin{proof}[Proof sketch]\\nLet $\\\\pi_i(b) = w_i / \\\\sum_j w_j$ denote normalized weights.\\nDifferentiating $\\\\alpha_{\\\\mathrm{eff}} = \\\\sum_i \\\\pi_i r_i$ yields\\n$\\\\frac{d\\\\alpha_{\\\\mathrm{eff}}}{db} = \\\\mathrm{Cov}_{\\\\pi}\\\\!\\\\bigl(r_i,\\\\, \\\\ln(1{-}q_i)\\\\bigr)$.\\nReal samples ($r_i = 1$) have $q_i \\\\leq 0.5$ and thus higher $\\\\ln(1{-}q_i)$, so this covariance is non-negative for any detector with better-than-random discrimination.\\nFull derivation in Appendix~\\\\ref{app:proofs}.\\n\\\\end{proof}\\n\\n\\\\noindent $\\\\mathrm{ESS}(b)$ is monotonically decreasing in $b$---larger exponents concentrate the weight distribution, a standard property of exponential tilting~\\\\citep{kimura_2024_iw_survey}.\\n\\n\\\\paragraph{Dual constraints.}\\nWe impose two requirements on $b$:\\n\\\\begin{enumerate}[nosep,leftmargin=*]\\n  \\\\item \\\\textbf{Quality floor}: $\\\\alpha_{\\\\mathrm{eff}}(b) \\\\geq \\\\tau$.\\n  Convergence under contaminated training improves with the effective real fraction~\\\\citep{wang_2026_survive_contamination}; $\\\\tau$ sets the minimum acceptable quality level.\\n  By Proposition~\\\\ref{prop:monotone}, this constraint defines a \\\\emph{lower bound} $b_\\\\tau = \\\\inf\\\\{b \\\\geq 0 : \\\\alpha_{\\\\mathrm{eff}}(b) \\\\geq \\\\tau\\\\}$.\\n  \\\\item \\\\textbf{Stability ceiling}: $\\\\mathrm{ESS}(b) \\\\geq n_{\\\\min}$.\\n  Overly concentrated weights yield high-variance gradients; $n_{\\\\min}$ prevents the batch from degenerating into a single effective sample.\\n  Since $\\\\mathrm{ESS}$ is decreasing, this defines an \\\\emph{upper bound} $b_{\\\\mathrm{ESS}} = \\\\sup\\\\{b \\\\geq 0 : \\\\mathrm{ESS}(b) \\\\geq n_{\\\\min}\\\\}$.\\n\\\\end{enumerate}\\nThe optimal exponent is\\n\\\\begin{equation}\\n  b^{*} = \\\\inf\\\\bigl\\\\{b \\\\geq 0 : \\\\alpha_{\\\\mathrm{eff}}(b) \\\\geq \\\\tau\\\\bigr\\\\} \\\\;\\\\;\\\\text{s.t.}\\\\;\\\\; \\\\mathrm{ESS}(b) \\\\geq n_{\\\\min}.\\n  \\\\label{eq:bstar}\\n\\\\end{equation}\\nThis is the \\\\emph{minimum intervention principle}: apply the smallest $b$ that achieves the quality floor.\\nBorderline samples---those with moderate $q$-values---still carry useful training signal; over-downweighting discards this signal unnecessarily.\\nWhen both constraints are satisfiable ($b_\\\\tau \\\\leq b_{\\\\mathrm{ESS}}$), $b^{*} = b_\\\\tau$ and $\\\\alpha_{\\\\mathrm{eff}}$ is the binding constraint---$b^{*}$ lies well below the ESS ceiling.\\nWhen they conflict ($b_\\\\tau > b_{\\\\mathrm{ESS}}$), the stability ceiling takes precedence: $b^{*} = b_{\\\\mathrm{ESS}}$, accepting a lower $\\\\alpha_{\\\\mathrm{eff}}$ to preserve gradient stability.\\nFigure~\\\\ref{fig:dual_constraint} illustrates the feasible region and the three regimes.\\n\\n\\\\subsection{Algorithm}\\n\\\\label{sec:algorithm}\\n\\nAlgorithm~\\\\ref{alg:bstar} computes $b^{*}$ for each training batch via bisection on the monotone functions $\\\\alpha_{\\\\mathrm{eff}}$ and $\\\\mathrm{ESS}$.\\nEach batch falls into one of three regimes:\\n\\\\begin{enumerate}[nosep,leftmargin=*]\\n  \\\\item \\\\textbf{Clean} ($\\\\alpha_{\\\\mathrm{eff}}(0) \\\\geq \\\\tau$): the quality floor holds at $b = 0$; no reweighting needed.\\n  \\\\item \\\\textbf{$\\\\alpha_{\\\\mathrm{eff}}$-binding} ($b_\\\\tau \\\\leq b_{\\\\mathrm{ESS}}$): the quality constraint determines $b^{*} = b_\\\\tau$; $\\\\mathrm{ESS}$ remains above $n_{\\\\min}$ with margin.\\n  \\\\item \\\\textbf{ESS-binding} ($b_\\\\tau > b_{\\\\mathrm{ESS}}$): the stability ceiling caps $b^{*} = b_{\\\\mathrm{ESS}}$.\\n\\\\end{enumerate}\\nAcross 51{,}913 micro-batches in our main experiment ($\\\\rho{=}0.4$, $\\\\tau{=}0.8$, $n_{\\\\min}{=}2$), 49.9\\\\% are clean, 20.2\\\\% are $\\\\alpha_{\\\\mathrm{eff}}$-binding, and 30.0\\\\% are ESS-binding.\\nIn $\\\\alpha_{\\\\mathrm{eff}}$-binding batches, the solver selects $b^{*} = 1.67$ on average, while an ESS-only strategy would choose $b = 4.15$ on the same batches---2.5$\\\\times$ more aggressive.\\nThe residual $\\\\mathrm{ESS} = 2.60$ in these batches (vs.\\\\ $n_{\\\\min} = 2.0$) confirms that the dual constraint prevents unnecessary over-downweighting.\\n\\n\\\\begin{algorithm}[t]\\n\\\\caption{Per-batch adaptive $b^{*}$ selection}\\n\\\\label{alg:bstar}\\n\\\\begin{algorithmic}[1]\\n\\\\Require Batch scores $\\\\{q_i\\\\}_{i=1}^{B}$, indicators $\\\\{r_i\\\\}$, quality threshold~$\\\\tau$, ESS floor~$n_{\\\\min}$, search bound~$b_{\\\\max}$, tolerance~$\\\\varepsilon$\\n\\\\Ensure Optimal exponent $b^{*}$\\n\\\\If{$\\\\alpha_{\\\\mathrm{eff}}(0) \\\\geq \\\\tau$}\\n  \\\\State \\\\Return $0$ \\\\Comment{clean batch}\\n\\\\EndIf\\n\\\\State $b_\\\\tau \\\\gets \\\\Call{Bisect}{\\\\alpha_{\\\\mathrm{eff}}(\\\\cdot){=}\\\\tau,\\\\; [0, b_{\\\\max}],\\\\; \\\\varepsilon}$\\n\\\\If{$\\\\mathrm{ESS}(b_\\\\tau) \\\\geq n_{\\\\min}$}\\n  \\\\State \\\\Return $b_\\\\tau$ \\\\Comment{$\\\\alpha_{\\\\mathrm{eff}}$-binding}\\n\\\\Else\\n  \\\\State $b_{\\\\mathrm{ESS}} \\\\gets \\\\Call{Bisect}{\\\\mathrm{ESS}(\\\\cdot){=}n_{\\\\min},\\\\; [0, b_{\\\\max}],\\\\; \\\\varepsilon}$\\n  \\\\State \\\\Return $b_{\\\\mathrm{ESS}}$ \\\\Comment{ESS-binding}\\n\\\\EndIf\\n\\\\end{algorithmic}\\n\\\\end{algorithm}\\n\\n\\\\paragraph{Implementation.}\\nGiven $b^{*}$, we compute normalized weights $\\\\pi_i = w_i(b^{*}) / \\\\sum_j w_j(b^{*})$ and form the weighted loss $\\\\mathcal{L} = \\\\sum_i \\\\pi_i \\\\ell_i$, where $\\\\ell_i$ is the per-sample cross-entropy.\\nThis \\\\emph{loss reweighting} maintains continuous gradients, unlike the SIR resampling of \\\\citet{drayson_2025_detection_collapse} which introduces discrete sampling noise by drawing a subset proportional to $w_i$.\\nEach bisection requires $\\\\mathcal{O}(B \\\\log(b_{\\\\max}/\\\\varepsilon))$ operations---with $B{=}4$, $b_{\\\\max}{=}20$, and $\\\\varepsilon{=}0.01$, roughly 44 floating-point operations per batch, negligible beside the forward and backward passes.\\n\\n\\\\subsection{Hyperparameters}\\n\\\\label{sec:hyperparameters}\\n\\nThe framework introduces two hyperparameters, both with principled defaults set once across all experiments.\\n\\n\\\\paragraph{Quality threshold $\\\\tau$.}\\nConvergence theory for contaminated training shows that convergence rate improves with the effective real fraction~\\\\citep{wang_2026_survive_contamination}, motivating a lower bound on $\\\\alpha_{\\\\mathrm{eff}}$.\\nThe specific value of $\\\\tau$ is set empirically.\\nWe find a wide safe range: $\\\\tau \\\\in [0.5, 0.8]$ consistently outperforms uniform training (Section~\\\\ref{sec:results}), with $\\\\tau = 0.8$ achieving the best perplexity.\\nAbove 0.8, $b^{*}$ inflates rapidly (mean $b^{*} = 3.08$ at $\\\\tau = 0.95$), causing over-downweighting.\\nWe use $\\\\tau = 0.8$ as the default throughout.\\n\\n\\\\paragraph{ESS floor $n_{\\\\min}$.}\\nWe set $n_{\\\\min} = 2$ for batch size $B = 4$.\\nThe constraint $n_{\\\\min} < B$ is necessary: $n_{\\\\min} \\\\geq B$ forces $b^{*} = 0$ on every batch, recovering uniform training.\\nAt the other extreme, $n_{\\\\min} = 1$ effectively removes the stability constraint---mean $b^{*}$ rises to 7.20, with 46.7\\\\% of batches hitting the search ceiling at $b_{\\\\max}{=}20$, and perplexity degrades by $+0.14$ relative to $n_{\\\\min} = 2$.\\nIn practice, $n_{\\\\min} \\\\in \\\\{2, 3\\\\}$ yields stable results across seeds (Section~\\\\ref{sec:results}).\\n```\\n\\n---\\n\\n=== related_work_0b6096.tex ===\\n\\n```\\n% Related Work for \\\"Minimum Intervention Reweighting: Adaptive Exponent Selection\\n% for Contamination-Aware Pretraining\\\"\\n% Generated: 2026-05-15\\n% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)\\n\\n\\\\section{Related Work}\\n\\\\label{sec:related}\\n\\n\\\\paragraph{Synthetic Contamination and Model Collapse.}\\nTraining on recursively generated data leads to irreversible quality degradation---\\\\emph{model collapse} \\\\citep{shumailov2024model}.\\n\\\\cite{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\\nMore critically, \\\\cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.\\nWith synthetic content now estimated at 20--60\\\\% of web corpora \\\\citep{cheng2025contamination}, these results motivate contamination-aware training strategies that explicitly account for data provenance rather than treating all tokens equally.\\n\\n\\\\paragraph{Detect and Reweight.}\\nA natural response to contamination is to detect and remove synthetic content.\\nDetectGPT \\\\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\\\% Prob \\\\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\\\\% tokens as a reference-free signal; both produce continuous confidence scores suitable as input to reweighting frameworks.\\n\\\\cite{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples; \\\\cite{guo2025escaping} similarly rely on verification-based selection.\\nSoft reweighting avoids the precision--recall threshold inherent in hard filtering by assigning continuous weights.\\n\\nMost directly related to our work, \\\\cite{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is a detector's synthetic probability.\\nWe adopt the same weighting formula but differ in several fundamental ways.\\n\\\\textbf{(i)}~Drayson et al.\\\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\\\leq}360$M parameters, $b{=}1$ for 1.7B), making the choice per-model and expensive.\\nOur $\\\\bstar$ is derived per-batch from dual constraints ($\\\\aeff \\\\geq \\\\tau$, $\\\\mathrm{ESS} \\\\geq \\\\nmin$) at zero validation cost, following a minimum intervention principle that selects the smallest sufficient exponent.\\n\\\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradient contributions.\\n\\\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\\\,=\\\\,0.986) on WikiText-2 (${\\\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\\\,=\\\\,0.939) suffices on FineWeb-scale data (132M+ tokens).\\n\\n\\\\paragraph{Data Mixing and Reweighting.}\\nA parallel line of work optimizes data composition without targeting synthetic contamination.\\nAt the \\\\emph{domain} level, DoReMi \\\\citep{xie2023doremi} learns mixture weights via Group DRO with a proxy model, DSIR \\\\citep{xie2023dsir} performs importance resampling with $n$-gram features, \\\\cite{ye2025mixing} discover predictable functional forms relating mixing ratios to performance, and AIOLI \\\\citep{chen2025aioli} unifies these into an online adaptive framework.\\nThese methods operate at the domain level and do not address instance-level contamination within a domain.\\nAt the \\\\emph{instance} level, SoftDedup \\\\citep{he2024softdedup} downweights high-frequency samples via $n$-gram commonness, and \\\\cite{sow2025dynamic} derive sample weights from per-sample loss with convergence guarantees.\\nOur reweighting differs from all of these in being driven by \\\\emph{provenance}---detector scores estimating human vs.\\\\ machine origin---rather than loss, frequency, or domain membership.\\n\\n\\\\paragraph{Theoretical Foundations.}\\n\\\\cite{he2025golden} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\\\\approx}0.62$) optimal when both sources are equally sized; their result requires the contamination ratio, unavailable in web-scale settings.\\n\\\\cite{wang2026survive} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\\\aeff(b) \\\\geq \\\\tau$ guarantees a convergence-rate lower bound.\\nWe operationalize this without the known-proportion assumption, estimating $\\\\aeff$ from batch-level statistics online.\\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \\\\cite{vehtari2024psis}.\\n\\\\cite{kimura2024iw} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as covariate-shift correction where the covariate is synthetic origin probability.\\n\\n\\\\smallskip\\n\\\\noindent\\\\textbf{Summary.}\\nNo existing method provides principled per-batch exponent selection without validation.\\nDrayson et al.\\\\ use the same $w{=}(1{-}q)^b$ formula but require per-model grid search; Golden Ratio weighting requires known mixture proportions; DoReMi and DSIR operate at the domain level rather than instance-level contamination.\\nOur dual-constraint framework fills this gap by deriving the minimum intervention $\\\\bstar$ from batch-level diagnostics alone.\\n```\\n\\n---\\n\\n=== related_work.tex ===\\n\\n```\\n\\\\section{Related Work}\\n\\n\\\\paragraph{Synthetic Contamination and Model Collapse.}\\nTraining on recursively generated data leads to irreversible quality degradation---\\\\emph{model collapse}~\\\\citep{shumailov_2024_model_collapse}.\\n\\\\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\\nMore critically, \\\\citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.\\n\\\\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\\\\% of web corpora.\\nThese results motivate \\\\emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.\\n\\n\\\\paragraph{Detection and Filtering of Machine-Generated Text.}\\nGiven the severity of contamination, a natural response is to detect and remove synthetic content.\\nDetectGPT~\\\\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\\\% Prob~\\\\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\\\\% tokens as a reference-free signal.\\nBoth produce continuous confidence scores suitable as input to downstream weighting---including ours.\\nOn the mitigation side, \\\\citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.\\n\\\\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.\\nHard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.\\n\\nMost directly related to our work, \\\\citet{drayson_2025_detection_collapse} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic probability.\\nWe adopt the same weighting formula but differ in several fundamental ways.\\n\\\\textbf{(i)}~Drayson et al.\\\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\\\leq}360$M, $b{=}1$ for 1.7B), making the choice \\\\emph{per-model} and expensive.\\nOur $b^*$ is derived per-batch from dual constraints ($\\\\alpha_{\\\\mathrm{eff}} \\\\geq \\\\tau$, $\\\\mathrm{ESS} \\\\geq n_{\\\\min}$) at zero validation cost.\\n\\\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradients.\\n\\\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\\\,=\\\\,0.986) on WikiText-2 (${\\\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\\\,=\\\\,0.939) suffices on FineWeb-scale data (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.\\n\\n\\\\paragraph{Data Mixing and Instance-Level Reweighting.}\\nA parallel line of work optimizes data composition without targeting synthetic contamination.\\nAt the \\\\emph{domain} level, DoReMi~\\\\citep{xie_2023_doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\\\\citep{xie_2023_dsir} performs importance resampling with $n$-gram features, and \\\\citet{ye_2025_data_mixing_laws} discover predictable functional forms relating mixing ratios to performance.\\nAIOLI~\\\\citep{chen_2025_aioli} unifies these into an online adaptive framework, while \\\\citet{yang_2026_data_mixing_agent} train an RL agent for domain-weight selection.\\nThese methods do not address instance-level contamination within a domain.\\nAt the \\\\emph{instance} level, SoftDedup~\\\\citep{he_2024_softdedup} downweights high-frequency samples via $n$-gram commonness, \\\\citet{sow_2025_dynamic_reweighting} derive sample weights from per-sample loss with convergence guarantees, and \\\\citet{kuo_2024_data_weighting} show that differentiated weighting of LLM-generated data improves downstream classification.\\nOur reweighting differs from all of these in being driven by \\\\emph{provenance}---detector scores estimating human vs.\\\\ synthetic origin---rather than loss, frequency, or domain membership.\\n\\n\\\\paragraph{Theoretical Foundations.}\\n\\\\citet{he_2025_golden_ratio} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\\\\approx}0.62$) optimal when both sources are equally sized.\\nTheir result requires the contamination ratio $k$, unavailable in web-scale settings; we use it as an oracle baseline.\\n\\\\citet{wang_2026_survive_contamination} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\\\alpha_{\\\\mathrm{eff}}(b) \\\\geq \\\\tau$ guarantees a convergence-rate lower bound.\\nWe operationalize this without the known-proportion assumption, estimating $\\\\alpha_{\\\\mathrm{eff}}$ from batch-level statistics online.\\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \\\\citet{vehtari_2024_psis}.\\n\\\\citet{kimura_2024_iw_survey} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as a special case of covariate-shift correction where the covariate is synthetic origin probability.\\n```\\n\\n---\\n\\n=== experiments_86dfd1.tex ===\\n\\n```\\n\\\\section{Experimental Setup}\\n\\\\label{sec:experiments}\\n\\n\\\\paragraph{Training Data.}\\nWe sample a 132M-token subset of FineWeb~\\\\citep{penedo_2024_fineweb} as the real-data source.\\nTo simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\\\\citep{yang_2025_qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\\\\rho = 0.4$ via uniform random mixing.\\nThis self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.\\n\\n\\\\paragraph{Detector.}\\nWe train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\\\\,=\\\\,0.939 with calibrated ECE\\\\,=\\\\,0.048 after temperature scaling ($T = 0.204$).\\nThe resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\\\\% of samples in the uncertain range $[0.2, 0.8]$.\\nWe use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\\\\,${\\\\geq}$\\\\,0.98 in \\\\citealt{drayson_2025_detection_collapse}) to test whether score \\\\emph{calibration} matters more than raw discrimination for reweighting.\\n\\n\\\\paragraph{Training.}\\nWe continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\\\\,=\\\\,$5{\\\\times}10^{-5}$), max sequence length 2048, and bf16 precision.\\nAll main comparisons use three random seeds (42, 123, 456).\\n\\n\\\\paragraph{Evaluation.}\\nWe report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\\\\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).\\nAll evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.\\n\\n\\\\paragraph{Methods.}\\nWe compare five approaches:\\n\\\\begin{itemize}[nosep,leftmargin=*]\\n  \\\\item \\\\textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).\\n  \\\\item \\\\textbf{Grid-$b$}: fixed $b \\\\in \\\\{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\\\}$, best selected post-hoc by held-out PPL.\\n        Represents validation-based selection~\\\\citep{drayson_2025_detection_collapse}.\\n  \\\\item \\\\textbf{ESS-only}: $b^* = \\\\max\\\\{b : \\\\mathrm{ESS}(b) \\\\geq n_{\\\\min}\\\\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\\\\alpha_{\\\\mathrm{eff}}$.\\n  \\\\item \\\\textbf{Golden Ratio}: $w = 1/\\\\varphi \\\\approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\\\\citep{he_2025_golden_ratio}.\\n        Requires known provenance labels (oracle).\\n  \\\\item \\\\textbf{Adaptive} (ours): per-batch $b^*$ from the dual-constraint formulation (\\\\S\\\\ref{sec:method}), with $\\\\tau = 0.8$ and $n_{\\\\min} = 2$ (half the micro-batch size).\\n\\\\end{itemize}\\n```\\n\\n---\\n\\n=== experiments.tex ===\\n\\n```\\n\\\\section{Experimental Setup}\\n\\\\label{sec:experiments}\\n\\n\\\\paragraph{Training Data.}\\nWe sample a 132M-token subset of FineWeb~\\\\citep{penedo_2024_fineweb} as the real-data source.\\nTo simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\\\\citep{yang_2025_qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\\\\rho = 0.4$ via uniform random mixing.\\nThis self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.\\n\\n\\\\paragraph{Detector.}\\nWe train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\\\\,=\\\\,0.939 with calibrated ECE\\\\,=\\\\,0.048 after temperature scaling ($T = 0.204$).\\nThe resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\\\\% of samples in the uncertain range $[0.2, 0.8]$.\\nWe use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\\\\,${\\\\geq}$\\\\,0.98 in \\\\citealt{drayson_2025_detection_collapse}) to test whether score \\\\emph{calibration} matters more than raw discrimination for reweighting.\\n\\n\\\\paragraph{Training.}\\nWe continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\\\\,=\\\\,$5{\\\\times}10^{-5}$), max sequence length 2048, and bf16 precision.\\nAll main comparisons use three random seeds (42, 123, 456).\\n\\n\\\\paragraph{Evaluation.}\\nWe report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\\\\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).\\nAll evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.\\n\\n\\\\paragraph{Methods.}\\nWe compare five approaches:\\n\\\\begin{itemize}[nosep,leftmargin=*]\\n  \\\\item \\\\textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).\\n  \\\\item \\\\textbf{Grid-$b$}: fixed $b \\\\in \\\\{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\\\}$, best selected post-hoc by held-out PPL.\\n        Represents validation-based selection~\\\\citep{drayson_2025_detection_collapse}.\\n  \\\\item \\\\textbf{ESS-only}: $b^* = \\\\max\\\\{b : \\\\mathrm{ESS}(b) \\\\geq n_{\\\\min}\\\\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\\\\alpha_{\\\\mathrm{eff}}$.\\n  \\\\item \\\\textbf{Golden Ratio}: $w = 1/\\\\varphi \\\\approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\\\\citep{he_2025_golden_ratio}.\\n        Requires known provenance labels (oracle).\\n  \\\\item \\\\textbf{Adaptive} (ours): per-batch $b^*$ from the dual-constraint formulation (\\\\S\\\\ref{sec:method}), with $\\\\tau = 0.8$ and $n_{\\\\min} = 2$ (half the micro-batch size).\\n\\\\end{itemize}\\n```\\n\\n---\\n\\n=== results_d0d647.tex ===\\n\\n```\\n\\\\section{Results}\\n\\\\label{sec:results}\\n\\n\\\\subsection{Main Comparison}\\n\\nTable~\\\\ref{tab:main} reports held-out perplexity across methods and seeds.\\nAdaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).\\nThis parity comes at zero validation cost---grid search requires $|\\\\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.\\n\\nThe grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\\\\ref{app:grid}), confirming that exponent selection is consequential.\\nThe optimal $b{=}0.5$ differs from the $b{=}10$ reported by \\\\citet{drayson_2025_detection_collapse} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.\\n\\n% Claim 1: Dual > ESS-only (3 seeds)\\nESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \\\\emph{worse} than uniform (17.694) by 0.029.\\nThe degradation is consistent: ESS-only exceeds uniform on every individual seed (Table~\\\\ref{tab:main}), ruling out seed-specific artifacts.\\nRemoving $\\\\alpha_{\\\\mathrm{eff}}$ and maximizing $b$ subject only to $\\\\mathrm{ESS} \\\\geq n_{\\\\min}$ leads to systematic over-downweighting, providing direct evidence for the minimum-intervention principle.\\nConversely, adaptive (dual) improves over uniform on all three seeds (by 0.041, 0.043, and 0.045 respectively), confirming that the $\\\\alpha_{\\\\mathrm{eff}}$ quality floor prevents the over-intervention that plagues ESS-only.\\n\\nThe Golden Ratio oracle~\\\\citep{he_2025_golden_ratio} achieves PPL 17.654 on seed 42 using known provenance labels.\\nAdaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.\\n\\nThe adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.\\nThe constraint regime breakdown in \\\\S\\\\ref{sec:algorithm} shows that $\\\\alpha_{\\\\mathrm{eff}}$ prevents over-intervention in the 40\\\\% of reweighted batches where moderate $b$ already meets the quality target.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\begin{tabular}{@{}lcccc@{}}\\n\\\\toprule\\n\\\\textbf{Method} & \\\\textbf{Seed 42} & \\\\textbf{Seed 123} & \\\\textbf{Seed 456} & \\\\textbf{Mean} \\\\\\\\\\n\\\\midrule\\nUniform               & 17.694 & 17.686 & 17.702 & 17.694 \\\\\\\\\\nGrid-best ($b{=}0.5$) & \\\\textbf{17.651} & \\\\textbf{17.638} & \\\\textbf{17.650} & \\\\textbf{17.646} \\\\\\\\\\nESS-only               & 17.730 & 17.720 & 17.719 & 17.723 \\\\\\\\\\nGolden Ratio$^\\\\dagger$ & 17.654 & --     & --     & --     \\\\\\\\\\n\\\\midrule\\nAdaptive (ours)        & 17.653 & 17.643 & 17.657 & 17.651 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\caption{Held-out perplexity (PPL, $\\\\downarrow$).\\nGrid-best selects the optimal fixed $b$ post-hoc from six candidates.\\n$^\\\\dagger$Evaluated on seed 42 only.\\nBest per column in \\\\textbf{bold}.}\\n\\\\label{tab:main}\\n\\\\end{table}\\n\\n\\\\subsection{Sensitivity Analysis}\\n\\n\\\\paragraph{Quality threshold $\\\\tau$.}\\nTable~\\\\ref{tab:tau} varies $\\\\tau$ while holding $n_{\\\\min} = 2$ (seed 42).\\nAll values in $\\\\tau \\\\in [0.5, 0.8]$ improve over uniform, with $\\\\tau = 0.8$ achieving the lowest PPL (17.653).\\nHigher $\\\\tau$ demands greater $\\\\alpha_{\\\\mathrm{eff}}$, forcing the solver to increase $b^*$: mean $\\\\bar{b}^*$ rises monotonically from 0.39 at $\\\\tau{=}0.5$ to 3.08 at $\\\\tau{=}0.95$.\\nBelow 0.8, reweighting is too gentle to fully exploit the detector signal; above, $b^*$ inflates past diminishing returns and PPL degrades.\\nThe range $[0.5, 0.8]$ provides a wide safe operating region, with $\\\\tau = 0.8$ as the recommended default.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\begin{tabular}{@{}cccc@{}}\\n\\\\toprule\\n$\\\\tau$ & \\\\textbf{PPL} & $\\\\Delta_{\\\\mathrm{unif}}$ & $\\\\bar{b}^*$ \\\\\\\\\\n\\\\midrule\\n0.50 & 17.688 & $-$0.006 & 0.39 \\\\\\\\\\n0.60 & 17.681 & $-$0.013 & 0.59 \\\\\\\\\\n0.70 & 17.679 & $-$0.015 & 0.89 \\\\\\\\\\n\\\\textbf{0.80} & \\\\textbf{17.653} & $\\\\mathbf{-0.041}$ & \\\\textbf{1.40} \\\\\\\\\\n0.90 & 17.712 & $+$0.018 & 2.36 \\\\\\\\\\n0.95 & 17.723 & $+$0.029 & 3.08 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\caption{Sensitivity to $\\\\tau$ (seed 42, $n_{\\\\min}{=}2$, $\\\\rho{=}0.4$).\\n$\\\\Delta_{\\\\mathrm{unif}}$: PPL change vs.\\\\ uniform baseline (17.694).\\n$\\\\bar{b}^*$: mean adaptive exponent across batches.}\\n\\\\label{tab:tau}\\n\\\\end{table}\\n\\n\\\\paragraph{Minimum ESS $n_{\\\\min}$.}\\nTable~\\\\ref{tab:nmin} ablates $n_{\\\\min}$ at batch size $B{=}4$.\\nRemoving the ESS floor ($n_{\\\\min} = 1$) allows $b^*$ to inflate to mean 7.20, degrading PPL to 17.789---0.095 worse than uniform.\\nAt $n_{\\\\min} = 2$ ($= \\\\lfloor B/2 \\\\rfloor$), $b^*$ is constrained to mean 1.40 and PPL reaches 17.653, verified across three seeds.\\nAt $n_{\\\\min} = B = 4$, the ESS constraint is trivially satisfied at $b^* = 0$ for every batch, and PPL reverts to the uniform level (17.695 vs.\\\\ 17.694).\\nThe results exhibit a U-shaped pattern: too-low $n_{\\\\min}$ permits over-downweighting, while $n_{\\\\min}$ at or near $B$ removes the ability to reweight.\\n\\nThe coupling between $n_{\\\\min}$ and $B$ extends beyond the $B{=}4$ setting.\\nAt batch size $B{=}8$ with $n_{\\\\min}{=}2$, the ESS range $[2, 8]$ is wide enough that the stability constraint rarely binds, yielding PPL 17.73---comparable to ESS-only and 0.036 worse than uniform.\\nThis confirms that $n_{\\\\min}$ must scale with $B$: a fixed $n_{\\\\min}$ that works for one batch size can degrade to near-ESS-only behavior at larger $B$.\\nThe rule $n_{\\\\min} = \\\\max(2, \\\\lfloor B/2 \\\\rfloor)$ keeps the ESS constraint active without over-restricting the solver, and we recommend it as a practical default.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\begin{tabular}{@{}ccc@{}}\\n\\\\toprule\\n$n_{\\\\min}$ & \\\\textbf{PPL} & $\\\\bar{b}^*$ \\\\\\\\\\n\\\\midrule\\n1 & 17.789 & 7.20 \\\\\\\\\\n\\\\textbf{2} & \\\\textbf{17.653} & \\\\textbf{1.40} \\\\\\\\\\n3$^\\\\ddagger$ & 17.644 & 1.43 \\\\\\\\\\n4 & 17.695 & 0.00 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\caption{Sensitivity to $n_{\\\\min}$ (seed 42, $B{=}4$, $\\\\tau{=}0.8$).\\n$n_{\\\\min} = 4 = B$ forces $b^* = 0$ on all batches, recovering uniform weighting.\\n$^\\\\ddagger$From an earlier adaptive configuration; not an independent ablation.}\\n\\\\label{tab:nmin}\\n\\\\end{table}\\n```\\n\\n---\\n\\n=== results.tex ===\\n\\n(Identical content to results_d0d647.tex — same verbatim text, no differences.)\\n\\n---\\n\\n=== discussion_270aaa.tex ===\\n\\n```\\n\\\\paragraph{Why minimum intervention works.}\\nThe central finding of our experiments is that restraint in downweighting outperforms aggressiveness.\\nESS-only reweighting---which maximizes $b$ subject only to $\\\\mathrm{ESS} \\\\geq \\\\nmin$---degrades PPL to 17.723, \\\\emph{worse} than the uniform baseline (17.694, Table~\\\\ref{tab:main}).\\nThe dual-constrained adaptive $\\\\bstar$, by contrast, achieves 17.651 by selecting the \\\\emph{smallest} $b$ that meets the quality floor $\\\\tau$.\\nThe mechanism is clear from the binding statistics: in the 40.1\\\\% of reweighted batches where $\\\\aeff$ binds, mean $\\\\bstar = 1.67$ versus 4.15 under ESS-only---a 2.5$\\\\times$ less aggressive exponent that retains ESS\\\\,=\\\\,2.60, well above the floor $\\\\nmin = 2$.\\nOver-downweighting discards gradient signal from borderline samples whose detector scores are intermediate (e.g., $q \\\\approx 0.4$--$0.6$); these samples carry partial but non-negligible training value, and aggressively suppressing them impoverishes the effective training distribution.\\nThe $\\\\aeff$ constraint prevents this by halting $b$ as soon as the quality target is met.\\n\\n\\\\paragraph{$\\\\tau$ as a practical dial.}\\nThe quality threshold $\\\\tau$ controls the trade-off between decontamination strength and sample retention.\\nOur sweep (Table~\\\\ref{tab:tau}) reveals a wide safe operating range: all $\\\\tau \\\\in [0.5, 0.8]$ outperform uniform training, with PPL varying only 0.035 across this interval.\\nThe sensitivity is asymmetric---under-cleaning ($\\\\tau < 0.8$) incurs mild degradation ($-$0.006 to $-$0.015 vs.\\\\ uniform), while over-cleaning ($\\\\tau > 0.8$) causes sharper regression as $\\\\bstar$ inflates (mean $\\\\bar{b}^* = 2.36$ at $\\\\tau{=}0.9$, 3.08 at $\\\\tau{=}0.95$).\\nThis asymmetry reinforces the minimum intervention intuition: the cost of doing too little is small, whereas the cost of doing too much is steep.\\nWe recommend $\\\\tau = 0.8$ as a principled default; practitioners operating at different contamination rates can adjust within the safe range with low risk.\\n\\n\\\\paragraph{Connection to convergence theory.}\\n\\\\citet{wang_2026_survive_contamination} prove that pretraining convergence rate scales with $\\\\alpha$, the effective real data fraction.\\nOur $\\\\tau$ serves an analogous role---setting a floor on the weighted real proportion per batch---but an important distinction must be noted: their analysis assumes a known contamination proportion, whereas our method estimates quality from detector scores without access to the true $\\\\alpha$.\\nWe therefore position $\\\\tau$ as an empirical hyperparameter with theoretical motivation: convergence theory explains \\\\emph{why} a quality threshold improves training, while the specific value of $\\\\tau$ is determined empirically.\\nBridging this gap---deriving $\\\\tau$ from first principles without known proportions---is an open theoretical question.\\n```\\n\\n---\\n\\n=== discussion.tex ===\\n\\n```\\n\\\\paragraph{Why minimum intervention works.}\\nThe central finding of our experiments is that restraint in downweighting outperforms aggressiveness.\\nESS-only reweighting---which maximizes $b$ subject only to $\\\\mathrm{ESS} \\\\geq \\\\nmin$---degrades PPL to 17.723, \\\\emph{worse} than the uniform baseline (17.694, Table~\\\\ref{tab:main}).\\nThe dual-constrained adaptive $\\\\bstar$, by contrast, achieves 17.651 by selecting the \\\\emph{smallest} $b$ that meets the quality floor $\\\\tau$.\\nThe mechanism is clear from the binding statistics: in the 40.1\\\\% of reweighted batches where $\\\\aeff$ binds, mean $\\\\bstar = 1.67$ versus 4.15 under ESS-only---a 2.5$\\\\times$ less aggressive exponent that retains ESS\\\\,=\\\\,2.60, well above the floor $\\\\nmin = 2$.\\nOver-downweighting discards gradient signal from borderline samples whose detector scores are intermediate (e.g., $q \\\\approx 0.4$--$0.6$); these samples carry partial but non-negligible training value, and aggressively suppressing them impoverishes the effective training distribution.\\nThe $\\\\aeff$ constraint prevents this by halting $b$ as soon as the quality target is met.\\n\\n\\\\paragraph{$\\\\tau$ as a practical dial.}\\nThe quality threshold $\\\\tau$ controls the trade-off between decontamination strength and sample retention.\\nOur sweep (Table~\\\\ref{tab:tau}) reveals a wide safe operating range: all $\\\\tau \\\\in [0.5, 0.8]$ outperform uniform training, with PPL varying only 0.035 across this interval.\\nThe sensitivity is asymmetric---under-cleaning ($\\\\tau < 0.8$) incurs mild degradation ($-$0.006 to $-$0.015 vs.\\\\ uniform), while over-cleaning ($\\\\tau > 0.8$) causes sharper regression as $\\\\bstar$ inflates (mean $\\\\bar{b}^* = 2.36$ at $\\\\tau{=}0.9$, 3.08 at $\\\\tau{=}0.95$).\\nThis asymmetry reinforces the minimum intervention intuition: the cost of doing too little is small, whereas the cost of doing too much is steep.\\nWe recommend $\\\\tau = 0.8$ as a principled default; practitioners operating at different contamination rates can adjust within the safe range with low risk.\\n\\n\\\\paragraph{Connection to convergence theory.}\\n\\\\citet{wang2026survive} prove that pretraining convergence rate scales with $\\\\alpha$, the effective real data fraction.\\nOur $\\\\tau$ serves an analogous role---setting a floor on the weighted real proportion per batch---but an important distinction must be noted: their analysis assumes a known contamination proportion, whereas our method estimates quality from detector scores without access to the true $\\\\alpha$.\\nWe therefore position $\\\\tau$ as an empirical hyperparameter with theoretical motivation: convergence theory explains \\\\emph{why} a quality threshold improves training, while the specific value of $\\\\tau$ is determined empirically.\\nBridging this gap---deriving $\\\\tau$ from first principles without known proportions---is an open theoretical question.\\n```\\n\\n---\\n\\n=== conclusion_386ecc.tex ===\\n\\n```\\n\\\\section{Conclusion}\\n\\\\label{sec:conclusion}\\n\\nWe introduced Minimum Intervention Reweighting, a dual-constrained framework for contamination-aware pretraining that selects per-batch exponents $b^*$ without validation data.\\nThe method finds the smallest $b$ satisfying $\\\\alpha_{\\\\mathrm{eff}}(b) \\\\geq \\\\tau$ subject to $\\\\mathrm{ESS}(b) \\\\geq n_{\\\\min}$, enforcing a minimum-intervention principle: apply only as much downweighting as needed to meet a quality floor, no more.\\nThis stands in direct contrast to ESS-only (maximum-intervention) strategies, which we show degrade performance below even uniform baselines by over-downweighting contaminated samples.\\n\\nAcross three seeds at 0.6B scale with 40\\\\% synthetic contamination, adaptive $b^*$ matches grid-search-optimal PPL (17.651 vs.\\\\ 17.646) within seed variance, eliminating the $|\\\\mathcal{B}|$-run grid search entirely.\\nThe quality threshold $\\\\tau$ is robust across $[0.5, 0.8]$---all values in this range outperform uniform weighting.\\nA lightweight TF-IDF + logistic regression detector (AUC\\\\,0.94) suffices when post-hoc calibrated (ECE\\\\,0.048); score calibration matters more than raw discriminative power.\\nThe batch-level constraint regime---49.9\\\\% clean (no reweighting needed), 20.2\\\\% $\\\\alpha_{\\\\mathrm{eff}}$-binding, 30.0\\\\% ESS-binding---confirms that both constraints are active and complementary in practice.\\n\\n\\\\section*{Limitations}\\n\\\\label{sec:limitations}\\n\\n\\\\paragraph{Scale.}\\nAll experiments use a single model size (Qwen3-0.6B) with batch size 4.\\nBatch-level $q$-score statistics concentrate differently at larger batch sizes typical of 3B+ training; the optimal $\\\\tau$ range and constraint dynamics may shift at scale.\\n\\n\\\\paragraph{Contamination distribution.}\\nWe inject synthetic data via uniform random mixing at a controlled ratio ($\\\\rho{=}0.4$).\\nReal web-scale contamination is domain-skewed, which may alter within-batch $\\\\alpha_{\\\\mathrm{eff}}$ distributions and require domain-aware extensions.\\n\\n\\\\paragraph{Detector coverage.}\\nWe evaluate one detector family (TF-IDF + logistic regression).\\nAlthough our results suggest calibration dominates discrimination for reweighting quality, a systematic ablation across detector architectures and quality levels is needed.\\n\\n\\\\paragraph{Threshold.}\\n$\\\\tau$ is an empirical hyperparameter.\\nThe convergence theory of \\\\citet{wang_2026_survive_contamination} assumes a known contamination proportion $\\\\alpha$, which we do not require; bridging this gap to derive $\\\\tau$ from first principles remains open.\\n\\n\\\\paragraph{Evaluation.}\\nWe report held-out perplexity only.\\nDownstream task evaluation (MMLU, HellaSwag) would strengthen the practical case, particularly at scales where PPL differences translate more reliably to task performance.\\n\\n\\\\paragraph{Effect size.}\\nThe PPL improvement over uniform weighting is 0.043 at 0.6B/40\\\\% contamination.\\nWhile consistent across seeds, this effect is modest; we expect amplification at higher contamination ratios and larger model scales, but verification is ongoing.\\n```\\n\\n---\\n\\n=== conclusion.tex ===\\n\\n(Identical content to conclusion_386ecc.tex — same verbatim text, no differences.)\\n\\n---\\n\\n=== table1_main_results.tex ===\\n\\n```\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Held-out perplexity under different weighting methods ($\\\\rho{=}0.4$, 3 seeds). $\\\\Delta$ is relative to the Uniform baseline.}\\n\\\\label{tab:main-results}\\n\\\\small\\n\\\\begin{tabular}{@{}lccccr@{}}\\n\\\\toprule\\nMethod & seed42 & seed123 & seed456 & Mean$\\\\pm$Std & $\\\\Delta$ \\\\\\\\\\n\\\\midrule\\nUniform                                  & 17.694 & 17.686 & 17.702 & 17.694$\\\\pm$0.008 & --- \\\\\\\\\\nGrid-best ($b{=}0.5$)                    & 17.651 & 17.638 & 17.650 & 17.646$\\\\pm$0.007 & $-$0.048 \\\\\\\\\\nAdaptive ($\\\\tau{=}0.8$, $n_{\\\\min}{=}3$\\\\textsuperscript{\\\\dag}) & 17.644 & 17.631 & 17.642 & \\\\textbf{17.639$\\\\pm$0.007} & $-$\\\\textbf{0.055} \\\\\\\\\\nAdaptive-fix ($\\\\tau{=}0.8$, $n_{\\\\min}{=}2$) & 17.653 & 17.643 & 17.657 & 17.651$\\\\pm$0.007 & $-$0.043 \\\\\\\\\\nESS-only                                 & 17.730 & 17.720 & 17.719 & 17.723$\\\\pm$0.006 & $+$0.029 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\n\\\\vspace{2pt}\\n{\\\\footnotesize \\\\textsuperscript{\\\\dag}$n_{\\\\min}{=}3$ is the original implementation (historical); $n_{\\\\min}{=}2$ is the theoretically derived correction.}\\n\\\\end{table}\\n```\\n\\n---\\n\\nAll 15 files have been returned verbatim. Note: `results_d0d647.tex` and `results.tex` are byte-for-byte identical, as are `conclusion_386ecc.tex` and `conclusion.tex`. The `discussion_270aaa.tex` and `discussion.tex` differ in only one citation key: `\\\\citet{wang_2026_survive_contamination}` (versioned) vs `\\\\citet{wang2026survive}` (base). The `table1_main_results.tex` contains a materially different table from the inline table in the results files — it includes an `Adaptive ($n_{\\\\min}{=}3$)` row showing PPL 17.639 (better than grid-best) and an `Adaptive-fix ($n_{\\\\min}{=}2$)` row at 17.651, whereas the results section tables only show `Adaptive (ours)` at 17.651 without the $n_{\\\\min}{=}3$ variant.\"\n  },\n  {\n    \"type\": \"text\",\n    \"text\": \"agentId: ac7fd3aa5a6be52f9 (use SendMessage with to: 'ac7fd3aa5a6be52f9' to continue this agent)\\n&lt;usage>total_tokens: 63594\\ntool_uses: 15\\nduration_ms: 337182&lt;/usage>\"\n  }\n]",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
````

</details>

---

### Assistant

_source line 85_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the file contents. Let me read the rest of the output file to make sure I have everything.

Let me now analyze systematically:

1. **Terminology consistency** across sections
2. **Number consistency** - PPL numbers in Table 1 vs text
3. **Claim consistency** - 3 contributions in intro vs evidence in results/discussion
4. **Citation consistency** 
5. **Terminology unification** 
6. **Missing content / TODOs**

Let me now go through each systematically.

### Key files and their latest versions:
- **introduction_c6a67f.tex** (latest) vs **introduction.tex** (base)


- **method_3f5a58.tex** (latest) vs **method.tex** (base)
- **related_work_0b6096.tex** (latest) vs **related_work.tex** (base)
- **experiments_86dfd1.tex** (latest) = **experiments.tex** (identical)
- **results_d0d647.tex** = **results.tex** (identical)
- **discussion_270aaa.tex** vs **discussion.tex** (differ in one cite key)
- **conclusion_386ecc.tex** = **conclusion.tex** (identical)
- **table1_main_results.tex** (standalone table)

Now I'm checking which versions are the current ones—the hashed versions appear to be the latest generated, so I'll focus on those for the consistency audit. Looking at the terminology across files, I'm noticing inconsistencies in how α_eff is notated: some files use the macro `\aeff` while others use the explicit form `\alpha_{\mathrm{eff}}`, and this varies even within the same file in some cases.

The same issue appears with b* notation—some files consistently use `\bstar` as a macro while others mix explicit forms like `b^*` and `b^{*}`. If these macros are defined in the main preamble, the rendering should be consistent, but the notation choices themselves are scattered across the document.

I'm also noticing a citation key inconsistency in the discussion section—the base file references one citation key while the latest version uses a different one for the same source. And the n_min notation follows the same pattern as the others: macros in some files, explicit subscript notation in others.

Looking at the rest of the files, τ is consistently formatted across everything, which is good. But b_tau and b_ESS show the same split—macros in the edited versions versus explicit formatting in the base files. Now I'm checking the numerical consistency in the main results section... Looking at the main results table, I'm seeing a discrepancy—there are actually two adaptive method rows with different hyperparameters and results. The version with n_min=3 achieves 17.639 (marked as the best), while the n_min=2 variant gets 17.651, but the results section only mentions the n_min=2 configuration as the reported method. This is a critical mismatch between what's being highlighted in the table versus what's described in the text.

Now checking the introduction, I notice it reports adaptive PPL as 17.650±0.007, which doesn't quite match the results table's mean of 17.651—a small but notable discrepancy that suggests the numbers may have been updated in one place but not the other.

Looking at the ESS-only variant, the introduction claims 17.722, but when I calculate from the results table (17.730+17.720+17.719)/3, I get 17.723—a critical rounding error that needs fixing.

Now checking the introduction_c6a67f.tex file, I'm finding more discrepancies: the adaptive mean is listed as 17.650 ± 0.007, but the actual average from the results is 17.651, so that's off by 0.001. The grid-searched value of 17.646 ± 0.007 checks out correctly though.

Moving through the rest of the document, the discussion section numbers all align properly with the results table—ESS-only at 17.723, uniform at 17.694, and adaptive at 17.651. The conclusion also matches, correctly stating the adaptive value versus the grid-search optimal. And when I cross-reference against the registry numbers from the task, the rounding is consistent: adaptive_fix_seed42 rounds to 17.653, uniform_seed42 to 17.694, and grid_b0.5_seed42 stays at 17.651.

I'm also seeing the other registry entries now—ess_only_seed42 at 17.73, golden_ratio_seed42 at 17.654, and a baseline_qwen3_0.6b at 22.97 which isn't mentioned in the paper since it's the pre-continued-pretraining baseline. The registry name "adaptive_fix" corresponds to the "Adaptive-fix" entry in the results table with n_min=2, so that's the main Adaptive result matching 17.653.

Now I'm looking at the batch statistics across different versions of the method section. The numbers vary slightly between the base version and the latest version—the base mentions 49.9% clean batches and specific values for α_eff-binding and ESS-binding strategies, while the latest version reports 40.1% of reweighted batches as α_eff-binding with the same mean b* of 1.67 versus 4.15 under ESS-only. The key insight is consistent: the adaptive approach is about 2.5× less aggressive than ESS-only while maintaining an effective sample size around 2.60.

There's a discrepancy I need to reconcile—the method.tex percentages (49.9%, 20.2%, 30.0%) don't align with the introduction's framing of "40% of cases" and "remaining 49.9%," so I should verify which breakdown is actually correct before finalizing the numbers across sections. I'm checking the micro-batch count against the training setup — 6,103 steps with 4 gradient accumulation steps gives 24,412 effective batches, but the paper reports 51,913 micro-batches, which doesn't match up unless it's calculated differently, maybe as total tokens divided by micro-batch size.

Let me work through this: 132M tokens divided by sequence length 2048 gives roughly 64,453 sequences, and with batch size 4 and gradient accumulation 4, that's an effective batch of 16 sequences per step, yielding about 4,028 steps — but the paper says 6,103. This suggests the total token count is higher than 132M, possibly because the contaminated corpus includes synthetic data. If the real data is 40% of the total with ρ=0.4, then the full corpus would be around 220M tokens, which gets closer to matching the reported step count. I'm trying to reconcile the micro-batch count with the optimizer steps — 51,913 divided by the gradient accumulation factor of 4 gives around 12,978 steps, which still doesn't align with the reported 6,103. The ratio between these numbers is roughly 8.5, which suggests either multiple runs are being counted or there's a different accounting method at play. If the 51,913 includes results across multiple seeds, dividing by 2 gets close to the expected 24,412 micro-batches, though it's not a perfect match. I'm working through the math on the training configuration and finding a real discrepancy — the method section claims 51,913 micro-batches, but the stated 6,103 optimizer steps with gradient accumulation 4 only gives 24,412 micro-batches. Even accounting for different GPU setups or batch size interpretations, I can't reconcile these numbers, and the token count implications suggest something's off.

Let me recalculate assuming the 51,913 figure is correct and work backward through possible epoch counts and token totals to see if there's a consistent interpretation. M is the actual number of tokens processed (not the corpus size). Then 132M / 2048 ≈ 64,453 / 4 ≈ 16,113 micro-batches. 16,113 ≠ 51,913.

Actually, maybe "132M tokens" is the real data corpus size and the total training involves more. The experiments say "We sample a 132M-token subset of FineWeb as the real-data source" and "inject them at ratio ρ = 0.4 via uniform random mixing." So if real data is 132M tokens and ρ = 0.4 (40% synthetic), then total data = 132M / 0.6 = 220M tokens. But wait, ρ = contamination ratio = |synthetic| / |total|. So if ρ = 0.4, then total = real / (1 - ρ) = 132M / 0.6 = 220M.

With 220M total tokens, that gives me about 107,422 sequences at 2048 tokens each, which breaks down to roughly 26,855 micro-batches and around 6,714 training steps. That's in the ballpark of 6,103, though there's still a gap to the 51,913 micro-batches mentioned in the method. The discrepancy might come from different batch size assumptions or how the data is actually partitioned—maybe the batch size isn't 4 samples as I've been assuming. but the configuration explicitly states "(batch size 4, gradient accumulation 4, effective batch 16)", so micro-batch is definitely 4. The real puzzle is whether "6,103 steps" refers to optimizer steps or micro-batch updates — if it's the latter, that gives 6,103 total micro-batches, which still doesn't align with the 51,913 figure. I should check if the latest version of the method file has different numbers, since this looks like a genuine inconsistency worth flagging.

Looking at the latest method file, I don't see the 51,913 number mentioned at all — it only appears in the base version. So if the paper is using the latest method version, this discrepancy isn't actually a problem. I'll note it anyway in case the older version is still being referenced.

Now I'm checking the intro contributions to see if the claims are consistent across versions.

The first two contributions check out: the method section develops the dual-constraint framework, and the results show the adaptive approach matches grid-searched values within seed variance while outperforming ESS-only. But the third contribution claims the detector achieves results comparable to stronger neural detectors, when the paper only actually tests one detector. That's a mismatch between what's claimed and what's demonstrated. There's a major inconsistency in how citations are formatted between the latest and base versions of the paper — the newer files use simplified cite keys without underscores, while the older versions use longer underscore-separated keys. This mismatch needs to be resolved for consistency.

Beyond the key names themselves, there's also variation in the citation commands: the latest files mix `\cite{}` and `\citep{}`, whereas the base files use `\citet{}` and `\citealt{}`. While both approaches are valid in natbib, I need to ensure the paper uses one consistent citation style throughout, especially since different sections might be pulling from different file versions.

Looking at specific examples, the discussion files are using different bib key formats entirely — one uses underscores like `wang_2026_survive_contamination` while the other uses no underscores like `wang2026survive`. If sections from both versions get combined, these mismatched keys will cause citations to fail.

For terminology, I'm checking consistency across the paper: "minimum intervention" appears uniform, and "Minimum Intervention Reweighting" is used as the title in the conclusion. However, there's some variation between "dual-constraint" and "dual-constrained" across different sections that needs standardizing. The terminology checks are mostly consistent — contamination-aware, detect-and-reweight, and α_eff-binding all use the same format throughout. The grid-search usage is actually correct since it's hyphenated when modifying a noun but not when standing alone. I'm noticing there are no explicit TODOs or LaTeX todo commands, and some referenced sections like the Abstract and Appendices appear to be missing from these files.

Now I'm checking the cross-references — the results section mentions Appendix A and proof appendices that I need to verify exist, and there's a potential label conflict where the results section references `tab:main` but the table file defines `tab:main-results`. I'm also spotting a critical discrepancy in the table values where the main results table and the inline results table show different numbers for the Adaptive method, which suggests one of them might be outdated or there's a version mismatch. I'm seeing a fundamental conflict in the paper's presentation: the main results table treats n_min=3 as the primary adaptive configuration and marks it as best, but the text throughout uses n_min=2 results and claims adaptive matches grid-search performance. The sensitivity analysis further undermines this by noting the n_min=3 value comes from an earlier run, not an independent ablation. I need to decide which configuration should be the main result and then systematically update all claims—the table comparisons, the text descriptions, and the conclusion—to be internally consistent.

Now I'm checking the numerical claims against the actual data. The intro reports PPL 17.650 ± 0.007, but when I calculate the standard deviation from the three seed runs, I get approximately 0.007 which is correct, though the mean should be 17.651 rather than 17.650. The method section cites PPL = 17.789 for n_min=1, which matches what appears in the sensitivity table, so I need to verify this value is used consistently across all sections. Now I'm verifying the per-seed improvements match the reported values—seed 42 shows 0.041, seed 123 shows 0.043, and seed 456 shows 0.045—and confirming the maximum gap between runs stays within the stated 0.007 threshold.

The adaptive-versus-grid gap of 0.007 is indeed less than half the cross-seed range of the uniform baseline, which spans 0.016, so that checks out.

Looking at the version coherence issue, there's a split between base files using `\citet{}` with explicit notation and hash files using `\cite{}` with macros—if sections are mixed across generations, the citation styles and bibliography keys will clash.

Now I'm compiling the critical issues I've found: the primary adaptive configuration differs between Table 1 and the results text, there are rounding discrepancies in the reported PPL values for both adaptive and ESS-only means, citation keys are incompatible across file versions, and the table labels themselves don't match. Beyond those, there are also warnings about notation inconsistencies and citation command mismatches between versions. I should write up the full audit report with these findings. dual-constrained" vs "dual-constraint" inconsistent across sections
4. Contribution 3 claims TF-IDF+LR achieves "results comparable to stronger neural detectors" but no direct comparison experiment exists
5. Method.tex (base) claims 51,913 micro-batches but experiments says 6,103 steps × 4 accum = 24,412 micro-batches
6. n_min=3 footnoted as "not an independent ablation" in results sensitivity table but used as primary result in table1

**INFO:**
1. Golden Ratio row missing from table1_main_results.tex (only in results inline table)
2. Appendix references (app:grid, app:proofs) — need to verify these exist
3. Figure reference (fig:dual_constraint) — need to verify this exists
4. No Abstract section found
5. The base_qwen3_0.6b model shows a perplexity of 22.97 that doesn't appear to be documented anywhere in the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "9c264d51-424c-4d30-9eb5-80c3fb60fbdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bpk8rj3McZCoq58TKo6NLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22655,
      "cache_read_input_tokens": 28147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22655
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

I have all the file contents. Now let me conduct the systematic audit and write the report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "424ae165-dc5e-4948-a2ce-010ab0d96024",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bpk8rj3McZCoq58TKo6NLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22655,
      "cache_read_input_tokens": 28147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22655
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BYrQ41534ssXUpwLHoqyFJ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "595ef273-68ca-45f0-b92a-88a31eec0977",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bpk8rj3McZCoq58TKo6NLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22655,
      "cache_read_input_tokens": 28147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22655
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-16T01:08:54.057Z_

<details><summary>↩ Tool result · `toolu_01BYrQ41534ssXUpwLHoqyFJ`</summary>

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
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "84cd7072-8667-4211-917c-25bb72b7693a",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 89_

The save_project_file tool only accepts a whitelist of files. I'll write the audit report directly to the artifacts directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "06eaab71-06dd-4d76-ac58-85e8f72746a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BaW2x5H1R3tNbHDn2atDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9814,
      "cache_read_input_tokens": 50802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9814
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

_source line 90_

<details open><summary>🔧 Tool call — Bash · `toolu_011BjeQoN3AJZmE4oNAjJT8g`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/",
  "description": "List paper artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "40df3f2d-90ca-43cd-95e2-9c2344bad7aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BaW2x5H1R3tNbHDn2atDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9814,
      "cache_read_input_tokens": 50802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9814
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

_source line 91 · 2026-05-16T01:08:59.104Z_

<details><summary>↩ Tool result · `toolu_011BjeQoN3AJZmE4oNAjJT8g`</summary>

```text
conclusion.tex
conclusion_386ecc.tex
discussion.tex
discussion_270aaa.tex
experiment_setup_draft.md
experiments.tex
experiments_1613c9.tex
experiments_86dfd1.tex
introduction.tex
introduction_a663ee.tex
introduction_c6a67f.tex
introduction_draft.md
method.tex
method_3f5a58.tex
method_76a694.tex
method_section_draft.md
related_work.tex
related_work_0b6096.tex
related_work_963aec.tex
related_work_draft.md
related_work_draft_0db5c4.md
results.tex
results_819b43.tex
results_d0d647.tex
table1_main_results.tex
writing_plan_v1_info.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "4fbd1535-4333-4215-9148-774bf7498e8b",
  "tool_use_result": {
    "stdout": "conclusion.tex\nconclusion_386ecc.tex\ndiscussion.tex\ndiscussion_270aaa.tex\nexperiment_setup_draft.md\nexperiments.tex\nexperiments_1613c9.tex\nexperiments_86dfd1.tex\nintroduction.tex\nintroduction_a663ee.tex\nintroduction_c6a67f.tex\nintroduction_draft.md\nmethod.tex\nmethod_3f5a58.tex\nmethod_76a694.tex\nmethod_section_draft.md\nrelated_work.tex\nrelated_work_0b6096.tex\nrelated_work_963aec.tex\nrelated_work_draft.md\nrelated_work_draft_0db5c4.md\nresults.tex\nresults_819b43.tex\nresults_d0d647.tex\ntable1_main_results.tex\nwriting_plan_v1_info.txt",
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

_source line 92_

<details open><summary>🔧 Tool call — Write · `toolu_012zAXZFWCQYx9AZCZTMdYeQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md",
  "content": "# Consistency Audit Report\n\n**Paper**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**Date**: 2026-05-16\n**Audited files**: All `.tex` files in `artifacts/_project/paper/` (both base and hash-versioned)\n\n---\n\n## CRITICAL Issues\n\n### C1. Table1 vs Results Text: Conflicting Primary Configuration\n\n**table1_main_results.tex** presents Adaptive with `n_min=3` as the primary result (bolded best, PPL 17.639, Delta=-0.055), with `n_min=2` as a secondary row labeled \"Adaptive-fix.\"\n\n**results_d0d647.tex** (and all other sections) use `n_min=2` as the primary \"Adaptive (ours)\" configuration (PPL 17.651, Delta=-0.043). The n_min=3 variant appears only in the sensitivity table (Table `tab:nmin`) with a footnote: \"From an earlier adaptive configuration; not an independent ablation.\"\n\n**Consequences:**\n- The intro claims \"adaptive matches grid-best within seed variance (17.651 vs 17.646)\" — consistent with n_min=2, inconsistent with table1's n_min=3 (17.639 vs 17.646, which *beats* grid-best).\n- The conclusion says \"adaptive b* matches grid-search-optimal PPL (17.651 vs. 17.646)\" — same conflict.\n- The discussion quotes adaptive PPL as 17.651 — same conflict.\n\n**Fix**: Decide which is the primary configuration. If n_min=2, remove or demote n_min=3 from table1. If n_min=3, update ALL text references to use 17.639 numbers and change the narrative from \"matches grid-best\" to \"outperforms grid-best.\"\n\n### C2. Introduction (c6a67f) Reports Wrong Adaptive Mean PPL\n\nText says: \"PPL 17.650 +/- 0.007\"\nCorrect value: (17.653 + 17.643 + 17.657) / 3 = **17.651**\n\nOff by 0.001. Small, but a number mismatch in the intro is visible to every reviewer.\n\n### C3. Introduction (base) Reports Wrong ESS-only Mean PPL\n\nText says: \"ESS-only variant (maximum intervention) yields mean PPL 17.722\"\nCorrect value from results table: (17.730 + 17.720 + 17.719) / 3 = **17.723**\n\nOff by 0.001.\n\n### C4. Citation Key Incompatibility Between File Versions\n\nHash-versioned files (c6a67f, 3f5a58, 0b6096, 86dfd1, 270aaa, 386ecc) use **short cite keys**:\n`\\cite{shumailov2024model}`, `\\cite{drayson2025detection}`, `\\cite{vehtari2024psis}`, etc.\n\nBase files use **underscore cite keys**:\n`\\citet{shumailov_2024_model_collapse}`, `\\citet{drayson_2025_detection_collapse}`, `\\citet{vehtari_2024_psis}`, etc.\n\nIf the final paper mixes sections from both generations, half the citations will produce \"[?]\" in the compiled PDF.\n\n**Fix**: Pick ONE citation key convention matching the `.bib` file. Update all sections to use it.\n\n### C5. Duplicate Table Labels\n\n- `results_d0d647.tex` defines `\\label{tab:main}`\n- `table1_main_results.tex` defines `\\label{tab:main-results}`\n\nIf both tables are included, `\\ref{tab:main}` in the text won't point to `table1_main_results.tex`. If only one table is included, ensure all `\\ref{}` calls use the correct label.\n\n---\n\n## WARNING Issues\n\n### W1. Macro vs Explicit Notation Inconsistency\n\nHash-versioned files use LaTeX macros: `\\aeff`, `\\bstar`, `\\nmin`, `\\btau`, `\\bess`\nBase files use explicit notation: `\\alpha_{\\mathrm{eff}}`, `b^*`, `n_{\\min}`, `b_\\tau`, `b_{\\mathrm{ESS}}`\n\nIf sections are mixed, macros must be defined in the preamble. If all-base is used, no macro definitions are needed. This isn't a compilation error if macros are defined, but it creates maintenance risk.\n\n### W2. Citation Command Style Inconsistency\n\nHash-versioned files use: `\\cite{}`, `\\citep{}`\nBase files use: `\\citet{}`, `\\citealt{}`\n\nIn natbib, `\\cite{}` and `\\citet{}` produce the same output, but mixing styles across sections looks inconsistent in source and may confuse co-authors or reviewers reading the LaTeX.\n\n### W3. \"dual-constrained\" vs \"dual-constraint\" Inconsistency\n\n| Location | Wording |\n|----------|---------|\n| intro (c6a67f) | \"dual-constraint framework\" |\n| method (3f5a58) | \"Dual-Constraint Framework\" (section title) |\n| results (d0d647) | \"dual-constrained adaptive b*\", \"dual constraint\" |\n| discussion (270aaa) | \"dual-constrained adaptive b*\", \"dual-constraint solver\" |\n| conclusion (386ecc) | \"dual-constrained framework\" |\n\n**Fix**: Standardize to one form. Recommendation: \"dual-constraint\" as compound modifier (e.g., \"dual-constraint framework\"), \"dual-constrained\" when used as predicate adjective.\n\n### W4. Contribution 3 Overclaims Neural Detector Comparability\n\nIntroduction (c6a67f) contribution 3: \"A demonstration that a lightweight TF-IDF + LR detector with calibrated q-scores supports effective reweighting, achieving results comparable to stronger neural detectors.\"\n\nThe paper never runs experiments with neural detectors (e.g., ModernBERT). There is no direct comparison. The only evidence is that TF-IDF+LR \"suffices\" — which is weaker than \"comparable to.\"\n\nIntroduction (base) contribution 3 has the same issue: \"achieving results comparable to stronger neural detectors (§experiments).\"\n\n**Fix**: Soften to \"suffices for effective reweighting\" or add an ablation with a neural detector.\n\n### W5. Micro-batch Count Mismatch (method.tex base only)\n\n`method.tex` (base): \"Across 51,913 micro-batches in our main experiment\"\n`experiments.tex`: \"6,103 steps (batch size 4, gradient accumulation 4, effective batch 16)\"\n\nExpected micro-batches: 6,103 steps x 4 gradient accumulation = **24,412**. The claimed 51,913 is ~2.1x larger.\n\nNote: `method_3f5a58.tex` (latest) does NOT include the 51,913 figure, so this is only a problem if the base method version is used.\n\n### W6. n_min=3 Has Contradictory Status\n\n- `table1_main_results.tex`: n_min=3 is the **primary result** (bolded, best PPL)\n- `results_d0d647.tex` sensitivity table: n_min=3 is footnoted as \"From an earlier adaptive configuration; **not an independent ablation**\"\n\nThese two characterizations are mutually exclusive. Either n_min=3 is a legitimate main result or it's a historical artifact.\n\n### W7. discussion.tex vs discussion_270aaa.tex Citation Key Divergence\n\n- `discussion_270aaa.tex`: `\\citet{wang_2026_survive_contamination}` (underscore style)\n- `discussion.tex`: `\\citet{wang2026survive}` (short style)\n\nThese are different bib keys for the same reference. Only one will resolve.\n\n---\n\n## INFO Issues\n\n### I1. Golden Ratio Row Missing from table1_main_results.tex\n\nThe inline table in `results_d0d647.tex` includes a Golden Ratio row (PPL 17.654, seed 42 only). `table1_main_results.tex` omits it. If table1 is the canonical table, the Golden Ratio baseline comparison is lost.\n\n### I2. Appendix and Figure References Not Verifiable\n\nThe following cross-references are used but no corresponding files exist in the paper directory:\n- `\\ref{app:grid}` — Appendix with full grid sweep results\n- `\\ref{app:proofs}` — Appendix with full monotonicity proofs\n- `\\ref{fig:dual_constraint}` — Dual constraint illustration figure\n\nThese may exist in main.tex or other files not audited. Verify before submission.\n\n### I3. No Abstract Section Found\n\nNo `abstract.tex` in the paper directory. It may be in `main.tex`. Verify that the abstract is consistent with the body — especially the PPL numbers, which must match whichever configuration (n_min=2 or n_min=3) is chosen as primary.\n\n### I4. Baseline PPL Not Reported\n\nRegistry shows `baseline_qwen3_0.6b: PPL=22.97` (pre-continued-pretraining). This provides useful context (continued pretraining improves PPL from 22.97 to ~17.65) but is not mentioned in the paper. Consider adding to experiments or results for completeness.\n\n### I5. Two File Generations Create Maintenance Risk\n\nThere are two complete parallel sets of sections:\n- **Base** (no hash): explicit notation, underscore cite keys, `\\citet` commands\n- **Hash** (latest): macro notation, short cite keys, `\\cite`/`\\citep` commands\n\nThe final `main.tex` must `\\input{}` from exactly one generation per section. Mixing will cause compilation failures (undefined macros) and citation resolution errors.\n\n**Recommendation**: Delete or archive whichever generation is not used in the final paper to prevent accidental inclusion.\n\n---\n\n## Summary\n\n| Severity | Count | Key Actions |\n|----------|-------|-------------|\n| CRITICAL | 5 | Fix table1 vs results conflict (C1); correct PPL numbers (C2, C3); unify cite keys (C4); resolve table labels (C5) |\n| WARNING | 7 | Standardize notation/macros (W1, W2); unify terminology (W3); soften contribution 3 (W4); verify micro-batch count (W5); resolve n_min=3 status (W6); fix discussion cite key (W7) |\n| INFO | 5 | Add Golden Ratio to table1 (I1); verify appendix/figure refs (I2); check abstract (I3); consider baseline PPL (I4); clean up file generations (I5) |\n\n**Highest priority before submission**: Resolve C1 (which n_min is the primary configuration) — this affects the entire narrative of the paper.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "e5c4d992-f721-4291-8a7e-3ac34d019282",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vmm8H5wmro2qzykdJwEUFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 453,
      "cache_read_input_tokens": 60616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 453
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-16T01:09:50.542Z_

<details><summary>↩ Tool result · `toolu_012zAXZFWCQYx9AZCZTMdYeQ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "db2149e9-7129-4180-9f09-3c3e172f4a94",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md",
    "content": "# Consistency Audit Report\n\n**Paper**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**Date**: 2026-05-16\n**Audited files**: All `.tex` files in `artifacts/_project/paper/` (both base and hash-versioned)\n\n---\n\n## CRITICAL Issues\n\n### C1. Table1 vs Results Text: Conflicting Primary Configuration\n\n**table1_main_results.tex** presents Adaptive with `n_min=3` as the primary result (bolded best, PPL 17.639, Delta=-0.055), with `n_min=2` as a secondary row labeled \"Adaptive-fix.\"\n\n**results_d0d647.tex** (and all other sections) use `n_min=2` as the primary \"Adaptive (ours)\" configuration (PPL 17.651, Delta=-0.043). The n_min=3 variant appears only in the sensitivity table (Table `tab:nmin`) with a footnote: \"From an earlier adaptive configuration; not an independent ablation.\"\n\n**Consequences:**\n- The intro claims \"adaptive matches grid-best within seed variance (17.651 vs 17.646)\" — consistent with n_min=2, inconsistent with table1's n_min=3 (17.639 vs 17.646, which *beats* grid-best).\n- The conclusion says \"adaptive b* matches grid-search-optimal PPL (17.651 vs. 17.646)\" — same conflict.\n- The discussion quotes adaptive PPL as 17.651 — same conflict.\n\n**Fix**: Decide which is the primary configuration. If n_min=2, remove or demote n_min=3 from table1. If n_min=3, update ALL text references to use 17.639 numbers and change the narrative from \"matches grid-best\" to \"outperforms grid-best.\"\n\n### C2. Introduction (c6a67f) Reports Wrong Adaptive Mean PPL\n\nText says: \"PPL 17.650 +/- 0.007\"\nCorrect value: (17.653 + 17.643 + 17.657) / 3 = **17.651**\n\nOff by 0.001. Small, but a number mismatch in the intro is visible to every reviewer.\n\n### C3. Introduction (base) Reports Wrong ESS-only Mean PPL\n\nText says: \"ESS-only variant (maximum intervention) yields mean PPL 17.722\"\nCorrect value from results table: (17.730 + 17.720 + 17.719) / 3 = **17.723**\n\nOff by 0.001.\n\n### C4. Citation Key Incompatibility Between File Versions\n\nHash-versioned files (c6a67f, 3f5a58, 0b6096, 86dfd1, 270aaa, 386ecc) use **short cite keys**:\n`\\cite{shumailov2024model}`, `\\cite{drayson2025detection}`, `\\cite{vehtari2024psis}`, etc.\n\nBase files use **underscore cite keys**:\n`\\citet{shumailov_2024_model_collapse}`, `\\citet{drayson_2025_detection_collapse}`, `\\citet{vehtari_2024_psis}`, etc.\n\nIf the final paper mixes sections from both generations, half the citations will produce \"[?]\" in the compiled PDF.\n\n**Fix**: Pick ONE citation key convention matching the `.bib` file. Update all sections to use it.\n\n### C5. Duplicate Table Labels\n\n- `results_d0d647.tex` defines `\\label{tab:main}`\n- `table1_main_results.tex` defines `\\label{tab:main-results}`\n\nIf both tables are included, `\\ref{tab:main}` in the text won't point to `table1_main_results.tex`. If only one table is included, ensure all `\\ref{}` calls use the correct label.\n\n---\n\n## WARNING Issues\n\n### W1. Macro vs Explicit Notation Inconsistency\n\nHash-versioned files use LaTeX macros: `\\aeff`, `\\bstar`, `\\nmin`, `\\btau`, `\\bess`\nBase files use explicit notation: `\\alpha_{\\mathrm{eff}}`, `b^*`, `n_{\\min}`, `b_\\tau`, `b_{\\mathrm{ESS}}`\n\nIf sections are mixed, macros must be defined in the preamble. If all-base is used, no macro definitions are needed. This isn't a compilation error if macros are defined, but it creates maintenance risk.\n\n### W2. Citation Command Style Inconsistency\n\nHash-versioned files use: `\\cite{}`, `\\citep{}`\nBase files use: `\\citet{}`, `\\citealt{}`\n\nIn natbib, `\\cite{}` and `\\citet{}` produce the same output, but mixing styles across sections looks inconsistent in source and may confuse co-authors or reviewers reading the LaTeX.\n\n### W3. \"dual-constrained\" vs \"dual-constraint\" Inconsistency\n\n| Location | Wording |\n|----------|---------|\n| intro (c6a67f) | \"dual-constraint framework\" |\n| method (3f5a58) | \"Dual-Constraint Framework\" (section title) |\n| results (d0d647) | \"dual-constrained adaptive b*\", \"dual constraint\" |\n| discussion (270aaa) | \"dual-constrained adaptive b*\", \"dual-constraint solver\" |\n| conclusion (386ecc) | \"dual-constrained framework\" |\n\n**Fix**: Standardize to one form. Recommendation: \"dual-constraint\" as compound modifier (e.g., \"dual-constraint framework\"), \"dual-constrained\" when used as predicate adjective.\n\n### W4. Contribution 3 Overclaims Neural Detector Comparability\n\nIntroduction (c6a67f) contribution 3: \"A demonstration that a lightweight TF-IDF + LR detector with calibrated q-scores supports effective reweighting, achieving results comparable to stronger neural detectors.\"\n\nThe paper never runs experiments with neural detectors (e.g., ModernBERT). There is no direct comparison. The only evidence is that TF-IDF+LR \"suffices\" — which is weaker than \"comparable to.\"\n\nIntroduction (base) contribution 3 has the same issue: \"achieving results comparable to stronger neural detectors (§experiments).\"\n\n**Fix**: Soften to \"suffices for effective reweighting\" or add an ablation with a neural detector.\n\n### W5. Micro-batch Count Mismatch (method.tex base only)\n\n`method.tex` (base): \"Across 51,913 micro-batches in our main experiment\"\n`experiments.tex`: \"6,103 steps (batch size 4, gradient accumulation 4, effective batch 16)\"\n\nExpected micro-batches: 6,103 steps x 4 gradient accumulation = **24,412**. The claimed 51,913 is ~2.1x larger.\n\nNote: `method_3f5a58.tex` (latest) does NOT include the 51,913 figure, so this is only a problem if the base method version is used.\n\n### W6. n_min=3 Has Contradictory Status\n\n- `table1_main_results.tex`: n_min=3 is the **primary result** (bolded, best PPL)\n- `results_d0d647.tex` sensitivity table: n_min=3 is footnoted as \"From an earlier adaptive configuration; **not an independent ablation**\"\n\nThese two characterizations are mutually exclusive. Either n_min=3 is a legitimate main result or it's a historical artifact.\n\n### W7. discussion.tex vs discussion_270aaa.tex Citation Key Divergence\n\n- `discussion_270aaa.tex`: `\\citet{wang_2026_survive_contamination}` (underscore style)\n- `discussion.tex`: `\\citet{wang2026survive}` (short style)\n\nThese are different bib keys for the same reference. Only one will resolve.\n\n---\n\n## INFO Issues\n\n### I1. Golden Ratio Row Missing from table1_main_results.tex\n\nThe inline table in `results_d0d647.tex` includes a Golden Ratio row (PPL 17.654, seed 42 only). `table1_main_results.tex` omits it. If table1 is the canonical table, the Golden Ratio baseline comparison is lost.\n\n### I2. Appendix and Figure References Not Verifiable\n\nThe following cross-references are used but no corresponding files exist in the paper directory:\n- `\\ref{app:grid}` — Appendix with full grid sweep results\n- `\\ref{app:proofs}` — Appendix with full monotonicity proofs\n- `\\ref{fig:dual_constraint}` — Dual constraint illustration figure\n\nThese may exist in main.tex or other files not audited. Verify before submission.\n\n### I3. No Abstract Section Found\n\nNo `abstract.tex` in the paper directory. It may be in `main.tex`. Verify that the abstract is consistent with the body — especially the PPL numbers, which must match whichever configuration (n_min=2 or n_min=3) is chosen as primary.\n\n### I4. Baseline PPL Not Reported\n\nRegistry shows `baseline_qwen3_0.6b: PPL=22.97` (pre-continued-pretraining). This provides useful context (continued pretraining improves PPL from 22.97 to ~17.65) but is not mentioned in the paper. Consider adding to experiments or results for completeness.\n\n### I5. Two File Generations Create Maintenance Risk\n\nThere are two complete parallel sets of sections:\n- **Base** (no hash): explicit notation, underscore cite keys, `\\citet` commands\n- **Hash** (latest): macro notation, short cite keys, `\\cite`/`\\citep` commands\n\nThe final `main.tex` must `\\input{}` from exactly one generation per section. Mixing will cause compilation failures (undefined macros) and citation resolution errors.\n\n**Recommendation**: Delete or archive whichever generation is not used in the final paper to prevent accidental inclusion.\n\n---\n\n## Summary\n\n| Severity | Count | Key Actions |\n|----------|-------|-------------|\n| CRITICAL | 5 | Fix table1 vs results conflict (C1); correct PPL numbers (C2, C3); unify cite keys (C4); resolve table labels (C5) |\n| WARNING | 7 | Standardize notation/macros (W1, W2); unify terminology (W3); soften contribution 3 (W4); verify micro-batch count (W5); resolve n_min=3 status (W6); fix discussion cite key (W7) |\n| INFO | 5 | Add Golden Ratio to table1 (I1); verify appendix/figure refs (I2); check abstract (I3); consider baseline PPL (I4); clean up file generations (I5) |\n\n**Highest priority before submission**: Resolve C1 (which n_min is the primary configuration) — this affects the entire narrative of the paper.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 94_

审查报告已写入 `artifacts/_project/paper/consistency_audit.md`。

核心发现：

**最高优先级（CRITICAL x5）**：
1. **table1_main_results.tex 与 results 正文冲突**：table1 用 n_min=3 作为主结果（PPL 17.639，标粗），但正文全部用 n_min=2（PPL 17.651）。整篇论文的 narrative 取决于选哪个——需要立刻决定。
2. **intro (c6a67f) adaptive PPL 写成 17.650，实际是 17.651**
3. **intro (base) ESS-only PPL 写成 17.722，实际是 17.723**
4. **两代文件的 citation key 完全不兼容**（`shumailov2024model` vs `shumailov_2024_model_collapse`），混用会导致 [?]
5. **table label 冲突**：`tab:main` vs `tab:main-results`

**WARNING x7**：macro/notation 不统一、"dual-constrained" vs "dual-constraint" 混用、contribution 3 overclaim（声称 comparable to neural detectors 但没做对比实验）、method.tex 51,913 micro-batches 与 experiments 描述的 24,412 不符、n_min=3 在 table1 是主结果但在 sensitivity table 标注为"not an independent ablation"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "uuid": "d93d0a82-3a87-4bbe-9005-af594f71d9cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZF1ExARWLZHe1zJRgdvnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2837,
      "cache_read_input_tokens": 61069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2837
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

_source line 95_

审查报告已写入 `artifacts/_project/paper/consistency_audit.md`。

核心发现：

**最高优先级（CRITICAL x5）**：
1. **table1_main_results.tex 与 results 正文冲突**：table1 用 n_min=3 作为主结果（PPL 17.639，标粗），但正文全部用 n_min=2（PPL 17.651）。整篇论文的 narrative 取决于选哪个——需要立刻决定。
2. **intro (c6a67f) adaptive PPL 写成 17.650，实际是 17.651**
3. **intro (base) ESS-only PPL 写成 17.722，实际是 17.723**
4. **两代文件的 citation key 完全不兼容**（`shumailov2024model` vs `shumailov_2024_model_collapse`），混用会导致 [?]
5. **table label 冲突**：`tab:main` vs `tab:main-results`

**WARNING x7**：macro/notation 不统一、"dual-constrained" vs "dual-constraint" 混用、contribution 3 overclaim（声称 comparable to neural detectors 但没做对比实验）、method.tex 51,913 micro-batches 与 experiments 描述的 24,412 不符、n_min=3 在 table1 是主结果但在 sensitivity table 标注为"not an independent ablation"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 611250,
  "duration_api_ms": 611827,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "aa969b71-d198-4ba3-9b84-63a2c341d557",
  "total_cost_usd": 1.37497265,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 52459,
    "cache_read_input_tokens": 312692,
    "output_tokens": 14802,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52459,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 400,
        "cache_read_input_tokens": 61069,
        "cache_creation_input_tokens": 2837,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2837
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1477,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001572,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 14802,
      "cacheReadInputTokens": 312692,
      "cacheCreationInputTokens": 52459,
      "webSearchRequests": 0,
      "costUSD": 0.8543397500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-sonnet-4-6": {
      "inputTokens": 4,
      "outputTokens": 22292,
      "cacheReadInputTokens": 8113,
      "cacheCreationInputTokens": 48596,
      "webSearchRequests": 0,
      "costUSD": 0.5190608999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fb391a1a-8914-46e6-a127-ef5fb01f52a0"
}
```

</details>

---
