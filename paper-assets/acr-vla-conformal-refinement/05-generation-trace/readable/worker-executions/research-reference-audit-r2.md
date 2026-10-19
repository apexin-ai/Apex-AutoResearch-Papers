# research reference audit r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 128
- **Recorded user turns:** 0
- **Tool calls:** 47
- **Original source:** `logs/workers/worker_research_reference-audit-r2_20260515T204542.log`
- **Structured JSON:** [`d7006cfb739fd163a63d.json`](../../sessions/d7/d7006cfb739fd163a63d.json)

## Before a recorded user message

128 recorded events

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
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
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
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "6fa607b3-a8f2-4f62-ba68-75ca833081d2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778886600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "3496ca14-5128-49e6-bc44-3e76e3117e1c",
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996"
}
```

---

### Assistant

_source line 4_

I'll start by reading all four paper sections to identify every citation and its attributed method.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "8c8aa052-0114-4dd9-ac79-f34c2a0b7e5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrmDzRGj82635evd2U5WTP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11582,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11582
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DaELntcEpnuVDq31b2DtQb`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__edit_paper_section,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,WebSearch",
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
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "a8ab1def-ece1-44ed-accb-c16cedeab7b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrmDzRGj82635evd2U5WTP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11582,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11582
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

_source line 6 · 2026-05-15T20:45:56.129Z_

<details><summary>↩ Tool result · `toolu_01DaELntcEpnuVDq31b2DtQb`</summary>

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
  "tool_name": "mcp__agent-ml-research__edit_paper_section"
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
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
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
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "abe4f35d-50a2-463e-befc-e0ba9ea47952",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact",
      "WebSearch"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__edit_paper_section,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,WebSearch",
    "total_deferred_tools": 24
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me read all four paper sections in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "3ef7cdfa-26fd-4a90-9f4e-8df36dfc5de5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NP6Ka4okUYDzoWSZtqxH7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2237,
      "cache_read_input_tokens": 23423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2237
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

Reading all four paper sections now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "e8d14699-c182-4a95-8f73-f6e7c3605200",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NP6Ka4okUYDzoWSZtqxH7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2237,
      "cache_read_input_tokens": 23423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2237
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0172q1tV7Vayb12JVdnHinnn`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper/intro.md",
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
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "b587712e-4a46-4ae9-ae89-558d849adf56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NP6Ka4okUYDzoWSZtqxH7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2237,
      "cache_read_input_tokens": 23423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2237
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T20:46:00.465Z_

<details><summary>↩ Tool result · `toolu_0172q1tV7Vayb12JVdnHinnn`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/intro.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "536a7377-bbfb-4d8b-b4a2-520abfcc60db",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/intro.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/intro.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016qCMxHnvxfDcUBTdvAaSZW`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper/method.md",
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
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "1b31d3a6-5fbf-41de-9f10-b7d45e88a372",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NP6Ka4okUYDzoWSZtqxH7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2237,
      "cache_read_input_tokens": 23423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2237
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T20:46:00.958Z_

<details><summary>↩ Tool result · `toolu_016qCMxHnvxfDcUBTdvAaSZW`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/method.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "8673472f-0e00-4606-8f07-03d7c8d4259d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/method.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/method.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LCRqyhzyH4Tp2DJRav1Q2G`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper/experiments.md",
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
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "8ac4efad-2640-43d3-994c-abd4210ec176",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NP6Ka4okUYDzoWSZtqxH7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2237,
      "cache_read_input_tokens": 23423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2237
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T20:46:01.928Z_

<details><summary>↩ Tool result · `toolu_01LCRqyhzyH4Tp2DJRav1Q2G`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/experiments.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "26c2999c-75d2-4592-9baa-4aac7c7a51fb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/experiments.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/experiments.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019ovX14zJ5AMz8FbAk2hvEc`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper/related_work.md",
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
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "398be07f-3a67-44d6-88e9-026083f1a35d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NP6Ka4okUYDzoWSZtqxH7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2237,
      "cache_read_input_tokens": 23423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2237
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T20:46:02.242Z_

<details><summary>↩ Tool result · `toolu_019ovX14zJ5AMz8FbAk2hvEc`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/related_work.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "03a1dca5-a172-4c37-8ecc-9ce5f8b73968",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/related_work.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/related_work.md'\", \"metadata\": {}}"
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
The read_project_file tool doesn't support paper sections directly. Let me find the actual paper files on disk.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "6e88d6c1-1403-4c2e-8f11-76da9ebf442e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Doc9n1hV8FnAHbM6h6zpZL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1198,
      "cache_read_input_tokens": 25660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1198
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

Paper sections aren't in the whitelist for `read_project_file`. Let me find the actual files on disk.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "f2164e1f-bd9e-4d4f-b9fc-38b4e7ee296b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Doc9n1hV8FnAHbM6h6zpZL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1198,
      "cache_read_input_tokens": 25660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1198
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

<details open><summary>🔧 Tool call — Glob · `toolu_01FEUZp2JPA8WoHNqriyuc9J`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "141bf306-eb19-433e-8503-ff76ccc8a4d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Doc9n1hV8FnAHbM6h6zpZL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1198,
      "cache_read_input_tokens": 25660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1198
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

_source line 20 · 2026-05-15T20:46:06.656Z_

<details><summary>↩ Tool result · `toolu_01FEUZp2JPA8WoHNqriyuc9J`</summary>

```text
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260513T015051/best/review_report.md
artifacts/dream_reports/dream_20260513T015051/median/review_report.md
artifacts/dream_reports/dream_20260513T023849/best/paper_framing.md
artifacts/libero-smolvla-env-report.md
artifacts/dream_reports/dream_20260513T023849/median/paper_framing.md
artifacts/dream_reports/dream_20260513T023849/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T023849/best/review_report.md
artifacts/dream_reports/dream_20260513T023849/median/review_report.md
artifacts/dream_reports/dream_20260513T023849/worst/review_report.md
artifacts/pipeline-dimension-verification.md
.claude/sessions/paper_agent_f11cbd51/memory/MEMORY.md
artifacts/smolvla-libero-finetune-survey.md
artifacts/lerobot-pipeline-alignment.md
artifacts/_project/report/v4_deployment_report.md
task_context/history/reviewer/loop_1.md
task_context/history/director/loop_1.md
artifacts/eval-reconvla-spatial-v1-diag.md
artifacts/_project/report/claim-strength-analysis.md
artifacts/precompute-k5-analysis.md
artifacts/precompute-k5/report/precompute-k5-analysis.md
artifacts/reconvla-comparison-report.md
task_context/history/director/loop_2.md
task_context/history/agent/loop_1.md
task_context/history/agent/loop_1_1778714300.md
task_context/history/agent/loop_1_1778723011.md
artifacts/_project/report/next_batch_plan.md
artifacts/diag-eval-v6-batch-failure.md
task_context/history/agent/loop_1_1778724391.md
task_context/history/agent/loop_1_1778724423.md
task_context/history/agent/loop_1_1778725595.md
task_context/history/reviewer/loop_2.md
task_context/history/agent/loop_2.md
task_context/history/agent/loop_2_1778728390.md
task_context/history/agent/loop_2_1778728392.md
task_context/history/agent/loop_2_1778728430.md
task_context/history/agent/loop_2_1778728433.md
task_context/history/agent/loop_2_1778744616.md
artifacts/_project/report/object_eval_commands.md
artifacts/object_eval_commands.md
artifacts/_project/report/competitor_analysis.md
artifacts/competitor_analysis.md
artifacts/_project/report/spatial_comparison_template.md
artifacts/spatial_comparison_template.md
artifacts/_project/report/correction_degradation_literature.md
artifacts/correction_degradation_literature.md
artifacts/crm_bug_audit.md
artifacts/_project/report/crm_bug_audit.md
artifacts/_project/report/fix_plan_code_sketch.md
artifacts/fix_plan_code_sketch.md
task_context/history/agent/loop_2_1778744620.md
task_context/history/agent/loop_3.md
task_context/history/reviewer/loop_3.md
artifacts/crm-train-v2-k5/intermediate/crm-train-v2-k5-blocked.md
task_context/history/reviewer/loop_4.md
task_context/history/agent/loop_3_1778782316.md
task_context/history/agent/loop_3_1778782348.md
task_context/history/agent/loop_3_1778782354.md
task_context/history/agent/loop_2_1778782355.md
task_context/history/agent/loop_4.md
task_context/history/agent/loop_3_1778782364.md
task_context/history/agent/loop_2_1778782399.md
task_context/history/agent/loop_3_1778782438.md
task_context/history/agent/loop_3_1778782446.md
task_context/history/agent/loop_2_1778782494.md
task_context/history/agent/loop_3_1778793764.md
artifacts/report_eval_progress.md
task_context/history/agent/loop_4_1778793770.md
task_context/history/agent/loop_4_1778793795.md
task_context/history/agent/loop_3_1778793802.md
task_context/history/agent/loop_4_1778793812.md
task_context/history/agent/loop_4_1778793825.md
task_context/history/agent/loop_4_1778796615.md
artifacts/ablation_eval_commands.md
artifacts/report_running_status.md
artifacts/_project/report/progress-report-20260515-0526.md
task_context/history/agent/loop_5.md
task_context/history/agent/loop_5_1778796698.md
task_context/history/agent/loop_5_1778796702.md
task_context/history/agent/loop_3_1778796713.md
task_context/history/agent/loop_3_1778796714.md
task_context/history/agent/loop_4_1778796841.md
task_context/history/agent/loop_5_1778804002.md
task_context/history/reviewer/loop_5.md
task_context/history/agent/loop_5_1778808402.md
task_context/history/agent/loop_5_1778808416.md
task_context/history/agent/loop_4_1778808418.md
task_context/history/agent/loop_5_1778808421.md
task_context/history/agent/loop_4_1778808431.md
task_context/history/agent/loop_5_1778808440.md
task_context/history/agent/loop_5_1778808444.md
task_context/history/agent/loop_5_1778808445.md
task_context/history/agent/loop_4_1778808450.md
task_context/history/agent/loop_6.md
task_context/history/agent/loop_5_1778808483.md
task_context/history/agent/loop_5_1778808831.md
task_context/history/agent/loop_6_1778809114.md
task_context/history/agent/loop_6_1778809360.md
task_context/history/agent/loop_6_1778815552.md
artifacts/_project/report/competitive_analysis_20260515.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "f03a139c-ee7b-42aa-97c3-138d8f1fdf12",
  "tool_use_result": {
    "filenames": [
      "docs/IDEA_BRIEF.md",
      "artifacts/dream_reports/dream_20260513T015051/best/review_report.md",
      "artifacts/dream_reports/dream_20260513T015051/median/review_report.md",
      "artifacts/dream_reports/dream_20260513T023849/best/paper_framing.md",
      "artifacts/libero-smolvla-env-report.md",
      "artifacts/dream_reports/dream_20260513T023849/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260513T023849/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260513T023849/best/review_report.md",
      "artifacts/dream_reports/dream_20260513T023849/median/review_report.md",
      "artifacts/dream_reports/dream_20260513T023849/worst/review_report.md",
      "artifacts/pipeline-dimension-verification.md",
      ".claude/sessions/paper_agent_f11cbd51/memory/MEMORY.md",
      "artifacts/smolvla-libero-finetune-survey.md",
      "artifacts/lerobot-pipeline-alignment.md",
      "artifacts/_project/report/v4_deployment_report.md",
      "task_context/history/reviewer/loop_1.md",
      "task_context/history/director/loop_1.md",
      "artifacts/eval-reconvla-spatial-v1-diag.md",
      "artifacts/_project/report/claim-strength-analysis.md",
      "artifacts/precompute-k5-analysis.md",
      "artifacts/precompute-k5/report/precompute-k5-analysis.md",
      "artifacts/reconvla-comparison-report.md",
      "task_context/history/director/loop_2.md",
      "task_context/history/agent/loop_1.md",
      "task_context/history/agent/loop_1_1778714300.md",
      "task_context/history/agent/loop_1_1778723011.md",
      "artifacts/_project/report/next_batch_plan.md",
      "artifacts/diag-eval-v6-batch-failure.md",
      "task_context/history/agent/loop_1_1778724391.md",
      "task_context/history/agent/loop_1_1778724423.md",
      "task_context/history/agent/loop_1_1778725595.md",
      "task_context/history/reviewer/loop_2.md",
      "task_context/history/agent/loop_2.md",
      "task_context/history/agent/loop_2_1778728390.md",
      "task_context/history/agent/loop_2_1778728392.md",
      "task_context/history/agent/loop_2_1778728430.md",
      "task_context/history/agent/loop_2_1778728433.md",
      "task_context/history/agent/loop_2_1778744616.md",
      "artifacts/_project/report/object_eval_commands.md",
      "artifacts/object_eval_commands.md",
      "artifacts/_project/report/competitor_analysis.md",
      "artifacts/competitor_analysis.md",
      "artifacts/_project/report/spatial_comparison_template.md",
      "artifacts/spatial_comparison_template.md",
      "artifacts/_project/report/correction_degradation_literature.md",
      "artifacts/correction_degradation_literature.md",
      "artifacts/crm_bug_audit.md",
      "artifacts/_project/report/crm_bug_audit.md",
      "artifacts/_project/report/fix_plan_code_sketch.md",
      "artifacts/fix_plan_code_sketch.md",
      "task_context/history/agent/loop_2_1778744620.md",
      "task_context/history/agent/loop_3.md",
      "task_context/history/reviewer/loop_3.md",
      "artifacts/crm-train-v2-k5/intermediate/crm-train-v2-k5-blocked.md",
      "task_context/history/reviewer/loop_4.md",
      "task_context/history/agent/loop_3_1778782316.md",
      "task_context/history/agent/loop_3_1778782348.md",
      "task_context/history/agent/loop_3_1778782354.md",
      "task_context/history/agent/loop_2_1778782355.md",
      "task_context/history/agent/loop_4.md",
      "task_context/history/agent/loop_3_1778782364.md",
      "task_context/history/agent/loop_2_1778782399.md",
      "task_context/history/agent/loop_3_1778782438.md",
      "task_context/history/agent/loop_3_1778782446.md",
      "task_context/history/agent/loop_2_1778782494.md",
      "task_context/history/agent/loop_3_1778793764.md",
      "artifacts/report_eval_progress.md",
      "task_context/history/agent/loop_4_1778793770.md",
      "task_context/history/agent/loop_4_1778793795.md",
      "task_context/history/agent/loop_3_1778793802.md",
      "task_context/history/agent/loop_4_1778793812.md",
      "task_context/history/agent/loop_4_1778793825.md",
      "task_context/history/agent/loop_4_1778796615.md",
      "artifacts/ablation_eval_commands.md",
      "artifacts/report_running_status.md",
      "artifacts/_project/report/progress-report-20260515-0526.md",
      "task_context/history/agent/loop_5.md",
      "task_context/history/agent/loop_5_1778796698.md",
      "task_context/history/agent/loop_5_1778796702.md",
      "task_context/history/agent/loop_3_1778796713.md",
      "task_context/history/agent/loop_3_1778796714.md",
      "task_context/history/agent/loop_4_1778796841.md",
      "task_context/history/agent/loop_5_1778804002.md",
      "task_context/history/reviewer/loop_5.md",
      "task_context/history/agent/loop_5_1778808402.md",
      "task_context/history/agent/loop_5_1778808416.md",
      "task_context/history/agent/loop_4_1778808418.md",
      "task_context/history/agent/loop_5_1778808421.md",
      "task_context/history/agent/loop_4_1778808431.md",
      "task_context/history/agent/loop_5_1778808440.md",
      "task_context/history/agent/loop_5_1778808444.md",
      "task_context/history/agent/loop_5_1778808445.md",
      "task_context/history/agent/loop_4_1778808450.md",
      "task_context/history/agent/loop_6.md",
      "task_context/history/agent/loop_5_1778808483.md",
      "task_context/history/agent/loop_5_1778808831.md",
      "task_context/history/agent/loop_6_1778809114.md",
      "task_context/history/agent/loop_6_1778809360.md",
      "task_context/history/agent/loop_6_1778815552.md",
      "artifacts/_project/report/competitive_analysis_20260515.md"
    ],
    "durationMs": 17,
    "numFiles": 100,
    "truncated": true
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Glob · `toolu_0136HyWxssrtk8pDXWTkhK81`</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "330a8cf9-3aef-4089-87b2-ea4ef27b2ff7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Doc9n1hV8FnAHbM6h6zpZL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1198,
      "cache_read_input_tokens": 25660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1198
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

_source line 22 · 2026-05-15T20:46:07.161Z_

<details><summary>↩ Tool result · `toolu_0136HyWxssrtk8pDXWTkhK81`</summary>

```text
artifacts/_project/paper/references_e9d4d2.bib
artifacts/_project/paper/method_section_draft.tex
artifacts/_project/paper/corl_paper_outline.md
paper/outline.md
paper/sections/related_work.md
paper/figure_plan.md
artifacts/_project/paper/abstract_a1674b.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/introduction_c83872.tex
artifacts/_project/paper/introduction_scenarioC_607d8d.tex
artifacts/_project/paper/introduction_scenarioC.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/related_work_9c2927.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/references.bib
artifacts/_project/paper/related_work_80791f.tex
artifacts/_project/paper/method_fb526b.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/_project/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/references.bib
docs/paper/discussion.tex
artifacts/_project/paper/experiments.tex
docs/paper/experiments.tex
artifacts/_project/paper/experiments_ac6246.tex
artifacts/_project/paper/sections/discussion.tex
artifacts/_project/paper/sections/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "196b1523-965a-4612-a8c3-3393ab06efc8",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/references_e9d4d2.bib",
      "artifacts/_project/paper/method_section_draft.tex",
      "artifacts/_project/paper/corl_paper_outline.md",
      "paper/outline.md",
      "paper/sections/related_work.md",
      "paper/figure_plan.md",
      "artifacts/_project/paper/abstract_a1674b.tex",
      "docs/paper/method.tex",
      "docs/paper/related_work.tex",
      "docs/paper/abstract.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/introduction_c83872.tex",
      "artifacts/_project/paper/introduction_scenarioC_607d8d.tex",
      "artifacts/_project/paper/introduction_scenarioC.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/related_work_9c2927.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/references.bib",
      "artifacts/_project/paper/related_work_80791f.tex",
      "artifacts/_project/paper/method_fb526b.tex",
      "artifacts/_project/paper/experiments_c64a8c.tex",
      "artifacts/_project/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/references.bib",
      "docs/paper/discussion.tex",
      "artifacts/_project/paper/experiments.tex",
      "docs/paper/experiments.tex",
      "artifacts/_project/paper/experiments_ac6246.tex",
      "artifacts/_project/paper/sections/discussion.tex",
      "artifacts/_project/paper/sections/introduction.tex"
    ],
    "durationMs": 14,
    "numFiles": 30,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
I see the paper files are in multiple locations. The most likely "canonical" versions are in `docs/paper/` (introduction.tex, method.tex, etc.) or `artifacts/_project/paper/`. Let me also check `paper/sections/`. Let me read the most recent/canonical versions. The `docs/paper/` directory seems to have a clean set. Let me read those and also the artifacts versions to see which are the latest.

Let me read the docs/paper versions first since they look like the canonical location.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "f0e1703d-e78f-48df-8b96-a7b06c7b0bed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUttNzwViG4VYXFksFY3Hr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 26858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2504
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

_source line 24_

Found the paper files. Let me read the canonical versions from `docs/paper/` and any recent artifact versions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "c33d06b6-0628-4306-9d82-e55d9732c048",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUttNzwViG4VYXFksFY3Hr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 26858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2504
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

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01XdRKtnmBEFBAUFQXuZWxdg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "15bd35a6-f4ce-4c1a-86e7-1cf8305eba84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUttNzwViG4VYXFksFY3Hr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 26858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2504
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

_source line 26 · 2026-05-15T20:46:13.167Z_

<details><summary>↩ Tool result · `toolu_01XdRKtnmBEFBAUFQXuZWxdg`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	% --- Para 1: VLAs are impressive but fragile under distribution shift ---
5	Vision-language-action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached high success rates on in-distribution benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet this near-saturation masks a fragile reality: visual and physical perturbations routinely encountered in deployment---camera viewpoint shifts, object layout changes, robot initial state variation---can degrade success rates by over 65 percentage points---for example, $\pi_0$ drops from 94.2\% to 6.6\% under robot initial-state perturbation, and UniVLA from 95.2\% to 4.3\% under camera viewpoint changes~\cite{fei2025liberoplus}.
7	Closing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled settings.
8	
9	% --- Para 2: Existing approaches and the gap ---
10	Two lines of work address VLA robustness.
11	\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\cite{liu2026ttvla}.
12	These approaches are effective but require retraining or per-task RL, and their gains are bounded by the training distribution.
13	\emph{Inference-time methods} leave the policy frozen.
14	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution states, but operates as an uncertainty quantification framework rather than an action improvement method.
15	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\,s per control step---too slow for real-time manipulation.
16	A2C2~\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.
17	In short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.
18	
19	% --- Para 3: Our approach — sample-then-correct ---
20	We introduce \textbf{ACR-VLA} (\textbf{A}daptive \textbf{C}onformal \textbf{R}efinement for VLA), an inference-time module that improves frozen VLA actions through a \emph{sample-then-correct} pipeline.
21	At each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the most conforming candidate via Mahalanobis-based nonconformity scoring with shrinkage covariance estimation~\cite{ledoit2004well,braun2025cgs}, and then applies a learned residual correction via a lightweight \emph{Conformal Residual Module} (CRM).
22	CRM is a 329K-parameter MLP conditioned on the VLA's frozen observation embedding.
23	It predicts a small residual $\boldsymbol{\delta}$ whose $L_2$ norm is clipped to a bound $\varepsilon$, producing the corrected action $\mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}(\boldsymbol{\delta})$.
24	The critical design insight is that correction operates on a high-quality starting point---the conformal-selected action---and that bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.
25	The base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.
26	
27	% --- Para 4: Key findings (with exp_id references) ---
28	We evaluate ACR-VLA on LIBERO-Object (10 tasks, 100 trials per method) and LIBERO-Spatial (10 tasks, 100 trials) using SmolVLA~\cite{shukor2025smolvla} as the frozen backbone. Three findings emerge:
29	
30	\textbf{(1)~Sample-then-correct outperforms sample-then-select.}
31	On LIBERO-Object, observation-conditioned CRM achieves 19.0\% success versus 12.0\% for conformal selection alone---a +7.0 percentage point improvement representing a 58\% relative gain.
32	% exp_id: eval-acr-object-v4-obs-only (19.0%), eval-argmin-only-object (12.0%)
33	% TODO: update with pooled seed=42+43 results and Fisher exact p-value
34	Averaging all $K$ samples (VLA-mean) or using a single sample (VLA-only) both yield 12.0\%, confirming that the gain comes from learned correction, not from increased sampling alone.
35	% exp_id: eval-vla-only-object-k1 (12.0%), eval-vla-mean-object (12.0%)
36	
37	\textbf{(2)~Observation features suffice for correction; conformal features do not help.}
38	Counter to intuition from synthetic experiments, conditioning CRM on per-DOF conformal statistics (perdof: 11.0\%) performs no better than selection alone (12.0\%), while scalar conformal conditioning (9.0\%) is actively harmful.
39	% exp_id: eval-acr-object-v4-small (perdof 11.0%), eval-acr-object-v4-scalar (9.0%)
40	Only observation-conditioned CRM (19.0\%) produces meaningful improvement.
41	This honest negative result highlights a gap between per-step prediction accuracy---where richer features help in offline evaluation---and closed-loop task success, where covariance estimation noise from $K{=}10$ samples undermines per-DOF conditioning.
42	
43	\textbf{(3)~Correction magnitude control is critical and previously unrecognized.}
44	Without magnitude bounding, the per-DOF-conditioned CRM's natural output ($\|\boldsymbol{\delta}\|_2 \approx 1.42$) causes catastrophic failure: 0\% success on LIBERO-Spatial, as compounding correction errors rapidly drive the state distribution away from the CRM's training regime.
45	Constraining corrections to $\|\boldsymbol{\delta}\|_2 \leq 0.1$ recovers the full +7.0\,pp gain.
46	% exp_id: eval-acr-spatial-v4-default-r3 (norm=1.42, 0%), eval-acr-object-v4-obs-only (norm=0.1, 19.0%)
47	Observation-conditioned CRM maintains stable 35--36\% success on LIBERO-Spatial across $\varepsilon \in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\% to 26\% over the same range---further evidence that observation features provide more robust conditioning for learned correction.
48	% exp_id: eval-mag-obsonly-norm005, eval-mag-obsonly-norm03, eval-mag-perdof-norm03
49	
50	We note that correction offers targeted improvements on object-centric manipulation rather than universal gains: on LIBERO-Spatial, all CRM variants perform within ${\pm}1$\,pp of selection alone, suggesting that the correction mechanism is most effective when distribution shift induces systematic action biases that a learned module can identify and compensate.
51	
52	% --- Para 5: Contributions ---
53	Our contributions are:
54	\begin{enumerate}[leftmargin=*,nosep]
55	  \item \textbf{A sample-then-correct pipeline for frozen VLAs.}
56	  We propose ACR-VLA, which combines conformal sample selection with learned residual correction for frozen flow-matching VLAs.
57	  On LIBERO-Object, this pipeline improves SmolVLA success by +7.0\,pp over selection alone.
58	  % TODO: update with pooled seed results and p-value: (p < 0.05 on combined 200 trials, Fisher exact test)
59	
60	  \item \textbf{Systematic conditioning comparison and honest negative result.}
61	  We compare three CRM conditioning variants---per-DOF conformal features, scalar uncertainty, and observation features---and find that only observation conditioning is effective.
62	  This challenges the intuition that richer uncertainty features should yield better corrections, and reveals that covariance estimation noise at $K{=}10$ undermines per-DOF conditioning in closed-loop settings.
63	
64	  \item \textbf{Systematic empirical study of correction magnitude sensitivity for VLA action refinement.}
65	  We show that unbounded correction causes catastrophic failure and that observation-conditioned CRM is uniquely robust across a $6{\times}$ range of magnitude bounds ($\varepsilon \in [0.05, 0.3]$), establishing magnitude control as a critical design axis for inference-time action correction.
66	\end{enumerate}
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "f4d846cb-b327-4bfc-b8e8-355e104066cc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% --- Para 1: VLAs are impressive but fragile under distribution shift ---\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached high success rates on in-distribution benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet this near-saturation masks a fragile reality: visual and physical perturbations routinely encountered in deployment---camera viewpoint shifts, object layout changes, robot initial state variation---can degrade success rates by over 65 percentage points---for example, $\\pi_0$ drops from 94.2\\% to 6.6\\% under robot initial-state perturbation, and UniVLA from 95.2\\% to 4.3\\% under camera viewpoint changes~\\cite{fei2025liberoplus}.\nClosing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled settings.\n\n% --- Para 2: Existing approaches and the gap ---\nTwo lines of work address VLA robustness.\n\\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\\cite{liu2026ttvla}.\nThese approaches are effective but require retraining or per-task RL, and their gains are bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen.\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution states, but operates as an uncertainty quantification framework rather than an action improvement method.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step---too slow for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.\nIn short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.\n\n% --- Para 3: Our approach — sample-then-correct ---\nWe introduce \\textbf{ACR-VLA} (\\textbf{A}daptive \\textbf{C}onformal \\textbf{R}efinement for VLA), an inference-time module that improves frozen VLA actions through a \\emph{sample-then-correct} pipeline.\nAt each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the most conforming candidate via Mahalanobis-based nonconformity scoring with shrinkage covariance estimation~\\cite{ledoit2004well,braun2025cgs}, and then applies a learned residual correction via a lightweight \\emph{Conformal Residual Module} (CRM).\nCRM is a 329K-parameter MLP conditioned on the VLA's frozen observation embedding.\nIt predicts a small residual $\\boldsymbol{\\delta}$ whose $L_2$ norm is clipped to a bound $\\varepsilon$, producing the corrected action $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\nThe critical design insight is that correction operates on a high-quality starting point---the conformal-selected action---and that bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.\nThe base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.\n\n% --- Para 4: Key findings (with exp_id references) ---\nWe evaluate ACR-VLA on LIBERO-Object (10 tasks, 100 trials per method) and LIBERO-Spatial (10 tasks, 100 trials) using SmolVLA~\\cite{shukor2025smolvla} as the frozen backbone. Three findings emerge:\n\n\\textbf{(1)~Sample-then-correct outperforms sample-then-select.}\nOn LIBERO-Object, observation-conditioned CRM achieves 19.0\\% success versus 12.0\\% for conformal selection alone---a +7.0 percentage point improvement representing a 58\\% relative gain.\n% exp_id: eval-acr-object-v4-obs-only (19.0%), eval-argmin-only-object (12.0%)\n% TODO: update with pooled seed=42+43 results and Fisher exact p-value\nAveraging all $K$ samples (VLA-mean) or using a single sample (VLA-only) both yield 12.0\\%, confirming that the gain comes from learned correction, not from increased sampling alone.\n% exp_id: eval-vla-only-object-k1 (12.0%), eval-vla-mean-object (12.0%)\n\n\\textbf{(2)~Observation features suffice for correction; conformal features do not help.}\nCounter to intuition from synthetic experiments, conditioning CRM on per-DOF conformal statistics (perdof: 11.0\\%) performs no better than selection alone (12.0\\%), while scalar conformal conditioning (9.0\\%) is actively harmful.\n% exp_id: eval-acr-object-v4-small (perdof 11.0%), eval-acr-object-v4-scalar (9.0%)\nOnly observation-conditioned CRM (19.0\\%) produces meaningful improvement.\nThis honest negative result highlights a gap between per-step prediction accuracy---where richer features help in offline evaluation---and closed-loop task success, where covariance estimation noise from $K{=}10$ samples undermines per-DOF conditioning.\n\n\\textbf{(3)~Correction magnitude control is critical and previously unrecognized.}\nWithout magnitude bounding, the per-DOF-conditioned CRM's natural output ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$) causes catastrophic failure: 0\\% success on LIBERO-Spatial, as compounding correction errors rapidly drive the state distribution away from the CRM's training regime.\nConstraining corrections to $\\|\\boldsymbol{\\delta}\\|_2 \\leq 0.1$ recovers the full +7.0\\,pp gain.\n% exp_id: eval-acr-spatial-v4-default-r3 (norm=1.42, 0%), eval-acr-object-v4-obs-only (norm=0.1, 19.0%)\nObservation-conditioned CRM maintains stable 35--36\\% success on LIBERO-Spatial across $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% to 26\\% over the same range---further evidence that observation features provide more robust conditioning for learned correction.\n% exp_id: eval-mag-obsonly-norm005, eval-mag-obsonly-norm03, eval-mag-perdof-norm03\n\nWe note that correction offers targeted improvements on object-centric manipulation rather than universal gains: on LIBERO-Spatial, all CRM variants perform within ${\\pm}1$\\,pp of selection alone, suggesting that the correction mechanism is most effective when distribution shift induces systematic action biases that a learned module can identify and compensate.\n\n% --- Para 5: Contributions ---\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{A sample-then-correct pipeline for frozen VLAs.}\n  We propose ACR-VLA, which combines conformal sample selection with learned residual correction for frozen flow-matching VLAs.\n  On LIBERO-Object, this pipeline improves SmolVLA success by +7.0\\,pp over selection alone.\n  % TODO: update with pooled seed results and p-value: (p < 0.05 on combined 200 trials, Fisher exact test)\n\n  \\item \\textbf{Systematic conditioning comparison and honest negative result.}\n  We compare three CRM conditioning variants---per-DOF conformal features, scalar uncertainty, and observation features---and find that only observation conditioning is effective.\n  This challenges the intuition that richer uncertainty features should yield better corrections, and reveals that covariance estimation noise at $K{=}10$ undermines per-DOF conditioning in closed-loop settings.\n\n  \\item \\textbf{Systematic empirical study of correction magnitude sensitivity for VLA action refinement.}\n  We show that unbounded correction causes catastrophic failure and that observation-conditioned CRM is uniquely robust across a $6{\\times}$ range of magnitude bounds ($\\varepsilon \\in [0.05, 0.3]$), establishing magnitude control as a critical design axis for inference-time action correction.\n\\end{enumerate}\n",
      "numLines": 67,
      "startLine": 1,
      "totalLines": 67
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01QRvcsXD4LS4o9frpinVm3j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "9105866f-ff15-4535-8d45-e92e06b69bfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUttNzwViG4VYXFksFY3Hr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 26858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2504
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

_source line 28 · 2026-05-15T20:46:13.394Z_

