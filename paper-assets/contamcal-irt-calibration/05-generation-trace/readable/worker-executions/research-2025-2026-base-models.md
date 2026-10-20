# research 2025 2026 base models

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 295
- **Recorded user turns:** 4
- **Tool calls:** 93
- **Original source:** `logs/workers/worker_research_2025-2026-base-models_20260518T070717.log`
- **Structured JSON:** [`97012fb2f8c6b7e24fbb.json`](../../sessions/97/97012fb2f8c6b7e24fbb.json)

## Before a recorded user message

10 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
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
  "uuid": "0b3503c8-acdc-4b11-97c7-50056534edf0",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1779105600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "bc751546-6e49-40f6-8c54-322dab075241",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to search for the latest open-source base models (7B-14B) from 2025-2026 for their contamination calibration paper. They need 5 model families for cross-family validation. Let me launch parallel web searches to gather this information efficiently.

Let me first load the WebSearch tool, then launch multiple search agents in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "64425b0b-bed5-4d3d-ab4a-921515c4ce87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4EJjVYM9HbZTpmY5NrpAh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14117,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14117
      },
      "output_tokens": 48,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SMhtys5MBoFBFVndtm2NYk`</summary>

```json
{
  "query": "select:WebSearch",
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
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "a2c19ded-8a6d-4d33-99b4-1de8c1356f92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4EJjVYM9HbZTpmY5NrpAh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14117,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14117
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T07:07:30.008Z_

<details><summary>↩ Tool result · `toolu_01SMhtys5MBoFBFVndtm2NYk`</summary>

````text
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
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "6faeecc4-926a-4726-81e8-3b2dff69c2e4",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
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
Now let me launch parallel web searches for all the keywords the user specified. I'll use multiple agents to search in parallel for efficiency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "96161667-043a-4797-9b74-af40c9154c95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2JdnQVstyta5ag8imEWYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 25958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 699
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

_source line 8_

开始并行搜索 10 个关键词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "6c4eff74-8844-4251-b4ac-072737428fa3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2JdnQVstyta5ag8imEWYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 25958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 699
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

_source line 9_

<details open><summary>🔧 Tool call — Agent · `toolu_019GEYgwrqvsAqC9HcwLnZ7s`</summary>

```json
{
  "description": "Search batch 1: general + HF",
  "subagent_type": "general-purpose",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"best open source LLM 2025 2026 base model\"\nSearch 2: \"latest base models huggingface 2025\"\nSearch 3: \"new open source LLM families 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "45f9c1d2-c26b-4532-b966-e7ffa02a770c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2JdnQVstyta5ag8imEWYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 25958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 699
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

### System

_source line 10_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Search batch 1: general + HF",
  "task_type": "local_agent",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"best open source LLM 2025 2026 base model\"\nSearch 2: \"latest base models huggingface 2025\"\nSearch 3: \"new open source LLM families 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range.",
  "uuid": "c340a3d3-3b87-4a41-95a9-6f008c4302cf",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

## Round 1

3 recorded events

### User

_source line 11 · 2026-05-18T07:07:38.449Z_

You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.

Search 1: "best open source LLM 2025 2026 base model"
Search 2: "latest base models huggingface 2025"
Search 3: "new open source LLM families 2025 2026"

Return ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f05d6f35-cf46-42fd-9ae7-58743bd9d106"
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Agent · `toolu_01UUx3h1Z4EHFrb7q9YJpLgR`</summary>

```json
{
  "description": "Search batch 2: Llama + Qwen + Mistral",
  "subagent_type": "general-purpose",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Llama 4 base model release\"\nSearch 2: \"Qwen 3 base model\"\nSearch 3: \"Mistral latest base model 2025\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "98f79d7d-3d0e-4989-bfea-4fbfe0109d7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2JdnQVstyta5ag8imEWYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 25958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 699
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

### System

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Search batch 2: Llama + Qwen + Mistral",
  "task_type": "local_agent",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Llama 4 base model release\"\nSearch 2: \"Qwen 3 base model\"\nSearch 3: \"Mistral latest base model 2025\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range.",
  "uuid": "7c2f7592-be07-49b7-9440-0f2e17303302",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

## Round 2

6 recorded events

### User

_source line 14 · 2026-05-18T07:07:40.453Z_

You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.

Search 1: "Llama 4 base model release"
Search 2: "Qwen 3 base model"
Search 3: "Mistral latest base model 2025"

Return ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "7c9c9d84-90e5-4c72-906c-75d0c2ad4ba3"
}
```

</details>

---

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Search batch 1: general + HF",
  "usage": {
    "total_tokens": 15529,
    "tool_uses": 1,
    "duration_ms": 3488
  },
  "last_tool_name": "ToolSearch",
  "uuid": "45830a79-419e-455b-b70b-f4fc5aef582b",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018ELxibVVD5ckC6fCZpvEp1`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "406ece16-a79f-47a2-ab48-4d6e7117c7ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg18Hh2mtyrCZHumEmUv1D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15518,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15518,
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

_source line 17 · 2026-05-18T07:07:41.941Z_

<details><summary>↩ Tool result · `toolu_018ELxibVVD5ckC6fCZpvEp1`</summary>

````text
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
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "499db8e1-e6b1-4929-8fb9-95c3ac52a50d"
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Agent · `toolu_01BPp8oiLtg786D15Msvztwn`</summary>

```json
{
  "description": "Search batch 3: Gemma + OLMo",
  "subagent_type": "general-purpose",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Gemma 3 base model\"\nSearch 2: \"OLMo 2 base model\"\nSearch 3: \"Gemma 3 pretrained model huggingface 2025\"\n\nReturn ALL findings in a structured format. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f98bdbe4-4d54-45ec-8be5-1afad109d931",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2JdnQVstyta5ag8imEWYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 25958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 699
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

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Search batch 3: Gemma + OLMo",
  "task_type": "local_agent",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Gemma 3 base model\"\nSearch 2: \"OLMo 2 base model\"\nSearch 3: \"Gemma 3 pretrained model huggingface 2025\"\n\nReturn ALL findings in a structured format. Be thorough.",
  "uuid": "d5540598-baf2-4592-b385-b030e41781ef",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

## Round 3

12 recorded events

### User

_source line 20 · 2026-05-18T07:07:42.911Z_

You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.

Search 1: "Gemma 3 base model"
Search 2: "OLMo 2 base model"
Search 3: "Gemma 3 pretrained model huggingface 2025"

Return ALL findings in a structured format. Be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "75fc47d9-3396-4094-83ba-1d741efd1f75"
}
```

</details>

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Search batch 2: Llama + Qwen + Mistral",
  "usage": {
    "total_tokens": 15517,
    "tool_uses": 1,
    "duration_ms": 3248
  },
  "last_tool_name": "ToolSearch",
  "uuid": "949090f5-5c93-499d-b27f-06ad714271ed",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for best open source LLM 2025 2026 base model 7B 14B …",
  "usage": {
    "total_tokens": 16984,
    "tool_uses": 2,
    "duration_ms": 6663
  },
  "last_tool_name": "WebSearch",
  "uuid": "27747dda-67e2-49ac-91e4-dab4c90bd62a",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for latest base models huggingface 2025 2026 open sou…",
  "usage": {
    "total_tokens": 16986,
    "tool_uses": 3,
    "duration_ms": 7163
  },
  "last_tool_name": "WebSearch",
  "uuid": "33708f07-71e3-448e-a89c-aa87789096c9",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for new open source LLM families 2025 2026 base model…",
  "usage": {
    "total_tokens": 16988,
    "tool_uses": 4,
    "duration_ms": 7215
  },
  "last_tool_name": "WebSearch",
  "uuid": "d6d5539f-7eab-486c-8e11-6c43d6be841e",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RKx8Sb6C1xa3wMXpnYfWmJ`</summary>

```json
{
  "query": "best open source LLM 2025 2026 base model 7B 14B parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "e8d7199f-46cf-4a72-9a85-5e03daabc728",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8bbgSSwYxysuP3tZgow4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
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

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xf1AdMfWajmi3d4RXg9YLA`</summary>

```json
{
  "query": "latest base models huggingface 2025 2026 open source LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "5b882b5a-c0c6-491b-9978-2c3ca06f2daf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8bbgSSwYxysuP3tZgow4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
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

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PuNz9DDDjEg8pJUQbgBHs2`</summary>

```json
{
  "query": "new open source LLM families 2025 2026 base model release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f0fc92ea-e644-40f9-81d4-4637ea81a036",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8bbgSSwYxysuP3tZgow4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
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

_source line 28_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Cg69Mr5Di3UT5C1vLtphpk`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "88188b0c-3649-446f-a4d1-fac2373a677d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxN232UscPWqes2sptmTJJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15506,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15506,
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

_source line 29 · 2026-05-18T07:07:43.705Z_

<details><summary>↩ Tool result · `toolu_01Cg69Mr5Di3UT5C1vLtphpk`</summary>

````text
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
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "a8d554dd-1b9c-4ba8-bd51-cee59ffb3c50"
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Agent · `toolu_01XSzbYG4aNMXhPUJ8DwFSt1`</summary>

```json
{
  "description": "Search batch 4: DeepSeek + Phi",
  "subagent_type": "general-purpose",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"DeepSeek V3 base model\"\nSearch 2: \"Phi-4 base model\"\nSearch 3: \"DeepSeek R2 base model 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range. Also note if any of these models use MoE architecture (mixture of experts) and what the active parameter count is."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "faccd5e5-3705-46db-bae1-72dc2de8c36a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2JdnQVstyta5ag8imEWYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 25958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 699
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

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Search batch 4: DeepSeek + Phi",
  "task_type": "local_agent",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"DeepSeek V3 base model\"\nSearch 2: \"Phi-4 base model\"\nSearch 3: \"DeepSeek R2 base model 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range. Also note if any of these models use MoE architecture (mixture of experts) and what the active parameter count is.",
  "uuid": "533c1e17-6e86-47c6-a474-73222a7699e1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

## Round 4

264 recorded events

### User

_source line 32 · 2026-05-18T07:07:46.106Z_

You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.

Search 1: "DeepSeek V3 base model"
Search 2: "Phi-4 base model"
Search 3: "DeepSeek R2 base model 2025 2026"

Return ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range. Also note if any of these models use MoE architecture (mixture of experts) and what the active parameter count is.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "dad4b010-2d99-4082-90f0-908dca468ef1"
}
```

</details>

---

### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Search batch 3: Gemma + OLMo",
  "usage": {
    "total_tokens": 15509,
    "tool_uses": 1,
    "duration_ms": 3251
  },
  "last_tool_name": "ToolSearch",
  "uuid": "637ed2bf-38fd-494e-9cf6-d4721d31dd09",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Jq43cw7wJ5FiZSQKwN7Jnb`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "9b67311d-85a9-4475-90c4-6391a0813d44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Nvw8SSJvH16inVA5LLeQF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7245,
      "cache_read_input_tokens": 8253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7245,
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

_source line 35 · 2026-05-18T07:07:46.167Z_

<details><summary>↩ Tool result · `toolu_01Jq43cw7wJ5FiZSQKwN7Jnb`</summary>

````text
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
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "9947205b-d4de-4bc8-93ad-7aa05fc2c068"
}
```

</details>

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Llama 4 base model release 2025 2026 7B 8B parame…",
  "usage": {
    "total_tokens": 16972,
    "tool_uses": 2,
    "duration_ms": 6541
  },
  "last_tool_name": "WebSearch",
  "uuid": "6e52562a-ae2a-4874-ad02-b4802d892aa7",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FXK3xJDKzFfkcFbZ6E77Qk`</summary>

```json
{
  "query": "Llama 4 base model release 2025 2026 7B 8B parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f084a653-61c6-485f-9998-ab103d92cc94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G5aosdJKkWnDuYT3VDZf7q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Qwen 3 base model 2025 2026 HuggingFace 7B 8B 14B",
  "usage": {
    "total_tokens": 16974,
    "tool_uses": 3,
    "duration_ms": 7448
  },
  "last_tool_name": "WebSearch",
  "uuid": "8fed84fa-a5d9-4a2a-83e1-196f2b6fff03",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DNEeXZxEKwijizS7fGCLwW`</summary>

```json
{
  "query": "Qwen 3 base model 2025 2026 HuggingFace 7B 8B 14B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "01f37fca-b7d6-4de6-bd45-779700a9c3ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G5aosdJKkWnDuYT3VDZf7q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Mistral latest base model 2025 2026 7B parameters…",
  "usage": {
    "total_tokens": 16976,
    "tool_uses": 4,
    "duration_ms": 7538
  },
  "last_tool_name": "WebSearch",
  "uuid": "77bbf8e8-47fb-4602-a0b7-b03b65174337",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EN3jKeC7ys8MU9HKsjmisi`</summary>

```json
{
  "query": "Mistral latest base model 2025 2026 7B parameters release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "418effc4-d643-4ea4-aa86-15b03a584861",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G5aosdJKkWnDuYT3VDZf7q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Search batch 4: DeepSeek + Phi",
  "usage": {
    "total_tokens": 15547,
    "tool_uses": 1,
    "duration_ms": 3026
  },
  "last_tool_name": "ToolSearch",
  "uuid": "623b7b97-51e4-499f-ba72-54eb1d5bb308",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PmuWZTvFJWW2UJr1SeeRDN`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "4493316f-cfaa-4c9b-b1e2-4b09804d7a9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcYy1HWgNmMvQ1LPTKgYXT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7283,
      "cache_read_input_tokens": 8253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7283,
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

_source line 44 · 2026-05-18T07:07:49.136Z_

<details><summary>↩ Tool result · `toolu_01PmuWZTvFJWW2UJr1SeeRDN`</summary>

````text
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
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "dd5729e2-89ca-4227-b3fd-a7491aaeaa94"
}
```

</details>

---

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for Gemma 3 base model 2025 huggingface parameters re…",
  "usage": {
    "total_tokens": 16964,
    "tool_uses": 2,
    "duration_ms": 8374
  },
  "last_tool_name": "WebSearch",
  "uuid": "da611475-59f0-4e06-9916-9fc51d3efa23",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BsD5iSvEVWfc6jhip8ttBD`</summary>

```json
{
  "query": "Gemma 3 base model 2025 huggingface parameters release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "38df6cfb-eb11-4031-adfb-59388f909f86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Tu8nBWJ3srPv9hN3zekij",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for OLMo 2 base model 2025 huggingface parameters rel…",
  "usage": {
    "total_tokens": 16966,
    "tool_uses": 3,
    "duration_ms": 8804
  },
  "last_tool_name": "WebSearch",
  "uuid": "cd74e424-29f1-401e-85b3-0cae43b24b51",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RuJsCtBnT55kfZce8p5rxh`</summary>

```json
{
  "query": "OLMo 2 base model 2025 huggingface parameters release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "a0c78931-c8fa-4e00-b542-426179e4e93a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Tu8nBWJ3srPv9hN3zekij",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for Gemma 3 pretrained model huggingface 2025",
  "usage": {
    "total_tokens": 16968,
    "tool_uses": 4,
    "duration_ms": 8847
  },
  "last_tool_name": "WebSearch",
  "uuid": "6bca9b99-279e-434c-861e-f9e314917e86",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jc2So4CcrNEZGfbqsypBzt`</summary>

```json
{
  "query": "Gemma 3 pretrained model huggingface 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "3562ec3c-c8bc-4c23-a5aa-dd893c5ff545",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Tu8nBWJ3srPv9hN3zekij",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for DeepSeek V3 base model HuggingFace 7B 14B paramet…",
  "usage": {
    "total_tokens": 17002,
    "tool_uses": 2,
    "duration_ms": 6026
  },
  "last_tool_name": "WebSearch",
  "uuid": "6231c60a-e5db-4290-af1f-f76bf354b183",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013dnFFByY7aXsWdv3Taau1a`</summary>

```json
{
  "query": "DeepSeek V3 base model HuggingFace 7B 14B parameters 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "c03ea3ca-6c63-4285-bf03-9e8a8a1b708b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4JzKiokS3km9MvED4LQgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Phi-4 base model HuggingFace parameters 2025 2026",
  "usage": {
    "total_tokens": 17004,
    "tool_uses": 3,
    "duration_ms": 6498
  },
  "last_tool_name": "WebSearch",
  "uuid": "35269d16-b2df-49b3-96f2-5fa294273937",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017VuJHp2EPxoQ9KhWYediGC`</summary>

```json
{
  "query": "Phi-4 base model HuggingFace parameters 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f51088c2-2dc6-42e3-be4b-48051e69e3ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4JzKiokS3km9MvED4LQgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for DeepSeek R2 base model 2025 2026",
  "usage": {
    "total_tokens": 17006,
    "tool_uses": 4,
    "duration_ms": 6711
  },
  "last_tool_name": "WebSearch",
  "uuid": "edf82222-8609-4164-afb3-432a4b5a181e",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015Cy6U2vyj3X8SnswnMQkLB`</summary>

```json
{
  "query": "DeepSeek R2 base model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "36036e67-a04c-4316-aa1f-03a04018b50d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4JzKiokS3km9MvED4LQgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 15536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
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

_source line 57 · 2026-05-18T07:07:53.897Z_

<details><summary>↩ Tool result · `toolu_01FXK3xJDKzFfkcFbZ6E77Qk`</summary>

```text
Web search results for query: "Llama 4 base model release 2025 2026 7B 8B parameters"

Links: [{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"Llama (language model) - Wikipedia","url":"https://en.wikipedia.org/wiki/Llama_(language_model)"},{"title":"Meta AI All Models Available: Llama‑4, Llama‑3, and Deployment Options","url":"https://www.datastudios.org/post/meta-ai-all-models-available-llama-4-llama-3-and-deployment-options"},{"title":"LLaMA 4 Explained - Everything You Need to Know","url":"https://www.labellerr.com/blog/llama-4/"},{"title":"Meta's Llama 4 models now available on AWS","url":"https://www.aboutamazon.com/news/aws/aws-meta-llama-4-models-available"},{"title":"Meta Llama 4 explained: Everything you need to know","url":"https://www.techtarget.com/whatis/feature/Meta-Llama-4-explained-Everything-you-need-to-know"},{"title":"Unmatched Performance and Efficiency | Llama 4","url":"https://www.llama.com/models/llama-4/"},{"title":"Llama 4: Did Meta just push the panic button?","url":"https://www.interconnects.ai/p/llama-4"},{"title":"Meta releases Llama 4, a new crop of flagship AI models | TechCrunch","url":"https://techcrunch.com/2025/04/05/meta-releases-llama-4-a-new-crop-of-flagship-ai-models/"},{"title":"Meta Llama: Everything you need to know about the open generative AI model | TechCrunch","url":"https://techcrunch.com/2025/10/06/meta-llama-everything-you-need-to-know-about-the-open-generative-ai-model/"}]

Based on the search results, here's what I found about Llama 4 base model releases:

## Llama 4 Release Information

On April 5, 2025, Meta released the Llama 4 model family, which includes the following base models:

### Model Specifications

Scout: 17 billion active parameter model with 16 experts, context window of 10M, with 109B parameters in total

Maverick: 17 billion active parameter model with 128 experts, context window of 1M, with 400B parameters in total

### Behemoth Model

The Behemoth model was also announced, but was not released. Meta claimed it was a 288 billion active parameter model with 16 experts and around 2T parameters in total; it was still in training when Scout and Maverick were released.

### Key Architecture Features

The Llama 4 models are the first LLMs in the Llama family to employ a mixture-of-experts architecture: Only a subset of the total parameters activate for an input token.

It's important to note that your query asked about 7B and 8B parameter models, but the released Llama 4 base models (Scout and Maverick) both feature 17 billion active parameters, not the smaller sizes you mentioned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f17b05ec-7d5e-4cfd-b765-0e589dbc2620"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-18T07:07:55.425Z_

<details><summary>↩ Tool result · `toolu_01Xf1AdMfWajmi3d4RXg9YLA`</summary>

```text
Web search results for query: "latest base models huggingface 2025 2026 open source LLM"

Links: [{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"State of Open Source on Hugging Face: Spring 2026","url":"https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026"},{"title":"Open LLM Leaderboard best models ❤️‍🔥 - a open-llm-leaderboard Collection","url":"https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-best-models"},{"title":"The Best Open Source and Open-Weight LLM Models to Run Locally in 2026","url":"https://huggingface.co/blog/daya-shankar/open-source-llm-models-to-run-locally"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Top 10 Downloaded Open-Source Models on HuggingFace","url":"https://www.analyticsvidhya.com/blog/2025/11/top-open-source-models-on-huggingface/"},{"title":"Top 10 LLM Models on Hugging Face | Cloudsmith","url":"https://cloudsmith.com/blog/top-10-most-popular-llm-models-on-hugging-face"},{"title":"Top 7 Platforms to Fine-Tune Open Source LLMs in 2026 | Second Talent","url":"https://www.secondtalent.com/resources/top-platforms-to-fine-tune-open-source-llms/"},{"title":"Models – Hugging Face","url":"https://huggingface.co/models"},{"title":"The Best Open-Source Small Language Models (SLMs) in 2026","url":"https://www.bentoml.com/blog/the-best-open-source-small-language-models"}]

Based on the search results, here's a comprehensive overview of the latest base models on Hugging Face for 2025-2026 open source LLMs:

## Key Latest Models (2025-2026)

### Flagship Models

Kimi K2.6 is one of the strongest open-weight models for developers in 2026. The Hugging Face model card lists it under a Modified MIT license and shows a model size of about 1.1T parameters.

Qwen3 is the model family that quietly became the answer to "what should I run locally?" for most developers. Sizes range from 1.7B to 235B, with an Apache 2.0 license with no user cap, no commercial restrictions, no legal headaches.

Meta dropped Llama 4 in April 2025, and it's a different beast from what came before. Llama 4 won gold medals in IMO 2025 and IOI 2025, solving competitive programming and math olympiads with an open-weights model.

### Small Language Models (SLMs)

SmolLM3-3B is a fully open instruct and reasoning model from Hugging Face, outperforming Llama-3.2-3B and Qwen2.5-3B while staying competitive with many 4B-class alternatives across 12 popular LLM benchmarks.

### For Local Deployment

Microsoft built Phi-4-mini-instruct, one of the most quietly impressive models of 2026, and the point is that it runs on the machine you already have.

## Ecosystem Growth

In 2025, Hugging Face grew to 13 million users, more than 2 million public models, and over 500,000 public datasets. China surpassed the U.S. in monthly downloads and overall downloads, with Chinese models quickly accounting for the plurality or 41% of downloads.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "4b2532cf-91a8-4a5d-990c-97a3142e6640"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-18T07:07:55.441Z_

<details><summary>↩ Tool result · `toolu_01DNEeXZxEKwijizS7fGCLwW`</summary>

```text
Web search results for query: "Qwen 3 base model 2025 2026 HuggingFace 7B 8B 14B"

Links: [{"title":"Qwen3 - a Qwen Collection","url":"https://huggingface.co/collections/Qwen/qwen3"},{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"Qwen (Qwen)","url":"https://huggingface.co/Qwen/collections"},{"title":"Qwen/Qwen3-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B"},{"title":"Download Qwen-3 Models - MoE, Dense & Quantized Versions","url":"https://qwen-3.com/en/download"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/qwen3"},{"title":"Qwen/Qwen3-8B-GGUF · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-GGUF"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen/Qwen3-1.7B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-1.7B-Base"},{"title":"Qwen/Qwen3-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B"}]

Based on the web search results, here's what I found about Qwen 3 base models:

## Qwen3 Overview

Qwen3 is the latest generation of large language models in Qwen series, offering a comprehensive suite of dense and mixture-of-experts (MoE) models.

## Available Base Models

Six dense models are open-weighted, including Qwen3-32B, Qwen3-14B, Qwen3-8B, Qwen3-4B, Qwen3-1.7B, and Qwen3-0.6B, with both pre-trained and post-trained versions available on platforms like Hugging Face, ModelScope, and Kaggle.

Notably, the specific models you asked about (7B, 8B, 14B) include the **Qwen3-8B** and **Qwen3-14B** base models. There is no 7B model in the Qwen3 lineup, but the 8B serves a similar purpose.

## Key Improvements

Qwen3 is pre-trained on 36 trillion tokens across 119 languages — tripling the language coverage of Qwen2.5 — with a much richer mix of high-quality data, including coding, STEM, reasoning, book, multilingual, and synthetic data.

## Technical Requirements

The latest version of transformers is recommended and transformers>=4.51.0 is required.

All Qwen3 base models are available on HuggingFace and can be accessed through their official model cards.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "fe693b11-a3c7-4b9f-a94f-bc394439f97f"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T07:07:56.121Z_

<details><summary>↩ Tool result · `toolu_01RKx8Sb6C1xa3wMXpnYfWmJ`</summary>

```text
Web search results for query: "best open source LLM 2025 2026 base model 7B 14B parameters"

Links: [{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"Best Open-Source LLM 2026: 8 Tested, 3 Beat GPT-4 | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"Best Open-Source LLMs in 2026 - Featherless","url":"https://featherless.ai/blog/best-open-source-llms-2026"},{"title":"Open LLM Leaderboard best models ❤️‍🔥 - a open-llm-leaderboard Collection","url":"https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-best-models"},{"title":"The Best Open Source and Open-Weight LLM Models to Run Locally in 2026","url":"https://huggingface.co/blog/daya-shankar/open-source-llm-models-to-run-locally"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Best Open-Source LLMs in 2026: A Practical Guide by Use Case - ML Journey","url":"https://mljourney.com/best-open-source-llms-in-2026-a-practical-guide-by-use-case/"},{"title":"Best Local LLM Models 2026 | Developer Comparison","url":"https://www.sitepoint.com/best-local-llm-models-2026/"},{"title":"Best Open Source LLMs in 2026: DeepSeek, Llama & More","url":"https://www.miniloop.ai/blog/best-open-source-llms-2026"}]

Based on the search results, here's a comprehensive overview of the best open-source LLM base models in the 7B-14B parameter range for 2025-2026:

## Top Base Models in 7B-14B Range

### 7B Models

**Qwen2.5-Coder 7B** - Fits on 8GB VRAM and outperforms general-purpose models twice its size on code generation, debugging, and refactoring.

**Qwen 3 7B** - Posts the highest HumanEval score (76.0) of any model under 8B parameters in this comparison, a 3.4-point margin over Llama 3.3's 72.6. Its multilingual support is the strongest across all four families, with particular strength in CJK languages alongside robust English performance.

**Mistral Small 3 7B** - Achieves approximately 50 tokens per second on mid-range 16GB hardware at Q4_K_M, the fastest in this comparison. It scores 8.0 on MT-Bench, the instruction-following benchmark, producing well-structured outputs with minimal prompt engineering.

### 14B Models

**DeepSeek-R1 14B** - DeepSeek also released distilled variants at 1.5B, 7B, 14B, 32B, and 70B parameters.

**Phi-4 14B** - Phi-4 14B is recommended for those who want to run something on a single GPU. The Phi-4 14B variant at Q5_K_M scales up to 76.2 MMLU, competitive with much larger models.

**Qwen2.5-Coder 14B** - The 14B variant is the sweet spot for 16GB VRAM setups — noticeably better at multi-file reasoning and complex algorithm implementation.

## Key Recommendations

For general use: For most developers, Llama 3.3 8B is the best overall starting point. Mistral Small 3 7B wins when throughput matters most, Phi-4-mini (3.8B) is the only real option on low-resource hardware, and Qwen 3 7B leads for code generation and multilingual work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "a503b54e-6289-4a49-98b4-6c73c1f7253f"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-18T07:07:56.417Z_

<details><summary>↩ Tool result · `toolu_01EN3jKeC7ys8MU9HKsjmisi`</summary>

```text
Web search results for query: "Mistral latest base model 2025 2026 7B parameters release"

Links: [{"title":"Mistral 7B","url":"https://mistral.ai/news/announcing-mistral-7b"},{"title":"Mistral Docs","url":"https://docs.mistral.ai/models/overview"},{"title":"Mistral 7B | Mistral AI","url":"https://legal.mistral.ai/ai-governance/models/mistral-7-b"},{"title":"Mistral 7B LLM | Prompt Engineering Guide&lt;!-- -->","url":"https://www.promptingguide.ai/models/mistral-7b"},{"title":"Mistral 7B - Mistral AI | Mistral Docs","url":"https://docs.mistral.ai/models/mistral-7b-0-1"},{"title":"Mistral 3 AI Explained - Open-Source Models Guide 2026 — Shawn Kanungo","url":"https://shawnkanungo.com/blog/what-is-mistral-3-ai-open-source-models-guide-2026"},{"title":"mistral","url":"https://ollama.com/library/mistral"},{"title":"mistral-7b-instruct-v0.2 Model by Mistral AI","url":"https://build.nvidia.com/mistralai/mistral-7b-instruct-v2/modelcard"},{"title":"Models - from cloud to edge | Mistral AI","url":"https://mistral.ai/models"},{"title":"Mistral AI Models 2026: Small 4, Large 3, Voxtral TTS, Forge — Complete Guide | Serenities AI","url":"https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide"}]

Based on the search results, here's information about Mistral's latest base models in 2025-2026:

## Mistral 3 Family (December 2025)

Mistral 3 AI is a family of 10 artificial intelligence models that launched in December 2025. The Ministral 3 family includes dense models at 14B, 8B, and 3B parameters. 

The base model lineup includes:
- 3B, 8B, and 14B models for different use cases

Key features of Mistral 3 base models:
- Every single model in the family can process both text and images, with vision baked into the core training
- Trained natively on over 40 languages with particular strength in European languages
- Mistral 3 extends context windows up to 256K tokens
- Released under the Apache 2.0 license, allowing free commercial use and modification

## Mistral Small 4 (March 2026)

In March 2026, Mistral launched Mistral Small 4, which combines instruction following, deep reasoning, image understanding, and coding with 119 billion total parameters but only activates 6 billion per token.

The original Mistral 7B was their very first open model, SOTA competing against models up to 2 to 3x larger.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "4b02a2d8-94d5-485b-b272-ab9e87a325ab"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-18T07:07:58.470Z_

<details><summary>↩ Tool result · `toolu_01PuNz9DDDjEg8pJUQbgBHs2`</summary>

```text
Web search results for query: "new open source LLM families 2025 2026 base model release"

Links: [{"title":"Open-Source LLM Landscape 2026, 15+ Model Families Mapped | Presenc AI","url":"https://presenc.ai/research/open-source-llm-landscape-2026"},{"title":"Best Open-Source LLMs in 2026 - Featherless","url":"https://featherless.ai/blog/best-open-source-llms-2026"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"AI Updates Today (May 2026) – Latest AI Model Releases","url":"https://llm-stats.com/llm-updates"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Open-Source LLMs 2026: Llama 4, Mistral, Qwen, Falcon & More | AI Moments","url":"https://www.singularitymoments.com/open-source-llms-2026/"},{"title":"Open Source LLM Releases 2026: Every Major Model So Far - Fazm Blog","url":"https://fazm.ai/blog/open-source-llm-releases-2026"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"}]

Based on the search results, here's a comprehensive overview of new open-source LLM families released in 2025-2026:

## Major Model Families Released

### Meta Llama 4 (April 2025)
Llama 4 includes Scout (109B total, 17B active, 10M context window), Maverick (400B total, 17B active, 1M context), and the announced but unreleased Behemoth (~2T total, 288B active). Llama 4 is the most widely deployed open source model family, with over 650 million total downloads and roughly 9% of enterprise production workloads running on Llama variants.

### DeepSeek Models (2024-2025)
DeepSeek has released open-weight models including DeepSeek V2, V3, and the reasoning-focused R1 (2024-2025). The latest release DeepSeek-V4 is designed for long-context reasoning, coding, and agentic workflows, with two large MoE models: DeepSeek-V4-Pro (1.6T total, 49B active) and DeepSeek-V4-Flash (284B total, 13B active).

### Alibaba Qwen Models (2025-2026)
Qwen 3.5 (released February 2026) is a native vision-language model with 397B total parameters (17B active per pass), supporting 201 languages and offering a 1M token context window.

### Moonshot Kimi K2 Line (2025)
Moonshot released the open-weight Kimi K2 line during 2025. Kimi K2.5 has 1 trillion parameters with MoE (32B active), 384 experts, and a unique Agent Swarm architecture.

### Google Gemma 3 (January 2026)
Google released Gemma 3 in January 2026 with four sizes: 1B, 4B, 12B, and 27B parameters. Key improvements include native vision support, a 128K context window across all sizes, and a new sliding-window attention mechanism that reduces memory usage.

### Mistral Family (2025-2026)
Mistral is a European frontier AI company with models including Mistral 7B, Mixtral 8x7B/8x22B (mixture-of-experts), Mistral Large (2024), and later iterations, offering both fully open-weight models under Apache 2.0 and commercial tier models.

### Other Notable Releases
Cohere released Command A in March 2026, using a 111B parameter MoE architecture with 23B active parameters and supporting a 256K context window, optimized for retrieval-augmented generation (RAG) workflows.

2025 was the year open-source LLMs closed the gap with proprietary models, and in 2026, they're on par in many areas – or better.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "086fa922-3f8e-4d73-b003-d965dc937345"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-18T07:07:59.263Z_

<details><summary>↩ Tool result · `toolu_013dnFFByY7aXsWdv3Taau1a`</summary>

```text
Web search results for query: "DeepSeek V3 base model HuggingFace 7B 14B parameters 2025 2026"

Links: [{"title":"deepseek-ai/DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3"},{"title":"DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/deepseek_v3"},{"title":"deepseek-ai/DeepSeek-V3-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3-Base"},{"title":"DeepSeek-V3","url":"https://huggingface.co/docs/transformers/main/en/model_doc/deepseek_v3"},{"title":"deepseek-ai/DeepSeek-V3.1-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Base"},{"title":"anchovy/DeepSeek-V3-Base · Hugging Face","url":"https://huggingface.co/anchovy/DeepSeek-V3-Base"},{"title":"README_WEIGHTS.md · deepseek-ai/DeepSeek-V3 at main","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/README_WEIGHTS.md"},{"title":"deepseek-ai/DeepSeek-V3.2 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3.2"},{"title":"unsloth/DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/unsloth/DeepSeek-V3"},{"title":"deepseek-ai/DeepSeek-V3 - Demo - DeepInfra","url":"https://deepinfra.com/deepseek-ai/DeepSeek-V3"}]

Based on the search results, I found information about DeepSeek V3. However, I should clarify that the specific 7B and 14B parameter versions you mentioned in your query don't appear to exist for DeepSeek V3.

## DeepSeek V3 Model Specifications

DeepSeek-V3 is a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. The total size of DeepSeek-V3 models on HuggingFace is 685B, which includes 671B of the Main Model weights and 14B of the Multi-Token Prediction (MTP) Module weights.

The DeepSeek V3 base model is available on HuggingFace under the repository `deepseek-ai/DeepSeek-V3-Base`. This is the primary base model available, and it does not come in 7B or 14B variants - it is a 671B parameter model.

There are newer versions like DeepSeek-V3.1, which is a hybrid model that supports both thinking mode and non-thinking mode.

If you're looking for smaller parameter models from DeepSeek, you may want to explore other versions like DeepSeek-V2 or other model families, as the V3 series appears to be focused on the large 671B parameter model architecture.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "be1f8a30-9c69-4e51-b9d0-88458d78fea3"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-18T07:07:59.293Z_

<details><summary>↩ Tool result · `toolu_01RuJsCtBnT55kfZce8p5rxh`</summary>

```text
Web search results for query: "OLMo 2 base model 2025 huggingface parameters release"

Links: [{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"OLMo 2 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-2"},{"title":"allenai/Olmo-3-1125-32B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1125-32B"},{"title":"allenai/OLMo-2-0325-32B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct"},{"title":"allenai/OLMo-2-0325-32B-SFT · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-SFT"},{"title":"allenai/OLMo-2-0425-1B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B"},{"title":"OLMo2 · Hugging Face","url":"https://huggingface.co/docs/transformers/main/en/model_doc/olmo2"},{"title":"allenai/OLMo-2-0425-1B-DPO · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B-DPO"},{"title":"allenai/OLMo-2-1124-13B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B"},{"title":"OLMo2","url":"https://huggingface.co/docs/transformers/v4.56.2/en/model_doc/olmo2"}]

Based on the search results, here's what I found about OLMo 2 base models released in 2025:

## OLMo 2 Model Releases

OLMo 2 is a new family of 7B and 13B models featuring a 9-point increase in MMLU, among other evaluation improvements, compared to the original OLMo 7B model.

### Available Model Sizes

The OLMo 2 family includes multiple model sizes:

1. **7B Model** - The 7B model was trained on OLMo-mix-1124 and Dolmino-mix-1124 datasets using a staged training approach.

2. **13B Model** - A 13B model trained on up to 5T tokens.

3. **1B Model** - OLMo 2 1B is the smallest model in the OLMo 2 family.

4. **32B Model** - Available as of March 2025

### Key Details

- **Training**: Models were trained on up to 5T tokens.
- **Release**: This model was released on 2024-12-31 and added to Hugging Face Transformers on 2024-11-25.
- **Licensing**: OLMo 2 is licensed under the Apache 2.0 license.

All these models are available on Hugging Face under the allenai organization and are designed as base models for further fine-tuning and research purposes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "2875200a-ea70-4241-8646-9bb8a6d3fef7"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-18T07:07:59.349Z_

<details><summary>↩ Tool result · `toolu_01BsD5iSvEVWfc6jhip8ttBD`</summary>

```text
Web search results for query: "Gemma 3 base model 2025 huggingface parameters release"

Links: [{"title":"Gemma 3 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma3"},{"title":"Gemma 3","url":"https://huggingface.co/docs/transformers/v4.57.3/en/model_doc/gemma3"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"Gemma 3 Release - a google Collection","url":"https://huggingface.co/collections/google/gemma-3-release"},{"title":"google/gemma-3n-E4B-it-litert-preview · Hugging Face","url":"https://huggingface.co/google/gemma-3n-E4B-it-litert-preview"},{"title":"Gemma 3 - a unsloth Collection","url":"https://huggingface.co/collections/unsloth/gemma-3"},{"title":"Gemma 3n fully available in the open-source ecosystem!","url":"https://huggingface.co/blog/gemma3n"},{"title":"Gemma3n","url":"https://huggingface.co/docs/transformers/en/model_doc/gemma3n"},{"title":"Gemma 3 - How to Run Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/models/tutorials/gemma-3-how-to-run-and-fine-tune"},{"title":"google/gemma-3-27b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-it"}]

Based on the search results, here's what I found about Gemma 3 base models released in 2025 on Hugging Face:

## Model Sizes and Parameters

Gemma 3 comes in four sizes: 1 billion, 4 billion, 12 billion, and 27 billion parameters with base (pre-trained) and instruction-tuned versions. Additionally, Google released Gemma 3 with a new 270M model, so the complete lineup includes five different sizes.

## Multimodal Capabilities

The 4, 12, and 27 billion parameter models can process both images and text, while the 1B variant is text only. The 270M model is also text-only.

## Context Window

The input context window length has been increased from Gemma 2's 8k to 32k for the 1B variants, and 128k for all others.

## Release Timeline

Gemma 3 is Google's latest iteration of open weight LLMs, released in 2025. Additionally, Gemma 3n was released on 2025-05-20, which is a variant with specialized parameter activation technology.

## Performance

Gemma-3-4B-IT beats Gemma-2-27B IT, while Gemma-3-27B-IT beats Gemini 1.5-Pro across benchmarks.

All these models are available on Hugging Face under Google's official collections.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "ed6e188d-3815-4646-b20b-efd98604f3d3"
}
```

</details>

---

### System

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Qwen3-8B-Base Qwen3-14B-Base HuggingFace release …",
  "usage": {
    "total_tokens": 19757,
    "tool_uses": 5,
    "duration_ms": 19207
  },
  "last_tool_name": "WebSearch",
  "uuid": "36ea71f8-fe44-41f2-a6b3-52da7777d4ce",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CHLNHEtJ4QyDFwSWnyUjbb`</summary>

```json
{
  "query": "Qwen3-8B-Base Qwen3-14B-Base HuggingFace release date benchmark performance training data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "ecc87d90-1ad6-4006-9037-98742013c009",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FSeDSPYSP7duqEnVEk73u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2781,
      "cache_read_input_tokens": 16957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2781,
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

### System

_source line 68_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Mistral 3 base model 8B 14B HuggingFace release d…",
  "usage": {
    "total_tokens": 19758,
    "tool_uses": 6,
    "duration_ms": 20015
  },
  "last_tool_name": "WebSearch",
  "uuid": "892af8e7-f667-4be8-8882-a2ecd2f9d3bc",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E1DRFFceYjffEdvZBRWwEC`</summary>

```json
{
  "query": "Mistral 3 base model 8B 14B HuggingFace release date December 2025 benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "939e8619-9066-4a9a-8dd4-d91efff63c12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FSeDSPYSP7duqEnVEk73u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2781,
      "cache_read_input_tokens": 16957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2781,
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

### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Llama 4 Scout Maverick base pretrained model Hugg…",
  "usage": {
    "total_tokens": 19759,
    "tool_uses": 7,
    "duration_ms": 20177
  },
  "last_tool_name": "WebSearch",
  "uuid": "25a239c2-15f1-47be-af9a-689021053a42",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HBBJANGbVDy5mUabSpGEmY`</summary>

```json
{
  "query": "Llama 4 Scout Maverick base pretrained model HuggingFace gated download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "cbb57737-5d72-41ed-a853-896d69d9fc28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FSeDSPYSP7duqEnVEk73u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2781,
      "cache_read_input_tokens": 16957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2781,
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

_source line 72 · 2026-05-18T07:08:01.119Z_

<details><summary>↩ Tool result · `toolu_017VuJHp2EPxoQ9KhWYediGC`</summary>

```text
Web search results for query: "Phi-4 base model HuggingFace parameters 2025 2026"

Links: [{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"},{"title":"microsoft/Phi-4-reasoning-vision-15B · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B"},{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"nvidia/Phi-4-multimodal-instruct-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Phi-4-multimodal-instruct-NVFP4"},{"title":"microsoft/Phi-4-mini-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-reasoning"},{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"nvidia/Phi-4-reasoning-plus-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Phi-4-reasoning-plus-NVFP4"},{"title":"microsoft/Phi-4-mini-flash-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-flash-reasoning"},{"title":"microsoft/Phi-4-multimodal-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-multimodal-instruct"}]

Based on the web search results, here's information about Phi-4 base model parameters available on HuggingFace:

## Phi-4 Model Variants and Parameters

The Phi-4 family includes several models with different parameter sizes:

1. **Phi-4-mini models**: The model with only 3.8B-param achieves a similar level of multilingual language understanding and reasoning ability as much larger models. This includes variants like Phi-4-mini-instruct and Phi-4-mini-reasoning.

2. **Phi-4 Base Model**: While the search results don't explicitly state the base model's parameter count, they reference a standard Phi-4 model.

3. **Phi-4-Reasoning**: Phi-4-reasoning, with only 14B parameters, performs well across a wide range of reasoning tasks

4. **Phi-4-Reasoning-Vision-15B**: Released March 4, 2026 with 15B parameters and 16,384 tokens context length

5. **Phi-4-multimodal-instruct**: Number of model parameters 5.6×10^9 (5.6B parameters)

6. **Phi-4-mini-flash-reasoning**: Featuring 3.8 billion parameters and a 200K vocabulary

## Additional Technical Details

- Phi-4-mini-instruct supports a vocabulary size of up to 200064 tokens
- The model supports 128K token context length

These models are available on HuggingFace under the Microsoft organization and were released/updated between 2025 and early 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "e41c0323-e56c-480f-bf40-e98999c6ec25"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-18T07:08:01.560Z_

<details><summary>↩ Tool result · `toolu_01Jc2So4CcrNEZGfbqsypBzt`</summary>

```text
Web search results for query: "Gemma 3 pretrained model huggingface 2025"

Links: [{"title":"Gemma 3 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma3"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"transformers/docs/source/en/model_doc/gemma3.md at main · huggingface/transformers","url":"https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/gemma3.md"},{"title":"Gemma 3","url":"https://huggingface.co/docs/transformers/v5.0.0rc2/model_doc/gemma3"},{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"Run Gemma with Hugging Face Transformers | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/huggingface_inference"},{"title":"google/gemma-3-27b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-it"},{"title":"google/gemma-3-1b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-1b-it"},{"title":"Gemma 3 Release - a google Collection","url":"https://huggingface.co/collections/google/gemma-3-release"},{"title":"Gemma3n","url":"https://huggingface.co/docs/transformers/main/en/model_doc/gemma3n"}]

Based on the search results, here's comprehensive information about Gemma 3 pretrained models on Hugging Face:

## Overview

Google released Gemma 3, which ranges from 1B to 27B parameters, has a context window up to 128k tokens, can accept images and text, and supports 140+ languages. This model was released on 2025-03-25 and added to Hugging Face Transformers on 2025-03-12.

## Model Variants

Gemma 3 comes in four sizes: 1 billion, 4 billion, 12 billion, and 27 billion parameters with base (pre-trained) and instruction-tuned versions. The 4, 12, and 27 billion parameter models can process both images and text, while the 1B variant is text only.

## Key Features

- **Context Window**: The input context window length has been increased from Gemma 2's 8k to 32k for the 1B variants, and 128k for all others.

- **Multimodal Capabilities**: Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants.

## Availability

All the models are on the Hub and tightly integrated with the Hugging Face ecosystem. Both pre-trained and instruction tuned models are released.

The models are available on Hugging Face under Google's collection, with specific model IDs like `google/gemma-3-1b-pt`, `google/gemma-3-4b-pt`, `google/gemma-3-12b-pt`, and `google/gemma-3-27b-pt` for the pretrained variants.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "ac4c12ed-7420-463d-8a3d-88a32cbcc18a"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-18T07:08:01.825Z_

<details><summary>↩ Tool result · `toolu_015Cy6U2vyj3X8SnswnMQkLB`</summary>

```text
Web search results for query: "DeepSeek R2 base model 2025 2026"

Links: [{"title":"The Ultimate DeepSeek Guide 2026 | Master AI with DeepSeek-V3.2 & R2","url":"https://deepseek.ai/blog/deepseek-guide-2026"},{"title":"Will DeepSeek’s new model spark another global AI shake-up in 2026?","url":"https://restofworld.org/2025/deepseek-china-r2-ai-model-us-rivalry/"},{"title":"DeepSeek V4 and R2 Deep Dive | Meta Intelligence","url":"https://www.meta-intelligence.tech/en/insight-deepseek-v4-r2"},{"title":"DeepSeek's Next Move: What V4 Will Look Like","url":"https://recodechinaai.substack.com/p/deepseeks-next-move-what-v4-will"},{"title":"What is DeepSeek R2: The Best Upcoming AI Model In 2025? | AI Hub","url":"https://overchat.ai/ai-hub/what-is-deepseek-r2"},{"title":"Deepseek R2 Release Timeline & Updates 2025","url":"https://www.byteplus.com/en/topic/384181"},{"title":"DeepSeek - Wikipedia","url":"https://en.wikipedia.org/wiki/DeepSeek"},{"title":"DeepSeek Plans AI Agent Rollout in Late 2025 - Techstrong.ai","url":"https://techstrong.ai/features/deepseek-plans-ai-agent-rollout-in-late-2025/"},{"title":"DeepSeek Roadmap, Rumors & Confirmed Releases: What Is Official and What Is Not - Chat-Deep.ai","url":"https://chat-deep.ai/guide/deepseek-roadmap-rumors/"},{"title":"Ultimate Guide - The Best DeepSeek-AI Models in 2026","url":"https://www.siliconflow.com/articles/en/the-best-deepseek-ai-models-in-2025"}]

Based on the search results, here's what I found regarding DeepSeek R2 base model in 2025-2026:

## DeepSeek R2 Status

In late February 2026, multiple sources confirmed that DeepSeek was preparing to release two new models: DeepSeek V4 (the fourth generation of its general-purpose foundation model) and DeepSeek R2 (the second generation of its reasoning model).

However, as of May 7, 2026, R2 is not listed among the current model IDs in the official DeepSeek API model list, and no official R2 release was found in the checked DeepSeek model list or release pages.

## Development Timeline and Delays

The widely anticipated DeepSeek-V4 and DeepSeek-R2, which were reportedly slated for release in the first half of 2025, were delayed. DeepSeek initially attempted to train R2 using Huawei's Ascend AI chips rather than Western silicon like Nvidia's GPUs, partly due to pressure from the Chinese government to reduce reliance on U.S.-made hardware. The training runs encountered repeated failures and performance issues stemming from stability problems, slow chip-to-chip interconnect speeds, and immature software tooling.

## What Is Currently Available

Instead of R2, on April 24, 2026, DeepSeek released a preview of its V4 series, including the 1.6-trillion parameter DeepSeek-V4-Pro and the 284-billion parameter DeepSeek-V4-Flash, both featuring a 1-million token context window.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "b71eefce-fc6d-41e8-b6bc-3ba293ae96a7"
}
```

</details>

---

### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Qwen3 7B 8B base model huggingface repo release d…",
  "usage": {
    "total_tokens": 20628,
    "tool_uses": 5,
    "duration_ms": 23946
  },
  "last_tool_name": "WebSearch",
  "uuid": "deed172d-6fd5-4ec9-a661-c864546715fe",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016j9mQYndRRdA9Q6Sth2QCj`</summary>

```json
{
  "query": "Qwen3 7B 8B base model huggingface repo release date benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "b63afec5-bbdb-4cd1-bc37-0b7fc9024c05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SKekHLGuou85HY3kMEt9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3640,
      "cache_read_input_tokens": 16969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3640,
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

### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Gemma 3 12B base model huggingface repo benchmark…",
  "usage": {
    "total_tokens": 20629,
    "tool_uses": 6,
    "duration_ms": 24283
  },
  "last_tool_name": "WebSearch",
  "uuid": "f13bd7a9-d596-4b4d-925f-3e79ea87cf84",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V4ACkuaeDNffwnUYvBQW5x`</summary>

```json
{
  "query": "Gemma 3 12B base model huggingface repo benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "1d3848b1-fad8-49bd-818e-fc25f79c8127",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SKekHLGuou85HY3kMEt9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3640,
      "cache_read_input_tokens": 16969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3640,
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

### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Llama 4 8B base model huggingface 2025 release",
  "usage": {
    "total_tokens": 20630,
    "tool_uses": 7,
    "duration_ms": 24813
  },
  "last_tool_name": "WebSearch",
  "uuid": "ef09a393-2802-4494-a50b-44b42278e770",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017sHpfYuQ6DKc2TMyiLhEQb`</summary>

```json
{
  "query": "Llama 4 8B base model huggingface 2025 release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "36b8db71-02e4-42b3-8481-a0b2fd9c4b7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SKekHLGuou85HY3kMEt9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3640,
      "cache_read_input_tokens": 16969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3640,
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

### System

_source line 81_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Phi-4 14B base model huggingface repo release dat…",
  "usage": {
    "total_tokens": 20631,
    "tool_uses": 8,
    "duration_ms": 25202
  },
  "last_tool_name": "WebSearch",
  "uuid": "2bc5ab8f-dacf-4b01-bd7f-38d318195efc",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AkbAta3waqKdU5g4qkRVcX`</summary>

```json
{
  "query": "Phi-4 14B base model huggingface repo release date training data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "9a45af7d-d527-4219-b217-8168086e030b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SKekHLGuou85HY3kMEt9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3640,
      "cache_read_input_tokens": 16969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3640,
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

### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for google/gemma-3-12b-pt huggingface model card gate…",
  "usage": {
    "total_tokens": 19861,
    "tool_uses": 5,
    "duration_ms": 22764
  },
  "last_tool_name": "WebSearch",
  "uuid": "f9d893c9-bcf8-4daf-bfd3-31cce588b8d9",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Cv1qQLAXnCJ43jDFhYwjR`</summary>

```json
{
  "query": "google/gemma-3-12b-pt huggingface model card gated benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "7ebd45a0-43cf-4c24-8026-c6091792df27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Urff7rBRDfEZZBQHyHLKkb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2893,
      "cache_read_input_tokens": 16949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2893,
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

### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for microsoft phi-4 14B base model HuggingFace parame…",
  "usage": {
    "total_tokens": 19946,
    "tool_uses": 5,
    "duration_ms": 19630
  },
  "last_tool_name": "WebSearch",
  "uuid": "84f98e56-2524-4f18-812a-7bf452a7fb81",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QNSqgeU7eL4UnNrVUnF346`</summary>

```json
{
  "query": "microsoft phi-4 14B base model HuggingFace parameters release date gated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "c379a0ea-de86-4ada-ab00-3edc215eca0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsLNqEhKFpFMvSMZNE6cvF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2940,
      "cache_read_input_tokens": 16987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2940,
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

### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for allenai/OLMo-2-1124-7B huggingface model card ben…",
  "usage": {
    "total_tokens": 19862,
    "tool_uses": 6,
    "duration_ms": 23110
  },
  "last_tool_name": "WebSearch",
  "uuid": "55da4e6a-e615-4092-b329-508dacdc0f40",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qf8zamfsMpMEAyKasYqsoB`</summary>

```json
{
  "query": "allenai/OLMo-2-1124-7B huggingface model card benchmark training tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "443343d6-9486-472f-9f19-c4f304da5c87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Urff7rBRDfEZZBQHyHLKkb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2893,
      "cache_read_input_tokens": 16949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2893,
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

_source line 89 · 2026-05-18T07:08:06.575Z_

<details><summary>↩ Tool result · `toolu_01HBBJANGbVDy5mUabSpGEmY`</summary>

```text
Web search results for query: "Llama 4 Scout Maverick base pretrained model HuggingFace gated download"

Links: [{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"},{"title":"meta-llama/Llama-4-Scout-17B-16E · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E"},{"title":"unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Original · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Original"},{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF"},{"title":"meta-llama/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct"},{"title":"unsloth/Llama-4-Maverick-17B-128E · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E"},{"title":"unsloth/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct"}]

Based on the search results, here's what I found about Llama 4 Scout and Maverick base pretrained models on HuggingFace:

## Model Overview

Llama 4 Maverick (~400B) and Llama 4 Scout (~109B) were released on the Hugging Face Hub, and both are Mixture of Experts (MoE) models with 17B active parameters.

## Base Pretrained Models

Llama 4 Scout was pretrained on ~40 trillion tokens and Llama 4 Maverick was pretrained on ~22 trillion tokens of multimodal data. The Llama 4 models were pre-trained with a context length of 256K.

## Model Weights and Formats

The Llama 4 Scout model is released as BF16 weights, but can fit within a single H100 GPU with on-the-fly int4 quantization; the Llama 4 Maverick model is released as both BF16 and FP8 quantized weights.

## License and Access

A custom commercial license, the Llama 4 Community License Agreement, is available. The search results indicate these models are available on the HuggingFace Hub under the meta-llama organization, but specific information about gated download access requirements isn't explicitly detailed in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "8d940305-eeea-496b-b2e5-e13f2896f944"
}
```

</details>

---

### System

_source line 90_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for allenai/OLMo-2-1124-13B huggingface model card be…",
  "usage": {
    "total_tokens": 19863,
    "tool_uses": 7,
    "duration_ms": 23691
  },
  "last_tool_name": "WebSearch",
  "uuid": "35bbac39-c684-404e-8892-7b90e42cbdc4",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R5wGDapjWC3JZiKHh7nbe5`</summary>

```json
{
  "query": "allenai/OLMo-2-1124-13B huggingface model card benchmark training data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "b45ac1af-4d9c-4327-9352-b957a7a1ced6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Urff7rBRDfEZZBQHyHLKkb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2893,
      "cache_read_input_tokens": 16949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2893,
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

### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for DeepSeek V3 V2 small model 7B 14B 16B lite base 2…",
  "usage": {
    "total_tokens": 19947,
    "tool_uses": 6,
    "duration_ms": 20574
  },
  "last_tool_name": "WebSearch",
  "uuid": "3180b199-b9e3-459c-9743-7a416b7ef7ed",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JKRViMRvEi7fp8YmNYvPE4`</summary>

```json
{
  "query": "DeepSeek V3 V2 small model 7B 14B 16B lite base 2025 2026 HuggingFace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "3b4d74b2-d7a0-44d7-af93-0ca48ff0395f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsLNqEhKFpFMvSMZNE6cvF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2940,
      "cache_read_input_tokens": 16987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2940,
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

### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for google/gemma-3-4b-pt huggingface pretrained base …",
  "usage": {
    "total_tokens": 19864,
    "tool_uses": 8,
    "duration_ms": 24127
  },
  "last_tool_name": "WebSearch",
  "uuid": "a32898e4-c39f-4eeb-a507-4c87fdf82540",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 95_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016x964ydLED7y8FhJRy3Ctr`</summary>

```json
{
  "query": "google/gemma-3-4b-pt huggingface pretrained base model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "2f2fadb9-e9e8-4a24-9f70-9a5e6cc8102d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Urff7rBRDfEZZBQHyHLKkb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2893,
      "cache_read_input_tokens": 16949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2893,
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

### System

_source line 96_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Phi-4 base pretrained model not instruct HuggingF…",
  "usage": {
    "total_tokens": 19948,
    "tool_uses": 7,
    "duration_ms": 21214
  },
  "last_tool_name": "WebSearch",
  "uuid": "10e6c487-c726-41e0-b11a-17dd4dee3728",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 97_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CkKiWfnh2V3QRabazuRRMP`</summary>

```json
{
  "query": "Phi-4 base pretrained model not instruct HuggingFace microsoft 14B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "70587238-2616-4115-896a-1ad5dc09d8c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsLNqEhKFpFMvSMZNE6cvF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2940,
      "cache_read_input_tokens": 16987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2940,
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

_source line 98 · 2026-05-18T07:08:08.241Z_

<details><summary>↩ Tool result · `toolu_01CHLNHEtJ4QyDFwSWnyUjbb`</summary>

```text
Web search results for query: "Qwen3-8B-Base Qwen3-14B-Base HuggingFace release date benchmark performance training data"

Links: [{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"Qwen/Qwen3-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B"},{"title":"Speed Benchmark - Qwen","url":"https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen 3 Benchmarks, Comparisons, Model Specifications, and More - DEV Community","url":"https://dev.to/best_codes/qwen-3-benchmarks-comparisons-model-specifications-and-more-4hoa"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen/Qwen3-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"}]

Based on the search results, here's comprehensive information about Qwen3-8B-Base and Qwen3-14B-Base:

## Release Date
Qwen3 was released on April 29, 2025, with both the 8B and 14B base models included in this release.

## Model Specifications

**Qwen3-8B-Base:**
- Dense model architecture with 8B parameters

**Qwen3-14B-Base:**
The model has 14.8B parameters, 13.2B non-embedding parameters, 40 layers, 40 attention heads (GQA) for Q and 8 for KV, and a context length of 32,768 tokens.

## Training Data
Qwen3 is pre-trained on 36 trillion tokens across 119 languages with a much richer mix of high-quality data, including coding, STEM, reasoning, book, multilingual, and synthetic data.

## Benchmark Performance
All Qwen3 8B/4B/1.7B/0.6B-Base models continue to maintain strong performance across nearly all benchmarks, with Qwen3-8B/4B/1.7B-Base models even outperforming larger size Qwen2.5-14B models.

For the 14B variant, Qwen3-14B-Base achieves very competitive results compared to Qwen2.5-32B-Base, bringing significant advantages in inference and training costs.

Additionally, Qwen3-8B/14B-Base performs as well as Qwen2.5-14B/32B-Base respectively, and notably in areas like STEM, coding, and reasoning, Qwen3 dense base models even outperform larger Qwen2.5 models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "ef695c16-201e-4939-ae39-8c80e797ff98"
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-18T07:08:08.357Z_

<details><summary>↩ Tool result · `toolu_01E1DRFFceYjffEdvZBRWwEC`</summary>

```text
Web search results for query: "Mistral 3 base model 8B 14B HuggingFace release date December 2025 benchmark"

Links: [{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"Mistral 3 AI Explained - Open-Source Models Guide 2026 — Shawn Kanungo","url":"https://shawnkanungo.com/blog/what-is-mistral-3-ai-open-source-models-guide-2026"},{"title":"NVIDIA Partners With Mistral AI to Accelerate New Family of Open Models | NVIDIA Blog","url":"https://blogs.nvidia.com/blog/mistral-frontier-open-models/"},{"title":"Mistral Large 3: An Open-Source MoE LLM Explained | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mistral-large-3-moe-llm-explained"},{"title":"Mistral Large 3: First Look and Testing","url":"https://www.analyticsvidhya.com/blog/2025/12/mistral-large-3/"},{"title":"Mistral 3 Arrives With Large 3 and Ministral Models for Enterprise and Edge AI","url":"https://www.reworked.co/ai-platforms/mistral-3-arrives-with-large-3-and-ministral-models-for-enterprise-and-edge-ai/"},{"title":"Mistral Large 3 by Mistral AI on Vercel AI Gateway, Specs, Pricing & API","url":"https://vercel.com/ai-gateway/models/mistral-large-3"},{"title":"Ministral 3 - 8B | Mistral AI","url":"https://legal.mistral.ai/ai-governance/models/ministral-3-8b"},{"title":"Mistral 3 Models on DigitalOcean | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/mistral-3-models"},{"title":"Mistral Large 3 and Ministral 3 family now available first on Amazon Bedrock - AWS","url":"https://aws.amazon.com/about-aws/whats-new/2025/12/mistral-large-3-ministral-3-family-available-amazon-bedrock/"}]

Based on the web search results, here's the information about Mistral 3 base models:

## Release Date

Mistral 3 AI is a family of 10 artificial intelligence models that launched in December 2025. More specifically, Mistral 3 launched on December 2, 2025.

## Model Sizes

For edge and local use cases, the Ministral 3 series is available in three model sizes: 3B, 8B, and 14B parameters. For each model size, base, instruct, and reasoning variants are released to the community, each with image understanding capabilities, all under the Apache 2.0 license.

## HuggingFace Availability

Mistral 3 is available on Hugging Face (Large 3 & Ministral).

## Key Benchmarks

Mistral Large 3 debuts at #2 in the OSS non-reasoning models category (#6 amongst OSS models overall) on the LMArena leaderboard. The Ministral reasoning variants can produce state-of-the-art accuracy amongst their weight class - for instance 85% on AIME '25 with the 14B variant.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "eb2ee34b-1730-413a-9deb-bb63694346ca"
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-18T07:08:09.944Z_

<details><summary>↩ Tool result · `toolu_016j9mQYndRRdA9Q6Sth2QCj`</summary>

```text
Web search results for query: "Qwen3 7B 8B base model huggingface repo release date benchmark"

Links: [{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"GitHub - QwenLM/Qwen: The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen/Qwen3-8B-FP8 · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-FP8"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen3.6-27B: 27B Model Beats 397B on Coding (2026)","url":"https://www.buildfastwithai.com/blogs/qwen3-6-27b-review-2026"},{"title":"Qwen3 - a Qwen Collection","url":"https://huggingface.co/collections/Qwen/qwen3"},{"title":"Qwen/Qwen3-Embedding-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-8B"},{"title":"Qwen (Qwen)","url":"https://huggingface.co/Qwen"}]

Based on the search results, here's what I found about Qwen3 7B/8B base models:

## Release Date

Qwen3 was released in 2025, with the technical report available on arXiv (2505.09388). More specifically, Qwen3 was announced as the latest addition to the Qwen family of large language models.

## Hugging Face Repository

Six dense models are open-weighted, including Qwen3-32B, Qwen3-14B, Qwen3-8B, Qwen3-4B, Qwen3-1.7B, and Qwen3-0.6B, with pre-trained counterparts available on Hugging Face, ModelScope, and Kaggle.

## Base Model Performance Benchmarks

The overall performance of Qwen3 dense base models matches that of Qwen2.5 base models with more parameters. For instance, Qwen3-8B-Base performs as well as Qwen2.5-14B-Base. Additionally, in areas like STEM, coding, and reasoning, Qwen3 dense base models even outperform larger Qwen2.5 models.

## Key Features

Qwen3 is pre-trained on 36 trillion tokens across 119 languages — tripling the language coverage of Qwen2.5 — with a much richer mix of high-quality data, including coding, STEM, reasoning, book, multilingual, and synthetic data.

For more detailed benchmark evaluations, the blog, GitHub, and documentation contain detailed information including benchmark evaluation, hardware requirements, and inference performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "3dd936d3-ccc3-4451-8e91-394b2fc5f927"
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-18T07:08:10.217Z_

<details><summary>↩ Tool result · `toolu_017sHpfYuQ6DKc2TMyiLhEQb`</summary>

```text
Web search results for query: "Llama 4 8B base model huggingface 2025 release"

Links: [{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 · Hugging Face","url":"https://huggingface.co/nvidia/Llama-4-Scout-17B-16E-Instruct-FP8"},{"title":"aviol/Meta-Llama-4-8B · Hugging Face","url":"https://huggingface.co/aviol/Meta-Llama-4-8B"},{"title":"nvidia/Llama-3.1-8B-Instruct-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Llama-3.1-8B-Instruct-NVFP4"},{"title":"Llama4 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/llama4"},{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"},{"title":"Meta Llama 4 explained: Everything you need to know","url":"https://www.techtarget.com/whatis/feature/Meta-Llama-4-explained-Everything-you-need-to-know"},{"title":"LLaMA 4 Explained - Everything You Need to Know","url":"https://www.labellerr.com/blog/llama-4/"},{"title":"Llama (language model) - Wikipedia","url":"https://en.wikipedia.org/wiki/Llama_(language_model)"},{"title":"meta-llama/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct"}]

Based on the search results, here's what I found about Llama 4 and the 8B base model:

## Llama 4 Release Information

Llama 4 was released on April 5, 2025. However, it's important to note that the Llama 4 family of models comes in two flavors: 109B and 402B parameters, along with smaller efficient models.

## Llama 4 Model Sizes

Rather than an 8B base model, Meta is launching two efficient models in the Llama 4 series: Llama 4 Scout, a 17 billion parameter model with 16 experts, and Llama 4 Maverick, a 17 billion parameter model with 128 experts.

The Llama 4 collection of models are natively multimodal AI models that enable text and multimodal experiences, leveraging a mixture-of-experts architecture to offer industry-leading performance in text and image understanding.

## Availability on Hugging Face

Llama 4 is available at https://huggingface.co/meta-llama. The models can be accessed and used through the Hugging Face platform with the appropriate licenses and authentication.

If you were specifically looking for an 8B Llama model, Meta's previous generation Llama 3 came in 8B and 70B sizes, but Llama 4 focuses on larger, more efficient models using mixture-of-experts architecture.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "b7eb9741-0a6c-40fa-af89-98a2e98eb596"
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-18T07:08:11.384Z_

<details><summary>↩ Tool result · `toolu_01AkbAta3waqKdU5g4qkRVcX`</summary>

```text
Web search results for query: "Phi-4 14B base model huggingface repo release date training data"

Links: [{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"microsoft/Phi-4-multimodal-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-multimodal-instruct"},{"title":"microsoft/Phi-4-mini-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-reasoning"},{"title":"OpenMeditron/Meditron3-Phi4-14B · Hugging Face","url":"https://huggingface.co/OpenMeditron/Meditron3-Phi4-14B"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"Phi · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/phi"},{"title":"NyxKrage/Microsoft_Phi-4 · Hugging Face","url":"https://huggingface.co/NyxKrage/Microsoft_Phi-4"},{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"}]

Based on the web search results, here's the information about Phi-4 14B base model:

## Release Date

Phi-4 is Microsoft's December 2024 release of their efficient-LLM family — a 14.7B-parameter model.

## Training Data

The training data is an extension of the data used for Phi-3 and includes a wide variety of sources from: Publicly available documents filtered rigorously for quality, selected high-quality educational data, and code. Newly created synthetic, "textbook-like" data for the purpose of teaching math, coding, common sense reasoning, general knowledge of the world. Acquired academic books and Q&A datasets. High quality chat format supervised data covering various topics to reflect human preferences on different aspects such as instruct-following, truthfulness, honesty and helpfulness. Additionally, multilingual data constitutes about 8% of the overall data.

## HuggingFace Repository

The base model can be found at the official HuggingFace repository: `microsoft/phi-4`


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "2fb2e494-fa2d-4817-889a-97679a0e5e85"
}
```

</details>

---

### System

_source line 103_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Ministral 3 8B base model HuggingFace repo \"mistr…",
  "usage": {
    "total_tokens": 22971,
    "tool_uses": 8,
    "duration_ms": 31328
  },
  "last_tool_name": "WebSearch",
  "uuid": "9610b537-6989-4374-8395-a5812cab2d1b",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 104_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015jTKT4ueZPtV6WDLNKS9A2`</summary>

```json
{
  "query": "Ministral 3 8B base model HuggingFace repo \"mistralai\" parameters context length"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "cb64310e-f999-4a56-b728-1fe86efef127",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrniYZzyu6fTSwvHrr2aML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 998,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 19738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2213,
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

_source line 105 · 2026-05-18T07:08:11.880Z_

<details><summary>↩ Tool result · `toolu_01QNSqgeU7eL4UnNrVUnF346`</summary>

```text
Web search results for query: "microsoft phi-4 14B base model HuggingFace parameters release date gated"

Links: [{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"Introducing Phi-4: Microsoft’s Newest Small Language Model Specializing in Complex Reasoning | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-phi-4-microsoft%E2%80%99s-newest-small-language-model-specializing-in-comple/4357090"},{"title":"Microsoft Launches Two Powerful Phi-4 Reasoning Models","url":"https://www.analyticsvidhya.com/blog/2025/05/phi-4-reasoning-models/"},{"title":"microsoft/Phi-4-reasoning-vision-15B · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B"},{"title":"NyxKrage/Microsoft_Phi-4 · Hugging Face","url":"https://huggingface.co/NyxKrage/Microsoft_Phi-4"},{"title":"microsoft/phi-4 · Base model","url":"https://huggingface.co/microsoft/phi-4/discussions/4"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"microsoft/Phi-4-multimodal-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-multimodal-instruct"}]

Based on the web search results, here's what I found about Microsoft Phi-4 14B base model on HuggingFace:

## Key Information

**Parameters:** Phi-4 has 14.7B parameters

**Release Date:** Phi-4 is the December 2024 release of Microsoft's Phi family

**Model Status:** Phi-4 is available on Azure AI Foundry and on Hugging Face

**Architecture:** It's a standard decoder-only transformer with 16K context and ChatML chat template

**License:** The license is MIT — most permissive of recent major releases

Regarding the "gated" status of the base model, the search results show that base model release becomes difficult because of safety guidelines, which suggests there may be some considerations around the base model availability, though the results don't explicitly confirm whether the model card itself is gated or if it's freely available with standard MIT licensing.

The model is designed to excel at complex reasoning tasks, particularly in mathematics and coding, despite its relatively small size compared to larger language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "6378e633-e0ce-46d7-98f4-3485e0deb956"
}
```

</details>

---

### System

_source line 106_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Qwen3-8B-Base parameters layers context length ga…",
  "usage": {
    "total_tokens": 22972,
    "tool_uses": 9,
    "duration_ms": 31857
  },
  "last_tool_name": "WebSearch",
  "uuid": "7c1bc8c5-8563-4344-853f-b463a1cf0d0e",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 107_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0128CbeLKSF3XU8Ykiyr6HFt`</summary>

```json
{
  "query": "Qwen3-8B-Base parameters layers context length gated apache license"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "156aebe9-26b4-48f7-9860-b041042d8c3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrniYZzyu6fTSwvHrr2aML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 998,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 19738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2213,
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

_source line 108 · 2026-05-18T07:08:13.157Z_

<details><summary>↩ Tool result · `toolu_018Cv1qQLAXnCJ43jDFhYwjR`</summary>

```text
Web search results for query: "google/gemma-3-12b-pt huggingface model card gated benchmark"

Links: [{"title":"google/gemma-3-12b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-pt"},{"title":"Gemma 4 model overview | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core"},{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"google/gemma-3-12b-it-qat-q4_0-gguf · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-gguf"},{"title":"google/gemma-3-27b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-it"},{"title":"google/gemma-3-12b-pt at main","url":"https://huggingface.co/google/gemma-3-12b-pt/tree/main"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"Gemma 3: Google’s new open model based on Gemini 2.0","url":"https://blog.google/technology/developers/gemma-3/"},{"title":"google/gemma-3-27b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-pt"},{"title":"google/gemma-3-12b-it-qat-q4_0-unquantized · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized"}]

Based on the search results, I found information about the **google/gemma-3-12b-pt** model on Hugging Face:

## Key Information

**Model Access:** To access Gemma on Hugging Face, you're required to review and agree to Google's usage license. This is a gated model.

**Model Description:** Gemma is a family of lightweight, state-of-the-art open models from Google, built from the same research and technology used to create the Gemini models. Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants.

**Model Capabilities:** Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions. Gemma 3 models are well-suited for a variety of text generation and image understanding tasks, including question answering, summarization, and reasoning.

**Training:** The 12B model was trained with 12 trillion tokens. Gemma was trained using Tensor Processing Unit (TPU) hardware (TPUv4p, TPUv5p and TPUv5e).

**Benchmark Performance:** Using the benchmark evaluation metrics described in this document, these models have shown to provide superior performance to other, comparably-sized open model alternatives.

The "pt" in the model name indicates this is the pre-trained (not instruction-tuned) variant of the 12B Gemma 3 model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "7f534f2b-7596-4448-b1e3-9bf0822570c4"
}
```

</details>

---

### System

_source line 109_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Llama 4 Scout base pretrained non-instruct Huggin…",
  "usage": {
    "total_tokens": 22973,
    "tool_uses": 10,
    "duration_ms": 32801
  },
  "last_tool_name": "WebSearch",
  "uuid": "f34a1c02-2d9d-451f-94d6-c9858da0bea3",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 110_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AiAnEdGJ4ZxTMc6Ve4j5Sj`</summary>

```json
{
  "query": "Llama 4 Scout base pretrained non-instruct HuggingFace \"meta-llama\" gated license"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "75fadf22-4f6b-4e48-a9dc-c97fce815d8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrniYZzyu6fTSwvHrr2aML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 998,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 19738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2213,
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

_source line 111 · 2026-05-18T07:08:13.461Z_

<details><summary>↩ Tool result · `toolu_016x964ydLED7y8FhJRy3Ctr`</summary>

```text
Web search results for query: "google/gemma-3-4b-pt huggingface pretrained base model"

Links: [{"title":"google/gemma-3-4b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-4b-pt"},{"title":"google/gemma-3-4b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-4b-it"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-1b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-1b-pt"},{"title":"Gemma 3 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma3"},{"title":"RedHatAI/gemma-3-4b-it-quantized.w4a16 · Hugging Face","url":"https://huggingface.co/RedHatAI/gemma-3-4b-it-quantized.w4a16"},{"title":"Run Gemma with Hugging Face Transformers | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/huggingface_inference"},{"title":"Full Model Fine-Tune using Hugging Face Transformers | Gemma | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/huggingface_text_full_finetune"},{"title":"Fine-Tune Gemma for Vision Tasks using Hugging Face Transformers and QLoRA | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/huggingface_vision_finetune_qlora"},{"title":"google/gemma-3-1b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-1b-it"}]

Based on the web search results, here's what I found about the **google/gemma-3-4b-pt** model on Hugging Face:

## Model Overview

Gemma is a family of lightweight, state-of-the-art open models from Google, built from the same research and technology used to create the Gemini models. The "pt" suffix indicates this is the **pre-trained (base) version** rather than an instruction-tuned variant.

## Key Characteristics

Gemma 3 comes in four sizes, 1 billion, 4 billion, 12 billion, and 27 billion parameters with base (pre-trained) and instruction-tuned versions. The 4B variant has 4 billion parameters.

Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants.

## Model Capabilities

Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions. Gemma 3 models are well-suited for a variety of text generation and image understanding tasks, including question answering, summarization, and reasoning.

## Training Details

The 4B model was trained with 4 trillion tokens and Gemma was trained using Tensor Processing Unit (TPU) hardware (TPUv4p, TPUv5p and TPUv5e).

## Access Requirements

To access Gemma on Hugging Face, you're required to review and agree to Google's usage license.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "bf9e26f7-02b4-43d3-ad56-06953a685f01"
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-18T07:08:13.634Z_

<details><summary>↩ Tool result · `toolu_01V4ACkuaeDNffwnUYvBQW5x`</summary>

```text
Web search results for query: "Gemma 3 12B base model huggingface repo benchmark 2026"

Links: [{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"tensorblock/gemma-3-12b-it-GGUF · Hugging Face","url":"https://huggingface.co/tensorblock/gemma-3-12b-it-GGUF"},{"title":"google/gemma-3-12b-it-qat-q4_0-gguf · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-gguf"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-12b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-pt"},{"title":"RedHatAI/gemma-3-12b-it-quantized.w8a8 · Hugging Face","url":"https://huggingface.co/RedHatAI/gemma-3-12b-it-quantized.w8a8"},{"title":"Gemma 4 model overview | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core"},{"title":"nocturne23/gemma-3-12b-it-Q4_K_M-GGUF · Hugging Face","url":"https://huggingface.co/nocturne23/gemma-3-12b-it-Q4_K_M-GGUF"},{"title":"lmstudio-community/gemma-3-12b-it-GGUF · Hugging Face","url":"https://huggingface.co/lmstudio-community/gemma-3-12b-it-GGUF"},{"title":"Quantized Models for google/gemma-3-12b-it – Hugging Face","url":"https://huggingface.co/models?other=base_model%3Aquantized%3Agoogle%2Fgemma-3-12b-it"}]

Based on the web search results, I found information about the Gemma 3 12B model on Hugging Face. Here's what I found:

## Gemma 3 12B Base Model Overview

Gemma 3 is a family of lightweight, state-of-the-art open models from Google, and Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants.

Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions.

## Benchmark Performance

Using the benchmark evaluation metrics described in this document, these models have shown to provide superior performance to other, comparably-sized open model alternatives. However, the specific benchmark metrics and numerical results are not detailed in the search results.

The 12B model was trained with 12 trillion tokens.

## Repository Access

The Gemma 3 12B model repositories on Hugging Face include:
- **Instruction-tuned version**: google/gemma-3-12b-it
- **Pre-trained version**: google/gemma-3-12b-pt

To access Gemma on Hugging Face, you're required to review and agree to Google's usage license.

If you're looking for specific benchmark scores or detailed performance metrics for the base model, you may need to check the official Gemma 3 report or the model documentation directly on the Hugging Face repository pages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "66dc5a2b-ad99-481b-9a86-9912e48c1235"
}
```

</details>

---

### System

_source line 113_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Qwen 3 base model benchmark MMLU GSM8K HumanEval …",
  "usage": {
    "total_tokens": 22974,
    "tool_uses": 11,
    "duration_ms": 33519
  },
  "last_tool_name": "WebSearch",
  "uuid": "f2d94c5d-e227-452f-a46d-91786a5bdc47",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 114_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014593Y6jxxgjyp4yWsUXQ7R`</summary>

```json
{
  "query": "Qwen 3 base model benchmark MMLU GSM8K HumanEval scores 8B 14B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "e1491862-0782-4b4f-8c3e-3e47b514fc91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrniYZzyu6fTSwvHrr2aML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 998,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 19738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2213,
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

_source line 115 · 2026-05-18T07:08:14.599Z_

<details><summary>↩ Tool result · `toolu_01R5wGDapjWC3JZiKHh7nbe5`</summary>

```text
Web search results for query: "allenai/OLMo-2-1124-13B huggingface model card benchmark training data"

Links: [{"title":"allenai/OLMo-2-1124-13B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B"},{"title":"allenai/OLMo-2-1124-13B-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-GGUF"},{"title":"allenai/OLMo-2-1124-13B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct-GGUF"},{"title":"allenai/OLMo-2-1124-13B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct"},{"title":"allenai/OLMo-2-1124-13B-DPO-Preview · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-DPO-Preview"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"allenai/OLMo-2-1124-13B-RM · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-RM"},{"title":"allenai/OLMo-2-1124-13B-SFT · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-SFT"},{"title":"allenai/OLMo-2-1124-13B-DPO · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-DPO"},{"title":"allenai/OLMo-2-1124-13B · What Instruct Template? Recommended Temperature?","url":"https://huggingface.co/allenai/OLMo-2-1124-13B/discussions/3"}]

Based on the search results, I found comprehensive information about the allenai/OLMo-2-1124-13B model card from Hugging Face. Here's what I found:

## Model Overview
OLMo is a series of Open Language Models designed to enable the science of language models. These models are trained on the Dolma dataset.

## Training Data
OLMo 2 is a new family of 7B and 13B models featuring a 9-point increase in MMLU, among other evaluation improvements, compared to the original OLMo 7B model. These gains come from training on OLMo-mix-1124 and Dolmino-mix-1124 datasets and staged training approach.

## Benchmark Results
Core model results for OLMo 2 7B and 13B models are found below. The model card indicates that benchmark results are available, though the specific benchmark scores would be visible on the actual model card page.

## Licensing and Intent
OLMo 2 is licensed under the Apache 2.0 license. OLMo 2 is intended for research and educational use.

For the complete model card with detailed benchmark results and additional specifications, you can visit the model directly at: https://huggingface.co/allenai/OLMo-2-1124-13B


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "5c617f9f-7e86-4724-a788-22aac7c879d8"
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-18T07:08:15.407Z_

<details><summary>↩ Tool result · `toolu_01CkKiWfnh2V3QRabazuRRMP`</summary>

```text
Web search results for query: "Phi-4 base pretrained model not instruct HuggingFace microsoft 14B"

Links: [{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"Introducing Phi-4: Microsoft’s Newest Small Language Model Specializing in Complex Reasoning | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-phi-4-microsoft%E2%80%99s-newest-small-language-model-specializing-in-comple/4357090"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"Welcome to the new Phi-4 models - Microsoft Phi-4-mini & Phi-4-multimodal","url":"https://techcommunity.microsoft.com/blog/educatordeveloperblog/welcome-to-the-new-phi-4-models---microsoft-phi-4-mini--phi-4-multimodal/4386037"},{"title":"NyxKrage/Microsoft_Phi-4 · Hugging Face","url":"https://huggingface.co/NyxKrage/Microsoft_Phi-4"},{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"},{"title":"Phi-4 - a microsoft Collection","url":"https://huggingface.co/collections/microsoft/phi-4-677e9380e514feb5577a40e4"},{"title":"Microsoft makes powerful Phi-4 model fully open-source on Hugging Face | VentureBeat","url":"https://venturebeat.com/ai/microsoft-makes-powerful-phi-4-model-fully-open-source-on-hugging-face"}]

Based on the search results, here's what I found about the Phi-4 base pretrained model:

## Phi-4 Base Model Overview

Phi-4 is a 14B parameters, dense decoder-only transformer model. Phi-4 is available on Azure AI Foundry and on Hugging Face.

### Model Details

The training data is an extension of the data used for Phi-3 and includes a wide variety of sources from: Publicly available documents filtered rigorously for quality, selected high-quality educational data, and code. Newly created synthetic, "textbook-like" data for the purpose of teaching math, coding, common sense reasoning, general knowledge of the world (science, daily activities, theory of mind, etc.). Acquired academic books and Q&A datasets.

### Architecture & Context

The architecture consists of a standard decoder-only transformer with 14.7B parameters and 16K context, using ChatML chat template.

### Licensing

Phi-4 comes with a permissive MIT License, allowing it to be used for commercial applications.

### Key Capabilities

The models improve significantly from Phi-4, despite the post-training being focused on reasoning. The base model is designed for high-quality reasoning and complex problem-solving tasks.

You can find the official microsoft/phi-4 repository on HuggingFace for direct access to the base pretrained model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "26f13acf-1b76-4cac-9d5c-2b622f7d2ea1"
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-18T07:08:16.189Z_

<details><summary>↩ Tool result · `toolu_01JKRViMRvEi7fp8YmNYvPE4`</summary>

```text
Web search results for query: "DeepSeek V3 V2 small model 7B 14B 16B lite base 2025 2026 HuggingFace"

Links: [{"title":"DeepSeek Official Models List 2026 (V4, Flash, Pro) | DeepSeek V4 Network","url":"https://deepseekv4.network/models"},{"title":"DeepSeek Models Guide: R1, V3, and Coder | InsiderLLM","url":"https://insiderllm.com/guides/deepseek-models-guide/"},{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"},{"title":"GitHub - deepseek-ai/DeepSeek-V3 · GitHub","url":"https://github.com/deepseek-ai/deepseek-v3"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder-V2: DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder-V2"},{"title":"Ultimate Guide - The Best DeepSeek-AI Models in 2026","url":"https://www.siliconflow.com/articles/en/the-best-deepseek-ai-models-in-2025"},{"title":"DeepSeek-V3.2 Release | DeepSeek API Docs","url":"https://api-docs.deepseek.com/news/news251201"},{"title":"DeepSeek Models: V3.2, R1, Distills, and Production Caveats","url":"https://fireworks.ai/blog/deepseek-models"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-R1"},{"title":"DeepSeek - Wikipedia","url":"https://en.wikipedia.org/wiki/DeepSeek"}]

Based on the search results, here's a comprehensive overview of DeepSeek models including the versions and sizes you asked about:

## DeepSeek Model Family Overview

### V1 Series
V1 has a dense stack of 7B and 67B models with 4K context and ~2T tokens.

### V2 Series
V2 uses MoE architecture with 236B total parameters, ~21B active, 128K context, ~8T tokens. V2-Lite trims to ~16B total and ~2.4B active for smaller clusters.

### V3 Series
V3 MoE has 671B total parameters, ~37B active, 256 experts, ~14T tokens. In March 2025, DeepSeek released DeepSeek-V3-0324, which uses the same base model as DeepSeek-V3 but with improved post-training pipeline drawing lessons from the RL technique in DeepSeek-R1, allowing better reasoning performance, coding skills and tool-use capabilities.

### Small Models and Lite Versions
Lite and 16B MoE models are available for constrained deployments. DeepSeek-Coder-V2 comes in 16B and 236B parameter sizes based on the DeepSeekMoE framework, with activated parameters of 2.4B and 21B respectively.

### R1 Distilled Models
DeepSeek open-sourced distilled 1.5B, 7B, 8B, 14B, 32B, and 70B checkpoints based on Qwen2.5 and Llama3 series.

### V4 Series (2026)
In April 2026, DeepSeek released a preview of its V4 series, including the 1.6-trillion parameter DeepSeek-V4-Pro and the 284-billion parameter DeepSeek-V4-Flash, both featuring a 1-million token context window.

All these models are available on HuggingFace for community use and deployment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f02ce24f-9a6c-409b-8564-e3b717b208cd"
}
```

</details>

---

### System

_source line 118_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Mistral Small 3 7B base model huggingface release…",
  "usage": {
    "total_tokens": 24618,
    "tool_uses": 9,
    "duration_ms": 38247
  },
  "last_tool_name": "WebSearch",
  "uuid": "1d268c95-b7ab-476d-a465-a652940fb7bd",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 119_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YUVVB71nKv5cP15eC66Yy9`</summary>

```json
{
  "query": "Mistral Small 3 7B base model huggingface release date 2025 benchmark MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "a4ee4359-30d5-4e24-bde6-599dc46f678a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNPJ5LscWEEDyyDb2jdW9m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1646,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 20609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-18T07:08:17.006Z_

<details><summary>↩ Tool result · `toolu_01Qf8zamfsMpMEAyKasYqsoB`</summary>

```text
Web search results for query: "allenai/OLMo-2-1124-7B huggingface model card benchmark training tokens"

Links: [{"title":"allenai/OLMo-2-1124-7B-RM · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-RM"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"allenai/OLMo-2-1124-7B-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-GGUF"},{"title":"allenai/OLMo-2-1124-7B-RM-Preview · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-RM-Preview"},{"title":"allenai/OLMo-2-1124-13B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct-GGUF"},{"title":"allenai/OLMo-2-1124-7B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct"},{"title":"OLMo 2 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-2"},{"title":"allenai/OLMo-2-1124-7B-DPO · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-DPO"},{"title":"README.md · allenai/OLMo-2-1124-7B at 22fbf33a789d28264eb2f5511cda7dbc8338e976","url":"https://huggingface.co/allenai/OLMo-2-1124-7B/blame/22fbf33a789d28264eb2f5511cda7dbc8338e976/README.md"},{"title":"allenai/OLMo-2-1124-7B-DPO-Preview · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-DPO-Preview"}]

Now let me search for more specific information about training tokens for this model:

Links: [{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"OLMo-2-1124-7B","url":"https://www.promptlayer.com/models/olmo-2-1124-7b"},{"title":"GitHub - allenai/OLMo: Modeling, training, eval, and inference code for OLMo · GitHub","url":"https://github.com/allenai/OLMo"},{"title":"allenai/OLMo-2-1124-7B-Instruct Free Chat Online - skywork.ai - Skywork ai","url":"https://skywork.ai/blog/models/allenai-olmo-2-1124-7b-instruct-free-chat-online-skywork-ai/"},{"title":"Papers Explained 284: OLMo 2. OLMo 2 are dense autoregressive models… | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-olmo-2-f4d34e886503"},{"title":"allenai/OLMo-2-1124-13B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B"},{"title":"allenai/OLMo-2-1124-7B · Checkpoint pre training data","url":"https://huggingface.co/allenai/OLMo-2-1124-7B/discussions/7"},{"title":"allenai/OLMo-2-1124-7B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct"},{"title":"OLMo/README.md at main · allenai/OLMo","url":"https://github.com/allenai/OLMo/blob/main/README.md"},{"title":"OLMo | Prompt Engineering Guide&lt;!-- -->","url":"https://www.promptingguide.ai/models/olmo"}]

Based on the web search results, I found comprehensive information about the allenai/OLMo-2-1124-7B model. Here's what I found:

## Model Overview

OLMo 2 is a family of 7B and 13B models featuring a 9-point increase in MMLU, among other evaluation improvements, compared to the original OLMo 7B model.

## Training Tokens

OLMo 2 7B is trained for one epoch, up to 4T tokens, which represents the total pretraining budget. The training follows a sophisticated two-stage approach:

**Stage 1 (Pretraining):** OLMo-Mix-1124 dataset with 3.9T tokens covering 90%+ of total pretraining budget, with the 7B Model trained on ~1 epoch

**Stage 2 (Mid-training):** Dolmino-Mix-1124 with 843B tokens, with the 7B Model trained on 3 versions on a 50B token mix, merged via model souping

## Benchmark Results

Core model results for OLMo 2 7B and 13B models are provided on the model card, though specific benchmark numbers aren't detailed in the search results. The model has a date cutoff of December 2023.

## Training Data Sources

Gains come from training on OLMo-mix-1124 and Dolmino-mix-1124 datasets and staged training approach.

For more detailed benchmark results and training specifications, you can visit the official model card at https://huggingface.co/allenai/OLMo-2-1124-7B or the research paper at https://arxiv.org/abs/2501.00656.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "ef39ae67-09b4-4cbe-b6ef-b1c5e7dcba47"
}
```

</details>

---

### System

_source line 121_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for DeepSeek V2 V3 7B 14B base model huggingface dist…",
  "usage": {
    "total_tokens": 24663,
    "tool_uses": 10,
    "duration_ms": 39320
  },
  "last_tool_name": "WebSearch",
  "uuid": "1d859960-2e6b-4e77-a48c-b7609e0978a6",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 122_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C7Fe9WLPEiE62JR9v3UxUK`</summary>

```json
{
  "query": "DeepSeek V2 V3 7B 14B base model huggingface distilled 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "6a8a1211-f929-4a36-bcda-ed7161cdbf75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNPJ5LscWEEDyyDb2jdW9m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1646,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 20609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 123_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Qwen2.5 7B 14B base model huggingface benchmark t…",
  "usage": {
    "total_tokens": 24708,
    "tool_uses": 11,
    "duration_ms": 39656
  },
  "last_tool_name": "WebSearch",
  "uuid": "f407e76a-7327-4749-bbe7-3e6ccfcb6cb8",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 124_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BEXBM5kKmHtDWYvbzuaCNo`</summary>

```json
{
  "query": "Qwen2.5 7B 14B base model huggingface benchmark training tokens 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "cd530fe0-1303-4c5a-b4cc-868e6733658c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNPJ5LscWEEDyyDb2jdW9m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1646,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 20609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-18T07:08:18.505Z_

<details><summary>↩ Tool result · `toolu_015jTKT4ueZPtV6WDLNKS9A2`</summary>

```text
Web search results for query: "Ministral 3 8B base model HuggingFace repo "mistralai" parameters context length"

Links: [{"title":"mistralai/Ministral-3-8B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Base-2512"},{"title":"mistralai/Ministral-3-8B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512"},{"title":"mistralai/Ministral-3-8B-Reasoning-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Reasoning-2512"},{"title":"mistralai/Ministral-3-8B-Instruct-2512-BF16 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512-BF16"},{"title":"mistralai/Ministral-8B-Instruct-2410 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-8B-Instruct-2410"},{"title":"mistralai/Ministral-3-8B-Instruct-2512-GGUF · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512-GGUF"},{"title":"mistralai/Ministral-3-3B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-3B-Base-2512"},{"title":"Mistral · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/mistral"},{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"Mistral 3 Models on DigitalOcean | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/mistral-3-models"}]

Based on the search results, here is the information about the Ministral 3 8B base model from the mistralai HuggingFace repository:

## Model: mistralai/Ministral-3-8B-Base-2512

**Context Length:** The model supports a 256k context window.

**Model Size:** The Ministral 3 series is available in three model sizes: 3B, 8B, and 14B parameters.

**Architecture and Capabilities:** For each model size, base, instruct, and reasoning variants are released to the community, each with image understanding capabilities, all under the Apache 2.0 license.

**Hardware Requirements:** Due to their size and the BF16 format of their weights, Ministral-3-3B-Base-2512 and Ministral-3-8B-Base-2512 can run on a single 1xH200 GPU.

The repository is located at: **https://huggingface.co/mistralai/Ministral-3-8B-Base-2512**


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "84b0298f-cb27-4ccd-bb7b-5a0835b3a17d"
}
```

</details>

---

### System

_source line 126_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for OLMo 2 7B 13B base model huggingface 2025 release…",
  "usage": {
    "total_tokens": 24753,
    "tool_uses": 12,
    "duration_ms": 40171
  },
  "last_tool_name": "WebSearch",
  "uuid": "906a5a32-6ae6-4a05-89a6-8d2dce346166",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 127_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018hzzuzEY7t4QqDTYYBH7z2`</summary>

```json
{
  "query": "OLMo 2 7B 13B base model huggingface 2025 release Allen AI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "24f8f430-5ced-484e-80b5-98c60e9f2a2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNPJ5LscWEEDyyDb2jdW9m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1646,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 20609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-18T07:08:19.969Z_

<details><summary>↩ Tool result · `toolu_0128CbeLKSF3XU8Ykiyr6HFt`</summary>

```text
Web search results for query: "Qwen3-8B-Base parameters layers context length gated apache license"

Links: [{"title":"Qwen3 8B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-8b/"},{"title":"Qwen3.5-0.8B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/qwen3.5-0.8b"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"LICENSE · Qwen/Qwen3-8B at main","url":"https://huggingface.co/Qwen/Qwen3-8B/blob/main/LICENSE"},{"title":"Qwen Models Guide: 600M to 1 Trillion Parameters","url":"https://www.digitalapplied.com/blog/qwen-models-complete-guide"},{"title":"dengcao/Qwen3-8B","url":"https://ollama.com/dengcao/Qwen3-8B"},{"title":"Qwen/Qwen3-Next-80B-A3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct"},{"title":"Qwen/Qwen3-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B"},{"title":"Qwen3-8B-Base: Open 8B LLM Overview","url":"https://www.emergentmind.com/topics/qwen3-8b-base"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/qwen3"}]

Based on the search results, here's the information about Qwen3-8B-Base:

## Parameters and Architecture

Qwen3-8B is a dense transformer-based model with 8.2 billion parameters—6.95 billion of which are non-embedding parameters—spanning 36 layers.

The model has 32 attention heads for Query and 8 for Key/Value (GQA), with a context length of 32,768 tokens natively and 131,072 tokens with YaRN.

## Gated Attention

While the search results mention gated attention in a related model, Qwen3-Next-80B-A3B replaces standard attention with the combination of Gated DeltaNet and Gated Attention, enabling efficient context modeling for ultra-long context length. However, specific information about whether Qwen3-8B-Base itself uses gated attention mechanisms is not explicitly stated in these results.

## License

The Qwen3-8B-Base and other dense models are open-weighted under Apache 2.0 license.

## Context Length Details

Qwen3-8B-Base supports context lengths of up to 128,000 tokens via YARN and Dual-Chunk Attention in inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "320fc79a-7b56-4ae9-990c-1ca8610294cf"
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-18T07:08:20.029Z_

<details><summary>↩ Tool result · `toolu_01AiAnEdGJ4ZxTMc6Ve4j5Sj`</summary>

```text
Web search results for query: "Llama 4 Scout base pretrained non-instruct HuggingFace "meta-llama" gated license"

Links: [{"title":"meta-llama/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct"},{"title":"unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF"},{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"},{"title":"meta-llama/Llama-4-Scout-17B-16E · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E"},{"title":"unsloth/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct"},{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"meta-llama/Llama-4-Scout-17B-16E-Instruct at main","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct/tree/main"},{"title":"LLaMA 4 Explained - Everything You Need to Know","url":"https://www.labellerr.com/blog/llama-4/"},{"title":"Llama4 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/llama4"},{"title":"future-technologies/FineTuned-Meta-Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/future-technologies/FineTuned-Meta-Llama-4-Scout-17B-16E-Instruct"}]

Based on the search results, here's what I found about Llama 4 Scout:

## Model Overview

Llama 4, developed by Meta, introduces a new auto-regressive Mixture-of-Experts (MoE) architecture, with Llama 4 Scout having 17B active parameters out of ~109B total, using just 16 experts.

## Base (Non-Instruct) Model

The base pretrained variant is available at `meta-llama/Llama-4-Scout-17B-16E` on HuggingFace. Pretrained models can be adapted for natural language generation.

## Gated License

You need to accept the license terms on the model card before accessing the weights. These models are released under the custom Llama 4 Community License Agreement, which is available at: https://github.com/meta-llama/llama-models/blob/main/models/llama4/LICENSE.

## Training & Specifications

Llama 4 Scout was pretrained on ~40 trillion tokens of multimodal data from a mix of publicly available, licensed data and information from Meta's products and services. The pretraining data has a cutoff of August 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "59a97c37-fe45-452c-a957-1fa950afc0d7"
}
```

</details>

---

### System

_source line 130_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for microsoft/phi-4 HuggingFace benchmark MMLU traini…",
  "usage": {
    "total_tokens": 23066,
    "tool_uses": 8,
    "duration_ms": 34388
  },
  "last_tool_name": "WebSearch",
  "uuid": "91dcbd29-41c9-4011-a9ad-21c88789e0a2",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 131_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HwhzW91FS2ggAX9YTzTGaZ`</summary>

```json
{
  "query": "microsoft/phi-4 HuggingFace benchmark MMLU training data size tokens gated access"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "c27f27ef-bc25-4787-84a7-c7dc491441ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB9dg2TFQahhP1NChMjrUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 935,
      "cache_creation_input_tokens": 2182,
      "cache_read_input_tokens": 19927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2182,
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

_source line 132 · 2026-05-18T07:08:21.140Z_

<details><summary>↩ Tool result · `toolu_014593Y6jxxgjyp4yWsUXQ7R`</summary>

```text
Web search results for query: "Qwen 3 base model benchmark MMLU GSM8K HumanEval scores 8B 14B"

Links: [{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"AngelSlim/Qwen3-14B_eagle3 · Hugging Face","url":"https://huggingface.co/AngelSlim/Qwen3-14B_eagle3"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"},{"title":"AngelSlim/Qwen3-4B_eagle3 · Hugging Face","url":"https://huggingface.co/AngelSlim/Qwen3-4B_eagle3"},{"title":"Qwen3 8B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-8b/"},{"title":"Swallow LLM Leaderboard","url":"https://swallow-llm.github.io/leaderboard/about.en.html"},{"title":"Technical Report Qwen2.5-Coder Technical Report Binyuan Hui* Jian Yang*","url":"https://arxiv.org/pdf/2409.12186"},{"title":"Qwen Latest Model | Most Recent Release","url":"https://qwen.co.com/latest-model.html"},{"title":"Qwen2.5-LLM: Extending the boundary of LLMs | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-llm/"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v3"}]

I found comprehensive benchmark results for Qwen 3 base models. Here are the key scores you're looking for:

## Qwen3-8B Base Model Scores

For general tasks, Qwen3-8B achieves MMLU: 79.66. For math & STEM tasks, it scores GSM8K: 90.22. For coding tasks, it achieves EvalPlus: 60.70.

## Qwen3-14B Base Model Scores

Qwen3-14B-Base achieves MMLU: 81.05, GSM8K: 92.49, and for coding tasks achieves EvalPlus: 72.23.

## Additional Context

For comparison with smaller models, Qwen3-4B-Base achieves MMLU: 74.16, GSM8K: 85.36.

The search results from the official Qwen3 Technical Report show comprehensive benchmark evaluations, though HumanEval scores were not explicitly listed in the comparison tables. The models demonstrate strong performance, particularly in STEM, coding, and reasoning benchmarks, where Qwen3 dense base models surpass Qwen2.5 base models at higher parameter scales.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "0568cddd-ef0e-48a9-bb95-8bd677121e90"
}
```

</details>

---

### System

_source line 133_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for DeepSeek-R1-Distill-Qwen-14B DeepSeek-R1-Distill-…",
  "usage": {
    "total_tokens": 23067,
    "tool_uses": 9,
    "duration_ms": 35545
  },
  "last_tool_name": "WebSearch",
  "uuid": "30f1834f-8c4f-4bb4-b7d4-a334a6928b96",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 134_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WBntCuDtM4WNQSMmgyTAwg`</summary>

```json
{
  "query": "DeepSeek-R1-Distill-Qwen-14B DeepSeek-R1-Distill-Qwen-7B HuggingFace base model benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "8b992dd7-5e04-4f6b-8ac3-fda146cb9f6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB9dg2TFQahhP1NChMjrUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 935,
      "cache_creation_input_tokens": 2182,
      "cache_read_input_tokens": 19927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2182,
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

### System

_source line 135_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for DeepSeek-Coder-V2-Lite-Base 16B HuggingFace param…",
  "usage": {
    "total_tokens": 23068,
    "tool_uses": 10,
    "duration_ms": 35837
  },
  "last_tool_name": "WebSearch",
  "uuid": "0d2014d8-fc03-401c-819c-ea1b61fe827a",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 136_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014PsKTJdbUUVH9PhiPuTAHN`</summary>

```json
{
  "query": "DeepSeek-Coder-V2-Lite-Base 16B HuggingFace parameters MoE active benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "fb003938-011a-421c-abf0-851090ce9499",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB9dg2TFQahhP1NChMjrUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 935,
      "cache_creation_input_tokens": 2182,
      "cache_read_input_tokens": 19927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2182,
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

### System

_source line 137_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for OLMo 2 7B 13B benchmark MMLU HellaSwag ARC result…",
  "usage": {
    "total_tokens": 24780,
    "tool_uses": 9,
    "duration_ms": 39145
  },
  "last_tool_name": "WebSearch",
  "uuid": "84389697-75b1-47a0-896f-a46b66f01fe8",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 138_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L9K3boLWoic7ZF6XnQD18e`</summary>

```json
{
  "query": "OLMo 2 7B 13B benchmark MMLU HellaSwag ARC results comparison 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "831805ea-9006-44ad-945c-62eaf3309ea1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmrqQCT37mcbBwrisrvoHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1941,
      "cache_creation_input_tokens": 2974,
      "cache_read_input_tokens": 19842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2974,
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

### System

_source line 139_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for Gemma 3 benchmark results MMLU HellaSwag 1B 4B 12…",
  "usage": {
    "total_tokens": 24781,
    "tool_uses": 10,
    "duration_ms": 39620
  },
  "last_tool_name": "WebSearch",
  "uuid": "cd8534ab-6ab2-44ea-bba5-0c0e682d0ce5",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 140_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rd5X2LXzWEQErV5MAYnMo9`</summary>

```json
{
  "query": "Gemma 3 benchmark results MMLU HellaSwag 1B 4B 12B 27B training tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "62c6b597-43a9-4044-8b36-2941020cab06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmrqQCT37mcbBwrisrvoHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1941,
      "cache_creation_input_tokens": 2974,
      "cache_read_input_tokens": 19842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2974,
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

_source line 141 · 2026-05-18T07:08:23.158Z_

<details><summary>↩ Tool result · `toolu_01YUVVB71nKv5cP15eC66Yy9`</summary>

```text
Web search results for query: "Mistral Small 3 7B base model huggingface release date 2025 benchmark MMLU"

Links: [{"title":"Mistral 7B","url":"https://mistral.ai/news/announcing-mistral-7b"},{"title":"Mistral Small 3 | Mistral AI","url":"https://mistral.ai/news/mistral-small-3"},{"title":"unsloth/Mistral-Small-24B-Base-2501-bnb-4bit · Hugging Face","url":"https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501-bnb-4bit"},{"title":"mistralai/Mistral-7B-v0.1 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-7B-v0.1"},{"title":"Mistral Small 3.1 | Mistral AI","url":"https://mistral.ai/news/mistral-small-3-1"},{"title":"unsloth/Mistral-Small-24B-Base-2501 · Hugging Face","url":"https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501"},{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"mistralai/Mistral-Small-24B-Instruct-2501 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501"},{"title":"mistralai/Mistral-Small-3.1-24B-Instruct-2503 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503"},{"title":"Mistral Docs","url":"https://docs.mistral.ai/getting-started/models/benchmark/"}]

Based on the search results, here's what I found about Mistral Small 3:

**Model Details:**
Mistral Small 3 boasts 24B parameters and achieves state-of-the-art capabilities comparable to larger models. Note that the search results do not show a 7B version of Mistral Small 3 - the model has 24 billion parameters, not 7 billion.

**Release Date:**
The model was released in January 2025. The version labeled "2501" (indicating January 2025) is referenced in the HuggingFace documentation.

**MMLU Benchmark:**
Mistral Small 3 achieves over 81% accuracy on MMLU and 150 tokens/s latency, making it currently the most efficient model of its category.

**HuggingFace Availability:**
Mistral Small 3.1 is available to download on the HuggingFace website in both Base and Instruct versions.

It's worth noting that there's also a newer version - Mistral Small 3.1 (2503) builds upon Mistral Small 3 (2501) and adds state-of-the-art vision understanding and enhances long context capabilities up to 128k tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "38b9b3a1-1103-43b6-8f54-ed0b3a5d0e9f"
}
```

</details>

---

### System

_source line 142_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for OLMo 2 0325 32B base model huggingface release da…",
  "usage": {
    "total_tokens": 24782,
    "tool_uses": 11,
    "duration_ms": 40612
  },
  "last_tool_name": "WebSearch",
  "uuid": "2d854a06-5159-4442-aecc-bbc7414969f0",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 143_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XzXrM7tjzezJhhP3Wayksn`</summary>

```json
{
  "query": "OLMo 2 0325 32B base model huggingface release date 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f76b85fb-a0f1-44e8-9cfd-4e93e8c78d15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmrqQCT37mcbBwrisrvoHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1941,
      "cache_creation_input_tokens": 2974,
      "cache_read_input_tokens": 19842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2974,
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

### System

_source line 144_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for google/gemma-3-27b-pt pretrained base model train…",
  "usage": {
    "total_tokens": 24783,
    "tool_uses": 12,
    "duration_ms": 40967
  },
  "last_tool_name": "WebSearch",
  "uuid": "1bf24cbe-41db-45a7-8fcb-0e96bf6a4642",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 145_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LP3EdK4mPkxzx5GMr24a2z`</summary>

```json
{
  "query": "google/gemma-3-27b-pt pretrained base model training data tokens gated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "bf6fbf86-9098-45db-8c9b-141c2753d401",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmrqQCT37mcbBwrisrvoHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1941,
      "cache_creation_input_tokens": 2974,
      "cache_read_input_tokens": 19842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2974,
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

### System

_source line 146_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Ministral 3 14B base model HuggingFace \"mistralai…",
  "usage": {
    "total_tokens": 26708,
    "tool_uses": 12,
    "duration_ms": 43545
  },
  "last_tool_name": "WebSearch",
  "uuid": "98c07025-efea-4816-b559-cf8c4cbaa66d",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 147_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DJBT91jU4xnPuyxhJFV7LC`</summary>

```json
{
  "query": "Ministral 3 14B base model HuggingFace \"mistralai/Ministral-3-14B\" benchmark MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "405d2096-ae7e-4348-b805-5a06e372b531",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YXLiEW5Jk56rkaPeZu1zr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4673,
      "cache_read_input_tokens": 21951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4673,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
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

_source line 148_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Qwen3-14B-Base architecture layers attention head…",
  "usage": {
    "total_tokens": 26766,
    "tool_uses": 13,
    "duration_ms": 44530
  },
  "last_tool_name": "WebSearch",
  "uuid": "e5bb5bec-7ba4-4c75-90f9-5e43afe10367",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 149_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VhBCZ75HAZ5z8pq9XLatYb`</summary>

```json
{
  "query": "Qwen3-14B-Base architecture layers attention heads non-embedding parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "31d7c876-9d13-4d2c-9efc-c4ce978636be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YXLiEW5Jk56rkaPeZu1zr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4673,
      "cache_read_input_tokens": 21951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4673,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
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

_source line 150_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Llama 4 Maverick base pretrained HuggingFace \"met…",
  "usage": {
    "total_tokens": 26824,
    "tool_uses": 14,
    "duration_ms": 44941
  },
  "last_tool_name": "WebSearch",
  "uuid": "0aadc88e-988b-407f-a5ac-23eba8a5fe55",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 151_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ky7THd2G2skXgTZzGFecBK`</summary>

```json
{
  "query": "Llama 4 Maverick base pretrained HuggingFace \"meta-llama/Llama-4-Maverick\" non-instruct"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "217a2551-ff5c-4316-8b08-90d9a1d387f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YXLiEW5Jk56rkaPeZu1zr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4673,
      "cache_read_input_tokens": 21951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4673,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-18T07:08:26.022Z_

<details><summary>↩ Tool result · `toolu_01BEXBM5kKmHtDWYvbzuaCNo`</summary>

```text
Web search results for query: "Qwen2.5 7B 14B base model huggingface benchmark training tokens 2024 2025"

Links: [{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Qwen/Qwen2.5-7B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-7B-Instruct"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen/Qwen2.5-7B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-7B"},{"title":"Qwen/Qwen2.5-Coder-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Coder-14B"},{"title":"Qwen/Qwen2.5-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-14B"},{"title":"Qwen/Qwen2.5-Coder-14B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct"},{"title":"Qwen/Qwen2.5-14B-Instruct-1M · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M"},{"title":"Qwen/Qwen2.5-7B-Instruct-1M · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M"},{"title":"Qwen/Qwen2.5-14B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-14B-Instruct"}]

Based on the search results, here's information about Qwen2.5 7B and 14B base models:

## Model Overview

Qwen2.5 includes pre-trained and instruction-tuned models of 7 sizes, including 0.5B, 1.5B, 3B, 7B, 14B, 32B, and 72B.

## Training Tokens

The pre-training data increased from 7 trillion tokens to 18 trillion tokens, with focus on knowledge, coding, and mathematics. For the Qwen2.5-Coder variant, the training tokens were scaled up into 5.5 trillion including source code, text-code grounding, Synthetic data, etc.

## Benchmark Performance

For the 7B model, Qwen2.5-7B demonstrates significant improvements achieving 74.2 on MMLU, 49.8 on MATH, and 57.9 on coding tasks like HumanEval.

The Qwen2.5-7B model surpasses its predecessors and counterparts in numerous benchmarks, despite having fewer non-embedding parameters.

## Capabilities

Qwen2.5 exhibits competitive performance in instruction following, multilingual knowledge, and mathematical reasoning, aligning well with models of comparable size.

The models are available on Hugging Face for both base and instruction-tuned variants, with long-context support up to 128K tokens and ability to generate up to 8K tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "345b54ef-b5d2-451b-ac21-6d010923bb36"
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-18T07:08:26.333Z_

<details><summary>↩ Tool result · `toolu_01C7Fe9WLPEiE62JR9v3UxUK`</summary>

```text
Web search results for query: "DeepSeek V2 V3 7B 14B base model huggingface distilled 2025"

Links: [{"title":"deepseek-ai/DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-7B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"},{"title":"deepseek-ai/DeepSeek-V4-Pro · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-32B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"},{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"},{"title":"DeepSeek-V2 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/deepseek_v2"},{"title":"DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/deepseek_v3"},{"title":"DeepSeek-V3.2 Release | DeepSeek API Docs","url":"https://api-docs.deepseek.com/news/news251201"},{"title":"deepseek-ai/DeepSeek-R1 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1"},{"title":"deepseek-ai/DeepSeek-V3-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3-Base"}]

Based on the search results, here's what I found about DeepSeek models and their distilled variants on Hugging Face:

## DeepSeek-V3 Base Model

DeepSeek-V3 is a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2.

## Distilled Models (2025)

DeepSeek has open-sourced distilled 1.5B, 7B, 8B, 14B, 32B, and 70B checkpoints based on Qwen2.5 and Llama3 series to the community. 

Specifically, DeepSeek-R1-Distill-Qwen-1.5B, DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Qwen-14B and DeepSeek-R1-Distill-Qwen-32B are derived from Qwen-2.5 series, which are originally licensed under Apache 2.0 License, and now finetuned with 800k samples curated with DeepSeek-R1. DeepSeek-R1-Distill-Llama-8B is derived from Llama3.1-8B-Base and is originally licensed under llama3.1 license.

DeepSeek-R1-Zero & DeepSeek-R1 are trained based on DeepSeek-V3-Base.

All of these models are available on Hugging Face in the deepseek-ai organization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "b1c49772-7f7b-4ffd-ae57-0e888e098e81"
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-18T07:08:26.428Z_

<details><summary>↩ Tool result · `toolu_018hzzuzEY7t4QqDTYYBH7z2`</summary>

```text
Web search results for query: "OLMo 2 7B 13B base model huggingface 2025 release Allen AI"

Links: [{"title":"OLMo 2 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-2"},{"title":"allenai/OLMo-2-1124-13B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"allenai/OLMo-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-7B"},{"title":"OLMo 2: The best fully open language model to date | Ai2","url":"https://allenai.org/blog/olmo2"},{"title":"allenai/OLMo-2-1124-13B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct-GGUF"},{"title":"OLMo release notes | Ai2","url":"https://allenai.org/olmo/release-notes"},{"title":"allenai/OLMo-2-1124-7B-RM · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-RM"},{"title":"allenai/OLMo-2-0325-32B-SFT · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-SFT"},{"title":"allenai/Olmo-3-1025-7B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1025-7B"}]

Based on the search results, here's what I found about OLMo 2:

## OLMo 2 Release Overview

OLMo 2 is a new family of 7B and 13B models trained on up to 5T tokens. These models are on par with or better than equivalently-sized fully-open models, and competitive with open-weight models from Meta and Mistral on English academic benchmarks.

## Base Models on Hugging Face

The base models are available on Hugging Face:
- OLMo 2 7B base version is available for use as foundation for post-training.
- OLMo 2 13B base version is available for use as foundation for post-training.

## Training Details

OLMo 2 features a 9-point increase in MMLU compared to the original OLMo 7B model, with these gains coming from training on OLMo-mix-1124 and Dolmino-mix-1124 datasets and staged training approach.

## Performance

OLMo 2 7B outperforms LLama-3.1 8B and OLMo 2 13B outperforms Qwen 2.5 7B despite its lower total training FLOPs.

The models were released in late 2024 and are available on the Allen AI Hugging Face collection with various variants including instruct, quantized, and reward model versions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "16168af6-e7d6-49ba-a82d-8940b5d1e15b"
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-18T07:08:28.219Z_

<details><summary>↩ Tool result · `toolu_01HwhzW91FS2ggAX9YTzTGaZ`</summary>

```text
Web search results for query: "microsoft/phi-4 HuggingFace benchmark MMLU training data size tokens gated access"

Links: [{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"},{"title":"phi-4 | AI Model Details","url":"https://www.aimodels.fyi/models/huggingFace/phi-4-microsoft"},{"title":"GitHub - microsoft/MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark [Official, ACL 2025] · GitHub","url":"https://github.com/microsoft/MMLU-CF"},{"title":"microsoft/Phi-4-multimodal-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-multimodal-instruct"},{"title":"Microsoft AI Just Released Phi-4: A Small Language Model Available on Hugging Face Under the MIT License - MarkTechPost","url":"https://www.marktechpost.com/2025/01/08/microsoft-ai-just-fully-open-sourced-phi-4-a-small-language-model-available-on-hugging-face-under-the-mit-license/"},{"title":"Phi-4: Small Language Models That Pack a Punch | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/educatordeveloperblog/phi-4-small-language-models-that-pack-a-punch/4464167"},{"title":"microsoft/phi-4-gguf · Hugging Face","url":"https://huggingface.co/microsoft/phi-4-gguf"}]

Based on the search results, here's what I found about microsoft/phi-4 on HuggingFace:

## MMLU Benchmark Performance
Phi-4 scores 84.8% on MMLU (a broad test of knowledge across 57 subjects), and achieved 84.8% on MMLU, 80.4% on MATH, and 82.6% on HumanEval.

## Training Data Size
Microsoft trained it on 9.8 trillion tokens over three weeks, using a mix of synthetic data (generated by larger models like GPT-4o) and high-quality web content.

## Model Architecture
Phi-4 represents Microsoft's latest advancement in language modeling, featuring 14B parameters and a 16K token context length.

## Training Sources
The training data is an extension of the data used for Phi-3 and includes publicly available documents filtered rigorously for quality, selected high-quality educational data and code, newly created synthetic "textbook-like" data for teaching math, coding, common sense reasoning and general knowledge, acquired academic books and Q&A datasets, and high quality chat format supervised data covering various topics.

## Gated Access
The model is available on HuggingFace under the MIT license with open access - Phi-4 is hosted on Hugging Face under the MIT license, so it does not appear to have gated access restrictions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "145a069e-4112-44f9-b04c-1b8572aedc78"
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-18T07:08:28.230Z_

<details><summary>↩ Tool result · `toolu_01WBntCuDtM4WNQSMmgyTAwg`</summary>

```text
Web search results for query: "DeepSeek-R1-Distill-Qwen-14B DeepSeek-R1-Distill-Qwen-7B HuggingFace base model benchmark"

Links: [{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-14B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-7B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-32B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"},{"title":"litert-community/DeepSeek-R1-Distill-Qwen-1.5B · Hugging Face","url":"https://huggingface.co/litert-community/DeepSeek-R1-Distill-Qwen-1.5B"},{"title":"unsloth/DeepSeek-R1-Distill-Qwen-14B · Hugging Face","url":"https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-14B"},{"title":"Mungert/DeepSeek-R1-Distill-Qwen-14B-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/DeepSeek-R1-Distill-Qwen-14B-GGUF"},{"title":"stelterlab/DeepSeek-R1-Distill-Qwen-14B-AWQ · Hugging Face","url":"https://huggingface.co/stelterlab/DeepSeek-R1-Distill-Qwen-14B-AWQ"},{"title":"deepseek-ai/DeepSeek-R1 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1"},{"title":"unsloth/DeepSeek-R1-Distill-Qwen-32B · Hugging Face","url":"https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-32B"}]

Based on the search results, here's what I found about the DeepSeek-R1-Distill-Qwen models on HuggingFace:

## Model Overview

DeepSeek has open-sourced distilled 1.5B, 7B, 8B, 14B, 32B, and 70B checkpoints based on Qwen2.5 and Llama3 series.

## Benchmark Performance

The evaluation results demonstrate that the distilled smaller dense models perform exceptionally well on benchmarks. DeepSeek-R1-Distill-Qwen-32B outperforms OpenAI-o1-mini across various benchmarks, achieving new state-of-the-art results for dense models.

## Model Development

DeepSeek-R1-Distill models are fine-tuned based on open-source models, using samples generated by DeepSeek-R1. Specifically, DeepSeek-R1-Distill-Qwen-1.5B, DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Qwen-14B and DeepSeek-R1-Distill-Qwen-32B are derived from Qwen-2.5 series, which are originally licensed under Apache 2.0 License, and now finetuned with 800k samples curated with DeepSeek-R1.

## Evaluation Settings

For benchmarks requiring sampling, they use a temperature of 0.6, a top-p value of 0.95, and generate 64 responses per query to estimate pass@1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "3b2fc2a8-b4a1-44e9-89e3-43274734a892"
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-18T07:08:29.516Z_

<details><summary>↩ Tool result · `toolu_014PsKTJdbUUVH9PhiPuTAHN`</summary>

```text
Web search results for query: "DeepSeek-Coder-V2-Lite-Base 16B HuggingFace parameters MoE active benchmark"

Links: [{"title":"deepseek-ai/DeepSeek-Coder-V2-Lite-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Base"},{"title":"deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"},{"title":"DeepSeek-Coder V2 Lite Instruct","url":"https://www.emergentmind.com/topics/deepseek-coder-v2-lite-instruct"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder-V2: DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder-V2"},{"title":"deepseek-ai/DeepSeek-V2-Lite · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite"},{"title":"deepseek-ai/deepseek-coder-v2-lite-instruct | Run with an API on Replicate","url":"https://replicate.com/deepseek-ai/deepseek-coder-v2-lite-instruct"},{"title":"deepseek-coder-v2:16b-lite-instruct-fp16","url":"https://ollama.com/library/deepseek-coder-v2:16b-lite-instruct-fp16"},{"title":"DeepSeek-Coder-V2: An Open-Source Marvel in Code Intelligence | by givkashi | Medium","url":"https://medium.com/@givkashi/deepseek-coder-v2-an-open-source-marvel-in-code-intelligence-e8572f7741e0"},{"title":"Model Variants | deepseek-ai/DeepSeek-Coder-V2 | DeepWiki","url":"https://deepwiki.com/deepseek-ai/DeepSeek-Coder-V2/2.1-model-variants"},{"title":"deepseek-coder-v2:16b","url":"https://ollama.com/library/deepseek-coder-v2:16b"}]

Based on the search results, here's the information about DeepSeek-Coder-V2-Lite-Base 16B parameters and MoE active parameters:

## Parameters and MoE Configuration

DeepSeek-Coder-V2-Lite-Base has 16B parameters based on the DeepSeekMoE framework, with only 2.4B active parameters. 

This means that for any given input, the model routes the computation through only about 15% of its total parameters (for Lite variants).

## Model Architecture Details

For the Lite variant specifically, each MoE layer consists of 2 shared experts and 64 routed experts, where 6 experts will be activated for each token, resulting in 15.7B total parameters with 2.4B activated for each token.

## Benchmark Performance

In standard benchmark evaluations, DeepSeek-Coder-V2 achieves superior performance compared to closed-source models such as GPT4-Turbo, Claude 3 Opus, and Gemini. Additionally, the full-sized models consistently outperform the Lite variants across all benchmarks, with the full DeepSeek-Coder-V2-Instruct model competing with or exceeding the performance of GPT-4-Turbo on many code and mathematical reasoning tasks.

The model is available on HuggingFace at the official DeepSeek-AI repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "50852bda-fa70-41cc-a113-f384e34cf2c2"
}
```

</details>

---

### System

_source line 158_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Qwen3 8B base benchmark MMLU ARC HellaSwag scores…",
  "usage": {
    "total_tokens": 28848,
    "tool_uses": 13,
    "duration_ms": 51097
  },
  "last_tool_name": "WebSearch",
  "uuid": "e0a55e47-ace3-4cb0-a456-1222cf2f0d70",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 159_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MpHfia2WRFeUQy4wHja4aT`</summary>

```json
{
  "query": "Qwen3 8B base benchmark MMLU ARC HellaSwag scores 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "7700b55f-8397-4e8d-8425-866a5d9edfd1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114AWbUGQKLmWDBLHRjt7Kt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 22906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5698,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-18T07:08:29.657Z_

<details><summary>↩ Tool result · `toolu_01XzXrM7tjzezJhhP3Wayksn`</summary>

```text
Web search results for query: "OLMo 2 0325 32B base model huggingface release date 2025"

Links: [{"title":"allenai/OLMo-2-0325-32B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct"},{"title":"allenai/OLMo-2-0325-32B-SFT · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-SFT"},{"title":"allenai/OLMo-2-0325-32B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B"},{"title":"allenai/OLMo-2-0325-32B-DPO · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-DPO"},{"title":"OLMo release notes | Ai2","url":"https://allenai.org/olmo/release-notes"},{"title":"allenai/Olmo-3-1125-32B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1125-32B"},{"title":"allenai/Olmo-3.1-32B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-32B-Think"},{"title":"allenai/OLMo-2-0325-32B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct-GGUF"},{"title":"OLMo-2-0325-32B huggingface.co api & allenai OLMo-2-0325-32B github AI Model - Toolify","url":"https://www.toolify.ai/ai-model/allenai-olmo-2-0325-32b"},{"title":"unsloth/OLMo-2-0325-32B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/OLMo-2-0325-32B-Instruct-GGUF"}]

Based on the search results, here's what I found about the OLMo 2 0325 32B base model on Hugging Face:

The OLMo-2-0325-32B base model was released on November 26, 2024. However, the model was last updated on March 26, 2025.

The search results show that OLMo 2 32B is the largest model in the OLMo 2 family, scaling up the OLMo 2 training recipe used for the 7B and 13B models released in November. Trained up to 6T tokens and post-trained using Tulu 3.1, it is the first fully-open model to outperform GPT3.5-Turbo and GPT-4o mini on a suite of popular, multi-skill academic benchmarks.

The model is available on Hugging Face under the repository name `allenai/OLMo-2-0325-32B`.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "2182233c-cb6f-471c-b8b6-6717d86816fe"
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-18T07:08:30.412Z_

<details><summary>↩ Tool result · `toolu_01VhBCZ75HAZ5z8pq9XLatYb`</summary>

```text
Web search results for query: "Qwen3-14B-Base architecture layers attention heads non-embedding parameters"

Links: [{"title":"Qwen/Qwen3-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B"},{"title":"Qwen3 14B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-14b/"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"Qwen/Qwen3-14B-Base Free Chat Online - skywork.ai - Skywork ai","url":"https://skywork.ai/blog/models/qwen-qwen3-14b-base-free-chat-online-skywork-ai/"},{"title":"unsloth/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/unsloth/Qwen3-14B-Base"},{"title":"Qwen3 14B Base API | Together AI","url":"https://www.together.ai/models/qwen3-14b-base"},{"title":"Qwen3-14B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/qwen3-14b"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Unpacking Qwen 3: Architecture, Capabilities, and Performance | by Erik Milošević | Towards AGI | Medium","url":"https://medium.com/towards-agi/unpacking-qwen-3-architecture-capabilities-and-performance-a87f6b317f72"},{"title":"Qwen/Qwen3-14B - Demo - DeepInfra","url":"https://deepinfra.com/Qwen/Qwen3-14B"}]

Based on the search results, here are the architecture specifications for **Qwen3-14B-Base**:

**Architecture Layers & Attention:**
- Number of Layers: 40
- Number of Attention Heads (GQA): 40 for Q and 8 for KV

**Parameter Details:**
- Total Number of Parameters: 14.8B
- Non-Embedding Parameters: 13.2B

**Additional Architectural Features:**
- The model employs a dense, causal transformer architecture with grouped query attention (GQA)
- The model employs SwiGLU activation functions and RMSNorm with pre-normalization for enhanced training stability
- Context Length: 32,768


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "c747e4d6-f042-4883-beb3-cd080724ec58"
}
```

</details>

---

### System

_source line 162_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Gemma 3 12B base pretrained benchmark scores MMLU…",
  "usage": {
    "total_tokens": 28890,
    "tool_uses": 14,
    "duration_ms": 52029
  },
  "last_tool_name": "WebSearch",
  "uuid": "eaff84a7-3e1a-498f-882d-50cfba40badb",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 163_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WXvDfUz4XiJ4CMQJ8m4QtY`</summary>

```json
{
  "query": "Gemma 3 12B base pretrained benchmark scores MMLU 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f626d3ed-da2c-4b1e-9172-6e4c55fb9d4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114AWbUGQKLmWDBLHRjt7Kt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 22906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5698,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-18T07:08:30.642Z_

<details><summary>↩ Tool result · `toolu_01Rd5X2LXzWEQErV5MAYnMo9`</summary>

```text
Web search results for query: "Gemma 3 benchmark results MMLU HellaSwag 1B 4B 12B 27B training tokens"

Links: [{"title":"Gemma 3 Technical Report","url":"https://arxiv.org/html/2503.19786v1"},{"title":"Gemma 3 model card | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/model_card_3"},{"title":"Gemma 3 Model: Multimodal & Efficient LLM","url":"https://www.emergentmind.com/topics/gemma-3-model"},{"title":"(PDF) Gemma 3 Technical Report","url":"https://www.researchgate.net/publication/390175982_Gemma_3_Technical_Report"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"GitHub - heilcheng/openevals: Benchmarking suite for open-weight language models · GitHub","url":"https://github.com/heilcheng/gemma-benchmark"},{"title":"Google's Gemma 3: Features, Benchmarks, Performance and Implementation","url":"https://www.analyticsvidhya.com/blog/2025/03/gemma-3/"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"Gemma 3 27B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/gemma-3-27b"},{"title":"Gemma 3 12B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/gemma-3-12b"}]

Based on the search results, here's comprehensive information about Gemma 3 benchmark results:

## Training Tokens

The 27B model was trained with 14 trillion tokens, the 12B model was trained with 12 trillion tokens, 4B model was trained with 4 trillion tokens, the 1B with 2 trillion tokens, and the 270M with 6 trillion tokens.

## HellaSwag Benchmark Results

For HellaSwag, the Gemma 3 models achieved the following scores: 1B: 62.3, 4B: 77.2, 12B: 84.2, and 27B: 85.6

## MMLU Benchmark Results

For MMLU-Pro specifically, Gemma 3-27B-IT yields 67.5% versus Gemini 2.0-Pro's 79.1% and Gemma 2-27B-IT's 56.9%

## Overall Performance

The Gemma 3 models are trained with distillation and achieve superior performance to Gemma 2 for both pre-trained and instruction finetuned versions. In particular, the novel post-training recipe significantly improves math, chat, instruction-following and multilingual abilities, making Gemma3-4B-IT competitive with Gemma2-27B-IT and Gemma3-27B-IT comparable to Gemini-1.5-Pro across benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "52b6785e-f30d-4fdb-a0d2-fda8c74cbf0e"
}
```

</details>

---

### System

_source line 165_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Llama 3.3 8B base model huggingface release 2024 …",
  "usage": {
    "total_tokens": 28932,
    "tool_uses": 15,
    "duration_ms": 52504
  },
  "last_tool_name": "WebSearch",
  "uuid": "398835ed-ed5b-49fc-b4f9-2fb9cceaa0ff",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 166_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xa8pxNSg9F2NoK2gFojeKR`</summary>

```json
{
  "query": "Llama 3.3 8B base model huggingface release 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "ecf0f50f-a483-4f40-9258-e92aadbd5ce1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114AWbUGQKLmWDBLHRjt7Kt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 22906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5698,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-18T07:08:31.230Z_

<details><summary>↩ Tool result · `toolu_01DJBT91jU4xnPuyxhJFV7LC`</summary>

```text
Web search results for query: "Ministral 3 14B base model HuggingFace "mistralai/Ministral-3-14B" benchmark MMLU"

Links: [{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"},{"title":"mistralai/Ministral-3-14B-Reasoning-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Reasoning-2512"},{"title":"mistralai / ministral-14b-instruct-2512","url":"https://docs.api.nvidia.com/nim/reference/mistralai-ministral-14b-instruct-2512"},{"title":"mistralai/Ministral-3-14B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512"},{"title":"unsloth/Ministral-3-14B-Reasoning-2512-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Ministral-3-14B-Reasoning-2512-GGUF"},{"title":"README.md · mistralai/Ministral-3-14B-Base-2512 at main","url":"https://huggingface.co/mistralai/Ministral-3-14B-Base-2512/blob/main/README.md"},{"title":"RedHatAI/Ministral-3-14B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/RedHatAI/Ministral-3-14B-Instruct-2512"},{"title":"mistralai/Ministral-3-14B-Instruct-2512-BF16 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512-BF16"},{"title":"unsloth/Ministral-3-14B-Base-2512 · Hugging Face","url":"https://huggingface.co/unsloth/Ministral-3-14B-Base-2512"},{"title":"mistralai/Ministral-3-14B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Base-2512"}]

Based on the web search results, here's information about the Ministral 3 14B base model and its MMLU benchmark performance:

## Model Overview
The largest model in the Ministral 3 family, Ministral 3 14B offers frontier capabilities and performance comparable to its larger Mistral Small 3.2 24B counterpart, and is a powerful and efficient language model with vision capabilities.

## MMLU Benchmark
The model was evaluated on MMLU and MMLU-Redux benchmarks as part of comprehensive evaluation efforts. The research paper indicates that results are reported after running evaluations using internal harness with identical configuration, with MMLU-Redux being one of the key metrics tracked.

## Model Availability
The base model is available on HuggingFace at `mistralai/Ministral-3-14B-Base-2512`. To fully exploit the Ministral-3-14B-Base-2512, using 2xH200 GPUs is recommended for deployment due to its large context, though a single GPU can be used if large context is not needed.

For detailed benchmark scores and specific MMLU-Redux results, the official research paper and model card on HuggingFace contain comprehensive evaluation tables with comparisons against other models like Gemma and Qwen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "385ff770-c084-4706-a5ca-7d245041a468"
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-18T07:08:31.816Z_

<details><summary>↩ Tool result · `toolu_01LP3EdK4mPkxzx5GMr24a2z`</summary>

```text
Web search results for query: "google/gemma-3-27b-pt pretrained base model training data tokens gated"

Links: [{"title":"google/gemma-3-27b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-it"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-27b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-pt"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"eramax/gemma-3-27b-it-qat:q4_0","url":"https://ollama.com/eramax/gemma-3-27b-it-qat:q4_0"},{"title":"Gemma 3 model card | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/model_card_3"},{"title":"eramax/gemma-3-27b-it-qat","url":"https://ollama.com/eramax/gemma-3-27b-it-qat"},{"title":"Full Model Fine-Tune using Hugging Face Transformers | Gemma | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/huggingface_text_full_finetune"},{"title":"google/gemma-3-1b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-1b-pt"},{"title":"google/gemma-3-27b • LM Studio","url":"https://lmstudio.ai/models/google/gemma-3-27b"}]

Based on the search results, here's the information about the google/gemma-3-27b-pt pretrained base model:

## Training Data Tokens

The 27B model was trained with 14 trillion tokens.

## Gated Access

To access Gemma on Hugging Face, you're required to review and agree to Google's usage license. To do this, please ensure you're logged in to Hugging Face and click below. Requests are processed immediately.

## Model Details

Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants. Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions.

The model was trained on a diverse dataset including web documents with a diverse collection of web text that ensures the model is exposed to a broad range of linguistic styles, topics, and vocabulary. The training dataset includes content in over 140 languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "d7cf8900-4c4a-4a9e-9451-e56058b4a049"
}
```

</details>

---

### System

_source line 169_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Falcon 3 7B 10B base model huggingface 2024 2025 …",
  "usage": {
    "total_tokens": 28974,
    "tool_uses": 16,
    "duration_ms": 53441
  },
  "last_tool_name": "WebSearch",
  "uuid": "8ac2c445-cd66-4c12-8443-00718956aa48",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 170_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011MS5A9Ji6Wabu5HpP6mQPR`</summary>

```json
{
  "query": "Falcon 3 7B 10B base model huggingface 2024 2025 TII"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "92b8a650-062c-480c-be76-e2af2288f7b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114AWbUGQKLmWDBLHRjt7Kt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 22906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5698,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-18T07:08:32.083Z_

<details><summary>↩ Tool result · `toolu_01L9K3boLWoic7ZF6XnQD18e`</summary>

```text
Web search results for query: "OLMo 2 7B 13B benchmark MMLU HellaSwag ARC results comparison 2025"

Links: [{"title":"OLMo 2: Advancing True Open-Source Language Models – The AI Observer","url":"https://www.theaiobserver.com/olmo-2-advancing-true-open-source-language-models/"},{"title":"OLMo 2: The best fully open language model to date | Ai2","url":"https://allenai.org/blog/olmo2"},{"title":"2 OLMo 2 Furious OLMo Team Pete Walsh 1 Luca Soldaini 1 Dirk Groeneveld 1","url":"https://arxiv.org/pdf/2501.00656"},{"title":"Comparative Analysis of Mistral 7B and OLMo2 7B on the Ollama Platform","url":"https://matasoft.hr/qtrendcontrol/index.php/un-perplexed-spready/un-perplexed-spready-various-articles/146-comparative-analysis-of-mistral-7b-and-olmo2-7b-on-the-ollama-platform"},{"title":"OLMo release notes | Ai2","url":"https://allenai.org/olmo/release-notes"},{"title":"OLMo-2-1124-13B & 7B · Issue #7863 · ollama/ollama","url":"https://github.com/ollama/ollama/issues/7863"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"OLMo 1.7–7B: A 24 point improvement on MMLU | Ai2","url":"https://allenai.org/blog/olmo-1-7-7b-a-24-point-improvement-on-mmlu-92b43f7d269d"},{"title":"HellaSwag Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/hellaswag"},{"title":"GitHub - heilcheng/openevals: Benchmarking suite for open-weight language models · GitHub","url":"https://github.com/heilcheng/gemma-benchmark"}]

Based on the web search results, here's what I found about OLMo 2 benchmark results for MMLU, HellaSwag, and ARC:

## OLMo 2 Benchmark Results

### MMLU Performance
OLMo 2 achieved 63.7 for the 7B model and 67.5 for the 13B model on MMLU. OLMo 2 features a 9-point increase in MMLU compared to the original OLMo 7B model.

### General Performance Comparison
The 7B version of OLMo 2 notably outperforms Meta's Llama 3.1 8B on several English academic benchmarks, while the 13B version surpasses Qwen 2.5 7B, despite utilizing fewer training FLOPs.

### Evaluation Benchmarks
OLMo 2 was evaluated on development benchmarks including ARC Challenge, HellaSwag, WinoGrande, MMLU, DROP, and Natural Questions, though the search results don't provide the specific numerical scores for HellaSwag and ARC Challenge.

### Training Approach
OLMo 2 was trained on up to 5 trillion tokens, incorporating innovative techniques in training stability, staged learning, and post-training methodologies.

For detailed benchmark comparisons across all three metrics you mentioned (MMLU, HellaSwag, and ARC), I'd recommend checking the official Ai2 technical report or their Hugging Face model card, which may contain more comprehensive benchmark tables.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "e47a1dde-86ce-48f4-a90a-b73a1de415a0"
}
```

</details>

---

### System

_source line 172_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for InternLM3 8B base model huggingface 2025 Shanghai…",
  "usage": {
    "total_tokens": 29016,
    "tool_uses": 17,
    "duration_ms": 53716
  },
  "last_tool_name": "WebSearch",
  "uuid": "21ab97bf-e6de-4418-bc22-154f6c5a3443",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 173_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K1z6xz2rXfA93LvH4PakR9`</summary>

```json
{
  "query": "InternLM3 8B base model huggingface 2025 Shanghai AI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "5d37c9dc-a375-46ef-8184-b72f25a697ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114AWbUGQKLmWDBLHRjt7Kt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 22906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5698,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-18T07:08:33.261Z_

<details><summary>↩ Tool result · `toolu_01Ky7THd2G2skXgTZzGFecBK`</summary>

```text
Web search results for query: "Llama 4 Maverick base pretrained HuggingFace "meta-llama/Llama-4-Maverick" non-instruct"

Links: [{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Original · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Original"},{"title":"unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF"},{"title":"meta-llama/Llama-4-Maverick-17B-128E · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"},{"title":"RedHatAI/Llama-4-Maverick-17B-128E-Instruct · Hugging Face","url":"https://huggingface.co/RedHatAI/Llama-4-Maverick-17B-128E-Instruct"},{"title":"future-technologies/FineTuned-Meta-Llama-4-Maverick-17B-128E-Instruct · Hugging Face","url":"https://huggingface.co/future-technologies/FineTuned-Meta-Llama-4-Maverick-17B-128E-Instruct"},{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"}]

Based on the search results, here's what I found about the Llama 4 Maverick base pretrained model on HuggingFace:

## Model Details

Llama 4 Maverick is a 17 billion parameter model with 128 experts. The model is available on HuggingFace under the meta-llama organization.

## Available Variants

Both Llama 4 Maverick and Llama 4 Scout model weights are available directly on the Hugging Face Hub under the meta-llama organization, including both base and instruction tuned variants.

The base/pretrained models (non-instruct) available are:
- **meta-llama/Llama-4-Maverick-17B-128E** (transformers format)
- **meta-llama/Llama-4-Maverick-17B-128E-Original** (original Meta format)

## Pretraining Details

Llama 4 Maverick was pretrained on ~22 trillion tokens of multimodal data from a mix of publicly available, licensed data and information from Meta's products and services. The pretraining data has a cutoff of August 2024.

## Architecture

Pretrained models can be adapted for natural language generation, and the Llama 4 models are auto-regressive language models that use a mixture-of-experts (MoE) architecture and support languages including Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "0f47c0ab-9c72-4fc9-9a4c-b1d4547b98b2"
}
```

</details>

---

### System

_source line 175_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for DeepSeek-R1-Distill-Qwen-14B benchmark MMLU MATH …",
  "usage": {
    "total_tokens": 26425,
    "tool_uses": 11,
    "duration_ms": 48633
  },
  "last_tool_name": "WebSearch",
  "uuid": "1eb114a2-c095-4bdd-8405-c28414dc0b49",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 176_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tr51pgpA5SvebdBXNEf7em`</summary>

```json
{
  "query": "DeepSeek-R1-Distill-Qwen-14B benchmark MMLU MATH AIME pass@1 scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "681bef2b-98a5-4a13-88b0-55a2c9a643f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MaZ6XxEVW2ZS7NBuyWRTsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 22109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4289,
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

### System

_source line 177_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Phi-4 mini 3.8B base pretrained model HuggingFace…",
  "usage": {
    "total_tokens": 26426,
    "tool_uses": 12,
    "duration_ms": 49597
  },
  "last_tool_name": "WebSearch",
  "uuid": "74212335-fba0-4623-9d23-ad49b4af3e8e",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 178_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RkknRkQyGS8BttodDkMAzn`</summary>

```json
{
  "query": "Phi-4 mini 3.8B base pretrained model HuggingFace release date benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "5241baa7-6448-4c25-9e3b-d98fca2b0052",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MaZ6XxEVW2ZS7NBuyWRTsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 22109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4289,
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

### System

_source line 179_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for OLMo 2 7B 13B MMLU ARC HellaSwag exact scores tab…",
  "usage": {
    "total_tokens": 28593,
    "tool_uses": 13,
    "duration_ms": 53063
  },
  "last_tool_name": "WebSearch",
  "uuid": "949430e5-5ed7-419b-ab2a-b8922025a9f5",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 180_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JiKSAWsvD6P8BdGqskQtpu`</summary>

```json
{
  "query": "OLMo 2 7B 13B MMLU ARC HellaSwag exact scores table arxiv 2501.00656"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "a567433b-5922-4ae0-90f1-68abe6d4d534",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoFvf4XqVno2Pf2ApiggxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2508,
      "cache_creation_input_tokens": 3235,
      "cache_read_input_tokens": 22816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3235,
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

_source line 181 · 2026-05-18T07:08:36.138Z_

<details><summary>↩ Tool result · `toolu_01MpHfia2WRFeUQy4wHja4aT`</summary>

```text
Web search results for query: "Qwen3 8B base benchmark MMLU ARC HellaSwag scores 2025"

Links: [{"title":"An Empirical Study of Qwen3 Quantization","url":"https://arxiv.org/html/2505.02214v1"},{"title":"An empirical study of Qwen3 quantization | Visual Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44267-026-00114-4"},{"title":"eaddario/Qwen3-8B-GGUF · Hugging Face","url":"https://huggingface.co/eaddario/Qwen3-8B-GGUF"},{"title":"Swallow LLM Leaderboard","url":"https://swallow-llm.github.io/leaderboard/about.en.html"},{"title":"Top LLM Benchmarks Explained: MMLU, HellaSwag, BBH, and Beyond - Confident AI","url":"https://www.confident-ai.com/blog/llm-benchmarks-mmlu-hellaswag-and-beyond"},{"title":"LLM Benchmarks Compared: MMLU, HumanEval, GSM8K and More (2026)","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"We Benchmarked 12 Small Language Models Across 8 Tasks to Find the Best Base Model for Fine-Tuning — distil labs","url":"https://www.distillabs.ai/blog/we-benchmarked-12-small-language-models-across-8-tasks-to-find-the-best-base-model-for-fine-tuning/"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"Qwen3 8B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/qwen3-8b-instruct"},{"title":"LLM Benchmark Wars 2025–2026: Performance, Cost, Speed, and Value | RankSaga","url":"https://ranksaga.com/blog/llm-benchmark-wars-2025-2026/"}]

Based on the search results, I found relevant benchmark information about Qwen3-8B-Base. Here's what I found:

Qwen-8B's MMLU score is 74.7 in its full precision form, though this appears to be from a quantization study focused on performance degradation at lower bit widths.

The search results include detailed benchmark data from an empirical study of Qwen3 quantization published in early 2025. Zero-shot accuracy is evaluated across reasoning benchmarks including ARC-Easy, ARC-Challenge, and HellaSwag, with 5-shot MMLU also examined. However, the specific individual scores for MMLU, ARC, and HellaSwag for the Qwen3-8B-Base model are referenced in tables within the research paper but not fully extracted in the search results provided.

For more complete and specific benchmark scores for Qwen3-8B-Base across MMLU, ARC, and HellaSwag, you would want to access the full research paper directly at the ArXiv link (https://arxiv.org/html/2505.02214v1), where Table 2 and related tables contain the detailed per-benchmark scores.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "84ab487b-308b-45c9-a029-4283625fb83f"
}
```

</details>

---

### System

_source line 182_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for open source base LLM 7B 8B 14B released 2025 2026…",
  "usage": {
    "total_tokens": 26427,
    "tool_uses": 13,
    "duration_ms": 50138
  },
  "last_tool_name": "WebSearch",
  "uuid": "e2f3a531-c27e-41e3-a70b-5bdfd11e2b22",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 183_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017ySAP5VC24qGWY2CAMipjh`</summary>

```json
{
  "query": "open source base LLM 7B 8B 14B released 2025 2026 Qwen Llama Gemma Mistral"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "c8fe4e97-a93d-4874-b9de-00ac934c20c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MaZ6XxEVW2ZS7NBuyWRTsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 22109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4289,
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

### System

_source line 184_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for allenai OLMo-2-0425-1B base model training tokens…",
  "usage": {
    "total_tokens": 28597,
    "tool_uses": 14,
    "duration_ms": 53538
  },
  "last_tool_name": "WebSearch",
  "uuid": "fbc8f388-2ef5-4ff4-8d83-f0b2696e7460",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 185_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018QUae2p1uum6EvFGB2BTca`</summary>

```json
{
  "query": "allenai OLMo-2-0425-1B base model training tokens release April 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "5cac5d25-c6bd-47ec-bd12-220833dad9ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoFvf4XqVno2Pf2ApiggxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2508,
      "cache_creation_input_tokens": 3235,
      "cache_read_input_tokens": 22816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3235,
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

### System

_source line 186_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Ministral 3 8B 14B base benchmark MMLU scores com…",
  "usage": {
    "total_tokens": 29846,
    "tool_uses": 15,
    "duration_ms": 56116
  },
  "last_tool_name": "WebSearch",
  "uuid": "704e83e2-7022-4a23-940e-c8607c82f1be",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 187_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EDSFXTd5DYW8uuSwEi3k8j`</summary>

```json
{
  "query": "Ministral 3 8B 14B base benchmark MMLU scores comparison Qwen3 December 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "83c6733c-64de-4de1-8cc6-e04c23ca0bb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pmny9sxqJN9qcrWPrC55bg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 26624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2975,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-18T07:08:36.863Z_

<details><summary>↩ Tool result · `toolu_01WXvDfUz4XiJ4CMQJ8m4QtY`</summary>

```text
Web search results for query: "Gemma 3 12B base pretrained benchmark scores MMLU 2025"

Links: [{"title":"Gemma 3 Technical Report","url":"https://arxiv.org/html/2503.19786v1"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"Gemma 3 12B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gemma-3-12b-it"},{"title":"(PDF) Gemma 3 Technical Report","url":"https://www.researchgate.net/publication/390175982_Gemma_3_Technical_Report"},{"title":"Google: Gemma 3 12B Review | Pricing, Benchmarks & Capabilities (2026) | Design for Online","url":"https://designforonline.com/ai-models/google-gemma-3-12b/"},{"title":"Gemma 3 model card | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/model_card_3"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"Gemma 3 12B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/gemma-3-12b"},{"title":"Google's Gemma 3: Features, Benchmarks, Performance and Implementation","url":"https://www.analyticsvidhya.com/blog/2025/03/gemma-3/"},{"title":"LLM Benchmarks March 2025","url":"https://www.timetoact-group.at/en/insights/llm-benchmarks/llm-benchmarks-march-2025"}]

Based on the search results, I found benchmark information for Gemma 3 12B, though the specific MMLU score for the base pretrained model wasn't directly listed in these results. Here's what I found:

**Gemma 3 12B Benchmark Performance:**

For the Gemma 3 12B model, MMLU-Pro shows a score of 59.5%. This is from the instruction-tuned (IT) variant.

The search results primarily focus on the instruction-tuned (IT) versions of Gemma 3 rather than the base pretrained models. Gemma 3 has been evaluated across benchmarks like MMLU-Pro (27B: 67.5), but specific base model MMLU scores for the 12B variant were not included in the available search results.

For context on the multilingual performance of the base models, the Gemma 3 12B base model showed a Global-MMLU-Lite (GMMLU) score of 69.4, which is a multilingual variant of MMLU.

If you need the specific MMLU score for the Gemma 3 12B base pretrained model, you may want to consult the full Gemma 3 Technical Report directly, as the search results focused more on the instruction-tuned variants and other benchmark types.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "3c172a62-41a5-43de-ac71-3a2f5c40b0a8"
}
```

</details>

---

### System

_source line 189_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "description": "Searching for Gemma 3 1B 4B 12B 27B MMLU exact score pretrained…",
  "usage": {
    "total_tokens": 28601,
    "tool_uses": 15,
    "duration_ms": 54032
  },
  "last_tool_name": "WebSearch",
  "uuid": "f03c1679-367a-4288-aa42-fea8690234c1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 190_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LnxcMFuYBudsJCxvdcxCKV`</summary>

```json
{
  "query": "Gemma 3 1B 4B 12B 27B MMLU exact score pretrained base model benchmark table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "8b5962cf-a19f-4304-a57c-90d8729e01d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoFvf4XqVno2Pf2ApiggxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2508,
      "cache_creation_input_tokens": 3235,
      "cache_read_input_tokens": 22816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3235,
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

### System

_source line 191_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "description": "Searching for Ministral 3 3B 8B 14B base model context length a…",
  "usage": {
    "total_tokens": 29893,
    "tool_uses": 16,
    "duration_ms": 56588
  },
  "last_tool_name": "WebSearch",
  "uuid": "f1c5e20b-2630-4e35-b89d-c80dcb576764",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 192_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013A5ufLxmLQ5d6De6TyVLMY`</summary>

```json
{
  "query": "Ministral 3 3B 8B 14B base model context length architecture layers gated access"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "e4c07b15-da9d-4c47-8d99-7ce522553e66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pmny9sxqJN9qcrWPrC55bg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 26624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2975,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-18T07:08:37.869Z_

<details><summary>↩ Tool result · `toolu_01Xa8pxNSg9F2NoK2gFojeKR`</summary>

```text
Web search results for query: "Llama 3.3 8B base model huggingface release 2024 2025"

Links: [{"title":"meta-llama/Llama-3.1-8B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.1-8B"},{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"meta-llama/Meta-Llama-3-8B · Hugging Face","url":"https://huggingface.co/meta-llama/Meta-Llama-3-8B"},{"title":"meta-llama/Llama-3.2-3B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.2-3B"},{"title":"NousResearch/Meta-Llama-3-8B · Hugging Face","url":"https://huggingface.co/NousResearch/Meta-Llama-3-8B"},{"title":"meta-llama/Llama-3.2-3B-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct"},{"title":"meta-llama/Llama-3.3-70B-Instruct · Release of an 8B model?","url":"https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/discussions/11"},{"title":"nvidia/Llama-3.1-8B-Instruct-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Llama-3.1-8B-Instruct-NVFP4"},{"title":"meta-llama/Llama-Guard-3-8B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-Guard-3-8B"},{"title":"QuantFactory/Meta-Llama-3-8B-GGUF · Hugging Face","url":"https://huggingface.co/QuantFactory/Meta-Llama-3-8B-GGUF"}]

Based on the search results, here's what I found regarding Llama 3.3 8B base model on Hugging Face:

Llama 3.3 is mentioned in Meta's Hugging Face collection, with the 71B model being updated on December 21, 2024. However, the search results indicate that as of late 2024, users were waiting for an 8B model release.

The Llama 3.3 8B Instruct model became available through third-party APIs (like OpenRouter) in mid-2025, but based on the search results provided, there is no direct mention of an official Llama 3.3 8B base model being released on Hugging Face's main meta-llama repository during 2024-2025.

The search results primarily show information about:
- Llama 3.1 8B released July 23, 2024
- Llama 3 8B released April 18, 2024
- Llama 3.2 released September 25, 2024

If you're looking for the Llama 3.3 8B base model specifically, you may need to check if it's available through alternative sources or wait for an official release on the main Hugging Face repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "035d2258-e952-42fc-9d20-4be4f083287b"
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-18T07:08:39.096Z_

<details><summary>↩ Tool result · `toolu_01K1z6xz2rXfA93LvH4PakR9`</summary>

```text
Web search results for query: "InternLM3 8B base model huggingface 2025 Shanghai AI"

Links: [{"title":"GitHub - InternLM/InternLM: Official release of InternLM series (InternLM, InternLM2, InternLM2.5, InternLM3). · GitHub","url":"https://github.com/InternLM/InternLM"},{"title":"internlm/internlm3-8b-instruct · Hugging Face","url":"https://huggingface.co/internlm/internlm3-8b-instruct"},{"title":"InternLM3 Open Source: Achieving High-Performance Models with 4T Data | by OpenMMLab | Medium","url":"https://openmmlab.medium.com/internlm3-open-source-achieving-high-performance-models-with-4t-data-c18e94bd5c6a"},{"title":"internlm/internlm3-8b-instruct-gguf · Hugging Face","url":"https://huggingface.co/internlm/internlm3-8b-instruct-gguf"},{"title":"internlm (Intern Large Models)","url":"https://huggingface.co/internlm"},{"title":"InternLM3 - a internlm Collection","url":"https://huggingface.co/collections/internlm/internlm3"},{"title":"Internlm3 8b Instruct - a Hugging Face Space by internlm","url":"https://huggingface.co/spaces/internlm/internlm3-8b-instruct"},{"title":"HuggingFace Transformers 😊 — InternLM","url":"https://internlm.readthedocs.io/en/latest/inference/huggingface_transformers.html"},{"title":"internlm3-8b-instruct | AI Model Details","url":"https://www.aimodels.fyi/models/huggingFace/internlm3-8b-instruct-internlm"},{"title":"Intern-ai","url":"https://internlm.intern-ai.org.cn/"}]

Based on the search results, here's what I found about InternLM3 8B:

## Overview

InternLM3 has open-sourced an 8-billion parameter instruction model, InternLM3-8B-Instruct, designed for general-purpose usage and advanced reasoning. InternLM is a conversational language model that is developed by Shanghai AI Laboratory.

## Release Date

On January 15, Shanghai AI Lab announced a major upgrade to the InternLM model with the release of InternLM3.

## Key Features

InternLM3 offers state-of-the-art performance on reasoning and knowledge-intensive tasks surpassing models like Llama3.1-8B and Qwen2.5-7B. InternLM3 is trained on only 4 trillion high-quality tokens, saving more than 75% of the training cost compared to other LLMs of similar scale.

InternLM3 supports both the deep thinking mode for solving complicated reasoning tasks via the long chain-of-thought and the normal response mode for fluent user interactions.

## HuggingFace Availability

The model is available on HuggingFace at `internlm/internlm3-8b-instruct`, where you can find documentation for loading and using the model with various frameworks like transformers, vLLM, and Ollama.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "2d91b21f-c1b7-4fda-bdc2-032567dd2f1a"
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-18T07:08:40.310Z_

<details><summary>↩ Tool result · `toolu_011MS5A9Ji6Wabu5HpP6mQPR`</summary>

```text
Web search results for query: "Falcon 3 7B 10B base model huggingface 2024 2025 TII"

Links: [{"title":"tiiuae/Falcon3-7B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-7B-Base"},{"title":"Welcome to the Falcon 3 Family of Open Models!","url":"https://huggingface.co/blog/falcon3"},{"title":"tiiuae/Falcon3-10B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-10B-Base"},{"title":"TII launches world’s most powerful SLMs under 13B parameters","url":"https://www.middleeastainews.com/p/tii-launches-most-powerful-slm"},{"title":"Falcon 3: UAE’s Technology Innovation Institute Launches World’s most Powerful Small AI Models that can also be run on Light Infrastructures, including Laptops | Technology Innovation Institute","url":"https://www.tii.ae/news/falcon-3-uaes-technology-innovation-institute-launches-worlds-most-powerful-small-ai-models"},{"title":"tiiuae/Falcon3-7B-Instruct · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-7B-Instruct"},{"title":"tiiuae/Falcon3-10B-Instruct · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-10B-Instruct"},{"title":"Technology Innovation Institute TII-UAE Just Released Falcon 3: A Family of Open-Source AI Models with 30 New Model Checkpoints from 1B to 10B - MarkTechPost","url":"https://www.marktechpost.com/2024/12/17/technology-innovation-institute-tii-uae-just-released-falcon-3-a-family-of-open-source-ai-models-with-30-new-model-checkpoints-from-1b-to-10b/"},{"title":"tiiuae/Falcon3-3B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-3B-Base"},{"title":"tiiuae/Falcon3-Mamba-7B-Instruct · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-Mamba-7B-Instruct"}]

Based on the search results, here's what I found about Falcon 3 models:

## Overview

Falcon3 is a family of decoder-only large language models under 10 billion parameters, developed by Technology Innovation Institute (TII) in Abu Dhabi. The Falcon 3 family of Open Foundation Models was released in December 2024 and includes four AI model sizes: Falcon3-1B, -3B, -7B and -10B, which are all available as open-source code via the Hugging Face community website.

## Base Models: 7B and 10B

**Falcon3-7B-Base:**
- Supports 4 languages (English, French, Spanish, Portuguese) and a context length up to 32K
- Pretrained on 14 Teratokens of datasets comprising web, code, STEM, high quality and multilingual data using 1024 H100 GPU chips

**Falcon3-10B-Base:**
- Depth up-scaled from Falcon3-7B-Base with continual pretraining on 2 Teratokens of datasets comprising web, code, STEM, high quality and multilingual data using 1024 H100 GPU chips
- Achieves state-of-the-art zero-shot and few-shot performance for models under 13B parameters

## Performance and Features

Falcon3-7B achieves competitive scores on reasoning and math, while Falcon3-10B demonstrates further improvements. All transformer-based Falcon3 models are compatible with Llama architecture allowing better integration in the AI ecosystem.

## Future Developments

In January 2025, enhanced models featuring multimodal capabilities including image, video, and audio support will be released, along with a full technical report.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "d6b6dc85-ed2a-4c5d-9bd1-6ece0ec17c4f"
}
```

</details>

---

### Tool result

_source line 196 · 2026-05-18T07:08:40.398Z_

<details><summary>↩ Tool result · `toolu_01Tr51pgpA5SvebdBXNEf7em`</summary>

```text
Web search results for query: "DeepSeek-R1-Distill-Qwen-14B benchmark MMLU MATH AIME pass@1 scores"

Links: [{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2501.12948v1"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/deepseek-r1"},{"title":"deepseek-ai/DeepSeek-R1 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1"},{"title":"DeepSeek-R1-Distill-Qwen-14B - Model Info, Parameters, Benchmarks - SiliconFlow\"","url":"https://www.siliconflow.com/models/deepseek-r1-distill-qwen-14b"},{"title":"DeepSeek R1 Distill Qwen 14B: Pricing, Benchmarks & Performance","url":"https://llm-stats.com/models/deepseek-r1-distill-qwen-14b"},{"title":"DeepSeek-R1: Features, o1 Comparison, Distilled Models & More | DataCamp","url":"https://www.datacamp.com/blog/deepseek-r1"},{"title":"Deployment-ready reasoning with quantized DeepSeek-R1 models | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/03/03/deployment-ready-reasoning-quantized-deepseek-r1-models"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-7B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"},{"title":"How to Benchmark DeepSeek-R1 Distilled Models on GPQA Using Ollama and OpenAI’s simple-evals | Towards Data Science","url":"https://towardsdatascience.com/how-to-benchmark-deepseek-r1-distilled-models-on-gpqa-using-ollama-and-openais-simple-evals/"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-14B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"}]

Based on the search results, I found benchmark scores for DeepSeek-R1-Distill-Qwen-14B:

## Benchmark Scores for DeepSeek-R1-Distill-Qwen-14B (Pass@1)

**AIME 2024:** 69.7% pass rate

**MATH-500:** 93.9% accuracy

**MMLU:** The search results do not contain specific MMLU pass@1 scores for the 14B distilled model specifically. However, DeepSeek-R1 (the full model) achieves 90.8% on MMLU.

The search results indicate that for benchmarks requiring sampling, a temperature of 0.6, a top-p value of 0.95, and 64 responses per query are generated to estimate pass@1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "d258e898-92cf-47af-8bc2-67ed7a1b3c59"
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-18T07:08:42.082Z_

<details><summary>↩ Tool result · `toolu_01JiKSAWsvD6P8BdGqskQtpu`</summary>

```text
Web search results for query: "OLMo 2 7B 13B MMLU ARC HellaSwag exact scores table arxiv 2501.00656"

Links: [{"title":"2 OLMo 2 Furious OLMo Team Pete Walsh 1 Luca Soldaini 1 Dirk Groeneveld 1","url":"https://arxiv.org/pdf/2501.00656"},{"title":"[2501.00656] 2 OLMo 2 Furious","url":"https://arxiv.org/abs/2501.00656"},{"title":"OLMo 2: The best fully open language model to date | Ai2","url":"https://allenai.org/blog/olmo2"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"allenai/OLMo-2-1124-13B-RM · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-RM"},{"title":"allenai/OLMo-2-1124-13B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B"},{"title":"eaddario/OLMo-2-1124-7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/eaddario/OLMo-2-1124-7B-Instruct-GGUF"},{"title":"OLMoE: Open Mixture-of-Experts Language Models","url":"https://arxiv.org/html/2409.02060v1"},{"title":"allenai/OLMo-2-0325-32B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct"},{"title":"GitHub - allenai/OLMo: Modeling, training, eval, and inference code for OLMo · GitHub","url":"https://github.com/allenai/OLMo"}]

I found information about OLMo 2 from arxiv paper 2501.00656. The search results include some benchmark scores, though the complete table with all the exact scores you're looking for may require viewing the full PDF directly.

Based on the search results, here are the scores I found:

For OLMo 2 7B and 13B models, the scores improved as follows: ARC: 80.2 → 83.5 for 13B; MMLU: 59.8 → 63.7 for 7B, 63.4 → 67.5 for 13B.

The search results also indicate that HellaSwag scores improved, along with reading comprehension and math skills benchmarks, though the specific HellaSwag scores aren't explicitly listed in the excerpts I retrieved.

For the most complete and detailed table of exact scores for MMLU, ARC, HellaSwag, and other benchmarks for both the 7B and 13B models, I recommend accessing the full PDF of the paper directly at https://arxiv.org/pdf/2501.00656, which appears to contain comprehensive evaluation tables.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "8342f698-7d59-4ae3-82cd-c36596938211"
}
```

</details>

---

### System

_source line 198_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for MAP-Neo 7B base model huggingface 2025 fully open…",
  "usage": {
    "total_tokens": 33948,
    "tool_uses": 18,
    "duration_ms": 65047
  },
  "last_tool_name": "WebSearch",
  "uuid": "26e98155-64bb-498b-897b-fafbdb93d2e0",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 199_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RktS9DiqVzLTK4YEBv2EeG`</summary>

```json
{
  "query": "MAP-Neo 7B base model huggingface 2025 fully open source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "0d04739c-0864-4a1a-8154-acd7c9e3b45e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eA9GFtGku2xt3U61mvLh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-18T07:08:43.673Z_

<details><summary>↩ Tool result · `toolu_018QUae2p1uum6EvFGB2BTca`</summary>

```text
Web search results for query: "allenai OLMo-2-0425-1B base model training tokens release April 2025"

Links: [{"title":"GitHub - allenai/OLMo: Modeling, training, eval, and inference code for OLMo · GitHub","url":"https://github.com/allenai/OLMo"},{"title":"allenai/OLMo-2-0425-1B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B"},{"title":"allenai/OLMo-2-0425-1B-early-training · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B-early-training"},{"title":"allenai/OLMo-2-0425-1B-DPO · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B-DPO"},{"title":"allenai/OLMo-2-0425-1B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct"},{"title":"allenai/OLMo-2-0425-1B-SFT · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B-SFT"},{"title":"OLMo release notes | Ai2","url":"https://allenai.org/olmo/release-notes"},{"title":"OLMo-2-0425-1B-SFT huggingface.co api & allenai OLMo-2-0425-1B-SFT github AI Model - Toolify","url":"https://www.toolify.ai/ai-model/allenai-olmo-2-0425-1b-sft"},{"title":"Olmo from Ai2","url":"https://allenai.org/olmo"},{"title":"OLMo 2: The best fully open language model to date | Ai2","url":"https://allenai.org/blog/olmo2"}]

Based on the search results, here's what I found about the Allen AI OLMo-2-0425-1B base model:

## Training Tokens

For the 1B model, the model was trained on 50B high quality tokens. However, this represents only the primary training run. OLMo 2 1B is pretrained on 4T tokens of high-quality data, specifically using the OLMo-mix-1124 as well as Dolmino-mix-1124 for mid-training.

## Model Architecture and Training Approach

The 1B model was trained three times with different data order on 50B high quality tokens, with the last checkpoint of seed 42 used as the final checkpoint.

## Release Date

The model naming follows Allen AI's updated convention. The OLMo naming convention was updated to include the model name, model version, model parameters, followed by the month and year of release, making it easier to track updates over time. As an example, OLMo v1.7 is now OLMo April 2024, and today's released models adhere to this updated naming convention. The "0425" in the model name indicates an April 2025 release date.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "03d58ad1-b8a2-4765-b6e2-90a8130e7700"
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-18T07:08:43.680Z_

<details><summary>↩ Tool result · `toolu_01RkknRkQyGS8BttodDkMAzn`</summary>

```text
Web search results for query: "Phi-4 mini 3.8B base pretrained model HuggingFace release date benchmark"

Links: [{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"microsoft/Phi-4-mini-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-reasoning"},{"title":"unsloth/Phi-4-mini-reasoning-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Phi-4-mini-reasoning-GGUF"},{"title":"Phi-4 Mini: Microsoft's Best Small Model (3.8B) — Guide & Benchmarks | Local AI Master","url":"https://localaimaster.com/models/phi-4-mini"},{"title":"microsoft/Phi-3-mini-4k-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-3-mini-4k-instruct"},{"title":"microsoft/Phi-4-mini-flash-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-flash-reasoning"},{"title":"unsloth/Phi-4-mini-instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF"},{"title":"microsoft/Phi-3.5-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-3.5-mini-instruct"},{"title":"Mungert/Phi-4-mini-reasoning-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/Phi-4-mini-reasoning-GGUF"}]

Based on the search results, here's the information about Phi-4 mini 3.8B:

## Release Information

Phi-4 (microsoft/phi-4 on HuggingFace) is the December 2024 release of Microsoft's Phi family. More specifically, Phi-4 Mini was published on March 19, 2026, representing a later update to the Phi-4 family.

## Base Model Availability

The search results primarily show instruct and reasoning variants of Phi-4-mini rather than explicit base pretrained models. However, the 3.8B parameters Phi-4-mini-instruct model was compared with a set of models over a variety of benchmarks using an internal benchmark platform.

## Benchmark Performance

The model with only 3.8B-param achieves a similar level of multilingual language understanding and reasoning ability as much larger models. More specifically, Phi-4 Mini matches Llama 3.1 8B on MMLU (73%) while using half the memory and running 2x faster.

For reasoning-focused variants, the 3.8B parameters Phi-4-mini-reasoning model was compared with a set of models over a variety of reasoning benchmarks, evaluating with Math-500, AIME 2024, and GPQA Diamond benchmarks.

## Technical Details

Phi-4-mini-instruct has 3.8B parameters and is a dense decoder-only Transformer model. Phi-4-mini's training data includes a wide variety of sources, totaling 5 trillion tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "4b336932-fbe6-4a43-bb44-55395ddf86f5"
}
```

</details>

---

### System

_source line 202_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for SmolLM2 7B base model huggingface 2025",
  "usage": {
    "total_tokens": 33995,
    "tool_uses": 19,
    "duration_ms": 65505
  },
  "last_tool_name": "WebSearch",
  "uuid": "328908ca-d233-4759-a76c-0594531f8e2a",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 203_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ACyQrSBPWCD2N3Mre5XZSf`</summary>

```json
{
  "query": "SmolLM2 7B base model huggingface 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "73bb96b7-cc9e-426d-a080-d58810397a0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eA9GFtGku2xt3U61mvLh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
      "service_tier": "standard",
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

_source line 204_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Phi-4 14B MMLU benchmark score base model decembe…",
  "usage": {
    "total_tokens": 34042,
    "tool_uses": 20,
    "duration_ms": 65977
  },
  "last_tool_name": "WebSearch",
  "uuid": "40a86d58-2e1a-4797-80ad-0ca77a64d46f",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 205_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GtWvkHwkNKo59yLKkcpKxt`</summary>

```json
{
  "query": "Phi-4 14B MMLU benchmark score base model december 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "e11d45ad-45f2-46e1-9006-abab827e4d7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eA9GFtGku2xt3U61mvLh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 206 · 2026-05-18T07:08:44.496Z_

<details><summary>↩ Tool result · `toolu_013A5ufLxmLQ5d6De6TyVLMY`</summary>

```text
Web search results for query: "Ministral 3 3B 8B 14B base model context length architecture layers gated access"

Links: [{"title":"mistralai/Ministral-3-14B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512"},{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"},{"title":"Ministral 3 — Megatron Bridge","url":"https://docs.nvidia.com/nemo/megatron-bridge/0.2.0/models/vlm/ministral3.html"},{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"Ministral 3","url":"https://arxiv.org/html/2601.08584v1"},{"title":"mistralai / ministral-14b-instruct-2512","url":"https://docs.api.nvidia.com/nim/reference/mistralai-ministral-14b-instruct-2512"},{"title":"Ministral 3 14B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/ministral-3-14b"},{"title":"Mistral 3 14B Reasoning 2512: Comprehensive Review, Features, and Performance Insights - GenAI Content","url":"https://www.genaicontent.org/news/mistral-3-14b-review-features-performance"},{"title":"Ministral 3 | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.08584"},{"title":"Ministral 3 - How to Run Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/models/tutorials/ministral-3"}]

Based on the search results, here is comprehensive information about Ministral 3:

## Model Sizes and Variants

The Ministral 3 series is available in three model sizes: 3B, 8B, and 14B parameters, with base, instruct, and reasoning variants available for each size, each with image understanding capabilities and all under the Apache 2.0 license.

## Architecture and Layers

The family consists of three sizes: 3B, 8B, and 14B parameters, with 26, 34, and 40 layers respectively.

More detailed architecture specifications:

- **Ministral 3 3B:** 3.4B parameter vision-language model with 26 layers, 3072 hidden size, 32 attention heads, and 8 query groups (GQA)
- **Ministral 3 8B:** 8.4B parameter vision-language model with 34 layers, 4096 hidden size, 32 attention heads, and 8 query groups (GQA)
- **Ministral 3 14B:** ~14B parameter vision-language model with 40 layers, 5120 hidden size, 32 attention heads, and 8 query groups (GQA)

## Context Length

All models support extended context lengths up to 256K tokens using YaRN RoPE scaling. More specifically, base and instruct variants have context lengths up to 256k tokens, while reasoning models support 128k tokens.

## Access

Regarding gated access, the search results indicate that these models are released to the community under the Apache 2.0 license, suggesting they are openly available rather than gated.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "8a4043fa-16d8-48a9-bfb5-a9c7ee511f45"
}
```

</details>

---

### System

_source line 207_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Yi-1.5 9B base model huggingface 01.AI 2024 2025",
  "usage": {
    "total_tokens": 34089,
    "tool_uses": 21,
    "duration_ms": 66968
  },
  "last_tool_name": "WebSearch",
  "uuid": "bbe0002c-4069-41d8-b62e-d50f8eb9a07a",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 208_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014WyPuvfMMbBafWjPzucQQQ`</summary>

```json
{
  "query": "Yi-1.5 9B base model huggingface 01.AI 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f9c30d4d-df3c-4636-83ab-ee3f50ae8a7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eA9GFtGku2xt3U61mvLh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
      "service_tier": "standard",
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

_source line 209_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Mistral Nemo 12B base model huggingface 2024 benc…",
  "usage": {
    "total_tokens": 34136,
    "tool_uses": 22,
    "duration_ms": 67217
  },
  "last_tool_name": "WebSearch",
  "uuid": "3ec7ef73-a792-49bf-9bcb-08e08c4bf758",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 210_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013VUt3RhDzXqDuaJT3s8rFu`</summary>

```json
{
  "query": "Mistral Nemo 12B base model huggingface 2024 benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "96e8385f-2ceb-4e4a-99ec-035f22b2c1e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eA9GFtGku2xt3U61mvLh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-18T07:08:47.242Z_

<details><summary>↩ Tool result · `toolu_01EDSFXTd5DYW8uuSwEi3k8j`</summary>

```text
Web search results for query: "Ministral 3 8B 14B base benchmark MMLU scores comparison Qwen3 December 2025"

Links: [{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"},{"title":"Ministral 3 (14B Reasoning 2512) vs Qwen3 VL 8B Thinking Comparison","url":"https://llm-stats.com/models/compare/ministral-14b-latest-vs-qwen3-vl-8b-thinking"},{"title":"Ministral 3 (14B Reasoning 2512) vs Qwen3.5-9B Comparison","url":"https://llm-stats.com/models/compare/ministral-14b-latest-vs-qwen3.5-9b"},{"title":"Ministral 3 (14B Base 2512) vs Qwen3 VL 30B A3B Thinking Comparison","url":"https://llm-stats.com/models/compare/ministral-3-14b-base-2512-vs-qwen3-vl-30b-a3b-thinking"},{"title":"Ministral 3 (14B Reasoning 2512) vs Qwen3 VL 30B A3B Thinking Comparison","url":"https://llm-stats.com/models/compare/ministral-14b-latest-vs-qwen3-vl-30b-a3b-thinking"},{"title":"Ministral 3 vs Others: Accuracy, Token Efficiency, and the Best Model per Budget","url":"https://kaitchup.substack.com/p/ministral-3-vs-others-accuracy-token"},{"title":"An Empirical Study of Qwen3 Quantization","url":"https://arxiv.org/html/2505.02214v1"},{"title":"Ministral 3 (3B Instruct 2512) vs Qwen3.5-2B Comparison","url":"https://llm-stats.com/models/compare/ministral-3-3b-instruct-2512-vs-qwen3.5-2b"},{"title":"MiniStral 3 (14B Instruct 2512) vs Qwen3.5-0.8B Comparison","url":"https://llm-stats.com/models/compare/ministral-3-14b-instruct-2512-vs-qwen3.5-0.8b"},{"title":"Ministral 3 (8B Instruct 2512) vs Qwen3 VL 8B Thinking Comparison: Benchmarks, Pricing & Performance","url":"https://llm-stats.com/models/compare/ministral-3-8b-instruct-2512-vs-qwen3-vl-8b-thinking"}]

Based on the search results, here's information about Ministral 3 and Qwen3 base model benchmark comparisons:

## Base Model MMLU Scores

Ministral 3 (14B Base) scores MMLU at 79.4%, while Qwen3 VL 30B A3B Thinking scores MMLU at 87.6%.

Ministral 3 (14B Base) also scores MMLU-Redux at 82.0%.

## Model Variants and Release Information

The Ministral 3 lineup includes base, instruct, and reasoning variants at 3B, 8B, and 14B parameters. Ministral 3 (14B Base) was released on 2025-12-04.

## Reasoning Model Comparison

For context on the reasoning variants, Qwen3-VL achieved AIME 2024: 83.7%, while Ministral 3 14B scored 89.8% on the same benchmark.

The search results indicate that while Ministral 3 base models perform well, larger Qwen3 variants generally show higher MMLU scores on base model evaluations, though Ministral 3's reasoning variants are competitive across other specialized benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "8a0150dc-6efb-4800-b6f5-329e9d73fc08"
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-18T07:08:47.543Z_

<details><summary>↩ Tool result · `toolu_01LnxcMFuYBudsJCxvdcxCKV`</summary>

```text
Web search results for query: "Gemma 3 1B 4B 12B 27B MMLU exact score pretrained base model benchmark table"

Links: [{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"Gemma 3 model card | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/model_card_3"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"Gemma 3 Technical Report","url":"https://arxiv.org/html/2503.19786v1"},{"title":"Gemma 3 Model: Multimodal & Efficient LLM","url":"https://www.emergentmind.com/topics/gemma-3-model"},{"title":"Gemma-3 LLMs: Multimodal DeepMind Models","url":"https://www.emergentmind.com/topics/gemma-3-models"},{"title":"Announcing Gemma 3n preview: powerful, efficient, mobile-first AI - Google Developers Blog","url":"https://developers.googleblog.com/en/introducing-gemma-3n/"},{"title":"(PDF) Gemma 3 Technical Report","url":"https://www.researchgate.net/publication/390175982_Gemma_3_Technical_Report"},{"title":"Google's Gemma 3: Features, Benchmarks, Performance and Implementation","url":"https://www.analyticsvidhya.com/blog/2025/03/gemma-3/"},{"title":"GitHub - heilcheng/openevals: Benchmarking suite for open-weight language models · GitHub","url":"https://github.com/heilcheng/gemma-benchmark"}]

Based on the search results, I found some MMLU benchmark information for Gemma 3 models, though the results mention MMLU-Pro rather than standard MMLU. Let me search more specifically for the standard MMLU scores across all model sizes.

Links: [{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"(PDF) Gemma 3 Technical Report","url":"https://www.researchgate.net/publication/390175982_Gemma_3_Technical_Report"},{"title":"Google Gemma 4: A Technical Overview","url":"https://www.labellerr.com/blog/gemma-4-open-weight-ai-model-overview/"},{"title":"Google's Gemma 3: Features, Benchmarks, Performance and Implementation","url":"https://www.analyticsvidhya.com/blog/2025/03/gemma-3/"},{"title":"Gemma 3 model card | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/model_card_3"},{"title":"Gemma 3 Technical Report","url":"https://arxiv.org/html/2503.19786v1"},{"title":"MMLU 87.1%, HumanEval 82.7% (2026) | Blog - Gemma 4","url":"https://gemma4-ai.com/blog/gemma4-benchmark"},{"title":"Gemma-3-27B-it: Multimodal Instruction-Tuned LLM","url":"https://www.emergentmind.com/topics/gemma-3-27b-it"},{"title":"sweelol/gemma3-270m-pruned-base · Hugging Face","url":"https://huggingface.co/sweelol/gemma3-270m-pruned-base"}]

Let me search more specifically for the pretrained base model MMLU scores table from the technical report.

Links: [{"title":"Gemma 3 Technical Report","url":"https://arxiv.org/html/2503.19786v1"},{"title":"(PDF) Gemma 3 Technical Report","url":"https://www.researchgate.net/publication/390175982_Gemma_3_Technical_Report"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"[PDF] Gemma 3 Technical Report | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Gemma-3-Technical-Report-Kamath-Ferret/adac25c0aebd013f1225ec02636edfcc0bf4cf7c"},{"title":"MedGemma Technical Report","url":"https://arxiv.org/html/2507.05201v4"},{"title":"Google's Gemma 3: Features, Benchmarks, Performance and Implementation","url":"https://www.analyticsvidhya.com/blog/2025/03/gemma-3/"},{"title":"2025-03-12 Gemma 3 Technical Report Gemma Team, Google DeepMind1","url":"https://storage.googleapis.com/deepmind-media/gemma/Gemma3Report.pdf"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"[2503.19786] Gemma 3 Technical Report","url":"https://arxiv.org/abs/2503.19786"},{"title":"Gemma-3 LLMs: Multimodal DeepMind Models","url":"https://www.emergentmind.com/topics/gemma-3-models"}]

Perfect! I found the exact data. Based on the search results, I can now provide you with the Gemma 3 MMLU pretrained base model benchmark scores.

For the pretrained (base) models, the MMLU scores are:
- Gemma 3 1B: 38.8%
- Gemma 3 4B: 58.1%
- Gemma 3 12B: 71.9%
- Gemma 3 27B: 76.9%

These scores represent the standard MMLU benchmark performance on the pretrained base models, showing clear improvement in performance as the model size increases from 1B to 27B parameters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f3687c0d-b564-4958-8a76-90e719c649af"
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-18T07:08:47.993Z_

<details><summary>↩ Tool result · `toolu_017ySAP5VC24qGWY2CAMipjh`</summary>

```text
Web search results for query: "open source base LLM 7B 8B 14B released 2025 2026 Qwen Llama Gemma Mistral"

Links: [{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"Best Open-Source LLMs in 2026 - Featherless","url":"https://featherless.ai/blog/best-open-source-llms-2026"},{"title":"Best Open Source LLMs in 2026: DeepSeek, Llama & More","url":"https://www.miniloop.ai/blog/best-open-source-llms-2026"},{"title":"Open-Source LLM Landscape 2026, 15+ Model Families Mapped | Presenc AI","url":"https://presenc.ai/research/open-source-llm-landscape-2026"},{"title":"Open-Source LLM Landscape 2026: DeepSeek V4 vs Llama 4 vs Qwen 3.5 vs Gemma 4","url":"https://codersera.com/blog/open-source-llms-landscape-2026/"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Best Open-Source LLM 2026: 8 Tested, 3 Beat GPT-4 | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"library","url":"https://ollama.com/library"},{"title":"Open Source LLM Comparison Table (2026) | ComputingForGeeks","url":"https://computingforgeeks.com/open-source-llm-comparison/"}]

Based on the search results, here's a comprehensive overview of open source base LLMs in the 7B-14B range released in 2025-2026 from the major providers you mentioned:

## Qwen
Qwen 3.5 (released February 2026) is a native vision-language model with 397B total parameters (17B active per pass), supporting 201 languages and offering a 1M token context window. The Qwen 3 family also includes smaller variants (32B, 14B, 8B, 4B) that run on consumer hardware. Qwen3 is a strong fit when you need multilingual support, commercial flexibility, and a broad ecosystem of fine-tunes, quantizations, and deployment examples.

## Llama
Meta's Llama family remains the most influential open-source LLM series, and the latest generation, Llama 4, released in April 2025, is Meta's first natively multimodal model family and its first to use a mixture-of-experts (MoE) architecture. Llama 4 Scout fits on a single NVIDIA H100 GPU and offers an industry-leading 10M token context window, outperforming previous-generation models like Gemma 3 and Mistral 3.1 across a broad range of benchmarks.

## Gemma
Google's open model family ranges from 1B to 27B – optimized for on-device use. Gemma 4 26B A4B is the most practical local model recommendation for many developers, with Apache 2.0 licensing, 25.2B total parameters, 3.8B active parameters, text and image support, and a 256K token context window.

## Mistral
The 7B model released by Mistral AI, updated to version 0.3. Mistral's flagship features 123B parameters, 128k context, 80+ languages. Both Mistral Large 3 and Mistral Small 4 now ship under Apache 2.0, a significant shift from Mistral's earlier restrictive licensing.

## Key Licensing Notes
LLaMA uses the Meta Community License, Mistral uses Apache 2.0, Qwen uses Apache 2.0, and DeepSeek uses MIT. Apache 2.0 has won the license war for permissive labs, with Gemma 4, Qwen 3.5, Mistral Large 3, and Yi all shipping under Apache 2.0; DeepSeek V4 ships MIT; and Llama 4 keeps the Meta custom license with the 700M MAU clause.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "28ce173e-2080-43ba-8162-352e2a1923f2"
}
```

</details>

---

### Tool result

_source line 214 · 2026-05-18T07:08:49.140Z_

<details><summary>↩ Tool result · `toolu_01GtWvkHwkNKo59yLKkcpKxt`</summary>

```text
Web search results for query: "Phi-4 14B MMLU benchmark score base model december 2024"

Links: [{"title":"Qwen3.5-27B vs Phi-4: When Twice the Parameters Is Not Twice as Obvious | Awesome Agents","url":"https://awesomeagents.ai/tools/qwen-3-5-27b-vs-phi-4/"},{"title":"Microsoft PHI-4: A 14B Parameter Model That Rivals Models 5x Its Size - Developers Digest","url":"https://www.developersdigest.tech/blog/microsoft-phi-4-guide"},{"title":"Phi-4: Small Language Models That Pack a Punch | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/educatordeveloperblog/phi-4-small-language-models-that-pack-a-punch/4464167"},{"title":"Microsoft releases full Phi-4 model with weights under MIT license","url":"https://the-decoder.com/microsoft-releases-full-phi-4-model-with-weights-under-mit-license/"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"Phi-4 Technical Report","url":"https://arxiv.org/html/2412.08905v1"},{"title":"Phi-4 - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/phi-4"},{"title":"Phi 4 by Microsoft: Complete Performance Review & Benchmarks (2025)","url":"https://airank.dev/models/phi-4"},{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"Phi-4","url":"https://ai.azure.com/catalog/models/Phi-4"}]

Based on the search results, here is the MMLU benchmark score for Phi-4 14B base model from December 2024:

On MMLU (a broad test of knowledge across 57 subjects), Phi-4 scores 84.8%. Microsoft released Phi-4 in December 2024, and this MMLU score of 84.8 puts Phi-4 ahead of Llama-3.3-70B on the same evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "13b43e15-0fbb-4622-be4f-6ee14fa600f3"
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-18T07:08:50.910Z_

<details><summary>↩ Tool result · `toolu_01ACyQrSBPWCD2N3Mre5XZSf`</summary>

```text
Web search results for query: "SmolLM2 7B base model huggingface 2025"

Links: [{"title":"HuggingFaceTB/SmolLM2-1.7B · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B"},{"title":"HuggingFaceTB/SmolLM2-1.7B-Instruct · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct"},{"title":"HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF"},{"title":"SmolLM2 - a HuggingFaceTB Collection","url":"https://huggingface.co/collections/HuggingFaceTB/smollm2"},{"title":"tensorblock/SmolLM2-1.7B-GGUF · Hugging Face","url":"https://huggingface.co/tensorblock/SmolLM2-1.7B-GGUF"},{"title":"HuggingFaceTB/SmolLM2-1.7B-Instruct-16k · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct-16k"},{"title":"HuggingFaceTB/SmolLM2-135M · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-135M"},{"title":"bartowski/SmolLM2-1.7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/bartowski/SmolLM2-1.7B-Instruct-GGUF"},{"title":"GitHub - huggingface/smollm: Everything about the SmolLM and SmolVLM family of models · GitHub","url":"https://github.com/huggingface/smollm"},{"title":"HuggingFaceTB/SmolVLM-Instruct · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct"}]

Based on the search results, here's what I found about SmolLM2 models:

## Overview

SmolLM2 is a family of compact language models available in three sizes: 135M, 360M, and 1.7B parameters. Note that there isn't a 7B variant in the SmolLM2 family—the largest model is 1.7B.

## Base Model Details

These models are capable of solving a wide range of tasks while being lightweight enough to run on-device. The 1.7B variant demonstrates significant advances over its predecessor SmolLM1-1.7B, particularly in instruction following, knowledge, reasoning, and mathematics. It was trained on 11 trillion tokens using a diverse dataset combination: FineWeb-Edu, DCLM, The Stack, along with new mathematics and coding datasets.

## Hugging Face Availability

The base model is available on Hugging Face as **HuggingFaceTB/SmolLM2-1.7B**. The research was published in 2025 with the paper titled "SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model" (arXiv:2502.02737).

There are also instruct versions and other variants available on Hugging Face Hub, such as the SmolLM2-1.7B-Instruct model with extended context support.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "a987eb7f-52b8-472b-9569-056aa9531102"
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-18T07:08:51.197Z_

<details><summary>↩ Tool result · `toolu_01RktS9DiqVzLTK4YEBv2EeG`</summary>

```text
Web search results for query: "MAP-Neo 7B base model huggingface 2025 fully open source"

Links: [{"title":"m-a-p/neo_7b · Hugging Face","url":"https://huggingface.co/m-a-p/neo_7b"},{"title":"Paper page - MAP-Neo: Highly Capable and Transparent Bilingual Large \nLanguage Model Series","url":"https://huggingface.co/papers/2405.19327"},{"title":"GitHub - multimodal-art-projection/MAP-NEO · GitHub","url":"https://github.com/multimodal-art-projection/MAP-NEO"},{"title":"m-a-p/neo_7b_instruct_v0.1 · Hugging Face","url":"https://huggingface.co/m-a-p/neo_7b_instruct_v0.1"},{"title":"m-a-p/neo_7b_sft_v0.1 · Hugging Face","url":"https://huggingface.co/m-a-p/neo_7b_sft_v0.1"},{"title":"MAP-NEO/README.md at main · multimodal-art-projection/MAP-NEO","url":"https://github.com/multimodal-art-projection/MAP-NEO/blob/main/README.md"},{"title":"GitHub - huggingface/open-r1: Fully open reproduction of DeepSeek-R1 · GitHub","url":"https://github.com/huggingface/open-r1"},{"title":"nvidia/OpenMath-Nemotron-7B · Hugging Face","url":"https://huggingface.co/nvidia/OpenMath-Nemotron-7B"},{"title":"neulab/Pangea-7B · Hugging Face","url":"https://huggingface.co/neulab/Pangea-7B"},{"title":"m-a-p/YuE-s1-7B-anneal-en-cot · Hugging Face","url":"https://huggingface.co/m-a-p/YuE-s1-7B-anneal-en-cot"}]

Based on the search results, here's what I found about MAP-Neo 7B:

## MAP-Neo 7B Overview

MAP-Neo is a fully open-sourced bilingual LLM with 7B parameters that achieves performance comparable to existing state-of-the-art LLMs.

## Key Characteristics

MAP-NEO is a fully open-sourced Large Language Model that includes the pretraining data, a data processing pipeline (Matrix), pretraining scripts, and alignment code, and is trained from scratch on 4.5T English and Chinese tokens, exhibiting performance comparable to LLaMA2 7B.

## Complete Transparency

All details to reproduce MAP-Neo are open-sourced, including the cleaned pre-training corpus, data cleaning pipeline, checkpoints, and well-optimized training/evaluation framework. The comprehensive release includes the final and intermediate checkpoints, a self-trained tokenizer, the pre-training corpus, and an efficient, stable optimized pre-training codebase.

## Performance

The MAP-Neo model delivers proprietary-model-like performance in challenging tasks such as reasoning, mathematics, and coding, outperforming its peers of similar size.

## Availability

The model is available on Hugging Face under the m-a-p organization, with both base and fine-tuned variants available. Commercial usage is permitted under the model's terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "d19f1b94-6fa1-4439-b673-c107ad586eb8"
}
```

</details>

---

### System

_source line 217_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Qwen3 7B 8B 14B base model HuggingFace release da…",
  "usage": {
    "total_tokens": 29696,
    "tool_uses": 14,
    "duration_ms": 65479
  },
  "last_tool_name": "WebSearch",
  "uuid": "49d709a9-c14e-4e0d-af4f-e8d5e7388543",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 218_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013HYTL2dHVWtVEVhtKkDC36`</summary>

```json
{
  "query": "Qwen3 7B 8B 14B base model HuggingFace release date benchmark MMLU parameters 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "26e629f3-c4bd-4369-8362-7da1772d558a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015f4Aixw9EZrsqfourjXbjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 26398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3267,
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

### System

_source line 219_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Gemma 3 7B 12B base model HuggingFace release dat…",
  "usage": {
    "total_tokens": 29697,
    "tool_uses": 15,
    "duration_ms": 66210
  },
  "last_tool_name": "WebSearch",
  "uuid": "704121fd-db5d-4324-82b6-310d0dc9b31c",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 220_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PtZj1rmNwwwPryZKyp3r3x`</summary>

```json
{
  "query": "Gemma 3 7B 12B base model HuggingFace release date 2025 benchmark parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "baa8a974-1363-4d5a-bbe5-ef6f475b25e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015f4Aixw9EZrsqfourjXbjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 26398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3267,
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

_source line 221 · 2026-05-18T07:08:52.575Z_

<details><summary>↩ Tool result · `toolu_013VUt3RhDzXqDuaJT3s8rFu`</summary>

```text
Web search results for query: "Mistral Nemo 12B base model huggingface 2024 benchmark"

Links: [{"title":"nvidia/Mistral-NeMo-12B-Base · Hugging Face","url":"https://huggingface.co/nvidia/Mistral-NeMo-12B-Base"},{"title":"nvidia/Mistral-NeMo-12B-Instruct · Hugging Face","url":"https://huggingface.co/nvidia/Mistral-NeMo-12B-Instruct"},{"title":"Mistral NeMo | Mistral AI","url":"https://mistral.ai/news/mistral-nemo"},{"title":"Mistral NeMo 12B | Open Laboratory","url":"https://openlaboratory.com/models/mistral-nemo-12b/"},{"title":"Mistral NeMo 12B — A comprehensive look at the next-generation enterprise AI model | UnfoldAI","url":"https://unfoldai.com/mistral-nemo-12b-review/"},{"title":"mistralai/Mistral-Nemo-Base-2407 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-Nemo-Base-2407"},{"title":"mistralai/Mistral-Nemo-Instruct-2407 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407"},{"title":"starble-dev/Mistral-Nemo-12B-Instruct-2407-GGUF · Hugging Face","url":"https://huggingface.co/starble-dev/Mistral-Nemo-12B-Instruct-2407-GGUF"},{"title":"EasierAI/Mistral-NeMo-12B · Hugging Face","url":"https://huggingface.co/EasierAI/Mistral-NeMo-12B"},{"title":"README.md · nvidia/Mistral-NeMo-12B-Base at main","url":"https://huggingface.co/nvidia/Mistral-NeMo-12B-Base/blob/main/README.md"}]

Based on the search results, here's comprehensive information about the Mistral Nemo 12B base model and its 2024 benchmarks:

## Model Overview

Mistral-NeMo-12B-Base is a Large Language Model (LLM) composed of 12B parameters, trained jointly by NVIDIA and Mistral AI. The model was trained between May 2024 and June 2024.

## Key Capabilities

Mistral-NeMo-12B-Base is a completion model intended for use in over 80+ programming languages and designed for global, multilingual applications. It is fast, trained on function-calling, has a large context window, and is particularly strong in English, French, German, Spanish, Italian, Portuguese, Chinese, Japanese, Korean, Arabic, and Hindi.

## Benchmark Performance

The model shows strong performance across major evaluation benchmarks:

Zero-shot performance on HellaSwag reaches 83.5%, and the model delivers 76.8% accuracy on Winogrande. On comprehension tasks, it scores 73.8% on TriviaQA (five-shot) and 68.0% on MMLU (five-shot).

Mistral NeMo 12B exhibits competitive results on established language model evaluation benchmarks, frequently surpassing other models in its parameter range such as Gemma 2 9B and Llama 3 8B.

## Availability

Weights are hosted on HuggingFace both for the base and for the instruct models. The base model is available at the official Mistral AI repository on Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "b7fce39d-6c0b-44a0-a69e-dad583b12659"
}
```

</details>

---

### System

_source line 222_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Llama 4 Scout Maverick 7B 8B parameters MoE activ…",
  "usage": {
    "total_tokens": 29698,
    "tool_uses": 16,
    "duration_ms": 66562
  },
  "last_tool_name": "WebSearch",
  "uuid": "beb15e17-3a8a-41a7-989a-cd94bc7f6ff2",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 223_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E4hPcgTXBxwZ8ctz3NfZHi`</summary>

```json
{
  "query": "Llama 4 Scout Maverick 7B 8B parameters MoE active base model HuggingFace 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "4561fe72-56de-452a-b74a-dc35bc60d16f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015f4Aixw9EZrsqfourjXbjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 26398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3267,
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

_source line 224 · 2026-05-18T07:08:52.700Z_

<details><summary>↩ Tool result · `toolu_014WyPuvfMMbBafWjPzucQQQ`</summary>

```text
Web search results for query: "Yi-1.5 9B base model huggingface 01.AI 2024 2025"

Links: [{"title":"01-ai (01-ai)","url":"https://huggingface.co/01-ai"},{"title":"GitHub - 01-ai/Yi-1.5: Yi-1.5 is an upgraded version of Yi, delivering stronger performance in coding, math, reasoning, and instruction-following capability. · GitHub","url":"https://github.com/01-ai/Yi-1.5"},{"title":"01-ai/Yi-1.5-9B · Hugging Face","url":"https://huggingface.co/01-ai/Yi-1.5-9B"},{"title":"Paper page - Yi: Open Foundation Models by 01.AI","url":"https://huggingface.co/papers/2403.04652"},{"title":"01-ai/Yi-1.5-9B-Chat-16K · Hugging Face","url":"https://huggingface.co/01-ai/Yi-1.5-9B-Chat-16K"},{"title":"Yi 1.5 34B | Open Laboratory","url":"https://openlaboratory.ai/models/yi-1_5-34b"},{"title":"01-ai/Yi-Coder-1.5B-Chat · Hugging Face","url":"https://huggingface.co/01-ai/Yi-Coder-1.5B-Chat"},{"title":"Models – Hugging Face","url":"https://huggingface.co/models"},{"title":"01-ai/Yi-1.5-9B · extended context","url":"https://huggingface.co/01-ai/Yi-1.5-9B/discussions/1"},{"title":"01-ai/Yi-1.5-9B-32K · Hugging Face","url":"https://huggingface.co/01-ai/Yi-1.5-9B-32K"}]

Based on the search results, here's what I found about the Yi-1.5 9B base model from 01.AI on Hugging Face:

## Overview
Yi-1.5 is an upgraded version of Yi, delivering stronger performance in coding, math, reasoning, and instruction-following capability. The Yi-1.5 series models were open-sourced on 2024-05-13, further improving coding, math, reasoning, and instruction-following abilities.

## Model Availability
The Yi 1.5 family includes multiple parameter scales and configurations, such as 6B, 9B, and 34B models, in both base and chat forms, and offers long-context and multimodal versions. The Yi-1.5-9B base model is available on Hugging Face at the official 01-ai organization.

## Performance
Yi-1.5-9B is the top performer among similarly sized open-source models. The base model achieves reported scores of 76.3 on MMLU, 54.3 on BBH, and 81.4 on C-Eval.

## Architecture
Yi 1.5 34B is a 34.4 billion parameter decoder-only Transformer language model featuring Grouped-Query Attention and SwiGLU activations, trained on 3.1 trillion bilingual tokens.

The model also has extended context variants available, including the Yi-1.5-9B-32K version that supports longer input sequences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "fdeb63c5-cc8f-4859-b4c6-2c3a0637b563"
}
```

</details>

---

### System

_source line 225_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Qwen3 14B base model huggingface benchmark 2025",
  "usage": {
    "total_tokens": 38936,
    "tool_uses": 23,
    "duration_ms": 77208
  },
  "last_tool_name": "WebSearch",
  "uuid": "393cc051-b78a-4028-9800-5420c8f9b618",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 226_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0115L1pj43aEA4fKbYJrBRAJ`</summary>

```json
{
  "query": "Qwen3 14B base model huggingface benchmark 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "0fcf659c-decf-426d-970b-1acf08805792",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TTynS6ZSPsB6GQxX3BZuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 974,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 32583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4681,
        "ephemeral_1h_input_tokens": 0
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

_source line 227 · 2026-05-18T07:08:58.935Z_

<details><summary>↩ Tool result · `toolu_01PtZj1rmNwwwPryZKyp3r3x`</summary>

```text
Web search results for query: "Gemma 3 7B 12B base model HuggingFace release date 2025 benchmark parameters"

Links: [{"title":"Gemma 3 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma3"},{"title":"Gemma 3 Release - a google Collection","url":"https://huggingface.co/collections/google/gemma-3-release"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"Google's Gemma 3: Features, Benchmarks, Performance and Implementation","url":"https://www.analyticsvidhya.com/blog/2025/03/gemma-3/"},{"title":"google/gemma-3-27b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-it"},{"title":"Gemma 3 12B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gemma-3-12b-it"},{"title":"google/gemma-7b · Hugging Face","url":"https://huggingface.co/google/gemma-7b"},{"title":"Gemma releases | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/releases"},{"title":"Gemma 3: Google’s new open model based on Gemini 2.0","url":"https://blog.google/technology/developers/gemma-3/"}]

Based on the search results, here's the information about Gemma 3:

## Model Sizes and Parameters

Gemma 3 is a multimodal model with pretrained and instruction-tuned variants, available in 1B, 13B, and 27B parameters. However, other sources indicate it comes in four distinct sizes – 1B, 4B, 12B, and 27B parameters with both base (pre-trained) and instruction-tuned variants. Note that there is no 7B variant in Gemma 3; the search results mention a 4B and 12B model instead.

## Release Date

Gemma 3 12B was released on March 12, 2025 by Google.

## Training Data

The 27B model was trained with 14 trillion tokens, the 12B model was trained with 12 trillion tokens, 4B model was trained with 4 trillion tokens and 1B with 2 trillion tokens.

## Key Features and Benchmarks

Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions. 

Regarding performance, Gemma 3 delivers state-of-the-art performance for its size, outperforming Llama3-405B, DeepSeek-V3 and o3-mini in preliminary human preference evaluations on LMArena's leaderboard.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "9fb907b4-5ef6-485b-8a96-417e4ee85b12"
}
```

</details>

---

### System

_source line 228_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for OLMo 2 7B 13B benchmark MMLU scores training toke…",
  "usage": {
    "total_tokens": 38988,
    "tool_uses": 24,
    "duration_ms": 80973
  },
  "last_tool_name": "WebSearch",
  "uuid": "108b5a14-0282-4a98-9ca2-579d89f8f674",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 229_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014pNScz91HxxLov4auhkB2G`</summary>

```json
{
  "query": "OLMo 2 7B 13B benchmark MMLU scores training tokens 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "0b2448c2-9b31-427b-8d2d-6daf361e0ed9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TTynS6ZSPsB6GQxX3BZuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 974,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 32583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4681,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 230_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Gemma 2 9B base model huggingface benchmark 2024",
  "usage": {
    "total_tokens": 39040,
    "tool_uses": 25,
    "duration_ms": 81056
  },
  "last_tool_name": "WebSearch",
  "uuid": "4acdecb0-170f-48f8-abe9-47406cf52682",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 231_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WgBEHpo4QiDgevicEsueoh`</summary>

```json
{
  "query": "Gemma 2 9B base model huggingface benchmark 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "432ab22e-7e66-4ad1-808d-57d03c4ee5a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TTynS6ZSPsB6GQxX3BZuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 974,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 32583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4681,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 232_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for StarCoder2 7B 15B base model huggingface 2024 2025",
  "usage": {
    "total_tokens": 39092,
    "tool_uses": 26,
    "duration_ms": 81156
  },
  "last_tool_name": "WebSearch",
  "uuid": "93376947-c995-4306-a2a4-db4bab980f39",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 233_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LJZdd6cx826GbwmJ13aSYQ`</summary>

```json
{
  "query": "StarCoder2 7B 15B base model huggingface 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "70a5f23f-dabc-4ad9-acb8-50c87a274f5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TTynS6ZSPsB6GQxX3BZuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 974,
      "cache_creation_input_tokens": 4681,
      "cache_read_input_tokens": 32583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4681,
        "ephemeral_1h_input_tokens": 0
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

_source line 234 · 2026-05-18T07:08:59.722Z_

<details><summary>↩ Tool result · `toolu_013HYTL2dHVWtVEVhtKkDC36`</summary>

```text
Web search results for query: "Qwen3 7B 8B 14B base model HuggingFace release date benchmark MMLU parameters 2025"

Links: [{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen/Qwen3.5-9B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-9B"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen/Qwen3.5-0.8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-0.8B"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"Qwen/Qwen3.5-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-27B"},{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"GitHub - QwenLM/Qwen: The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen"}]

Based on the search results, here's the information about Qwen3 models:

## Release Date and Model Sizes

Qwen3 was announced as the latest addition to the Qwen family of large language models, with the release occurring in 2025. Six dense models were open-weighted, including Qwen3-32B, Qwen3-14B, Qwen3-8B, Qwen3-4B, Qwen3-1.7B, and Qwen3-0.6B, under Apache 2.0 license.

## Model Parameters and Performance

The overall performance of Qwen3 dense base models matches that of Qwen2.5 base models with more parameters. For instance, Qwen3-1.7B/4B/8B/14B/32B-Base performs as well as Qwen2.5-3B/7B/14B/32B/72B-Base, respectively.

## MMLU Benchmark

The search results reference MMLU benchmark testing. For MMLU-ProX, they report the averaged accuracy on 29 languages. However, the specific MMLU scores are mentioned as being available in detailed evaluation results but are not provided in the excerpts returned.

## HuggingFace Availability

The post-trained models and their pre-trained counterparts are now available on platforms like Hugging Face, ModelScope, and Kaggle. You can access the base models directly on HuggingFace's model hub with model IDs like `Qwen/Qwen3-8B-Base`, `Qwen/Qwen3-14B-Base`, etc.

For detailed benchmark results including specific MMLU scores, you may want to refer to the official Qwen blog post or the technical report mentioned in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "72109dc4-e0ef-4f78-b8f2-b7f3df63e2d3"
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-18T07:09:01.040Z_

<details><summary>↩ Tool result · `toolu_01E4hPcgTXBxwZ8ctz3NfZHi`</summary>

```text
Web search results for query: "Llama 4 Scout Maverick 7B 8B parameters MoE active base model HuggingFace 2025"

Links: [{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"},{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"Evolution of Meta’s LLaMA Models and Parameter-Efficient Fine-Tuning of Large Language Models: A Survey","url":"https://arxiv.org/html/2510.12178v1"},{"title":"meta-llama/Llama-4-Scout-17B-16E · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E"},{"title":"Llama4 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/llama4"},{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"Llama 4 (Scout/Maverick) - D-Central","url":"https://d-central.tech/ai/model/llama-4/"},{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://github.com/huggingface/blog/blob/main/llama4-release.md"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct"},{"title":"meta-llama/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct"}]

Based on the search results, here's detailed information about Llama 4 Scout and Maverick:

## Model Parameters and Architecture

Llama 4 Maverick (~400B) and Llama 4 Scout (~109B) were released by Meta in 2025. Both models feature Mixture of Experts (MoE) architecture:

- Both are Mixture of Experts (MoE) models with 17B active parameters
- Llama 4 Maverick with 17B active parameters out of ~400B total, with 128 experts
- Llama 4 Scout also has 17B active parameters out of ~109B total, using just 16 experts

## MoE Architecture Details

The two models differ in their expert implementation:

- Llama Scout is a full MoE consisting of 16 experts
- Llama Maverick uses 128 experts, but MoE and dense layers alternate. Therefore, experts are applied in half of the layers

## Availability on HuggingFace

Both Llama 4 Maverick and Llama 4 Scout model weights are available directly on the Hugging Face Hub under the meta-llama organization. This includes both base and instruction tuned variants.

## Context Length and Training Data

The Llama 4 models were pre-trained with a context length of 256K. The Instruct models were fine-tuned to support much larger context lengths: 1M in the large 128 experts version (Maverick), and 10M (!) for the 16 experts version (Scout).

Llama 4 Scout was pretrained on ~40 trillion tokens and Llama 4 Maverick was pretrained on ~22 trillion tokens of multimodal data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "c965c21f-1f88-449f-9a5d-d53e690d1b07"
}
```

</details>

---

### Tool result

_source line 236 · 2026-05-18T07:09:02.681Z_

<details><summary>↩ Tool result · `toolu_0115L1pj43aEA4fKbYJrBRAJ`</summary>

```text
Web search results for query: "Qwen3 14B base model huggingface benchmark 2025"

Links: [{"title":"Qwen/Qwen3-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"nvidia/Qwen3-14B-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Qwen3-14B-NVFP4"},{"title":"unsloth/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/unsloth/Qwen3-14B-Base"},{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"nvidia/Qwen3-14B-FP8 · Hugging Face","url":"https://huggingface.co/nvidia/Qwen3-14B-FP8"},{"title":"Quantized Models for Qwen/Qwen3-14B – Hugging Face","url":"https://huggingface.co/models?other=base_model%3Aquantized%3AQwen%2FQwen3-14B"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/qwen3"}]

Based on the search results, here's what I found about the Qwen3 14B base model and its 2025 benchmarks:

## Model Specifications

Qwen3-14B-Base has 14.8B parameters (13.2B non-embedding parameters), 40 layers, 40 attention heads (Q) and 8 for KV with Group Query Attention (GQA), and a context length of 32,768 tokens.

## Benchmark Performance

Qwen3-14B-Base performs as well as Qwen2.5-32B-Base, and notably outperforms larger Qwen2.5 models in areas like STEM, coding, and reasoning.

More specifically, Qwen3-14B-Base achieves very competitive results compared to Qwen2.5-32B-Base, demonstrating significant efficiency gains.

## Training and Performance

Qwen3 is pre-trained on 36 trillion tokens across 119 languages, tripling the language coverage of Qwen2.5, with a rich mix of high-quality data including coding, STEM, reasoning, book, multilingual, and synthetic data.

## Documentation Reference

Detailed evaluation results are reported in a blog post, and transformers version 4.51.0 or higher is required to use the model. The official technical report was published in May 2025 (arXiv:2505.09388).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "6bd2b8c4-1bdd-42ad-bda2-07259b3a46e6"
}
```

</details>

---

### System

_source line 237_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Qwen3 14B base training tokens data size MMLU ben…",
  "usage": {
    "total_tokens": 32869,
    "tool_uses": 17,
    "duration_ms": 78426
  },
  "last_tool_name": "WebSearch",
  "uuid": "5ed9591b-03b8-4364-9b93-3617e9b6d584",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 238_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WNo2ZGCJjkoS9Y9idP5kdi`</summary>

```json
{
  "query": "Qwen3 14B base training tokens data size MMLU benchmark score release date April 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "2b3ba1ba-9ae4-4880-a79a-efa6c3a1bb14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD522mNXRwZzytfigMGV1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 29665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3169,
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

### System

_source line 239_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Gemma 3 12B base pretrained \"gemma-3-12b-pt\" Hugg…",
  "usage": {
    "total_tokens": 32870,
    "tool_uses": 18,
    "duration_ms": 79427
  },
  "last_tool_name": "WebSearch",
  "uuid": "8224cfb8-5c6d-424d-a7c5-3c50306fb2ed",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 240_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GvgZjFUCLx83GyN8QLCnbk`</summary>

```json
{
  "query": "Gemma 3 12B base pretrained \"gemma-3-12b-pt\" HuggingFace gated benchmark MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "9fd5f462-fc5e-4da4-8dda-47fa28035bf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD522mNXRwZzytfigMGV1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 29665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3169,
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

### System

_source line 241_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Mistral Small 3 7B 8B base model 2025 HuggingFace…",
  "usage": {
    "total_tokens": 32871,
    "tool_uses": 19,
    "duration_ms": 79829
  },
  "last_tool_name": "WebSearch",
  "uuid": "b096933b-e72f-4fe9-b79f-229b3b0726a6",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 242_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012zdEe8pjsiA4f1fqpZ6dCA`</summary>

```json
{
  "query": "Mistral Small 3 7B 8B base model 2025 HuggingFace parameters benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "163020bb-0d72-491c-a57f-562c5eeeaf72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD522mNXRwZzytfigMGV1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 29665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3169,
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

_source line 243 · 2026-05-18T07:09:06.243Z_

<details><summary>↩ Tool result · `toolu_014pNScz91HxxLov4auhkB2G`</summary>

```text
Web search results for query: "OLMo 2 7B 13B benchmark MMLU scores training tokens 2024"

Links: [{"title":"OLMo 1.7–7B: A 24 point improvement on MMLU | Ai2","url":"https://allenai.org/blog/olmo-1-7-7b-a-24-point-improvement-on-mmlu-92b43f7d269d"},{"title":"OLMo 2: The best fully open language model to date | Ai2","url":"https://allenai.org/blog/olmo2"},{"title":"OLMo release notes | Ai2","url":"https://allenai.org/olmo/release-notes"},{"title":"2 OLMo 2 Furious OLMo Team Pete Walsh 1 Luca Soldaini 1 Dirk Groeneveld 1","url":"https://arxiv.org/pdf/2501.00656"},{"title":"allenai/OLMo-2-1124-7B-Instruct Free Chat Online - skywork.ai - Skywork ai","url":"https://skywork.ai/blog/models/allenai-olmo-2-1124-7b-instruct-free-chat-online-skywork-ai/"},{"title":"OLMo 2 7B vs 13B: Research Performance and Resource Analysis | Markaicode","url":"https://markaicode.com/vs/olmo-2-7b-vs-13b/"},{"title":"OLMo 1.7–7B: A 24 point improvement on MMLU | by Ai2 | Ai2 Blog | Medium","url":"https://medium.com/ai2-blog/olmo-1-7-7b-a-24-point-improvement-on-mmlu-92b43f7d269d"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"(PDF) 2 OLMo 2 Furious","url":"https://www.researchgate.net/publication/387671074_2_OLMo_2_Furious"},{"title":"allenai/OLMo-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-7B"}]

Based on the search results, here's the key information about OLMo 2 7B and 13B models:

## Training Tokens

OLMo 2 is a family of 7B and 13B models trained on up to 5T tokens. More specifically, OLMo 2 7B is trained for approximately one epoch on the first-stage dataset, while OLMo 2 13B is trained for 1.2 epochs up to 5T tokens.

## MMLU Benchmark Scores

OLMo 2 achieved MMLU scores of 63.7 for the 7B model and 67.5 for the 13B model. This represents a 9-point increase in MMLU compared to the original OLMo 7B model.

## Training Approach

OLMo 2 is pretrained in two stages using a curriculum approach. In the first stage, which covers over 90% of the total pretraining budget, the models use OLMo-Mix-1124, a collection of approximately 3.9 trillion tokens sourced from DCLM, Dolma, Starcoder, and Proof Pile II. The second stage curates a mixture of high-quality web data and domain-specific content, consisting of 843 billion tokens total, sampled to create mixes of 50 billion, 100 billion, and 300 billion tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "1f1ca039-5b2f-4854-9ac5-e1595d6ac861"
}
```

</details>

---

### Tool result

_source line 244 · 2026-05-18T07:09:07.013Z_

<details><summary>↩ Tool result · `toolu_01WgBEHpo4QiDgevicEsueoh`</summary>

```text
Web search results for query: "Gemma 2 9B base model huggingface benchmark 2024"

Links: [{"title":"google/gemma-2-9b · Hugging Face","url":"https://huggingface.co/google/gemma-2-9b"},{"title":"RedHatAI/gemma-2-9b-it-FP8 · Hugging Face","url":"https://huggingface.co/RedHatAI/gemma-2-9b-it-FP8"},{"title":"google/gemma-2-2b · Hugging Face","url":"https://huggingface.co/google/gemma-2-2b"},{"title":"bartowski/gemma-2-9b-it-GGUF · Hugging Face","url":"https://huggingface.co/bartowski/gemma-2-9b-it-GGUF"},{"title":"neuralmagic/gemma-2-9b-it-FP8 · Hugging Face","url":"https://huggingface.co/neuralmagic/gemma-2-9b-it-FP8"},{"title":"Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/html/2408.00118v2"},{"title":"google/gemma-2-2b-it · Hugging Face","url":"https://huggingface.co/google/gemma-2-2b-it"},{"title":"Gemma2 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/gemma2"},{"title":"google/gemma-2-27b · Hugging Face","url":"https://huggingface.co/google/gemma-2-27b"},{"title":"google/recurrentgemma-9b · Hugging Face","url":"https://huggingface.co/google/recurrentgemma-9b"}]

Based on the search results, here's information about the Gemma 2 9B base model and its benchmark performance:

## Model Overview

Gemma 2 is a family of language models with pretrained and instruction-tuned variants, available in 2B, 9B, 27B parameters. The 9B model was trained with 8 trillion tokens, and the 2B and 9B models are trained with knowledge distillation.

## Architecture

The architecture features interleaved local attention (4096 tokens) and global attention (8192 tokens) and grouped-query attention (GQA) to increase inference performance.

## Benchmark Performance

The search results include benchmark information for the Gemma 2 9B instruction-tuned variant. The unquantized gemma-2-9b-it model achieves an average score of 73.23 on the OpenLLM benchmark (version 1).

Additionally, there was a massive improvement in the models compared to previous versions, by up to 10% in some benchmarks for the 9B model. Gemma 2 significantly advances state-of-the-art performance relative to comparable-scale open models and are even competitive with some models more than twice their size.

The Gemma 2 9B model was released in July 2024 and is available on Hugging Face for download and use.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "64e2c99d-153c-4ca4-a63a-ddab7fddc48d"
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-18T07:09:07.107Z_

<details><summary>↩ Tool result · `toolu_01LJZdd6cx826GbwmJ13aSYQ`</summary>

```text
Web search results for query: "StarCoder2 7B 15B base model huggingface 2024 2025"

Links: [{"title":"Starcoder2 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/starcoder2"},{"title":"bigcode/starcoder2-15b · Hugging Face","url":"https://huggingface.co/bigcode/starcoder2-15b"},{"title":"GitHub - bigcode-project/starcoder2: Home of StarCoder2! · GitHub","url":"https://github.com/bigcode-project/starcoder2"},{"title":"bigcode/starcoder2-7b · Hugging Face","url":"https://huggingface.co/bigcode/starcoder2-7b"},{"title":"Starcoder2","url":"https://huggingface.co/docs/transformers/v4.46.0/model_doc/starcoder2"},{"title":"StarCoder2: AI-Powered Code Generation by ServiceNow, Hugging Face and NVIDIA | by My Social | 𝐀𝐈 𝐦𝐨𝐧𝐤𝐬.𝐢𝐨 | Medium","url":"https://medium.com/aimonks/starcoder2-ai-powered-code-generation-by-servicenow-hugging-face-and-nvidia-7f51763af0e6"},{"title":"blog/starcoder2.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/starcoder2.md"},{"title":"bigcode (BigCode)","url":"https://huggingface.co/bigcode"},{"title":"FineTuning StarCoder2 on Google Colab T4 GPU","url":"https://medium.com/codex/finetuning-starcoder2-on-google-colab-t4-gpu-a7a416efde4e"},{"title":"StarCoder 2 is a code-generating AI that runs on most GPUs | TechCrunch","url":"https://techcrunch.com/2024/02/28/starcoder-2-is-a-code-generating-ai-that-runs-on-most-gpus/"}]

Based on the search results, here's what I found about StarCoder2 7B and 15B base models on Hugging Face:

## Release Information

StarCoder2 was released on February 29, 2024 and added to Hugging Face Transformers on February 28, 2024.

## Model Overview

StarCoder2 is a family of open LLMs for code and comes in 3 different sizes with 3B, 7B and 15B parameters.

## StarCoder2-7B Details

StarCoder2-7B is a 7B parameter model trained on 17 programming languages from The Stack v2, with opt-out requests excluded. The model uses Grouped Query Attention, a context window of 16,384 tokens with a sliding window attention of 4,096 tokens, and was trained using the Fill-in-the-Middle objective on 3.5+ trillion tokens.

## StarCoder2-15B Details

StarCoder2-15B is a 15B parameter model trained on 600+ programming languages from The Stack v2, with opt-out requests excluded. The model uses Grouped Query Attention, a context window of 16,384 tokens with a sliding window attention of 4,096 tokens, and was trained using the Fill-in-the-Middle objective on 4+ trillion tokens.

## Licensing

The models are licensed under the BigCode OpenRAIL-M v1 license agreement.

Both models are available on Hugging Face Hub under the `bigcode` organization and can be accessed via the model IDs `bigcode/starcoder2-7b` and `bigcode/starcoder2-15b`.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "aefd724c-ba73-4983-8a17-41b126011cde"
}
```

</details>

---

### System

_source line 246_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Falcon3 7B 10B MMLU benchmark scores training dat…",
  "usage": {
    "total_tokens": 43106,
    "tool_uses": 27,
    "duration_ms": 91405
  },
  "last_tool_name": "WebSearch",
  "uuid": "36ee1eaa-6bb9-4b41-b1a1-e70e3f1579c3",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 247_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FhcwKwrrSymitQTfCHJokP`</summary>

```json
{
  "query": "Falcon3 7B 10B MMLU benchmark scores training data 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "5a86e11a-43ac-4ab3-8e06-edfe3149383b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZH1gmWYngF8M89n3ztzXs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4942,
      "cache_read_input_tokens": 37264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 248 · 2026-05-18T07:09:10.583Z_

<details><summary>↩ Tool result · `toolu_01WNo2ZGCJjkoS9Y9idP5kdi`</summary>

```text
Web search results for query: "Qwen3 14B base training tokens data size MMLU benchmark score release date April 2025"

Links: [{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3 14B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-14b/"},{"title":"An Empirical Study of Qwen3 Quantization","url":"https://arxiv.org/html/2505.02214v1"},{"title":"2025-05-13 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://cdn.jsdelivr.net/gh/yanfeng98/paper-is-all-you-need/papers/00069-Qwen3_Technical_Report.pdf"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"},{"title":"An empirical study of Qwen3 quantization | Visual Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44267-026-00114-4"},{"title":"Qwen3 4B | Open Laboratory","url":"https://openlaboratory.ai/models/qwen3-4b"},{"title":"Qwen3 14B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/qwen3-14b-instruct"},{"title":"Qwen3 0.6B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-0_6b/"},{"title":"Home GPU LLM Leaderboard: Best Open Source Models by VRAM Tier with Token/s Benchmarks | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/home-gpu-llm-leaderboard/"}]

Based on the search results, here's the information about Qwen3 14B:

## Key Information:

**Release Date:** Qwen3-14B was officially released on April 29, 2025.

**MMLU Benchmark Score:** Qwen3-14B-Base attains scores of 81.05 on MMLU.

**Training Data:** While the search results don't provide the exact training token count specifically for Qwen3-14B, they indicate that the Qwen3 series was developed by Alibaba Cloud's Qwen team and represents a significant advancement in their model lineup.

**Model Size:** Qwen3-14B is a dense model with 14 billion total parameters.

The model demonstrates strong performance across multiple benchmarks and includes hybrid "thinking" and "non-thinking" modes for flexible reasoning capabilities. The model and its weights are made publicly available under the Apache 2.0 license.

Note: The search results did not contain specific information about the exact data size (in terms of training tokens) for Qwen3-14B's pretraining, though this data may be available in the full technical report.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "babca3c5-0e2f-4d6d-80ae-e06d7df4a548"
}
```

</details>

---

### System

_source line 249_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Gemma 3 release date January March 2025 google 4B…",
  "usage": {
    "total_tokens": 43151,
    "tool_uses": 28,
    "duration_ms": 92331
  },
  "last_tool_name": "WebSearch",
  "uuid": "2e54d8f6-90d2-4824-8916-2c69f608177f",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 250_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NFkezhfys1NQ7yj79NC3ii`</summary>

```json
{
  "query": "Gemma 3 release date January March 2025 google 4B 12B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "1fe5c4c2-385c-4806-84b9-3c21fba2f167",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZH1gmWYngF8M89n3ztzXs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4942,
      "cache_read_input_tokens": 37264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 251_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for OLMo 3 7B base model allenai huggingface 2025",
  "usage": {
    "total_tokens": 43196,
    "tool_uses": 29,
    "duration_ms": 92863
  },
  "last_tool_name": "WebSearch",
  "uuid": "8343a4ac-f9e6-470d-8dd7-6e999a586255",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 252_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PaC8nq3HA8YvDRJXxDUTaM`</summary>

```json
{
  "query": "OLMo 3 7B base model allenai huggingface 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "05d50d94-2c16-49b8-b4e9-cb16d282f365",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZH1gmWYngF8M89n3ztzXs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4942,
      "cache_read_input_tokens": 37264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-18T07:09:11.500Z_

<details><summary>↩ Tool result · `toolu_01GvgZjFUCLx83GyN8QLCnbk`</summary>

```text
Web search results for query: "Gemma 3 12B base pretrained "gemma-3-12b-pt" HuggingFace gated benchmark MMLU"

Links: [{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"google/gemma-3-12b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-pt"},{"title":"cjvt/GaMS3-12B-Instruct · Hugging Face","url":"https://huggingface.co/cjvt/GaMS3-12B-Instruct"},{"title":"gemma3:12b","url":"https://ollama.com/library/gemma3:12b"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"litert-community/Gemma3-12B-IT · Hugging Face","url":"https://huggingface.co/litert-community/Gemma3-12B-IT"},{"title":"google/gemma-3-12b-pt at main","url":"https://huggingface.co/google/gemma-3-12b-pt/tree/main"},{"title":"Gemma 3 12B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gemma-3-12b-it"},{"title":"INSAIT-Institute/MamayLM-Gemma-3-12B-IT-v1.0 · Hugging Face","url":"https://huggingface.co/INSAIT-Institute/MamayLM-Gemma-3-12B-IT-v1.0"}]

Based on the search results, here's what I found regarding Gemma 3 12B base pretrained model:

## Model Access
To access Gemma on Hugging Face, you're required to review and agree to Google's usage license, and you need to be logged in to Hugging Face. The model is indeed gated on HuggingFace.

## Model Specifications
Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants. Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions.

## MMLU Benchmark
Regarding MMLU benchmarks, the search results indicate that Gemma 3 has been evaluated across benchmarks like MMLU-Pro (27B: 67.5), LiveCodeBench (27B: 29.7), and Bird-SQL (27B: 54.4). However, the specific MMLU benchmark scores for the 12B base pretrained variant ("gemma-3-12b-pt") were not included in the search results. The available benchmark data focuses on the 27B model size.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "fb9a4b45-9344-4b85-a28c-0ba2c83402b9"
}
```

</details>

---

### System

_source line 254_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Llama 3.1 8B base MMLU benchmark training tokens …",
  "usage": {
    "total_tokens": 43241,
    "tool_uses": 30,
    "duration_ms": 93245
  },
  "last_tool_name": "WebSearch",
  "uuid": "c526d7c8-a621-4f4b-a68f-f1146bdf850b",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 255_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RP9eAduRdF9AwM9oR6ovxG`</summary>

```json
{
  "query": "Llama 3.1 8B base MMLU benchmark training tokens 15T 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f3684f2f-cb36-4c44-8de9-677abd897496",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZH1gmWYngF8M89n3ztzXs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4942,
      "cache_read_input_tokens": 37264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 256 · 2026-05-18T07:09:16.812Z_

<details><summary>↩ Tool result · `toolu_01NFkezhfys1NQ7yj79NC3ii`</summary>

```text
Web search results for query: "Gemma 3 release date January March 2025 google 4B 12B"

Links: [{"title":"Gemma releases | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/releases"},{"title":"Gemma 3 - D-Central","url":"https://d-central.tech/ai/model/gemma-3/"},{"title":"Gemma (language model) - Wikipedia","url":"https://en.wikipedia.org/wiki/Gemma_(language_model)"},{"title":"Gemma 3 4B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gemma-3-4b-it"},{"title":"Gemma 3 4B – Try & Compare | Roboflow Playground","url":"https://playground.roboflow.com/models/google/gemma-3-4b"},{"title":"Gemma 3 12B Model Specs, Costs & Benchmarks (April 2026) | Galaxy.ai","url":"https://blog.galaxy.ai/model/gemma-3-12b-it"},{"title":"Introducing Gemma 3: The Developer Guide - Google Developers Blog","url":"https://developers.googleblog.com/en/introducing-gemma3/"},{"title":"Gemma 3 12B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/gemma-3-12b"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"Notes on Google’s Gemma 3","url":"https://simonwillison.net/2025/Mar/12/gemma-3/"}]

Based on the search results, here's what I found about Gemma 3's release:

Gemma 3 was released on March 12, 2025. This was not in January, but rather in March 2025 as part of your search query timeframe.

Google DeepMind's March 2025 Gemma family includes vision-capable models (4B+) with 128K context and official quantization-aware 4-bit variants.

**Available Model Sizes:**
Gemma 3 was offered in 1, 4, 12, and 27 billion parameter sizes with support for over 140 languages. So the 4B and 12B models you mentioned in your query were indeed released as part of the Gemma 3 family.

**Key Features:**
As multimodal models, they support both text and image input. Additionally, Gemma 3 handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities, including structured outputs and function calling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f8d23114-f9b9-4ec6-8e40-1a7bc5c1650b"
}
```

</details>

---

### Tool result

_source line 257 · 2026-05-18T07:09:17.492Z_

<details><summary>↩ Tool result · `toolu_012zdEe8pjsiA4f1fqpZ6dCA`</summary>

```text
Web search results for query: "Mistral Small 3 7B 8B base model 2025 HuggingFace parameters benchmark"

Links: [{"title":"unsloth/Mistral-Small-24B-Base-2501-bnb-4bit · Hugging Face","url":"https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501-bnb-4bit"},{"title":"Mistral 7B","url":"https://mistral.ai/news/announcing-mistral-7b"},{"title":"unsloth/Mistral-Small-24B-Base-2501 · Hugging Face","url":"https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501"},{"title":"NVIDIA-Accelerated Mistral 3 Open Models Deliver Efficiency, Accuracy at Any Scale | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/nvidia-accelerated-mistral-3-open-models-deliver-efficiency-accuracy-at-any-scale/"},{"title":"Mistral Docs","url":"https://docs.mistral.ai/models/overview"},{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"mistralai/Mistral-7B-Instruct-v0.3 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3"},{"title":"mistralai/Mistral-7B-v0.1 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-7B-v0.1"},{"title":"Mistral · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/mistral"},{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"}]

Based on the search results, here's what I found about Mistral models in 2025:

## Mistral Small 3 (2501)

Mistral Small 3 (2501) sets a new benchmark in the "small" Large Language Models category below 70B, boasting 24B parameters and achieving state-of-the-art capabilities comparable to larger models.

## Ministral 3 Series

For smaller models, Mistral released the Ministral 3 family, which includes multiple parameter sizes:

A suite of small, dense high-performance models (called Ministral 3) of sizes 3B, 8B, and 14B, each with Base, Instruct, and Reasoning variants (nine models total) All the models were trained on NVIDIA Hopper GPUs and are now available through Mistral AI on Hugging Face.

## Performance Benchmarks

The Ministral instruct models match or exceed the performance of comparable models while often producing an order of magnitude fewer tokens. Additionally, Ministral 3 8B outperforms the larger Gemma 12B in most of the evaluations (except TriviaQA), highlighting the strong parameter efficiency of Ministral 3 models.

The Ministral reasoning variants can think longer to produce state-of-the-art accuracy amongst their weight class - for instance 85% on AIME '25 with our 14B variant.

All these models are available on HuggingFace under the Apache 2.0 license.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "4de84d8a-dcaf-4a48-82d5-25870d65900f"
}
```

</details>

---

### Tool result

_source line 258 · 2026-05-18T07:09:18.134Z_

<details><summary>↩ Tool result · `toolu_01PaC8nq3HA8YvDRJXxDUTaM`</summary>

```text
Web search results for query: "OLMo 3 7B base model allenai huggingface 2025"

Links: [{"title":"allenai/Olmo-3-1025-7B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1025-7B"},{"title":"allenai/Olmo-3-1125-32B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1125-32B"},{"title":"Olmo 3 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-3"},{"title":"allenai/Olmo-3-7B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Instruct"},{"title":"allenai/Olmo-3-7B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think"},{"title":"allenai/Olmo-3.1-32B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-32B-Instruct"},{"title":"allenai/Olmo-3.1-32B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-32B-Think"},{"title":"allenai/Olmo-3-7B-RL-Zero-Math · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Math"},{"title":"Mungert/Olmo-3-1025-7B-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/Olmo-3-1025-7B-GGUF"},{"title":"allenai/Olmo-3-7B-Think-DPO · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think-DPO"}]

Based on the web search results, here's what I found about the OLMo 3 7B base model from Allen AI on Hugging Face:

## Overview

OLMo 3 is a new family of 7B and 32B models, with a suite that includes Base, Instruct, and Think variants. The Base models were trained using a staged training approach.

## Training Details

The main dataset used is dolma3_6T-mix-1025, consisting of 5.93T tokens with coverage of 97.53%+ of total pretraining budget. The training mix composition includes 20% code, 28% web pages, 19% math, 14% QA, 8% thinking, 6% instruction, and 5% PDFs.

## Model Availability

The base model is available on Hugging Face at `allenai/Olmo-3-1025-7B`. The research paper and details are available at https://allenai.org/papers/olmo3.

## Licensing and Usage

This model is licensed under Apache 2.0 and is intended for research and educational use in accordance with AI2's Responsible Use Guidelines.

The search results show this is a relatively recent release, with information from January 2026 regarding the October 2025 model version.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "4627875b-9362-4861-a566-bcc0a864a120"
}
```

</details>

---

### Tool result

_source line 259 · 2026-05-18T07:09:19.207Z_

<details><summary>↩ Tool result · `toolu_01FhcwKwrrSymitQTfCHJokP`</summary>

```text
Web search results for query: "Falcon3 7B 10B MMLU benchmark scores training data 2024"

Links: [{"title":"Welcome to the Falcon 3 Family of Open Models! | Falcon","url":"https://falcon-lm.github.io/blog/falcon-3/"},{"title":"Welcome to the Falcon 3 Family of Open Models!","url":"https://huggingface.co/blog/falcon3"},{"title":"🐺🐦‍⬛ LLM Comparison/Test: DeepSeek-V3, QVQ-72B-Preview, Falcon3 10B, Llama 3.3 70B, Nemotron 70B in my updated MMLU-Pro CS benchmark","url":"https://huggingface.co/blog/wolfram/llm-comparison-test-2025-01-02"},{"title":"tiiuae/Falcon3-7B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-7B-Base"},{"title":"tiiuae/Falcon3-1B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-1B-Base"},{"title":"Falcon LLM Architecture: Deep Dive into its Design and Performance | SaM Solutions","url":"https://sam-solutions.com/blog/falcon-llm-architecture/"},{"title":"Experience Advanced AI Anywhere with Falcon 3's Lightweight Design","url":"https://www.analyticsvidhya.com/blog/2024/12/falcon-3/"},{"title":"TII launches world’s most powerful SLMs under 13B parameters","url":"https://www.middleeastainews.com/p/tii-launches-most-powerful-slm"},{"title":"Falcon 3 series sets new benchmarks for open-source LLMs on a single GPU","url":"https://the-decoder.com/abu-dhabis-tii-releases-falcon-3-setting-new-benchmarks-for-efficient-open-source-ai-models/"},{"title":"Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance | Falcon","url":"https://falcon-lm.github.io/blog/falcon-h1/"}]

Based on the search results, here's the information about Falcon3 7B and 10B MMLU benchmark scores and training data:

## MMLU Benchmark Scores

Falcon3-7B-Base achieved scores of 67.4 on MMLU and 39.2 on MMLU-PRO, while Falcon3-10B-Base achieved 73.1 on MMLU and 42.5 on MMLU-PRO respectively.

## Training Data

The 7B model was trained on 14 trillion tokens using 1024 H100 GPU chips, leveraging web, code, STEM, and curated high-quality multilingual data. The 10B model was created by upscaling the 7B model with continued pre-training using 2 trillion tokens of high-quality data.

Falcon 3 was trained in four major languages: English, Spanish, Portuguese, and French.

## Performance Context

Falcon3-10B-Base achieves state-of-the-art zero-shot and few-shot performance for models under 13B parameters. Falcon3-7B-Base demonstrates top performance, on par with Qwen2.5-7B, among models under the 9B scale.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "2accc153-854e-41c8-9449-5e2d5e25d2a5"
}
```

</details>

---

### Tool result

_source line 260 · 2026-05-18T07:09:20.089Z_

<details><summary>↩ Tool result · `toolu_01RP9eAduRdF9AwM9oR6ovxG`</summary>

```text
Web search results for query: "Llama 3.1 8B base MMLU benchmark training tokens 15T 2024"

Links: [{"title":"Llama 3.1 8B Instruct - NGC Catalog - NVIDIA","url":"https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/llama-3_1-8b-instruct-nemo"},{"title":"MLPerf Training Adds Llama 3.1 8B Benchmark - MLCommons","url":"https://mlcommons.org/2025/10/training-llama-3-1-8b/"},{"title":"Llama 3.1 8B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/llama-3-1-instruct-8b"},{"title":"Introducing Meta Llama 3: The most capable openly available LLM to date","url":"https://ai.meta.com/blog/meta-llama-3/"},{"title":"Llama 3.1","url":"https://www.llama.com/llama3_1/"},{"title":"Llama 3's Performance Benchmark Values Explained | by Ingrid Stevens | Medium","url":"https://medium.com/@ingridwickstevens/more-llm-acronyms-an-explainer-on-llama-3s-performance-benchmark-values-36722c6dcabb"},{"title":"Llama 3.2: Revolutionizing edge AI and vision with open, customizable models","url":"https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/"},{"title":"llama-models/models/llama3_1/eval_details.md at main · meta-llama/llama-models","url":"https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/eval_details.md"},{"title":"Meta's New Llama 3.1 AI Model: Use Cases & Benchmark","url":"https://research.aimultiple.com/meta-llama/"},{"title":"Llama 3.1 Guide: What to know about Meta's new 405B model and its data","url":"https://kili-technology.com/large-language-models-llms/llama-3-1-guide-what-to-know-about-meta-s-new-405b-model-and-its-data"}]

Based on the search results, I found relevant information about Llama 3.1 8B's training and MMLU benchmark performance:

## Training Tokens

Llama 3.1 used about 15T multilingual tokens, compared to 1.8T tokens for Llama 2. This confirms the 15T token training mentioned in your query.

## MMLU Benchmark Performance

For the Llama 3.1 8B base model specifically:

- For the pre-trained 8B model, the micro average MMLU score is 65.6 for the 5-shot config

The search results also show that Llama 3.1 scores 89 on the MMLU Chat (0-shot) benchmark, though this appears to be referring to the instruction-tuned version rather than the base model.

The official Meta evaluation details indicate that different evaluation configurations produce different scores, with the base pre-trained 8B model achieving 65.6 micro average on MMLU using a 5-shot configuration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "99957111-683b-4f5a-9112-203578f7e63a"
}
```

</details>

---

### System

_source line 261_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Qwen2.5 14B MMLU benchmark base model training to…",
  "usage": {
    "total_tokens": 46945,
    "tool_uses": 31,
    "duration_ms": 104769
  },
  "last_tool_name": "WebSearch",
  "uuid": "dc5eb993-983a-4712-87a2-f658ace2a6da",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 262_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P5bNa3iv6SNa5xQKDh7j6P`</summary>

```json
{
  "query": "Qwen2.5 14B MMLU benchmark base model training tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "2ba850e7-2e1f-4ac2-bb22-91c600edd9b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Tv4BNUpe83tjC98U8uGKF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3658,
      "cache_read_input_tokens": 42206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

_source line 263_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Gemma 4 base model release 2026 huggingface google",
  "usage": {
    "total_tokens": 46991,
    "tool_uses": 32,
    "duration_ms": 105253
  },
  "last_tool_name": "WebSearch",
  "uuid": "4f887687-737b-4d77-929b-b6ab8f4dcbfd",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 264_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FHqgLBPxKo5AdbHgYqnHfu`</summary>

```json
{
  "query": "Gemma 4 base model release 2026 huggingface google"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "ca2a55d1-56fd-4a00-a028-6886208d7935",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Tv4BNUpe83tjC98U8uGKF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3658,
      "cache_read_input_tokens": 42206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

_source line 265_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "description": "Searching for Falcon H1 7B 14B hybrid model huggingface 2025",
  "usage": {
    "total_tokens": 47037,
    "tool_uses": 33,
    "duration_ms": 105758
  },
  "last_tool_name": "WebSearch",
  "uuid": "f77b9328-785c-4e26-acd7-3642e19f300a",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 266_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CAcCQMJzPrL5gxnKWUDARF`</summary>

```json
{
  "query": "Falcon H1 7B 14B hybrid model huggingface 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "9f17553e-61aa-440d-975f-31c86133a7ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Tv4BNUpe83tjC98U8uGKF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3658,
      "cache_read_input_tokens": 42206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

_source line 267_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a21ba8d3a3938265b",
  "tool_use_id": "toolu_01BPp8oiLtg786D15Msvztwn",
  "status": "completed",
  "output_file": "",
  "summary": "Search batch 3: Gemma + OLMo",
  "usage": {
    "total_tokens": 32276,
    "tool_uses": 15,
    "duration_ms": 101561
  },
  "uuid": "a2e063ba-b9c5-40fe-9383-3e35dbeda67c",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool result

_source line 268 · 2026-05-18T07:09:24.475Z_

<details><summary>↩ Tool result · `toolu_01BPp8oiLtg786D15Msvztwn`</summary>

```text
Here are all findings compiled in structured format.

---

## Gemma 3 (Google DeepMind)

**Release date:** March 12, 2025 (added to HuggingFace Transformers); public release ~March 25, 2025

**License:** Gemma Terms of Use (custom Google license)

**Gated:** Yes. Requires agreeing to Google's usage license on HuggingFace before downloading.

**Base (pretrained) versions exist:** Yes. All sizes have a `-pt` (pretrained) variant.

| Size | HuggingFace Repo ID | Parameters | Modality | Context Window | Training Tokens | MMLU (base) | HellaSwag (base) |
|------|---------------------|------------|----------|----------------|-----------------|-------------|------------------|
| 1B | `google/gemma-3-1b-pt` | 1B | Text only | 32K | 2T | 38.8% | 62.3 |
| 4B | `google/gemma-3-4b-pt` | 4B | Text + Image | 128K | 4T | 58.1% | 77.2 |
| 12B | `google/gemma-3-12b-pt` | 12B | Text + Image | 128K | 12T | 71.9% | 84.2 |
| 27B | `google/gemma-3-27b-pt` | 27B | Text + Image | 128K | 14T | 76.9% | 85.6 |

**Instruction-tuned counterparts** use the `-it` suffix (e.g., `google/gemma-3-12b-it`).

**Additional notes:**
- 140+ language support
- Trained using knowledge distillation from larger Gemini models
- Trained on TPUv4p, TPUv5p, and TPUv5e hardware
- A 270M text-only variant also exists, trained on 6T tokens
- Gemma 3 4B-IT beats Gemma 2 27B-IT; Gemma 3 27B-IT is comparable to Gemini 1.5 Pro
- Technical report: [arxiv.org/abs/2503.19786](https://arxiv.org/abs/2503.19786)

---

## OLMo 2 (Allen Institute for AI / Ai2)

**License:** Apache 2.0 (fully open, including training data, code, and weights)

**Gated:** No. All models are openly available.

**Base (pretrained) versions exist:** Yes. The base repo IDs below are the pretrained models; instruct/SFT/DPO variants have corresponding suffixes.

| Size | HuggingFace Repo ID | Parameters | Release Date | Training Tokens | MMLU (base) |
|------|---------------------|------------|--------------|-----------------|-------------|
| 1B | `allenai/OLMo-2-0425-1B` | 1B | April 2025 | 4T (+ 50B mid-training) | Not reported in search results |
| 7B | `allenai/OLMo-2-1124-7B` | 7B | November 2024 (updated Dec 31, 2024) | ~4T (Stage 1: 3.9T OLMo-Mix-1124, Stage 2: 50B Dolmino-Mix-1124) | 63.7 |
| 13B | `allenai/OLMo-2-1124-13B` | 13B | November 2024 | Up to 5T | 67.5 |
| 32B | `allenai/OLMo-2-0325-32B` | 32B | March 2025 | Up to 6T | Not reported in search results |

**Instruct variants:**
- `allenai/OLMo-2-1124-7B-Instruct`
- `allenai/OLMo-2-1124-13B-Instruct`
- `allenai/OLMo-2-0325-32B-Instruct`
- `allenai/OLMo-2-0425-1B-Instruct`

**Additional OLMo 2 details:**
- Modality: Text only
- Training data: OLMo-Mix-1124 (Stage 1) + Dolmino-Mix-1124 (Stage 2, mid-training)
- 7B model: trained for ~1 epoch on 3.9T tokens, then 3 runs of 50B token mid-training merged via model souping
- 9-point MMLU increase over original OLMo 7B
- OLMo 2 7B outperforms Llama 3.1 8B on English academic benchmarks
- OLMo 2 13B surpasses Qwen 2.5 7B despite fewer training FLOPs
- OLMo 2 32B is described as "the first fully-open model to outperform GPT-3.5-Turbo and GPT-4o mini" on multi-skill academic benchmarks
- ARC scores: improved from 80.2 to 83.5 for 13B
- Data cutoff: December 2023
- Technical report: [arxiv.org/abs/2501.00656](https://arxiv.org/abs/2501.00656)
- Also note: Ai2 has released **OLMo 3** (`allenai/Olmo-3-1125-32B`) and **OLMo 3.1** (`allenai/Olmo-3.1-32B-Think`), though these are outside your 7B-14B scope

---

## Summary: Models in the 7B-14B Range

For the specific 7B-14B parameter range relevant to the paper:

| Model | Repo ID | Params | Gated | License | Training Data | MMLU |
|-------|---------|--------|-------|---------|---------------|------|
| Gemma 3 12B PT | `google/gemma-3-12b-pt` | 12B | Yes | Gemma ToU | 12T tokens | 71.9% |
| OLMo 2 7B | `allenai/OLMo-2-1124-7B` | 7B | No | Apache 2.0 | ~4T tokens | 63.7% |
| OLMo 2 13B | `allenai/OLMo-2-1124-13B` | 13B | No | Apache 2.0 | ~5T tokens | 67.5% |

OLMo 2 is the stronger choice for reproducibility research since it is fully open (Apache 2.0, open training data and code). Gemma 3 12B has stronger benchmark numbers but is gated and uses a custom license.

---

Sources:
- [Gemma 3 HuggingFace Docs](https://huggingface.co/docs/transformers/model_doc/gemma3)
- [Welcome Gemma 3 Blog Post](https://huggingface.co/blog/gemma3)
- [Gemma 3 Release Collection](https://huggingface.co/collections/google/gemma-3-release)
- [google/gemma-3-12b-pt](https://huggingface.co/google/gemma-3-12b-pt)
- [google/gemma-3-4b-pt](https://huggingface.co/google/gemma-3-4b-pt)
- [google/gemma-3-27b-pt](https://huggingface.co/google/gemma-3-27b-pt)
- [google/gemma-3-1b-pt](https://huggingface.co/google/gemma-3-1b-pt)
- [Gemma 3 Technical Report (arxiv)](https://arxiv.org/abs/2503.19786)
- [Gemma 3 Model Card (Google)](https://ai.google.dev/gemma/docs/core/model_card_3)
- [allenai/OLMo-2-1124-7B](https://huggingface.co/allenai/OLMo-2-1124-7B)
- [allenai/OLMo-2-1124-13B](https://huggingface.co/allenai/OLMo-2-1124-13B)
- [allenai/OLMo-2-0325-32B](https://huggingface.co/allenai/OLMo-2-0325-32B)
- [allenai/OLMo-2-0425-1B](https://huggingface.co/allenai/OLMo-2-0425-1B)
- [OLMo 2 Collection](https://huggingface.co/collections/allenai/olmo-2)
- [OLMo 2 Blog Post (Ai2)](https://allenai.org/blog/olmo2)
- [OLMo 2 Paper (arxiv)](https://arxiv.org/abs/2501.00656)
- [OLMo Release Notes](https://allenai.org/olmo/release-notes)
- [Google DeepMind Gemma 3](https://deepmind.google/models/gemma/gemma-3/)

agentId: a21ba8d3a3938265b (use SendMessage with to: 'a21ba8d3a3938265b' to continue this agent)
&lt;usage>total_tokens: 34598
tool_uses: 15
duration_ms: 101562&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "b9805f26-85f8-4bc5-b4b6-4090fada6a60",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Gemma 3 base model\"\nSearch 2: \"OLMo 2 base model\"\nSearch 3: \"Gemma 3 pretrained model huggingface 2025\"\n\nReturn ALL findings in a structured format. Be thorough.",
    "agentId": "a21ba8d3a3938265b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are all findings compiled in structured format.\n\n---\n\n## Gemma 3 (Google DeepMind)\n\n**Release date:** March 12, 2025 (added to HuggingFace Transformers); public release ~March 25, 2025\n\n**License:** Gemma Terms of Use (custom Google license)\n\n**Gated:** Yes. Requires agreeing to Google's usage license on HuggingFace before downloading.\n\n**Base (pretrained) versions exist:** Yes. All sizes have a `-pt` (pretrained) variant.\n\n| Size | HuggingFace Repo ID | Parameters | Modality | Context Window | Training Tokens | MMLU (base) | HellaSwag (base) |\n|------|---------------------|------------|----------|----------------|-----------------|-------------|------------------|\n| 1B | `google/gemma-3-1b-pt` | 1B | Text only | 32K | 2T | 38.8% | 62.3 |\n| 4B | `google/gemma-3-4b-pt` | 4B | Text + Image | 128K | 4T | 58.1% | 77.2 |\n| 12B | `google/gemma-3-12b-pt` | 12B | Text + Image | 128K | 12T | 71.9% | 84.2 |\n| 27B | `google/gemma-3-27b-pt` | 27B | Text + Image | 128K | 14T | 76.9% | 85.6 |\n\n**Instruction-tuned counterparts** use the `-it` suffix (e.g., `google/gemma-3-12b-it`).\n\n**Additional notes:**\n- 140+ language support\n- Trained using knowledge distillation from larger Gemini models\n- Trained on TPUv4p, TPUv5p, and TPUv5e hardware\n- A 270M text-only variant also exists, trained on 6T tokens\n- Gemma 3 4B-IT beats Gemma 2 27B-IT; Gemma 3 27B-IT is comparable to Gemini 1.5 Pro\n- Technical report: [arxiv.org/abs/2503.19786](https://arxiv.org/abs/2503.19786)\n\n---\n\n## OLMo 2 (Allen Institute for AI / Ai2)\n\n**License:** Apache 2.0 (fully open, including training data, code, and weights)\n\n**Gated:** No. All models are openly available.\n\n**Base (pretrained) versions exist:** Yes. The base repo IDs below are the pretrained models; instruct/SFT/DPO variants have corresponding suffixes.\n\n| Size | HuggingFace Repo ID | Parameters | Release Date | Training Tokens | MMLU (base) |\n|------|---------------------|------------|--------------|-----------------|-------------|\n| 1B | `allenai/OLMo-2-0425-1B` | 1B | April 2025 | 4T (+ 50B mid-training) | Not reported in search results |\n| 7B | `allenai/OLMo-2-1124-7B` | 7B | November 2024 (updated Dec 31, 2024) | ~4T (Stage 1: 3.9T OLMo-Mix-1124, Stage 2: 50B Dolmino-Mix-1124) | 63.7 |\n| 13B | `allenai/OLMo-2-1124-13B` | 13B | November 2024 | Up to 5T | 67.5 |\n| 32B | `allenai/OLMo-2-0325-32B` | 32B | March 2025 | Up to 6T | Not reported in search results |\n\n**Instruct variants:**\n- `allenai/OLMo-2-1124-7B-Instruct`\n- `allenai/OLMo-2-1124-13B-Instruct`\n- `allenai/OLMo-2-0325-32B-Instruct`\n- `allenai/OLMo-2-0425-1B-Instruct`\n\n**Additional OLMo 2 details:**\n- Modality: Text only\n- Training data: OLMo-Mix-1124 (Stage 1) + Dolmino-Mix-1124 (Stage 2, mid-training)\n- 7B model: trained for ~1 epoch on 3.9T tokens, then 3 runs of 50B token mid-training merged via model souping\n- 9-point MMLU increase over original OLMo 7B\n- OLMo 2 7B outperforms Llama 3.1 8B on English academic benchmarks\n- OLMo 2 13B surpasses Qwen 2.5 7B despite fewer training FLOPs\n- OLMo 2 32B is described as \"the first fully-open model to outperform GPT-3.5-Turbo and GPT-4o mini\" on multi-skill academic benchmarks\n- ARC scores: improved from 80.2 to 83.5 for 13B\n- Data cutoff: December 2023\n- Technical report: [arxiv.org/abs/2501.00656](https://arxiv.org/abs/2501.00656)\n- Also note: Ai2 has released **OLMo 3** (`allenai/Olmo-3-1125-32B`) and **OLMo 3.1** (`allenai/Olmo-3.1-32B-Think`), though these are outside your 7B-14B scope\n\n---\n\n## Summary: Models in the 7B-14B Range\n\nFor the specific 7B-14B parameter range relevant to the paper:\n\n| Model | Repo ID | Params | Gated | License | Training Data | MMLU |\n|-------|---------|--------|-------|---------|---------------|------|\n| Gemma 3 12B PT | `google/gemma-3-12b-pt` | 12B | Yes | Gemma ToU | 12T tokens | 71.9% |\n| OLMo 2 7B | `allenai/OLMo-2-1124-7B` | 7B | No | Apache 2.0 | ~4T tokens | 63.7% |\n| OLMo 2 13B | `allenai/OLMo-2-1124-13B` | 13B | No | Apache 2.0 | ~5T tokens | 67.5% |\n\nOLMo 2 is the stronger choice for reproducibility research since it is fully open (Apache 2.0, open training data and code). Gemma 3 12B has stronger benchmark numbers but is gated and uses a custom license.\n\n---\n\nSources:\n- [Gemma 3 HuggingFace Docs](https://huggingface.co/docs/transformers/model_doc/gemma3)\n- [Welcome Gemma 3 Blog Post](https://huggingface.co/blog/gemma3)\n- [Gemma 3 Release Collection](https://huggingface.co/collections/google/gemma-3-release)\n- [google/gemma-3-12b-pt](https://huggingface.co/google/gemma-3-12b-pt)\n- [google/gemma-3-4b-pt](https://huggingface.co/google/gemma-3-4b-pt)\n- [google/gemma-3-27b-pt](https://huggingface.co/google/gemma-3-27b-pt)\n- [google/gemma-3-1b-pt](https://huggingface.co/google/gemma-3-1b-pt)\n- [Gemma 3 Technical Report (arxiv)](https://arxiv.org/abs/2503.19786)\n- [Gemma 3 Model Card (Google)](https://ai.google.dev/gemma/docs/core/model_card_3)\n- [allenai/OLMo-2-1124-7B](https://huggingface.co/allenai/OLMo-2-1124-7B)\n- [allenai/OLMo-2-1124-13B](https://huggingface.co/allenai/OLMo-2-1124-13B)\n- [allenai/OLMo-2-0325-32B](https://huggingface.co/allenai/OLMo-2-0325-32B)\n- [allenai/OLMo-2-0425-1B](https://huggingface.co/allenai/OLMo-2-0425-1B)\n- [OLMo 2 Collection](https://huggingface.co/collections/allenai/olmo-2)\n- [OLMo 2 Blog Post (Ai2)](https://allenai.org/blog/olmo2)\n- [OLMo 2 Paper (arxiv)](https://arxiv.org/abs/2501.00656)\n- [OLMo Release Notes](https://allenai.org/olmo/release-notes)\n- [Google DeepMind Gemma 3](https://deepmind.google/models/gemma/gemma-3/)"
      }
    ],
    "totalDurationMs": 101562,
    "totalTokens": 34598,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6181,
      "cache_read_input_tokens": 26051,
      "output_tokens": 2365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6181
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2365,
          "cache_read_input_tokens": 26051,
          "cache_creation_input_tokens": 6181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6181,
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
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 15
    }
  }
}
```

</details>

---

### System

_source line 269_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Ministral 3 8B 14B base model HuggingFace repo ID…",
  "usage": {
    "total_tokens": 35681,
    "tool_uses": 20,
    "duration_ms": 100161
  },
  "last_tool_name": "WebSearch",
  "uuid": "3c45902b-634a-43d5-b566-42345e5badff",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 270_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G98CMuXEmGPRyFJiBk4Doz`</summary>

```json
{
  "query": "Ministral 3 8B 14B base model HuggingFace repo ID release date 2025 2026 training data benchmark MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f4e6eeaf-d987-4f15-a8d2-6fed4345d7a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DximVYVGSmQw7hRTjn1vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 32834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

_source line 271_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Qwen3 8B 14B base training data tokens pretrainin…",
  "usage": {
    "total_tokens": 35732,
    "tool_uses": 21,
    "duration_ms": 100326
  },
  "last_tool_name": "WebSearch",
  "uuid": "bdf5ca0d-ed54-4f5d-98fc-906939a594a3",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 272_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YVHFp9Vm2wqTh7xANos3ce`</summary>

```json
{
  "query": "Qwen3 8B 14B base training data tokens pretraining technical report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f747e1a4-3685-4979-9f43-800f9f285772",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DximVYVGSmQw7hRTjn1vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 32834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

_source line 273_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for DeepSeek V2 Lite base 15.7B HuggingFace release d…",
  "usage": {
    "total_tokens": 35783,
    "tool_uses": 22,
    "duration_ms": 100410
  },
  "last_tool_name": "WebSearch",
  "uuid": "251a68ce-cf9f-4b85-bffd-68230e8221c2",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 274_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019e5HAbuVBBLensc33Hy7Yk`</summary>

```json
{
  "query": "DeepSeek V2 Lite base 15.7B HuggingFace release date gated benchmark MMLU training tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "acef8e8d-221f-4bac-8ab2-1d1c4e85fa97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DximVYVGSmQw7hRTjn1vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 32834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 275 · 2026-05-18T07:09:28.942Z_

<details><summary>↩ Tool result · `toolu_01P5bNa3iv6SNa5xQKDh7j6P`</summary>

```text
Web search results for query: "Qwen2.5 14B MMLU benchmark base model training tokens"

Links: [{"title":"Qwen2.5-LLM: Extending the boundary of LLMs | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-llm/"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Qwen2.5 14B Instruct Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/qwen-2.5-14b-instruct"},{"title":"2025-01-26 Qwen2.5-1M Technical Report","url":"https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/Qwen2_5_1M_Technical_Report.pdf"},{"title":"Qwen 2.5 14B | Open Laboratory","url":"https://openlaboratory.ai/models/qwen-2_5-14b"},{"title":"Technical Report Qwen2.5-Coder Technical Report Binyuan Hui* Jian Yang*","url":"https://arxiv.org/pdf/2409.12186"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v3"},{"title":"Qwen 2.5","url":"https://qwen2.org/qwen2-5/"},{"title":"Qwen2.5-LLM: Extending the Boundary of LLMs - Alibaba Cloud Community","url":"https://www.alibabacloud.com/blog/601786"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"}]

Based on the search results, here's what I found about Qwen2.5-14B:

## MMLU Benchmark Performance

The Qwen2.5-14B model achieves a score of 79.7 on MMLU, demonstrating strong performance on this general language understanding benchmark.

## Training Tokens

The pre-training dataset was expanded from 7 trillion tokens to a maximum of 18 trillion tokens. This represents the training data size used for the Qwen2.5 series models, including the 14B variant.

## Additional Context

Qwen2.5 models, including the 14B variant, are pretrained on a large-scale corpus comprising up to 18 trillion tokens, with the pretraining data covering diverse domains and curated for high data quality.

The Qwen2.5-14B base model demonstrates competitive performance, particularly excelling in general language understanding tasks as evidenced by its MMLU score.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "fda321d4-5bb5-4482-9a02-70db3508cb14"
}
```

</details>

---

### Tool result

_source line 276 · 2026-05-18T07:09:29.885Z_

<details><summary>↩ Tool result · `toolu_01FHqgLBPxKo5AdbHgYqnHfu`</summary>

```text
Web search results for query: "Gemma 4 base model release 2026 huggingface google"

Links: [{"title":"google/gemma-4-26B-A4B · Hugging Face","url":"https://huggingface.co/google/gemma-4-26B-A4B"},{"title":"Gemma 4 model overview | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core"},{"title":"Gemma 4 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-4/"},{"title":"google/gemma-4-E4B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-E4B-it"},{"title":"google/gemma-4-26B-A4B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-26B-A4B-it"},{"title":"What Is Google Gemma 4? Architecture, Benchmarks, and Why It Matters | WaveSpeed Blog","url":"https://wavespeed.ai/blog/posts/what-is-google-gemma-4/"},{"title":"google/gemma-4-31B · Hugging Face","url":"https://huggingface.co/google/gemma-4-31B"},{"title":"google/gemma-4-E4B · Hugging Face","url":"https://huggingface.co/google/gemma-4-E4B"},{"title":"Gemma4 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma4"},{"title":"Gemma 4: Byte for byte, the most capable open models","url":"https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/"}]

I've found comprehensive information about the Gemma 4 base model release. Here's what I found:

## Gemma 4 Release

On April 2, 2026, Google DeepMind released Gemma 4 — four open-weight models built from the same research lineage as Gemini 3, now shipped under the Apache 2.0 license.

## Model Variants

The models are available in four distinct sizes: E2B, E4B, 26B A4B, and 31B. This release includes open-weights models in both pre-trained and instruction-tuned variants.

## Key Capabilities

Gemma 4 models are multimodal, handling text and image input (with audio supported on small models) and generating text output. Gemma 4 features a context window of up to 256K tokens and maintains multilingual support in over 140 languages.

## Availability

You can download Gemma 4 models from Kaggle and Hugging Face. The models are available on Hugging Face under Google's official collection, with both base and instruction-tuned variants for each size.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "0cc50757-b08c-4b73-8a7b-d5b9bcaf46dc"
}
```

</details>

---

### Tool result

_source line 277 · 2026-05-18T07:09:33.222Z_

<details><summary>↩ Tool result · `toolu_01CAcCQMJzPrL5gxnKWUDARF`</summary>

```text
Web search results for query: "Falcon H1 7B 14B hybrid model huggingface 2025"

Links: [{"title":"tiiuae/Falcon-H1R-7B · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon-H1R-7B"},{"title":"Introducing Falcon H1R 7B","url":"https://huggingface.co/blog/tiiuae/falcon-h1r-7b"},{"title":"tiiuae/Falcon-H1R-7B-GGUF · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon-H1R-7B-GGUF"},{"title":"Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance | Falcon","url":"https://falcon-lm.github.io/blog/falcon-h1/"},{"title":"Falcon-H1R: Pushing the Reasoning Frontiers with a Hybrid Model for Efficient Test-Time Scaling | Falcon","url":"https://falcon-lm.github.io/blog/falcon-h1r-7b/"},{"title":"FalconH1","url":"https://huggingface.co/docs/transformers/en/model_doc/falcon_h1"},{"title":"tiiuae/Falcon-H1-7B-Instruct · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon-H1-7B-Instruct"},{"title":"[2507.22448] Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance","url":"https://arxiv.org/abs/2507.22448"},{"title":"Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance","url":"https://huggingface.co/blog/tiiuae/falcon-h1"},{"title":"tiiuae/Falcon-H1-7B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon-H1-7B-Base"}]

Based on the search results, here's information about the Falcon H1 hybrid models:

## Falcon-H1 Hybrid Model Family

Falcon-H1 is a series of large language models featuring hybrid architecture designs that combines Transformer-based attention with State Space Models (SSMs), known for superior long-context memory and computational efficiency.

### Model Sizes and Availability

Falcon-H1 is released in multiple configurations, including base and instruction-tuned variants at 0.5B, 1.5B, 1.5B-deep, 3B, 7B, and 34B parameters.

### Key Features

- The amount of attention and mamba heads can be adjusted independently, allowing for an optimal attention/SSM ratio, which enables faster inference, lower memory usage, and strong generalization across tasks.

- Falcon-H1 models support up to 256K context length, enabling applications in long-document processing, multi-turn dialogue, and long-range reasoning.

- The models support 18 languages natively, including Arabic, Czech, German, English, Spanish, French, Hindi, Italian, Japanese, Korean, Dutch, Polish, Portuguese, Romanian, Russian, Swedish, Urdu, and Chinese.

### Performance

The flagship Falcon-H1-34B matches or outperforms models up to 70B scale, while using fewer parameters and less data. Smaller models show similar trends: the Falcon-H1-1.5B-Deep rivals current leading 7B-10B models, and Falcon-H1-0.5B performs comparably to typical 7B models from 2024.

### Falcon-H1R Reasoning Variant

Falcon-H1R-7B is a reasoning-specialized model that was trained via cold-start supervised fine-tuning with long reasoning traces and further enhanced by scaling RL with GRPO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "f82af57f-e711-4be3-a599-837f9f2ab522"
}
```

</details>

---

### Tool result

_source line 278 · 2026-05-18T07:09:33.457Z_

<details><summary>↩ Tool result · `toolu_019e5HAbuVBBLensc33Hy7Yk`</summary>

```text
Web search results for query: "DeepSeek V2 Lite base 15.7B HuggingFace release date gated benchmark MMLU training tokens"

Links: [{"title":"deepseek-ai/DeepSeek-V2-Lite · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite"},{"title":"deepseek-ai/DeepSeek-V4-Pro · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"},{"title":"deepseek-ai/DeepSeek-Coder-V2-Lite-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Base"},{"title":"deepseek-ai/DeepSeek-V2-Lite-Chat · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite-Chat"},{"title":"lmstudio-community/DeepSeek-Coder-V2-Lite-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/lmstudio-community/DeepSeek-Coder-V2-Lite-Instruct-GGUF"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder-V2: DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder-V2"},{"title":"deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"},{"title":"deepseek-ai/DeepSeek-V2 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V2"},{"title":"deepseek-ai/DeepSeek-Coder-V2-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Base"},{"title":"GitHub - deepseek-ai/DeepSeek-LLM: DeepSeek LLM: Let there be answers · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-LLM"}]

Based on the search results, here's what I found about DeepSeek V2 Lite base 15.7B:

**Model Architecture & Parameters:**
DeepSeek-V2-Lite comprises 15.7B total parameters, of which 2.4B are activated for each token.

**Training Details:**
During pre-training, the maximum sequence length was set to 4K, and DeepSeek-V2-Lite was trained on 5.7T tokens. DeepSeek-V2-Lite was trained from scratch on the same pre-training corpus of DeepSeek-V2, which is not polluted by any SFT data.

**Release Date:**
DeepSeek-V2-Lite comes out with 16B total params, 2.4B active params, scratch training with 5.7T tokens. According to the metadata, this was released on May 7, 2024.

**Performance:**
DeepSeek-V2-Lite outperforms 7B dense and 16B MoE on many English & Chinese benchmarks.

However, I didn't find specific information in the search results about MMLU benchmark scores or whether the model is gated on HuggingFace. You may need to check the HuggingFace model card directly for those specific details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "4e0de0ee-4fe4-435c-8475-0ea5b5efd45f"
}
```

</details>

---

### Tool result

_source line 279 · 2026-05-18T07:09:33.511Z_

<details><summary>↩ Tool result · `toolu_01YVHFp9Vm2wqTh7xANos3ce`</summary>

```text
Web search results for query: "Qwen3 8B 14B base training data tokens pretraining technical report"

Links: [{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3-8B-Base: Open 8B LLM Overview","url":"https://www.emergentmind.com/topics/qwen3-8b-base"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"[Literature Review] Qwen3 Technical Report","url":"https://www.themoonlight.io/en/review/qwen3-technical-report"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"},{"title":"2025-05-13 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://cdn.jsdelivr.net/gh/yanfeng98/paper-is-all-you-need/papers/00069-Qwen3_Technical_Report.pdf"},{"title":"(PDF) QWEN TECHNICAL REPORT","url":"https://www.researchgate.net/publication/377112868_QWEN_TECHNICAL_REPORT"},{"title":"Qwen3 Technical Report: Reasoning in Pre-Training and Post-Training","url":"https://thesalt.substack.com/p/qwen3-technical-report-reasoning"},{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"}]

Based on the search results, here's the information about Qwen3 8B and 14B base models' pretraining details from the technical report:

## Pretraining Data and Tokens

Qwen3 uses approximately 36 trillion tokens covering 119 languages and dialects, which is a significant expansion compared to its predecessor.

### Three-Stage Pretraining Process

In the first stage (S1), the model was pretrained on over 30 trillion tokens with a context length of 4K tokens, which provided the model with basic language skills and general knowledge. In the second stage (S2), the dataset was improved by increasing the proportion of knowledge-intensive data such as STEM, coding, and reasoning tasks, and the model was pretrained on an additional 5 trillion tokens. In the final stage, high-quality long-context data was used to extend the context length to 32K tokens.

### Data Sources

Pretraining spans 36 trillion tokens covering 119 languages and dialects, sourced from web crawls, OCR-extracted PDFs, Wikipedia, code repositories, and synthetic STEM/coding datasets.

### Model Performance

Qwen3-1.7B/4B/8B/14B/32B-Base performs as well as Qwen2.5-3B/7B/14B/32B/72B-Base, respectively.

The official Qwen3 Technical Report is available on arXiv (2505.09388) for more detailed information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "62ba2887-7441-4831-91e4-7eee0892538a"
}
```

</details>

---

### System

_source line 280_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ac855f59be58ea3ac",
  "tool_use_id": "toolu_01UUx3h1Z4EHFrb7q9YJpLgR",
  "status": "completed",
  "output_file": "",
  "summary": "Search batch 2: Llama + Qwen + Mistral",
  "usage": {
    "total_tokens": 32064,
    "tool_uses": 16,
    "duration_ms": 120408
  },
  "uuid": "620a95ae-f23e-4039-b83f-abbe914f68cb",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool result

_source line 281 · 2026-05-18T07:09:40.865Z_

<details><summary>↩ Tool result · `toolu_01UUx3h1Z4EHFrb7q9YJpLgR`</summary>

```text
Here are the compiled findings from all three searches.

---

## SEARCH 1: Llama 4 Base Model Release

**Important caveat:** Llama 4 does NOT have any models in the 7B-14B parameter range. All Llama 4 models have 17B active parameters (MoE), with total parameter counts of 109B+ . There is no Llama 4 equivalent of the old Llama 3.1 8B.

### Llama 4 Scout

| Field | Detail |
|---|---|
| **Full name** | Llama 4 Scout 17B 16E |
| **HuggingFace repo (base)** | `meta-llama/Llama-4-Scout-17B-16E` |
| **HuggingFace repo (instruct)** | `meta-llama/Llama-4-Scout-17B-16E-Instruct` |
| **Parameter count** | 17B active, ~109B total (16 experts) |
| **Release date** | April 5, 2025 |
| **Gated?** | Yes -- requires accepting the Llama 4 Community License Agreement on HuggingFace |
| **Base (non-instruct) version?** | Yes (`meta-llama/Llama-4-Scout-17B-16E`) |
| **Training data size** | ~40 trillion tokens (multimodal), cutoff August 2024 |
| **Context window** | 10M tokens (pretrained at 256K) |
| **Architecture** | Mixture-of-Experts (MoE), auto-regressive, natively multimodal |
| **Benchmark** | Not individually broken out in public announcements for the base model |

### Llama 4 Maverick

| Field | Detail |
|---|---|
| **Full name** | Llama 4 Maverick 17B 128E |
| **HuggingFace repo (base)** | `meta-llama/Llama-4-Maverick-17B-128E` (also `meta-llama/Llama-4-Maverick-17B-128E-Original` for Meta format) |
| **HuggingFace repo (instruct)** | `meta-llama/Llama-4-Maverick-17B-128E-Instruct` |
| **Parameter count** | 17B active, ~400B total (128 experts) |
| **Release date** | April 5, 2025 |
| **Gated?** | Yes -- same Llama 4 Community License |
| **Base (non-instruct) version?** | Yes |
| **Training data size** | ~22 trillion tokens (multimodal), cutoff August 2024 |
| **Context window** | 1M tokens |
| **Architecture** | MoE, auto-regressive, natively multimodal |

### Llama 4 Behemoth (not released)

Announced but still in training at time of Scout/Maverick release. 288B active parameters, ~2T total, 16 experts.

**Bottom line for your paper:** Llama 4 has no dense 7B-14B model. If you need a Meta base model in that range, the closest is still **Llama 3.1 8B** or **Llama 3.2 (1B/3B)**.

---

## SEARCH 2: Qwen 3 Base Model

Qwen3 was released on **April 29, 2025** by Alibaba Cloud's Qwen team. Dense base models in the 7B-14B range:

### Qwen3-8B-Base

| Field | Detail |
|---|---|
| **Full name** | Qwen3-8B-Base |
| **HuggingFace repo** | `Qwen/Qwen3-8B-Base` |
| **Parameter count** | 8.2B total, 6.95B non-embedding |
| **Architecture** | Dense causal transformer, 36 layers, 32 Q-heads / 8 KV-heads (GQA), SwiGLU, RMSNorm |
| **Release date** | April 29, 2025 |
| **Gated?** | No -- open weights under Apache 2.0 |
| **Base (non-instruct) version?** | Yes (this IS the base version; instruct = `Qwen/Qwen3-8B`) |
| **Training data size** | 36 trillion tokens, 119 languages |
| **Context length** | 32,768 native; up to 131,072 with YaRN |
| **Benchmarks (base)** | MMLU: 79.66, GSM8K: 90.22, EvalPlus: 60.70 |
| **Notable** | Outperforms Qwen2.5-14B-Base on many benchmarks |

### Qwen3-14B-Base

| Field | Detail |
|---|---|
| **Full name** | Qwen3-14B-Base |
| **HuggingFace repo** | `Qwen/Qwen3-14B-Base` |
| **Parameter count** | 14.8B total, 13.2B non-embedding |
| **Architecture** | Dense causal transformer, 40 layers, 40 Q-heads / 8 KV-heads (GQA), SwiGLU, RMSNorm |
| **Release date** | April 29, 2025 |
| **Gated?** | No -- open weights under Apache 2.0 |
| **Base (non-instruct) version?** | Yes (instruct = `Qwen/Qwen3-14B`) |
| **Training data size** | 36 trillion tokens, 119 languages |
| **Context length** | 32,768 native |
| **Benchmarks (base)** | MMLU: 81.05, GSM8K: 92.49, EvalPlus: 72.23 |
| **Notable** | Competitive with Qwen2.5-32B-Base; significant cost advantage |

### Other Qwen3 dense base models (outside 7B-14B but for reference)

- `Qwen/Qwen3-0.6B-Base` (0.6B)
- `Qwen/Qwen3-1.7B-Base` (1.7B)
- `Qwen/Qwen3-4B-Base` (4B) -- MMLU: 74.16, GSM8K: 85.36
- `Qwen/Qwen3-32B-Base` (32B)

**Technical report:** [arxiv.org/abs/2505.09388](https://arxiv.org/abs/2505.09388) (May 15, 2025)

---

## SEARCH 3: Mistral Latest Base Model 2025

The Mistral 3 family launched on **December 2, 2025**, including the Ministral 3 edge/local models with base variants.

### Ministral-3-8B-Base-2512

| Field | Detail |
|---|---|
| **Full name** | Ministral 3 8B Base 2512 |
| **HuggingFace repo** | `mistralai/Ministral-3-8B-Base-2512` |
| **Parameter count** | 8.4B total |
| **Architecture** | Dense vision-language model, 34 layers, 4096 hidden size, 32 attention heads, 8 KV groups (GQA) |
| **Release date** | December 2 (or 4), 2025 |
| **Gated?** | No -- Apache 2.0 license |
| **Base (non-instruct) version?** | Yes (instruct = `mistralai/Ministral-3-8B-Instruct-2512`; reasoning = `mistralai/Ministral-3-8B-Reasoning-2512`) |
| **Training data size** | Not publicly disclosed |
| **Context length** | Up to 256K tokens (YaRN RoPE scaling) |
| **Benchmarks (base)** | Specific MMLU score for the 8B base not found in search results |
| **Notable** | Natively multimodal (vision baked into core training); trained on 40+ languages (strong European language support); fits on single H200 GPU |

### Ministral-3-14B-Base-2512

| Field | Detail |
|---|---|
| **Full name** | Ministral 3 14B Base 2512 |
| **HuggingFace repo** | `mistralai/Ministral-3-14B-Base-2512` |
| **Parameter count** | ~14B total |
| **Architecture** | Dense vision-language model, 40 layers, 5120 hidden size, 32 attention heads, 8 KV groups (GQA) |
| **Release date** | December 2 (or 4), 2025 |
| **Gated?** | No -- Apache 2.0 license |
| **Base (non-instruct) version?** | Yes (instruct = `mistralai/Ministral-3-14B-Instruct-2512`; reasoning = `mistralai/Ministral-3-14B-Reasoning-2512`) |
| **Training data size** | Not publicly disclosed |
| **Context length** | Up to 256K tokens |
| **Benchmarks (base)** | MMLU: 79.4%, MMLU-Redux: 82.0% |
| **Notable** | Performance comparable to Mistral Small 3.2 24B; recommended 2xH200 for full 256K context |

### Ministral-3-3B-Base-2512 (outside 7B-14B but for reference)

- HuggingFace repo: `mistralai/Ministral-3-3B-Base-2512`
- 3.4B params, 26 layers, Apache 2.0, 256K context

### Mistral Small 4 (March 2026, for context)

- MoE model: 119B total, 6B active per token
- Not a base model in the traditional sense; instruction/reasoning focused
- Not in the 7B-14B dense range

**Technical report:** [arxiv.org/abs/2601.08584](https://arxiv.org/abs/2601.08584)

---

## Summary: All Base Models in the 7B-14B Range (2025-2026)

| Model | Repo ID | Params | Released | License | Gated? | Training Data | Context | MMLU (base) |
|---|---|---|---|---|---|---|---|---|
| **Qwen3-8B-Base** | `Qwen/Qwen3-8B-Base` | 8.2B | 2025-04-29 | Apache 2.0 | No | 36T tokens | 32K (131K w/ YaRN) | 79.66 |
| **Qwen3-14B-Base** | `Qwen/Qwen3-14B-Base` | 14.8B | 2025-04-29 | Apache 2.0 | No | 36T tokens | 32K | 81.05 |
| **Ministral-3-8B-Base** | `mistralai/Ministral-3-8B-Base-2512` | 8.4B | 2025-12-02 | Apache 2.0 | No | Undisclosed | 256K | -- |
| **Ministral-3-14B-Base** | `mistralai/Ministral-3-14B-Base-2512` | ~14B | 2025-12-02 | Apache 2.0 | No | Undisclosed | 256K | 79.4 |
| **Llama 4 Scout (MoE)** | `meta-llama/Llama-4-Scout-17B-16E` | 17B active / 109B total | 2025-04-05 | Llama 4 CLA | Yes | 40T tokens | 10M | -- |

Llama 4 Scout/Maverick are included for completeness but are MoE models with 17B active params (outside the strict 7B-14B dense range). There is **no Llama 4 dense model in the 7B-14B range**.

Sources:
- [Meta Llama 4 blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [meta-llama/Llama-4-Scout-17B-16E](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E)
- [meta-llama/Llama-4-Maverick-17B-128E](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E)
- [HuggingFace Llama 4 release blog](https://huggingface.co/blog/llama4-release)
- [Qwen3 blog](https://qwenlm.github.io/blog/qwen3/)
- [Qwen/Qwen3-8B-Base](https://huggingface.co/Qwen/Qwen3-8B-Base)
- [Qwen/Qwen3-14B-Base](https://huggingface.co/Qwen/Qwen3-14B-Base)
- [Qwen3 Technical Report (arXiv 2505.09388)](https://arxiv.org/pdf/2505.09388)
- [Introducing Mistral 3](https://mistral.ai/news/mistral-3)
- [mistralai/Ministral-3-8B-Base-2512](https://huggingface.co/mistralai/Ministral-3-8B-Base-2512)
- [mistralai/Ministral-3-14B-Base-2512](https://huggingface.co/mistralai/Ministral-3-14B-Base-2512)
- [Ministral 3 Technical Report (arXiv 2601.08584)](https://arxiv.org/pdf/2601.08584)
- [Mistral 3 guide (Shawn Kanungo)](https://shawnkanungo.com/blog/what-is-mistral-3-ai-open-source-models-guide-2026)
- [Mistral AI Models 2026 guide (Serenities AI)](https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide)

agentId: ac855f59be58ea3ac (use SendMessage with to: 'ac855f59be58ea3ac' to continue this agent)
&lt;usage>total_tokens: 35454
tool_uses: 16
duration_ms: 120410&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "4096d60c-2402-47e3-a46f-328f56e71514",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Llama 4 base model release\"\nSearch 2: \"Qwen 3 base model\"\nSearch 3: \"Mistral latest base model 2025\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range.",
    "agentId": "ac855f59be58ea3ac",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the compiled findings from all three searches.\n\n---\n\n## SEARCH 1: Llama 4 Base Model Release\n\n**Important caveat:** Llama 4 does NOT have any models in the 7B-14B parameter range. All Llama 4 models have 17B active parameters (MoE), with total parameter counts of 109B+ . There is no Llama 4 equivalent of the old Llama 3.1 8B.\n\n### Llama 4 Scout\n\n| Field | Detail |\n|---|---|\n| **Full name** | Llama 4 Scout 17B 16E |\n| **HuggingFace repo (base)** | `meta-llama/Llama-4-Scout-17B-16E` |\n| **HuggingFace repo (instruct)** | `meta-llama/Llama-4-Scout-17B-16E-Instruct` |\n| **Parameter count** | 17B active, ~109B total (16 experts) |\n| **Release date** | April 5, 2025 |\n| **Gated?** | Yes -- requires accepting the Llama 4 Community License Agreement on HuggingFace |\n| **Base (non-instruct) version?** | Yes (`meta-llama/Llama-4-Scout-17B-16E`) |\n| **Training data size** | ~40 trillion tokens (multimodal), cutoff August 2024 |\n| **Context window** | 10M tokens (pretrained at 256K) |\n| **Architecture** | Mixture-of-Experts (MoE), auto-regressive, natively multimodal |\n| **Benchmark** | Not individually broken out in public announcements for the base model |\n\n### Llama 4 Maverick\n\n| Field | Detail |\n|---|---|\n| **Full name** | Llama 4 Maverick 17B 128E |\n| **HuggingFace repo (base)** | `meta-llama/Llama-4-Maverick-17B-128E` (also `meta-llama/Llama-4-Maverick-17B-128E-Original` for Meta format) |\n| **HuggingFace repo (instruct)** | `meta-llama/Llama-4-Maverick-17B-128E-Instruct` |\n| **Parameter count** | 17B active, ~400B total (128 experts) |\n| **Release date** | April 5, 2025 |\n| **Gated?** | Yes -- same Llama 4 Community License |\n| **Base (non-instruct) version?** | Yes |\n| **Training data size** | ~22 trillion tokens (multimodal), cutoff August 2024 |\n| **Context window** | 1M tokens |\n| **Architecture** | MoE, auto-regressive, natively multimodal |\n\n### Llama 4 Behemoth (not released)\n\nAnnounced but still in training at time of Scout/Maverick release. 288B active parameters, ~2T total, 16 experts.\n\n**Bottom line for your paper:** Llama 4 has no dense 7B-14B model. If you need a Meta base model in that range, the closest is still **Llama 3.1 8B** or **Llama 3.2 (1B/3B)**.\n\n---\n\n## SEARCH 2: Qwen 3 Base Model\n\nQwen3 was released on **April 29, 2025** by Alibaba Cloud's Qwen team. Dense base models in the 7B-14B range:\n\n### Qwen3-8B-Base\n\n| Field | Detail |\n|---|---|\n| **Full name** | Qwen3-8B-Base |\n| **HuggingFace repo** | `Qwen/Qwen3-8B-Base` |\n| **Parameter count** | 8.2B total, 6.95B non-embedding |\n| **Architecture** | Dense causal transformer, 36 layers, 32 Q-heads / 8 KV-heads (GQA), SwiGLU, RMSNorm |\n| **Release date** | April 29, 2025 |\n| **Gated?** | No -- open weights under Apache 2.0 |\n| **Base (non-instruct) version?** | Yes (this IS the base version; instruct = `Qwen/Qwen3-8B`) |\n| **Training data size** | 36 trillion tokens, 119 languages |\n| **Context length** | 32,768 native; up to 131,072 with YaRN |\n| **Benchmarks (base)** | MMLU: 79.66, GSM8K: 90.22, EvalPlus: 60.70 |\n| **Notable** | Outperforms Qwen2.5-14B-Base on many benchmarks |\n\n### Qwen3-14B-Base\n\n| Field | Detail |\n|---|---|\n| **Full name** | Qwen3-14B-Base |\n| **HuggingFace repo** | `Qwen/Qwen3-14B-Base` |\n| **Parameter count** | 14.8B total, 13.2B non-embedding |\n| **Architecture** | Dense causal transformer, 40 layers, 40 Q-heads / 8 KV-heads (GQA), SwiGLU, RMSNorm |\n| **Release date** | April 29, 2025 |\n| **Gated?** | No -- open weights under Apache 2.0 |\n| **Base (non-instruct) version?** | Yes (instruct = `Qwen/Qwen3-14B`) |\n| **Training data size** | 36 trillion tokens, 119 languages |\n| **Context length** | 32,768 native |\n| **Benchmarks (base)** | MMLU: 81.05, GSM8K: 92.49, EvalPlus: 72.23 |\n| **Notable** | Competitive with Qwen2.5-32B-Base; significant cost advantage |\n\n### Other Qwen3 dense base models (outside 7B-14B but for reference)\n\n- `Qwen/Qwen3-0.6B-Base` (0.6B)\n- `Qwen/Qwen3-1.7B-Base` (1.7B)\n- `Qwen/Qwen3-4B-Base` (4B) -- MMLU: 74.16, GSM8K: 85.36\n- `Qwen/Qwen3-32B-Base` (32B)\n\n**Technical report:** [arxiv.org/abs/2505.09388](https://arxiv.org/abs/2505.09388) (May 15, 2025)\n\n---\n\n## SEARCH 3: Mistral Latest Base Model 2025\n\nThe Mistral 3 family launched on **December 2, 2025**, including the Ministral 3 edge/local models with base variants.\n\n### Ministral-3-8B-Base-2512\n\n| Field | Detail |\n|---|---|\n| **Full name** | Ministral 3 8B Base 2512 |\n| **HuggingFace repo** | `mistralai/Ministral-3-8B-Base-2512` |\n| **Parameter count** | 8.4B total |\n| **Architecture** | Dense vision-language model, 34 layers, 4096 hidden size, 32 attention heads, 8 KV groups (GQA) |\n| **Release date** | December 2 (or 4), 2025 |\n| **Gated?** | No -- Apache 2.0 license |\n| **Base (non-instruct) version?** | Yes (instruct = `mistralai/Ministral-3-8B-Instruct-2512`; reasoning = `mistralai/Ministral-3-8B-Reasoning-2512`) |\n| **Training data size** | Not publicly disclosed |\n| **Context length** | Up to 256K tokens (YaRN RoPE scaling) |\n| **Benchmarks (base)** | Specific MMLU score for the 8B base not found in search results |\n| **Notable** | Natively multimodal (vision baked into core training); trained on 40+ languages (strong European language support); fits on single H200 GPU |\n\n### Ministral-3-14B-Base-2512\n\n| Field | Detail |\n|---|---|\n| **Full name** | Ministral 3 14B Base 2512 |\n| **HuggingFace repo** | `mistralai/Ministral-3-14B-Base-2512` |\n| **Parameter count** | ~14B total |\n| **Architecture** | Dense vision-language model, 40 layers, 5120 hidden size, 32 attention heads, 8 KV groups (GQA) |\n| **Release date** | December 2 (or 4), 2025 |\n| **Gated?** | No -- Apache 2.0 license |\n| **Base (non-instruct) version?** | Yes (instruct = `mistralai/Ministral-3-14B-Instruct-2512`; reasoning = `mistralai/Ministral-3-14B-Reasoning-2512`) |\n| **Training data size** | Not publicly disclosed |\n| **Context length** | Up to 256K tokens |\n| **Benchmarks (base)** | MMLU: 79.4%, MMLU-Redux: 82.0% |\n| **Notable** | Performance comparable to Mistral Small 3.2 24B; recommended 2xH200 for full 256K context |\n\n### Ministral-3-3B-Base-2512 (outside 7B-14B but for reference)\n\n- HuggingFace repo: `mistralai/Ministral-3-3B-Base-2512`\n- 3.4B params, 26 layers, Apache 2.0, 256K context\n\n### Mistral Small 4 (March 2026, for context)\n\n- MoE model: 119B total, 6B active per token\n- Not a base model in the traditional sense; instruction/reasoning focused\n- Not in the 7B-14B dense range\n\n**Technical report:** [arxiv.org/abs/2601.08584](https://arxiv.org/abs/2601.08584)\n\n---\n\n## Summary: All Base Models in the 7B-14B Range (2025-2026)\n\n| Model | Repo ID | Params | Released | License | Gated? | Training Data | Context | MMLU (base) |\n|---|---|---|---|---|---|---|---|---|\n| **Qwen3-8B-Base** | `Qwen/Qwen3-8B-Base` | 8.2B | 2025-04-29 | Apache 2.0 | No | 36T tokens | 32K (131K w/ YaRN) | 79.66 |\n| **Qwen3-14B-Base** | `Qwen/Qwen3-14B-Base` | 14.8B | 2025-04-29 | Apache 2.0 | No | 36T tokens | 32K | 81.05 |\n| **Ministral-3-8B-Base** | `mistralai/Ministral-3-8B-Base-2512` | 8.4B | 2025-12-02 | Apache 2.0 | No | Undisclosed | 256K | -- |\n| **Ministral-3-14B-Base** | `mistralai/Ministral-3-14B-Base-2512` | ~14B | 2025-12-02 | Apache 2.0 | No | Undisclosed | 256K | 79.4 |\n| **Llama 4 Scout (MoE)** | `meta-llama/Llama-4-Scout-17B-16E` | 17B active / 109B total | 2025-04-05 | Llama 4 CLA | Yes | 40T tokens | 10M | -- |\n\nLlama 4 Scout/Maverick are included for completeness but are MoE models with 17B active params (outside the strict 7B-14B dense range). There is **no Llama 4 dense model in the 7B-14B range**.\n\nSources:\n- [Meta Llama 4 blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)\n- [meta-llama/Llama-4-Scout-17B-16E](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E)\n- [meta-llama/Llama-4-Maverick-17B-128E](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E)\n- [HuggingFace Llama 4 release blog](https://huggingface.co/blog/llama4-release)\n- [Qwen3 blog](https://qwenlm.github.io/blog/qwen3/)\n- [Qwen/Qwen3-8B-Base](https://huggingface.co/Qwen/Qwen3-8B-Base)\n- [Qwen/Qwen3-14B-Base](https://huggingface.co/Qwen/Qwen3-14B-Base)\n- [Qwen3 Technical Report (arXiv 2505.09388)](https://arxiv.org/pdf/2505.09388)\n- [Introducing Mistral 3](https://mistral.ai/news/mistral-3)\n- [mistralai/Ministral-3-8B-Base-2512](https://huggingface.co/mistralai/Ministral-3-8B-Base-2512)\n- [mistralai/Ministral-3-14B-Base-2512](https://huggingface.co/mistralai/Ministral-3-14B-Base-2512)\n- [Ministral 3 Technical Report (arXiv 2601.08584)](https://arxiv.org/pdf/2601.08584)\n- [Mistral 3 guide (Shawn Kanungo)](https://shawnkanungo.com/blog/what-is-mistral-3-ai-open-source-models-guide-2026)\n- [Mistral AI Models 2026 guide (Serenities AI)](https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide)"
      }
    ],
    "totalDurationMs": 120410,
    "totalTokens": 35454,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 904,
      "cache_creation_input_tokens": 1267,
      "cache_read_input_tokens": 29599,
      "output_tokens": 3684,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1267
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 904,
          "output_tokens": 3684,
          "cache_read_input_tokens": 29599,
          "cache_creation_input_tokens": 1267,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1267,
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
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 16
    }
  }
}
```

</details>

---

### Tool result

_source line 282 · 2026-05-18T07:09:42.139Z_

<details><summary>↩ Tool result · `toolu_01G98CMuXEmGPRyFJiBk4Doz`</summary>

```text
Web search results for query: "Ministral 3 8B 14B base model HuggingFace repo ID release date 2025 2026 training data benchmark MMLU"

Links: [{"title":"mistralai/Ministral-3-3B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512"},{"title":"mistralai/Ministral-3-14B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512"},{"title":"mistralai/Ministral-3-8B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Base-2512"},{"title":"Ministral3","url":"https://huggingface.co/docs/transformers/main/en/model_doc/ministral3"},{"title":"mistralai/Ministral-3-14B-Reasoning-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Reasoning-2512"},{"title":"mistralai/Ministral-3-3B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-3B-Base-2512"},{"title":"Ministral 3 - a mistralai Collection","url":"https://huggingface.co/collections/mistralai/ministral-3"},{"title":"mistralai/Ministral-3-14B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Base-2512"},{"title":"mistralai/Ministral-3-14B-Instruct-2512-BF16 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512-BF16"},{"title":"mistralai/Ministral-3-8B-Reasoning-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Reasoning-2512"}]

Now let me search for more specific information about training data and benchmark performance including MMLU scores:

Links: [{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"},{"title":"Multilingual MMLU Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/multilingual-mmlu"},{"title":"Mistral: Ministral 3B Free Chat Online - Skywork ai","url":"https://skywork.ai/blog/models/mistral-ministral-3b-free-chat-online/"},{"title":"Mistral 3: Model Family, Architecture, Benchmarks & More - CometAPI - All AI Models in One API","url":"https://www.cometapi.com/mistral-3-model-family-architecture-benchmarks-more/"},{"title":"MMLU - Wikipedia","url":"https://en.wikipedia.org/wiki/MMLU"},{"title":"Min istral 3 (3B Reasoning 2512): Pricing, Benchmarks & Performance","url":"https://llm-stats.com/models/ministral-3b-latest"},{"title":"MMLU | DeepEval by Confident AI - The LLM Evaluation Framework","url":"https://deepeval.com/docs/benchmarks-mmlu"},{"title":"Ministral 3","url":"https://arxiv.org/html/2601.08584v1"},{"title":"What is MMLU? LLM Benchmark Explained and Why It Matters | DataCamp","url":"https://www.datacamp.com/blog/what-is-mmlu"},{"title":"MMLU Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/mmlu"}]

Now let me search for more specific information about the training data composition:

Links: [{"title":"Ministral 3","url":"https://arxiv.org/html/2601.08584v1"},{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"},{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"Ministral 3 3B - Mistral AI | Mistral Docs","url":"https://docs.mistral.ai/models/ministral-3-3b-25-12"},{"title":"Fine-Tuning Ministral 3: A Step-by-Step Guide to Training a Vision-Language Model for X-Ray Classification | DataCamp","url":"https://www.datacamp.com/tutorial/fine-tuning-ministral-3"},{"title":"Mistral 3 Models on DigitalOcean | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/mistral-3-models"},{"title":"Mistral Large 3: An Open-Source MoE LLM Explained | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mistral-large-3-moe-llm-explained"},{"title":"mistralai/Ministral-3-3B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512"},{"title":"mistralai/Ministral-3-3B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-3B-Base-2512"},{"title":"Mistral 3 : Best Open-sourced model is here !! | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/mistral-3-best-open-sourced-model-is-here-3b93a6b2b2e8"}]

Based on my web search results, here's a comprehensive summary of the Ministral 3 models:

## Release Information

The Ministral 3 models were released on December 1, 2025, and added to Hugging Face Transformers on the same date. The models were updated on December 2, 2025.

## Model Sizes and HuggingFace Repository IDs

The Ministral 3 family consists of edge models with Base, Instruct, and Reasoning variants in three different sizes: 3B, 8B, and 14B. The HuggingFace repository IDs follow the pattern:
- `mistralai/Ministral-3-3B-Base-2512`, `mistralai/Ministral-3-3B-Instruct-2512`, `mistralai/Ministral-3-3B-Reasoning-2512`
- `mistralai/Ministral-3-8B-Base-2512`, `mistralai/Ministral-3-8B-Instruct-2512`, `mistralai/Ministral-3-8B-Reasoning-2512`
- `mistralai/Ministral-3-14B-Base-2512`, `mistralai/Ministral-3-14B-Instruct-2512`, `mistralai/Ministral-3-14B-Reasoning-2512`

## Training Methodology

A key component of Ministral 3 is the Cascade Distillation training strategy, an iterative pruning and distillation method which progressively transfers pretrained knowledge from a large parent model down to a family of compact children models. Pretraining starts from pruning the parent model, Mistral Small 3.1, into the largest child model (14B), which continues pretraining with logit distillation from the parent model as the teacher to obtain the short context child model, followed by another round of distillation with a longer context window to obtain the final Ministral 3 14B Base model.

## Training Data

Mistral does not publicly disclose its dataset composition, which is common practice. However, given the model's strong multilingual performance, it likely included diverse sources (Web text, books, code, etc. in many languages) in training.

## MMLU Benchmark Performance

On Multilingual MMLU, Ministral 3 14B Base 2512 achieved 74.2% and Ministral 3 8B Base 2512 achieved 70.6%. For external benchmarks, Ministral 3 was evaluated on MMLU, MMLU-Redux, ARC-Challenge, RACE High, TriviaQA, NaturalQS, and AGIEval.

## Additional Features

All models have vision capabilities. All models use a vocabulary size of 131K tokens. All models are released under the Apache 2.0 license.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "433ca3d6-6f1c-4449-9159-8cf2b156952a"
}
```

</details>

---

### System

_source line 283_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Gemma 4 base model HuggingFace 2026 parameters 12…",
  "usage": {
    "total_tokens": 40155,
    "tool_uses": 23,
    "duration_ms": 119820
  },
  "last_tool_name": "WebSearch",
  "uuid": "3b31cbbc-df30-4b0c-b8a5-321f86f5181d",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 284_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HhNCBBiqo47LzXPRX9cdr4`</summary>

```json
{
  "query": "Gemma 4 base model HuggingFace 2026 parameters 12B release date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "52f08d55-8531-4bdc-8434-36b387941ab5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDvLGxMTiu64i81AFWsSpo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1902,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 35593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2469,
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

### System

_source line 285_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "description": "Searching for Phi-4 reasoning 14B HuggingFace release date gate…",
  "usage": {
    "total_tokens": 40156,
    "tool_uses": 24,
    "duration_ms": 120486
  },
  "last_tool_name": "WebSearch",
  "uuid": "5e649f86-9873-45d9-a86d-a23627e45b69",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool call

_source line 286_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B6jYQCh3LrWW2wng68aAbb`</summary>

```json
{
  "query": "Phi-4 reasoning 14B HuggingFace release date gated benchmark AIME MATH training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "0f96a87d-653d-4621-be3f-10cfd4b8a5f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDvLGxMTiu64i81AFWsSpo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1902,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 35593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2469,
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

_source line 287 · 2026-05-18T07:09:53.054Z_

<details><summary>↩ Tool result · `toolu_01HhNCBBiqo47LzXPRX9cdr4`</summary>

```text
Web search results for query: "Gemma 4 base model HuggingFace 2026 parameters 12B release date"

Links: [{"title":"Gemma4 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma4"},{"title":"google/gemma-4-31B · Hugging Face","url":"https://huggingface.co/google/gemma-4-31B"},{"title":"nvidia/Gemma-4-26B-A4B-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Gemma-4-26B-A4B-NVFP4"},{"title":"Gemma 4 model overview | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core"},{"title":"google/gemma-4-26B-A4B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-26B-A4B-it"},{"title":"google/gemma-4-31B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-31B-it"},{"title":"Welcome Gemma 4: Frontier multimodal intelligence on device","url":"https://huggingface.co/blog/gemma4"},{"title":"nvidia/Gemma-4-31B-IT-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Gemma-4-31B-IT-NVFP4"},{"title":"google/gemma-4-E4B · Hugging Face","url":"https://huggingface.co/google/gemma-4-E4B"},{"title":"Gemma 4: Our most capable open models to date","url":"https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/"}]

Based on the search results, here's what I found regarding Gemma 4:

## Gemma 4 Model Overview

Gemma 4 is a multimodal model with pretrained and instruction-tuned variants, available in E2B, E4B, 31B and 26B-A4B (MoE) parameter sizes. 

**Important Note:** The search results do not show a 12B base model variant. The available sizes are E2B, E4B, 26B A4B, and 31B.

## Release Date

The model was added to Hugging Face Transformers on 2026-04-01.

## Model Characteristics

Gemma 4 models are multimodal, handling text and image input (with audio supported on small models) and generating text output. Gemma 4 features a context window of up to 256K tokens and maintains multilingual support in over 140 languages.

If you were specifically looking for information about a 12B parameter model, it doesn't appear to be part of the Gemma 4 family based on the available documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "c149174f-7c35-4964-9236-c1b5a6566968"
}
```

</details>

---

### Tool result

_source line 288 · 2026-05-18T07:09:55.734Z_

<details><summary>↩ Tool result · `toolu_01B6jYQCh3LrWW2wng68aAbb`</summary>

```text
Web search results for query: "Phi-4 reasoning 14B HuggingFace release date gated benchmark AIME MATH training"

Links: [{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"microsoft/Phi-4-mini-flash-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-flash-reasoning"},{"title":"Microsoft Phi-4 Reasoning: Small Model, Big Math | Awesome Agents","url":"https://awesomeagents.ai/reviews/review-phi-4-reasoning/"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"Phi 4 Reasoning Benchmarks, Model Specs, and Comparisons - DEV Community","url":"https://dev.to/best_codes/phi-4-reasoning-benchmarks-model-specs-and-comparisons-4hk"},{"title":"unsloth/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/unsloth/Phi-4-reasoning-plus"},{"title":"unsloth/Phi-4-reasoning-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Phi-4-reasoning-GGUF"},{"title":"microsoft/Phi-4-mini-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-reasoning"},{"title":"Microsoft Launches Two Powerful Phi-4 Reasoning Models","url":"https://www.analyticsvidhya.com/blog/2025/05/phi-4-reasoning-models/"}]

Based on the search results, here's comprehensive information about Phi-4 reasoning models:

## Release Timeline

The original Phi-4 (14B) was released in December 2024 under MIT license. Phi-4-reasoning and Phi-4-reasoning-plus were released simultaneously on April 30, 2025. Phi-4-mini-flash-reasoning was released on July 9, 2025.

## Model Specifications

The core text models are Phi-4-reasoning and Phi-4-reasoning-plus, both 14B parameters with a 32K token context window. Both ship under MIT license, run locally via Ollama on a consumer GPU, and cost nothing to download.

## Benchmark Performance

When Phi-4-reasoning was released in April 2025, it scored 75.3% on AIME 2024, beating DeepSeek-R1-Distill-70B (69.3%). The stronger sibling, Phi-4-reasoning-plus, pushed that number to 81.3%.

The models were evaluated on AIME 2025, 2024, 2023, and 2022 (math olympiad questions), GPQA-Diamond (complex, graduate-level science questions), and OmniMath (collection of over 4000 olympiad-level math problems with human annotation).

## Training Data

The training data is a mixture of Q&A, chat format data in math, science, and coding, with chat prompts sourced from filtered high-quality web data and optionally rewritten through a synthetic data generation pipeline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "92b127b7-2538-43d9-9c74-4e4f3887c91e"
}
```

</details>

---

### System

_source line 289_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a72b4b1ce170203bc",
  "tool_use_id": "toolu_01XSzbYG4aNMXhPUJ8DwFSt1",
  "status": "completed",
  "output_file": "",
  "summary": "Search batch 4: DeepSeek + Phi",
  "usage": {
    "total_tokens": 42114,
    "tool_uses": 24,
    "duration_ms": 198279
  },
  "uuid": "cb0bf515-c7c7-4553-ab0e-6c7b32955ed9",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool result

_source line 290 · 2026-05-18T07:11:04.389Z_

<details><summary>↩ Tool result · `toolu_01XSzbYG4aNMXhPUJ8DwFSt1`</summary>

```text
Here is the compiled structured report of all findings.

---

## Search 1: DeepSeek V3 Base Model

DeepSeek-V3 is **not** in the 7B-14B range. It is a large MoE model. However, the DeepSeek ecosystem includes several models that do fall in the target range.

### DeepSeek-V3 (for reference, out of range)
- **Full name:** DeepSeek-V3
- **HuggingFace repo:** `deepseek-ai/DeepSeek-V3-Base`
- **Total parameters:** 671B (+14B MTP module = 685B total weights)
- **Active parameters:** 37B per token
- **Architecture:** MoE (256 experts)
- **Release date:** December 2024 (V3-0324 update March 2025; V3.1 and V3.2 followed)
- **Gated:** No (MIT license)
- **Base version exists:** Yes (`deepseek-ai/DeepSeek-V3-Base`)
- **Training data:** ~14.8T tokens
- **NOT in 7B-14B range**

### DeepSeek-V2-Lite (in range)
- **Full name:** DeepSeek-V2-Lite
- **HuggingFace repo:** `deepseek-ai/DeepSeek-V2-Lite`
- **Total parameters:** 15.7B
- **Active parameters:** 2.4B per token
- **Architecture:** MoE (2 shared experts + 64 routed experts, 6 activated per token)
- **Release date:** May 7, 2024
- **Gated:** No (MIT license)
- **Base version exists:** Yes (this IS the base version; chat version at `deepseek-ai/DeepSeek-V2-Lite-Chat`)
- **Training data:** 5.7T tokens (same pre-training corpus as DeepSeek-V2)
- **Benchmarks:** Outperforms 7B dense and 16B MoE models on many English/Chinese benchmarks (specific MMLU not retrieved)

### DeepSeek-Coder-V2-Lite-Base (in range)
- **Full name:** DeepSeek-Coder-V2-Lite-Base
- **HuggingFace repo:** `deepseek-ai/DeepSeek-Coder-V2-Lite-Base`
- **Total parameters:** 15.7B (sometimes cited as 16B)
- **Active parameters:** 2.4B per token
- **Architecture:** MoE (2 shared experts + 64 routed experts, 6 activated per token)
- **Release date:** June 2024
- **Gated:** No
- **Base version exists:** Yes (this IS the base; instruct variant at `deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct`)
- **Training data:** Not separately disclosed; code-focused extension of V2 data
- **Benchmarks:** Strong on code intelligence tasks; competes with closed-source models on coding benchmarks

### DeepSeek-R1-Distill-Qwen-14B (in range)
- **Full name:** DeepSeek-R1-Distill-Qwen-14B
- **HuggingFace repo:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`
- **Parameters:** 14B (dense)
- **Architecture:** Dense transformer (based on Qwen2.5-14B)
- **Release date:** January 20, 2025
- **Gated:** No (MIT license for DeepSeek distillation; underlying Qwen2.5 is Apache 2.0)
- **Base version exists:** No -- this is a distilled/fine-tuned model (SFT on 800K reasoning samples from DeepSeek-R1), not a base pretrained model
- **Training data:** Fine-tuned with 800K samples curated from DeepSeek-R1 outputs
- **Benchmarks:** AIME 2024: 69.7%, MATH-500: 93.9% (pass@1 with temperature=0.6, top-p=0.95, 64 samples)

### DeepSeek-R1-Distill-Qwen-7B (in range)
- **Full name:** DeepSeek-R1-Distill-Qwen-7B
- **HuggingFace repo:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`
- **Parameters:** 7B (dense)
- **Architecture:** Dense transformer (based on Qwen2.5-7B)
- **Release date:** January 20, 2025
- **Gated:** No
- **Base version exists:** No -- distilled model, not base pretrained
- **Training data:** Fine-tuned with 800K samples from DeepSeek-R1

---

## Search 2: Phi-4 Base Model

### Phi-4 (14B base)
- **Full name:** Phi-4
- **HuggingFace repo:** `microsoft/phi-4`
- **Parameters:** 14.7B (dense)
- **Architecture:** Dense decoder-only transformer
- **Release date:** December 2024 (initially on Azure; open-sourced on HuggingFace January 2025)
- **Gated:** No (MIT license, fully open access)
- **Base version exists:** Yes -- `microsoft/phi-4` IS the base pretrained model
- **Training data:** 9.8T tokens; mix of synthetic data (generated by GPT-4o), high-quality web content, educational data, code, academic books, Q&A datasets
- **Context length:** 16K tokens
- **Benchmarks:** MMLU: 84.8%, MATH: 80.4%, HumanEval: 82.6%

### Phi-4-reasoning (14B, fine-tuned)
- **Full name:** Phi-4-reasoning
- **HuggingFace repo:** `microsoft/Phi-4-reasoning`
- **Parameters:** 14B (dense)
- **Release date:** April 30, 2025
- **Gated:** No (MIT license)
- **Base version exists:** Not a base model; fine-tuned from Phi-4 for reasoning
- **Benchmarks:** AIME 2024: 75.3%

### Phi-4-reasoning-plus (14B, fine-tuned)
- **Full name:** Phi-4-reasoning-plus
- **HuggingFace repo:** `microsoft/Phi-4-reasoning-plus`
- **Parameters:** 14B (dense)
- **Release date:** April 30, 2025
- **Gated:** No (MIT license)
- **Base version exists:** Not a base model
- **Benchmarks:** AIME 2024: 81.3%

### Phi-4-mini-instruct (3.8B, NOT in 7B-14B range)
- **Full name:** Phi-4-mini-instruct
- **HuggingFace repo:** `microsoft/Phi-4-mini-instruct`
- **Parameters:** 3.8B (dense)
- **Release date:** March 19, 2026
- **Training data:** 5T tokens
- **Context length:** 128K tokens
- **Benchmarks:** MMLU: ~73% (matches Llama 3.1 8B)
- **NOT in 7B-14B range**

---

## Search 3: DeepSeek R2

**DeepSeek R2 has NOT been released as of May 2026.** Key findings:

- DeepSeek R2 was widely anticipated as the second-generation reasoning model.
- It was reportedly slated for release in H1 2025 but was delayed.
- The delay was caused by failed training runs on Huawei Ascend AI chips (stability problems, slow interconnect, immature software tooling).
- As of April 2026, DeepSeek instead released DeepSeek-V4-Pro (1.6T parameters) and DeepSeek-V4-Flash (284B parameters) with 1M token context windows.
- R2 is NOT listed in the official DeepSeek API model list as of May 2026.
- No HuggingFace repository exists for DeepSeek R2.

---

## Additional Models Found in the 7B-14B Range (2025-2026)

### Qwen3-14B-Base
- **HuggingFace repo:** `Qwen/Qwen3-14B-Base`
- **Parameters:** 14B (dense)
- **Architecture:** Dense transformer
- **Release date:** April 29, 2025
- **Gated:** No (Apache 2.0)
- **Base version exists:** Yes (this IS the base)
- **Training data:** ~36T tokens covering 119 languages (3-stage pretraining: S1 >30T tokens at 4K context, S2 +5T tokens STEM-heavy, S3 long-context extension to 32K)
- **Benchmarks:** MMLU: 81.05 (base model). Performance matches Qwen2.5-32B-Base.

### Qwen3-8B-Base
- **HuggingFace repo:** `Qwen/Qwen3-8B-Base`
- **Parameters:** 8B (dense)
- **Architecture:** Dense transformer
- **Release date:** April 29, 2025
- **Gated:** No (Apache 2.0)
- **Base version exists:** Yes
- **Training data:** ~36T tokens (same corpus as all Qwen3 models)
- **Benchmarks:** Performance matches Qwen2.5-14B-Base

### Gemma 3 12B (pretrained base)
- **Full name:** Gemma 3 12B PT
- **HuggingFace repo:** `google/gemma-3-12b-pt`
- **Parameters:** 12B (dense)
- **Architecture:** Dense transformer, multimodal (text+image input, text output)
- **Release date:** March 12, 2025
- **Gated:** Yes (requires agreeing to Google's usage license on HuggingFace)
- **Base version exists:** Yes (`google/gemma-3-12b-pt` is the pretrained base)
- **Training data:** 12T tokens
- **Context length:** 128K tokens
- **Benchmarks:** Specific MMLU for 12B not retrieved; 27B version: MMLU-Pro 67.5

### Ministral-3-14B-Base-2512
- **Full name:** Ministral 3 14B Base
- **HuggingFace repo:** `mistralai/Ministral-3-14B-Base-2512`
- **Parameters:** 14B (dense)
- **Architecture:** Dense transformer with vision capabilities
- **Release date:** December 1, 2025
- **Gated:** No (Apache 2.0)
- **Base version exists:** Yes (this IS the base)
- **Training data:** Not publicly disclosed. Trained via cascade distillation from Mistral Small 3.1 (24B parent)
- **Vocab size:** 131K tokens
- **Benchmarks:** Multilingual MMLU: 74.2%. Reasoning variant achieves 85% on AIME 2025.

### Ministral-3-8B-Base-2512
- **Full name:** Ministral 3 8B Base
- **HuggingFace repo:** `mistralai/Ministral-3-8B-Base-2512`
- **Parameters:** 8B (dense)
- **Architecture:** Dense transformer with vision capabilities
- **Release date:** December 1, 2025
- **Gated:** No (Apache 2.0)
- **Base version exists:** Yes
- **Training data:** Not disclosed. Cascade distillation from Ministral 3 14B.
- **Benchmarks:** Multilingual MMLU: 70.6%. Outperforms Gemma 3 12B on most evaluations except TriviaQA.

### Llama 4 Scout (out of strict 7B-14B range but noteworthy for active params)
- **Full name:** Llama 4 Scout 17B-16E
- **HuggingFace repo:** `meta-llama/Llama-4-Scout-17B-16E`
- **Total parameters:** ~109B
- **Active parameters:** 17B per token
- **Architecture:** MoE (16 experts)
- **Release date:** April 2025
- **Gated:** Yes (Meta Community License, 700M MAU clause)
- **Base version exists:** Yes (base and instruct variants both available)
- **Training data:** ~40T tokens (multimodal)
- **Context length:** 256K (pretrained), 10M (instruct)
- **Note:** While total params are 109B, active params (17B) are close to the 14B range. This is an MoE model.

---

## Summary Table: Models with Base Versions in the 7B-14B Dense Parameter Range

| Model | HF Repo ID | Params | Architecture | Release | License | Gated | Training Data | Base Exists | MMLU |
|---|---|---|---|---|---|---|---|---|---|
| **Phi-4** | `microsoft/phi-4` | 14.7B dense | Dense | Dec 2024 / Jan 2025 | MIT | No | 9.8T tokens | Yes | 84.8% |
| **Qwen3-14B** | `Qwen/Qwen3-14B-Base` | 14B dense | Dense | Apr 29, 2025 | Apache 2.0 | No | ~36T tokens | Yes | 81.05% |
| **Qwen3-8B** | `Qwen/Qwen3-8B-Base` | 8B dense | Dense | Apr 29, 2025 | Apache 2.0 | No | ~36T tokens | Yes | -- |
| **Gemma 3 12B** | `google/gemma-3-12b-pt` | 12B dense | Dense | Mar 12, 2025 | Gemma license | Yes | 12T tokens | Yes | -- |
| **Ministral 3 14B** | `mistralai/Ministral-3-14B-Base-2512` | 14B dense | Dense | Dec 1, 2025 | Apache 2.0 | No | Undisclosed | Yes | 74.2% (multilingual) |
| **Ministral 3 8B** | `mistralai/Ministral-3-8B-Base-2512` | 8B dense | Dense | Dec 1, 2025 | Apache 2.0 | No | Undisclosed | Yes | 70.6% (multilingual) |
| **DeepSeek-V2-Lite** | `deepseek-ai/DeepSeek-V2-Lite` | 15.7B total / **2.4B active** | **MoE** | May 7, 2024 | MIT | No | 5.7T tokens | Yes | -- |
| **DeepSeek-Coder-V2-Lite** | `deepseek-ai/DeepSeek-Coder-V2-Lite-Base` | 15.7B total / **2.4B active** | **MoE** | Jun 2024 | MIT | No | Undisclosed | Yes | -- |

## MoE Models Near the Range (for reference)

| Model | Total Params | Active Params | Experts | Notes |
|---|---|---|---|---|
| DeepSeek-V2-Lite | 15.7B | 2.4B | 64 routed + 2 shared, 6 active | Smallest DeepSeek MoE |
| DeepSeek-Coder-V2-Lite | 15.7B | 2.4B | Same as above | Code-focused variant |
| Llama 4 Scout | ~109B | 17B | 16 experts | Active params close to range |
| Gemma 4 26B-A4B | 25.2B | 3.8B | MoE | Out of range but notable |
| DeepSeek-V3 | 671B | 37B | 256 experts | Far out of range |

## Key Takeaway for Your Paper

For an academic paper needing open-source base (non-instruct) LLMs in the 7B-14B dense parameter range released in 2025-2026, the strongest candidates are:

1. **Phi-4** (`microsoft/phi-4`) -- 14.7B, MIT, not gated, highest MMLU at 84.8%
2. **Qwen3-14B-Base** (`Qwen/Qwen3-14B-Base`) -- 14B, Apache 2.0, not gated, MMLU 81.05%, largest training corpus (36T tokens)
3. **Qwen3-8B-Base** (`Qwen/Qwen3-8B-Base`) -- 8B, Apache 2.0, not gated
4. **Gemma 3 12B PT** (`google/gemma-3-12b-pt`) -- 12B, gated (license agreement required)
5. **Ministral 3 14B Base** (`mistralai/Ministral-3-14B-Base-2512`) -- 14B, Apache 2.0, Dec 2025
6. **Ministral 3 8B Base** (`mistralai/Ministral-3-8B-Base-2512`) -- 8B, Apache 2.0, Dec 2025

DeepSeek R2 does not exist yet. DeepSeek V3 is far too large (671B). The DeepSeek-R1-Distill models (7B/14B) exist but are fine-tuned reasoning models, not base pretrained models.

agentId: a72b4b1ce170203bc (use SendMessage with to: 'a72b4b1ce170203bc' to continue this agent)
&lt;usage>total_tokens: 46413
tool_uses: 24
duration_ms: 198282&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "b3b8c1b4-7f9c-41d4-ad56-68c6a45a7422",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"DeepSeek V3 base model\"\nSearch 2: \"Phi-4 base model\"\nSearch 3: \"DeepSeek R2 base model 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range. Also note if any of these models use MoE architecture (mixture of experts) and what the active parameter count is.",
    "agentId": "a72b4b1ce170203bc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the compiled structured report of all findings.\n\n---\n\n## Search 1: DeepSeek V3 Base Model\n\nDeepSeek-V3 is **not** in the 7B-14B range. It is a large MoE model. However, the DeepSeek ecosystem includes several models that do fall in the target range.\n\n### DeepSeek-V3 (for reference, out of range)\n- **Full name:** DeepSeek-V3\n- **HuggingFace repo:** `deepseek-ai/DeepSeek-V3-Base`\n- **Total parameters:** 671B (+14B MTP module = 685B total weights)\n- **Active parameters:** 37B per token\n- **Architecture:** MoE (256 experts)\n- **Release date:** December 2024 (V3-0324 update March 2025; V3.1 and V3.2 followed)\n- **Gated:** No (MIT license)\n- **Base version exists:** Yes (`deepseek-ai/DeepSeek-V3-Base`)\n- **Training data:** ~14.8T tokens\n- **NOT in 7B-14B range**\n\n### DeepSeek-V2-Lite (in range)\n- **Full name:** DeepSeek-V2-Lite\n- **HuggingFace repo:** `deepseek-ai/DeepSeek-V2-Lite`\n- **Total parameters:** 15.7B\n- **Active parameters:** 2.4B per token\n- **Architecture:** MoE (2 shared experts + 64 routed experts, 6 activated per token)\n- **Release date:** May 7, 2024\n- **Gated:** No (MIT license)\n- **Base version exists:** Yes (this IS the base version; chat version at `deepseek-ai/DeepSeek-V2-Lite-Chat`)\n- **Training data:** 5.7T tokens (same pre-training corpus as DeepSeek-V2)\n- **Benchmarks:** Outperforms 7B dense and 16B MoE models on many English/Chinese benchmarks (specific MMLU not retrieved)\n\n### DeepSeek-Coder-V2-Lite-Base (in range)\n- **Full name:** DeepSeek-Coder-V2-Lite-Base\n- **HuggingFace repo:** `deepseek-ai/DeepSeek-Coder-V2-Lite-Base`\n- **Total parameters:** 15.7B (sometimes cited as 16B)\n- **Active parameters:** 2.4B per token\n- **Architecture:** MoE (2 shared experts + 64 routed experts, 6 activated per token)\n- **Release date:** June 2024\n- **Gated:** No\n- **Base version exists:** Yes (this IS the base; instruct variant at `deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct`)\n- **Training data:** Not separately disclosed; code-focused extension of V2 data\n- **Benchmarks:** Strong on code intelligence tasks; competes with closed-source models on coding benchmarks\n\n### DeepSeek-R1-Distill-Qwen-14B (in range)\n- **Full name:** DeepSeek-R1-Distill-Qwen-14B\n- **HuggingFace repo:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`\n- **Parameters:** 14B (dense)\n- **Architecture:** Dense transformer (based on Qwen2.5-14B)\n- **Release date:** January 20, 2025\n- **Gated:** No (MIT license for DeepSeek distillation; underlying Qwen2.5 is Apache 2.0)\n- **Base version exists:** No -- this is a distilled/fine-tuned model (SFT on 800K reasoning samples from DeepSeek-R1), not a base pretrained model\n- **Training data:** Fine-tuned with 800K samples curated from DeepSeek-R1 outputs\n- **Benchmarks:** AIME 2024: 69.7%, MATH-500: 93.9% (pass@1 with temperature=0.6, top-p=0.95, 64 samples)\n\n### DeepSeek-R1-Distill-Qwen-7B (in range)\n- **Full name:** DeepSeek-R1-Distill-Qwen-7B\n- **HuggingFace repo:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`\n- **Parameters:** 7B (dense)\n- **Architecture:** Dense transformer (based on Qwen2.5-7B)\n- **Release date:** January 20, 2025\n- **Gated:** No\n- **Base version exists:** No -- distilled model, not base pretrained\n- **Training data:** Fine-tuned with 800K samples from DeepSeek-R1\n\n---\n\n## Search 2: Phi-4 Base Model\n\n### Phi-4 (14B base)\n- **Full name:** Phi-4\n- **HuggingFace repo:** `microsoft/phi-4`\n- **Parameters:** 14.7B (dense)\n- **Architecture:** Dense decoder-only transformer\n- **Release date:** December 2024 (initially on Azure; open-sourced on HuggingFace January 2025)\n- **Gated:** No (MIT license, fully open access)\n- **Base version exists:** Yes -- `microsoft/phi-4` IS the base pretrained model\n- **Training data:** 9.8T tokens; mix of synthetic data (generated by GPT-4o), high-quality web content, educational data, code, academic books, Q&A datasets\n- **Context length:** 16K tokens\n- **Benchmarks:** MMLU: 84.8%, MATH: 80.4%, HumanEval: 82.6%\n\n### Phi-4-reasoning (14B, fine-tuned)\n- **Full name:** Phi-4-reasoning\n- **HuggingFace repo:** `microsoft/Phi-4-reasoning`\n- **Parameters:** 14B (dense)\n- **Release date:** April 30, 2025\n- **Gated:** No (MIT license)\n- **Base version exists:** Not a base model; fine-tuned from Phi-4 for reasoning\n- **Benchmarks:** AIME 2024: 75.3%\n\n### Phi-4-reasoning-plus (14B, fine-tuned)\n- **Full name:** Phi-4-reasoning-plus\n- **HuggingFace repo:** `microsoft/Phi-4-reasoning-plus`\n- **Parameters:** 14B (dense)\n- **Release date:** April 30, 2025\n- **Gated:** No (MIT license)\n- **Base version exists:** Not a base model\n- **Benchmarks:** AIME 2024: 81.3%\n\n### Phi-4-mini-instruct (3.8B, NOT in 7B-14B range)\n- **Full name:** Phi-4-mini-instruct\n- **HuggingFace repo:** `microsoft/Phi-4-mini-instruct`\n- **Parameters:** 3.8B (dense)\n- **Release date:** March 19, 2026\n- **Training data:** 5T tokens\n- **Context length:** 128K tokens\n- **Benchmarks:** MMLU: ~73% (matches Llama 3.1 8B)\n- **NOT in 7B-14B range**\n\n---\n\n## Search 3: DeepSeek R2\n\n**DeepSeek R2 has NOT been released as of May 2026.** Key findings:\n\n- DeepSeek R2 was widely anticipated as the second-generation reasoning model.\n- It was reportedly slated for release in H1 2025 but was delayed.\n- The delay was caused by failed training runs on Huawei Ascend AI chips (stability problems, slow interconnect, immature software tooling).\n- As of April 2026, DeepSeek instead released DeepSeek-V4-Pro (1.6T parameters) and DeepSeek-V4-Flash (284B parameters) with 1M token context windows.\n- R2 is NOT listed in the official DeepSeek API model list as of May 2026.\n- No HuggingFace repository exists for DeepSeek R2.\n\n---\n\n## Additional Models Found in the 7B-14B Range (2025-2026)\n\n### Qwen3-14B-Base\n- **HuggingFace repo:** `Qwen/Qwen3-14B-Base`\n- **Parameters:** 14B (dense)\n- **Architecture:** Dense transformer\n- **Release date:** April 29, 2025\n- **Gated:** No (Apache 2.0)\n- **Base version exists:** Yes (this IS the base)\n- **Training data:** ~36T tokens covering 119 languages (3-stage pretraining: S1 >30T tokens at 4K context, S2 +5T tokens STEM-heavy, S3 long-context extension to 32K)\n- **Benchmarks:** MMLU: 81.05 (base model). Performance matches Qwen2.5-32B-Base.\n\n### Qwen3-8B-Base\n- **HuggingFace repo:** `Qwen/Qwen3-8B-Base`\n- **Parameters:** 8B (dense)\n- **Architecture:** Dense transformer\n- **Release date:** April 29, 2025\n- **Gated:** No (Apache 2.0)\n- **Base version exists:** Yes\n- **Training data:** ~36T tokens (same corpus as all Qwen3 models)\n- **Benchmarks:** Performance matches Qwen2.5-14B-Base\n\n### Gemma 3 12B (pretrained base)\n- **Full name:** Gemma 3 12B PT\n- **HuggingFace repo:** `google/gemma-3-12b-pt`\n- **Parameters:** 12B (dense)\n- **Architecture:** Dense transformer, multimodal (text+image input, text output)\n- **Release date:** March 12, 2025\n- **Gated:** Yes (requires agreeing to Google's usage license on HuggingFace)\n- **Base version exists:** Yes (`google/gemma-3-12b-pt` is the pretrained base)\n- **Training data:** 12T tokens\n- **Context length:** 128K tokens\n- **Benchmarks:** Specific MMLU for 12B not retrieved; 27B version: MMLU-Pro 67.5\n\n### Ministral-3-14B-Base-2512\n- **Full name:** Ministral 3 14B Base\n- **HuggingFace repo:** `mistralai/Ministral-3-14B-Base-2512`\n- **Parameters:** 14B (dense)\n- **Architecture:** Dense transformer with vision capabilities\n- **Release date:** December 1, 2025\n- **Gated:** No (Apache 2.0)\n- **Base version exists:** Yes (this IS the base)\n- **Training data:** Not publicly disclosed. Trained via cascade distillation from Mistral Small 3.1 (24B parent)\n- **Vocab size:** 131K tokens\n- **Benchmarks:** Multilingual MMLU: 74.2%. Reasoning variant achieves 85% on AIME 2025.\n\n### Ministral-3-8B-Base-2512\n- **Full name:** Ministral 3 8B Base\n- **HuggingFace repo:** `mistralai/Ministral-3-8B-Base-2512`\n- **Parameters:** 8B (dense)\n- **Architecture:** Dense transformer with vision capabilities\n- **Release date:** December 1, 2025\n- **Gated:** No (Apache 2.0)\n- **Base version exists:** Yes\n- **Training data:** Not disclosed. Cascade distillation from Ministral 3 14B.\n- **Benchmarks:** Multilingual MMLU: 70.6%. Outperforms Gemma 3 12B on most evaluations except TriviaQA.\n\n### Llama 4 Scout (out of strict 7B-14B range but noteworthy for active params)\n- **Full name:** Llama 4 Scout 17B-16E\n- **HuggingFace repo:** `meta-llama/Llama-4-Scout-17B-16E`\n- **Total parameters:** ~109B\n- **Active parameters:** 17B per token\n- **Architecture:** MoE (16 experts)\n- **Release date:** April 2025\n- **Gated:** Yes (Meta Community License, 700M MAU clause)\n- **Base version exists:** Yes (base and instruct variants both available)\n- **Training data:** ~40T tokens (multimodal)\n- **Context length:** 256K (pretrained), 10M (instruct)\n- **Note:** While total params are 109B, active params (17B) are close to the 14B range. This is an MoE model.\n\n---\n\n## Summary Table: Models with Base Versions in the 7B-14B Dense Parameter Range\n\n| Model | HF Repo ID | Params | Architecture | Release | License | Gated | Training Data | Base Exists | MMLU |\n|---|---|---|---|---|---|---|---|---|---|\n| **Phi-4** | `microsoft/phi-4` | 14.7B dense | Dense | Dec 2024 / Jan 2025 | MIT | No | 9.8T tokens | Yes | 84.8% |\n| **Qwen3-14B** | `Qwen/Qwen3-14B-Base` | 14B dense | Dense | Apr 29, 2025 | Apache 2.0 | No | ~36T tokens | Yes | 81.05% |\n| **Qwen3-8B** | `Qwen/Qwen3-8B-Base` | 8B dense | Dense | Apr 29, 2025 | Apache 2.0 | No | ~36T tokens | Yes | -- |\n| **Gemma 3 12B** | `google/gemma-3-12b-pt` | 12B dense | Dense | Mar 12, 2025 | Gemma license | Yes | 12T tokens | Yes | -- |\n| **Ministral 3 14B** | `mistralai/Ministral-3-14B-Base-2512` | 14B dense | Dense | Dec 1, 2025 | Apache 2.0 | No | Undisclosed | Yes | 74.2% (multilingual) |\n| **Ministral 3 8B** | `mistralai/Ministral-3-8B-Base-2512` | 8B dense | Dense | Dec 1, 2025 | Apache 2.0 | No | Undisclosed | Yes | 70.6% (multilingual) |\n| **DeepSeek-V2-Lite** | `deepseek-ai/DeepSeek-V2-Lite` | 15.7B total / **2.4B active** | **MoE** | May 7, 2024 | MIT | No | 5.7T tokens | Yes | -- |\n| **DeepSeek-Coder-V2-Lite** | `deepseek-ai/DeepSeek-Coder-V2-Lite-Base` | 15.7B total / **2.4B active** | **MoE** | Jun 2024 | MIT | No | Undisclosed | Yes | -- |\n\n## MoE Models Near the Range (for reference)\n\n| Model | Total Params | Active Params | Experts | Notes |\n|---|---|---|---|---|\n| DeepSeek-V2-Lite | 15.7B | 2.4B | 64 routed + 2 shared, 6 active | Smallest DeepSeek MoE |\n| DeepSeek-Coder-V2-Lite | 15.7B | 2.4B | Same as above | Code-focused variant |\n| Llama 4 Scout | ~109B | 17B | 16 experts | Active params close to range |\n| Gemma 4 26B-A4B | 25.2B | 3.8B | MoE | Out of range but notable |\n| DeepSeek-V3 | 671B | 37B | 256 experts | Far out of range |\n\n## Key Takeaway for Your Paper\n\nFor an academic paper needing open-source base (non-instruct) LLMs in the 7B-14B dense parameter range released in 2025-2026, the strongest candidates are:\n\n1. **Phi-4** (`microsoft/phi-4`) -- 14.7B, MIT, not gated, highest MMLU at 84.8%\n2. **Qwen3-14B-Base** (`Qwen/Qwen3-14B-Base`) -- 14B, Apache 2.0, not gated, MMLU 81.05%, largest training corpus (36T tokens)\n3. **Qwen3-8B-Base** (`Qwen/Qwen3-8B-Base`) -- 8B, Apache 2.0, not gated\n4. **Gemma 3 12B PT** (`google/gemma-3-12b-pt`) -- 12B, gated (license agreement required)\n5. **Ministral 3 14B Base** (`mistralai/Ministral-3-14B-Base-2512`) -- 14B, Apache 2.0, Dec 2025\n6. **Ministral 3 8B Base** (`mistralai/Ministral-3-8B-Base-2512`) -- 8B, Apache 2.0, Dec 2025\n\nDeepSeek R2 does not exist yet. DeepSeek V3 is far too large (671B). The DeepSeek-R1-Distill models (7B/14B) exist but are fine-tuned reasoning models, not base pretrained models."
      }
    ],
    "totalDurationMs": 198282,
    "totalTokens": 46413,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3858,
      "cache_read_input_tokens": 38062,
      "output_tokens": 4492,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4492,
          "cache_read_input_tokens": 38062,
          "cache_creation_input_tokens": 3858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3858,
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
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 24
    }
  }
}
```

</details>

---

### System

_source line 291_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a07b72467ddf2db7b",
  "tool_use_id": "toolu_019GEYgwrqvsAqC9HcwLnZ7s",
  "status": "completed",
  "output_file": "",
  "summary": "Search batch 1: general + HF",
  "usage": {
    "total_tokens": 49865,
    "tool_uses": 33,
    "duration_ms": 233528
  },
  "uuid": "c03470f7-1ac0-4533-ac14-bb156a3017d6",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37"
}
```

---

### Tool result

_source line 292 · 2026-05-18T07:11:31.980Z_

<details><summary>↩ Tool result · `toolu_019GEYgwrqvsAqC9HcwLnZ7s`</summary>

```text
Now I have comprehensive data. Here is the structured compilation of all findings.

---

## Open-Source Base LLMs (7B-14B Parameters) Released 2024-2026

### 1. Qwen3-8B-Base (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen3-8B-Base |
| **HuggingFace Repo** | `Qwen/Qwen3-8B-Base` |
| **Parameters** | 8B (7.6B non-embedding) |
| **Release Date** | May 2025 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 36T tokens, 119 languages |
| **Benchmarks** | MMLU ~74.7; performs on par with Qwen2.5-14B-Base. Top HumanEval (76.0) under 8B. Strong CJK multilingual. |

### 2. Qwen3-14B-Base (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen3-14B-Base |
| **HuggingFace Repo** | `Qwen/Qwen3-14B-Base` |
| **Parameters** | 14.8B (13.2B non-embedding), 40 layers, GQA (40 Q heads / 8 KV heads) |
| **Release Date** | May 2025 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 36T tokens, 119 languages |
| **Benchmarks** | Performs on par with Qwen2.5-32B-Base; outperforms larger Qwen2.5 in STEM, coding, reasoning. Context 32K. |

### 3. Qwen2.5-7B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-7B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-7B` |
| **Parameters** | 7B |
| **Release Date** | September 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 18T tokens |
| **Benchmarks** | MMLU 74.2, MATH 49.8, HumanEval 57.9. Context 128K, generates up to 8K tokens. |

### 4. Qwen2.5-14B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-14B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-14B` |
| **Parameters** | 14B |
| **Release Date** | September 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | Up to 18T tokens |
| **Benchmarks** | MMLU 79.7. Context 128K. |

### 5. Qwen2.5-Coder-7B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-Coder-7B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-Coder-7B` |
| **Parameters** | 7B |
| **Release Date** | Late 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 5.5T tokens (source code, text-code grounding, synthetic data) |
| **Benchmarks** | Outperforms general-purpose models 2x its size on code generation. Fits 8GB VRAM. |

### 6. Qwen2.5-Coder-14B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-Coder-14B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-Coder-14B` |
| **Parameters** | 14B |
| **Release Date** | Late 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 5.5T tokens |
| **Benchmarks** | Sweet spot for 16GB VRAM; stronger multi-file reasoning and algorithm implementation vs 7B. |

### 7. Gemma 3 12B (Google)

| Field | Detail |
|---|---|
| **Full Name** | Gemma 3 12B |
| **HuggingFace Repo** | `google/gemma-3-12b-pt` (pretrained) / `google/gemma-3-12b-it` (instruct) |
| **Parameters** | 12B |
| **Release Date** | March 12, 2025 |
| **Gated** | Yes (requires Google usage license agreement) |
| **Base Version Exists** | Yes (`gemma-3-12b-pt`) |
| **Training Data** | 12T tokens |
| **Benchmarks** | Global-MMLU-Lite 69.4 (base); MMLU-Pro 59.5 (IT). Native vision support, 128K context, 140+ languages. |

### 8. Gemma 2 9B (Google)

| Field | Detail |
|---|---|
| **Full Name** | Gemma 2 9B |
| **HuggingFace Repo** | `google/gemma-2-9b` |
| **Parameters** | 9B |
| **Release Date** | July 2024 |
| **Gated** | Yes (Google usage license) |
| **Base Version Exists** | Yes |
| **Training Data** | 8T tokens; trained with knowledge distillation |
| **Benchmarks** | OpenLLM v1 average 73.23 (IT). Interleaved local/global attention, GQA. Competitive with 2x-size models. |

### 9. Phi-4 14B (Microsoft)

| Field | Detail |
|---|---|
| **Full Name** | Phi-4 |
| **HuggingFace Repo** | `microsoft/phi-4` |
| **Parameters** | 14.7B |
| **Release Date** | December 2024 |
| **Gated** | No (MIT license) |
| **Base Version Exists** | Yes (the `microsoft/phi-4` model is the base) |
| **Training Data** | Extension of Phi-3 data: filtered web docs, educational data, synthetic "textbook-like" data for math/coding/reasoning, academic books, Q&A datasets. ~8% multilingual. |
| **Benchmarks** | MMLU 84.8 (surpasses Llama-3.3-70B). Q5_K_M variant reaches 76.2 MMLU. Strong in reasoning and math. |

### 10. Llama 3.1 8B (Meta)

| Field | Detail |
|---|---|
| **Full Name** | Llama 3.1 8B |
| **HuggingFace Repo** | `meta-llama/Llama-3.1-8B` |
| **Parameters** | 8B |
| **Release Date** | July 23, 2024 |
| **Gated** | Yes (Llama 3.1 Community License) |
| **Base Version Exists** | Yes |
| **Training Data** | ~15T multilingual tokens |
| **Benchmarks** | MMLU 65.6 (5-shot, base). 128K context window. |

### 11. Llama 3 8B (Meta)

| Field | Detail |
|---|---|
| **Full Name** | Meta-Llama-3-8B |
| **HuggingFace Repo** | `meta-llama/Meta-Llama-3-8B` |
| **Parameters** | 8B |
| **Release Date** | April 18, 2024 |
| **Gated** | Yes (Llama 3 Community License) |
| **Base Version Exists** | Yes |
| **Training Data** | ~15T tokens |
| **Benchmarks** | Predecessor to 3.1; widely used baseline. |

### 12. DeepSeek-R1-Distill-Qwen-7B (DeepSeek)

| Field | Detail |
|---|---|
| **Full Name** | DeepSeek-R1-Distill-Qwen-7B |
| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` |
| **Parameters** | 7B |
| **Release Date** | January 2025 |
| **Gated** | No (Apache 2.0, inherited from Qwen2.5) |
| **Base Version Exists** | This is a distilled/fine-tuned model (from Qwen2.5 base), not a pretrained-from-scratch base |
| **Training Data** | Distilled from DeepSeek-R1 with 800K curated reasoning samples |
| **Benchmarks** | Strong chain-of-thought reasoning; inherits R1's reasoning capabilities at 7B scale. |

### 13. DeepSeek-R1-Distill-Qwen-14B (DeepSeek)

| Field | Detail |
|---|---|
| **Full Name** | DeepSeek-R1-Distill-Qwen-14B |
| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` |
| **Parameters** | 14B |
| **Release Date** | January 2025 |
| **Gated** | No (Apache 2.0, inherited from Qwen2.5) |
| **Base Version Exists** | Distilled model, not pretrained base |
| **Training Data** | 800K curated samples from DeepSeek-R1 |
| **Benchmarks** | Strongest distilled reasoning model at 14B scale. |

### 14. DeepSeek-R1-Distill-Llama-8B (DeepSeek)

| Field | Detail |
|---|---|
| **Full Name** | DeepSeek-R1-Distill-Llama-8B |
| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |
| **Parameters** | 8B |
| **Release Date** | January 2025 |
| **Gated** | Llama 3.1 license (inherited from Llama3.1-8B-Base) |
| **Base Version Exists** | Distilled model built on Llama 3.1 8B base |
| **Training Data** | 800K curated samples from DeepSeek-R1 |
| **Benchmarks** | Reasoning-enhanced Llama variant. |

### 15. Falcon 3 7B (TII)

| Field | Detail |
|---|---|
| **Full Name** | Falcon3-7B-Base |
| **HuggingFace Repo** | `tiiuae/Falcon3-7B-Base` |
| **Parameters** | 7B |
| **Release Date** | December 2024 |
| **Gated** | No (TII Falcon License 2.0; compatible with Llama architecture) |
| **Base Version Exists** | Yes |
| **Training Data** | 14T tokens (web, code, STEM, multilingual: EN/FR/ES/PT) |
| **Benchmarks** | MMLU 67.4, MMLU-PRO 39.2. On par with Qwen2.5-7B among sub-9B models. |

### 16. Falcon 3 10B (TII)

| Field | Detail |
|---|---|
| **Full Name** | Falcon3-10B-Base |
| **HuggingFace Repo** | `tiiuae/Falcon3-10B-Base` |
| **Parameters** | 10B |
| **Release Date** | December 2024 |
| **Gated** | No |
| **Base Version Exists** | Yes |
| **Training Data** | Upscaled from 7B + 2T additional tokens (web, code, STEM) |
| **Benchmarks** | MMLU 73.1, MMLU-PRO 42.5. SOTA zero-shot and few-shot for sub-13B models. |

### 17. Falcon-H1-7B (TII)

| Field | Detail |
|---|---|
| **Full Name** | Falcon-H1-7B-Base |
| **HuggingFace Repo** | `tiiuae/Falcon-H1-7B-Base` |
| **Parameters** | 7B |
| **Release Date** | 2025 |
| **Gated** | No |
| **Base Version Exists** | Yes |
| **Training Data** | Not specified in search results |
| **Benchmarks** | Hybrid Transformer + SSM (Mamba) architecture. 256K context. 18 native languages. Adjustable attention/SSM ratio for efficiency. |

### 18. OLMo 2 7B (Allen AI)

| Field | Detail |
|---|---|
| **Full Name** | OLMo-2-1124-7B |
| **HuggingFace Repo** | `allenai/OLMo-2-1124-7B` |
| **Parameters** | 7B |
| **Release Date** | November 2024 |
| **Gated** | No (fully open: data, code, weights, training logs) |
| **Base Version Exists** | Yes |
| **Training Data** | ~5T tokens (OLMo-Mix-1124: DCLM, Dolma, Starcoder, Proof Pile II) |
| **Benchmarks** | MMLU 63.7. Outperforms Llama-3.1-8B. Staged training approach. |

### 19. OLMo 2 13B (Allen AI)

| Field | Detail |
|---|---|
| **Full Name** | OLMo-2-1124-13B |
| **HuggingFace Repo** | `allenai/OLMo-2-1124-13B` |
| **Parameters** | 13B |
| **Release Date** | November 2024 |
| **Gated** | No (fully open) |
| **Base Version Exists** | Yes |
| **Training Data** | ~5T tokens (1.2 epochs) |
| **Benchmarks** | MMLU 67.5. Outperforms Qwen2.5-7B despite lower training FLOPs. |

### 20. OLMo 3 7B (Allen AI)

| Field | Detail |
|---|---|
| **Full Name** | Olmo-3-1025-7B |
| **HuggingFace Repo** | `allenai/Olmo-3-1025-7B` |
| **Parameters** | 7B |
| **Release Date** | October 2025 |
| **Gated** | No (Apache 2.0; fully open) |
| **Base Version Exists** | Yes |
| **Training Data** | ~5.93T tokens (dolma3_6T-mix-1025). Mix: 20% code, 28% web, 19% math, 14% QA, 8% thinking, 6% instruction, 5% PDFs. |
| **Benchmarks** | Successor to OLMo 2; details in paper at allenai.org/papers/olmo3. |

### 21. Mistral Nemo 12B (Mistral AI / NVIDIA)

| Field | Detail |
|---|---|
| **Full Name** | Mistral-NeMo-12B-Base |
| **HuggingFace Repo** | `mistralai/Mistral-Nemo-Base-2407` (also `nvidia/Mistral-NeMo-12B-Base`) |
| **Parameters** | 12B |
| **Release Date** | July 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | Trained May-June 2024; 80+ programming languages, multilingual (EN/FR/DE/ES/IT/PT/ZH/JA/KO/AR/HI) |
| **Benchmarks** | MMLU 68.0 (5-shot), HellaSwag 83.5, Winogrande 76.8, TriviaQA 73.8. Outperforms Gemma 2 9B and Llama 3 8B. |

### 22. InternLM3 8B (Shanghai AI Lab)

| Field | Detail |
|---|---|
| **Full Name** | InternLM3-8B |
| **HuggingFace Repo** | `internlm/internlm3-8b-instruct` (instruct version released; base checkpoint may be in the `internlm` collection) |
| **Parameters** | 8B |
| **Release Date** | January 15, 2025 |
| **Gated** | No |
| **Base Version Exists** | Instruct version publicly available; base checkpoint availability unclear from search results |
| **Training Data** | 4T tokens (claimed 75% training cost savings vs comparable models) |
| **Benchmarks** | Surpasses Llama3.1-8B and Qwen2.5-7B on reasoning/knowledge tasks. Supports deep thinking (long CoT) mode. |

### 23. Yi-1.5-9B (01.AI)

| Field | Detail |
|---|---|
| **Full Name** | Yi-1.5-9B |
| **HuggingFace Repo** | `01-ai/Yi-1.5-9B` |
| **Parameters** | 9B |
| **Release Date** | May 13, 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | Bilingual (EN/ZH); 34B variant trained on 3.1T tokens (9B likely similar or subset) |
| **Benchmarks** | MMLU 76.3, BBH 54.3, C-Eval 81.4. Top performer among similarly sized open-source models. GQA + SwiGLU architecture. |

### 24. MAP-Neo 7B (MAP)

| Field | Detail |
|---|---|
| **Full Name** | MAP-Neo 7B |
| **HuggingFace Repo** | `m-a-p/neo_7b` |
| **Parameters** | 7B |
| **Release Date** | Mid 2024 |
| **Gated** | No (commercial use permitted) |
| **Base Version Exists** | Yes |
| **Training Data** | 4.5T tokens (English + Chinese). Fully open: data pipeline, cleaning code, all checkpoints, tokenizer. |
| **Benchmarks** | Comparable to LLaMA 2 7B. Strong in reasoning, math, coding. Fully reproducible (all artifacts released). |

### 25. StarCoder2-7B (BigCode)

| Field | Detail |
|---|---|
| **Full Name** | StarCoder2-7B |
| **HuggingFace Repo** | `bigcode/starcoder2-7b` |
| **Parameters** | 7B |
| **Release Date** | February 28, 2024 |
| **Gated** | No (BigCode OpenRAIL-M v1) |
| **Base Version Exists** | Yes (code-only base model) |
| **Training Data** | 3.5T+ tokens, 17 programming languages (The Stack v2) |
| **Benchmarks** | Code generation specialist. GQA, 16K context, sliding window attention 4K. Fill-in-the-Middle objective. |

### 26. StarCoder2-15B (BigCode)

| Field | Detail |
|---|---|
| **Full Name** | StarCoder2-15B |
| **HuggingFace Repo** | `bigcode/starcoder2-15b` |
| **Parameters** | 15B (slightly above 14B range, included for completeness) |
| **Release Date** | February 28, 2024 |
| **Gated** | No (BigCode OpenRAIL-M v1) |
| **Base Version Exists** | Yes (code-only base model) |
| **Training Data** | 4T+ tokens, 600+ programming languages (The Stack v2) |
| **Benchmarks** | Strongest code model in its size class at release. 16K context. |

### 27. Mistral Small 3 24B (Mistral AI) [NOTE: Not 7B]

| Field | Detail |
|---|---|
| **Full Name** | Mistral-Small-24B-Base-2501 |
| **HuggingFace Repo** | `mistralai/Mistral-Small-24B-Base-2501` (also Instruct: `mistralai/Mistral-Small-3.1-24B-Instruct-2503`) |
| **Parameters** | 24B (outside 7B-14B range) |
| **Release Date** | January 2025 |
| **Gated** | No |
| **Base Version Exists** | Yes |
| **Note** | Included because some sources incorrectly describe it as "7B." Actual parameter count is 24B. MMLU >81%, ~150 tokens/s, MT-Bench 8.0. |

---

## Summary: Models Strictly in 7B-14B Range with Base Versions Available

| Model | Params | Release | License | Training Data | MMLU (base) | HF Repo |
|---|---|---|---|---|---|---|
| Qwen3-8B-Base | 8B | May 2025 | Apache 2.0 | 36T tokens | ~74.7 | `Qwen/Qwen3-8B-Base` |
| Qwen3-14B-Base | 14.8B | May 2025 | Apache 2.0 | 36T tokens | ~Qwen2.5-32B level | `Qwen/Qwen3-14B-Base` |
| Qwen2.5-7B | 7B | Sep 2024 | Apache 2.0 | 18T tokens | 74.2 | `Qwen/Qwen2.5-7B` |
| Qwen2.5-14B | 14B | Sep 2024 | Apache 2.0 | 18T tokens | 79.7 | `Qwen/Qwen2.5-14B` |
| Qwen2.5-Coder-7B | 7B | Late 2024 | Apache 2.0 | 5.5T tokens | Code specialist | `Qwen/Qwen2.5-Coder-7B` |
| Qwen2.5-Coder-14B | 14B | Late 2024 | Apache 2.0 | 5.5T tokens | Code specialist | `Qwen/Qwen2.5-Coder-14B` |
| Phi-4 | 14.7B | Dec 2024 | MIT | Synthetic+web+academic | 84.8 | `microsoft/phi-4` |
| Gemma 3 12B | 12B | Mar 2025 | Google license (gated) | 12T tokens | GMMLU 69.4 | `google/gemma-3-12b-pt` |
| Gemma 2 9B | 9B | Jul 2024 | Google license (gated) | 8T tokens | ~68-70 est. | `google/gemma-2-9b` |
| Llama 3.1 8B | 8B | Jul 2024 | Llama license (gated) | 15T tokens | 65.6 | `meta-llama/Llama-3.1-8B` |
| Mistral Nemo 12B | 12B | Jul 2024 | Apache 2.0 | Multilingual | 68.0 | `mistralai/Mistral-Nemo-Base-2407` |
| Falcon3-7B | 7B | Dec 2024 | Falcon License 2.0 | 14T tokens | 67.4 | `tiiuae/Falcon3-7B-Base` |
| Falcon3-10B | 10B | Dec 2024 | Falcon License 2.0 | 7B+2T upscale | 73.1 | `tiiuae/Falcon3-10B-Base` |
| Falcon-H1-7B | 7B | 2025 | Open | Not specified | Hybrid SSM+Attn | `tiiuae/Falcon-H1-7B-Base` |
| OLMo 2 7B | 7B | Nov 2024 | Apache 2.0 (fully open) | 5T tokens | 63.7 | `allenai/OLMo-2-1124-7B` |
| OLMo 2 13B | 13B | Nov 2024 | Apache 2.0 (fully open) | 5T tokens | 67.5 | `allenai/OLMo-2-1124-13B` |
| OLMo 3 7B | 7B | Oct 2025 | Apache 2.0 (fully open) | 5.93T tokens | Improved over OLMo 2 | `allenai/Olmo-3-1025-7B` |
| InternLM3 8B | 8B | Jan 2025 | Open | 4T tokens | Beats Llama3.1-8B | `internlm/internlm3-8b-instruct` |
| Yi-1.5-9B | 9B | May 2024 | Apache 2.0 | ~3T tokens | 76.3 | `01-ai/Yi-1.5-9B` |
| MAP-Neo 7B | 7B | Mid 2024 | Open (commercial OK) | 4.5T tokens | ~LLaMA2-7B level | `m-a-p/neo_7b` |
| StarCoder2-7B | 7B | Feb 2024 | OpenRAIL-M | 3.5T tokens | Code specialist | `bigcode/starcoder2-7b` |
| DeepSeek-R1-Distill-Qwen-7B | 7B | Jan 2025 | Apache 2.0 | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` |
| DeepSeek-R1-Distill-Qwen-14B | 14B | Jan 2025 | Apache 2.0 | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` |
| DeepSeek-R1-Distill-Llama-8B | 8B | Jan 2025 | Llama 3.1 license | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |

---

## Key Observations for Academic Paper Use

1. **Strongest base models by MMLU in range**: Phi-4 (84.8) > Qwen2.5-14B (79.7) > Yi-1.5-9B (76.3) > Qwen3-8B (~74.7) > Qwen2.5-7B (74.2) > Falcon3-10B (73.1)

2. **Fully open models** (data + code + weights): OLMo 2/3 (Allen AI) and MAP-Neo are the only models with complete reproducibility artifacts (training data, pipeline code, all checkpoints).

3. **2025-2026 releases**: Qwen3-8B-Base, Qwen3-14B-Base, Gemma 3 12B, InternLM3-8B, OLMo 3 7B, Falcon-H1-7B, DeepSeek-R1 distilled variants.

4. **Llama 4 does NOT have a dense 7B-14B base model**. Llama 4 uses MoE: Scout (109B total, 17B active) and Maverick (400B total, 17B active). The last dense Llama base in this range is Llama 3.1 8B.

5. **Gated models** requiring license agreement: All Gemma models (Google), all Llama models (Meta). Non-gated: Qwen, Phi-4, Falcon, OLMo, Mistral Nemo, Yi, MAP-Neo, StarCoder2.

6. **Gemma 4** was released April 2, 2026 but its sizes are E2B, E4B, 26B-A4B, and 31B (none in the 7B-14B dense range).

Sources:
- [Qwen3-8B-Base on HuggingFace](https://huggingface.co/Qwen/Qwen3-8B-Base)
- [Qwen3 Blog Post](https://qwenlm.github.io/blog/qwen3/)
- [Qwen3-14B-Base on HuggingFace](https://huggingface.co/Qwen/Qwen3-14B-Base)
- [Qwen2.5-7B on HuggingFace](https://huggingface.co/Qwen/Qwen2.5-7B)
- [Qwen2.5-14B on HuggingFace](https://huggingface.co/Qwen/Qwen2.5-14B)
- [Qwen2.5 Technical Report](https://arxiv.org/pdf/2412.15115)
- [Phi-4 on HuggingFace](https://huggingface.co/microsoft/phi-4)
- [Phi-4 Technical Report](https://arxiv.org/html/2412.08905v1)
- [Gemma 3 12B Pretrained](https://huggingface.co/google/gemma-3-12b-pt)
- [Gemma 3 Blog](https://huggingface.co/blog/gemma3)
- [Gemma 2 9B](https://huggingface.co/google/gemma-2-9b)
- [Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B)
- [Mistral Nemo Base](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407)
- [Falcon3-7B-Base](https://huggingface.co/tiiuae/Falcon3-7B-Base)
- [Falcon3-10B-Base](https://huggingface.co/tiiuae/Falcon3-10B-Base)
- [Falcon3 Blog](https://huggingface.co/blog/falcon3)
- [Falcon-H1 Blog](https://falcon-lm.github.io/blog/falcon-h1/)
- [OLMo 2 Collection](https://huggingface.co/collections/allenai/olmo-2)
- [OLMo 2 Blog](https://allenai.org/blog/olmo2)
- [OLMo 3 7B](https://huggingface.co/allenai/Olmo-3-1025-7B)
- [InternLM3-8B](https://huggingface.co/internlm/internlm3-8b-instruct)
- [Yi-1.5-9B](https://huggingface.co/01-ai/Yi-1.5-9B)
- [MAP-Neo 7B](https://huggingface.co/m-a-p/neo_7b)
- [StarCoder2-7B](https://huggingface.co/bigcode/starcoder2-7b)
- [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)
- [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B)
- [Open-Source LLM Landscape 2026](https://presenc.ai/research/open-source-llm-landscape-2026)
- [Featherless Best Open-Source LLMs 2026](https://featherless.ai/blog/best-open-source-llms-2026)
- [HuggingFace State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [Gemma 4 Overview](https://ai.google.dev/gemma/docs/core)

agentId: a07b72467ddf2db7b (use SendMessage with to: 'a07b72467ddf2db7b' to continue this agent)
&lt;usage>total_tokens: 57338
tool_uses: 33
duration_ms: 233530&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "c96b92d4-ef3e-48e4-b0ed-2ca63b335621",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"best open source LLM 2025 2026 base model\"\nSearch 2: \"latest base models huggingface 2025\"\nSearch 3: \"new open source LLM families 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range.",
    "agentId": "a07b72467ddf2db7b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Here is the structured compilation of all findings.\n\n---\n\n## Open-Source Base LLMs (7B-14B Parameters) Released 2024-2026\n\n### 1. Qwen3-8B-Base (Alibaba)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Qwen3-8B-Base |\n| **HuggingFace Repo** | `Qwen/Qwen3-8B-Base` |\n| **Parameters** | 8B (7.6B non-embedding) |\n| **Release Date** | May 2025 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 36T tokens, 119 languages |\n| **Benchmarks** | MMLU ~74.7; performs on par with Qwen2.5-14B-Base. Top HumanEval (76.0) under 8B. Strong CJK multilingual. |\n\n### 2. Qwen3-14B-Base (Alibaba)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Qwen3-14B-Base |\n| **HuggingFace Repo** | `Qwen/Qwen3-14B-Base` |\n| **Parameters** | 14.8B (13.2B non-embedding), 40 layers, GQA (40 Q heads / 8 KV heads) |\n| **Release Date** | May 2025 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 36T tokens, 119 languages |\n| **Benchmarks** | Performs on par with Qwen2.5-32B-Base; outperforms larger Qwen2.5 in STEM, coding, reasoning. Context 32K. |\n\n### 3. Qwen2.5-7B (Alibaba)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Qwen2.5-7B |\n| **HuggingFace Repo** | `Qwen/Qwen2.5-7B` |\n| **Parameters** | 7B |\n| **Release Date** | September 2024 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 18T tokens |\n| **Benchmarks** | MMLU 74.2, MATH 49.8, HumanEval 57.9. Context 128K, generates up to 8K tokens. |\n\n### 4. Qwen2.5-14B (Alibaba)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Qwen2.5-14B |\n| **HuggingFace Repo** | `Qwen/Qwen2.5-14B` |\n| **Parameters** | 14B |\n| **Release Date** | September 2024 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | Up to 18T tokens |\n| **Benchmarks** | MMLU 79.7. Context 128K. |\n\n### 5. Qwen2.5-Coder-7B (Alibaba)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Qwen2.5-Coder-7B |\n| **HuggingFace Repo** | `Qwen/Qwen2.5-Coder-7B` |\n| **Parameters** | 7B |\n| **Release Date** | Late 2024 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 5.5T tokens (source code, text-code grounding, synthetic data) |\n| **Benchmarks** | Outperforms general-purpose models 2x its size on code generation. Fits 8GB VRAM. |\n\n### 6. Qwen2.5-Coder-14B (Alibaba)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Qwen2.5-Coder-14B |\n| **HuggingFace Repo** | `Qwen/Qwen2.5-Coder-14B` |\n| **Parameters** | 14B |\n| **Release Date** | Late 2024 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 5.5T tokens |\n| **Benchmarks** | Sweet spot for 16GB VRAM; stronger multi-file reasoning and algorithm implementation vs 7B. |\n\n### 7. Gemma 3 12B (Google)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Gemma 3 12B |\n| **HuggingFace Repo** | `google/gemma-3-12b-pt` (pretrained) / `google/gemma-3-12b-it` (instruct) |\n| **Parameters** | 12B |\n| **Release Date** | March 12, 2025 |\n| **Gated** | Yes (requires Google usage license agreement) |\n| **Base Version Exists** | Yes (`gemma-3-12b-pt`) |\n| **Training Data** | 12T tokens |\n| **Benchmarks** | Global-MMLU-Lite 69.4 (base); MMLU-Pro 59.5 (IT). Native vision support, 128K context, 140+ languages. |\n\n### 8. Gemma 2 9B (Google)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Gemma 2 9B |\n| **HuggingFace Repo** | `google/gemma-2-9b` |\n| **Parameters** | 9B |\n| **Release Date** | July 2024 |\n| **Gated** | Yes (Google usage license) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 8T tokens; trained with knowledge distillation |\n| **Benchmarks** | OpenLLM v1 average 73.23 (IT). Interleaved local/global attention, GQA. Competitive with 2x-size models. |\n\n### 9. Phi-4 14B (Microsoft)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Phi-4 |\n| **HuggingFace Repo** | `microsoft/phi-4` |\n| **Parameters** | 14.7B |\n| **Release Date** | December 2024 |\n| **Gated** | No (MIT license) |\n| **Base Version Exists** | Yes (the `microsoft/phi-4` model is the base) |\n| **Training Data** | Extension of Phi-3 data: filtered web docs, educational data, synthetic \"textbook-like\" data for math/coding/reasoning, academic books, Q&A datasets. ~8% multilingual. |\n| **Benchmarks** | MMLU 84.8 (surpasses Llama-3.3-70B). Q5_K_M variant reaches 76.2 MMLU. Strong in reasoning and math. |\n\n### 10. Llama 3.1 8B (Meta)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Llama 3.1 8B |\n| **HuggingFace Repo** | `meta-llama/Llama-3.1-8B` |\n| **Parameters** | 8B |\n| **Release Date** | July 23, 2024 |\n| **Gated** | Yes (Llama 3.1 Community License) |\n| **Base Version Exists** | Yes |\n| **Training Data** | ~15T multilingual tokens |\n| **Benchmarks** | MMLU 65.6 (5-shot, base). 128K context window. |\n\n### 11. Llama 3 8B (Meta)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Meta-Llama-3-8B |\n| **HuggingFace Repo** | `meta-llama/Meta-Llama-3-8B` |\n| **Parameters** | 8B |\n| **Release Date** | April 18, 2024 |\n| **Gated** | Yes (Llama 3 Community License) |\n| **Base Version Exists** | Yes |\n| **Training Data** | ~15T tokens |\n| **Benchmarks** | Predecessor to 3.1; widely used baseline. |\n\n### 12. DeepSeek-R1-Distill-Qwen-7B (DeepSeek)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | DeepSeek-R1-Distill-Qwen-7B |\n| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` |\n| **Parameters** | 7B |\n| **Release Date** | January 2025 |\n| **Gated** | No (Apache 2.0, inherited from Qwen2.5) |\n| **Base Version Exists** | This is a distilled/fine-tuned model (from Qwen2.5 base), not a pretrained-from-scratch base |\n| **Training Data** | Distilled from DeepSeek-R1 with 800K curated reasoning samples |\n| **Benchmarks** | Strong chain-of-thought reasoning; inherits R1's reasoning capabilities at 7B scale. |\n\n### 13. DeepSeek-R1-Distill-Qwen-14B (DeepSeek)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | DeepSeek-R1-Distill-Qwen-14B |\n| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` |\n| **Parameters** | 14B |\n| **Release Date** | January 2025 |\n| **Gated** | No (Apache 2.0, inherited from Qwen2.5) |\n| **Base Version Exists** | Distilled model, not pretrained base |\n| **Training Data** | 800K curated samples from DeepSeek-R1 |\n| **Benchmarks** | Strongest distilled reasoning model at 14B scale. |\n\n### 14. DeepSeek-R1-Distill-Llama-8B (DeepSeek)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | DeepSeek-R1-Distill-Llama-8B |\n| **HuggingFace Repo** | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |\n| **Parameters** | 8B |\n| **Release Date** | January 2025 |\n| **Gated** | Llama 3.1 license (inherited from Llama3.1-8B-Base) |\n| **Base Version Exists** | Distilled model built on Llama 3.1 8B base |\n| **Training Data** | 800K curated samples from DeepSeek-R1 |\n| **Benchmarks** | Reasoning-enhanced Llama variant. |\n\n### 15. Falcon 3 7B (TII)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Falcon3-7B-Base |\n| **HuggingFace Repo** | `tiiuae/Falcon3-7B-Base` |\n| **Parameters** | 7B |\n| **Release Date** | December 2024 |\n| **Gated** | No (TII Falcon License 2.0; compatible with Llama architecture) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 14T tokens (web, code, STEM, multilingual: EN/FR/ES/PT) |\n| **Benchmarks** | MMLU 67.4, MMLU-PRO 39.2. On par with Qwen2.5-7B among sub-9B models. |\n\n### 16. Falcon 3 10B (TII)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Falcon3-10B-Base |\n| **HuggingFace Repo** | `tiiuae/Falcon3-10B-Base` |\n| **Parameters** | 10B |\n| **Release Date** | December 2024 |\n| **Gated** | No |\n| **Base Version Exists** | Yes |\n| **Training Data** | Upscaled from 7B + 2T additional tokens (web, code, STEM) |\n| **Benchmarks** | MMLU 73.1, MMLU-PRO 42.5. SOTA zero-shot and few-shot for sub-13B models. |\n\n### 17. Falcon-H1-7B (TII)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Falcon-H1-7B-Base |\n| **HuggingFace Repo** | `tiiuae/Falcon-H1-7B-Base` |\n| **Parameters** | 7B |\n| **Release Date** | 2025 |\n| **Gated** | No |\n| **Base Version Exists** | Yes |\n| **Training Data** | Not specified in search results |\n| **Benchmarks** | Hybrid Transformer + SSM (Mamba) architecture. 256K context. 18 native languages. Adjustable attention/SSM ratio for efficiency. |\n\n### 18. OLMo 2 7B (Allen AI)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | OLMo-2-1124-7B |\n| **HuggingFace Repo** | `allenai/OLMo-2-1124-7B` |\n| **Parameters** | 7B |\n| **Release Date** | November 2024 |\n| **Gated** | No (fully open: data, code, weights, training logs) |\n| **Base Version Exists** | Yes |\n| **Training Data** | ~5T tokens (OLMo-Mix-1124: DCLM, Dolma, Starcoder, Proof Pile II) |\n| **Benchmarks** | MMLU 63.7. Outperforms Llama-3.1-8B. Staged training approach. |\n\n### 19. OLMo 2 13B (Allen AI)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | OLMo-2-1124-13B |\n| **HuggingFace Repo** | `allenai/OLMo-2-1124-13B` |\n| **Parameters** | 13B |\n| **Release Date** | November 2024 |\n| **Gated** | No (fully open) |\n| **Base Version Exists** | Yes |\n| **Training Data** | ~5T tokens (1.2 epochs) |\n| **Benchmarks** | MMLU 67.5. Outperforms Qwen2.5-7B despite lower training FLOPs. |\n\n### 20. OLMo 3 7B (Allen AI)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Olmo-3-1025-7B |\n| **HuggingFace Repo** | `allenai/Olmo-3-1025-7B` |\n| **Parameters** | 7B |\n| **Release Date** | October 2025 |\n| **Gated** | No (Apache 2.0; fully open) |\n| **Base Version Exists** | Yes |\n| **Training Data** | ~5.93T tokens (dolma3_6T-mix-1025). Mix: 20% code, 28% web, 19% math, 14% QA, 8% thinking, 6% instruction, 5% PDFs. |\n| **Benchmarks** | Successor to OLMo 2; details in paper at allenai.org/papers/olmo3. |\n\n### 21. Mistral Nemo 12B (Mistral AI / NVIDIA)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Mistral-NeMo-12B-Base |\n| **HuggingFace Repo** | `mistralai/Mistral-Nemo-Base-2407` (also `nvidia/Mistral-NeMo-12B-Base`) |\n| **Parameters** | 12B |\n| **Release Date** | July 2024 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | Trained May-June 2024; 80+ programming languages, multilingual (EN/FR/DE/ES/IT/PT/ZH/JA/KO/AR/HI) |\n| **Benchmarks** | MMLU 68.0 (5-shot), HellaSwag 83.5, Winogrande 76.8, TriviaQA 73.8. Outperforms Gemma 2 9B and Llama 3 8B. |\n\n### 22. InternLM3 8B (Shanghai AI Lab)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | InternLM3-8B |\n| **HuggingFace Repo** | `internlm/internlm3-8b-instruct` (instruct version released; base checkpoint may be in the `internlm` collection) |\n| **Parameters** | 8B |\n| **Release Date** | January 15, 2025 |\n| **Gated** | No |\n| **Base Version Exists** | Instruct version publicly available; base checkpoint availability unclear from search results |\n| **Training Data** | 4T tokens (claimed 75% training cost savings vs comparable models) |\n| **Benchmarks** | Surpasses Llama3.1-8B and Qwen2.5-7B on reasoning/knowledge tasks. Supports deep thinking (long CoT) mode. |\n\n### 23. Yi-1.5-9B (01.AI)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Yi-1.5-9B |\n| **HuggingFace Repo** | `01-ai/Yi-1.5-9B` |\n| **Parameters** | 9B |\n| **Release Date** | May 13, 2024 |\n| **Gated** | No (Apache 2.0) |\n| **Base Version Exists** | Yes |\n| **Training Data** | Bilingual (EN/ZH); 34B variant trained on 3.1T tokens (9B likely similar or subset) |\n| **Benchmarks** | MMLU 76.3, BBH 54.3, C-Eval 81.4. Top performer among similarly sized open-source models. GQA + SwiGLU architecture. |\n\n### 24. MAP-Neo 7B (MAP)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | MAP-Neo 7B |\n| **HuggingFace Repo** | `m-a-p/neo_7b` |\n| **Parameters** | 7B |\n| **Release Date** | Mid 2024 |\n| **Gated** | No (commercial use permitted) |\n| **Base Version Exists** | Yes |\n| **Training Data** | 4.5T tokens (English + Chinese). Fully open: data pipeline, cleaning code, all checkpoints, tokenizer. |\n| **Benchmarks** | Comparable to LLaMA 2 7B. Strong in reasoning, math, coding. Fully reproducible (all artifacts released). |\n\n### 25. StarCoder2-7B (BigCode)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | StarCoder2-7B |\n| **HuggingFace Repo** | `bigcode/starcoder2-7b` |\n| **Parameters** | 7B |\n| **Release Date** | February 28, 2024 |\n| **Gated** | No (BigCode OpenRAIL-M v1) |\n| **Base Version Exists** | Yes (code-only base model) |\n| **Training Data** | 3.5T+ tokens, 17 programming languages (The Stack v2) |\n| **Benchmarks** | Code generation specialist. GQA, 16K context, sliding window attention 4K. Fill-in-the-Middle objective. |\n\n### 26. StarCoder2-15B (BigCode)\n\n| Field | Detail |\n|---|---|\n| **Full Name** | StarCoder2-15B |\n| **HuggingFace Repo** | `bigcode/starcoder2-15b` |\n| **Parameters** | 15B (slightly above 14B range, included for completeness) |\n| **Release Date** | February 28, 2024 |\n| **Gated** | No (BigCode OpenRAIL-M v1) |\n| **Base Version Exists** | Yes (code-only base model) |\n| **Training Data** | 4T+ tokens, 600+ programming languages (The Stack v2) |\n| **Benchmarks** | Strongest code model in its size class at release. 16K context. |\n\n### 27. Mistral Small 3 24B (Mistral AI) [NOTE: Not 7B]\n\n| Field | Detail |\n|---|---|\n| **Full Name** | Mistral-Small-24B-Base-2501 |\n| **HuggingFace Repo** | `mistralai/Mistral-Small-24B-Base-2501` (also Instruct: `mistralai/Mistral-Small-3.1-24B-Instruct-2503`) |\n| **Parameters** | 24B (outside 7B-14B range) |\n| **Release Date** | January 2025 |\n| **Gated** | No |\n| **Base Version Exists** | Yes |\n| **Note** | Included because some sources incorrectly describe it as \"7B.\" Actual parameter count is 24B. MMLU >81%, ~150 tokens/s, MT-Bench 8.0. |\n\n---\n\n## Summary: Models Strictly in 7B-14B Range with Base Versions Available\n\n| Model | Params | Release | License | Training Data | MMLU (base) | HF Repo |\n|---|---|---|---|---|---|---|\n| Qwen3-8B-Base | 8B | May 2025 | Apache 2.0 | 36T tokens | ~74.7 | `Qwen/Qwen3-8B-Base` |\n| Qwen3-14B-Base | 14.8B | May 2025 | Apache 2.0 | 36T tokens | ~Qwen2.5-32B level | `Qwen/Qwen3-14B-Base` |\n| Qwen2.5-7B | 7B | Sep 2024 | Apache 2.0 | 18T tokens | 74.2 | `Qwen/Qwen2.5-7B` |\n| Qwen2.5-14B | 14B | Sep 2024 | Apache 2.0 | 18T tokens | 79.7 | `Qwen/Qwen2.5-14B` |\n| Qwen2.5-Coder-7B | 7B | Late 2024 | Apache 2.0 | 5.5T tokens | Code specialist | `Qwen/Qwen2.5-Coder-7B` |\n| Qwen2.5-Coder-14B | 14B | Late 2024 | Apache 2.0 | 5.5T tokens | Code specialist | `Qwen/Qwen2.5-Coder-14B` |\n| Phi-4 | 14.7B | Dec 2024 | MIT | Synthetic+web+academic | 84.8 | `microsoft/phi-4` |\n| Gemma 3 12B | 12B | Mar 2025 | Google license (gated) | 12T tokens | GMMLU 69.4 | `google/gemma-3-12b-pt` |\n| Gemma 2 9B | 9B | Jul 2024 | Google license (gated) | 8T tokens | ~68-70 est. | `google/gemma-2-9b` |\n| Llama 3.1 8B | 8B | Jul 2024 | Llama license (gated) | 15T tokens | 65.6 | `meta-llama/Llama-3.1-8B` |\n| Mistral Nemo 12B | 12B | Jul 2024 | Apache 2.0 | Multilingual | 68.0 | `mistralai/Mistral-Nemo-Base-2407` |\n| Falcon3-7B | 7B | Dec 2024 | Falcon License 2.0 | 14T tokens | 67.4 | `tiiuae/Falcon3-7B-Base` |\n| Falcon3-10B | 10B | Dec 2024 | Falcon License 2.0 | 7B+2T upscale | 73.1 | `tiiuae/Falcon3-10B-Base` |\n| Falcon-H1-7B | 7B | 2025 | Open | Not specified | Hybrid SSM+Attn | `tiiuae/Falcon-H1-7B-Base` |\n| OLMo 2 7B | 7B | Nov 2024 | Apache 2.0 (fully open) | 5T tokens | 63.7 | `allenai/OLMo-2-1124-7B` |\n| OLMo 2 13B | 13B | Nov 2024 | Apache 2.0 (fully open) | 5T tokens | 67.5 | `allenai/OLMo-2-1124-13B` |\n| OLMo 3 7B | 7B | Oct 2025 | Apache 2.0 (fully open) | 5.93T tokens | Improved over OLMo 2 | `allenai/Olmo-3-1025-7B` |\n| InternLM3 8B | 8B | Jan 2025 | Open | 4T tokens | Beats Llama3.1-8B | `internlm/internlm3-8b-instruct` |\n| Yi-1.5-9B | 9B | May 2024 | Apache 2.0 | ~3T tokens | 76.3 | `01-ai/Yi-1.5-9B` |\n| MAP-Neo 7B | 7B | Mid 2024 | Open (commercial OK) | 4.5T tokens | ~LLaMA2-7B level | `m-a-p/neo_7b` |\n| StarCoder2-7B | 7B | Feb 2024 | OpenRAIL-M | 3.5T tokens | Code specialist | `bigcode/starcoder2-7b` |\n| DeepSeek-R1-Distill-Qwen-7B | 7B | Jan 2025 | Apache 2.0 | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` |\n| DeepSeek-R1-Distill-Qwen-14B | 14B | Jan 2025 | Apache 2.0 | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` |\n| DeepSeek-R1-Distill-Llama-8B | 8B | Jan 2025 | Llama 3.1 license | 800K reasoning samples | Reasoning specialist | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |\n\n---\n\n## Key Observations for Academic Paper Use\n\n1. **Strongest base models by MMLU in range**: Phi-4 (84.8) > Qwen2.5-14B (79.7) > Yi-1.5-9B (76.3) > Qwen3-8B (~74.7) > Qwen2.5-7B (74.2) > Falcon3-10B (73.1)\n\n2. **Fully open models** (data + code + weights): OLMo 2/3 (Allen AI) and MAP-Neo are the only models with complete reproducibility artifacts (training data, pipeline code, all checkpoints).\n\n3. **2025-2026 releases**: Qwen3-8B-Base, Qwen3-14B-Base, Gemma 3 12B, InternLM3-8B, OLMo 3 7B, Falcon-H1-7B, DeepSeek-R1 distilled variants.\n\n4. **Llama 4 does NOT have a dense 7B-14B base model**. Llama 4 uses MoE: Scout (109B total, 17B active) and Maverick (400B total, 17B active). The last dense Llama base in this range is Llama 3.1 8B.\n\n5. **Gated models** requiring license agreement: All Gemma models (Google), all Llama models (Meta). Non-gated: Qwen, Phi-4, Falcon, OLMo, Mistral Nemo, Yi, MAP-Neo, StarCoder2.\n\n6. **Gemma 4** was released April 2, 2026 but its sizes are E2B, E4B, 26B-A4B, and 31B (none in the 7B-14B dense range).\n\nSources:\n- [Qwen3-8B-Base on HuggingFace](https://huggingface.co/Qwen/Qwen3-8B-Base)\n- [Qwen3 Blog Post](https://qwenlm.github.io/blog/qwen3/)\n- [Qwen3-14B-Base on HuggingFace](https://huggingface.co/Qwen/Qwen3-14B-Base)\n- [Qwen2.5-7B on HuggingFace](https://huggingface.co/Qwen/Qwen2.5-7B)\n- [Qwen2.5-14B on HuggingFace](https://huggingface.co/Qwen/Qwen2.5-14B)\n- [Qwen2.5 Technical Report](https://arxiv.org/pdf/2412.15115)\n- [Phi-4 on HuggingFace](https://huggingface.co/microsoft/phi-4)\n- [Phi-4 Technical Report](https://arxiv.org/html/2412.08905v1)\n- [Gemma 3 12B Pretrained](https://huggingface.co/google/gemma-3-12b-pt)\n- [Gemma 3 Blog](https://huggingface.co/blog/gemma3)\n- [Gemma 2 9B](https://huggingface.co/google/gemma-2-9b)\n- [Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B)\n- [Mistral Nemo Base](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407)\n- [Falcon3-7B-Base](https://huggingface.co/tiiuae/Falcon3-7B-Base)\n- [Falcon3-10B-Base](https://huggingface.co/tiiuae/Falcon3-10B-Base)\n- [Falcon3 Blog](https://huggingface.co/blog/falcon3)\n- [Falcon-H1 Blog](https://falcon-lm.github.io/blog/falcon-h1/)\n- [OLMo 2 Collection](https://huggingface.co/collections/allenai/olmo-2)\n- [OLMo 2 Blog](https://allenai.org/blog/olmo2)\n- [OLMo 3 7B](https://huggingface.co/allenai/Olmo-3-1025-7B)\n- [InternLM3-8B](https://huggingface.co/internlm/internlm3-8b-instruct)\n- [Yi-1.5-9B](https://huggingface.co/01-ai/Yi-1.5-9B)\n- [MAP-Neo 7B](https://huggingface.co/m-a-p/neo_7b)\n- [StarCoder2-7B](https://huggingface.co/bigcode/starcoder2-7b)\n- [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)\n- [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B)\n- [Open-Source LLM Landscape 2026](https://presenc.ai/research/open-source-llm-landscape-2026)\n- [Featherless Best Open-Source LLMs 2026](https://featherless.ai/blog/best-open-source-llms-2026)\n- [HuggingFace State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)\n- [Gemma 4 Overview](https://ai.google.dev/gemma/docs/core)"
      }
    ],
    "totalDurationMs": 233530,
    "totalTokens": 57338,
    "totalToolUseCount": 33,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2827,
      "cache_read_input_tokens": 45864,
      "output_tokens": 8646,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2827
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8646,
          "cache_read_input_tokens": 45864,
          "cache_creation_input_tokens": 2827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2827,
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
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 33
    }
  }
}
```

</details>

---

### Assistant

_source line 293_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive results from all 4 search agents. Let me compile everything into a clear recommendation. Let me summarize the key findings:

**2025-2026 base models in 7B-14B range (dense, non-instruct):**

1. **Qwen3-8B-Base** - 8B, Apr 2025, Apache 2.0, not gated, 36T tokens, MMLU 79.66
2. **Qwen3-14B-Base** - 14.8B, Apr 2025, Apache 2.0, not gated, 36T tokens, MMLU 81.05


3. **Gemma 3 12B PT** - 12B, Mar 2025, gated under Google license, 12T tokens, MMLU ~71.9
4. **Phi-4** - 14.7B, Dec 2024/Jan 2025, MIT licensed and openly available, 9.8T tokens, MMLU 84.8
5. **Ministral-3-8B-Base** and **Ministral-3-14B-Base** - 8.4B and 14B respectively, Dec 2025, Apache 2.0, not gated

, with the larger variant showing MMLU 79.4 and multilingual capabilities
6. **OLMo 2** comes in 7B and 13B variants from Nov 2024, fully open under Apache 2.0, with 4T and 5T tokens respectively and MMLU scores of 63.7 and 67.5
7. **Falcon3** has 7B and 10B base models from Dec 2024, not gated, with the 7B trained on 14T tokens and achieving MMLU 67.4

, while the 10B reaches MMLU 73.1
8. **Falcon-H1-7B-Base** is a 2025 model using a hybrid SSM+Attention architecture

Looking at what's actually available, Llama 4 doesn't have a dense model in the 7B-14B range—it's all MoE with 17B active parameters, DeepSeek hasn't released an R2 base model (only R1-Distill variants which are fine-tuned), Qwen3 is a clear step up from Qwen 2.5, and Ministral 3 from December 2025 is the latest Mistral offering in this size range. For the paper's cross-family validation, I'm working with Llama 3.1 as one of the core models.

For the strongest set of five families with recent 2025 or late 2024 base models, I'd go with Qwen3-8B replacing Qwen 2.5, Gemma 3 12B from Google, Phi-4 from Microsoft, Ministral-3-8B replacing Mistral v0.3, and OLMo 2 at either 7B or 13B.

The main trade-off here is that Gemma 3 is gated, and there's no good Llama replacement since Llama 4 doesn't have a dense model in the 7B-14B range. If I want to avoid gated models entirely, I could swap Gemma 3 for Falcon3 at 7B or 10B, keeping the other four and still covering five different families across Qwen, Microsoft, Mistral, Allen AI, and TII.

For the paper itself, having models from 2025 would help address reviewer concerns about recency, and since the work focuses on SFT-injected benchmark contamination and IRT calibration, I need diverse model families anyway. The size consistency question is interesting—the paper uses varying sizes depending on what's available, but the 7B-14B range request seems deliberate, so I should probably respect that constraint and compile the final recommendations accordingly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "81bc8689-174a-4955-90cb-546777d8c9e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkQGBeFJfTNvCwmsKvBzs3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10828,
      "cache_creation_input_tokens": 9929,
      "cache_read_input_tokens": 26657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9929
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 294_

搜索完成。以下是汇总。

---

## 全部候选模型（7B-14B dense base，按推荐度排序）

| 模型 | HF Repo ID | 参数量 | 发布日期 | License | Gated | 训练数据 | MMLU (base) |
|---|---|---|---|---|---|---|---|
| **Qwen3-8B-Base** | `Qwen/Qwen3-8B-Base` | 8.2B | 2025-04 | Apache 2.0 | No | 36T tokens | 79.7 |
| **Qwen3-14B-Base** | `Qwen/Qwen3-14B-Base` | 14.8B | 2025-04 | Apache 2.0 | No | 36T tokens | 81.1 |
| **Phi-4** | `microsoft/phi-4` | 14.7B | 2024-12 | MIT | No | 9.8T tokens | 84.8 |
| **Ministral-3-8B-Base** | `mistralai/Ministral-3-8B-Base-2512` | 8.4B | 2025-12 | Apache 2.0 | No | 未公开 | 70.6 |
| **Ministral-3-14B-Base** | `mistralai/Ministral-3-14B-Base-2512` | ~14B | 2025-12 | Apache 2.0 | No | 未公开 | 79.4 |
| **Gemma 3 12B PT** | `google/gemma-3-12b-pt` | 12B | 2025-03 | Gemma ToU | **Yes** | 12T tokens | 71.9 |
| **OLMo 2 7B** | `allenai/OLMo-2-1124-7B` | 7B | 2024-11 | Apache 2.0 | No | 4T tokens | 63.7 |
| **OLMo 2 13B** | `allenai/OLMo-2-1124-13B` | 13B | 2024-11 | Apache 2.0 | No | 5T tokens | 67.5 |
| **Falcon3-10B-Base** | `tiiuae/Falcon3-10B-Base` | 10B | 2024-12 | Falcon 2.0 | No | 14T+2T | 73.1 |
| **Falcon3-7B-Base** | `tiiuae/Falcon3-7B-Base` | 7B | 2024-12 | Falcon 2.0 | No | 14T tokens | 67.4 |
| **Falcon-H1-7B-Base** | `tiiuae/Falcon-H1-7B-Base` | 7B | 2025 | Open | No | 未公开 | — |
| Qwen2.5-7B | `Qwen/Qwen2.5-7B` | 7B | 2024-09 | Apache 2.0 | No | 18T tokens | 74.2 |
| Qwen2.5-14B | `Qwen/Qwen2.5-14B` | 14B | 2024-09 | Apache 2.0 | No | 18T tokens | 79.7 |
| Mistral-Nemo-12B | `mistralai/Mistral-Nemo-Base-2407` | 12B | 2024-07 | Apache 2.0 | No | 未公开 | 68.0 |
| Llama 3.1 8B | `meta-llama/Llama-3.1-8B` | 8B | 2024-07 | Llama CLA | **Yes** | 15T tokens | 65.6 |
| Yi-1.5-9B | `01-ai/Yi-1.5-9B` | 9B | 2024-05 | Apache 2.0 | No | ~3T tokens | 76.3 |

### 排除的模型
- **Llama 4**: 全部 MoE（Scout 17B active/109B total），无 dense 7B-14B base
- **DeepSeek R2**: 未发布
- **DeepSeek V3/V4**: 671B+ MoE，远超范围
- **DeepSeek-R1-Distill-***: 是 SFT 微调模型，不是 base pretrained model，不适合做 controlled contamination injection
- **Gemma 4**: MoE 架构，无 dense 7B-14B
- **InternLM3-8B**: base checkpoint 未公开发布（仅 instruct）

---

## 推荐

### 1. 最佳 5 模型组合（全部 2024Q4-2025，全部 non-gated）

| Family | 模型 | 理由 |
|---|---|---|
| **Qwen** (Alibaba) | Qwen3-8B-Base | 2025-04，36T tokens，Apache 2.0，MMLU 79.7，直接替代 Qwen 2.5 |
| **Phi** (Microsoft) | Phi-4 | 2024-12，MIT，MMLU 84.8，14.7B 强基线 |
| **Mistral** (Mistral AI) | Ministral-3-8B-Base | 2025-12，Apache 2.0，替代 Mistral v0.3 |
| **OLMo** (Allen AI) | OLMo-2-1124-7B | 完全开源（数据+代码+权重），Apache 2.0，学术可复现性最强 |
| **Falcon** (TII) | Falcon3-10B-Base | 2024-12，14T tokens，MMLU 73.1 |

**优势**：5 个不同机构/家族，全部 non-gated，全部 2024Q4+，覆盖不同训练规模（4T-36T tokens）和能力水平（MMLU 63.7-84.8），审稿人无法质疑模型过时。

**备选**：如果想用 Google 家族替换 Falcon，可选 Gemma 3 12B PT（但 gated）。

### 2. Llama-3.1-8B 的替代

Llama 4 无 dense 7B-14B，所以 Meta 家族无直接替代。最佳替代方案按优先级：

1. **Phi-4** (14.7B) — 不同家族，MIT 开放，性能最强
2. **OLMo-2-7B** — 参数量最接近（7B），完全开源，学术论文天然认可
3. **Falcon3-10B-Base** — 不同家族，non-gated

### 3. Qwen 3 状况

**Qwen3 已发布（2025-04-29）**，有完整的 base 系列。Qwen3-8B-Base 在 36T tokens 上训练，MMLU 79.7（vs Qwen2.5-7B 的 74.2），性能已达 Qwen2.5-14B 水平。**强烈建议用 Qwen3-8B-Base 替换 Qwen 2.5**。技术报告：arXiv 2505.09388。

---

### 实际操作注意

- Phi-4 是 14.7B，bf16 下约 29.4GB，96GB GPU 做 LoRA SFT 无压力
- Ministral-3-8B-Base 是 2025-12 发布，如果论文投稿时间早于此，改用 Mistral-Nemo-Base-2407 (12B, 2024-07)
- OLMo 2 的 MMLU 偏低（63.7），但其完全开源属性在 contamination 研究中是加分项（审稿人重视可复现性）
- Falcon-H1-7B 是 hybrid SSM+Attention 架构，可能引入架构差异混淆因素，建议用 Falcon3 而非 H1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "uuid": "563ff31f-7e37-4d79-b830-d3213eeff35a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkQGBeFJfTNvCwmsKvBzs3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10828,
      "cache_creation_input_tokens": 9929,
      "cache_read_input_tokens": 26657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9929
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 295_

搜索完成。以下是汇总。

---

## 全部候选模型（7B-14B dense base，按推荐度排序）

| 模型 | HF Repo ID | 参数量 | 发布日期 | License | Gated | 训练数据 | MMLU (base) |
|---|---|---|---|---|---|---|---|
| **Qwen3-8B-Base** | `Qwen/Qwen3-8B-Base` | 8.2B | 2025-04 | Apache 2.0 | No | 36T tokens | 79.7 |
| **Qwen3-14B-Base** | `Qwen/Qwen3-14B-Base` | 14.8B | 2025-04 | Apache 2.0 | No | 36T tokens | 81.1 |
| **Phi-4** | `microsoft/phi-4` | 14.7B | 2024-12 | MIT | No | 9.8T tokens | 84.8 |
| **Ministral-3-8B-Base** | `mistralai/Ministral-3-8B-Base-2512` | 8.4B | 2025-12 | Apache 2.0 | No | 未公开 | 70.6 |
| **Ministral-3-14B-Base** | `mistralai/Ministral-3-14B-Base-2512` | ~14B | 2025-12 | Apache 2.0 | No | 未公开 | 79.4 |
| **Gemma 3 12B PT** | `google/gemma-3-12b-pt` | 12B | 2025-03 | Gemma ToU | **Yes** | 12T tokens | 71.9 |
| **OLMo 2 7B** | `allenai/OLMo-2-1124-7B` | 7B | 2024-11 | Apache 2.0 | No | 4T tokens | 63.7 |
| **OLMo 2 13B** | `allenai/OLMo-2-1124-13B` | 13B | 2024-11 | Apache 2.0 | No | 5T tokens | 67.5 |
| **Falcon3-10B-Base** | `tiiuae/Falcon3-10B-Base` | 10B | 2024-12 | Falcon 2.0 | No | 14T+2T | 73.1 |
| **Falcon3-7B-Base** | `tiiuae/Falcon3-7B-Base` | 7B | 2024-12 | Falcon 2.0 | No | 14T tokens | 67.4 |
| **Falcon-H1-7B-Base** | `tiiuae/Falcon-H1-7B-Base` | 7B | 2025 | Open | No | 未公开 | — |
| Qwen2.5-7B | `Qwen/Qwen2.5-7B` | 7B | 2024-09 | Apache 2.0 | No | 18T tokens | 74.2 |
| Qwen2.5-14B | `Qwen/Qwen2.5-14B` | 14B | 2024-09 | Apache 2.0 | No | 18T tokens | 79.7 |
| Mistral-Nemo-12B | `mistralai/Mistral-Nemo-Base-2407` | 12B | 2024-07 | Apache 2.0 | No | 未公开 | 68.0 |
| Llama 3.1 8B | `meta-llama/Llama-3.1-8B` | 8B | 2024-07 | Llama CLA | **Yes** | 15T tokens | 65.6 |
| Yi-1.5-9B | `01-ai/Yi-1.5-9B` | 9B | 2024-05 | Apache 2.0 | No | ~3T tokens | 76.3 |

### 排除的模型
- **Llama 4**: 全部 MoE（Scout 17B active/109B total），无 dense 7B-14B base
- **DeepSeek R2**: 未发布
- **DeepSeek V3/V4**: 671B+ MoE，远超范围
- **DeepSeek-R1-Distill-***: 是 SFT 微调模型，不是 base pretrained model，不适合做 controlled contamination injection
- **Gemma 4**: MoE 架构，无 dense 7B-14B
- **InternLM3-8B**: base checkpoint 未公开发布（仅 instruct）

---

## 推荐

### 1. 最佳 5 模型组合（全部 2024Q4-2025，全部 non-gated）

| Family | 模型 | 理由 |
|---|---|---|
| **Qwen** (Alibaba) | Qwen3-8B-Base | 2025-04，36T tokens，Apache 2.0，MMLU 79.7，直接替代 Qwen 2.5 |
| **Phi** (Microsoft) | Phi-4 | 2024-12，MIT，MMLU 84.8，14.7B 强基线 |
| **Mistral** (Mistral AI) | Ministral-3-8B-Base | 2025-12，Apache 2.0，替代 Mistral v0.3 |
| **OLMo** (Allen AI) | OLMo-2-1124-7B | 完全开源（数据+代码+权重），Apache 2.0，学术可复现性最强 |
| **Falcon** (TII) | Falcon3-10B-Base | 2024-12，14T tokens，MMLU 73.1 |

**优势**：5 个不同机构/家族，全部 non-gated，全部 2024Q4+，覆盖不同训练规模（4T-36T tokens）和能力水平（MMLU 63.7-84.8），审稿人无法质疑模型过时。

**备选**：如果想用 Google 家族替换 Falcon，可选 Gemma 3 12B PT（但 gated）。

### 2. Llama-3.1-8B 的替代

Llama 4 无 dense 7B-14B，所以 Meta 家族无直接替代。最佳替代方案按优先级：

1. **Phi-4** (14.7B) — 不同家族，MIT 开放，性能最强
2. **OLMo-2-7B** — 参数量最接近（7B），完全开源，学术论文天然认可
3. **Falcon3-10B-Base** — 不同家族，non-gated

### 3. Qwen 3 状况

**Qwen3 已发布（2025-04-29）**，有完整的 base 系列。Qwen3-8B-Base 在 36T tokens 上训练，MMLU 79.7（vs Qwen2.5-7B 的 74.2），性能已达 Qwen2.5-14B 水平。**强烈建议用 Qwen3-8B-Base 替换 Qwen 2.5**。技术报告：arXiv 2505.09388。

---

### 实际操作注意

- Phi-4 是 14.7B，bf16 下约 29.4GB，96GB GPU 做 LoRA SFT 无压力
- Ministral-3-8B-Base 是 2025-12 发布，如果论文投稿时间早于此，改用 Mistral-Nemo-Base-2407 (12B, 2024-07)
- OLMo 2 的 MMLU 偏低（63.7），但其完全开源属性在 contamination 研究中是加分项（审稿人重视可复现性）
- Falcon-H1-7B 是 hybrid SSM+Attention 架构，可能引入架构差异混淆因素，建议用 Falcon3 而非 H1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 303217,
  "duration_api_ms": 1162777,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "b4bb6832-311d-424b-8b19-57bd3d213f37",
  "total_cost_usd": 5.022087500000001,
  "usage": {
    "input_tokens": 10834,
    "cache_creation_input_tokens": 24745,
    "cache_read_input_tokens": 64456,
    "output_tokens": 4808,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 24745,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 10828,
        "output_tokens": 3457,
        "cache_read_input_tokens": 26657,
        "cache_creation_input_tokens": 9929,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 9929
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1639379,
      "outputTokens": 41470,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 89,
      "costUSD": 2.7367290000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 23589,
      "outputTokens": 29967,
      "cacheReadInputTokens": 812127,
      "cacheCreationInputTokens": 161948,
      "webSearchRequests": 0,
      "costUSD": 2.2853585,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f1a41075-2952-4713-aa69-152fc1fd1847"
}
```

</details>

---
