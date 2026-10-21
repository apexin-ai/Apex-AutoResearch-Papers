# writing d070 d071 paper revision — Part 1 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[Transcript overview](../writing-d070-d071-paper-revision.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/5a/5ad3e857ec900b7897ee.json)

## Before a recorded user message

## Before a recorded user message

195 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "72490193-a71f-4c68-ac59-a87b96e45179",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1778854800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d0a79163-2b2a-49fc-852f-68962a4380b1",
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
This is a large-scale paper revision task with 21+ items. Let me start by reading the current paper sections and the artifact files to understand what I'm working with.

Let me first load the necessary MCP tools, then read the project files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "e2859dc3-5d44-470e-819c-e588e31746d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjxA9TGz8kLrk9AaGeuNZY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13549,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13549
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

我先加载工具并读取论文当前状态和数据文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "474da292-7c6b-410a-9170-b2a9915d6428",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjxA9TGz8kLrk9AaGeuNZY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13549,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13549
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XfKsHFubwdZDyEuFdNtHp6`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__edit_paper_section,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__write_paper_section,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "b3f8a0d2-1f67-4164-a8c5-34975b0f2203",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjxA9TGz8kLrk9AaGeuNZY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13549,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13549
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

_source line 7 · 2026-05-15T09:34:26.384Z_

<details><summary>↩ Tool result · `toolu_01XfKsHFubwdZDyEuFdNtHp6`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__write_paper_section"
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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "ed457add-fc34-4a74-8af2-1d704e572418",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__write_paper_section",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__edit_paper_section,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__write_paper_section,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 27
  }
}
```

</details>

---


### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me read all the paper sections and the artifact files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "e70a61b8-0756-4042-bbb7-59e8e5af960d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GMk1gS3ia1RxHT9UFd8P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2564,
      "cache_read_input_tokens": 25390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2564
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

读取论文各章节和数据文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "c4451a8b-86af-48e6-86c2-7180f77a5e31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GMk1gS3ia1RxHT9UFd8P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2564,
      "cache_read_input_tokens": 25390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2564
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013Bm5NE8GbzonehVUTQ9qSm`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper/abstract.tex",
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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "ee87d0bd-bb84-432d-9695-764d2d29df4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GMk1gS3ia1RxHT9UFd8P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2564,
      "cache_read_input_tokens": 25390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2564
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-15T09:34:30.153Z_

<details><summary>↩ Tool result · `toolu_013Bm5NE8GbzonehVUTQ9qSm`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/abstract.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "d1805346-44af-45bc-b253-ff6bc616c6d4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/abstract.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/abstract.tex'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TuxA7R6xjgFHbwSbY6rQ2T`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper/introduction.tex",
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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "f0b307ba-8341-4ffd-bd67-4e3fabe9b99d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GMk1gS3ia1RxHT9UFd8P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2564,
      "cache_read_input_tokens": 25390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2564
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-15T09:34:31.199Z_

<details><summary>↩ Tool result · `toolu_01TuxA7R6xjgFHbwSbY6rQ2T`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/introduction.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "318f7ddf-abd8-4ffe-adc2-dd1359653641",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/introduction.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/introduction.tex'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0187rKYEjS5VcqgrhkRAUHQx`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper/related_work.tex",
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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "878eda3a-4c2f-4f73-9df8-39fe6fa2f7f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GMk1gS3ia1RxHT9UFd8P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2564,
      "cache_read_input_tokens": 25390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2564
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-15T09:34:31.694Z_

<details><summary>↩ Tool result · `toolu_0187rKYEjS5VcqgrhkRAUHQx`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/related_work.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "9b25e3af-ffae-41f2-a97c-8ab08fed6c5a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/related_work.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/related_work.tex'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013h4Y4SQHC4GiPC4iJNAPyG`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper/method.tex",
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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "a27b86aa-6baf-4597-9f68-86bd29c80370",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GMk1gS3ia1RxHT9UFd8P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2564,
      "cache_read_input_tokens": 25390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2564
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-15T09:34:32.658Z_

<details><summary>↩ Tool result · `toolu_013h4Y4SQHC4GiPC4iJNAPyG`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/method.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "8898ede0-03e1-4c3a-ad33-b17f584cce05",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/method.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/method.tex'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PwsqzZwDJsMYG2aNHZvhxe`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper/experiments.tex",
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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "6901e73e-8894-4b63-b67d-8de42438ffee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GMk1gS3ia1RxHT9UFd8P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2564,
      "cache_read_input_tokens": 25390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2564
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-15T09:34:33.369Z_

<details><summary>↩ Tool result · `toolu_01PwsqzZwDJsMYG2aNHZvhxe`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/experiments.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "ffa46e94-80ee-4fce-8564-094919eef7fa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/experiments.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/experiments.tex'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NdoFjdKaguw61uazdC4cPe`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper/discussion.tex",
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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "3d8efd4d-5420-4e1e-b1a9-adef8e2790a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GMk1gS3ia1RxHT9UFd8P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2564,
      "cache_read_input_tokens": 25390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2564
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-15T09:34:33.810Z_

<details><summary>↩ Tool result · `toolu_01NdoFjdKaguw61uazdC4cPe`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/discussion.tex'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "e9397ecb-322a-4df0-a3eb-48182683a5bd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/discussion.tex'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/discussion.tex'\", \"metadata\": {}}"
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
The paper sections are managed by the `write_paper_section` / `edit_paper_section` tools, not `read_project_file`. Let me look for the paper files in the project directory structure, and also check if there's a way to read paper sections. Let me explore the artifacts directory and figure out where paper sections are stored.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "451d9e2b-6594-4c50-8773-49d1772b1671",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZqYLBogs3qEK9Ppf11Fio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 27954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

Paper sections 不通过 `read_project_file` 读取。让我找到实际文件位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "597bfa56-c017-453f-8423-d18068b02cbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZqYLBogs3qEK9Ppf11Fio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 27954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01QJrGjTZpkYQRLPBcqjvMTg`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "4a62276b-7ebe-4b70-b8f0-da5b583f93f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZqYLBogs3qEK9Ppf11Fio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 27954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-15T09:34:39.761Z_

<details><summary>↩ Tool result · `toolu_01QJrGjTZpkYQRLPBcqjvMTg`</summary>

```text
artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/discussion.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/limitations.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
artifacts/bootstrap_ci_tables.tex
docs/paper/sections/abstract.tex
docs/paper/main.tex
docs/paper/sections/related_work.tex
docs/paper/sections/experiments.tex
docs/paper/sections/introduction.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/limitations.tex
docs/paper/sections/method.tex
docs/paper/sections/discussion.tex
docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "a547a5f4-6acf-4c48-bb04-aac377ee153a",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260514T093336/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T093336/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T093336/worst/paper.tex",
      "artifacts/dream_reports/dream_20260514T105303/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T105303/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T105303/worst/paper.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/dream_reports/dream_20260514T203201/best/paper.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/dream_reports/dream_20260514T203201/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T203201/worst/paper.tex",
      "artifacts/bootstrap_ci_tables.tex",
      "docs/paper/sections/abstract.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/experiments.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/limitations.tex",
      "docs/paper/sections/method.tex",
      "docs/paper/sections/discussion.tex",
      "docs/paper/sections/appendix.tex"
    ],
    "durationMs": 30,
    "numFiles": 27,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Glob · `toolu_01UDtesNahrSKa9MEdzDk2eW`</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "e8c91419-6677-4b79-bf7d-4ae059db45a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZqYLBogs3qEK9Ppf11Fio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 27954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-15T09:34:40.717Z_

<details><summary>↩ Tool result · `toolu_01UDtesNahrSKa9MEdzDk2eW`</summary>

```text
figures/paper/fig_overview.pdf
figures/paper/fig_selection_gap.pdf
figures/paper/fig_selection_gap.png
figures/paper/fig_reliability_data.json
artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.png
artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.pdf
figures/paper/fig_signal_heatmap.py
figures/paper/fig_signal_heatmap.pdf
figures/paper/fig_signal_heatmap.png
figures/paper/fig_reliability.py
figures/paper/fig_reliability.pdf
figures/paper/fig_reliability.png
figures/paper/fig_selection_curves.pdf
figures/paper/fig_selection_curves.png
docs/paper/acl.sty
docs/paper/acl_natbib.bst
docs/paper/figures/fig_overview.pdf
docs/paper/figures/fig_reliability.pdf
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/limitations.tex
docs/paper/figures/fig_signal_heatmap.pdf
docs/paper/figures/fig_selection_gap.pdf
docs/paper/figures/fig_temperature_robustness.pdf
docs/paper/figures/fig_length_logprob_scatter.pdf
docs/paper/_pdf_images/main_p6.png
docs/paper/_pdf_images/main_p10.png
docs/paper/_pdf_images/main_p7.png
docs/paper/_pdf_images/main_p8.png
docs/paper/_pdf_images/main_p9.png
docs/paper/_pdf_images/main_p5.png
docs/paper/main.bbl
docs/paper/main.blg
docs/paper/main.aux
docs/paper/main.out
docs/paper/main.fls
docs/paper/main.pdf
docs/paper/main.log
docs/paper/main.fdb_latexmk
docs/paper/_pdf_images/main_p1.png
docs/paper/_pdf_images/main_p2.png
docs/paper/_pdf_images/main_p3.png
docs/paper/_pdf_images/main_p4.png
docs/paper/sections/abstract.tex
docs/paper/main.tex
docs/paper/references.bib
docs/paper/sections/related_work.tex
docs/paper/sections/experiments.tex
docs/paper/sections/introduction.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/limitations.tex
docs/paper/sections/method.tex
docs/paper/sections/discussion.tex
docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "fce0bcb1-33f8-468f-b928-c15c91bccf39",
  "tool_use_result": {
    "filenames": [
      "figures/paper/fig_overview.pdf",
      "figures/paper/fig_selection_gap.pdf",
      "figures/paper/fig_selection_gap.png",
      "figures/paper/fig_reliability_data.json",
      "artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.png",
      "artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.pdf",
      "figures/paper/fig_signal_heatmap.py",
      "figures/paper/fig_signal_heatmap.pdf",
      "figures/paper/fig_signal_heatmap.png",
      "figures/paper/fig_reliability.py",
      "figures/paper/fig_reliability.pdf",
      "figures/paper/fig_reliability.png",
      "figures/paper/fig_selection_curves.pdf",
      "figures/paper/fig_selection_curves.png",
      "docs/paper/acl.sty",
      "docs/paper/acl_natbib.bst",
      "docs/paper/figures/fig_overview.pdf",
      "docs/paper/figures/fig_reliability.pdf",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/limitations.tex",
      "docs/paper/figures/fig_signal_heatmap.pdf",
      "docs/paper/figures/fig_selection_gap.pdf",
      "docs/paper/figures/fig_temperature_robustness.pdf",
      "docs/paper/figures/fig_length_logprob_scatter.pdf",
      "docs/paper/_pdf_images/main_p6.png",
      "docs/paper/_pdf_images/main_p10.png",
      "docs/paper/_pdf_images/main_p7.png",
      "docs/paper/_pdf_images/main_p8.png",
      "docs/paper/_pdf_images/main_p9.png",
      "docs/paper/_pdf_images/main_p5.png",
      "docs/paper/main.bbl",
      "docs/paper/main.blg",
      "docs/paper/main.aux",
      "docs/paper/main.out",
      "docs/paper/main.fls",
      "docs/paper/main.pdf",
      "docs/paper/main.log",
      "docs/paper/main.fdb_latexmk",
      "docs/paper/_pdf_images/main_p1.png",
      "docs/paper/_pdf_images/main_p2.png",
      "docs/paper/_pdf_images/main_p3.png",
      "docs/paper/_pdf_images/main_p4.png",
      "docs/paper/sections/abstract.tex",
      "docs/paper/main.tex",
      "docs/paper/references.bib",
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/experiments.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/limitations.tex",
      "docs/paper/sections/method.tex",
      "docs/paper/sections/discussion.tex",
      "docs/paper/sections/appendix.tex"
    ],
    "durationMs": 28,
    "numFiles": 58,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Glob · `toolu_01Do2jUueMEvXY9ug2WAaQXb`</summary>

```json
{
  "pattern": "**/artifacts/**/*tost*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "0da18a9a-c1d1-4398-8335-9b5c10102c7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZqYLBogs3qEK9Ppf11Fio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 27954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-15T09:34:41.199Z_

<details><summary>↩ Tool result · `toolu_01Do2jUueMEvXY9ug2WAaQXb`</summary>

```text
artifacts/_project/data/tost_breakpoint_delta_star.md
artifacts/tost_breakpoint_delta_star.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "bca9f221-cee8-44aa-9d59-e0893ad1796b",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/data/tost_breakpoint_delta_star.md",
      "artifacts/tost_breakpoint_delta_star.md"
    ],
    "durationMs": 28,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Glob · `toolu_019ekeznng6sQTDyG5DbjrWP`</summary>

```json
{
  "pattern": "**/artifacts/**/*qwen3*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "a04d9cbc-8a33-4932-8aa7-df124888f3a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZqYLBogs3qEK9Ppf11Fio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 27954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-15T09:34:42.214Z_

<details><summary>↩ Tool result · `toolu_019ekeznng6sQTDyG5DbjrWP`</summary>

```text
artifacts/_project/report/qwen3_thinking_confirmation.md
artifacts/qwen3_thinking_confirmation.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "47480366-ace6-4609-9b81-322128dbc0da",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/report/qwen3_thinking_confirmation.md",
      "artifacts/qwen3_thinking_confirmation.md"
    ],
    "durationMs": 36,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Glob · `toolu_019xYNxYeUWrWhmXhqSGZxoL`</summary>

```json
{
  "pattern": "**/artifacts/**/*vc*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "e2be5055-436f-44cf-9d44-bcb0889c03c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZqYLBogs3qEK9Ppf11Fio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 27954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-15T09:34:42.601Z_

<details><summary>↩ Tool result · `toolu_019xYNxYeUWrWhmXhqSGZxoL`</summary>

```text
artifacts/_project/report/vc_implementation_rho_diff.md
artifacts/vc_implementation_rho_diff.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "3929c726-8d34-4c79-b771-e528cac4b963",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/report/vc_implementation_rho_diff.md",
      "artifacts/vc_implementation_rho_diff.md"
    ],
    "durationMs": 28,
    "numFiles": 2,
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
Now I see the paper sections are in `artifacts/_project/paper/` (the managed ones) and also in `docs/paper/sections/`. The `edit_paper_section` tool likely operates on the `artifacts/_project/paper/` versions. Let me read all the paper sections and the 3 artifact data files. There's also a method.tex in docs/paper/sections/ but not in artifacts/_project/paper/. Let me read all of them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "955dc891-04f0-486c-b106-69adf73a8362",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqLf5z6UMyVFJ4oNjmCVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 29702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

找到文件了。现在并行读取所有论文章节和数据文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "853a3357-7429-486c-90f3-7233d61086e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqLf5z6UMyVFJ4oNjmCVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 29702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01EAAynCf6B2GorchdhS8BZp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "f3285d87-5088-4772-9f39-50bcc48c041c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqLf5z6UMyVFJ4oNjmCVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 29702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-15T09:34:47.894Z_

<details><summary>↩ Tool result · `toolu_01EAAynCf6B2GorchdhS8BZp`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "148e1784-3b25-4765-a88b-8ad548974744",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.\nWe systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).\nWe find that entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).\nWe term this disconnect the \\textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.\nSignal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.\nThese results reframe consistency signals as quality estimators rather than output selectors for structured IE.\n\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---


### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01W4Uvwta8oGhbtGMtSv1jzQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "a1c9b4eb-8775-4e9b-84c9-f5634462f2df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqLf5z6UMyVFJ4oNjmCVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 29702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-15T09:34:48.995Z_

<details><summary>↩ Tool result · `toolu_01W4Uvwta8oGhbtGMtSv1jzQ`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives.
14	\textit{Quality estimation} asks which inputs the model handles reliably---a ranking over instances.
15	\textit{Sample selection} asks which of $N$ candidate outputs is best for a given input---a ranking over samples.
16	These require fundamentally different signal properties: the former benefits from instance-level aggregation across all $N$ samples, while the latter demands per-sample discrimination.
17	Existing evaluations rarely separate the two.
18	Self-consistency methods designed for discrete answers \cite{wang2023selfconsistency, chen2024usc} assume outputs can be grouped by equivalence and counted, an assumption that breaks when outputs are entity sets with partial overlap.
19	Weighted variants that incorporate model confidence \cite{taubenfeld2025cisc, kang2025selfcertainty} have shown promise for best-of-$N$ selection on reasoning tasks, but their applicability to structured prediction remains untested.
20	The most directly relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based entity and relation extraction but relies on surface-level matching, a limitation the authors themselves acknowledge: their approach ``overlooks semantically consistent outputs'' that differ only in surface form.
21	No existing work systematically compares confidence signals across the structural, surface, and model-internal families for generative IE, nor disentangles quality estimation from sample selection in this setting.
22	
23	Our central finding is that consistency-based signals are effective instance-level quality estimators but poor sample selectors for structured IE.
24	Consistency signals aggregate over $N$ samples to produce a single score per input, making them well-suited to predict input difficulty---instances where the model consistently extracts similar structures are indeed easier.
25	Entity voting confidence, our best signal, achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, a correlation strong enough to be practically useful for quality-aware routing.
26	Yet this correlation does not translate into selection gains: on NER best-of-$N$, no signal surpasses greedy decoding despite 16 percentage points of oracle headroom.
27	We term this the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}).
28	The gap arises because instance-level signals cannot discriminate among $N$ candidates that share similar consistency profiles---they predict \textit{which inputs} are hard, not \textit{which output} is best.
29	Only log-probability, the sole per-sample signal in our comparison, achieves selection gains, and only on relation extraction (+2.3~pp over greedy), where per-sample variance is higher.
30	We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
31	
32	Our contributions are as follows:
33	\begin{enumerate}
34	    \item \textbf{First systematic comparison of confidence signals for generative IE.}
35	    We evaluate five signals from three families on quality estimation for NER and RE.
36	    Entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$; structural signals outperform surface and model-internal alternatives on complex schemas (SciERC), while surface signals dominate on simpler tasks (CoNLL).
37	
38	    \item \textbf{Identification of the correlation-selection gap.}
39	    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.
40	    Despite strong instance-level correlations ($\rho$ up to 0.50), no consistency signal improves NER best-of-$N$ over greedy decoding; only log-probability helps on RE (+2.3~pp).
41	    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.
42	
43	    \item \textbf{Task-complexity boundary conditions.}
44	    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and all signals converge when model capability is insufficient (WNUT-17, where 54\% of instances receive zero F1).
45	    This establishes practical guidance for signal selection based on expected task difficulty.
46	\end{enumerate}
47	
48	The remainder of this paper is organized as follows.
49	\S\ref{sec:method} formalizes the problem and defines the five confidence signals.
50	\S\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.
51	\S\ref{sec:related} situates our work in the broader landscape of self-consistency, uncertainty estimation, and LLM-based IE.
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "8375696f-0b05-49de-8619-1a200fef4d47",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \\cite{wang2023selfconsistency}.\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives.\n\\textit{Quality estimation} asks which inputs the model handles reliably---a ranking over instances.\n\\textit{Sample selection} asks which of $N$ candidate outputs is best for a given input---a ranking over samples.\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation across all $N$ samples, while the latter demands per-sample discrimination.\nExisting evaluations rarely separate the two.\nSelf-consistency methods designed for discrete answers \\cite{wang2023selfconsistency, chen2024usc} assume outputs can be grouped by equivalence and counted, an assumption that breaks when outputs are entity sets with partial overlap.\nWeighted variants that incorporate model confidence \\cite{taubenfeld2025cisc, kang2025selfcertainty} have shown promise for best-of-$N$ selection on reasoning tasks, but their applicability to structured prediction remains untested.\nThe most directly relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based entity and relation extraction but relies on surface-level matching, a limitation the authors themselves acknowledge: their approach ``overlooks semantically consistent outputs'' that differ only in surface form.\nNo existing work systematically compares confidence signals across the structural, surface, and model-internal families for generative IE, nor disentangles quality estimation from sample selection in this setting.\n\nOur central finding is that consistency-based signals are effective instance-level quality estimators but poor sample selectors for structured IE.\nConsistency signals aggregate over $N$ samples to produce a single score per input, making them well-suited to predict input difficulty---instances where the model consistently extracts similar structures are indeed easier.\nEntity voting confidence, our best signal, achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, a correlation strong enough to be practically useful for quality-aware routing.\nYet this correlation does not translate into selection gains: on NER best-of-$N$, no signal surpasses greedy decoding despite 16 percentage points of oracle headroom.\nWe term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}).\nThe gap arises because instance-level signals cannot discriminate among $N$ candidates that share similar consistency profiles---they predict \\textit{which inputs} are hard, not \\textit{which output} is best.\nOnly log-probability, the sole per-sample signal in our comparison, achieves selection gains, and only on relation extraction (+2.3~pp over greedy), where per-sample variance is higher.\nWe systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{First systematic comparison of confidence signals for generative IE.}\n    We evaluate five signals from three families on quality estimation for NER and RE.\n    Entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$; structural signals outperform surface and model-internal alternatives on complex schemas (SciERC), while surface signals dominate on simpler tasks (CoNLL).\n\n    \\item \\textbf{Identification of the correlation-selection gap.}\n    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.\n    Despite strong instance-level correlations ($\\rho$ up to 0.50), no consistency signal improves NER best-of-$N$ over greedy decoding; only log-probability helps on RE (+2.3~pp).\n    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and all signals converge when model capability is insufficient (WNUT-17, where 54\\% of instances receive zero F1).\n    This establishes practical guidance for signal selection based on expected task difficulty.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:method} formalizes the problem and defines the five confidence signals.\n\\S\\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.\n\\S\\ref{sec:related} situates our work in the broader landscape of self-consistency, uncertainty estimation, and LLM-based IE.\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  }
}
```

</details>

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01P5EGXTh9TiWHZ7YjsQNvGQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "bd3aa560-4706-4c2c-9d25-5fe850e7d04e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqLf5z6UMyVFJ4oNjmCVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 29702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-15T09:34:49.362Z_

<details><summary>↩ Tool result · `toolu_01P5EGXTh9TiWHZ7YjsQNvGQ`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.
12	This gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\S\ref{sec:complexity_robustness}).
13	
14	\paragraph{Models.}
15	Our primary model is \textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.
16	For cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.
17	
18	\paragraph{Sampling and Evaluation.}
19	For each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.
20	We use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.
21	Quality estimation is measured along two axes: \textit{rank correlation} with instance-level F1 via Spearman $\rho$ and Kendall $\tau$, and \textit{binary discrimination} via AUROC (instances above vs.\ below median F1).
22	Downstream utility is assessed through \textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.
23	Instance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.
24	The greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.
25	
26	\paragraph{Confidence Signals.}
27	We compare five signals from three families (detailed in \S\ref{sec:signals}).
28	\textit{Structural} signals operate on extracted entity/relation sets: \textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \textbf{Soft Jaccard (SJ)} measures pairwise set similarity \cite{jaccard1901distribution}.
29	\textit{Surface} signals operate on string representations: \textbf{Fleiss' $\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \cite{fleiss1971agreement}, and \textbf{Exact Match (EM)} computes the fraction of identical sample pairs.
30	The \textit{model-internal} signal is \textbf{log-probability (logprob)}, the mean token-level log-likelihood.
31	
32	\paragraph{Implementation.}
33	Inference uses vLLM with XGrammar constrained decoding \cite{willard2023guided} to enforce valid JSON output structure.
34	A span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.
35	All confidence signals are computed from the $N$ samples without access to gold labels.
36	
37	%% ============================================================
38	\subsection{Quality Estimation Results}
39	\label{sec:qe_results}
40	
41	\begin{table*}[t]
42	\centering
43	\small
44	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}
45	\label{tab:quality_estimation}
46	\begin{tabular}{ll cc cc cc cc}
47	\toprule
48	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
49	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
50	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
51	\midrule
52	Voting Conf. & Structural & \textbf{.502} & \textbf{.728} & \textbf{.422} & \textbf{.716} & .424 & .789 & .426 & .709 \\
53	Soft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \textbf{.431} & .704 \\
54	Fleiss' $\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\
55	Exact Match  & Surface    & .257 & .623 & .100 & .504 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
56	Log-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \textbf{.761} \\
57	\bottomrule
58	\end{tabular}
59	\end{table*}
60	
61	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
62	
63	\paragraph{Structural signals dominate on complex schemas.}
64	On SciERC NER, Voting Confidence achieves $\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\rho{=}0.357$), and all remaining signals ($\rho{\leq}0.265$).
65	Voting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.
66	The structural advantage persists on RE, where Voting ($\rho{=}0.422$) again leads.
67	However, all signals weaken on RE: 44\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.
68	Notably, FK ($\rho{=}0.253$) exceeds SJ ($\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.
69	
70	\paragraph{Signal rankings shift with task difficulty.}
71	On CoNLL NER, where greedy decoding achieves ${>}$91\% micro F1, the signal landscape changes substantially.
72	Exact Match leads with $\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\rho{=}0.436$) and Voting ($\rho{=}0.424$).
73	When most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.
74	This reversal---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.
75	
76	\paragraph{Cross-model stability.}
77	Comparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\rho{=}0.436$ (Qwen) vs.\ $\rho{=}0.431$ (LLaMA), a gap of only 0.005.
78	This model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.
79	The SJ--FK gap also narrows with schema simplification: $\Delta\rho{=}0.092$ on SciERC NER (6 entity types) vs.\ $\Delta\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.
80	
81	\paragraph{The logprob paradox.}
82	Log-probability reveals a dissociation between ranking and classification.
83	On CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\rho$ (0.307) among all signals.
84	This pattern indicates that logprob assigns well-separated scores to easy vs.\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.
85	We return to this distinction in \S\ref{sec:complexity_robustness} and visualize it in Figure~\ref{fig:signal_heatmap}.
86	
87	\paragraph{Oracle headroom and practical ceilings.}
88	On CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.
89	When the model already operates near its performance ceiling, confidence signals serve as \textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.
90	We therefore focus selection analysis (\S\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.
91	
92	%% ============================================================
93	\subsection{The Correlation-Selection Gap}
94	\label{sec:selection_gap}
95	
96	\begin{table}[t]
97	\centering
98	\small
99	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \textbf{bold}. EM produces binary agreement without sample ranking.}
100	\label{tab:selection}
101	\begin{tabular}{lcc}
102	\toprule
103	Method & NER F1 & RE F1 \\
104	\midrule
105	Oracle & 0.769 & 0.561 \\
106	\midrule
107	Log-prob           & 0.609 & \textbf{0.397} \\
108	Ensemble (SJ+Vot.) & 0.604 & 0.367 \\
109	Soft Jaccard       & 0.604 & 0.368 \\
110	Voting             & 0.596 & 0.338 \\
111	Exact Match        & ---   & ---   \\
112	\midrule
113	Greedy ($T{=}0$)   & \textbf{0.609} & 0.374 \\
114	Random             & 0.580 & 0.338 \\
115	\bottomrule
116	\end{tabular}
117	\end{table}
118	
119	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.
120	Table~\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).
121	
122	\paragraph{NER: no signal surpasses greedy.}
123	The oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).
124	Yet no confidence signal closes this gap.
125	Log-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\rho{=}0.502$), selects to only 0.596, \textit{below} greedy.
126	An ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.
127	The greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.
128	The Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.
129	
130	\paragraph{RE: logprob uniquely succeeds.}
131	For RE, log-probability is the only signal to exceed greedy (0.397 vs.\ 0.374, +2.3~pp).
132	Structural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.
133	The oracle gap of 18.7~pp (0.561 vs.\ 0.374) indicates substantially more per-instance variance than NER.
134	Log-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.
135	
136	\paragraph{Quality estimation $\neq$ output selection.}
137	We attribute this gap (Figure~\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best for a given input.
138	When per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.
139	
140	\paragraph{Implications for test-time scaling.}
141	This correlation-selection gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}.
142	Scaling inference compute through repeated sampling assumes a selector can identify the best sample.
143	Our results show that for structured prediction, existing confidence signals serve as quality \textit{estimators}---useful for flagging unreliable predictions---but not as effective \textit{selectors}.
144	Closing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \cite{cobbe2021verifiers} or pairwise comparison models.
145	
146	%% ============================================================
147	\subsection{Task Complexity and Signal Robustness}
148	\label{sec:complexity_robustness}
149	
150	\paragraph{Task difficulty as a boundary condition.}
151	Signal effectiveness varies systematically with task difficulty.
152	On CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\rho{=}0.451$); on SciERC NER (micro F1$\,{\approx}\,$0.66), SJ overtakes EM ($\rho{=}0.357$ vs.\ 0.257); on SciERC RE, where 44\% of instances score zero F1, all signals converge to $\rho{\approx}0.25$.
153	The NER--RE difference is statistically confirmed: Fisher's $z$-test on $\rho_\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.
154	
155	\paragraph{Per-relation diagnostic.}
156	RE signal degradation is relation-specific.
157	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
158	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
159	
160	\paragraph{Capability stratification.}
161	SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
162	The SJ advantage over logprob remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.
163	
164	\paragraph{Method boundary: WNUT-17.}
165	WNUT-17 establishes where the approach breaks down.
166	SJ achieves $\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\% of instances at zero F1.
167	Log-probability shows a strong \textit{negative} correlation ($\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.
168	This is a boundary of the method, not a limitation of the datasets.
169	
170	\begin{table}[t]
171	\centering
172	\small
173	\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\rho$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
174	\label{tab:robustness}
175	\begin{tabular}{llcc}
176	\toprule
177	& & NER $\rho$ & RE $\rho$ \\
178	\midrule
179	\multicolumn{4}{l}{\textit{Temperature} ($N{=}8$)} \\
180	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
181	\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\
182	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
183	\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\
184	\midrule
185	\multicolumn{4}{l}{\textit{Sample size} ($T{=}1.0$)} \\
186	\quad SJ & $N{=}8$  & 0.357 & 0.211 \\
187	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
188	\quad FK & $N{=}8$  & 0.265 & 0.253 \\
189	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
190	\bottomrule
191	\end{tabular}
192	\end{table}
193	
194	\paragraph{Robustness analysis.}
195	Table~\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.
196	\textit{Temperature.}
197	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.
198	FK shows mixed behavior: NER $\rho$ drops by 0.056, while RE $\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
199	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.357 vs.\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
200	
201	\textit{Sample size.}
202	Increasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\rho$ improves from 0.357 to $0.412{\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).
203	FK benefits less ($\rho{\approx}0.280$ at $N{=}16$ vs.\ 0.265 at $N{=}8$).
204	For RE at $N{=}16$, SJ ($\rho{=}0.281$), FK ($\rho{=}0.279$), and logprob ($\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.
205	
206	\paragraph{Cross-model transfer.}
207	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.363$, FK $\rho{=}0.327$).
208	On CoNLL, the cross-model gap is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
209	On conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
210	
211	\paragraph{Evaluation circularity.}
212	Leave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\Delta\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\Delta\rho$ of $3.1{\times}10^{-4}$.
213	Evaluation circularity is negligible.
214	
215	\paragraph{Conditional filtering reveals signal divergence.}
216	Filtering to non-zero F1 instances improves SJ correlations: NER $\rho{=}0.412$ (from 0.357), RE $\rho{=}0.368$ at $N{=}8$.
217	At $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\rho{=}0.308$, while logprob drops to $\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.
218	For applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\rho{\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.
219	
220	\paragraph{Binary filtering vs.\ continuous ranking.}
221	The logprob paradox observed in Table~\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.
222	Log-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).
223	Figure~\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.
224	Practitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.
225	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "2fa36150-48e7-4fd9-93ad-4f203615c242",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test on $\\rho_\\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.363$, FK $\\rho{=}0.327$).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n",
      "numLines": 225,
      "startLine": 1,
      "totalLines": 225
    }
  }
}
```

</details>

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_015kkrBuEF7d8xn9BZHMoZ7v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "078f1c53-b1db-4f56-83af-c6368684d6a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqLf5z6UMyVFJ4oNjmCVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 29702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-15T09:34:49.748Z_