<details><summary>↩ Tool result · `toolu_01QRvcsXD4LS4o9frpinVm3j`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\subsection{VLA Robustness}
4	
5	Methods for improving VLA robustness divide into training-time and inference-time approaches.
6	
7	\paragraph{Training-time methods.}
8	RobustVLA~\cite{robustvla2025} combines RL post-training with Jacobian regularization and smoothness regularization to stabilize action predictions under observation noise and action perturbations.
9	SRPO~\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as references to shape rewards for failed trajectories via latent world model representations.
10	DiG-Flow~\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control, without modifying the flow-matching trajectory.
11	TT-VLA~\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.
12	A shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.
13	
14	\paragraph{Inference-time methods.}
15	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, providing a principled uncertainty quantification framework that operates without retraining but does not modify the VLA's actions.
16	SC-VLA~\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.
17	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\,s per control step---prohibitive for real-time manipulation.
18	A2C2~\cite{a2c2_2025} learns a lightweight correction head that runs at every control step to correct each action within a pre-generated chunk, restoring closed-loop responsiveness; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.
19	
20	A2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy.
21	The key architectural difference is that ACR-VLA operates as a two-stage pipeline---multi-sample conformal selection followed by bounded residual correction---whereas A2C2 applies per-step correction directly to the base policy's action chunks without a selection stage.
22	ACR-VLA additionally enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\ref{sec:magnitude_results}).
23	Selection alone is upper-bounded by sample quality---it cannot produce an action better than the best sample.
24	Correction alone lacks a mechanism to identify a good starting point.
25	ACR-VLA addresses both by selecting a low-nonconformity candidate via Mahalanobis scoring, then applying a bounded residual correction trained offline with supervised $L_2$ loss.
26	
27	\subsection{Conformal Prediction in Robotics}
28	
29	Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\cite{angelopoulos2023gentle}.
30	For multivariate outputs, Braun et al.~\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.
31	
32	In robotics, CP has been applied to several safety-critical settings.
33	Conformalized Teleoperation~\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.
34	CP-in-the-Loop~\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.
35	ACP+CBF~\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.
36	A common pattern across these methods is that CP serves as a \emph{binary decision mechanism}---accept or reject, safe or unsafe, execute or abstain.
37	
38	ACR-VLA uses Mahalanobis nonconformity scores derived from shrinkage covariance estimates in its selection stage, but does \emph{not} claim formal coverage guarantees for the corrected output.
39	CP serves here as a scoring mechanism: the Mahalanobis score ranks samples for selection, and the covariance structure is available as conditioning features for the correction module (though our ablations find that observation features alone suffice; Section~\ref{sec:ablation}).
40	The downstream correction module produces a refined action whose relationship to the original conformal region is no longer governed by coverage theory.
41	
42	\subsection{Residual Policy Learning}
43	
44	Residual policy learning augments a base controller with a learned additive correction.
45	Silver et al.~\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization to ensure the learned residual starts from the base policy's behavior and gradually improves upon it.
46	Subsequent work has focused on controlling residual magnitude---a central design concern, since unconstrained corrections lead to compounding error and policy collapse.
47	TRANSIC~\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to decide whether to apply a sim-to-real residual, demonstrating that ungated correction causes model collapse.
48	PLD~\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\xi, \xi]$) via off-policy RL, then distills improved trajectories back into the base model.
49	DRC~\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade after application.
50	
51	Magnitude control is the key connection to ACR-VLA: Silver et al.\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, DRC uses exponential decay after correction events.
52	ACR-VLA uses fixed $L_2$ norm clipping---the simplest possible scheme---yet our ablations show that the choice of clipping threshold $\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\ref{sec:experiments}).
53	We view this as evidence that magnitude control in VLA inference-time correction is an underexplored hyperparameter.
54	A second distinction separates ACR-VLA from the above methods: all four require RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, requiring neither reward design nor environment access during training.
55	
56	\subsection{Uncertainty Quantification for VLAs}
57	
58	Recent work has developed UQ methods tailored to VLA architectures.
59	DiU~\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.
60	SAFE~\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering intervention when anomalous states are detected.
61	Zollo and Zemel~\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.
62	
63	ACR-VLA takes a multi-sample approach to UQ ($K{=}10$ forward passes), in contrast to DiU's single-pass estimation.
64	The multi-sample strategy is more expensive but captures both epistemic and aleatoric uncertainty components---a property that matters under distribution shift, where epistemic uncertainty rises but single-pass aleatoric estimates may not.
65	Functionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\cite{zollo2025vla_calibration} targets confidence reliability.
66	Our ablations reveal a negative result connecting to this literature: per-DOF conformal features, despite their richer structure, do not improve correction performance when used as CRM input at the $K{=}10$ budget (Section~\ref{sec:ablation}), suggesting that translating fine-grained uncertainty estimates into actionable correction signals remains an open challenge.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "749197ab-f902-469f-a231-51b51991e4de",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization and smoothness regularization to stabilize action predictions under observation noise and action perturbations.\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as references to shape rewards for failed trajectories via latent world model representations.\nDiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control, without modifying the flow-matching trajectory.\nTT-VLA~\\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.\nA shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, providing a principled uncertainty quantification framework that operates without retraining but does not modify the VLA's actions.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\\,s per control step---prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a lightweight correction head that runs at every control step to correct each action within a pre-generated chunk, restoring closed-loop responsiveness; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.\n\nA2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy.\nThe key architectural difference is that ACR-VLA operates as a two-stage pipeline---multi-sample conformal selection followed by bounded residual correction---whereas A2C2 applies per-step correction directly to the base policy's action chunks without a selection stage.\nACR-VLA additionally enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).\nSelection alone is upper-bounded by sample quality---it cannot produce an action better than the best sample.\nCorrection alone lacks a mechanism to identify a good starting point.\nACR-VLA addresses both by selecting a low-nonconformity candidate via Mahalanobis scoring, then applying a bounded residual correction trained offline with supervised $L_2$ loss.\n\n\\subsection{Conformal Prediction in Robotics}\n\nConformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\\cite{angelopoulos2023gentle}.\nFor multivariate outputs, Braun et al.~\\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.\n\nIn robotics, CP has been applied to several safety-critical settings.\nConformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.\nCP-in-the-Loop~\\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.\nACP+CBF~\\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.\nA common pattern across these methods is that CP serves as a \\emph{binary decision mechanism}---accept or reject, safe or unsafe, execute or abstain.\n\nACR-VLA uses Mahalanobis nonconformity scores derived from shrinkage covariance estimates in its selection stage, but does \\emph{not} claim formal coverage guarantees for the corrected output.\nCP serves here as a scoring mechanism: the Mahalanobis score ranks samples for selection, and the covariance structure is available as conditioning features for the correction module (though our ablations find that observation features alone suffice; Section~\\ref{sec:ablation}).\nThe downstream correction module produces a refined action whose relationship to the original conformal region is no longer governed by coverage theory.\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization to ensure the learned residual starts from the base policy's behavior and gradually improves upon it.\nSubsequent work has focused on controlling residual magnitude---a central design concern, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to decide whether to apply a sim-to-real residual, demonstrating that ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.\nDRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade after application.\n\nMagnitude control is the key connection to ACR-VLA: Silver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, DRC uses exponential decay after correction events.\nACR-VLA uses fixed $L_2$ norm clipping---the simplest possible scheme---yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nWe view this as evidence that magnitude control in VLA inference-time correction is an underexplored hyperparameter.\nA second distinction separates ACR-VLA from the above methods: all four require RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, requiring neither reward design nor environment access during training.\n\n\\subsection{Uncertainty Quantification for VLAs}\n\nRecent work has developed UQ methods tailored to VLA architectures.\nDiU~\\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.\nSAFE~\\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering intervention when anomalous states are detected.\nZollo and Zemel~\\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.\n\nACR-VLA takes a multi-sample approach to UQ ($K{=}10$ forward passes), in contrast to DiU's single-pass estimation.\nThe multi-sample strategy is more expensive but captures both epistemic and aleatoric uncertainty components---a property that matters under distribution shift, where epistemic uncertainty rises but single-pass aleatoric estimates may not.\nFunctionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\\cite{zollo2025vla_calibration} targets confidence reliability.\nOur ablations reveal a negative result connecting to this literature: per-DOF conformal features, despite their richer structure, do not improve correction performance when used as CRM input at the $K{=}10$ budget (Section~\\ref{sec:ablation}), suggesting that translating fine-grained uncertainty estimates into actionable correction signals remains an open challenge.",
      "numLines": 66,
      "startLine": 1,
      "totalLines": 66
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_016syHh6cGmNsxTgwx3nqdng`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "2065a094-4048-4e4d-bda6-ec8f09a5507f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUttNzwViG4VYXFksFY3Hr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 26858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2504
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

_source line 30 · 2026-05-15T20:46:14.418Z_

<details><summary>↩ Tool result · `toolu_016syHh6cGmNsxTgwx3nqdng`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate ACR-VLA on two LIBERO task suites to answer three questions:
6	(i)~Does observation-conditioned residual correction improve over conformal selection alone?
7	(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?
8	(iii)~How sensitive is performance to the magnitude bound $\varepsilon$?
9	The answers are: yes (+7.0\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\_only is robust across a wide range.
10	
11	\subsection{Experimental Setup}
12	\label{sec:exp_setup}
13	
14	\paragraph{Benchmarks.}
15	We use two suites from the LIBERO benchmark~\cite{liu2023libero}:
16	\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).
17	Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.
18	
19	\paragraph{Base VLA.}
20	We build on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
21	We use the checkpoint \texttt{lerobot/smolvla\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\times}256$) and 8D proprioceptive state.
22	Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.
23	
24	\paragraph{Baselines.}
25	All methods use the same frozen SmolVLA checkpoint:
26	\begin{itemize}[nosep]
27	  \item \textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.
28	  \item \textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.
29	  \item \textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\ref{sec:selection}), no CRM correction.
30	\end{itemize}
31	
32	\paragraph{CRM variants.}
33	All CRM variants share the same 3-layer MLP architecture (input$\to$256$\to$256$\to$30) and differ only in their conditioning input:
34	\begin{itemize}[nosep]
35	  \item \textbf{obs\_only}: frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ (329K params). This is our primary method.
36	  \item \textbf{perdof}: $\mathbf{z}_{\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).
37	  \item \textbf{scalar}: $\mathbf{z}_{\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).
38	\end{itemize}
39	
40	\paragraph{Training.}
41	CRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.
42	For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\mathrm{base}}$.
43	Optimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.
44	Data augmentation includes additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and uncertainty features ($\sigma \approx 0.006$).
45	The default magnitude bound is $\varepsilon = 0.1$ for all CRM variants unless stated otherwise.
46	
47	\paragraph{Statistical protocol.}
48	We report success rates from seed 42 (10 rollouts $\times$ 10 tasks = 100 episodes per suite).
49	Fisher's exact test and bootstrap confidence intervals will be computed pending seed 43 replication [\textsc{pending}: seed43].
50	Until then, we report absolute differences descriptively without claiming statistical significance.
51	
52	
53	\subsection{Main Results}
54	\label{sec:main_results}
55	
56	Table~\ref{tab:main} compares all methods on both benchmarks.
57	
58	\begin{table}[t]
59	\centering
60	\caption{Task success rate (\%\,$\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\times$ 10 rollouts each, seed 42). $\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}
61	\label{tab:main}
62	\small
63	\begin{tabular}{lccc}
64	\toprule
65	Method & Object (\%) & Spatial (\%) & $\Delta$ Object \\
66	\midrule
67	VLA-only ($K{=}1$)    & 12.0 & 30.0 & $\phantom{+}0.0$ \\
68	VLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\phantom{+}0.0$ \\
69	Argmin ($K{=}10$)      & 12.0 & 34.0 & --- \\
70	\midrule
71	scalar ($\varepsilon{=}0.1$)  & \phantom{0}9.0 & 32.0 & $-3.0$ \\
72	perdof ($\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\
73	\textbf{obs\_only} ($\varepsilon{=}0.1$) & \textbf{19.0} & \textbf{35.0} & $\mathbf{+7.0}$ \\
74	\midrule
75	obs\_only ($\varepsilon{=}0.2$) & \textbf{22.0} & 35.0 & $+10.0$ \\
76	\bottomrule
77	\end{tabular}
78	\end{table}
79	
80	\paragraph{Object benchmark: correction helps.}
81	On LIBERO-Object, obs\_only at $\varepsilon{=}0.1$ achieves 19.0\%, a +7.0\,pp improvement over the Argmin baseline (12.0\%).
82	Increasing the magnitude bound to $\varepsilon{=}0.2$ yields 22.0\% (+10.0\,pp).
83	This is the core result: observation-conditioned residual correction recovers performance that conformal selection alone cannot.
84	
85	Three baselines---VLA-only, VLA-mean, and Argmin---all achieve 12.0\% on LIBERO-Object, indicating that neither multi-sample averaging nor Mahalanobis-based selection provides meaningful benefit on this benchmark.
86	On LIBERO-Spatial, by contrast, Argmin improves +4\,pp over VLA-only (34\% vs.\ 30\%), suggesting that object perturbations shift the action distribution more uniformly across samples, limiting the value of selection alone.
87	The obs\_only CRM breaks through this plateau by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.
88	
89	\paragraph{Spatial benchmark: correction does not help.}
90	On LIBERO-Spatial, all methods cluster within a 5\,pp band (30--35\%).
91	The best CRM variants (obs\_only, perdof) achieve 35\%, only 1\,pp above the Argmin baseline (34\%).
92	This is a null result that we report prominently.
93	
94	We interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.
95	The VLA's observation encoder cannot extract correctable error signals from spatial shifts---the problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.
96	Residual correction at the action level is the wrong granularity for this type of generalization.
97	
98	\paragraph{Key finding.}
99	Sample-then-correct outperforms sample-then-select for object manipulation, where the challenge is fine-grained motor control with novel objects.
100	For spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.
101	
102	
103	\subsection{CRM Conditioning Ablation}
104	\label{sec:ablation}
105	
106	We focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\ref{tab:main}).
107	
108	\paragraph{Ranking.}
109	obs\_only (19.0\%) $\gg$ Argmin (12.0\%) $\approx$ perdof (11.0\%) $>$ scalar (9.0\%).
110	
111	This ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \emph{hurt} rather than help.
112	Scalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\,pp below the Argmin baseline that uses no correction at all.
113	
114	\paragraph{Why does richer conditioning fail?}
115	We identify three factors:
116	
117	\emph{(1) Noisy covariance estimation.}
118	With $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.
119	While Ledoit--Wolf shrinkage~\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\ref{sec:selection}), the per-DOF features derived from this estimate---standard deviations, conformal radii---still carry substantial estimation noise.
120	Feeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).
121	
122	\emph{(2) Observation features are sufficient.}
123	The frozen VLA observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.
124	This information subsumes what the per-DOF conformal features attempt to capture---namely, which action dimensions are uncertain given the current scene.
125	The CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.
126	
127	\emph{(3) Per-step MSE $\neq$ episode success.}
128	All CRM variants achieve low per-step MSE on held-out demonstration data, yet offline prediction accuracy does not predict closed-loop task success.
129	In closed-loop evaluation, small per-step errors compound and the robot visits states far from the demonstration distribution~\cite{ross2011dagger}.
130	The noisy conformal features amplify this drift: occasional erroneous correction directions, even when small in magnitude, can trigger cascading failures in individual episodes.
131	
132	\paragraph{Connection to magnitude sensitivity.}
133	The obs\_only variant is also more robust across magnitude bounds $\varepsilon$ than perdof (Section~\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.
134	
135	
136	\subsection{Magnitude Sensitivity}
137	\label{sec:magnitude_results}
138	
139	The norm bound $\varepsilon$ determines how much CRM can deviate from the conformal-selected action.
140	Figure~\ref{fig:magnitude} shows performance on LIBERO-Spatial across $\varepsilon \in [0.05, 1.42]$.
141	
142	\begin{figure}[t]
143	\centering
144	% \includegraphics[width=\linewidth]{figures/magnitude_sweep.pdf}
145	\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}[Placeholder: Magnitude sweep --- obs\_only vs.\ perdof vs.\ Argmin reference]\vspace{2em}}}
146	\caption{Success rate (\%) on LIBERO-Spatial as a function of magnitude bound $\varepsilon$. obs\_only (solid blue) maintains 35--36\% across $\varepsilon \in [0.05, 0.3]$. perdof (dashed orange) collapses at larger $\varepsilon$. The Argmin baseline (dotted gray, 34\%) is independent of $\varepsilon$. Without magnitude control ($\varepsilon{\approx}1.42$), perdof achieves 0\% on spatial.}
147	\label{fig:magnitude}
148	\end{figure}
149	
150	\begin{table}[t]
151	\centering
152	\caption{Success rate (\%) on LIBERO-Spatial across magnitude bounds $\varepsilon$. The Argmin baseline (34\%, no correction) is independent of $\varepsilon$.}
153	\label{tab:magnitude}
154	\small
155	\begin{tabular}{lcccc}
156	\toprule
157	$\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\
158	\midrule
159	obs\_only & 35.0 & 35.0 & 36.0 & --- \\
160	perdof    & 31.0 & 35.0 & 26.0 & 0.0 \\
161	\midrule
162	Argmin (ref.) & \multicolumn{4}{c}{34.0 (flat, no correction)} \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\paragraph{obs\_only is robust.}
168	The obs\_only variant maintains 35--36\% across the full range $\varepsilon \in [0.05, 0.3]$---a remarkably flat profile.
169	This stability means the practitioner need not carefully tune $\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.
170	
171	\paragraph{perdof is fragile.}
172	In contrast, perdof peaks at 35\% when $\varepsilon{=}0.1$ but collapses to 26\% at $\varepsilon{=}0.3$---a 9\,pp drop.
173	This fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.
174	At $\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.
175	
176	\paragraph{Unbounded correction is catastrophic.}
177	Without magnitude control ($\varepsilon{\approx}1.42$, the natural CRM output norm), perdof achieves 0\% on LIBERO-Spatial---compounding error across the trajectory destroys performance entirely (Section~\ref{sec:magnitude}).
178	The Argmin baseline (34\%) outperforms all CRM variants at this setting, demonstrating that unbounded correction is harmful.
179	The obs\_only variant was not evaluated at $\varepsilon{=}1.42$ on spatial, though analogous catastrophic failure is expected given the magnitude of unconstrained corrections.
180	
181	\paragraph{Practical recommendation.}
182	The safe operating range is $\varepsilon \in [0.05, 0.2]$.
183	Within this range, obs\_only is the only variant that consistently matches or exceeds the Argmin baseline.
184	We use $\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.
185	
186	
187	\subsection{Per-Task Analysis}
188	\label{sec:per_task}
189	
190	Per-task success rate breakdowns will reveal which task categories benefit most from residual correction and where the method provides no improvement.
191	
192	[\textsc{pending}: seed43] --- A per-task heatmap comparing obs\_only, Argmin, and VLA-only across all 20 tasks (10 LIBERO-Spatial + 10 LIBERO-Object) will be included upon completion of the seed 43 replication.
193	We expect the analysis to show that obs\_only's gains on LIBERO-Object concentrate on tasks requiring precise object grasping under visual variation, while LIBERO-Spatial tasks remain uniformly unaffected by correction.
194	Task difficulty analysis (measured by VLA-only success rate) will additionally test whether CRM helps more on medium-difficulty tasks where the base policy partially succeeds, versus easy tasks (ceiling effect) or hard tasks (base policy too far from success for small corrections to recover).
195	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "3deb8648-1bde-4aaf-89c5-f1bbed915cda",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
      "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate ACR-VLA on two LIBERO task suites to answer three questions:\n(i)~Does observation-conditioned residual correction improve over conformal selection alone?\n(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?\n(iii)~How sensitive is performance to the magnitude bound $\\varepsilon$?\nThe answers are: yes (+7.0\\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\\_only is robust across a wide range.\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmarks.}\nWe use two suites from the LIBERO benchmark~\\cite{liu2023libero}:\n\\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \\textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).\nEach task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.\nWe use the checkpoint \\texttt{lerobot/smolvla\\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state.\nActions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.\n\n\\paragraph{Baselines.}\nAll methods use the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.\n  \\item \\textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\\ref{sec:selection}), no CRM correction.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nAll CRM variants share the same 3-layer MLP architecture (input$\\to$256$\\to$256$\\to$30) and differ only in their conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ (329K params). This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).\n\\end{itemize}\n\n\\paragraph{Training.}\nCRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.\nFor each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\\mathrm{base}}$.\nOptimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.\nData augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and uncertainty features ($\\sigma \\approx 0.006$).\nThe default magnitude bound is $\\varepsilon = 0.1$ for all CRM variants unless stated otherwise.\n\n\\paragraph{Statistical protocol.}\nWe report success rates from seed 42 (10 rollouts $\\times$ 10 tasks = 100 episodes per suite).\nFisher's exact test and bootstrap confidence intervals will be computed pending seed 43 replication [\\textsc{pending}: seed43].\nUntil then, we report absolute differences descriptively without claiming statistical significance.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} compares all methods on both benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Task success rate (\\%\\,$\\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\\times$ 10 rollouts each, seed 42). $\\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Object (\\%) & Spatial (\\%) & $\\Delta$ Object \\\\\n\\midrule\nVLA-only ($K{=}1$)    & 12.0 & 30.0 & $\\phantom{+}0.0$ \\\\\nVLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\\phantom{+}0.0$ \\\\\nArgmin ($K{=}10$)      & 12.0 & 34.0 & --- \\\\\n\\midrule\nscalar ($\\varepsilon{=}0.1$)  & \\phantom{0}9.0 & 32.0 & $-3.0$ \\\\\nperdof ($\\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\\\\n\\textbf{obs\\_only} ($\\varepsilon{=}0.1$) & \\textbf{19.0} & \\textbf{35.0} & $\\mathbf{+7.0}$ \\\\\n\\midrule\nobs\\_only ($\\varepsilon{=}0.2$) & \\textbf{22.0} & 35.0 & $+10.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Object benchmark: correction helps.}\nOn LIBERO-Object, obs\\_only at $\\varepsilon{=}0.1$ achieves 19.0\\%, a +7.0\\,pp improvement over the Argmin baseline (12.0\\%).\nIncreasing the magnitude bound to $\\varepsilon{=}0.2$ yields 22.0\\% (+10.0\\,pp).\nThis is the core result: observation-conditioned residual correction recovers performance that conformal selection alone cannot.\n\nThree baselines---VLA-only, VLA-mean, and Argmin---all achieve 12.0\\% on LIBERO-Object, indicating that neither multi-sample averaging nor Mahalanobis-based selection provides meaningful benefit on this benchmark.\nOn LIBERO-Spatial, by contrast, Argmin improves +4\\,pp over VLA-only (34\\% vs.\\ 30\\%), suggesting that object perturbations shift the action distribution more uniformly across samples, limiting the value of selection alone.\nThe obs\\_only CRM breaks through this plateau by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.\n\n\\paragraph{Spatial benchmark: correction does not help.}\nOn LIBERO-Spatial, all methods cluster within a 5\\,pp band (30--35\\%).\nThe best CRM variants (obs\\_only, perdof) achieve 35\\%, only 1\\,pp above the Argmin baseline (34\\%).\nThis is a null result that we report prominently.\n\nWe interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.\nThe VLA's observation encoder cannot extract correctable error signals from spatial shifts---the problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.\nResidual correction at the action level is the wrong granularity for this type of generalization.\n\n\\paragraph{Key finding.}\nSample-then-correct outperforms sample-then-select for object manipulation, where the challenge is fine-grained motor control with novel objects.\nFor spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.\n\n\n\\subsection{CRM Conditioning Ablation}\n\\label{sec:ablation}\n\nWe focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\\ref{tab:main}).\n\n\\paragraph{Ranking.}\nobs\\_only (19.0\\%) $\\gg$ Argmin (12.0\\%) $\\approx$ perdof (11.0\\%) $>$ scalar (9.0\\%).\n\nThis ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \\emph{hurt} rather than help.\nScalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\\,pp below the Argmin baseline that uses no correction at all.\n\n\\paragraph{Why does richer conditioning fail?}\nWe identify three factors:\n\n\\emph{(1) Noisy covariance estimation.}\nWith $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.\nWhile Ledoit--Wolf shrinkage~\\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\\ref{sec:selection}), the per-DOF features derived from this estimate---standard deviations, conformal radii---still carry substantial estimation noise.\nFeeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).\n\n\\emph{(2) Observation features are sufficient.}\nThe frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.\nThis information subsumes what the per-DOF conformal features attempt to capture---namely, which action dimensions are uncertain given the current scene.\nThe CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.\n\n\\emph{(3) Per-step MSE $\\neq$ episode success.}\nAll CRM variants achieve low per-step MSE on held-out demonstration data, yet offline prediction accuracy does not predict closed-loop task success.\nIn closed-loop evaluation, small per-step errors compound and the robot visits states far from the demonstration distribution~\\cite{ross2011dagger}.\nThe noisy conformal features amplify this drift: occasional erroneous correction directions, even when small in magnitude, can trigger cascading failures in individual episodes.\n\n\\paragraph{Connection to magnitude sensitivity.}\nThe obs\\_only variant is also more robust across magnitude bounds $\\varepsilon$ than perdof (Section~\\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.\n\n\n\\subsection{Magnitude Sensitivity}\n\\label{sec:magnitude_results}\n\nThe norm bound $\\varepsilon$ determines how much CRM can deviate from the conformal-selected action.\nFigure~\\ref{fig:magnitude} shows performance on LIBERO-Spatial across $\\varepsilon \\in [0.05, 1.42]$.\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\linewidth]{figures/magnitude_sweep.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: Magnitude sweep --- obs\\_only vs.\\ perdof vs.\\ Argmin reference]\\vspace{2em}}}\n\\caption{Success rate (\\%) on LIBERO-Spatial as a function of magnitude bound $\\varepsilon$. obs\\_only (solid blue) maintains 35--36\\% across $\\varepsilon \\in [0.05, 0.3]$. perdof (dashed orange) collapses at larger $\\varepsilon$. The Argmin baseline (dotted gray, 34\\%) is independent of $\\varepsilon$. Without magnitude control ($\\varepsilon{\\approx}1.42$), perdof achieves 0\\% on spatial.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Spatial across magnitude bounds $\\varepsilon$. The Argmin baseline (34\\%, no correction) is independent of $\\varepsilon$.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\\\\n\\midrule\nobs\\_only & 35.0 & 35.0 & 36.0 & --- \\\\\nperdof    & 31.0 & 35.0 & 26.0 & 0.0 \\\\\n\\midrule\nArgmin (ref.) & \\multicolumn{4}{c}{34.0 (flat, no correction)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{obs\\_only is robust.}\nThe obs\\_only variant maintains 35--36\\% across the full range $\\varepsilon \\in [0.05, 0.3]$---a remarkably flat profile.\nThis stability means the practitioner need not carefully tune $\\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.\n\n\\paragraph{perdof is fragile.}\nIn contrast, perdof peaks at 35\\% when $\\varepsilon{=}0.1$ but collapses to 26\\% at $\\varepsilon{=}0.3$---a 9\\,pp drop.\nThis fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.\nAt $\\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.\n\n\\paragraph{Unbounded correction is catastrophic.}\nWithout magnitude control ($\\varepsilon{\\approx}1.42$, the natural CRM output norm), perdof achieves 0\\% on LIBERO-Spatial---compounding error across the trajectory destroys performance entirely (Section~\\ref{sec:magnitude}).\nThe Argmin baseline (34\\%) outperforms all CRM variants at this setting, demonstrating that unbounded correction is harmful.\nThe obs\\_only variant was not evaluated at $\\varepsilon{=}1.42$ on spatial, though analogous catastrophic failure is expected given the magnitude of unconstrained corrections.\n\n\\paragraph{Practical recommendation.}\nThe safe operating range is $\\varepsilon \\in [0.05, 0.2]$.\nWithin this range, obs\\_only is the only variant that consistently matches or exceeds the Argmin baseline.\nWe use $\\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nPer-task success rate breakdowns will reveal which task categories benefit most from residual correction and where the method provides no improvement.\n\n[\\textsc{pending}: seed43] --- A per-task heatmap comparing obs\\_only, Argmin, and VLA-only across all 20 tasks (10 LIBERO-Spatial + 10 LIBERO-Object) will be included upon completion of the seed 43 replication.\nWe expect the analysis to show that obs\\_only's gains on LIBERO-Object concentrate on tasks requiring precise object grasping under visual variation, while LIBERO-Spatial tasks remain uniformly unaffected by correction.\nTask difficulty analysis (measured by VLA-only success rate) will additionally test whether CRM helps more on medium-difficulty tasks where the base policy partially succeeds, versus easy tasks (ceiling effect) or hard tasks (base policy too far from success for small corrections to recover).\n",
      "numLines": 195,
      "startLine": 1,
      "totalLines": 195
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01EFWvWYjN1ZTj6wTMGzhERk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "25bdcc1e-b8b0-499a-922b-b6d993538a5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUttNzwViG4VYXFksFY3Hr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 26858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2504
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

_source line 32 · 2026-05-15T20:46:14.897Z_

<details><summary>↩ Tool result · `toolu_01EFWvWYjN1ZTj6wTMGzhERk`</summary>

```text
1	Flow-matching vision-language-action models (VLAs) achieve high success rates on standard manipulation benchmarks but degrade sharply under distribution shift---dropping over 65 percentage points on LIBERO-Plus perturbations.
2	Existing inference-time remedies either select among multiple action samples, which cannot exceed the quality of the best candidate, or learn corrections through reinforcement learning or slow optimization loops.
3	%
4	We propose ACR-VLA, an inference-time two-stage pipeline that wraps a frozen flow-matching VLA without retraining.
5	At each control step, ACR-VLA draws $K{=}10$ action samples, selects one via Mahalanobis-based conformal scoring, and applies a bounded residual correction through a lightweight Conformal Residual Module (CRM, ${\sim}$329K parameters, ${\sim}$3\,ms overhead).
6	%
7	On LIBERO-Object, observation-conditioned CRM achieves 19.0\% success versus 12.0\% for selection alone (+7.0\,pp, 58\% relative gain).
8	Conditioning CRM on per-DOF conformal features (11.0\%) or scalar uncertainty (9.0\%) fails to improve over selection alone (12.0\%)---only observation features reach 19.0\%---an honest negative result we attribute to noisy covariance estimation at the $K{=}10$ sample budget.
9	Magnitude control proves critical: unbounded correction leads to 0\% success.
10	On LIBERO-Spatial, correction and selection perform comparably (${\pm}$1\,pp), indicating the benefit is task-dependent.
11	%
12	Sample-then-correct outperforms sample-then-select for object manipulation, but whether correction helps depends on the structure of the distribution shift.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "05dc9bde-8daa-4719-8777-bac9ba432bca",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex",
      "content": "Flow-matching vision-language-action models (VLAs) achieve high success rates on standard manipulation benchmarks but degrade sharply under distribution shift---dropping over 65 percentage points on LIBERO-Plus perturbations.\nExisting inference-time remedies either select among multiple action samples, which cannot exceed the quality of the best candidate, or learn corrections through reinforcement learning or slow optimization loops.\n%\nWe propose ACR-VLA, an inference-time two-stage pipeline that wraps a frozen flow-matching VLA without retraining.\nAt each control step, ACR-VLA draws $K{=}10$ action samples, selects one via Mahalanobis-based conformal scoring, and applies a bounded residual correction through a lightweight Conformal Residual Module (CRM, ${\\sim}$329K parameters, ${\\sim}$3\\,ms overhead).\n%\nOn LIBERO-Object, observation-conditioned CRM achieves 19.0\\% success versus 12.0\\% for selection alone (+7.0\\,pp, 58\\% relative gain).\nConditioning CRM on per-DOF conformal features (11.0\\%) or scalar uncertainty (9.0\\%) fails to improve over selection alone (12.0\\%)---only observation features reach 19.0\\%---an honest negative result we attribute to noisy covariance estimation at the $K{=}10$ sample budget.\nMagnitude control proves critical: unbounded correction leads to 0\\% success.\nOn LIBERO-Spatial, correction and selection perform comparably (${\\pm}$1\\,pp), indicating the benefit is task-dependent.\n%\nSample-then-correct outperforms sample-then-select for object manipulation, but whether correction helps depends on the structure of the distribution shift.",
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

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01RPEJ6MBk2TzheVVtjBMbrL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "5710166c-a804-4327-b30c-c25bef606ae0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUttNzwViG4VYXFksFY3Hr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 26858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2504
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

_source line 34 · 2026-05-15T20:46:15.301Z_

<details><summary>↩ Tool result · `toolu_01RPEJ6MBk2TzheVVtjBMbrL`</summary>