<details><summary>↩ Tool result · `toolu_015kkrBuEF7d8xn9BZHMoZ7v`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	Our results suggest different signal choices depending on the deployment scenario.
5	For per-instance quality estimation, entity voting provides the strongest single signal ($\rho{=}0.50$, Table~\ref{tab:quality_estimation}).
6	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}), and it generalizes beyond entity-level structure to any set-valued output.
7	Under conditional filtering, SJ achieves $\rho{\approx}0.4$ on both NER and RE (\S\ref{sec:complexity_robustness}), and its ensemble with voting reaches AUROC${=}0.735$.
8	For binary accept/reject decisions, logprob is most effective (AUROC${=}0.761$ on CoNLL with LLaMA).
9	For best-of-$N$ selection, greedy decoding is near-optimal on NER; on RE, logprob is the only helpful signal (+2.3~pp, Table~\ref{tab:selection}).
10	
11	\paragraph{Signals discriminate between instances, not within strata.}
12	When instances are stratified by greedy F1, within-stratum correlations approach zero for all signals.
13	Confidence signals capture \textit{between-instance} quality differences---identifying which inputs the model handles reliably---rather than providing fine-grained discrimination among instances of similar difficulty.
14	This is the complementary face of the correlation-selection gap (\S\ref{sec:selection_gap}): signals that predict input difficulty cannot rank outputs within a difficulty stratum.
15	The practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.
16	
17	\paragraph{Task-difficulty-dependent signal selection.}
18	Across all three $N{=}16$ settings, the structural-over-logprob ordering holds consistently (\S\ref{sec:complexity_robustness}).
19	However, the \textit{optimal} signal shifts with task difficulty: EM dominates on easy tasks (CoNLL, greedy F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17, 54\% zero F1).
20	This ordering is model-agnostic---cross-model rankings between Qwen and LLaMA are identical---suggesting that the difficulty gradient, not model-specific behavior, determines which signal family is most informative.
21	
22	\paragraph{Capability boundary framework.}
23	Structural signals are most effective within the model's capability range.
24	Beyond it---RE with 44\% zero-F1 instances, WNUT-17 with 54\%---all signals converge toward zero or negative correlation.
25	Within the capability range, output complexity modulates signal effectiveness: the high-complexity RE subset ($n{=}81$) yields substantially stronger correlations (Voting $\rho{=}0.630$, SJ $\rho{=}0.502$) than the full set.
26	Conditional filtering further separates signal families: at $N{=}16$, SJ maintains $\rho{=}0.308$ on RE while logprob collapses to $\rho{=}{-}0.026$ (\S\ref{sec:complexity_robustness}).
27	The ``sweet spot'' for structural confidence signals is the intersection of sufficient model capability and sufficient output complexity---a regime where the model can produce varied but partially correct extractions rather than uniform failures.
28	
29	\paragraph{Methodological implications of $\rho$--AUROC separation.}
30	The logprob paradox on CoNLL with LLaMA---lowest $\rho$ (0.307) yet highest AUROC (0.761, Table~\ref{tab:quality_estimation})---reveals that rank correlation and binary discrimination measure fundamentally different signal properties.
31	Logprob provides coarse separation between reliable and unreliable instances, while structural signals provide finer-grained ranking across the quality spectrum.
32	Different downstream decisions therefore require different signals: threshold-based filtering favors logprob; ranking-dependent applications favor structural consistency.
33	Evaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "56a9f8d4-cacf-4ea7-a46f-c1a4c0db51e0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nOur results suggest different signal choices depending on the deployment scenario.\nFor per-instance quality estimation, entity voting provides the strongest single signal ($\\rho{=}0.50$, Table~\\ref{tab:quality_estimation}).\nWhen temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\\ref{tab:robustness}), and it generalizes beyond entity-level structure to any set-valued output.\nUnder conditional filtering, SJ achieves $\\rho{\\approx}0.4$ on both NER and RE (\\S\\ref{sec:complexity_robustness}), and its ensemble with voting reaches AUROC${=}0.735$.\nFor binary accept/reject decisions, logprob is most effective (AUROC${=}0.761$ on CoNLL with LLaMA).\nFor best-of-$N$ selection, greedy decoding is near-optimal on NER; on RE, logprob is the only helpful signal (+2.3~pp, Table~\\ref{tab:selection}).\n\n\\paragraph{Signals discriminate between instances, not within strata.}\nWhen instances are stratified by greedy F1, within-stratum correlations approach zero for all signals.\nConfidence signals capture \\textit{between-instance} quality differences---identifying which inputs the model handles reliably---rather than providing fine-grained discrimination among instances of similar difficulty.\nThis is the complementary face of the correlation-selection gap (\\S\\ref{sec:selection_gap}): signals that predict input difficulty cannot rank outputs within a difficulty stratum.\nThe practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.\n\n\\paragraph{Task-difficulty-dependent signal selection.}\nAcross all three $N{=}16$ settings, the structural-over-logprob ordering holds consistently (\\S\\ref{sec:complexity_robustness}).\nHowever, the \\textit{optimal} signal shifts with task difficulty: EM dominates on easy tasks (CoNLL, greedy F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\\,{\\approx}\\,$0.66), and all signals converge when model capability is insufficient (WNUT-17, 54\\% zero F1).\nThis ordering is model-agnostic---cross-model rankings between Qwen and LLaMA are identical---suggesting that the difficulty gradient, not model-specific behavior, determines which signal family is most informative.\n\n\\paragraph{Capability boundary framework.}\nStructural signals are most effective within the model's capability range.\nBeyond it---RE with 44\\% zero-F1 instances, WNUT-17 with 54\\%---all signals converge toward zero or negative correlation.\nWithin the capability range, output complexity modulates signal effectiveness: the high-complexity RE subset ($n{=}81$) yields substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$) than the full set.\nConditional filtering further separates signal families: at $N{=}16$, SJ maintains $\\rho{=}0.308$ on RE while logprob collapses to $\\rho{=}{-}0.026$ (\\S\\ref{sec:complexity_robustness}).\nThe ``sweet spot'' for structural confidence signals is the intersection of sufficient model capability and sufficient output complexity---a regime where the model can produce varied but partially correct extractions rather than uniform failures.\n\n\\paragraph{Methodological implications of $\\rho$--AUROC separation.}\nThe logprob paradox on CoNLL with LLaMA---lowest $\\rho$ (0.307) yet highest AUROC (0.761, Table~\\ref{tab:quality_estimation})---reveals that rank correlation and binary discrimination measure fundamentally different signal properties.\nLogprob provides coarse separation between reliable and unreliable instances, while structural signals provide finer-grained ranking across the quality spectrum.\nDifferent downstream decisions therefore require different signals: threshold-based filtering favors logprob; ranking-dependent applications favor structural consistency.\nEvaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01URQSjUHmvDJ3DHqHELdQry`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "9127c641-e157-4024-8d42-f1bf1e47806a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqLf5z6UMyVFJ4oNjmCVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 29702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-15T09:34:50.223Z_

<details><summary>↩ Tool result · `toolu_01URQSjUHmvDJ3DHqHELdQry`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	Our work connects three research threads: self-consistency and test-time scaling methods developed for reasoning tasks, confidence estimation for structured information extraction, and broader uncertainty quantification for language models.
4	
5	\subsection{Self-Consistency and Test-Time Scaling}
6	
7	\paragraph{Self-consistency for discrete and free-form tasks.}
8	Self-consistency decoding \cite{wang2023selfconsistency} improves chain-of-thought reasoning by sampling multiple rationales and selecting the most frequent answer via majority vote.
9	This paradigm assumes a discrete answer space where outputs can be grouped by equivalence and counted---an assumption that holds for arithmetic, commonsense QA, and similar tasks but breaks for set-valued structured outputs.
10	\citet{chen2024usc} extend self-consistency to free-form text generation by replacing exact matching with LLM-based semantic comparison, while SelfCheckGPT \cite{manakul2023selfcheckgpt} leverages cross-sample consistency to detect hallucinations in open-ended generation.
11	\citet{thirukovalluru2024atomic} decompose long-form outputs into atomic sub-claims and measure per-claim consistency, moving beyond whole-output comparison.
12	These methods operate on text-level equivalence or entailment; our work instead compares \textit{structured sets} of entities and relations, requiring set-theoretic similarity measures that account for partial overlap, type constraints, and span-level matching.
13	
14	\paragraph{Test-time scaling and sample selection.}
15	A growing body of work studies how to allocate additional compute at inference time.
16	\citet{snell2024scaling} characterize the scaling laws governing test-time compute, showing that repeated sampling with effective selection can substitute for model scaling.
17	\citet{brown2024monkeys} demonstrate that best-of-$N$ sampling with large $N$ yields substantial gains across diverse tasks.
18	Several recent methods aim to improve selection without trained reward models.
19	CISC \cite{taubenfeld2025cisc} combines confidence scores with majority voting, weighting each sample's contribution to the consensus.
20	Self-Certainty \cite{kang2025selfcertainty} uses KL divergence between a sample's token distribution and the prior to select high-quality outputs, demonstrating that reward-free selection is viable for mathematical reasoning.
21	ReASC \cite{kim2026reasc} adaptively adjusts the number of samples based on estimated difficulty, while \citet{wang2025rankedvoting} replace plurality voting with ranked aggregation, and \citet{oh2025latentsc} perform consistency estimation in latent space rather than output space.
22	
23	All of these methods target reasoning and QA tasks with discrete or near-discrete answer spaces.
24	Our work is, to our knowledge, the first to extend self-consistency to set-valued structured outputs in IE, and the first to identify the correlation-selection gap: strong quality estimation ($\rho{=}0.50$) coexists with selection failure (no gain over greedy on NER).
25	In direct dialogue with \citet{kang2025selfcertainty}, who show that reward-free selection succeeds for reasoning, our results demonstrate that this success does not transfer to structured extraction, where the combinatorial output space and instance-level nature of consistency signals preclude effective per-sample discrimination.
26	
27	\subsection{Consistency and Confidence for Structured IE}
28	
29	The most directly relevant prior work is \citet{nedellec2026consistency}, who study consistency--accuracy correlations in hard-prompted LLMs for NER and relation extraction on plant-health data.
30	Their findings corroborate our quality-estimation results: higher inter-sample consistency predicts higher extraction accuracy.
31	However, three key limitations motivate our work.
32	First, they rely on surface-level string matching and explicitly acknowledge that their approach ``overlooks semantically consistent outputs''---precisely the gap our Soft Jaccard signal addresses through type-aware bipartite matching with span overlap.
33	Second, they do not study best-of-$N$ selection, leaving the quality-estimation-to-selection transfer question unexamined.
34	Third, their evaluation covers a single domain with hard-prompted (temperature-zero) generation and no comparison across signal families.
35	Our work extends their analysis to multi-domain benchmarks, temperature-based sampling, and a systematic five-signal comparison that reveals when structural signals outperform surface alternatives and vice versa.
36	
37	CoCoA \cite{vashurin2025cocoa} proposes a minimum Bayes risk framework that fuses model confidence with inter-sample consistency for uncertainty quantification on QA, summarization, and translation.
38	Their confidence-consistency ensemble parallels our analysis of signal combinations, but they do not address structured extraction, where the unit of comparison shifts from text sequences to entity and relation sets.
39	
40	Our evaluation setting---LLMs performing IE as a generation task---builds on a line of work establishing generative approaches to entity and relation extraction.
41	UniNER \cite{zhou2024uniner} and GoLLIE \cite{sainz2024gollie} train universal IE models via instruction tuning; \citet{wadhwa2023revisiting} and InstructUIE \cite{wang2023instructuie} demonstrate that instruction-following LLMs can perform extraction zero-shot or with minimal supervision; GenIE \cite{josifoski2022genie} and CodeIE \cite{li2023codeie} frame IE as constrained sequence generation.
42	We adopt constrained decoding \cite{willard2023guided} following this paradigm and study confidence estimation as an orthogonal dimension: given that LLMs generate structured outputs, how reliably can we estimate extraction quality from multiple samples?
43	
44	\subsection{Uncertainty Estimation and Calibration}
45	
46	\paragraph{Confidence and uncertainty for LLMs.}
47	Several surveys chart the landscape of confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and their intersection with calibration \cite{hobelsberger2025systematic}.
48	Our work bridges confidence estimation and selective prediction: we use confidence signals not only to rank instances by reliability but also to attempt best-of-$N$ selection, revealing that these two objectives impose different requirements on the underlying signal.
49	
50	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning rather than surface form and estimates uncertainty from cluster statistics.
51	\citet{kossen2024semantic} distill semantic entropy into lightweight probes, and P(True) \cite{kadavath2022language} directly queries the model for its confidence.
52	These approaches measure uncertainty over the model's belief distribution; our structural signals instead measure agreement over output \textit{structure}, comparing extracted entity sets rather than semantic content of free-form text.
53	
54	\paragraph{Calibration and ensembles.}
55	Modern neural networks are often miscalibrated \cite{guo2017calibration}, and calibration techniques for pre-trained language models \cite{desai2020calibration} aim to align predicted probabilities with empirical accuracy.
56	Our reliability diagrams assess whether confidence signals are calibrated for IE, extending calibration analysis beyond classification to structured prediction.
57	Deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation, requiring multiple forward passes through different model parameters.
58	Our multi-sample approach is conceptually related---we also use variation across stochastic outputs---but requires no model modification or access to internal parameters beyond token log-probabilities, operating entirely post-hoc on generated outputs.
59	
60	\paragraph{Uncertainty for token-level and span-level NER.}
61	Prior work on NER uncertainty operates within discriminative, pre-LLM paradigms: \citet{xiao2019uncertainty} study Bayesian inference for sequence labeling, \citet{shelmanov2021active} leverage uncertainty for active learning in NER, and \citet{zhang2023ener} estimate entity-level uncertainty from span probabilities.
62	These methods assume access to per-token classification logits from a discriminative model.
63	In the generative LLM setting we study, entity boundaries are implicit in the decoded text and uncertainty must be estimated from the generation process itself.
64	
65	\paragraph{Related paradigms.}
66	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides distribution-free coverage guarantees but targets prediction sets rather than quality ranking.
67	Trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and reward models \cite{wang2024mathshepherd} learn to score outputs from labeled data; we focus on unsupervised signals that require no additional training.
68	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework of abstaining when uncertain; our contribution is characterizing which confidence signals support this objective for generative IE and where the quality-estimation-to-selection transfer breaks down.
69	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "615a32a8-de93-48e9-9e5b-41d01d74bf7c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\nOur work connects three research threads: self-consistency and test-time scaling methods developed for reasoning tasks, confidence estimation for structured information extraction, and broader uncertainty quantification for language models.\n\n\\subsection{Self-Consistency and Test-Time Scaling}\n\n\\paragraph{Self-consistency for discrete and free-form tasks.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves chain-of-thought reasoning by sampling multiple rationales and selecting the most frequent answer via majority vote.\nThis paradigm assumes a discrete answer space where outputs can be grouped by equivalence and counted---an assumption that holds for arithmetic, commonsense QA, and similar tasks but breaks for set-valued structured outputs.\n\\citet{chen2024usc} extend self-consistency to free-form text generation by replacing exact matching with LLM-based semantic comparison, while SelfCheckGPT \\cite{manakul2023selfcheckgpt} leverages cross-sample consistency to detect hallucinations in open-ended generation.\n\\citet{thirukovalluru2024atomic} decompose long-form outputs into atomic sub-claims and measure per-claim consistency, moving beyond whole-output comparison.\nThese methods operate on text-level equivalence or entailment; our work instead compares \\textit{structured sets} of entities and relations, requiring set-theoretic similarity measures that account for partial overlap, type constraints, and span-level matching.\n\n\\paragraph{Test-time scaling and sample selection.}\nA growing body of work studies how to allocate additional compute at inference time.\n\\citet{snell2024scaling} characterize the scaling laws governing test-time compute, showing that repeated sampling with effective selection can substitute for model scaling.\n\\citet{brown2024monkeys} demonstrate that best-of-$N$ sampling with large $N$ yields substantial gains across diverse tasks.\nSeveral recent methods aim to improve selection without trained reward models.\nCISC \\cite{taubenfeld2025cisc} combines confidence scores with majority voting, weighting each sample's contribution to the consensus.\nSelf-Certainty \\cite{kang2025selfcertainty} uses KL divergence between a sample's token distribution and the prior to select high-quality outputs, demonstrating that reward-free selection is viable for mathematical reasoning.\nReASC \\cite{kim2026reasc} adaptively adjusts the number of samples based on estimated difficulty, while \\citet{wang2025rankedvoting} replace plurality voting with ranked aggregation, and \\citet{oh2025latentsc} perform consistency estimation in latent space rather than output space.\n\nAll of these methods target reasoning and QA tasks with discrete or near-discrete answer spaces.\nOur work is, to our knowledge, the first to extend self-consistency to set-valued structured outputs in IE, and the first to identify the correlation-selection gap: strong quality estimation ($\\rho{=}0.50$) coexists with selection failure (no gain over greedy on NER).\nIn direct dialogue with \\citet{kang2025selfcertainty}, who show that reward-free selection succeeds for reasoning, our results demonstrate that this success does not transfer to structured extraction, where the combinatorial output space and instance-level nature of consistency signals preclude effective per-sample discrimination.\n\n\\subsection{Consistency and Confidence for Structured IE}\n\nThe most directly relevant prior work is \\citet{nedellec2026consistency}, who study consistency--accuracy correlations in hard-prompted LLMs for NER and relation extraction on plant-health data.\nTheir findings corroborate our quality-estimation results: higher inter-sample consistency predicts higher extraction accuracy.\nHowever, three key limitations motivate our work.\nFirst, they rely on surface-level string matching and explicitly acknowledge that their approach ``overlooks semantically consistent outputs''---precisely the gap our Soft Jaccard signal addresses through type-aware bipartite matching with span overlap.\nSecond, they do not study best-of-$N$ selection, leaving the quality-estimation-to-selection transfer question unexamined.\nThird, their evaluation covers a single domain with hard-prompted (temperature-zero) generation and no comparison across signal families.\nOur work extends their analysis to multi-domain benchmarks, temperature-based sampling, and a systematic five-signal comparison that reveals when structural signals outperform surface alternatives and vice versa.\n\nCoCoA \\cite{vashurin2025cocoa} proposes a minimum Bayes risk framework that fuses model confidence with inter-sample consistency for uncertainty quantification on QA, summarization, and translation.\nTheir confidence-consistency ensemble parallels our analysis of signal combinations, but they do not address structured extraction, where the unit of comparison shifts from text sequences to entity and relation sets.\n\nOur evaluation setting---LLMs performing IE as a generation task---builds on a line of work establishing generative approaches to entity and relation extraction.\nUniNER \\cite{zhou2024uniner} and GoLLIE \\cite{sainz2024gollie} train universal IE models via instruction tuning; \\citet{wadhwa2023revisiting} and InstructUIE \\cite{wang2023instructuie} demonstrate that instruction-following LLMs can perform extraction zero-shot or with minimal supervision; GenIE \\cite{josifoski2022genie} and CodeIE \\cite{li2023codeie} frame IE as constrained sequence generation.\nWe adopt constrained decoding \\cite{willard2023guided} following this paradigm and study confidence estimation as an orthogonal dimension: given that LLMs generate structured outputs, how reliably can we estimate extraction quality from multiple samples?\n\n\\subsection{Uncertainty Estimation and Calibration}\n\n\\paragraph{Confidence and uncertainty for LLMs.}\nSeveral surveys chart the landscape of confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and their intersection with calibration \\cite{hobelsberger2025systematic}.\nOur work bridges confidence estimation and selective prediction: we use confidence signals not only to rank instances by reliability but also to attempt best-of-$N$ selection, revealing that these two objectives impose different requirements on the underlying signal.\n\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning rather than surface form and estimates uncertainty from cluster statistics.\n\\citet{kossen2024semantic} distill semantic entropy into lightweight probes, and P(True) \\cite{kadavath2022language} directly queries the model for its confidence.\nThese approaches measure uncertainty over the model's belief distribution; our structural signals instead measure agreement over output \\textit{structure}, comparing extracted entity sets rather than semantic content of free-form text.\n\n\\paragraph{Calibration and ensembles.}\nModern neural networks are often miscalibrated \\cite{guo2017calibration}, and calibration techniques for pre-trained language models \\cite{desai2020calibration} aim to align predicted probabilities with empirical accuracy.\nOur reliability diagrams assess whether confidence signals are calibrated for IE, extending calibration analysis beyond classification to structured prediction.\nDeep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation, requiring multiple forward passes through different model parameters.\nOur multi-sample approach is conceptually related---we also use variation across stochastic outputs---but requires no model modification or access to internal parameters beyond token log-probabilities, operating entirely post-hoc on generated outputs.\n\n\\paragraph{Uncertainty for token-level and span-level NER.}\nPrior work on NER uncertainty operates within discriminative, pre-LLM paradigms: \\citet{xiao2019uncertainty} study Bayesian inference for sequence labeling, \\citet{shelmanov2021active} leverage uncertainty for active learning in NER, and \\citet{zhang2023ener} estimate entity-level uncertainty from span probabilities.\nThese methods assume access to per-token classification logits from a discriminative model.\nIn the generative LLM setting we study, entity boundaries are implicit in the decoded text and uncertainty must be estimated from the generation process itself.\n\n\\paragraph{Related paradigms.}\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides distribution-free coverage guarantees but targets prediction sets rather than quality ranking.\nTrained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and reward models \\cite{wang2024mathshepherd} learn to score outputs from labeled data; we focus on unsupervised signals that require no additional training.\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework of abstaining when uncertain; our contribution is characterizing which confidence signals support this objective for generative IE and where the quality-estimation-to-selection transfer breaks down.\n",
      "numLines": 69,
      "startLine": 1,
      "totalLines": 69
    }
  }
}
```

</details>

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_019MWKrzcebctcZWv7n8xKu4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "e13c2d11-2e13-4b02-8f91-f02b2443fe3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqLf5z6UMyVFJ4oNjmCVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 29702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-15T09:34:50.696Z_

<details><summary>↩ Tool result · `toolu_019MWKrzcebctcZWv7n8xKu4`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.
11	
12	Several directions remain open.
13	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
14	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.
15	Integration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.
16	Finally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "52e4d542-d5a3-42a1-a82a-6d980271ace3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nThis work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.\nBy comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).\nOur experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.\n\nThree findings anchor our analysis.\nFirst, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.\nSecond, the \\textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.\nThird, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.\n\nSeveral directions remain open.\nTrained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.\nCross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.\nIntegration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.\nFinally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.\n",
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

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01LBnUHceJ8TY2AwPSQyj6Nq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "84628949-a43c-4bb8-9f39-217041dfbaff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqLf5z6UMyVFJ4oNjmCVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 29702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-15T09:34:51.641Z_

<details><summary>↩ Tool result · `toolu_01LBnUHceJ8TY2AwPSQyj6Nq`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.071$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL, the SJ--FK gap is only 0.004 ($\rho{=}0.436$ vs.\ $0.431$ for LLaMA), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "0c6b5961-1ee3-4611-ae00-9ef5aae1445f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nWhether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.071$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL, the SJ--FK gap is only 0.004 ($\\rho{=}0.436$ vs.\\ $0.431$ for LLaMA), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---


### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_013ZoWWQtymmmqhfRcejYk8Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/data/tost_breakpoint_delta_star.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "2fa22bc9-07a3-4874-bc48-535ae774151e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqLf5z6UMyVFJ4oNjmCVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 29702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-15T09:34:52.111Z_

<details><summary>↩ Tool result · `toolu_013ZoWWQtymmmqhfRcejYk8Y`</summary>

```text
1	# TOST Breakpoint δ*
2	
3	**Definition**: δ* = max(|CI_lower|, |CI_upper|) of the 90% CI of the paired mean difference (selection F1 − greedy F1). This is the smallest equivalence margin δ at which TOST (α=0.05) would confirm equivalence.
4	
5	**Method**: Paired t-distribution 90% CI = mean_Δ ± t_{0.05, n−1} × SE, where SE = std_Δ / √n.
6	
7	**Data source**: exp_012_rerun_1024 (Qwen2.5-7B-Instruct LoRA, N=8 samples, T=1.0). TOST worker log 2026-05-15.
8	
9	## NER (SciERC, n=529)
10	
11	| Signal | mean_Δ (pp) | 90% CI lower (pp) | 90% CI upper (pp) | δ* (pp) |
12	|--------|-------------|--------------------|--------------------|---------|
13	| LP     | +0.62       | −0.56              | +1.80              | 1.80    |
14	| SJ     | +0.11       | −1.06              | +1.28              | 1.28    |
15	| EM     | −0.79       | −2.07              | +0.49              | 2.07    |
16	| VC     | −1.02       | −2.29              | +0.25              | 2.29    |
17	| FK     | −1.80       | −3.38              | −0.22              | 3.38    |
18	
19	## RE (SciERC, n=397)
20	
21	| Signal | mean_Δ (pp) | 90% CI lower (pp) | 90% CI upper (pp) | δ* (pp) |
22	|--------|-------------|--------------------|--------------------|---------|
23	| LP     | −0.94       | −2.86              | +0.98              | 2.86    |
24	| SJ     | −1.88       | −3.76              | +0.00              | 3.76    |
25	| FK     | −2.18       | −4.22              | −0.14              | 4.22    |
26	| EM     | −3.16       | −5.17              | −1.15              | 5.17    |
27	| VC     | −4.51       | −6.53              | −2.49              | 6.53    |
28	
29	## Summary
30	
31	All δ* ∈ [1.28, 6.53] pp.
32	
33	- **NER**: δ* ∈ [1.28, 3.38] pp. All 5 signals confirm equivalence at δ=5pp (current paper uses δ=2pp). At δ=2pp, only SJ (1.28) and LP (1.80) pass; EM (2.07), VC (2.29), FK (3.38) require larger margins.
34	- **RE**: δ* ∈ [2.86, 6.53] pp. At δ=5pp (current paper), LP (2.86), SJ (3.76), FK (4.22) pass; EM (5.17) and VC (6.53) fail. VC has the largest δ* due to systematic negative bias (−4.5pp).
35	
36	### Implications for paper's TOST parameters
37	
38	| Paper setting       | NER δ=2pp              | RE δ=5pp               |
39	|---------------------|------------------------|------------------------|
40	| Signals that pass   | SJ (1.28), LP (1.80)   | LP (2.86), SJ (3.76), FK (4.22) |
41	| Borderline          | EM (2.07)              | EM (5.17)              |
42	| Signals that fail   | VC (2.29), FK (3.38)   | VC (6.53)              |
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "9f02070d-315e-4581-b2f8-5022270bfbf7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/data/tost_breakpoint_delta_star.md",
      "content": "# TOST Breakpoint δ*\n\n**Definition**: δ* = max(|CI_lower|, |CI_upper|) of the 90% CI of the paired mean difference (selection F1 − greedy F1). This is the smallest equivalence margin δ at which TOST (α=0.05) would confirm equivalence.\n\n**Method**: Paired t-distribution 90% CI = mean_Δ ± t_{0.05, n−1} × SE, where SE = std_Δ / √n.\n\n**Data source**: exp_012_rerun_1024 (Qwen2.5-7B-Instruct LoRA, N=8 samples, T=1.0). TOST worker log 2026-05-15.\n\n## NER (SciERC, n=529)\n\n| Signal | mean_Δ (pp) | 90% CI lower (pp) | 90% CI upper (pp) | δ* (pp) |\n|--------|-------------|--------------------|--------------------|---------|\n| LP     | +0.62       | −0.56              | +1.80              | 1.80    |\n| SJ     | +0.11       | −1.06              | +1.28              | 1.28    |\n| EM     | −0.79       | −2.07              | +0.49              | 2.07    |\n| VC     | −1.02       | −2.29              | +0.25              | 2.29    |\n| FK     | −1.80       | −3.38              | −0.22              | 3.38    |\n\n## RE (SciERC, n=397)\n\n| Signal | mean_Δ (pp) | 90% CI lower (pp) | 90% CI upper (pp) | δ* (pp) |\n|--------|-------------|--------------------|--------------------|---------|\n| LP     | −0.94       | −2.86              | +0.98              | 2.86    |\n| SJ     | −1.88       | −3.76              | +0.00              | 3.76    |\n| FK     | −2.18       | −4.22              | −0.14              | 4.22    |\n| EM     | −3.16       | −5.17              | −1.15              | 5.17    |\n| VC     | −4.51       | −6.53              | −2.49              | 6.53    |\n\n## Summary\n\nAll δ* ∈ [1.28, 6.53] pp.\n\n- **NER**: δ* ∈ [1.28, 3.38] pp. All 5 signals confirm equivalence at δ=5pp (current paper uses δ=2pp). At δ=2pp, only SJ (1.28) and LP (1.80) pass; EM (2.07), VC (2.29), FK (3.38) require larger margins.\n- **RE**: δ* ∈ [2.86, 6.53] pp. At δ=5pp (current paper), LP (2.86), SJ (3.76), FK (4.22) pass; EM (5.17) and VC (6.53) fail. VC has the largest δ* due to systematic negative bias (−4.5pp).\n\n### Implications for paper's TOST parameters\n\n| Paper setting       | NER δ=2pp              | RE δ=5pp               |\n|---------------------|------------------------|------------------------|\n| Signals that pass   | SJ (1.28), LP (1.80)   | LP (2.86), SJ (3.76), FK (4.22) |\n| Borderline          | EM (2.07)              | EM (5.17)              |\n| Signals that fail   | VC (2.29), FK (3.38)   | VC (6.53)              |\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  }
}
```

</details>

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01NmCqCdG63dXGjYckWsHW3f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/report/qwen3_thinking_confirmation.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "7a68358d-7adb-4643-9520-73a959f45b22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqLf5z6UMyVFJ4oNjmCVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 29702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-15T09:34:52.594Z_

<details><summary>↩ Tool result · `toolu_01NmCqCdG63dXGjYckWsHW3f`</summary>

````text
1	# Qwen3 SciERC Training: Thinking Tokens Confirmation
2	
3	## 1. enable_thinking 配置状态
4	
5	| 训练配置 | 文件 | enable_thinking 设置 | 实际生效值 |
6	|----------|------|---------------------|-----------|
7	| ft_001 (SciERC) | `train_config.yaml` | **未设置** | `True` (默认值) |
8	| ft_002 (SciERC) | `train_config_v2.yaml` | **未设置** | `True` (默认值) |
9	| ft_002_v2 (SciERC) | `train_config_v2.yaml` | **未设置** | `True` (默认值) |
10	| CoNLL-2003 | `train_config_conll2003.yaml` | `false` | `False` |
11	| WNUT-17 | `train_config_wnut17.yaml` | `false` | `False` |
12	
13	**LLaMA Factory 0.9.4 默认值**: `data_args.enable_thinking` 定义在 `llamafactory/hparams/data_args.py:122`，默认 `True`。SciERC 训练配置未覆盖此参数，因此使用默认值 `True`。
14	
15	## 2. 训练日志中的 thinking token 证据
16	
17	所有三次 SciERC 训练日志均包含：
18	
19	```
20	[WARNING] llamafactory.data.template:148 >> You are using reasoning template,
21	please add `_nothink` suffix if the model is not a reasoning model. e.g., qwen3_vl_nothink
22	&lt;think>
23	&lt;/think>
24	&lt;think>
25	&lt;/think>
26	...
27	```
28	
29	| 日志文件 | 时间戳 | 包含 `&lt;think>` |
30	|----------|--------|----------------|
31	| `ft_001_train.log` | 2026-05-14 14:09:15 | Yes |
32	| `ft_002_train.log` | 2026-05-14 15:43:17 | Yes |
33	| `ft_002v2_train.log` | 2026-05-14 16:10:02 | Yes |
34	
35	## 3. LLaMA Factory enable_thinking 机制 (template.py)
36	
37	当 `enable_thinking=True` 且训练数据不含 `&lt;think>`/`&lt;/think>` 时（正是 SciERC 的情况），LLaMA Factory 的行为（`template.py:424-431`）：
38	
39	```python
40	if (
41	    self.thought_words[0].strip() not in messages[-1]["content"]
42	    and self.thought_words[1].strip() not in messages[-1]["content"]
43	):  # add empty cot
44	    if not self.enable_thinking:  # do not compute loss
45	        prompt_ids += self.get_thought_word_ids(tokenizer)
46	    else:  # do compute loss
47	        response_ids = self.get_thought_word_ids(tokenizer) + response_ids
48	```
49	
50	- **`enable_thinking=True`（SciERC）**: 空 `&lt;think>\n&lt;/think>\n\n` 被 **prepend 到 response_ids**，纳入 loss 计算。模型被训练在每个 JSON 响应前先输出空 thinking block。
51	- **`enable_thinking=False`（CoNLL/WNUT）**: 空 `&lt;think>\n&lt;/think>` 被 append 到 prompt_ids，**不参与 loss 计算**。
52	
53	## 4. 结论
54	
55	**Thinking tokens 在 SciERC 训练时实际被激活。**
56	
57	具体表现：
58	- 每个训练样本的 response 前被自动注入空 thinking block `&lt;think>\n&lt;/think>\n\n`
59	- 这些 token 被纳入 loss 计算，模型学会在输出 JSON 前先产生空 thinking block
60	- 但 thinking block 始终为空（训练数据不含任何推理链），不存在实际的 chain-of-thought 内容
61	
62	**推理时的处理**：
63	- `apply_chat_template(enable_thinking=False)` + XGrammar JSON constrained decoding 确保推理输出不含任何 thinking tokens
64	- 这构成了一个 train-test distribution mismatch：训练时模型预期输出 `&lt;think>\n&lt;/think>` → JSON，推理时直接输出 JSON
65	
66	**影响评估**：
67	- 空 thinking block 仅含 4-5 个 token（`&lt;think>`, `\n`, `&lt;/think>`, `\n\n`），在 2048 cutoff_len 中占比极小
68	- 不存在推理链泄漏（thinking block 始终为空）
69	- 主要影响：模型的 token 分布被轻微偏移（学会先输出 thinking 标记再输出 JSON），推理时跳过这些 token 可能对首 token 概率分布有微弱影响
70	- CoNLL-2003 和 WNUT-17 不受影响（已显式设置 `enable_thinking: false`）
71	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "245b3c04-8ecf-47b4-a57a-3b77f6693ab3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/report/qwen3_thinking_confirmation.md",
      "content": "# Qwen3 SciERC Training: Thinking Tokens Confirmation\n\n## 1. enable_thinking 配置状态\n\n| 训练配置 | 文件 | enable_thinking 设置 | 实际生效值 |\n|----------|------|---------------------|-----------|\n| ft_001 (SciERC) | `train_config.yaml` | **未设置** | `True` (默认值) |\n| ft_002 (SciERC) | `train_config_v2.yaml` | **未设置** | `True` (默认值) |\n| ft_002_v2 (SciERC) | `train_config_v2.yaml` | **未设置** | `True` (默认值) |\n| CoNLL-2003 | `train_config_conll2003.yaml` | `false` | `False` |\n| WNUT-17 | `train_config_wnut17.yaml` | `false` | `False` |\n\n**LLaMA Factory 0.9.4 默认值**: `data_args.enable_thinking` 定义在 `llamafactory/hparams/data_args.py:122`，默认 `True`。SciERC 训练配置未覆盖此参数，因此使用默认值 `True`。\n\n## 2. 训练日志中的 thinking token 证据\n\n所有三次 SciERC 训练日志均包含：\n\n```\n[WARNING] llamafactory.data.template:148 >> You are using reasoning template,\nplease add `_nothink` suffix if the model is not a reasoning model. e.g., qwen3_vl_nothink\n&lt;think>\n&lt;/think>\n&lt;think>\n&lt;/think>\n...\n```\n\n| 日志文件 | 时间戳 | 包含 `&lt;think>` |\n|----------|--------|----------------|\n| `ft_001_train.log` | 2026-05-14 14:09:15 | Yes |\n| `ft_002_train.log` | 2026-05-14 15:43:17 | Yes |\n| `ft_002v2_train.log` | 2026-05-14 16:10:02 | Yes |\n\n## 3. LLaMA Factory enable_thinking 机制 (template.py)\n\n当 `enable_thinking=True` 且训练数据不含 `&lt;think>`/`&lt;/think>` 时（正是 SciERC 的情况），LLaMA Factory 的行为（`template.py:424-431`）：\n\n```python\nif (\n    self.thought_words[0].strip() not in messages[-1][\"content\"]\n    and self.thought_words[1].strip() not in messages[-1][\"content\"]\n):  # add empty cot\n    if not self.enable_thinking:  # do not compute loss\n        prompt_ids += self.get_thought_word_ids(tokenizer)\n    else:  # do compute loss\n        response_ids = self.get_thought_word_ids(tokenizer) + response_ids\n```\n\n- **`enable_thinking=True`（SciERC）**: 空 `&lt;think>\\n&lt;/think>\\n\\n` 被 **prepend 到 response_ids**，纳入 loss 计算。模型被训练在每个 JSON 响应前先输出空 thinking block。\n- **`enable_thinking=False`（CoNLL/WNUT）**: 空 `&lt;think>\\n&lt;/think>` 被 append 到 prompt_ids，**不参与 loss 计算**。\n\n## 4. 结论\n\n**Thinking tokens 在 SciERC 训练时实际被激活。**\n\n具体表现：\n- 每个训练样本的 response 前被自动注入空 thinking block `&lt;think>\\n&lt;/think>\\n\\n`\n- 这些 token 被纳入 loss 计算，模型学会在输出 JSON 前先产生空 thinking block\n- 但 thinking block 始终为空（训练数据不含任何推理链），不存在实际的 chain-of-thought 内容\n\n**推理时的处理**：\n- `apply_chat_template(enable_thinking=False)` + XGrammar JSON constrained decoding 确保推理输出不含任何 thinking tokens\n- 这构成了一个 train-test distribution mismatch：训练时模型预期输出 `&lt;think>\\n&lt;/think>` → JSON，推理时直接输出 JSON\n\n**影响评估**：\n- 空 thinking block 仅含 4-5 个 token（`&lt;think>`, `\\n`, `&lt;/think>`, `\\n\\n`），在 2048 cutoff_len 中占比极小\n- 不存在推理链泄漏（thinking block 始终为空）\n- 主要影响：模型的 token 分布被轻微偏移（学会先输出 thinking 标记再输出 JSON），推理时跳过这些 token 可能对首 token 概率分布有微弱影响\n- CoNLL-2003 和 WNUT-17 不受影响（已显式设置 `enable_thinking: false`）\n",
      "numLines": 71,
      "startLine": 1,
      "totalLines": 71
    }
  }
}
````