```text
1	@misc{a2c2_2025,
2	    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},
3	    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},
4	    year={2025},
5	    eprint={2509.23224},
6	    archivePrefix={arXiv},
7	    primaryClass={cs.RO}
8	}
9	
10	@article{angelopoulos2023gentle,
11	    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
12	    author={Anastasios N. Angelopoulos and Stephen Bates},
13	    journal={Foundations and Trends in Machine Learning},
14	    year={2023},
15	    eprint={2107.07511},
16	    archivePrefix={arXiv},
17	    primaryClass={cs.LG}
18	}
19	
20	@article{barber2023conformal,
21	    title={Conformal Prediction Beyond Exchangeability},
22	    author={Rina Foygel Barber and Emmanuel J. Cand{\`e}s and Aaditya Ramdas and Ryan J. Tibshirani},
23	    journal={Annals of Statistics},
24	    volume={51},
25	    number={2},
26	    pages={816--845},
27	    year={2023}
28	}
29	
30	@misc{black2024pi0,
31	    title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
32	    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},
33	    year={2024},
34	    eprint={2410.24164},
35	    archivePrefix={arXiv},
36	    primaryClass={cs.RO}
37	}
38	
39	@misc{braun2025cgs,
40	    title={Multivariate Standardized Residuals for Conformal Prediction},
41	    author={Sacha Braun and Eug{\`e}ne Berta and Michael I. Jordan and Francis Bach},
42	    year={2025},
43	    eprint={2507.20941},
44	    archivePrefix={arXiv},
45	    primaryClass={stat.ML}
46	}
47	
48	@misc{brohan2023rt2,
49	    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
50	    author={Anthony Brohan and Noah Brown and Justice Carbajal and Yevgen Chebotar and Xi Chen and Krzysztof Choromanski and Tianli Ding and Danny Driess and Avinava Dubey and Chelsea Finn and Pete Florence and Chuyuan Fu and Montse Gonzalez Arenas and Keerthana Gopalakrishnan and Kehang Han and Karol Hausman and Alexander Herzog and Jasmine Hsu and Brian Ichter and Alex Irpan and Nikhil Joshi and Ryan Julian and Dmitry Kalashnikov and Yuheng Kuang and Isabel Leal and Lisa Lee and Tsang-Wei Edward Lee and Sergey Levine and Yao Lu and Henryk Michalewski and Igor Mordatch and Karl Pertsch and Kanishka Rao and Krista Reymann and Michael Ryoo and Grecia Salazar and Pannag Sanketi and Pierre Sermanet and Jaspiar Singh and Anikait Singh and Radu Soricut and Huong Tran and Vincent Vanhoucke and Quan Vuong and Ayzaan Wahid and Stefan Welker and Paul Wohlhart and Jialin Wu and Fei Xia and Ted Xiao and Peng Xu and Sichun Xu and Tianhe Yu and Brianna Zitkovich},
51	    year={2023},
52	    eprint={2307.15818},
53	    archivePrefix={arXiv},
54	    primaryClass={cs.RO}
55	}
56	
57	@misc{chen2026reconvla,
58	    title={ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control},
59	    author={Lingling Chen and Zongyao Lyu and William J. Beksi},
60	    year={2026},
61	    eprint={2604.16677},
62	    archivePrefix={arXiv},
63	    primaryClass={cs.RO}
64	}
65	
66	@misc{cosmos_policy_2026,
67	    title={Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning},
68	    author={Moo Jin Kim and Yihuai Gao and Tsung-Yi Lin and Yen-Chen Lin and Yunhao Ge and Grace Lam and Percy Liang and Shuran Song and Ming-Yu Liu and Chelsea Finn and Jinwei Gu},
69	    year={2026},
70	    eprint={2601.16163},
71	    archivePrefix={arXiv},
72	    primaryClass={cs.AI}
73	}
74	
75	@misc{digflow2025,
76	    title={DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models},
77	    author={Wanpeng Zhang and Ye Wang and Hao Luo and Haoqi Yuan and Yicheng Feng and Sipeng Zheng and Qin Jin and Zongqing Lu},
78	    year={2025},
79	    eprint={2512.01715},
80	    archivePrefix={arXiv},
81	    primaryClass={cs.RO}
82	}
83	
84	@misc{fei2025liberoplus,
85	    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},
86	    author={Senyu Fei and Siyin Wang and Junhao Shi and Zihao Dai and Jikun Cai and Pengfang Qian and Li Ji and Xinzhe He and Shiduo Zhang and Zhaoye Fei and Jinlan Fu and Jingjing Gong and Xipeng Qiu},
87	    year={2025},
88	    eprint={2510.13626},
89	    archivePrefix={arXiv},
90	    primaryClass={cs.RO}
91	}
92	
93	@inproceedings{gal2016dropout,
94	    title={Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},
95	    author={Yarin Gal and Zoubin Ghahramani},
96	    booktitle={International Conference on Machine Learning (ICML)},
97	    year={2016}
98	}
99	
100	@misc{ghosh2024octo,
101	    title={Octo: An Open-Source Generalist Robot Policy},
102	    author={Dibya Ghosh and Homer Walke and Karl Pertsch and Kevin Black and Oier Mees and Sudeep Dasari and Joey Hejna and Tobias Kreiman and Charles Xu and Jianlan Luo and You Liang Tan and Lawrence Yunliang Chen and Pannag Sanketi and Quan Vuong and Ted Xiao and Dorsa Sadigh and Chelsea Finn and Sergey Levine},
103	    year={2024},
104	    eprint={2405.12213},
105	    archivePrefix={arXiv},
106	    primaryClass={cs.RO}
107	}
108	
109	@inproceedings{gibbs2021aci,
110	    title={Adaptive Conformal Inference Under Distribution Shift},
111	    author={Isaac Gibbs and Emmanuel Cand{\`e}s},
112	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
113	    year={2021}
114	}
115	
116	@inproceedings{gu2025safe,
117	    title={SAFE: Multitask Failure Detection for Vision-Language-Action Models},
118	    author={Qiao Gu and Yuanliang Ju and Shengxiang Sun and Igor Gilitschenski and Haruki Nishimura and Masha Itkina and Florian Shkurti},
119	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
120	    year={2025}
121	}
122	
123	@misc{kim2024openvla,
124	    title={OpenVLA: An Open-Source Vision-Language-Action Model},
125	    author={Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},
126	    year={2024},
127	    eprint={2406.09246},
128	    archivePrefix={arXiv},
129	    primaryClass={cs.RO}
130	}
131	
132	@inproceedings{lakshminarayanan2017ensembles,
133	    title={Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},
134	    author={Balaji Lakshminarayanan and Alexander Pritzel and Charles Blundell},
135	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
136	    year={2017}
137	}
138	
139	@article{ledoit2004well,
140	    title={A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices},
141	    author={Olivier Ledoit and Michael Wolf},
142	    journal={Journal of Multivariate Analysis},
143	    volume={88},
144	    number={2},
145	    pages={365--411},
146	    year={2004}
147	}
148	
149	@inproceedings{lipman2023flow,
150	    title={Flow Matching for Generative Modeling},
151	    author={Yaron Lipman and Ricky T. Q. Chen and Heli Ben-Hamu and Maximilian Nickel and Matt Le},
152	    booktitle={International Conference on Learning Representations (ICLR)},
153	    year={2023}
154	}
155	
156	@inproceedings{liu2023libero,
157	    title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
158	    author={Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},
159	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
160	    year={2023}
161	}
162	
163	@misc{liu2026ttvla,
164	    title={On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning},
165	    author={Changyu Liu and Yiyang Liu and Taowen Wang and Qiao Zhuang and James Chenhao Liang and Wenhao Yang and Renjing Xu and Qifan Wang and Dongfang Liu and Cheng Han},
166	    year={2026},
167	    eprint={2601.06748},
168	    archivePrefix={arXiv},
169	    primaryClass={cs.RO}
170	}
171	
172	@misc{luan2026snapflow,
173	    title={SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation},
174	    author={Wuyang Luan and Junhui Li and Weiguang Zhao and Wenjian Zhang and Tieru Wu and Rui Ma},
175	    year={2026},
176	    eprint={2604.05656},
177	    archivePrefix={arXiv},
178	    primaryClass={cs.RO}
179	}
180	
181	@misc{robustvla2025,
182	    title={RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models},
183	    author={Hongyin Zhang and Shuo Zhang and Junxi Jin and Qixin Zeng and Runze Li and Donglin Wang},
184	    year={2025},
185	    eprint={2511.01331},
186	    archivePrefix={arXiv},
187	    primaryClass={cs.RO}
188	}
189	
190	@inproceedings{romano2019cqr,
191	    title={Conformalized Quantile Regression},
192	    author={Yaniv Romano and Evan Patterson and Emmanuel J. Cand{\`e}s},
193	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
194	    year={2019}
195	}
196	
197	@article{shafer2008tutorial,
198	    title={A Tutorial on Conformal Prediction},
199	    author={Glenn Shafer and Vladimir Vovk},
200	    journal={Journal of Machine Learning Research},
201	    volume={9},
202	    pages={371--421},
203	    year={2008}
204	}
205	
206	@misc{shukor2025smolvla,
207	    title={SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics},
208	    author={Mustafa Shukor and Dana Aubakirova and Francesco Capuano and Pepijn Kooijmans and Steven Palma and Adil Zouitine and Michel Aractingi and Caroline Pascal and Martino Russi and Andres Marafioti and Simon Alibert and Matthieu Cord and Thomas Wolf and Remi Cadene},
209	    year={2025},
210	    eprint={2506.01844},
211	    archivePrefix={arXiv},
212	    primaryClass={cs.RO}
213	}
214	
215	@misc{srpo2025,
216	    title={SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models},
217	    author={Senyu Fei and Siyin Wang and Li Ji and Ao Li and Shiduo Zhang and Liming Liu and Jinlong Hou and Jingjing Gong and Xianzhong Zhao and Xipeng Qiu},
218	    year={2025},
219	    eprint={2511.15605},
220	    archivePrefix={arXiv},
221	    primaryClass={cs.RO}
222	}
223	
224	@misc{vla_gse_2026,
225	    title={VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts},
226	    author={Yuhua Jiang and Junjie Lu and Xinyao Qin and Xiaoyu Chen and Kaixin Wang and Feifei Gao and Li Zhao},
227	    year={2026},
228	    eprint={2605.06175},
229	    archivePrefix={arXiv},
230	    primaryClass={cs.RO}
231	}
232	
233	@misc{wang2025cploop,
234	    title={Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization},
235	    author={Han Wang and Chao Ning},
236	    year={2025},
237	    eprint={2510.16376},
238	    archivePrefix={arXiv},
239	    primaryClass={cs.RO}
240	}
241	
242	@misc{xing2026diu,
243	    title={Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching},
244	    author={Jiarui Xing and Song Wang and Jian Wang},
245	    year={2026},
246	    eprint={2605.00941},
247	    archivePrefix={arXiv},
248	    primaryClass={cs.LG}
249	}
250	
251	@misc{yuan2026ups,
252	    title={When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering},
253	    author={Jessie Yuan and Yilin Wu and Andrea Bajcsy},
254	    year={2026},
255	    eprint={2602.22474},
256	    archivePrefix={arXiv},
257	    primaryClass={cs.RO}
258	}
259	
260	@inproceedings{chi2023diffusion_policy,
261	    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
262	    author={Cheng Chi and Zhenjia Xu and Siyuan Feng and Eric Cousineau and Benjamin Burchfiel and Shuran Song},
263	    booktitle={Robotics: Science and Systems (RSS)},
264	    year={2023},
265	    note={Also published in IJRR 2024. arXiv:2303.04137}
266	}
267	
268	@inproceedings{zhao2024conformalized,
269	    title={Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions},
270	    author={Michelle Zhao and Reid Simmons and Henny Admoni and Andrea Bajcsy},
271	    booktitle={Robotics: Science and Systems (RSS)},
272	    year={2024}
273	}
274	
275	@inproceedings{silver2018residual,
276	    title={Residual Policy Learning},
277	    author={Tom Silver and Kelsey Allen and Josh Tenenbaum and Leslie Kaelbling},
278	    booktitle={Robotics: Science and Systems (RSS)},
279	    year={2018},
280	    note={arXiv:1812.06298}
281	}
282	
283	@inproceedings{jiang2024transic,
284	    title={TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction},
285	    author={Yunfan Jiang and Chen Wang and Ruohan Zhang and Jiajun Wu and Li Fei-Fei},
286	    booktitle={Conference on Robot Learning (CoRL)},
287	    year={2024},
288	    note={arXiv:2405.10315}
289	}
290	
291	@inproceedings{xiao2026pld,
292	    title={Self-Improving Vision-Language-Action Models with Data Generation via Residual RL},
293	    author={Wenli Xiao and others},
294	    booktitle={International Conference on Learning Representations (ICLR)},
295	    year={2026},
296	    note={arXiv:2511.00091}
297	}
298	
299	@misc{pan2025drc,
300	    title={DRC: Decaying Relative Correction for Policy Refinement},
301	    author={Xinjie Pan and Ruizhe Shi and Dongjie Yu and Zhiyuan Nan and Xiaowei Hu and Muxin Wei and Pengfei Li and Xin Li and Zhixiang Wang and Liang Gao and Xue Liu},
302	    year={2025},
303	    eprint={2503.15368},
304	    archivePrefix={arXiv},
305	    primaryClass={cs.RO}
306	}
307	
308	@inproceedings{zhou2025acp_cbf,
309	    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},
310	    author={Hao Zhou and Yanze Zhang and Wenhao Luo},
311	    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
312	    year={2025},
313	    note={arXiv:2503.17678}
314	}
315	
316	@misc{zollo2025vla_calibration,
317	    title={Confidence Calibration in Vision-Language-Action Models},
318	    author={Thomas Zollo and Richard Zemel},
319	    year={2025},
320	    eprint={2507.17383},
321	    archivePrefix={arXiv},
322	    primaryClass={cs.RO}
323	}
324	
325	@inproceedings{ross2011dagger,
326	    title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},
327	    author={St{\'e}phane Ross and Geoffrey J. Gordon and J. Andrew Bagnell},
328	    booktitle={International Conference on Artificial Intelligence and Statistics (AISTATS)},
329	    year={2011}
330	}
331	
332	@misc{tang2026shifting,
333	    title={Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model},
334	    author={Yanchuan Tang and Taowen Wang and Yuefei Chen and Boxuan Zhang and Qiang Guan and Ruixiang Tang},
335	    year={2026},
336	    eprint={2603.18342},
337	    archivePrefix={arXiv},
338	    primaryClass={cs.RO}
339	}
340	
341	@misc{liu2026scvla,
342	    title={Self-Correcting VLA: Online Action Refinement via Sparse World Imagination},
343	    author={Chenyv Liu and Wentao Tan and Lei Zhu and Fengling Li and Jingjing Li and Guoli Yang and Heng Tao Shen},
344	    year={2026},
345	    eprint={2602.21633},
346	    archivePrefix={arXiv},
347	    primaryClass={cs.RO}
348	}
349	
350	@misc{li2025vlapilot,
351	    title={Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion},
352	    author={Zhuo Li and Junjia Liu and Zhipeng Dong and Tao Teng and Quentin Rouxel and Darwin Caldwell and Fei Chen},
353	    year={2025},
354	    eprint={2511.14178},
355	    archivePrefix={arXiv},
356	    primaryClass={cs.RO}
357	}
358	
359	@inproceedings{zhong2026acotvla,
360	    title={ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models},
361	    author={Linqing Zhong and Yi Liu and Yifei Wei and Ziyu Xiong and Maoqing Yao and Si Liu and Guanghui Ren},
362	    year={2026},
363	    eprint={2601.11404},
364	    archivePrefix={arXiv},
365	    primaryClass={cs.RO},
366	    booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}
367	}
368	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "e65d5566-702e-4616-b4d9-57f4be4dde74",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
      "content": "@misc{a2c2_2025,\n    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},\n    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},\n    year={2025},\n    eprint={2509.23224},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@article{angelopoulos2023gentle,\n    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},\n    author={Anastasios N. Angelopoulos and Stephen Bates},\n    journal={Foundations and Trends in Machine Learning},\n    year={2023},\n    eprint={2107.07511},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG}\n}\n\n@article{barber2023conformal,\n    title={Conformal Prediction Beyond Exchangeability},\n    author={Rina Foygel Barber and Emmanuel J. Cand{\\`e}s and Aaditya Ramdas and Ryan J. Tibshirani},\n    journal={Annals of Statistics},\n    volume={51},\n    number={2},\n    pages={816--845},\n    year={2023}\n}\n\n@misc{black2024pi0,\n    title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},\n    year={2024},\n    eprint={2410.24164},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{braun2025cgs,\n    title={Multivariate Standardized Residuals for Conformal Prediction},\n    author={Sacha Braun and Eug{\\`e}ne Berta and Michael I. Jordan and Francis Bach},\n    year={2025},\n    eprint={2507.20941},\n    archivePrefix={arXiv},\n    primaryClass={stat.ML}\n}\n\n@misc{brohan2023rt2,\n    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n    author={Anthony Brohan and Noah Brown and Justice Carbajal and Yevgen Chebotar and Xi Chen and Krzysztof Choromanski and Tianli Ding and Danny Driess and Avinava Dubey and Chelsea Finn and Pete Florence and Chuyuan Fu and Montse Gonzalez Arenas and Keerthana Gopalakrishnan and Kehang Han and Karol Hausman and Alexander Herzog and Jasmine Hsu and Brian Ichter and Alex Irpan and Nikhil Joshi and Ryan Julian and Dmitry Kalashnikov and Yuheng Kuang and Isabel Leal and Lisa Lee and Tsang-Wei Edward Lee and Sergey Levine and Yao Lu and Henryk Michalewski and Igor Mordatch and Karl Pertsch and Kanishka Rao and Krista Reymann and Michael Ryoo and Grecia Salazar and Pannag Sanketi and Pierre Sermanet and Jaspiar Singh and Anikait Singh and Radu Soricut and Huong Tran and Vincent Vanhoucke and Quan Vuong and Ayzaan Wahid and Stefan Welker and Paul Wohlhart and Jialin Wu and Fei Xia and Ted Xiao and Peng Xu and Sichun Xu and Tianhe Yu and Brianna Zitkovich},\n    year={2023},\n    eprint={2307.15818},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{chen2026reconvla,\n    title={ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control},\n    author={Lingling Chen and Zongyao Lyu and William J. Beksi},\n    year={2026},\n    eprint={2604.16677},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{cosmos_policy_2026,\n    title={Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning},\n    author={Moo Jin Kim and Yihuai Gao and Tsung-Yi Lin and Yen-Chen Lin and Yunhao Ge and Grace Lam and Percy Liang and Shuran Song and Ming-Yu Liu and Chelsea Finn and Jinwei Gu},\n    year={2026},\n    eprint={2601.16163},\n    archivePrefix={arXiv},\n    primaryClass={cs.AI}\n}\n\n@misc{digflow2025,\n    title={DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models},\n    author={Wanpeng Zhang and Ye Wang and Hao Luo and Haoqi Yuan and Yicheng Feng and Sipeng Zheng and Qin Jin and Zongqing Lu},\n    year={2025},\n    eprint={2512.01715},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{fei2025liberoplus,\n    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},\n    author={Senyu Fei and Siyin Wang and Junhao Shi and Zihao Dai and Jikun Cai and Pengfang Qian and Li Ji and Xinzhe He and Shiduo Zhang and Zhaoye Fei and Jinlan Fu and Jingjing Gong and Xipeng Qiu},\n    year={2025},\n    eprint={2510.13626},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{gal2016dropout,\n    title={Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n    author={Yarin Gal and Zoubin Ghahramani},\n    booktitle={International Conference on Machine Learning (ICML)},\n    year={2016}\n}\n\n@misc{ghosh2024octo,\n    title={Octo: An Open-Source Generalist Robot Policy},\n    author={Dibya Ghosh and Homer Walke and Karl Pertsch and Kevin Black and Oier Mees and Sudeep Dasari and Joey Hejna and Tobias Kreiman and Charles Xu and Jianlan Luo and You Liang Tan and Lawrence Yunliang Chen and Pannag Sanketi and Quan Vuong and Ted Xiao and Dorsa Sadigh and Chelsea Finn and Sergey Levine},\n    year={2024},\n    eprint={2405.12213},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{gibbs2021aci,\n    title={Adaptive Conformal Inference Under Distribution Shift},\n    author={Isaac Gibbs and Emmanuel Cand{\\`e}s},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2021}\n}\n\n@inproceedings{gu2025safe,\n    title={SAFE: Multitask Failure Detection for Vision-Language-Action Models},\n    author={Qiao Gu and Yuanliang Ju and Shengxiang Sun and Igor Gilitschenski and Haruki Nishimura and Masha Itkina and Florian Shkurti},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2025}\n}\n\n@misc{kim2024openvla,\n    title={OpenVLA: An Open-Source Vision-Language-Action Model},\n    author={Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},\n    year={2024},\n    eprint={2406.09246},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n    title={Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n    author={Balaji Lakshminarayanan and Alexander Pritzel and Charles Blundell},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2017}\n}\n\n@article{ledoit2004well,\n    title={A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices},\n    author={Olivier Ledoit and Michael Wolf},\n    journal={Journal of Multivariate Analysis},\n    volume={88},\n    number={2},\n    pages={365--411},\n    year={2004}\n}\n\n@inproceedings{lipman2023flow,\n    title={Flow Matching for Generative Modeling},\n    author={Yaron Lipman and Ricky T. Q. Chen and Heli Ben-Hamu and Maximilian Nickel and Matt Le},\n    booktitle={International Conference on Learning Representations (ICLR)},\n    year={2023}\n}\n\n@inproceedings{liu2023libero,\n    title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n    author={Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2023}\n}\n\n@misc{liu2026ttvla,\n    title={On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning},\n    author={Changyu Liu and Yiyang Liu and Taowen Wang and Qiao Zhuang and James Chenhao Liang and Wenhao Yang and Renjing Xu and Qifan Wang and Dongfang Liu and Cheng Han},\n    year={2026},\n    eprint={2601.06748},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{luan2026snapflow,\n    title={SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation},\n    author={Wuyang Luan and Junhui Li and Weiguang Zhao and Wenjian Zhang and Tieru Wu and Rui Ma},\n    year={2026},\n    eprint={2604.05656},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{robustvla2025,\n    title={RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models},\n    author={Hongyin Zhang and Shuo Zhang and Junxi Jin and Qixin Zeng and Runze Li and Donglin Wang},\n    year={2025},\n    eprint={2511.01331},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{romano2019cqr,\n    title={Conformalized Quantile Regression},\n    author={Yaniv Romano and Evan Patterson and Emmanuel J. Cand{\\`e}s},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2019}\n}\n\n@article{shafer2008tutorial,\n    title={A Tutorial on Conformal Prediction},\n    author={Glenn Shafer and Vladimir Vovk},\n    journal={Journal of Machine Learning Research},\n    volume={9},\n    pages={371--421},\n    year={2008}\n}\n\n@misc{shukor2025smolvla,\n    title={SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n    author={Mustafa Shukor and Dana Aubakirova and Francesco Capuano and Pepijn Kooijmans and Steven Palma and Adil Zouitine and Michel Aractingi and Caroline Pascal and Martino Russi and Andres Marafioti and Simon Alibert and Matthieu Cord and Thomas Wolf and Remi Cadene},\n    year={2025},\n    eprint={2506.01844},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{srpo2025,\n    title={SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models},\n    author={Senyu Fei and Siyin Wang and Li Ji and Ao Li and Shiduo Zhang and Liming Liu and Jinlong Hou and Jingjing Gong and Xianzhong Zhao and Xipeng Qiu},\n    year={2025},\n    eprint={2511.15605},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{vla_gse_2026,\n    title={VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts},\n    author={Yuhua Jiang and Junjie Lu and Xinyao Qin and Xiaoyu Chen and Kaixin Wang and Feifei Gao and Li Zhao},\n    year={2026},\n    eprint={2605.06175},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{wang2025cploop,\n    title={Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization},\n    author={Han Wang and Chao Ning},\n    year={2025},\n    eprint={2510.16376},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{xing2026diu,\n    title={Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching},\n    author={Jiarui Xing and Song Wang and Jian Wang},\n    year={2026},\n    eprint={2605.00941},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG}\n}\n\n@misc{yuan2026ups,\n    title={When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering},\n    author={Jessie Yuan and Yilin Wu and Andrea Bajcsy},\n    year={2026},\n    eprint={2602.22474},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{chi2023diffusion_policy,\n    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n    author={Cheng Chi and Zhenjia Xu and Siyuan Feng and Eric Cousineau and Benjamin Burchfiel and Shuran Song},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2023},\n    note={Also published in IJRR 2024. arXiv:2303.04137}\n}\n\n@inproceedings{zhao2024conformalized,\n    title={Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions},\n    author={Michelle Zhao and Reid Simmons and Henny Admoni and Andrea Bajcsy},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2024}\n}\n\n@inproceedings{silver2018residual,\n    title={Residual Policy Learning},\n    author={Tom Silver and Kelsey Allen and Josh Tenenbaum and Leslie Kaelbling},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2018},\n    note={arXiv:1812.06298}\n}\n\n@inproceedings{jiang2024transic,\n    title={TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction},\n    author={Yunfan Jiang and Chen Wang and Ruohan Zhang and Jiajun Wu and Li Fei-Fei},\n    booktitle={Conference on Robot Learning (CoRL)},\n    year={2024},\n    note={arXiv:2405.10315}\n}\n\n@inproceedings{xiao2026pld,\n    title={Self-Improving Vision-Language-Action Models with Data Generation via Residual RL},\n    author={Wenli Xiao and others},\n    booktitle={International Conference on Learning Representations (ICLR)},\n    year={2026},\n    note={arXiv:2511.00091}\n}\n\n@misc{pan2025drc,\n    title={DRC: Decaying Relative Correction for Policy Refinement},\n    author={Xinjie Pan and Ruizhe Shi and Dongjie Yu and Zhiyuan Nan and Xiaowei Hu and Muxin Wei and Pengfei Li and Xin Li and Zhixiang Wang and Liang Gao and Xue Liu},\n    year={2025},\n    eprint={2503.15368},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{zhou2025acp_cbf,\n    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},\n    author={Hao Zhou and Yanze Zhang and Wenhao Luo},\n    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n    year={2025},\n    note={arXiv:2503.17678}\n}\n\n@misc{zollo2025vla_calibration,\n    title={Confidence Calibration in Vision-Language-Action Models},\n    author={Thomas Zollo and Richard Zemel},\n    year={2025},\n    eprint={2507.17383},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{ross2011dagger,\n    title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},\n    author={St{\\'e}phane Ross and Geoffrey J. Gordon and J. Andrew Bagnell},\n    booktitle={International Conference on Artificial Intelligence and Statistics (AISTATS)},\n    year={2011}\n}\n\n@misc{tang2026shifting,\n    title={Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model},\n    author={Yanchuan Tang and Taowen Wang and Yuefei Chen and Boxuan Zhang and Qiang Guan and Ruixiang Tang},\n    year={2026},\n    eprint={2603.18342},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{liu2026scvla,\n    title={Self-Correcting VLA: Online Action Refinement via Sparse World Imagination},\n    author={Chenyv Liu and Wentao Tan and Lei Zhu and Fengling Li and Jingjing Li and Guoli Yang and Heng Tao Shen},\n    year={2026},\n    eprint={2602.21633},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{li2025vlapilot,\n    title={Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion},\n    author={Zhuo Li and Junjia Liu and Zhipeng Dong and Tao Teng and Quentin Rouxel and Darwin Caldwell and Fei Chen},\n    year={2025},\n    eprint={2511.14178},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{zhong2026acotvla,\n    title={ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models},\n    author={Linqing Zhong and Yi Liu and Yifei Wei and Ziyu Xiong and Maoqing Yao and Si Liu and Guanghui Ren},\n    year={2026},\n    eprint={2601.11404},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO},\n    booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}\n}\n",
      "numLines": 368,
      "startLine": 1,
      "totalLines": 368
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Now let me also read the method section and the discussion section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "0d911d6f-1bfc-40e5-ae63-b3ebeb11dd1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wsbvUdNzPhTiG88Q9mYNj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16402,
      "cache_read_input_tokens": 29362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16402
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

_source line 36_

Good, I have all sections. Let me also read the method.tex and discussion.tex, then check the paper/sections/related_work.md to see if there's a newer version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "b0858d0b-be81-467a-b1ad-628bbb11604a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wsbvUdNzPhTiG88Q9mYNj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16402,
      "cache_read_input_tokens": 29362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16402
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

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01ULPQoU7p86YTLqeszFXP9S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "d3d28f2d-9af8-4bb1-85bc-eed23df0cdaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wsbvUdNzPhTiG88Q9mYNj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16402,
      "cache_read_input_tokens": 29362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16402
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

_source line 38 · 2026-05-15T20:46:21.560Z_

<details><summary>↩ Tool result · `toolu_01ULPQoU7p86YTLqeszFXP9S`</summary>

```text
1	
2	\section{Method}
3	\label{sec:method}
4	
5	\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.
6	
7	\subsection{Problem Setup}
8	\label{sec:problem_setup}
9	
10	Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.
11	
12	At each control step, $\pi_\theta$ can be queried multiple times via independent flow-matching rollouts~\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\pi_\theta$.
13	
14	\subsection{Multi-Sample Generation and Conformal Selection}
15	\label{sec:selection}
16	
17	\paragraph{Sampling and truncation.}
18	We draw $K{=}10$ action chunks from $\pi_\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\{a_h^{(k)}\}_{k=1}^K$ with $a_h^{(k)} \in \mathbb{R}^d$ for each horizon step $h = 1, \dots, H$.
19	
20	\paragraph{Shrinkage covariance estimation.}
21	For each horizon step $h$, we compute the sample mean $\boldsymbol{\mu}_h = \frac{1}{K}\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\cite{ledoit2004well}:
22	\begin{equation}
23	  \boldsymbol{\Sigma}_h = (1 - \alpha_{\mathrm{LW}})\,\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}} + \alpha_{\mathrm{LW}}\,\frac{\mathrm{tr}(\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}})}{d}\,\mathbf{I},
24	  \label{eq:shrinkage}
25	\end{equation}
26	where $\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}}$ is the empirical covariance and $\alpha_{\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\% estimation error; shrinkage reduces this to below 5\%~\cite{ledoit2004well}.
27	
28	\paragraph{Mahalanobis nonconformity score.}
29	For each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:
30	\begin{equation}
31	  s_h(a) = (a - \boldsymbol{\mu}_h)^\top \boldsymbol{\Sigma}_h^{-1} (a - \boldsymbol{\mu}_h).
32	  \label{eq:mahal}
33	\end{equation}
34	This score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\cite{braun2025cgs}.
35	
36	\paragraph{Argmin selection.}
37	We select the sample with the lowest total nonconformity across all horizon steps:
38	\begin{equation}
39	  a_{\mathrm{base}} = \argmin_{k \in \{1,\dots,K\}} \sum_{h=1}^{H} s_h\bigl(a_h^{(k)}\bigr).
40	  \label{eq:argmin}
41	\end{equation}
42	This selection procedure uses Mahalanobis-based scoring~\cite{braun2025cgs} to identify the sample closest to the consensus of the action distribution, isolating the effect of the downstream correction module. The selected $a_{\mathrm{base}} \in \mathbb{R}^{d \times H}$ is the starting point for residual correction.
43	
44	\subsection{Conformal Residual Module}
45	\label{sec:crm}
46	
47	The Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.
48	
49	\paragraph{Architecture.}
50	CRM is a 3-layer MLP with input normalization (input$\to$256$\to$256$\to$30; 329K parameters for the primary obs\_only variant).
51	Its input is the frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\boldsymbol{\delta} \in \mathbb{R}^{d \times H} = \mathbb{R}^{30}$, and the corrected action is:
52	\begin{equation}
53	  \mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}\bigl(\boldsymbol{\delta},\; \|\boldsymbol{\delta}\|_2 \leq \varepsilon\bigr),
54	  \label{eq:crm}
55	\end{equation}
56	where $\varepsilon$ is a norm bound hyperparameter (Section~\ref{sec:magnitude}).
57	
58	\paragraph{Observation-only conditioning.}
59	CRM receives only the observation embedding $\mathbf{z}_{\mathrm{obs}}$ and does \emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.
60	
61	\paragraph{Training.}
62	CRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\cite{liu2023libero}:
63	\begin{equation}
64	  \mathcal{L} = \bigl\|\mathbf{a}^* - \mathbf{a}_{\mathrm{expert}}\bigr\|_2^2.
65	  \label{eq:loss}
66	\end{equation}
67	The training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\ref{eq:argmin}) to obtain $a_{\mathrm{base}}$. The expert action $\mathbf{a}_{\mathrm{expert}}$ is the corresponding demonstration action.
68	
69	We apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\sigma \approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\cite{ross2011dagger}.
70	
71	\paragraph{Base VLA.}
72	We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.
73	
74	\subsection{Magnitude Control}
75	\label{sec:magnitude}
76	
77	The norm bound $\varepsilon$ in~(\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.
78	
79	\paragraph{Unbounded correction fails catastrophically.}
80	Without clipping, the natural CRM output has $\|\boldsymbol{\delta}\|_2 \approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.
81	
82	\paragraph{Small corrections are effective.}
83	Constraining $\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.
84	
85	\paragraph{Connection to residual policy learning.}
86	The necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\cite{silver2018residual} introduced residual policy learning with zero-initialization for combining learned and classical controllers. TRANSIC~\cite{jiang2024transic} uses learned binary gating conditioned on the current state to selectively apply residual actions. PLD~\cite{xiao2026pld} bounds residual actor corrections within a fixed range during RL training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no multi-stage pipeline, just a hard constraint that prevents the correction from overwhelming the base policy.
87	
88	\paragraph{Differential sensitivity across CRM variants.}
89	Observation-conditioned CRM (obs\_only) maintains 35--36\% success on LIBERO-Spatial across the full range $\varepsilon \in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\% at $\varepsilon = 0.1$ to 26\% at $\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\ref{sec:ablation}).
90	
91	\subsection{Inference Protocol}
92	\label{sec:inference_protocol}
93	
94	Each control step proceeds as follows:
95	\begin{enumerate}[nosep]
96	  \item Draw $K{=}10$ action chunks from the frozen VLA $\pi_\theta$ and truncate to $H{=}5$ steps.
97	  \item Compute shrinkage covariance $\boldsymbol{\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.
98	  \item Select $a_{\mathrm{base}}$ via argmin over total nonconformity~(\ref{eq:argmin}).
99	  \item Compute residual $\boldsymbol{\delta} = \mathrm{CRM}(\mathbf{z}_{\mathrm{obs}})$ and clip to $\|\boldsymbol{\delta}\|_2 \leq \varepsilon$.
100	  \item Execute the first action of $\mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}(\boldsymbol{\delta})$.
101	  \item Observe new state and re-plan from step~1.
102	\end{enumerate}
103	The computational overhead consists of $K{=}10$ extra forward passes through the base VLA plus ${\sim}$3\,ms for CRM inference. The base VLA is never modified.
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "10c28643-c6e8-4d1d-b244-8a87cae62aa7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
      "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.\n\nAt each control step, $\\pi_\\theta$ can be queried multiple times via independent flow-matching rollouts~\\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\\pi_\\theta$.\n\n\\subsection{Multi-Sample Generation and Conformal Selection}\n\\label{sec:selection}\n\n\\paragraph{Sampling and truncation.}\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for each horizon step $h = 1, \\dots, H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each horizon step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1 - \\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nFor each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\\cite{braun2025cgs}.\n\n\\paragraph{Argmin selection.}\nWe select the sample with the lowest total nonconformity across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} s_h\\bigl(a_h^{(k)}\\bigr).\n  \\label{eq:argmin}\n\\end{equation}\nThis selection procedure uses Mahalanobis-based scoring~\\cite{braun2025cgs} to identify the sample closest to the consensus of the action distribution, isolating the effect of the downstream correction module. The selected $a_{\\mathrm{base}} \\in \\mathbb{R}^{d \\times H}$ is the starting point for residual correction.\n\n\\subsection{Conformal Residual Module}\n\\label{sec:crm}\n\nThe Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.\n\n\\paragraph{Architecture.}\nCRM is a 3-layer MLP with input normalization (input$\\to$256$\\to$256$\\to$30; 329K parameters for the primary obs\\_only variant).\nIts input is the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{d \\times H} = \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound hyperparameter (Section~\\ref{sec:magnitude}).\n\n\\paragraph{Observation-only conditioning.}\nCRM receives only the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ and does \\emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.\n\n\\paragraph{Training.}\nCRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\\cite{liu2023libero}:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2.\n  \\label{eq:loss}\n\\end{equation}\nThe training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$. The expert action $\\mathbf{a}_{\\mathrm{expert}}$ is the corresponding demonstration action.\n\nWe apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\\sigma \\approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\\cite{ross2011dagger}.\n\n\\paragraph{Base VLA.}\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.\n\n\\paragraph{Unbounded correction fails catastrophically.}\nWithout clipping, the natural CRM output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.\n\n\\paragraph{Small corrections are effective.}\nConstraining $\\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.\n\n\\paragraph{Connection to residual policy learning.}\nThe necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\\cite{silver2018residual} introduced residual policy learning with zero-initialization for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} uses learned binary gating conditioned on the current state to selectively apply residual actions. PLD~\\cite{xiao2026pld} bounds residual actor corrections within a fixed range during RL training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no multi-stage pipeline, just a hard constraint that prevents the correction from overwhelming the base policy.\n\n\\paragraph{Differential sensitivity across CRM variants.}\nObservation-conditioned CRM (obs\\_only) maintains 35--36\\% success on LIBERO-Spatial across the full range $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% at $\\varepsilon = 0.1$ to 26\\% at $\\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\\ref{sec:ablation}).\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute shrinkage covariance $\\boldsymbol{\\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.\n  \\item Select $a_{\\mathrm{base}}$ via argmin over total nonconformity~(\\ref{eq:argmin}).\n  \\item Compute residual $\\boldsymbol{\\delta} = \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}})$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead consists of $K{=}10$ extra forward passes through the base VLA plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01AMJZ9Vom3VuFHgh5Ezc87m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "6b93ae34-9e3e-4298-a528-bfa9e8aef53d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wsbvUdNzPhTiG88Q9mYNj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16402,
      "cache_read_input_tokens": 29362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16402
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

_source line 40 · 2026-05-15T20:46:21.728Z_

<details><summary>↩ Tool result · `toolu_01AMJZ9Vom3VuFHgh5Ezc87m`</summary>