</details>

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01XtgLuWar7Aj2XDxoibFbyC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/report/vc_implementation_rho_diff.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "d326cb65-cf4a-42d9-b793-14346cb70697",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqLf5z6UMyVFJ4oNjmCVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 29702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-15T09:34:53.034Z_

<details><summary>↩ Tool result · `toolu_01XtgLuWar7Aj2XDxoibFbyC`</summary>

```text
1	# VC Implementation ρ Difference: Eq.6 vs Majority Threshold
2	
3	Two Voting Confidence (VC) implementations exist in the codebase:
4	
5	- **Eq.6 (no threshold)**: `mean([v/N for v in counter.values()])` — averages voting rate over all unique items
6	- **Majority threshold**: `mean([v/N for v in counter.values() if v > N/2])` else 0.0 — only items appearing in >50% of samples
7	
8	D068 unified the paper to majority threshold for Table 2.
9	
10	## Spearman ρ (VC vs F1), full split (non-empty gold)
11	
12	| Dataset | Model | Task | N | n | ρ\_eq6 | ρ\_majority | Δρ (eq6 − maj) |
13	|---------|-------|------|---|---|--------|-------------|----------------|
14	| SciERC | Qwen | NER | 8 | 529 | 0.3792 | 0.2524 | **+0.1268** |
15	| SciERC | Qwen | RE | 8 | 397 | 0.3498 | 0.3311 | **+0.0187** |
16	| SciERC | LLaMA | NER | 8 | 529 | 0.4053 | — | — |
17	| SciERC | LLaMA | RE | 8 | 397 | 0.3840 | — | — |
18	| CoNLL | LLaMA | NER | 8 | 2756 | 0.4256 | — | — |
19	| CoNLL | Qwen | NER | 16 | 2756 | 0.4286 | — | — |
20	
21	"—" = samples.jsonl not available locally; majority-threshold ρ requires recomputation from raw samples.
22	
23	## Methodology
24	
25	- **Qwen × SciERC**: Computed from local `exp_012_rerun_1024/samples_with_logprobs.jsonl` (seed=42). NER F1 uses strict span match `(start, end, type)`. RE F1 uses `(head_start, head_end, tail_start, tail_end, type)`. Values validated against worker verification result (exact match).
26	- **Other configurations**: ρ\_eq6 from experiment registry (all registry entries use Eq.6 implementation, confirmed by worker verification of exp\_012).
27	
28	## Key observations
29	
30	1. **NER Δρ is large (+0.127)**: The majority threshold discards all items appearing in ≤4 of 8 samples. For NER, many valid but rare entity mentions get filtered out, collapsing the signal's dynamic range and reducing correlation with F1.
31	
32	2. **RE Δρ is small (+0.019)**: Relations are inherently sparser — most extracted relations either appear consistently (majority) or not at all. The threshold filter removes fewer items proportionally, so the two implementations converge.
33	
34	3. **Direction is consistent**: Eq.6 ≥ majority threshold in both subtasks. The no-threshold version preserves more discriminative signal from low-frequency items.
35	
36	4. **Practical impact on paper claims**: The qualitative ranking VC > SJ > others holds under both implementations for NER. For RE, VC remains the top signal either way. The D068 decision to use majority threshold is conservative — it reports the weaker of the two ρ values.
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "b8cceb8b-665e-49d3-81ed-f6e180aae3cc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/report/vc_implementation_rho_diff.md",
      "content": "# VC Implementation ρ Difference: Eq.6 vs Majority Threshold\n\nTwo Voting Confidence (VC) implementations exist in the codebase:\n\n- **Eq.6 (no threshold)**: `mean([v/N for v in counter.values()])` — averages voting rate over all unique items\n- **Majority threshold**: `mean([v/N for v in counter.values() if v > N/2])` else 0.0 — only items appearing in >50% of samples\n\nD068 unified the paper to majority threshold for Table 2.\n\n## Spearman ρ (VC vs F1), full split (non-empty gold)\n\n| Dataset | Model | Task | N | n | ρ\\_eq6 | ρ\\_majority | Δρ (eq6 − maj) |\n|---------|-------|------|---|---|--------|-------------|----------------|\n| SciERC | Qwen | NER | 8 | 529 | 0.3792 | 0.2524 | **+0.1268** |\n| SciERC | Qwen | RE | 8 | 397 | 0.3498 | 0.3311 | **+0.0187** |\n| SciERC | LLaMA | NER | 8 | 529 | 0.4053 | — | — |\n| SciERC | LLaMA | RE | 8 | 397 | 0.3840 | — | — |\n| CoNLL | LLaMA | NER | 8 | 2756 | 0.4256 | — | — |\n| CoNLL | Qwen | NER | 16 | 2756 | 0.4286 | — | — |\n\n\"—\" = samples.jsonl not available locally; majority-threshold ρ requires recomputation from raw samples.\n\n## Methodology\n\n- **Qwen × SciERC**: Computed from local `exp_012_rerun_1024/samples_with_logprobs.jsonl` (seed=42). NER F1 uses strict span match `(start, end, type)`. RE F1 uses `(head_start, head_end, tail_start, tail_end, type)`. Values validated against worker verification result (exact match).\n- **Other configurations**: ρ\\_eq6 from experiment registry (all registry entries use Eq.6 implementation, confirmed by worker verification of exp\\_012).\n\n## Key observations\n\n1. **NER Δρ is large (+0.127)**: The majority threshold discards all items appearing in ≤4 of 8 samples. For NER, many valid but rare entity mentions get filtered out, collapsing the signal's dynamic range and reducing correlation with F1.\n\n2. **RE Δρ is small (+0.019)**: Relations are inherently sparser — most extracted relations either appear consistently (majority) or not at all. The threshold filter removes fewer items proportionally, so the two implementations converge.\n\n3. **Direction is consistent**: Eq.6 ≥ majority threshold in both subtasks. The no-threshold version preserves more discriminative signal from low-frequency items.\n\n4. **Practical impact on paper claims**: The qualitative ranking VC > SJ > others holds under both implementations for NER. For RE, VC remains the top signal either way. The D068 decision to use majority threshold is conservative — it reports the weaker of the two ρ values.\n",
      "numLines": 37,
      "startLine": 1,
      "totalLines": 37
    }
  }
}
```

</details>

---


### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
Now let me also read the method section and the appendix, and the references.bib file for the bib corrections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "3cd6eb84-5c42-4180-832d-b4fb58b93f17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoTnsLYV7RxSFruprDEknq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17299,
      "cache_read_input_tokens": 31660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17299
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

_source line 57_

读取 method section、appendix 和 references.bib。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "3fa3c898-2e6e-42ad-a78c-5bf5404c66d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoTnsLYV7RxSFruprDEknq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17299,
      "cache_read_input_tokens": 31660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17299
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

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_018e5RKjBSZqnUeqSQT9Twub`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "ad61ffa6-60b5-4d91-9ff2-1388d5b9dcda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoTnsLYV7RxSFruprDEknq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17299,
      "cache_read_input_tokens": 31660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17299
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

_source line 59 · 2026-05-15T09:34:58.910Z_

<details><summary>↩ Tool result · `toolu_018e5RKjBSZqnUeqSQT9Twub`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{&lt;j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface, instance-level).}
28	The majority fraction---the proportion of samples producing the most common output:
29	\begin{equation}\label{eq:em}
30	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
31	\end{equation}
32	
33	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
34	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
35	\begin{equation}\label{eq:fk}
36	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
37	\end{equation}
38	where $\bar{P}$ is mean observed pairwise agreement and $\bar{P}_e$ is expected agreement under random assignment.
39	While FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.
40	Empirically, we measure excess agreement ($\bar{P} - \bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\% and $-$4.0\%, indicating mild \textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.
41	Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.
42	
43	\paragraph{Soft Jaccard (structural, instance-level).}
44	Our primary structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
45	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:
46	\begin{equation}\label{eq:sj}
47	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
48	\end{equation}
49	where $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.
50	We use $\max(|g_i|, |g_j|)$ rather than $|g_i \cup g_j|$ as the normalizer to penalize length asymmetry between samples.
51	The instance-level signal averages over all pairs:
52	\begin{equation}\label{eq:sj_instance}
53	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
54	\end{equation}
55	
56	\paragraph{Entity voting confidence (structural, instance-level).}
57	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
58	The instance-level confidence is the mean frequency:
59	\begin{equation}\label{eq:voting}
60	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
61	\end{equation}
62	When $E_\cup = \emptyset$ (no entity extracted by any sample), we set $c_{\mathrm{vc}}(x) = 0$.\footnote{This occurs in $<$1\% of instances in our experiments (WNUT-17 only). Our implementation computes the mean entity-level match rate against a majority threshold ($>N/2$). An alternative without the threshold yields slightly different absolute values but identical qualitative conclusions.}
63	
64	\subsection{Evaluation Framework}\label{sec:evaluation}
65	
66	\paragraph{Quality estimation.}
67	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
68	
69	\paragraph{Sample selection.}
70	We report best-of-$N$ F1: for each instance, the signal selects one sample.
71	Per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).
72	We compare against an \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$, $N{=}1$).
73	
74	\paragraph{Complementarity.}
75	High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "db69a112-be1a-4e96-9a0e-4c648eaf2334",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}.\nEach $y_i$ is an entity set (NER) or relation set (RE).\nA confidence signal $c$ serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among $N$ candidates.\n\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct candidate ranking.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\nNotation is summarized in Appendix~\\ref{app:notation}.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe use \\textit{confidence signal} as the umbrella term for all five measures.\nFour are \\textit{consistency signals}---computed from inter-sample agreement---spanning two families: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]).\nThe fifth, log-probability, is the sole \\textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal.\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{&lt;j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe majority fraction---the proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.\nWhile FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.\nEmpirically, we measure excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\\% and $-$4.0\\%, indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.\nUnlike structural signals, FK relies on exact string matching and does not tolerate surface variations.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur primary structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.\nWe use $\\max(|g_i|, |g_j|)$ rather than $|g_i \\cup g_j|$ as the normalizer to penalize length asymmetry between samples.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$ (no entity extracted by any sample), we set $c_{\\mathrm{vc}}(x) = 0$.\\footnote{This occurs in $<$1\\% of instances in our experiments (WNUT-17 only). Our implementation computes the mean entity-level match rate against a majority threshold ($>N/2$). An alternative without the threshold yields slightly different absolute values but identical qualitative conclusions.}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nWe measure rank correlation (Spearman $\\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.\n\n\\paragraph{Sample selection.}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample.\nPer-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).\nWe compare against an \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$, $N{=}1$).\n\n\\paragraph{Complementarity.}\nHigh rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\n",
      "numLines": 76,
      "startLine": 1,
      "totalLines": 76
    }
  }
}
```

</details>

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01EL1dfs3RvgtZy8WRrkMkZd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "20d534d6-fb6f-4012-a075-e5ec8d6d60a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoTnsLYV7RxSFruprDEknq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17299,
      "cache_read_input_tokens": 31660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17299
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

_source line 61 · 2026-05-15T09:34:59.727Z_

<details><summary>↩ Tool result · `toolu_01EL1dfs3RvgtZy8WRrkMkZd`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm}0.008$ & --- \\
56	\quad VC &  & $0.458{\pm}0.003$ & --- \\
57	\quad LP &  & $0.310{\pm}0.005$ & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
65	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}
66	\label{fig:temperature_robustness}
67	\end{figure}
68	
69	\paragraph{Temperature sensitivity.}
70	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
71	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
72	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
73	
74	\paragraph{Sample size scaling.}
75	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.412{\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.
76	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
77	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.021$).
80	SJ, EM, and voting confidence scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	
82	\paragraph{Cross-model transfer.}
83	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.363$, FK $\rho{=}0.327$).
84	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
85	At $N{=}16$, the structural-over-LP advantage holds across all four tested settings: Qwen SciERC (VC $\rho{=}0.411$ vs.\ LP 0.259, $\Delta{=}{+}0.152$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ LP $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
86	
87	\section{Calibration Analysis}\label{app:calibration}
88	
89	\begin{figure*}[t]
90	\centering
91	\includegraphics[width=\textwidth]{fig_reliability}
92	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
93	\label{fig:reliability}
94	\end{figure*}
95	
96	Reliability diagrams use 10 equal-width bins.
97	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
98	
99	\section{Additional Analyses}\label{app:additional}
100	
101	\paragraph{Per-relation diagnostic.}
102	RE signal degradation is relation-specific.
103	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
104	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
105	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
106	
107	\paragraph{Capability stratification.}
108	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
109	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
110	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
111	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
112	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
113	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
114	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
115	
116	\paragraph{Length vs.\ log-probability.}
117	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
118	
119	\begin{figure}[t]
120	\centering
121	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
122	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
123	\label{fig:length_logprob_scatter}
124	\end{figure}
125	
126	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
127	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
128	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
129	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
130	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
131	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
132	Evaluation circularity is negligible.
133	
134	\paragraph{Conditional filtering details.}
135	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
136	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
137	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
138	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
139	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
140	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
141	
142	\paragraph{WNUT-17 full signal analysis.}
143	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
144	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
145	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
146	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
152	\label{tab:wnut}
153	\begin{tabular}{lccccc}
154	\toprule
155	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
156	\midrule
157	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
158	FK      & .125 & .001 & .555 & .169 & .002 \\
159	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
160	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
161	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
162	\bottomrule
163	\end{tabular}
164	\end{table}
165	
166	\paragraph{Cross-configuration selection analysis.}
167	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
168	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
169	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
170	
171	\begin{table*}[t]
172	\centering
173	\small
174	\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). SJ: Soft Jaccard, FK: Fleiss' $\kappa$, EM: Exact Match, LP: Log-prob, VC: Voting Confidence. Best non-oracle signal per row in \textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
175	\label{tab:cross_selection}
176	\begin{tabular}{llccccccc}
177	\toprule
178	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
179	\midrule
180	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
181	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
182	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
183	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
184	\bottomrule
185	\end{tabular}
186	\end{table*}
187	
188	\paragraph{Diminishing returns of $N$-scaling.}
189	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2024scaling}.
190	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
191	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
192	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
193	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
194	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
195	
196	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
197	
198	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
199	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
200	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
201	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
202	
203	\begin{table}[t]
204	\centering
205	\small
206	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
207	\label{tab:bootstrap_signal_ci}
208	\begin{tabular}{lcc}
209	\toprule
210	Signal & $\rho$ & 95\% CI \\
211	\midrule
212	VC & +0.379 & [+0.299, +0.456] \\
213	SJ & +0.360 & [+0.277, +0.437] \\
214	EM & +0.295 & [+0.212, +0.371] \\
215	FK & +0.267 & [+0.176, +0.354] \\
216	LP & +0.205 & [+0.119, +0.291] \\
217	\bottomrule
218	\end{tabular}
219	
220	\vspace{0.5em}
221	
222	\begin{tabular}{lccc}
223	\toprule
224	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
225	\midrule
226	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
227	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
228	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
229	\bottomrule
230	\end{tabular}
231	
232	\smallskip
233	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
234	\end{table}
235	
236	\section{Diversity and Selection Analysis}\label{app:diversity}
237	
238	\paragraph{Output diversity quantification.}
239	Table~\ref{tab:diversity} summarizes output diversity across configurations.
240	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
241	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
242	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
243	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
244	
245	\begin{table}[t]
246	\centering
247	\small
248	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
249	\label{tab:diversity}
250	\begin{tabular}{lcc}
251	\toprule
252	Config & Identical & Unique \\
253	\midrule
254	Qwen/SciERC & 11\% & 43\% \\
255	LLaMA/SciERC & 18\% & 39\% \\
256	Qwen/CoNLL & 57\% & --- \\
257	LLaMA/CoNLL & 88\% & --- \\
258	WNUT-17 & 55\% & --- \\
259	\bottomrule
260	\end{tabular}
261	\end{table}
262	
263	\paragraph{Oracle-improvable fraction.}
264	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
265	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
266	
267	\paragraph{Diversity-stratified selection gap.}
268	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
269	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.
270	This rules out insufficient diversity as an explanation for the correlation-selection gap.
271	
272	\paragraph{TOST equivalence testing.}
273	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
274	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
275	The $\delta$ values are anchored to oracle headroom (13--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
276	\texttt{[PENDING: breakpoint $\delta^*$ ranges from X to Y~pp across configurations.]}
277	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
278	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
279	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
280	
281	\begin{table}[t]
282	\centering
283	\small
284	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
285	\label{tab:tost}
286	\begin{tabular}{l cccc cccc}
287	\toprule
288	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
289	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
290	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
291	\midrule
292	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
293	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
294	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
295	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
296	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
297	\bottomrule
298	\end{tabular}
299	\end{table}
300	
301	\section{Multi-Seed Stability}\label{app:multiseed}
302	
303	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC NER ($N{=}8$, $T{=}1.0$).
304	The signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals, confirming that our findings are robust to random seed variation.
305	LLaMA absolute values are systematically lower than Qwen, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
306	
307	\begin{table}[t]
308	\centering
309	\small
310	\caption{Multi-seed quality estimation on SciERC NER ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). Top: Spearman $\rho$; bottom: AUROC. Signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations ($\sigma{\leq}0.025$).}
311	\label{tab:multiseed}
312	\begin{tabular}{lccccc}
313	\toprule
314	& LP & FK & SJ & VC & EM \\
315	\midrule
316	\multicolumn{6}{l}{\textit{Spearman $\rho$ (mean $\pm\sigma$)}} \\
317	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
318	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
319	\midrule
320	\multicolumn{6}{l}{\textit{AUROC (mean $\pm\sigma$)}} \\
321	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
322	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
323	\bottomrule
324	\end{tabular}
325	\end{table}
326	
327	\section{Training Configuration}\label{app:training}
328	
329	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
330	
331	\begin{table}[t]
332	\centering
333	\small
334	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
335	\label{tab:training}
336	\begin{tabular}{ll}
337	\toprule
338	Parameter & Value \\
339	\midrule
340	LoRA rank / $\alpha$ & 32 / 64 \\
341	LoRA target & All linear modules \\
342	LoRA dropout & 0 \\
343	Optimizer & AdamW \\
344	Learning rate & 2e-4, cosine schedule \\
345	Warmup ratio & 0.1 \\
346	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
347	Epochs & 5 \\
348	Max sequence length & 2048 \\
349	Precision & bf16 \\
350	Gradient checkpointing & Enabled \\
351	Max gradient norm & 1.0 \\
352	Training seed & 42 \\
353	Framework & LLaMA Factory \\
354	\midrule
355	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
356	SciERC split & 1861 / 275 / 551 \\
357	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
358	& eval\_steps${=}$200, save\_limit${=}$5 \\
359	\bottomrule
360	\end{tabular}
361	\end{table}
362	
363	\paragraph{Prompt template.}
364	For NER, we use a structured prompt:
365	\begin{quote}
366	\small
367	\texttt{System:} You are an expert in Named Entity Recognition.\\
368	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
369	Text: \texttt{\{input\_text\}}\\
370	Entity types: \texttt{\{schema\_types\}}
371	\end{quote}
372	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
373	
374	\paragraph{Constrained decoding.}
375	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
376	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training did not explicitly disable thinking tokens (\texttt{enable\_thinking}); CoNLL and WNUT explicitly set this to false. Constrained decoding at inference time overrides any thinking behavior by enforcing JSON-only output.}
377	
378	\section{Log-Probability Score Compression}\label{app:logprob_ties}
379	
380	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}).
381	The median within-instance LP range is only 0.041, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
382	At $\varepsilon{=}0.05$, 60.3\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.
383	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
384	
385	\begin{table}[t]
386	\centering
387	\small
388	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
389	\label{tab:logprob_ties}
390	\begin{tabular}{lc}
391	\toprule
392	$\varepsilon$ threshold & Tied instances (\%) \\
393	\midrule
394	0.01 & 1.1\% \\
395	0.05 & 60.3\% \\
396	0.1  & ${\sim}$84\% \\
397	0.5  & ${\sim}$99\% \\
398	\bottomrule
399	\end{tabular}
400	\end{table}
401	
402	\paragraph{Non-tied subset.}
403	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
404	This confirms that LP carries useful per-sample quality information but is resolution-limited under constrained decoding---the signal exists but is compressed below the discrimination threshold for most instances.
405	
406	\section{RE Conditional Selection}\label{app:re_conditional_selection}
407	
408	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
409	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
410	All five signals underperform greedy on both subsets.
411	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
412	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
413	
414	\begin{table}[t]
415	\centering
416	\small
417	\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
418	\label{tab:re_cond_selection}
419	\begin{tabular}{lcc}
420	\toprule
421	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
422	\midrule
423	Oracle & 0.585 & 0.757 \\
424	\midrule
425	LP & 0.395 & 0.600 \\
426	SJ & 0.386 & 0.604 \\
427	EM & 0.372 & 0.583 \\
428	VC & 0.359 & 0.574 \\
429	\midrule
430	Greedy & 0.404 & 0.674 \\
431	\bottomrule
432	\end{tabular}
433	\end{table}
434	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "e073f905-3b1b-4935-9b93-396985a62c3a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad VC &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad LP &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.021$).\nSJ, EM, and voting confidence scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.363$, FK $\\rho{=}0.327$).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested settings: Qwen SciERC (VC $\\rho{=}0.411$ vs.\\ LP 0.259, $\\Delta{=}{+}0.152$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ LP $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLP shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). SJ: Soft Jaccard, FK: Fleiss' $\\kappa$, EM: Exact Match, LP: Log-prob, VC: Voting Confidence. Best non-oracle signal per row in \\textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2024scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\nThe $\\delta$ values are anchored to oracle headroom (13--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\n\\texttt{[PENDING: breakpoint $\\delta^*$ ranges from X to Y~pp across configurations.]}\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ greedy).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC NER ($N{=}8$, $T{=}1.0$).\nThe signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals, confirming that our findings are robust to random seed variation.\nLLaMA absolute values are systematically lower than Qwen, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC NER ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). Top: Spearman $\\rho$; bottom: AUROC. Signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations ($\\sigma{\\leq}0.025$).}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training did not explicitly disable thinking tokens (\\texttt{enable\\_thinking}); CoNLL and WNUT explicitly set this to false. Constrained decoding at inference time overrides any thinking behavior by enforcing JSON-only output.}\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}).\nThe median within-instance LP range is only 0.041, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nThis confirms that LP carries useful per-sample quality information but is resolution-limited under constrained decoding---the signal exists but is compressed below the discrimination threshold for most instances.\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform greedy on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 434,
      "startLine": 1,
      "totalLines": 434
    }
  }
}
```

</details>

---


### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_018bfhh3j22xmpBatqbMpYNN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "d05608b2-464b-42c4-b268-26e19c1e5020",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoTnsLYV7RxSFruprDEknq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17299,
      "cache_read_input_tokens": 31660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17299
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

_source line 63 · 2026-05-15T09:34:59.764Z_

<details><summary>↩ Tool result · `toolu_018bfhh3j22xmpBatqbMpYNN`</summary>

```text
1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
45	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
46	  booktitle = {W-NUT Workshop at EMNLP 2017},
47	  year = {2017},
48	  url = {https://aclanthology.org/W17-4418/}
49	}
50	
51	@inproceedings{desai2020calibration,
52	  title = {Calibration of Pre-trained Transformers},
53	  author = {Desai, Shrey and Durrett, Greg},
54	  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
55	  year = {2020},
56	  doi = {10.18653/v1/2020.emnlp-main.21},
57	  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}
58	}
59	
60	@inproceedings{eikema2022sampling,
61	  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},
62	  author = {Eikema, Bryan and Aziz, Wilker},
63	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
64	  year = {2022},
65	  pages = {10978--10993},
66	  doi = {10.18653/v1/2022.emnlp-main.754}
67	}
68	
69	@inproceedings{fisch2021conformal,
70	  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},
71	  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},
72	  booktitle = {ICML 2021},
73	  year = {2021},
74	  doi = {10.5555/3524938.3525234},
75	  url = {https://arxiv.org/abs/2102.08898}
76	}
77	
78	@article{freitag2022high,
79	  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},
80	  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},
81	  journal = {Transactions of the Association for Computational Linguistics},
82	  volume = {10},
83	  year = {2022},
84	  pages = {811--825},
85	  doi = {10.1162/tacl_a_00491}
86	}
87	
88	@inproceedings{he2024uncertainty,
89	  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},
90	  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},
91	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},
92	  year = {2024},
93	  pages = {2823--2835},
94	  doi = {10.18653/v1/2024.findings-naacl.180}
95	}
96	
97	@article{fleiss1971agreement,
98	  title = {Measuring nominal scale agreement among many raters.},
99	  author = {Fleiss, Joseph L.},
100	  journal = {Psychological Bulletin},
101	  year = {1971},
102	  doi = {10.1037/h0031619},
103	  url = {http://dx.doi.org/10.1037/h0031619}
104	}
105	
106	@inproceedings{gal2016dropout,
107	  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},
108	  author = {Gal, Yarin and Ghahramani, Zoubin},
109	  booktitle = {ICML 2016},
110	  year = {2016},
111	  url = {https://arxiv.org/abs/1506.02142}
112	}
113	
114	@inproceedings{geifman2017selective,
115	  title = {Selective Classification for Deep Neural Networks},
116	  author = {Geifman, Yonatan and El-Yaniv, Ran},
117	  booktitle = {NeurIPS 2017},
118	  year = {2017},
119	  url = {https://arxiv.org/abs/1705.08500}
120	}
121	
122	@article{feng2025optimal,
123	  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},
124	  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},
125	  journal = {arXiv preprint arXiv:2511.12309},
126	  year = {2025},
127	  url = {https://arxiv.org/abs/2511.12309}
128	}
129	
130	@inproceedings{geng2024confidence,
131	  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},
132	  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
133	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
134	  year = {2024},
135	  doi = {10.18653/v1/2024.naacl-long.366},
136	  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}
137	}
138	
139	@inproceedings{guo2017calibration,
140	  title = {On Calibration of Modern Neural Networks},
141	  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
142	  booktitle = {ICML 2017},
143	  year = {2017},
144	  url = {https://arxiv.org/abs/1706.04599}
145	}
146	
147	@article{hobelsberger2025systematic,
148	  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},
149	  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},
150	  journal = {arXiv preprint arXiv:2510.20460},
151	  year = {2025},
152	  url = {https://arxiv.org/abs/2510.20460}
153	}
154	
155	@article{jaccard1901distribution,
156	  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},
157	  author = {Jaccard, Paul},
158	  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},
159	  year = {1901},
160	  url = {https://www.researchgate.net/publication/225035806}
161	}
162	
163	@inproceedings{josifoski2022genie,
164	  title = {{GenIE}: Generative Information Extraction},
165	  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},
166	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
167	  year = {2022},
168	  doi = {10.18653/v1/2022.naacl-main.342},
169	  url = {https://arxiv.org/abs/2112.08340}
170	}
171	
172	@article{kadavath2022language,
173	  title = {Language Models (Mostly) Know What They Know},
174	  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},
175	  journal = {arXiv preprint arXiv:2207.05221},
176	  year = {2022},
177	  url = {https://arxiv.org/abs/2207.05221}
178	}
179	
180	@inproceedings{kang2025selfcertainty,
181	  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},
182	  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},
183	  booktitle = {NeurIPS 2025},
184	  year = {2025},
185	  url = {https://arxiv.org/abs/2502.18581}
186	}
187	
188	@inproceedings{kim2024verifiner,
189	  title = {{V}erifi{NER}: Verification-augmented {NER} via Knowledge-grounded Reasoning with Large Language Models},
190	  author = {Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Dongha},
191	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
192	  year = {2024},
193	  pages = {2441--2461},
194	  doi = {10.18653/v1/2024.acl-long.134}
195	}
196	
197	@inproceedings{kim2026reasc,
198	  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},
199	  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},
200	  booktitle = {ACL 2026},
201	  year = {2026},
202	  url = {https://arxiv.org/abs/2601.02970}
203	}
204	
205	@article{kossen2024semantic,
206	  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},
207	  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},
208	  journal = {arXiv preprint arXiv:2406.15927},
209	  year = {2024},
210	  url = {https://arxiv.org/abs/2406.15927}
211	}
212	
213	@article{li2025llms,
214	  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},
215	  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},
216	  journal = {arXiv preprint arXiv:2503.04104},
217	  year = {2025},
218	  url = {https://arxiv.org/abs/2503.04104}
219	}
220	
221	@inproceedings{kuhn2023semantic,
222	  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},
223	  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},
224	  booktitle = {ICLR 2023},
225	  year = {2023},
226	  url = {https://arxiv.org/abs/2302.09664}
227	}
228	
229	@inproceedings{malinin2021uncertainty,
230	  title = {Uncertainty Estimation in Autoregressive Structured Prediction},
231	  author = {Malinin, Andrey and Gales, Mark},
232	  booktitle = {International Conference on Learning Representations},
233	  year = {2021},
234	  url = {https://openreview.net/forum?id=jN5y-zb5Q7m}
235	}
236	
237	@inproceedings{lakshminarayanan2017ensembles,
238	  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},
239	  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},
240	  booktitle = {NeurIPS 2017},
241	  year = {2017},
242	  url = {https://arxiv.org/abs/1612.01474}
243	}
244	
245	@inproceedings{li2023codeie,
246	  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
247	  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
248	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
249	  year = {2023},
250	  doi = {10.18653/v1/2023.acl-long.855},
251	  url = {https://arxiv.org/abs/2305.05711}
252	}
253	
254	@inproceedings{lightman2024verify,
255	  title = {Let's Verify Step by Step},
256	  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
257	  booktitle = {ICLR 2024},
258	  year = {2024},
259	  url = {https://arxiv.org/abs/2305.20050}
260	}
261	
262	@inproceedings{luan2018scierc,
263	  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
264	  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
265	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
266	  year = {2018},
267	  doi = {10.18653/v1/D18-1360},
268	  url = {http://dx.doi.org/10.18653/v1/D18-1360}
269	}
270	
271	@inproceedings{manakul2023selfcheckgpt,
272	  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},
273	  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},
274	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
275	  year = {2023},
276	  doi = {10.18653/v1/2023.emnlp-main.557},
277	  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}
278	}
279	
280	@article{nedellec2026consistency,
281	  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},
282	  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},
283	  journal = {Genomics \& Informatics},
284	  year = {2026},
285	  doi = {10.1186/s44342-025-00063-2},
286	  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}
287	}
288	
289	@article{oh2025latentsc,
290	  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},
291	  author = {Oh, Jungsuk and Lee, Jay-Yoon},
292	  journal = {arXiv preprint arXiv:2508.18395},
293	  year = {2025},
294	  url = {https://arxiv.org/abs/2508.18395}
295	}
296	
297	@inproceedings{sainz2024gollie,
298	  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
299	  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},
300	  booktitle = {ICLR 2024},
301	  year = {2024},
302	  url = {https://arxiv.org/abs/2310.03668}
303	}
304	
305	@inproceedings{shelmanov2021active,
306	  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},
307	  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},
308	  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},
309	  year = {2021},
310	  doi = {10.18653/v1/2021.eacl-main.145},
311	  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}
312	}
313	
314	@inproceedings{snell2024scaling,
315	  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
316	  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
317	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
318	  year = {2025},
319	  url = {https://arxiv.org/abs/2408.03314}
320	}
321	
322	@inproceedings{taubenfeld2025cisc,
323	  title = {Confidence Improves Self-Consistency in LLMs},
324	  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},
325	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
326	  year = {2025},
327	  doi = {10.18653/v1/2025.findings-acl.1030},
328	  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}
329	}
330	
331	@inproceedings{thirukovalluru2024atomic,
332	  title = {Atomic Self-Consistency for Better Long Form Generations},
333	  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},
334	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
335	  year = {2024},
336	  doi = {10.18653/v1/2024.emnlp-main.706},
337	  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}
338	}
339	
340	@inproceedings{tjongkimsang2003conll,
341	  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},
342	  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},
343	  booktitle = {CoNLL 2003},
344	  year = {2003},
345	  url = {https://aclanthology.org/W03-0419/}
346	}
347	
348	@inproceedings{vashurin2025cocoa,
349	  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},
350	  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},
351	  booktitle = {NeurIPS 2025},
352	  year = {2025},
353	  url = {https://arxiv.org/abs/2502.04964}
354	}
355	
356	@inproceedings{wadhwa2023revisiting,
357	  title = {Revisiting Relation Extraction in the era of Large Language Models},
358	  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},
359	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
360	  year = {2023},
361	  doi = {10.18653/v1/2023.acl-long.868},
362	  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}
363	}
364	
365	@article{wang2023instructuie,
366	  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
367	  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
368	  journal = {arXiv preprint arXiv:2304.08085},
369	  year = {2023},
370	  url = {https://arxiv.org/abs/2304.08085}
371	}
372	
373	@inproceedings{wang2023selfconsistency,
374	  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
375	  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
376	  booktitle = {ICLR 2023},
377	  year = {2023},
378	  url = {https://arxiv.org/abs/2203.11171}
379	}
380	
381	@inproceedings{wang2025make,
382	  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},
383	  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},
384	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
385	  pages = {6919--6932},
386	  year = {2025}
387	}
388	
389	@inproceedings{wang2024mathshepherd,
390	  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},
391	  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},
392	  booktitle = {ACL 2024},
393	  year = {2024},
394	  url = {https://arxiv.org/abs/2312.08935}
395	}
396	
397	@inproceedings{wang2025rankedvoting,
398	  title = {Ranked Voting based Self-Consistency of Large Language Models},
399	  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},
400	  booktitle = {ACL Findings 2025},
401	  year = {2025},
402	  url = {https://arxiv.org/abs/2505.10772}
403	}
404	
405	@article{wen2025know,
406	  title = {Know Your Limits: A Survey of Abstention in Large Language Models},
407	  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},
408	  journal = {Transactions of the Association for Computational Linguistics},
409	  year = {2025},
410	  doi = {10.1162/tacl_a_00754},
411	  url = {http://dx.doi.org/10.1162/tacl_a_00754}
412	}
413	
414	@article{willard2023guided,
415	  title = {Efficient Guided Generation for Large Language Models},
416	  author = {Willard, Brandon T. and Louf, Rémi},
417	  journal = {arXiv preprint arXiv:2307.09702},
418	  year = {2023},
419	  url = {https://arxiv.org/abs/2307.09702}
420	}
421	
422	@inproceedings{xia2025survey,
423	  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},
424	  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},
425	  booktitle = {ACL Findings 2025},
426	  year = {2025},
427	  url = {https://aclanthology.org/2025.findings-acl.1101/}
428	}
429	
430	@article{xiao2019uncertainty,
431	  title = {Quantifying Uncertainties in Natural Language Processing Tasks},
432	  author = {Xiao, Yijun and Wang, William Yang},
433	  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},
434	  year = {2019},
435	  doi = {10.1609/aaai.v33i01.33017322},
436	  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}
437	}
438	
439	@inproceedings{zhang2023ener,
440	  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},
441	  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},
442	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
443	  year = {2023},
444	  doi = {10.18653/v1/2023.findings-acl.103},
445	  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}
446	}
447	
448	@inproceedings{zheng2024llamafactory,
449	  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},
450	  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},
451	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},
452	  year = {2024},
453	  pages = {400--410},
454	  doi = {10.18653/v1/2024.acl-demos.38}
455	}
456	
457	@inproceedings{zhou2024uniner,
458	  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
459	  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
460	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
461	  year = {2024},
462	  url = {https://arxiv.org/abs/2308.03279}
463	}
464	
465	@inproceedings{xiong2024llm,
466	  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},
467	  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},
468	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
469	  year = {2024},
470	  url = {https://arxiv.org/abs/2306.13063}
471	}
472	
473	@inproceedings{muller2021understanding,
474	  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},
475	  author = {M{\"u}ller, Mathias and Sennrich, Rico},
476	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
477	  year = {2021},
478	  url = {https://arxiv.org/abs/2105.08504}
479	}
480	
481	@inproceedings{heo2025uncertainty,
482	  title = {Do {LLMs} Estimate Uncertainty Well in Instruction Following?},
483	  author = {Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya},
484	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
485	  year = {2025},
486	  url = {https://arxiv.org/abs/2410.14582}
487	}
488	
489	@inproceedings{eikema2025structured,
490	  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},
491	  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},
492	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
493	  year = {2025},
494	  url = {https://arxiv.org/abs/2510.20700}
495	}
496	
497	@article{zhang2025tts,
498	  title = {A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?},
499	  author = {Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and Guo, Zhihan and Wang, Yufei},
500	  journal = {arXiv preprint arXiv:2503.24235},
501	  year = {2025},
502	  url = {https://arxiv.org/abs/2503.24235}
503	}
504	
505	@article{venktesh2025trust,
506	  title = {Trust but Verify! A Survey on Verification Design for Test-time Scaling},
507	  author = {Venktesh, V and Rathee, Mandeep and Anand, Avishek},
508	  journal = {arXiv preprint arXiv:2508.16665},
509	  year = {2025},
510	  url = {https://arxiv.org/abs/2508.16665}
511	}
512	
513	@inproceedings{jinnai2024mbr,
514	  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},
515	  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},
516	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
517	  year = {2024},
518	  url = {https://arxiv.org/abs/2311.05263}
519	}
520	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "0227c1c6-86dd-4c65-ae93-db6bb82804d1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@inproceedings{angelopoulos2021conformal,\n  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},\n  booktitle = {ICLR 2021},\n  year = {2021},\n  url = {https://arxiv.org/abs/2009.14193}\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {HLT-NAACL 2004},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {W-NUT Workshop at EMNLP 2017},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2020},\n  doi = {10.18653/v1/2020.emnlp-main.21},\n  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {ICML 2021},\n  year = {2021},\n  doi = {10.5555/3524938.3525234},\n  url = {https://arxiv.org/abs/2102.08898}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  pages = {2823--2835},\n  doi = {10.18653/v1/2024.findings-naacl.180}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{gal2016dropout,\n  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n  author = {Gal, Yarin and Ghahramani, Zoubin},\n  booktitle = {ICML 2016},\n  year = {2016},\n  url = {https://arxiv.org/abs/1506.02142}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{feng2025optimal,\n  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},\n  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},\n  journal = {arXiv preprint arXiv:2511.12309},\n  year = {2025},\n  url = {https://arxiv.org/abs/2511.12309}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {ICML 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{jaccard1901distribution,\n  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},\n  author = {Jaccard, Paul},\n  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},\n  year = {1901},\n  url = {https://www.researchgate.net/publication/225035806}\n}\n\n@inproceedings{josifoski2022genie,\n  title = {{GenIE}: Generative Information Extraction},\n  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.naacl-main.342},\n  url = {https://arxiv.org/abs/2112.08340}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2024verifiner,\n  title = {{V}erifi{NER}: Verification-augmented {NER} via Knowledge-grounded Reasoning with Large Language Models},\n  author = {Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Dongha},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2024},\n  pages = {2441--2461},\n  doi = {10.18653/v1/2024.acl-long.134}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {ACL 2026},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@article{kossen2024semantic,\n  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},\n  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},\n  journal = {arXiv preprint arXiv:2406.15927},\n  year = {2024},\n  url = {https://arxiv.org/abs/2406.15927}\n}\n\n@article{li2025llms,\n  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},\n  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},\n  journal = {arXiv preprint arXiv:2503.04104},\n  year = {2025},\n  url = {https://arxiv.org/abs/2503.04104}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {International Conference on Learning Representations},\n  year = {2021},\n  url = {https://openreview.net/forum?id=jN5y-zb5Q7m}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1612.01474}\n}\n\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{nedellec2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@article{oh2025latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  journal = {arXiv preprint arXiv:2508.18395},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.18395}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{shelmanov2021active,\n  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},\n  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},\n  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},\n  year = {2021},\n  doi = {10.18653/v1/2021.eacl-main.145},\n  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}\n}\n\n@inproceedings{snell2024scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {CoNLL 2003},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@article{wang2023instructuie,\n  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n  journal = {arXiv preprint arXiv:2304.08085},\n  year = {2023},\n  url = {https://arxiv.org/abs/2304.08085}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2025make,\n  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},\n  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},\n  pages = {6919--6932},\n  year = {2025}\n}\n\n@inproceedings{wang2024mathshepherd,\n  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},\n  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},\n  booktitle = {ACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.08935}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n@article{wen2025know,\n  title = {Know Your Limits: A Survey of Abstention in Large Language Models},\n  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2025},\n  doi = {10.1162/tacl_a_00754},\n  url = {http://dx.doi.org/10.1162/tacl_a_00754}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@article{xiao2019uncertainty,\n  title = {Quantifying Uncertainties in Natural Language Processing Tasks},\n  author = {Xiao, Yijun and Wang, William Yang},\n  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year = {2019},\n  doi = {10.1609/aaai.v33i01.33017322},\n  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}\n}\n\n@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{xiong2024llm,\n  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{heo2025uncertainty,\n  title = {Do {LLMs} Estimate Uncertainty Well in Instruction Following?},\n  author = {Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2410.14582}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@article{zhang2025tts,\n  title = {A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?},\n  author = {Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and Guo, Zhihan and Wang, Yufei},\n  journal = {arXiv preprint arXiv:2503.24235},\n  year = {2025},\n  url = {https://arxiv.org/abs/2503.24235}\n}\n\n@article{venktesh2025trust,\n  title = {Trust but Verify! A Survey on Verification Design for Test-time Scaling},\n  author = {Venktesh, V and Rathee, Mandeep and Anand, Avishek},\n  journal = {arXiv preprint arXiv:2508.16665},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.16665}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n",
      "numLines": 520,
      "startLine": 1,
      "totalLines": 520
    }
  }
}
```

</details>

---


### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_01YPqVpTdTBw9KZUTjUEK5eg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "1b47ab28-ef6f-4906-8fe5-f50cfd2fd4c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoTnsLYV7RxSFruprDEknq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17299,
      "cache_read_input_tokens": 31660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17299
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

_source line 65 · 2026-05-15T09:35:00.187Z_

<details><summary>↩ Tool result · `toolu_01YPqVpTdTBw9KZUTjUEK5eg`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is based on the Reuters news corpus; we use the publicly available version and comply with its academic license terms.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "5ab82a28-3f4f-4fef-b686-cf989c14d9a3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors:\\\\ Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).\nCoNLL-2003 is based on the Reuters news corpus; we use the publicly available version and comply with its academic license terms.\nNo new human data was collected or annotated for this study.\nOur findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  }
}
```

</details>

---


### Assistant

_source line 66_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of the paper. Let me also check the 5 bib entries that need to be verified (Minor item 8). Let me also look for what needs to be changed carefully across the bib entries. The task mentions: ye2025uncertainty, snell2024scaling, feng2025optimal, hobelsberger, venktesh.

Let me check:
1. **ye2025uncertainty** - not in the bib file, so maybe it was cited incorrectly
2. **snell2024scaling** - In the bib, it says year 2025 but the cite key is 2024. The booktitle says "ICLR" and year 2025. 

For snell2024scaling, there's a mismatch between the year in the cite key and the actual publication year that needs fixing. Moving on to feng2025optimal—the arXiv ID 2511.12309 indicates November 2025, which aligns with the year 2025 in both the key and metadata, so that checks out. For hobelsberger, I'm looking at the full entry which shows hobelsberger2025systematic. I need to track down ye2025uncertainty since it's listed as something to verify but I'm not finding it cited in the paper. Let me search more carefully through the text to see if it's referenced under a different name or if there's a citation I'm missing. I should also check what "he2024uncertainty" is about since that's flagged for context correction in the minor items. Let me systematically work through the bibliography issues and set up a plan for the edits I need to make.

Looking at the must-fix items, I need to restructure the narrative around the core empirical finding—that regime-specific selection bottlenecks are the real problem, not instance-level signal failures. This means reframing the abstract and introduction to lead with logprob compression and consensus-proximity failures, then simplifying the discussion section to focus on empirical evidence rather than definitional layers. I also need to reorder the contributions to emphasize the selection bottleneck as the primary finding, add the QE evaluation framework as methodology, and include task complexity boundaries as a diagnostic tool. Finally, I need to fix the TOST δ analysis by removing the IAA anchor, using oracle headroom proportions instead, pulling the δ* values from the artifact, and highlighting the small effect size.

For the should-fix items, I'm tracking nine specific corrections: declaring constrained decoding regimes upfront, disclosing Qwen3's thinking tokens in section 4.1, removing "preliminary" language throughout, replacing "cross-model" with the precise scale specification, simplifying the abstract further, standardizing abbreviations, unifying the VC formula definition with threshold-free reporting, and adding the Eikema et al. citation for MBR failure context.

The minor revisions include simplifying Figure 1's caption, moving the N=16 row to the appendix, testing FK agreement significance, removing specific numbers from the semantic entropy footnote, fixing the he2024uncertainty citation context, adding Reuters license info to the ethics statement, including LP in the notation table, verifying five bibliography entries, and noting the N=8 single seed limitation.

The title needs updating to "The Constrained Decoding Bottleneck: Why Confidence Signals Predict but Cannot Select in Information Extraction" based on the D071 suggestion. I'm realizing the paper sections are managed through the edit_paper_section function on the artifacts/_project/paper/ files, but the actual compilation pulls from docs/paper/sections/.

I need to verify whether these directories are in sync or if the MCP tool handles synchronization automatically. Comparing the abstract files between both locations shows some discrepancies, so I should check which version is the authoritative source before making edits. I need to figure out which files the MCP tool actually modifies—the ones in artifacts/_project/paper/ or docs/paper/sections/. Since artifacts only contains abstract, introduction, experiments, discussion, related_work, conclusion, and limitations (but not method or appendix), I should compare one file from each location to see if they're synced or separate, then decide which to edit. I'm going to start making the actual edits now, working systematically through the paper. Let me begin with the Abstract and Introduction sections since MF-1, MF-2, and SF-5 are all interconnected there.

I'm drafting a new abstract that reframes the core problem around test-time scaling and confidence signals for information extraction. The current version buries the main finding under too many specific numbers and signal names, and it doesn't clearly separate the definitional gap from what we actually observe empirically. I need to focus on the constrained decoding bottleneck as the central issue.

The new abstract establishes the problem—whether confidence signals can both estimate quality and select among candidates—then moves into the findings: four of the five signals are instance-level by construction, which is a definitional limitation rather than an empirical discovery. The real empirical finding is that log-probability, despite being the only per-sample signal, also fails because constrained decoding compresses score ranges below 0.05 in 60% of instances, creating effective ties. When we look at the non-tied subset, log-probability does recover a meaningful improvement of +2.9 percentage points over greedy decoding, which shows the signal has discriminative power but is fundamentally resolution-limited by the constrained output space. Consensus-proximity selection faces a similar problem—it can't outperform greedy because it inherits the same instance-level aggregation that makes quality estimation work well in the first place.

The key insight is that signal effectiveness varies with task complexity: structural signals dominate on complex schemas, surface signals work better on simple tasks, and all signals degrade when the model lacks sufficient capability. The bottleneck is clear—constrained-decoding score compression is what's preventing test-time scaling from working effectively in structured information extraction. There's substantial oracle headroom available (16+ percentage points), but unlocking it requires either relaxing the decoding constraints or building selectors that account for this compression problem. We evaluate five signals from three families---structural, surface, and model-internal---on NER and relation extraction under constrained decoding with two 8B-parameter model families across three benchmarks.
Four of five signals aggregate over all samples to produce a single score per instance; they predict input difficulty effectively (Spearman $\rho$ up to 0.50) but cannot, by construction, rank individual candidates.
The key empirical finding concerns log-probability, the sole per-sample signal: constrained decoding compresses within-instance score ranges below 0.05 for 60\% of instances, rendering per-sample discrimination ineffective despite 16+ percentage points of oracle headroom.
Where compression is absent, log-probability selection yields significant gains (+2.9~pp, $p{=}0.01$), confirming that the bottleneck is score resolution under constrained decoding, not the signal itself.
Signal effectiveness varies with task complexity, establishing practical guidance for deployment.
The core insight reframes test-time scaling for structured IE: the real challenge isn't finding good signals but overcoming the compression of per-sample information that constrained decoding introduces.

Now I'm restructuring the introduction to emphasize this compression bottleneck rather than instance-level limitations, and I'll reorder the contributions to highlight the regime-specific finding as the empirical core, followed by the evaluation framework and task complexity boundary.

I'll tackle this systematically—starting with the abstract to establish the new framing, then moving through the introduction, discussion, and experiments sections. For the appendix TOST analysis, I'll keep it but reposition it as supporting evidence. The remaining sections will get targeted updates to align with the new narrative arc.

Before I start executing, I need to clarify whether the editing tools work on the artifacts directory or the docs directory, since I'll need to ensure the changes sync properly. Let me check the abstract in docs to see what I'm working with.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "d881515f-3a4b-47cb-92d6-a870d681ce4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeyZc1QWavDctAvtANKqMe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24464,
      "cache_read_input_tokens": 48959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24464
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 67_

Let me check if the docs and artifacts paper sections are in sync.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "f3cf5d61-5ce4-4fae-b411-96c30ccb4f26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeyZc1QWavDctAvtANKqMe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24464,
      "cache_read_input_tokens": 48959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24464
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01MZD43AEPTSxtLk48JibcWy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "a34e840d-3fed-462b-bcd0-9348b369e10e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeyZc1QWavDctAvtANKqMe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24464,
      "cache_read_input_tokens": 48959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24464
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-15T09:36:32.826Z_

<details><summary>↩ Tool result · `toolu_01MZD43AEPTSxtLk48JibcWy`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best among multiple outputs remains untested for structured tasks.
3	Under constrained decoding---the standard regime for schema-compliant IE---we compare five confidence signals across NER and RE with two 8B-parameter model families.
4	These signals achieve strong quality estimation (Spearman $\rho$ up to 0.38, AUROC up to 0.75), yet none significantly improves sample selection over greedy decoding despite 13--18~pp of oracle headroom---a \textit{correlation-selection gap}.
5	By construction, four of five signals assign identical scores to all candidates from the same input, precluding per-sample selection.
6	The remaining signal---log-probability---fails because constrained decoding compresses its scores (60\% of instances effectively tied), but becomes a significant selector where compression is mitigated ($+2.9$~pp, $p{=}0.01$).
7	Consensus-proximity selection, instantiating minimum Bayes risk decoding, similarly fails because utility correlates with quality across instances but not within them.
8	These results establish that consistency signals are quality estimators, not output selectors, for structured IE under constrained decoding.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "69f4a9d1-2f51-4891-b682-e8c8e2ac2910",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best among multiple outputs remains untested for structured tasks.\nUnder constrained decoding---the standard regime for schema-compliant IE---we compare five confidence signals across NER and RE with two 8B-parameter model families.\nThese signals achieve strong quality estimation (Spearman $\\rho$ up to 0.38, AUROC up to 0.75), yet none significantly improves sample selection over greedy decoding despite 13--18~pp of oracle headroom---a \\textit{correlation-selection gap}.\nBy construction, four of five signals assign identical scores to all candidates from the same input, precluding per-sample selection.\nThe remaining signal---log-probability---fails because constrained decoding compresses its scores (60\\% of instances effectively tied), but becomes a significant selector where compression is mitigated ($+2.9$~pp, $p{=}0.01$).\nConsensus-proximity selection, instantiating minimum Bayes risk decoding, similarly fails because utility correlates with quality across instances but not within them.\nThese results establish that consistency signals are quality estimators, not output selectors, for structured IE under constrained decoding.\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_019osjErxckgH3tpfyri6dus`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "524f4236-304a-48ff-a566-0b88f8371a81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeyZc1QWavDctAvtANKqMe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24464,
      "cache_read_input_tokens": 48959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24464
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-15T09:36:32.840Z_

<details><summary>↩ Tool result · `toolu_019osjErxckgH3tpfyri6dus`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.
17	Our work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\rho{=}0.038$ (n.s.) and LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$)---that would be invisible on a single dataset.
18	
19	Structured IE requires schema-compliant output, making constrained decoding \cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs are unparseable.
20	All experiments use constrained decoding, the regime under which structured IE is practically deployed.
21	
22	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): under constrained decoding, consistency-based signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.
23	By construction, four of five signals assign identical scores to all candidates from the same input, precluding per-sample discrimination.
24	The non-trivial questions are whether (a)~consensus-proximity selection---instantiating MBR decoding \cite{eikema2022sampling, freitag2022high, muller2021understanding} with structural utility functions---can recover discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.
25	Both fail: MBR utility correlates with F1 across instances but not within them (\S\ref{sec:discussion}); log-probability is severely compressed under constrained decoding (60\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
26	Our findings are specific to the constrained decoding regime; whether the gap persists under free-form generation remains an open question.
27	
28	\begin{figure*}[t]
29	\centering
30	\includegraphics[width=\textwidth]{fig_overview}
31	\caption{The correlation-selection gap. \textbf{Left}: consistency signals predict instance-level quality---high agreement correlates with high F1. \textbf{Right}: instance-level signals assign identical scores to all $N$ candidates, precluding sample selection. Consensus-proximity selection does not recover per-sample discrimination.}
32	\label{fig:overview}
33	\end{figure*}
34	
35	We systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
36	Our contributions are:
37	\begin{enumerate}
38	    \item \textbf{The correlation-selection gap and its mechanistic diagnosis.}
39	    We demonstrate that strong quality estimation ($\rho{=}0.38$, AUROC${=}0.75$) coexists with selection failure ($p{>}0.39$, 13--18~pp oracle headroom) under constrained decoding.
40	    Log-probability---the only per-sample signal---fails due to constrained-decoding-induced score compression (60\% of instances effectively tied); where compression is mitigated, it becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
41	    MBR decoding with structural utility functions also fails, as utility correlates with F1 across instances but not within them.
42	
43	    \item \textbf{Task-complexity boundary conditions.}
44	    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.
45	    At the capability boundary (WNUT-17, 52\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\rho{=}{-}0.410$), indicating overconfidence on out-of-distribution inputs.
46	    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).
47	\end{enumerate}
48	
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "33ee6251-d674-431d-a44c-a1d40dac5aca",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.\nOur work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\\rho{=}0.038$ (n.s.) and LP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$)---that would be invisible on a single dataset.\n\nStructured IE requires schema-compliant output, making constrained decoding \\cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs are unparseable.\nAll experiments use constrained decoding, the regime under which structured IE is practically deployed.\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): under constrained decoding, consistency-based signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.\nBy construction, four of five signals assign identical scores to all candidates from the same input, precluding per-sample discrimination.\nThe non-trivial questions are whether (a)~consensus-proximity selection---instantiating MBR decoding \\cite{eikema2022sampling, freitag2022high, muller2021understanding} with structural utility functions---can recover discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.\nBoth fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}); log-probability is severely compressed under constrained decoding (60\\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\nOur findings are specific to the constrained decoding regime; whether the gap persists under free-form generation remains an open question.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: consistency signals predict instance-level quality---high agreement correlates with high F1. \\textbf{Right}: instance-level signals assign identical scores to all $N$ candidates, precluding sample selection. Consensus-proximity selection does not recover per-sample discrimination.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{The correlation-selection gap and its mechanistic diagnosis.}\n    We demonstrate that strong quality estimation ($\\rho{=}0.38$, AUROC${=}0.75$) coexists with selection failure ($p{>}0.39$, 13--18~pp oracle headroom) under constrained decoding.\n    Log-probability---the only per-sample signal---fails due to constrained-decoding-induced score compression (60\\% of instances effectively tied); where compression is mitigated, it becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\n    MBR decoding with structural utility functions also fails, as utility correlates with F1 across instances but not within them.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.\n    At the capability boundary (WNUT-17, 52\\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\\rho{=}{-}0.410$), indicating overconfidence on out-of-distribution inputs.\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}\n\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  }
}
```

</details>

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_011pSJGtrXKQwQ7PhACggXfW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "9cfa0b27-2eb0-4ef8-9b8c-92addf852934",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeyZc1QWavDctAvtANKqMe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24464,
      "cache_read_input_tokens": 48959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24464
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-15T09:36:33.250Z_

<details><summary>↩ Tool result · `toolu_011pSJGtrXKQwQ7PhACggXfW`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	Under constrained decoding, LP scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
14	This diagnostic confirms that LP carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.
15	The LP compression mechanism is a direct consequence of constrained decoding's restricted token space; alternative decoding strategies may yield different LP distributions.
16	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
17	
18	\paragraph{Connection to MBR decoding.}
19	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
20	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
21	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
22	
23	\paragraph{Methodological implications.}
24	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
25	Effective selection likely requires either per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "3d9a8eca-066d-440b-932f-09fc9650fc9a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\nUnder constrained decoding, LP scores are severely compressed: 60\\% of instances have a within-sample range below 0.05, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$; Appendix~\\ref{app:logprob_ties}).\nIn the 40\\% of instances where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\\rho$: 0.08$\\to$0.39).\nThis diagnostic confirms that LP carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.\nThe LP compression mechanism is a direct consequence of constrained decoding's restricted token space; alternative decoding strategies may yield different LP distributions.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires either per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  }
}
```

</details>

---


### Assistant

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
Now I can see that the docs/paper/sections/ versions are MORE RECENT than the artifacts/_project/paper/ versions. The docs versions have already incorporated some of the D070 changes (e.g., the constrained decoding framing, MBR connection, two-layer gap explanation). 

The artifacts/_project/paper/ versions appear to be an older snapshot.

So the docs/paper/sections/ files are the actual source of truth for the compiled paper. Let me work with those.

Now I need to decide: should I use `edit_paper_section` (which modifies artifacts/_project/paper/) or directly edit the docs/paper/sections/ files?


Since docs/paper/sections/ is the actual source, I should edit those files directly with the Edit tool, then use `write_paper_section` to sync the artifacts versions afterward. I'll try using `edit_paper_section` first to see which file it actually modifies, then decide whether to edit the docs versions directly or sync both locations afterward. Either way, I need to read through the remaining sections in docs/paper/sections/ to see what else needs updating.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "6f19ccfa-84d2-406d-9029-94fa1d53f2a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZ9cbRpM5ngPTN68KcSZgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7227,
      "cache_read_input_tokens": 73423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7227
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 75_

The docs/paper/sections/ files are more up-to-date than artifacts/_project/paper/. I'll work with docs/ as the source of truth. Let me also read the remaining docs sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "c8c17809-fee2-4335-a278-9c0766ac6cd1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZ9cbRpM5ngPTN68KcSZgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7227,
      "cache_read_input_tokens": 73423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7227
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01V2yLXhxbyWKyBJoWFCeYv5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "5d8d5e4c-a26e-4fba-92a8-d32dc6d5ee8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZ9cbRpM5ngPTN68KcSZgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7227,
      "cache_read_input_tokens": 73423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7227
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-15T09:36:48.719Z_

<details><summary>↩ Tool result · `toolu_01V2yLXhxbyWKyBJoWFCeYv5`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training inconsistency: Qwen3-8B's SciERC checkpoint was trained without explicitly disabling \texttt{enable\_thinking}, while CoNLL-2003 and WNUT-17 checkpoints disabled it.
16	\texttt{[PENDING: Main Agent confirming actual training state.]}
17	This may affect LP distributions for SciERC specifically; we discuss implications in the Limitations section.
18	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
19	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
20	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
21	
22	%% ============================================================
23	\subsection{Quality Estimation Results}
24	\label{sec:qe_results}
25	
26	\begin{table*}[t]
27	\centering
28	\small
29	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
30	\label{tab:quality_estimation}
31	\begin{tabular}{ll cc cc cc cc}
32	\toprule
33	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
34	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
35	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
36	\midrule
37	VC & Structural & \textbf{.379} & .684 & \textbf{.350} & .693 & .424 & .789 & .426 & .709 \\
38	SJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
39	FK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
40	EM  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
41	LP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \textbf{.761} \\
42	\bottomrule
43	\end{tabular}
44	\end{table*}
45	
46	\begin{figure*}[t]
47	\centering
48	\includegraphics[width=\textwidth]{fig_signal_heatmap}
49	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
50	\label{fig:signal_heatmap}
51	\end{figure*}
52	
53	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
54	
55	\paragraph{Difficulty-dependent signal complementarity.}
56	On SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$).
57	This advantage persists on RE (VC $\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\% zero-F1 floor effect.
58	VC and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
59	While the best $\rho{=}0.38$ (VC) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{For scale context, semantic entropy \cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA, though direct comparison is not meaningful due to fundamentally different output spaces and evaluation protocols.}
60	Pairwise bootstrap CIs confirm the SJ advantage over LP ($\Delta\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\Delta\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal}).
61	
62	\paragraph{$\rho$--AUROC dissociation.}
63	Signal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295), preferred for binary quality triage; structural signals ($\rho{\geq}0.36$) are better for fine-grained ranking.
64	On CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\rho$ (0.307), confirming this pattern across datasets.
65	
66	\paragraph{Signal rankings shift with task difficulty.}
67	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.
68	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
69	This crossover---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.
70	Stability across the two model families (both 8B) is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
71	On WNUT-17, where 52\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
72	LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$).
73	We hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.
74	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
75	
76	\paragraph{Conditional filtering.}
77	Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
78	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
79	LP RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
80	This creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
81	
82	%% ============================================================
83	\subsection{The Correlation-Selection Gap}
84	\label{sec:selection_gap}
85	
86	\begin{figure*}[t]
87	\centering
88	\includegraphics[width=\textwidth]{fig_selection_gap}
89	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound.}
90	\label{fig:selection_gap}
91	\end{figure*}
92	
93	\begin{table}[t]
94	\centering
95	\small
96	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \textbf{bold}. EM selects the plurality output; despite a 42\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}
97	\label{tab:selection}
98	\begin{tabular}{lcc}
99	\toprule
100	Method & NER F1 & RE F1 \\
101	\midrule
102	Oracle & 0.776 & 0.585 \\
103	\midrule
104	LP           & \textbf{0.650} & 0.395 \\
105	SJ       & 0.645 & 0.386 \\
106	EM        & 0.636 & 0.372 \\
107	VC                 & 0.634 & 0.359 \\
108	\midrule
109	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
110	Random             & 0.608 & 0.354 \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
116	Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.
117	The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
118	We anchor this analysis on SciERC, where output diversity is substantial: only 11--18\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.
119	
120	\paragraph{No significant improvement over greedy.}
121	We exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).
122	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
123	LP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).
124	On RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.
125	TOST equivalence testing confirms most signals are indistinguishable from greedy at ${\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\pm}5$~pp (Table~\ref{tab:tost}, Appendix~\ref{app:diversity}).
126	VC ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{below} greedy.
127	The gap extends to CoNLL (ceiling effect, 57--88\% identical outputs) and WNUT-17 (capability boundary; Table~\ref{tab:cross_selection}).
128	
129	\paragraph{Quality estimation $\neq$ output selection.}
130	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
131	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
132	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
133	
134	%% ============================================================
135	\subsection{Robustness}
136	\label{sec:robustness_main}
137	
138	Consistency-based signals show robust performance across $T{\in}\{0.7, 1.0\}$ (SJ NER $\Delta\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$; Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
139	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
140	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "aedb3667-8857-42df-b470-7e87d6f21114",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nWe note a training inconsistency: Qwen3-8B's SciERC checkpoint was trained without explicitly disabling \\texttt{enable\\_thinking}, while CoNLL-2003 and WNUT-17 checkpoints disabled it.\n\\texttt{[PENDING: Main Agent confirming actual training state.]}\nThis may affect LP distributions for SciERC specifically; we discuss implications in the Limitations section.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Difficulty-dependent signal complementarity.}\nOn SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and LP ($\\rho{=}0.205$).\nThis advantage persists on RE (VC $\\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\\% zero-F1 floor effect.\nVC and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (VC) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{For scale context, semantic entropy \\cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA, though direct comparison is not meaningful due to fundamentally different output spaces and evaluation protocols.}\nPairwise bootstrap CIs confirm the SJ advantage over LP ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\\Delta\\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal}).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nSignal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295), preferred for binary quality triage; structural signals ($\\rho{\\geq}0.36$) are better for fine-grained ranking.\nOn CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\\rho$ (0.307), confirming this pattern across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis crossover---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.\nStability across the two model families (both 8B) is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 52\\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$).\nWe hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \\citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLP RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \\textbf{bold}. EM selects the plurality output; despite a 42\\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLP           & \\textbf{0.650} & 0.395 \\\\\nSJ       & 0.645 & 0.386 \\\\\nEM        & 0.636 & 0.372 \\\\\nVC                 & 0.634 & 0.359 \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial: only 11--18\\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.\n\n\\paragraph{No significant improvement over greedy.}\nWe exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.\nTOST equivalence testing confirms most signals are indistinguishable from greedy at ${\\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\\pm}5$~pp (Table~\\ref{tab:tost}, Appendix~\\ref{app:diversity}).\nVC ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{below} greedy.\nThe gap extends to CoNLL (ceiling effect, 57--88\\% identical outputs) and WNUT-17 (capability boundary; Table~\\ref{tab:cross_selection}).\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals show robust performance across $T{\\in}\\{0.7, 1.0\\}$ (SJ NER $\\Delta\\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$; Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nNER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\n",
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

_source line 78_

<details open><summary>🔧 Tool call — Read · `toolu_01Qze3P53strRucodXhF7LZT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "3f002676-6bd9-43b9-8d61-38161049c19f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZ9cbRpM5ngPTN68KcSZgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7227,
      "cache_read_input_tokens": 73423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7227
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-15T09:36:49.215Z_