```text
1	
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\paragraph{Why per-DOF conformal features fail.}
6	The negative result on conformal conditioning (Section~\ref{sec:ablation}) warrants explanation.
7	% exp_id: perdof_eps0.1_object → 11.0%, obs_only_eps0.1_object → 19.0%
8	At $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio $d/K = 0.6$ means that even with Ledoit--Wolf shrinkage~\cite{ledoit2004well}, per-DOF statistics---standard deviations, conformal radii---carry substantial estimation noise.
9	The frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ already encodes the geometric information these features attempt to capture: object identity, spatial layout, and gripper-object relationship.
10	Adding noisy low-dimensional statistics to a rich representation does not improve the CRM's predictions; it degrades them.
11	
12	A subtler issue is the gap between offline and closed-loop metrics.
13	All CRM variants achieve low per-step MSE on held-out demonstration data, yet offline prediction accuracy does not predict closed-loop success.
14	In closed-loop execution, compounding error~\cite{ross2011dagger} shifts the state distribution away from training data, and the noisy conformal features amplify this drift---occasional erroneous correction directions, even when small in magnitude, can trigger cascading failures in individual episodes.
15	This challenges the intuition from controlled synthetic settings that richer uncertainty features improve corrections, and raises an open question: would larger $K$ (e.g., $K{=}50$) yield reliable enough covariance estimates for per-DOF features to help?
16	We cannot test this due to the $K$-fold increase in VLA forward passes per control step.
17	
18	\paragraph{When does action-level correction help?}
19	% exp_id: obs_only_eps0.1_object → 19.0%, argmin_K10_object → 12.0%
20	% exp_id: obs_only_eps0.1_spatial → 35.0%, argmin_K10_spatial → 34.0%
21	The +7.0\,pp gain on LIBERO-Object versus the null result on LIBERO-Spatial (Table~\ref{tab:main}) reveals a structural distinction.
22	Object perturbations (novel object instances) create systematic action biases: the VLA produces actions with consistent directional errors that a learned module can identify and compensate from observation features alone.
23	Spatial perturbations (layout changes) require higher-level re-planning---the actions may be locally reasonable but directed at the wrong goal location.
24	Action-level residuals are effective for fine-grained motor adjustments, not for strategic re-planning.
25	This suggests that the benefit of post-hoc correction depends on whether the distribution shift manifests as correctable motor error or as a planning-level failure.
26	
27	\paragraph{Limitations.}
28	We identify seven limitations, each of which qualifies the scope of our findings:
29	\begin{enumerate}[nosep]
30	  \item \emph{Simulation only.} All experiments use LIBERO~\cite{liu2023libero}; real-robot transfer is untested.
31	  \item \emph{Single VLA backbone.} We evaluate only SmolVLA~\cite{shukor2025smolvla} (450M parameters). Whether ACR-VLA transfers to larger VLAs (e.g., $\pi_0$, OpenVLA) is unknown.
32	  \item \emph{Limited benchmarks.} Two LIBERO suites (20 tasks total); other manipulation benchmarks and perturbation types are not evaluated.
33	  % exp_id: obs_only per-task variance — some object tasks underperform argmin
34	  \item \emph{Per-task variance.} On individual LIBERO-Object tasks, obs\_only occasionally underperforms the Argmin baseline. The method does not universally help.
35	  \item \emph{Magnitude bound requires tuning.} We use $\varepsilon{=}0.1$ throughout, but the optimal $\varepsilon$ likely varies across VLA architectures and task domains.
36	  % exp_id: seed42 only; seed43 pending
37	  \item \emph{Single-seed results.} All primary results use seed 42. Seed 43 replication is pending; we make no statistical significance claims.
38	  % exp_id: obs_only_eps0.1_object → 19.0%
39	  \item \emph{Absolute performance.} 19.0\% success on LIBERO-Object is far from deployment-ready. ACR-VLA reduces the gap relative to selection-only but does not close it.
40	\end{enumerate}
41	
42	
43	\section{Conclusion}
44	\label{sec:conclusion}
45	
46	% exp_id: obs_only_eps0.1_object → 19.0%, argmin_K10_object → 12.0%
47	% exp_id: obs_only_eps0.1_spatial → 35.0%, argmin_K10_spatial → 34.0%
48	We presented ACR-VLA, a sample-then-correct pipeline that wraps a frozen flow-matching VLA with multi-sample conformal selection followed by a lightweight residual correction module (${\sim}$329K parameters, ${\sim}$3\,ms overhead).
49	On LIBERO-Object, observation-conditioned CRM achieves 19.0\% task success versus 12.0\% for selection alone (+7.0\,pp).
50	On LIBERO-Spatial, correction provides no measurable benefit over selection (best CRM within 1\,pp of the selection baseline), indicating the approach is effective for fine-grained motor correction under object-level distribution shift but not for spatial re-planning.
51	
52	% exp_id: perdof_eps0.1_object → 11.0%, obs_only_eps0.1_object → 19.0%
53	Our central negative result is that per-DOF conformal features do not improve correction over observation-only conditioning, despite providing intuitively richer uncertainty information.
54	At the $K{=}10$ sample budget, covariance estimation noise outweighs the information gain.
55	This is a cautionary finding for the broader agenda of uncertainty-conditioned action correction: the gap between offline prediction accuracy and closed-loop task success remains a fundamental challenge.
56	
57	Concrete next steps include: (i)~validation across multiple VLA backbones and scales, (ii)~real-robot transfer experiments, (iii)~adaptive magnitude scheduling (learned $\varepsilon$ conditioned on observation uncertainty), and (iv)~higher-$K$ sampling to revisit whether per-DOF conformal features become useful with better covariance estimates.
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "e8e637b9-61e5-40f7-ae7f-177be74a6d95",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex",
      "content": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why per-DOF conformal features fail.}\nThe negative result on conformal conditioning (Section~\\ref{sec:ablation}) warrants explanation.\n% exp_id: perdof_eps0.1_object → 11.0%, obs_only_eps0.1_object → 19.0%\nAt $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio $d/K = 0.6$ means that even with Ledoit--Wolf shrinkage~\\cite{ledoit2004well}, per-DOF statistics---standard deviations, conformal radii---carry substantial estimation noise.\nThe frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ already encodes the geometric information these features attempt to capture: object identity, spatial layout, and gripper-object relationship.\nAdding noisy low-dimensional statistics to a rich representation does not improve the CRM's predictions; it degrades them.\n\nA subtler issue is the gap between offline and closed-loop metrics.\nAll CRM variants achieve low per-step MSE on held-out demonstration data, yet offline prediction accuracy does not predict closed-loop success.\nIn closed-loop execution, compounding error~\\cite{ross2011dagger} shifts the state distribution away from training data, and the noisy conformal features amplify this drift---occasional erroneous correction directions, even when small in magnitude, can trigger cascading failures in individual episodes.\nThis challenges the intuition from controlled synthetic settings that richer uncertainty features improve corrections, and raises an open question: would larger $K$ (e.g., $K{=}50$) yield reliable enough covariance estimates for per-DOF features to help?\nWe cannot test this due to the $K$-fold increase in VLA forward passes per control step.\n\n\\paragraph{When does action-level correction help?}\n% exp_id: obs_only_eps0.1_object → 19.0%, argmin_K10_object → 12.0%\n% exp_id: obs_only_eps0.1_spatial → 35.0%, argmin_K10_spatial → 34.0%\nThe +7.0\\,pp gain on LIBERO-Object versus the null result on LIBERO-Spatial (Table~\\ref{tab:main}) reveals a structural distinction.\nObject perturbations (novel object instances) create systematic action biases: the VLA produces actions with consistent directional errors that a learned module can identify and compensate from observation features alone.\nSpatial perturbations (layout changes) require higher-level re-planning---the actions may be locally reasonable but directed at the wrong goal location.\nAction-level residuals are effective for fine-grained motor adjustments, not for strategic re-planning.\nThis suggests that the benefit of post-hoc correction depends on whether the distribution shift manifests as correctable motor error or as a planning-level failure.\n\n\\paragraph{Limitations.}\nWe identify seven limitations, each of which qualifies the scope of our findings:\n\\begin{enumerate}[nosep]\n  \\item \\emph{Simulation only.} All experiments use LIBERO~\\cite{liu2023libero}; real-robot transfer is untested.\n  \\item \\emph{Single VLA backbone.} We evaluate only SmolVLA~\\cite{shukor2025smolvla} (450M parameters). Whether ACR-VLA transfers to larger VLAs (e.g., $\\pi_0$, OpenVLA) is unknown.\n  \\item \\emph{Limited benchmarks.} Two LIBERO suites (20 tasks total); other manipulation benchmarks and perturbation types are not evaluated.\n  % exp_id: obs_only per-task variance — some object tasks underperform argmin\n  \\item \\emph{Per-task variance.} On individual LIBERO-Object tasks, obs\\_only occasionally underperforms the Argmin baseline. The method does not universally help.\n  \\item \\emph{Magnitude bound requires tuning.} We use $\\varepsilon{=}0.1$ throughout, but the optimal $\\varepsilon$ likely varies across VLA architectures and task domains.\n  % exp_id: seed42 only; seed43 pending\n  \\item \\emph{Single-seed results.} All primary results use seed 42. Seed 43 replication is pending; we make no statistical significance claims.\n  % exp_id: obs_only_eps0.1_object → 19.0%\n  \\item \\emph{Absolute performance.} 19.0\\% success on LIBERO-Object is far from deployment-ready. ACR-VLA reduces the gap relative to selection-only but does not close it.\n\\end{enumerate}\n\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\n% exp_id: obs_only_eps0.1_object → 19.0%, argmin_K10_object → 12.0%\n% exp_id: obs_only_eps0.1_spatial → 35.0%, argmin_K10_spatial → 34.0%\nWe presented ACR-VLA, a sample-then-correct pipeline that wraps a frozen flow-matching VLA with multi-sample conformal selection followed by a lightweight residual correction module (${\\sim}$329K parameters, ${\\sim}$3\\,ms overhead).\nOn LIBERO-Object, observation-conditioned CRM achieves 19.0\\% task success versus 12.0\\% for selection alone (+7.0\\,pp).\nOn LIBERO-Spatial, correction provides no measurable benefit over selection (best CRM within 1\\,pp of the selection baseline), indicating the approach is effective for fine-grained motor correction under object-level distribution shift but not for spatial re-planning.\n\n% exp_id: perdof_eps0.1_object → 11.0%, obs_only_eps0.1_object → 19.0%\nOur central negative result is that per-DOF conformal features do not improve correction over observation-only conditioning, despite providing intuitively richer uncertainty information.\nAt the $K{=}10$ sample budget, covariance estimation noise outweighs the information gain.\nThis is a cautionary finding for the broader agenda of uncertainty-conditioned action correction: the gap between offline prediction accuracy and closed-loop task success remains a fundamental challenge.\n\nConcrete next steps include: (i)~validation across multiple VLA backbones and scales, (ii)~real-robot transfer experiments, (iii)~adaptive magnitude scheduling (learned $\\varepsilon$ conditioned on observation uncertainty), and (iv)~higher-$K$ sampling to revisit whether per-DOF conformal features become useful with better covariance estimates.\n",
      "numLines": 58,
      "startLine": 1,
      "totalLines": 58
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the paper sections. Let me systematically extract every citation and the method attribution made about it, then verify each one.

Let me catalog all citations and their attributions:

From Introduction:
1. `black2024pi0` - π₀: VLA that generates actions via flow matching
2. `shukor2025smolvla` - SmolVLA: VLA that generates actions via flow matching
3. `lipman2023flow` - Flow matching (technique)
4. `liu2023libero` - LIBERO benchmark
5. `fei2025liberoplus` - LIBERO-Plus: visual/physical perturbation benchmark; claims π₀ drops from 94.2% to 6.6% under robot initial-state perturbation, UniVLA from 95.2% to 4.3% under camera viewpoint changes


6. `srpo2025` - SRPO: training-time robustness method with "robustness-aware objectives"
7. `robustvla2025` - RobustVLA: training-time robustness method with "robustness-aware objectives"
8. `digflow2025` - DiG-Flow: training-time robustness method with "robustness-aware objectives"
9. `liu2026ttvla` - TT-VLA: "test-time reinforcement learning"
10. `chen2026reconvla` - ReconVLA: applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution scenarios

, though it functions as an uncertainty quantification framework rather than directly improving actions. VLA-Pilot uses evolutionary optimization across action samples but takes 2.41 seconds per control step, while A2C2 learns a per-step correction head on a frozen VLA without multi-sample selection or explicit magnitude constraints. I'm also noting Ledoit-Wolf shrinkage covariance estimation and Braun et al.'s Conformalized Gaussian Scoring as relevant statistical methods, plus RobustVLA's approach combining RL post-training with Jacobian and smoothness regularization.

Moving through more recent work: SRPO applies self-referential RL fine-tuning using successful rollouts as references for reward shaping, DigFlow gates control rebalancing via distributional discrepancy between embeddings without modifying the flow trajectory, and Liu et al.'s method adapts VLA parameters at test time through RL with progress rewards. Chen et al.'s approach applies conformal quantile regression for per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, providing a principled uncertainty framework that doesn't require retraining.

Continuing with the recent methods: SC-VLA performs online action refinement through sparse world imagination and residual RL, VLA-Pilot applies evolutionary diffusion optimization guided by an MLLM verifier, and A2C² learns a lightweight correction head that refines actions within pre-generated chunks at each control step. Angelopoulos et al. provide distribution-free coverage guarantees under exchangeability, Braun et al. develop Conformalized Gaussian Scoring using Mahalanobis-based nonconformity scores for prediction regions respecting cross-dimensional covariance, and Zhao et al. apply conformal prediction to quantify uncertainty in high-DOF action mappings during shared autonomy.

Now looking at more recent approaches: CP-Loop integrates conformal prediction regions as feedback constraints in trajectory optimization, while ACP-CBF combines adaptive conformal prediction with control barrier functions to maintain safety under distribution shift in RL policies. Silver et al. introduced residual policy learning for classical controllers with zero-initialization, TRANSIC uses a learned binary gate to decide when to apply sim-to-real residuals, PLD freezes the VLA backbone and trains lightweight residual actors with bounded corrections via off-policy RL before distilling improved trajectories back, and DRC applies exponential decay to each expert correction event.

Moving into more recent work: DiU derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, SAFE trains a multitask failure detector on VLA internal features with conformal prediction for calibration timing, and there's a systematic study on confidence calibration in VLAs showing that prompt ensembles with Platt scaling improve calibration. DAgger is the foundational imitation learning approach dealing with compounding error.

I'm seeing these citations repeated across the Method and Experiments sections, so I need to verify the key attributions now, particularly for ReconVLA which the context indicates was previously mentioned. Now I'm going through the remaining method attributions—PLD's bounded residual actors, DRC's exponential decay, DiU's closed-form posterior approach, and several conformal prediction variants like SAFE and the Braun et al. work. I need to verify these papers exist and that the descriptions match their actual contributions, particularly focusing on the less-established ones that are more prone to attribution errors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "a7b2d9d4-f6d9-44a0-a989-1817c7389f0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YSqfLFYRKLEsjWQxXcx3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5426,
      "cache_read_input_tokens": 45764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5426
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

_source line 42_

Now I have all sections. Let me systematically verify each citation's method attribution. I'll start with the most critical ones in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "02ae10aa-5862-4878-80b8-0c58784c1b0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YSqfLFYRKLEsjWQxXcx3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5426,
      "cache_read_input_tokens": 45764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5426
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_011ZZTZhQmByRAHrjxq2oeyd`</summary>

```json
{
  "query": "ReconVLA chen 2026 \"uncertainty-guided\" conformal quantile regression VLA robotic control arXiv 2604.16677"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "555bc65f-b53c-4885-b9b2-3e8a746a6beb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YSqfLFYRKLEsjWQxXcx3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5426,
      "cache_read_input_tokens": 45764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5426
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

_source line 44_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019prxYFviMYVjz53rRCLPG2`</summary>

```json
{
  "query": "A2C2 \"Leave No Observation Behind\" VLA action chunks correction 2025 arXiv 2509.23224"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "b6ad960b-2ae3-4d33-a65c-e8fa421fdb05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YSqfLFYRKLEsjWQxXcx3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5426,
      "cache_read_input_tokens": 45764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5426
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X19pJtQKGfR3o5AcXeAA7y`</summary>

```json
{
  "query": "SRPO \"self-referential policy optimization\" VLA 2025 arXiv 2511.15605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "5a9ac99a-5419-48e2-802d-2bc7494d6b4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YSqfLFYRKLEsjWQxXcx3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5426,
      "cache_read_input_tokens": 45764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5426
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U2QmXUmi9ULv7U7s7H1kGt`</summary>

```json
{
  "query": "RobustVLA \"robustness-aware reinforcement post-training\" VLA 2025 arXiv 2511.01331"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "a549061e-8221-428f-b5f9-4930bcfd4f81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YSqfLFYRKLEsjWQxXcx3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5426,
      "cache_read_input_tokens": 45764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5426
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

_source line 47 · 2026-05-15T20:47:12.582Z_

<details><summary>↩ Tool result · `toolu_011ZZTZhQmByRAHrjxq2oeyd`</summary>

```text
Web search results for query: "ReconVLA chen 2026 "uncertainty-guided" conformal quantile regression VLA robotic control arXiv 2604.16677"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"Conformal Quantile Regression for Neural Probabilistic Constitutive Modeling","url":"https://arxiv.org/html/2601.17437"},{"title":"Conformal prediction for uncertainties in the neutron star equation of state","url":"https://arxiv.org/html/2604.21039"},{"title":"1 INTRODUCTION","url":"https://arxiv.org/html/2306.08693v2"},{"title":"QUTCC : Quantile Uncertainty Training and Conformal Calibration for Imaging Inverse Problems","url":"https://arxiv.org/html/2507.14760"},{"title":"[2507.14760] QUTCC: Quantile Uncertainty Training and Conformal Calibration for Imaging Inverse Problems","url":"https://arxiv.org/abs/2507.14760"},{"title":"[2306.08693] Integrating Uncertainty Awareness into Conformalized Quantile Regression","url":"https://arxiv.org/abs/2306.08693"},{"title":"Behind the Noise: Conformal Quantile Regression Reveals Emergent Representations","url":"https://arxiv.org/html/2505.08176v1"},{"title":"Conformalized Quantile Regression Yaniv Romano Department of Statistics","url":"https://papers.neurips.cc/paper/8613-conformalized-quantile-regression.pdf"},{"title":"Conformalized quantile regression | Proceedings of the 33rd International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3454287.3454605"}]

Perfect! I found the paper. Here are the search results for your query:

The paper "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control" was authored by Lingling Chen, Zongyao Lyu, and William J. Beksi from The University of Texas at Arlington, with arXiv ID 2604.16677v1 posted on April 17, 2026.

The paper introduces ReconVLA, a reliable conformal model that produces uncertainty-guided and failure-aware control signals. The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success.

The work incorporates conformal quantile regression (CQR)-based uncertainty quantification into the VLA's action generation process and its state monitoring, allowing the robot to detect when it "doesn't know" or is likely to fail before a catastrophe occurs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "f6659d63-ad3c-4790-a328-06501d48bf9b",
  "tool_use_result": {
    "query": "ReconVLA chen 2026 \"uncertainty-guided\" conformal quantile regression VLA robotic control arXiv 2604.16677",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XFyQP5P8sn1LBzVorC8SwJ",
        "content": [
          {
            "title": "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control",
            "url": "https://arxiv.org/html/2604.16677v1"
          },
          {
            "title": "Conformal Quantile Regression for Neural Probabilistic Constitutive Modeling",
            "url": "https://arxiv.org/html/2601.17437"
          },
          {
            "title": "Conformal prediction for uncertainties in the neutron star equation of state",
            "url": "https://arxiv.org/html/2604.21039"
          },
          {
            "title": "1 INTRODUCTION",
            "url": "https://arxiv.org/html/2306.08693v2"
          },
          {
            "title": "QUTCC : Quantile Uncertainty Training and Conformal Calibration for Imaging Inverse Problems",
            "url": "https://arxiv.org/html/2507.14760"
          },
          {
            "title": "[2507.14760] QUTCC: Quantile Uncertainty Training and Conformal Calibration for Imaging Inverse Problems",
            "url": "https://arxiv.org/abs/2507.14760"
          },
          {
            "title": "[2306.08693] Integrating Uncertainty Awareness into Conformalized Quantile Regression",
            "url": "https://arxiv.org/abs/2306.08693"
          },
          {
            "title": "Behind the Noise: Conformal Quantile Regression Reveals Emergent Representations",
            "url": "https://arxiv.org/html/2505.08176v1"
          },
          {
            "title": "Conformalized Quantile Regression Yaniv Romano Department of Statistics",
            "url": "https://papers.neurips.cc/paper/8613-conformalized-quantile-regression.pdf"
          },
          {
            "title": "Conformalized quantile regression | Proceedings of the 33rd International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3454287.3454605"
          }
        ]
      },
      "Perfect! I found the paper. Here are the search results for your query:\n\nThe paper \"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\" was authored by Lingling Chen, Zongyao Lyu, and William J. Beksi from The University of Texas at Arlington, with arXiv ID 2604.16677v1 posted on April 17, 2026.\n\nThe paper introduces ReconVLA, a reliable conformal model that produces uncertainty-guided and failure-aware control signals. The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success.\n\nThe work incorporates conformal quantile regression (CQR)-based uncertainty quantification into the VLA's action generation process and its state monitoring, allowing the robot to detect when it \"doesn't know\" or is likely to fail before a catastrophe occurs."
    ],
    "durationSeconds": 5.8254580879999995
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T20:47:17.696Z_

<details><summary>↩ Tool result · `toolu_019prxYFviMYVjz53rRCLPG2`</summary>

```text
Web search results for query: "A2C2 "Leave No Observation Behind" VLA action chunks correction 2025 arXiv 2509.23224"

Links: [{"title":"[2509.23224] Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/abs/2509.23224"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"},{"title":"LEAVE NO OBSERVATION BEHIND: REAL-TIME COR- RECTION FOR VLA ACTION CHUNKS","url":"https://www.arxiv.org/pdf/2509.23224"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks | OpenReview","url":"https://openreview.net/forum?id=y5SGBsndWv"},{"title":"VLA Model Post-Training via Action-Chunked PPO and Self Behavior Cloning","url":"https://arxiv.org/html/2509.25718"},{"title":"VGAS: Value-Guided Action-Chunk Selection for Few-Shot Vision-Language-Action Adaptation","url":"https://arxiv.org/html/2602.07399"},{"title":"VLA Knows Its Limits","url":"https://arxiv.org/html/2602.21445"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"},{"title":": A Vision-Language-Action Model Bridging Understanding and Generation to Actions","url":"https://arxiv.org/html/2509.06951v2"},{"title":"Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding","url":"https://arxiv.org/html/2503.02310v1"}]

Based on the search results, I found detailed information about the paper you're looking for:

## "Leave No Observation Behind: Real-time Correction for VLA Action Chunks"

Asynchronous Action Chunk Correction (A2C2) is a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk.

### Key Problem and Solution

To improve efficiency and temporal coherence, Vision-Language-Action (VLA) models often predict action chunks; however, this action chunking harms reactivity under inference delay and long horizons. The module combines the latest observation, the predicted action from VLA (base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction.

### Key Features

This preserves the base model's competence while restoring closed-loop responsiveness. The approach requires no retraining of the base policy and is orthogonal to asynchronous execution schemes such as Real Time Chunking (RTC).

### Results

On the dynamic Kinetix task suite (12 tasks) and LIBERO Spatial, the method yields consistent success rate improvements across increasing delays and execution horizons (+23% point and +7% point respectively, compared to RTC), and also improves robustness for long horizons even with zero injected delay.

The paper was submitted to arXiv on September 27, 2025 (arXiv:2509.23224).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "6c8a51b4-83ed-4ebd-9b40-9931d1619cb1",
  "tool_use_result": {
    "query": "A2C2 \"Leave No Observation Behind\" VLA action chunks correction 2025 arXiv 2509.23224",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FcYneJcHd6Qtu47vyVng8u",
        "content": [
          {
            "title": "[2509.23224] Leave No Observation Behind: Real-time Correction for VLA Action Chunks",
            "url": "https://arxiv.org/abs/2509.23224"
          },
          {
            "title": "Leave No Observation Behind: Real-time Correction for VLA Action Chunks",
            "url": "https://arxiv.org/html/2509.23224v1"
          },
          {
            "title": "LEAVE NO OBSERVATION BEHIND: REAL-TIME COR- RECTION FOR VLA ACTION CHUNKS",
            "url": "https://www.arxiv.org/pdf/2509.23224"
          },
          {
            "title": "Leave No Observation Behind: Real-time Correction for VLA Action Chunks | OpenReview",
            "url": "https://openreview.net/forum?id=y5SGBsndWv"
          },
          {
            "title": "VLA Model Post-Training via Action-Chunked PPO and Self Behavior Cloning",
            "url": "https://arxiv.org/html/2509.25718"
          },
          {
            "title": "VGAS: Value-Guided Action-Chunk Selection for Few-Shot Vision-Language-Action Adaptation",
            "url": "https://arxiv.org/html/2602.07399"
          },
          {
            "title": "VLA Knows Its Limits",
            "url": "https://arxiv.org/html/2602.21445"
          },
          {
            "title": "Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge",
            "url": "https://arxiv.org/html/2512.06951v1"
          },
          {
            "title": ": A Vision-Language-Action Model Bridging Understanding and Generation to Actions",
            "url": "https://arxiv.org/html/2509.06951v2"
          },
          {
            "title": "Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding",
            "url": "https://arxiv.org/html/2503.02310v1"
          }
        ]
      },
      "Based on the search results, I found detailed information about the paper you're looking for:\n\n## \"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\"\n\nAsynchronous Action Chunk Correction (A2C2) is a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk.\n\n### Key Problem and Solution\n\nTo improve efficiency and temporal coherence, Vision-Language-Action (VLA) models often predict action chunks; however, this action chunking harms reactivity under inference delay and long horizons. The module combines the latest observation, the predicted action from VLA (base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction.\n\n### Key Features\n\nThis preserves the base model's competence while restoring closed-loop responsiveness. The approach requires no retraining of the base policy and is orthogonal to asynchronous execution schemes such as Real Time Chunking (RTC).\n\n### Results\n\nOn the dynamic Kinetix task suite (12 tasks) and LIBERO Spatial, the method yields consistent success rate improvements across increasing delays and execution horizons (+23% point and +7% point respectively, compared to RTC), and also improves robustness for long horizons even with zero injected delay.\n\nThe paper was submitted to arXiv on September 27, 2025 (arXiv:2509.23224)."
    ],
    "durationSeconds": 10.009251168999995
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T20:47:19.941Z_

<details><summary>↩ Tool result · `toolu_01X19pJtQKGfR3o5AcXeAA7y`</summary>

```text
Web search results for query: "SRPO "self-referential policy optimization" VLA 2025 arXiv 2511.15605"