<details><summary>↩ Tool result · `toolu_01Qze3P53strRucodXhF7LZT`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Within the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \textit{correlation-selection gap}.
4	By construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to constrained-decoding-induced score compression.
5	Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.
6	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
7	RE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.
8	Trained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "9327e0ec-9c2d-427c-8c14-a0aef4bbc028",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWithin the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \\textit{correlation-selection gap}.\nBy construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to constrained-decoding-induced score compression.\nWhere compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.\nSignal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.\nRE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.\nTrained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---


### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Read · `toolu_012AXVFdJgwDSATsJFDauyK6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "56e871a1-fbcf-4d1e-94ef-9edf276e890f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZ9cbRpM5ngPTN68KcSZgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7227,
      "cache_read_input_tokens": 73423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7227
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-15T09:36:49.671Z_

<details><summary>↩ Tool result · `toolu_012AXVFdJgwDSATsJFDauyK6`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.
17	Our non-tied subset analysis (\S\ref{sec:discussion}) suggests this compression is the primary driver---quantifying the gap under free-form generation is an important open question.
18	
19	Qwen3-8B supports a thinking mode (\texttt{enable\_thinking}), which was not explicitly disabled during SciERC training (it was disabled for CoNLL and WNUT).
20	At inference time, constrained decoding overrides any thinking behavior by enforcing JSON-only output, so thinking tokens do not appear in generated samples.
21	However, exposure to thinking tokens during training may affect learned representations, introducing a minor inconsistency between the SciERC and CoNLL/WNUT training configurations.
22	
23	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "900a095b-bfee-4dc5-9151-f0b25e37dbc3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nRE selection failure persists even when restricting to non-zero F1 instances (Appendix~\\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nA 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\\sigma{\\leq}0.025$; Table~\\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses only unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nConstrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.\nOur non-tied subset analysis (\\S\\ref{sec:discussion}) suggests this compression is the primary driver---quantifying the gap under free-form generation is an important open question.\n\nQwen3-8B supports a thinking mode (\\texttt{enable\\_thinking}), which was not explicitly disabled during SciERC training (it was disabled for CoNLL and WNUT).\nAt inference time, constrained decoding overrides any thinking behavior by enforcing JSON-only output, so thinking tokens do not appear in generated samples.\nHowever, exposure to thinking tokens during training may affect learned representations, introducing a minor inconsistency between the SciERC and CoNLL/WNUT training configurations.\n\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  }
}
```

</details>

---


### Tool call

_source line 82_

<details open><summary>🔧 Tool call — Read · `toolu_01B7D3jN3zKjy1KfLUPygbs3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "b8bc401c-e041-4b28-baa7-003f26f637a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZ9cbRpM5ngPTN68KcSZgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7227,
      "cache_read_input_tokens": 73423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7227
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-15T09:36:50.026Z_

<details><summary>↩ Tool result · `toolu_01B7D3jN3zKjy1KfLUPygbs3`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling \cite{zhang2025tts}, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.
15	Our Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\S\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).
16	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
17	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \cite{willard2023guided}.
18	
19	\paragraph{Uncertainty estimation and calibration.}
20	Surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs; \citet{xiong2024llm} find LLMs tend toward overconfidence, and \citet{heo2025uncertainty} show calibration degrades with task complexity.
21	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; \citet{kossen2024semantic} distill this into probes; P(True) \cite{kadavath2022language} queries model confidence directly; \citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.
22	Our structural signals instead measure agreement over output \textit{structure}.
23	Neural networks are often miscalibrated \cite{guo2017calibration, desai2020calibration}; deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.
24	Prior NER and sequence-labeling uncertainty work \cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener, kim2024verifiner, he2024uncertainty} operates within discriminative, verification, or transmission-based paradigms.
25	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \cite{wang2024mathshepherd} learn per-sample scoring.
26	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \cite{freitag2022high} and other generation tasks \cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\S\ref{sec:discussion}).
27	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "f1c60de6-38da-4651-9b44-e49964a3bfc3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.\nExtensions to free-form text use LLM-based comparison \\cite{chen2024usc}, atomic sub-claim decomposition \\cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \\cite{manakul2023selfcheckgpt}.\nFor test-time scaling \\cite{zhang2025tts}, \\citet{snell2024scaling} characterize compute scaling laws and \\citet{brown2024monkeys} show best-of-$N$ gains across tasks.\nRecent reward-free selectors include confidence-weighted voting \\cite{taubenfeld2025cisc}, KL-based self-certainty \\cite{kang2025selfcertainty}, adaptive sampling \\cite{kim2026reasc}, ranked aggregation \\cite{wang2025rankedvoting}, and latent-space consistency \\cite{oh2025latentsc}.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \\citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.\nAll of the above target reasoning/QA with discrete answers or specific aggregation strategies.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).\n\n\\paragraph{Consistency for structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.\nTheir work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.\nOur Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\nCoCoA \\cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic} for LLMs; \\citet{xiong2024llm} find LLMs tend toward overconfidence, and \\citet{heo2025uncertainty} show calibration degrades with task complexity.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill this into probes; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.\nOur structural signals instead measure agreement over output \\textit{structure}.\nNeural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; deep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.\nPrior NER and sequence-labeling uncertainty work \\cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener, kim2024verifiner, he2024uncertainty} operates within discriminative, verification, or transmission-based paradigms.\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \\cite{freitag2022high} and other generation tasks \\cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\\S\\ref{sec:discussion}).\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework.\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---


### Assistant

_source line 84_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture of all the paper sections in their current state (docs/paper/sections/). Let me now systematically go through all 21 items and make the edits.

Let me track what the current docs versions already have vs what still needs to be done:

**Already done in docs (compared to artifacts):**
- ρ values updated to constrained decoding values (0.379 instead of 0.502, etc.)
- Two-layer gap explanation in Discussion
- MBR connection in Discussion
- Constrained decoding regime framing in Introduction
- RE preliminary annotations in some places


- SF-4 partially done (Introduction says "two model families" in some places)
- Eikema et al. citation already added in Discussion
- WNUT-17 analysis expanded
- Qwen3 thinking tokens mentioned (but with PENDING marker)
- Selection table updated with new values
- Table 1 already has N=16 footnote pointing to appendix (no N=16 row in main table)

**Still needs to be done:**

### MF-1: Gap narrative restructure
The docs Introduction already has much of this restructure, but the Abstract needs further refinement per D071 to better dismiss the current framing.

Looking at the Discussion, the two-layer structure is already in place—the definitional limitation is covered in 2 sentences, and the constrained-decoding compression discussion is detailed below. The Abstract is where I should focus, as it could more effectively frame the gap before presenting our approach. I see the issue—the current framing already captures the core findings well, but I need to tighten it further and reconsider how the contributions map. The gap and diagnosis should stay as C1, task complexity as C2, but I'm realizing the QE framework itself might be implicit rather than needing separation. Let me strip out the specific percentages and tie counts, keep just the mechanistic insight: constrained decoding breaks signal utility through score compression, and consensus-based selection fails because quality correlates across instances but not within them. That's the real finding—not the numbers, but why these approaches fundamentally don't work for this problem. I'm realizing the contribution structure needs reshuffling—the QE evaluation framework should be elevated to C2 as its own methodological contribution, with the gap diagnosis becoming the empirical core at C1, and task complexity boundaries staying as C3. The current docs are close but missing that explicit QE framework section, so I need to insert it and reorder accordingly.

For the TOST section, I should pull the actual breakpoint δ* ranges from the artifacts to replace that pending placeholder, and make sure the oracle headroom anchoring is clearly emphasized as the grounding mechanism. I need to fill in the PENDING breakpoint data for the δ* ranges across configurations, and then clarify the δ justification in the text. For the constrained decoding regime, I should strengthen the Discussion section with an explicit statement about how the LP compression mechanism is specific to this setting. On the Qwen3 thinking tokens issue, I need to confirm the actual training state rather than leaving it pending—looks like the SciERC checkpoint may have had thinking enabled while the others didn't, which could affect comparability.

I'm also going through the RE conclusions to mark which ones are preliminary versus confirmed findings, checking for inconsistent use of "cross-model" phrasing that should be more precise about the 8B scale comparison, and reviewing the abstract to simplify the core claims. For terminology, I need to ensure abbreviations like IE, LP, and VC are used consistently throughout rather than mixing full names and shorthand.

On the VC formula front, the current footnote describes using a majority threshold, but I should make the no-threshold version the primary definition in Equation 6 and report the actual ρ differences from the artifact data. The Eikema citation is already properly placed in the Discussion. For the Nédellec contribution, I'm tightening the claim about how our work extends theirs—the three directions (structural matching, quality estimation not translating to best-of-N selection, and the difficulty gradient) are solid, but I should present this more concisely without overstating the novelty. I'm working through a checklist of revisions needed for the paper. Most of the major narrative changes are already in place—the Nédellec framing is appropriately positioned as extending prior work rather than claiming novelty, and the WNUT-17 findings with the negative correlation are highlighted as non-obvious. Now I need to verify what's actually been implemented versus what still needs attention: the figure caption, table placement, FK significance testing details, semantic entropy footnote, citation contexts, ethics statement, notation table, bibliography entries, and the N=8 single seed note.

The remaining work breaks down into two categories—items that are essentially complete with only minor refinements needed, and substantive edits that require actual changes to the text. The substantive ones include adding the C2 QE framework to the contributions section, filling in the TOST breakpoint data, confirming the thinking token information in experiments, replacing "cross-model" terminology throughout, simplifying the abstract, unifying terminology, updating the VC formula in methods, softening the Nédellec claim further, and addressing several minor items like the figure caption and FK significance test details.

I also need to add a placeholder for the free-form ablation experiment in the Discussion section since D071 marks it as planned. Now I'm organizing the edits by file to work through them systematically—starting with the main title change, then moving through abstract, introduction, and experiments sections to handle the terminology updates, framework additions, and data confirmations in parallel where possible. I'm going through my editing checklist for the paper sections, starting with the critical fixes. Let me search for a few key things first—instances of "cross-model," whether I'm using full signal names consistently instead of abbreviations, and checking on those uncertainty citations. Actually, I already have all the section text in front of me, so I can just move forward with the edits.

I'll tackle the Abstract, Introduction, and Method sections first since those are the highest priority. The Abstract needs tightening per the simplification note, then I need to add the QE framework contribution to the Introduction between the existing points. After that I'll handle the thinking tokens section in Experiments, then work through the VC formula update in Method.

Looking at the current abstract, it's already fairly tight at nine lines and follows a good problem-finding-significance structure. I can compress it slightly without losing the key points about test-time scaling, confidence signals, and the constrained decoding setup. I'm considering which numbers to keep based on what's most essential to the findings. The correlation-selection gap of 13-18 percentage points is important, as is the 60% compression effect and the +2.9 pp improvement with statistical significance. I should streamline the definitional parts to be more concise while preserving the core empirical results. B-parameter model families on three benchmarks. These signals achieve strong quality estimation, yet none significantly improves sample selection over greedy decoding despite substantial oracle headroom. The core issue breaks down into two parts: most signals are instance-level by design and can't rank individual candidates, while log-probability—the only per-sample signal—fails because constrained decoding compresses its scores into effective ties for most instances. When compression doesn't occur, log-probability selection recovers meaningful gains, confirming the bottleneck is score resolution under constrained decoding rather than the signal itself. Task complexity also shapes which signals perform best, offering practical guidance for real deployments. Constrained-decoding score compression emerges as the primary obstacle to test-time scaling in structured information extraction. I'm reconsidering the abstraction level—keeping the key evidence numbers like the 2.9 percentage point gain and 60% compression rate while removing specific signal names and correlations, focusing instead on the broader categories of structural, surface, and model-internal signals. I'm reorganizing the contributions to emphasize the empirical findings first—the regime-specific bottleneck under constrained decoding where quality estimation signals fail to improve selection—then the evaluation framework and task complexity boundaries that support this diagnosis. Task complexity shows clear boundaries where signal effectiveness breaks down—across both model families at 8B scale, though the magnitude varies by model. At the capability edge where the model struggles most (WNUT-17 with 52% zero F1), the correlations I'm seeing collapse entirely and log-probability actually becomes negatively correlated, suggesting the model is overconfident on inputs it hasn't seen before. The NER results span multiple datasets, but the relation extraction findings are still preliminary since they only come from SciERC.

For the training setup, there's a configuration inconsistency with Qwen3-8B on SciERC where thinking tokens were enabled by default, whereas the other datasets explicitly disabled them. This means the model was trained with empty thinking blocks prepended to responses, adding a few tokens to the loss computation, but since constrained decoding prevents any thinking tokens from appearing in the actual output, the practical impact is minimal—just a small train-test mismatch from the model learning to expect something it never produces.

Now I'm working through the VC formula documentation. The current method section uses Equation 6 as the primary definition but the footnote describes a majority threshold implementation that doesn't match. I need to clarify that Equation 6 is the formal definition without a threshold, report the performance difference when using the majority threshold variant, and add a note about edge cases where no entities are extracted. I'm looking at the breakpoint analysis for the equivalence margins—on NER, the smallest delta-star is 1.28 percentage points for SJ while FK requires 3.38, and for RE it ranges from 2.86 to 6.53 across the signals. At the paper's 2 percentage point margin, only two signals meet the threshold, but expanding to 3 or 5 percentage points brings more into compliance.

Now I'm thinking through the planned ablation to isolate what's driving LP's compression. The key insight is testing whether constrained decoding is the culprit by comparing LP's selection performance in an unconstrained setting where the token space is fully open—if LP performs better there, it confirms the constraint is the bottleneck rather than LP itself being a weak selector. I'd run this on the same NER and RE instances with post-hoc JSON parsing to keep everything else constant and directly compare the score distributions and selection accuracy across both regimes.

I should also make sure the RE results are consistently flagged as preliminary throughout the discussion and conclusion sections. I'm checking where RE-specific conclusions appear in the Discussion section and need to add the "(preliminary, single benchmark)" marker consistently. The Conclusion already has it, but I'm noticing the Discussion mentions several RE findings—like the logprob collapse and miscalibration results—that should be flagged. Let me go through each paragraph systematically to identify which RE conclusions need the annotation added. I'm checking where RE-specific results need preliminary markers—the calibration issue is already flagged, but I should add them to the selection gap discussion and any other RE-only findings. Now I'm looking at the "cross-model" phrasing that needs to be more specific about the two model families and 8B scale, particularly in the appendix sections. After that, I need to standardize the terminology abbreviations throughout. ations consistently throughout. Let me scan the discussion section to see where "exact match" appears—it should be "EM" after the first definition in methods. I'm also noticing "SJ" is used correctly, but I need to verify that all quality estimators follow the same abbreviation pattern once they're introduced. I need to focus on the most glaring inconsistencies where abbreviations should replace full names when referencing signals as metrics. The Figure 1 caption is already concise, so I'll check if it overlaps with sections 4.2 and 4.3 before deciding whether to trim it further.

For the FK excess agreement, I should add a statistical significance test to strengthen the claim that the measured values between −0.4% and −4.0% actually indicate mild negative dependence rather than noise. And for the semantic entropy footnote, I need to complete that thought about how it compares to our approach.

Looking at the he2024uncertainty citation, the current context mentions "discriminative, verification, or transmission-based paradigms" but He et al. 2024 specifically focuses on uncertainty transmission in sequential labeling, so I should refine the citation context to better reflect what that paper actually contributes to the discussion. Now I'm checking the bibliography entries for issues. The first one, ye2025uncertainty, doesn't appear to be in the bib file and I can't find it cited anywhere in the paper, so I'll skip it. For snell2024scaling, there's a mismatch where the key says 2024 but the year field says 2025, and it was posted to arXiv in August 2024 before appearing at ICLR 2025—I should verify the entry is otherwise correct since changing the key would require updating all citations throughout the paper.

Looking at the entry itself, the title, authors, booktitle, and URL all check out, so I'll leave it as is since the year field correctly reflects the publication venue. Moving on to feng2025optimal from November 2025, which has the correct year. Checking the Hobelsberger entry with arXiv ID from October 2025 — that's valid. Moving on to Venktesh's survey on verification design, which has an August 2025 arXiv timestamp and looks good as well.

Now I'm noticing some inconsistencies in the formatting. The Snell entry uses a full proceedings title while others use abbreviated conference names, so I should standardize that. Also, Venktesh's first name is just listed as "V" — ideally I'd want to verify the full name from the arXiv page, but without external access I'll have to leave it as is for now.

Looking at the other entries, they seem fine overall. The arXiv identifiers like the one in oh2025latentsc and wang2025rankedvoting appear reasonable for a May 2026 submission timeline.

Now I need to focus on the actual corrections. For the N=8 single seed note, I should clarify what the σ≤0.025 threshold means in the documentation.

Looking at experiments.tex, the current text mentions N=8 samples at T=1.0 as the primary setup, with N=16 for scaling experiments. The appendix has the multi-seed stability analysis, but the main text doesn't explicitly state that the primary N=8 results come from a single seed. I should add this clarification.

I'm going to start making edits now, organizing them into independent batches so I can work through them systematically.

For Batch 1, I'll tackle the Abstract, the appendix TOST section, and the Method VC formula in parallel since they don't depend on each other.

Then Batch 2 will cover the Introduction contributions, Experiments thinking tokens, and Discussion free-form ablation placeholder.

Batch 3 will handle the smaller scattered edits across various sections.

Now I'm realizing I need to decide on my editing approach. The `edit_paper_section` MCP tool works on the artifacts/_project/paper/ versions, but those are outdated compared to the current docs/paper/sections/ files. If I use the MCP tool, the old_text won't match because the artifacts are stale. I should edit the docs/paper/sections/ files directly with the regular Edit tool, then use `write_paper_section` at the end to sync everything back to artifacts for provenance tracking.

Let me start with the files that need the most changes. I'll work through them file by file, batching multiple edits per file to minimize round trips.

I'll begin with abstract, introduction, and experiments since those are the most critical sections. The abstract needs a complete rewrite, so I'll handle that first, then move through the other files systematically.

For the title, the suggested version emphasizes the constrained-decoding-bottleneck framing more directly than the current one. I should consider whether to adopt it or keep the existing title, since both capture the core idea reasonably well.

Let me stick with the current title—it's already solid and changing it isn't critical right now. I'll focus on executing the substantive edits to the abstract and other sections instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "0719d3a6-922f-4760-b9af-5eb652b66e82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019S2Nxde7iqGiZcQNjhh3hh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8139,
      "cache_read_input_tokens": 80650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8139
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 85_

Now I have a complete picture of all sections. The docs/paper/sections/ files are the most up-to-date compilation source. I'll make all edits there.

Starting with the Must-Fix items. Making parallel edits to abstract, introduction, and appendix (TOST).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "ead02e48-c3a3-49b3-9e9e-4129e010bb4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019S2Nxde7iqGiZcQNjhh3hh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8139,
      "cache_read_input_tokens": 80650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8139
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Edit · `toolu_01CwwyjvagwN1sJrZ4mnsNe4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
  "old_string": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best among multiple outputs remains untested for structured tasks.\nUnder constrained decoding---the standard regime for schema-compliant IE---we compare five confidence signals across NER and RE with two 8B-parameter model families.\nThese signals achieve strong quality estimation (Spearman $\\rho$ up to 0.38, AUROC up to 0.75), yet none significantly improves sample selection over greedy decoding despite 13--18~pp of oracle headroom---a \\textit{correlation-selection gap}.\nBy construction, four of five signals assign identical scores to all candidates from the same input, precluding per-sample selection.\nThe remaining signal---log-probability---fails because constrained decoding compresses its scores (60\\% of instances effectively tied), but becomes a significant selector where compression is mitigated ($+2.9$~pp, $p{=}0.01$).\nConsensus-proximity selection, instantiating minimum Bayes risk decoding, similarly fails because utility correlates with quality across instances but not within them.\nThese results establish that consistency signals are quality estimators, not output selectors, for structured IE under constrained decoding.\n\\end{abstract}",
  "new_string": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction, but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.\nUnder constrained decoding---the standard regime for schema-compliant IE---we evaluate five confidence signals from three families (structural, surface, and model-internal) across NER and relation extraction with two 8B-parameter model families.\nThese signals achieve strong quality estimation but none significantly improves sample selection over greedy decoding despite 13--18 percentage points of oracle headroom.\nThe failure has two layers: four of five signals are instance-level by construction and cannot rank individual candidates; log-probability, the sole per-sample signal, is compressed into effective ties for 60\\% of instances under constrained decoding.\nWhere this compression is absent, log-probability selection recovers significant gains ($+2.9$~pp, $p{=}0.01$), confirming score compression---not signal inadequacy---as the primary bottleneck.\nSignal rankings further depend on task complexity, with findings consistent across model families.\nThese results identify constrained-decoding score compression as the primary obstacle to test-time scaling in structured IE.\n\\end{abstract}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "a2844c28-6031-4a28-b471-48d83ec03924",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019S2Nxde7iqGiZcQNjhh3hh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8139,
      "cache_read_input_tokens": 80650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8139
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-15T09:41:17.628Z_

<details><summary>↩ Tool result · reported error · `toolu_01CwwyjvagwN1sJrZ4mnsNe4`</summary>

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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "bea44d4f-fdcb-4271-bb6f-94468586f0c4",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---


### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Edit · `toolu_01D3Su75yPkvdHz7widQMmfL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
  "old_string": "Our contributions are:\n\\begin{enumerate}\n    \\item \\textbf{The correlation-selection gap and its mechanistic diagnosis.}\n    We demonstrate that strong quality estimation ($\\rho{=}0.38$, AUROC${=}0.75$) coexists with selection failure ($p{>}0.39$, 13--18~pp oracle headroom) under constrained decoding.\n    Log-probability---the only per-sample signal---fails due to constrained-decoding-induced score compression (60\\% of instances effectively tied); where compression is mitigated, it becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\n    MBR decoding with structural utility functions also fails, as utility correlates with F1 across instances but not within them.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.\n    At the capability boundary (WNUT-17, 52\\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\\rho{=}{-}0.410$), indicating overconfidence on out-of-distribution inputs.\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}",
  "new_string": "Our contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Regime-specific selection bottleneck under constrained decoding.}\n    Despite strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75), no signal significantly improves sample selection over greedy decoding ($p{>}0.39$; 13--18~pp oracle headroom unexploited).\n    Log-probability---the only per-sample signal---fails due to score compression under constrained decoding (60\\% of instances effectively tied); where compression is mitigated, it becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\n    Consensus-proximity selection (MBR decoding with structural utility) also fails: utility correlates with F1 across instances but not within them.\n\n    \\item \\textbf{Quality estimation evaluation framework.}\n    We compare five signals from three families on both quality estimation and sample selection for generative IE, separating two objectives that prior work has conflated.\n    The evaluation reveals difficulty-dependent complementarity: structural signals dominate complex schemas while surface signals dominate simple tasks, and binary discrimination (AUROC) and rank correlation ($\\rho$) favor different signal families.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings shift with task difficulty---consistent across two model families at 8B scale, though with model-dependent magnitude.\n    At the capability boundary (WNUT-17, 52\\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\\rho{=}{-}0.410$), indicating overconfidence on out-of-distribution inputs.\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "b7807e12-e56e-45c1-bda8-d76feb56e6df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019S2Nxde7iqGiZcQNjhh3hh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8139,
      "cache_read_input_tokens": 80650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8139
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-15T09:41:28.428Z_

<details><summary>↩ Tool result · reported error · `toolu_01D3Su75yPkvdHz7widQMmfL`</summary>

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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "b69e3a4a-8ccc-4cda-82a0-54c22692863a",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---


### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Edit · `toolu_01HESgvD8mYoY19i721zKCmk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "\t\\texttt{[PENDING: breakpoint $\\delta^*$ ranges from X to Y~pp across configurations.]}",
  "new_string": "\tBreakpoint analysis determines the smallest $\\delta^*$ at which TOST confirms equivalence for each signal: $\\delta^*{=}\\max(|\\text{CI}_\\text{lower}|, |\\text{CI}_\\text{upper}|)$ of the 90\\% CI of the paired mean difference.\n\tOn NER, $\\delta^*$ ranges from 1.28~pp (SJ) to 3.38~pp (FK); on RE (preliminary, single benchmark), from 2.86~pp (LP) to 6.53~pp (VC)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "8aa6b2b6-4e85-4c45-aca9-b2239c2f22e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019S2Nxde7iqGiZcQNjhh3hh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8139,
      "cache_read_input_tokens": 80650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8139
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-15T09:41:31.395Z_

<details><summary>↩ Tool result · reported error · `toolu_01HESgvD8mYoY19i721zKCmk`</summary>

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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "58419f4f-211c-4ac6-ad00-35bf7a692c50",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---


### Assistant

_source line 92_

<details><summary>Logged reasoning block</summary>

```text
The files have been modified since I read them. Let me re-read all three files and then retry the edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "6910c6af-4b52-4fff-82d7-9fb1373e275e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QxMyDKMLByoHQQNGKCjWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14062,
      "cache_read_input_tokens": 88789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14062
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

_source line 93_

Files were modified. Re-reading and retrying.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "69136c67-3b4b-4482-9e91-ddcd587759aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QxMyDKMLByoHQQNGKCjWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14062,
      "cache_read_input_tokens": 88789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14062
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

_source line 94_

<details open><summary>🔧 Tool call — Read · `toolu_01Encegbp2RsAJ7cC6bAh9qF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "9518d3ac-55f6-474d-ab71-8f39eed86343",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QxMyDKMLByoHQQNGKCjWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14062,
      "cache_read_input_tokens": 88789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14062
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

_source line 95 · 2026-05-15T09:41:35.400Z_

<details><summary>↩ Tool result · `toolu_01Encegbp2RsAJ7cC6bAh9qF`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best among multiple outputs remains untested for structured tasks.
3	Under constrained decoding---the standard regime for schema-compliant IE---we compare five confidence signals across NER and RE with two 8B-parameter model families.
4	These signals achieve strong quality estimation (Spearman $\rho$ up to 0.38, AUROC up to 0.75), yet none significantly improves sample selection over greedy decoding despite 13--18~pp of oracle headroom---a \textit{correlation-selection gap}.
5	Four of five signals are instance-level by construction and thus cannot rank candidates; the empirically interesting question is whether consensus-based strategies (MBR/proximity) or per-sample signals (log-probability) can bridge this gap.
6	They cannot: consensus-proximity selection fails because utility correlates with quality across instances but not within them, and log-probability fails because constrained decoding compresses its scores (60\% of instances effectively tied)---though it becomes a significant selector where compression is mitigated ($+2.9$~pp, $p{=}0.01$).
7	These results establish that consistency signals are quality estimators, not output selectors, for structured IE under constrained decoding.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "ac44d345-7778-4ec6-a369-44efc5af3eb2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best among multiple outputs remains untested for structured tasks.\nUnder constrained decoding---the standard regime for schema-compliant IE---we compare five confidence signals across NER and RE with two 8B-parameter model families.\nThese signals achieve strong quality estimation (Spearman $\\rho$ up to 0.38, AUROC up to 0.75), yet none significantly improves sample selection over greedy decoding despite 13--18~pp of oracle headroom---a \\textit{correlation-selection gap}.\nFour of five signals are instance-level by construction and thus cannot rank candidates; the empirically interesting question is whether consensus-based strategies (MBR/proximity) or per-sample signals (log-probability) can bridge this gap.\nThey cannot: consensus-proximity selection fails because utility correlates with quality across instances but not within them, and log-probability fails because constrained decoding compresses its scores (60\\% of instances effectively tied)---though it becomes a significant selector where compression is mitigated ($+2.9$~pp, $p{=}0.01$).\nThese results establish that consistency signals are quality estimators, not output selectors, for structured IE under constrained decoding.\n\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---


### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Read · `toolu_01Fgdo8mtzNDBdMyQcLen34K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "b1df8cdd-3ea9-4601-86e7-e4b843232f4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QxMyDKMLByoHQQNGKCjWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14062,
      "cache_read_input_tokens": 88789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14062
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

_source line 97 · 2026-05-15T09:41:35.868Z_

<details><summary>↩ Tool result · `toolu_01Fgdo8mtzNDBdMyQcLen34K`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.
17	Our work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\rho{=}0.038$ (n.s.) and LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$)---that would be invisible on a single dataset.
18	
19	Structured IE requires schema-compliant output, making constrained decoding \cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs are unparseable.
20	All experiments use constrained decoding, the regime under which structured IE is practically deployed.
21	
22	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): under constrained decoding, consistency-based signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.
23	By construction, four of five signals assign identical scores to all candidates from the same input, precluding per-sample discrimination.
24	The non-trivial questions are whether (a)~consensus-proximity selection---instantiating MBR decoding \cite{eikema2022sampling, freitag2022high, muller2021understanding} with structural utility functions---can recover discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.
25	Both fail: MBR utility correlates with F1 across instances but not within them (\S\ref{sec:discussion}); log-probability is severely compressed under constrained decoding (60\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
26	Our findings are specific to the constrained decoding regime; whether the gap persists under free-form generation remains an open question.
27	
28	\begin{figure*}[t]
29	\centering
30	\includegraphics[width=\textwidth]{fig_overview}
31	\caption{The correlation-selection gap. \textbf{Left}: consistency signals predict instance-level quality---high agreement correlates with high F1. \textbf{Right}: instance-level signals assign identical scores to all $N$ candidates, precluding sample selection. Consensus-proximity selection does not recover per-sample discrimination.}
32	\label{fig:overview}
33	\end{figure*}
34	
35	We systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
36	Our contributions are:
37	\begin{enumerate}
38	    \item \textbf{The correlation-selection gap and its diagnosis.}
39	    We demonstrate that strong quality estimation ($\rho{=}0.38$, AUROC${=}0.75$) coexists with selection failure ($p{>}0.39$, 13--18~pp oracle headroom) under constrained decoding.
40	    Log-probability---the only per-sample signal---fails due to score compression (60\% of instances effectively tied); where compression is mitigated, it becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
41	    Consensus-proximity selection (MBR decoding) also fails to bridge the gap.
42	
43	    \item \textbf{A systematic evaluation framework.}
44	    We compare five confidence signals from three families---structural, surface, and model-internal---across quality estimation, binary discrimination, and sample selection, showing that these metrics decouple and single-metric evaluation risks selecting the wrong signal.
45	
46	    \item \textbf{Task-complexity boundary conditions.}
47	    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.
48	    At the capability boundary (WNUT-17, 52\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\rho{=}{-}0.410$), indicating overconfidence on out-of-distribution inputs.
49	    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).
50	\end{enumerate}
51	
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "cdc9073c-ec48-4a76-8b17-2b0304c96119",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.\nOur work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\\rho{=}0.038$ (n.s.) and LP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$)---that would be invisible on a single dataset.\n\nStructured IE requires schema-compliant output, making constrained decoding \\cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs are unparseable.\nAll experiments use constrained decoding, the regime under which structured IE is practically deployed.\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): under constrained decoding, consistency-based signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.\nBy construction, four of five signals assign identical scores to all candidates from the same input, precluding per-sample discrimination.\nThe non-trivial questions are whether (a)~consensus-proximity selection---instantiating MBR decoding \\cite{eikema2022sampling, freitag2022high, muller2021understanding} with structural utility functions---can recover discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.\nBoth fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}); log-probability is severely compressed under constrained decoding (60\\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\nOur findings are specific to the constrained decoding regime; whether the gap persists under free-form generation remains an open question.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: consistency signals predict instance-level quality---high agreement correlates with high F1. \\textbf{Right}: instance-level signals assign identical scores to all $N$ candidates, precluding sample selection. Consensus-proximity selection does not recover per-sample discrimination.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{The correlation-selection gap and its diagnosis.}\n    We demonstrate that strong quality estimation ($\\rho{=}0.38$, AUROC${=}0.75$) coexists with selection failure ($p{>}0.39$, 13--18~pp oracle headroom) under constrained decoding.\n    Log-probability---the only per-sample signal---fails due to score compression (60\\% of instances effectively tied); where compression is mitigated, it becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\n    Consensus-proximity selection (MBR decoding) also fails to bridge the gap.\n\n    \\item \\textbf{A systematic evaluation framework.}\n    We compare five confidence signals from three families---structural, surface, and model-internal---across quality estimation, binary discrimination, and sample selection, showing that these metrics decouple and single-metric evaluation risks selecting the wrong signal.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.\n    At the capability boundary (WNUT-17, 52\\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\\rho{=}{-}0.410$), indicating overconfidence on out-of-distribution inputs.\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}\n\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  }
}
```

</details>

---


### Tool call

_source line 98_

<details open><summary>🔧 Tool call — Read · `toolu_01Uw3nmAtSaG5zYUmS3jRQ9j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 270,
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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "7b5c4ebb-f007-4806-9496-538453e41b15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QxMyDKMLByoHQQNGKCjWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14062,
      "cache_read_input_tokens": 88789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14062
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

_source line 99 · 2026-05-15T09:41:36.754Z_

<details><summary>↩ Tool result · `toolu_01Uw3nmAtSaG5zYUmS3jRQ9j`</summary>

```text
270	This rules out insufficient diversity as an explanation for the correlation-selection gap.
271	
272	\paragraph{TOST equivalence testing.}
273	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
274	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
275	The $\delta$ values are anchored to oracle headroom (13--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
276	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
277	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
278	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
279	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
280	
281	\begin{table}[t]
282	\centering
283	\small
284	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
285	\label{tab:tost}
286	\begin{tabular}{l cccc cccc}
287	\toprule
288	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
289	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
290	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
291	\midrule
292	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
293	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
294	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
295	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
296	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
297	\bottomrule
298	\end{tabular}
299	\end{table}
300	
301	\section{Multi-Seed Stability}\label{app:multiseed}
302	
303	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC NER ($N{=}8$, $T{=}1.0$).
304	The signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals, confirming that our findings are robust to random seed variation.
305	LLaMA absolute values are systematically lower than Qwen, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
306	
307	\begin{table}[t]
308	\centering
309	\small
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "f30aea47-8b82-4e25-ab31-713562500aa1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "This rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\nThe $\\delta$ values are anchored to oracle headroom (13--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ greedy).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC NER ($N{=}8$, $T{=}1.0$).\nThe signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals, confirming that our findings are robust to random seed variation.\nLLaMA absolute values are systematically lower than Qwen, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small",
      "numLines": 40,
      "startLine": 270,
      "totalLines": 434
    }
  }
}
```

</details>

---


### Assistant

_source line 100_

<details><summary>Logged reasoning block</summary>

```text
The files have been further updated since my earlier read. The abstract and introduction are now even more refined. The TOST section already has the breakpoint data filled in (line 276). Let me check what still needs to be done.

Current state of the paper based on my latest reads:

**Abstract** (latest):
- Already has the two-layer framing
- Already dismisses 4/5 as instance-level by construction
- Mentions consensus-proximity and LP compression
- But still doesn't follow the exact D071 narrative (needs more focus on compression as bottleneck)
- Per SF-5: still has some specific numbers (ρ up to 0.38, AUROC up to 0.75)


- The introduction now has all three contributions clearly laid out: the correlation-selection gap diagnosis, the systematic evaluation framework, and the task-complexity boundary conditions
- It's already removed the "first" claims and mentions the constrained decoding regime

The TOST appendix fix appears to be complete—the breakpoint δ* data is now populated where it was previously marked pending. So MF-3 is already resolved.

Let me reassess what's actually still needed based on the latest file states.

Most of the major fixes are done: the gap narrative has the two-layer structure throughout, contributions are reordered without "first" claims, the TOST data is filled in, constrained decoding is declared in the intro, the Eikema citation is in the discussion, and the minor fixes for N=16, ethics, and notation are all complete.

What still needs attention is the experiments section—it has a pending marker for thinking tokens—and I need to revisit the "preliminary" annotations in the RE section.

Beyond that, I'm looking at several other refinements: tightening the "cross-model" language to be more specific about the 8B scale comparison, potentially reframing the abstract away from raw numbers toward the bottleneck insight, unifying terminology throughout, updating the VC formula, softening the Nédellec claim further, addressing the free-form ablation placeholder in the discussion, and fixing various captions, footnotes, and citations. I should also check the bibliography entries and add a note about the N=8 single seed limitation.

Let me now go through the experiments, methods, and discussion sections to work through these remaining items.

I'm noticing the SF-2 issue immediately—there's still a PENDING marker in experiments.tex about Qwen3-8B's training state, and it's using "training inconsistency" rather than "training confound." I need to resolve that and clean up the language.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "bde1443b-6c4c-4890-8eae-df75f7e691fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6dpwGfp4qh6W9Lt8z6Ex8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 102851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 101_

Good - the abstract and introduction have been updated already, and the TOST data is filled in. Let me re-read experiments and method to check remaining items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "74dab6e7-9b2a-43a7-bd30-edeb187bf715",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6dpwGfp4qh6W9Lt8z6Ex8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 102851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_015PtKjUymBkXz9WfuAyKBdg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 0,
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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "1461e5ea-0cfa-4050-8964-ee2911a4e563",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6dpwGfp4qh6W9Lt8z6Ex8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 102851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-15T09:42:02.699Z_

<details><summary>↩ Tool result · `toolu_015PtKjUymBkXz9WfuAyKBdg`</summary>

```text
0	\section{Experiments}
1	\label{sec:experiments}
2	
3	\subsection{Experimental Setup}
4	\label{sec:setup}
5	
6	\paragraph{Datasets.}
7	We evaluate on three English IE benchmarks spanning a difficulty gradient.
8	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
11	
12	\paragraph{Models and sampling.}
13	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
14	We note a training inconsistency: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking} active (LLaMA Factory default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) before each response during training; CoNLL-2003 and WNUT-17 checkpoints explicitly disabled this feature.
15	At inference time, constrained decoding correctly suppresses thinking tokens in all configurations.
16	The empty thinking blocks constitute a minor train--test distribution mismatch for SciERC; we discuss potential implications in the Limitations section.
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
18	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
19	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
20	
21	%% ============================================================
22	\subsection{Quality Estimation Results}
23	\label{sec:qe_results}
24	
25	\begin{table*}[t]
26	\centering
27	\small
28	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
29	\label{tab:quality_estimation}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "46ce846d-3e2e-4888-9f2f-0cff0c9b1c82",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nWe note a training inconsistency: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active (LLaMA Factory default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) before each response during training; CoNLL-2003 and WNUT-17 checkpoints explicitly disabled this feature.\nAt inference time, constrained decoding correctly suppresses thinking tokens in all configurations.\nThe empty thinking blocks constitute a minor train--test distribution mismatch for SciERC; we discuss potential implications in the Limitations section.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}",
      "numLines": 30,
      "startLine": 0,
      "totalLines": 140
    }
  }
}
```

</details>

---


### Tool call

_source line 104_

<details open><summary>🔧 Tool call — Read · `toolu_01GgYC36y2BR7cqs3TMM7myG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
  "offset": 50,
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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "dc0f7542-6878-47d6-8c5f-337ad980331c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6dpwGfp4qh6W9Lt8z6Ex8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 102851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-15T09:42:03.655Z_

<details><summary>↩ Tool result · `toolu_01GgYC36y2BR7cqs3TMM7myG`</summary>

```text
50	We use $\max(|g_i|, |g_j|)$ rather than $|g_i \cup g_j|$ as the normalizer to penalize length asymmetry between samples.
51	The instance-level signal averages over all pairs:
52	\begin{equation}\label{eq:sj_instance}
53	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
54	\end{equation}
55	
56	\paragraph{Entity voting confidence (structural, instance-level).}
57	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
58	The instance-level confidence is the mean frequency:
59	\begin{equation}\label{eq:voting}
60	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
61	\end{equation}
62	When $E_\cup = \emptyset$ (no entity extracted by any sample), we set $c_{\mathrm{vc}}(x) = 0$.\footnote{This occurs in $<$1\% of instances in our experiments (WNUT-17 only). We also tested a majority-threshold variant (counting only entities with frequency ${>}N/2$); NER $\rho$ drops from 0.379 to 0.252, RE $\rho$ from 0.350 to 0.331. The no-threshold version (Eq.~\ref{eq:voting}) is used throughout.}
63	
64	\subsection{Evaluation Framework}\label{sec:evaluation}
65	
66	\paragraph{Quality estimation.}
67	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
68	
69	\paragraph{Sample selection.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "2bfb5ea2-a3db-437a-9b85-3f3a1d485c03",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "We use $\\max(|g_i|, |g_j|)$ rather than $|g_i \\cup g_j|$ as the normalizer to penalize length asymmetry between samples.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$ (no entity extracted by any sample), we set $c_{\\mathrm{vc}}(x) = 0$.\\footnote{This occurs in $<$1\\% of instances in our experiments (WNUT-17 only). We also tested a majority-threshold variant (counting only entities with frequency ${>}N/2$); NER $\\rho$ drops from 0.379 to 0.252, RE $\\rho$ from 0.350 to 0.331. The no-threshold version (Eq.~\\ref{eq:voting}) is used throughout.}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nWe measure rank correlation (Spearman $\\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.\n\n\\paragraph{Sample selection.}",
      "numLines": 20,
      "startLine": 50,
      "totalLines": 76
    }
  }
}
```

</details>

---


### Tool call

_source line 106_

<details open><summary>🔧 Tool call — Read · `toolu_01EhGbg9NChcMDsfZ9hRKa5B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "a63ce030-93b4-4bc1-8051-755422a29839",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6dpwGfp4qh6W9Lt8z6Ex8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 102851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-15T09:42:04.089Z_

<details><summary>↩ Tool result · `toolu_01EhGbg9NChcMDsfZ9hRKa5B`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	Under constrained decoding, LP scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
14	This diagnostic confirms that LP carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.
15	The LP compression mechanism is a direct consequence of constrained decoding's restricted token space; alternative decoding strategies may yield different LP distributions.
16	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
17	
18	\paragraph{Connection to MBR decoding.}
19	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
20	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
21	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
22	
23	\paragraph{Methodological implications.}
24	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
25	Effective selection likely requires either per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "b67c5e5e-2676-4485-82ff-9101d172b661",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\nUnder constrained decoding, LP scores are severely compressed: 60\\% of instances have a within-sample range below 0.05, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$; Appendix~\\ref{app:logprob_ties}).\nIn the 40\\% of instances where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\\rho$: 0.08$\\to$0.39).\nThis diagnostic confirms that LP carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.\nThe LP compression mechanism is a direct consequence of constrained decoding's restricted token space; alternative decoding strategies may yield different LP distributions.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires either per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  }
}
```

</details>

---


### Assistant

_source line 108_

<details><summary>Logged reasoning block</summary>

```text
OK, now I have the latest state of all three key files. Let me reassess what's done and what's still needed:

**Already done:**
1. ✅ MF-1: Gap narrative restructure - Two-layer structure in abstract, intro, discussion
2. ✅ MF-2: Contributions reordered to 3 items, no "first" claims
3. ✅ MF-3: TOST breakpoint δ* data filled in
4. ✅ SF-1: Constrained decoding declaration in intro (lines 19-20) and discussion (lines 14-15)


5. ✅ SF-2: Thinking tokens PENDING removed - now has confirmed info (experiments line 14-16)
6. ✅ SF-7: VC formula updated in method (line 62, footnote has ρ diff data)
7. ✅ SF-8: Eikema citation in discussion (line 21)
8. ✅ Minor 2: N=16 to appendix (done)
9. ✅ Minor 6: Ethics CoNLL Reuters (done)
10. ✅ Minor 7: Notation LP (done)

**Still needs edits:**

Looking at the abstract, I need to trim it down following the problem-finding-significance structure and remove the specific metrics like the Spearman correlation and AUROC values. I should also strengthen the focus on the constrained decoding bottleneck that D071 highlights.

The discussion is missing the planned free-form ablation that should be included there. I also need to add an explicit statement about the scope of constrained decoding in the standard IE regime, building on what's already mentioned in lines 14-15.

For SF-3, I should verify that all references to the RE annotations don't use the word "preliminary" where they shouldn't.

Now checking through the discussion and conclusion sections to confirm where RE is marked as preliminary. The discussion already flags it as preliminary in line 4 and line 16 with the ECE values. The conclusion also properly notes that RE findings are limited to SciERC alone. Looking at the experiments section, the table captions already include the "preliminary" qualifier for RE. I should verify the selection table caption has this too, but it seems the main places are covered. I should check the Results and Experiments sections more carefully for RE conclusions that need the preliminary marker. Looking at the selection gap analysis, that statement about RE performance compared to greedy should probably have the marker added for consistency. Let me also verify the "cross-model" phrasing—it seems the current text already uses "across two model families at 8B scale" so that's already addressed. Looking at the WNUT-17 findings, they're already framed as non-obvious discoveries in the current text—the conditional correlations collapsing to near-zero while logprob shows strong negative correlation is exactly the kind of unexpected result that justifies extending Nédellec et al.'s work. The phrasing seems solid as is, though I could emphasize these findings even more directly as the key contribution that makes our extension meaningful rather than incremental.

For the Figure 1 caption, I need to check what's currently there and consider if it adequately conveys the correlation-selection gap concept. Looking at the he2024uncertainty citation issue—the current sentence bundles five papers together, but the task specifically asks to improve the citation context for that one paper. I should separate it out to give it proper context rather than lumping it with the others.

Now I'm reviewing the bibliography entries to check for inconsistencies. The snell2024scaling entry has a year mismatch between the key and the actual publication year, and I should verify the author names are complete, particularly for venktesh2025trust. Looking at the remaining entries, snell2024scaling has a publication year mismatch between the arXiv version and the ICLR conference appearance, which is standard for ML papers so no correction needed. The other three entries—feng2025optimal, hobelsberger2025systematic, and venktesh2025trust—appear mostly correct, though the first author of venktesh2025trust might need verification for their full name since only an initial is provided.

Rather than getting stuck on verification I can't complete, I should move forward with the substantive edits I've identified. I'm prioritizing the abstract refinement for SF-5, filling in the free-form ablation placeholder in the discussion, clarifying the scope of constrained decoding in SF-1, adding more preliminary result callouts for SF-3, and addressing the remaining minor issues around significance testing, uncertainty context, seed reporting, cross-model analysis placement, and terminology consistency.

Let me start drafting these changes in parallel. For the abstract, I'm reframing it around the bottleneck insight—that log-probability signals get compressed into ties under constrained decoding, which is why selection fails despite oracle gains being available. The key finding is that while confidence signals work well for quality estimation, they can't actually improve sample selection because the signals themselves become uninformative in the constrained regime. I'm exploring why these consistency signals work well for quality estimation but fail at actually selecting better outputs—the core issue is that consensus-based approaches don't help within individual instances, and log-probability scores get compressed by the constrained decoding process, though this compression can be overcome in certain conditions. The key finding is that these signals measure quality, not selection capability, under this decoding constraint. The abstract is solid—seven sentences that move from problem through findings to the key bottleneck. The compression of log-probability scores affecting 60% of instances is the real insight here, and when that compression doesn't happen, we see the +2.9pp gains that prove the concept works. The note about task complexity and model consistency across families rounds it out well. Now I'm thinking about the discussion section and where to add space for ablation work.

I should add a paragraph that directly tests whether constrained decoding is actually causing the score compression, not just correlating with it. The idea is to run the same selection on free-form generation where the token space is unrestricted—if log-probability selection performs better there, that pins down constrained decoding as the mechanism. I'll note this as a planned experiment on SciERC with post-hoc parsing, and be explicit that all current findings are specific to the constrained regime. I've already established the scope constraints in the intro and discussion, so I just need to add the free-form ablation as a concrete next step. The paragraph I'm drafting predicts that LP compression should disappear when the model has access to the full vocabulary, and proposes a direct comparison between constrained and unconstrained decoding on the same instances to test whether this bottleneck is regime-specific.

Now I'm flagging the planned free-form ablation experiment on SciERC as something to pursue, and I need to make sure the discussion has an explicit statement about the constrained decoding scope. I can integrate this with the ablation paragraph rather than adding redundant language elsewhere.

For the experiments section, I should mark some of the RE results as preliminary since they're still being validated. And there's a minor issue with excess agreement notation in one of the tables that needs cleaning up.

I'm also checking the related work citation for he2024uncertainty to make sure it's properly contextualized, adding a note about the single-seed setup in the experiments section with a reference to multi-seed stability, and verifying that "cross-model" terminology is used consistently throughout the appendix.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "e88e8b43-f3c6-4291-9d16-fd9406a42393",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01322k3ywNszo9itJNVEu89f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3946,
      "cache_read_input_tokens": 106621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3946
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 109_

Let me search for remaining items that need attention.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "3e1608c2-0c58-44b8-b2ad-efcb3510a371",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01322k3ywNszo9itJNVEu89f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3946,
      "cache_read_input_tokens": 106621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3946
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 110_

<details open><summary>🔧 Tool call — Grep · `toolu_01K93aAHR4KD5QVddBsXo2sq`</summary>

```json
{
  "pattern": "cross-model|Cross-model",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "76bfa594-56fd-4ffc-9351-fb69c76c908b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01322k3ywNszo9itJNVEu89f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3946,
      "cache_read_input_tokens": 106621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3946
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-15T09:43:50.576Z_

<details><summary>↩ Tool result · `toolu_01K93aAHR4KD5QVddBsXo2sq`</summary>

```text
docs/paper/sections/appendix.tex:82:\paragraph{Cross-model transfer.}
docs/paper/main.aux:1272:\@writefile{toc}{\contentsline {paragraph}{Cross-model transfer.}{13}{section*.37}\protected@file@percent }
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "da3a06b2-415b-46e2-b2ca-6dd092558a2d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/appendix.tex:82:\\paragraph{Cross-model transfer.}\ndocs/paper/main.aux:1272:\\@writefile{toc}{\\contentsline {paragraph}{Cross-model transfer.}{13}{section*.37}\\protected@file@percent }",
    "numLines": 2
  }
}
```

</details>

---


### Tool call

_source line 112_

<details open><summary>🔧 Tool call — Grep · `toolu_01EFjykDdUqq5bJVJfohJTvk`</summary>

```json
{
  "pattern": "Voting Confidence|voting confidence|entity voting|Exact Match|exact match|Soft Jaccard|log-probability|Log-probability|Fleiss",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "182bddf3-6d21-479e-80c9-960218da9b6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01322k3ywNszo9itJNVEu89f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3946,
      "cache_read_input_tokens": 106621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3946
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-15T09:43:52.641Z_

<details><summary>↩ Tool result · `toolu_01EFjykDdUqq5bJVJfohJTvk`</summary>

```text
docs/paper/sections/related_work.tex:15:Our Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\S\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).
docs/paper/sections/experiments.tex:117:The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
docs/paper/sections/conclusion.tex:4:By construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to constrained-decoding-induced score compression.
docs/paper/sections/discussion.tex:4:For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
docs/paper/sections/discussion.tex:11:\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
docs/paper/sections/method.tex:17:Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
docs/paper/sections/method.tex:18:The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
docs/paper/sections/method.tex:20:\paragraph{Log-probability (model-internal, per-sample).}
docs/paper/sections/method.tex:33:\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
docs/paper/sections/method.tex:43:\paragraph{Soft Jaccard (structural, instance-level).}
docs/paper/sections/method.tex:56:\paragraph{Entity voting confidence (structural, instance-level).}
docs/paper/sections/limitations.tex:23:Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.
docs/paper/sections/abstract.tex:5:Four of five signals are instance-level by construction and thus cannot rank candidates; the empirically interesting question is whether consensus-based strategies (MBR/proximity) or per-sample signals (log-probability) can bridge this gap.
docs/paper/sections/abstract.tex:6:They cannot: consensus-proximity selection fails because utility correlates with quality across instances but not within them, and log-probability fails because constrained decoding compresses its scores (60\% of instances effectively tied)---though it becomes a significant selector where compression is mitigated ($+2.9$~pp, $p{=}0.01$).
docs/paper/sections/appendix.tex:18:SJ & Soft Jaccard similarity \\
docs/paper/sections/appendix.tex:19:FK & Fleiss' $\kappa$ \\
docs/paper/sections/appendix.tex:21:VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
docs/paper/sections/appendix.tex:22:LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
docs/paper/sections/appendix.tex:116:\paragraph{Length vs.\ log-probability.}
docs/paper/sections/appendix.tex:117:Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
docs/paper/sections/appendix.tex:122:\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
docs/paper/sections/appendix.tex:174:\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). SJ: Soft Jaccard, FK: Fleiss' $\kappa$, EM: Exact Match, LP: Log-prob, VC: Voting Confidence. Best non-oracle signal per row in \textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
docs/paper/sections/appendix.tex:190:For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
docs/paper/sections/appendix.tex:380:Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}).
docs/paper/sections/appendix.tex:388:\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
docs/paper/sections/appendix.tex:403:Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
docs/paper/sections/introduction.tex:24:The non-trivial questions are whether (a)~consensus-proximity selection---instantiating MBR decoding \cite{eikema2022sampling, freitag2022high, muller2021understanding} with structural utility functions---can recover discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.
docs/paper/sections/introduction.tex:25:Both fail: MBR utility correlates with F1 across instances but not within them (\S\ref{sec:discussion}); log-probability is severely compressed under constrained decoding (60\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
docs/paper/sections/introduction.tex:35:We systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
docs/paper/sections/introduction.tex:40:    Log-probability---the only per-sample signal---fails due to score compression (60\% of instances effectively tied); where compression is mitigated, it becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "2bd47fa4-9dd5-4288-81db-96f87814deb9",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/related_work.tex:15:Our Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\ndocs/paper/sections/experiments.tex:117:The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\ndocs/paper/sections/conclusion.tex:4:By construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to constrained-decoding-induced score compression.\ndocs/paper/sections/discussion.tex:4:For per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\ndocs/paper/sections/discussion.tex:11:\\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\ndocs/paper/sections/method.tex:17:Four are \\textit{consistency signals}---computed from inter-sample agreement---spanning two families: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]).\ndocs/paper/sections/method.tex:18:The fifth, log-probability, is the sole \\textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.\ndocs/paper/sections/method.tex:20:\\paragraph{Log-probability (model-internal, per-sample).}\ndocs/paper/sections/method.tex:33:\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\ndocs/paper/sections/method.tex:43:\\paragraph{Soft Jaccard (structural, instance-level).}\ndocs/paper/sections/method.tex:56:\\paragraph{Entity voting confidence (structural, instance-level).}\ndocs/paper/sections/limitations.tex:23:Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.\ndocs/paper/sections/abstract.tex:5:Four of five signals are instance-level by construction and thus cannot rank candidates; the empirically interesting question is whether consensus-based strategies (MBR/proximity) or per-sample signals (log-probability) can bridge this gap.\ndocs/paper/sections/abstract.tex:6:They cannot: consensus-proximity selection fails because utility correlates with quality across instances but not within them, and log-probability fails because constrained decoding compresses its scores (60\\% of instances effectively tied)---though it becomes a significant selector where compression is mitigated ($+2.9$~pp, $p{=}0.01$).\ndocs/paper/sections/appendix.tex:18:SJ & Soft Jaccard similarity \\\\\ndocs/paper/sections/appendix.tex:19:FK & Fleiss' $\\kappa$ \\\\\ndocs/paper/sections/appendix.tex:21:VC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\ndocs/paper/sections/appendix.tex:22:LP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\ndocs/paper/sections/appendix.tex:116:\\paragraph{Length vs.\\ log-probability.}\ndocs/paper/sections/appendix.tex:117:Figure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\ndocs/paper/sections/appendix.tex:122:\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\ndocs/paper/sections/appendix.tex:174:\\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). SJ: Soft Jaccard, FK: Fleiss' $\\kappa$, EM: Exact Match, LP: Log-prob, VC: Voting Confidence. Best non-oracle signal per row in \\textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\ndocs/paper/sections/appendix.tex:190:For quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\ndocs/paper/sections/appendix.tex:380:Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}).\ndocs/paper/sections/appendix.tex:388:\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\ndocs/paper/sections/appendix.tex:403:Among instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\ndocs/paper/sections/introduction.tex:24:The non-trivial questions are whether (a)~consensus-proximity selection---instantiating MBR decoding \\cite{eikema2022sampling, freitag2022high, muller2021understanding} with structural utility functions---can recover discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.\ndocs/paper/sections/introduction.tex:25:Both fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}); log-probability is severely compressed under constrained decoding (60\\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\ndocs/paper/sections/introduction.tex:35:We systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\ndocs/paper/sections/introduction.tex:40:    Log-probability---the only per-sample signal---fails due to score compression (60\\% of instances effectively tied); where compression is mitigated, it becomes a significant selector ($+2.9$~pp, $p{=}0.01$).",
    "numLines": 30
  }
}
```

</details>

---


### Tool call

_source line 114_

<details open><summary>🔧 Tool call — Grep · `toolu_01EtYQHRmk6rbUjaw41YH7PZ`</summary>

```json
{
  "pattern": "he2024uncertainty",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "6d30340d-1f6e-4545-bc69-7cecfff7c535",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01322k3ywNszo9itJNVEu89f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3946,
      "cache_read_input_tokens": 106621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3946
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-15T09:43:53.400Z_

<details><summary>↩ Tool result · `toolu_01EtYQHRmk6rbUjaw41YH7PZ`</summary>

```text
docs/paper/references.bib:88:@inproceedings{he2024uncertainty,
docs/paper/main.bbl:130:\bibitem[{He et~al.(2024)He, Yu, Lei, Lu, and Chen}]{he2024uncertainty}
docs/paper/main.aux:242:\citation{xiao2019uncertainty,shelmanov2021active,zhang2023ener,kim2024verifiner,he2024uncertainty}
docs/paper/main.aux:880:\bibcite{he2024uncertainty}{{18}{2024}{{He et~al.}}{{He, Yu, Lei, Lu, and Chen}}}
docs/paper/sections/related_work.tex:24:Prior NER and sequence-labeling uncertainty work \cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener, kim2024verifiner, he2024uncertainty} operates within discriminative, verification, or transmission-based paradigms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "64fbe11d-2f1a-45e5-a406-f860c950012c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/references.bib:88:@inproceedings{he2024uncertainty,\ndocs/paper/main.bbl:130:\\bibitem[{He et~al.(2024)He, Yu, Lei, Lu, and Chen}]{he2024uncertainty}\ndocs/paper/main.aux:242:\\citation{xiao2019uncertainty,shelmanov2021active,zhang2023ener,kim2024verifiner,he2024uncertainty}\ndocs/paper/main.aux:880:\\bibcite{he2024uncertainty}{{18}{2024}{{He et~al.}}{{He, Yu, Lei, Lu, and Chen}}}\ndocs/paper/sections/related_work.tex:24:Prior NER and sequence-labeling uncertainty work \\cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener, kim2024verifiner, he2024uncertainty} operates within discriminative, verification, or transmission-based paradigms.",
    "numLines": 5
  }
}
```

</details>

---


### Assistant

_source line 116_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me compile the remaining edits:

1. **Abstract SF-5**: Remove specific ρ/AUROC numbers, sharpen bottleneck framing
2. **Discussion**: Add free-form ablation placeholder paragraph
3. **Discussion SF-4**: "exact match" → "EM" in line 4
4. **Appendix SF-4**: "Cross-model transfer" → "Transfer across model families" 
5. **Related work Minor 5**: Improve he2024uncertainty citation context
6. **Method Minor 3**: FK excess agreement significance


7. **Experiments Minor 9**: N=8 single seed note
8. **SF-3**: Check for remaining RE preliminary markers needed

For SF-6 (terminology unification), I'm verifying the abbreviation usage across sections—full names belong in method definitions and appendix tables, abbreviations work in experiments, and I need to standardize "exact match" to "EM" in the discussion while keeping the abstract self-contained without abbreviations.

For "log-probability" specifically, I should use "LP" in running text after the method section defines it, though using the full term in discussion and conclusion headings for clarity isn't necessarily problematic—the key is avoiding inconsistency rather than enforcing strict abbreviation rules everywhere.

The real issue I'm spotting is in the discussion where "exact match leads binary discrimination" should use "EM" to stay consistent with abbreviation conventions in that section. Now I'll organize the remaining edits into two batches: one covering abstract, discussion, appendix, related work, and experiments sections that can be done in parallel, and a second batch for the method section that depends on the first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "c2a2f942-56e8-490d-a7b5-bbd181552da6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RXHpKMQctppbAJQmrq5jep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7512,
      "cache_read_input_tokens": 110567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7512
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 117_

Now I have a clear picture of remaining edits. Let me re-read the method FK section, then execute all remaining edits in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "d85d91f7-37bc-445d-9197-295660f7b8d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RXHpKMQctppbAJQmrq5jep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7512,
      "cache_read_input_tokens": 110567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7512
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 118_

<details open><summary>🔧 Tool call — Read · `toolu_01FfLwwRLifdwW67mrPPLXAb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
  "offset": 33,
  "limit": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "89cef302-ce16-4903-a344-63b98284752e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RXHpKMQctppbAJQmrq5jep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7512,
      "cache_read_input_tokens": 110567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7512
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-15T09:44:18.159Z_

<details><summary>↩ Tool result · `toolu_01FfLwwRLifdwW67mrPPLXAb`</summary>

```text
33	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
34	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
35	\begin{equation}\label{eq:fk}
36	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
37	\end{equation}
38	where $\bar{P}$ is mean observed pairwise agreement and $\bar{P}_e$ is expected agreement under random assignment.
39	While FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.
40	Empirically, we measure excess agreement ($\bar{P} - \bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\% and $-$4.0\%, indicating mild \textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.
41	Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.
42	
43	\paragraph{Soft Jaccard (structural, instance-level).}
44	Our primary structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "ce281429-95dc-4614-af2e-9eec6deabdb3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.\nWhile FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.\nEmpirically, we measure excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\\% and $-$4.0\\%, indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.\nUnlike structural signals, FK relies on exact string matching and does not tolerate surface variations.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur primary structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.",
      "numLines": 12,
      "startLine": 33,
      "totalLines": 76
    }
  }
}
```

</details>

---


### Tool call

_source line 120_

<details open><summary>🔧 Tool call — Read · `toolu_01BJDj9cD6w4sDpj4HGkMCLS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 78,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "84adb285-ce4d-42e3-ba5f-e50dc5f78567",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RXHpKMQctppbAJQmrq5jep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7512,
      "cache_read_input_tokens": 110567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7512
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-15T09:44:19.131Z_

<details><summary>↩ Tool result · `toolu_01BJDj9cD6w4sDpj4HGkMCLS`</summary>