Links: [{"title":"[2511.15605] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.15605"},{"title":"Paper page - SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://huggingface.co/papers/2511.15605"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.15605"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/resources/2511.15605v1"},{"title":"[Quick Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://liner.com/review/srpo-selfreferential-policy-optimization-for-visionlanguageaction-models"},{"title":"[Literature Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/srpo-self-referential-policy-optimization-for-vision-language-action-models"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/397780691_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models"},{"title":"SRPO Code Implementation Explained — siiRL documentation","url":"https://siirl.readthedocs.io/en/latest/programming_guide/srpo_code_explained.html"},{"title":"[2406.01660] Self-Improving Robust Preference Optimization","url":"https://arxiv.org/abs/2406.01660"},{"title":"WMPO: World Model-based Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.09515v1"}]

I found comprehensive information about the SRPO paper. Here's what the search results reveal:

## SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models

The paper was submitted on November 19, 2025, with a second version on November 30, 2025, authored by Senyu Fei and 9 other collaborators.

### Problem and Solution

Vision-Language-Action (VLA) models excel in robotic manipulation but are constrained by their heavy reliance on expert demonstrations, leading to demonstration bias and limiting performance. Current VLA-RL methods are crippled by severe reward sparsity, with relying on binary success indicators wasting valuable information in failed trajectories and resulting in low training efficiency.

To solve this, the paper proposes Self-Referential Policy Optimization (SRPO), a novel VLA-RL framework that eliminates the need for external demonstrations or manual reward engineering by leveraging the model's own successful trajectories, generated within the current training batch, as a self-reference.

### Key Innovation

A core innovation is the use of latent world representations to measure behavioral progress robustly. Rather than relying on raw pixels or requiring domain-specific fine-tuning, the method utilizes compressed, transferable encodings from a world model's latent space that naturally capture progress patterns across environments, enabling accurate, generalized trajectory comparison.

### Results

Starting from a supervised baseline with 48.9% success, SRPO achieves a new state-of-the-art success rate of 99.2% in just 200 RL steps, representing a 103% relative improvement without any extra supervision. Furthermore, SRPO shows substantial robustness, achieving a 167% performance improvement on the LIBERO-Plus benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "d152fdbc-29a4-46aa-9860-19af7ab61cd8",
  "tool_use_result": {
    "query": "SRPO \"self-referential policy optimization\" VLA 2025 arXiv 2511.15605",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CWrrLpoijqiaG2XugNgWfJ",
        "content": [
          {
            "title": "[2511.15605] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2511.15605"
          },
          {
            "title": "Paper page - SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2511.15605"
          },
          {
            "title": "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.15605"
          },
          {
            "title": "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2511.15605v1"
          },
          {
            "title": "[Quick Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://liner.com/review/srpo-selfreferential-policy-optimization-for-visionlanguageaction-models"
          },
          {
            "title": "[Literature Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://www.themoonlight.io/en/review/srpo-self-referential-policy-optimization-for-vision-language-action-models"
          },
          {
            "title": "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | Request PDF",
            "url": "https://www.researchgate.net/publication/397780691_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models"
          },
          {
            "title": "SRPO Code Implementation Explained — siiRL documentation",
            "url": "https://siirl.readthedocs.io/en/latest/programming_guide/srpo_code_explained.html"
          },
          {
            "title": "[2406.01660] Self-Improving Robust Preference Optimization",
            "url": "https://arxiv.org/abs/2406.01660"
          },
          {
            "title": "WMPO: World Model-based Policy Optimization for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.09515v1"
          }
        ]
      },
      "I found comprehensive information about the SRPO paper. Here's what the search results reveal:\n\n## SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\n\nThe paper was submitted on November 19, 2025, with a second version on November 30, 2025, authored by Senyu Fei and 9 other collaborators.\n\n### Problem and Solution\n\nVision-Language-Action (VLA) models excel in robotic manipulation but are constrained by their heavy reliance on expert demonstrations, leading to demonstration bias and limiting performance. Current VLA-RL methods are crippled by severe reward sparsity, with relying on binary success indicators wasting valuable information in failed trajectories and resulting in low training efficiency.\n\nTo solve this, the paper proposes Self-Referential Policy Optimization (SRPO), a novel VLA-RL framework that eliminates the need for external demonstrations or manual reward engineering by leveraging the model's own successful trajectories, generated within the current training batch, as a self-reference.\n\n### Key Innovation\n\nA core innovation is the use of latent world representations to measure behavioral progress robustly. Rather than relying on raw pixels or requiring domain-specific fine-tuning, the method utilizes compressed, transferable encodings from a world model's latent space that naturally capture progress patterns across environments, enabling accurate, generalized trajectory comparison.\n\n### Results\n\nStarting from a supervised baseline with 48.9% success, SRPO achieves a new state-of-the-art success rate of 99.2% in just 200 RL steps, representing a 103% relative improvement without any extra supervision. Furthermore, SRPO shows substantial robustness, achieving a 167% performance improvement on the LIBERO-Plus benchmark."
    ],
    "durationSeconds": 11.781910784000006
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T20:47:20.293Z_

<details><summary>↩ Tool result · `toolu_01U2QmXUmi9ULv7U7s7H1kGt`</summary>

```text
Web search results for query: "RobustVLA "robustness-aware reinforcement post-training" VLA 2025 arXiv 2511.01331"

Links: [{"title":"[2511.01331] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.01331"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.01331v1"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/397231717_RobustVLA_Robustness-Aware_Reinforcement_Post-Training_for_Vision-Language-Action_Models"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=9g7UXLqD4B"},{"title":"[Literature Review] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/robustvla-robustness-aware-reinforcement-post-training-for-vision-language-action-models"},{"title":"ROBUSTVLA: ROBUSTNESS-AWARE REINFORCE","url":"https://openreview.net/pdf/d2f9e3b68ce76261050b0db5ea64048b5e336142.pdf"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/html/2510.00037"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"}]

I found comprehensive information about RobustVLA. Here are the key findings:

## Overview

RobustVLA is a lightweight online RL post-training method designed to explicitly enhance the resilience of VLA models. Vision-Language-Action (VLA) models have recently emerged as powerful general-purpose policies for robotic manipulation, but they often fail to generalize reliably in out-of-distribution deployments, where unavoidable disturbances such as observation noise, sensor errors, or actuation perturbations become prevalent.

## Key Technical Approach

Through a systematic robustness analysis, two key regularizations were identified: Jacobian regularization, which mitigates sensitivity to observation noise, and smoothness regularization, which stabilizes policies under action perturbations. The robustness gap under observation perturbations is governed by the Jacobian sensitivity of the VLA model, whereas under action perturbations it is controlled by the smoothness of the VLA model update.

## Results and Performance

Extensive experiments across diverse robotic environments demonstrate that RobustVLA significantly outperforms prior state-of-the-art methods in robustness and reliability. The paper was published to arXiv in November 2025 (arXiv:2511.01331) by authors including Hongyin Zhang and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "9e8781e8-9957-46a7-8398-728b9697def5",
  "tool_use_result": {
    "query": "RobustVLA \"robustness-aware reinforcement post-training\" VLA 2025 arXiv 2511.01331",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GjzKCpvSDCnhszFzD28x9z",
        "content": [
          {
            "title": "[2511.01331] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2511.01331"
          },
          {
            "title": "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.01331"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2511.01331v1"
          },
          {
            "title": "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/397231717_RobustVLA_Robustness-Aware_Reinforcement_Post-Training_for_Vision-Language-Action_Models"
          },
          {
            "title": "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=9g7UXLqD4B"
          },
          {
            "title": "[Literature Review] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models",
            "url": "https://www.themoonlight.io/en/review/robustvla-robustness-aware-reinforcement-post-training-for-vision-language-action-models"
          },
          {
            "title": "ROBUSTVLA: ROBUSTNESS-AWARE REINFORCE",
            "url": "https://openreview.net/pdf/d2f9e3b68ce76261050b0db5ea64048b5e336142.pdf"
          },
          {
            "title": "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/html/2510.00037"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 ON ROBUSTNESS",
            "url": "https://arxiv.org/pdf/2510.00037v4"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/html/2509.09674v1"
          }
        ]
      },
      "I found comprehensive information about RobustVLA. Here are the key findings:\n\n## Overview\n\nRobustVLA is a lightweight online RL post-training method designed to explicitly enhance the resilience of VLA models. Vision-Language-Action (VLA) models have recently emerged as powerful general-purpose policies for robotic manipulation, but they often fail to generalize reliably in out-of-distribution deployments, where unavoidable disturbances such as observation noise, sensor errors, or actuation perturbations become prevalent.\n\n## Key Technical Approach\n\nThrough a systematic robustness analysis, two key regularizations were identified: Jacobian regularization, which mitigates sensitivity to observation noise, and smoothness regularization, which stabilizes policies under action perturbations. The robustness gap under observation perturbations is governed by the Jacobian sensitivity of the VLA model, whereas under action perturbations it is controlled by the smoothness of the VLA model update.\n\n## Results and Performance\n\nExtensive experiments across diverse robotic environments demonstrate that RobustVLA significantly outperforms prior state-of-the-art methods in robustness and reliability. The paper was published to arXiv in November 2025 (arXiv:2511.01331) by authors including Hongyin Zhang and colleagues."
    ],
    "durationSeconds": 11.542530593000004
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Good, let me continue verifying the remaining citations. Let me check:
1. ReconVLA: The paper says it "applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, providing a principled uncertainty quantification framework that operates without retraining but does not modify the VLA's actions." The search confirms it's an uncertainty-guided and failure-aware framework using CQR. This matches the current attribution. The D034 context says it should be positioned as "UQ-guided approach" not "selection-only" — the current text already correctly describes it as a UQ framework. Good.


2. Now I'm double-checking the ReconVLA description more carefully. The intro clarifies that it applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution states, functioning as an uncertainty quantification framework rather than an action improvement method. The title "Uncertainty-Guided and Failure-Aware" confirms this positioning. Let me verify what ReconVLA actually does with the actions themselves.
3. A2C2: described as "learns a lightweight correction head that runs at every control step to correct each action within a pre-generated chunk, restoring closed-loop responsiveness; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty." The search confirms it's a correction head for action chunks. A2C2 doesn't have a selection stage—it just corrects the existing action chunk unconditionally, so that attribution seems fair, though calling out the lack of multi-sample selection might be slightly unfair since that's simply a different design philosophy rather than a limitation.

For SRPO, the description about using the policy's own successful rollouts as references to shape rewards for failed trajectories via latent world model representations checks out—the search confirms it leverages successful trajectories from the current batch and uses latent world representations to measure behavioral progress.

RobustVLA combines RL post-training with Jacobian regularization to handle observation noise and smoothness regularization for action perturbations, which matches what the search results show.

Now I need to find information on the remaining papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "816cc82e-df3d-4712-b6d8-b52bf741a4c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvW4k27UULzbzNBW8avxmh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5739,
      "cache_read_input_tokens": 51190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5739
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

_source line 52_

ReconVLA attribution looks correct — it's described as a UQ framework, matching the D034 repositioning. Let me continue verifying the remaining citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "3764e7a2-ac59-4624-86d0-f0337e2fc9b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvW4k27UULzbzNBW8avxmh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5739,
      "cache_read_input_tokens": 51190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5739
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

_source line 53_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MRxwGPsTTyVCKP5ts2q5zA`</summary>

```json
{
  "query": "DiG-Flow \"discrepancy-guided flow matching\" VLA 2025 arXiv 2512.01715 distributional discrepancy gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "1e7a6ecf-b71e-453e-ad00-4a3c8c8ad32b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvW4k27UULzbzNBW8avxmh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5739,
      "cache_read_input_tokens": 51190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5739
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UFKBbLJkqs9JNESPKrYyeX`</summary>

```json
{
  "query": "TT-VLA \"test-time reinforcement learning\" VLA adaptation 2026 arXiv 2601.06748"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "545e9a32-9d6d-4b7b-bcf9-71d336c8a0b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvW4k27UULzbzNBW8avxmh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5739,
      "cache_read_input_tokens": 51190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5739
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XkRSZTtMWabfooFsJuME61`</summary>

```json
{
  "query": "VLA-Pilot \"evolutionary diffusion optimization\" MLLM verifier 2025 arXiv 2511.14178 inference time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "56a88399-0192-41f3-bf1d-267cc5bb93bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvW4k27UULzbzNBW8avxmh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5739,
      "cache_read_input_tokens": 51190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5739
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WogBaUJ8r6Yf1w56ViG4Hy`</summary>

```json
{
  "query": "SC-VLA \"self-correcting VLA\" sparse world imagination residual RL 2026 arXiv 2602.21633"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "c83f7f46-e86e-47aa-80cd-1af271569761",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvW4k27UULzbzNBW8avxmh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5739,
      "cache_read_input_tokens": 51190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5739
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

_source line 57 · 2026-05-15T20:47:47.430Z_

<details><summary>↩ Tool result · `toolu_01XkRSZTtMWabfooFsJuME61`</summary>

```text
Web search results for query: "VLA-Pilot "evolutionary diffusion optimization" MLLM verifier 2025 arXiv 2511.14178 inference time"

Links: [{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"},{"title":"[2511.14178] Towards Deploying VLA without Fine-Tuning","url":"https://arxiv.org/abs/2511.14178"},{"title":"[2511.01718] Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process","url":"https://arxiv.org/abs/2511.01718"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process","url":"https://arxiv.org/html/2511.01718v1"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/html/2508.20072v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"[2511.21542] E0: Enhancing Generalization and Fine-Grained Control in VLA Models via Tweedie Discrete Diffusion","url":"https://arxiv.org/abs/2511.21542"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2509.06951"},{"title":"Beyond Autoregression: An Empirical Study of Diffusion Large Language Models for Code Generation","url":"https://arxiv.org/html/2509.11252v1"}]

I found the paper you're searching for! Here's what I found about VLA-Pilot and the relevant details:

VLA-Pilot is a training-free inference-time policy steering method that improves both the generalization and task alignment of pre-trained VLA policies for downstream deployment. 

Regarding the key components you asked about:

- **MLLM Verifier**: The method leverages Multimodal Large Language Model (MLLMs) as open-world verifiers to enhance generalization, and employs an Evolutionary Diffusion process as an action optimizer to improve task alignment.

- **Inference Time**: The overall inference time is reported at 2.41 seconds. The main bottleneck lies in MLLM-based reward reasoning.

The paper (arXiv 2511.14178) was submitted on November 18, 2025. VLA-Pilot is a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection, and experimental results demonstrate that it substantially boosts the success rates of off-the-shelf pre-trained VLA policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "a39b4d24-04b7-496c-8fe6-0a3df8fe2943",
  "tool_use_result": {
    "query": "VLA-Pilot \"evolutionary diffusion optimization\" MLLM verifier 2025 arXiv 2511.14178 inference time",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K71xPETaT17NParGrDHR7X",
        "content": [
          {
            "title": "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion",
            "url": "https://arxiv.org/html/2511.14178"
          },
          {
            "title": "[2511.14178] Towards Deploying VLA without Fine-Tuning",
            "url": "https://arxiv.org/abs/2511.14178"
          },
          {
            "title": "[2511.01718] Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process",
            "url": "https://arxiv.org/abs/2511.01718"
          },
          {
            "title": "Diffusion models for robotic manipulation: a survey - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"
          },
          {
            "title": "Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process",
            "url": "https://arxiv.org/html/2511.01718v1"
          },
          {
            "title": "Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies",
            "url": "https://arxiv.org/html/2508.20072v1"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "[2511.21542] E0: Enhancing Generalization and Fine-Grained Control in VLA Models via Tweedie Discrete Diffusion",
            "url": "https://arxiv.org/abs/2511.21542"
          },
          {
            "title": "Arxiv",
            "url": "https://arxiv.org/pdf/2509.06951"
          },
          {
            "title": "Beyond Autoregression: An Empirical Study of Diffusion Large Language Models for Code Generation",
            "url": "https://arxiv.org/html/2509.11252v1"
          }
        ]
      },
      "I found the paper you're searching for! Here's what I found about VLA-Pilot and the relevant details:\n\nVLA-Pilot is a training-free inference-time policy steering method that improves both the generalization and task alignment of pre-trained VLA policies for downstream deployment. \n\nRegarding the key components you asked about:\n\n- **MLLM Verifier**: The method leverages Multimodal Large Language Model (MLLMs) as open-world verifiers to enhance generalization, and employs an Evolutionary Diffusion process as an action optimizer to improve task alignment.\n\n- **Inference Time**: The overall inference time is reported at 2.41 seconds. The main bottleneck lies in MLLM-based reward reasoning.\n\nThe paper (arXiv 2511.14178) was submitted on November 18, 2025. VLA-Pilot is a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection, and experimental results demonstrate that it substantially boosts the success rates of off-the-shelf pre-trained VLA policies."
    ],
    "durationSeconds": 6.315133258999995
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T20:47:47.688Z_

<details><summary>↩ Tool result · `toolu_01UFKBbLJkqs9JNESPKrYyeX`</summary>

```text
Web search results for query: "TT-VLA "test-time reinforcement learning" VLA adaptation 2026 arXiv 2601.06748"

Links: [{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"[2601.06748] On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2601.06748"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.06748"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/399707107_On-the-Fly_VLA_Adaptation_via_Test-Time_Reinforcement_Learning"},{"title":"Test-Time RL for VLAs","url":"https://www.emergentmind.com/topics/test-time-reinforcement-learning-for-vlas-tt-vla"},{"title":"[2504.16084] TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2504.16084"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for","url":"https://arxiv.org/pdf/2604.18107"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"arXiv:2504.16084v3 [cs.CL] 30 Jun 2025 TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2504.16084"},{"title":"TTRL: Test-Time Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=VuVhgEiu20"}]

Based on the search results, I found the paper you were looking for. Here's what the research is about:

## TT-VLA: On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning

TT-VLA is a framework that enables on-the-fly policy adaptation during inference. The paper addresses a key limitation in Vision-Language-Action models by enabling robots to adapt their behavior during deployment without requiring explicit fine-tuning phases.

**Key Details:**

- **ArXiv ID**: 2601.06748
- **Submission Date**: January 11, 2026 (latest version: April 7, 2026)
- **Authors**: Led by Changyu Liu with 10 co-authors

**Problem Being Addressed:**

Current VLAs are primarily trained via supervised fine-tuning or training-time reinforcement learning, requiring explicit fine-tuning phases, human interventions, or controlled data collection, making them unsuitable for challenging simulated- or physical-world deployments where robots must respond autonomously and flexibly to evolving environments.

**Solution:**

TT-VLA formulates a dense reward mechanism that leverages step-by-step task-progress signals to refine action policies during test time while preserving the SFT/RL-trained priors.

**Results:**

Empirical results show that the approach enhances overall adaptability, stability, and task success in dynamic, previously unseen scenarios under simulated and real-world settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "eccfc602-967e-43ec-89df-4ea68e2117b1",
  "tool_use_result": {
    "query": "TT-VLA \"test-time reinforcement learning\" VLA adaptation 2026 arXiv 2601.06748",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Likxqk4rjowrMneXgDGSHP",
        "content": [
          {
            "title": "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2601.06748v1"
          },
          {
            "title": "[2601.06748] On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/abs/2601.06748"
          },
          {
            "title": "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2601.06748"
          },
          {
            "title": "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning | Request PDF",
            "url": "https://www.researchgate.net/publication/399707107_On-the-Fly_VLA_Adaptation_via_Test-Time_Reinforcement_Learning"
          },
          {
            "title": "Test-Time RL for VLAs",
            "url": "https://www.emergentmind.com/topics/test-time-reinforcement-learning-for-vlas-tt-vla"
          },
          {
            "title": "[2504.16084] TTRL: Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/abs/2504.16084"
          },
          {
            "title": "Test-Time Perturbation Learning with Delayed Feedback for",
            "url": "https://arxiv.org/pdf/2604.18107"
          },
          {
            "title": "[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/abs/2505.18719"
          },
          {
            "title": "arXiv:2504.16084v3 [cs.CL] 30 Jun 2025 TTRL: Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2504.16084"
          },
          {
            "title": "TTRL: Test-Time Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=VuVhgEiu20"
          }
        ]
      },
      "Based on the search results, I found the paper you were looking for. Here's what the research is about:\n\n## TT-VLA: On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\n\nTT-VLA is a framework that enables on-the-fly policy adaptation during inference. The paper addresses a key limitation in Vision-Language-Action models by enabling robots to adapt their behavior during deployment without requiring explicit fine-tuning phases.\n\n**Key Details:**\n\n- **ArXiv ID**: 2601.06748\n- **Submission Date**: January 11, 2026 (latest version: April 7, 2026)\n- **Authors**: Led by Changyu Liu with 10 co-authors\n\n**Problem Being Addressed:**\n\nCurrent VLAs are primarily trained via supervised fine-tuning or training-time reinforcement learning, requiring explicit fine-tuning phases, human interventions, or controlled data collection, making them unsuitable for challenging simulated- or physical-world deployments where robots must respond autonomously and flexibly to evolving environments.\n\n**Solution:**\n\nTT-VLA formulates a dense reward mechanism that leverages step-by-step task-progress signals to refine action policies during test time while preserving the SFT/RL-trained priors.\n\n**Results:**\n\nEmpirical results show that the approach enhances overall adaptability, stability, and task success in dynamic, previously unseen scenarios under simulated and real-world settings."
    ],
    "durationSeconds": 7.512004474999994
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-15T20:47:49.203Z_

<details><summary>↩ Tool result · `toolu_01WogBaUJ8r6Yf1w56ViG4Hy`</summary>

```text
Web search results for query: "SC-VLA "self-correcting VLA" sparse world imagination residual RL 2026 arXiv 2602.21633"

Links: [{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633.pdf"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy","url":"https://arxiv.org/pdf/2602.06508"},{"title":"Interesting Directions in Vision-Language-Action Model Research","url":"https://itcanthink.substack.com/p/interesting-directions-in-vision"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL","url":"https://arxiv.org/html/2511.00091"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance","url":"https://arxiv.org/html/2507.22424v1"}]

Based on the search results, here's what I found about SC-VLA (Self-Correcting VLA):

Self-Correcting VLA (SC-VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination. The method designs sparse world imagination by integrating auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution. It also introduces an online action refinement module to reshape progress-dependent dense rewards, adjusting trajectory orientation based on predicted sparse future states.

Evaluations on challenging robot manipulation tasks from simulation benchmarks and real-world settings demonstrate that SC-VLA achieves state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.

The paper was published on arXiv on February 25, 2026 (arXiv 2602.21633), with authors including Chenyv Liu, Wentao Tan, and others. Code is available on GitHub at the repository "Kisaragi0/SC-VLA".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "a8543f5f-dd63-43d7-8723-9eb746e3d7c6",
  "tool_use_result": {
    "query": "SC-VLA \"self-correcting VLA\" sparse world imagination residual RL 2026 arXiv 2602.21633",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PtkKpbCoRMoYwHTar8DmLF",
        "content": [
          {
            "title": "[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/abs/2602.21633"
          },
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/html/2602.21633.pdf"
          },
          {
            "title": "GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub",
            "url": "https://github.com/Kisaragi0/SC-VLA"
          },
          {
            "title": "World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy",
            "url": "https://arxiv.org/pdf/2602.06508"
          },
          {
            "title": "Interesting Directions in Vision-Language-Action Model Research",
            "url": "https://itcanthink.substack.com/p/interesting-directions-in-vision"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL",
            "url": "https://arxiv.org/html/2511.00091"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data ...",
            "url": "https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"
          },
          {
            "title": "[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/abs/2505.18719"
          },
          {
            "title": "Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance",
            "url": "https://arxiv.org/html/2507.22424v1"
          }
        ]
      },
      "Based on the search results, here's what I found about SC-VLA (Self-Correcting VLA):\n\nSelf-Correcting VLA (SC-VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination. The method designs sparse world imagination by integrating auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution. It also introduces an online action refinement module to reshape progress-dependent dense rewards, adjusting trajectory orientation based on predicted sparse future states.\n\nEvaluations on challenging robot manipulation tasks from simulation benchmarks and real-world settings demonstrate that SC-VLA achieves state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.\n\nThe paper was published on arXiv on February 25, 2026 (arXiv 2602.21633), with authors including Chenyv Liu, Wentao Tan, and others. Code is available on GitHub at the repository \"Kisaragi0/SC-VLA\"."
    ],
    "durationSeconds": 7.276388690000007
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T20:47:49.946Z_

<details><summary>↩ Tool result · `toolu_01MRxwGPsTTyVCKP5ts2q5zA`</summary>

```text
Web search results for query: "DiG-Flow "discrepancy-guided flow matching" VLA 2025 arXiv 2512.01715 distributional discrepancy gating"

Links: [{"title":"BeingBeyond ∝ DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/pdf/2512.01715"},{"title":"[2512.01715] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/abs/2512.01715"},{"title":"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/html/2512.01715v1"},{"title":"GitHub - BeingBeyond/DiG-Flow: DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://github.com/BeingBeyond/DiG-Flow"},{"title":"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models - Takara TLDR | Takara TLDR","url":"https://tldr.takara.ai/p/2512.01715"},{"title":"[Quick Review] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://liner.com/review/digflow-discrepancyguided-flow-matching-for-robust-vla-models"},{"title":"GitHub - iszhanjiawei/flow_matching_arxiv_daily · GitHub","url":"https://github.com/iszhanjiawei/flow_matching_arxiv_daily"},{"title":"Dream-VL & Dream-VLA: Open Vision-Language and ...","url":"https://arxiv.org/pdf/2512.22615"},{"title":"AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.14148v1"},{"title":"[2506.02070] An Introduction to Flow Matching and Diffusion Models","url":"https://arxiv.org/abs/2506.02070"}]

Based on the search results, I found the paper you're looking for. Here's information about DiG-Flow:

## DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models

DiG-Flow is a framework for Vision-Language-Action (VLA) models trained with flow matching for robotic manipulation tasks. The paper addresses the problem that VLA model performance often degrades under distribution shift and on complex multi-step tasks, suggesting that learned representations may not robustly capture task-relevant semantics.

### Key Concepts

DiG-Flow enhances VLA robustness through geometric regularization, with the key insight that the distributional discrepancy between observation and action embeddings provides a meaningful geometric signal: lower transport cost indicates compatible representations, while higher cost suggests potential misalignment.

### Framework Components

DiG-Flow computes a discrepancy measure between empirical distributions of observation and action embeddings and maps it to a modulation weight. This intervention operates at the representation level without modifying the flow matching path or target vector field.

### Theoretical and Empirical Results

The paper provides theoretical guarantees showing that discrepancy-guided training provably decreases the training objective, and that guided inference refinement converges with contraction. Empirically, DiG-Flow integrates into existing VLA architectures with negligible overhead and consistently improves performance, with particularly pronounced gains on complex multi-step tasks and under limited training data.

The paper was published on arXiv on December 1, 2025 (arXiv:2512.01715) by authors including Wanpeng Zhang and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "477a222f-b621-49e8-a04c-ef5892518b55",
  "tool_use_result": {
    "query": "DiG-Flow \"discrepancy-guided flow matching\" VLA 2025 arXiv 2512.01715 distributional discrepancy gating",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NWhT2eJtuE14ampEkzjnze",
        "content": [
          {
            "title": "BeingBeyond ∝ DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://arxiv.org/pdf/2512.01715"
          },
          {
            "title": "[2512.01715] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://arxiv.org/abs/2512.01715"
          },
          {
            "title": "DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://arxiv.org/html/2512.01715v1"
          },
          {
            "title": "GitHub - BeingBeyond/DiG-Flow: DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://github.com/BeingBeyond/DiG-Flow"
          },
          {
            "title": "DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models - Takara TLDR | Takara TLDR",
            "url": "https://tldr.takara.ai/p/2512.01715"
          },
          {
            "title": "[Quick Review] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://liner.com/review/digflow-discrepancyguided-flow-matching-for-robust-vla-models"
          },
          {
            "title": "GitHub - iszhanjiawei/flow_matching_arxiv_daily · GitHub",
            "url": "https://github.com/iszhanjiawei/flow_matching_arxiv_daily"
          },
          {
            "title": "Dream-VL & Dream-VLA: Open Vision-Language and ...",
            "url": "https://arxiv.org/pdf/2512.22615"
          },
          {
            "title": "AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.14148v1"
          },
          {
            "title": "[2506.02070] An Introduction to Flow Matching and Diffusion Models",
            "url": "https://arxiv.org/abs/2506.02070"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's information about DiG-Flow:\n\n## DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\n\nDiG-Flow is a framework for Vision-Language-Action (VLA) models trained with flow matching for robotic manipulation tasks. The paper addresses the problem that VLA model performance often degrades under distribution shift and on complex multi-step tasks, suggesting that learned representations may not robustly capture task-relevant semantics.\n\n### Key Concepts\n\nDiG-Flow enhances VLA robustness through geometric regularization, with the key insight that the distributional discrepancy between observation and action embeddings provides a meaningful geometric signal: lower transport cost indicates compatible representations, while higher cost suggests potential misalignment.\n\n### Framework Components\n\nDiG-Flow computes a discrepancy measure between empirical distributions of observation and action embeddings and maps it to a modulation weight. This intervention operates at the representation level without modifying the flow matching path or target vector field.\n\n### Theoretical and Empirical Results\n\nThe paper provides theoretical guarantees showing that discrepancy-guided training provably decreases the training objective, and that guided inference refinement converges with contraction. Empirically, DiG-Flow integrates into existing VLA architectures with negligible overhead and consistently improves performance, with particularly pronounced gains on complex multi-step tasks and under limited training data.\n\nThe paper was published on arXiv on December 1, 2025 (arXiv:2512.01715) by authors including Wanpeng Zhang and colleagues."
    ],
    "durationSeconds": 10.781320143000004
  }
}
```

</details>

---

### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
Let me continue checking the remaining citations. Let me verify:

1. DiG-Flow: Paper says "uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control, without modifying the flow-matching trajectory." Search says it "computes a discrepancy measure between empirical distributions of observation and action embeddings and maps it to a modulation weight. This intervention operates at the representation level without modifying the flow matching path or target vector field." This matches.

2. TT-VLA: Paper says "blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment." Search says "formulates a dense reward mechanism that leverages step-by-step task-progress signals to refine action policies during test time." The description says "per-task reward design" but the search says it uses "task-progress signals" as a general mechanism. 

I need to look more carefully at whether the related work actually claims per-task reward design is required, or if that's an overstatement. The intro mentions test-time RL with progress rewards, and the search confirms task-progress signals are used as the reward mechanism. The claim about requiring per-task reward design might be too strong given that the search suggests it enhances adaptability in unseen scenarios without explicitly mentioning per-task customization. Let me search for the exact wording in the related work section.

For VLA-Pilot, the intro describes "evolutionary optimization over action samples" while the related work specifies "Evolutionary Diffusion optimization" with an MLLM verifier. The search confirms both the Evolutionary Diffusion process and the MLLM verifier role, so the methods match — though the intro's phrasing is a bit loose since it's describing a specific technique rather than generic evolutionary optimization.

Now checking SC-VLA: the paper claims it uses "residual RL" for online action refinement, but the search results describe "sparse world imagination with auxiliary predictive heads" and "online action refinement to reshape progress-dependent dense rewards." The search doesn't explicitly mention "residual RL" — it talks about self-improvement and trajectory adjustment based on predicted sparse states. I need to verify whether this is actually residual RL or just a different form of RL-based refinement. Now I'm checking the specific claims about ReconVLA more carefully — the paper describes it as applying conformal quantile regression to calibrate action-level uncertainty bounds and detect out-of-distribution states, which aligns with what the search results show about conformal prediction on action tokens and uncertainty quantification in the state monitoring process.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "e9beee90-50a4-4dec-962d-1cd0ab70edcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WeiecS4NRprxWD7s1eEK7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2532,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 56929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
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

Let me verify more citations and dig deeper into ReconVLA's actual mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "0476d760-a424-4f10-b97a-f90a64babb22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WeiecS4NRprxWD7s1eEK7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2532,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 56929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SYdW1QVj22Gbw7UMs4mFW6`</summary>

```json
{
  "query": "ReconVLA arXiv 2604.16677 action selection modification \"failure-aware\" mechanism what does it do with actions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "5c59f95d-7c46-4a57-9162-029ce3d460fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WeiecS4NRprxWD7s1eEK7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2532,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 56929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_018SVSX8T52AvzEwCUJ4ecdf`</summary>

```json
{
  "query": "TRANSIC \"sim-to-real policy transfer\" \"online correction\" binary gate 2024 arXiv 2405.10315"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "29b50568-2179-4d94-bce1-b35ad58101cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WeiecS4NRprxWD7s1eEK7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2532,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 56929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HiPTQcYsDNFABbCR1iU4DV`</summary>

```json
{
  "query": "PLD \"self-improving VLA\" \"residual RL\" bounded corrections distillation 2026 arXiv 2511.00091"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "cfa21336-02f8-4981-b9ae-f550232f5b87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WeiecS4NRprxWD7s1eEK7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2532,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 56929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
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

_source line 66_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WHSKFPunPGLyHijE6kUmS9`</summary>

```json
{
  "query": "DRC \"decaying relative correction\" policy refinement exponential decay 2025 arXiv 2503.15368"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "f5dc8d97-af9f-4748-9bcd-41b6297bee84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WeiecS4NRprxWD7s1eEK7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2532,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 56929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
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

_source line 67 · 2026-05-15T20:48:31.025Z_

<details><summary>↩ Tool result · `toolu_01SYdW1QVj22Gbw7UMs4mFW6`</summary>

```text
Web search results for query: "ReconVLA arXiv 2604.16677 action selection modification "failure-aware" mechanism what does it do with actions"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=263&show=2000"},{"title":"[2604.15771] Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing","url":"https://arxiv.org/abs/2604.15771"},{"title":"Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming","url":"https://arxiv.org/html/2604.05595v1"},{"title":"Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection","url":"https://arxiv.org/html/2604.13942v1"},{"title":"Machine Learning Jul 2025","url":"https://www.arxiv.org/list/cs.LG/2025-07?skip=675&show=1000"},{"title":"Failure Makes the Agent Stronger: Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions","url":"https://arxiv.org/html/2509.18847v2"},{"title":"1. Introduction","url":"https://arxiv.org/html/2604.16339"}]

Based on the search results, I found information about the ReconVLA paper (arXiv 2604.16677) and its failure-aware mechanism.

The failure-aware mechanism in ReconVLA uses an SMD-based detector that monitors latent state distributions to identify out-of-distribution (OOD) or failure-prone conditions. 

More specifically, this failure detection mechanism works by extending conformal prediction to the robot state space to detect outliers or unsafe states before failures occur. The framework incorporates conformal quantile regression (CQR)-based uncertainty quantification into the VLA's action generation process and its state monitoring, allowing the robot to detect when it "doesn't know" or is likely to fail before a catastrophe occurs.

In terms of what it does with actions, ReconVLA includes a CQR-based estimator that computes calibrated action-level uncertainty to guide reliable action selection under generative variability. Together, these modules enable robust action selection and proactive failure detection during deployment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "c6f0b9b4-e461-4334-a2f3-6d2e2370fe78",
  "tool_use_result": {
    "query": "ReconVLA arXiv 2604.16677 action selection modification \"failure-aware\" mechanism what does it do with actions",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M4R4XhHJWfuFdL4MYGVfYF",
        "content": [
          {
            "title": "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control",
            "url": "https://arxiv.org/html/2604.16677v1"
          },
          {
            "title": "ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/html/2508.10333v1"
          },
          {
            "title": "[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/abs/2508.10333"
          },
          {
            "title": "Computer Science",
            "url": "https://arxiv.org/list/cs/pastweek?skip=263&show=2000"
          },
          {
            "title": "[2604.15771] Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing",
            "url": "https://arxiv.org/abs/2604.15771"
          },
          {
            "title": "Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming",
            "url": "https://arxiv.org/html/2604.05595v1"
          },
          {
            "title": "Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection",
            "url": "https://arxiv.org/html/2604.13942v1"
          },
          {
            "title": "Machine Learning Jul 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-07?skip=675&show=1000"
          },
          {
            "title": "Failure Makes the Agent Stronger: Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions",
            "url": "https://arxiv.org/html/2509.18847v2"
          },
          {
            "title": "1. Introduction",
            "url": "https://arxiv.org/html/2604.16339"
          }
        ]
      },
      "Based on the search results, I found information about the ReconVLA paper (arXiv 2604.16677) and its failure-aware mechanism.\n\nThe failure-aware mechanism in ReconVLA uses an SMD-based detector that monitors latent state distributions to identify out-of-distribution (OOD) or failure-prone conditions. \n\nMore specifically, this failure detection mechanism works by extending conformal prediction to the robot state space to detect outliers or unsafe states before failures occur. The framework incorporates conformal quantile regression (CQR)-based uncertainty quantification into the VLA's action generation process and its state monitoring, allowing the robot to detect when it \"doesn't know\" or is likely to fail before a catastrophe occurs.\n\nIn terms of what it does with actions, ReconVLA includes a CQR-based estimator that computes calibrated action-level uncertainty to guide reliable action selection under generative variability. Together, these modules enable robust action selection and proactive failure detection during deployment."
    ],
    "durationSeconds": 6.300135190000001
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T20:48:31.574Z_

<details><summary>↩ Tool result · `toolu_01HiPTQcYsDNFABbCR1iU4DV`</summary>

```text
Web search results for query: "PLD "self-improving VLA" "residual RL" bounded corrections distillation 2026 arXiv 2511.00091"

Links: [{"title":"PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)","url":"https://wenlixiao.com/self-improve-VLA-PLD"}]

Based on the search results, I found the paper you're looking for:

**PLD (Probe, Learn, Distill)** is a three-stage plug-and-play framework that improves VLAs through residual reinforcement learning (RL) and distribution-aware data collection.

The framework works as follows:

- **Stage 1 (specialist acquisition)**: Freeze the VLA backbone and train lightweight residual actors via off-policy RL. These specialists take over in states where the base policy fails, thereby probing failure regions of the VLA generalist.

- **Stage 2 (data collection)**: Employ a hybrid rollout scheme that biases residual interventions toward states frequently visited by the base policy, aligning collected trajectories with the generalist's deployment distribution while capturing recovery behaviors.

- **Stage 3 (fine-tuning)**: Curated trajectories are distilled back into the generalist with standard SFT, applicable to both flow-matching and autoregressive heads.

The framework achieves a near-saturated 99% task success rate on the LIBERO benchmark, delivers over 50% performance gains in SimplerEnv, and demonstrates a 100% success rate on real-world Franka arm and YAM arm dexterous manipulation tasks.

This is the arXiv paper 2511.00091 (also accepted to ICLR 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "06d44bc3-4d1d-484f-9502-f78e02ceb247",
  "tool_use_result": {
    "query": "PLD \"self-improving VLA\" \"residual RL\" bounded corrections distillation 2026 arXiv 2511.00091",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GePjKtfEWwiYT6huuVtodE",
        "content": [
          {
            "title": "PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)",
            "url": "https://wenlixiao.com/self-improve-VLA-PLD"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**PLD (Probe, Learn, Distill)** is a three-stage plug-and-play framework that improves VLAs through residual reinforcement learning (RL) and distribution-aware data collection.\n\nThe framework works as follows:\n\n- **Stage 1 (specialist acquisition)**: Freeze the VLA backbone and train lightweight residual actors via off-policy RL. These specialists take over in states where the base policy fails, thereby probing failure regions of the VLA generalist.\n\n- **Stage 2 (data collection)**: Employ a hybrid rollout scheme that biases residual interventions toward states frequently visited by the base policy, aligning collected trajectories with the generalist's deployment distribution while capturing recovery behaviors.\n\n- **Stage 3 (fine-tuning)**: Curated trajectories are distilled back into the generalist with standard SFT, applicable to both flow-matching and autoregressive heads.\n\nThe framework achieves a near-saturated 99% task success rate on the LIBERO benchmark, delivers over 50% performance gains in SimplerEnv, and demonstrates a 100% success rate on real-world Franka arm and YAM arm dexterous manipulation tasks.\n\nThis is the arXiv paper 2511.00091 (also accepted to ICLR 2026)."
    ],
    "durationSeconds": 4.991256198999996
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-15T20:48:34.671Z_

<details><summary>↩ Tool result · `toolu_01WHSKFPunPGLyHijE6kUmS9`</summary>

```text
Web search results for query: "DRC "decaying relative correction" policy refinement exponential decay 2025 arXiv 2503.15368"

Links: [{"title":"[2503.15368] Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation","url":"https://arxiv.org/abs/2503.15368"},{"title":"Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation","url":"https://arxiv.org/html/2503.15368"}]

I found the paper! Here's what the search returned:

The Decaying Relative Correction (DRC) is a correction method based upon the spatial offset vector provided by the expert and exists temporarily, reducing the intervention steps required by an expert.

The DRC method is designed for correction of robotic manipulation and is made possible by a use of an 8 degree of freedom (DoF) teleoperation system and cable driven robot. The relative correction motion provided by the expert's teleoperation is a vector of correction which is only temporary, and stays valid for only a period of time, disappearing with a given decay rate.

The results demonstrate that DRC reduces the required expert intervention rate by 30% compared to a standard absolute corrective method. Integrating DRC within an online imitation learning framework rapidly increases the success rate of manipulation tasks such as raspberry harvesting and cloth wiping.

The paper was published on March 19, 2025, with the arXiv identifier 2503.15368.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "7179de14-7df6-41ed-acee-7ffc9216386d",
  "tool_use_result": {
    "query": "DRC \"decaying relative correction\" policy refinement exponential decay 2025 arXiv 2503.15368",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JT1dQHj5smCEFiouWEMrv3",
        "content": [
          {
            "title": "[2503.15368] Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation",
            "url": "https://arxiv.org/abs/2503.15368"
          },
          {
            "title": "Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation",
            "url": "https://arxiv.org/html/2503.15368"
          }
        ]
      },
      "I found the paper! Here's what the search returned:\n\nThe Decaying Relative Correction (DRC) is a correction method based upon the spatial offset vector provided by the expert and exists temporarily, reducing the intervention steps required by an expert.\n\nThe DRC method is designed for correction of robotic manipulation and is made possible by a use of an 8 degree of freedom (DoF) teleoperation system and cable driven robot. The relative correction motion provided by the expert's teleoperation is a vector of correction which is only temporary, and stays valid for only a period of time, disappearing with a given decay rate.\n\nThe results demonstrate that DRC reduces the required expert intervention rate by 30% compared to a standard absolute corrective method. Integrating DRC within an online imitation learning framework rapidly increases the success rate of manipulation tasks such as raspberry harvesting and cloth wiping.\n\nThe paper was published on March 19, 2025, with the arXiv identifier 2503.15368."
    ],
    "durationSeconds": 7.8172783950000015
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T20:48:35.005Z_

<details><summary>↩ Tool result · `toolu_018SVSX8T52AvzEwCUJ4ecdf`</summary>

```text
Web search results for query: "TRANSIC "sim-to-real policy transfer" "online correction" binary gate 2024 arXiv 2405.10315"

Links: [{"title":"[2405.10315] TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://arxiv.org/abs/2405.10315"},{"title":"Transic: Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://arxiv.org/html/2405.10315v2"},{"title":"(PDF) TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://www.researchgate.net/publication/380635321_TRANSIC_Sim-to-Real_Policy_Transfer_by_Learning_from_Online_Correction"},{"title":"TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction | alphaXiv","url":"https://www.alphaxiv.org/overview/2405.10315v3"},{"title":"(PDF) TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction (2024) | Yunfan Jiang | 10 Citations","url":"https://scispace.com/papers/transic-sim-to-real-policy-transfer-by-learning-from-online-2heee0h3xd"},{"title":"TRANSIC | Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://transic-robot.github.io/"},{"title":"TRANSIC: Sim-to-Real Policy Transfer by Learning ...","url":"https://arxiv-sanity-lite.com/?rank=pid&pid=2405.10315"},{"title":"GitHub - transic-robot/transic · GitHub","url":"https://github.com/transic-robot/transic"},{"title":"TRANSIC: Human-in-the-Loop Sim-to-Real Transfer","url":"https://www.emergentmind.com/papers/2405.10315"},{"title":"transic-robot/data · Datasets at Hugging Face","url":"https://huggingface.co/datasets/transic-robot/data"}]

I found comprehensive information about TRANSIC (arXiv 2405.10315). Here's a summary of what the research presents:

## Overview

TRANSIC is a data-driven approach to enable successful sim-to-real transfer based on a human-in-the-loop framework that allows humans to augment simulation policies to overcome various unmodeled sim-to-real gaps holistically through intervention and online correction.

## Key Approach

Residual policies can be learned from human corrections and integrated with simulation policies for autonomous execution. The method specifically uses a gated residual policy learned from a small amount of human correction data to address the challenge of avoiding catastrophic forgetting of the base policy.

## Technical Innovation

A notable feature of TRANSIC is its use of gated residual policies. Transic bypasses catastrophic forgetting issues by learning gated residual policies only from human correction. This design choice allows the system to scale effectively with human data—when increasing the dataset size from 25% to 75% of the full size, Transic improves on average by 42%, whereas IWR (a baseline) only achieves a 23% relative improvement.

## Applications

The approach can achieve successful sim-to-real transfer in complex and contact-rich manipulation tasks such as furniture assembly.

The paper was submitted on May 16, 2024, and last revised October 14, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "fc2076f3-ced2-494c-bc8a-367fcaffa698",
  "tool_use_result": {
    "query": "TRANSIC \"sim-to-real policy transfer\" \"online correction\" binary gate 2024 arXiv 2405.10315",
    "results": [
      {
        "tool_use_id": "srvtoolu_0117vAATsDEHUHrpR2Yfe3gY",
        "content": [
          {
            "title": "[2405.10315] TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction",
            "url": "https://arxiv.org/abs/2405.10315"
          },
          {
            "title": "Transic: Sim-to-Real Policy Transfer by Learning from Online Correction",
            "url": "https://arxiv.org/html/2405.10315v2"
          },
          {
            "title": "(PDF) TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction",
            "url": "https://www.researchgate.net/publication/380635321_TRANSIC_Sim-to-Real_Policy_Transfer_by_Learning_from_Online_Correction"
          },
          {
            "title": "TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2405.10315v3"
          },
          {
            "title": "(PDF) TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction (2024) | Yunfan Jiang | 10 Citations",
            "url": "https://scispace.com/papers/transic-sim-to-real-policy-transfer-by-learning-from-online-2heee0h3xd"
          },
          {
            "title": "TRANSIC | Sim-to-Real Policy Transfer by Learning from Online Correction",
            "url": "https://transic-robot.github.io/"
          },
          {
            "title": "TRANSIC: Sim-to-Real Policy Transfer by Learning ...",
            "url": "https://arxiv-sanity-lite.com/?rank=pid&pid=2405.10315"
          },
          {
            "title": "GitHub - transic-robot/transic · GitHub",
            "url": "https://github.com/transic-robot/transic"
          },
          {
            "title": "TRANSIC: Human-in-the-Loop Sim-to-Real Transfer",
            "url": "https://www.emergentmind.com/papers/2405.10315"
          },
          {
            "title": "transic-robot/data · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/transic-robot/data"
          }
        ]
      },
      "I found comprehensive information about TRANSIC (arXiv 2405.10315). Here's a summary of what the research presents:\n\n## Overview\n\nTRANSIC is a data-driven approach to enable successful sim-to-real transfer based on a human-in-the-loop framework that allows humans to augment simulation policies to overcome various unmodeled sim-to-real gaps holistically through intervention and online correction.\n\n## Key Approach\n\nResidual policies can be learned from human corrections and integrated with simulation policies for autonomous execution. The method specifically uses a gated residual policy learned from a small amount of human correction data to address the challenge of avoiding catastrophic forgetting of the base policy.\n\n## Technical Innovation\n\nA notable feature of TRANSIC is its use of gated residual policies. Transic bypasses catastrophic forgetting issues by learning gated residual policies only from human correction. This design choice allows the system to scale effectively with human data—when increasing the dataset size from 25% to 75% of the full size, Transic improves on average by 42%, whereas IWR (a baseline) only achieves a 23% relative improvement.\n\n## Applications\n\nThe approach can achieve successful sim-to-real transfer in complex and contact-rich manipulation tasks such as furniture assembly.\n\nThe paper was submitted on May 16, 2024, and last revised October 14, 2024."
    ],
    "durationSeconds": 9.348288387000007
  }
}
```

</details>

---

### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the findings so far:

1. **ReconVLA (chen2026reconvla)**: The search reveals that ReconVLA actually does include "reliable action selection" — "a CQR-based estimator that computes calibrated action-level uncertainty to guide reliable action selection under generative variability." So it's not purely a UQ framework that "does not modify the VLA's actions" as stated in the related work. It does action selection guided by uncertainty. This is a potential misattribution.

The current text in related_work.tex says: "providing a principled uncertainty quantification framework that operates without retraining but does not modify the VLA's actions."
 
I need to correct this characterization. ReconVLA uses CQR-based uncertainty to actively select among generated actions, which means it does modify the action distribution through selection. The description of it as a framework that "does not modify the VLA's actions" is inaccurate—it's actually a UQ-guided approach that performs action selection based on uncertainty estimates, so I should revise the related work section to reflect this distinction properly. I need to correct my understanding of ReconVLA's positioning. It's not just a UQ framework that visualizes uncertainty—it actively uses uncertainty to guide action selection through conformal quantile regression and Mahalanobis distance-based OOD detection. The current description undersells this by saying it "does not modify the VLA's actions," which is factually wrong since it does perform uncertainty-guided action selection. I should reposition it as a UQ-guided approach that influences action selection, distinguishing it from ACR-VLA's sample-then-correct strategy.

Now looking at TRANSIC, which uses a learned binary gate to decide whether to apply sim-to-real residuals based on the current state...

the search results mention "gated residual policies" trained on human correction data, and note that ungated versions suffer from catastrophic forgetting. The "binary gate" terminology seems close enough to "gated" that I won't flag this as an error, though the exact mechanism could use verification.

For PLD, the search confirms the approach of freezing the VLA backbone and training lightweight residual actors via off-policy RL with bounded corrections, then distilling improved trajectories back—this matches the paper's description well.

With DRC, the search describes correction motions from expert teleoperation that decay over time, which aligns with the paper's framing of exponential decay on correction events, though there's a subtle distinction between expert-provided corrections versus policy-generated ones that's worth noting.

A2C2 is confirmed as a lightweight real-time correction head that preserves base model competence while restoring closed-loop responsiveness, and the paper's characterization of it applying corrections unconditionally without a selection stage is accurate.

Now I need to verify the remaining methods—DiU, SAFE, Braun CGS, and the conformal/uncertainty quantification papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "3ef27ec4-a050-4569-8203-60f6de44de95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNSLBYqmuqkYmHFot3WrWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 58874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6039
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

Key finding: ReconVLA actually includes uncertainty-guided action selection, not just UQ. Let me verify more papers and check DiU/SAFE.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "e1513495-a24f-4cfd-9c19-03df5bb5a38f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNSLBYqmuqkYmHFot3WrWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 58874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6039
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NvyhpPedr7EXP8gLYvLFt9`</summary>

```json
{
  "query": "DiU \"divergence is uncertainty\" flow matching posterior covariance velocity field divergence 2026 arXiv 2605.00941"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "6a212d66-9f2f-4a7d-86dd-7de4e859f7ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNSLBYqmuqkYmHFot3WrWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 58874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6039
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

_source line 74_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015SV74a1tU3sV4CCtMeHTUh`</summary>

```json
{
  "query": "SAFE \"multitask failure detection\" VLA conformal prediction 2025 NeurIPS arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "2d317bf0-0234-47bc-a92b-3b85f02a71de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNSLBYqmuqkYmHFot3WrWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 58874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6039
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U7WYJMxYBf6zqdMCrYaqB8`</summary>

```json
{
  "query": "Zollo Zemel \"confidence calibration\" VLA \"prompt ensembles\" \"Platt scaling\" 2025 arXiv 2507.17383"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "67d8335b-116f-4d1b-a6c3-77d69f536a09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNSLBYqmuqkYmHFot3WrWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 58874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6039
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

_source line 76_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0173ku4Z5tdnjSxhG7NQamEw`</summary>

```json
{
  "query": "Braun Berta Jordan Bach \"conformalized gaussian scoring\" multivariate standardized residuals conformal prediction 2025 arXiv 2507.20941"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "311a6646-247e-479f-95e5-9582f7d10343",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNSLBYqmuqkYmHFot3WrWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 58874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6039
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

_source line 77 · 2026-05-15T20:49:16.250Z_

<details><summary>↩ Tool result · `toolu_015SV74a1tU3sV4CCtMeHTUh`</summary>

```text
Web search results for query: "SAFE "multitask failure detection" VLA conformal prediction 2025 NeurIPS arXiv"

Links: [{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://vla-safe.github.io/"},{"title":"[2506.09937] SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.09937"},{"title":"GitHub - vla-safe/SAFE: This is the official repository for \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\" (NeurIPS 2025) · GitHub","url":"https://github.com/vla-safe/SAFE"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.09937v2"},{"title":"NeurIPS Poster SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://neurips.cc/virtual/2025/poster/117510"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=XPyAukgsFf"},{"title":"[PDF] SAFE: Multitask Failure Detection for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SAFE:-Multitask-Failure-Detection-for-Models-Gu-Ju/8165f26c174bd327506242ee898cf18a3abe61cf"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models | Toyota Research Institute","url":"https://www.tri.global/research/safe-multitask-failure-detection-vision-language-action-models"},{"title":"Paper page - SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.09937"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://neurips.cc/media/neurips-2025/Slides/117510.pdf"}]

Based on the search results, I found comprehensive information about SAFE:

## SAFE: Multitask Failure Detection for Vision-Language-Action Models

SAFE is a failure detector for generalist robot policies such as VLAs, and it was published as a NeurIPS 2025 poster.

### Key Contributions

The paper introduces the multitask failure detection problem and proposes SAFE as a failure detector for generalist robot policies such as VLAs. SAFE analysis found that VLAs have sufficient high-level knowledge about task success and failure, which is generic across different tasks.

### Technical Approach

SAFE learns from VLA internal features and predicts a single scalar indicating the likelihood of task failure. The methodology has three main components: SAFE extracts the latent feature from the last layer of a VLA model, sequentially processes the latent feature and predicts a failure score using an MLP or an LSTM backbone, and determines a time-varying threshold using functional conformal prediction (CP) on a hold-out calibration set.

### Evaluation and Performance

SAFE was tested on OpenVLA, π0, and π0-FAST in both simulated and real-world environments. SAFE achieves state-of-the-art failure detection performance and the best trade-off between accuracy and detection time using conformal prediction.

### Publication Details

The paper was published on arXiv as preprint arXiv:2506.09937 in 2025, and the official GitHub repository indicates it is the implementation for "SAFE: Multitask Failure Detection for Vision-Language-Action Models" (NeurIPS 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "ce0022aa-0131-4fda-88c4-7f463ceb81aa",
  "tool_use_result": {
    "query": "SAFE \"multitask failure detection\" VLA conformal prediction 2025 NeurIPS arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KPMe5ghtMDUQZhjpKEAtZC",
        "content": [
          {
            "title": "SAFE: Multitask Failure Detection for Vision-Language-Action Models",
            "url": "https://vla-safe.github.io/"
          },
          {
            "title": "[2506.09937] SAFE: Multitask Failure Detection for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2506.09937"
          },
          {
            "title": "GitHub - vla-safe/SAFE: This is the official repository for \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\" (NeurIPS 2025) · GitHub",
            "url": "https://github.com/vla-safe/SAFE"
          },
          {
            "title": "SAFE: Multitask Failure Detection for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2506.09937v2"
          },
          {
            "title": "NeurIPS Poster SAFE: Multitask Failure Detection for Vision-Language-Action Models",
            "url": "https://neurips.cc/virtual/2025/poster/117510"
          },
          {
            "title": "SAFE: Multitask Failure Detection for Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=XPyAukgsFf"
          },
          {
            "title": "[PDF] SAFE: Multitask Failure Detection for Vision-Language-Action Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/SAFE:-Multitask-Failure-Detection-for-Models-Gu-Ju/8165f26c174bd327506242ee898cf18a3abe61cf"
          },
          {
            "title": "SAFE: Multitask Failure Detection for Vision-Language-Action Models | Toyota Research Institute",
            "url": "https://www.tri.global/research/safe-multitask-failure-detection-vision-language-action-models"
          },
          {
            "title": "Paper page - SAFE: Multitask Failure Detection for Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2506.09937"
          },
          {
            "title": "SAFE: Multitask Failure Detection for Vision-Language-Action Models",
            "url": "https://neurips.cc/media/neurips-2025/Slides/117510.pdf"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about SAFE:\n\n## SAFE: Multitask Failure Detection for Vision-Language-Action Models\n\nSAFE is a failure detector for generalist robot policies such as VLAs, and it was published as a NeurIPS 2025 poster.\n\n### Key Contributions\n\nThe paper introduces the multitask failure detection problem and proposes SAFE as a failure detector for generalist robot policies such as VLAs. SAFE analysis found that VLAs have sufficient high-level knowledge about task success and failure, which is generic across different tasks.\n\n### Technical Approach\n\nSAFE learns from VLA internal features and predicts a single scalar indicating the likelihood of task failure. The methodology has three main components: SAFE extracts the latent feature from the last layer of a VLA model, sequentially processes the latent feature and predicts a failure score using an MLP or an LSTM backbone, and determines a time-varying threshold using functional conformal prediction (CP) on a hold-out calibration set.\n\n### Evaluation and Performance\n\nSAFE was tested on OpenVLA, π0, and π0-FAST in both simulated and real-world environments. SAFE achieves state-of-the-art failure detection performance and the best trade-off between accuracy and detection time using conformal prediction.\n\n### Publication Details\n\nThe paper was published on arXiv as preprint arXiv:2506.09937 in 2025, and the official GitHub repository indicates it is the implementation for \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\" (NeurIPS 2025)."
    ],
    "durationSeconds": 7.111017713999987
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-15T20:49:17.107Z_

<details><summary>↩ Tool result · `toolu_01NvyhpPedr7EXP8gLYvLFt9`</summary>

```text
Web search results for query: "DiU "divergence is uncertainty" flow matching posterior covariance velocity field divergence 2026 arXiv 2605.00941"

Links: [{"title":"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching","url":"https://arxiv.org/html/2605.00941"},{"title":"[2605.00941] Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching","url":"https://arxiv.org/abs/2605.00941"},{"title":"Discrete Flow Matching: Convergence Guarantees Under Minimal Assumptions","url":"https://arxiv.org/html/2605.08882"},{"title":"GitHub - iszhanjiawei/flow_matching_arxiv_daily · GitHub","url":"https://github.com/iszhanjiawei/flow_matching_arxiv_daily"},{"title":"[2511.05480] On Flow Matching KL Divergence","url":"https://arxiv.org/abs/2511.05480"},{"title":"[2605.08882] Discrete Flow Matching: Convergence Guarantees Under Minimal Assumptions","url":"https://arxiv.org/abs/2605.08882"},{"title":"Training-Free Refinement of Flow Matching with Divergence-based Sampling","url":"https://arxiv.org/html/2604.04646v1"},{"title":"How and Why: Taming Flow Matching for Unsupervised Anomaly Detection and Localization","url":"https://arxiv.org/html/2508.05461v1"},{"title":"[2604.04646v1] Training-Free Refinement of Flow Matching with Divergence-based Sampling","url":"https://arxiv.org/abs/2604.04646v1"},{"title":"Last Update: Novermber 7, 2025 On Flow Matching KL Divergence Maojiang Su†∗1","url":"https://arxiv.org/pdf/2511.05480"}]

I found the paper you're looking for! Here's information about arXiv 2605.00941:

## "Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching"

The paper was submitted on May 1, 2026 by Jiarui Xing and 2 other authors.

**Main Contribution:**

The paper proves that for any pre-trained flow matching velocity field, the trace of the posterior covariance over the clean data given the current state equals, in closed form, the divergence of the velocity field, up to a known time-dependent prefactor and an additive constant. This is called the divergence-uncertainty identity for flow matching.

**Key Advantages:**

- The identity is exact and post-hoc, making it computable on any pre-trained flow matching model with no retraining and no architectural modification
- For one-step generators such as MeanFlow, the same identity yields exact end-to-end generation uncertainty in a single forward pass, eliminating multi-step variance propagation required by all prior methods
- The divergence can be efficiently estimated via Hutchinson's trace estimator using a handful of Jacobian-vector products

**Experimental Results:**

Experiments on MNIST confirm that the resulting per-pixel uncertainty maps are semantically meaningful, concentrating on digit boundaries where inter-sample variation is highest, and that the scalar uncertainty score tracks actual prediction error, all at roughly 10,000× less total compute than ensembling or Monte Carlo dropout.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "229dc799-3c14-4326-be95-cb01cb59cf6c",
  "tool_use_result": {
    "query": "DiU \"divergence is uncertainty\" flow matching posterior covariance velocity field divergence 2026 arXiv 2605.00941",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Dv9BF39h8KFSt9e5pLdzoz",
        "content": [
          {
            "title": "Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching",
            "url": "https://arxiv.org/html/2605.00941"
          },
          {
            "title": "[2605.00941] Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching",
            "url": "https://arxiv.org/abs/2605.00941"
          },
          {
            "title": "Discrete Flow Matching: Convergence Guarantees Under Minimal Assumptions",
            "url": "https://arxiv.org/html/2605.08882"
          },
          {
            "title": "GitHub - iszhanjiawei/flow_matching_arxiv_daily · GitHub",
            "url": "https://github.com/iszhanjiawei/flow_matching_arxiv_daily"
          },
          {
            "title": "[2511.05480] On Flow Matching KL Divergence",
            "url": "https://arxiv.org/abs/2511.05480"
          },
          {
            "title": "[2605.08882] Discrete Flow Matching: Convergence Guarantees Under Minimal Assumptions",
            "url": "https://arxiv.org/abs/2605.08882"
          },
          {
            "title": "Training-Free Refinement of Flow Matching with Divergence-based Sampling",
            "url": "https://arxiv.org/html/2604.04646v1"
          },
          {
            "title": "How and Why: Taming Flow Matching for Unsupervised Anomaly Detection and Localization",
            "url": "https://arxiv.org/html/2508.05461v1"
          },
          {
            "title": "[2604.04646v1] Training-Free Refinement of Flow Matching with Divergence-based Sampling",
            "url": "https://arxiv.org/abs/2604.04646v1"
          },
          {
            "title": "Last Update: Novermber 7, 2025 On Flow Matching KL Divergence Maojiang Su†∗1",
            "url": "https://arxiv.org/pdf/2511.05480"
          }
        ]
      },
      "I found the paper you're looking for! Here's information about arXiv 2605.00941:\n\n## \"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\"\n\nThe paper was submitted on May 1, 2026 by Jiarui Xing and 2 other authors.\n\n**Main Contribution:**\n\nThe paper proves that for any pre-trained flow matching velocity field, the trace of the posterior covariance over the clean data given the current state equals, in closed form, the divergence of the velocity field, up to a known time-dependent prefactor and an additive constant. This is called the divergence-uncertainty identity for flow matching.\n\n**Key Advantages:**\n\n- The identity is exact and post-hoc, making it computable on any pre-trained flow matching model with no retraining and no architectural modification\n- For one-step generators such as MeanFlow, the same identity yields exact end-to-end generation uncertainty in a single forward pass, eliminating multi-step variance propagation required by all prior methods\n- The divergence can be efficiently estimated via Hutchinson's trace estimator using a handful of Jacobian-vector products\n\n**Experimental Results:**\n\nExperiments on MNIST confirm that the resulting per-pixel uncertainty maps are semantically meaningful, concentrating on digit boundaries where inter-sample variation is highest, and that the scalar uncertainty score tracks actual prediction error, all at roughly 10,000× less total compute than ensembling or Monte Carlo dropout."
    ],
    "durationSeconds": 7.975087113999995
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-15T20:49:17.212Z_

<details><summary>↩ Tool result · `toolu_01U7WYJMxYBf6zqdMCrYaqB8`</summary>

```text
Web search results for query: "Zollo Zemel "confidence calibration" VLA "prompt ensembles" "Platt scaling" 2025 arXiv 2507.17383"

Links: [{"title":"[2507.17383] Confidence Calibration in Vision-Language-Action Models","url":"https://arxiv.org/abs/2507.17383"},{"title":"Confidence Calibration in Vision-Language-Action Models","url":"https://arxiv.org/html/2507.17383"},{"title":"Confidence Calibration in Vision-Language-Action Models Thomas Zollo","url":"https://arxiv.org/pdf/2507.17383"},{"title":"(PDF) Confidence Calibration in Vision-Language-Action Models","url":"https://www.researchgate.net/publication/393966020_Confidence_Calibration_in_Vision-Language-Action_Models"},{"title":"Confidence Calibration in Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=aiPC7jAd2f"},{"title":"[2410.05407v1] Improving Predictor Reliability with Selective Recalibration","url":"https://arxiv.org/abs/2410.05407v1"},{"title":"[2604.19444] Unsupervised Confidence Calibration for Reasoning LLMs from a Single Generation","url":"https://arxiv.org/abs/2604.19444"},{"title":"[2507.05220] QuEst: Enhancing Estimates of Quantile-Based Distributional Measures Using Model Predictions","url":"https://arxiv.org/abs/2507.05220"},{"title":"[1706.04599] On Calibration of Modern Neural Networks","url":"https://arxiv.org/abs/1706.04599"},{"title":"Calibration Meets Reality: Making Machine Learning Predictions Trustworthy","url":"https://arxiv.org/html/2509.23665v1"}]

I found the paper you're looking for! Here are the key findings:

## Paper Summary

The paper presents a first-of-its-kind study of confidence calibration in vision-language-action (VLA) foundation models, which map visual observations and natural language instructions to low-level robot motor commands.

## Main Contributions

The researchers establish a confidence baseline for VLAs, examine how task success relates to calibration error and how calibration evolves over time, and introduce two lightweight techniques to remedy the miscalibration they observe: prompt ensembles and action-wise Platt scaling.

## Key Motivation

Since VLAs are designed for closed-loop interaction with the physical world, knowing when and how strongly to trust their actions is critical. In safety-critical scenarios, if the policy can accurately express uncertainty, then costly or dangerous accidents can be avoided, such as by refining the instruction or deferring the task to a human.

## Experimental Approach

The experiments use models derived from the OpenVLA model, fine-tuned on 3 different task suites from the LIBERO benchmark: Spatial, Object, and Goal.

The paper (arXiv 2507.17383) was authored by Thomas Zollo and Richard Zemel from Columbia University, with the latest version released on December 22, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "fa430a06-308e-42d9-ab8c-404bb4cbd53b",
  "tool_use_result": {
    "query": "Zollo Zemel \"confidence calibration\" VLA \"prompt ensembles\" \"Platt scaling\" 2025 arXiv 2507.17383",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XCCUuyaHAmztqA7wAFs8Rf",
        "content": [
          {
            "title": "[2507.17383] Confidence Calibration in Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2507.17383"
          },
          {
            "title": "Confidence Calibration in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2507.17383"
          },
          {
            "title": "Confidence Calibration in Vision-Language-Action Models Thomas Zollo",
            "url": "https://arxiv.org/pdf/2507.17383"
          },
          {
            "title": "(PDF) Confidence Calibration in Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/393966020_Confidence_Calibration_in_Vision-Language-Action_Models"
          },
          {
            "title": "Confidence Calibration in Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=aiPC7jAd2f"
          },
          {
            "title": "[2410.05407v1] Improving Predictor Reliability with Selective Recalibration",
            "url": "https://arxiv.org/abs/2410.05407v1"
          },
          {
            "title": "[2604.19444] Unsupervised Confidence Calibration for Reasoning LLMs from a Single Generation",
            "url": "https://arxiv.org/abs/2604.19444"
          },
          {
            "title": "[2507.05220] QuEst: Enhancing Estimates of Quantile-Based Distributional Measures Using Model Predictions",
            "url": "https://arxiv.org/abs/2507.05220"
          },
          {
            "title": "[1706.04599] On Calibration of Modern Neural Networks",
            "url": "https://arxiv.org/abs/1706.04599"
          },
          {
            "title": "Calibration Meets Reality: Making Machine Learning Predictions Trustworthy",
            "url": "https://arxiv.org/html/2509.23665v1"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key findings:\n\n## Paper Summary\n\nThe paper presents a first-of-its-kind study of confidence calibration in vision-language-action (VLA) foundation models, which map visual observations and natural language instructions to low-level robot motor commands.\n\n## Main Contributions\n\nThe researchers establish a confidence baseline for VLAs, examine how task success relates to calibration error and how calibration evolves over time, and introduce two lightweight techniques to remedy the miscalibration they observe: prompt ensembles and action-wise Platt scaling.\n\n## Key Motivation\n\nSince VLAs are designed for closed-loop interaction with the physical world, knowing when and how strongly to trust their actions is critical. In safety-critical scenarios, if the policy can accurately express uncertainty, then costly or dangerous accidents can be avoided, such as by refining the instruction or deferring the task to a human.\n\n## Experimental Approach\n\nThe experiments use models derived from the OpenVLA model, fine-tuned on 3 different task suites from the LIBERO benchmark: Spatial, Object, and Goal.\n\nThe paper (arXiv 2507.17383) was authored by Thomas Zollo and Richard Zemel from Columbia University, with the latest version released on December 22, 2025."
    ],
    "durationSeconds": 7.342015419999981
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T20:49:18.077Z_

<details><summary>↩ Tool result · `toolu_0173ku4Z5tdnjSxhG7NQamEw`</summary>

```text
Web search results for query: "Braun Berta Jordan Bach "conformalized gaussian scoring" multivariate standardized residuals conformal prediction 2025 arXiv 2507.20941"

Links: [{"title":"[2507.20941] Multivariate Standardized Residuals for Conformal Prediction","url":"https://arxiv.org/abs/2507.20941"},{"title":"(PDF) Multivariate Conformal Prediction via Conformalized Gaussian Scoring","url":"https://www.researchgate.net/publication/394081259_Multivariate_Conformal_Prediction_via_Conformalized_Gaussian_Scoring"},{"title":"Multivariate Conformal Prediction via Conformalized Gaussian Scoring","url":"https://arxiv.org/pdf/2507.20941"},{"title":"[PDF] Multivariate Conformal Prediction via Conformalized Gaussian Scoring | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multivariate-Conformal-Prediction-via-Conformalized-Braun-Berta/eb97eda6c4159d62c1fd5d2ca6404b323e44123c"},{"title":"Multivariate Standardized Residuals for Conformal Prediction","url":"https://arxiv.org/html/2507.20941"},{"title":"Multivariate Conformal Prediction via Conformalized Gaussian ...","url":"https://ribbitribbit.co/paper/arxiv.2507.20941-Multivariate-Conformal-Prediction-via-Conformalized-Gaussian-Scoring"},{"title":"Publications - People @EECS","url":"https://people.eecs.berkeley.edu/~jordan/publications.html"},{"title":"Methodology Jul 2025","url":"https://www.arxiv.org/list/stat.ME/2025-07?skip=350&show=1000"},{"title":"Statistics","url":"https://www.arxiv.org/list/stat/recent?skip=111&show=25"},{"title":"Eugene Berta","url":"https://eugeneberta.github.io/"}]

I found the paper you're looking for! Here are the search results for arXiv paper 2507.20941:

## Paper Information

The paper is titled "Multivariate Standardized Residuals for Conformal Prediction" by Sacha Braun, Eugène Berta, Michael I. Jordan, and Francis Bach.

## Main Contribution

The paper proposes a natural extension of normalization to the multivariate setting, effectively whitening the residuals to decouple output correlations and standardize local variance.

## Key Results

The authors derive a sufficient condition characterizing a broad class of distributions for which standardized residuals yield asymptotic conditional coverage. They demonstrate that using the Mahalanobis distance induced by a learned local covariance as a non-conformity score provides a closed-form, computationally efficient mechanism for capturing inter-output correlations and heteroskedasticity, avoiding the expensive sampling required by previous methods based on cumulative distribution functions.

## Practical Extensions and Empirical Results

The method's structure unlocks several practical extensions, including the handling of missing output values, the refinement of conformal sets when partial information is revealed, and the construction of valid conformal sets for transformations of the output. Empirical evidence on both synthetic and real-world datasets shows that the approach yields conformal sets that improve upon the conditional coverage of existing multivariate baselines.

The paper was submitted to arXiv on July 28, 2025, and the most recent version is from May 7, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "4fda182e-e299-41f7-a568-f375d1b3e63b",
  "tool_use_result": {
    "query": "Braun Berta Jordan Bach \"conformalized gaussian scoring\" multivariate standardized residuals conformal prediction 2025 arXiv 2507.20941",
    "results": [
      {
        "tool_use_id": "srvtoolu_016V5kNEJzftJRyEXtxNjnJM",
        "content": [
          {
            "title": "[2507.20941] Multivariate Standardized Residuals for Conformal Prediction",
            "url": "https://arxiv.org/abs/2507.20941"
          },
          {
            "title": "(PDF) Multivariate Conformal Prediction via Conformalized Gaussian Scoring",
            "url": "https://www.researchgate.net/publication/394081259_Multivariate_Conformal_Prediction_via_Conformalized_Gaussian_Scoring"
          },
          {
            "title": "Multivariate Conformal Prediction via Conformalized Gaussian Scoring",
            "url": "https://arxiv.org/pdf/2507.20941"
          },
          {
            "title": "[PDF] Multivariate Conformal Prediction via Conformalized Gaussian Scoring | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Multivariate-Conformal-Prediction-via-Conformalized-Braun-Berta/eb97eda6c4159d62c1fd5d2ca6404b323e44123c"
          },
          {
            "title": "Multivariate Standardized Residuals for Conformal Prediction",
            "url": "https://arxiv.org/html/2507.20941"
          },
          {
            "title": "Multivariate Conformal Prediction via Conformalized Gaussian ...",
            "url": "https://ribbitribbit.co/paper/arxiv.2507.20941-Multivariate-Conformal-Prediction-via-Conformalized-Gaussian-Scoring"
          },
          {
            "title": "Publications - People @EECS",
            "url": "https://people.eecs.berkeley.edu/~jordan/publications.html"
          },
          {
            "title": "Methodology Jul 2025",
            "url": "https://www.arxiv.org/list/stat.ME/2025-07?skip=350&show=1000"
          },
          {
            "title": "Statistics",
            "url": "https://www.arxiv.org/list/stat/recent?skip=111&show=25"
          },
          {
            "title": "Eugene Berta",
            "url": "https://eugeneberta.github.io/"
          }
        ]
      },
      "I found the paper you're looking for! Here are the search results for arXiv paper 2507.20941:\n\n## Paper Information\n\nThe paper is titled \"Multivariate Standardized Residuals for Conformal Prediction\" by Sacha Braun, Eugène Berta, Michael I. Jordan, and Francis Bach.\n\n## Main Contribution\n\nThe paper proposes a natural extension of normalization to the multivariate setting, effectively whitening the residuals to decouple output correlations and standardize local variance.\n\n## Key Results\n\nThe authors derive a sufficient condition characterizing a broad class of distributions for which standardized residuals yield asymptotic conditional coverage. They demonstrate that using the Mahalanobis distance induced by a learned local covariance as a non-conformity score provides a closed-form, computationally efficient mechanism for capturing inter-output correlations and heteroskedasticity, avoiding the expensive sampling required by previous methods based on cumulative distribution functions.\n\n## Practical Extensions and Empirical Results\n\nThe method's structure unlocks several practical extensions, including the handling of missing output values, the refinement of conformal sets when partial information is revealed, and the construction of valid conformal sets for transformations of the output. Empirical evidence on both synthetic and real-world datasets shows that the approach yields conformal sets that improve upon the conditional coverage of existing multivariate baselines.\n\nThe paper was submitted to arXiv on July 28, 2025, and the most recent version is from May 7, 2026."
    ],
    "durationSeconds": 7.0833781399999864
  }
}
```

</details>

---

### Assistant

_source line 81_

<details><summary>Logged reasoning block</summary>

```text
Let me continue with the analysis:

1. **DiU**: Paper says "derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling." Search confirms: "trace of the posterior covariance over the clean data given the current state equals, in closed form, the divergence of the velocity field." This matches.

2. **SAFE**: Paper says "trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering intervention when anomalous states are detected." Search says: "learns from VLA internal features and predicts a single scalar indicating the likelihood of task failure" and "determines a time-varying threshold using functional conformal prediction (CP) on a hold-out calibration set." The paper says it "calibrate detection timing" but the search says it "determines a time-varying threshold" — same concept. Matches.


3. **Zollo & Zemel**: The paper identifies this as the first systematic study of confidence calibration in VLAs, using prompt ensembles and Platt scaling to improve calibration on manipulation tasks, which the search results confirm.

4. **Braun et al. CGS**: They develop Conformalized Gaussian Scoring using Mahalanobis-based nonconformity scores to construct prediction regions that capture cross-dimensional covariance, which aligns with what the search results describe.

Now I need to verify the remaining papers on my list: Conformalized Teleoperation, CP-in-the-Loop, ACP+CBF, the Silver et al. residual policy work, and LIBERO-Plus with its specific cited numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "e274f600-e14a-42ae-8fe0-d8a367afe9cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MV8T9s5XyQkYdxYnKpe3Ni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 64913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6149
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

Good progress. Let me verify the remaining citations and the specific LIBERO-Plus numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "0fcedaa1-d106-4afe-9bd3-fc3bc689f6d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MV8T9s5XyQkYdxYnKpe3Ni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 64913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6149
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ai6A69dbfBxoMRyvq4CD3i`</summary>

```json
{
  "query": "LIBERO-Plus \"pi0\" \"94.2\" \"6.6\" OR \"UniVLA\" \"95.2\" \"4.3\" robustness perturbation arXiv 2510.13626"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "fc610ceb-0384-473a-a31c-1bc31955ce29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MV8T9s5XyQkYdxYnKpe3Ni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 64913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6149
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NAZNpUfFa8t7VdamJHtPD5`</summary>

```json
{
  "query": "\"conformalized teleoperation\" Zhao Simmons Admoni Bajcsy RSS 2024 high-DOF action mappings shared autonomy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "7a83de3a-875b-4c89-b225-09886e0d2529",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MV8T9s5XyQkYdxYnKpe3Ni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 64913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6149
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

_source line 85_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bi2upVJn7riBP2AXAbS4v7`</summary>

```json
{
  "query": "\"CP-in-the-Loop\" Wang Ning conformal prediction trajectory optimization 2025 arXiv 2510.16376"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "5308897d-4175-4042-9373-50258d105bb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MV8T9s5XyQkYdxYnKpe3Ni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 64913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6149
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

_source line 86_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016fsZzfgAAqbAmaoLUxytHi`</summary>

```json
{
  "query": "Silver Allen Tenenbaum Kaelbling \"residual policy learning\" zero-initialization 2018 RSS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "5fe319c9-2a3b-4c85-ad44-9d0d01863bb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MV8T9s5XyQkYdxYnKpe3Ni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6149,
      "cache_read_input_tokens": 64913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6149
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

_source line 87 · 2026-05-15T20:49:43.637Z_

<details><summary>↩ Tool result · `toolu_01NAZNpUfFa8t7VdamJHtPD5`</summary>

```text
Web search results for query: ""conformalized teleoperation" Zhao Simmons Admoni Bajcsy RSS 2024 high-DOF action mappings shared autonomy"

Links: [{"title":"[2406.07767] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/abs/2406.07767"},{"title":"[2406.07767v1] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"http://arxiv.org/abs/2406.07767v1"},{"title":"dblp: Robotics: Science and Systems 2024","url":"https://dblp.org/db/conf/rss/rss2024.html"},{"title":"Conformalized Teleoperation: Confidently Mapping Human ...","url":"https://www.roboticsproceedings.org/rss20/p008.pdf"},{"title":"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/html/2406.07767v2"},{"title":"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions · Robotics: Science and Systems","url":"https://roboticsconference.org/2024/program/papers/8/"},{"title":"[2410.08852] Conformalized Interactive Imitation Learning: Handling Expert Shift and Intermittent Feedback","url":"https://arxiv.org/abs/2410.08852"},{"title":"Publications | Henny Admoni","url":"https://www.hennyadmoni.com/publications/"},{"title":"Michelle Zhao","url":"https://michellezhao.net/"},{"title":"Reid SIMMONS | Carnegie Mellon University, Pittsburgh | CMU | Robotics Institute | Research profile","url":"https://www.researchgate.net/profile/Reid-Simmons"}]

Great! I found the research paper you were looking for. Here are the search results:

## Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions

The paper "Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions" was authored by Michelle D. Zhao, Reid G. Simmons, Henny Admoni, and Andrea Bajcsy, and it was presented at RSS 2024 (Robotics: Science and Systems) in Delft, Netherlands from July 15-19, 2024.

### Paper Overview

The paper addresses the challenge that assistive robotic arms often have more degrees-of-freedom than a human teleoperator can control with a low-dimensional input, like a joystick. While existing approaches use data-driven methods to learn mappings from low-dimensional human inputs to high-dimensional robot actions, determining if such a black-box mapping can confidently infer a user's intended high-dimensional action from low-dimensional inputs remains an open problem.

### Methodology

The key approach leverages adaptive conformal prediction which adjusts the intervals over time, reducing the uncertainty bounds when the mapping is performant and increasing the bounds when the mapping consistently mis-predicts. The authors also propose an uncertainty-interval-based mechanism for detecting high-uncertainty user inputs and robot states.

### Evaluation

The efficacy of the approach was evaluated in a 2D assistive navigation task and two 7DOF Kinova Jaco tasks involving assistive cup grasping and goal reaching.

The paper and additional resources are available through multiple sources including arXiv and the official Robotics: Science and Systems conference proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "5b515652-f4c5-4d5a-b3c0-c8f9ad225d03",
  "tool_use_result": {
    "query": "\"conformalized teleoperation\" Zhao Simmons Admoni Bajcsy RSS 2024 high-DOF action mappings shared autonomy",
    "results": [
      {
        "tool_use_id": "srvtoolu_019DSaLrUNZMFkjp79Nv41mP",
        "content": [
          {
            "title": "[2406.07767] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions",
            "url": "https://arxiv.org/abs/2406.07767"
          },
          {
            "title": "[2406.07767v1] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions",
            "url": "http://arxiv.org/abs/2406.07767v1"
          },
          {
            "title": "dblp: Robotics: Science and Systems 2024",
            "url": "https://dblp.org/db/conf/rss/rss2024.html"
          },
          {
            "title": "Conformalized Teleoperation: Confidently Mapping Human ...",
            "url": "https://www.roboticsproceedings.org/rss20/p008.pdf"
          },
          {
            "title": "Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions",
            "url": "https://arxiv.org/html/2406.07767v2"
          },
          {
            "title": "Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions · Robotics: Science and Systems",
            "url": "https://roboticsconference.org/2024/program/papers/8/"
          },
          {
            "title": "[2410.08852] Conformalized Interactive Imitation Learning: Handling Expert Shift and Intermittent Feedback",
            "url": "https://arxiv.org/abs/2410.08852"
          },
          {
            "title": "Publications | Henny Admoni",
            "url": "https://www.hennyadmoni.com/publications/"
          },
          {
            "title": "Michelle Zhao",
            "url": "https://michellezhao.net/"
          },
          {
            "title": "Reid SIMMONS | Carnegie Mellon University, Pittsburgh | CMU | Robotics Institute | Research profile",
            "url": "https://www.researchgate.net/profile/Reid-Simmons"
          }
        ]
      },
      "Great! I found the research paper you were looking for. Here are the search results:\n\n## Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\n\nThe paper \"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\" was authored by Michelle D. Zhao, Reid G. Simmons, Henny Admoni, and Andrea Bajcsy, and it was presented at RSS 2024 (Robotics: Science and Systems) in Delft, Netherlands from July 15-19, 2024.\n\n### Paper Overview\n\nThe paper addresses the challenge that assistive robotic arms often have more degrees-of-freedom than a human teleoperator can control with a low-dimensional input, like a joystick. While existing approaches use data-driven methods to learn mappings from low-dimensional human inputs to high-dimensional robot actions, determining if such a black-box mapping can confidently infer a user's intended high-dimensional action from low-dimensional inputs remains an open problem.\n\n### Methodology\n\nThe key approach leverages adaptive conformal prediction which adjusts the intervals over time, reducing the uncertainty bounds when the mapping is performant and increasing the bounds when the mapping consistently mis-predicts. The authors also propose an uncertainty-interval-based mechanism for detecting high-uncertainty user inputs and robot states.\n\n### Evaluation\n\nThe efficacy of the approach was evaluated in a 2D assistive navigation task and two 7DOF Kinova Jaco tasks involving assistive cup grasping and goal reaching.\n\nThe paper and additional resources are available through multiple sources including arXiv and the official Robotics: Science and Systems conference proceedings."
    ],
    "durationSeconds": 6.98329394199999
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T20:49:44.774Z_

<details><summary>↩ Tool result · `toolu_016fsZzfgAAqbAmaoLUxytHi`</summary>

```text
Web search results for query: "Silver Allen Tenenbaum Kaelbling "residual policy learning" zero-initialization 2018 RSS"

Links: [{"title":"[PDF] Residual Policy Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Residual-Policy-Learning-Silver-Allen/8c21a1d8844e6b58fd74b2b94c512a23497029c1"},{"title":"[1812.06298] Residual Policy Learning","url":"https://arxiv.org/abs/1812.06298"},{"title":"Residual Policy Learning","url":"https://www.researchgate.net/publication/329734796_Residual_Policy_Learning"},{"title":"Residual Policy Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv181206298S/abstract"},{"title":"[1812.06298v2] Residual Policy Learning","url":"https://arxiv.org/abs/1812.06298v2"},{"title":"Residual Policy Learning","url":"https://vitalab.github.io/article/2019/06/27/RPL.html"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Residual+policy+learning&amp=&author=T+Silver&amp=&author=K+Allen&amp=&author=J+Tenenbaum&amp=&author=L+Kaelbling&amp=&publication_year=2018&amp=&journal=arXiv+preprint+arXiv:1812.06298"},{"title":"Residual Policy Learning","url":"https://arxiv.org/pdf/1812.06298v2"},{"title":"[1812.06298] Residual Policy Learning - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/1812.06298"},{"title":"Accelerating Residual Reinforcement Learning with Uncertainty Estimation | Request PDF","url":"https://www.researchgate.net/publication/392942022_Accelerating_Residual_Reinforcement_Learning_with_Uncertainty_Estimation"}]

I found the paper! Here are the search results for the "Residual Policy Learning" paper:

**Paper Details:**
- Authors: Tom Silver, Kelsey Allen, Josh Tenenbaum, and Leslie Kaelbling from MIT
- Published on arXiv as paper 1812.06298 (released January 3, 2019, but dated 2018)

**Summary:**
The paper presents Residual Policy Learning (RPL): a simple method for improving nondifferentiable policies using model-free deep reinforcement learning that thrives in complex robotic manipulation tasks where good but imperfect controllers are available. 

In these tasks, reinforcement learning from scratch remains data-inefficient or intractable, but learning a residual on top of the initial controller can yield substantial improvements. The authors study RPL in six challenging MuJoCo tasks involving partial observability, sensor noise, model misspecification, and controller miscalibration, considering both hand-designed policies and model-predictive controllers with known or learned transition models for initial controllers.

The paper and code are available at: https://k-r-allen.github.io/residual-policy-learning/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "6d66d24d-f729-4aa9-a030-2488adde564d",
  "tool_use_result": {
    "query": "Silver Allen Tenenbaum Kaelbling \"residual policy learning\" zero-initialization 2018 RSS",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UpZc3dUG1wgBjin6jbSkeH",
        "content": [
          {
            "title": "[PDF] Residual Policy Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Residual-Policy-Learning-Silver-Allen/8c21a1d8844e6b58fd74b2b94c512a23497029c1"
          },
          {
            "title": "[1812.06298] Residual Policy Learning",
            "url": "https://arxiv.org/abs/1812.06298"
          },
          {
            "title": "Residual Policy Learning",
            "url": "https://www.researchgate.net/publication/329734796_Residual_Policy_Learning"
          },
          {
            "title": "Residual Policy Learning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2018arXiv181206298S/abstract"
          },
          {
            "title": "[1812.06298v2] Residual Policy Learning",
            "url": "https://arxiv.org/abs/1812.06298v2"
          },
          {
            "title": "Residual Policy Learning",
            "url": "https://vitalab.github.io/article/2019/06/27/RPL.html"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar_lookup?title=Residual+policy+learning&amp=&author=T+Silver&amp=&author=K+Allen&amp=&author=J+Tenenbaum&amp=&author=L+Kaelbling&amp=&publication_year=2018&amp=&journal=arXiv+preprint+arXiv:1812.06298"
          },
          {
            "title": "Residual Policy Learning",
            "url": "https://arxiv.org/pdf/1812.06298v2"
          },
          {
            "title": "[1812.06298] Residual Policy Learning - ar5iv - arXiv",
            "url": "https://ar5iv.labs.arxiv.org/html/1812.06298"
          },
          {
            "title": "Accelerating Residual Reinforcement Learning with Uncertainty Estimation | Request PDF",
            "url": "https://www.researchgate.net/publication/392942022_Accelerating_Residual_Reinforcement_Learning_with_Uncertainty_Estimation"
          }
        ]
      },
      "I found the paper! Here are the search results for the \"Residual Policy Learning\" paper:\n\n**Paper Details:**\n- Authors: Tom Silver, Kelsey Allen, Josh Tenenbaum, and Leslie Kaelbling from MIT\n- Published on arXiv as paper 1812.06298 (released January 3, 2019, but dated 2018)\n\n**Summary:**\nThe paper presents Residual Policy Learning (RPL): a simple method for improving nondifferentiable policies using model-free deep reinforcement learning that thrives in complex robotic manipulation tasks where good but imperfect controllers are available. \n\nIn these tasks, reinforcement learning from scratch remains data-inefficient or intractable, but learning a residual on top of the initial controller can yield substantial improvements. The authors study RPL in six challenging MuJoCo tasks involving partial observability, sensor noise, model misspecification, and controller miscalibration, considering both hand-designed policies and model-predictive controllers with known or learned transition models for initial controllers.\n\nThe paper and code are available at: https://k-r-allen.github.io/residual-policy-learning/"
    ],
    "durationSeconds": 6.401099396999983
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-15T20:49:44.834Z_

<details><summary>↩ Tool result · `toolu_01Ai6A69dbfBxoMRyvq4CD3i`</summary>

```text
Web search results for query: "LIBERO-Plus "pi0" "94.2" "6.6" OR "UniVLA" "95.2" "4.3" robustness perturbation arXiv 2510.13626"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.13626v2"}]

I found the research paper you were looking for. Here are the key details:

## LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models

Visual-Language-Action (VLA) models report impressive success rates on robotic manipulation benchmarks, yet a systematic vulnerability analysis by introducing controlled perturbations across seven dimensions—objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise—reveals fundamental robustness weaknesses.

### Key Findings

The analysis reveals consistent brittleness beneath apparent competence, with models exhibiting extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

### Models Evaluated

The analysis includes π0-fast, Nora, WorldVLA, UniVLA and RIPT-VLA among other representative models.

### Paper Information

- **arXiv ID:** 2510.13626
- **Title:** LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models
- **Resources:** 
  - Official arxiv.org abstract: https://arxiv.org/abs/2510.13626
  - GitHub repository: https://github.com/sylvestf/LIBERO-plus
  - Hugging Face dataset: https://huggingface.co/datasets/Sylvest/LIBERO-plus


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "8f20ea54-8bae-44df-bd8b-890c9568f4d1",
  "tool_use_result": {
    "query": "LIBERO-Plus \"pi0\" \"94.2\" \"6.6\" OR \"UniVLA\" \"95.2\" \"4.3\" robustness perturbation arXiv 2510.13626",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KEE67pEjXpe5rXiEH32X6a",
        "content": [
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "Sylvest/LIBERO-plus · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/Sylvest/LIBERO-plus"
          },
          {
            "title": "LIBERO-plus/README.md at main · sylvestf/LIBERO-plus",
            "url": "https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"
          },
          {
            "title": "[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626v1"
          },
          {
            "title": "LIBERO-X: Robustness Litmus for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2602.06556v1"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2510.13626v2"
          }
        ]
      },
      "I found the research paper you were looking for. Here are the key details:\n\n## LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\n\nVisual-Language-Action (VLA) models report impressive success rates on robotic manipulation benchmarks, yet a systematic vulnerability analysis by introducing controlled perturbations across seven dimensions—objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise—reveals fundamental robustness weaknesses.\n\n### Key Findings\n\nThe analysis reveals consistent brittleness beneath apparent competence, with models exhibiting extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.\n\n### Models Evaluated\n\nThe analysis includes π0-fast, Nora, WorldVLA, UniVLA and RIPT-VLA among other representative models.\n\n### Paper Information\n\n- **arXiv ID:** 2510.13626\n- **Title:** LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\n- **Resources:** \n  - Official arxiv.org abstract: https://arxiv.org/abs/2510.13626\n  - GitHub repository: https://github.com/sylvestf/LIBERO-plus\n  - Hugging Face dataset: https://huggingface.co/datasets/Sylvest/LIBERO-plus"
    ],
    "durationSeconds": 9.109923588000004
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-15T20:49:45.523Z_

<details><summary>↩ Tool result · `toolu_01Bi2upVJn7riBP2AXAbS4v7`</summary>

```text
Web search results for query: ""CP-in-the-Loop" Wang Ning conformal prediction trajectory optimization 2025 arXiv 2510.16376"

Links: [{"title":"[2510.16376] Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization","url":"https://arxiv.org/abs/2510.16376"},{"title":"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization","url":"https://arxiv.org/html/2510.16376v1"},{"title":"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization | OpenReview","url":"https://openreview.net/forum?id=lg51XnHt2H"},{"title":"End-to-End Conformal Prediction for Trajectory Optimization | OpenReview","url":"https://openreview.net/forum?id=ilcsm8B7Pe"},{"title":"NeurIPS Poster Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/116267"},{"title":"Adaptive Conformal Prediction Intervals Over Trajectory Ensembles","url":"https://arxiv.org/html/2508.13362v1"},{"title":"Conformal Prediction in The Loop: A Feedback-Based ...","url":"https://www.researchgate.net/publication/396714858_Conformal_Prediction_in_The_Loop_A_Feedback-Based_Uncertainty_Model_for_Trajectory_Optimization"},{"title":"Who Moved My Distribution? Conformal Prediction for Interactive Multi-Agent Systems","url":"https://arxiv.org/html/2511.11567"},{"title":"Adaptive Conformal Prediction Intervals Over Trajectory Ensembles","url":"https://www.arxiv.org/pdf/2508.13362"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"}]

I found the paper! Here's what I found about the research:

## "Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization"

**Paper Details:**
- arXiv: 2510.16376
- Authors: Han Wang and Chao Ning
- Submitted: October 18, 2025

**Overview:**
The paper addresses how Conformal Prediction (CP) is a powerful statistical machine learning tool to construct uncertainty sets with coverage guarantees for generating prediction regions for decision-making tasks like Trajectory Optimization (TO) in uncertain environments.

**Key Innovation:**
While existing methods use a sequential scheme where decisions rely unidirectionally on the prediction regions, the paper proposes a novel Feedback-Based CP (Fb-CP) framework for shrinking-horizon TO with a joint risk constraint over the entire mission time.

**Main Contributions:**
- The realized trajectories are continuously fed back to the CP, enabling feedback-based adjustments of the prediction regions and provable online improvement in trajectory performance.
- These adjustments consistently maintain the coverage guarantees of the prediction regions, ensuring provable safety.
- The paper develops a decision-focused iterative risk allocation algorithm with theoretical convergence analysis.
- The method is extended to handle distribution shift.

The paper was also presented at NeurIPS 2025 as a poster presentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "9b5ae355-1a45-4c79-b25a-6adc863d7817",
  "tool_use_result": {
    "query": "\"CP-in-the-Loop\" Wang Ning conformal prediction trajectory optimization 2025 arXiv 2510.16376",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M2cmfyvAMSCoKqY1uwQX2m",
        "content": [
          {
            "title": "[2510.16376] Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization",
            "url": "https://arxiv.org/abs/2510.16376"
          },
          {
            "title": "Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization",
            "url": "https://arxiv.org/html/2510.16376v1"
          },
          {
            "title": "Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization | OpenReview",
            "url": "https://openreview.net/forum?id=lg51XnHt2H"
          },
          {
            "title": "End-to-End Conformal Prediction for Trajectory Optimization | OpenReview",
            "url": "https://openreview.net/forum?id=ilcsm8B7Pe"
          },
          {
            "title": "NeurIPS Poster Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/116267"
          },
          {
            "title": "Adaptive Conformal Prediction Intervals Over Trajectory Ensembles",
            "url": "https://arxiv.org/html/2508.13362v1"
          },
          {
            "title": "Conformal Prediction in The Loop: A Feedback-Based ...",
            "url": "https://www.researchgate.net/publication/396714858_Conformal_Prediction_in_The_Loop_A_Feedback-Based_Uncertainty_Model_for_Trajectory_Optimization"
          },
          {
            "title": "Who Moved My Distribution? Conformal Prediction for Interactive Multi-Agent Systems",
            "url": "https://arxiv.org/html/2511.11567"
          },
          {
            "title": "Adaptive Conformal Prediction Intervals Over Trajectory Ensembles",
            "url": "https://www.arxiv.org/pdf/2508.13362"
          },
          {
            "title": "Artificial Intelligence Jun 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"
          }
        ]
      },
      "I found the paper! Here's what I found about the research:\n\n## \"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\"\n\n**Paper Details:**\n- arXiv: 2510.16376\n- Authors: Han Wang and Chao Ning\n- Submitted: October 18, 2025\n\n**Overview:**\nThe paper addresses how Conformal Prediction (CP) is a powerful statistical machine learning tool to construct uncertainty sets with coverage guarantees for generating prediction regions for decision-making tasks like Trajectory Optimization (TO) in uncertain environments.\n\n**Key Innovation:**\nWhile existing methods use a sequential scheme where decisions rely unidirectionally on the prediction regions, the paper proposes a novel Feedback-Based CP (Fb-CP) framework for shrinking-horizon TO with a joint risk constraint over the entire mission time.\n\n**Main Contributions:**\n- The realized trajectories are continuously fed back to the CP, enabling feedback-based adjustments of the prediction regions and provable online improvement in trajectory performance.\n- These adjustments consistently maintain the coverage guarantees of the prediction regions, ensuring provable safety.\n- The paper develops a decision-focused iterative risk allocation algorithm with theoretical convergence analysis.\n- The method is extended to handle distribution shift.\n\nThe paper was also presented at NeurIPS 2025 as a poster presentation."
    ],
    "durationSeconds": 7.925629657000012
  }
}
```

</details>

---

### Assistant

_source line 91_

<details><summary>Logged reasoning block</summary>

```text
Let me verify more things:

1. **LIBERO-Plus numbers**: The paper claims "π₀ drops from 94.2% to 6.6% under robot initial-state perturbation, and UniVLA from 95.2% to 4.3% under camera viewpoint changes." The search says "performance dropping from 95% to below 30% under modest perturbations." It doesn't directly confirm the exact numbers. I should note this but not flag it as an error — the exact numbers need to be verified against the actual paper tables, and the general trend matches.


2. **Conformalized Teleoperation**: The paper's description of using conformal prediction to quantify uncertainty in high-DOF action mappings and flag unreliable predictions aligns with the search results mentioning adaptive conformal prediction for constructing uncertainty intervals and detecting high-uncertainty inputs.
3. **CP-in-the-Loop**: The integration of conformal prediction regions as feedback constraints in trajectory optimization matches what the search describes about feedback-based adjustments of prediction regions.
4. **Silver et al.**: The paper mentions introducing a framework for classical controllers, but the thought cuts off here.

For the residual policy learning claim about zero-initialization, the search doesn't explicitly confirm this detail, though I'm confident from my knowledge that RPL does initialize residual outputs to zero so the combined policy starts from the base policy. Now I need to verify the ACP+CBF paper, double-check the SC-VLA residual RL claim, and confirm the specific LIBERO-Plus numbers before compiling my final attribution summary.

I've verified the first batch of attributions and they all check out — from the VLA and flow matching papers through to the more recent methods like SRPO, RobustVLA, DiG-Flow, TT-VLA, and A2C2, each with their specific technical contributions properly attributed.

Now I'm continuing through the next set of papers, covering VLA-Pilot's evolutionary diffusion approach with MLLM verification, then moving into the statistical and conformal prediction methods — Ledoit-Wolf covariance shrinkage, CGS with Mahalanobis scoring, and several conformal prediction applications across different domains like shared autonomy and trajectory optimization, plus residual policy learning.

Continuing with more recent work on residual policies and VLA-based approaches — TRANSIC's gated residual mechanism for sim-to-real transfer, PLD combining frozen VLA with lightweight residual actors and off-policy RL, DRC's decaying correction for teleoperation, and DiU's closed-form posterior covariance through velocity field divergence. Then there's SAFE's multitask failure detection on VLA features with conformal calibration, followed by the first systematic VLA calibration study using prompt ensembles and Platt scaling, and DAgger for behavioral cloning.

Now I'm spotting some issues that need fixing. ReconVLA is described incorrectly — it's not just a UQ visualization tool that leaves actions unchanged. The paper actually shows it uses uncertainty-guided action selection based on CQR, so it does influence what actions the VLA takes. And for LIBERO-Plus, I need to verify those specific performance numbers for π₀ and UniVLA across the different conditions, since the search results mention several models tested but I'm not certain about the exact percentages cited.

SC-VLA's description as using "residual RL" might also be off — it sounds more like it's doing online refinement through world model imagination and dense reward shaping rather than traditional residual RL. Let me dig into these three issues more carefully, starting with the LIBERO-Plus numbers and SC-VLA's actual method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "c9894db6-cd7e-4fa3-8335-b8032782d948",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qpUAp6H4xtw5wfJHftYKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 844,
      "cache_creation_input_tokens": 3851,
      "cache_read_input_tokens": 71062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3851
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

_source line 92_

Let me verify the LIBERO-Plus specific numbers and SC-VLA's method classification more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "ea5c9b83-1ec3-47f5-afdf-6d0441230802",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qpUAp6H4xtw5wfJHftYKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 844,
      "cache_creation_input_tokens": 3851,
      "cache_read_input_tokens": 71062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3851
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

_source line 93_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AuwvAHt6iWnGYex2E76oXd`</summary>

```json
{
  "query": "LIBERO-Plus arXiv 2510.13626 pi0 UniVLA success rate robot initial state camera viewpoint specific numbers table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "bcf568ac-ec73-405f-affd-c938864929b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qpUAp6H4xtw5wfJHftYKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 844,
      "cache_creation_input_tokens": 3851,
      "cache_read_input_tokens": 71062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3851
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0129b2nN4LhZvi2mgYF9wpTs`</summary>

```json
{
  "query": "SC-VLA arXiv 2602.21633 method details \"residual RL\" OR \"reinforcement learning\" action refinement training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "18cb1dd3-c0d6-47f1-9492-b35e8574015d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qpUAp6H4xtw5wfJHftYKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 844,
      "cache_creation_input_tokens": 3851,
      "cache_read_input_tokens": 71062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3851
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FG39zMfFYyqvKtEVb9Xp5r`</summary>

```json
{
  "query": "Zhou Zhang Luo \"adaptive conformal prediction\" \"control barrier functions\" safe reinforcement learning ICRA 2025 arXiv 2503.17678"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "ab54bf62-096d-4fb8-8a59-6915c6ff4ed8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qpUAp6H4xtw5wfJHftYKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 844,
      "cache_creation_input_tokens": 3851,
      "cache_read_input_tokens": 71062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3851
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

_source line 96 · 2026-05-15T20:50:33.404Z_

<details><summary>↩ Tool result · `toolu_0129b2nN4LhZvi2mgYF9wpTs`</summary>

```text
Web search results for query: "SC-VLA arXiv 2602.21633 method details "residual RL" OR "reinforcement learning" action refinement training"

Links: [{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633"},{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"RLinf-Co: Reinforcement Learning–Based Sim–Real Co-Training for VLA Models","url":"https://arxiv.org/html/2602.12628v1"},{"title":"From Imitation to Refinement – Residual RL for Precise Assembly","url":"https://arxiv.org/html/2407.16677v4"},{"title":"[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"RLinf-VLA: A unified and efficient framework for VLA+RL training","url":"https://arxiv.org/html/2510.06710v1"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"From Imitation to Refinement – Residual RL for Precise Visual Assembly","url":"https://arxiv.org/html/2407.16677v1"},{"title":"World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy","url":"https://arxiv.org/html/2602.06508v1"}]

Based on the search results, here are the method details for SC-VLA (arXiv 2602.21633):

## SC-VLA Method Overview

Self-Correcting VLA (SC-VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination.

## Key Components

**Sparse World Imagination:** The method integrates auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution.

**Online Action Refinement Module:** SC-VLA introduces an online action refinement module to reshape progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states.

## Performance Results

Evaluations on challenging robot manipulation tasks from simulation benchmarks and real-world settings demonstrate that SC-VLA achieves state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.

**Note:** The search results do not contain explicit references to "residual RL" as a specific training technique used in SC-VLA 2602.21633. The sparse world imagination and online action refinement modules appear to be the primary mechanisms for action refinement in this method.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "d8f9d0d7-4719-4f53-9d17-cafcaf22d3d6",
  "tool_use_result": {
    "query": "SC-VLA arXiv 2602.21633 method details \"residual RL\" OR \"reinforcement learning\" action refinement training",
    "results": [
      {
        "tool_use_id": "srvtoolu_019qShCE7NnRKdibZgk3LZ1q",
        "content": [
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/html/2602.21633"
          },
          {
            "title": "[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/abs/2602.21633"
          },
          {
            "title": "RLinf-Co: Reinforcement Learning–Based Sim–Real Co-Training for VLA Models",
            "url": "https://arxiv.org/html/2602.12628v1"
          },
          {
            "title": "From Imitation to Refinement – Residual RL for Precise Assembly",
            "url": "https://arxiv.org/html/2407.16677v4"
          },
          {
            "title": "[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/abs/2509.09674"
          },
          {
            "title": "[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/abs/2505.18719"
          },
          {
            "title": "RLinf-VLA: A unified and efficient framework for VLA+RL training",
            "url": "https://arxiv.org/html/2510.06710v1"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=TQhSodCM4r"
          },
          {
            "title": "From Imitation to Refinement – Residual RL for Precise Visual Assembly",
            "url": "https://arxiv.org/html/2407.16677v1"
          },
          {
            "title": "World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy",
            "url": "https://arxiv.org/html/2602.06508v1"
          }
        ]
      },
      "Based on the search results, here are the method details for SC-VLA (arXiv 2602.21633):\n\n## SC-VLA Method Overview\n\nSelf-Correcting VLA (SC-VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination.\n\n## Key Components\n\n**Sparse World Imagination:** The method integrates auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution.\n\n**Online Action Refinement Module:** SC-VLA introduces an online action refinement module to reshape progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states.\n\n## Performance Results\n\nEvaluations on challenging robot manipulation tasks from simulation benchmarks and real-world settings demonstrate that SC-VLA achieves state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.\n\n**Note:** The search results do not contain explicit references to \"residual RL\" as a specific training technique used in SC-VLA 2602.21633. The sparse world imagination and online action refinement modules appear to be the primary mechanisms for action refinement in this method."
    ],
    "durationSeconds": 7.1029568870000075
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-15T20:50:33.691Z_

<details><summary>↩ Tool result · `toolu_01AuwvAHt6iWnGYex2E76oXd`</summary>

```text
Web search results for query: "LIBERO-Plus arXiv 2510.13626 pi0 UniVLA success rate robot initial state camera viewpoint specific numbers table"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"Unified Vision-Language-Action Model","url":"https://arxiv.org/html/2506.19850v1"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"Experiences from Benchmarking Vision–Language–Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2511.11298v1"},{"title":"[Literature Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/libero-plus-in-depth-robustness-analysis-of-vision-language-action-models"}]

Based on the search results from arXiv paper 2510.13626 (LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models), here are the key findings about performance under perturbations:

## Key Results

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

## UniVLA Specific Performance

UniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing π0-FAST's 85.5%. However, this baseline performance degrades significantly under perturbations.

## Evaluation Methodology

Table 1 presents model performance under different perturbations, where for each model, the first row reports the task success rate (%) under each perturbation dimension, with the "Original" column indicating the performance on unperturbed inputs, and the second row shows the corresponding absolute performance drop.

## Key Perturbation Factors

Camera viewpoints involve modifications to camera distance, spherical position, and orientation. The paper also evaluates robustness across robot initial states as one of the critical perturbation dimensions tested.

The search results show that while specific numerical values for UniVLA and π0 are referenced in the paper, the complete detailed table data appears to be in the full PDF which may require direct access to the arXiv HTML or PDF version for the complete table with all specific numbers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "7eed396d-74c3-466c-83db-6a95d30954e2",
  "tool_use_result": {
    "query": "LIBERO-Plus arXiv 2510.13626 pi0 UniVLA success rate robot initial state camera viewpoint specific numbers table",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q88yNb6KCTnVDpvvKpywss",
        "content": [
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "Unified Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2506.19850v1"
          },
          {
            "title": "[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626v1"
          },
          {
            "title": "Experiences from Benchmarking Vision–Language–Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.11298v1"
          },
          {
            "title": "[Literature Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://www.themoonlight.io/en/review/libero-plus-in-depth-robustness-analysis-of-vision-language-action-models"
          }
        ]
      },
      "Based on the search results from arXiv paper 2510.13626 (LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models), here are the key findings about performance under perturbations:\n\n## Key Results\n\nModels exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.\n\n## UniVLA Specific Performance\n\nUniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing π0-FAST's 85.5%. However, this baseline performance degrades significantly under perturbations.\n\n## Evaluation Methodology\n\nTable 1 presents model performance under different perturbations, where for each model, the first row reports the task success rate (%) under each perturbation dimension, with the \"Original\" column indicating the performance on unperturbed inputs, and the second row shows the corresponding absolute performance drop.\n\n## Key Perturbation Factors\n\nCamera viewpoints involve modifications to camera distance, spherical position, and orientation. The paper also evaluates robustness across robot initial states as one of the critical perturbation dimensions tested.\n\nThe search results show that while specific numerical values for UniVLA and π0 are referenced in the paper, the complete detailed table data appears to be in the full PDF which may require direct access to the arXiv HTML or PDF version for the complete table with all specific numbers."
    ],
    "durationSeconds": 7.994007362000004
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-15T20:50:34.345Z_

<details><summary>↩ Tool result · `toolu_01FG39zMfFYyqvKtEVb9Xp5r`</summary>

```text
Web search results for query: "Zhou Zhang Luo "adaptive conformal prediction" "control barrier functions" safe reinforcement learning ICRA 2025 arXiv 2503.17678"

Links: [{"title":"[2503.17678] Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/abs/2503.17678"},{"title":"Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/html/2503.17678"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=1000&show=100"},{"title":"Computer Vision and Pattern Recognition Jul 2025","url":"https://arxiv.org/list/cs.CV/2025-07?skip=1500&show=2000"},{"title":"Computer Science Feb 2025 - arXiv","url":"https://arxiv.org/list/cs/2025-02?skip=8775&show=2000"},{"title":"[2302.12238] Improving Adaptive Conformal Prediction Using Self-Supervised Learning","url":"https://arxiv.org/abs/2302.12238"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=1725&show=2000"},{"title":"Conformal Prediction: A Data Perspective","url":"https://arxiv.org/pdf/2410.06494"},{"title":"[2506.07804] Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/abs/2506.07804"},{"title":"Computer Science Mar 2024","url":"https://arxiv.org/list/cs/2024-03?skip=7065&show=2000"}]

I found the paper you're looking for! The paper is "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction" (arXiv 2503.17678).

The authors are Hao Zhou and 2 other authors (including Yanze Zhang), and based on the search results, the third author is Wenhao Luo. The paper addresses safety concerns in learning-enabled autonomous systems, especially for real-world deployment.

The key technical approach is: The Adaptive Conformal Prediction (ACP) is used to quantify the uncertainty from online observations and combined with the Control Barrier Functions (CBF) to characterize the uncertainty-aware safe control constraints under learned dynamics. Additionally, Quadrature Fourier Features (QFF) are employed for kernel function approximation of Gaussian Processes (GPs) to enable efficient approximation of unknown dynamics.

An optimism-based exploration strategy is integrated with ACP-based CBFs for safe exploration and near-optimal safe nonlinear control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "4965db22-d1ad-4bc6-b3b4-6f31aebd6dba",
  "tool_use_result": {
    "query": "Zhou Zhang Luo \"adaptive conformal prediction\" \"control barrier functions\" safe reinforcement learning ICRA 2025 arXiv 2503.17678",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Smaa1Lg84ftcohk6p71G9r",
        "content": [
          {
            "title": "[2503.17678] Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction",
            "url": "https://arxiv.org/abs/2503.17678"
          },
          {
            "title": "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction",
            "url": "https://arxiv.org/html/2503.17678"
          },
          {
            "title": "Machine Learning Sep 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-09?skip=1000&show=100"
          },
          {
            "title": "Computer Vision and Pattern Recognition Jul 2025",
            "url": "https://arxiv.org/list/cs.CV/2025-07?skip=1500&show=2000"
          },
          {
            "title": "Computer Science Feb 2025 - arXiv",
            "url": "https://arxiv.org/list/cs/2025-02?skip=8775&show=2000"
          },
          {
            "title": "[2302.12238] Improving Adaptive Conformal Prediction Using Self-Supervised Learning",
            "url": "https://arxiv.org/abs/2302.12238"
          },
          {
            "title": "Computer Science May 2025",
            "url": "https://arxiv.org/list/cs/2025-05?skip=1725&show=2000"
          },
          {
            "title": "Conformal Prediction: A Data Perspective",
            "url": "https://arxiv.org/pdf/2410.06494"
          },
          {
            "title": "[2506.07804] Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/abs/2506.07804"
          },
          {
            "title": "Computer Science Mar 2024",
            "url": "https://arxiv.org/list/cs/2024-03?skip=7065&show=2000"
          }
        ]
      },
      "I found the paper you're looking for! The paper is \"Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction\" (arXiv 2503.17678).\n\nThe authors are Hao Zhou and 2 other authors (including Yanze Zhang), and based on the search results, the third author is Wenhao Luo. The paper addresses safety concerns in learning-enabled autonomous systems, especially for real-world deployment.\n\nThe key technical approach is: The Adaptive Conformal Prediction (ACP) is used to quantify the uncertainty from online observations and combined with the Control Barrier Functions (CBF) to characterize the uncertainty-aware safe control constraints under learned dynamics. Additionally, Quadrature Fourier Features (QFF) are employed for kernel function approximation of Gaussian Processes (GPs) to enable efficient approximation of unknown dynamics.\n\nAn optimism-based exploration strategy is integrated with ACP-based CBFs for safe exploration and near-optimal safe nonlinear control."
    ],
    "durationSeconds": 6.886891792999988
  }
}
```

</details>

---

### Assistant

_source line 99_

<details><summary>Logged reasoning block</summary>

```text
Let me summarize what I've found:

### Critical Findings:

**1. ReconVLA (chen2026reconvla) — ⚠️ NEEDS CORRECTION**
The current text in multiple places says ReconVLA "does not modify the VLA's actions" / "operates as an uncertainty quantification framework rather than an action improvement method." But according to the search, ReconVLA does "enable robust action selection and proactive failure detection" — it uses CQR-based uncertainty to "guide reliable action selection under generative variability." 


So ReconVLA actually does influence action selection through uncertainty-guided mechanisms. It applies conformal quantile regression for action-level uncertainty bounds, uses Mahalanobis distance for detecting out-of-distribution states, and directly guides action selection based on those uncertainty estimates. The current framing as a passive UQ framework is inaccurate—I need to revise the intro and related work sections to reflect that it's an active uncertainty-guided approach that shapes which actions get selected.

For SC-VLA, the "residual RL" characterization is imprecise. The method actually uses auxiliary predictive heads to estimate task progress and future trajectories, then performs online action refinement through world imagination with progress-dependent rewards. This is fundamentally a world-imagination-based refinement approach rather than a residual policy method, so I should clarify that distinction to avoid conflating it with other residual RL techniques.

Now I'm checking the LIBERO-Plus baseline numbers more carefully. The paper cites π₀ dropping from 94.2% to 6.6% under perturbation, but LIBERO-Plus actually evaluates π0-fast, which is a different model variant. I need to verify whether the cited numbers refer to the original π₀ or π0-fast, and also double-check that UniVLA's baseline is correctly reported as 95.5% rather than 95.2%.

For the ACP+CBF paper, there's a mismatch between the bibliography title and the actual paper title—the bib has "Adaptive Conformal Prediction with Control Barrier Functions" but the real title is "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction." The method description in the related work is accurate though. On Silver et al., the paper mentions zero-initialization as a key technique, but the search results frame it as residual policy learning without explicitly highlighting zero-initialization in the abstract.

For TRANSIC, the description calls it a "binary gate" when it's actually a "gated residual policy"—the gate might be continuous rather than strictly binary, though the paper does explore gated versus ungated variants. Now I need to verify whether LIBERO-Plus specifically uses π₀ or π₀-fast and double-check those performance numbers before finalizing the audit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "e5a8e275-f5af-40ab-a4f0-7bdc6443c762",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzajsPCCy4ynnJ6XuLi1wS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 74913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5118
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

_source line 100_

Let me verify the π₀ vs π₀-fast distinction in LIBERO-Plus and check a few more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "1c416954-6445-47d3-9207-7f64bd73c7cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzajsPCCy4ynnJ6XuLi1wS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 74913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5118
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

_source line 101_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PWDZYr1cpZRWbvwBybtBCP`</summary>

```json
{
  "query": "LIBERO-Plus 2510.13626 \"pi0\" OR \"π0\" OR \"pi0-fast\" \"94.2\" OR \"94\" success rate original table results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "5649f9c4-ae91-4caa-8f4c-7dd9c65b584d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzajsPCCy4ynnJ6XuLi1wS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 74913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5118
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

_source line 102_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HkvtnPpqVXULLpjR1q7zon`</summary>

```json
{
  "query": "SC-VLA self-correcting VLA 2602.21633 how is the action refinement module trained RL or supervised"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "b9b58b43-830a-466f-9b1a-bbda4fb9797b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzajsPCCy4ynnJ6XuLi1wS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 74913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5118
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

_source line 103 · 2026-05-15T20:51:05.536Z_

<details><summary>↩ Tool result · `toolu_01PWDZYr1cpZRWbvwBybtBCP`</summary>

```text
Web search results for query: "LIBERO-Plus 2510.13626 "pi0" OR "π0" OR "pi0-fast" "94.2" OR "94" success rate original table results"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626.pdf"},{"title":"Fine-tuned π0 and π0.5 models fail to replicate reported success rates on LIBERO benchmark · Issue #2114 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2114"},{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"PI0 Evaluation results on LIBERO is very low · Issue #952 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/952"},{"title":"Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/734"},{"title":"pi0.5 on LIBERO simulation reproduce, zero success rate on pi05_libero_base · Issue #2533 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2533"}]

I found relevant information about the LIBERO-Plus paper (arXiv:2510.13626) and related models. Based on the search results, the LIBERO-Plus paper evaluated 10,030 tasks using four representative models—OpenVLA-OFT, π0, π0-fast, and UniVLA.

However, I was unable to locate specific success rate data showing "94.2%" or "94%" for π0 or π0-fast in an original table from the paper. The search results include references to the paper content and related discussions, but not the complete original table data you're asking about.

To find the exact table with those specific success rates, you would need to:
1. Access the full PDF of the paper at arxiv.org/pdf/2510.13626
2. Look for the results tables that compare model performance across different LIBERO task suites

If you need a specific success rate value from the paper, you may want to check the PDF directly or clarify which specific task suite (libero_spatial, libero_object, libero_goal, libero_10) or benchmark variant you're interested in.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "7a0e9043-67ae-4cb8-95a7-24d8420e5c78",
  "tool_use_result": {
    "query": "LIBERO-Plus 2510.13626 \"pi0\" OR \"π0\" OR \"pi0-fast\" \"94.2\" OR \"94\" success rate original table results",
    "results": [
      {
        "tool_use_id": "srvtoolu_014H7SxYo8DUSi8Zuc79Dzu1",
        "content": [
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626.pdf"
          },
          {
            "title": "Fine-tuned π0 and π0.5 models fail to replicate reported success rates on LIBERO benchmark · Issue #2114 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2114"
          },
          {
            "title": "PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/711"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "PI0 Evaluation results on LIBERO is very low · Issue #952 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/952"
          },
          {
            "title": "Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/734"
          },
          {
            "title": "pi0.5 on LIBERO simulation reproduce, zero success rate on pi05_libero_base · Issue #2533 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2533"
          }
        ]
      },
      "I found relevant information about the LIBERO-Plus paper (arXiv:2510.13626) and related models. Based on the search results, the LIBERO-Plus paper evaluated 10,030 tasks using four representative models—OpenVLA-OFT, π0, π0-fast, and UniVLA.\n\nHowever, I was unable to locate specific success rate data showing \"94.2%\" or \"94%\" for π0 or π0-fast in an original table from the paper. The search results include references to the paper content and related discussions, but not the complete original table data you're asking about.\n\nTo find the exact table with those specific success rates, you would need to:\n1. Access the full PDF of the paper at arxiv.org/pdf/2510.13626\n2. Look for the results tables that compare model performance across different LIBERO task suites\n\nIf you need a specific success rate value from the paper, you may want to check the PDF directly or clarify which specific task suite (libero_spatial, libero_object, libero_goal, libero_10) or benchmark variant you're interested in."
    ],
    "durationSeconds": 6.410612351000018
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-15T20:51:16.050Z_

<details><summary>↩ Tool result · `toolu_01HkvtnPpqVXULLpjR1q7zon`</summary>

```text
Web search results for query: "SC-VLA self-correcting VLA 2602.21633 how is the action refinement module trained RL or supervised"

Links: [{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260221633L/abstract"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation","url":"https://arxiv.org/html/2405.17418v2"},{"title":"From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models","url":"https://arxiv.org/pdf/2602.01811"},{"title":"[2405.17418] A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation","url":"https://arxiv.org/abs/2405.17418"},{"title":"[2602.01811] From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models","url":"https://arxiv.org/abs/2602.01811"},{"title":"DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving","url":"https://arxiv.org/html/2602.14577"},{"title":"JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse","url":"https://craftjarvis.github.io/JarvisVLA/"}]

Based on the search results for SC-VLA (arXiv:2602.21633), the online action refinement module reshapes progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states. 

The Online Action Refinement (OAR) dynamically optimizes policies via residual adjustments and reshaped rewards. This indicates that the action refinement module uses a **reinforcement learning approach** rather than purely supervised learning, as it operates through reward reshaping and policy optimization rather than direct action supervision. The module works in conjunction with the Sparse World Imagination component to enable self-improvement during online execution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "f38b3f33-c66e-4d6f-8cdd-990538ee59d3",
  "tool_use_result": {
    "query": "SC-VLA self-correcting VLA 2602.21633 how is the action refinement module trained RL or supervised",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TjHv6NyxCUMbuZBRFZytYP",
        "content": [
          {
            "title": "[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/abs/2602.21633"
          },
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/html/2602.21633"
          },
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260221633L/abstract"
          },
          {
            "title": "GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub",
            "url": "https://github.com/Kisaragi0/SC-VLA"
          },
          {
            "title": "A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation",
            "url": "https://arxiv.org/html/2405.17418v2"
          },
          {
            "title": "From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models",
            "url": "https://arxiv.org/pdf/2602.01811"
          },
          {
            "title": "[2405.17418] A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation",
            "url": "https://arxiv.org/abs/2405.17418"
          },
          {
            "title": "[2602.01811] From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models",
            "url": "https://arxiv.org/abs/2602.01811"
          },
          {
            "title": "DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving",
            "url": "https://arxiv.org/html/2602.14577"
          },
          {
            "title": "JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse",
            "url": "https://craftjarvis.github.io/JarvisVLA/"
          }
        ]
      },
      "Based on the search results for SC-VLA (arXiv:2602.21633), the online action refinement module reshapes progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states. \n\nThe Online Action Refinement (OAR) dynamically optimizes policies via residual adjustments and reshaped rewards. This indicates that the action refinement module uses a **reinforcement learning approach** rather than purely supervised learning, as it operates through reward reshaping and policy optimization rather than direct action supervision. The module works in conjunction with the Sparse World Imagination component to enable self-improvement during online execution."
    ],
    "durationSeconds": 16.253369498999962
  }
}
```

</details>

---

### Assistant

_source line 105_

<details><summary>Logged reasoning block</summary>

```text
OK let me now also read the LIBERO-Plus paper to check the specific numbers. Actually, I can't read the PDF directly. Let me try the arXiv HTML version.

Actually, let me also think about what exact numbers the LIBERO-Plus paper uses. The search says it tests "OpenVLA-OFT, π0, π0-fast, and UniVLA." So both π0 and π0-fast are tested. The intro says "π₀ drops from 94.2% to 6.6% under robot initial-state perturbation" — this could be correct if LIBERO-Plus does test the original π₀ (not just π0-fast). But I need to verify the specific numbers.


I can't easily access the exact table numbers from the search results, but the general claim about dramatic performance drops under perturbation aligns with what the paper reports, so I'll mark this as needing verification of those specific percentages before finalizing. For SC-VLA, the search confirms it uses residual adjustments and reshaped rewards, which makes "residual RL" a reasonable characterization since OAR applies RL with residual adjustments.

Now I need to compile the full audit report and address the critical issues. The ReconVLA attribution needs corrections in two places — the intro should clarify that it applies conformal quantile regression for uncertainty calibration and out-of-distribution detection rather than functioning as an action improvement method, and the related work section needs a similar fix. I'm checking the specific performance numbers from LIBERO-Plus against the actual tables to make sure they're accurate, and I notice the bibliography entry for the ACP+CBF paper has the wrong title—it should be "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction" rather than what's currently listed. Now I'm revising the ReconVLA description in the introduction to clarify that it does guide action selection through uncertainty, not just quantify uncertainty passively. I need to reconsider how ReconVLA fits into the positioning now that it actually does perform uncertainty-guided action selection rather than just quantifying uncertainty. The key distinction is that my method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline, which ReconVLA doesn't do—so that claim still holds. But I should reframe ReconVLA's role in the inference-time methods section to reflect that it's now a competitor doing UQ-guided selection, not just a passive uncertainty framework.

The corrected positioning treats ReconVLA as a complementary approach in the same domain rather than a direct competitor—both use uncertainty to improve actions, but through different mechanisms. I'm updating the intro paragraph to clarify that ReconVLA uses conformal quantile regression for uncertainty-guided action selection and failure detection, which better captures what it actually does while still distinguishing it from my approach's combination of selection and learned correction. The gap statement still holds—ReconVLA uses uncertainty-guided selection but doesn't apply learned residual correction, whereas ACR-VLA's contribution is combining both approaches in a two-stage pipeline. Let me verify the bibliography entry for ACP+CBF and then apply all these revisions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "4e3abe08-a5b3-40a8-a935-bab7b3c62d0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EURYrTVmwdnrBwdsZ7sop3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2838,
      "cache_read_input_tokens": 80031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2838
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

_source line 106_

I now have a complete picture. Let me compile findings and make corrections. Here are the issues found:

**CRITICAL: ReconVLA attribution (2 locations)** — Text claims it "does not modify the VLA's actions" / "operates as an uncertainty quantification framework rather than an action improvement method." But ReconVLA actually includes uncertainty-guided action selection. Needs fixing per D034.

Let me fix the intro and related work now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "df888fcf-da1d-44a2-9b02-75380a77f17b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EURYrTVmwdnrBwdsZ7sop3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2838,
      "cache_read_input_tokens": 80031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2838
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

_source line 107_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__edit_paper_section · `toolu_01RjY7cDqC5VALieRkkbQwDm`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "section": "introduction",
  "old_text": "ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution states, but operates as an uncertainty quantification framework rather than an action improvement method.",
  "new_text": "ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "937f40eb-5861-47d9-985e-27a728c854c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EURYrTVmwdnrBwdsZ7sop3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2838,
      "cache_read_input_tokens": 80031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2838
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

_source line 108 · 2026-05-15T20:51:57.264Z_

<details><summary>↩ Tool result · `toolu_01RjY7cDqC5VALieRkkbQwDm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex\", \"version\": 8, \"coverage\": \"0/0\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "27c59884-59db-4dfa-8f52-124656a93356",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"section_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex\\\", \\\"version\\\": 8, \\\"coverage\\\": \\\"0/0\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex\", \"version\": 8, \"coverage\": \"0/0\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 109_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__edit_paper_section · `toolu_01XxqpV2UmdjcwnrDtCbmGew`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "section": "related_work",
  "old_text": "ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, providing a principled uncertainty quantification framework that operates without retraining but does not modify the VLA's actions.",
  "new_text": "ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "379fb493-23ac-4085-bd35-0e632c55e5ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EURYrTVmwdnrBwdsZ7sop3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2838,
      "cache_read_input_tokens": 80031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2838
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

_source line 110 · 2026-05-15T20:51:58.705Z_

<details><summary>↩ Tool result · `toolu_01XxqpV2UmdjcwnrDtCbmGew`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex\", \"version\": 9, \"coverage\": \"0/0\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "1a50bdc7-951f-4a56-bff3-477ae5c1b16f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"section_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex\\\", \\\"version\\\": 9, \\\"coverage\\\": \\\"0/0\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex\", \"version\": 9, \"coverage\": \"0/0\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 111_

<details><summary>Logged reasoning block</summary>

````text
Both edits succeeded. Now let me also fix the ACP+CBF bib title. Let me first check what the current bib entry says and what the correct title should be.

The bib entry currently says:
```
@inproceedings{zhou2025acp_cbf,
    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},
    ...
}
```

The actual paper title from the search is: "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction"

Let me fix this.


Before I update it, I should check if other entries have similar title mismatches. Looking at the Braun et al. entry, the bib currently has "Multivariate Standardized Residuals for Conformal Prediction," which matches the latest arXiv version, so that one's fine. But I need to verify whether the ACP+CBF title in the bib is from an earlier version or if it's genuinely incorrect.

The search results show the current title should be "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction," so the bib entry definitely needs updating. I'll also flag the LIBERO-Plus numbers in my audit report since I can't verify them without the full PDF, but I won't change the paper text itself.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "eebb47ec-7d03-4fdb-89da-6e54e51a9062",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMbngzHGZbS84A9cnCaKUp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 82869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2906
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

_source line 112_

Both ReconVLA fixes applied. Now let me fix the ACP+CBF bib title which is incorrect.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "d5517c69-6bbd-4570-9073-7c1eb9dcea0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMbngzHGZbS84A9cnCaKUp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 82869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2906
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

_source line 113_

<details open><summary>🔧 Tool call — Edit · `toolu_011pzHaBiBaUxymJWt6bMyQh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
  "old_string": "    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},",
  "new_string": "    title={Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "55194e61-62d3-419a-8275-76aea75230bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMbngzHGZbS84A9cnCaKUp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 82869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2906
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

_source line 114 · 2026-05-15T20:52:10.301Z_

<details><summary>↩ Tool result · reported error · `toolu_011pzHaBiBaUxymJWt6bMyQh`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "a248550e-40ec-49d4-839c-b4738b414871",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 115_

<details open><summary>🔧 Tool call — Read · `toolu_01NaHmos4wEj6UBD11o6T988`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
  "offset": 305,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "d5787ee5-871e-40e6-800e-c9ab05cfcf3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eb9TKUacNTc6PKZe6EDujo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 85775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 712
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

_source line 116 · 2026-05-15T20:52:14.271Z_

<details><summary>↩ Tool result · `toolu_01NaHmos4wEj6UBD11o6T988`</summary>

```text
305	    primaryClass={cs.RO}
306	}
307	
308	@inproceedings{zhou2025acp_cbf,
309	    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},
310	    author={Hao Zhou and Yanze Zhang and Wenhao Luo},
311	    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
312	    year={2025},
313	    note={arXiv:2503.17678}
314	}
315	
316	@misc{zollo2025vla_calibration,
317	    title={Confidence Calibration in Vision-Language-Action Models},
318	    author={Thomas Zollo and Richard Zemel},
319	    year={2025},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "04b5a4c3-f5b1-4d95-8cee-9930d3260fe2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
      "content": "    primaryClass={cs.RO}\n}\n\n@inproceedings{zhou2025acp_cbf,\n    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},\n    author={Hao Zhou and Yanze Zhang and Wenhao Luo},\n    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n    year={2025},\n    note={arXiv:2503.17678}\n}\n\n@misc{zollo2025vla_calibration,\n    title={Confidence Calibration in Vision-Language-Action Models},\n    author={Thomas Zollo and Richard Zemel},\n    year={2025},",
      "numLines": 15,
      "startLine": 305,
      "totalLines": 368
    }
  }
}
```

</details>

---

### Tool call

_source line 117_

<details open><summary>🔧 Tool call — Edit · `toolu_019ft6oDiVTXzeoK9yu6g5ts`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
  "old_string": "    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},",
  "new_string": "    title={Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "63d0424e-603c-43f6-a6cb-b40d3a4952a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqb4b9xAtTVCpMxw8YhauE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 86487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
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

_source line 118 · 2026-05-15T20:52:17.678Z_

<details><summary>↩ Tool result · `toolu_019ft6oDiVTXzeoK9yu6g5ts`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "8d123959-d7d5-45b7-bb82-bb1b3aff4f4c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
    "oldString": "    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},",
    "newString": "    title={Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction},",
    "originalFile": "@misc{a2c2_2025,\n    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},\n    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},\n    year={2025},\n    eprint={2509.23224},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@article{angelopoulos2023gentle,\n    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},\n    author={Anastasios N. Angelopoulos and Stephen Bates},\n    journal={Foundations and Trends in Machine Learning},\n    year={2023},\n    eprint={2107.07511},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG}\n}\n\n@article{barber2023conformal,\n    title={Conformal Prediction Beyond Exchangeability},\n    author={Rina Foygel Barber and Emmanuel J. Cand{\\`e}s and Aaditya Ramdas and Ryan J. Tibshirani},\n    journal={Annals of Statistics},\n    volume={51},\n    number={2},\n    pages={816--845},\n    year={2023}\n}\n\n@misc{black2024pi0,\n    title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},\n    year={2024},\n    eprint={2410.24164},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{braun2025cgs,\n    title={Multivariate Conformal Prediction via Conformalized Gaussian Scoring},\n    author={Sacha Braun and Eug{\\`e}ne Berta and Michael I. Jordan and Francis Bach},\n    year={2025},\n    eprint={2507.20941},\n    archivePrefix={arXiv},\n    primaryClass={stat.ML}\n}\n\n@misc{brohan2023rt2,\n    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n    author={Anthony Brohan and Noah Brown and Justice Carbajal and Yevgen Chebotar and Xi Chen and Krzysztof Choromanski and Tianli Ding and Danny Driess and Avinava Dubey and Chelsea Finn and Pete Florence and Chuyuan Fu and Montse Gonzalez Arenas and Keerthana Gopalakrishnan and Kehang Han and Karol Hausman and Alexander Herzog and Jasmine Hsu and Brian Ichter and Alex Irpan and Nikhil Joshi and Ryan Julian and Dmitry Kalashnikov and Yuheng Kuang and Isabel Leal and Lisa Lee and Tsang-Wei Edward Lee and Sergey Levine and Yao Lu and Henryk Michalewski and Igor Mordatch and Karl Pertsch and Kanishka Rao and Krista Reymann and Michael Ryoo and Grecia Salazar and Pannag Sanketi and Pierre Sermanet and Jaspiar Singh and Anikait Singh and Radu Soricut and Huong Tran and Vincent Vanhoucke and Quan Vuong and Ayzaan Wahid and Stefan Welker and Paul Wohlhart and Jialin Wu and Fei Xia and Ted Xiao and Peng Xu and Sichun Xu and Tianhe Yu and Brianna Zitkovich},\n    year={2023},\n    eprint={2307.15818},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{chen2026reconvla,\n    title={ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control},\n    author={Lingling Chen and Zongyao Lyu and William J. Beksi},\n    year={2026},\n    eprint={2604.16677},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{cosmos_policy_2026,\n    title={Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning},\n    author={Moo Jin Kim and Yihuai Gao and Tsung-Yi Lin and Yen-Chen Lin and Yunhao Ge and Grace Lam and Percy Liang and Shuran Song and Ming-Yu Liu and Chelsea Finn and Jinwei Gu},\n    year={2026},\n    eprint={2601.16163},\n    archivePrefix={arXiv},\n    primaryClass={cs.AI}\n}\n\n@misc{digflow2025,\n    title={DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models},\n    author={Wanpeng Zhang and Ye Wang and Hao Luo and Haoqi Yuan and Yicheng Feng and Sipeng Zheng and Qin Jin and Zongqing Lu},\n    year={2025},\n    eprint={2512.01715},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{fei2025liberoplus,\n    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},\n    author={Senyu Fei and Siyin Wang and Junhao Shi and Zihao Dai and Jikun Cai and Pengfang Qian and Li Ji and Xinzhe He and Shiduo Zhang and Zhaoye Fei and Jinlan Fu and Jingjing Gong and Xipeng Qiu},\n    year={2025},\n    eprint={2510.13626},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{gal2016dropout,\n    title={Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n    author={Yarin Gal and Zoubin Ghahramani},\n    booktitle={International Conference on Machine Learning (ICML)},\n    year={2016}\n}\n\n@misc{ghosh2024octo,\n    title={Octo: An Open-Source Generalist Robot Policy},\n    author={Dibya Ghosh and Homer Walke and Karl Pertsch and Kevin Black and Oier Mees and Sudeep Dasari and Joey Hejna and Tobias Kreiman and Charles Xu and Jianlan Luo and You Liang Tan and Lawrence Yunliang Chen and Pannag Sanketi and Quan Vuong and Ted Xiao and Dorsa Sadigh and Chelsea Finn and Sergey Levine},\n    year={2024},\n    eprint={2405.12213},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{gibbs2021aci,\n    title={Adaptive Conformal Inference Under Distribution Shift},\n    author={Isaac Gibbs and Emmanuel Cand{\\`e}s},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2021}\n}\n\n@inproceedings{gu2025safe,\n    title={SAFE: Multitask Failure Detection for Vision-Language-Action Models},\n    author={Qiao Gu and Yuanliang Ju and Shengxiang Sun and Igor Gilitschenski and Haruki Nishimura and Masha Itkina and Florian Shkurti},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2025}\n}\n\n@misc{kim2024openvla,\n    title={OpenVLA: An Open-Source Vision-Language-Action Model},\n    author={Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},\n    year={2024},\n    eprint={2406.09246},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n    title={Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n    author={Balaji Lakshminarayanan and Alexander Pritzel and Charles Blundell},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2017}\n}\n\n@article{ledoit2004well,\n    title={A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices},\n    author={Olivier Ledoit and Michael Wolf},\n    journal={Journal of Multivariate Analysis},\n    volume={88},\n    number={2},\n    pages={365--411},\n    year={2004}\n}\n\n@inproceedings{lipman2023flow,\n    title={Flow Matching for Generative Modeling},\n    author={Yaron Lipman and Ricky T. Q. Chen and Heli Ben-Hamu and Maximilian Nickel and Matt Le},\n    booktitle={International Conference on Learning Representations (ICLR)},\n    year={2023}\n}\n\n@inproceedings{liu2023libero,\n    title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n    author={Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2023}\n}\n\n@misc{liu2026ttvla,\n    title={On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning},\n    author={Changyu Liu and Yiyang Liu and Taowen Wang and Qiao Zhuang and James Chenhao Liang and Wenhao Yang and Renjing Xu and Qifan Wang and Dongfang Liu and Cheng Han},\n    year={2026},\n    eprint={2601.06748},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{luan2026snapflow,\n    title={SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation},\n    author={Wuyang Luan and Junhui Li and Weiguang Zhao and Wenjian Zhang and Tieru Wu and Rui Ma},\n    year={2026},\n    eprint={2604.05656},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{robustvla2025,\n    title={RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models},\n    author={Hongyin Zhang and Shuo Zhang and Junxi Jin and Qixin Zeng and Runze Li and Donglin Wang},\n    year={2025},\n    eprint={2511.01331},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{romano2019cqr,\n    title={Conformalized Quantile Regression},\n    author={Yaniv Romano and Evan Patterson and Emmanuel J. Cand{\\`e}s},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2019}\n}\n\n@article{shafer2008tutorial,\n    title={A Tutorial on Conformal Prediction},\n    author={Glenn Shafer and Vladimir Vovk},\n    journal={Journal of Machine Learning Research},\n    volume={9},\n    pages={371--421},\n    year={2008}\n}\n\n@misc{shukor2025smolvla,\n    title={SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n    author={Mustafa Shukor and Dana Aubakirova and Francesco Capuano and Pepijn Kooijmans and Steven Palma and Adil Zouitine and Michel Aractingi and Caroline Pascal and Martino Russi and Andres Marafioti and Simon Alibert and Matthieu Cord and Thomas Wolf and Remi Cadene},\n    year={2025},\n    eprint={2506.01844},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{srpo2025,\n    title={SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models},\n    author={Senyu Fei and Siyin Wang and Li Ji and Ao Li and Shiduo Zhang and Liming Liu and Jinlong Hou and Jingjing Gong and Xianzhong Zhao and Xipeng Qiu},\n    year={2025},\n    eprint={2511.15605},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{vla_gse_2026,\n    title={VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts},\n    author={Yuhua Jiang and Junjie Lu and Xinyao Qin and Xiaoyu Chen and Kaixin Wang and Feifei Gao and Li Zhao},\n    year={2026},\n    eprint={2605.06175},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{wang2025cploop,\n    title={Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization},\n    author={Han Wang and Chao Ning},\n    year={2025},\n    eprint={2510.16376},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{xing2026diu,\n    title={Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching},\n    author={Jiarui Xing and Song Wang and Jian Wang},\n    year={2026},\n    eprint={2605.00941},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG}\n}\n\n@misc{yuan2026ups,\n    title={When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering},\n    author={Jessie Yuan and Yilin Wu and Andrea Bajcsy},\n    year={2026},\n    eprint={2602.22474},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{chi2023diffusion_policy,\n    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n    author={Cheng Chi and Zhenjia Xu and Siyuan Feng and Eric Cousineau and Benjamin Burchfiel and Shuran Song},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2023},\n    note={Also published in IJRR 2024. arXiv:2303.04137}\n}\n\n@inproceedings{zhao2024conformalized,\n    title={Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions},\n    author={Michelle Zhao and Reid Simmons and Henny Admoni and Andrea Bajcsy},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2024}\n}\n\n@inproceedings{silver2018residual,\n    title={Residual Policy Learning},\n    author={Tom Silver and Kelsey Allen and Josh Tenenbaum and Leslie Kaelbling},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2018},\n    note={arXiv:1812.06298}\n}\n\n@inproceedings{jiang2024transic,\n    title={TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction},\n    author={Yunfan Jiang and Chen Wang and Ruohan Zhang and Jiajun Wu and Li Fei-Fei},\n    booktitle={Conference on Robot Learning (CoRL)},\n    year={2024},\n    note={arXiv:2405.10315}\n}\n\n@inproceedings{xiao2026pld,\n    title={Self-Improving Vision-Language-Action Models with Data Generation via Residual RL},\n    author={Wenli Xiao and others},\n    booktitle={International Conference on Learning Representations (ICLR)},\n    year={2026},\n    note={arXiv:2511.00091}\n}\n\n@misc{pan2025drc,\n    title={DRC: Decaying Relative Correction for Policy Refinement},\n    author={Xinjie Pan and Ruizhe Shi and Dongjie Yu and Zhiyuan Nan and Xiaowei Hu and Muxin Wei and Pengfei Li and Xin Li and Zhixiang Wang and Liang Gao and Xue Liu},\n    year={2025},\n    eprint={2503.15368},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{zhou2025acp_cbf,\n    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},\n    author={Hao Zhou and Yanze Zhang and Wenhao Luo},\n    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n    year={2025},\n    note={arXiv:2503.17678}\n}\n\n@misc{zollo2025vla_calibration,\n    title={Confidence Calibration in Vision-Language-Action Models},\n    author={Thomas Zollo and Richard Zemel},\n    year={2025},\n    eprint={2507.17383},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{ross2011dagger,\n    title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},\n    author={St{\\'e}phane Ross and Geoffrey J. Gordon and J. Andrew Bagnell},\n    booktitle={International Conference on Artificial Intelligence and Statistics (AISTATS)},\n    year={2011}\n}\n\n@misc{tang2026shifting,\n    title={Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model},\n    author={Yanchuan Tang and Taowen Wang and Yuefei Chen and Boxuan Zhang and Qiang Guan and Ruixiang Tang},\n    year={2026},\n    eprint={2603.18342},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{liu2026scvla,\n    title={Self-Correcting VLA: Online Action Refinement via Sparse World Imagination},\n    author={Chenyv Liu and Wentao Tan and Lei Zhu and Fengling Li and Jingjing Li and Guoli Yang and Heng Tao Shen},\n    year={2026},\n    eprint={2602.21633},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{li2025vlapilot,\n    title={Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion},\n    author={Zhuo Li and Junjia Liu and Zhipeng Dong and Tao Teng and Quentin Rouxel and Darwin Caldwell and Fei Chen},\n    year={2025},\n    eprint={2511.14178},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{zhong2026acotvla,\n    title={ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models},\n    author={Linqing Zhong and Yi Liu and Yifei Wei and Ziyu Xiong and Maoqing Yao and Si Liu and Guanghui Ren},\n    year={2026},\n    eprint={2601.11404},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO},\n    booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 306,
        "oldLines": 7,
        "newStart": 306,
        "newLines": 7,
        "lines": [
          " }",
          " ",
          " @inproceedings{zhou2025acp_cbf,",
          "-    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},",
          "+    title={Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction},",
          "     author={Hao Zhou and Yanze Zhang and Wenhao Luo},",
          "     booktitle={IEEE International Conference on Robotics and Automation (ICRA)},",
          "     year={2025},"
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

_source line 119_

Now let me verify the edits were applied correctly by reading the modified sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "d83096fe-e64f-4326-9286-b10b2284083f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUdMp2DtqkoKWk8SsaxyPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 86828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 256
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

_source line 120_

<details open><summary>🔧 Tool call — Read · `toolu_01CEYdsFVj2AcRJu5x8LnicV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
  "offset": 13,
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
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "e65b12aa-0e8c-478c-8ba5-80111a5055a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUdMp2DtqkoKWk8SsaxyPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 86828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 256
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

_source line 121 · 2026-05-15T20:52:21.221Z_

<details><summary>↩ Tool result · `toolu_01CEYdsFVj2AcRJu5x8LnicV`</summary>

```text
13	\emph{Inference-time methods} leave the policy frozen.
14	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.
15	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\,s per control step---too slow for real-time manipulation.
16	A2C2~\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.
17	In short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "03c25ec5-6125-4dcb-a97f-5e59d853055c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
      "content": "\\emph{Inference-time methods} leave the policy frozen.\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step---too slow for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.\nIn short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.",
      "numLines": 5,
      "startLine": 13,
      "totalLines": 67
    }
  }
}
```

</details>

---

### Tool call

_source line 122_

<details open><summary>🔧 Tool call — Read · `toolu_018C3FgqYthaHjSLo7ZHP677`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "offset": 14,
  "limit": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "0a9b97cb-0303-4694-9b44-4a45cd603eff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUdMp2DtqkoKWk8SsaxyPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 86828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 256
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

_source line 123 · 2026-05-15T20:52:21.911Z_

<details><summary>↩ Tool result · `toolu_018C3FgqYthaHjSLo7ZHP677`</summary>

```text
14	\paragraph{Inference-time methods.}
15	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.
16	SC-VLA~\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "38464812-ca79-4867-b865-56d29206689d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
      "content": "\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.",
      "numLines": 3,
      "startLine": 14,
      "totalLines": 66
    }
  }
}
```

</details>

---

### Assistant

_source line 124_

All three fixes applied. Now let me write the full audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "1029c32a-95e8-406a-b0fc-bc466832397a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171CjBoMDk3Dz8bxkzPLqH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 87084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 656
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

_source line 125_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01K5Vean7wdY5hEBCYNw1t5e`</summary>

```json
{
  "name": "reference_audit_r2",
  "type": "report",
  "description": "Method attribution audit for all citations in the ACR-VLA paper (intro, method, experiments, related work, discussion). Verified each citation's method description against the actual paper via web search.",
  "project": "acr-vla-conformal-refinement",
  "content_filename": "reference_audit_r2.md",
  "content": "# Method Attribution Audit — ACR-VLA Paper (R2)\n\n**Date**: 2026-05-15\n**Scope**: All citations across Introduction, Method, Experiments, Related Work, Discussion sections\n**Method**: Web search verification of each citation's method description against actual paper content\n\n---\n\n## Summary\n\n- **Total citations audited**: 30 unique references\n- **Critical errors found & fixed**: 2 (ReconVLA attribution in intro + related work)\n- **Bib title error found & fixed**: 1 (ACP+CBF)\n- **Minor issues flagged**: 2 (SC-VLA classification, LIBERO-Plus specific numbers)\n- **All other attributions**: ✅ Verified correct\n\n---\n\n## FIXED: ReconVLA (chen2026reconvla) — CRITICAL\n\n### Error\n**Intro**: \"operates as an uncertainty quantification framework rather than an action improvement method\"\n**Related Work**: \"providing a principled uncertainty quantification framework that operates without retraining but does not modify the VLA's actions\"\n\n### Reality\nReconVLA uses CQR-based uncertainty estimation to **guide action selection** under generative variability and performs OOD/failure detection. It DOES influence action selection, contradicting \"does not modify the VLA's actions.\"\n\n### Fix Applied\n**Intro**: → \"applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.\"\n**Related Work**: → \"applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.\"\n\n### D034 Alignment\nNow correctly positions ReconVLA as a **UQ-guided approach** (same domain, different route) rather than a direct competitor or a passive UQ tool. The gap statement (\"no existing inference-time method combines multi-sample conformal selection with bounded residual correction\") remains valid since ReconVLA does UQ-guided selection but not learned residual correction.\n\n---\n\n## FIXED: ACP+CBF Bib Title (zhou2025acp_cbf)\n\n### Error\nBib entry title: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"\nActual paper title: \"Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction\"\n\n### Fix Applied\nUpdated bib entry title to match actual paper.\n\n---\n\n## FLAGGED (not changed): SC-VLA \"residual RL\" Classification\n\n### Current Text\n\"SC-VLA performs online action refinement through sparse world imagination combined with residual RL\"\n\n### Observation\nSC-VLA uses an Online Action Refinement (OAR) module with progress-dependent dense rewards and residual adjustments. The term \"residual RL\" is defensible (it does use RL with residual adjustments) but could be confused with the RPL framework (Silver et al.). More precise would be \"RL-based action refinement with progress-dependent rewards.\"\n\n### Recommendation\nMinor issue — acceptable as-is. Consider \"online RL\" instead of \"residual RL\" if a future revision refines the taxonomy.\n\n---\n\n## FLAGGED (not changed): LIBERO-Plus Specific Numbers\n\n### Current Text (Intro)\n\"π₀ drops from 94.2% to 6.6% under robot initial-state perturbation, and UniVLA from 95.2% to 4.3% under camera viewpoint changes\"\n\n### Observation\n- LIBERO-Plus tests π0, π0-fast, UniVLA, OpenVLA-OFT among others\n- Web search confirms UniVLA achieves ~95.5% baseline (close to cited 95.2%)\n- General trend (dramatic drops under perturbation) is confirmed\n- Exact numbers (94.2%, 6.6%, 95.2%, 4.3%) could not be precisely verified via web search alone\n\n### Recommendation\nVerify exact numbers against LIBERO-Plus Table 1 before submission. The general claim is sound.\n\n---\n\n## Verified Correct: All Other Citations\n\n### Training-time VLA Robustness\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `robustvla2025` | RL post-training + Jacobian regularization + smoothness regularization | ✅ Confirmed |\n| `srpo2025` | Self-referential RL fine-tuning, own successful rollouts as references, latent world model | ✅ Confirmed |\n| `digflow2025` | Distributional discrepancy as gating signal to rebalance representation-level control | ✅ Confirmed |\n| `liu2026ttvla` | Test-time RL with step-by-step progress rewards | ✅ Confirmed |\n\n### Inference-time VLA Methods\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `a2c2_2025` | Lightweight per-step correction head for action chunks, no selection stage | ✅ Confirmed |\n| `li2025vlapilot` | Evolutionary diffusion optimization + MLLM verifier, 2.41s/step | ✅ Confirmed |\n| `liu2026scvla` | Online action refinement via sparse world imagination + RL | ✅ (see flag above) |\n\n### Conformal Prediction in Robotics\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `angelopoulos2023gentle` | Distribution-free coverage guarantees under exchangeability | ✅ Confirmed |\n| `braun2025cgs` | CGS: Mahalanobis-based nonconformity scores for multivariate CP | ✅ Confirmed |\n| `zhao2024conformalized` | CP for high-DOF action mappings in shared autonomy teleoperation | ✅ Confirmed |\n| `wang2025cploop` | CP regions as feedback constraints in trajectory optimization | ✅ Confirmed |\n| `zhou2025acp_cbf` | Adaptive CP + control barrier functions for safe RL | ✅ Confirmed |\n\n### Residual Policy Learning\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `silver2018residual` | Introduced RPL framework for classical controllers, zero-initialization | ✅ Confirmed |\n| `jiang2024transic` | Gated residual policy for sim-to-real transfer | ✅ Confirmed |\n| `xiao2026pld` | Frozen VLA + lightweight residual actors + off-policy RL + distillation | ✅ Confirmed |\n| `pan2025drc` | Decaying relative correction for online imitation learning via teleoperation | ✅ Confirmed |\n\n### Uncertainty Quantification for VLAs\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `xing2026diu` | Closed-form posterior covariance via velocity field divergence (single-pass) | ✅ Confirmed |\n| `gu2025safe` | Multitask failure detector on VLA features + functional CP calibration | ✅ Confirmed |\n| `zollo2025vla_calibration` | First systematic VLA calibration study, prompt ensembles + Platt scaling | ✅ Confirmed |\n\n### Foundation / Infrastructure\n| Citation | Attribution | Verdict |\n|----------|-----------|---------|\n| `black2024pi0` | π₀: flow-matching VLA | ✅ |\n| `shukor2025smolvla` | SmolVLA: 450M flow-matching VLA | ✅ |\n| `lipman2023flow` | Flow matching for generative modeling | ✅ |\n| `liu2023libero` | LIBERO benchmark | ✅ |\n| `fei2025liberoplus` | LIBERO-Plus robustness analysis | ✅ (numbers flagged) |\n| `ledoit2004well` | Ledoit-Wolf shrinkage covariance estimation | ✅ |\n| `ross2011dagger` | DAgger / compounding error in imitation learning | ✅ |\n\n---\n\n## Pre-Submission Checklist\n- [x] ReconVLA attribution fixed (intro + related work)\n- [x] ACP+CBF bib title corrected\n- [ ] Verify LIBERO-Plus exact numbers (94.2%, 6.6%, 95.2%, 4.3%) against Table 1\n- [ ] Consider refining SC-VLA \"residual RL\" → \"online RL\" (optional)\n",
  "tags": [
    "audit",
    "paper",
    "references",
    "corl-submission"
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
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "bc6e50b5-f4b6-4f40-8608-9f83899ec865",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171CjBoMDk3Dz8bxkzPLqH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 87084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 656
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

_source line 126 · 2026-05-15T20:53:09.153Z_

<details><summary>↩ Tool result · `toolu_01K5Vean7wdY5hEBCYNw1t5e`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_fa22d2\", \"name\": \"reference_audit_r2\", \"type\": \"report\", \"description\": \"Method attribution audit for all citations in the ACR-VLA paper (intro, method, experiments, related work, discussion). Verified each citation's method description against the actual paper via web search.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/reference_audit_r2.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T20:53:08.961788+00:00\", \"tags\": [\"audit\", \"paper\", \"references\", \"corl-submission\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "4bfe8472-f32d-4c0f-896f-1bf6ee3d0e4b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_fa22d2\\\", \\\"name\\\": \\\"reference_audit_r2\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Method attribution audit for all citations in the ACR-VLA paper (intro, method, experiments, related work, discussion). Verified each citation's method description against the actual paper via web search.\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/report/reference_audit_r2.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T20:53:08.961788+00:00\\\", \\\"tags\\\": [\\\"audit\\\", \\\"paper\\\", \\\"references\\\", \\\"corl-submission\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_fa22d2\", \"name\": \"reference_audit_r2\", \"type\": \"report\", \"description\": \"Method attribution audit for all citations in the ACR-VLA paper (intro, method, experiments, related work, discussion). Verified each citation's method description against the actual paper via web search.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/reference_audit_r2.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T20:53:08.961788+00:00\", \"tags\": [\"audit\", \"paper\", \"references\", \"corl-submission\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 127_

Audit complete. Here's the summary:

### Fixes Applied (3)

1. **ReconVLA intro** — Changed "operates as an uncertainty quantification framework rather than an action improvement method" → correctly describes it as using UQ for **action selection and OOD detection**, taking a "complementary UQ-driven approach rather than learning explicit corrective residuals"

2. **ReconVLA related work** — Changed "does not modify the VLA's actions" → correctly states it "enables uncertainty-guided action selection and proactive failure detection without retraining"

3. **ACP+CBF bib title** — Corrected from fabricated title to actual paper title "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction"

### Flagged for Pre-Submission (2, not blocking)

- **LIBERO-Plus numbers** (94.2%→6.6% for π₀, 95.2%→4.3% for UniVLA) — general trend confirmed, exact numbers need verification against Table 1 of the actual paper
- **SC-VLA "residual RL"** — defensible but imprecise; "online RL" would be more accurate

### Verified Correct (27/30 citations)
All other method attributions checked out against the actual papers via web search.

Full report registered as `artifacts/_project/report/reference_audit_r2.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "uuid": "2e46bbf7-5825-4be9-aa79-af23a7a1c6ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ds8fS9t8VQmivL7CiPxSH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2653,
      "cache_read_input_tokens": 87740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2653
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 128_

Audit complete. Here's the summary:

### Fixes Applied (3)

1. **ReconVLA intro** — Changed "operates as an uncertainty quantification framework rather than an action improvement method" → correctly describes it as using UQ for **action selection and OOD detection**, taking a "complementary UQ-driven approach rather than learning explicit corrective residuals"

2. **ReconVLA related work** — Changed "does not modify the VLA's actions" → correctly states it "enables uncertainty-guided action selection and proactive failure detection without retraining"

3. **ACP+CBF bib title** — Corrected from fabricated title to actual paper title "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction"

### Flagged for Pre-Submission (2, not blocking)

- **LIBERO-Plus numbers** (94.2%→6.6% for π₀, 95.2%→4.3% for UniVLA) — general trend confirmed, exact numbers need verification against Table 1 of the actual paper
- **SC-VLA "residual RL"** — defensible but imprecise; "online RL" would be more accurate

### Verified Correct (27/30 citations)
All other method attributions checked out against the actual papers via web search.

Full report registered as `artifacts/_project/report/reference_audit_r2.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 446100,
  "duration_api_ms": 586275,
  "num_turns": 48,
  "stop_reason": "end_turn",
  "session_id": "66e1f82c-860b-4f8b-871c-9191060ea996",
  "total_cost_usd": 2.2003134999999996,
  "usage": {
    "input_tokens": 4248,
    "cache_creation_input_tokens": 78552,
    "cache_read_input_tokens": 1137603,
    "output_tokens": 18745,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 78552,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 331,
        "cache_read_input_tokens": 87740,
        "cache_creation_input_tokens": 2653,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2653
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 344967,
      "outputTokens": 11146,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 25,
      "costUSD": 0.6506970000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4248,
      "outputTokens": 18745,
      "cacheReadInputTokens": 1137603,
      "cacheCreationInputTokens": 78552,
      "webSearchRequests": 0,
      "costUSD": 1.5496165,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0175147f-e53d-4d8b-a43e-7ed434d58f2d"
}
```

</details>

---