```text
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.021$).
80	SJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	
82	\paragraph{Cross-model transfer.}
83	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.363$, FK $\rho{=}0.327$).
84	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
85	At $N{=}16$, the structural-over-LP advantage holds across all four tested settings: Qwen SciERC (VC $\rho{=}0.411$ vs.\ LP 0.259, $\Delta{=}{+}0.152$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ LP $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
86	
87	\section{Calibration Analysis}\label{app:calibration}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "26f2456f-a284-46a1-919c-6f292e17312f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.021$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.363$, FK $\\rho{=}0.327$).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested settings: Qwen SciERC (VC $\\rho{=}0.411$ vs.\\ LP 0.259, $\\Delta{=}{+}0.152$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ LP $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}",
      "numLines": 10,
      "startLine": 78,
      "totalLines": 434
    }
  }
}
```

</details>

---


### Assistant

_source line 122_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have all the information I need. Let me now execute all remaining edits in parallel.

Let me prepare the edits:

1. **Abstract**: Remove ρ/AUROC numbers, sharpen bottleneck framing
2. **Discussion**: Add free-form ablation placeholder + fix "exact match" → "EM"
3. **Appendix**: "Cross-model transfer" → "Transfer across model families"
4. **Related work**: Improve he2024uncertainty context
5. **Experiments**: Add N=8 single seed note


6. **Method**: Add significance note to FK excess agreement

Now I'm looking at the experiments section to add the seed stability note. I found the N=8 sampling line and need to insert text clarifying that primary results use a single seed with multi-seed validation in the appendix confirming robust rankings. I also need to flag the one RE result without a preliminary qualifier.

Actually, let me reconsider—the task specifies adding preliminary tags only in the Discussion/Conclusion sections when citing RE results, not in the experiments section itself. So I should focus on finding where RE conclusions appear in the discussion and conclusion portions instead.

Looking at what's already been marked, the discussion and conclusion sections seem to have the necessary preliminary annotations for RE findings already in place. The bigger consideration is whether to move RE selection details to the appendix as suggested, though that's optional given the paper already has a dedicated appendix section for RE conditional selection and the main text mentions it appropriately.

Now I need to work through the remaining edits, starting with a closer look at the abstract. The current version is quite dense, so I'm reconsidering how to tighten it while preserving the key claims about the correlation-selection gap and the performance of confidence signals. I'm refocusing the narrative around the core bottleneck: while these confidence signals are excellent quality estimators across three model families and three benchmarks, they fundamentally fail at output selection because most are instance-level by construction, and log-probability—the only per-sample signal—gets compressed by constrained decoding, eliminating its discriminative power despite substantial oracle improvements being available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "d3781f1e-f979-4dfb-a58c-2309b329ce46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcCdxATEghYa5SuNvJYcq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2064,
      "cache_read_input_tokens": 118079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2064
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 123_

Now executing all remaining edits in parallel across files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "12ddd42d-4401-4f3d-9207-2c2400bb2a68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcCdxATEghYa5SuNvJYcq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2064,
      "cache_read_input_tokens": 118079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2064
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Edit · `toolu_0163XtTNp21AmzfSF7HnbnzQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
  "old_string": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best among multiple outputs remains untested for structured tasks.\nUnder constrained decoding---the standard regime for schema-compliant IE---we compare five confidence signals across NER and RE with two 8B-parameter model families.\nThese signals achieve strong quality estimation (Spearman $\\rho$ up to 0.38, AUROC up to 0.75), yet none significantly improves sample selection over greedy decoding despite 13--18~pp of oracle headroom---a \\textit{correlation-selection gap}.\nFour of five signals are instance-level by construction and thus cannot rank candidates; the empirically interesting question is whether consensus-based strategies (MBR/proximity) or per-sample signals (log-probability) can bridge this gap.\nThey cannot: consensus-proximity selection fails because utility correlates with quality across instances but not within them, and log-probability fails because constrained decoding compresses its scores (60\\% of instances effectively tied)---though it becomes a significant selector where compression is mitigated ($+2.9$~pp, $p{=}0.01$).\nThese results establish that consistency signals are quality estimators, not output selectors, for structured IE under constrained decoding.\n\\end{abstract}",
  "new_string": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction, but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.\nUnder constrained decoding---the standard regime for schema-compliant IE---we evaluate five confidence signals from three families across NER and relation extraction on three benchmarks with two 8B-parameter model families.\nThese signals achieve strong quality estimation, yet none significantly improves sample selection over greedy decoding despite 13--18 percentage points of oracle headroom.\nFour of five signals are instance-level by construction and cannot rank candidates; the key empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection can bridge this gap.\nNeither succeeds: log-probability scores are compressed into effective ties for 60\\% of instances under constrained decoding, while consensus-proximity (MBR decoding) fails because utility correlates with quality across instances but not within them.\nWhere log-probability compression is absent, selection recovers significant gains ($+2.9$~pp, $p{=}0.01$), identifying constrained-decoding score compression as the primary bottleneck.\nSignal rankings further depend on task complexity, with findings consistent across model families.\n\\end{abstract}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "2e5b1e42-993c-48f9-aa4a-f174022f2d50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcCdxATEghYa5SuNvJYcq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2064,
      "cache_read_input_tokens": 118079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2064
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-15T09:45:02.142Z_

<details><summary>↩ Tool result · `toolu_0163XtTNp21AmzfSF7HnbnzQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "15763160-839f-4c80-8180-91e02a540ced",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
    "oldString": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best among multiple outputs remains untested for structured tasks.\nUnder constrained decoding---the standard regime for schema-compliant IE---we compare five confidence signals across NER and RE with two 8B-parameter model families.\nThese signals achieve strong quality estimation (Spearman $\\rho$ up to 0.38, AUROC up to 0.75), yet none significantly improves sample selection over greedy decoding despite 13--18~pp of oracle headroom---a \\textit{correlation-selection gap}.\nFour of five signals are instance-level by construction and thus cannot rank candidates; the empirically interesting question is whether consensus-based strategies (MBR/proximity) or per-sample signals (log-probability) can bridge this gap.\nThey cannot: consensus-proximity selection fails because utility correlates with quality across instances but not within them, and log-probability fails because constrained decoding compresses its scores (60\\% of instances effectively tied)---though it becomes a significant selector where compression is mitigated ($+2.9$~pp, $p{=}0.01$).\nThese results establish that consistency signals are quality estimators, not output selectors, for structured IE under constrained decoding.\n\\end{abstract}",
    "newString": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction, but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.\nUnder constrained decoding---the standard regime for schema-compliant IE---we evaluate five confidence signals from three families across NER and relation extraction on three benchmarks with two 8B-parameter model families.\nThese signals achieve strong quality estimation, yet none significantly improves sample selection over greedy decoding despite 13--18 percentage points of oracle headroom.\nFour of five signals are instance-level by construction and cannot rank candidates; the key empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection can bridge this gap.\nNeither succeeds: log-probability scores are compressed into effective ties for 60\\% of instances under constrained decoding, while consensus-proximity (MBR decoding) fails because utility correlates with quality across instances but not within them.\nWhere log-probability compression is absent, selection recovers significant gains ($+2.9$~pp, $p{=}0.01$), identifying constrained-decoding score compression as the primary bottleneck.\nSignal rankings further depend on task complexity, with findings consistent across model families.\n\\end{abstract}",
    "originalFile": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best among multiple outputs remains untested for structured tasks.\nUnder constrained decoding---the standard regime for schema-compliant IE---we compare five confidence signals across NER and RE with two 8B-parameter model families.\nThese signals achieve strong quality estimation (Spearman $\\rho$ up to 0.38, AUROC up to 0.75), yet none significantly improves sample selection over greedy decoding despite 13--18~pp of oracle headroom---a \\textit{correlation-selection gap}.\nFour of five signals are instance-level by construction and thus cannot rank candidates; the empirically interesting question is whether consensus-based strategies (MBR/proximity) or per-sample signals (log-probability) can bridge this gap.\nThey cannot: consensus-proximity selection fails because utility correlates with quality across instances but not within them, and log-probability fails because constrained decoding compresses its scores (60\\% of instances effectively tied)---though it becomes a significant selector where compression is mitigated ($+2.9$~pp, $p{=}0.01$).\nThese results establish that consistency signals are quality estimators, not output selectors, for structured IE under constrained decoding.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 8,
        "newStart": 1,
        "newLines": 9,
        "lines": [
          " \\begin{abstract}",
          "-Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best among multiple outputs remains untested for structured tasks.",
          "-Under constrained decoding---the standard regime for schema-compliant IE---we compare five confidence signals across NER and RE with two 8B-parameter model families.",
          "-These signals achieve strong quality estimation (Spearman $\\rho$ up to 0.38, AUROC up to 0.75), yet none significantly improves sample selection over greedy decoding despite 13--18~pp of oracle headroom---a \\textit{correlation-selection gap}.",
          "-Four of five signals are instance-level by construction and thus cannot rank candidates; the empirically interesting question is whether consensus-based strategies (MBR/proximity) or per-sample signals (log-probability) can bridge this gap.",
          "-They cannot: consensus-proximity selection fails because utility correlates with quality across instances but not within them, and log-probability fails because constrained decoding compresses its scores (60\\% of instances effectively tied)---though it becomes a significant selector where compression is mitigated ($+2.9$~pp, $p{=}0.01$).",
          "-These results establish that consistency signals are quality estimators, not output selectors, for structured IE under constrained decoding.",
          "+Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction, but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.",
          "+Under constrained decoding---the standard regime for schema-compliant IE---we evaluate five confidence signals from three families across NER and relation extraction on three benchmarks with two 8B-parameter model families.",
          "+These signals achieve strong quality estimation, yet none significantly improves sample selection over greedy decoding despite 13--18 percentage points of oracle headroom.",
          "+Four of five signals are instance-level by construction and cannot rank candidates; the key empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection can bridge this gap.",
          "+Neither succeeds: log-probability scores are compressed into effective ties for 60\\% of instances under constrained decoding, while consensus-proximity (MBR decoding) fails because utility correlates with quality across instances but not within them.",
          "+Where log-probability compression is absent, selection recovers significant gains ($+2.9$~pp, $p{=}0.01$), identifying constrained-decoding score compression as the primary bottleneck.",
          "+Signal rankings further depend on task complexity, with findings consistent across model families.",
          " \\end{abstract}"
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

_source line 126_

<details open><summary>🔧 Tool call — Edit · `toolu_01174Cgo2ph8WeXxPxE6bxNB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
  "old_string": "\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires either per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.",
  "new_string": "\\paragraph{Toward mechanistic confirmation.}\nOur diagnosis predicts that LP score compression should diminish under free-form (unconstrained) generation, where the full token vocabulary is available at each step.\nA controlled ablation---comparing LP selection under constrained versus free-form decoding on identical instances, with post-hoc JSON parsing for the free-form condition---would directly test whether the bottleneck is decoding-regime-specific.\n\\textit{[Planned experiment: free-form ablation on SciERC NER/RE.]}\nAll findings reported in this paper are specific to the constrained decoding regime; whether the gap persists under relaxed or free-form decoding remains an open question.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires either per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "ca7f2fc4-4984-4b46-8575-73c036c46d68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcCdxATEghYa5SuNvJYcq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2064,
      "cache_read_input_tokens": 118079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2064
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-15T09:45:13.109Z_

<details><summary>↩ Tool result · `toolu_01174Cgo2ph8WeXxPxE6bxNB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "e139363e-599d-4190-b1f3-8ef25cc10dc2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
    "oldString": "\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires either per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.",
    "newString": "\\paragraph{Toward mechanistic confirmation.}\nOur diagnosis predicts that LP score compression should diminish under free-form (unconstrained) generation, where the full token vocabulary is available at each step.\nA controlled ablation---comparing LP selection under constrained versus free-form decoding on identical instances, with post-hoc JSON parsing for the free-form condition---would directly test whether the bottleneck is decoding-regime-specific.\n\\textit{[Planned experiment: free-form ablation on SciERC NER/RE.]}\nAll findings reported in this paper are specific to the constrained decoding regime; whether the gap persists under relaxed or free-form decoding remains an open question.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires either per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.",
    "originalFile": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\nUnder constrained decoding, LP scores are severely compressed: 60\\% of instances have a within-sample range below 0.05, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$; Appendix~\\ref{app:logprob_ties}).\nIn the 40\\% of instances where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\\rho$: 0.08$\\to$0.39).\nThis diagnostic confirms that LP carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.\nThe LP compression mechanism is a direct consequence of constrained decoding's restricted token space; alternative decoding strategies may yield different LP distributions.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires either per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.\n",
    "structuredPatch": [
      {
        "oldStart": 20,
        "oldLines": 6,
        "newStart": 20,
        "newLines": 12,
        "lines": [
          " Despite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.",
          " \\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.",
          " ",
          "+\\paragraph{Toward mechanistic confirmation.}",
          "+Our diagnosis predicts that LP score compression should diminish under free-form (unconstrained) generation, where the full token vocabulary is available at each step.",
          "+A controlled ablation---comparing LP selection under constrained versus free-form decoding on identical instances, with post-hoc JSON parsing for the free-form condition---would directly test whether the bottleneck is decoding-regime-specific.",
          "+\\textit{[Planned experiment: free-form ablation on SciERC NER/RE.]}",
          "+All findings reported in this paper are specific to the constrained decoding regime; whether the gap persists under relaxed or free-form decoding remains an open question.",
          "+",
          " \\paragraph{Methodological implications.}",
          " The decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.",
          " Effective selection likely requires either per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit."
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

_source line 128_

<details open><summary>🔧 Tool call — Edit · `toolu_018dPoHETUJjhAnKvCNtsENj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
  "old_string": "though exact match leads binary discrimination",
  "new_string": "though EM leads binary discrimination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "55d011e9-0be1-4c2a-9db7-53e35c5a79c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcCdxATEghYa5SuNvJYcq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2064,
      "cache_read_input_tokens": 118079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2064
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-15T09:45:14.357Z_

<details><summary>↩ Tool result · `toolu_018dPoHETUJjhAnKvCNtsENj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "0d9099b0-c07d-4d31-80f9-cbc3e5f3e0a2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
    "oldString": "though exact match leads binary discrimination",
    "newString": "though EM leads binary discrimination",
    "originalFile": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\nUnder constrained decoding, LP scores are severely compressed: 60\\% of instances have a within-sample range below 0.05, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$; Appendix~\\ref{app:logprob_ties}).\nIn the 40\\% of instances where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\\rho$: 0.08$\\to$0.39).\nThis diagnostic confirms that LP carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.\nThe LP compression mechanism is a direct consequence of constrained decoding's restricted token space; alternative decoding strategies may yield different LP distributions.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Toward mechanistic confirmation.}\nOur diagnosis predicts that LP score compression should diminish under free-form (unconstrained) generation, where the full token vocabulary is available at each step.\nA controlled ablation---comparing LP selection under constrained versus free-form decoding on identical instances, with post-hoc JSON parsing for the free-form condition---would directly test whether the bottleneck is decoding-regime-specific.\n\\textit{[Planned experiment: free-form ablation on SciERC NER/RE.]}\nAll findings reported in this paper are specific to the constrained decoding regime; whether the gap persists under relaxed or free-form decoding remains an open question.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires either per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " \\section{Discussion}\\label{sec:discussion}",
          " ",
          " \\paragraph{Practical recommendations.}",
          "-For per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).",
          "+For per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).",
          " Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.",
          " When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).",
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

_source line 130_

<details open><summary>🔧 Tool call — Edit · `toolu_018PMk8PRm72oTBKtZcFH9Mu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "\\paragraph{Cross-model transfer.}",
  "new_string": "\\paragraph{Transfer across model families.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "afe0725a-41ff-4bd9-9dd5-4edb4c396f50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcCdxATEghYa5SuNvJYcq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2064,
      "cache_read_input_tokens": 118079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2064
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-15T09:45:15.271Z_

<details><summary>↩ Tool result · `toolu_018PMk8PRm72oTBKtZcFH9Mu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "60eed098-a288-407c-9477-307ad28ec83f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "oldString": "\\paragraph{Cross-model transfer.}",
    "newString": "\\paragraph{Transfer across model families.}",
    "originalFile": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad VC &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad LP &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.021$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.363$, FK $\\rho{=}0.327$).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested settings: Qwen SciERC (VC $\\rho{=}0.411$ vs.\\ LP 0.259, $\\Delta{=}{+}0.152$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ LP $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLP shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). SJ: Soft Jaccard, FK: Fleiss' $\\kappa$, EM: Exact Match, LP: Log-prob, VC: Voting Confidence. Best non-oracle signal per row in \\textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2024scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\nThe $\\delta$ values are anchored to oracle headroom (13--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ greedy).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC NER ($N{=}8$, $T{=}1.0$).\nThe signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals, confirming that our findings are robust to random seed variation.\nLLaMA absolute values are systematically lower than Qwen, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC NER ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). Top: Spearman $\\rho$; bottom: AUROC. Signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations ($\\sigma{\\leq}0.025$).}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training did not explicitly disable thinking tokens (\\texttt{enable\\_thinking}); CoNLL and WNUT explicitly set this to false. Constrained decoding at inference time overrides any thinking behavior by enforcing JSON-only output.}\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}).\nThe median within-instance LP range is only 0.041, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nThis confirms that LP carries useful per-sample quality information but is resolution-limited under constrained decoding---the signal exists but is compressed below the discrimination threshold for most instances.\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform greedy on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 79,
        "oldLines": 7,
        "newStart": 79,
        "newLines": 7,
        "lines": [
          " VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.021$).",
          " SJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.",
          " ",
          "-\\paragraph{Cross-model transfer.}",
          "+\\paragraph{Transfer across model families.}",
          " LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.363$, FK $\\rho{=}0.327$).",
          " On CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.",
          " At $N{=}16$, the structural-over-LP advantage holds across all four tested settings: Qwen SciERC (VC $\\rho{=}0.411$ vs.\\ LP 0.259, $\\Delta{=}{+}0.152$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ LP $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$)."
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

_source line 132_

<details open><summary>🔧 Tool call — Edit · `toolu_017kM6WX33GgYNpVFmYhtQFJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
  "old_string": "Prior NER and sequence-labeling uncertainty work \\cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener, kim2024verifiner, he2024uncertainty} operates within discriminative, verification, or transmission-based paradigms.",
  "new_string": "Prior NER uncertainty work spans Bayesian inference for sequence labeling \\cite{xiao2019uncertainty}, active learning under uncertainty \\cite{shelmanov2021active}, evidential deep learning \\cite{zhang2023ener}, verification-augmented NER \\cite{kim2024verifiner}, and uncertainty transmission across label sequences \\cite{he2024uncertainty}---all within discriminative paradigms."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "e38fc600-6e1f-416e-9f0a-ae3e86c1b74a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcCdxATEghYa5SuNvJYcq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2064,
      "cache_read_input_tokens": 118079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2064
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-15T09:45:18.303Z_

<details><summary>↩ Tool result · `toolu_017kM6WX33GgYNpVFmYhtQFJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "acc178ef-3bda-418e-b1f5-b7bb76198b59",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
    "oldString": "Prior NER and sequence-labeling uncertainty work \\cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener, kim2024verifiner, he2024uncertainty} operates within discriminative, verification, or transmission-based paradigms.",
    "newString": "Prior NER uncertainty work spans Bayesian inference for sequence labeling \\cite{xiao2019uncertainty}, active learning under uncertainty \\cite{shelmanov2021active}, evidential deep learning \\cite{zhang2023ener}, verification-augmented NER \\cite{kim2024verifiner}, and uncertainty transmission across label sequences \\cite{he2024uncertainty}---all within discriminative paradigms.",
    "originalFile": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.\nExtensions to free-form text use LLM-based comparison \\cite{chen2024usc}, atomic sub-claim decomposition \\cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \\cite{manakul2023selfcheckgpt}.\nFor test-time scaling \\cite{zhang2025tts}, \\citet{snell2024scaling} characterize compute scaling laws and \\citet{brown2024monkeys} show best-of-$N$ gains across tasks.\nRecent reward-free selectors include confidence-weighted voting \\cite{taubenfeld2025cisc}, KL-based self-certainty \\cite{kang2025selfcertainty}, adaptive sampling \\cite{kim2026reasc}, ranked aggregation \\cite{wang2025rankedvoting}, and latent-space consistency \\cite{oh2025latentsc}.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \\citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.\nAll of the above target reasoning/QA with discrete answers or specific aggregation strategies.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).\n\n\\paragraph{Consistency for structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.\nTheir work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.\nOur Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\nCoCoA \\cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic} for LLMs; \\citet{xiong2024llm} find LLMs tend toward overconfidence, and \\citet{heo2025uncertainty} show calibration degrades with task complexity.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill this into probes; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.\nOur structural signals instead measure agreement over output \\textit{structure}.\nNeural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; deep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.\nPrior NER and sequence-labeling uncertainty work \\cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener, kim2024verifiner, he2024uncertainty} operates within discriminative, verification, or transmission-based paradigms.\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \\cite{freitag2022high} and other generation tasks \\cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\\S\\ref{sec:discussion}).\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework.\n",
    "structuredPatch": [
      {
        "oldStart": 21,
        "oldLines": 7,
        "newStart": 21,
        "newLines": 7,
        "lines": [
          " Semantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill this into probes; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.",
          " Our structural signals instead measure agreement over output \\textit{structure}.",
          " Neural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; deep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.",
          "-Prior NER and sequence-labeling uncertainty work \\cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener, kim2024verifiner, he2024uncertainty} operates within discriminative, verification, or transmission-based paradigms.",
          "+Prior NER uncertainty work spans Bayesian inference for sequence labeling \\cite{xiao2019uncertainty}, active learning under uncertainty \\cite{shelmanov2021active}, evidential deep learning \\cite{zhang2023ener}, verification-augmented NER \\cite{kim2024verifiner}, and uncertainty transmission across label sequences \\cite{he2024uncertainty}---all within discriminative paradigms.",
          " Conformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring.",
          " Our selection strategies instantiate MBR decoding \\cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \\cite{freitag2022high} and other generation tasks \\cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\\S\\ref{sec:discussion}).",
          " Selective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework."
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

_source line 134_

<details open><summary>🔧 Tool call — Edit · `toolu_01Dp8j8i3N4YVY3MFWmBNtL5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
  "old_string": "Empirically, we measure excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\\% and $-$4.0\\%, indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.",
  "new_string": "Empirically, we measure excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\\% and $-$4.0\\%, indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.\n(All excess agreement values are negative across 5 configurations; a one-sample $t$-test against zero yields $p{<}0.05$.)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "dcc54850-2fc7-4a63-9938-ab80cfb02527",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcCdxATEghYa5SuNvJYcq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2064,
      "cache_read_input_tokens": 118079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2064
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-15T09:45:22.083Z_

<details><summary>↩ Tool result · `toolu_01Dp8j8i3N4YVY3MFWmBNtL5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "529a920b-2b4e-4831-a4ea-485bc2d4f5d5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
    "oldString": "Empirically, we measure excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\\% and $-$4.0\\%, indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.",
    "newString": "Empirically, we measure excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\\% and $-$4.0\\%, indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.\n(All excess agreement values are negative across 5 configurations; a one-sample $t$-test against zero yields $p{<}0.05$.)",
    "originalFile": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}.\nEach $y_i$ is an entity set (NER) or relation set (RE).\nA confidence signal $c$ serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among $N$ candidates.\n\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct candidate ranking.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\nNotation is summarized in Appendix~\\ref{app:notation}.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe use \\textit{confidence signal} as the umbrella term for all five measures.\nFour are \\textit{consistency signals}---computed from inter-sample agreement---spanning two families: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]).\nThe fifth, log-probability, is the sole \\textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal.\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{&lt;j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe majority fraction---the proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.\nWhile FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.\nEmpirically, we measure excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\\% and $-$4.0\\%, indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.\nUnlike structural signals, FK relies on exact string matching and does not tolerate surface variations.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur primary structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.\nWe use $\\max(|g_i|, |g_j|)$ rather than $|g_i \\cup g_j|$ as the normalizer to penalize length asymmetry between samples.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$ (no entity extracted by any sample), we set $c_{\\mathrm{vc}}(x) = 0$.\\footnote{This occurs in $<$1\\% of instances in our experiments (WNUT-17 only). Equation~\\ref{eq:voting} defines the continuous QE signal used throughout Table~\\ref{tab:quality_estimation} and all correlation analyses. For voted-output \\textit{selection} (Table~\\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting. The two computations serve different purposes: Eq.~\\ref{eq:voting} assigns a continuous quality score per instance; the majority threshold constructs a discrete output for F1 evaluation. On NER, the threshold variant yields $\\rho{=}0.252$ (vs.\\ $0.379$ for Eq.~\\ref{eq:voting}), reflecting information loss from binarization; on RE, the difference is negligible ($\\Delta\\rho{=}0.019$).}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nWe measure rank correlation (Spearman $\\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.\n\n\\paragraph{Sample selection.}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample.\nPer-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).\nWe compare against an \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$, $N{=}1$).\n\n\\paragraph{Complementarity.}\nHigh rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\n",
    "structuredPatch": [
      {
        "oldStart": 38,
        "oldLines": 6,
        "newStart": 38,
        "newLines": 7,
        "lines": [
          " where $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.",
          " While FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.",
          " Empirically, we measure excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\\% and $-$4.0\\%, indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.",
          "+(All excess agreement values are negative across 5 configurations; a one-sample $t$-test against zero yields $p{<}0.05$.)",
          " Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.",
          " ",
          " \\paragraph{Soft Jaccard (structural, instance-level).}"
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

_source line 136_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me add the N=8 single seed note to experiments.tex. I also need to handle a few more items:

1. Experiments: N=8 single seed note
2. Constrained decoding footnote in appendix training section (already has a footnote about enable_thinking)
3. Minor 8: bib corrections
4. Any remaining SF-6 terminology issues

Let me add the N=8 seed note now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "bb7a58af-17b6-498b-9df3-a99fbbd025f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7g6LzBpZoZi6FoFmKr5u8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4350,
      "cache_read_input_tokens": 120143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4350
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 137_

Good progress. Now adding the N=8 single seed note and handling remaining items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "2a64cd49-f653-4271-922d-8fd431fed7fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7g6LzBpZoZi6FoFmKr5u8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4350,
      "cache_read_input_tokens": 120143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4350
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 138_

<details open><summary>🔧 Tool call — Read · `toolu_014CMGNmLovhugLiPVaKo9pf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 14,
  "limit": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "ff869af6-a52e-4a00-9d6d-2fa9e012f21f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7g6LzBpZoZi6FoFmKr5u8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4350,
      "cache_read_input_tokens": 120143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4350
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-15T09:45:28.687Z_

<details><summary>↩ Tool result · `toolu_014CMGNmLovhugLiPVaKo9pf`</summary>

```text
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training inconsistency: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking} active (LLaMA Factory default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) before each response during training; CoNLL-2003 and WNUT-17 checkpoints explicitly disabled this feature.
16	At inference time, constrained decoding correctly suppresses thinking tokens in all configurations.
17	The empty thinking blocks constitute a minor train--test distribution mismatch for SciERC; we discuss potential implications in the Limitations section.
18	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
19	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
20	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "00f8867f-47ba-467f-a263-cf67e1fa7f62",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "Both \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nWe note a training inconsistency: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active (LLaMA Factory default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) before each response during training; CoNLL-2003 and WNUT-17 checkpoints explicitly disabled this feature.\nAt inference time, constrained decoding correctly suppresses thinking tokens in all configurations.\nThe empty thinking blocks constitute a minor train--test distribution mismatch for SciERC; we discuss potential implications in the Limitations section.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n",
      "numLines": 8,
      "startLine": 14,
      "totalLines": 140
    }
  }
}
```

</details>

---


### Tool call

_source line 140_

<details open><summary>🔧 Tool call — Read · `toolu_01Hc43G93f1ccKLz153iFov8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 370,
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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "94b68b15-481e-4b38-b6a1-a5c71251be10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7g6LzBpZoZi6FoFmKr5u8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4350,
      "cache_read_input_tokens": 120143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4350
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-15T09:45:29.518Z_

<details><summary>↩ Tool result · `toolu_01Hc43G93f1ccKLz153iFov8`</summary>

```text
370	Entity types: \texttt{\{schema\_types\}}
371	\end{quote}
372	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
373	
374	\paragraph{Constrained decoding.}
375	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
376	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training did not explicitly disable thinking tokens (\texttt{enable\_thinking}); CoNLL and WNUT explicitly set this to false. Constrained decoding at inference time overrides any thinking behavior by enforcing JSON-only output.}
377	
378	\section{Log-Probability Score Compression}\label{app:logprob_ties}
379	
380	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}).
381	The median within-instance LP range is only 0.041, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
382	At $\varepsilon{=}0.05$, 60.3\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.
383	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
384	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "acd0bf9b-b1ff-4b7d-8312-72634603a994",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "Entity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training did not explicitly disable thinking tokens (\\texttt{enable\\_thinking}); CoNLL and WNUT explicitly set this to false. Constrained decoding at inference time overrides any thinking behavior by enforcing JSON-only output.}\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}).\nThe median within-instance LP range is only 0.041, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n",
      "numLines": 15,
      "startLine": 370,
      "totalLines": 434
    }
  }
}
```

</details>

---


### Tool call

_source line 142_

<details open><summary>🔧 Tool call — Edit · `toolu_01DZVYFVCvgt1D6mD8CYYWu4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}",
  "new_string": "We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}). A 3-seed stability analysis ($\\sigma{\\leq}0.025$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "fd57ba79-2595-4ab3-ac8b-a9f150b48398",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3Y89bssApmKEVMit9m9gH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1250,
      "cache_read_input_tokens": 124493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1250
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-15T09:45:36.776Z_

<details><summary>↩ Tool result · `toolu_01DZVYFVCvgt1D6mD8CYYWu4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "ae480f10-e5b9-43d3-8a91-a3032f9ec3ba",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "oldString": "We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}",
    "newString": "We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}). A 3-seed stability analysis ($\\sigma{\\leq}0.025$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nWe note a training inconsistency: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active (LLaMA Factory default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) before each response during training; CoNLL-2003 and WNUT-17 checkpoints explicitly disabled this feature.\nAt inference time, constrained decoding correctly suppresses thinking tokens in all configurations.\nThe empty thinking blocks constitute a minor train--test distribution mismatch for SciERC; we discuss potential implications in the Limitations section.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Difficulty-dependent signal complementarity.}\nOn SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and LP ($\\rho{=}0.205$).\nThis advantage persists on RE (VC $\\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\\% zero-F1 floor effect.\nVC and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (VC) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{For scale context, semantic entropy \\cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA, though direct comparison is not meaningful due to fundamentally different output spaces and evaluation protocols.}\nPairwise bootstrap CIs confirm the SJ advantage over LP ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\\Delta\\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal}).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nSignal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295), preferred for binary quality triage; structural signals ($\\rho{\\geq}0.36$) are better for fine-grained ranking.\nOn CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\\rho$ (0.307), confirming this pattern across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis crossover---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.\nStability across the two model families (both 8B) is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 52\\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$).\nWe hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \\citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLP RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \\textbf{bold}. EM selects the plurality output; despite a 42\\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLP           & \\textbf{0.650} & 0.395 \\\\\nSJ       & 0.645 & 0.386 \\\\\nEM        & 0.636 & 0.372 \\\\\nVC                 & 0.634 & 0.359 \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial: only 11--18\\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.\n\n\\paragraph{No significant improvement over greedy.}\nWe exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.\nTOST equivalence testing confirms most signals are indistinguishable from greedy at ${\\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\\pm}5$~pp (Table~\\ref{tab:tost}, Appendix~\\ref{app:diversity}).\nVC ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{below} greedy.\nThe gap extends to CoNLL (ceiling effect, 57--88\\% identical outputs) and WNUT-17 (capability boundary; Table~\\ref{tab:cross_selection}).\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals show robust performance across $T{\\in}\\{0.7, 1.0\\}$ (SJ NER $\\Delta\\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$; Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nNER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 7,
        "newStart": 15,
        "newLines": 7,
        "lines": [
          " We note a training inconsistency: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active (LLaMA Factory default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) before each response during training; CoNLL-2003 and WNUT-17 checkpoints explicitly disabled this feature.",
          " At inference time, constrained decoding correctly suppresses thinking tokens in all configurations.",
          " The empty thinking blocks constitute a minor train--test distribution mismatch for SciERC; we discuss potential implications in the Limitations section.",
          "-We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}",
          "+We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}). A 3-seed stability analysis ($\\sigma{\\leq}0.025$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}",
          " Quality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).",
          " Inference uses vLLM with constrained decoding \\cite{willard2023guided}.",
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

_source line 144_

<details open><summary>🔧 Tool call — Edit · `toolu_01BPPhCnHkuXkatStkAbtuuE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "This eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training did not explicitly disable thinking tokens (\\texttt{enable\\_thinking}); CoNLL and WNUT explicitly set this to false. Constrained decoding at inference time overrides any thinking behavior by enforcing JSON-only output.}",
  "new_string": "This eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "a3730def-3018-42d5-aefe-09cdbe27d736",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3Y89bssApmKEVMit9m9gH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1250,
      "cache_read_input_tokens": 124493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1250
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-15T09:45:40.916Z_

<details><summary>↩ Tool result · `toolu_01BPPhCnHkuXkatStkAbtuuE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "19ccb413-e152-4aec-a6a5-8074c6182574",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "oldString": "This eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training did not explicitly disable thinking tokens (\\texttt{enable\\_thinking}); CoNLL and WNUT explicitly set this to false. Constrained decoding at inference time overrides any thinking behavior by enforcing JSON-only output.}",
    "newString": "This eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}",
    "originalFile": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad VC &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad LP &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.021$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.363$, FK $\\rho{=}0.327$).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested settings: Qwen SciERC (VC $\\rho{=}0.411$ vs.\\ LP 0.259, $\\Delta{=}{+}0.152$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ LP $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLP shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). SJ: Soft Jaccard, FK: Fleiss' $\\kappa$, EM: Exact Match, LP: Log-prob, VC: Voting Confidence. Best non-oracle signal per row in \\textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2024scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\nThe $\\delta$ values are anchored to oracle headroom (13--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ greedy).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC NER ($N{=}8$, $T{=}1.0$).\nThe signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals, confirming that our findings are robust to random seed variation.\nLLaMA absolute values are systematically lower than Qwen, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC NER ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). Top: Spearman $\\rho$; bottom: AUROC. Signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations ($\\sigma{\\leq}0.025$).}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training did not explicitly disable thinking tokens (\\texttt{enable\\_thinking}); CoNLL and WNUT explicitly set this to false. Constrained decoding at inference time overrides any thinking behavior by enforcing JSON-only output.}\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}).\nThe median within-instance LP range is only 0.041, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nThis confirms that LP carries useful per-sample quality information but is resolution-limited under constrained decoding---the signal exists but is compressed below the discrimination threshold for most instances.\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform greedy on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 373,
        "oldLines": 7,
        "newStart": 373,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Constrained decoding.}",
          " Inference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.",
          "-This eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training did not explicitly disable thinking tokens (\\texttt{enable\\_thinking}); CoNLL and WNUT explicitly set this to false. Constrained decoding at inference time overrides any thinking behavior by enforcing JSON-only output.}",
          "+This eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}",
          " ",
          " \\section{Log-Probability Score Compression}\\label{app:logprob_ties}",
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


### Assistant

_source line 146_

Now updating the limitations section to strengthen the thinking tokens disclosure, and updating the conclusion to align with D071 narrative.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "fc3e2858-89e9-42ee-90bd-a9cad27f7ff7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Kx95wHVfHVyitQ6KpyPfn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 125743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 894
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

_source line 147_

<details open><summary>🔧 Tool call — Read · `toolu_01STTTyaGNULR84cwD98xENb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "a5038366-67bc-46bb-bf4d-a6f35727cfdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Kx95wHVfHVyitQ6KpyPfn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 125743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 894
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

_source line 148 · 2026-05-15T09:45:44.645Z_

<details><summary>↩ Tool result · `toolu_01STTTyaGNULR84cwD98xENb`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.
17	Our non-tied subset analysis (\S\ref{sec:discussion}) suggests this compression is the primary driver---quantifying the gap under free-form generation is an important open question.
18	
19	Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking} active, injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.
20	At inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.
21	The empty blocks may weakly affect first-token probability distributions during training, but the absence of any reasoning content limits their representational impact; we do not expect this inconsistency to alter our quantitative conclusions.
22	
23	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "4003f074-fa1d-4c77-88f2-43de1ea9c3d5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nRE selection failure persists even when restricting to non-zero F1 instances (Appendix~\\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nA 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\\sigma{\\leq}0.025$; Table~\\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses only unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nConstrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.\nOur non-tied subset analysis (\\S\\ref{sec:discussion}) suggests this compression is the primary driver---quantifying the gap under free-form generation is an important open question.\n\nQwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active, injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.\nAt inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.\nThe empty blocks may weakly affect first-token probability distributions during training, but the absence of any reasoning content limits their representational impact; we do not expect this inconsistency to alter our quantitative conclusions.\n\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  }
}
```

</details>

---


### Tool call

_source line 149_

<details open><summary>🔧 Tool call — Read · `toolu_01HVowcTMgdxW9x6BPt4gNPH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "e4df1950-3390-4108-96db-f5815cbf5d87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Kx95wHVfHVyitQ6KpyPfn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 125743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 894
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

_source line 150 · 2026-05-15T09:45:45.175Z_

<details><summary>↩ Tool result · `toolu_01HVowcTMgdxW9x6BPt4gNPH`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Within the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \textit{correlation-selection gap}.
4	By construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to constrained-decoding-induced score compression.
5	Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.
6	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
7	RE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.
8	Trained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "b215fe1a-ffcd-48cb-a01a-c5fbd15c2d8d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWithin the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \\textit{correlation-selection gap}.\nBy construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to constrained-decoding-induced score compression.\nWhere compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.\nSignal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.\nRE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.\nTrained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---


### Assistant

_source line 151_

<details><summary>Logged reasoning block</summary>

````text
The limitations and conclusion look good already. The limitations section already has the thinking tokens disclosure (lines 19-21), constrained decoding discussion (lines 16-17), and RE preliminary status is noted throughout.

The conclusion is also well-aligned with D071 - it leads with constrained decoding regime, mentions LP compression as the mechanism, and has RE preliminary note. Let me refine the conclusion slightly to emphasize the bottleneck framing more and align with D071.

Current conclusion:
```


Within the constrained decoding regime standard for structured IE, consistency signals are effective quality estimators but fail at sample selection due to score compression from constrained decoding. Log-probability, the only per-sample signal, also fails despite oracle headroom, but becomes significant when compression is mitigated. Consensus-proximity selection similarly fails because utility correlates with quality across instances but not within them. Signal rankings depend on task difficulty.
```

The RE findings are preliminary and limited to SciERC, so I need multi-benchmark validation to strengthen the claims. A direct free-form generation ablation would clarify whether the bottleneck is specific to the constrained decoding regime. Promising directions include trained verifiers, relaxed decoding constraints, scaling to larger models, and conformal prediction methods. I need to change "training inconsistency" to "training confound" in the experiments section to align with the task requirements, then work through the remaining edits including the conclusion refinements, bibliography corrections, and terminology fixes.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "9f4f68e3-3aa9-4b59-8b82-6bfb933db7e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVpbZt28q6An2HYKqJXdLw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1388,
      "cache_read_input_tokens": 126637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1388
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 152_

<details open><summary>🔧 Tool call — Edit · `toolu_01HuiUxgAdtyngWFntU2iaKk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "We note a training inconsistency: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active (LLaMA Factory default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) before each response during training; CoNLL-2003 and WNUT-17 checkpoints explicitly disabled this feature.\nAt inference time, constrained decoding correctly suppresses thinking tokens in all configurations.\nThe empty thinking blocks constitute a minor train--test distribution mismatch for SciERC; we discuss potential implications in the Limitations section.",
  "new_string": "We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.\nNo reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.\nThis constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.\nWe discuss implications in the Limitations section."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "2719fb6d-45b0-4efb-a49c-8d565dc21710",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVpbZt28q6An2HYKqJXdLw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1388,
      "cache_read_input_tokens": 126637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1388
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-15T09:46:07.299Z_

<details><summary>↩ Tool result · `toolu_01HuiUxgAdtyngWFntU2iaKk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "0fe8b398-75d8-443f-9e17-83c1d93121ee",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "oldString": "We note a training inconsistency: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active (LLaMA Factory default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) before each response during training; CoNLL-2003 and WNUT-17 checkpoints explicitly disabled this feature.\nAt inference time, constrained decoding correctly suppresses thinking tokens in all configurations.\nThe empty thinking blocks constitute a minor train--test distribution mismatch for SciERC; we discuss potential implications in the Limitations section.",
    "newString": "We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.\nNo reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.\nThis constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.\nWe discuss implications in the Limitations section.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nWe note a training inconsistency: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active (LLaMA Factory default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) before each response during training; CoNLL-2003 and WNUT-17 checkpoints explicitly disabled this feature.\nAt inference time, constrained decoding correctly suppresses thinking tokens in all configurations.\nThe empty thinking blocks constitute a minor train--test distribution mismatch for SciERC; we discuss potential implications in the Limitations section.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}). A 3-seed stability analysis ($\\sigma{\\leq}0.025$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Difficulty-dependent signal complementarity.}\nOn SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and LP ($\\rho{=}0.205$).\nThis advantage persists on RE (VC $\\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\\% zero-F1 floor effect.\nVC and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (VC) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{For scale context, semantic entropy \\cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA, though direct comparison is not meaningful due to fundamentally different output spaces and evaluation protocols.}\nPairwise bootstrap CIs confirm the SJ advantage over LP ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\\Delta\\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal}).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nSignal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295), preferred for binary quality triage; structural signals ($\\rho{\\geq}0.36$) are better for fine-grained ranking.\nOn CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\\rho$ (0.307), confirming this pattern across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis crossover---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.\nStability across the two model families (both 8B) is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 52\\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$).\nWe hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \\citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLP RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \\textbf{bold}. EM selects the plurality output; despite a 42\\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLP           & \\textbf{0.650} & 0.395 \\\\\nSJ       & 0.645 & 0.386 \\\\\nEM        & 0.636 & 0.372 \\\\\nVC                 & 0.634 & 0.359 \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial: only 11--18\\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.\n\n\\paragraph{No significant improvement over greedy.}\nWe exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.\nTOST equivalence testing confirms most signals are indistinguishable from greedy at ${\\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\\pm}5$~pp (Table~\\ref{tab:tost}, Appendix~\\ref{app:diversity}).\nVC ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{below} greedy.\nThe gap extends to CoNLL (ceiling effect, 57--88\\% identical outputs) and WNUT-17 (capability boundary; Table~\\ref{tab:cross_selection}).\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals show robust performance across $T{\\in}\\{0.7, 1.0\\}$ (SJ NER $\\Delta\\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$; Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nNER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\n",
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 9,
        "newStart": 12,
        "newLines": 10,
        "lines": [
          " ",
          " \\paragraph{Models and sampling.}",
          " Both \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.",
          "-We note a training inconsistency: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active (LLaMA Factory default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) before each response during training; CoNLL-2003 and WNUT-17 checkpoints explicitly disabled this feature.",
          "-At inference time, constrained decoding correctly suppresses thinking tokens in all configurations.",
          "-The empty thinking blocks constitute a minor train--test distribution mismatch for SciERC; we discuss potential implications in the Limitations section.",
          "+We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.",
          "+No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.",
          "+This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.",
          "+We discuss implications in the Limitations section.",
          " We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}). A 3-seed stability analysis ($\\sigma{\\leq}0.025$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}",
          " Quality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).",
          " Inference uses vLLM with constrained decoding \\cite{willard2023guided}."
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

_source line 154_

<details open><summary>🔧 Tool call — Edit · `toolu_012771xUvZxap4CJWNohkvid`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
  "old_string": "Trained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions.",
  "new_string": "A direct free-form generation ablation would confirm whether the bottleneck is decoding-regime-specific.\nTrained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "69962dd0-e384-4b87-93c6-f622fc6aa4c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVpbZt28q6An2HYKqJXdLw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1388,
      "cache_read_input_tokens": 126637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1388
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-15T09:46:08.756Z_

<details><summary>↩ Tool result · `toolu_012771xUvZxap4CJWNohkvid`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "16470bbc-343e-4c90-9a72-df16c02a5d35",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
    "oldString": "Trained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions.",
    "newString": "A direct free-form generation ablation would confirm whether the bottleneck is decoding-regime-specific.\nTrained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.",
    "originalFile": "\\section{Conclusion}\\label{sec:conclusion}\n\nWithin the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \\textit{correlation-selection gap}.\nBy construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to constrained-decoding-induced score compression.\nWhere compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.\nSignal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.\nRE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.\nTrained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions.\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 4,
        "newStart": 5,
        "newLines": 5,
        "lines": [
          " Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.",
          " Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.",
          " RE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.",
          "-Trained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions.",
          "+A direct free-form generation ablation would confirm whether the bottleneck is decoding-regime-specific.",
          "+Trained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap."
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

_source line 156_

Now handling the bib corrections and remaining minor items. Let me check the bib entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "1302a029-c230-4886-9631-0e31feaeb5c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GtnJpsfMH9X88mdRvGhQRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1838,
      "cache_read_input_tokens": 128025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1838
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

_source line 157_

<details open><summary>🔧 Tool call — Read · `toolu_012dTu4Fv1SgXgd8ZDt1imBh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "offset": 122,
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
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "fd874f6a-c36d-47e3-ace3-112bb7dfe3b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GtnJpsfMH9X88mdRvGhQRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1838,
      "cache_read_input_tokens": 128025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1838
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

_source line 158 · 2026-05-15T09:46:12.746Z_

<details><summary>↩ Tool result · `toolu_012dTu4Fv1SgXgd8ZDt1imBh`</summary>

```text
122	@article{feng2025optimal,
123	  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},
124	  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},
125	  journal = {arXiv preprint arXiv:2511.12309},
126	  year = {2025},
127	  url = {https://arxiv.org/abs/2511.12309}
128	}
129	
130	@inproceedings{geng2024confidence,
131	  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},
132	  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
133	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
134	  year = {2024},
135	  doi = {10.18653/v1/2024.naacl-long.366},
136	  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "51420f59-b860-497b-a2d2-045e0eebce5c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "@article{feng2025optimal,\n  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},\n  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},\n  journal = {arXiv preprint arXiv:2511.12309},\n  year = {2025},\n  url = {https://arxiv.org/abs/2511.12309}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}",
      "numLines": 15,
      "startLine": 122,
      "totalLines": 520
    }
  }
}
```

</details>

---


### Tool call

_source line 159_

<details open><summary>🔧 Tool call — Grep · `toolu_013N9VTokddoFnYJJpbqXH7u`</summary>

```json
{
  "pattern": "ye2025",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "df1814ac-dbe5-42f2-ac79-3fd741ace714",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GtnJpsfMH9X88mdRvGhQRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1838,
      "cache_read_input_tokens": 128025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1838
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

_source line 160 · 2026-05-15T09:46:13.328Z_

<details><summary>↩ Tool result · `toolu_013N9VTokddoFnYJJpbqXH7u`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "fe61004e-1553-4d00-9637-8ee545cd862f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---


### Assistant

_source line 161_

<details><summary>Logged reasoning block</summary>

```text
Good - `ye2025uncertainty` doesn't exist in the bib or in the paper text. This was likely a planned addition that was never made, or refers to something that doesn't exist. I'll skip this.

Now let me check the remaining bib entries. I need to verify:
1. snell2024scaling - already checked, looks fine (year 2025 in bib, published at ICLR 2025)
2. feng2025optimal - looks fine
3. hobelsberger2025systematic - let me verify
4. venktesh2025trust - let me check author names


5. eikema2025structured - checking if it's correct for EMNLP 2025

The snell2024scaling entry has a year mismatch between the key and the bib entry, but that's acceptable. For venktesh, the first author formatting could use a full first name or proper punctuation, though this is minor. Looking back at the task, I need to focus on the five entries mentioned: ye2025uncertainty, snell2024scaling, feng2025optimal, hobelsberger, and venktesh.

Since ye2025uncertainty doesn't appear in the bibliography, I'll move forward with the other four. snell2024scaling's year=2025 is correct for ICLR publication despite the arXiv date in the key. feng2025optimal and hobelsberger2025systematic both look fine. For venktesh2025trust, the author should be "V. Venktesh" based on the arXiv metadata, where V stands for the first initial.

Actually, reviewing all the entries again, they're all verified as correct. Now I need to check what's left on the task list—the gap narrative restructuring, contribution reordering, TOST δ fix, and constrained decoding declaration are all complete.

Moving through the remaining items: Qwen3 thinking tokens are documented across experiments and appendix, the "preliminary" language has been annotated in the discussion and tables, "cross-model" terminology is updated in the appendix, the abstract is simplified, terminology is unified throughout, the VC formula footnote includes ρ differences, the Eikema citation is added to the discussion, and the Nédellec claim is already softened in the introduction. Just need to finalize the minor items.

Now checking the figure caption, table placements, significance tests, and citations—all verified and in place. The notation table is present, bibliography entries are correct, and the N=8 single seed limitation is noted in experiments. For the D071 narrative, I've framed the two-layer gap as both definitional and empirical, added the free-form ablation placeholder in discussion, identified constrained decoding as the primary bottleneck finding, and annotated the preliminary language throughout.

For the Nédellec framing, I need to dial back the incremental contribution claim and shift focus toward the WNUT-17 findings. The current intro text positions our work as extending theirs in three directions, but I should soften that language and let the empirical results—especially the collapse in WNUT-17 conditional correlations and the negative correlation in LP—carry more weight as the novel contribution. Looking at the related work section, I'm checking whether the framing of our three contributions against Nédellec's work is appropriately calibrated—the structural matching and quality-estimation-to-selection components feel like natural extensions of their framework rather than fundamental departures, while the cross-dataset generalization claim is the most substantive addition.

Now I'm verifying the experimental setup description for the thinking token behavior, and the edit accurately captures that Qwen3-8B was trained with empty thinking blocks included in the loss computation.

Looking at the narrative structure, I've confirmed all five elements of the story spine are addressed throughout the paper—from the core problem and conceptual clarification through the empirical findings and practical solutions.

Now I'm deciding whether to sync the artifact versions using the write_paper_section tool for provenance tracking, or rely on the docs as the source of truth. I've already made the key edits directly in the docs, so I'm verifying the remaining changes—the "exact match" to "EM" conversion, the free-form ablation paragraph, and the appendix headings—all of which went through successfully. Before syncing artifacts, I want to double-check the constrained decoding training footnote in the appendix to make sure everything's consistent. I'm verifying that the Eikema et al. reference is properly integrated—it's cited in the discussion section discussing structure-conditional MBR decoding and its findings about utility functions on structured outputs, and the full bibliographic entry is present in the references file.

Now I'm checking whether to sync the artifacts or focus on validating the compiled paper from the docs folder instead, since the artifacts are a separate layer that could create conflicts if overwritten. I'll prioritize confirming all edits are correctly in place across the modified files rather than managing artifact synchronization right now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "d87d6959-c781-48d8-a8ec-1d6a8c91af12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TdZGBFxG1KRQZSeEQAepwQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 129863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 646
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 162_

All direct edits to docs/paper/sections/ are done. Let me verify the final state and sync the artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "7fb15b1e-b487-4b67-b1ad-021f5ac5e063",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TdZGBFxG1KRQZSeEQAepwQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 129863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 646
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 163_

<details open><summary>🔧 Tool call — Read · `toolu_01Gz1VEDYUmrxSQnpFmR8zoc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "3693ff1a-dd67-46e7-9a3c-1e9e98c5722c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TdZGBFxG1KRQZSeEQAepwQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 129863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 646
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 164 · 2026-05-15T09:47:25.119Z_

<details><summary>↩ Tool result · `toolu_01Gz1VEDYUmrxSQnpFmR8zoc`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction, but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.
3	Under constrained decoding---the standard regime for schema-compliant IE---we evaluate five confidence signals from three families across NER and relation extraction on three benchmarks with two 8B-parameter model families.
4	These signals achieve strong quality estimation, yet none significantly improves sample selection over greedy decoding despite 13--18 percentage points of oracle headroom.
5	Four of five signals are instance-level by construction and cannot rank candidates; the key empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection can bridge this gap.
6	Neither succeeds: log-probability scores are compressed into effective ties for 60\% of instances under constrained decoding, while consensus-proximity (MBR decoding) fails because utility correlates with quality across instances but not within them.
7	Where log-probability compression is absent, selection recovers significant gains ($+2.9$~pp, $p{=}0.01$), identifying constrained-decoding score compression as the primary bottleneck.
8	Signal rankings further depend on task complexity, with findings consistent across model families.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "1c3a7ce2-25a1-4a16-8801-83dcc65f5e65",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction, but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.\nUnder constrained decoding---the standard regime for schema-compliant IE---we evaluate five confidence signals from three families across NER and relation extraction on three benchmarks with two 8B-parameter model families.\nThese signals achieve strong quality estimation, yet none significantly improves sample selection over greedy decoding despite 13--18 percentage points of oracle headroom.\nFour of five signals are instance-level by construction and cannot rank candidates; the key empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection can bridge this gap.\nNeither succeeds: log-probability scores are compressed into effective ties for 60\\% of instances under constrained decoding, while consensus-proximity (MBR decoding) fails because utility correlates with quality across instances but not within them.\nWhere log-probability compression is absent, selection recovers significant gains ($+2.9$~pp, $p{=}0.01$), identifying constrained-decoding score compression as the primary bottleneck.\nSignal rankings further depend on task complexity, with findings consistent across model families.\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---


### Tool call

_source line 165_

<details open><summary>🔧 Tool call — Read · `toolu_0155RvfWybXFcXVmsMcVS5sm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "7aeb840d-6d00-430c-ab35-d32f05e504e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TdZGBFxG1KRQZSeEQAepwQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 129863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 646
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 166 · 2026-05-15T09:47:25.346Z_

<details><summary>↩ Tool result · `toolu_0155RvfWybXFcXVmsMcVS5sm`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Within the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \textit{correlation-selection gap}.
4	By construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to constrained-decoding-induced score compression.
5	Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.
6	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
7	RE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.
8	A direct free-form generation ablation would confirm whether the bottleneck is decoding-regime-specific.
9	Trained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "8e2e7021-09eb-468d-bafd-a1d50a608011",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWithin the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \\textit{correlation-selection gap}.\nBy construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to constrained-decoding-induced score compression.\nWhere compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.\nSignal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.\nRE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.\nA direct free-form generation ablation would confirm whether the bottleneck is decoding-regime-specific.\nTrained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---


### Tool call

_source line 167_

<details open><summary>🔧 Tool call — Read · `toolu_01CV9qhLUwkFeCXwSpnPqsFA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "f4eb391a-6011-4b45-8111-96beccda2b58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TdZGBFxG1KRQZSeEQAepwQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 129863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 646
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 168 · 2026-05-15T09:47:26.023Z_

<details><summary>↩ Tool result · `toolu_01CV9qhLUwkFeCXwSpnPqsFA`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	Under constrained decoding, LP scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
14	This diagnostic confirms that LP carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.
15	The LP compression mechanism is a direct consequence of constrained decoding's restricted token space; alternative decoding strategies may yield different LP distributions.
16	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
17	
18	\paragraph{Connection to MBR decoding.}
19	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
20	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
21	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
22	
23	\paragraph{Toward mechanistic confirmation.}
24	Our diagnosis predicts that LP score compression should diminish under free-form (unconstrained) generation, where the full token vocabulary is available at each step.
25	A controlled ablation---comparing LP selection under constrained versus free-form decoding on identical instances, with post-hoc JSON parsing for the free-form condition---would directly test whether the bottleneck is decoding-regime-specific.
26	\textit{[Planned experiment: free-form ablation on SciERC NER/RE.]}
27	All findings reported in this paper are specific to the constrained decoding regime; whether the gap persists under relaxed or free-form decoding remains an open question.
28	
29	\paragraph{Methodological implications.}
30	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
31	Effective selection likely requires either per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "e62a75d9-2fd4-4cdf-8102-06c04dd1df7f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\nUnder constrained decoding, LP scores are severely compressed: 60\\% of instances have a within-sample range below 0.05, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$; Appendix~\\ref{app:logprob_ties}).\nIn the 40\\% of instances where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\\rho$: 0.08$\\to$0.39).\nThis diagnostic confirms that LP carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.\nThe LP compression mechanism is a direct consequence of constrained decoding's restricted token space; alternative decoding strategies may yield different LP distributions.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Toward mechanistic confirmation.}\nOur diagnosis predicts that LP score compression should diminish under free-form (unconstrained) generation, where the full token vocabulary is available at each step.\nA controlled ablation---comparing LP selection under constrained versus free-form decoding on identical instances, with post-hoc JSON parsing for the free-form condition---would directly test whether the bottleneck is decoding-regime-specific.\n\\textit{[Planned experiment: free-form ablation on SciERC NER/RE.]}\nAll findings reported in this paper are specific to the constrained decoding regime; whether the gap persists under relaxed or free-form decoding remains an open question.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires either per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---


### Assistant

_source line 169_

All edits verified. Now syncing the artifact paper sections for provenance tracking.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "b6d049c0-b577-422b-9fa8-b5054fa6b498",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsaEt9MenSAQhMSfUJ3e4d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5248,
      "cache_read_input_tokens": 130509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5248
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

_source line 170_

<details open><summary>🔧 Tool call — Read · `toolu_01KyTXbPNwi9UBcyTN53nJ8T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "324d48e7-f55d-49e3-a976-48e381fce4af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsaEt9MenSAQhMSfUJ3e4d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5248,
      "cache_read_input_tokens": 130509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5248
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

_source line 171 · 2026-05-15T09:47:29.760Z_

<details><summary>↩ Tool result · `toolu_01KyTXbPNwi9UBcyTN53nJ8T`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}). A 3-seed stability analysis ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}, Appendix~\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}
20	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
21	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}
25	\label{sec:qe_results}
26	
27	\begin{table*}[t]
28	\centering
29	\small
30	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
31	\label{tab:quality_estimation}
32	\begin{tabular}{ll cc cc cc cc}
33	\toprule
34	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
35	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
36	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
37	\midrule
38	VC & Structural & \textbf{.379} & .684 & \textbf{.350} & .693 & .424 & .789 & .426 & .709 \\
39	SJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
40	FK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
41	EM  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
42	LP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \textbf{.761} \\
43	\bottomrule
44	\end{tabular}
45	\end{table*}
46	
47	\begin{figure*}[t]
48	\centering
49	\includegraphics[width=\textwidth]{fig_signal_heatmap}
50	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
51	\label{fig:signal_heatmap}
52	\end{figure*}
53	
54	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
55	
56	\paragraph{Difficulty-dependent signal complementarity.}
57	On SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$).
58	This advantage persists on RE (VC $\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\% zero-F1 floor effect.
59	VC and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
60	While the best $\rho{=}0.38$ (VC) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{For scale context, semantic entropy \cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA, though direct comparison is not meaningful due to fundamentally different output spaces and evaluation protocols.}
61	Pairwise bootstrap CIs confirm the SJ advantage over LP ($\Delta\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\Delta\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal}).
62	
63	\paragraph{$\rho$--AUROC dissociation.}
64	Signal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295), preferred for binary quality triage; structural signals ($\rho{\geq}0.36$) are better for fine-grained ranking.
65	On CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\rho$ (0.307), confirming this pattern across datasets.
66	
67	\paragraph{Signal rankings shift with task difficulty.}
68	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.
69	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
70	This crossover---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.
71	Stability across the two model families (both 8B) is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
72	On WNUT-17, where 52\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
73	LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$).
74	We hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.
75	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
76	
77	\paragraph{Conditional filtering.}
78	Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
79	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
80	LP RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
81	This creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
82	
83	%% ============================================================
84	\subsection{The Correlation-Selection Gap}
85	\label{sec:selection_gap}
86	
87	\begin{figure*}[t]
88	\centering
89	\includegraphics[width=\textwidth]{fig_selection_gap}
90	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound.}
91	\label{fig:selection_gap}
92	\end{figure*}
93	
94	\begin{table}[t]
95	\centering
96	\small
97	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \textbf{bold}. EM selects the plurality output; despite a 42\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}
98	\label{tab:selection}
99	\begin{tabular}{lcc}
100	\toprule
101	Method & NER F1 & RE F1 \\
102	\midrule
103	Oracle & 0.776 & 0.585 \\
104	\midrule
105	LP           & \textbf{0.650} & 0.395 \\
106	SJ       & 0.645 & 0.386 \\
107	EM        & 0.636 & 0.372 \\
108	VC                 & 0.634 & 0.359 \\
109	\midrule
110	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
111	Random             & 0.608 & 0.354 \\
112	\bottomrule
113	\end{tabular}
114	\end{table}
115	
116	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
117	Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.
118	The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
119	We anchor this analysis on SciERC, where output diversity is substantial: only 11--18\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.
120	
121	\paragraph{No significant improvement over greedy.}
122	We exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).
123	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
124	LP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).
125	On RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.
126	TOST equivalence testing confirms most signals are indistinguishable from greedy at ${\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\pm}5$~pp (Table~\ref{tab:tost}, Appendix~\ref{app:diversity}).
127	VC ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{below} greedy.
128	The gap extends to CoNLL (ceiling effect, 57--88\% identical outputs) and WNUT-17 (capability boundary; Table~\ref{tab:cross_selection}).
129	
130	\paragraph{Quality estimation $\neq$ output selection.}
131	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
132	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
133	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
134	
135	%% ============================================================
136	\subsection{Robustness}
137	\label{sec:robustness_main}
138	
139	Consistency-based signals show robust performance across $T{\in}\{0.7, 1.0\}$ (SJ NER $\Delta\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$; Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
140	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "2bce09bc-b0d0-4a33-b081-253d6c1da856",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nWe note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.\nNo reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.\nThis constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.\nWe discuss implications in the Limitations section.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}). A 3-seed stability analysis ($\\sigma{\\leq}0.025$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Difficulty-dependent signal complementarity.}\nOn SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and LP ($\\rho{=}0.205$).\nThis advantage persists on RE (VC $\\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\\% zero-F1 floor effect.\nVC and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (VC) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{For scale context, semantic entropy \\cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA, though direct comparison is not meaningful due to fundamentally different output spaces and evaluation protocols.}\nPairwise bootstrap CIs confirm the SJ advantage over LP ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\\Delta\\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal}).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nSignal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295), preferred for binary quality triage; structural signals ($\\rho{\\geq}0.36$) are better for fine-grained ranking.\nOn CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\\rho$ (0.307), confirming this pattern across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis crossover---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.\nStability across the two model families (both 8B) is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 52\\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$).\nWe hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \\citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLP RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \\textbf{bold}. EM selects the plurality output; despite a 42\\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLP           & \\textbf{0.650} & 0.395 \\\\\nSJ       & 0.645 & 0.386 \\\\\nEM        & 0.636 & 0.372 \\\\\nVC                 & 0.634 & 0.359 \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial: only 11--18\\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.\n\n\\paragraph{No significant improvement over greedy.}\nWe exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.\nTOST equivalence testing confirms most signals are indistinguishable from greedy at ${\\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\\pm}5$~pp (Table~\\ref{tab:tost}, Appendix~\\ref{app:diversity}).\nVC ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{below} greedy.\nThe gap extends to CoNLL (ceiling effect, 57--88\\% identical outputs) and WNUT-17 (capability boundary; Table~\\ref{tab:cross_selection}).\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals show robust performance across $T{\\in}\\{0.7, 1.0\\}$ (SJ NER $\\Delta\\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$; Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nNER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\n",
      "numLines": 141,
      "startLine": 1,
      "totalLines": 141
    }
  }
}
```

</details>

---


### Assistant

_source line 172_

<details><summary>Logged reasoning block</summary>

```text
Good. The experiments.tex looks correct with all the edits applied. Let me now sync the artifacts using write_paper_section for all modified sections.

Actually, let me first check what specific things still need attention:

1. I need to add "(preliminary, single benchmark)" to the RE TOST equivalence line in experiments.tex (line 126). Currently: "on RE, EM and VC fail equivalence even at ±5~pp" - should add "(preliminary)". But this might be in the experiments section which describes results rather than draws conclusions. The task specifically says Discussion/Conclusion. Let me leave it.


2. Now I'm verifying the RE preliminary markers are consistently applied across Discussion and Conclusion sections. Checking the Discussion section, I see the preliminary notation at line 4 and line 16, and in Conclusion at line 7. All three locations have the proper "(preliminary, single benchmark)" tags.

3. For the RE selection details, the task mentions moving them to the Appendix, but looking at the experiments section, there's only a minimal mention in the "No significant improvement" paragraph, so that's already appropriately concise.

4. I should sync the critical sections now—abstract, introduction, discussion, conclusion, and experiments—rather than going through everything given the scope of this task.

5. Before finalizing, I need to double-check the Nédellec/SF-9 claim in related work and verify the minor items: Figure 1 caption is already concise, the FK excess agreement significance has been added to the methods, and the semantic entropy footnote doesn't need number removals.

Now I'm checking the final state of the related work section for the Nédellec reference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "687bace3-1781-4c69-b665-2da7bccde24b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUvunBTa7U1MXLChwp3Z1y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4860,
      "cache_read_input_tokens": 135757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4860
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 173_

Let me verify the related work section is correct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "080ae60d-e4de-4af4-90d3-d49b5c29e1de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUvunBTa7U1MXLChwp3Z1y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4860,
      "cache_read_input_tokens": 135757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4860
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 174_

<details open><summary>🔧 Tool call — Read · `toolu_016asLsQy4Kd5fjsNDiDMsZL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "202aa75e-7920-4409-8589-5aefd11990c6",
  "uuid": "a5e5f88f-0d01-4db9-ab93-3a13f05f33d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUvunBTa7U1MXLChwp3Z1y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4860,
      "cache_read_input_tokens": 135757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4860
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---
