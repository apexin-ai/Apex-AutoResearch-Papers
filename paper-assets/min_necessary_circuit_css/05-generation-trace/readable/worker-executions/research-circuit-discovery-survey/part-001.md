# research circuit discovery survey — Part 1 of 2

**Transformer Model EAP-IG** · Worker execution logs

[Transcript overview](../research-circuit-discovery-survey.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/a3/a392b4a33b8633107758.json)

## Before a recorded user message

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
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
  "uuid": "83f1a659-9069-4086-b516-80e31acdc6b3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-structfuse-context/memory/"
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
    "resetsAt": 1778637000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0260a28b-ff59-453d-b9c1-f6155acb5c0d",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a literature survey on Circuit Discovery (2024-2026) focusing on novelty verification for their project structfuse-context. The key questions are about whether anyone has compared consistency across circuit discovery methods or aggregated multiple methods' results.

Let me launch multiple search agents in parallel to cover the different questions efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "6e11afc5-bfd3-4359-845e-9165e7d0a3ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNF9Kdgwyn4nhyrpTZEaAt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11925,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11925
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

_source line 5_

开始文献调研，分四个方向并行搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "fc7c2246-e37c-4a59-b35b-9a81c52b630b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNF9Kdgwyn4nhyrpTZEaAt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11925,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11925
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013AuTaAqpYhP5UsT6MCSAAx`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
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
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b88b6742-25ca-4094-b44d-d702995edbdf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNF9Kdgwyn4nhyrpTZEaAt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11925,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11925
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

_source line 7 · 2026-05-12T22:07:37.070Z_

<details><summary>↩ Tool result · `toolu_013AuTaAqpYhP5UsT6MCSAAx`</summary>

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
  "tool_name": "WebFetch"
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
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "60b35c21-e7fa-4d49-8748-0f6bf81bd6be",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
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
Now let me launch parallel search agents for the four questions. I'll use multiple agents to search in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2a9e9fa9-3d8d-45bc-af1b-072a420209d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o6KmdZm6WtJbmosiU4UfQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 23766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1204
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

_source line 9_

<details open><summary>🔧 Tool call — Agent · `toolu_01LDQfvBwWGQLX9DkoSBc9AR`</summary>

```json
{
  "description": "Q1: Circuit method consistency comparison",
  "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability. \n\n**Task**: Find papers that systematically compare different circuit discovery methods (e.g., EAP, ACDC, Edge Pruning, subnetwork probing, activation patching) and evaluate the consistency/agreement of the circuits they find.\n\nSearch using these keyword combinations (at least 3 different searches):\n1. \"circuit discovery comparison mechanistic interpretability\"\n2. \"circuit agreement consistency different methods transformers\"\n3. \"comparing automated circuit discovery ACDC EAP edge pruning\"\n4. \"circuit discovery benchmark evaluation\"\n5. \"mechanistic interpretability methods comparison 2024 2025\"\n\nFor each search, use WebSearch. For any highly relevant paper found, use WebFetch on its arXiv abstract page to confirm the content.\n\n**Output format**: For each relevant paper found, report:\n- Title\n- Authors (first author + et al.)\n- Year / Venue\n- URL\n- What methods they compare\n- Key findings about consistency/disagreement\n- How it relates to \"cross-method binary consensus\" or aggregation\n\nIf no paper directly compares method consistency, say so explicitly. Be thorough - this is the most important question for novelty assessment.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "588fb5df-a246-4538-8108-9e1ef3279fd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o6KmdZm6WtJbmosiU4UfQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 23766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1204
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


### System

_source line 10_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Q1: Circuit method consistency comparison",
  "task_type": "local_agent",
  "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability. \n\n**Task**: Find papers that systematically compare different circuit discovery methods (e.g., EAP, ACDC, Edge Pruning, subnetwork probing, activation patching) and evaluate the consistency/agreement of the circuits they find.\n\nSearch using these keyword combinations (at least 3 different searches):\n1. \"circuit discovery comparison mechanistic interpretability\"\n2. \"circuit agreement consistency different methods transformers\"\n3. \"comparing automated circuit discovery ACDC EAP edge pruning\"\n4. \"circuit discovery benchmark evaluation\"\n5. \"mechanistic interpretability methods comparison 2024 2025\"\n\nFor each search, use WebSearch. For any highly relevant paper found, use WebFetch on its arXiv abstract page to confirm the content.\n\n**Output format**: For each relevant paper found, report:\n- Title\n- Authors (first author + et al.)\n- Year / Venue\n- URL\n- What methods they compare\n- Key findings about consistency/disagreement\n- How it relates to \"cross-method binary consensus\" or aggregation\n\nIf no paper directly compares method consistency, say so explicitly. Be thorough - this is the most important question for novelty assessment.",
  "uuid": "d1b55584-33f6-4e88-8129-de15d0ec6bd5",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


## Round 1

## Round 1

6 recorded events


### User

_source line 11 · 2026-05-12T22:07:47.268Z_

You are conducting a literature survey on circuit discovery in mechanistic interpretability. 

**Task**: Find papers that systematically compare different circuit discovery methods (e.g., EAP, ACDC, Edge Pruning, subnetwork probing, activation patching) and evaluate the consistency/agreement of the circuits they find.

Search using these keyword combinations (at least 3 different searches):
1. "circuit discovery comparison mechanistic interpretability"
2. "circuit agreement consistency different methods transformers"
3. "comparing automated circuit discovery ACDC EAP edge pruning"
4. "circuit discovery benchmark evaluation"
5. "mechanistic interpretability methods comparison 2024 2025"

For each search, use WebSearch. For any highly relevant paper found, use WebFetch on its arXiv abstract page to confirm the content.

**Output format**: For each relevant paper found, report:
- Title
- Authors (first author + et al.)
- Year / Venue
- URL
- What methods they compare
- Key findings about consistency/disagreement
- How it relates to "cross-method binary consensus" or aggregation

If no paper directly compares method consistency, say so explicitly. Be thorough - this is the most important question for novelty assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "cb53cad7-8a05-4d2b-bce6-e5f066c94abf"
}
```

</details>

---


### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Q1: Circuit method consistency comparison",
  "usage": {
    "total_tokens": 14352,
    "tool_uses": 1,
    "duration_ms": 3459
  },
  "last_tool_name": "ToolSearch",
  "uuid": "8c9bed02-62a0-4c39-baf4-e6b16ab39e75",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 13_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HypJL5fzLU3pX6fiSijb3H`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "f318ff49-180d-46bc-b6f5-90f1377d6fae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeU65xgtrU8v92xusaHsus",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14333,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14333,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 14 · 2026-05-12T22:07:50.735Z_

<details><summary>↩ Tool result · `toolu_01HypJL5fzLU3pX6fiSijb3H`</summary>

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
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "4618d340-8e92-4825-b1e4-ddf5d6330c34"
}
```

</details>

---


### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Agent · `toolu_01JX4st1y5kYpBpUAVKFTMdz`</summary>

```json
{
  "description": "Q2: Circuit aggregation/ensemble methods",
  "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability.\n\n**Task**: Find papers that propose aggregating or ensembling results from multiple circuit discovery methods to get more robust circuits. This is the most critical novelty threat - if someone has done \"multi-method circuit aggregation\" or \"consensus circuit discovery\", we need to know.\n\nSearch using these keyword combinations (at least 3 different searches):\n1. \"circuit aggregation ensemble mechanistic interpretability\"\n2. \"robust circuit discovery multi-method consensus\"\n3. \"combining circuit discovery methods transformers\"\n4. \"cross-method circuit stability scoring\"\n5. \"circuit discovery robustness ensemble neural network\"\n\nFor each search, use WebSearch. For any highly relevant paper found, use WebFetch on its arXiv abstract page to confirm the content.\n\n**Output format**: For each relevant paper found, report:\n- Title\n- Authors\n- Year / Venue\n- URL\n- What aggregation/ensemble approach they use\n- How similar it is to \"Cross-method Stability Scoring\" (CSS) - binary consensus across methods\n\nIf nothing found, explicitly state \"No papers found proposing multi-method circuit aggregation.\" Be very thorough.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "bd4dbeda-fc01-4b07-b7d3-f1066a412592",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o6KmdZm6WtJbmosiU4UfQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 23766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1204
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


### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Q2: Circuit aggregation/ensemble methods",
  "task_type": "local_agent",
  "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability.\n\n**Task**: Find papers that propose aggregating or ensembling results from multiple circuit discovery methods to get more robust circuits. This is the most critical novelty threat - if someone has done \"multi-method circuit aggregation\" or \"consensus circuit discovery\", we need to know.\n\nSearch using these keyword combinations (at least 3 different searches):\n1. \"circuit aggregation ensemble mechanistic interpretability\"\n2. \"robust circuit discovery multi-method consensus\"\n3. \"combining circuit discovery methods transformers\"\n4. \"cross-method circuit stability scoring\"\n5. \"circuit discovery robustness ensemble neural network\"\n\nFor each search, use WebSearch. For any highly relevant paper found, use WebFetch on its arXiv abstract page to confirm the content.\n\n**Output format**: For each relevant paper found, report:\n- Title\n- Authors\n- Year / Venue\n- URL\n- What aggregation/ensemble approach they use\n- How similar it is to \"Cross-method Stability Scoring\" (CSS) - binary consensus across methods\n\nIf nothing found, explicitly state \"No papers found proposing multi-method circuit aggregation.\" Be very thorough.",
  "uuid": "01ff3234-4bb9-4e67-af3d-38ef85d14876",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


## Round 2

## Round 2

16 recorded events


### User

_source line 17 · 2026-05-12T22:07:52.141Z_

You are conducting a literature survey on circuit discovery in mechanistic interpretability.

**Task**: Find papers that propose aggregating or ensembling results from multiple circuit discovery methods to get more robust circuits. This is the most critical novelty threat - if someone has done "multi-method circuit aggregation" or "consensus circuit discovery", we need to know.

Search using these keyword combinations (at least 3 different searches):
1. "circuit aggregation ensemble mechanistic interpretability"
2. "robust circuit discovery multi-method consensus"
3. "combining circuit discovery methods transformers"
4. "cross-method circuit stability scoring"
5. "circuit discovery robustness ensemble neural network"

For each search, use WebSearch. For any highly relevant paper found, use WebFetch on its arXiv abstract page to confirm the content.

**Output format**: For each relevant paper found, report:
- Title
- Authors
- Year / Venue
- URL
- What aggregation/ensemble approach they use
- How similar it is to "Cross-method Stability Scoring" (CSS) - binary consensus across methods

If nothing found, explicitly state "No papers found proposing multi-method circuit aggregation." Be very thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8714e45b-054c-4832-86d9-377e71c197c9"
}
```

</details>

---


### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for circuit discovery comparison mechanistic interpre…",
  "usage": {
    "total_tokens": 16316,
    "tool_uses": 2,
    "duration_ms": 6740
  },
  "last_tool_name": "WebSearch",
  "uuid": "5bdbac6b-1f87-4cc0-9190-b94765a3ff5d",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for circuit agreement consistency different methods t…",
  "usage": {
    "total_tokens": 16318,
    "tool_uses": 3,
    "duration_ms": 7243
  },
  "last_tool_name": "WebSearch",
  "uuid": "eef6b578-4ef0-4091-8681-79c5a6754999",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for comparing automated circuit discovery ACDC EAP ed…",
  "usage": {
    "total_tokens": 16320,
    "tool_uses": 4,
    "duration_ms": 7645
  },
  "last_tool_name": "WebSearch",
  "uuid": "3f0c2be7-fd92-4810-b1f7-bea3791fa12f",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for circuit discovery benchmark evaluation mechanisti…",
  "usage": {
    "total_tokens": 16322,
    "tool_uses": 5,
    "duration_ms": 7666
  },
  "last_tool_name": "WebSearch",
  "uuid": "2b87f0b4-a24b-418f-93f5-87c16450c94b",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Q2: Circuit aggregation/ensemble methods",
  "usage": {
    "total_tokens": 14335,
    "tool_uses": 1,
    "duration_ms": 3139
  },
  "last_tool_name": "ToolSearch",
  "uuid": "287d40dc-0bfe-45c3-9c5b-3ed081b42ea0",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for mechanistic interpretability methods comparison 2…",
  "usage": {
    "total_tokens": 16324,
    "tool_uses": 6,
    "duration_ms": 9051
  },
  "last_tool_name": "WebSearch",
  "uuid": "75a366c2-76dd-494a-8134-13d57c487c1a",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RRMPATYvYpUJVusRmZYAjW`</summary>

```json
{
  "query": "circuit discovery comparison mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2014b0dc-a1b6-4bc2-aa52-d3b1cdd8bd51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zYyKgrTNwKAZCet5KvWkz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1960,
      "cache_read_input_tokens": 14333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1960,
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AtzDU7uwJFZCgGRYGTGkVs`</summary>

```json
{
  "query": "circuit agreement consistency different methods transformers mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e836a322-10fd-46e3-a940-287f840d8c6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zYyKgrTNwKAZCet5KvWkz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1960,
      "cache_read_input_tokens": 14333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1960,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CKc5g2WqUb7U4NvvHtLeTv`</summary>

```json
{
  "query": "comparing automated circuit discovery ACDC EAP edge pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "d7d4e3c5-aa10-44ae-97e2-bc4e4304a78e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zYyKgrTNwKAZCet5KvWkz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1960,
      "cache_read_input_tokens": 14333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1960,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GygjfYjCcPU31WzaaHmLVe`</summary>

```json
{
  "query": "circuit discovery benchmark evaluation mechanistic interpretability 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "da346f7c-2b63-497d-9be2-61eb6c17e3bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zYyKgrTNwKAZCet5KvWkz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1960,
      "cache_read_input_tokens": 14333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1960,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lktu12GKZLhRQK7vYmiiV2`</summary>

```json
{
  "query": "mechanistic interpretability methods comparison 2024 2025 circuit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "9123c387-5d84-4c27-8520-2bc1b32d3be0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zYyKgrTNwKAZCet5KvWkz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1960,
      "cache_read_input_tokens": 14333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1960,
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

_source line 29_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MunNYpCjnEwBmytRNnAhxQ`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "9440da93-98ed-483f-bc1f-7825055d6aaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gLxmFPQZPfFY7RhyHBhfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6071,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6071,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 30 · 2026-05-12T22:07:55.284Z_

<details><summary>↩ Tool result · `toolu_01MunNYpCjnEwBmytRNnAhxQ`</summary>

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
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "48ee51c0-6e50-4a35-ba29-478011bba64b"
}
```

</details>

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Agent · `toolu_01L3fLhWV9gRjmmjD2tKgqGa`</summary>

```json
{
  "description": "Q3: New circuit discovery methods 2024-2026",
  "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability.\n\n**Task**: Find important new circuit discovery methods published in 2024-2026, beyond the well-known ones (EAP-IG, ACDC, Edge Pruning, IFR, activation patching).\n\nSearch using these keywords:\n1. \"circuit discovery 2024 2025 mechanistic interpretability\"\n2. \"automated circuit discovery new method transformer 2024\"\n3. \"mechanistic interpretability circuit finding 2025 2026\"\n4. \"subnetwork discovery interpretability 2024\"\n\nFor each search, use WebSearch. For promising papers, use WebFetch to read the abstract.\n\n**Output format**: A table with columns:\n- Method name\n- Paper title\n- Authors (first + et al.)\n- Year\n- Venue (if known)\n- Algorithm family (gradient-based, pruning-based, attribution-based, etc.)\n- Brief description\n- URL\n\nFocus on genuinely new methods, not just applications of existing methods to new models/tasks.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "6c810407-5965-4670-a536-a852a80f2a68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o6KmdZm6WtJbmosiU4UfQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 23766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1204
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


### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Q3: New circuit discovery methods 2024-2026",
  "task_type": "local_agent",
  "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability.\n\n**Task**: Find important new circuit discovery methods published in 2024-2026, beyond the well-known ones (EAP-IG, ACDC, Edge Pruning, IFR, activation patching).\n\nSearch using these keywords:\n1. \"circuit discovery 2024 2025 mechanistic interpretability\"\n2. \"automated circuit discovery new method transformer 2024\"\n3. \"mechanistic interpretability circuit finding 2025 2026\"\n4. \"subnetwork discovery interpretability 2024\"\n\nFor each search, use WebSearch. For promising papers, use WebFetch to read the abstract.\n\n**Output format**: A table with columns:\n- Method name\n- Paper title\n- Authors (first + et al.)\n- Year\n- Venue (if known)\n- Algorithm family (gradient-based, pruning-based, attribution-based, etc.)\n- Brief description\n- URL\n\nFocus on genuinely new methods, not just applications of existing methods to new models/tasks.",
  "uuid": "1a075a0b-46f1-4e9f-aed8-a35f11b754bb",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


## Round 3

## Round 3

8 recorded events


### User

_source line 33 · 2026-05-12T22:07:56.888Z_

You are conducting a literature survey on circuit discovery in mechanistic interpretability.

**Task**: Find important new circuit discovery methods published in 2024-2026, beyond the well-known ones (EAP-IG, ACDC, Edge Pruning, IFR, activation patching).

Search using these keywords:
1. "circuit discovery 2024 2025 mechanistic interpretability"
2. "automated circuit discovery new method transformer 2024"
3. "mechanistic interpretability circuit finding 2025 2026"
4. "subnetwork discovery interpretability 2024"

For each search, use WebSearch. For promising papers, use WebFetch to read the abstract.

**Output format**: A table with columns:
- Method name
- Paper title
- Authors (first + et al.)
- Year
- Venue (if known)
- Algorithm family (gradient-based, pruning-based, attribution-based, etc.)
- Brief description
- URL

Focus on genuinely new methods, not just applications of existing methods to new models/tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "d59633c3-cfaa-438b-bd6e-e63caf232296"
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
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for circuit aggregation ensemble mechanistic interpre…",
  "usage": {
    "total_tokens": 16306,
    "tool_uses": 2,
    "duration_ms": 6698
  },
  "last_tool_name": "WebSearch",
  "uuid": "20ca5660-36d7-4897-b2d6-8a018ac29ad5",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Q3: New circuit discovery methods 2024-2026",
  "usage": {
    "total_tokens": 14305,
    "tool_uses": 1,
    "duration_ms": 3561
  },
  "last_tool_name": "ToolSearch",
  "uuid": "c703759f-5a1b-45fc-81d4-eb6a27eb33ef",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FRNrVKeBSAKU6hKQQv9u2v`</summary>

```json
{
  "query": "circuit aggregation ensemble mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "5202409b-8123-47db-9a5c-54e69aba899e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqX4tpLB9PdZH4VfvVqnZ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 14320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1967,
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

_source line 37_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017HRkK1f2rdejqhcybMcWa2`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "724e34ee-8696-4514-9e53-6b5463d511ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFGVnhmTNE7p1SYtMcridV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6045,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6045,
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

_source line 38 · 2026-05-12T22:08:00.451Z_

<details><summary>↩ Tool result · `toolu_017HRkK1f2rdejqhcybMcWa2`</summary>

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
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "62bdbc12-35b9-4a20-9a84-c0d19a4c65b8"
}
```

</details>

---


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Agent · `toolu_011k1dq6zk5AsEF3sipmxFHp`</summary>

```json
{
  "description": "Q4: Top venue circuit papers 2024-2025",
  "prompt": "You are conducting a literature survey on circuit discovery and mechanistic interpretability at top ML venues.\n\n**Task**: Find circuit discovery / mechanistic interpretability papers published at these venues:\n- ICLR 2024, ICLR 2025\n- NeurIPS 2024\n- ICML 2024, ICML 2025\n\nSearch using these queries:\n1. \"circuit discovery ICLR 2024 2025\"\n2. \"mechanistic interpretability NeurIPS 2024\"\n3. \"circuit discovery ICML 2024 2025\"\n4. \"automated interpretability circuits top conference 2024 2025\"\n5. \"mechanistic interpretability ICLR 2025 accepted papers\"\n\nFor each search, use WebSearch. Use WebFetch to confirm venue/year for important papers.\n\n**Output format**: A table with columns:\n- Paper title\n- Conference + Year\n- Main contribution (1-2 sentences)\n- URL\n\nOnly include papers genuinely about circuit discovery or closely related mechanistic interpretability (not general XAI or probing studies).",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b823c913-9973-42fd-9154-877e64bdb5b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o6KmdZm6WtJbmosiU4UfQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 23766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1204
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


### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Q4: Top venue circuit papers 2024-2025",
  "task_type": "local_agent",
  "prompt": "You are conducting a literature survey on circuit discovery and mechanistic interpretability at top ML venues.\n\n**Task**: Find circuit discovery / mechanistic interpretability papers published at these venues:\n- ICLR 2024, ICLR 2025\n- NeurIPS 2024\n- ICML 2024, ICML 2025\n\nSearch using these queries:\n1. \"circuit discovery ICLR 2024 2025\"\n2. \"mechanistic interpretability NeurIPS 2024\"\n3. \"circuit discovery ICML 2024 2025\"\n4. \"automated interpretability circuits top conference 2024 2025\"\n5. \"mechanistic interpretability ICLR 2025 accepted papers\"\n\nFor each search, use WebSearch. Use WebFetch to confirm venue/year for important papers.\n\n**Output format**: A table with columns:\n- Paper title\n- Conference + Year\n- Main contribution (1-2 sentences)\n- URL\n\nOnly include papers genuinely about circuit discovery or closely related mechanistic interpretability (not general XAI or probing studies).",
  "uuid": "1ef6cae0-21c3-4f14-8aa6-943d4995147b",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


## Round 4

## Round 4

427 recorded events


### User

_source line 41 · 2026-05-12T22:08:01.170Z_

You are conducting a literature survey on circuit discovery and mechanistic interpretability at top ML venues.

**Task**: Find circuit discovery / mechanistic interpretability papers published at these venues:
- ICLR 2024, ICLR 2025
- NeurIPS 2024
- ICML 2024, ICML 2025

Search using these queries:
1. "circuit discovery ICLR 2024 2025"
2. "mechanistic interpretability NeurIPS 2024"
3. "circuit discovery ICML 2024 2025"
4. "automated interpretability circuits top conference 2024 2025"
5. "mechanistic interpretability ICLR 2025 accepted papers"

For each search, use WebSearch. Use WebFetch to confirm venue/year for important papers.

**Output format**: A table with columns:
- Paper title
- Conference + Year
- Main contribution (1-2 sentences)
- URL

Only include papers genuinely about circuit discovery or closely related mechanistic interpretability (not general XAI or probing studies).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "a15810b6-24c4-47a4-9453-fe75f85aa0b0"
}
```

</details>

---


### Tool result

_source line 42 · 2026-05-12T22:08:01.311Z_

<details><summary>↩ Tool result · `toolu_01GygjfYjCcPU31WzaaHmLVe`</summary>

```text
Web search results for query: "circuit discovery benchmark evaluation mechanistic interpretability 2024 2025"

Links: [{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"Corti introduces GIM: Benchmark-leading method for understanding AI model behavior | Corti","url":"https://www.corti.ai/stories/gim-a-new-standard-for-mechanistic-interpretability"},{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=FbZSZEIkEU"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823"},{"title":"Mechanistic Interpretability Explained: Circuits, Sparse Autoencoders, Causal Tracing, and AI Safety | by Adnan Masood, PhD. | Apr, 2026 | Medium","url":"https://medium.com/@adnanmasood/mechanistic-interpretability-explained-circuits-sparse-autoencoders-causal-tracing-and-ai-88ecc8d70b72"},{"title":"(PDF) Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://www.researchgate.net/publication/400970365_Formal_Mechanistic_Interpretability_Automated_Circuit_Discovery_with_Provable_Guarantees"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Shared Task - BlackboxNLP 2025 - GitHub Pages","url":"https://blackboxnlp.github.io/2025/task/"},{"title":"MIB: A Mechanistic Interpretability Benchmark | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.13151v2"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"}]

Based on the web search results, here's what I found about circuit discovery benchmark evaluation in mechanistic interpretability for 2024-2025:

## Key Benchmarks and Evaluations

The Mechanistic Interpretability Benchmark (MIB) establishes two evaluation tracks—circuit localization and causal variable localization—across diverse tasks (IOI, arithmetic, MCQA, ARC) and models (GPT-2-Small, Qwen-2.5, Gemma-2, Llama-3.1).

The circuit localization track benchmarks methods that aim to locate graphs of causal dependencies in neural networks, while the causal variable localization track benchmarks methods that aim to locate specific human-interpretable causal variables in neural networks.

## Evaluation Metrics

Circuit localization metrics include faithfulness integral (CPR), minimality, and AUROC where ground-truth is available. Causal variable localization leverages IIA, DBM, PCA, SAE, and DAS featurizers; supervised DAS significantly outperforms unsupervised SAE features.

## Recent Advances

GIM (Gradient Interaction Modifications) has reached the top of the Hugging Face Mechanistic Interpretability Benchmark, which is the industry standard maintained by researchers from MIT, Stanford, Cambridge, Boston, and ETH Zurich.

Manual intervention mapping does not scale; there is a need for higher-throughput automated circuit discovery, hypothesis generation, and robust evaluation standards.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "16748415-dd35-4efb-bacd-a3b7d989dbfe"
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-12T22:08:01.599Z_

<details><summary>↩ Tool result · `toolu_01AtzDU7uwJFZCgGRYGTGkVs`</summary>

```text
Web search results for query: "circuit agreement consistency different methods transformers mechanistic interpretability"

Links: [{"title":"A Mathematical Framework for Transformer Circuits","url":"https://transformer-circuits.pub/2021/framework/index.html"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"A Practical Review of Mechanistic Interpretability for Transformer-Based Language Models","url":"https://arxiv.org/html/2407.02646v1"},{"title":"Mechanistic Interpretability in Action: Understanding Induction Heads and QK Circuits in Transformers | by Ayyüce Kızrak, Ph.D. | Medium","url":"https://ayyucekizrak.medium.com/mechanistic-interpretability-in-action-understanding-induction-heads-and-qk-circuits-in-c2a3549b6ff2"},{"title":"Transformer Circuits Thread","url":"https://transformer-circuits.pub/"},{"title":"Mechanistic Interpretability Part 1: Introduction and Transformer circuits","url":"https://www.uio.no/studier/emner/matnat/ifi/IN5550/v25/slides/slides12_1.pdf"},{"title":"Seeing Through Circuits: Faithful Mechanistic Interpretability for Vision Transformers","url":"https://arxiv.org/html/2604.14477"},{"title":"Mechanistic Analysis Of Universality: Numerical Comparison Circuits Across Transformer Architectures | OpenReview","url":"https://openreview.net/forum?id=79igg0kRtd"},{"title":"GitHub - ayyucekizrak/Mechanistic-Interpretability: Mechanistic Interpretability in Transformers: This repository explores advanced techniques like Induction Head Detection and QK Circuit Analysis to uncover the inner workings of transformer-based models. · GitHub","url":"https://github.com/ayyucekizrak/Mechanistic-Interpretability"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"}]

Based on the search results, I found relevant information about circuit agreement and consistency in mechanistic interpretability for transformers. Here are the key findings:

## Circuit Agreement and Consistency Across Methods

Mechanistic interpretability seeks to identify task circuits within individual models, but it is unclear whether such circuits generalize across model families and scales. This question of circuit consistency has been directly investigated in recent research.

### Research on Circuit Universality

One study examines circuit universality through the lens of numerical comparisons using a set of transformer models spanning different families and sizes from 1.7b to 9b parameters. The findings reveal mixed results regarding consistency:

Models within the Qwen family exhibit a highly consistent circuit structure across architecture and scale, featuring localized attention heads that write a task relevant signal. In contrast, models from other families show qualitatively different implementations, where task relevant information emerges much earlier and is distributed across components.

### Validation of Circuit Discovery Methods

Across prompts, perturbation experiments are generally qualitatively consistent with attribution graphs, though there are some deviations. This suggests that different circuit discovery methods show reasonable agreement, though not perfect consistency.

The research indicates that while some circuit structures may be universal within specific model families, circuits discovered across different transformer families and scales can show significant variations in their implementation strategy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "301e836c-7ae9-4d3e-b74b-fbaf37016497"
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-12T22:08:01.672Z_

<details><summary>↩ Tool result · `toolu_01RRMPATYvYpUJVusRmZYAjW`</summary>

```text
Web search results for query: "circuit discovery comparison mechanistic interpretability"

Links: [{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | FAR.AI","url":"https://www.far.ai/research/towards-automated-circuit-discovery-for-mechanistic-interpretability"},{"title":"(PDF) Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://www.researchgate.net/publication/370417693_Towards_Automated_Circuit_Discovery_for_Mechanistic_Interpretability"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"Evaluating Brain-Inspired Modular Training in Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/html/2401.03646v1"},{"title":"(PDF) Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://www.researchgate.net/publication/400970365_Formal_Mechanistic_Interpretability_Automated_Circuit_Discovery_with_Provable_Guarantees"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823"}]

Based on the search results, here's an overview of circuit discovery and its comparison in mechanistic interpretability:

## What is Circuit Discovery?

Automated circuit discovery is a central tool in mechanistic interpretability for identifying the internal components of neural networks responsible for specific behaviors. Circuit discovery seeks to identify subgraphs within neural networks, called circuits, that drive specific model behaviors.

## The Mechanistic Interpretability Process

The mechanistic interpretability process involves researchers choosing a metric and dataset that elicit the desired model behavior, then applying activation patching to find which abstract neural network units are involved in the behavior. By varying the dataset, metric, and units under investigation, researchers can understand the functionality of each component.

## Automated Approaches and Comparisons

The ACDC algorithm rediscovered 5/5 of the component types in a circuit in GPT-2 Small that computes the Greater-Than operation. This demonstrates the effectiveness of automated approaches.

Recent work has advanced beyond heuristic-based methods. Newer approaches leverage neural network verification to propose algorithms that yield circuits with provable guarantees, focusing on input domain robustness, robust patching, and minimality. These algorithms yield circuits with substantially stronger robustness guarantees than standard circuit discovery methods.

## Comparative Metrics

Key metrics for evaluating circuits include whether the subgraph achieves relative performance on the task (indicating it implements the underlying algorithm), and the number of edges in the circuit, with sparser circuits that achieve good performance being preferred because smaller graphs are easier to interpret.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e1e18dc7-2f31-4093-bbdb-7c05cbc116dd"
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-12T22:08:03.399Z_

<details><summary>↩ Tool result · `toolu_01CKc5g2WqUb7U4NvvHtLeTv`</summary>

```text
Web search results for query: "comparing automated circuit discovery ACDC EAP edge pruning"

Links: [{"title":"Attribution Patching Outperforms Automated Circuit Discovery Aaquib Syed","url":"https://openreview.net/pdf?id=tiLbFR4bJW"},{"title":"Multi-Granular Node Pruning for Circuit Discovery","url":"https://arxiv.org/html/2512.10903"},{"title":"Published as a conference paper at ICLR 2025 EFFICIENT AUTOMATED CIRCUIT","url":"https://arxiv.org/pdf/2407.00886"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://www.arxiv.org/pdf/2510.03282"},{"title":"Automatic Circuit Discovery","url":"https://sidn.baulab.info/autocircuits/"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/html/2510.23264"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://aclanthology.org/2024.blackboxnlp-1.25.pdf"},{"title":"Finding Transformer Circuits with Edge Pruning Adithya Bhaskar Alexander Wettig","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/20fdaf67581e6d7157376d1ed584040a-Paper-Conference.pdf"},{"title":"EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification","url":"https://arxiv.org/html/2502.06852v1"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://www.researchgate.net/publication/386190657_Attribution_Patching_Outperforms_Automated_Circuit_Discovery"}]

Based on the search results, here's a comprehensive comparison of automated circuit discovery methods focusing on ACDC, EAP, and edge pruning:

## Key Methods

Automated Circuit Discovery (ACDC) formulates circuit finding as iteratively removing edges between components while maintaining task performance, while Edge Attribution Patching (EAP) is a technique to estimate the impact of activation patching using only two forward passes and one backward pass, linearly approximating the metric after corrupting a single edge in the computational graph using the first-order Taylor series.

## Efficiency vs. Faithfulness Trade-offs

The main trade-off between these methods is computational efficiency versus accuracy:

- **ACDC**: EAP is competitive with ACDC on recovering circuits while significantly reducing the computational demand: EAP only takes a constant number of forward and backwards passes while the number of forward passes required by ACDC is scaling exponentially with the number of nodes. However, ACDC is the least efficient as it often takes hours to identify a circuit.

- **EAP**: EAP achieves linear efficiency via gradient-based edge estimation, but this comes at the cost of approximation errors in multi-layer nonlinear computations.

- **Edge Pruning (EP)**: Edge Pruning scales effectively to 100K examples, where it is the fastest and most faithful method, and it is considerably more faithful on IOI and GT than both ACDC and EAP, especially at higher sparsities.

## Performance Comparisons

Across the three evaluated tasks (IOI, GP, and GT), the multi-granularity approach consistently achieves competitive edge sparsity levels while substantially reducing the number of retained attention heads compared to both EAP and EP. For GT, this method delivers the best overall results, achieving both the lowest KL divergence and the highest probability, while requiring far fewer attention heads than either EAP or EP.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "ee958095-fe51-46f0-a9c1-9bb99d913f90"
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
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for circuit discovery 2024 2025 mechanistic interpret…",
  "usage": {
    "total_tokens": 16265,
    "tool_uses": 2,
    "duration_ms": 6817
  },
  "last_tool_name": "WebSearch",
  "uuid": "bfad3204-ccac-44e8-8a9a-dfc45a232c34",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 47_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DUf9WzXgFqwZAhLadyAbto`</summary>

```json
{
  "query": "circuit discovery 2024 2025 mechanistic interpretability new method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8e888ec9-db55-4589-9c48-d3c63a38eb0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYuTUzCaKw4ujsjV6EQ6UV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for automated circuit discovery new method transforme…",
  "usage": {
    "total_tokens": 16267,
    "tool_uses": 3,
    "duration_ms": 7256
  },
  "last_tool_name": "WebSearch",
  "uuid": "fcc8b8c1-202b-412c-84c2-dcc0f7acf63c",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011rTMSMCX614sr1mzJi5W2a`</summary>

```json
{
  "query": "automated circuit discovery new method transformer 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2822ddea-7631-4950-94f3-a9ab543429ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYuTUzCaKw4ujsjV6EQ6UV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Q4: Top venue circuit papers 2024-2025",
  "usage": {
    "total_tokens": 14315,
    "tool_uses": 1,
    "duration_ms": 3207
  },
  "last_tool_name": "ToolSearch",
  "uuid": "a8a664d5-aac0-49ec-b17c-5d0cf000e51b",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SFZDWYCczSqrpzGNh17eeT`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "3750014a-decc-4e28-b9c8-9684ba2b0984",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfKxaeyha1jkEmy3YjcskN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6055,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6055,
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

_source line 52 · 2026-05-12T22:08:04.379Z_

<details><summary>↩ Tool result · `toolu_01SFZDWYCczSqrpzGNh17eeT`</summary>

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
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2124cab7-686b-4137-9427-54ff7473e629"
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
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for mechanistic interpretability circuit finding 2025…",
  "usage": {
    "total_tokens": 16269,
    "tool_uses": 4,
    "duration_ms": 7704
  },
  "last_tool_name": "WebSearch",
  "uuid": "b130f0ff-a150-429b-855d-16bbcd0b129f",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0116M84vh3hJpMtJokEcTT6y`</summary>

```json
{
  "query": "mechanistic interpretability circuit finding 2025 2026 new algorithm"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "67db6460-5c4c-4fec-9eae-9bc16cb59299",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYuTUzCaKw4ujsjV6EQ6UV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 55 · 2026-05-12T22:08:04.688Z_

<details><summary>↩ Tool result · `toolu_01Lktu12GKZLhRQK7vYmiiV2`</summary>

```text
Web search results for query: "mechanistic interpretability methods comparison 2024 2025 circuit"

Links: [{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=do5vVfKEXZ"},{"title":"Circuits Updates - July 2025","url":"https://transformer-circuits.pub/2025/july-update/index.html"},{"title":"ICML 2024 Mechanistic Interpretability Workshop","url":"https://icml2024mi.pages.dev/"},{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=FbZSZEIkEU"},{"title":"The 2nd New England Mechanistic Interpretability (NEMI) Workshop","url":"https://nemiconf.github.io/summer25/"},{"title":"Transcoders find interpretable LLM feature circuits","url":"https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"},{"title":"A Practical Review of Mechanistic Interpretability for Transformer-Based Language Models","url":"https://arxiv.org/html/2407.02646v4"},{"title":"Open problems in mechanistic interpretability: 2026 status report","url":"https://gist.github.com/bigsnarfdude/629f19f635981999c51a8bd44c6e2a54"},{"title":"Sparse Attention Post-Training for Mechanistic Interpretability","url":"https://arxiv.org/html/2512.05865v1"}]

Based on the web search results, here's what recent research shows about mechanistic interpretability methods comparison:

## Key Frameworks and Categories

Mechanistic interpretability divides into two main categories: Semantic Interpretation (discovering which features or distributed codes correspond to human-interpretable properties, including sparse dictionary learning and concept-based circuits) and Algorithmic Interpretation (elucidating how internal circuits operate over representations, often reconstructing them with human-readable algorithms).

## Prominent Methods (2024-2025)

Several key techniques have emerged:

**Sparse Autoencoders (SAEs)**: SAEs are trained to reconstruct model activations and have been shown to reveal interpretable directions in activation space. Recent variants include transcoders (which model MLP computation), crosscoders (which identify shared and unique features when comparing representations of two models), and SAEs trained directly on activation differences.

**Distributed Interchange Interventions (DII)**: DII performs intervention in rotated subspaces of the representation rather than in the raw neuron basis, first applying a change-of-basis rotation, identifying subspaces corresponding to high-level causal variables, and then performing interventions on those subspaces.

## Evaluation and Benchmarking

The Mechanistic Interpretability Benchmark (MIB) establishes two evaluation tracks—circuit localization and causal variable localization—across diverse tasks, with circuit localization metrics including faithfulness integral (CPR), minimality, and AUROC, while causal variable localization leverages IIA, DBM, PCA, SAE, and DAS featurizers, with supervised DAS significantly outperforming unsupervised SAE features.

## Current Challenges

Core concepts like "feature" lack rigorous definitions, computational complexity results prove many interpretability queries are intractable, and practical methods still underperform simple baselines on safety-relevant tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "0d041bc2-04bd-4065-8902-a7f1f3030133"
}
```

</details>

---


### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for subnetwork discovery interpretability 2024 2025 m…",
  "usage": {
    "total_tokens": 16271,
    "tool_uses": 5,
    "duration_ms": 7838
  },
  "last_tool_name": "WebSearch",
  "uuid": "236e380e-62ee-4fd3-bdc2-a9fc5ca4aa3e",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EcUTYdNneMYnq58DPj31nL`</summary>

```json
{
  "query": "subnetwork discovery interpretability 2024 2025 method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "a752ee98-e618-4439-bb44-72606108d095",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYuTUzCaKw4ujsjV6EQ6UV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 58 · 2026-05-12T22:08:05.962Z_

<details><summary>↩ Tool result · `toolu_01FRNrVKeBSAKU6hKQQv9u2v`</summary>

```text
Web search results for query: "circuit aggregation ensemble mechanistic interpretability"

Links: [{"title":"Mechanistic Interpretability for AI Safety A Review","url":"https://arxiv.org/html/2404.14082v3"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG","url":"https://arxiv.org/html/2510.00845v2"},{"title":"Contents","url":"https://arxiv.org/html/2605.09881"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Mechanistic interpretability - Wikipedia","url":"https://en.wikipedia.org/wiki/Mechanistic_interpretability"},{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=FbZSZEIkEU"},{"title":"[2506.17237] Mechanistic Interpretability of Diffusion Models: Circuit-Level Analysis and Causal Validation","url":"https://arxiv.org/abs/2506.17237"},{"title":"Counting Circuits: Mechanistic Interpretability of Visual Reasoning in Large Vision-Language Models","url":"https://arxiv.org/html/2603.18523v1"},{"title":"Mechanistic Analysis of Circuit Preservation in Federated Learning","url":"https://arxiv.org/html/2512.23043"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523v2"}]

The web search results reveal several important research directions and findings related to circuit aggregation, ensemble methods, and mechanistic interpretability:

## Key Findings

**Circuit Discovery and Aggregation:**

Circuit discovery faces a measurement problem where different analyst choices yield different circuits, with CIRCUS addressing this by computing empirical inclusion frequencies over a configuration family, turning analyst-choice variability into a diagnostic.

The resulting core/contingent/noise taxonomy makes analyst disagreement actionable, demonstrating that ideas from probabilistic model selection transfer naturally to mechanistic interpretability.

**Variance and Stability in Circuit Discovery:**

Varying multiple circuit finding parameters at once (resampling strategy, aggregation method, type of intervention, EAP method, and pruning strategy) yields many different circuits, along with the union and median circuit.

Mechanistic interpretability methods such as circuit discovery should be viewed as statistical estimators subject to questions of variance and robustness, with systematic stability analysis examining variance and robustness through controlled perturbations.

**Circuit Aggregation in Federated Learning:**

Research hypothesizes that the aggregation of conflicting client updates leads to circuit collapse—the destructive interference of functional, sparse sub-networks responsible for specific class predictions.

**Ensemble Approaches:**

Recent work has focused on ensemble SAE features and feature importances, with approaches that ensemble structure (which edges appear) rather than saliency magnitudes.

These findings highlight the importance of treating circuit discovery as an ensemble problem where aggregation methods and stability across configurations are critical for obtaining reliable mechanistic interpretability results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "afeaf1a7-a2a0-4e85-825b-1a8346b7f3a4"
}
```

</details>

---


### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for circuit discovery ICLR 2024 2025 mechanistic inte…",
  "usage": {
    "total_tokens": 16275,
    "tool_uses": 2,
    "duration_ms": 6717
  },
  "last_tool_name": "WebSearch",
  "uuid": "4acc0b69-3aaf-4d10-a646-8fc77c695975",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R476Ca5kuAyMNPTWHaqdE9`</summary>

```json
{
  "query": "circuit discovery ICLR 2024 2025 mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "866dcbf0-846e-451e-8536-2525f50cc015",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3bhSYxas2FdBpiQpdi3vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for robust circuit discovery multi-method consensus t…",
  "usage": {
    "total_tokens": 17217,
    "tool_uses": 3,
    "duration_ms": 16049
  },
  "last_tool_name": "WebSearch",
  "uuid": "11de847b-2a4d-4c25-910e-d4065b537b79",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 62_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HesYAJE4iXowRwz7tvRdad`</summary>

```json
{
  "query": "robust circuit discovery multi-method consensus transformer interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "68805dff-87f1-4756-8db8-07258f90020a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmLXitcUNYpoicRFsKLkQM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 16287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 852,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for mechanistic interpretability NeurIPS 2024 accepte…",
  "usage": {
    "total_tokens": 16277,
    "tool_uses": 3,
    "duration_ms": 7126
  },
  "last_tool_name": "WebSearch",
  "uuid": "e39dc35f-64d3-41fc-8256-a3184fbbaadc",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 64_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RZVTcooWfYDtyEXY9uh1Fo`</summary>

```json
{
  "query": "mechanistic interpretability NeurIPS 2024 accepted papers circuits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "fed22e9e-5795-4b24-90a8-3fe0a03a8c25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3bhSYxas2FdBpiQpdi3vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for circuit discovery ICML 2024 2025 neural network",
  "usage": {
    "total_tokens": 16279,
    "tool_uses": 4,
    "duration_ms": 7687
  },
  "last_tool_name": "WebSearch",
  "uuid": "a75c83d2-2ebf-4d8d-8278-382d9cf0cfc7",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 66_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013F5WqoHqsno1VS9RD6dJv1`</summary>

```json
{
  "query": "circuit discovery ICML 2024 2025 neural network"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "7eca822f-d9b6-41f2-8e05-473e64fac96c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3bhSYxas2FdBpiQpdi3vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for automated interpretability circuits top conferenc…",
  "usage": {
    "total_tokens": 16281,
    "tool_uses": 5,
    "duration_ms": 8095
  },
  "last_tool_name": "WebSearch",
  "uuid": "3cf5b6fc-64ae-4aed-9a2c-c72d539b2393",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LhLtzc7gjShrsPb1EzBoxe`</summary>

```json
{
  "query": "automated interpretability circuits top conference 2024 2025 ICLR NeurIPS ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "472ab986-2db4-4477-96e5-637482297e79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3bhSYxas2FdBpiQpdi3vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 69_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for mechanistic interpretability ICLR 2025 accepted p…",
  "usage": {
    "total_tokens": 16283,
    "tool_uses": 6,
    "duration_ms": 8191
  },
  "last_tool_name": "WebSearch",
  "uuid": "9817552b-fcc6-4bcb-9b86-eac027aaa02d",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GHstMjuhnpNgrbeYG7KMkC`</summary>

```json
{
  "query": "mechanistic interpretability ICLR 2025 accepted papers circuit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "031a6bda-1ac5-493d-93b3-aef1f5811b0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3bhSYxas2FdBpiQpdi3vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/abs/2407.00886",
  "usage": {
    "total_tokens": 21153,
    "tool_uses": 7,
    "duration_ms": 22388
  },
  "last_tool_name": "WebFetch",
  "uuid": "f36a8904-f8c4-4199-b509-44a8e5dff8ba",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KXHQVL51CZJL8asRMvNnBu`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.00886",
  "prompt": "Extract the full title, authors, year, abstract, and key findings. What circuit discovery methods does this paper compare? Does it evaluate consistency or agreement between methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "93e2e822-67b7-4f0d-ae83-e5f433b3a8bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjPdkJjo975cKNuAdr41D4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 16293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4829,
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

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/abs/2512.10903",
  "usage": {
    "total_tokens": 21154,
    "tool_uses": 8,
    "duration_ms": 22809
  },
  "last_tool_name": "WebFetch",
  "uuid": "8f4adb28-fb02-4b1f-a5d7-40327ee74ef8",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 74_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q8GZikFttssbFu22TmzeXr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.10903",
  "prompt": "Extract the full title, authors, year, abstract, and key findings. What circuit discovery methods does this paper compare? Does it evaluate agreement or consistency between different methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "bba57d7e-dcc9-4e91-b8f9-b5492122920d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjPdkJjo975cKNuAdr41D4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 16293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4829,
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

_source line 75 · 2026-05-12T22:08:10.308Z_

<details><summary>↩ Tool result · `toolu_011rTMSMCX614sr1mzJi5W2a`</summary>

```text
Web search results for query: "automated circuit discovery new method transformer 2024 2025"

Links: [{"title":"GitHub - adelaidehsu/CD_Circuit: [ICLR 2025] CD-T: Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition. Paper: https://arxiv.org/abs/2407.00886","url":"https://github.com/adelaidehsu/CD_Circuit"},{"title":"[2407.00886] Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/abs/2407.00886"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition | OpenReview","url":"https://openreview.net/forum?id=41HlN8XYM5"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/html/2407.00886v3"},{"title":"[Quick Review] Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://liner.com/review/efficient-automated-circuit-discovery-in-transformers-using-contextual-decomposition"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/html/2510.03282v1"},{"title":"Circuits Updates - July 2025","url":"https://transformer-circuits.pub/2025/july-update/index.html"},{"title":"ICLR Poster Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://iclr.cc/virtual/2025/poster/31044"},{"title":"[PDF] Towards Automated Circuit Discovery for Mechanistic Interpretability | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Towards-Automated-Circuit-Discovery-for-Mechanistic-Conmy-Mavor-Parker/eefbd8b384a58f464827b19e30a6920ba976def9"},{"title":"Published as a conference paper at ICLR 2025 EFFICIENT AUTOMATED CIRCUIT","url":"https://arxiv.org/pdf/2407.00886"}]

Based on the search results, here are the key findings about automated circuit discovery in transformers using new methods:

## Contextual Decomposition for Transformers (CD-T)

A significant new method is contextual decomposition for transformers (CD-T), which builds interpretable circuits in large language models. CD-T can produce circuits of arbitrary level of abstraction and is the first able to produce circuits as fine-grained as attention heads at specific sequence positions efficiently.

### Key Advantages

CD-T addresses the limitations of previous circuit discovery approaches by significantly reducing runtime, using mathematical decomposition equations with no approximations, allowing for arbitrary level of abstraction of circuits, and avoiding both model training and manually crafted examples. CD-T is compatible with all transformer types and requires no training or manually-crafted examples.

### Comparison to Prior Methods

Existing automated circuit discovery work relies on activation patching or its approximations, and often suffer from slow runtime, approximation errors, and specific requirements of metrics such as non-zero gradients.

## Hybrid Attribution and Pruning Framework (HAP)

Another recent approach is HAP, a hybrid framework that resolves the speed-faithfulness tradeoff in circuit discovery by strategically sequencing EAP with Edge Pruning, and is 46% faster than Edge Pruning while maintaining comparable faithfulness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "21ea1355-b2a8-4c84-82d7-7b2a0d7c25a7"
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-12T22:08:11.147Z_

<details><summary>↩ Tool result · `toolu_01DUf9WzXgFqwZAhLadyAbto`</summary>

```text
Web search results for query: "circuit discovery 2024 2025 mechanistic interpretability new method"

Links: [{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Circuits Updates - July 2025","url":"https://transformer-circuits.pub/2025/july-update/index.html"},{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=FbZSZEIkEU"},{"title":"Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=do5vVfKEXZ"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823"},{"title":"Corti introduces GIM: Benchmark-leading method for understanding AI model behavior | Corti","url":"https://www.corti.ai/stories/gim-a-new-standard-for-mechanistic-interpretability"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"}]

Based on the web search results, here are the key findings on circuit discovery in mechanistic interpretability for 2024-2025:

## Recent Methods and Approaches

A new method called ModCirc has been proposed as a modular circuits discovery method. This addresses limitations in current mechanistic interpretability approaches that focus on discovering task-specific circuits, which have poor generalizability across different language tasks and high costs associated with human interpretation of each computational node. ModCirc is a novel global-level mechanistic interpretability framework for discovering modular circuit vocabularies in LLMs.

Another recent development is GIM (gradient interaction modifications), a gradient-based method that achieves the highest known accuracy for identifying which components in a model are responsible for specific behaviors. GIM tops the Hugging Face Mechanistic Interpretability Benchmark and can identify the circuits behind specific model behaviors faster, cheaper, and more accurately than any other available method.

## Formal Approaches with Guarantees

A new paper on "Formal Mechanistic Interpretability" presents automated circuit discovery that identifies the internal components of neural networks responsible for specific behaviors, with provable guarantees over continuous input domains, addressing limitations where prior methods depend on heuristics or approximations. This work is the first to employ neural network verification based strategies for circuit discovery in mechanistic interpretability.

## Circuit Generalization

Recent research investigating the generality of the indirect object identification (IOI) circuit in GPT-2 small found that the circuit generalizes surprisingly well, reusing all of its components and mechanisms while only adding additional input edges.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "9d648860-9762-4c0e-a7a6-62a2487c286c"
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
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://www.alphaxiv.org/overview/2504.13151v2",
  "usage": {
    "total_tokens": 21155,
    "tool_uses": 9,
    "duration_ms": 24089
  },
  "last_tool_name": "WebFetch",
  "uuid": "aebe79ca-daf5-438d-9878-ffe60c809cc3",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 78_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H39WRxnHaUdx9eeCq3jPwK`</summary>

```json
{
  "url": "https://www.alphaxiv.org/overview/2504.13151v2",
  "prompt": "Extract the full title, authors, year, abstract, and key findings of the MIB (Mechanistic Interpretability Benchmark) paper. What circuit discovery methods does it benchmark? Does it measure agreement or consistency between methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "a82647c5-863d-4cc6-89e8-f568a873bc1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjPdkJjo975cKNuAdr41D4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 16293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4829,
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

_source line 79 · 2026-05-12T22:08:11.744Z_

<details><summary>↩ Tool result · `toolu_01EcUTYdNneMYnq58DPj31nL`</summary>

```text
Web search results for query: "subnetwork discovery interpretability 2024 2025 method"

Links: [{"title":"Mechanistic Interpretability for AI Safety — A Review | Leonard F. Bereska","url":"https://leonardbereska.github.io/blog/2024/mechinterpreview/"},{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"Mechanistic Interpretability for AI Safety A Review","url":"https://arxiv.org/html/2404.14082v1"},{"title":"Mechanistic Interpretability Workshop at ICML 2026","url":"https://mechinterpworkshop.com/"},{"title":"Network Intrusion Detection: Evolution from Conventional Approaches to LLM Collaboration and Emerging Risks","url":"https://arxiv.org/html/2510.23313v1"},{"title":"GitHub - flyingdoog/awesome-graph-explainability-papers: Papers about explainability of GNNs · GitHub","url":"https://github.com/flyingdoog/awesome-graph-explainability-papers"},{"title":"Frontiers | A systematic review on the integration of explainable artificial intelligence in intrusion detection systems to enhancing transparency and interpretability in cybersecurity","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1526221/full"},{"title":"arXiv:2410.01434v3 [cs.LG] 23 Jun 2025","url":"https://arxiv.org/pdf/2410.01434"},{"title":"Trends in NLP Model Interpretability in the Era of LLMs","url":"https://aclanthology.org/2025.naacl-long.29.pdf"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"}]

Here are the search results for subnetwork discovery and interpretability methods from 2024-2025:

## Key Methods and Approaches

Circuit-style mechanistic interpretability has been applied to language models to discover subnetworks (circuits) responsible for specific capabilities. Several automated approaches have emerged:

### Automated Circuit Discovery Methods

Methods like Automated Circuit Discovery (ACDC) and Attribution Patching iteratively knock out model activations, pinpointing components whose removal has the most significant impact on performance. Attribution patching offers a faster and more scalable approach, particularly advantageous in automated circuit discovery and large model applications, providing a more feasible and efficient means of probing neural network behaviors.

### Recent Advances and Techniques

In March 2025, Anthropic introduced circuit tracing that combines earlier methods into a unified framework by replacing a model's MLPs with cross-layer transcoders—a new type of sparse autoencoder that produces an interpretable "replacement model" where the building blocks are sparse, human-readable features rather than polysemantic neurons.

### Evaluation Frameworks

The Mechanistic Interpretability Benchmark establishes two evaluation tracks—circuit localization and causal variable localization—across diverse tasks, with circuit localization metrics including faithfulness integral, minimality, and AUROC.

### Challenges and Future Directions

Manual intervention mapping does not scale; there is a need for higher-throughput automated circuit discovery, hypothesis generation, and robust evaluation standards.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "1f4af22e-0e43-49d8-85c4-1505333b2183"
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-12T22:08:11.799Z_

<details><summary>↩ Tool result · `toolu_0116M84vh3hJpMtJokEcTT6y`</summary>

```text
Web search results for query: "mechanistic interpretability circuit finding 2025 2026 new algorithm"

Links: [{"title":"Open problems in mechanistic interpretability: 2026 status report","url":"https://gist.github.com/bigsnarfdude/629f19f635981999c51a8bd44c6e2a54"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"},{"title":"Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable? | OpenReview","url":"https://openreview.net/forum?id=5IWJBStfU7"},{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=FbZSZEIkEU"},{"title":"Unboxing the Black Box: Mechanistic Interpretability for Algorithmic Understanding of Neural Networks","url":"https://arxiv.org/html/2511.19265v1"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"MIB: A Mechanistic Interpretability Benchmark | OpenReview","url":"https://openreview.net/forum?id=sSrOwve6vb"},{"title":"ICML Poster MIB: A Mechanistic Interpretability Benchmark","url":"https://icml.cc/virtual/2025/poster/43836"},{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"}]

Based on the search results, here are the key findings on mechanistic interpretability circuit finding advances in 2025-2026:

## New Algorithms and Methods

The Stream algorithm (October 2025) achieved near-linear time complexity for attention analysis through hierarchical pruning, enabling interpretability up to 100,000 tokens on consumer hardware by eliminating 97-99% of token interactions.

Researchers have leveraged neural network verification advances to propose automated algorithms that yield circuits with provable guarantees, including input domain robustness, robust patching, and minimality.

## Field Status and Recognition

A landmark collaborative paper published in January 2025 by 29 researchers across 18 organizations established the field's consensus open problems, while MIT Technology Review named the field a "breakthrough technology for 2026."

## Benchmarking Progress

MIB (Mechanistic Interpretability Benchmark) was proposed with two tracks spanning four tasks and five models, favoring methods that precisely and concisely recover relevant causal pathways or causal variables in neural language models. Attribution and mask optimization methods perform best on circuit localization.

## Current Challenges

Despite progress, a 2025 ICLR paper proved many circuit-finding queries are NP-hard, remain fixed-parameter intractable, and are inapproximable under standard computational assumptions. Anthropic's attribution graphs, released in March 2025, can successfully trace computational paths for only about 25% of prompts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "977b75de-2b33-4878-aa7d-afc72d4084eb"
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
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/abs/2407.02646",
  "usage": {
    "total_tokens": 21156,
    "tool_uses": 10,
    "duration_ms": 25737
  },
  "last_tool_name": "WebFetch",
  "uuid": "a535fd32-7ab2-4dd4-947b-9c59163c0aec",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 82_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AKnMqd2t6oYkX98Wgme9ZC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.02646",
  "prompt": "Extract the full title, authors, year, abstract, and key findings. This is a practical review - does it compare circuit discovery methods? Does it discuss consistency or agreement between methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "fb548df1-0bbf-4f59-9f5e-fd2afecf4422",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjPdkJjo975cKNuAdr41D4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 16293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4829,
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
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://openreview.net/forum?id=tiLbFR4bJW",
  "usage": {
    "total_tokens": 21157,
    "tool_uses": 11,
    "duration_ms": 26554
  },
  "last_tool_name": "WebFetch",
  "uuid": "56d0e136-556d-4a0c-b5e7-3e87fadf9b28",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 84_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ns8uDVmM76wpigWmwZvYoj`</summary>

```json
{
  "url": "https://openreview.net/forum?id=tiLbFR4bJW",
  "prompt": "Extract the full title, authors, year, venue, abstract, and key findings. What methods does this paper compare (EAP vs ACDC)? What does it find about their relative performance?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "aac245da-d9a8-4110-9bc1-131f3f935722",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjPdkJjo975cKNuAdr41D4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 16293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4829,
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

_source line 85 · 2026-05-12T22:08:14.170Z_

<details><summary>↩ Tool result · `toolu_013F5WqoHqsno1VS9RD6dJv1`</summary>

```text
Web search results for query: "circuit discovery ICML 2024 2025 neural network"

Links: [{"title":"ICML 2024 Workshops","url":"https://icml.cc/virtual/2024/events/workshop"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"},{"title":"ICML 2024 Schedule","url":"https://icml.cc/virtual/2024/calendar"},{"title":"GitHub - azminewasi/Awesome-Graph-Research-ICML2024: All graph/GNN papers accepted at the International Conference on Machine Learning (ICML) 2024. · GitHub","url":"https://github.com/azminewasi/Awesome-Graph-Research-ICML2024"},{"title":"2026 Conference","url":"https://icml.cc/"},{"title":"International Conference on Machine Learning - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Machine_Learning"},{"title":"ICML 2025 Schedule","url":"https://icml.cc/virtual/2025/calendar"},{"title":"ICML 2024 – Research Impact & Leadership","url":"https://sites.gatech.edu/research/icml-2024/"},{"title":"International Conference on Machine Learning (ICML) 2024 - Apple Machine Learning Research","url":"https://machinelearning.apple.com/updates/apple-at-icml-2024"}]

Based on the search results, I found some relevant information about circuit-related research at ICML conferences:

## Circuit Research at ICML 2024 and 2025

At ICML 2024, the emergence of interpretable behaviors such as circuit mechanisms was highlighted as an example topic in workshops focused on understanding neural networks.

For ICML 2025, there are papers related to circuit research:
- A paper titled "Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models" is scheduled for the conference
- Another paper titled "Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis" is included in the ICML 2025 program

These papers focus on understanding neural networks and language models through circuit analysis and mechanistic interpretability, which aligns with the broader research interest in discovering and understanding the internal circuit structures that emerge within neural networks during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "9cc10eb4-bc72-4597-a15c-be97674b7327"
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-12T22:08:14.402Z_

<details><summary>↩ Tool result · `toolu_01LhLtzc7gjShrsPb1EzBoxe`</summary>

```text
Web search results for query: "automated interpretability circuits top conference 2024 2025 ICLR NeurIPS ICML"

Links: [{"title":"Mechanistic Interpretability Workshop at ICML 2026","url":"https://mechinterpworkshop.com/"},{"title":"2026 Conference","url":"https://icml.cc/"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"ICML 2024 Mechanistic Interpretability Workshop","url":"https://icml2024mi.pages.dev/"},{"title":"Mechanistic Interpretability Workshop at NeurIPS 2025","url":"https://mechinterpworkshop.com/neurips2025/"},{"title":"2024 Conference","url":"https://iclr.cc/Conferences/2024"},{"title":"The NeurIPS/ICLR/ICML Journal-to-Conference Track","url":"https://icml.cc/public/JournalToConference"},{"title":"NeurIPS/ICLR/ICML Journal-to-Conference Track","url":"https://neurips.cc/public/JournalToConference"},{"title":"Workshop on Mechanistic Interpretability","url":"https://icml.cc/virtual/2024/workshop/29953"},{"title":"Actionable Interpretability","url":"https://icml.cc/virtual/2025/workshop/39962"}]

Based on the search results, here's what I found about automated interpretability and circuits research at top conferences in 2024-2025:

## Mechanistic Interpretability Workshop Activity

There have been Mechanistic Interpretability Workshops at ICML 2024 and NeurIPS 2025, with another edition at ICML 2026. 

The field has grown rapidly, with 140+ papers submitted to the ICML 2024 workshop, indicating substantial research activity in this area at top conferences.

The workshop on mechanistic interpretability focuses on the study of reverse-engineering trained neural networks to understand their learned algorithms and internal structure.

## Additional Conference Activity

Beyond the dedicated mechanistic interpretability workshops, interpretability research has advanced considerably in uncovering the inner mechanisms of AI systems and has become a crucial subfield within AI, with workshops on related topics like "Actionable Interpretability" appearing at conferences like ICML 2025.

The search results confirm that automated interpretability and circuits research has been a significant focus area at major conferences (ICLR, NeurIPS, ICML) during 2024-2025, with dedicated workshops attracting substantial submissions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "7e35f0d2-3dad-45fe-b926-b76852870c57"
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-12T22:08:14.942Z_

<details><summary>↩ Tool result · `toolu_01Q8GZikFttssbFu22TmzeXr`</summary>

```text
# Paper Summary

**Full Title:** Multi-Granular Node Pruning for Circuit Discovery

**Authors:** Muhammad Umair Haider, Hammad Rizwan, Hassan Sajjad, A.B. Siddique

**Year:** 2025 (submitted December 11, 2025)

**Abstract:** The research proposes a node-level pruning framework for identifying minimal subnetworks responsible for specific behaviors in large language models. The method introduces "learnable masks across multiple levels of granularity, from entire blocks to individual neurons" with sparsity penalties, achieving compression in a single fine-tuning pass while reducing memory requirements by 5-10x.

## Comparative Methods

The paper compares against "prior methods" but does not specify particular circuit discovery approaches by name in the provided abstract. It notes that existing approaches rely on "iterative edge pruning" and operate at "coarse-grained units such as attention heads or MLP blocks."

## Agreement/Consistency Evaluation

The abstract does not indicate whether this paper evaluates agreement between different circuit discovery methods. Instead, it focuses on demonstrating that neurons deemed important by coarse-grained approaches are "actually irrelevant" while maintaining task performance—suggesting a critique of consistency rather than an explicit comparative analysis of methodological agreement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "d71a1180-46b8-4c31-9786-499f147492e6"
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-12T22:08:15.428Z_

<details><summary>↩ Tool result · `toolu_01R476Ca5kuAyMNPTWHaqdE9`</summary>

```text
Web search results for query: "circuit discovery ICLR 2024 2025 mechanistic interpretability"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2502.20914"},{"title":"ICLR Poster Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://iclr.cc/virtual/2025/poster/31044"},{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=FbZSZEIkEU"},{"title":"Published as a conference paper at ICLR 2025 EFFICIENT AUTOMATED CIRCUIT","url":"https://arxiv.org/pdf/2407.00886"},{"title":"ICML 2024 Mechanistic Interpretability Workshop","url":"https://icml2024mi.pages.dev/"},{"title":"ICLR.2025 - Spotlight | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2025?group=Spotlight"},{"title":"ICLR Poster The Computational Complexity of Circuit Discovery for Inner Interpretability","url":"https://iclr.cc/virtual/2025/poster/29673"},{"title":"Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims","url":"https://arxiv.org/html/2605.08012"},{"title":"AUTOMATED CIRCUIT DISCOVERY WITH PROVABLE ...","url":"https://openreview.net/pdf/2a96a0e7b48eb87468aa147e202b58c818feecbd.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/84ca3f2d9d9bfca13f69b48ea63eb4a5-Paper-Conference.pdf"}]

Based on the web search results, here are the key findings related to circuit discovery and mechanistic interpretability at ICLR 2024-2025:

## Key Papers and Research

**Efficient Automated Circuit Discovery:**

Contextual Decomposition for Transformers (CD-T) has been introduced to build interpretable circuits in large language models, producing circuits at any level of abstraction and being the first to efficiently produce circuits as fine-grained as attention heads at specific sequence positions. CD-T reduces circuit discovery runtime from hours to seconds compared to state-of-the-art baselines.

**Circuit Generalization:**

Mechanistic interpretability aims to understand neural networks by identifying circuits, or minimal subgraphs that implement algorithms for specific tasks, typically discovered and analyzed using narrowly defined prompt formats, though it remains unclear how well these circuits generalize across various prompt formats.

**Computational Complexity:**

Many proposed applications of neural networks hinge on the feasibility of inner interpretability via circuit discovery, which calls for empirical and theoretical explorations of viable algorithmic options.

**Methodological Approaches:**

The "where-then-what" strategy focuses on finding a subset of the network – a circuit – that captures information flow from inputs to outputs, and once identified using heuristics, the next step is to interpret its components to derive the explanatory algorithm.

**Circuit Analysis with SAEs:**

Sparse autoencoders (SAEs) have been used for circuit analysis and to replicate the identification of a circuit for indirect object identification in GPT-2.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "752bf5b9-a3f7-4705-8bad-cdebc52fea0d"
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-12T22:08:15.439Z_

<details><summary>↩ Tool result · `toolu_01H39WRxnHaUdx9eeCq3jPwK`</summary>

```text
# MIB: Mechanistic Interpretability Benchmark

Based on the webpage content provided, I can only confirm limited information:

**What's Available:**
The page shows this is a paper titled "MIB: A Mechanistic Interpretability Benchmark" hosted on alphaXiv. The interface indicates there are associated resources including a blog post, audio content, and 234 citations.

**What's Missing:**
Unfortunately, the actual paper content—including authors, publication year, abstract, and detailed findings—is not included in the webpage excerpt you provided. The snippet only shows the navigation interface and title.

**To Get the Information You Need:**
To extract the full title with author names, year, abstract describing the benchmark's scope, and specifics about:
- Which circuit discovery methods are benchmarked
- Whether it measures agreement/consistency between methods

I would need access to the actual paper content, typically found by clicking the "[Paper](/abs/2504.13151v2)" link shown in the interface. The paper identifier "2504.13151v2" suggests this is an arXiv preprint that would contain this information.

Would you be able to share the full paper abstract or text content?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "0d216530-9492-4e62-9ff1-0aa242138e44"
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-12T22:08:15.475Z_

<details><summary>↩ Tool result · `toolu_01KXHQVL51CZJL8asRMvNnBu`</summary>

```text
# Paper Summary

**Full Title:** Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition

**Authors:** Aliyah R. Hsu, Georgia Zhou, Yeshwanth Cherapanamjeri, Yaxuan Huang, Anobel Y. Odisho, Peter R. Carroll, Bin Yu

**Year:** 2024 (submitted July 1, 2024; latest revision March 2, 2025)

**Abstract:** The authors introduce CD-T (contextual decomposition for transformers) to identify interpretable circuits in large language models. The method uses "mathematical equations to isolate contribution of model features" and achieves fine-grained circuit discovery at the attention head level with significantly faster runtimes.

## Circuit Discovery Methods Compared

The paper compares CD-T against two baseline approaches:
- **ACDC** (Automated Circuit Discovery)
- **EAP** (Evaluation-based Attribution Pruning)

## Consistency and Agreement Evaluation

Yes, the paper evaluates consistency across methods:

- CD-T "outperforms ACDC and EAP by better recovering the manual circuits with an average of 97% ROC AUC under low runtimes"
- Achieves perfect faithfulness (score = 1) using fewer nodes than baselines
- Shows circuits are "80% more faithful than random circuits of up to 60% of the original model size"

The authors validate agreement with ground truth through three standard evaluation datasets: indirect object identification, greater-than comparisons, and docstring completion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "6810fb7a-a386-4317-82c5-c27c33735cc4"
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-12T22:08:15.515Z_

<details><summary>↩ Tool result · `toolu_01RZVTcooWfYDtyEXY9uh1Fo`</summary>

```text
Web search results for query: "mechanistic interpretability NeurIPS 2024 accepted papers circuits"

Links: [{"title":"Compact Proofs of Model Performance via Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/90e73f3cf1a6c84c723a2e8b7fb2b2c1-Paper-Conference.pdf"},{"title":"Mechanistic Interpretability Workshop at ICML 2026","url":"https://mechinterpworkshop.com/"},{"title":"Call for Papers | Mechanistic Interpretability Workshop at ICML 2026","url":"https://mechinterpworkshop.com/cfp/"},{"title":"ICML 2024 Mechanistic Interpretability Workshop","url":"https://icml2024mi.pages.dev/"},{"title":"LLM Circuit Analyses Are Consistent Across Training and Scale Curt Tigges","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf"},{"title":"NeurIPS Poster InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://neurips.cc/virtual/2024/poster/97689"},{"title":"Mechanistic interpretability - Wikipedia","url":"https://en.wikipedia.org/wiki/Mechanistic_interpretability"},{"title":"[2406.11944] Transcoders Find Interpretable LLM Feature Circuits","url":"https://arxiv.org/abs/2406.11944"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"NeurReps Workshop","url":"https://www.neurreps.org/"}]

Based on the search results, I found several mechanistic interpretability papers that were accepted to NeurIPS 2024, particularly focusing on circuits:

## Key NeurIPS 2024 Mechanistic Interpretability Papers on Circuits

**1. "Compact Proofs of Model Performance via Mechanistic Interpretability"**

This paper provides a formalization of mechanistic interpretability with theorem statements that are exact expressions for the difference between the actual behavior of the model and the purported behavior, and proofs that are computations that bound the expression. The work studies a simple model used in the mathematical framework for transformer circuits and discusses extending the approach to proving bounds on 1-layer transformers with ReLU MLP trained on modular addition.

**2. "LLM Circuit Analyses Are Consistent Across Training and Scale"**

This paper shows that the stability of circuit algorithms over the course of training suggests that analyses performed on models at a given point during training may provide valuable insights into earlier and later phases of training, and the consistency in the emergence of critical components and the algorithmic structure of these circuits across different model scales suggests that studying smaller models can sometimes provide insights applicable to larger models.

**3. "InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques"**

This work presents InterpBench, a collection of semi-synthetic yet realistic transformers with known circuits for evaluating mechanistic interpretability techniques. The benchmark can train transformers with larger circuits, like Indirect Object Identification (IOI), and is used to evaluate existing circuit discovery techniques.

These papers represent recent advances in understanding, proving properties of, and validating neural network circuits through mechanistic interpretability approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "c92a91a3-7414-4e7a-821a-8552f034d1bf"
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
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://arxiv.org/abs/2407.00886",
  "usage": {
    "total_tokens": 19991,
    "tool_uses": 6,
    "duration_ms": 19053
  },
  "last_tool_name": "WebFetch",
  "uuid": "083f9f58-0272-4bcd-92aa-4625ebf9896b",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 93_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015tJiTtM7HJ1qy8HkJrAQdB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.00886",
  "prompt": "Extract: paper title, full author list, year, venue, and the complete abstract. Also note the key algorithmic contribution."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "33fdc118-9cba-41ca-a7a5-9d841bb4542a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Lp8GzRywNy1xW6q8R8foq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 857,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 16250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2864,
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

_source line 94 · 2026-05-12T22:08:16.910Z_

<details><summary>↩ Tool result · `toolu_01GHstMjuhnpNgrbeYG7KMkC`</summary>

```text
Web search results for query: "mechanistic interpretability ICLR 2025 accepted papers circuit"

Links: [{"title":"ICLR Poster Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable?","url":"https://iclr.cc/virtual/2025/poster/30956"},{"title":"ICLR.2025 - Spotlight | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2025?group=Spotlight"},{"title":"ICML 2024 Mechanistic Interpretability Workshop","url":"https://icml2024mi.pages.dev/"},{"title":"Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable? | OpenReview","url":"https://openreview.net/forum?id=5IWJBStfU7"},{"title":"Mechanistic Interpretability of In-Context Learning Generalization through Structured Task Curriculum | OpenReview","url":"https://openreview.net/forum?id=2Fv4GxUElU"},{"title":"Call for Papers | Mechanistic Interpretability Workshop at ICML 2026","url":"https://mechinterpworkshop.com/cfp/"},{"title":"Is Mechanistic Interpretability Identifiable?","url":"https://iclr.cc/media/iclr-2025/Slides/30956.pdf"},{"title":"ICML Poster MIB: A Mechanistic Interpretability Benchmark","url":"https://icml.cc/virtual/2025/poster/43836"},{"title":"Open problems in mechanistic interpretability: 2026 status report","url":"https://gist.github.com/bigsnarfdude/629f19f635981999c51a8bd44c6e2a54"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2502.20914"}]

Based on the search results, here are some mechanistic interpretability papers related to circuits that were accepted at ICLR 2025:

## Accepted Papers

**1. "Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable?"**

This paper examines how mechanistic interpretability aims to reverse-engineer neural networks by extracting human-understandable algorithms embedded within their structures. The work identifies two broad strategies: "where-then-what," which first identifies a subset of the network (a circuit) that replicates the model's behavior before deriving its interpretation, and "what-then-where," which begins with candidate explanatory algorithms and searches in the activation subspaces of the neural model. The experiments reveal overwhelming evidence of non-identifiability in all cases: multiple circuits can replicate model behavior, multiple interpretations can exist for a circuit, several algorithms can be causally aligned with the neural network, and a single algorithm can be causally aligned with different subspaces of the network.

**2. "Mechanistic Interpretability of In-Context Learning Generalization through Structured Task Curriculum"**

This paper identifies mechanistically interpretable "common structures" in the Transformer QK circuits at lower layers, along with higher-layer features, that support cross-task generalization.

**3. "MIB: A Mechanistic Interpretability Benchmark"**

This paper proposes MIB, a large-scale dataset for evaluating and comparing mechanistic interpretability methods. Using MIB, attribution and mask optimization methods perform best on circuit localization.

**4. "The Computational Complexity of Circuit Discovery for Inner Interpretability"**

A 2025 ICLR paper proved many circuit-finding queries are NP-hard, remain fixed-parameter intractable, and are inapproximable under standard computational assumptions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "5a1c23df-6c63-43e7-916b-cda505db6436"
}
```

</details>

---


### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://arxiv.org/abs/2602.16823",
  "usage": {
    "total_tokens": 19992,
    "tool_uses": 7,
    "duration_ms": 20047
  },
  "last_tool_name": "WebFetch",
  "uuid": "34d40fd8-9214-4cf7-9d1f-bc0dea00f594",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 96_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XGj7UMz6Hz8KVhCqVCCo5v`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.16823",
  "prompt": "Extract: paper title, full author list, year, venue, and the complete abstract. Also note the key algorithmic contribution."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "c37361d7-1bd8-462a-a7af-f866e02de19b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Lp8GzRywNy1xW6q8R8foq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 857,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 16250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2864,
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

_source line 97 · 2026-05-12T22:08:17.085Z_

<details><summary>↩ Tool result · `toolu_01HesYAJE4iXowRwz7tvRdad`</summary>

```text
Web search results for query: "robust circuit discovery multi-method consensus transformer interpretability"

Links: [{"title":"Transformer Circuit Faithfulness Metrics Are Not Robust","url":"https://arxiv.org/html/2407.08734v1"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/html/2407.00886v2"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"[2407.00886] Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/abs/2407.00886"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition | OpenReview","url":"https://openreview.net/forum?id=41HlN8XYM5"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/html/2510.03282v1"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://arxiv.org/html/2407.14494v2"}]

I found several relevant research papers on circuit discovery and transformer interpretability. Here's a summary of what the search returned:

## Key Research Areas

**Circuit Discovery Methods:**
Circuit analysis is a form of post-hoc interpretability focused on understanding the learned algorithm responsible for specified behavior, where a circuit is a subgraph of the full computational graph of the model.

**Automated Circuit Discovery Approaches:**

1. **ACDC (Automatic Circuit Discovery):** This work automates finding connections between abstract neural network units that form a circuit, proposing several algorithms and reproducing previous interpretability results to validate them.

2. **Contextual Decomposition for Transformers (CD-T):** CD-T is introduced to build interpretable circuits in large language models and can produce circuits of arbitrary level of abstraction, with the ability to produce circuits as fine-grained as attention heads at specific sequence positions efficiently. On three standard circuit evaluation datasets, CD-T outperforms ACDC and EAP by better recovering the manual circuits with an average of 97% ROC AUC under low runtimes.

3. **Hybrid Attribution and Pruning (HAP):** HAP is a hybrid framework that resolves the speed-faithfulness tradeoff in circuit discovery by strategically sequencing EAP with edge pruning, showing it is 46% faster than edge pruning while maintaining comparable faithfulness.

**Robustness Concerns:**
Existing circuit faithfulness methods are highly sensitive to seemingly insignificant changes in ablation methodology, with faithfulness scores reflecting both methodological choices and actual circuit components.

The research demonstrates ongoing work to improve circuit discovery robustness and efficiency across different transformer interpretability methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "0708534e-63ea-4451-adad-d44bec1c017c"
}
```

</details>

---


### Tool result

_source line 98 · 2026-05-12T22:08:17.244Z_

<details><summary>↩ Tool result · `toolu_01Ns8uDVmM76wpigWmwZvYoj`</summary>

```text
# Attribution Patching Research Summary

**Title:** "Attribution Patching Outperforms Automated Circuit Discovery"

**Authors:** Not listed in the provided content

**Year:** 2023

**Venue:** NeurIPS 2023 Workshop ATTRIB

**Abstract:** The paper presents a technique using attribution patching to identify neural network subnetworks responsible for specific tasks. The authors demonstrate their method requires "just two forward passes and a backward pass" while outperforming existing approaches through linear approximation of activation patching to estimate edge importance.

## Methods Comparison

The paper contrasts attribution-based patching against automated circuit discovery methods (ACDC). While specific technical details of ACDC aren't elaborated in this excerpt, the research applies "a linear approximation to activation patching" to rank edges by importance.

## Key Findings

The primary result is that the proposed attribution patching method achieves "greater AUC from circuit recovery than other methods" when averaged across all tasks. The innovation emphasizes computational efficiency—accomplishing circuit identification with minimal forward/backward passes compared to existing expensive activation patching approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "c7a14388-add6-4610-9b3e-b2d41275bc6c"
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-12T22:08:17.681Z_

<details><summary>↩ Tool result · `toolu_01AKnMqd2t6oYkX98Wgme9ZC`</summary>

```text
# Paper Summary

**Title:** "A Practical Review of Mechanistic Interpretability for Transformer-Based Language Models"

**Authors:** Daking Rai, Yilun Zhou, Shi Feng, Abulhair Saparov, Ziyu Yao

**Year:** 2024 (submitted July 2, 2024; latest revision October 13, 2025)

**Abstract Overview:**
This survey examines mechanistic interpretability research through a task-centric lens. The authors state they aim to help newcomers by organizing "the taxonomy of MI research around specific research questions or tasks," covering fundamental study objects, techniques, evaluation methods, and findings while discussing field gaps and future directions.

## Regarding Circuit Discovery Methods

The provided web page content does not include the full paper text, only the abstract and metadata. Based on what's available, **the abstract does not explicitly mention comparing circuit discovery methods or discussing consistency between approaches.**

The page offers links to view the PDF and HTML versions where such comparisons would likely appear in the detailed content, but those sections aren't included in the excerpt provided. To determine whether this practical review compares methodologies or examines inter-method agreement, you would need to access the full paper directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "08f30886-e117-458c-aa44-bd98b1a99b96"
}
```

</details>

---


### System

_source line 100_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://arxiv.org/html/2510.03282v1",
  "usage": {
    "total_tokens": 19993,
    "tool_uses": 8,
    "duration_ms": 21022
  },
  "last_tool_name": "WebFetch",
  "uuid": "b470db8c-ffe4-4390-9376-78507e09cbd6",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 101_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XTu8msJFz9i494ABKVvhRf`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.03282v1",
  "prompt": "Extract: paper title, full author list, year, venue, and the complete abstract. Also note the key algorithmic contribution (HAP framework)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "1d3364c8-a020-4fe4-ac0c-eb9c67e62f25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Lp8GzRywNy1xW6q8R8foq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 857,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 16250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2864,
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

_source line 102_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for combining circuit discovery methods transformers …",
  "usage": {
    "total_tokens": 18213,
    "tool_uses": 4,
    "duration_ms": 27333
  },
  "last_tool_name": "WebSearch",
  "uuid": "83c1f1f8-a339-463f-aa14-54b87a403f8c",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 103_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BAj4gm5pwzvwJtMGKywbyh`</summary>

```json
{
  "query": "combining circuit discovery methods transformers mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e5f10e08-93e9-4387-aad8-1e3b8b3335b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oe47qFKjff6qzeb9ga7gU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 935,
      "cache_read_input_tokens": 17139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 935,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 104_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://openreview.net/forum?id=do5vVfKEXZ",
  "usage": {
    "total_tokens": 19994,
    "tool_uses": 9,
    "duration_ms": 22781
  },
  "last_tool_name": "WebFetch",
  "uuid": "a81b35d8-d159-4aac-a068-9931a6f28647",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 105_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VZZftqfBuwADoP2Wp3JBtH`</summary>

```json
{
  "url": "https://openreview.net/forum?id=do5vVfKEXZ",
  "prompt": "Extract: paper title, full author list, year, venue, and the abstract. Note the method name (ModCirc) and key algorithmic contribution."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "fbadbcd3-0865-45a7-85d7-7d1a5234bbaa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Lp8GzRywNy1xW6q8R8foq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 857,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 16250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2864,
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

_source line 106_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://openreview.net/forum?id=sSrOwve6vb",
  "usage": {
    "total_tokens": 19995,
    "tool_uses": 10,
    "duration_ms": 23047
  },
  "last_tool_name": "WebFetch",
  "uuid": "9ee2725f-f5b6-4016-881f-4f6417248e47",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 107_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V5P649tvVizSFuby4nsecc`</summary>

```json
{
  "url": "https://openreview.net/forum?id=sSrOwve6vb",
  "prompt": "Extract: paper title, full author list, year, venue, and the abstract for the MIB (Mechanistic Interpretability Benchmark) paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "d94d2aef-0700-4f08-a625-8ecc411f2e3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Lp8GzRywNy1xW6q8R8foq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 857,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 16250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2864,
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

_source line 108_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for sparse autoencoders circuit discovery NeurIPS 202…",
  "usage": {
    "total_tokens": 20588,
    "tool_uses": 7,
    "duration_ms": 19493
  },
  "last_tool_name": "WebSearch",
  "uuid": "325ad444-7b50-421c-9ede-69948cdd5601",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 109_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PyeY9udtB3dnk1u6MBptrV`</summary>

```json
{
  "query": "sparse autoencoders circuit discovery NeurIPS 2024 ICLR 2025 feature circuits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "68a1d8ab-d99b-45c4-bd17-30e8698561b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RmNjXikE2g2fQUuWthiKy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4305,
      "cache_read_input_tokens": 16260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4305,
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

_source line 110 · 2026-05-12T22:08:20.822Z_

<details><summary>↩ Tool result · `toolu_01XGj7UMz6Hz8KVhCqVCCo5v`</summary>

```text
# Paper Summary

**Title:** Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees

**Authors:** Itamar Hadad, Guy Katz, Shahaf Bassan

**Year:** 2026

**Venue:** ICLR 2026

**Abstract:**
The paper introduces "automated circuit discovery" methods that leverage neural network verification to identify internal neural network components responsible for specific behaviors. The researchers propose algorithms offering three types of formal guarantees: "(1) input domain robustness, ensuring the circuit agrees with the model across a continuous input region; (2) robust patching, certifying circuit alignment under continuous patching perturbations; and (3) minimality."

**Key Algorithmic Contribution:**
The primary contribution is a suite of algorithms that yield circuits with provable guarantees over continuous input domains. Rather than relying on heuristics or approximations typical of prior methods, these algorithms establish theoretical connections among the three guarantee families and demonstrate substantially stronger robustness properties through experiments with state-of-the-art verifiers on vision models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "4f154a65-0cdf-4181-b160-40c863feb05a"
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-12T22:08:21.034Z_

<details><summary>↩ Tool result · `toolu_015tJiTtM7HJ1qy8HkJrAQdB`</summary>

```text
# Paper Summary

**Title:** Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition

**Authors:** Aliyah R. Hsu, Georgia Zhou, Yeshwanth Cherapanamjeri, Yaxuan Huang, Anobel Y. Odisho, Peter R. Carroll, Bin Yu

**Year:** 2024 (submitted July 1, 2024; latest revision March 2, 2025)

**Venue:** arXiv (cs.AI, cs.CL, cs.LG)

**Abstract:**
The authors introduce contextual decomposition for transformers (CD-T), a method for "automated mechanistic interpretation" that identifies interpretable subgraphs in language models. CD-T uses mathematical equations to isolate feature contributions throughout a model's computational graph. The approach dramatically improves efficiency—reducing "circuit discovery runtime from hours to seconds"—while achieving superior performance. Testing on three standard benchmarks shows CD-T attains "an average of 97% ROC AUC" and produces circuits with perfect fidelity using fewer nodes than existing baselines.

**Key Algorithmic Contribution:**
CD-T introduces a recursive mathematical framework that computes node contributions in transformer computational graphs, enabling fine-grained circuit extraction at attention head and sequence position levels. This approach eliminates reliance on activation patching approximations and gradient requirements, achieving orders-of-magnitude speedup while maintaining or improving faithfulness metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "24dd0a46-90c5-4df5-85eb-7438af940708"
}
```

</details>

---


### System

_source line 112_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"circuit discovery\" OR \"circuit finding\" ICML 202…",
  "usage": {
    "total_tokens": 20589,
    "tool_uses": 8,
    "duration_ms": 20104
  },
  "last_tool_name": "WebSearch",
  "uuid": "2b05db68-0785-490e-a07d-325f3a58c2ba",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 113_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ApTdV7LxZP7HH3vumidxav`</summary>

```json
{
  "query": "\"circuit discovery\" OR \"circuit finding\" ICML 2024 transformers interpretability paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "9d4ebd91-b270-42c1-9c97-f1cffda25836",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RmNjXikE2g2fQUuWthiKy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4305,
      "cache_read_input_tokens": 16260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4305,
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

_source line 114_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for ACDC automated circuit discovery NeurIPS 2023 202…",
  "usage": {
    "total_tokens": 20590,
    "tool_uses": 9,
    "duration_ms": 20552
  },
  "last_tool_name": "WebSearch",
  "uuid": "f1811796-d8ee-4d87-b498-2bf056148cd0",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 115_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LU41E9VbGcqijVnAvhZcYo`</summary>

```json
{
  "query": "ACDC automated circuit discovery NeurIPS 2023 2024 transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "61d1d63f-4c6a-43e6-bfe1-1bfcf857a680",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RmNjXikE2g2fQUuWthiKy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4305,
      "cache_read_input_tokens": 16260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4305,
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

_source line 116_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/abs/2504.13151",
  "usage": {
    "total_tokens": 23289,
    "tool_uses": 12,
    "duration_ms": 35131
  },
  "last_tool_name": "WebFetch",
  "uuid": "92ed3ab1-7abb-4845-aabb-9851144d8eb3",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 117_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015c1x5KTba1aDri8TNKc5Gs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.13151",
  "prompt": "Extract the full title, authors, year, abstract. What circuit discovery methods does MIB benchmark? Does it measure agreement or consistency between different methods? What are the key findings about how different methods perform?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "9ca38b17-bae5-4d6c-bc01-b4b2f6b0772e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8ehJqhFWzFZpD21tZGiFn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 1854,
      "cache_read_input_tokens": 21122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1854,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 118 · 2026-05-12T22:08:22.963Z_

<details><summary>↩ Tool result · `toolu_01VZZftqfBuwADoP2Wp3JBtH`</summary>

```text
# Paper Summary

**Title:** "Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models"

**Authors:** Yinhan He, Wendy Zheng, Yushun Dong, Yaochen Zhu, Chen Chen, Jundong Li

**Year:** 2025

**Venue:** ICML 2025 Conference

**Abstract:**
The research addresses limitations in current mechanistic interpretability approaches by proposing a framework that discovers task-agnostic functional units rather than task-specific circuits. The authors state: "This approach enables global interpretability by allowing different language tasks to share common MCs, while reducing costs by reusing established interpretations for new tasks."

**Method:** ModCirc is the proposed framework for discovering modular circuit vocabularies. Its key algorithmic contribution involves establishing five criteria to characterize modular circuits and developing mechanisms for identifying reusable computational subgraphs with consistent interpretations across diverse language tasks, thereby reducing the expense of human interpretation while improving generalizability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "ec25efea-a46c-48e2-a049-e09ace079e72"
}
```

</details>

---


### System

_source line 119_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for \"circuit discovery\" methods disagree inconsistent…",
  "usage": {
    "total_tokens": 23292,
    "tool_uses": 13,
    "duration_ms": 35738
  },
  "last_tool_name": "WebSearch",
  "uuid": "ddc12fb5-f22f-42c4-9ca3-2ca04925f624",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 120_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ML4GAb8Nbn4FjiNYwnupNy`</summary>

```json
{
  "query": "\"circuit discovery\" methods disagree inconsistent different circuits same task transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "34e5be31-492d-4bac-8183-a9cb89d1530c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8ehJqhFWzFZpD21tZGiFn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 1854,
      "cache_read_input_tokens": 21122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1854,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-12T22:08:23.296Z_

<details><summary>↩ Tool result · `toolu_01XTu8msJFz9i494ABKVvhRf`</summary>

```text
# Paper Summary

**Title:** Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework

**Authors:** Hao Gu, Vibhas Nair, Amrithaa Ashok Kumar, Jayvart Sharma, Ryan Lagasse (Algoverse AI Research)

**Year:** 2025

**Venue:** arXiv (preprint arXiv:2510.03282v1)

**Abstract:**
The paper addresses a fundamental challenge in mechanistic interpretability: existing circuit discovery methods face a trade-off between speed and accuracy. The authors propose that "attribution patching is fast but unfaithful to the full model, while edge pruning is faithful but computationally expensive." Their solution combines both approaches strategically.

**Key Algorithmic Contribution (HAP Framework):**

The Hybrid Attribution and Pruning (HAP) framework operates in three sequential steps:

1. **Computational Graph Construction** – Represents transformer components as nodes with information flow as edges
2. **Edge Attribution Patching** – Uses EAP to quickly identify high-potential edges through gradient-based scoring
3. **Subgraph Selection and Edge Pruning** – Applies EP to extract faithful circuits from the EAP-filtered subgraph

The innovation leverages EAP's speed to narrow the search space, enabling EP to operate more efficiently. Results demonstrate HAP achieves 46% faster computation than EP alone while maintaining comparable faithfulness, and notably preserves cooperative circuit components (S-inhibition heads) that pure attribution methods overlook.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "a2e5e8dc-304f-4c44-9d01-44b17d1f6460"
}
```

</details>

---


### System

_source line 122_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for edge pruning ACDC EAP attribution patching circui…",
  "usage": {
    "total_tokens": 23295,
    "tool_uses": 14,
    "duration_ms": 36066
  },
  "last_tool_name": "WebSearch",
  "uuid": "33b548f1-3de1-458e-bd44-da3ce57a399a",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 123_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LAPc9G7t3wT7UPMGNqS2Qk`</summary>

```json
{
  "query": "edge pruning ACDC EAP attribution patching circuits overlap agreement 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b7f69e89-0015-4c1d-891e-e3a212aed478",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8ehJqhFWzFZpD21tZGiFn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 1854,
      "cache_read_input_tokens": 21122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1854,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 124 · 2026-05-12T22:08:23.919Z_

<details><summary>↩ Tool result · `toolu_01V5P649tvVizSFuby4nsecc`</summary>

```text
# MIB Paper Details

**Title:** "MIB: A Mechanistic Interpretability Benchmark"

**Authors:** Aaron Mueller, Atticus Geiger, Sarah Wiegreffe, Dana Arad, Iván Arcuschin, Adam Belfki, Yik Siu Chan, Jaden Fried Fiotto-Kaufman, Tal Haklay, Michael Hanna, Jing Huang, Rohan Gupta, Yaniv Nikankin, Hadas Orgad, Nikhil Prakash, Anja Reusch, Aruna Sankaranarayanan, Shun Shao, Alessandro Stolfo, Martin Tutek, and 3 additional authors

**Year:** 2025

**Venue:** ICML 2025 Conference

**Abstract:** The authors propose a benchmark establishing evaluation standards for mechanistic interpretability methods across two tracks: circuit localization and causal variable localization. They assess "methods that precisely and concisely recover relevant causal pathways or causal variables in neural language models." Their findings indicate that attribution and mask optimization methods excel at circuit localization, while supervised DAS outperforms sparse autoencoders for causal variable tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8ffb2f35-a522-40dd-95d2-17d717cb81bc"
}
```

</details>

---


### System

_source line 125_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"Transcoders Find Interpretable LLM Feature Circu…",
  "usage": {
    "total_tokens": 20591,
    "tool_uses": 10,
    "duration_ms": 23102
  },
  "last_tool_name": "WebSearch",
  "uuid": "5104ca38-cc84-489c-93bc-e23e2c3fa4e7",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 126_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NCgyndzqwHVcZpQHZECJMf`</summary>

```json
{
  "query": "\"Transcoders Find Interpretable LLM Feature Circuits\" venue conference 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "f0c0b47b-973a-4fb8-a4d3-8694c89fec94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RmNjXikE2g2fQUuWthiKy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4305,
      "cache_read_input_tokens": 16260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4305,
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

_source line 127 · 2026-05-12T22:08:26.963Z_

<details><summary>↩ Tool result · `toolu_01BAj4gm5pwzvwJtMGKywbyh`</summary>

```text
Web search results for query: "combining circuit discovery methods transformers mechanistic interpretability"

Links: [{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"Seeing Through Circuits: Faithful Mechanistic Interpretability for Vision Transformers","url":"https://arxiv.org/html/2604.14477"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/html/2510.03282v1"},{"title":"[2407.00886] Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/abs/2407.00886"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | alphaXiv","url":"https://www.alphaxiv.org/overview/2304.14997"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/html/2407.00886v3"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition | OpenReview","url":"https://openreview.net/forum?id=41HlN8XYM5"},{"title":"Transformer Circuits Thread","url":"https://transformer-circuits.pub/"}]

Based on the search results, here's what I found about combining circuit discovery methods for transformer mechanistic interpretability:

## Key Research Areas

Combining edge-level and neuron-level analyses to identify which neurons within circuit edges carry the most semantically interpretable information would yield richer mechanistic descriptions than either approach provides alone.

## Multiple Circuit Discovery Approaches

Recent research has developed several complementary methods for circuit discovery:

1. **Activation Patching Methods**: Researchers choose a metric and dataset that elicit the desired model behavior, then apply activation patching to find which abstract neural network units are involved in the behavior.

2. **Contextual Decomposition (CD-T)**: Contextual decomposition for transformers can produce circuits of arbitrary level of abstraction and is the first able to produce circuits as fine-grained as attention heads at specific sequence positions efficiently. By recursively computing contribution of all nodes in a computational graph using CD-T followed by pruning, circuit discovery runtime can be reduced from hours to seconds compared to state-of-the-art baselines.

3. **Hybrid Approaches**: A hybrid attribution and pruning framework (HAP) is 46% faster than baseline algorithms without sacrificing circuit faithfulness, and shows that the method preserves cooperative circuit components that attribution patching methods prune at high sparsity.

4. **Edge-Based Pruning**: Edge pruning and optimization-based methods frame circuit discovery as a gradient-based optimization problem with binary masks over edges, allowing for finer-grained and more faithful recovery of causal pathways.

These approaches address different challenges in circuit discovery, with varying trade-offs between runtime, faithfulness, and interpretability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "1a9469b0-f96e-4f41-9bc3-c679368bdba9"
}
```

</details>

---


### System

_source line 128_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for GIM gradient interaction modifications mechanisti…",
  "usage": {
    "total_tokens": 22097,
    "tool_uses": 11,
    "duration_ms": 31054
  },
  "last_tool_name": "WebSearch",
  "uuid": "66824817-39ba-423b-9c58-6ff698b61a20",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 129_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WjakV8dGVAkJLZprN1x2Ri`</summary>

```json
{
  "query": "GIM gradient interaction modifications mechanistic interpretability Corti circuit discovery"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "367cc996-e4d4-44fa-8d22-4bd9e9b3e11b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiUNT6hzJjtxG8bRvMQNjD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2956,
      "cache_read_input_tokens": 19114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2956,
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

_source line 130 · 2026-05-12T22:08:28.092Z_

<details><summary>↩ Tool result · `toolu_01LU41E9VbGcqijVnAvhZcYo`</summary>

```text
Web search results for query: "ACDC automated circuit discovery NeurIPS 2023 2024 transformer"

Links: [{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery · GitHub","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"NeurIPS Poster Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://neurips.cc/virtual/2023/poster/72666"},{"title":"Towards automated circuit discovery for mechanistic interpretability | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3666841"},{"title":"Automatic Circuit Discovery","url":"https://sidn.baulab.info/autocircuits/"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://papers.nips.cc/paper_files/paper/2023/hash/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Abstract-Conference.html"},{"title":"(PDF) Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://www.researchgate.net/publication/370417693_Towards_Automated_Circuit_Discovery_for_Mechanistic_Interpretability"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery Aaquib Syed","url":"https://openreview.net/pdf?id=tiLbFR4bJW"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://www.arxiv.org/pdf/2510.03282"}]

Based on the web search results, here's what I found about ACDC (Automated Circuit Discovery):

## Overview

ACDC is the accompanying code to the paper "Towards Automated Circuit Discovery for Mechanistic Interpretability" (NeurIPS 2023 Spotlight). Automated Circuit DisCovery (ACDC) is an attempt to formalize and automate the process of circuit discovery.

## What It Does

ACDC automates the process to identify the circuit that implements the specified behavior in the model's computational graph. Researchers apply activation patching to find which abstract neural network units are involved in the behavior.

## Key Results

The ACDC algorithm rediscovered 5/5 of the component types in a circuit in GPT-2 Small that computes the Greater-Than operation. ACDC selected 68 of the 32,000 edges in GPT-2 Small, all of which were manually found by previous work.

## Implementation

The code is available at https://github.com/ArthurConmy/Automatic-Circuit-Discovery.

## Recent Developments

This paper was published at NeurIPS 2023, and subsequent work has built upon it. For example, a novel Hybrid Attribution and Pruning (HAP) framework was proposed to enhance the scalability and maintain the faithfulness of discovered circuits, presented at NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b6930ba7-02a2-48ae-9100-df7a9e3c9dc5"
}
```

</details>

---


### System

_source line 131_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for Anthropic circuit tracing cross-layer transcoders…",
  "usage": {
    "total_tokens": 22098,
    "tool_uses": 12,
    "duration_ms": 31374
  },
  "last_tool_name": "WebSearch",
  "uuid": "eb44033e-cfd3-487d-91e2-4bd55c303352",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 132_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QCiroMzFHpetwsrwXR8XGN`</summary>

```json
{
  "query": "Anthropic circuit tracing cross-layer transcoders 2025 attribution graphs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8dbb5b8b-41dd-4882-bace-f1921dfc4f96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiUNT6hzJjtxG8bRvMQNjD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2956,
      "cache_read_input_tokens": 19114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2956,
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

_source line 133 · 2026-05-12T22:08:28.806Z_

<details><summary>↩ Tool result · `toolu_01PyeY9udtB3dnk1u6MBptrV`</summary>

```text
Web search results for query: "sparse autoencoders circuit discovery NeurIPS 2024 ICLR 2025 feature circuits"

Links: [{"title":"sparse feature circuits: discovering","url":"https://belinkov.com/assets/pdf/iclr2025-sfc.pdf"},{"title":"NeurIPS Poster Transcoders find interpretable LLM feature circuits","url":"https://neurips.cc/virtual/2024/poster/95736"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/1fa1ab11f4bd5f94b2ec20e794dbfa3b-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/42ef3308c230942d223c411adf182c88-Paper-Conference.pdf"},{"title":"Circuits Updates - July 2025","url":"https://transformer-circuits.pub/2025/july-update/index.html"},{"title":"Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | OpenReview","url":"https://openreview.net/forum?id=I4e82CIDxv"},{"title":"[PDF] Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sparse-Feature-Circuits:-Discovering-and-Editing-in-Marks-Rager/b8f280d8bf685f8da7c83068e73f000528072d6b"},{"title":"SCALING SPARSE AUTOENCODER CIRCUITS FOR IN","url":"https://openreview.net/pdf?id=Pa1vr1Prww"},{"title":"Sparse Autoencoders Find Highly Interpretable Features in Language Models | OpenReview","url":"https://openreview.net/forum?id=F76bwRSLeK"},{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=F76bwRSLeK"}]

Based on the search results, here's what I found regarding sparse autoencoders, circuit discovery, and recent conference work:

## Key Findings

**Sparse Feature Circuits (ICLR 2025):**
Sparse feature circuits are methods for discovering causally implicated subnetworks of human-interpretable features for explaining language model behaviors. These circuits enable detailed understanding of mechanisms in neural networks and can be used for downstream tasks like improving classifier generalization, with an entirely unsupervised and scalable interpretability pipeline discovering thousands of sparse feature circuits for automatically discovered model behaviors.

**Sparse Autoencoders Overview:**
Interpretability researchers have recently turned to sparse autoencoders (SAEs), an unsupervised technique for identifying a large number of interpretable neural network latents. SAEs are trained on an objective which promotes having small reconstruction error while using only a sparse set of feature activations.

**NeurIPS 2024 Work:**
A key goal in mechanistic interpretability is circuit analysis: finding sparse subgraphs of models corresponding to specific behaviors or capabilities. However, MLP sublayers make fine-grained circuit analysis on transformer-based language models difficult. Transcoders seek to faithfully approximate a densely activating MLP layer with a wider, sparsely-activating MLP layer, with a novel method for using transcoders to perform weights-based circuit analysis through MLP sublayers.

**Circuit Discovery Methodology:**
Sparse Feature Circuits are a methodology introduced by Marks et al. (2024) to identify and analyze causal subgraphs of sparse autoencoder features that explain specific model behaviors, combining the interpretability benefits of SAEs with causal analysis to uncover mechanisms underlying language model behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "54622e7b-18cb-440f-9ad5-21317ebb2197"
}
```

</details>

---


### Tool result

_source line 134 · 2026-05-12T22:08:28.810Z_

<details><summary>↩ Tool result · `toolu_015c1x5KTba1aDri8TNKc5Gs`</summary>

```text
# MIB: A Mechanistic Interpretability Benchmark

## Title, Authors, and Year
**Full Title:** "MIB: A Mechanistic Interpretability Benchmark"

**Authors:** Aaron Mueller, Atticus Geiger, Sarah Wiegreffe, Dana Arad, Iván Arcuschin, Adam Belfki, Yik Siu Chan, Jaden Fiotto-Kaufman, Tal Haklay, Michael Hanna, Jing Huang, Rohan Gupta, Yaniv Nikankin, Hadas Orgad, Nikhil Prakash, Anja Reusch, Aruna Sankaranarayanan, Shun Shao, Alessandro Stolfo, Martin Tutek, Amir Zur, David Bau, and Yonatan Belinkov

**Year:** 2025 (accepted to ICML 2025; submitted April 17, 2025)

## Abstract
The paper proposes MIB to establish evaluation standards for mechanistic interpretability methods. It features "two tracks spanning four tasks and five models," evaluating approaches that locate important model components or featurize hidden vectors.

## Circuit Discovery Methods Benchmarked
MIB evaluates circuit localization methods including "attribution patching," information flow techniques, and "mask optimization methods."

## Measurement of Method Agreement
The abstract emphasizes that MIB "favors methods that precisely and concisely recover relevant causal pathways," suggesting evaluation focuses on precision and efficiency rather than explicit inter-method agreement metrics.

## Key Performance Findings
- Attribution and mask optimization methods demonstrated superior performance in circuit localization tasks
- For causal variable localization, "supervised DAS method performs best"
- Notably, sparse autoencoders showed no advantage over basic neurons for featurization
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "f047b93a-f847-4eed-a87a-ca7e73f48370"
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-12T22:08:29.183Z_

<details><summary>↩ Tool result · `toolu_01ApTdV7LxZP7HH3vumidxav`</summary>

```text
Web search results for query: ""circuit discovery" OR "circuit finding" ICML 2024 transformers interpretability paper"

Links: [{"title":"[Quick Review] Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://liner.com/review/efficient-automated-circuit-discovery-in-transformers-using-contextual-decomposition"},{"title":"ICLR Poster Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://iclr.cc/virtual/2025/poster/31044"},{"title":"Transformer Circuits Thread","url":"https://transformer-circuits.pub/"},{"title":"Circuits Updates - July 2025","url":"https://transformer-circuits.pub/2025/july-update/index.html"},{"title":"Tutorials","url":"https://projects.illc.uva.nl/indeep/tutorial/"},{"title":"Transcoders find interpretable LLM feature circuits","url":"https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"},{"title":"GitHub - interpretingdl/eacl2024_transformer_interpretability_tutorial: Materials for EACL2024 tutorial: Transformer-specific Interpretability · GitHub","url":"https://github.com/interpretingdl/eacl2024_transformer_interpretability_tutorial"},{"title":"Transcoders find interpretable LLM feature circuits | OpenReview","url":"https://openreview.net/forum?id=J6zHcScAo0&noteId=aOaSSMtgfp"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/html/2407.00886v2"}]

Based on the search results, I found relevant papers on circuit discovery in transformers, though most are from venues other than ICML 2024. Here are the key findings:

## Circuit Discovery Papers (2024)

**Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition**

This ICLR 2024 paper introduces Contextual Decomposition for Transformers, an efficient automated circuit discovery method. CD-T reduces circuit discovery runtime from hours to seconds compared to state-of-the-art baselines, and demonstrates superior performance on three standard circuit evaluation datasets (indirect object identification, greater-than comparisons, and docstring completion), with an average of 97% ROC AUC.

**Transcoders find interpretable LLM feature circuits**

Published as a NeurIPS 2024 poster, this work focuses on circuit analysis by finding sparse subgraphs of models corresponding to specific behaviors or capabilities. The paper explores transcoders, which seek to faithfully approximate a densely activating MLP layer with a wider, sparsely-activating MLP layer, and introduces a novel method for using transcoders to perform weights-based circuit analysis through MLP sublayers.

## Related Circuit Discovery Work

Merullo et al. (ICLR 2024) published "Circuit Component Reuse Across Tasks in Transformer Language Models", and Gould et al. (ICLR 2024) published "Successor Heads: Recurring, Interpretable Attention Heads In The Wild".

I did not find a specific ICML 2024 circuit discovery paper in the search results, but these 2024 papers from ICLR and NeurIPS represent the latest work in transformer circuit discovery and interpretability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "454752a1-dc92-4847-b0e4-763bdc19436a"
}
```

</details>

---


### System

_source line 136_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for cross-method circuit stability scoring mechanisti…",
  "usage": {
    "total_tokens": 19173,
    "tool_uses": 5,
    "duration_ms": 37194
  },
  "last_tool_name": "WebSearch",
  "uuid": "5327defd-795d-4508-a0c6-a486a26c3755",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 137_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018ZSVQSTgAnQ7BfeaDc7MGj`</summary>

```json
{
  "query": "cross-method circuit stability scoring mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "96a07982-25fc-46d0-9ec7-1916a32d0efe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UtPnNgYjM77BAcku6fnuz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 908,
      "cache_read_input_tokens": 18074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 908,
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

_source line 138_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for \"Stream algorithm\" hierarchical pruning mechanist…",
  "usage": {
    "total_tokens": 22099,
    "tool_uses": 13,
    "duration_ms": 32474
  },
  "last_tool_name": "WebSearch",
  "uuid": "825064f9-4bd9-4b3b-b219-879e03c36ed5",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 139_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SfTEhoznmQrvLAgXe2jN2y`</summary>

```json
{
  "query": "\"Stream algorithm\" hierarchical pruning mechanistic interpretability attention 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "ec72369c-d136-4e09-b2cf-55a243b4195a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiUNT6hzJjtxG8bRvMQNjD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2956,
      "cache_read_input_tokens": 19114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2956,
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

_source line 140_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for circuit discovery NP-hard intractable ICLR 2025 m…",
  "usage": {
    "total_tokens": 22100,
    "tool_uses": 14,
    "duration_ms": 32611
  },
  "last_tool_name": "WebSearch",
  "uuid": "3f95dc42-0bdc-46eb-89b6-ef5d67ed5dba",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 141_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BE9snrYSFrvP95GzG5jQka`</summary>

```json
{
  "query": "circuit discovery NP-hard intractable ICLR 2025 mechanistic interpretability identifiable"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "739dda25-f159-456c-8a7d-40d94d04c0b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiUNT6hzJjtxG8bRvMQNjD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2956,
      "cache_read_input_tokens": 19114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2956,
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

_source line 142 · 2026-05-12T22:08:30.168Z_

<details><summary>↩ Tool result · `toolu_01NCgyndzqwHVcZpQHZECJMf`</summary>

```text
Web search results for query: ""Transcoders Find Interpretable LLM Feature Circuits" venue conference 2024 2025"

Links: [{"title":"NeurIPS Poster Transcoders find interpretable LLM feature circuits","url":"https://neurips.cc/virtual/2024/poster/95736"},{"title":"Transcoders find interpretable LLM feature circuits | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738684"},{"title":"Transcoders find interpretable LLM feature circuits","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/2b8f4db0464cc5b6e9d5e6bea4b9f308-Abstract-Conference.html"},{"title":"Transcoders find interpretable LLM feature circuits","url":"https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"},{"title":"[2406.11944] Transcoders Find Interpretable LLM Feature Circuits","url":"https://arxiv.org/abs/2406.11944"},{"title":"Transcoders find interpretable LLM feature circuits | OpenReview","url":"https://openreview.net/forum?id=J6zHcScAo0&noteId=aOaSSMtgfp"},{"title":"Transcoders Find Interpretable LLM Feature Circuits [Quick Review]","url":"https://liner.com/review/transcoders-find-interpretable-llm-feature-circuits"},{"title":"Transcoders find interpretable LLM feature circuits - proceedings.com","url":"https://www.proceedings.com/079017-0768.html"},{"title":"Transcoders Find Interpretable LLM Feature Circuits","url":"https://arxiv.org/html/2406.11944v1"},{"title":"Transcoders Find Interpretable LLM Feature Circuits Jacob Dunefsky∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2b8f4db0464cc5b6e9d5e6bea4b9f308-Paper-Conference.pdf"}]

Based on the search results, I can provide you with information about the paper "Transcoders Find Interpretable LLM Feature Circuits":

## Venue and Conference

The paper was published as a NeurIPS 2024 poster. More specifically, it is presented at the 38th International Conference on Neural Information Processing Systems (NeurIPS 2024).

## Key Details

The paper addresses an important problem in mechanistic interpretability: circuit analysis involves finding sparse subgraphs of models corresponding to specific behaviors or capabilities, but MLP sublayers make fine-grained circuit analysis on transformer-based language models difficult.

The authors' main contribution is exploring transcoders, which seek to faithfully approximate a densely activating MLP layer with a wider, sparsely-activating MLP layer, and introducing a novel method for using transcoders to perform weights-based circuit analysis through MLP sublayers.

The authors successfully train transcoders on language models with 120M, 410M, and 1.4B parameters, and find them to perform at least on par with SAEs in terms of sparsity, faithfulness, and human-interpretability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "fd6e3f2f-ae74-4a5b-a7b2-61f6e703676a"
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-12T22:08:31.234Z_

<details><summary>↩ Tool result · `toolu_01ML4GAb8Nbn4FjiNYwnupNy`</summary>

```text
Web search results for query: ""circuit discovery" methods disagree inconsistent different circuits same task transformer"

Links: [{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition | OpenReview","url":"https://openreview.net/forum?id=41HlN8XYM5"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/html/2407.00886v2"},{"title":"Same Task, Different Circuits: Disentangling Modality-Specific Mechanisms in VLMs","url":"https://arxiv.org/html/2506.09047v2"},{"title":"Towards Interpretable Sequence Continuation: Analyzing Shared Circuits in Large Language Models","url":"https://arxiv.org/html/2311.04131v6"},{"title":"[Quick Review] Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://liner.com/review/efficient-automated-circuit-discovery-in-transformers-using-contextual-decomposition"},{"title":"GitHub - adelaidehsu/CD_Circuit: [ICLR 2025] CD-T: Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition. Paper: https://arxiv.org/abs/2407.00886","url":"https://github.com/adelaidehsu/CD_Circuit"},{"title":"Circuit Component Reuse Across Tasks in Transformer Language Models","url":"https://arxiv.org/html/2310.08744v2"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"CIRCUIT COMPONENT REUSE ACROSS TASKS IN ...","url":"https://health-nlp.com/files/pubs/iclr24a.pdf"},{"title":"[PDF] Towards Automated Circuit Discovery for Mechanistic Interpretability | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Towards-Automated-Circuit-Discovery-for-Mechanistic-Conmy-Mavor-Parker/eefbd8b384a58f464827b19e30a6920ba976def9"}]

Based on the search results, I found relevant information about circuit discovery methods and their relationship to finding circuits for the same task in transformers.

## Key Findings

The search results reveal important insights about circuit discovery inconsistencies:

**Different Methods, Similar Tasks:**

Different automated circuit discovery methods (CD-T, ACDC, and EAP) are compared on standard circuit evaluation datasets including indirect object identification, greater-than comparisons, and docstring completion, with CD-T outperforming baselines by better identifying attention heads in manual circuits with an average of 97% ROC AUC.

**Task Granularity Variations:**

The optimal granularity for circuits varies by task; for the IOI task, fine-grained attention heads at specific sequence positions yielded the best faithfulness, while for Greater-than and Docstring tasks, coarse-level attention heads were sufficient.

**Limitations of Automated Methods:**

While automated circuit discovery methods like CD-T and EAP both outperform random baselines, manual circuits of the same size still exhibit higher faithfulness, suggesting that advanced automated techniques have not yet fully captured the intricate relationships identified through human expert analysis.

**Separate Circuits for Same Functionality:**

Interestingly, research on vision-language models discovered that even models trained simultaneously on both modalities develop separate circuits for each, and despite being separate, the circuits are functionally equivalent for the most part when processing query tokens and generating answers.

These findings suggest that different circuit discovery methods can yield varying results, and the granularity of discovered circuits may depend significantly on the task and methodology used.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "63ee423a-d60c-40aa-82ea-dbe8da427744"
}
```

</details>

---


### Tool result

_source line 144 · 2026-05-12T22:08:31.298Z_

<details><summary>↩ Tool result · `toolu_01LAPc9G7t3wT7UPMGNqS2Qk`</summary>

```text
Web search results for query: "edge pruning ACDC EAP attribution patching circuits overlap agreement 2024 2025"

Links: [{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://aclanthology.org/2024.blackboxnlp-1.25.pdf"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://www.arxiv.org/pdf/2510.03282"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery Aaquib Syed","url":"https://openreview.net/pdf?id=tiLbFR4bJW"},{"title":"Finding Transformer Circuits with Edge Pruning Adithya Bhaskar Alexander Wettig","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/20fdaf67581e6d7157376d1ed584040a-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025 EFFICIENT AUTOMATED CIRCUIT","url":"https://arxiv.org/pdf/2407.00886"},{"title":"Transformer Circuits via Edge Pruning","url":"https://www.emergentmind.com/papers/2406.16778"},{"title":"[2403.17806] Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms","url":"https://arxiv.org/abs/2403.17806"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework | OpenReview","url":"https://openreview.net/forum?id=hhD5MjHtLi"},{"title":"Researchers at Princeton University Proposes Edge Pruning: An Effective and Scalable Method for Automated Circuit Finding - MarkTechPost","url":"https://www.marktechpost.com/2024/07/02/researchers-at-princeton-university-proposes-edge-pruning-an-effective-and-scalable-method-for-automated-circuit-finding/"},{"title":"Finding Transformer Circuits with Edge Pruning","url":"https://www.cl.cam.ac.uk/teaching/2425/L193/files/pres4-joseph.pdf"}]

I found several research papers and resources related to edge pruning, ACDC, EAP, and circuit discovery in transformer models. Here's what the search revealed:

## Key Methods and Comparisons

Existing circuit discovery algorithms face a fundamental trade-off: attribution patching is fast but unfaithful to the full model, while edge pruning is faithful but computationally expensive.

### Edge Attribution Patching (EAP)
EAP uses a first-order Taylor series approximation to ablate all edges simultaneously. Although faster than ACDC, the first-order approximations show low faithfulness to the full model.

### ACDC (Automated Circuit Discovery with Causal Intervention)
ACDC's greedy search approach is computationally expensive and doesn't scale well to large datasets or billion-parameter models.

### Edge Pruning
Edge Pruning outperforms prior methods on more complex tasks. It is considerably more faithful on IOI and GT than both ACDC and EAP, especially at higher sparsities. Edge Pruning scales effectively to 100K examples, where it is the fastest and most faithful method.

## Recent Hybrid Approach (2025)

A hybrid attribution and pruning (HAP) framework has been developed that uses attribution patching to identify a high-potential subgraph, then applies edge pruning to extract a faithful circuit from it.

## Faithfulness vs. Overlap

Circuits found using EAP are less faithful than those found using EAP-IG, even though both have high node overlap with circuits found previously using causal interventions. Faithfulness, not overlap, is what should be measured when comparing the mechanisms models use to solve tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "3938d6b7-ba4d-42d4-8ed9-bf44e1551602"
}
```

</details>

---


### System

_source line 145_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"circuit component reuse\" Merullo ICLR 2024 trans…",
  "usage": {
    "total_tokens": 24490,
    "tool_uses": 11,
    "duration_ms": 32778
  },
  "last_tool_name": "WebSearch",
  "uuid": "0e85795e-d94d-4449-b3cb-2da3ef1cda19",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 146_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013hn84XJWV1GznGEAv5HtJk`</summary>

```json
{
  "query": "\"circuit component reuse\" Merullo ICLR 2024 transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "95733ac2-bd30-47f4-8843-ccfbd52f7ff5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cn2acUEEk6ag2tUaLzUPN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3897,
      "cache_read_input_tokens": 20565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3897,
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

_source line 147_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"computational complexity circuit discovery\" ICLR…",
  "usage": {
    "total_tokens": 24491,
    "tool_uses": 12,
    "duration_ms": 33303
  },
  "last_tool_name": "WebSearch",
  "uuid": "fe853260-ab33-4a17-80d2-682aff75400e",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 148_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ALkxqf4HFTyYo7sJ5vy1Zc`</summary>

```json
{
  "query": "\"computational complexity circuit discovery\" ICLR 2025 interpretability NP-hard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b4b4525e-046a-4e04-b784-430172a11559",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cn2acUEEk6ag2tUaLzUPN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3897,
      "cache_read_input_tokens": 20565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3897,
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

_source line 149_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"Sparse Autoencoders Find Highly Interpretable Fe…",
  "usage": {
    "total_tokens": 24492,
    "tool_uses": 13,
    "duration_ms": 33848
  },
  "last_tool_name": "WebSearch",
  "uuid": "c446d53a-cf8a-458b-ba89-2b99a6af19a8",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 150_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UCLZkNXubXG46ZgahNGdNJ`</summary>

```json
{
  "query": "\"Sparse Autoencoders Find Highly Interpretable Features\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "fbd76ba4-385c-4196-b34d-7ac503543635",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cn2acUEEk6ag2tUaLzUPN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3897,
      "cache_read_input_tokens": 20565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3897,
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

_source line 151 · 2026-05-12T22:08:35.524Z_

<details><summary>↩ Tool result · `toolu_01WjakV8dGVAkJLZprN1x2Ri`</summary>

```text
Web search results for query: "GIM gradient interaction modifications mechanistic interpretability Corti circuit discovery"

Links: [{"title":"Corti introduces GIM: Benchmark-leading method for understanding AI model behavior | Corti","url":"https://www.corti.ai/stories/gim-a-new-standard-for-mechanistic-interpretability"},{"title":"GIM: Improved Interpretability for Large Language Models","url":"https://arxiv.org/html/2505.17630"},{"title":"GIM: Improved Interpretability for Large Language Models Joakim Edin1,3","url":"https://arxiv.org/pdf/2505.17630v3"},{"title":"Decompose the model: mechanistic interpretability in image models with generalized integrated gradients (GIG)","url":"https://arxiv.org/html/2409.01610v1"},{"title":"[2505.17630v3] GIM: Improved Interpretability for Large Language Models","url":"https://arxiv.org/abs/2505.17630v3"},{"title":"GitHub - JoakimEdin/gim · GitHub","url":"https://github.com/JoakimEdin/gim"},{"title":"Corti Unlocks \"Surgical\" AI Improvement, Outperforming Big Tech in Interpretability Benchmark","url":"https://finance.yahoo.com/news/corti-unlocks-surgical-ai-improvement-211200700.html"},{"title":"GIM: Improved Interpretability for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=ZRDYvWF1ZJ"},{"title":"[2505.17630] GIM: Improved Interpretability for Large Language Models","url":"https://arxiv.org/abs/2505.17630"},{"title":"Decompose the model: mechanistic interpretability in image models with generalized integrated gradients (GIG) | OpenReview","url":"https://openreview.net/forum?id=avlfmW32qO"}]

Based on the search results, here's what I found about GIM (Gradient Interaction Modifications), mechanistic interpretability, and circuit discovery:

## Overview

GIM (Gradient Interaction Modifications) is a method for revealing which parts of a model are responsible for specific behaviors, developed as a gradient-based method that achieves the highest known accuracy for identifying which components in a model are responsible for specific behaviors.

## Key Accomplishments

GIM has topped the Hugging Face Mechanistic Interpretability Benchmark, demonstrating both superior accuracy and production-scale speed, and is the first interpretability method to top the industry benchmark while remaining fast enough for production-scale models.

## Technical Approach

GIM is a novel gradient-based attribution method specifically designed to account for self-repair effects in language models, introducing targeted modifications to backpropagation to better handle interactions that cause self-repair. 

The method develops temperature-adjusted softmax gradients to address the attention self-repair problem, implements layernorm freeze to deal with layer normalization self-repair, and incorporates gradient normalization which was found essential for making the backpropagation modifications effective.

## The Self-Repair Problem

Self-repair is a phenomenon where networks compensate for reduced signal in one component by amplifying others, masking the true importance of the ablated component. A novel form occurs within the attention mechanism where softmax redistribution conceals the influence of important attention scores, leading traditional ablation and gradient-based methods to underestimate the significance of all components contributing to these attention scores.

## Circuit Discovery

Circuit discovery, the foundation upon which GIM was built, identifies the specific neurons and connections that contribute to particular behaviors. GIM can now identify the circuits behind specific model behaviors faster, cheaper, and more accurately than any other available method.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "1bd1b082-e135-4d12-a7cf-d57815fcf312"
}
```

</details>

---


### System

_source line 152_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/abs/2403.17806",
  "usage": {
    "total_tokens": 25946,
    "tool_uses": 15,
    "duration_ms": 48503
  },
  "last_tool_name": "WebFetch",
  "uuid": "34538905-401b-4cf3-86ba-1e18c4aba3c0",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 153_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018rbqg423UTpV9F5ai8Bdbs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2403.17806",
  "prompt": "Extract the full title, authors, year, abstract, and key findings. This paper is about going beyond circuit overlap - does it directly measure agreement between different circuit discovery methods? What does it find about overlap vs faithfulness?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "0f9f1173-1e96-476f-89f9-acd672ccae8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPGaMo9LX4N59xkuwcUpPa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 22976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2917,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 154_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for ICML 2025 \"mechanistic interpretability\" circuit …",
  "usage": {
    "total_tokens": 24493,
    "tool_uses": 14,
    "duration_ms": 34626
  },
  "last_tool_name": "WebSearch",
  "uuid": "059ce39f-5367-4e64-b7a1-c6ce5eae2847",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 155_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BzjpcdGe3nemcSUXStUkzy`</summary>

```json
{
  "query": "ICML 2025 \"mechanistic interpretability\" circuit accepted paper poster spotlight"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "bf7838e1-1c63-49ee-bf32-e88c665c6806",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cn2acUEEk6ag2tUaLzUPN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3897,
      "cache_read_input_tokens": 20565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3897,
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

_source line 156 · 2026-05-12T22:08:36.069Z_

<details><summary>↩ Tool result · `toolu_01QCiroMzFHpetwsrwXR8XGN`</summary>

```text
Web search results for query: "Anthropic circuit tracing cross-layer transcoders 2025 attribution graphs"

Links: [{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"On the Biology of a Large Language Model","url":"https://transformer-circuits.pub/2025/attribution-graphs/biology.html"},{"title":"Anthropic Open-Sources Tool to Trace the \"Thoughts\" of Large Language Models - InfoQ","url":"https://www.infoq.com/news/2025/06/anthropic-circuit-tracing/"},{"title":"Circuit Tracing: A Step Closer to Understanding Large Language Models | Towards Data Science","url":"https://towardsdatascience.com/circuit-tracing-a-step-closer-to-understanding-large-language-models/"},{"title":"Anthropic drops an amazing report on LLM interpretability | by Lee Fischman | Medium","url":"https://medium.com/@lee.fischman/anthropic-drops-an-amazing-report-on-llm-interpretability-d3fbcd5ba762"},{"title":"The Circuits Research Landscape: Results and Perspectives - August 2025 ｜ Neuronpedia","url":"https://www.neuronpedia.org/graph/info"},{"title":"Open-sourcing circuit-tracing tools","url":"https://www.anthropic.com/research/open-source-circuit-tracing"},{"title":"Replicating Circuit Tracing for a Simple Known Mechanism","url":"https://www.goodfire.ai/research/replicating-circuit-tracing-for-a-simple-mechanism"},{"title":"Tracing Attention Computation Through Feature Interactions","url":"https://transformer-circuits.pub/2025/attention-qk/index.html"},{"title":"How Anthropic’s Open-Source Circuit Tracing is Revolutionizing LLM Interpretability | by Milan's Outlook | Medium","url":"https://medium.com/@itsmybestview/how-anthropics-open-source-circuit-tracing-is-revolutionizing-llm-interpretability-f372b1e67d91"}]

I found comprehensive information about Anthropic's circuit tracing research involving cross-layer transcoders and attribution graphs from 2025. Here are the key findings:

## Overview

Anthropic produces graph descriptions of model computation by tracing individual computational steps in a "replacement model," which substitutes a more interpretable component (a "cross-layer transcoder") for parts of the underlying model (the multi-layer perceptrons) that it is trained to approximate.

## Attribution Graphs

Attribution graphs describe the steps a model used to produce an output for a target token on a particular prompt, with nodes representing active features, token embeddings from the prompt, reconstruction errors, and output logits, while edges represent linear effects between nodes.

## Cross-Layer Transcoders

Cross-layer transcoders are based on features that read from the residual stream at one layer and contribute to the outputs of all subsequent MLP layers of the original model, which greatly simplifies the resulting circuits. Remarkably, the team can substitute their learned CLT features for the model's MLPs while matching the underlying model's outputs in approximately 50% of cases.

## Applications

The research focuses on applying attribution graphs to study Claude 3.5 Haiku, released in October 2024, which serves as Anthropic's lightweight production model. Anthropic researchers have open-sourced the tool they used to trace what goes on inside a large language model during inference, including a circuit tracing Python library that can be used with any open-weights model and a frontend hosted on Neuropedia to explore the library output through a graph.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e07e18aa-fb25-42d3-87f2-70e277def19f"
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-12T22:08:37.374Z_

<details><summary>↩ Tool result · `toolu_01SfTEhoznmQrvLAgXe2jN2y`</summary>

```text
Web search results for query: ""Stream algorithm" hierarchical pruning mechanistic interpretability attention 2025"

Links: [{"title":"[2510.19875] Stream: Scaling up Mechanistic Interpretability to Long Context in LLMs via Sparse Attention","url":"https://arxiv.org/abs/2510.19875"},{"title":"Stream: Scaling up Mechanistic Interpretability to Long Context in LLMs via Sparse Attention | OpenReview","url":"https://openreview.net/forum?id=5HGu0ZqBl9"},{"title":"Stream: Scaling up Mechanistic Interpretability to Long Context in LLMs via Sparse Attention","url":"https://arxiv.org/html/2510.19875v1"},{"title":"Stream: Scaling up Mechanistic Interpretability to","url":"https://openreview.net/pdf/f603971c3ecdf5c4fedd2a41750175ef937c33fb.pdf"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Sparse Attention Post-Training for Mechanistic Interpretability","url":"https://arxiv.org/html/2512.05865v1"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025","url":"https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"},{"title":"Unboxing the Black Box: Mechanistic Interpretability for Algorithmic Understanding of Neural Networks","url":"https://arxiv.org/html/2511.19265v1"},{"title":"Artificial Intelligence Feb 2025","url":"https://arxiv.org/list/cs.AI/2025-02?skip=2250&show=2000"}]

Based on the search results, I found relevant information about Stream and related work on hierarchical pruning, mechanistic interpretability, and attention in 2025.

## Stream Algorithm Overview

Stream is a compilable hierarchical pruning algorithm that estimates per-head sparse attention masks in near-linear time O(T log T) and linear space O(T), enabling one-pass interpretability at scale.

## Purpose and Problem It Solves

As Large Language Models (LLMs) scale to million-token contexts, traditional Mechanistic Interpretability techniques for analyzing attention scale quadratically with context length, demanding terabytes of memory beyond 100,000 tokens. Stream addresses this challenge through sparse attention techniques.

## How Stream Works

Stream performs a binary-search-style refinement to retain only the top-k key blocks per query while preserving the model's next-token behavior. By tuning block size and k, practitioners can finely control the resolution (e.g. sentence level vs paragraph level) and amount of pruning.

## Performance and Results

Stream is applied to long chain-of-thought reasoning traces and identifies thought anchors while pruning 97-99% of token interactions. On the RULER needle-in-a-haystack benchmark, Stream preserves the critical retrieval paths while discarding 90-96% of interactions and exposes layer-wise routes from the needle to output.

## Practical Impact

Stream offers a practical drop-in tool for analyzing attention patterns, computing salience scores, and tracing information flow without terabytes of caches. By making long-context interpretability feasible on consumer GPUs, Sparse Tracing helps democratize chain-of-thought monitoring.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "3c29b377-e362-429c-8764-b0d3b137fa8f"
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
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/abs/2406.16778",
  "usage": {
    "total_tokens": 25949,
    "tool_uses": 16,
    "duration_ms": 50409
  },
  "last_tool_name": "WebFetch",
  "uuid": "b4cbe8e4-4419-44ca-9f2f-e308c8cb42c1",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 159_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017DW7fcdJ9Vc5LEyMCYBtpE`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.16778",
  "prompt": "Extract the full title, authors, year, abstract, and key findings. This is the Edge Pruning paper - what methods does it compare against (ACDC, EAP, etc.)? What does it find about the circuits found by different methods - do they agree?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "122fbeb1-4d5c-4276-a760-9c512d9993e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPGaMo9LX4N59xkuwcUpPa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 22976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2917,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 160 · 2026-05-12T22:08:37.813Z_

<details><summary>↩ Tool result · `toolu_01BE9snrYSFrvP95GzG5jQka`</summary>

```text
Web search results for query: "circuit discovery NP-hard intractable ICLR 2025 mechanistic interpretability identifiable"

Links: [{"title":"Open problems in mechanistic interpretability: 2026 status report","url":"https://gist.github.com/bigsnarfdude/629f19f635981999c51a8bd44c6e2a54"},{"title":"The Computational Complexity of Circuit Discovery for Inner Interpretability | OpenReview","url":"https://openreview.net/forum?id=QogcGNXJVw"},{"title":"ICLR Poster The Computational Complexity of Circuit Discovery for Inner Interpretability","url":"https://iclr.cc/virtual/2025/poster/29673"},{"title":"Published as a conference paper at ICLR 2025 THE COMPUTATIONAL COMPLEXITY OF","url":"https://openreview.net/pdf?id=QogcGNXJVw"},{"title":"ICLR.2025 - Spotlight | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2025?group=Spotlight"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2502.20914"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=FbZSZEIkEU"},{"title":"ICLR Poster Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://iclr.cc/virtual/2025/poster/31044"},{"title":"Published as a conference paper at ICLR 2025 EFFICIENT AUTOMATED CIRCUIT","url":"https://arxiv.org/pdf/2407.00886"}]

Based on the search results, I found highly relevant information about circuit discovery complexity from ICLR 2025:

## Key Findings

A 2025 ICLR paper proved many circuit-finding queries are NP-hard, remain fixed-parameter intractable, and are inapproximable under standard computational assumptions.

Many queries are intractable (NP-hard, Σ²ₚ-hard), remain fixed-parameter intractable (W[1]-hard) when constraining model/circuit features (e.g., depth), and are inapproximable under additive, multiplicative, and probabilistic approximation schemes.

## Implications for Mechanistic Interpretability

Circuit discovery—identifying the minimal computational subgraphs responsible for specific behaviors—faces fundamental complexity barriers. 

The paper frames circuit discovery queries "in terms of affordances for description, explanation, prediction and control" and proves there exist transformations to tackle some of these hard problems with better-understood heuristics, and prove the tractability or fixed-parameter tractability of more modest queries which retain useful affordances.

Core concepts like "feature" lack rigorous definitions, computational complexity results prove many interpretability queries are intractable, and practical methods still underperform simple baselines on safety-relevant tasks.

The paper was published at ICLR 2025 as a Spotlight presentation and provides a formal computational complexity framework for understanding both the limits and viable approaches to circuit discovery in mechanistic interpretability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "67041094-7d64-4a1c-80b9-04441adf3501"
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-12T22:08:38.071Z_

<details><summary>↩ Tool result · `toolu_018ZSVQSTgAnQ7BfeaDc7MGj`</summary>

```text
Web search results for query: "cross-method circuit stability scoring mechanistic interpretability"

Links: [{"title":"Certified Circuits: Stability Guarantees for Mechanistic Circuits","url":"https://arxiv.org/html/2602.22968"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG","url":"https://arxiv.org/html/2510.00845v2"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis","url":"https://arxiv.org/html/2510.00845"},{"title":"MECHANISTIC INTERPRETABILITY AS STATISTICAL ESTIMATION:","url":"https://www.arxiv.org/pdf/2510.00845"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"Mechanistic Interpretability of Diffusion Models: Circuit-Level Analysis and Causal Validation","url":"https://arxiv.org/html/2506.17237v1"},{"title":"Circuit Stability Characterizes Language Model Generalization","url":"https://arxiv.org/html/2505.24731"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"}]

Based on the web search results, here are the key findings related to cross-method circuit stability scoring in mechanistic interpretability:

## Overview of Circuit Stability Research

Circuit discovery has a measurement problem: different analyst choices yield different circuits, with no principled way to separate robust structure from threshold-sensitive artifacts.

## Key Approaches to Measuring Stability

**CIRCUS Framework**: CIRCUS addresses this by computing empirical inclusion frequencies over a configuration family, turning analyst-choice variability into a diagnostic. The resulting core/contingent/noise taxonomy makes analyst disagreement actionable, and demonstrates that ideas from probabilistic model selection transfer naturally to mechanistic interpretability.

**Statistical Estimation Perspective**: The scientific validity of mechanistic interpretability findings depends on their stability. Circuit discovery is not a standalone task but a statistical estimation problem. Circuits are often reported without quantification of their statistical stability, robustness to perturbations, and uncertainty estimates.

**Certified Circuits**: Certified Circuits is a framework providing provable stability guarantees for circuit discovery. By combining deletion-based randomized smoothing with per-neuron abstention, the method certifies that circuits remain unchanged under bounded dataset edits.

## Cross-Method Stability Analysis

Varying multiple circuit finding parameters at once (resampling strategy, aggregation method, type of intervention, EAP method, and pruning strategy) yields many different circuits. The MDS projection of the pairwise Jaccard index matrix shows that none of the tested EAP methods consistently yields circuits with lower variance.

These research directions collectively address the critical challenge of establishing reliability and reproducibility in mechanistic interpretability findings through rigorous stability assessment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e1911b52-9306-489d-970b-42671721006d"
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
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for \"cross-method\" OR \"method agreement\" OR \"consensu…",
  "usage": {
    "total_tokens": 25952,
    "tool_uses": 17,
    "duration_ms": 51048
  },
  "last_tool_name": "WebSearch",
  "uuid": "9cdbaf0a-8f54-40bd-b88f-b85558705738",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 163_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AaYuioktKPPi44CynoZCf1`</summary>

```json
{
  "query": "\"cross-method\" OR \"method agreement\" OR \"consensus\" circuit discovery interpretability neural network"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "3ffccddf-f120-49e6-ae01-50c291f6731e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPGaMo9LX4N59xkuwcUpPa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 22976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2917,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 164_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for subnetwork probing circuit discovery comparison a…",
  "usage": {
    "total_tokens": 25955,
    "tool_uses": 18,
    "duration_ms": 51101
  },
  "last_tool_name": "WebSearch",
  "uuid": "c9dd149b-5564-40da-94c5-a0fc7e18995a",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 165_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KihcBDejfR6mqxFDQSm9re`</summary>

```json
{
  "query": "subnetwork probing circuit discovery comparison activation patching edge attribution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b1163ca8-59da-45cf-adfc-860e6f5df744",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPGaMo9LX4N59xkuwcUpPa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 22976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2917,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 166_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for circuit discovery robustness ensemble neural netw…",
  "usage": {
    "total_tokens": 20095,
    "tool_uses": 6,
    "duration_ms": 48207
  },
  "last_tool_name": "WebSearch",
  "uuid": "fa8f6cb4-1464-40d9-8047-9b7713453b42",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 167_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A48jG7tNehtHBnYbnR9wQk`</summary>

```json
{
  "query": "circuit discovery robustness ensemble neural network interpretability 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8d735bf6-1cf5-4849-9cfc-4adb82abf724",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017WfkSrXvDdxF19481Yvwzv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 18982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 877,
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

_source line 168 · 2026-05-12T22:08:40.451Z_

<details><summary>↩ Tool result · `toolu_013hn84XJWV1GznGEAv5HtJk`</summary>

```text
Web search results for query: ""circuit component reuse" Merullo ICLR 2024 transformer"

Links: [{"title":"[2310.08744] Circuit Component Reuse Across Tasks in Transformer Language Models","url":"https://arxiv.org/abs/2310.08744"},{"title":"CIRCUIT COMPONENT REUSE ACROSS TASKS IN ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/4ffbfbcf4ad7304d57158b046525e46c-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2024","url":"https://arxiv.org/pdf/2310.08744"},{"title":"Circuit Component Reuse Across Tasks in Transformer Language Models | OpenReview","url":"https://openreview.net/forum?id=fpoAYV6Wsk"},{"title":"Circuit Component Reuse Across Tasks in Transformer Language Models","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/4ffbfbcf4ad7304d57158b046525e46c-Abstract-Conference.html"},{"title":"[PDF] Circuit Component Reuse Across Tasks in Transformer Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/c0d9a48547d728dd320b453b01a0ab1ce2f96098"},{"title":"GitHub - jmerullo/circuit_reuse","url":"https://github.com/jmerullo/circuit_reuse"},{"title":"Tutorials","url":"https://projects.illc.uva.nl/indeep/tutorial/"},{"title":"Circuit Compositions: Exploring Modular Structures in Transformer-Based Language Models","url":"https://arxiv.org/html/2410.01434v3"},{"title":"Published at Building Trust Workshop at ICLR 2025","url":"https://openreview.net/pdf/f1ec1ce1656041d53e9acd23bfd9ea21fee487be.pdf"}]

I found the paper you're looking for! Here's what I discovered:

The paper "Circuit Component Reuse Across Tasks in Transformer Language Models" by Jack Merullo, Carsten Eickhoff, and Ellie Pavlick was published at ICLR 2024.

The core findings of the research are:

A common criticism of circuit analysis is that each circuit is task-specific and cannot contribute to understanding models at a higher level, but this work presents evidence that insights can indeed generalize across tasks.

Specifically, the researchers studied the circuit discovered for the Indirect Object Identification (IOI) task, showed that it reproduces on a larger GPT2 model, and found that it is mostly reused to solve a seemingly different task: Colored Objects.

The researchers provide evidence that the process underlying both tasks is functionally very similar, and contains about a 78% overlap in in-circuit attention heads.

You can find the paper at the official ICLR proceedings or on arXiv (2310.08744), with a GitHub repository available at https://github.com/jmerullo/circuit_reuse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "ec7206ec-4d17-431d-9992-3c42ba812111"
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-12T22:08:40.691Z_

<details><summary>↩ Tool result · `toolu_01ALkxqf4HFTyYo7sJ5vy1Zc`</summary>

```text
Web search results for query: ""computational complexity circuit discovery" ICLR 2025 interpretability NP-hard"

Links: [{"title":"The Computational Complexity of Circuit Discovery for Inner Interpretability | OpenReview","url":"https://openreview.net/forum?id=QogcGNXJVw"},{"title":"ICLR Poster The Computational Complexity of Circuit Discovery for Inner Interpretability","url":"https://iclr.cc/virtual/2025/poster/29673"},{"title":"Published as a conference paper at ICLR 2025 THE COMPUTATIONAL COMPLEXITY OF","url":"https://openreview.net/pdf?id=QogcGNXJVw"},{"title":"Published as a conference paper at ICLR 2025 THE COMPUTATIONAL COMPLEXITY OF","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/1e45dc45f1649f880130169b2271129e-Paper-Conference.pdf"},{"title":"ICLR.2025 - Spotlight | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2025?group=Spotlight"},{"title":"The Computational Complexity of Circuit Discovery for Inner Interpretability","url":"https://arxiv.org/html/2410.08025v1"},{"title":"[2410.08025v3] The Computational Complexity of Circuit Discovery for Inner Interpretability","url":"https://arxiv.org/abs/2410.08025v3"},{"title":"[2410.08025] The Computational Complexity of Circuit Discovery for Inner Interpretability","url":"https://arxiv.org/abs/2410.08025"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2502.20914"},{"title":"Lesswrong","url":"https://www.lesswrong.com/posts/roL7BchNM75ew5ntG/the-computational-complexity-of-circuit-discovery-for-inner"}]

Based on the search results, I found a relevant paper published at ICLR 2025:

## "The Computational Complexity of Circuit Discovery for Inner Interpretability"

This paper was published at ICLR 2025 as a Spotlight presentation. The work applies computational complexity theory to understand the hardness of circuit discovery problems in neural network interpretability.

### Key Findings

Many circuit discovery queries are intractable (NP-hard, Σ²_p-hard), remain fixed-parameter intractable (W[1]-hard) when constraining model/circuit features like depth, and are inapproximable under additive, multiplicative, and probabilistic approximation schemes.

Notably, many variants of sufficient circuit problems are NP-hard, and counterintuitively, this intractability does not depend straightforwardly on parameters such as network depth, meaning hardness is not mitigated by keeping models shallow.

### Research Approach

The paper describes a conceptual scaffolding to reason about circuit finding queries in terms of affordances for description, explanation, prediction and control; formalizes a comprehensive set of queries for mechanistic explanation; and uses a formal framework to settle the complexity of many query variants and relaxations of practical interest.

### Implications

The researchers proved there exist transformations to tackle some of these hard problems with better-understood heuristics, and proved the tractability or fixed-parameter tractability of more modest queries which retain useful affordances, allowing understanding of the scope and limits of interpretability queries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8ac80041-7ff4-4c3e-8dcb-85330a0655b3"
}
```

</details>

---


### Tool result

_source line 170 · 2026-05-12T22:08:41.201Z_

<details><summary>↩ Tool result · `toolu_018rbqg423UTpV9F5ai8Bdbs`</summary>

```text
# Paper Summary

**Full Title:** "Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms"

**Authors:** Michael Hanna, Sandro Pezzelle, Yonatan Belinkov

**Year:** 2024 (submitted March 26, 2024; revised July 15, 2024)

**Abstract:** The researchers address circuit discovery in language models, proposing that "faithfulness" rather than "overlap" should be the primary measurement when comparing circuit-finding methods. They introduce EAP-IG (Edge Attribution Patching with Integrated Gradients) as an improvement over standard EAP for maintaining circuit faithfulness.

## Key Findings

**On Overlap vs. Faithfulness:**

The paper does not directly measure agreement between multiple circuit discovery methods. Rather, it compares circuits found via different techniques (EAP versus EAP-IG) against a causal intervention baseline. 

The critical finding: "circuits found using EAP are less faithful than those found using EAP-IG, even though both have high node overlap" with causal intervention circuits. This demonstrates a key disconnect—two methods can produce highly similar circuits that nonetheless differ substantially in faithfulness (whether edges outside the circuit can be removed without affecting performance).

The authors argue this reveals an important methodological principle: overlap with prior results provides a misleading sense of validity. True circuit evaluation requires measuring faithfulness—the core property that justifies circuit analysis over studying full models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "d6f519f7-9a1e-4c92-9b47-724325816356"
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-12T22:08:41.287Z_

<details><summary>↩ Tool result · `toolu_01BzjpcdGe3nemcSUXStUkzy`</summary>

```text
Web search results for query: "ICML 2025 "mechanistic interpretability" circuit accepted paper poster spotlight"

Links: [{"title":"ICML Poster MIB: A Mechanistic Interpretability Benchmark","url":"https://icml.cc/virtual/2025/poster/43836"},{"title":"General Information | Workshop on Actionable Interpretability@ICML 2025","url":"https://actionable-interpretability.github.io/"},{"title":"ICML Poster Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models","url":"https://icml.cc/virtual/2025/poster/44616"},{"title":"Call for Papers | Mechanistic Interpretability Workshop at ICML 2026","url":"https://mechinterpworkshop.com/cfp/"},{"title":"ICML 2024 Mechanistic Interpretability Workshop","url":"https://icml2024mi.pages.dev/"},{"title":"ICML MIB: A Mechanistic Interpretability Benchmark","url":"https://icml.cc/virtual/2025/49583"},{"title":"MIB: A Mechanistic Interpretability Benchmark | OpenReview","url":"https://openreview.net/forum?id=sSrOwve6vb"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis","url":"https://arxiv.org/html/2510.00845"},{"title":"Mechanistic Interpretability Workshop at ICML 2026","url":"https://mechinterpworkshop.com/"}]

Based on the search results, I found several ICML 2025 papers related to mechanistic interpretability and circuits:

1. **MIB: A Mechanistic Interpretability Benchmark** - This paper proposes MIB, a large-scale dataset for evaluating and comparing mechanistic interpretability methods. It was published on May 1, 2025 as an ICML 2025 poster.

2. **Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models** - This work establishes five criteria for characterizing the MC vocabulary and presents ModCirc, a novel global-level mechanistic interpretability framework for discovering MC vocabularies in LLMs. This also appears to be an ICML 2025 poster that demonstrates ModCirc's effectiveness in identifying modular circuits.

Both papers appear to be poster presentations at ICML 2025. The search results show these are recent mechanistic interpretability papers focused on circuit analysis and localization methods. If you're looking for information about specific spotlight presentations or other particular papers, please let me know and I can search for more details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b35377dc-e921-40ba-8e87-99a9b731a393"
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
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://arxiv.org/abs/2505.17630",
  "usage": {
    "total_tokens": 25991,
    "tool_uses": 15,
    "duration_ms": 44633
  },
  "last_tool_name": "WebFetch",
  "uuid": "ecfbfc4f-7b9d-40c2-a6e2-636ab64f7728",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 173_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011oqRGQN5TVgHMm2HCdEViY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.17630",
  "prompt": "Extract: paper title, full author list, year, venue, and the complete abstract for the GIM paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b70e60d1-7e86-4ebb-b0d4-e1df2e063761",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7em4AmBQfHZFMZHsMqfPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3889,
      "cache_read_input_tokens": 22070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3889,
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

_source line 174 · 2026-05-12T22:08:42.011Z_

<details><summary>↩ Tool result · `toolu_01UCLZkNXubXG46ZgahNGdNJ`</summary>

```text
Web search results for query: ""Sparse Autoencoders Find Highly Interpretable Features" ICLR 2024"

Links: [{"title":"Sparse Autoencoders Find Highly Interpretable Features in Language Models | OpenReview","url":"https://openreview.net/forum?id=F76bwRSLeK"},{"title":"[2309.08600] Sparse Autoencoders Find Highly Interpretable Features in Language Models","url":"https://arxiv.org/abs/2309.08600"},{"title":"SPARSE AUTOENCODERS FIND HIGHLY INTER","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/1fa1ab11f4bd5f94b2ec20e794dbfa3b-Paper-Conference.pdf"},{"title":"ICLR Poster Sparse Autoencoders Find Highly Interpretable Features in Language Models","url":"https://iclr.cc/virtual/2024/poster/19081"},{"title":"SPARSE AUTOENCODERS FIND HIGHLY INTER- PRETABLE FEATURES IN LANGUAGE MODELS","url":"https://arxiv.org/pdf/2309.08600"},{"title":"[PDF] Sparse Autoencoders Find Highly Interpretable Features in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sparse-Autoencoders-Find-Highly-Interpretable-in-Cunningham-Ewart/edb548fe7574d99454b352ffdb61bca93c3072ba"},{"title":"Sparse Autoencoders Find Highly Interpretable Features in Language Models [Quick Review]","url":"https://liner.com/review/sparse-autoencoders-find-highly-interpretable-features-in-language-models"},{"title":"Paper page - Sparse Autoencoders Find Highly Interpretable Features in Language Models","url":"https://huggingface.co/papers/2309.08600"},{"title":"InterPLM: discovering interpretable features in protein language models via sparse autoencoders | Nature Methods","url":"https://www.nature.com/articles/s41592-025-02836-7"},{"title":"I Have Covered All the Bases Here: Interpreting Reasoning Features in Large Language Models via Sparse Autoencoders","url":"https://arxiv.org/html/2503.18878v1"}]

Based on the search results, I found comprehensive information about this paper:

## "Sparse Autoencoders Find Highly Interpretable Features in Language Models" - ICLR 2024

This work uses sparse autoencoders, a scalable and unsupervised method, to find interpretable, monosemantic features in the residual streams of language models (Pythia-70M/410M).

### Key Problem and Approach

The paper addresses polysemanticity, where neurons appear to activate in multiple, semantically distinct contexts, which prevents identifying concise, human-understandable explanations for what neural networks are doing internally. One hypothesized cause of polysemanticity is superposition, where neural networks represent more features than they have neurons by assigning features to an overcomplete set of directions in activation space.

### Main Findings

The autoencoders learn sets of sparsely activating features that are more interpretable and monosemantic than directions identified by alternative approaches, where interpretability is measured by automated methods. The learned features can pinpoint the features that are causally responsible for counterfactual behavior on the indirect object identification task to a finer degree than previous decompositions.

### Broader Impact

The work indicates that it is possible to resolve superposition in language models using a scalable, unsupervised method, which may serve as a foundation for future mechanistic interpretability work that could enable greater model transparency and steerability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "9f935f44-70e3-44c5-9df5-2191766f68cd"
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
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://arxiv.org/abs/2510.19875",
  "usage": {
    "total_tokens": 25992,
    "tool_uses": 16,
    "duration_ms": 45133
  },
  "last_tool_name": "WebFetch",
  "uuid": "82f06b11-ea56-4780-8e8c-cbab875e3583",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 176_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MVKB6RJ95L3hU5WDXxVLtp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.19875",
  "prompt": "Extract: paper title, full author list, year, venue, and the complete abstract for the Stream paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "5854d58a-4443-4816-b379-9c29a3a76294",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7em4AmBQfHZFMZHsMqfPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3889,
      "cache_read_input_tokens": 22070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3889,
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

_source line 177 · 2026-05-12T22:08:42.490Z_

<details><summary>↩ Tool result · `toolu_017DW7fcdJ9Vc5LEyMCYBtpE`</summary>

```text
# Edge Pruning Paper Summary

**Title:** Finding Transformer Circuits with Edge Pruning

**Authors:** Adithya Bhaskar, Alexander Wettig, Dan Friedman, Danqi Chen

**Year:** 2024 (submitted June 24, 2024; NeurIPS 2024 Spotlight)

**Abstract Overview:**
The researchers propose Edge Pruning, a gradient-based method for automated circuit discovery in language models. Rather than removing entire neurons or components, this approach "prunes the edges between components." The technique discovers circuits in GPT-2 using "less than half the number of edges compared to circuits found by previous methods."

**Key Findings:**

- Edge Pruning achieves comparable performance to prior approaches while being significantly more efficient, scaling to CodeLlama-13B (100x larger than previous methods could handle)
- The method recovers ground-truth circuits perfectly in two Tracr-compiled models
- A case study reveals two circuits with "more than 99.96% sparsity" that match full model performance, showing substantial overlap between instruction prompting and in-context learning mechanisms

**Note on Comparisons:**
While the abstract indicates Edge Pruning outperforms "previous methods" in discovering sparse circuits, the provided excerpt doesn't explicitly name competing approaches like ACDC or EAP or directly compare their discovered circuits' agreement levels.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "3a5d9fc7-f20d-4ecd-b47d-259930993185"
}
```

</details>

---


### System

_source line 178_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://transformer-circuits.pub/2025/attribution…",
  "usage": {
    "total_tokens": 25993,
    "tool_uses": 17,
    "duration_ms": 46988
  },
  "last_tool_name": "WebFetch",
  "uuid": "d8fba987-7dd9-4a04-83e7-78a4ebdf9046",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 179_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DoS6jSG6eYkYLemLXMgytM`</summary>

```json
{
  "url": "https://transformer-circuits.pub/2025/attribution-graphs/methods.html",
  "prompt": "Extract: paper/report title, full author list, year/date, and a summary of the circuit tracing method. What is the key algorithmic contribution? How do cross-layer transcoders and attribution graphs work?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e61ee426-bfd4-4ea8-9e8e-f81d083bdd90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7em4AmBQfHZFMZHsMqfPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3889,
      "cache_read_input_tokens": 22070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3889,
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

_source line 180_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://openreview.net/forum?id=QogcGNXJVw",
  "usage": {
    "total_tokens": 25994,
    "tool_uses": 18,
    "duration_ms": 47746
  },
  "last_tool_name": "WebFetch",
  "uuid": "8921d6c4-2bcf-48fc-bc2c-f8b2a45d9e08",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 181_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CNZZkt146XNu8wi5gy6Hdq`</summary>

```json
{
  "url": "https://openreview.net/forum?id=QogcGNXJVw",
  "prompt": "Extract: paper title, full author list, year, venue for 'The Computational Complexity of Circuit Discovery for Inner Interpretability'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "901b91c2-4573-4181-a211-8050ef0ad29f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7em4AmBQfHZFMZHsMqfPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3889,
      "cache_read_input_tokens": 22070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3889,
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

_source line 182 · 2026-05-12T22:08:45.112Z_

<details><summary>↩ Tool result · `toolu_01KihcBDejfR6mqxFDQSm9re`</summary>

```text
Web search results for query: "subnetwork probing circuit discovery comparison activation patching edge attribution"

Links: [{"title":"[2310.10348] Attribution Patching Outperforms Automated Circuit Discovery","url":"https://arxiv.org/abs/2310.10348"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery - ACL Anthology","url":"https://aclanthology.org/2024.blackboxnlp-1.25/"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery Aaquib Syed","url":"https://openreview.net/pdf?id=tiLbFR4bJW"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery | OpenReview","url":"https://openreview.net/forum?id=RysbaxAnc6"},{"title":"Automatic Circuit Discovery","url":"https://sidn.baulab.info/autocircuits/"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://www.researchgate.net/publication/386190657_Attribution_Patching_Outperforms_Automated_Circuit_Discovery"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://aclanthology.org/2024.blackboxnlp-1.25.pdf"},{"title":"[PDF] Attribution Patching Outperforms Automated Circuit Discovery | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Attribution-Patching-Outperforms-Automated-Circuit-Syed-Rager/27f7aa77bf343fefd3984c6b23265af672bcc0a3"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery | alphaXiv","url":"https://www.alphaxiv.org/abs/2310.10348"},{"title":"NeurIPS Attribution Patching Outperforms Automated Circuit Discovery","url":"https://neurips.cc/virtual/2023/83394"}]

I found relevant research on this topic. The search results focus on a comparison of automated circuit discovery methods in neural networks. Here's what the research shows:

## Attribution Patching vs. Circuit Discovery Methods

Existing automated circuit discovery work applies activation patching to identify subnetworks responsible for solving specific tasks (circuits). A simple method based on attribution patching outperforms all existing methods while requiring just two forward passes and a backward pass.

## Key Methods Compared

The paper introduces two baselines: Subnetwork Probing (SP) which optimizes a mask over model components using gradient descent, and Head Importance Score for Pruning (HISP) which uses a first-order Taylor approximation to estimate the effect of replacing a head's output with corrupted inputs.

## Edge Attribution Patching (EAP)

The method applies a linear approximation to activation patching to estimate the importance of each edge in the computational subgraph. Attribution patching approximates the impact of activation patching on model's output using the first-order Taylor series and is a technique that estimates the impact using only two forward passes and one backward pass.

## Performance Comparison

ACDC outperformed the existing methods HISP and Subnetwork Probing methods. However, the results indicate that the EAP outperforms ACDC.

The research comes from a paper titled "Attribution Patching Outperforms Automated Circuit Discovery" presented at NeurIPS 2023 and the 2024 BlackboxNLP Workshop.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "d2f727c6-1d06-4fb3-9386-b42802cba3b4"
}
```

</details>

---


### System

_source line 183_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for ICML 2025 \"fine-tuning\" \"circuit analysis\" LLM ac…",
  "usage": {
    "total_tokens": 28094,
    "tool_uses": 15,
    "duration_ms": 44382
  },
  "last_tool_name": "WebSearch",
  "uuid": "9b0389c7-4adf-4380-b0ee-24e3a705de8a",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 184_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011pYpR9gA2QNeJwHvvBXUxz`</summary>

```json
{
  "query": "ICML 2025 \"fine-tuning\" \"circuit analysis\" LLM accepted paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "ce7c33e4-a0da-406a-828f-3a1e5f63bcc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LysSLJq49QJyqGkCLe6if4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 718,
      "cache_creation_input_tokens": 2882,
      "cache_read_input_tokens": 24462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2882,
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

_source line 185_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"Adaptive Circuit Behavior and Generalization\" IC…",
  "usage": {
    "total_tokens": 28095,
    "tool_uses": 16,
    "duration_ms": 44703
  },
  "last_tool_name": "WebSearch",
  "uuid": "eb00d5b8-2fd6-4fd2-88de-8581ecf730a4",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 186_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013NsQWkDjGHuwmaZmLrrTJH`</summary>

```json
{
  "query": "\"Adaptive Circuit Behavior and Generalization\" ICLR 2024 mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "745767fe-4750-4d59-8f37-e1f11904486e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LysSLJq49QJyqGkCLe6if4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 718,
      "cache_creation_input_tokens": 2882,
      "cache_read_input_tokens": 24462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2882,
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

_source line 187 · 2026-05-12T22:08:45.963Z_

<details><summary>↩ Tool result · `toolu_011oqRGQN5TVgHMm2HCdEViY`</summary>

```text
# GIM Paper Information

**Title:** GIM: Improved Interpretability for Large Language Models

**Authors:** Joakim Edin, Róbert Csordás, Tuukka Ruotsalo, Zhengxuan Wu, Maria Maistro, Casper L. Christensen, Jing Huang, Lars Maaløe

**Year:** 2025

**Venue:** arXiv (cs.CL - Computation and Language)

**Abstract:**

"Ensuring faithful interpretability in large language models is imperative for trustworthy and reliable AI. A key obstacle is self-repair, a phenomenon where networks compensate for reduced signal in one component by amplifying others, masking the true importance of the ablated component." The authors identify a novel form of self-repair within attention mechanisms involving softmax redistribution. They present Gradient Interaction Modifications (GIM), a technique addressing self-repair during backpropagation. Testing across multiple LLMs (Gemma, LLAMA, Qwen) and tasks demonstrates that "GIM significantly improves faithfulness over existing circuit identification and feature attribution methods," advancing understanding of LLM mechanisms for safety and improvement purposes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "fa7b939a-5464-4fc2-956a-364f29fdb290"
}
```

</details>

---


### Tool result

_source line 188 · 2026-05-12T22:08:46.146Z_

<details><summary>↩ Tool result · `toolu_01CNZZkt146XNu8wi5gy6Hdq`</summary>

```text
# Paper Details

**Title:** "The Computational Complexity of Circuit Discovery for Inner Interpretability"

**Authors:** Federico Adolfi, Martina G. Vilas, Todd Wareham

**Year:** 2025

**Venue:** ICLR 2025 Conference (Spotlight presentation)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "61a5fd22-9ec2-4cef-8dd0-f43de391c77d"
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
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"attribution patching\" circuit discovery NeurIPS …",
  "usage": {
    "total_tokens": 28096,
    "tool_uses": 17,
    "duration_ms": 45661
  },
  "last_tool_name": "WebSearch",
  "uuid": "f6d01fe3-6709-457c-a980-2a969cdaa1eb",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 190_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QZjRxiPjZji8V8xu2nmjFZ`</summary>

```json
{
  "query": "\"attribution patching\" circuit discovery NeurIPS 2024 ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "3161f98e-32a7-437e-b395-2c810f31dba0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LysSLJq49QJyqGkCLe6if4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 718,
      "cache_creation_input_tokens": 2882,
      "cache_read_input_tokens": 24462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2882,
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

_source line 191 · 2026-05-12T22:08:46.974Z_

<details><summary>↩ Tool result · `toolu_01MVKB6RJ95L3hU5WDXxVLtp`</summary>

```text
# Stream Paper Details

**Title:** "Stream: Scaling up Mechanistic Interpretability to Long Context in LLMs via Sparse Attention"

**Authors:** J Rosser, José Luis Redondo García, Gustavo Penha, Konstantina Palla, Hugues Bouchard

**Year:** 2025 (submitted October 22, 2025; revised February 2, 2026)

**Venue:** arXiv (cs.CL - Computation and Language)

**Abstract:**

This research addresses memory constraints when analyzing attention in extended-context language models by introducing Sparse Tracing. The method leverages dynamic sparse attention to examine long-context patterns efficiently. Stream, their hierarchical pruning algorithm, computes per-head sparse attention masks in "near-linear time O(T log T) and linear space O(T)," enabling single-pass analysis at scale. The approach uses binary-search refinement to maintain only top-k key blocks per query while preserving model behavior. Testing on chain-of-thought reasoning and the RULER benchmark demonstrates that Stream "preserves critical retrieval paths while discarding 90-96% of interactions," making long-context interpretability feasible on consumer GPUs and supporting chain-of-thought monitoring accessibility.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "612b7694-c6d3-4309-b438-56784a5c9a7e"
}
```

</details>

---


### System

_source line 192_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for NeurIPS 2024 \"compact proofs\" mechanistic interpr…",
  "usage": {
    "total_tokens": 28097,
    "tool_uses": 18,
    "duration_ms": 46053
  },
  "last_tool_name": "WebSearch",
  "uuid": "35fd811a-5942-4d78-8b73-9b60f0cd4c13",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 193_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LBrb6avfD6b413zsgbMPKw`</summary>

```json
{
  "query": "NeurIPS 2024 \"compact proofs\" mechanistic interpretability model performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "a349b467-15ed-470b-8597-4c6ffb0e2d5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LysSLJq49QJyqGkCLe6if4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 718,
      "cache_creation_input_tokens": 2882,
      "cache_read_input_tokens": 24462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2882,
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

_source line 194 · 2026-05-12T22:08:47.922Z_

<details><summary>↩ Tool result · `toolu_01AaYuioktKPPi44CynoZCf1`</summary>

```text
Web search results for query: ""cross-method" OR "method agreement" OR "consensus" circuit discovery interpretability neural network"

Links: [{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"},{"title":"Towards automated circuit discovery for mechanistic interpretability | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3666841"},{"title":"[2510.14936] Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/abs/2510.14936"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://papers.nips.cc/paper_files/paper/2023/hash/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Abstract-Conference.html"}]

I've performed a web search for research on circuit discovery, interpretability, and neural networks. Here are the key findings:

## Circuit Discovery and Mechanistic Interpretability

Automated circuit discovery is a central tool in mechanistic interpretability for identifying the internal components of neural networks responsible for specific behaviors.

### Current Methodological Approaches

Researchers choose a metric and dataset that elicit the desired model behavior, then apply activation patching to find which abstract neural network units are involved in the behavior, and by varying the dataset, metric, and units under investigation, can understand the functionality of each component.

### Recent Developments and Methods

The field is urgently exploring how to automate and scale interpretability with tools like sparse autoencoders, automated circuit discovery, and circuit tracing, with significant progress made in 2025.

WeightLens and CircuitLens are complementary methods that go beyond activation-based analysis, with CircuitLens capturing how feature activations arise from interactions between components.

### Validation and Consensus Issues

The 2025 "Open Problems" paper acknowledged that conflating hypotheses with conclusions has been commonplace in mechanistic interpretability research, and validation is an important area for improvement, as it is often hard to distinguish faithful explanations from merely plausible ones.

The search results reveal an active area of research focused on automating circuit discovery and addressing cross-method validation challenges in neural network interpretability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "3204c69b-5528-43ad-acda-84e535107ed5"
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-12T22:08:47.970Z_

<details><summary>↩ Tool result · `toolu_01A48jG7tNehtHBnYbnR9wQk`</summary>

```text
Web search results for query: "circuit discovery robustness ensemble neural network interpretability 2024 2025"

Links: [{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823"},{"title":"Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/html/2510.14936v2"},{"title":"Automated Interpretability-Driven Model Auditing and Control: A Research Agenda","url":"https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"},{"title":"Mechanistic Interpretability Techniques","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-techniques"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Mechanistic Interpretability | Decode Neural Networks | CSA","url":"https://cloudsecurityalliance.org/blog/2024/09/05/mechanistic-interpretability-101"},{"title":"Unboxing the Black Box: Mechanistic Interpretability for Algorithmic Understanding of Neural Networks","url":"https://arxiv.org/html/2511.19265v1"},{"title":"Safety, Robustness, and Interpretability in Machine Learning Samuel Pfrommer","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-67.pdf"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"}]

I've found several relevant research results on circuit discovery, robustness, and neural network interpretability from 2024-2025. Here's a summary of the key findings:

## Key Recent Developments

**Robustness and Circuit Discovery:**
Faithfulness measures the robustness of circuits in reproducing model outputs under targeted interventions or ablations, and most current circuit discovery algorithms remain heuristic or approximate, without rigorous guarantees of circuit faithfulness, particularly under continuous perturbation domains. However, recent algorithms yield circuits with substantially stronger robustness guarantees than standard circuit discovery methods — establishing a principled foundation for provable circuit discovery.

**Ensemble and Identifiability Issues:**
State-of-the-art research shows systematic non-identifiability in circuit explanations, urging reporting of explanation ensembles. This is a critical insight suggesting that ensemble-based approaches may be necessary when discovering circuits.

**Automation and Scalability:**
There is a need for higher-throughput automated circuit discovery, hypothesis generation, and robust evaluation standards. Recent progress includes Anthropic's attribution graphs successfully applied to Claude 3.5 Haiku, a production model, and DeepMind's Gemma Scope 2 scaled SAE analysis up to 27B parameters.

**Circuit-Based Interpretability Improvements:**
Circuit-based approaches uncover patterns missed by activation-only methods, improving robustness on smaller datasets by combining weight-based and circuit-based information.

These results reflect the field's active progress toward more robust and automated circuit discovery methods in 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "87d161f4-1f52-4248-a3cd-912eca9dc67d"
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-12T22:08:51.683Z_

<details><summary>↩ Tool result · `toolu_011pYpR9gA2QNeJwHvvBXUxz`</summary>

```text
Web search results for query: "ICML 2025 "fine-tuning" "circuit analysis" LLM accepted paper"

Links: [{"title":"ICML Poster Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis","url":"https://icml.cc/virtual/2025/poster/46507"},{"title":"Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis | OpenReview","url":"https://openreview.net/forum?id=45EIiFd6Oa"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"},{"title":"Track: Poster Session 3 East","url":"https://icml.cc/virtual/2025/session/50265"},{"title":"ICML 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/icml-paper-list/icml-2025-paper-list/"},{"title":"ICML 2025 Schedule","url":"https://icml.cc/virtual/2025/calendar"},{"title":"ICML Poster AUTOCIRCUIT-RL: Reinforcement Learning-Driven LLM for Automated Circuit Topology Generation","url":"https://icml.cc/virtual/2025/poster/45474"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf"},{"title":"Paper Digest: ICML 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/06/icml-2025-papers-highlights/"},{"title":"Learning Dynamics of LLM Finetuning | OpenReview","url":"https://openreview.net/forum?id=tPNHOoZFl9"}]

I found the paper you're looking for! "Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis" was published as an ICML 2025 poster.

Here are the key details about this accepted paper:

**Overview:** Fine-tuning significantly improves the performance of Large Language Models (LLMs), yet its underlying mechanisms remain poorly understood. The paper aims to provide an in-depth interpretation of the fine-tuning process through circuit analysis, a popular tool in Mechanistic Interpretability (MI).

**Methodology:** The authors identify circuits at various checkpoints during fine-tuning and examine the interplay between circuit analysis, fine-tuning methods, and task complexities.

**Key Findings:** The researchers found that most of the key pieces stay intact, but the strength and pattern of their connections change significantly. They introduce a circuit-aware Low-Rank Adaptation (LoRA) method that devotes extra capacity to the most altered connections, achieving better accuracy with fewer added parameters.

**Further Contribution:** They further demonstrate that merging the connection patterns from simpler subtasks can effectively handle compositional tasks without finding circuit for this task again.

You can find the paper on the ICML 2025 virtual conference website and on OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "6fd491d9-fe18-467e-9a0a-1138c1709f3f"
}
```

</details>

---


### System

_source line 197_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for BlackboxNLP 2025 shared task circuit discovery me…",
  "usage": {
    "total_tokens": 28792,
    "tool_uses": 19,
    "duration_ms": 64800
  },
  "last_tool_name": "WebSearch",
  "uuid": "7a572a8f-5c7c-4031-895a-c857795e4555",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 198_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LapuS4bS3ykWrdo5AKpUmB`</summary>

```json
{
  "query": "BlackboxNLP 2025 shared task circuit discovery mechanistic interpretability benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "9d4a249e-9733-4c48-a249-3652e20db9a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYiYJAegB4fu9ndgYfKTGK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 869,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 25893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1967,
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

_source line 199 · 2026-05-12T22:08:52.417Z_

<details><summary>↩ Tool result · `toolu_01DoS6jSG6eYkYLemLXMgytM`</summary>

```text
# Circuit Tracing: Revealing Computational Graphs in Language Models

## Paper Information
**Title:** Circuit Tracing: Revealing Computational Graphs in Language Models

**Authors:** Emmanuel Ameisen, Jack Lindsey, Adam Pearce, Wes Gurnee, Nicholas L. Turner, Brian Chen, Craig Citro, David Abrahams, Shan Carter, Basil Hosmer, Jonathan Marcus, Michael Sklar, Adly Templeton, Trenton Bricken, Callum McDougall, Hoagy Cunningham, Thomas Henighan, Adam Jermyn, Andy Jones, Andrew Persic, Zhenyi Qi, T. Ben Thompson, Sam Zimmerman, Kelley Rivoire, Thomas Conerly, Chris Olah, Joshua Batson

**Date:** March 27, 2025

**Organization:** Anthropic

## Summary of the Method

The paper introduces a technique for interpreting language model behavior by constructing interpretable computational graphs. The core innovation involves replacing opaque neural network components with more transparent ones for analysis.

## Key Algorithmic Contributions

**Cross-Layer Transcoders (CLTs):** The primary technical contribution replaces standard multi-layer perceptrons with "a variant of transcoders" that enables interpretable feature extraction. Rather than analyzing individual neurons, CLTs identify sparsely active features that represent meaningful concepts. Each feature reads from the residual stream at one layer and "contributes to the outputs of all subsequent MLP layers," allowing downstream analysis of their interactions.

**Attribution Graphs:** The method constructs directed acyclic graphs depicting computational flow for specific prompts. As the authors explain, "edges in the graph represent direct, linear effects between nodes," with feature activations decomposable into weighted contributions from earlier features. This linearity is achieved by freezing attention patterns and normalization denominators during analysis.

**Local Replacement Model:** For individual prompts, the underlying model's computation is rewritten using CLT features plus error correction terms, creating an equivalent fully-connected network suitable for classical circuit analysis.

## How They Work Together

The pipeline operates as follows: CLTs decompose MLP outputs into interpretable features; for target prompts, these features form attribution graphs showing mechanistic pathways; researchers then validate graph predictions through targeted perturbation experiments, measuring whether feature interventions produce expected downstream effects consistent with the graph structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "d86a0ff4-380a-4a9a-80ee-189956400919"
}
```

</details>

---


### Tool result

_source line 200 · 2026-05-12T22:08:52.591Z_

<details><summary>↩ Tool result · `toolu_013NsQWkDjGHuwmaZmLrrTJH`</summary>

```text
Web search results for query: ""Adaptive Circuit Behavior and Generalization" ICLR 2024 mechanistic interpretability"

Links: [{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=FbZSZEIkEU"},{"title":"[2411.16105] Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability","url":"https://arxiv.org/abs/2411.16105"},{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241116105N/abstract"},{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability","url":"https://arxiv.org/html/2411.16105v2"},{"title":"[PDF] Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Adaptive-Circuit-Behavior-and-Generalization-in-Nainani-Vaidyanathan/ac2fa12190cb6de71fef60f04c1a499167bec938"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/4ffbfbcf4ad7304d57158b046525e46c-Paper-Conference.pdf"},{"title":"Computation and Language Nov 2024","url":"https://arxiv.org/list/cs.CL/2024-11?skip=1225&show=250"},{"title":"Machine Learning Nov 2024","url":"https://www.arxiv.org/list/cs.LG/2024-11?skip=1325&show=1000"},{"title":"Mechanistic Interpretability of In-Context Learning Generalization through Structured Task Curriculum | OpenReview","url":"https://openreview.net/forum?id=2Fv4GxUElU"},{"title":"ICML 2024 Mechanistic Interpretability Workshop","url":"https://icml2024mi.pages.dev/"}]

I found the paper "Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability"! Here's what the search results reveal:

## Overview

The paper focuses on mechanistic interpretability, which aims to understand the inner workings of large neural networks by identifying circuits, or minimal subgraphs within the model that implement algorithms responsible for performing specific tasks.

## Key Research Question

The work addresses how well circuits generalize across various prompt formats, given the abilities of large language models to generalize across different prompt formats for the same task.

## Main Findings

The researchers investigated the generality of the indirect object identification (IOI) circuit in GPT-2 small, finding that the circuit generalizes surprisingly well, reusing all of its components and mechanisms while only adding additional input edges. 

Notably, the circuit generalizes even to prompt variants where the original algorithm should fail; the researchers discover a mechanism that explains this which they term "S2 Hacking".

## Significance

The findings indicate that circuits within LLMs may be more flexible and general than previously recognized, underscoring the importance of studying circuit generalization to better understand the broader capabilities of these models.

The paper is by Jatin Nainani, Sankaran Vaidyanathan, AJ Yeung, Kartik Gupta, and David Jensen, and was published on arXiv in November 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "40b1c42b-a5a9-47f0-8d0f-6f4c2626fc22"
}
```

</details>

---


### System

_source line 201_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for \"ensemble\" OR \"aggregate\" OR \"combine\" circuit di…",
  "usage": {
    "total_tokens": 28793,
    "tool_uses": 20,
    "duration_ms": 65381
  },
  "last_tool_name": "WebSearch",
  "uuid": "7653d520-9eb6-4b48-84b3-40a70aa62246",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 202_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QxNzdZwH93jKi6Ywnu9Lp2`</summary>

```json
{
  "query": "\"ensemble\" OR \"aggregate\" OR \"combine\" circuit discovery methods interpretability 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "f05758f2-a915-4ca4-8361-2ef406f7e38f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYiYJAegB4fu9ndgYfKTGK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 869,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 25893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1967,
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

_source line 203 · 2026-05-12T22:08:52.696Z_

<details><summary>↩ Tool result · `toolu_01QZjRxiPjZji8V8xu2nmjFZ`</summary>

```text
Web search results for query: ""attribution patching" circuit discovery NeurIPS 2024 ICLR 2024"

Links: [{"title":"GitHub - Aaquib111/edge-attribution-patching: Code for my NeurIPS 2024 ATTRIB paper titled \"Attribution Patching Outperforms Automated Circuit Discovery\" · GitHub","url":"https://github.com/Aaquib111/edge-attribution-patching"},{"title":"NeurIPS Attribution Patching Outperforms Automated Circuit Discovery","url":"https://neurips.cc/virtual/2023/83394"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery - ACL Anthology","url":"https://aclanthology.org/2024.blackboxnlp-1.25/"},{"title":"RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching | OpenReview","url":"https://openreview.net/forum?id=5PKPy82sWN"},{"title":"Actions · Aaquib111/edge-attribution-patching","url":"https://github.com/Aaquib111/edge-attribution-patching/actions"},{"title":"Arthur Conmy","url":"https://scholar.google.com/citations?user=n4HIyXQAAAAJ&hl=en"},{"title":"LLM Circuit Analyses Are Consistent Across Training and Scale Curt Tigges","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf"},{"title":"[2310.10348] Attribution Patching Outperforms Automated Circuit Discovery","url":"https://arxiv.org/abs/2310.10348"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/06a52a54c8ee03cd86771136bc91eb1f-Paper-Conference.pdf"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery | OpenReview","url":"https://openreview.net/forum?id=tiLbFR4bJW"}]

I found results related to your search. Here's what I found:

## Attribution Patching and Circuit Discovery

The paper "Attribution Patching Outperforms Automated Circuit Discovery" by Aaquib Syed, Can Rager, and Arthur Conmy was published in 2024. It appeared in the Proceedings of the 7th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP in Miami, Florida.

The research addresses automated circuit discovery in neural networks. Existing automated circuit discovery work applies activation patching to identify subnetworks responsible for solving specific tasks (circuits). In contrast, the authors show that a simple method based on attribution patching outperforms all existing methods while requiring just two forward passes and a backward pass. They apply a linear approximation to activation patching to estimate the importance of each edge in the computational subgraph and prune the least important edges of the network.

Note: While the paper was presented at a workshop in November 2024, the search results indicate it also appeared as a NeurIPS 2024 workshop paper (titled "NeurIPS 2024 ATTRIB paper"), though I did not find confirmation of an ICLR 2024 publication for this specific paper on attribution patching.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "f571a629-43dd-4f93-a27d-cf8db6efd213"
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
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for circuit discovery methods produce different circu…",
  "usage": {
    "total_tokens": 28794,
    "tool_uses": 21,
    "duration_ms": 65785
  },
  "last_tool_name": "WebSearch",
  "uuid": "3ee50ef0-fd36-4d6d-9d6d-2332a2ee0356",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 205_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CRGtxrGgYuKLLnPhzT3w56`</summary>

```json
{
  "query": "circuit discovery methods produce different circuits reliability robustness interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "40f5b92e-5b99-4768-856d-7d2af3ac1d2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYiYJAegB4fu9ndgYfKTGK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 869,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 25893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1967,
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

_source line 206_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Fetching https://arxiv.org/abs/2603.00523",
  "usage": {
    "total_tokens": 21020,
    "tool_uses": 7,
    "duration_ms": 61523
  },
  "last_tool_name": "WebFetch",
  "uuid": "17b9f493-5dc1-4c83-bb0d-ef94139b4ddc",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 207_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NppKZhbcWNE2FHNzzeQkZU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.00523",
  "prompt": "Extract the full title, all authors, year, venue/status, and a detailed description of the method. Specifically: What exactly does CIRCUS do? Does it aggregate results from multiple different circuit discovery methods (like ACDC, EAP, SP, etc.), or does it vary hyperparameters within a single method? What is the \"stability ensemble\" approach? How does it compute consensus? What is the core/contingent/noise taxonomy?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2369944d-da7b-45d5-b5db-274d449192ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XapKkdqt9EaSibBSCmXVkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 923,
      "cache_read_input_tokens": 19859,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 923,
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

_source line 208 · 2026-05-12T22:08:55.127Z_

<details><summary>↩ Tool result · `toolu_01LBrb6avfD6b413zsgbMPKw`</summary>

```text
Web search results for query: "NeurIPS 2024 "compact proofs" mechanistic interpretability model performance"

Links: [{"title":"Compact Proofs of Model Performance via Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/90e73f3cf1a6c84c723a2e8b7fb2b2c1-Paper-Conference.pdf"},{"title":"NeurIPS Poster Compact Proofs of Model Performance via Mechanistic Interpretability","url":"https://neurips.cc/virtual/2024/poster/96781"},{"title":"Compact Proofs of Model Performance via Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=2zWbzx50mH"},{"title":"[2406.11779] Compact Proofs of Model Performance via Mechanistic Interpretability","url":"https://arxiv.org/abs/2406.11779"},{"title":"[Quick Review] Compact Proofs of Model Performance via Mechanistic Interpretability","url":"https://liner.com/review/compact-proofs-of-model-performance-via-mechanistic-interpretability"},{"title":"Compact Proofs of Model Performance via Mechanistic Interpretability","url":"https://papers.nips.cc/paper_files/paper/2024/hash/90e73f3cf1a6c84c723a2e8b7fb2b2c1-Abstract-Conference.html"},{"title":"Compact Proofs of Model Performance via Mechanistic Interpretability TLDR","url":"https://neurips.cc/media/neurips-2024/Slides/96781.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.07476"},{"title":"Compact Proofs of Model Performance via Mechanistic ...","url":"https://www.alignmentforum.org/posts/bRsKimQcPTX3tNNJZ/compact-proofs-of-model-performance-via-mechanistic"},{"title":"Unifying and Verifying Mechanistic Interpretations: A Case Study with Group Operations","url":"https://arxiv.org/html/2410.07476v2"}]

I've successfully performed the web search on "NeurIPS 2024 compact proofs mechanistic interpretability model performance." Here's what I found:

## Overview

The research proposes using mechanistic interpretability—techniques for reverse engineering model weights into human-interpretable algorithms—to derive and compactly prove formal guarantees on model performance.

## Methodology

The approach was prototyped by formally proving accuracy lower bounds for a small transformer trained on Max-of-K, validating proof transferability across 151 random seeds and four values of K. The researchers created 102 different computer-assisted proof strategies and assessed their length and tightness of bound on each of their models.

## Key Findings

The paper establishes important connections between proof properties and mechanistic understanding:

- Shorter proofs seem to require and provide more mechanistic understanding.
- More faithful mechanistic understanding leads to tighter performance bounds.

## Main Challenges

The researchers identified compounding structureless errors as a key challenge for using mechanistic interpretability to generate compact proofs on model performance. Additionally, it is an open question whether the mechanistic interpretability approach to proofs can scale to larger models, with a large part of this question lying in the feasibility of deriving a high degree of faithful mechanistic understanding from large models.

This was a NeurIPS 2024 poster paper with authors including Jason Gross and seven others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "045efcc8-a8cb-4342-a2a4-c64ce3bdb033"
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
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for mask learning circuit discovery differentiable ma…",
  "usage": {
    "total_tokens": 27678,
    "tool_uses": 19,
    "duration_ms": 60491
  },
  "last_tool_name": "WebSearch",
  "uuid": "62e469f9-1dce-4a4f-9213-ddc2fe914996",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 210_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0131o17dRvTxSM2iLiJL4F2W`</summary>

```json
{
  "query": "mask learning circuit discovery differentiable masking transformer interpretability 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "1269a94b-6058-4248-8bec-5e3fa2d246ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFJVj6bVeKdU7AUgagMFTy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 100,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 25959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1583,
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

_source line 211_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for sparse feature circuits dictionary learning SAE c…",
  "usage": {
    "total_tokens": 27679,
    "tool_uses": 20,
    "duration_ms": 61385
  },
  "last_tool_name": "WebSearch",
  "uuid": "ccdeb4f1-4f9b-4f42-a42d-776026e31d72",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 212_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MhmakzqMBtr3AXQEQ9w2ss`</summary>

```json
{
  "query": "sparse feature circuits dictionary learning SAE circuit discovery 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "fb3819d9-b6c4-47df-8495-8cc66463c051",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFJVj6bVeKdU7AUgagMFTy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 100,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 25959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1583,
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

_source line 213_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for causal scrubbing circuit verification 2024 2025 n…",
  "usage": {
    "total_tokens": 27680,
    "tool_uses": 21,
    "duration_ms": 61699
  },
  "last_tool_name": "WebSearch",
  "uuid": "44f9ed43-3b18-44c5-9c77-dfeec73f9661",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 214_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DWjbGPCZ5ZBdBQykKDUDaB`</summary>

```json
{
  "query": "causal scrubbing circuit verification 2024 2025 new method mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "760e0637-5077-4c7b-9e0d-f952d68a31f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFJVj6bVeKdU7AUgagMFTy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 100,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 25959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1583,
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

_source line 215_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for ICML 2024 main conference circuit interpretabilit…",
  "usage": {
    "total_tokens": 31838,
    "tool_uses": 19,
    "duration_ms": 57731
  },
  "last_tool_name": "WebSearch",
  "uuid": "605f51a3-f2c9-4f59-84ff-28201e5e79c0",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 216_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NRLoA93fy9JyRcA65FLPRj`</summary>

```json
{
  "query": "ICML 2024 main conference circuit interpretability activation patching causal abstraction accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "90ebeedc-6080-44aa-9c37-2fbec645aacc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019yDiTzpd6n8zQnimG7V6vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4456,
      "cache_read_input_tokens": 27344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4456,
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

_source line 217 · 2026-05-12T22:08:59.171Z_

<details><summary>↩ Tool result · `toolu_01NppKZhbcWNE2FHNzzeQkZU`</summary>

```text
# CIRCUS Paper Summary

**Title:** CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles

**Author:** Swapnil Parekh

**Year:** 2026 (submitted February 28, 2026)

**Venue/Status:** arXiv preprint (cs.CL, cs.AI, cs.LG)

---

## Method Description

CIRCUS addresses a fundamental problem in mechanistic circuit analysis: circuit discovery results depend heavily on the pruning threshold chosen, yet conventional practice treats a single pruned graph as definitive without acknowledging this sensitivity.

**What CIRCUS Does:**

Rather than aggregating multiple circuit discovery methods, CIRCUS varies the pruning threshold within a single attribution-based approach. It generates B different configurations by systematically adjusting this hyperparameter, creating a family of circuits under different pruning intensities.

**The Stability Ensemble Approach:**

The method assigns each edge an empirical inclusion frequency s(e) ∈ [0,1] based on "how robustly it survives across the configuration family." Edges appearing consistently across threshold variations receive higher stability scores.

**Consensus Computation:**

A consensus circuit extracts edges present in every configuration view, filtering out threshold-sensitive artifacts while preserving robust structural elements.

**Core/Contingent/Noise Taxonomy:**

This decomposition parallels Bayesian variable selection methodology:
- **Core:** Edges in the consensus (universally robust)
- **Contingent:** Threshold-dependent edges
- **Noise:** Spurious connections in union sets

**Results:** On tested models, consensus circuits were approximately 40x smaller than union configurations while maintaining comparable explanatory power.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "1f48ba53-397b-497f-8841-f9a9454290c1"
}
```

</details>

---


### System

_source line 218_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"LLM Circuit Analyses Are Consistent Across Train…",
  "usage": {
    "total_tokens": 31839,
    "tool_uses": 20,
    "duration_ms": 58171
  },
  "last_tool_name": "WebSearch",
  "uuid": "d1cc1178-2a0c-4683-960a-d7a421c9a221",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 219_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HNHNdSpZPRch8BLonz7Ht7`</summary>

```json
{
  "query": "\"LLM Circuit Analyses Are Consistent Across Training and Scale\" NeurIPS 2024 Tigges"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "20948ecc-c728-4989-8730-328d6892cccf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019yDiTzpd6n8zQnimG7V6vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4456,
      "cache_read_input_tokens": 27344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4456,
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

_source line 220 · 2026-05-12T22:08:59.522Z_

<details><summary>↩ Tool result · `toolu_01LapuS4bS3ykWrdo5AKpUmB`</summary>

```text
Web search results for query: "BlackboxNLP 2025 shared task circuit discovery mechanistic interpretability benchmark"

Links: [{"title":"Shared Task - BlackboxNLP 2025 - GitHub Pages","url":"https://blackboxnlp.github.io/2025/task/"},{"title":"[2511.18409] Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/abs/2511.18409"},{"title":"[2510.06811] BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/abs/2510.06811"},{"title":"[2510.25786] BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection","url":"https://arxiv.org/abs/2510.25786"},{"title":"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/html/2511.18409"},{"title":"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection","url":"https://arxiv.org/html/2510.25786"},{"title":"BlackboxNLP 2025","url":"https://blackboxnlp.github.io/2025/accepted_papers/"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/html/2510.06811v1"},{"title":"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.29/"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods | Request PDF","url":"https://www.researchgate.net/publication/397423880_BlackboxNLP-2025_MIB_Shared_Task_Exploring_Ensemble_Strategies_for_Circuit_Localization_Methods"}]

Based on the search results, here's what I found about the BlackboxNLP 2025 shared task on circuit discovery and mechanistic interpretability:

## Overview

BlackboxNLP 2025 hosts a shared task for benchmarking new techniques for localizing circuits and causal latent variables in language models. The BlackboxNLP 2025 Shared Task extends the Mechanistic Interpretability Benchmark (MIB) into a community-wide reproducible comparison of MI techniques, featuring two tracks: circuit localization, which assesses methods that identify causally influential components and interactions driving model behavior, and causal variable localization, which evaluates approaches that map activations into interpretable features.

## Track Details

The circuit localization track benchmarks methods that aim to locate graphs of causal dependencies in neural networks, while the causal variable localization track benchmarks methods that aim to locate specific human-interpretable causal variables in neural networks.

## Key Results

With three teams spanning eight different methods, participants achieved notable gains in circuit localization using ensemble and regularization strategies for circuit discovery. In the circuit localization track, ensembling strategies and regularization techniques that filter components with unstable contributions to model behavior proved particularly effective.

## Submission Details

Participants submit a report no more than 4 pages long (excluding references) following the BlackboxNLP 2025 formatting guidelines, and the report is considered archival and published in the BlackboxNLP 2025 workshop proceedings on the ACL Anthology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "c65a267a-5c5a-48dd-8f44-c1c44ce779b5"
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-12T22:08:59.690Z_

<details><summary>↩ Tool result · `toolu_01CRGtxrGgYuKLLnPhzT3w56`</summary>

```text
Web search results for query: "circuit discovery methods produce different circuits reliability robustness interpretability"

Links: [{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG","url":"https://arxiv.org/html/2510.00845v2"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis","url":"https://arxiv.org/html/2510.00845"},{"title":"Circuit Insights: Towards Interpretability Beyond Activations | OpenReview","url":"https://openreview.net/forum?id=2Jyb1yu3nN"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Seeing Through Circuits: Faithful Mechanistic Interpretability for Vision Transformers","url":"https://arxiv.org/html/2604.14477"},{"title":"[2510.14936] Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/abs/2510.14936"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"},{"title":"Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/html/2510.14936v2"}]

Based on the search results, I found relevant research on this topic. Here are the key findings:

## Circuit Discovery Methods Produce Different Circuits

Research shows that circuit extraction methods produce highly unstable circuits across nearly all sources of variation, with substantial variance at every stage of the discovery process. Studies have documented structural inconsistency among circuits discovered when multiple parameters are varied simultaneously.

## Reliability and Robustness Issues

Interpretability methods such as circuit discovery should be viewed as statistical estimators, subject to questions of variance and robustness. Circuits are often reported without quantification of their statistical stability, robustness to perturbations, and uncertainty estimates. 

Interventions based on discovered circuits may not generalize reliably, as edits derived from methods like causal tracing can fail to extend to novel contexts.

## Interpretability Considerations

Evaluation of circuits relies on proxy metrics assessing desirable properties including faithfulness, sufficiency/predictive power, interpretability (a qualitative assessment of understandability and alignment with intuition), and sparsity/minimality.

## Moving Forward

Recent work proposes best practices for the mechanistic interpretability community, including systematic bootstrap resampling and the reporting of stability metrics, to promote more rigorous and reliable interpretability research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "52c3b900-f0b9-44f4-a001-bc74b120e90f"
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
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for ICLR 2025 \"sparse feature circuits\" discovering e…",
  "usage": {
    "total_tokens": 31840,
    "tool_uses": 21,
    "duration_ms": 59115
  },
  "last_tool_name": "WebSearch",
  "uuid": "3108da21-e7d1-4ed7-98e1-ce37efe0e93c",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 223_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LHaini1GahhxzMKQpJVbFQ`</summary>

```json
{
  "query": "ICLR 2025 \"sparse feature circuits\" discovering editing interpretable causal graphs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "cb0017e6-e3a7-4588-8a3b-96b60b7602ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019yDiTzpd6n8zQnimG7V6vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4456,
      "cache_read_input_tokens": 27344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4456,
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

_source line 224 · 2026-05-12T22:09:00.670Z_

<details><summary>↩ Tool result · `toolu_01QxNzdZwH93jKi6Ywnu9Lp2`</summary>

```text
Web search results for query: ""ensemble" OR "aggregate" OR "combine" circuit discovery methods interpretability 2024 2025"

Links: [{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/html/2510.06811"},{"title":"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/html/2511.18409v1"},{"title":"Sparse Feature Circuit Discovery","url":"https://www.emergentmind.com/topics/sparse-feature-circuit-discovery"},{"title":"Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/html/2510.14936"},{"title":"Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | OpenReview","url":"https://openreview.net/forum?id=I4e82CIDxv"},{"title":"[PDF] Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sparse-Feature-Circuits:-Discovering-and-Editing-in-Marks-Rager/b8f280d8bf685f8da7c83068e73f000528072d6b"},{"title":"[2403.19647] Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models","url":"https://arxiv.org/abs/2403.19647"},{"title":"Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models","url":"https://arxiv.org/html/2403.19647v1"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"}]

I found several highly relevant recent papers on ensemble and aggregation methods for circuit discovery interpretability. Here are the key findings:

## Recent Work on Ensemble Methods for Circuit Discovery (2024-2025)

Recent work investigates whether ensembling two or more baseline methods can lead to better performance in circuit discovery, hypothesizing that different methods might be biased towards different model components, and that ensembling them might yield a more robust picture.

### Ensemble Approaches

Two variants of ensembling have been explored: parallel ensembling, where scores assigned to each edge by different methods are gathered, typically by averaging, but also by taking the maximum or minimum score, and sequential ensembling, which first warm-starts with EAP-IG (Integrated Gradients) attribution scores, then applies edge pruning with attribution score sign recovery.

**Score Aggregation Methods:**
Four score reduction methods were tested across base approaches: (1) mean, (2) weighted average, (3) maximum, and (4) minimum. Interpreting scores as binary indicators, the maximum corresponds to a union of circuits (edges selected by any method), while the minimum corresponds to an intersection (edges selected by all methods). Ultimately, taking the mean yields the best results.

### Performance and Findings

With three teams spanning eight different methods, participants achieved notable gains in circuit localization using ensemble and regularization strategies for circuit discovery.

### Other Relevant Approaches

Additional interpretability methods include transcoders, which sparsely approximate entire MLP layers while maintaining a clear separation between input-dependent and weight-dependent contributions, enabling efficient circuit discovery and providing direct attributions to other features, attention heads and vocabulary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "16707d3c-6bda-4aa3-995e-aa30c3c952ab"
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
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"scaling sparse autoencoder circuits\" ICLR 2025 m…",
  "usage": {
    "total_tokens": 31841,
    "tool_uses": 22,
    "duration_ms": 59507
  },
  "last_tool_name": "WebSearch",
  "uuid": "271d70d0-d03c-4612-8cc1-6a8287ea9b43",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 226_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TZUCc2UJ2Kp2iUSBLjt2o9`</summary>

```json
{
  "query": "\"scaling sparse autoencoder circuits\" ICLR 2025 mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "d962ae36-4457-427d-8ab3-17994348a83e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019yDiTzpd6n8zQnimG7V6vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4456,
      "cache_read_input_tokens": 27344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4456,
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

_source line 227 · 2026-05-12T22:09:04.706Z_

<details><summary>↩ Tool result · `toolu_01NRLoA93fy9JyRcA65FLPRj`</summary>

```text
Web search results for query: "ICML 2024 main conference circuit interpretability activation patching causal abstraction accepted"

Links: [{"title":"Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims","url":"https://arxiv.org/html/2605.08012"},{"title":"Mechanistic Interpretability for AI Safety — A Review | Leonard F. Bereska","url":"https://leonardbereska.github.io/blog/2024/mechinterpreview/"},{"title":"Explanation in the Era of LLMs NAACL 2024 tutorial","url":"https://explanation-llm.github.io/slides/section_4_slides.pdf"},{"title":"A Theoretical Foundation for Mechanistic Interpretability","url":"https://jmlr.org/papers/volume26/23-0058/23-0058.pdf"},{"title":"TOWARDS BEST PRACTICES OF ACTIVATION PATCH-","url":"https://arxiv.org/pdf/2309.16042"},{"title":"IBCircuit: Towards Holistic Circuit Discovery with Information Bottleneck","url":"https://arxiv.org/html/2602.22581"},{"title":"Activation Patching and Causal Interventions | Learn Mechanistic Interpretability","url":"https://learnmechinterp.com/topics/activation-patching/"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/06a52a54c8ee03cd86771136bc91eb1f-Paper-Conference.pdf"},{"title":"[2309.16042] Towards Best Practices of Activation Patching in Language Models: Metrics and Methods","url":"https://arxiv.org/abs/2309.16042"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"}]

I found search results related to circuit interpretability, activation patching, and causal abstraction techniques. The results include relevant papers and discussions on these mechanistic interpretability methods. Here's what the search revealed:

There was a Mechanistic Interpretability Workshop @ ICML 2024, which indicates that these topics were actively discussed at the conference.

The search results show several key connections between these concepts:

- Causal abstraction provides a solid theoretical foundation for the field of mechanistic interpretability.

- A wide range of existing interpretability methodologies can be unified in a common language, including activation and path patching, causal mediation analysis, causal scrubbing, causal tracing, circuit analysis, concept erasure, sparse autoencoders, differential binary masking, distributed alignment search, and activation steering.

- These causal interventions include activation patching, causal abstraction, and hypothesis testing methods.

However, the search results don't specifically list which papers on these topics were accepted to the main ICML 2024 conference track. The reference to ICML 2024 papers appears limited in the results. If you're looking for the specific list of accepted papers on circuit interpretability, activation patching, and causal abstraction at ICML 2024, you may need to check the official ICML 2024 proceedings directly or the conference website's paper list.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "7346b607-51fe-4ae5-9aa2-246c1015792c"
}
```

</details>

---


### Tool result

_source line 228 · 2026-05-12T22:09:04.764Z_

<details><summary>↩ Tool result · `toolu_01HNHNdSpZPRch8BLonz7Ht7`</summary>

```text
Web search results for query: ""LLM Circuit Analyses Are Consistent Across Training and Scale" NeurIPS 2024 Tigges"

Links: [{"title":"LLM Circuit Analyses Are Consistent Across Training and Scale Curt Tigges","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf"},{"title":"LLM Circuit Analyses Are Consistent Across Training and Scale","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/47c7edadfee365b394b2a3bd416048da-Abstract-Conference.html"},{"title":"[2407.10827] LLM Circuit Analyses Are Consistent Across Training and Scale","url":"https://arxiv.org/abs/2407.10827"},{"title":"NeurIPS Poster LLM Circuit Analyses Are Consistent Across Training and Scale","url":"https://neurips.cc/virtual/2024/poster/96762"},{"title":"LLM Circuit Analyses Are Consistent Across Training and Scale","url":"https://arxiv.org/html/2407.10827v1"},{"title":"Paper page - LLM Circuit Analyses Are Consistent Across Training and Scale","url":"https://huggingface.co/papers/2407.10827"},{"title":"Publications | Michael Hanna - GitHub Pages","url":"https://hannamw.github.io/publications/"},{"title":"LLM Circuit Analyses Are Consistent Across Training and Scale Curt Tigges","url":"https://arxiv.org/pdf/2407.10827"},{"title":"LLM Circuit Analyses Are Consistent Across Training and Scale | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/llm-circuit-analyses-are-consistent-across-training"},{"title":"LLM Circuit Analyses Are Consistent Across Training and Scale | OpenReview","url":"https://openreview.net/forum?id=3Ds5vNudIE"}]

I found the paper "LLM Circuit Analyses Are Consistent Across Training and Scale" by Curt Tigges and colleagues. Here's what the research is about:

## Overview

Most research into LLMs' internal mechanisms focuses on models at one snapshot in time (the end of pre-training), raising the question of whether their results generalize to real-world settings, particularly since most currently deployed LLMs undergo continuous training or additional finetuning.

## Research Methodology

The study tracks how model mechanisms, operationalized as circuits, emerge and evolve across 300 billion tokens of training in decoder-only LLMs, in models ranging from 70 million to 2.8 billion parameters.

## Key Findings

The researchers find that task abilities and the functional components that support them emerge consistently at similar token counts across scale. Additionally, although such components may be implemented by different attention heads over time, the overarching algorithm that they implement remains.

Both these algorithms and the types of components involved therein tend to replicate across model scale. Importantly, these results suggest that circuit analyses conducted on small models at the end of pre-training can provide insights that still apply after additional training and over model scale.

## Publication

The paper was presented by Curt Tigges, Michael Hanna, Qinan Yu, and Stella Biderman at NeurIPS 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "86e6e8e8-728d-4e05-9aa0-5b22dafcb675"
}
```

</details>

---


### System

_source line 229_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Fetching https://arxiv.org/abs/2510.00845",
  "usage": {
    "total_tokens": 21671,
    "tool_uses": 8,
    "duration_ms": 72748
  },
  "last_tool_name": "WebFetch",
  "uuid": "6fc66e01-63f4-4d38-a0cc-bc15f52e7a04",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 230_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LMa6KKNEQkep3cLGfzxyEY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.00845",
  "prompt": "Extract the full title, all authors, year, venue/status, and detailed description. Specifically: Does this paper propose aggregating results from multiple different circuit discovery methods? Or does it analyze variance within a single method (EAP-IG)? What exactly do they vary - do they compare ACDC vs EAP vs SP, or just hyperparameters of EAP? What is their main finding about stability across methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e0ec3c5c-1517-4212-816e-db40a0dff0b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHLXg9t8CKczWcqS23More",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 20782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 586,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-12T22:09:05.261Z_

<details><summary>↩ Tool result · `toolu_01DWjbGPCZ5ZBdBQykKDUDaB`</summary>

```text
Web search results for query: "causal scrubbing circuit verification 2024 2025 new method mechanistic interpretability"

Links: [{"title":"Causal Scrubbing: a method for rigorously testing ...","url":"https://www.alignmentforum.org/posts/JvZhhzycHu2Yd57RN/causal-scrubbing-a-method-for-rigorously-testing"},{"title":"Mechanistic Interpretability for AI Safety — A Review | Leonard F. Bereska","url":"https://leonardbereska.github.io/blog/2024/mechinterpreview/"},{"title":"[2301.04709] Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability","url":"https://arxiv.org/abs/2301.04709"},{"title":"GitHub - Dakingrai/awesome-mechanistic-interpretability-lm-papers · GitHub","url":"https://github.com/Dakingrai/awesome-mechanistic-interpretability-lm-papers"},{"title":"Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability","url":"https://jmlr.org/papers/v26/23-0058.html"},{"title":"Mechanistic Interpretability Explained: Circuits, Sparse Autoencoders, Causal Tracing, and AI Safety | by Adnan Masood, PhD. | Apr, 2026 | Medium","url":"https://medium.com/@adnanmasood/mechanistic-interpretability-explained-circuits-sparse-autoencoders-causal-tracing-and-ai-88ecc8d70b72"},{"title":"Mechanistic Interpretability Techniques","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-techniques"},{"title":"Journal of Machine Learning Research 26 (2025) 1-63","url":"https://arxiv.org/pdf/2301.04709"},{"title":"A Theoretical Foundation for Mechanistic Interpretability","url":"https://jmlr.org/papers/volume26/23-0058/23-0058.pdf"},{"title":"Causal Scrubbing: a method for rigorously testing interpretability hypotheses | Lawrence Chan","url":"https://chanlawrence.me/publication/chan-2022-causal/"}]

Based on the search results, here's what I found about causal scrubbing and circuit verification in mechanistic interpretability:

## Causal Scrubbing Overview

Causal scrubbing is a principled approach for evaluating the quality of mechanistic interpretations. The method works by treating mechanistic interpretability hypotheses as defining which activations inside a neural network can be resampled without affecting behavior, testing these hypotheses through behavior-preserving resampling ablations.

## Recent Theoretical Development (2024-2025)

A significant advancement in the field is the generalization of causal abstraction theory to arbitrary mechanism transformation, providing precise formalization for core concepts including polysemantic neurons, the linear representation hypothesis, modular features, and graded faithfulness, while unifying mechanistic interpretability methods such as activation and path patching, causal mediation analysis, causal scrubbing, causal tracing, circuit analysis, concept erasure, sparse autoencoders, differential binary masking, distributed alignment search, and steering. This theoretical work was updated as recently as May 2025.

## Role in Circuit Verification

Causal scrubbing forms part of a hierarchy of verification methods alongside full causal abstractions and locally consistent abstractions, with different levels of strictness affecting the ability to find acceptable explanations, generalization, and mechanistic anomaly detection. Causal scrubbing and hypothesis testing replace activations consistent with an interpretable causal hypothesis, verifying whether the hypothesized subcircuit is sufficient for model accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "6222f6b2-975c-4a56-addb-4db62dd6b5e3"
}
```

</details>

---


### Tool result

_source line 232 · 2026-05-12T22:09:05.642Z_

<details><summary>↩ Tool result · `toolu_0131o17dRvTxSM2iLiJL4F2W`</summary>

```text
Web search results for query: "mask learning circuit discovery differentiable masking transformer interpretability 2024 2025"

Links: [{"title":"Beyond Components: Singular Vector-Based Interpretability of Transformer Circuits","url":"https://arxiv.org/html/2511.20273"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/html/2510.03282v1"},{"title":"Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning","url":"https://arxiv.org/html/2407.03779v1/"},{"title":"Circuits Updates - July 2025","url":"https://transformer-circuits.pub/2025/july-update/index.html"},{"title":"Weight-sparse transformers have interpretable circuits","url":"https://cdn.openai.com/pdf/41df8f28-d4ef-43e9-aed2-823f9393e470/circuit-sparsity-paper.pdf"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/html/2407.00886v3"},{"title":"Finding Transformer Circuits With Edge Pruning | OpenReview","url":"https://openreview.net/forum?id=8oSY3rA9jY"},{"title":"Learn to explain transformer via interpretation path by reinforcement learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608025003752"},{"title":"A Practical Review of Mechanistic Interpretability for Transformer-Based Language Models","url":"https://arxiv.org/html/2407.02646v4"}]

I've found relevant research on mask learning, circuit discovery, differentiable masking, and transformer interpretability from 2024-2025. Here are the key findings:

## Recent Work on Masking and Circuit Discovery

### Directional Masking in Transformer Circuits (2025)

A recent approach introduces a directional interpretability perspective that models transformer components as superpositions of orthogonal subfunctions rather than atomic units, using an optimization-based masking scheme that identifies functionally important singular directions within attention and MLP layers. This allows continuous, direction-level control over component behavior while maintaining differentiability for optimization.

### Edge Pruning and Gradient-Based Optimization (2024-2025)

Edge Pruning frames circuit discovery as an optimization problem and leverages gradient-based pruning techniques to prune the edges between components. This method finds circuits in GPT-2 that use less than half the number of edges than circuits found by previous methods while being equally faithful to the full model predictions.

### Differentiable Computation Graph Pruning (2024)

Existing circuit discovery efforts face challenges where researchers must choose between identifying important model weights or recognizing essential connections between model components, which cannot be localized together by prior circuit discovery methods.

### RL-Based Masking Approach (2025)

A reinforcement learning-based framework applies masking or deletion operations to the input, forming an interpretation path that reveals high-order compositional relationships between tokens.

## Automated Circuit Discovery Methods

Manual circuit discovery methods have largely been replaced by automated approaches like Automated Circuit DisCovery (ACDC), which uses a greedy search algorithm to ablate edges one by one.

These recent developments show significant progress in using differentiable masking techniques for more precise and scalable circuit discovery in transformers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b390582c-1449-42fe-a98a-2895365ef130"
}
```

</details>

---


### System

_source line 233_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/abs/2510.06811",
  "usage": {
    "total_tokens": 31658,
    "tool_uses": 22,
    "duration_ms": 78463
  },
  "last_tool_name": "WebFetch",
  "uuid": "171e518a-a486-4122-8528-c9f14b8e0dbb",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 234_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XHxW291UVT3JQ9tCjAe8ba`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.06811",
  "prompt": "Extract the full title, authors, year, venue, abstract, and key findings. This paper is about ensemble strategies for circuit localization. What specific methods does it ensemble? What does it find about agreement between methods? Does it discuss intersection/union of circuits from different methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8f3c4a24-ae84-4ff6-affc-c7491c5f7195",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JY1pfNxdjiEh15PV4ku4Gs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 2950,
      "cache_read_input_tokens": 27860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2950,
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

_source line 235 · 2026-05-12T22:09:06.076Z_

<details><summary>↩ Tool result · `toolu_01MhmakzqMBtr3AXQEQ9w2ss`</summary>

```text
Web search results for query: "sparse feature circuits dictionary learning SAE circuit discovery 2024 2025"

Links: [{"title":"Sparse Feature Circuit Discovery","url":"https://www.emergentmind.com/topics/sparse-feature-circuit-discovery"},{"title":"[2403.19647] Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models","url":"https://arxiv.org/abs/2403.19647"},{"title":"Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models","url":"https://arxiv.org/html/2403.19647v1"},{"title":"sparse feature circuits: discovering","url":"https://belinkov.com/assets/pdf/iclr2025-sfc.pdf"},{"title":"Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models","url":"https://features.baulab.info/"},{"title":"GitHub - saprmarks/feature-circuits · GitHub","url":"https://github.com/saprmarks/feature-circuits"},{"title":"[PDF] Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sparse-Feature-Circuits:-Discovering-and-Editing-in-Marks-Rager/b8f280d8bf685f8da7c83068e73f000528072d6b"},{"title":"SCALING SPARSE AUTOENCODER CIRCUITS FOR IN","url":"https://openreview.net/pdf?id=Pa1vr1Prww"},{"title":"Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | OpenReview","url":"https://openreview.net/forum?id=I4e82CIDxv"},{"title":"Transcoders find interpretable LLM feature circuits","url":"https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"}]

Based on the search results, here's what I found about sparse feature circuits, dictionary learning, and SAE circuit discovery in 2024-2025:

## Overview

Sparse autoencoders (SAEs) and dictionary learning are widely employed to decompose dense model activations into overcomplete, ideally monosemantic, sparse features.

## Key Research: Sparse Feature Circuits

The most significant recent work is the "Sparse Feature Circuits" paper by Marks et al. This work introduces methods for discovering and applying sparse feature circuits, which are causally implicated subnetworks of human-interpretable features for explaining language model behaviors.

The paper demonstrates an entirely unsupervised and scalable interpretability pipeline by discovering thousands of sparse feature circuits for automatically discovered model behaviors.

## Applications and Methodologies

SAEs are used to identify directions in LM latent spaces which represent human-interpretable concepts. Sparse feature circuit discovery has been deployed across several domains including model interpretability in NLP: SAE-based feature circuits are used to dissect mechanisms such as syntactic agreement or in-context learning.

## Recent Advances (2025)

Recent work has extended these methods. Researchers adapted the Sparse Feature Circuits methodology of Marks et al. to work on the more complex in-context learning task and the larger Gemma-1 2B model, allowing discovery and analysis of the subgraph of key SAE latents involved in ICL.

Alternative approaches are also emerging: Unlike SAEs that reconstruct a single layer, transcoders learn sparse mappings from one layer to the next, and SAEs and related dictionary learning methods decompose neural activations into sparse, interpretable features.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "df4a9b13-a172-4234-9d0c-65dd1f78e7c2"
}
```

</details>

---


### System

_source line 236_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/abs/2510.00845",
  "usage": {
    "total_tokens": 31659,
    "tool_uses": 23,
    "duration_ms": 79988
  },
  "last_tool_name": "WebFetch",
  "uuid": "b78b743f-a4af-4c54-9052-cf9cbc8faf91",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 237_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y19JxZtXP5mBHpZVMALRci`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.00845",
  "prompt": "Extract the full title, authors, year, venue, abstract, and key findings. This paper is about variance analysis of EAP-IG. What does it find about the stability/reliability of circuit discovery? Does it show that different runs or configurations produce different circuits?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "865481b9-be58-4bf1-ace4-8e30ac765b3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JY1pfNxdjiEh15PV4ku4Gs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 2950,
      "cache_read_input_tokens": 27860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2950,
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

_source line 238_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/abs/2511.18409",
  "usage": {
    "total_tokens": 31660,
    "tool_uses": 24,
    "duration_ms": 81473
  },
  "last_tool_name": "WebFetch",
  "uuid": "42b51f81-5c8b-4ac8-8a48-0402974de9ea",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 239_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SVRiUyBTbxfQAVQNcaDfJm`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.18409",
  "prompt": "Extract the full title, authors, year, venue, abstract, and key findings. This is the findings paper for the BlackboxNLP 2025 shared task. What methods participated? What were the key findings about how different methods compare? Does it discuss agreement or consistency between methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "01cd3afd-4f8e-4926-a877-200a44a78353",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JY1pfNxdjiEh15PV4ku4Gs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 2950,
      "cache_read_input_tokens": 27860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2950,
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

_source line 240_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://arxiv.org/abs/2403.19647",
  "usage": {
    "total_tokens": 30695,
    "tool_uses": 22,
    "duration_ms": 72369
  },
  "last_tool_name": "WebFetch",
  "uuid": "1e46e772-9061-4961-9551-0daf862b7bf0",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 241_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HeSdyiVAWJ2PBTcynff1gV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2403.19647",
  "prompt": "Extract: paper title, full author list, year, venue, and complete abstract for the Sparse Feature Circuits paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "262a73af-ea59-4d4d-b1a6-96441f0270c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbuMuYxanPTygXHAMvRzwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 944,
      "cache_creation_input_tokens": 2109,
      "cache_read_input_tokens": 27542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2109,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 242_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/abs/2310.10348",
  "usage": {
    "total_tokens": 31661,
    "tool_uses": 25,
    "duration_ms": 82129
  },
  "last_tool_name": "WebFetch",
  "uuid": "74cf3033-08eb-4cfa-857c-b4e26cbd18b5",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 243_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018pEfpz6FddrVsz2JfLsXp8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2310.10348",
  "prompt": "Extract the full title, authors, year, venue, abstract, and key findings. What specific methods does this paper compare? What metrics does it use? What does it find about circuit overlap between methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "a81101a9-7e9a-4706-b439-c6b20a23a9fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JY1pfNxdjiEh15PV4ku4Gs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 2950,
      "cache_read_input_tokens": 27860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2950,
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

_source line 244 · 2026-05-12T22:09:09.466Z_

<details><summary>↩ Tool result · `toolu_01TZUCc2UJ2Kp2iUSBLjt2o9`</summary>

```text
Web search results for query: ""scaling sparse autoencoder circuits" ICLR 2025 mechanistic interpretability"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/42ef3308c230942d223c411adf182c88-Paper-Conference.pdf"},{"title":"Sparse Autoencoders Find Highly Interpretable Features in Language Models | OpenReview","url":"https://openreview.net/forum?id=F76bwRSLeK"},{"title":"Published as a conference paper at ICLR 2025","url":"https://belinkov.com/assets/pdf/iclr2025-sfc.pdf"},{"title":"Scaling and evaluating sparse autoencoders Leo Gao∗ Tom Dupré la Tour†","url":"https://cdn.openai.com/papers/sparse-autoencoders.pdf"},{"title":"Towards Monosemanticity: Decomposing Language Models With Dictionary Learning","url":"https://transformer-circuits.pub/2023/monosemantic-features"},{"title":"Scaling and evaluating sparse autoencoders | OpenReview","url":"https://openreview.net/forum?id=tcsZt9ZNKD"},{"title":"Scaling Sparse Feature Circuits For Studying In-Context Learning | OpenReview","url":"https://openreview.net/forum?id=sdLwJTtKpM"},{"title":"SCALING SPARSE AUTOENCODER CIRCUITS FOR IN","url":"https://openreview.net/pdf?id=Pa1vr1Prww"},{"title":"GitHub - zepingyu0512/awesome-SAE: awesome SAE papers · GitHub","url":"https://github.com/zepingyu0512/awesome-SAE"},{"title":"ICLR 2025 Scaling and evaluating sparse autoencoders Oral","url":"https://iclr.cc/virtual/2025/oral/31752"}]

I found several papers related to sparse autoencoders and mechanistic interpretability from ICLR 2025. Here are the key results:

## Major ICLR 2025 Papers on Sparse Autoencoders

**1. Scaling and Evaluating Sparse Autoencoders**

Sparse autoencoders provide a promising unsupervised approach for extracting interpretable features from a language model by reconstructing activations from a sparse bottleneck layer. The paper proposes using k-sparse autoencoders to directly control sparsity, simplifying tuning and improving the reconstruction-sparsity frontier. To demonstrate the scalability of the approach, the authors train a 16 million latent autoencoder on GPT-4 activations for 40 billion tokens. The paper introduces several new metrics for evaluating feature quality based on the recovery of hypothesized features, the explainability of activation patterns, and the sparsity of downstream effects.

**2. Scaling Sparse Feature Circuits for In-Context Learning**

This work uses sparse autoencoders to deepen understanding of the mechanism behind in-context learning, identifying abstract SAE features that encode the model's knowledge of which task to execute and whose latent vectors causally induce the task zero-shot. The authors adapt the sparse feature circuits methodology to work for the much larger Gemma-1 2B model with 30 times as many parameters.

**3. Sparse Feature Circuits**

This work uses sparse autoencoders to identify directions in language model latent spaces which represent human-interpretable concepts.

These papers represent significant advances in using sparse autoencoders as tools for mechanistic interpretability at scale.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "085a3aae-bf4f-4739-ae05-81c3ba48ac1f"
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-12T22:09:10.292Z_

<details><summary>↩ Tool result · `toolu_01LHaini1GahhxzMKQpJVbFQ`</summary>

```text
Web search results for query: "ICLR 2025 "sparse feature circuits" discovering editing interpretable causal graphs"

Links: [{"title":"ICLR 2025 Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models Oral","url":"https://iclr.cc/virtual/2025/oral/31874"},{"title":"Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | OpenReview","url":"https://openreview.net/forum?id=I4e82CIDxv"},{"title":"[2403.19647] Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models","url":"https://arxiv.org/abs/2403.19647"},{"title":"sparse feature circuits: discovering","url":"https://belinkov.com/assets/pdf/iclr2025-sfc.pdf"},{"title":"Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models","url":"https://features.baulab.info/"},{"title":"Discovering and Editing Interpretable Causal Graphs in ...","url":"https://iclr.cc/media/iclr-2025/Slides/31874_DFSMWNC.pdf"},{"title":"ICLR Poster Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models","url":"https://iclr.cc/virtual/2025/poster/30192"},{"title":"SPARSE FEATURE CIRCUITS: DISCOVERING AND EDITING INTERPRETABLE CAUSAL GRAPHS IN LANGUAGE MODELS - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/sparse-feature-circuits-discovering-and-editing-interpretable-cau/"},{"title":"[PDF] Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sparse-Feature-Circuits:-Discovering-and-Editing-in-Marks-Rager/b8f280d8bf685f8da7c83068e73f000528072d6b"},{"title":"Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models","url":"https://arxiv.org/html/2403.19647v1"}]

I found comprehensive information about the ICLR 2025 paper on Sparse Feature Circuits. Here's what the search revealed:

## Paper Overview

The paper introduces methods for discovering and applying sparse feature circuits, which are causally implicated subnetworks of human-interpretable features for explaining language model behaviors. Circuits identified in prior work consist of polysemantic and difficult-to-interpret units like attention heads or neurons, rendering them unsuitable for many downstream applications. In contrast, sparse feature circuits enable detailed understanding of unanticipated mechanisms in neural networks.

## Methodology

The work leverages recent progress in dictionary learning to train sparse autoencoders (SAEs) to identify directions in a language model's latent space which represent human-interpretable features. To solve the scalability challenge, the authors employ linear approximations to efficiently identify SAE features which are most causally implicated in model behaviors, as well as connections between these features.

## Applications

The paper introduces SHIFT, where generalization of a classifier is improved by ablating features that a human judges to be task-irrelevant. The work demonstrates an entirely unsupervised and scalable interpretability pipeline by discovering thousands of sparse feature circuits for automatically discovered model behaviors.

## Evaluation and Results

The method discovers human-interpretable causal graphs for a subject-verb agreement task, a classifier, and thousands of general token prediction tasks.

The paper was presented as an oral presentation at ICLR 2025, which took place in Singapore from April 24-28, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "049405a6-1d4e-4cca-bc3d-6531dd57c1c3"
}
```

</details>

---


### Tool result

_source line 246 · 2026-05-12T22:09:10.564Z_

<details><summary>↩ Tool result · `toolu_01LMa6KKNEQkep3cLGfzxyEY`</summary>

```text
# Paper Analysis

**Full Title:** "Mechanistic Interpretability as Statistical Estimation: A Variance Analysis"

**Authors:** Maxime Méloux, François Portet, Maxime Peyrard

**Year:** 2025 (submitted October 1, 2025; v3 February 3, 2026)

**Venue/Status:** arXiv preprint (cs.LG - Computer Science/Machine Learning)

---

## Scope of Analysis

Based on the abstract provided, this paper **analyzes variance within the circuit discovery framework itself**, rather than comparing multiple distinct methods like ACDC versus EAP versus SP.

The research focuses on a fundamental problem: "exact, single-input CMA scores exhibit high intrinsic variance, implying that the causal effect of a component is a volatile random variable rather than a fixed property."

The authors examine how "circuit discovery pipelines inherit this variance and further amplify it," specifically noting that approximation methods like Edge Attribution Patching introduce additional estimation noise, and aggregating these scores across datasets produces unstable structural estimates.

---

## Main Finding on Stability

The critical instability finding centers on **fragility to perturbations**: "small perturbations in input data or hyperparameters yield vastly different circuits." Rather than comparing across different methods, they systematically decompose variance sources within the existing pipeline and advocate for "more rigorous MI practices, prioritizing statistical robustness and routine reporting of stability metrics."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "9828fc12-a0c2-425a-a20e-47750a2718fb"
}
```

</details>

---


### System

_source line 247_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://arxiv.org/html/2407.03779v1/",
  "usage": {
    "total_tokens": 30757,
    "tool_uses": 23,
    "duration_ms": 73766
  },
  "last_tool_name": "WebFetch",
  "uuid": "4f65d75c-b287-42d7-92fb-424e845f8e28",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 248_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015mPR9GFS3V1AMBW2YNXHvE`</summary>

```json
{
  "url": "https://arxiv.org/html/2407.03779v1/",
  "prompt": "Extract: paper title, full author list, year, venue, and abstract. What is the method name and key algorithmic contribution for differentiable computation graph pruning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "82746248-4e84-430e-9524-389d85ad7ded",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbuMuYxanPTygXHAMvRzwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 944,
      "cache_creation_input_tokens": 2109,
      "cache_read_input_tokens": 27542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2109,
        "ephemeral_1h_input_tokens": 0
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

_source line 249 · 2026-05-12T22:09:11.287Z_

<details><summary>↩ Tool result · `toolu_01XHxW291UVT3JQ9tCjAe8ba`</summary>

```text
# Paper Summary: Circuit Localization Ensemble Strategies

**Full Title:** "BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods"

**Authors:** Philipp Mondorf, Mingyang Wang, Sebastian Gerstner, Ahmad Dawar Hakimi, Yihong Liu, Leonor Veloso, Shijia Zhou, Hinrich Schütze, Barbara Plank

**Year:** 2025 (submitted October 8, 2025)

**Venue:** The 8th BlackboxNLP Workshop (Shared Task)

## Abstract Summary
The research investigates whether combining multiple circuit localization methods can enhance performance in identifying subnetworks responsible for specific behaviors in large language models. The team evaluates both parallel and sequential ensembling approaches.

## Specific Methods Ensembled
- **Parallel ensembling:** Combines attribution scores from different methods through operations like averaging, minimum, or maximum values
- **Sequential ensembling:** Uses EAP-IG scores as a warm start for edge pruning

## Key Findings
The authors report that "both approaches yield notable gains on the benchmark metrics" and discover that parallel ensembling over various methods, including the sequential approach, produces optimal results. However, the provided content does not explicitly discuss agreement patterns between individual methods or specific intersection/union analyses of circuits from different methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "1f523e2e-19c5-4c7e-a011-f71af6c8ef31"
}
```

</details>

---


### System

_source line 250_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://arxiv.org/html/2511.20273",
  "usage": {
    "total_tokens": 30819,
    "tool_uses": 24,
    "duration_ms": 74666
  },
  "last_tool_name": "WebFetch",
  "uuid": "8c9de3c5-11dc-4092-a258-e5ebea86c410",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 251_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LjzHWJ9zqfsv7icWVhNyh6`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.20273",
  "prompt": "Extract: paper title, full author list, year, venue, and abstract. What is the key method for singular vector-based circuit interpretability?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b9cf341c-1cc2-45a4-a785-fd7bf78ba96b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbuMuYxanPTygXHAMvRzwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 944,
      "cache_creation_input_tokens": 2109,
      "cache_read_input_tokens": 27542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2109,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 252_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for weight sparse transformers interpretable circuits…",
  "usage": {
    "total_tokens": 30881,
    "tool_uses": 25,
    "duration_ms": 75298
  },
  "last_tool_name": "WebSearch",
  "uuid": "8e93ca62-3980-41a5-9325-b5fd27032d96",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 253_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ave17iPJKprkyc6Z862tja`</summary>

```json
{
  "query": "weight sparse transformers interpretable circuits OpenAI 2025 circuit sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "d7718583-c35a-4d4c-a8b0-a69e063e51f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbuMuYxanPTygXHAMvRzwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 944,
      "cache_creation_input_tokens": 2109,
      "cache_read_input_tokens": 27542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2109,
        "ephemeral_1h_input_tokens": 0
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

_source line 254 · 2026-05-12T22:09:12.427Z_

<details><summary>↩ Tool result · `toolu_01Y19JxZtXP5mBHpZVMALRci`</summary>

```text
# Paper Summary

**Title:** Mechanistic Interpretability as Statistical Estimation: A Variance Analysis

**Authors:** Maxime Méloux, François Portet, Maxime Peyrard

**Year:** 2025 (submitted October 1, 2025; v3 February 3, 2026)

**Venue:** arXiv (cs.LG - Computer Science, Machine Learning)

## Abstract
The authors argue that circuit discovery represents "a statistical estimation problem built upon causal mediation analysis" rather than a standalone task. They identify fundamental instability issues where causal effect measurements function as volatile variables rather than stable properties.

## Key Findings on Stability/Reliability

The research demonstrates that circuit discovery exhibits critical reliability problems:

1. **Inherent Variance:** The base causal mediation analysis layer produces high intrinsic variance, making individual component effects unstable.

2. **Pipeline Amplification:** Circuit discovery pipelines "inherit this variance and further amplify it" through their operations.

3. **Approximation Noise:** Methods like Edge Attribution Patching introduce "additional estimation noise" that compounds problems.

4. **Fragile Aggregation:** Combining noisy scores across datasets produces "fragile structural estimates."

5. **Sensitivity to Perturbations:** The paper reveals that "small perturbations in input data or hyperparameters yield vastly different circuits," indicating substantial instability across configurations and runs.

The authors advocate for prioritizing "statistical robustness and routine reporting of stability metrics" in mechanistic interpretability practices.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2e18d392-9f6c-4ddb-84e2-48e1056ff33f"
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-12T22:09:12.990Z_

<details><summary>↩ Tool result · `toolu_01HeSdyiVAWJ2PBTcynff1gV`</summary>

```text
**Paper Title:** "Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models"

**Authors:** Samuel Marks, Can Rager, Eric J. Michaud, Yonatan Belinkov, David Bau, Aaron Mueller

**Year:** 2024 (submitted March 28, 2024; published 2025)

**Venue:** International Conference on Learning Representations, 2025

**Abstract:**

The researchers present techniques for identifying and utilizing sparse feature circuits—causally relevant subnetworks composed of interpretable features that explain language model behaviors. Unlike earlier circuit work relying on opaque units such as attention heads or neurons, these circuits leverage fine-grained components for improved interpretability. The team introduces SHIFT, a method that enhances classifier generalization by removing features deemed task-irrelevant by human evaluators. Additionally, they demonstrate a fully automated, large-scale interpretability approach by uncovering "thousands of sparse feature circuits for automatically discovered model behaviors."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e9cd2b45-c022-48cd-8bff-f719606e759f"
}
```

</details>

---


### Tool result

_source line 256 · 2026-05-12T22:09:13.804Z_

<details><summary>↩ Tool result · `toolu_01SVRiUyBTbxfQAVQNcaDfJm`</summary>

```text
# BlackboxNLP 2025 Shared Task Findings

**Full Title:** "Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models"

**Authors:** Dana Arad, Yonatan Belinkov, Hanjie Chen, Najoung Kim, Hosein Mohebbi, Aaron Mueller, Gabriele Sarti, Martin Tutek

**Year:** 2025 (submitted November 23, 2025)

**Venue:** BlackboxNLP 2025

## Abstract Summary

The paper presents results from a shared task extending the Mechanistic Interpretability Benchmark. The work evaluates community methods across two tracks: identifying causally influential model components and mapping activations to interpretable features.

## Key Findings

**Circuit Localization Track:** Three teams submitted eight different methods. The most effective approaches employed "ensemble and regularization strategies for circuit discovery," suggesting that combining multiple techniques improved component identification.

**Causal Variable Localization Track:** One team contributed two methods that achieved "significant gains in causal variable localization using low-dimensional and non-linear projections to featurize activation vectors," indicating that dimensionality reduction and non-linear transformations enhanced feature mapping.

## Discussion of Method Comparison

The document does not discuss agreement or consistency between different methods. Instead, it focuses on performance improvements within each track and notes that the MIB leaderboard remains open for continued benchmarking efforts in mechanistic interpretability research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "398a3b62-6fea-428e-a358-f907f5cadd79"
}
```

</details>

---


### System

_source line 257_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Fetching https://arxiv.org/abs/2602.22968",
  "usage": {
    "total_tokens": 22256,
    "tool_uses": 9,
    "duration_ms": 81927
  },
  "last_tool_name": "WebFetch",
  "uuid": "3cbfa5bc-0b29-45d3-9fe5-d975c59ed1c1",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 258_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H18oQ439dZovxBm6NE6fjF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.22968",
  "prompt": "Extract the full title, all authors, year, venue/status, and detailed description. Does this paper propose combining results from multiple different circuit discovery methods? What are \"Certified Circuits\"? What stability guarantees do they provide? Do they aggregate across methods or just certify a single method's output?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e6a81f17-92c4-42a2-9006-aaa8694642f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4ko1JpsMS83cdZfVVQJHs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 513,
      "cache_read_input_tokens": 21368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 513,
        "ephemeral_1h_input_tokens": 0
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

_source line 259 · 2026-05-12T22:09:14.554Z_

<details><summary>↩ Tool result · `toolu_018pEfpz6FddrVsz2JfLsXp8`</summary>

```text
# Paper Summary

**Title:** "Attribution Patching Outperforms Automated Circuit Discovery"

**Authors:** Aaquib Syed, Can Rager, Arthur Conmy

**Year:** 2023 (submitted October 16, 2023; revised November 20, 2023)

**Venue:** NeurIPS 2023 ATTRIB Workshop

## Abstract Overview

The researchers propose that "a simple method based on attribution patching outperforms all existing methods while requiring just two forward passes and a backward pass." They apply linear approximation to activation patching to assess edge importance and prune less critical network connections.

## Methods Compared

The paper contrasts their attribution patching approach against "existing methods" in automated circuit discovery that utilize activation patching. The specific competing techniques aren't detailed in this abstract.

## Metrics

The evaluation relies on **AUC from circuit recovery** as the primary performance measure. The authors report that "averaged over all tasks our method has greater AUC from circuit recovery than other methods."

## Circuit Overlap Findings

The provided content does not explicitly address circuit overlap comparisons between methods. The abstract focuses on overall AUC performance rather than analyzing overlap patterns among different circuit discovery approaches.

**Note:** Full methodological details would require accessing the complete paper PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "4971a96e-b1fd-4bba-bcd5-f0530c6060b3"
}
```

</details>

---


### System

_source line 260_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"Towards Best Practices of Activation Patching\" I…",
  "usage": {
    "total_tokens": 35683,
    "tool_uses": 23,
    "duration_ms": 73414
  },
  "last_tool_name": "WebSearch",
  "uuid": "0505fc13-a39a-4676-a9ca-a56f6f22a8a8",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 261_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015bdAwxrJKhR1HJroUzZbEZ`</summary>

```json
{
  "query": "\"Towards Best Practices of Activation Patching\" ICLR 2024 circuit metrics methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "dd2315ad-b16d-4ed4-93d0-f990e8824407",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HkpYicKJGz7EKCDW9E9nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 922,
      "cache_creation_input_tokens": 2919,
      "cache_read_input_tokens": 31800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2919,
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

_source line 262_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for ICLR 2024 \"successor heads\" interpretable attenti…",
  "usage": {
    "total_tokens": 35684,
    "tool_uses": 24,
    "duration_ms": 73886
  },
  "last_tool_name": "WebSearch",
  "uuid": "a7af695b-be51-455d-9d0f-df62088ca073",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 263_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MLtFp1fjTU8CoLJpzwFf6y`</summary>

```json
{
  "query": "ICLR 2024 \"successor heads\" interpretable attention circuit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "160a9a3b-3ae6-4505-a51d-368145f49674",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HkpYicKJGz7EKCDW9E9nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 922,
      "cache_creation_input_tokens": 2919,
      "cache_read_input_tokens": 31800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2919,
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

_source line 264 · 2026-05-12T22:09:15.170Z_

<details><summary>↩ Tool result · `toolu_015mPR9GFS3V1AMBW2YNXHvE`</summary>

```text
# Paper Information

**Title:** Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning

**Authors:** Lei Yu, Jingcheng Niu, Zining Zhu, Gerald Penn

**Year:** 2024

**Venue:** ICML (International Conference on Machine Learning)

**Abstract:** The paper introduces a comprehensive reformulation of circuit discovery—interpreting language model computational mechanisms through sparse subnetworks. The authors identify limitations in existing approaches and propose DiscoGP, which achieves state-of-the-art performance by addressing the dichotomy between weight and connection-based pruning.

---

# Method Name and Key Contribution

**Method Name:** DiscoGP (Differentiable Computational Graph Pruning)

**Key Algorithmic Contribution:** DiscoGP enables "joint weight and edge computation graph pruning" by placing "learnable binary mask parameters at the weights of LM components and their interconnecting edges" that are "trained together in an end-to-end manner." This unified approach overcomes prior methods' limitation of choosing between pruning weights or edges alone, allowing simultaneous optimization of both parameter sparsity and structural connectivity in transformer models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "c70fda23-c6fb-4514-a148-a79f4978075b"
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
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for NeurIPS 2024 \"InterpBench\" semi-synthetic transfo…",
  "usage": {
    "total_tokens": 35685,
    "tool_uses": 25,
    "duration_ms": 75436
  },
  "last_tool_name": "WebSearch",
  "uuid": "cdad0735-31f8-4ccd-87e7-bbcccf4e0a42",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 266_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UcqLP2WFBfV54pforRTiPa`</summary>

```json
{
  "query": "NeurIPS 2024 \"InterpBench\" semi-synthetic transformers evaluating mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "1fd00907-4029-4862-9981-eaf4755db5f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HkpYicKJGz7EKCDW9E9nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 922,
      "cache_creation_input_tokens": 2919,
      "cache_read_input_tokens": 31800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2919,
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

_source line 267_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"Automated Circuit Discovery with Provable\" ICLR …",
  "usage": {
    "total_tokens": 35686,
    "tool_uses": 26,
    "duration_ms": 75923
  },
  "last_tool_name": "WebSearch",
  "uuid": "3ddcc60f-6c9f-4229-8d2d-363501f13046",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 268_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QD5ACf6pjBbBAJuY9JosRa`</summary>

```json
{
  "query": "\"Automated Circuit Discovery with Provable\" ICLR 2025 guarantees"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2eddab12-d0c7-4484-8254-e3f8d091e55e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HkpYicKJGz7EKCDW9E9nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 922,
      "cache_creation_input_tokens": 2919,
      "cache_read_input_tokens": 31800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2919,
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

_source line 269 · 2026-05-12T22:09:17.836Z_

<details><summary>↩ Tool result · `toolu_01LjzHWJ9zqfsv7icWVhNyh6`</summary>

```text
# Paper Details

**Title:** Beyond Components: Singular Vector-Based Interpretability of Transformer Circuits

**Authors:** Areeb Ahmad, Abhinav Joshi, Ashutosh Modi (Indian Institute of Technology Kanpur)

**Year:** 2025 (arXiv:2511.20273v1)

**Venue:** arXiv preprint

## Abstract

The authors introduce a fine-grained perspective decomposing transformer attention heads and MLPs into orthogonal singular directions, revealing "superposed and independent computations within a single head." They validate this on standard mechanistic interpretability tasks (IOI, Gender Pronoun, Greater Than), demonstrating that canonical functional heads contain multiple overlapping subfunctions aligned with distinct singular directions.

## Key Method

The core technique involves:

1. **Unified Linear Formulation:** Representing both attention and MLP transformations using augmented matrices that jointly include learned weights and biases, enabling uniform SVD application across components.

2. **Directional Masking:** Applying learnable diagonal masks to singular values across decomposed matrices to identify functionally important directions while maintaining model fidelity through a KL divergence plus sparsity objective.

3. **Logit Receptors:** Discovering that transformer layers contain "inherent fixed directions in logit space" that act as "stable, task-relevant axes" selectively activated via input-dependent scalar coefficients for contextual control.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "76a1956c-8d14-4dfc-b435-48fed3459c6f"
}
```

</details>

---


### Tool result

_source line 270 · 2026-05-12T22:09:19.067Z_

<details><summary>↩ Tool result · `toolu_01H18oQ439dZovxBm6NE6fjF`</summary>

```text
# Paper Summary

**Full Title:** Certified Circuits: Stability Guarantees for Mechanistic Circuits

**Authors:** Alaa Anani, Tobias Lorenz, Bernt Schiele, Mario Fritz, Jonas Fischer

**Year:** 2026 (submitted February 26, 2026)

**Venue/Status:** arXiv preprint (cs.AI, cs.CV, cs.CY); arXiv:2602.22968

---

## What Are Certified Circuits?

Certified Circuits represent a framework that enhances mechanistic circuit discovery by providing formal stability guarantees. Rather than aggregating multiple methods, this approach "wraps any black-box discovery algorithm" with a certification layer—meaning it works with a single method's output to validate robustness.

## Stability Guarantees Provided

The method certifies that circuit component decisions remain "invariant to bounded edit-distance perturbations of the concept dataset." Specifically, it employs randomized data subsampling to verify stability. Neurons judged unstable are excluded, yielding more compact and accurate circuits.

## Method Integration

This paper does **not** propose combining results from multiple circuit discovery methods. Instead, it applies a certification wrapper to validate and stabilize any single existing algorithm's output, improving transferability across out-of-distribution datasets.

**Key Results:** On ImageNet and OOD datasets, certified circuits achieved up to 91% higher accuracy while using 45% fewer neurons than baseline approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "a0a59981-5e89-4e8f-97f5-1f63a0b6b139"
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-12T22:09:22.066Z_

<details><summary>↩ Tool result · `toolu_01MLtFp1fjTU8CoLJpzwFf6y`</summary>

```text
Web search results for query: "ICLR 2024 "successor heads" interpretable attention circuit"

Links: [{"title":"Published as a conference paper at ICLR 2024 SUCCESSOR HEADS:","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/2722a0ccf6acfe3d144fdbb0dedd80b5-Paper-Conference.pdf"},{"title":"Successor Heads: Recurring, Interpretable Attention Heads In The Wild | OpenReview","url":"https://openreview.net/forum?id=kvcbV8KQsi"},{"title":"GitHub - IAAR-Shanghai/Awesome-Attention-Heads: An awesome repository & A comprehensive survey on interpretability of LLM attention heads. · GitHub","url":"https://github.com/IAAR-Shanghai/Awesome-Attention-Heads"},{"title":"Published as a conference paper at ICLR 2024","url":"https://arxiv.org/pdf/2310.08744"},{"title":"Circuits Updates - September 2024","url":"https://transformer-circuits.pub/2024/september-update/index.html"},{"title":"Tutorials","url":"https://projects.illc.uva.nl/indeep/tutorial/"},{"title":"[PDF] Successor Heads: Recurring, Interpretable Attention Heads In The Wild | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Successor-Heads:-Recurring,-Interpretable-Attention-Gould-Ong/07c2c3b4af7e4ff1577f36f47f1c93398a6df648"},{"title":"ICLR 2024 Orals","url":"https://iclr.cc/virtual/2024/events/oral"},{"title":"Published as a conference paper at ICLR 2024","url":"https://health-nlp.com/files/pubs/iclr24a.pdf"},{"title":"ICLR 2024 Schedule","url":"https://iclr.cc/virtual/2024/calendar"}]

Based on the search results, I found comprehensive information about the ICLR 2024 paper on successor heads. Here's what I found:

## Overview

The paper discovered and interpreted a class of attention heads called successor heads, which are attention heads that perform incrementation in language models.

## What Successor Heads Do

The input to a successor head is the representation of a token in an ordinal sequence such as 'Monday', 'first', 'January', or 'one', and the output assigns a higher likelihood to the incremented token, such as 'Tuesday', 'second', 'February', or 'two'. For example, successor heads increment 'Monday' into 'Tuesday'.

## Key Findings

Successor heads form in LLMs with as few as 31 million parameters, and at least as many as 12 billion parameters, such as GPT-2, Pythia, and Llama-2.

The researchers found a set of 'mod 10' features that underlie how successor heads increment in LLMs across different architectures and sizes.

## Mechanistic Interpretability Approach

The successor head behavior is explained with an approach rooted in mechanistic interpretability, the field that aims to explain how models complete tasks in human-understandable terms. The study examines the behavior of successor heads on natural language data, where they find that successor heads are important for achieving low loss on examples involving succession, and also identify interpretable polysemanticity in a Pythia successor head.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "a710e750-260e-483d-9883-20c674efcea0"
}
```

</details>

---


### Tool result

_source line 272 · 2026-05-12T22:09:22.338Z_

<details><summary>↩ Tool result · `toolu_015bdAwxrJKhR1HJroUzZbEZ`</summary>

```text
Web search results for query: ""Towards Best Practices of Activation Patching" ICLR 2024 circuit metrics methods"

Links: [{"title":"TOWARDS BEST PRACTICES OF ACTIVATION PATCH","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/06a52a54c8ee03cd86771136bc91eb1f-Paper-Conference.pdf"},{"title":"Towards Best Practices of Activation Patching in Language Models: Metrics and Methods | OpenReview","url":"https://openreview.net/forum?id=Hf17y6u9BC"},{"title":"[2309.16042] Towards Best Practices of Activation Patching in Language Models: Metrics and Methods","url":"https://arxiv.org/abs/2309.16042"},{"title":"Towards Best Practices of Activation Patching in Language Models: Metrics and Methods","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/06a52a54c8ee03cd86771136bc91eb1f-Abstract-Conference.html"},{"title":"TOWARDS BEST PRACTICES OF ACTIVATION PATCH-","url":"https://arxiv.org/pdf/2309.16042"},{"title":"[PDF] Towards Best Practices of Activation Patching in Language Models: Metrics and Methods | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Towards-Best-Practices-of-Activation-Patching-in-Zhang-Nanda/c16c05ca0a3d24519405849fd24604fc1ce47751"},{"title":"ICLR Poster Towards Best Practices of Activation Patching in Language Models: Metrics and Methods","url":"https://iclr.cc/virtual/2024/poster/18984"},{"title":"[Quick Review] Towards Best Practices of Activation Patching in Language Models: Metrics and Methods","url":"https://liner.com/review/towards-best-practices-of-activation-patching-in-language-models-metrics"},{"title":"Activation Patching: Metrics & Methods","url":"https://www.emergentmind.com/papers/2309.16042"},{"title":"International Conference on Learning Representations 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024"}]

I found the paper you're looking for! Here's information about "Towards Best Practices of Activation Patching" from ICLR 2024:

## Overview

The paper addresses mechanistic interpretability by examining activation patching, also known as causal tracing or interchange intervention—a standard technique for identifying important model components—and systematically examines the impact of methodological details in activation patching, including evaluation metrics and corruption methods.

## Key Findings

The researchers found that varying hyperparameters could lead to disparate interpretability results, and backed by empirical observations, they give conceptual arguments for why certain metrics or methods may be preferred, providing recommendations for best practices of activation patching going forwards.

## Methodology

Activation patching identifies the important model components by intervening on their latent activations. The paper identifies three degrees of freedom in activation patching, focusing on the approach of generating corrupted prompts and evaluating two prominent methods from the literature including ability and logit difference.

The work studies the choice of evaluation metrics in activation patching and performs experiments highlighting potential gaps between logit difference and probability, along with conceptual arguments for why probability can overlook negative components in certain settings.

## Applications

The research empirically examines the impact of these hyperparameters on several interpretability tasks, including factual recall and circuit discovery for indirect object identification (IOI), greater-than, and Python docstring completion.

The paper was published as part of ICLR 2024 by Fred Zhang and Neel Nanda.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "631724d7-9c38-4c44-864c-336274d3447c"
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
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Fetching https://arxiv.org/abs/2407.08734",
  "usage": {
    "total_tokens": 22793,
    "tool_uses": 10,
    "duration_ms": 90277
  },
  "last_tool_name": "WebFetch",
  "uuid": "2610cb21-afa8-40d1-be8a-a3caab6c9e47",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 274_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SEckSv1LPzb8iT8Pm7rVKf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.08734",
  "prompt": "Extract the full title, all authors, year, venue/status. Does this paper compare results across multiple circuit discovery methods? Does it propose aggregating or ensembling circuit outputs from different methods? What is the main finding about faithfulness metrics?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "0a5f8fe5-125c-4dcc-9f0b-f24676aa0fee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWEF8Mm3hxmpojXFEHK91d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 487,
      "cache_read_input_tokens": 21881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 487,
        "ephemeral_1h_input_tokens": 0
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

_source line 275 · 2026-05-12T22:09:22.793Z_

<details><summary>↩ Tool result · `toolu_01Ave17iPJKprkyc6Z862tja`</summary>

```text
Web search results for query: "weight sparse transformers interpretable circuits OpenAI 2025 circuit sparsity"

Links: [{"title":"Weight-sparse transformers have interpretable circuits","url":"https://cdn.openai.com/pdf/41df8f28-d4ef-43e9-aed2-823f9393e470/circuit-sparsity-paper.pdf"},{"title":"[2511.13653] Weight-sparse transformers have interpretable circuits","url":"https://arxiv.org/abs/2511.13653"},{"title":"OpenAI Researchers Train Weight Sparse Transformers to Expose Interpretable Circuits - MarkTechPost","url":"https://www.marktechpost.com/2025/11/14/openai-researchers-train-weight-sparse-transformers-to-expose-interpretable-circuits/"},{"title":"Weight-sparse transformers have interpretable circuits","url":"https://arxiv.org/html/2511.13653v1"},{"title":"OpenAI has Released the 'circuit-sparsity': A Set of Open Tools for Connecting Weight Sparse Models and Dense Baselines through Activation Bridges - MarkTechPost","url":"https://www.marktechpost.com/2025/12/13/openai-has-released-the-circuit-sparsity-a-set-of-open-tools-for-connecting-weight-sparse-models-and-dense-baselines-through-activation-bridges/"},{"title":"Weight-sparse transformers have interpretable circuits [pdf] | Hacker News","url":"https://news.ycombinator.com/item?id=45926371"},{"title":"OpenAI Trains Weight-Sparse Transformers to Reveal Compact, Interpretable Circuits | Timekeeper","url":"https://www.kiadev.net/news/2025-11-15-openai-weight-sparse-transformers-interpretability/"},{"title":"Understanding neural networks through sparse circuits | OpenAI","url":"https://openai.com/index/understanding-neural-networks-through-sparse-circuits/"},{"title":"GitHub - openai/circuit_sparsity: Open-source release accompanying Gao et al. 2025","url":"https://github.com/openai/circuit_sparsity"},{"title":"OpenAI Released Circuit-Sparsity Tools for Models","url":"https://kiadev.net/news/2025-12-14-openai-circuit-sparsity-tools-connection"}]

Based on the search results, here's information about OpenAI's research on weight-sparse transformers and interpretable circuits:

## Overview

OpenAI researchers are working to find human-understandable circuits in language models by training models to have more understandable circuits by constraining most of their weights to be zeros, so that each neuron only has a few connections.

## Training Method

The OpenAI team trains GPT-2 style decoder only transformers so that almost all weights are zero, around 1 in 1000 weights is non zero, enforcing sparsity across all weights and biases including token embeddings, which yields thin connectivity graphs that are structurally easier to analyze. After each AdamW optimizer step they keep only the largest magnitude entries in every weight matrix and bias, including token embeddings, and zero out the rest. An annealing schedule gradually reduces the fraction of nonzero parameters until the model reaches a target sparsity.

## Key Findings

These circuits often contain neurons and residual channels that correspond to natural concepts, with a small number of straightforwardly interpretable connections between them. At matched pre-training loss levels, weight sparse models require circuits that are roughly 16 times smaller than those recovered from dense baselines, defining a capability interpretability frontier where increased sparsity improves interpretability while slightly reducing raw capability.

## Tools and Resources

OpenAI releases the weights and pruned circuits for all sparse models used in the experiments, as well as code for visualizing circuits, at https://github.com/openai/circuit_sparsity/. OpenAI released the 0.4B parameter openai/circuit-sparsity model on Hugging Face and the full openai/circuit_sparsity codebase on GitHub under Apache 2.0.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "7c083a79-5af2-4b9b-b0f5-88265978af23"
}
```

</details>

---


### Tool result

_source line 276 · 2026-05-12T22:09:23.194Z_

<details><summary>↩ Tool result · `toolu_01UcqLP2WFBfV54pforRTiPa`</summary>

```text
Web search results for query: "NeurIPS 2024 "InterpBench" semi-synthetic transformers evaluating mechanistic interpretability"

Links: [{"title":"NeurIPS Poster InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://neurips.cc/virtual/2024/poster/97689"},{"title":"INTERPBENCH: Semi-Synthetic Transformers for ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/a8f7d43ae092d9a5295775eb17f3f4f7-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques | OpenReview","url":"https://openreview.net/forum?id=R9gR9MPuD5"},{"title":"[2407.14494] InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://arxiv.org/abs/2407.14494"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/a8f7d43ae092d9a5295775eb17f3f4f7-Abstract-Datasets_and_Benchmarks_Track.html"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://arxiv.org/html/2407.14494v1"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques | FAR.AI","url":"https://far.ai/research/interpbench-semi-synthetic-transformers-for-evaluating-mechanistic-interpretability-techniques"},{"title":"[Quick Review] InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://liner.com/review/interpbench-semisynthetic-transformers-for-evaluating-mechanistic-interpretability-techniques"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques | Iván Arcuschin Moreno","url":"https://iarcuschin.com/publication/interpbench/"},{"title":"[PDF] InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques | Semantic Scholar","url":"https://www.semanticscholar.org/paper/a9ceeafaa5cffc975fb5aa3d591666fb0ebc47d8"}]

Based on the search results, I found comprehensive information about InterpBench at NeurIPS 2024:

## Overview

InterpBench is a collection of semi-synthetic yet realistic transformers with known circuits for evaluating mechanistic interpretability techniques. It was published on the NeurIPS 2024 Datasets and Benchmarks Track.

## Motivation

Mechanistic interpretability methods aim to identify the algorithm a neural network implements, but it is difficult to validate such methods when the true algorithm is unknown. This work addresses that challenge by creating models with ground truth circuits.

## Methodology

The researchers train simple neural networks using a stricter version of Interchange Intervention Training (IIT) which they call Strict IIT (SIIT), which trains neural networks by aligning their internal computation with a desired high-level causal model, but also prevents non-circuit nodes from affecting the model's output. SIIT models maintain Tracr's original circuit while being more realistic, and can also train transformers with larger circuits, like Indirect Object Identification (IOI).

## Benchmark Composition

The benchmark comprises 86 semi-synthetic, realistic transformers with known circuits designed for evaluating mechanistic interpretability techniques.

## Evaluation Results

The benchmark can be used to evaluate existing mechanistic interpretability techniques, showing that ACDC is substantially better at identifying true circuits than node- and edge-based Subnetwork Probing, but statistically indistinguishable from Edge Attribution Patching with integrated gradients.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "be9ce69e-c80d-47a9-8021-0e63a1f0853d"
}
```

</details>

---


### System

_source line 277_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/html/2510.06811v1",
  "usage": {
    "total_tokens": 33585,
    "tool_uses": 26,
    "duration_ms": 95979
  },
  "last_tool_name": "WebFetch",
  "uuid": "abb5853a-eef5-467b-a7b4-022e3844086d",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 278_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JUiVYW479HEmCpyv2LAvx6`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.06811v1",
  "prompt": "Extract detailed information about the ensemble strategies. Specifically: (1) What base methods are ensembled (EAP-IG, Edge Pruning, etc.)? (2) What score reduction methods are used (mean, max, min)? (3) Does it discuss union/intersection of circuits as binary consensus? (4) What are the specific results - which ensemble strategy works best? (5) Do the authors analyze HOW MUCH different methods agree or disagree on which edges are important?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "3b38f981-6be3-43a1-b5b2-1c1131378394",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Abn8fcQSF25i8VaZGavkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2694,
      "cache_read_input_tokens": 30810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2694,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 279 · 2026-05-12T22:09:25.371Z_

<details><summary>↩ Tool result · `toolu_01QD5ACf6pjBbBAJuY9JosRa`</summary>

```text
Web search results for query: ""Automated Circuit Discovery with Provable" ICLR 2025 guarantees"

Links: [{"title":"ICLR Poster Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://iclr.cc/virtual/2025/poster/31044"},{"title":"(PDF) Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://www.researchgate.net/publication/400970365_Formal_Mechanistic_Interpretability_Automated_Circuit_Discovery_with_Provable_Guarantees"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823v1"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"},{"title":"GitHub - adelaidehsu/CD_Circuit: [ICLR 2025] CD-T: Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition. Paper: https://arxiv.org/abs/2407.00886","url":"https://github.com/adelaidehsu/CD_Circuit"},{"title":"AUTOMATED CIRCUIT DISCOVERY WITH PROVABLE ...","url":"https://openreview.net/pdf/2a96a0e7b48eb87468aa147e202b58c818feecbd.pdf"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f0552f14388d95b19740dee809f5cad1-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025 EFFICIENT AUTOMATED CIRCUIT","url":"https://arxiv.org/pdf/2407.00886"}]

Based on my search results, I found a paper titled "Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees" that appears to be the work you're searching for.

## Key Details

Automated circuit discovery is a central tool in mechanistic interpretability for identifying the internal components of neural networks responsible for specific behaviors. While prior methods have made significant progress, they typically depend on heuristics or approximations and do not offer provable guarantees over continuous input domains for the resulting circuits.

## Provable Guarantees

The work proposes a suite of automated algorithms that yield circuits with provable guarantees, focusing on three types of guarantees: (1) input domain robustness, ensuring the circuit agrees with the model across a continuous input region; (2) robust patching, certifying circuit alignment under continuous patching perturbations; and (3) minimality, formalizing and capturing a wide array of various notions of succinctness.

Interestingly, the work uncovers a diverse set of novel theoretical connections among these three families of guarantees, with critical implications for the convergence of their algorithms.

## Approach and Results

The work introduces a novel algorithmic framework that builds on recent advances in the emerging field of neural network verification, enabling the derivation of circuits with provable guarantees across continuous domains of interest. Experiments with state-of-the-art verifiers on various vision models show that the algorithms yield circuits with substantially stronger robustness guarantees than standard circuit discovery methods.

The paper appears in ICLR 2025 and is available on OpenReview and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "819f6cea-d2ec-4229-8eb8-eb95b777b7ef"
}
```

</details>

---


### System

_source line 280_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://arxiv.org/abs/2511.13653",
  "usage": {
    "total_tokens": 33233,
    "tool_uses": 26,
    "duration_ms": 88583
  },
  "last_tool_name": "WebFetch",
  "uuid": "0b96255e-2562-481a-a5ad-8b804548f975",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 281_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R726EWpnohRnvTCHMMbw2s`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.13653",
  "prompt": "Extract: paper title, full author list, year, venue, and abstract for the weight-sparse transformers paper from OpenAI."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b7021c90-ac23-45ef-8ec0-62dd7a444ccb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mxo1u5yQWfF6LX1755hF9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3225,
      "cache_read_input_tokens": 29651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3225,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 282_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for circuit discovery information flow routes transfo…",
  "usage": {
    "total_tokens": 33303,
    "tool_uses": 27,
    "duration_ms": 89456
  },
  "last_tool_name": "WebSearch",
  "uuid": "9c14e130-9b43-4778-819e-966ed27ebdda",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 283_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QfDuVyM574R2mx2kQF2HWK`</summary>

```json
{
  "query": "circuit discovery information flow routes transformer 2024 2025 new approach ICML NeurIPS ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "43ebb27e-c779-4843-88ef-c9e5f13a7593",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mxo1u5yQWfF6LX1755hF9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3225,
      "cache_read_input_tokens": 29651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3225,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 284_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/html/2510.00845v2",
  "usage": {
    "total_tokens": 33590,
    "tool_uses": 27,
    "duration_ms": 99083
  },
  "last_tool_name": "WebFetch",
  "uuid": "3a6932dd-53ef-4316-bdb5-6aec87d9b450",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 285_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U1FD8PjsuFNdqT922cK5VT`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.00845v2",
  "prompt": "Extract the detailed findings about variance and instability in circuit discovery. Specifically: (1) What sources of variance do they identify? (2) How much do circuits change across different runs/datasets/hyperparameters? (3) Do they measure overlap between circuits found under different conditions? (4) What are their recommendations? (5) Do they compare variance ACROSS different methods (EAP vs ACDC vs Edge Pruning)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2978be62-d7f1-4354-8172-35f44b486026",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Abn8fcQSF25i8VaZGavkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2694,
      "cache_read_input_tokens": 30810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2694,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 286_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for \"binary mask\" circuit discovery consensus voting …",
  "usage": {
    "total_tokens": 33595,
    "tool_uses": 28,
    "duration_ms": 99446
  },
  "last_tool_name": "WebSearch",
  "uuid": "459ebe56-680e-49c8-b35b-d3e6f040f341",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 287_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F46Gh4aSxxrBdE4AukXvfG`</summary>

```json
{
  "query": "\"binary mask\" circuit discovery consensus voting ensemble edges interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "35ef057d-d3af-42bb-9631-f05d4796687b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Abn8fcQSF25i8VaZGavkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2694,
      "cache_read_input_tokens": 30810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2694,
        "ephemeral_1h_input_tokens": 0
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


### Tool result

_source line 288 · 2026-05-12T22:09:26.751Z_

<details><summary>↩ Tool result · `toolu_01SEckSv1LPzb8iT8Pm7rVKf`</summary>

```text
# Paper Summary

**Full Title:** Transformer Circuit Faithfulness Metrics are not Robust

**Authors:** Joseph Miller, Bilal Chughtai, William Saunders

**Year:** 2024

**Venue/Status:** CoLM 2024 Conference Paper (submitted July 11, 2024)

## Key Findings

**Does it compare multiple circuit discovery methods?**
The paper does not appear to focus on comparing different circuit discovery methods themselves. Instead, it examines "a wide range of ablation methodologies" used to *evaluate* circuits.

**Does it propose ensembling/aggregating outputs?**
No aggregation or ensembling of circuit outputs is proposed. The work is diagnostic rather than prescriptive in this regard.

**Main Finding on Faithfulness Metrics:**
The researchers discovered that existing circuit faithfulness measurements are highly unreliable. As stated in the abstract: "existing methods are highly sensitive to seemingly insignificant changes in the ablation methodology." The core conclusion is that "existing circuit faithfulness scores reflect both the methodological choices of researchers as well as the actual components of the circuit." This means the measured performance depends substantially on which ablation technique researchers choose, undermining confidence in circuit evaluation reliability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "6b3d03ff-abaf-49de-9cc3-6b66e794aecb"
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-12T22:09:28.179Z_

<details><summary>↩ Tool result · `toolu_01JUiVYW479HEmCpyv2LAvx6`</summary>

```text
# Ensemble Strategies for Circuit Localization

## Base Methods Ensembled

The paper combines four primary approaches:
- **Three EAP variants**: EAP, EAP-IG-inputs, and EAP-IG-activations
- **Edge pruning**: A computationally expensive but more precise method

The authors note these EAP methods are "designed to be approximations of edge activation patching" and treat their scores as comparable.

## Score Reduction Methods

The researchers experimented with four reduction techniques:

1. **Mean** (unweighted average) - yielded best results
2. **Weighted average**
3. **Maximum** - interpreted as union of circuits
4. **Minimum** - interpreted as intersection of circuits

The paper explicitly states: "taking the maximum corresponds to a union of circuits (edges selected by any method), while the minimum corresponds to an intersection (edges selected by all methods)."

## Union/Intersection as Binary Consensus

Yes, the authors conceptualize reduction methods through this lens. Maximum represents edges selected *by any method*, while minimum represents edges selected *by all methods*—a form of consensus-based circuit identification.

## Best-Performing Strategy

**Hybrid ensemble** achieved superior results, combining parallel and sequential approaches by averaging all four methods. On the private test set, it achieved the lowest CMD score (0.03 average) and highest CPR score (1.83 average).

## Analysis of Method Agreement

**Notably absent**: The paper does not analyze correlation or agreement rates between different methods regarding which edges they identify as important. It focuses on combining scores rather than investigating their concordance patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "dc80123e-5662-4e67-9d13-b18f8dcfa3d4"
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-12T22:09:29.125Z_

<details><summary>↩ Tool result · `toolu_01R726EWpnohRnvTCHMMbw2s`</summary>

```text
# Weight-Sparse Transformers Paper

**Title:** "Weight-sparse transformers have interpretable circuits"

**Authors:** Leo Gao, Achyuta Rajaram, Jacob Coxon, Soham V. Govande, Bowen Baker, Dan Mossing

**Year:** 2025

**Venue:** arXiv (Computer Science > Machine Learning)

**Abstract:** The researchers developed models with constrained weights to enhance circuit interpretability in language models. By enforcing sparsity, each neuron maintains only minimal connections, allowing researchers to identify task-specific circuits containing neurons corresponding to natural concepts. The study reveals that greater sparsity trades capability for interpretability, while larger model sizes improve this capability-interpretability frontier. However, extending sparse models beyond tens of millions of nonzero parameters while maintaining interpretability presents ongoing challenges. The team demonstrated their method can also help explain existing dense models and validated their work with rigorous analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "f5a48bec-f5a9-4c80-8180-17a7a8b5af30"
}
```

</details>

---


### System

_source line 291_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for CIRCUS \"circuit consensus\" stability ensemble mec…",
  "usage": {
    "total_tokens": 23243,
    "tool_uses": 11,
    "duration_ms": 97316
  },
  "last_tool_name": "WebSearch",
  "uuid": "e81c618d-4802-4c9d-a323-ec4975e26a2e",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 292_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VAEWcHtzNmR8ES8WSsWPtv`</summary>

```json
{
  "query": "CIRCUS \"circuit consensus\" stability ensemble mechanistic interpretability multi-method ACDC EAP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "235a0e6b-368d-48a9-b6f3-904bd0b8d0f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5G6Xn56TmGGuX6Er6rYAb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 414,
      "cache_read_input_tokens": 22368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 414,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 293_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Fetching https://openreview.net/forum?id=FbZSZEIkEU",
  "usage": {
    "total_tokens": 39854,
    "tool_uses": 27,
    "duration_ms": 89455
  },
  "last_tool_name": "WebFetch",
  "uuid": "dc123759-f261-479a-bf30-7e4628c22090",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 294_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016mFB7f35iJyMSE2akMjQGH`</summary>

```json
{
  "url": "https://openreview.net/forum?id=FbZSZEIkEU",
  "prompt": "What venue was this paper accepted to? Is it ICLR 2025 or another conference? What is the paper title and decision?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8c9d875a-97b9-46fa-a926-39d676ffac4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWAH73pqjts1M1xPgrJUQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5087,
      "cache_read_input_tokens": 34719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5087,
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

_source line 295_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for ICML 2024 main track \"causal abstraction\" OR \"cir…",
  "usage": {
    "total_tokens": 39855,
    "tool_uses": 28,
    "duration_ms": 90393
  },
  "last_tool_name": "WebSearch",
  "uuid": "5ccb11fd-a01e-4531-bee2-df88fa22b0d6",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 296_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XHZAgdVecb7oY3ZCGm945D`</summary>

```json
{
  "query": "ICML 2024 main track \"causal abstraction\" OR \"circuit\" OR \"mechanistic interpretability\" transformer accepted paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "f7d077d5-f392-4cda-87b9-6f36adfb31f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWAH73pqjts1M1xPgrJUQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5087,
      "cache_read_input_tokens": 34719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5087,
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

_source line 297_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"Scaling and Evaluating Sparse Autoencoders\" ICLR…",
  "usage": {
    "total_tokens": 39856,
    "tool_uses": 29,
    "duration_ms": 90965
  },
  "last_tool_name": "WebSearch",
  "uuid": "2574d5c4-3ada-4860-b102-c00fb5df2620",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 298_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DLxRTifrM7QH1KqADZBuij`</summary>

```json
{
  "query": "\"Scaling and Evaluating Sparse Autoencoders\" ICLR 2025 OpenAI Gao"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "dfe9789a-ccfc-4e7c-a634-53a3dcf7212a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWAH73pqjts1M1xPgrJUQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5087,
      "cache_read_input_tokens": 34719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5087,
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

_source line 299 · 2026-05-12T22:09:32.669Z_

<details><summary>↩ Tool result · `toolu_01U1FD8PjsuFNdqT922cK5VT`</summary>

```text
# Variance and Instability in Circuit Discovery: Key Findings

## (1) Sources of Variance Identified

The paper distinguishes two primary sources of instability:

- **Variance**: Statistical variability when resampling input data used for circuit discovery
- **Robustness**: Stability under controlled changes to analytical setup, including hyperparameter variations and experimental perturbations

## (2) Magnitude of Circuit Changes

The findings reveal substantial instability:

- Bootstrap resampling produced circuits with a Jaccard index of only 0.561, indicating significant structural divergence
- Average circuit error reached 0.440 under bootstrap conditions—notably higher than other resampling approaches
- Hyperparameter variations yielded Jaccard similarities to median circuits ranging from 0.086 to 1.0 on individual tasks

## (3) Overlap Measurements Between Circuits

The researchers employed the Jaccard index extensively to quantify circuit similarity:

- This metric measures structural overlap by calculating `|intersection|/|union|` of edge sets
- Results showed multimodal distributions, suggesting the method can converge to "multiple, distinct, yet stable circuit solutions"
- Different resampling strategies produced substantially different overlap patterns

## (4) Recommendations

The authors propose three key practices:

1. Routinely report stability metrics including variance and coefficient of variation via bootstrap resampling
2. Transparently justify and report all hyperparameter choices with sensitivity analyses
3. Use noise injection as controlled stress tests, suggesting 0.2 amplitude as a reasonable starting point

## (5) Comparison Across Methods

**The paper does not compare variance across different circuit discovery methods.** Their analysis focuses exclusively on EAP-IG variants. While they mention ACDC and other approaches in related work, no direct variance comparisons between different discovery methods appear in the results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "c4c9a28f-482d-4ca4-955a-3649b607001e"
}
```

</details>

---


### Tool result

_source line 300 · 2026-05-12T22:09:33.151Z_

<details><summary>↩ Tool result · `toolu_016mFB7f35iJyMSE2akMjQGH`</summary>

```text
# Paper Submission Information

**Venue:** ICLR 2025 Conference

**Paper Title:** "Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability"

**Decision Status:** The page indicates this is a submission that was "Submitted to ICLR 2025" as of February 5, 2025. However, no acceptance decision is displayed on this OpenReview page. The paper appears to be under review rather than accepted, as there is no explicit acceptance notification provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8cf9f0f5-346f-4c5a-9b83-6219b3302629"
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-12T22:09:33.394Z_

<details><summary>↩ Tool result · `toolu_01F46Gh4aSxxrBdE4AukXvfG`</summary>

```text
Web search results for query: ""binary mask" circuit discovery consensus voting ensemble edges interpretability"

Links: [{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/html/2510.06811"},{"title":"Sparse Feature Circuit Discovery","url":"https://www.emergentmind.com/topics/sparse-feature-circuit-discovery"},{"title":"Towards automated circuit discovery for mechanistic interpretability | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3666841"},{"title":"Voting Ensemble: Hard vs Soft Voting Explained (Python VotingClassifier)","url":"https://mcpanalytics.ai/articles/voting-ensemble-practical-guide-for-data-driven-decisions"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Weight-sparse transformers have interpretable circuits","url":"https://cdn.openai.com/pdf/41df8f28-d4ef-43e9-aed2-823f9393e470/circuit-sparsity-paper.pdf"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Finding Transformer Circuits With Edge Pruning | OpenReview","url":"https://openreview.net/forum?id=8oSY3rA9jY"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"}]

Based on the search results, I found relevant information about your query. Here's what the research shows:

## Circuit Discovery with Ensemble Methods

The Circuit Localization track of the Mechanistic Interpretability Benchmark (MIB) evaluates methods for localizing circuits within large language models (LLMs), and research investigates whether ensembling two or more circuit localization methods can improve performance.

## Ensemble Approaches for Circuit Localization

Two variants of ensembling are explored: parallel and sequential ensembling. In parallel ensembling, attribution scores assigned to each edge by different methods are combined—for example, by averaging or taking the minimum or maximum value.

Interpreting scores as binary indicators, the maximum corresponds to a union of circuits (edges selected by any method), while the minimum corresponds to an intersection (edges selected by all methods). Ultimately, taking the mean yields the best results.

## Binary Masking in Circuit Discovery

Differentiable masking algorithms such as DiscoGP learn binary masks on weights and edges, enabling simultaneous pruning and direct optimization for faithfulness and completeness.

## Consensus Through Voting Mechanisms

The research demonstrates that ensemble methods effectively combine multiple circuit discovery approaches through consensus mechanisms on edge selection. This approach improves circuit identification by balancing different methods' outputs rather than relying on a single discovery technique.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e579f1b2-6b9c-4a55-8b4e-7517e31bc897"
}
```

</details>

---


### System

_source line 302_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for Conmy Mavor-Parker ACDC automated circuit discove…",
  "usage": {
    "total_tokens": 35706,
    "tool_uses": 29,
    "duration_ms": 109532
  },
  "last_tool_name": "WebSearch",
  "uuid": "483d1c4d-20da-4a21-b34e-edcb94394143",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 303_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GMkoAwkFUQfEnUrrnhzWNf`</summary>

```json
{
  "query": "Conmy Mavor-Parker ACDC automated circuit discovery NeurIPS 2023 comparison methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "865f1df0-923b-4065-9d55-fc48988e2fd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuhmvNq2pF9fk59VHxdcyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2109,
      "cache_read_input_tokens": 33504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2109,
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

_source line 304 · 2026-05-12T22:09:37.424Z_

<details><summary>↩ Tool result · `toolu_01QfDuVyM574R2mx2kQF2HWK`</summary>

```text
Web search results for query: "circuit discovery information flow routes transformer 2024 2025 new approach ICML NeurIPS ICLR"

Links: [{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"ICLR 2024 Papers","url":"https://iclr.cc/virtual/2024/papers.html"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"},{"title":"NeurIPS 2024 Papers","url":"https://nips.cc/virtual/2024/papers.html"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"ICLR 2025 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2025%2FConference"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7422317f84e8c83e4c1ad2ff87e1e88e-Paper-Conference.pdf"},{"title":"Foundation AI Models for VLSI Circuit Design and EDA","url":"https://zhiyaoxie.com/files/Survey_CFM.pdf"},{"title":"ICLR 2024 Schedule","url":"https://iclr.cc/virtual/2024/calendar"}]

The search returned general conference pages and navigation content. Let me search more specifically for circuit discovery and mechanistic interpretability research.

Links: [{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Circuits Updates - July 2025","url":"https://transformer-circuits.pub/2025/july-update/index.html"},{"title":"Transformer Circuits Thread","url":"https://transformer-circuits.pub/"},{"title":"[2407.00886] Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/abs/2407.00886"},{"title":"Published as a conference paper at ICLR 2025 EFFICIENT AUTOMATED CIRCUIT","url":"https://arxiv.org/pdf/2407.00886"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/html/2407.00886v3"},{"title":"NeurIPS Poster InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://neurips.cc/virtual/2024/poster/97689"},{"title":"ICLR Poster Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://iclr.cc/virtual/2025/poster/31044"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/html/2510.03282v1"},{"title":"Transcoders find interpretable LLM feature circuits","url":"https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"}]

Based on the web search results, I found several relevant papers on circuit discovery and mechanistic interpretability in transformers from 2024-2025. Here are the key findings:

## Recent Circuit Discovery Research

**Contextual Decomposition for Transformers (CD-T)** - ICLR 2025

A new approach called Contextual Decomposition for Transformers (CD-T) was introduced to build interpretable circuits in large language models, and is the first able to produce circuits as fine-grained as attention heads at specific sequence positions efficiently. Through recursively computing contribution of all nodes in a computational graph of a model using CD-T followed by pruning, circuit discovery runtime can be reduced from hours to seconds compared to state-of-the-art baselines.

On three standard circuit evaluation datasets (indirect object identification, greater-than comparisons, and docstring completion), CD-T outperforms ACDC and EAP by better recovering the manual circuits with an average of 97% ROC AUC under low runtimes.

**Circuit Tracing with Attribution Graphs**

Recent work has followed a two-step approach: first identifying features, interpretable building blocks that the model uses in its computations, and second, describing the processes, or circuits, by which these features interact to produce model outputs. This work is somewhat unique in focusing on attribution graphs for individual prompts, rather than identifying circuits underlying the model's performance of an entire task.

**HAP Framework** - A Hybrid Attribution and Pruning Approach

A hybrid framework called HAP was introduced that resolves the longstanding speed-faithfulness tradeoff in circuit discovery by strategically sequencing EAP with EP, and is 46% faster than EP while maintaining comparable faithfulness.

**InterpBench** - NeurIPS 2024

InterpBench presents a collection of semi-synthetic yet realistic transformers with known circuits for evaluating mechanistic interpretability techniques.

These approaches represent significant advances in automated circuit discovery, addressing challenges of runtime efficiency, fine-grained granularity, and faithfulness in mechanistic interpretability research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "78c3f2a4-7abe-4eb1-9f35-1eecd2f20aff"
}
```

</details>

---


### System

_source line 305_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for \"hybrid attribution pruning\" HAP circuit discover…",
  "usage": {
    "total_tokens": 35707,
    "tool_uses": 30,
    "duration_ms": 110485
  },
  "last_tool_name": "WebSearch",
  "uuid": "34945fba-7b86-403f-8463-1ab4cea6793e",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 306_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MXchZToHBJwAQxEqN1mbkW`</summary>

```json
{
  "query": "\"hybrid attribution pruning\" HAP circuit discovery 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "31121699-ac41-4750-aee7-fb12ba012795",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuhmvNq2pF9fk59VHxdcyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2109,
      "cache_read_input_tokens": 33504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2109,
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

_source line 307 · 2026-05-12T22:09:37.820Z_

<details><summary>↩ Tool result · `toolu_01VAEWcHtzNmR8ES8WSsWPtv`</summary>

```text
Web search results for query: "CIRCUS "circuit consensus" stability ensemble mechanistic interpretability multi-method ACDC EAP"

Links: [{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523v2"},{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG","url":"https://arxiv.org/html/2510.00845v2"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery Aaquib Syed","url":"https://openreview.net/pdf?id=tiLbFR4bJW"},{"title":"Published as a conference paper at ICLR 2025 EFFICIENT AUTOMATED CIRCUIT","url":"https://arxiv.org/pdf/2407.00886"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://arxiv.org/html/2407.14494v2"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Automatic Circuit Discovery","url":"https://sidn.baulab.info/autocircuits/"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Abstract-Conference.html"},{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery · GitHub","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery"}]

Based on the web search results, I found comprehensive information about CIRCUS and related mechanistic interpretability methods. Here are the key findings:

## CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles

CIRCUS addresses the problem that different analyst choices yield different circuits by computing empirical inclusion frequencies over a configuration family, turning analyst-choice variability into a diagnostic. The method constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score (the fraction of configurations that retain it), and extracts a strict-consensus circuit consisting only of edges that appear in all views.

### Core Innovation

The resulting core/contingent/noise taxonomy makes analyst disagreement actionable, and demonstrates that ideas from probabilistic model selection transfer naturally to mechanistic interpretability. This produces a threshold-robust "core" circuit while explicitly surfacing contingent alternatives and enabling rejection of low-agreement structure.

### Performance and Validation

On Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40x smaller than the union of all configurations while retaining comparable influence-flow explanatory power. Causal relevance is validated with activation patching, where consensus-identified nodes consistently beat matched non-consensus controls (p=0.0004).

## Related Methods

The paper also discusses related mechanistic interpretability approaches including ACDC (Automated Circuit Discovery), which employs activation patching to find interpretable circuits, and EAP (Edge Activation Patching with Integrated Gradients), which combines causal patching with gradient-based attribution to score individual edge importance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8efcd33b-8607-4f4a-95fb-36c7636d7b82"
}
```

</details>

---


### System

_source line 308_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for GIM gradient interaction mechanistic interpretabi…",
  "usage": {
    "total_tokens": 35708,
    "tool_uses": 31,
    "duration_ms": 110720
  },
  "last_tool_name": "WebSearch",
  "uuid": "3d347c76-b572-4b48-8959-6fb5599e82a5",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 309_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MjxngZ91kPxsU6Dme8TEPc`</summary>

```json
{
  "query": "GIM gradient interaction mechanistic interpretability benchmark circuit discovery comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "eacda09a-3509-446e-a616-8a6e816dfb51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuhmvNq2pF9fk59VHxdcyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2109,
      "cache_read_input_tokens": 33504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2109,
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

_source line 310 · 2026-05-12T22:09:39.393Z_

<details><summary>↩ Tool result · `toolu_01DLxRTifrM7QH1KqADZBuij`</summary>

```text
Web search results for query: ""Scaling and Evaluating Sparse Autoencoders" ICLR 2025 OpenAI Gao"

Links: [{"title":"Scaling and evaluating sparse autoencoders | OpenReview","url":"https://openreview.net/forum?id=tcsZt9ZNKD"},{"title":"[2406.04093] Scaling and evaluating sparse autoencoders","url":"https://arxiv.org/abs/2406.04093"},{"title":"Scaling and evaluating sparse autoencoders Leo Gao∗ Tom Dupré la Tour†","url":"https://cdn.openai.com/papers/sparse-autoencoders.pdf"},{"title":"Scaling and evaluating sparse autoencoders","url":"https://arxiv.org/html/2406.04093v1"},{"title":"ICLR 2025 Scaling and evaluating sparse autoencoders Oral","url":"https://iclr.cc/virtual/2025/oral/31752"},{"title":"ICLR Poster Scaling and evaluating sparse autoencoders","url":"https://iclr.cc/virtual/2025/poster/28040"},{"title":"[PDF] Scaling and evaluating sparse autoencoders | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scaling-and-evaluating-sparse-autoencoders-Gao-Tour/0d24c5680efe9769e6d7ea579db0499ec819a8c7"},{"title":"SCALING AND EVALUATING SPARSE AUTOENCODERS","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/42ef3308c230942d223c411adf182c88-Paper-Conference.pdf"},{"title":"Scaling and evaluating sparse autoencoders - YouTube","url":"https://www.youtube.com/watch?v=3vYHg9wPzeg"},{"title":"SPARSE AUTOENCODERS DO NOT FIND CANONICAL ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/84ca3f2d9d9bfca13f69b48ea63eb4a5-Paper-Conference.pdf"}]

I found the paper you're looking for! Here are the search results for "Scaling and Evaluating Sparse Autoencoders" from ICLR 2025 by Leo Gao and the OpenAI team:

## Paper Overview

Sparse autoencoders provide a promising unsupervised approach for extracting interpretable features from a language model by reconstructing activations from a sparse bottleneck layer. Since language models learn many concepts, autoencoders need to be very large to recover all relevant features.

## Key Contributions

The researchers propose using k-sparse autoencoders to directly control sparsity, simplifying tuning and improving the reconstruction-sparsity frontier.

They develop a state-of-the-art methodology to reliably train extremely wide and sparse autoencoders with very few dead latents on the activations of any language model, and systematically study the scaling laws with respect to sparsity, autoencoder size, and language model size.

## Scale and Evaluation

The paper introduces several new metrics for evaluating feature quality based on the recovery of hypothesized features, the explainability of activation patterns, and the sparsity of downstream effects, with these metrics all generally improving with autoencoder size.

To demonstrate the scalability of the approach, they train a 16 million latent autoencoder on GPT-4 activations for 40 billion tokens.

## Additional Resources

The researchers release training code and autoencoders for open-source models, as well as a visualizer.

The paper was published in ICLR 2025 and is available through various sources including OpenReview, arXiv (2406.04093), and the official conference proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "99cd51f7-bd80-46cf-bbb1-5efa59413d7a"
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-12T22:09:39.556Z_

<details><summary>↩ Tool result · `toolu_01XHZAgdVecb7oY3ZCGm945D`</summary>

```text
Web search results for query: "ICML 2024 main track "causal abstraction" OR "circuit" OR "mechanistic interpretability" transformer accepted paper"

Links: [{"title":"ICML 2024 Mechanistic Interpretability Workshop","url":"https://icml2024mi.pages.dev/"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"},{"title":"Mechanistic Interpretability for AI Safety — A Review | Leonard F. Bereska","url":"https://leonardbereska.github.io/blog/2024/mechinterpreview/"},{"title":"2024 ICML Mechanistic Interpretability Workshop — Beneficial AI Foundation","url":"https://www.beneficialaifoundation.org/events/2024-buterin-fellows-symposium-kc7za"},{"title":"A Theoretical Foundation for Mechanistic Interpretability","url":"https://jmlr.org/papers/volume26/23-0058/23-0058.pdf"},{"title":"Transformer-Specific Interpretability","url":"https://explanation-llm.github.io/slides/section_4_slides.pdf"},{"title":"Is Causal Abstraction Enough for Mechanistic Interpretability?","url":"https://openreview.net/pdf?id=ZYXTLo7kCi"},{"title":"ICML 2024 Schedule","url":"https://icml.cc/virtual/2024/calendar"},{"title":"Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims","url":"https://arxiv.org/html/2605.08012"},{"title":"ICML 2024","url":"https://joltml.com/icml-2024/"}]

Based on the search results, I found information about mechanistic interpretability research at ICML 2024, though the results primarily show workshop papers rather than main track papers. Here's what I found:

## ICML 2024 Mechanistic Interpretability Workshop

There was a 1 day workshop at ICML on mechanistic interpretability, held on July 27th in Vienna, Austria. This workshop had 93 accepted papers showcasing the latest mechanistic interpretability research.

The prize-winning papers included: First prize ($1000): "The Geometry of Categorical and Hierarchical Concepts in Large Language Models"; Second prize ($500): "InversionView: A General-Purpose Method for Reading Information from Neural Activations"; Third prize ($250): "Hypothesis Testing the Circuit Hypothesis in LLMs"; and honorable mentions including "Missed Causes and Ambiguous Effects: Counterfactuals Pose Challenges for Interpreting Neural Networks" and "Measuring Progress in Dictionary Learning for Language Model Interpretability with Board Game Models."

## Transformer-Related Research

One paper appearing in the ICML 2024 schedule was "StableMask: Refining Causal Masking in Decoder-only Transformer."

## Causal Abstraction Research

Recent work shows how causal abstraction provides a theoretical foundation for mechanistic interpretability, offering definitions for core concepts like polysemantic neurons, the linear representation hypothesis, modular features, and graded faithfulness.

However, the search results primarily focus on the workshop track rather than main conference track papers. If you need specific information about main track accepted papers with these topics, a more targeted search of the official ICML 2024 main conference papers may be necessary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "22a65da0-f32f-469e-90d9-a498cd97f400"
}
```

</details>

---


### System

_source line 312_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for InterpBench semi-synthetic transformers evaluatin…",
  "usage": {
    "total_tokens": 35066,
    "tool_uses": 28,
    "duration_ms": 105120
  },
  "last_tool_name": "WebSearch",
  "uuid": "b2ff03b7-ed06-48b4-9b93-078b655d0386",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 313_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019ABUYiStbm8rH6A7SMzr8y`</summary>

```json
{
  "query": "InterpBench semi-synthetic transformers evaluating mechanistic interpretability NeurIPS 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8283c0e4-4580-4222-b021-8795682b5d3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Aw3viF4DMEy91gRVXEnqq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 32876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1761,
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

_source line 314_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Searching for transcoders interpretable LLM feature circuits 20…",
  "usage": {
    "total_tokens": 35067,
    "tool_uses": 29,
    "duration_ms": 105364
  },
  "last_tool_name": "WebSearch",
  "uuid": "3ab45965-8345-4db1-a81d-0f9ae9bd1b89",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 315_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0193pAZiCBS2zo8wyZFzrCB8`</summary>

```json
{
  "query": "transcoders interpretable LLM feature circuits 2024 sparse autoencoder MLP replacement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "67e6d7a1-4946-4e5c-b47a-c31abf390bdf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Aw3viF4DMEy91gRVXEnqq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 32876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1761,
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

_source line 316_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Fetching https://arxiv.org/html/2603.00523v2",
  "usage": {
    "total_tokens": 24246,
    "tool_uses": 12,
    "duration_ms": 110701
  },
  "last_tool_name": "WebFetch",
  "uuid": "4bb8eec3-987b-407c-8d33-b598bb003259",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 317_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011rvaw39sPqDXXypNHJhUiL`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.00523v2",
  "prompt": "I need to understand if CIRCUS aggregates across MULTIPLE different circuit discovery methods (e.g., ACDC, EAP, SP, attribution patching) or if it only varies hyperparameters (like pruning threshold) within ONE method. Specifically look for: 1) Does it run multiple different circuit discovery algorithms and combine their outputs? 2) Or does it take a single attribution graph and vary the pruning threshold? 3) What \"configuration family\" does it sweep over - just thresholds, or also different methods? 4) Is there any mention of combining outputs from fundamentally different circuit discovery approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b6efd519-820a-4902-95e3-632ec5464882",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TKKdhMvwoMwoDzvwdkgvp1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 933,
      "cache_read_input_tokens": 22782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 933,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 318_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"Adaptive Circuit Behavior\" ICLR 2025 rejected OR…",
  "usage": {
    "total_tokens": 42125,
    "tool_uses": 30,
    "duration_ms": 101816
  },
  "last_tool_name": "WebSearch",
  "uuid": "2129b215-09b4-40bd-904c-f3148977d61a",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 319_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VPAF859wTPpf5WieDN8Saj`</summary>

```json
{
  "query": "\"Adaptive Circuit Behavior\" ICLR 2025 rejected OR accepted decision OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "50968c8e-4968-4d99-88f3-336800fabfa8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMyULSpuhiCRRgcmWD8LL3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 978,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 39806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1286,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 320 · 2026-05-12T22:09:43.872Z_

<details><summary>↩ Tool result · `toolu_01MXchZToHBJwAQxEqN1mbkW`</summary>

```text
Web search results for query: ""hybrid attribution pruning" HAP circuit discovery 2025 arxiv"

Links: [{"title":"[2510.03282] Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/abs/2510.03282"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/html/2510.03282v1"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://www.arxiv.org/pdf/2510.03282"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework | OpenReview","url":"https://openreview.net/forum?id=hhD5MjHtLi"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework | Request PDF","url":"https://www.researchgate.net/publication/396250590_Discovering_Transformer_Circuits_via_a_Hybrid_Attribution_and_Pruning_Framework"},{"title":"[PDF] Finding Transformer Circuits with Edge Pruning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f8ed3401a5f3fb14bbf77da53e132b36102aa0e3"},{"title":"NeurIPS Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://neurips.cc/virtual/2025/127612"},{"title":"[2506.13727] Attribution-guided Pruning for Compression, Circuit Discovery, and Targeted Correction in LLMs","url":"https://arxiv.org/abs/2506.13727"},{"title":"Attribution-Guided Pruning for Insight and Control: Circuit Discovery and Targeted Correction in Small-scale LLMs","url":"https://arxiv.org/html/2506.13727"},{"title":"Attribution-guided Pruning for Compression, Circuit ...","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250613727V/abstract"}]

Based on the search results, I found comprehensive information about the HAP (Hybrid Attribution and Pruning) framework for circuit discovery. Here's what the research presents:

## Overview

The HAP framework uses attribution patching to identify a high-potential subgraph, then applies edge pruning to extract a faithful circuit from it.

## Motivation and Problem

Existing circuit discovery algorithms face a fundamental trade-off: attribution patching is fast but unfaithful to the full model, while edge pruning is faithful but computationally expensive.

## Key Results

HAP is 46% faster than baseline algorithms without sacrificing circuit faithfulness. Additionally, in a case study on the Indirect Object Identification task, the method preserves cooperative circuit components (e.g. S-inhibition heads) that attribution patching methods prune at high sparsity.

## Publication Status

The paper was published on September 30, 2025 as a poster for the Mech Interp Workshop at NeurIPS 2025. The arXiv identifier is 2510.03282.

## Broader Impact

HAP could be an effective approach for improving the scalability of mechanistic interpretability research to larger models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "68cf9f3b-ca01-424f-acde-4569da9a6774"
}
```

</details>

---


### System

_source line 321_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for ICLR 2025 \"Unifying and Verifying Mechanistic Int…",
  "usage": {
    "total_tokens": 42128,
    "tool_uses": 31,
    "duration_ms": 102731
  },
  "last_tool_name": "WebSearch",
  "uuid": "0184b6f1-4830-4d3e-995f-b3fe452edd68",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 322_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Er6oN94mCH8XZuYb2yrPaN`</summary>

```json
{
  "query": "ICLR 2025 \"Unifying and Verifying Mechanistic Interpretations\" group operations circuit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "c1a03184-dc66-41df-ba6e-8ff452d2895c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMyULSpuhiCRRgcmWD8LL3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 978,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 39806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1286,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 323_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for ICML 2025 \"Towards Global-level Mechanistic Inter…",
  "usage": {
    "total_tokens": 42131,
    "tool_uses": 32,
    "duration_ms": 103064
  },
  "last_tool_name": "WebSearch",
  "uuid": "06b6c470-4ce1-4c3d-88e2-1e634a99ba0d",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 324_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MSDetELuL3KLL8G9Avfnsr`</summary>

```json
{
  "query": "ICML 2025 \"Towards Global-level Mechanistic Interpretability\" modular circuits LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "312a8a0b-1fcd-4376-b8e0-244b3d2ab583",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMyULSpuhiCRRgcmWD8LL3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 978,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 39806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1286,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-12T22:09:44.925Z_

<details><summary>↩ Tool result · `toolu_01GMkoAwkFUQfEnUrrnhzWNf`</summary>

```text
Web search results for query: "Conmy Mavor-Parker ACDC automated circuit discovery NeurIPS 2023 comparison methods"

Links: [{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Abstract-Conference.html"},{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery · GitHub","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery"},{"title":"Structure and Interpretation of Deep Networks","url":"https://sidn.baulab.info/autocircuits/"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"[Quick Review] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://liner.com/review/towards-automated-circuit-discovery-for-mechanistic-interpretability"},{"title":"Towards automated circuit discovery for mechanistic interpretability | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3666841"},{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery/tree/main"},{"title":"The Persistent Vulnerability of Aligned AI Systems","url":"https://arxiv.org/html/2604.00324v1"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery Aaquib Syed","url":"https://openreview.net/pdf?id=tiLbFR4bJW"},{"title":"AI Alignment Research | PhD student at UCL researching AI Alignment, mechanistic interpretability, and AI safety. Former MATS scholar with Stephen Casper.","url":"https://www.aenguslynch.com/"}]

I found comprehensive information about the ACDC paper from NeurIPS 2023. Here's what the search revealed:

## Paper Overview

The paper "Towards Automated Circuit Discovery for Mechanistic Interpretability" was authored by Arthur Conmy, Augustine Mavor-Parker, Aengus Lynch, Stefan Heimersheim, and Adrià Garriga-Alonso and presented at NeurIPS 2023.

## Main Contribution

The paper automates the process of finding connections between abstract neural network units that form a circuit, and proposes several algorithms to reproduce previous interpretability results.

## Algorithm Performance

The ACDC algorithm rediscovered 5/5 of the component types in a circuit in GPT-2 Small that computes the Greater-Than operation, and ACDC selected 68 of the 32,000 edges in GPT-2 Small, all of which were manually found by previous work.

## Comparison Methods

The paper introduces two baselines: Subnetwork Probing (SP) and Head Importance Score for Pruning (HISP), where SP optimizes a mask over model components using gradient descent, while HISP uses a first-order Taylor approximation to estimate the effect of replacing a head's output with corrupted inputs.

## Performance Comparison Results

The ACDC algorithm demonstrates strong effectiveness in identifying correct subgraphs for various tasks, often outperforming Subnetwork Probing (SP) and Head Importance Score for Pruning (HISP). On the Docstring task, ACDC achieved an AUC of 0.982 for edge-level ROC curves when optimizing for KL divergence, significantly higher than HISP (0.805) and SP (0.937), and for the Greater-Than task, ACDC yielded an AUC of 0.853, surpassing HISP (0.693) and SP (0.806).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "c6e13caf-2a21-42f2-a0ac-371552a3c766"
}
```

</details>

---


### Tool result

_source line 326 · 2026-05-12T22:09:45.993Z_

<details><summary>↩ Tool result · `toolu_019ABUYiStbm8rH6A7SMzr8y`</summary>

```text
Web search results for query: "InterpBench semi-synthetic transformers evaluating mechanistic interpretability NeurIPS 2024 authors"

Links: [{"title":"NeurIPS Poster InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://neurips.cc/virtual/2024/poster/97689"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques | OpenReview","url":"https://openreview.net/forum?id=R9gR9MPuD5"},{"title":"INTERPBENCH: Semi-Synthetic Transformers for ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/a8f7d43ae092d9a5295775eb17f3f4f7-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"[2407.14494] InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://arxiv.org/abs/2407.14494"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/a8f7d43ae092d9a5295775eb17f3f4f7-Abstract-Datasets_and_Benchmarks_Track.html"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://arxiv.org/html/2407.14494v1"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques | Iván Arcuschin Moreno","url":"https://iarcuschin.com/publication/interpbench/"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques | FAR.AI","url":"https://far.ai/research/interpbench-semi-synthetic-transformers-for-evaluating-mechanistic-interpretability-techniques"},{"title":"[Quick Review] InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://liner.com/review/interpbench-semisynthetic-transformers-for-evaluating-mechanistic-interpretability-techniques"},{"title":"[PDF] InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques | Semantic Scholar","url":"https://www.semanticscholar.org/paper/a9ceeafaa5cffc975fb5aa3d591666fb0ebc47d8"}]

Based on the search results, I found the information about InterpBench and its authors:

The authors of InterpBench are Rohan Gupta, Iván Arcuschin, Thomas Kwa, and Adrià Garriga-Alonso.

InterpBench is a collection of semi-synthetic yet realistic transformers with known circuits for evaluating mechanistic interpretability techniques, and the authors train neural networks using a stricter version of Interchange Intervention Training (IIT) which they call Strict IIT (SIIT).

The paper was published at NeurIPS 2024 in the Datasets and Benchmarks track.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "542f7e3c-3e1e-4813-b7e5-beaee5f738f0"
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-12T22:09:46.348Z_

<details><summary>↩ Tool result · `toolu_01MjxngZ91kPxsU6Dme8TEPc`</summary>

```text
Web search results for query: "GIM gradient interaction mechanistic interpretability benchmark circuit discovery comparison"

Links: [{"title":"Corti introduces GIM: Benchmark-leading method for understanding AI model behavior | Corti","url":"https://www.corti.ai/stories/gim-a-new-standard-for-mechanistic-interpretability"},{"title":"GIM: Improved Interpretability for Large Language Models","url":"https://arxiv.org/html/2505.17630"},{"title":"Prune, Interpret, Evaluate (PIE ): A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution","url":"https://arxiv.org/html/2604.16889"},{"title":"EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification","url":"https://arxiv.org/html/2502.06852v1"},{"title":"mib-bench (Mechanistic Interpretability Benchmark)","url":"https://huggingface.co/mib-bench"},{"title":"(PDF) Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://www.researchgate.net/publication/400970365_Formal_Mechanistic_Interpretability_Automated_Circuit_Discovery_with_Provable_Guarantees"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823"}]

Based on the search results, here's a comprehensive overview of GIM and its position in mechanistic interpretability:

## GIM Overview

GIM (Gradient Interaction Modifications) is a gradient-based method that achieves the highest known accuracy for identifying which components in a model are responsible for specific behaviors. GIM is a novel gradient-based attribution method that combines three complementary techniques to address feature interactions in transformer components.

## Benchmark Performance

GIM tops the Hugging Face Mechanistic Interpretability Benchmark, the industry standard maintained by researchers from MIT, Stanford, Cambridge, Boston, and ETH Zurich. This means GIM can identify the circuits behind specific model behaviors faster, cheaper, and more accurately than any other available method.

## Circuit Discovery Comparison

GIM is compared with various circuit discovery methods including Edge Activation Patching (EActP), Edge Attribution Patching (EAP), EAP with integrated gradients (EAP-IG), Node Attribution Patching (NAP), Information Flow Routes (IFR), and Uniform Gradient Sampling (UGS).

GIM is more faithful than other gradient-based circuit identification methods and significantly outperforms other circuit identification methods in early layers, while Integrated Gradients demonstrates slight advantages in middle and late layers.

## Technical Strengths

GIM demonstrates greater faithfulness than other gradient-based circuit identification and feature attribution methods across multiple large language models (Gemma 2B/9B, LLAMA 1B/3B/8B, and Qwen 1.5B/3B) and six datasets spanning four tasks (question-answering, fact-verification, sentiment classification, and hate speech detection).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "6775f65e-cc64-4c82-88a9-5790836955f5"
}
```

</details>

---


### Tool result

_source line 328 · 2026-05-12T22:09:47.403Z_

<details><summary>↩ Tool result · `toolu_011rvaw39sPqDXXypNHJhUiL`</summary>

```text
# CIRCUS: Single Method, Multiple Configurations

CIRCUS does **not** aggregate across different circuit discovery methods. Instead, it varies hyperparameters within a single attribution-based approach.

## Key Finding

The method operates on "one attribution run" with a single attribution graph, then applies different pruning configurations:

> "one attribution run, BB non-nested configurations, frequency-based inclusion scores"

## Configuration Family

The "configuration family" consists exclusively of **pruning threshold variations**, not different algorithmic approaches. Specifically, CIRCUS crosses node and edge cumulative-influence thresholds in opposite directions to create non-nested views of the same graph.

For example, the paper mentions configurations like `(0.6,0.99)` and `(0.9,0.95)`, where the numbers represent different threshold pairs applied to the same underlying attribution graph.

## Why This Matters

The authors explicitly state the design principle: configurations must be "non-nested" to avoid degenerating to a single view. This constraint only makes sense within one method's output space—comparing fundamentally different circuit discovery algorithms would not naturally satisfy this mathematical requirement.

**Conclusion**: CIRCUS addresses uncertainty from analyst choices (threshold selection) within a single attribution method, not uncertainty from choosing between different circuit discovery approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8f8b47bb-9d73-4cd3-990c-484a533cf4df"
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-12T22:09:48.770Z_

<details><summary>↩ Tool result · `toolu_01Er6oN94mCH8XZuYb2yrPaN`</summary>

```text
Web search results for query: "ICLR 2025 "Unifying and Verifying Mechanistic Interpretations" group operations circuit"

Links: [{"title":"Unifying and Verifying Mechanistic Interpretations: A Case Study with Group Operations","url":"https://arxiv.org/html/2410.07476v2"},{"title":"Unifying and Verifying Mechanistic Interpretations: A Case Study with Group Operations | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/unifying-verifying-mechanistic-interpretations-case-study-group"},{"title":"Unifying and Verifying Mechanistic Interpretations: A Case Study ...","url":"https://www.researchgate.net/publication/384811373_Unifying_and_Verifying_Mechanistic_Interpretations_A_Case_Study_with_Group_Operations"}]

Based on the search results, I found information about the paper you're looking for:

The paper focuses on mechanistic interpretability research examining how neural networks reverse-engineer the computation performed when trained on the binary operation of finite groups.

The research evaluates the completeness of mechanistic explanations by translating them into a compact proof of model performance, leveraging interpretations to efficiently compute guarantees on the model's global accuracy.

The paper titled "Unifying and Verifying Mechanistic Interpretations: A Case Study with Group Operations" appears to be available on arXiv (version 2 from October 11, 2024). It represents a contribution to the field of mechanistic interpretability in neural networks, specifically examining how models learn and execute group operations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "0800ab62-6f26-454a-b480-07751bd6847a"
}
```

</details>

---


### Tool result

_source line 330 · 2026-05-12T22:09:49.110Z_

<details><summary>↩ Tool result · `toolu_01VPAF859wTPpf5WieDN8Saj`</summary>

```text
Web search results for query: ""Adaptive Circuit Behavior" ICLR 2025 rejected OR accepted decision OpenReview"

Links: [{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=FbZSZEIkEU"},{"title":"ICLR 2025 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2025%2FConference"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"ICLR 2025 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?page=163&venue=ICLR.cc/2025/Conference"},{"title":"ICLR 2025 Conference Submissions","url":"https://openreview.net/submissions?page=233&venue=ICLR.cc/2025/Conference"},{"title":"ICLR 2025 | OpenReview","url":"https://openreview.net/group?id=ICLR.cc/2025"},{"title":"Published as a conference paper at ICLR 2025 THE COMPUTATIONAL COMPLEXITY OF","url":"https://openreview.net/pdf?id=QogcGNXJVw"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"ICLR 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2025-paper-list/"},{"title":"ICLR 2026","url":"https://iclr.cc/"}]

Based on the web search results, I found information about a paper titled "Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability" on OpenReview.

The paper appears to focus on mechanistic interpretability and how well circuits generalize across various prompt formats for the same task. The findings reveal that the circuit generalizes surprisingly well, reusing all of its components and mechanisms while only adding additional input edges.

However, the search results do not explicitly show the final decision status (accepted or rejected) for this paper at ICLR 2025. The paper was found on OpenReview with a submission dated October 4, 2024, but the specific acceptance or rejection decision is not visible in the search results returned. To find the definitive decision status, you may need to visit the paper's OpenReview page directly at the URL found in the search results (https://openreview.net/forum?id=FbZSZEIkEU).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e2db2ef8-6ac5-446e-a7e5-3868fbb2df84"
}
```

</details>

---


### System

_source line 331_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for \"multi-method\" OR \"cross-method\" OR \"method-agnos…",
  "usage": {
    "total_tokens": 24797,
    "tool_uses": 13,
    "duration_ms": 118043
  },
  "last_tool_name": "WebSearch",
  "uuid": "cfd33896-45ca-4d4c-9dea-b350b3508902",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 332_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L4C98a8ujfwodgr6KFCo27`</summary>

```json
{
  "query": "\"multi-method\" OR \"cross-method\" OR \"method-agnostic\" circuit discovery aggregation interpretability 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "70129540-9172-4c8b-9fac-0e2ac3f4d5a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCsvRpZ2ko4mJojZMkoQYi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 508,
      "cache_read_input_tokens": 23715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 508,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-12T22:09:50.470Z_

<details><summary>↩ Tool result · `toolu_01MSDetELuL3KLL8G9Avfnsr`</summary>

```text
Web search results for query: "ICML 2025 "Towards Global-level Mechanistic Interpretability" modular circuits LLM"

Links: [{"title":"ICML Poster Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models","url":"https://icml.cc/virtual/2025/poster/44616"},{"title":"Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=do5vVfKEXZ"},{"title":"Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models","url":"https://proceedings.mlr.press/v267/he25x.html"},{"title":"ICML 2025 Schedule","url":"https://icml.cc/virtual/2025/calendar"}]

I found the paper you were looking for! Here are the key results:

Mechanistic interpretability (MI) research aims to understand large language models (LLMs) by identifying computational circuits, subgraphs of model components with associated functional interpretations, that explain specific behaviors.

The paper titled "Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models" was presented as a poster at ICML 2025. Current MI approaches focus on discovering task-specific circuits, which has two key limitations: (1) poor generalizability across different language tasks, and (2) high costs associated with requiring human or advanced LLM interpretation of each computational node.

The paper proposes a novel framework called ModCirc. The authors propose developing a "modular circuit (MC) vocabulary" consisting of task-agnostic functional units, and present ModCirc, a novel global-level mechanistic interpretability framework for discovering MC vocabularies in LLMs. This method creates a vocabulary of reusable components with pre-established interpretations, dramatically reducing the cost of understanding new AI behaviors.

The paper is available through multiple sources including the ICML conference website, OpenReview, and the official PMLR proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "42538456-d7cc-494c-95c0-e189751a13f2"
}
```

</details>

---


### System

_source line 334_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/abs/2505.17630",
  "usage": {
    "total_tokens": 38640,
    "tool_uses": 32,
    "duration_ms": 123796
  },
  "last_tool_name": "WebFetch",
  "uuid": "954244f2-f900-47e4-b408-d05c7319a643",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 335_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0142A2WDtkSfWbt7dAu1iNHk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.17630",
  "prompt": "Extract the full title, authors, year, abstract. What methods does GIM compare against? Does it measure overlap or agreement between circuits found by different methods? What are the key findings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "6a99f764-231a-4a21-ae87-83641209c8a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jg5VH8Q8Cp2whacf816AiJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2930,
      "cache_read_input_tokens": 35613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2930,
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

_source line 336 · 2026-05-12T22:09:51.119Z_

<details><summary>↩ Tool result · `toolu_0193pAZiCBS2zo8wyZFzrCB8`</summary>

```text
Web search results for query: "transcoders interpretable LLM feature circuits 2024 sparse autoencoder MLP replacement"

Links: [{"title":"[2406.11944] Transcoders Find Interpretable LLM Feature Circuits","url":"https://arxiv.org/abs/2406.11944"},{"title":"NeurIPS Poster Transcoders find interpretable LLM feature circuits","url":"https://neurips.cc/virtual/2024/poster/95736"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Transcoders Find Interpretable LLM Feature Circuits Jacob Dunefsky∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2b8f4db0464cc5b6e9d5e6bea4b9f308-Paper-Conference.pdf"},{"title":"Transcoders find interpretable LLM feature circuits | OpenReview","url":"https://openreview.net/forum?id=J6zHcScAo0&noteId=aOaSSMtgfp"},{"title":"Transcoders Beat Sparse Autoencoders for Interpretability","url":"https://arxiv.org/html/2501.18823v1"},{"title":"Transcoders Find Interpretable LLM Feature Circuits","url":"https://arxiv.org/html/2406.11944v1"},{"title":"Transcoders Find Interpretable LLM Feature Circuits [Quick Review]","url":"https://liner.com/review/transcoders-find-interpretable-llm-feature-circuits"},{"title":"Transcoders find interpretable LLM feature circuits","url":"https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"},{"title":"Transcoders find interpretable LLM feature circuits | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738684"}]

Based on the search results, here's comprehensive information about transcoders for interpretable LLM feature circuits:

## Overview

Transcoders seek to faithfully approximate a densely activating MLP layer with a wider, sparsely-activating MLP layer. This approach addresses the challenge that MLP sublayers make fine-grained circuit analysis on transformer-based language models difficult, particularly because interpretable features are typically linear combinations of extremely many neurons, each with its own nonlinearity to account for.

## Key Differences from SAEs

Transcoders were originally conceived as a variant of SAEs and have many similarities in architecture, but differ in how they are trained: SAEs measure reconstruction error between the SAE's output and its original input, while transcoders measure error between the transcoder's output and the original MLP sublayer's output.

## Performance and Methodology

Transcoders have been successfully trained on language models with 120M, 410M, and 1.4B parameters, and perform at least on par with SAEs in terms of sparsity, faithfulness, and human-interpretability.

A novel method uses transcoders to perform weights-based circuit analysis through MLP sublayers, with resulting circuits factorizing into input-dependent and input-invariant terms.

## Recent Developments (2025)

Unlike SAEs, transcoders approximate the input-output function of a target component, such as an MLP, using a sparse bottleneck. Recent work recommends shifting focus from sparse autoencoders trained on MLP outputs toward skip transcoders, which add a linear skip connection to improve the transcoder's ability to approximate the original MLP without compromising interpretability scores.

Cross-layer transcoders (CLT) can substitute learned CLT features for a model's MLPs while matching the underlying model's outputs in approximately 50% of cases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "09ca8a22-8b3d-4bcc-97fe-e9d9a867bda7"
}
```

</details>

---


### System

_source line 337_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Searching for \"do different circuit discovery methods agree\" OR…",
  "usage": {
    "total_tokens": 38641,
    "tool_uses": 33,
    "duration_ms": 124707
  },
  "last_tool_name": "WebSearch",
  "uuid": "07f7e2f0-fab7-424c-8dd8-53e147420202",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 338_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LEbv5Ah5iAxLTqALbjfwiw`</summary>

```json
{
  "query": "\"do different circuit discovery methods agree\" OR \"circuit overlap between methods\" OR \"which edges important across methods\" interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "f65aae37-0998-4457-a865-c95172bf1598",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jg5VH8Q8Cp2whacf816AiJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2930,
      "cache_read_input_tokens": 35613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2930,
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

_source line 339_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Fetching https://arxiv.org/abs/2510.03282",
  "usage": {
    "total_tokens": 38642,
    "tool_uses": 34,
    "duration_ms": 125411
  },
  "last_tool_name": "WebFetch",
  "uuid": "d0c5c40f-afe2-4e51-9432-905b8715102b",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 340_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ax3g4Hq7GPFyhfH4nvNvqz`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.03282",
  "prompt": "Extract the full title, authors, year, abstract. What methods does it compare? Does it analyze agreement between circuits found by different methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2acb985a-f016-4d6f-96fd-9b25c462ede5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jg5VH8Q8Cp2whacf816AiJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2930,
      "cache_read_input_tokens": 35613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2930,
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

_source line 341_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Fetching https://arxiv.org/abs/2406.11944",
  "usage": {
    "total_tokens": 37146,
    "tool_uses": 30,
    "duration_ms": 116787
  },
  "last_tool_name": "WebFetch",
  "uuid": "edd4a840-0665-4456-b58e-04800c76d1a2",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 342_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GTqCrEd1XKMq1USXQo8FtF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.11944",
  "prompt": "Extract: paper title, full author list, year, venue, and abstract for the Transcoders paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "c4a1c5b7-3725-47fc-a17c-47f114c745a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FopDHeHFpHtWbyDZE13eWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2009,
      "cache_read_input_tokens": 34637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2009,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 343_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Fetching https://openreview.net/forum?id=FbZSZEIkEU",
  "usage": {
    "total_tokens": 44114,
    "tool_uses": 33,
    "duration_ms": 112877
  },
  "last_tool_name": "WebFetch",
  "uuid": "6bc0541a-f227-4831-944f-529f82695a77",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 344_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0175EPdjxW8pJG2W4furgZp1`</summary>

```json
{
  "url": "https://openreview.net/forum?id=FbZSZEIkEU",
  "prompt": "What is the final decision on this paper? Was it accepted or rejected at ICLR 2025? Look for any decision tag, acceptance notification, or rejection notification."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "29fbb87c-655b-4b62-be8c-0f36018c22ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Fvkd8UzPj14GN4Cyc8AmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2894,
      "cache_read_input_tokens": 41092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2894,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 345_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for \"Unifying and Verifying Mechanistic Interpretatio…",
  "usage": {
    "total_tokens": 44180,
    "tool_uses": 34,
    "duration_ms": 113212
  },
  "last_tool_name": "WebSearch",
  "uuid": "98df1d09-8778-431a-801d-a061c4e96fec",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 346_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018gVwBBZksLbZcJerWrsE94`</summary>

```json
{
  "query": "\"Unifying and Verifying Mechanistic Interpretations\" ICLR 2025 published conference paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e43ba656-2cc0-4363-bbac-c748459409c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Fvkd8UzPj14GN4Cyc8AmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2894,
      "cache_read_input_tokens": 41092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2894,
        "ephemeral_1h_input_tokens": 0
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

_source line 347 · 2026-05-12T22:09:56.207Z_

<details><summary>↩ Tool result · `toolu_0142A2WDtkSfWbt7dAu1iNHk`</summary>

```text
# GIM: Improved Interpretability for Large Language Models

**Full Title:** GIM: Improved Interpretability for Large Language Models

**Authors:** Joakim Edin, Róbert Csordás, Tuukka Ruotsalo, Zhengxuan Wu, Maria Maistro, Casper L. Christensen, Jing Huang, Lars Maaløe

**Year:** 2025 (submitted May 23, 2025; last revised October 1, 2025)

**Abstract:**
The paper addresses faithful interpretability in LLMs by identifying a novel self-repair mechanism within attention. The researchers note that "softmax redistribution conceals the influence of important attention scores," causing traditional methods to underestimate component significance. They introduce Gradient Interaction Modifications (GIM) to account for self-repair during backpropagation, testing across multiple models (Gemma, LLAMA, Qwen) and demonstrating improved faithfulness.

## Methods Compared Against

The paper compares GIM against "circuit identification and feature attribution methods," though specific method names aren't detailed in the provided abstract section.

## Overlap/Agreement Measurement

The excerpt does not specify whether the paper measures overlap or agreement between circuits identified by different methods.

## Key Findings

- GIM identifies a previously undocumented self-repair phenomenon in attention mechanisms
- The technique significantly improves faithfulness over existing interpretability approaches
- Results are validated across multiple LLM architectures and diverse tasks
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "034278f6-3cc6-4422-84be-8061663d45f2"
}
```

</details>

---


### Tool result

_source line 348 · 2026-05-12T22:09:56.215Z_

<details><summary>↩ Tool result · `toolu_0175EPdjxW8pJG2W4furgZp1`</summary>

```text
Based on the content provided, there is no decision information visible on this page. The document shows a paper submission to ICLR 2025 with metadata indicating it was "Submitted to ICLR 2025" and last modified on "05 Feb 2025," but there is no acceptance or rejection notification present in the displayed content.

To find the final decision, you would likely need to check the full OpenReview page or wait for the official ICLR 2025 decision announcements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "85420174-1707-4a29-bc92-742e3e5867dd"
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-12T22:09:57.122Z_

<details><summary>↩ Tool result · `toolu_01GTqCrEd1XKMq1USXQo8FtF`</summary>

```text
# Transcoders Paper Details

**Title:** "Transcoders Find Interpretable LLM Feature Circuits"

**Authors:** Jacob Dunefsky, Philippe Chlenski, Neel Nanda

**Year:** 2024

**Venue:** NeurIPS 2024

**Abstract:** The paper addresses circuit analysis in transformer models by introducing transcoders—wider, sparsely-activating MLP layers that approximate densely-activating ones. The authors present "a novel method for using transcoders to perform weights-based circuit analysis through MLP sublayers." They successfully trained transcoders on language models ranging from 120M to 1.4B parameters, achieving performance comparable to sparse autoencoders in sparsity, faithfulness, and interpretability. The work includes reverse-engineering of the "greater-than circuit" in GPT2-small, demonstrating that transcoders effectively decompose model computations involving MLPs into interpretable components.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "9c8181a0-e34f-4da0-93c7-4bf32c62445e"
}
```

</details>

---


### Tool result

_source line 350 · 2026-05-12T22:09:57.463Z_

<details><summary>↩ Tool result · `toolu_01Ax3g4Hq7GPFyhfH4nvNvqz`</summary>

```text
# Paper Summary

**Full Title:** "Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework"

**Authors:** Hao Gu, Vibhas Nair, Amrithaa Ashok Kumar, Jayvart Sharma, Ryan Lagasse

**Year:** 2025 (submitted September 28, 2025)

**Abstract:** The researchers propose HAP (hybrid attribution and pruning), a framework that combines two existing approaches for circuit discovery. The method uses "attribution patching to identify a high-potential subgraph, then applies edge pruning to extract a faithful circuit from it." They report 46% speed improvements over baseline methods while maintaining circuit faithfulness.

## Methods Compared

The paper compares two traditional circuit discovery approaches:
1. **Attribution patching** — faster but less accurate to the full model
2. **Edge pruning** — more accurate but computationally expensive

## Circuit Agreement Analysis

Yes, the paper addresses differences between methods. The authors present a case study on the Indirect Object Identification task demonstrating that their hybrid approach "preserves cooperative circuit components (e.g. S-inhibition heads) that attribution patching methods prune at high sparsity," showing where traditional attribution methods miss important components that their approach captures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "3e1fee01-4729-4b16-9610-7a2b20095063"
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-12T22:09:58.510Z_

<details><summary>↩ Tool result · `toolu_01L4C98a8ujfwodgr6KFCo27`</summary>

```text
Web search results for query: ""multi-method" OR "cross-method" OR "method-agnostic" circuit discovery aggregation interpretability 2024 2025 2026"

Links: [{"title":"Automated Interpretability-Driven Model Auditing and Control: A Research Agenda","url":"https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"},{"title":"Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/html/2510.14936"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=FbZSZEIkEU"},{"title":"Position-aware Automatic Circuit Discovery","url":"https://aclanthology.org/2025.acl-long.141.pdf"},{"title":"(PDF) Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://www.researchgate.net/publication/400970365_Formal_Mechanistic_Interpretability_Automated_Circuit_Discovery_with_Provable_Guarantees"}]

I found several relevant results on circuit discovery and mechanistic interpretability research from 2024-2026. Here are the key findings:

## Recent Circuit Discovery Advances

Sparse Crosscoders (introduced by Lindsey et al., 2024) are a variant of SAEs/transcoders that map activations across multiple layers and models into a shared feature space, enabling interpretable, cross-layer and cross-model comparisons.

Query Circuits (Wu and Barez, 2025) introduced a method to trace the specific information flow for a single input query, bridging the gap between global circuits and local explanations.

## Interpretability Methods and Tools

A series of works has focused on building automated interpretability pipelines for LLMs (Choi et al., 2024; Paulo et al., 2025a; Puri et al., 2025; Gur-Arieh et al., 2025).

Later studies extend interpretability pipelines to SAE features, which are generally more interpretable and often monosemantic (Templeton et al., 2024; Gur-Arieh et al., 2025; Paulo et al., 2025a; Puri et al., 2025).

## Evaluation and Benchmarking

The Mechanistic Interpretability Benchmark (MIB) establishes two evaluation tracks—circuit localization and causal variable localization—across diverse tasks (IOI, arithmetic, MCQA, ARC) and models. Circuit localization metrics include faithfulness integral (CPR), minimality, and AUROC where ground-truth is available, while causal variable localization leverages IIA, DBM, PCA, SAE, and DAS featurizers.

## Position-Aware Circuit Discovery

In position-aware circuits, the same edge can be distinguished at different positions, yielding better trade-offs between circuit size and faithfulness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "c7ee1f08-a586-4067-bca2-731a0011c175"
}
```

</details>

---


### Tool result

_source line 352 · 2026-05-12T22:09:59.020Z_

<details><summary>↩ Tool result · `toolu_01LEbv5Ah5iAxLTqALbjfwiw`</summary>

```text
Web search results for query: ""do different circuit discovery methods agree" OR "circuit overlap between methods" OR "which edges important across methods" interpretability"

Links: [{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823v1"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"},{"title":"(PDF) Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://www.researchgate.net/publication/400970365_Formal_Mechanistic_Interpretability_Automated_Circuit_Discovery_with_Provable_Guarantees"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms","url":"https://arxiv.org/html/2403.17806v1"},{"title":"(PDF) Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://www.researchgate.net/publication/370417693_Towards_Automated_Circuit_Discovery_for_Mechanistic_Interpretability"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"}]

Based on the search results, I found relevant research on circuit discovery methods and their agreement/overlap in mechanistic interpretability:

## Key Findings

Research shows that circuits found using different methods (EAP and EAP-IG) have high node overlap, but the paper concludes that when using circuits to compare mechanisms, faithfulness, not overlap, is what should be measured.

When circuit overlap is moderate, it does not predict faithfulness—for example, node overlap between different tasks can be 0.58, but faithfulness values vary dramatically from 0.61 to 0.2, leading to the conclusion that overlap is not a good predictor of cross-task faithfulness when overlaps are moderate.

## Circuit Discovery Methods Vary

Recent circuit discovery approaches differ by domain (text vs. vision), patching methods (zero, mean, sampling), and the balance between manual and automated steps.

## Comparison with Manual Circuits

When comparing the ACDC algorithm to manually-identified circuits, researchers found overlapping components, components found by ACDC only, and components found only in manual interpretation, with all manually-identified heads being recovered by ACDC.

The research suggests that while different circuit discovery methods may have overlapping findings, **agreement in node overlap does not necessarily indicate agreement in faithfulness or functional accuracy**, which is an important consideration when evaluating whether different discovery methods are truly finding the same circuits.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "21fdc216-342c-40c7-bd23-1da2432077a3"
}
```

</details>

---


### System

_source line 353_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "description": "Q3: New circuit discovery methods 2024-2026",
  "usage": {
    "total_tokens": 37477,
    "tool_uses": 31,
    "duration_ms": 123452
  },
  "last_tool_name": "ToolSearch",
  "uuid": "ae4b7b37-1d18-4bac-a9e2-3fc1ba6ad534",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 354_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012ncJqUuwGz4fTUGeptsajr`</summary>

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
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "acc011fd-99a8-40ec-8046-9bff0766d265",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS8CeaWQv1kikqhLW1Hx8X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 329,
      "cache_read_input_tokens": 36646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 329,
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

_source line 355 · 2026-05-12T22:10:00.342Z_

<details><summary>↩ Tool result · `toolu_012ncJqUuwGz4fTUGeptsajr`</summary>

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
  "parent_tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "86e2f549-a65f-49ab-a36f-613ef66a0fac"
}
```

</details>

---


### Tool result

_source line 356 · 2026-05-12T22:10:01.190Z_

<details><summary>↩ Tool result · `toolu_018gVwBBZksLbZcJerWrsE94`</summary>

```text
Web search results for query: ""Unifying and Verifying Mechanistic Interpretations" ICLR 2025 published conference paper"

Links: [{"title":"Unifying and Verifying Mechanistic Interpretations: A Case Study with Group Operations | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/unifying-verifying-mechanistic-interpretations-case-study-group"},{"title":"Unifying Mechanistic Interpretations of Neural Networks Trained on Modular Addition | OpenReview","url":"https://openreview.net/forum?id=cCJoZxwh9s"},{"title":"International Conference on Learning Representations 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025"},{"title":"ICLR Poster Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable?","url":"https://iclr.cc/virtual/2025/poster/30956"},{"title":"Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable? | OpenReview","url":"https://openreview.net/forum?id=5IWJBStfU7"},{"title":"Open problems in mechanistic interpretability: 2026 status report","url":"https://gist.github.com/bigsnarfdude/629f19f635981999c51a8bd44c6e2a54"},{"title":"Unifying and Verifying Mechanistic Interpretations: A Case Study with Group Operations","url":"https://arxiv.org/html/2410.07476v2"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"ICLR From Mechanistic Interpretability to Mechanistic Biology: Training, Evaluating, and Interpreting Sparse Autoencoders on Protein Language Models","url":"https://iclr.cc/virtual/2025/35937"},{"title":"ICLR Poster Tracking Equivalent Mechanistic Interpretations Across Neural Networks","url":"https://iclr.cc/virtual/2026/poster/10011083"}]

Based on the search results, I found the paper you're looking for. The paper "Unifying and Verifying Mechanistic Interpretations: A Case Study with Group Operations" clarifies previous mechanistic interpretability results on the group composition task, provides a more complete explanation, shows that the interpretation unifies findings of previous works, and verifies this explanation by translating it into guarantees on model accuracy.

The paper performs mechanistic interpretability on one-hidden-layer neural networks trained on the binary operation of finite groups. More specifically, the authors investigate internal model structure by examining how irreducible representations act by permutation on a discrete set of vectors learned by the model, and propose a model explanation that unifies previous findings by showing that the model approximates equivariance in each of its input arguments.

The authors' philosophy is that any rigorous mechanistic knowledge of a model's inner workings should yield a guarantee on the model's performance, with more complete explanations yielding either tighter performance bounds or more compact proofs. The paper verifies the explanation with compact proofs of model performance, and uses compact proofs to provide rigorous and quantitative positive evidence for interpretation completeness.

The paper is available on arXiv and has been published in conference proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "958c73cb-0651-4436-9bd7-76791fdf9030"
}
```

</details>

---


### System

_source line 357_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for comparing ACDC EAP edge pruning subnetwork probin…",
  "usage": {
    "total_tokens": 25895,
    "tool_uses": 14,
    "duration_ms": 129847
  },
  "last_tool_name": "WebSearch",
  "uuid": "0ab38528-4d3e-42b2-90cb-d2564af377ad",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 358_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AxxfNLkk1Tam9EupvLivAX`</summary>

```json
{
  "query": "comparing ACDC EAP edge pruning subnetwork probing circuit agreement overlap analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "59319eab-dfb7-4f1b-a603-1967b20e1cdf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRvU5jthAmpQsNjuXfivFN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 24223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1057,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 359_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "description": "Q1: Circuit method consistency comparison",
  "usage": {
    "total_tokens": 40540,
    "tool_uses": 35,
    "duration_ms": 135507
  },
  "last_tool_name": "ToolSearch",
  "uuid": "83b6a9a0-ccd7-44dc-a646-4046a7747173",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 360_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LWb1qLs2i4oQuY73J3mcig`</summary>

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
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "6aa386d5-2b45-4e8d-9cc2-6160c7ada5c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAWLFpBH8uBaz5po6SHAMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 313,
      "cache_creation_input_tokens": 1584,
      "cache_read_input_tokens": 38543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1584,
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

_source line 361 · 2026-05-12T22:10:02.777Z_

<details><summary>↩ Tool result · `toolu_01LWb1qLs2i4oQuY73J3mcig`</summary>

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
  "parent_tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "1d882f04-5369-4f37-9e12-b06ba8455b19"
}
```

</details>

---


### System

_source line 362_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Fetching https://arxiv.org/abs/2410.07476",
  "usage": {
    "total_tokens": 45415,
    "tool_uses": 35,
    "duration_ms": 123466
  },
  "last_tool_name": "WebFetch",
  "uuid": "132dab78-c65d-44ef-aab8-c08e08cc3d22",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 363_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017G2dE7mFTUXgZ1WQbzyaCG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.07476",
  "prompt": "What venue was this paper published at? Look for 'Published as a conference paper at ICLR 2025' or similar text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "0c92baaa-69f5-4e4a-aa00-5dec58d9fcc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHbGy5t8jWWTrry6JwzviW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1173,
      "cache_read_input_tokens": 43986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1173,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 364_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for ICLR 2025 \"Mechanistic Interpretability of In-Con…",
  "usage": {
    "total_tokens": 45477,
    "tool_uses": 36,
    "duration_ms": 124134
  },
  "last_tool_name": "WebSearch",
  "uuid": "ec2e9769-0698-4a27-a25f-cafe41b1e85d",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 365_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JRgjYKhanLt6YjGn5VAWvD`</summary>

```json
{
  "query": "ICLR 2025 \"Mechanistic Interpretability of In-Context Learning\" structured task curriculum accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e53631cd-66a4-4846-9f24-a1e0a6775c53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHbGy5t8jWWTrry6JwzviW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1173,
      "cache_read_input_tokens": 43986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1173,
        "ephemeral_1h_input_tokens": 0
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

_source line 366 · 2026-05-12T22:10:06.121Z_

<details><summary>↩ Tool result · `toolu_017G2dE7mFTUXgZ1WQbzyaCG`</summary>

```text
Based on the content provided, this paper was accepted to **ICLR 2025**. The submission history notes state: "ICLR 2025 camera ready. 32 pages, 11 figures," indicating it was published as a conference paper at that venue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2ce4507b-3f26-43d7-af05-8bdb6aa3298c"
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-12T22:10:08.443Z_

<details><summary>↩ Tool result · `toolu_01JRgjYKhanLt6YjGn5VAWvD`</summary>

```text
Web search results for query: "ICLR 2025 "Mechanistic Interpretability of In-Context Learning" structured task curriculum accepted"

Links: [{"title":"Mechanistic Interpretability of In-Context Learning Generalization through Structured Task Curriculum | OpenReview","url":"https://openreview.net/forum?id=2Fv4GxUElU"}]

Based on the search results, I found the paper you're looking for. The paper "Mechanistic Interpretability of In-Context Learning Generalization through Structured Task Curriculum" studies the generalization mechanisms of In-Context Learning (ICL) in Transformer-based language models from the perspective of mechanistic interpretability, conducting a systematic study using two structured tasks: ICL Markov Chain and ICL Regression.

However, I should note that according to the search results, this paper was submitted to ICLR 2026, not ICLR 2025. The paper is available on OpenReview and appears to still be under review as of the search date.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "fcdcc95d-e039-4286-a492-fce38009b0a8"
}
```

</details>

---


### Tool result

_source line 368 · 2026-05-12T22:10:10.044Z_

<details><summary>↩ Tool result · `toolu_01AxxfNLkk1Tam9EupvLivAX`</summary>

```text
Web search results for query: "comparing ACDC EAP edge pruning subnetwork probing circuit agreement overlap analysis"

Links: [{"title":"Attribution Patching Outperforms Automated Circuit Discovery Aaquib Syed","url":"https://openreview.net/pdf?id=tiLbFR4bJW"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://aclanthology.org/2024.blackboxnlp-1.25.pdf"},{"title":"Automatic Circuit Discovery","url":"https://sidn.baulab.info/autocircuits/"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://www.arxiv.org/pdf/2510.03282"},{"title":"Finding Transformer Circuits with Edge Pruning Adithya Bhaskar Alexander Wettig","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/20fdaf67581e6d7157376d1ed584040a-Paper-Conference.pdf"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://www.researchgate.net/publication/386190657_Attribution_Patching_Outperforms_Automated_Circuit_Discovery"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/html/2510.06811"},{"title":"Multi-Granular Node Pruning for Circuit Discovery","url":"https://arxiv.org/html/2512.10903"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://arxiv.org/html/2407.14494"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/html/2510.23264"}]

Based on the search results, I found comprehensive information about comparing ACDC, EAP, edge pruning, subnetwork probing, circuit discovery methods, and their performance metrics. Here's what the research shows:

## Overview of Key Methods

EAP outperforms all previous methods for circuit discovery, being competitive with ACDC on recovering circuits while significantly reducing the computational demand: EAP only takes a constant number of forward and backwards passes while ACDC requires a number of forward passes scaling exponentially with the number of nodes.

## Performance Comparisons

EAP's performance is better than ACDC overall with maximal AUC in most tasks, while ACDC used with the KL Divergence metric outperforms EAP in some cases.

Edge Pruning is competitive with ACDC on circuit overlap metrics. However, Edge Pruning outperforms both ACDC and EAP by a significant margin on IOI and GT tasks.

## Method Characteristics

ACDC uses an expensive greedy search that ablates each edge to estimate its importance, and cannot scale to datasets beyond a few hundred examples or to billion-parameter models.

EAP uses gradient-based linear approximations of activation patching to estimate the importance of all edges simultaneously, but while fast, these first-order approximations often sacrifice faithfulness to the full model.

Subnetwork Probing optimizes a mask over model components using gradient descent, while HISP uses a first-order Taylor approximation to estimate the effect of replacing a head's output with corrupted inputs.

## Combined Approaches

Ensembling two or more circuit localization methods through parallel and sequential ensembling yields notable gains on benchmark metrics, leading to more precise circuit identification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2a76d199-2af6-4c0c-86bc-6d81382c903a"
}
```

</details>

---


### System

_source line 369_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Fetching https://openreview.net/forum?id=sdLwJTtKpM",
  "usage": {
    "total_tokens": 46030,
    "tool_uses": 37,
    "duration_ms": 132631
  },
  "last_tool_name": "WebFetch",
  "uuid": "69cbc137-5ba2-4897-a830-60a71a5bbce9",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 370_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01T7bxjTNHHwcx6adzWKftbY`</summary>

```json
{
  "url": "https://openreview.net/forum?id=sdLwJTtKpM",
  "prompt": "What is the paper title? What venue was it submitted to or published at? What is the decision? ICLR 2025?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "9585f479-af36-4447-ad3a-020a41e57762",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5iit37FXfWqizWU57mxco",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 551,
      "cache_read_input_tokens": 45159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 551,
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

_source line 371_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Fetching https://openreview.net/forum?id=Timsb74vIY",
  "usage": {
    "total_tokens": 46031,
    "tool_uses": 38,
    "duration_ms": 133498
  },
  "last_tool_name": "WebFetch",
  "uuid": "f4ea6fda-0df8-4154-9a7e-59c9dbd3101d",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 372_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014n57vwKrVmfi8dqkF2ms6b`</summary>

```json
{
  "url": "https://openreview.net/forum?id=Timsb74vIY",
  "prompt": "What is the paper title? What venue? What is the decision - accepted or rejected? ICML 2025?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "5c8ff998-939d-4590-8b69-2dec6e3648e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5iit37FXfWqizWU57mxco",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 551,
      "cache_read_input_tokens": 45159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 551,
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

_source line 373_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Fetching https://arxiv.org/abs/2510.06811",
  "usage": {
    "total_tokens": 26856,
    "tool_uses": 15,
    "duration_ms": 143661
  },
  "last_tool_name": "WebFetch",
  "uuid": "c2a4e737-c4fd-412a-80de-8ccb6a93773f",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 374_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VKbY28czv3aVdYNQDHjTgK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.06811",
  "prompt": "Extract the full title, all authors, year, venue/status. This appears to be about ensembling circuit localization methods. I need to know: 1) Do they combine outputs from multiple different circuit discovery methods? If so, which methods? 2) How do they ensemble - voting, averaging, intersection, union? 3) What is the \"parallel and sequential ensembling\" approach? 4) How similar is this to a binary consensus across methods? 5) What are the main results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "71b1cb6e-5fe2-4ad4-ae12-add9d581e2f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BgYjKKLja5gDHMbQ7Agtc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 959,
      "cache_read_input_tokens": 25280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 959,
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

_source line 375 · 2026-05-12T22:10:16.394Z_

<details><summary>↩ Tool result · `toolu_01T7bxjTNHHwcx6adzWKftbY`</summary>

```text
# Paper Information

**Title:** "Scaling Sparse Feature Circuits For Studying In-Context Learning"

**Venue:** ICLR 2025 Workshop SLLM (Small Language Models)

**Decision:** The document does not specify a final decision. The paper appears to be a workshop submission rather than the main conference, categorized as a "tiny / short paper (up to 4 pages)." The publication date is listed as "05 Mar 2025" with a last modification of "23 Apr 2025," but no acceptance or rejection decision is explicitly stated in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "157e8637-c42f-4a1a-b466-e065a2376211"
}
```

</details>

---


### Tool result

_source line 376 · 2026-05-12T22:10:16.641Z_

<details><summary>↩ Tool result · `toolu_014n57vwKrVmfi8dqkF2ms6b`</summary>

```text
# Paper Details

**Title:** "Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees"

**Venue:** ICLR 2026 Conference

**Decision:** Accepted as a poster presentation (the page indicates "ICLR 2026 Poster")

**Regarding ICML 2025:** No, this is not an ICML 2025 submission. The paper was published at ICLR 2026, with publication dated January 26, 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e57cedd1-d1a3-4393-adfc-889ae4f9e196"
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-12T22:10:21.852Z_

<details><summary>↩ Tool result · `toolu_01VKbY28czv3aVdYNQDHjTgK`</summary>

```text
# Research Summary

**Title:** "BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods"

**Authors:** Philipp Mondorf, Mingyang Wang, Sebastian Gerstner, Ahmad Dawar Hakimi, Yihong Liu, Leonor Veloso, Shijia Zhou, Hinrich Schütze, Barbara Plank

**Year:** 2025 (submitted October 8, 2025)

**Venue:** The 8th BlackboxNLP Workshop (Shared Task)

---

## Key Findings

**1) Multi-method combination:** Yes, they integrate outputs from multiple circuit localization approaches, specifically mentioning EAP-IG and edge pruning methods.

**2) Ensembling strategies:** The researchers employ "parallel ensembling" by combining "attribution scores assigned to each edge by different methods—e.g., by averaging or taking the minimum or maximum value."

**3) Parallel vs. sequential approach:** Parallel ensembling merges scores from multiple methods simultaneously. Sequential ensembling uses "edge attribution scores obtained via EAP-IG as a warm start for a more expensive but more precise circuit identification method, namely edge pruning."

**4) Comparison to binary consensus:** While not explicitly described as consensus-based, the approach shares similarities—combining multiple detection methods to improve precision, though their methodology extends beyond simple binary agreement.

**5) Main results:** "Both approaches yield notable gains on the benchmark metrics, leading to a more precise circuit identification approach." The combined parallel ensemble (including the sequential variant) achieved superior performance across model-task combinations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "d58accfb-cb27-42a1-809c-be9eabdd25b1"
}
```

</details>

---


### System

_source line 378_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Fetching https://openreview.net/forum?id=Pa1vr1Prww",
  "usage": {
    "total_tokens": 46621,
    "tool_uses": 39,
    "duration_ms": 140965
  },
  "last_tool_name": "WebFetch",
  "uuid": "beaa5f78-1df4-4d36-a3ba-79ba61735e81",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 379_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012ZmXaUyoabV1jx5cz4yQx2`</summary>

```json
{
  "url": "https://openreview.net/forum?id=Pa1vr1Prww",
  "prompt": "What is the paper title and what venue was it accepted to? ICLR 2025 main conference or a workshop?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "0106a9cc-7397-404f-944d-f622de26b563",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7jgMqMRaebk8227BGPFAi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 45710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 588,
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

_source line 380_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for ICLR 2025 accepted \"Sparse Autoencoders Do Not Fi…",
  "usage": {
    "total_tokens": 46622,
    "tool_uses": 40,
    "duration_ms": 141290
  },
  "last_tool_name": "WebSearch",
  "uuid": "ad5b22e0-19af-45e0-a678-7371ff0283a7",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 381_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XaYRQgCGkM6XuhvfeCGPvc`</summary>

```json
{
  "query": "ICLR 2025 accepted \"Sparse Autoencoders Do Not Find Canonical\" circuit features"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "f743c47d-b0c6-4c20-a265-9024af966d36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7jgMqMRaebk8227BGPFAi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 45710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 588,
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

_source line 382 · 2026-05-12T22:10:24.725Z_

<details><summary>↩ Tool result · `toolu_012ZmXaUyoabV1jx5cz4yQx2`</summary>

```text
# Paper Information

**Title:** "Scaling Sparse Feature Circuits For Studying In-Context Learning"

**Venue Status:** The paper was submitted to ICLR 2025, but based on the page content, it appears to be under review rather than accepted. The submission shows a date of "27 Sept 2024 (modified: 05 Feb 2025)" with "Submitted to ICLR 2025" indicated, suggesting it is a main conference submission awaiting decision, not a workshop paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "bffd483a-1b22-4b86-b8f2-6ff487aea61f"
}
```

</details>

---


### System

_source line 383_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Fetching https://arxiv.org/html/2510.06811",
  "usage": {
    "total_tokens": 27516,
    "tool_uses": 16,
    "duration_ms": 155648
  },
  "last_tool_name": "WebFetch",
  "uuid": "e2b0d09d-a449-4356-8628-358c441459c0",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 384_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DGbMjbUSgyMu2NAcZ3sCrG`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.06811",
  "prompt": "I need more details about how exactly they ensemble the methods. Specifically: 1) Do they compute a binary inclusion (edge in / edge out) per method and then vote, or do they average continuous scores? 2) What exact methods do they combine - list all of them? 3) Do they use the term \"consensus\" anywhere? 4) Is this about aggregating fundamentally different circuit discovery algorithms, or just different configurations of the same algorithm? 5) What is their main ensemble formula or aggregation rule? 6) How much improvement does ensembling give over single methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "a281ff77-7321-4a7e-aba7-5d5ee98afd05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfaNbmMfrT7xgMcHgEMkk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 26239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 599,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-12T22:10:30.326Z_

<details><summary>↩ Tool result · `toolu_01XaYRQgCGkM6XuhvfeCGPvc`</summary>

```text
Web search results for query: "ICLR 2025 accepted "Sparse Autoencoders Do Not Find Canonical" circuit features"

Links: [{"title":"SPARSE AUTOENCODERS DO NOT FIND CANONICAL ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/84ca3f2d9d9bfca13f69b48ea63eb4a5-Paper-Conference.pdf"},{"title":"Sparse Autoencoders Do Not Find Canonical Units of Analysis | OpenReview","url":"https://openreview.net/forum?id=9ca9eHNrdH"},{"title":"[2502.04878] Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://arxiv.org/abs/2502.04878"},{"title":"Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://arxiv.org/html/2502.04878v1"},{"title":"Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/84ca3f2d9d9bfca13f69b48ea63eb4a5-Abstract-Conference.html"},{"title":"GitHub - zepingyu0512/awesome-SAE: awesome SAE papers · GitHub","url":"https://github.com/zepingyu0512/awesome-SAE"},{"title":"ICLR Poster Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://iclr.cc/virtual/2025/poster/30676"},{"title":"(PDF) Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://www.researchgate.net/publication/388847461_Sparse_Autoencoders_Do_Not_Find_Canonical_Units_of_Analysis"},{"title":"Sparse Autoencoders Find Highly Interpretable Features in Language Models | OpenReview","url":"https://openreview.net/forum?id=F76bwRSLeK"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/42ef3308c230942d223c411adf182c88-Paper-Conference.pdf"}]

I found the paper! Here are the search results for "Sparse Autoencoders Do Not Find Canonical Units of Analysis" accepted at ICLR 2025:

## Paper Overview

The paper was published at ICLR 2025 as a poster presentation on January 22, 2025.

## Authors and Main Contributions

The authors are Patrick Leask, Bart Bussmann, Michael Pearce, Joseph Bloom, Curt Tigges, Noura Al Moubayed, Lee Sharkey, and Neel Nanda.

## Key Findings

The paper uses two novel techniques: SAE stitching to show sparse autoencoders (SAEs) are incomplete, and meta-SAEs to show they are not atomic.

Through SAE stitching, the authors demonstrated that smaller SAEs are incomplete, missing information that novel features in larger SAEs capture.

Using meta-SAEs - SAEs trained on the decoder matrix of another SAE - they find that latents in SAEs often decompose into combinations of latents from a smaller SAE, showing that larger SAE latents are not atomic. For example, a latent representing "Einstein" decomposes into "scientist", "Germany", and "famous person".

## Conclusion

The findings challenge the idea that SAEs can discover a canonical set of features. However, even if SAEs do not find canonical units of analysis, they may still be useful tools, and the authors suggest that future research should either pursue different approaches for identifying such units, or pragmatically choose the SAE size suited to their task.

The authors also provide an interactive dashboard to explore meta-SAEs at https://metasaes.streamlit.app/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "add922a9-71cb-4001-a587-e330400fc1df"
}
```

</details>

---


### Tool result

_source line 386 · 2026-05-12T22:10:33.239Z_

<details><summary>↩ Tool result · `toolu_01DGbMjbUSgyMu2NAcZ3sCrG`</summary>

```text
# Ensemble Methods for Circuit Localization

## 1. Continuous Scores vs. Binary Voting
They aggregate **continuous attribution scores**, not binary inclusions. As stated: "a circuit detection method gives a score to each edge of the model" and they "consolidate these to one final score for each edge."

## 2. Methods Combined
Their approaches combine:
- **Parallel ensemble**: EAP, EAP-IG-inputs, and EAP-IG-activations (three EAP variants)
- **Sequential ensemble**: EAP-IG-inputs + edge pruning
- **Hybrid ensemble**: All four methods above (three EAP variants + warm-start edge pruning)

## 3. "Consensus" Terminology
The term "consensus" does **not** appear in the document. They use "ensemble," "parallel ensembling," and "sequential ensembling" instead.

## 4. Different Algorithms vs. Configurations
These are **fundamentally different circuit discovery methods**. They include attribution-based approaches (EAP variants) and a pruning-based method, representing distinct algorithmic families.

## 5. Main Aggregation Formula
The primary rule is straightforward: "taking the mean yields the best results." They also tested maximum and minimum operations, which correspond to circuit union and intersection respectively.

## 6. Performance Improvements
The hybrid ensemble achieved average improvements of **+0.24 CPR** (1.59 → 1.83) over the baseline EAP-IG-inputs method on the private test set.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "1798828b-38ee-472a-a051-85ab77113d2e"
}
```

</details>

---


### System

_source line 387_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for NeurIPS 2024 accepted \"Hypothesis Testing the Cir…",
  "usage": {
    "total_tokens": 48015,
    "tool_uses": 41,
    "duration_ms": 152619
  },
  "last_tool_name": "WebSearch",
  "uuid": "a9232a40-6778-46c4-9b76-135813d8a8f5",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 388_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NiEa4FRLWUvSc6zCfA6Un8`</summary>

```json
{
  "query": "NeurIPS 2024 accepted \"Hypothesis Testing the Circuit Hypothesis\" LLM main conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "504f3a7b-f37f-4f3f-adc4-8cce555338e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013b7S7HnrBhp8aUwkfmLECA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1391,
      "cache_read_input_tokens": 46298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1391,
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

_source line 389_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Searching for ICLR 2025 accepted \"Everything Everywhere All at …",
  "usage": {
    "total_tokens": 48016,
    "tool_uses": 42,
    "duration_ms": 153082
  },
  "last_tool_name": "WebSearch",
  "uuid": "82a0779f-e6f2-421e-9b57-948b329e7fda",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 390_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GykVmxs3RsZbLv6WDXt2mS`</summary>

```json
{
  "query": "ICLR 2025 accepted \"Everything Everywhere All at Once\" mechanistic interpretability identifiable spotlight oral"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "f6ed0be7-fd7b-4ca0-a47b-eb212663c73a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013b7S7HnrBhp8aUwkfmLECA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1391,
      "cache_read_input_tokens": 46298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1391,
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

_source line 391_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for ensemble circuit localization methods MIB benchma…",
  "usage": {
    "total_tokens": 28089,
    "tool_uses": 17,
    "duration_ms": 164566
  },
  "last_tool_name": "WebSearch",
  "uuid": "27318fe3-d59d-43ac-8bff-d5ed007d17fb",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 392_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AD8uDTQsLZxHUv2wo8xJVt`</summary>

```json
{
  "query": "ensemble circuit localization methods MIB benchmark voting intersection union 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e52982ad-e488-4622-b829-f750189225e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015b6LbykTzxhYFgQeHgjk7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 26838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 571,
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

_source line 393 · 2026-05-12T22:10:37.985Z_

<details><summary>↩ Tool result · `toolu_01GykVmxs3RsZbLv6WDXt2mS`</summary>

```text
Web search results for query: "ICLR 2025 accepted "Everything Everywhere All at Once" mechanistic interpretability identifiable spotlight oral"

No links found.

I searched for information about an ICLR 2025 paper with that title related to mechanistic interpretability, but the search didn't return specific results about this particular paper. 

The search query combined several specific terms (the paper title, the conference, and keywords like "mechanistic interpretability," "identifiable," "spotlight," and "oral"), which may have been too restrictive to find matching results in the search engine's index.

To help you find this information, you might try:
1. Visiting the official ICLR 2025 website directly for accepted papers lists
2. Searching for the authors' names if you know them
3. Checking preprint servers like arXiv.org
4. Searching with just the paper title or just key authors

Would you like me to search again with a different query strategy?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "ed32f338-e32d-41d5-b3ec-de978a530816"
}
```

</details>

---


### Tool result

_source line 394 · 2026-05-12T22:10:40.731Z_

<details><summary>↩ Tool result · `toolu_01NiEa4FRLWUvSc6zCfA6Un8`</summary>

```text
Web search results for query: "NeurIPS 2024 accepted "Hypothesis Testing the Circuit Hypothesis" LLM main conference"

Links: [{"title":"Hypothesis Testing the Circuit Hypothesis in LLMs Claudia Shi∗1","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/abccb8a90b30d45b948360ba41f5a20f-Paper-Conference.pdf"},{"title":"Hypothesis Testing the Circuit Hypothesis in LLMs","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/abccb8a90b30d45b948360ba41f5a20f-Abstract-Conference.html"},{"title":"NeurIPS Poster Hypothesis Testing the Circuit Hypothesis in LLMs","url":"https://neurips.cc/virtual/2024/poster/96582"},{"title":"NeurIPS Hypothesis testing the circuit hypothesis in LLMs","url":"https://neurips.cc/virtual/2024/108648"},{"title":"Seventeen papers by CSE researchers at NeurIPS 2024","url":"https://cse.engin.umich.edu/stories/seventeen-papers-by-cse-researchers-at-neurips-2024"},{"title":"Hypothesis Testing the Circuit Hypothesis in LLMs Claudia Shi∗1","url":"http://www.cs.columbia.edu/~blei/papers/ShiBeltran-VelezNazaretZhengGarriga-AlonsoJessonMakarBlei2024.pdf"},{"title":"Hypothesis Testing the Circuit Hypothesis in LLMs | OpenReview","url":"https://openreview.net/forum?id=5ai2YFAXV7"},{"title":"[2410.13032] Hypothesis Testing the Circuit Hypothesis in LLMs","url":"https://arxiv.org/abs/2410.13032"},{"title":"(PDF) Hypothesis Testing the Circuit Hypothesis in LLMs","url":"https://www.researchgate.net/publication/385009900_Hypothesis_Testing_the_Circuit_Hypothesis_in_LLMs"},{"title":"Hypothesis Testing the Circuit Hypothesis in LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241013032S/abstract"}]

Yes, "Hypothesis Testing the Circuit Hypothesis in LLMs" was published at NeurIPS 2024 as a poster. 

The paper addresses how large language models (LLMs) implement surprising capabilities, with one hypothesis suggesting these capabilities are primarily executed by small subnetworks within the LLM, known as circuits. The researchers formalize a set of criteria that a circuit is hypothesized to meet and develop a suite of hypothesis tests to evaluate them, with criteria focusing on the extent to which the LLM's behavior is preserved, the degree of localization of this behavior, and whether the circuit is minimal.

The paper applies these tests to six circuits described in the research literature, finding that synthetic circuits -- circuits that are hard-coded in the model -- align with the idealized properties, while circuits discovered in Transformer models satisfy the criteria to varying degrees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "cb2c5c66-1b64-42da-ab87-7bb59935bc58"
}
```

</details>

---


### System

_source line 395_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Fetching https://iclr.cc/virtual/2025/poster/30956",
  "usage": {
    "total_tokens": 49294,
    "tool_uses": 43,
    "duration_ms": 162811
  },
  "last_tool_name": "WebFetch",
  "uuid": "5cdfbff4-0cab-438b-a973-049df8686854",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 396_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017orY27q9CtWJMiHT2y2UXg`</summary>

```json
{
  "url": "https://iclr.cc/virtual/2025/poster/30956",
  "prompt": "What is this paper? Is it a poster, spotlight, or oral at ICLR 2025? What are the authors?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b5d4b1d2-5441-4938-ae5f-3ff454c4e81c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEbWBmxqiBYRwHKmLC1wCK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 47689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 943,
        "ephemeral_1h_input_tokens": 0
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

_source line 397 · 2026-05-12T22:10:44.272Z_

<details><summary>↩ Tool result · `toolu_01AD8uDTQsLZxHUv2wo8xJVt`</summary>

```text
Web search results for query: "ensemble circuit localization methods MIB benchmark voting intersection union 2025 2026"

Links: [{"title":"[2510.06811] BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/abs/2510.06811"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/html/2510.06811v1"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for","url":"https://arxiv.org/pdf/2510.06811"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.31/"},{"title":"MIB: A Mechanistic Interpretability Benchmark | OpenReview","url":"https://openreview.net/forum?id=sSrOwve6vb"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods | Request PDF","url":"https://www.researchgate.net/publication/397423880_BlackboxNLP-2025_MIB_Shared_Task_Exploring_Ensemble_Strategies_for_Circuit_Localization_Methods"},{"title":"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/html/2511.18409v1"},{"title":"[PDF] BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BlackboxNLP-2025-MIB-Shared-Task:-Exploring-for-Mondorf-Wang/6de77c59381b74de6e6f554c3f6e12690d6628e8"},{"title":"MCML - BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://mcml.ai/publications/mwg+25/"},{"title":"Shared Task - BlackboxNLP 2025 - GitHub Pages","url":"https://blackboxnlp.github.io/2025/task/"}]

I found comprehensive information about ensemble strategies for circuit localization methods in the context of the MIB (Mechanistic Interpretability Benchmark) and the BlackboxNLP 2025 shared task. Here are the key findings:

## Ensemble Strategies

Two variants of ensembling are explored: parallel and sequential ensembling, where parallel ensembling combines attribution scores assigned to each edge by different methods—e.g., by averaging or taking the minimum or maximum value.

## Score Reduction Methods

Four score reduction methods are experimented with across base approaches: (1) mean, (2) weighted average, (3) maximum, and (4) minimum. The maximum corresponds to a union of circuits (edges selected by any method), while the minimum corresponds to an intersection (edges selected by all methods). Taking the mean yields the best results.

## Sequential Ensembling

The main idea of sequential ensemble approach is to use the attribution scores produced by a fast circuit identification method to warm-start a slower, more precise method, whereby using edge attribution values computed via EAP-IG-inputs to initialize the learnable mask of edge pruning.

## Performance Results

Taking a parallel ensemble over various methods, including the sequential ensemble, achieves the best results. Ensembling strategies may be an accessible and fruitful line of work for future circuit discovery research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "42652d1a-22a6-4adf-8d3e-487b4207940e"
}
```

</details>

---


### Tool result

_source line 398 · 2026-05-12T22:10:46.795Z_

<details><summary>↩ Tool result · `toolu_017orY27q9CtWJMiHT2y2UXg`</summary>

```text
# Paper Information

**Presentation Format:** Poster at ICLR 2025

**Authors:** Maxime Méloux, Silviu Maniu, François Portet, and Maxime Peyrard

**Title:** "Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable?"

**Overview:** The paper examines whether mechanistic interpretability explanations of neural networks are uniquely identifiable. The researchers tested two main strategies for producing such explanations using simple Boolean function tasks and found "overwhelming evidence of non-identifiability in all cases," suggesting multiple valid explanations can exist for the same model behavior.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "12891bb8-489e-4ffd-908e-c5da6baf0ff2"
}
```

</details>

---


### System

_source line 399_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for structfuse context-aware fusion circuit discovery…",
  "usage": {
    "total_tokens": 29169,
    "tool_uses": 18,
    "duration_ms": 174892
  },
  "last_tool_name": "WebSearch",
  "uuid": "f47ba613-7081-4362-935e-665f1ff7d141",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 400_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YLEqv93CypvBxzJontBcKh`</summary>

```json
{
  "query": "structfuse context-aware fusion circuit discovery methods 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2e9088f8-3391-4246-b9f8-31c9358811fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TykeuuWb2mkjDdiyLHB7V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1044,
      "cache_read_input_tokens": 27409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1044,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 401_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Fetching https://iclr.cc/virtual/2025/poster/30956",
  "usage": {
    "total_tokens": 49563,
    "tool_uses": 44,
    "duration_ms": 169336
  },
  "last_tool_name": "WebFetch",
  "uuid": "dc7a2bc5-ad00-4f16-a44a-c13d0dfea2a1",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 402_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RsV3gf159R7PVu9iQ43Sc4`</summary>

```json
{
  "url": "https://iclr.cc/virtual/2025/poster/30956",
  "prompt": "Confirm this is ICLR 2025 poster. What are the full details?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "315e67d0-2724-4236-b827-d8090832f63e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgf6JAKgcGYtweFeekJXBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 48632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 539,
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

_source line 403_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ab64af982756e2f1f",
  "tool_use_id": "toolu_01L3fLhWV9gRjmmjD2tKgqGa",
  "status": "completed",
  "output_file": "",
  "summary": "Q3: New circuit discovery methods 2024-2026",
  "usage": {
    "total_tokens": 37860,
    "tool_uses": 31,
    "duration_ms": 175344
  },
  "uuid": "e5f52e37-bed3-44f5-b7e6-450fa583b494",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool result

_source line 404 · 2026-05-12T22:10:52.236Z_

<details><summary>↩ Tool result · `toolu_01L3fLhWV9gRjmmjD2tKgqGa`</summary>

```text


Here is the compiled literature survey table of new circuit discovery methods (2024--2026), excluding the well-known baselines (EAP-IG, ACDC, Edge Pruning, IFR, activation patching):

---

| **Method** | **Paper Title** | **Authors** | **Year** | **Venue** | **Algorithm Family** | **Brief Description** | **URL** |
|---|---|---|---|---|---|---|---|
| **CD-T** | Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition | Aliyah R. Hsu et al. | 2024 | ICLR 2025 | Decomposition-based | Recursively decomposes feature contributions through the computational graph using contextual decomposition equations. No activation patching needed. Reduces circuit discovery from hours to seconds; 97% ROC AUC on standard benchmarks. | [arxiv.org/abs/2407.00886](https://arxiv.org/abs/2407.00886) |
| **DiscoGP** | Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning | Lei Yu et al. | 2024 | ICML 2024 | Pruning-based (differentiable) | Joint weight and edge pruning via learnable binary masks trained end-to-end. Unifies weight-level and connection-level circuit discovery, which prior methods treated separately. | [arxiv.org/html/2407.03779v1](https://arxiv.org/html/2407.03779v1/) |
| **Transcoders** | Transcoders Find Interpretable LLM Feature Circuits | Jacob Dunefsky et al. | 2024 | NeurIPS 2024 | Sparse replacement model | Replaces dense MLP layers with wider, sparsely-activating MLP layers (transcoders) that approximate the original. Enables weights-based circuit analysis through MLPs, decomposing circuits into input-dependent and input-invariant terms. | [arxiv.org/abs/2406.11944](https://arxiv.org/abs/2406.11944) |
| **Sparse Feature Circuits** | Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | Samuel Marks et al. | 2024 | ICLR 2025 | Attribution-based (SAE features) | Discovers circuits over SAE-learned sparse features rather than neurons/heads. Introduces SHIFT for editing model behavior by removing task-irrelevant features. Fully unsupervised pipeline discovering thousands of circuits at scale. | [arxiv.org/abs/2403.19647](https://arxiv.org/abs/2403.19647) |
| **Circuit Tracing (Attribution Graphs)** | Circuit Tracing: Revealing Computational Graphs in Language Models | Emmanuel Ameisen, Chris Olah et al. (Anthropic, 26 authors) | 2025 | Anthropic Technical Report | Sparse replacement model + attribution | Replaces MLPs with cross-layer transcoders (CLTs) to build a "replacement model" of interpretable sparse features. Constructs per-prompt attribution graphs (DAGs) with linear edges between features. Applied to Claude 3.5 Haiku. | [transformer-circuits.pub](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) |
| **GIM** | GIM: Improved Interpretability for Large Language Models | Joakim Edin et al. (Corti) | 2025 | arXiv (under review) | Gradient-based (modified backprop) | Addresses self-repair in attention (softmax redistribution) and LayerNorm by modifying gradient computation during backpropagation. Temperature-adjusted softmax gradients + LayerNorm freeze + gradient normalization. Tops HuggingFace MIB benchmark. | [arxiv.org/abs/2505.17630](https://arxiv.org/abs/2505.17630) |
| **HAP** | Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework | Hao Gu et al. (Algoverse) | 2025 | arXiv preprint | Hybrid (attribution + pruning) | Sequences EAP (fast, approximate) then Edge Pruning (faithful) on the EAP-filtered subgraph. 46% faster than EP alone with comparable faithfulness. Preserves cooperative circuit components (e.g., S-inhibition heads) that pure attribution misses. | [arxiv.org/html/2510.03282v1](https://arxiv.org/html/2510.03282v1) |
| **ModCirc** | Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of LLMs | Yinhan He et al. | 2025 | ICML 2025 | Modular decomposition | Discovers task-agnostic modular circuit vocabularies shared across language tasks, rather than task-specific circuits. Defines five criteria characterizing modular circuits. Enables global-level interpretability with reusable interpretations. | [openreview.net/forum?id=do5vVfKEXZ](https://openreview.net/forum?id=do5vVfKEXZ) |
| **Stream** | Stream: Scaling up Mechanistic Interpretability to Long Context in LLMs via Sparse Attention | J. Rosser et al. | 2025 | arXiv preprint | Hierarchical pruning | Compilable hierarchical pruning algorithm for per-head sparse attention masks in O(T log T) time. Binary-search-style refinement retains top-k key blocks per query. Prunes 97--99% of token interactions, enabling interpretability at 100K+ tokens on consumer GPUs. | [arxiv.org/abs/2510.19875](https://arxiv.org/abs/2510.19875) |
| **Weight-Sparse Circuits** | Weight-sparse transformers have interpretable circuits | Leo Gao et al. (OpenAI) | 2025 | arXiv preprint | Sparsity-constrained training | Trains transformers with extreme weight sparsity (~1 in 1000 nonzero). Resulting circuits are ~16x smaller than those from dense baselines. Neurons correspond to natural concepts with interpretable connections. Defines a capability--interpretability frontier. | [arxiv.org/abs/2511.13653](https://arxiv.org/abs/2511.13653) |
| **Formal MI (Verification-based)** | Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | Itamar Hadad et al. | 2026 | ICLR 2026 | Verification-based | First to use neural network verification for circuit discovery. Provides three provable guarantees: (1) input domain robustness, (2) robust patching over continuous perturbations, (3) minimality. Eliminates reliance on heuristics. | [arxiv.org/abs/2602.16823](https://arxiv.org/abs/2602.16823) |
| **SVD Directional Masking** | Beyond Components: Singular Vector-Based Interpretability of Transformer Circuits | Areeb Ahmad et al. | 2025 | arXiv preprint | SVD + differentiable masking | Decomposes attention heads and MLPs into orthogonal singular directions via SVD, revealing superposed subfunctions within single heads. Learnable diagonal masks on singular values identify functionally important directions. | [arxiv.org/html/2511.20273](https://arxiv.org/html/2511.20273) |

---

**Notable non-method papers relevant to the field:**

| **Paper** | **Authors** | **Year** | **Venue** | **Relevance** |
|---|---|---|---|---|
| The Computational Complexity of Circuit Discovery for Inner Interpretability | Federico Adolfi et al. | 2025 | ICLR 2025 (Spotlight) | Proves many circuit-finding queries are NP-hard and inapproximable; establishes fundamental complexity barriers. |
| MIB: A Mechanistic Interpretability Benchmark | Aaron Mueller et al. (20+ authors) | 2025 | ICML 2025 | Standard benchmark with two tracks (circuit localization, causal variable localization) across 5 models. Attribution and mask optimization methods lead on circuit localization. |
| InterpBench: Semi-Synthetic Transformers for Evaluating MI Techniques | Rohan Gupta et al. | 2024 | NeurIPS 2024 | Semi-synthetic transformers with known ground-truth circuits for evaluating discovery methods. Uses Strict IIT training. |

**Key trends observed:**

1. **Decomposition over patching**: CD-T and SVD directional masking avoid activation patching entirely, using mathematical decomposition for speedups of orders of magnitude.
2. **Feature-level circuits**: Sparse Feature Circuits, Transcoders, and Anthropic's Circuit Tracing all operate over learned sparse features (via SAEs or transcoders) rather than raw neurons/heads, yielding more interpretable units.
3. **Formal guarantees**: The verification-based approach (ICLR 2026) is the first to provide provable correctness, addressing a long-standing gap.
4. **Sparsity by design**: OpenAI's weight-sparse training creates models that are inherently more interpretable, sidestepping post-hoc discovery entirely.
5. **Scaling**: Stream and GIM specifically target practical scalability -- long contexts and production-scale models respectively.

agentId: ab64af982756e2f1f (use SendMessage with to: 'ab64af982756e2f1f' to continue this agent)
&lt;usage>total_tokens: 39682
tool_uses: 31
duration_ms: 175345&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "1c65dfb4-e921-4dc1-b061-a8984d146f2a",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability.\n\n**Task**: Find important new circuit discovery methods published in 2024-2026, beyond the well-known ones (EAP-IG, ACDC, Edge Pruning, IFR, activation patching).\n\nSearch using these keywords:\n1. \"circuit discovery 2024 2025 mechanistic interpretability\"\n2. \"automated circuit discovery new method transformer 2024\"\n3. \"mechanistic interpretability circuit finding 2025 2026\"\n4. \"subnetwork discovery interpretability 2024\"\n\nFor each search, use WebSearch. For promising papers, use WebFetch to read the abstract.\n\n**Output format**: A table with columns:\n- Method name\n- Paper title\n- Authors (first + et al.)\n- Year\n- Venue (if known)\n- Algorithm family (gradient-based, pruning-based, attribution-based, etc.)\n- Brief description\n- URL\n\nFocus on genuinely new methods, not just applications of existing methods to new models/tasks.",
    "agentId": "ab64af982756e2f1f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nHere is the compiled literature survey table of new circuit discovery methods (2024--2026), excluding the well-known baselines (EAP-IG, ACDC, Edge Pruning, IFR, activation patching):\n\n---\n\n| **Method** | **Paper Title** | **Authors** | **Year** | **Venue** | **Algorithm Family** | **Brief Description** | **URL** |\n|---|---|---|---|---|---|---|---|\n| **CD-T** | Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition | Aliyah R. Hsu et al. | 2024 | ICLR 2025 | Decomposition-based | Recursively decomposes feature contributions through the computational graph using contextual decomposition equations. No activation patching needed. Reduces circuit discovery from hours to seconds; 97% ROC AUC on standard benchmarks. | [arxiv.org/abs/2407.00886](https://arxiv.org/abs/2407.00886) |\n| **DiscoGP** | Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning | Lei Yu et al. | 2024 | ICML 2024 | Pruning-based (differentiable) | Joint weight and edge pruning via learnable binary masks trained end-to-end. Unifies weight-level and connection-level circuit discovery, which prior methods treated separately. | [arxiv.org/html/2407.03779v1](https://arxiv.org/html/2407.03779v1/) |\n| **Transcoders** | Transcoders Find Interpretable LLM Feature Circuits | Jacob Dunefsky et al. | 2024 | NeurIPS 2024 | Sparse replacement model | Replaces dense MLP layers with wider, sparsely-activating MLP layers (transcoders) that approximate the original. Enables weights-based circuit analysis through MLPs, decomposing circuits into input-dependent and input-invariant terms. | [arxiv.org/abs/2406.11944](https://arxiv.org/abs/2406.11944) |\n| **Sparse Feature Circuits** | Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | Samuel Marks et al. | 2024 | ICLR 2025 | Attribution-based (SAE features) | Discovers circuits over SAE-learned sparse features rather than neurons/heads. Introduces SHIFT for editing model behavior by removing task-irrelevant features. Fully unsupervised pipeline discovering thousands of circuits at scale. | [arxiv.org/abs/2403.19647](https://arxiv.org/abs/2403.19647) |\n| **Circuit Tracing (Attribution Graphs)** | Circuit Tracing: Revealing Computational Graphs in Language Models | Emmanuel Ameisen, Chris Olah et al. (Anthropic, 26 authors) | 2025 | Anthropic Technical Report | Sparse replacement model + attribution | Replaces MLPs with cross-layer transcoders (CLTs) to build a \"replacement model\" of interpretable sparse features. Constructs per-prompt attribution graphs (DAGs) with linear edges between features. Applied to Claude 3.5 Haiku. | [transformer-circuits.pub](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) |\n| **GIM** | GIM: Improved Interpretability for Large Language Models | Joakim Edin et al. (Corti) | 2025 | arXiv (under review) | Gradient-based (modified backprop) | Addresses self-repair in attention (softmax redistribution) and LayerNorm by modifying gradient computation during backpropagation. Temperature-adjusted softmax gradients + LayerNorm freeze + gradient normalization. Tops HuggingFace MIB benchmark. | [arxiv.org/abs/2505.17630](https://arxiv.org/abs/2505.17630) |\n| **HAP** | Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework | Hao Gu et al. (Algoverse) | 2025 | arXiv preprint | Hybrid (attribution + pruning) | Sequences EAP (fast, approximate) then Edge Pruning (faithful) on the EAP-filtered subgraph. 46% faster than EP alone with comparable faithfulness. Preserves cooperative circuit components (e.g., S-inhibition heads) that pure attribution misses. | [arxiv.org/html/2510.03282v1](https://arxiv.org/html/2510.03282v1) |\n| **ModCirc** | Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of LLMs | Yinhan He et al. | 2025 | ICML 2025 | Modular decomposition | Discovers task-agnostic modular circuit vocabularies shared across language tasks, rather than task-specific circuits. Defines five criteria characterizing modular circuits. Enables global-level interpretability with reusable interpretations. | [openreview.net/forum?id=do5vVfKEXZ](https://openreview.net/forum?id=do5vVfKEXZ) |\n| **Stream** | Stream: Scaling up Mechanistic Interpretability to Long Context in LLMs via Sparse Attention | J. Rosser et al. | 2025 | arXiv preprint | Hierarchical pruning | Compilable hierarchical pruning algorithm for per-head sparse attention masks in O(T log T) time. Binary-search-style refinement retains top-k key blocks per query. Prunes 97--99% of token interactions, enabling interpretability at 100K+ tokens on consumer GPUs. | [arxiv.org/abs/2510.19875](https://arxiv.org/abs/2510.19875) |\n| **Weight-Sparse Circuits** | Weight-sparse transformers have interpretable circuits | Leo Gao et al. (OpenAI) | 2025 | arXiv preprint | Sparsity-constrained training | Trains transformers with extreme weight sparsity (~1 in 1000 nonzero). Resulting circuits are ~16x smaller than those from dense baselines. Neurons correspond to natural concepts with interpretable connections. Defines a capability--interpretability frontier. | [arxiv.org/abs/2511.13653](https://arxiv.org/abs/2511.13653) |\n| **Formal MI (Verification-based)** | Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | Itamar Hadad et al. | 2026 | ICLR 2026 | Verification-based | First to use neural network verification for circuit discovery. Provides three provable guarantees: (1) input domain robustness, (2) robust patching over continuous perturbations, (3) minimality. Eliminates reliance on heuristics. | [arxiv.org/abs/2602.16823](https://arxiv.org/abs/2602.16823) |\n| **SVD Directional Masking** | Beyond Components: Singular Vector-Based Interpretability of Transformer Circuits | Areeb Ahmad et al. | 2025 | arXiv preprint | SVD + differentiable masking | Decomposes attention heads and MLPs into orthogonal singular directions via SVD, revealing superposed subfunctions within single heads. Learnable diagonal masks on singular values identify functionally important directions. | [arxiv.org/html/2511.20273](https://arxiv.org/html/2511.20273) |\n\n---\n\n**Notable non-method papers relevant to the field:**\n\n| **Paper** | **Authors** | **Year** | **Venue** | **Relevance** |\n|---|---|---|---|---|\n| The Computational Complexity of Circuit Discovery for Inner Interpretability | Federico Adolfi et al. | 2025 | ICLR 2025 (Spotlight) | Proves many circuit-finding queries are NP-hard and inapproximable; establishes fundamental complexity barriers. |\n| MIB: A Mechanistic Interpretability Benchmark | Aaron Mueller et al. (20+ authors) | 2025 | ICML 2025 | Standard benchmark with two tracks (circuit localization, causal variable localization) across 5 models. Attribution and mask optimization methods lead on circuit localization. |\n| InterpBench: Semi-Synthetic Transformers for Evaluating MI Techniques | Rohan Gupta et al. | 2024 | NeurIPS 2024 | Semi-synthetic transformers with known ground-truth circuits for evaluating discovery methods. Uses Strict IIT training. |\n\n**Key trends observed:**\n\n1. **Decomposition over patching**: CD-T and SVD directional masking avoid activation patching entirely, using mathematical decomposition for speedups of orders of magnitude.\n2. **Feature-level circuits**: Sparse Feature Circuits, Transcoders, and Anthropic's Circuit Tracing all operate over learned sparse features (via SAEs or transcoders) rather than raw neurons/heads, yielding more interpretable units.\n3. **Formal guarantees**: The verification-based approach (ICLR 2026) is the first to provide provable correctness, addressing a long-standing gap.\n4. **Sparsity by design**: OpenAI's weight-sparse training creates models that are inherently more interpretable, sidestepping post-hoc discovery entirely.\n5. **Scaling**: Stream and GIM specifically target practical scalability -- long contexts and production-scale models respectively."
      }
    ],
    "totalDurationMs": 175345,
    "totalTokens": 39682,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 36975,
      "output_tokens": 2325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 379
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2325,
          "cache_read_input_tokens": 36975,
          "cache_creation_input_tokens": 379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 379,
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
      "otherToolCount": 31
    }
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-12T22:10:52.531Z_

<details><summary>↩ Tool result · `toolu_01YLEqv93CypvBxzJontBcKh`</summary>

```text
Web search results for query: "structfuse context-aware fusion circuit discovery methods 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf"},{"title":"Accepted Tutorials - FUSION 2025","url":"https://fusion2025.org/tutorials/"},{"title":"2025-2026 Fusion Course Catalog by Fusion Academy - Issuu","url":"https://issuu.com/fusionacademy/docs/2025-2026_fusion_course_catalog"},{"title":"Home - FUSION 2026 - NTNU","url":"https://www.ntnu.edu/fusion2026"},{"title":"FUSION 2025-2025 28th International Conference on Information Fusion--iConf","url":"https://www.iconf.org/conference/fusion2025"},{"title":"29th International Conference on Information Fusion (FUSION 2026), 23-26 Jun 2026 | Conference Locate (Clocate)","url":"https://www.clocate.com/international-conference-on-information-fusion-fusion/14439/"},{"title":"Fusion Conferences 2026/2027/2028 - Conference Index","url":"https://conferenceindex.org/conferences/fusion"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Multi-Sensor Data Fusion and Machine Learning for ...","url":"https://escholarship.org/content/qt1w8631sp/qt1w8631sp.pdf"},{"title":"Context-Enhanced Information Fusion","url":"https://www.sto.nato.int/publications/STO%20Educational%20Notes/STO-EN-IST-155/EN-IST-155-04.pdf"}]

Based on the search results, I found relevant information about circuit discovery methods. The most relevant result is a paper published at ICLR 2025.

CircuitFusion is the first multimodal fused and implementation-aware circuit encoder designed to capture informative general circuit representations, leveraging the multimodal nature of circuits by encoding them separately under three modalities (HDL code, structural graph, and functionality summary) through three independent unimodal encoders.

The approach proposes four tasks to capture structural and semantic information, while aligning the netlist stage for implementation awareness.

A retrieval-augmented inference method is used to improve CircuitFusion for downstream tasks, utilizing the pre-trained encoder to retrieve similar circuits during inference on new designs and use their design quality metrics as references.

The paper appears to be a significant contribution to circuit design automation and representation learning, presenting methods for context-aware fusion in circuit discovery presented at ICLR 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "fe9e5866-bed5-48d6-8e74-e1c5e87480e0"
}
```

</details>

---


### Tool result

_source line 406 · 2026-05-12T22:10:53.194Z_

<details><summary>↩ Tool result · `toolu_01RsV3gf159R7PVu9iQ43Sc4`</summary>

```text
# ICLR 2025 Poster Confirmation

Yes, this is confirmed as an **ICLR 2025 poster**.

## Full Details

**Title:** "Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable?"

**Authors:** Maxime Méloux, Silviu Maniu, François Portet, Maxime Peyrard

**Paper ID:** 30956

**Core Question:** The work investigates whether mechanistic interpretability explanations are uniquely identifiable—that is, "for a fixed behavior to explain...are we guaranteed a unique explanation?"

**Two Strategies Examined:**
1. "Where-then-what": Identifies network circuits replicating behavior, then interprets them
2. "What-then-where": Tests candidate algorithms against neural network activation subspaces

**Key Findings:** The research demonstrates "overwhelming evidence of non-identifiability in all cases," showing multiple circuits, interpretations, and algorithms can explain the same neural network behavior.

**Resources Available:**
- Project Page
- Slides (PDF)
- OpenReview forum link

The research contributes to formalizing expectations for AI explanations and discusses whether uniqueness is necessary for meaningful interpretability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "6404a62b-456b-4e2c-a3a8-3cf96ecb0249"
}
```

</details>

---


### System

_source line 407_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for binary consensus voting edges circuit discovery m…",
  "usage": {
    "total_tokens": 29957,
    "tool_uses": 19,
    "duration_ms": 183802
  },
  "last_tool_name": "WebSearch",
  "uuid": "7e810681-10f2-4689-b0c8-939e83ee0482",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 408_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KVEsx7AmGuBpew3rAAYnx3`</summary>

```json
{
  "query": "binary consensus voting edges circuit discovery multiple methods ACDC subnetwork probing edge pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "11832cfc-e1e1-42c0-8620-1032d0f852ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wg73UtEE9MkB4tQM2gkMG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 28453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 786,
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

_source line 409_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "description": "Q4: Top venue circuit papers 2024-2025",
  "usage": {
    "total_tokens": 50007,
    "tool_uses": 45,
    "duration_ms": 177479
  },
  "last_tool_name": "ToolSearch",
  "uuid": "bb33f45f-23e3-4bd8-8a3d-97c115b179aa",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 410_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SWZaeVVxmXW3TUwH6QiuxC`</summary>

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
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e6d2f1ec-c20c-430c-869b-24bf7127e981",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzuT37MbWx8Vyq3Sm8qpfV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 49171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 436,
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

_source line 411 · 2026-05-12T22:10:58.652Z_

<details><summary>↩ Tool result · `toolu_01SWZaeVVxmXW3TUwH6QiuxC`</summary>

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
  "parent_tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "3ce94b88-f365-4403-9aa0-77861c190394"
}
```

</details>

---


### Tool result

_source line 412 · 2026-05-12T22:11:10.781Z_

<details><summary>↩ Tool result · `toolu_01KVEsx7AmGuBpew3rAAYnx3`</summary>

```text
Web search results for query: "binary consensus voting edges circuit discovery multiple methods ACDC subnetwork probing edge pruning"

Links: [{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"ACDC (not that one) - by Grigory Sapunov - Gonzo ML","url":"https://gonzoml.substack.com/p/acdc-towards-automated-circuit-discovery"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"Automatic Circuit Discovery (ACDC)","url":"https://www.emergentmind.com/topics/automatic-circuit-discovery-acdc"},{"title":"Automatic Circuit Discovery","url":"https://sidn.baulab.info/autocircuits/"},{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery · GitHub","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery"},{"title":"GitHub - Phylliida/ACDC: An alternative implementation of ACDC (Automated Circuit Discovery) · GitHub","url":"https://github.com/Phylliida/ACDC"},{"title":"IBCircuit: Towards Holistic Circuit Discovery with Information Bottleneck","url":"https://arxiv.org/html/2602.22581"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"(PDF) Long route to consensus: Two-stage coarsening in a binary choice voting model","url":"https://www.academia.edu/65938720/Long_route_to_consensus_Two_stage_coarsening_in_a_binary_choice_voting_model"}]

Based on the search results, I found comprehensive information about the topics you're interested in. Here's what the research reveals:

## ACDC (Automated Circuit Discovery)

Automated Circuit DisCovery (ACDC) is an attempt to formalize and automate the process of circuit discovery. ACDC formalizes the search for subnetworks—termed "circuits"—that are minimal and functionally sufficient to produce a desired behavior within a model or physical system. In transformer-based language and vision models, a circuit is a sparse subgraph of the overall computation graph (nodes: e.g., attention heads, MLPs, neurons; edges: data flow between nodes), whose activation flow implements a specific cognitive or algorithmic function.

## Algorithm Mechanism

ACDC iterates from outputs to inputs in the computation graph, starting with the output node (nodes are topologically sorted in reverse order). At each node, the algorithm tries to remove as many incoming edges as possible while maintaining model performance on the chosen metric. Performance degradation is evaluated using KL-divergence, and an edge is removed if the change is below a specified threshold τ>0.

## Multiple Methods for Circuit Discovery

Alternatives to ACDC exist, including Subnetwork Probing (SP) and Head Importance Score for Pruning (HISP). Additionally, SP optimizes a mask over model components using gradient descent, while HISP uses a first-order Taylor approximation to estimate the effect of replacing a head's output with corrupted inputs.

## Evaluation Approach

The authors used previously discovered canonical circuits as ground truth and treated it as a binary classification problem for each graph edge. These questions map to high true-positive rate (TPR) for Q1 and low false-positive rate (FPR) for Q2, which can be evaluated using ROC curves.

## Recent Advances: CIRCUS

CIRCUS addresses this by adapting stability selection (Meinshausen and Bühlmann, 2010) to circuit discovery. The resulting per-edge scores play a role analogous to posterior inclusion probabilities in Bayesian variable selection: they summarize which structural claims are supported across plausible analysis choices, enabling the analyst to abstain from reporting unstable edges.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "97ab241b-881a-453d-913f-385a3f18999e"
}
```

</details>

---


### System

_source line 413_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a12b9308a37a2d7a7",
  "tool_use_id": "toolu_01LDQfvBwWGQLX9DkoSBc9AR",
  "status": "completed",
  "output_file": "",
  "summary": "Q1: Circuit method consistency comparison",
  "usage": {
    "total_tokens": 40924,
    "tool_uses": 35,
    "duration_ms": 206230
  },
  "uuid": "180adc96-0871-4497-ac2f-e6c189211f1e",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool result

_source line 414 · 2026-05-12T22:11:13.502Z_

<details><summary>↩ Tool result · `toolu_01LDQfvBwWGQLX9DkoSBc9AR`</summary>

```text


Here is the comprehensive literature survey on cross-method comparison and consistency in circuit discovery.

---

## Summary of Findings

**No paper directly studies "cross-method binary consensus" as a first-class research question.** No existing work systematically takes multiple circuit discovery methods, runs them on the same tasks, binarizes each method's output into edge-level masks, and then measures agreement rates (e.g., Jaccard, intersection-over-union, Cohen's kappa) across methods. This is a clear gap in the literature.

However, several papers are closely adjacent and provide partial evidence or related frameworks. Below are the relevant papers organized by relevance.

---

## Tier 1: Papers That Directly Compare Multiple Circuit Discovery Methods

### 1. "Towards Automated Circuit Discovery for Mechanistic Interpretability"
- **Authors:** Conmy, Mavor-Parker, Lynch, Heimersheim, Garriga-Alonso
- **Year/Venue:** NeurIPS 2023
- **URL:** https://arxiv.org/abs/2304.14997
- **Methods compared:** ACDC vs. Subnetwork Probing (SP) vs. Head Importance Score Pruning (HISP)
- **Key findings:** ACDC achieved ROC AUC of 0.982 on Docstring (vs. SP 0.937, HISP 0.805) and 0.853 on Greater-Than (vs. SP 0.806, HISP 0.693). All manually-identified heads were recovered by ACDC, but ACDC also found additional components not in manual circuits.
- **Re: cross-method consensus:** Compares methods via ROC AUC against ground-truth manual circuits, but does NOT measure pairwise agreement between automated methods themselves.

### 2. "Attribution Patching Outperforms Automated Circuit Discovery"
- **Authors:** Syed, Rager, Conmy
- **Year/Venue:** NeurIPS 2023 ATTRIB Workshop; BlackboxNLP 2024 (ACL Anthology)
- **URL:** https://arxiv.org/abs/2310.10348
- **Methods compared:** EAP vs. ACDC vs. SP vs. HISP
- **Key findings:** EAP achieves greater AUC from circuit recovery than ACDC while requiring only two forward passes and one backward pass (vs. ACDC's exponential scaling). EAP is competitive with ACDC on recovering ground-truth circuits.
- **Re: cross-method consensus:** Evaluates each method against ground-truth via AUC. Does not measure inter-method overlap or agreement directly.

### 3. "Finding Transformer Circuits with Edge Pruning"
- **Authors:** Bhaskar, Wettig, Friedman, Chen
- **Year/Venue:** NeurIPS 2024 (Spotlight)
- **URL:** https://arxiv.org/abs/2406.16778
- **Methods compared:** Edge Pruning vs. ACDC vs. EAP
- **Key findings:** Edge Pruning is "considerably more faithful on IOI and GT than both ACDC and EAP, especially at higher sparsities." Scales to CodeLlama-13B (100x larger). Finds circuits with less than half the edges of prior methods.
- **Re: cross-method consensus:** Shows methods disagree substantially on which edges matter, especially at high sparsity. Edge Pruning finds sparser, more faithful circuits than EAP/ACDC, implying the circuits do NOT fully overlap.

### 4. "Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition" (CD-T)
- **Authors:** Hsu, Zhou, Cherapanamjeri, Huang, Odisho, Carroll, Yu
- **Year/Venue:** ICLR 2025
- **URL:** https://arxiv.org/abs/2407.00886
- **Methods compared:** CD-T vs. ACDC vs. EAP
- **Key findings:** CD-T achieves 97% ROC AUC on average for recovering manual circuits, outperforming ACDC and EAP. Optimal granularity varies by task (fine-grained for IOI, coarse for Greater-Than).
- **Re: cross-method consensus:** Evaluates against ground-truth circuits. Notes that manual circuits of the same size still exhibit higher faithfulness than any automated method, suggesting all automated methods miss some edges.

### 5. "GIM: Improved Interpretability for Large Language Models"
- **Authors:** Edin, Csordás, Ruotsalo, Wu, Maistro, Christensen, Huang, Maaløe
- **Year/Venue:** 2025 (arXiv, tops HuggingFace MIB leaderboard)
- **URL:** https://arxiv.org/abs/2505.17630
- **Methods compared:** GIM vs. EActP, EAP, EAP-IG, NAP, IFR, UGS
- **Key findings:** GIM significantly outperforms other gradient-based methods in early layers; Integrated Gradients has slight advantages in middle/late layers. Tested across Gemma, LLAMA, Qwen families.
- **Re: cross-method consensus:** Compares faithfulness metrics across methods but does not measure structural overlap between discovered circuits.

---

## Tier 2: Papers That Address Method Agreement / Disagreement Directly

### 6. "Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms"
- **Authors:** Hanna, Pezzelle, Belinkov
- **Year/Venue:** 2024 (arXiv)
- **URL:** https://arxiv.org/abs/2403.17806
- **Methods compared:** EAP vs. EAP-IG (with causal intervention baseline)
- **Key findings:** **This is the closest paper to the "consensus" question.** It shows that EAP and EAP-IG circuits have HIGH NODE OVERLAP with causal intervention circuits, yet EAP circuits are LESS FAITHFUL than EAP-IG circuits. The critical insight: **overlap ≠ faithfulness**. Two methods can agree on ~same edges yet produce circuits with very different functional properties.
- **Re: cross-method consensus:** Directly measures node overlap between methods and shows it is misleading. Argues faithfulness, not overlap, should be the evaluation criterion. This is a strong cautionary result for any "binary consensus" approach.

### 7. "Mechanistic Interpretability as Statistical Estimation: A Variance Analysis"
- **Authors:** Méloux, Portet, Peyrard
- **Year/Venue:** 2025 (arXiv, v3 Feb 2026)
- **URL:** https://arxiv.org/abs/2510.00845
- **Methods compared:** Focuses on EAP-IG variants (does NOT compare across fundamentally different methods)
- **Key findings:** **Circuits are highly unstable.** Bootstrap resampling produces circuits with Jaccard index of only 0.561. Hyperparameter variations yield Jaccard similarities ranging from 0.086 to 1.0. Small perturbations in input data or hyperparameters yield "vastly different circuits." The method can converge to "multiple, distinct, yet stable circuit solutions."
- **Re: cross-method consensus:** Uses Jaccard index to measure overlap but only WITHIN one method under different conditions. Does NOT compare across methods. The finding of extreme instability within a single method raises serious questions about whether cross-method consensus is meaningful if intra-method consistency is already low.

---

## Tier 3: Ensemble / Aggregation Approaches (Most Relevant to "Binary Consensus")

### 8. "BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods"
- **Authors:** Mondorf, Wang, Gerstner, Hakimi, Liu, Veloso, Zhou, Schütze, Plank
- **Year/Venue:** BlackboxNLP 2025 (ACL Workshop)
- **URL:** https://arxiv.org/abs/2510.06811
- **Methods ensembled:** EAP, EAP-IG-inputs, EAP-IG-activations, Edge Pruning
- **Key findings:** **This is the most directly relevant paper to "binary consensus."** They explicitly frame score aggregation in binary terms:
  - **Maximum** = union of circuits (edge selected by ANY method)
  - **Minimum** = intersection of circuits (edge selected by ALL methods)
  - **Mean** = soft consensus
  - Result: **Mean outperforms both union and intersection.** The hybrid ensemble (parallel + sequential) achieved best results (CMD 0.03, CPR 1.83).
- **Re: cross-method consensus:** Directly implements union/intersection as binary consensus operations. However, they do NOT report the agreement rate itself (what fraction of edges are selected by all methods vs. only one). They treat it as a score combination problem, not an analysis of disagreement.

### 9. "Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models"
- **Authors:** Arad, Belinkov, Chen, Kim, Mohebbi, Mueller, Sarti, Tutek
- **Year/Venue:** BlackboxNLP 2025
- **URL:** https://arxiv.org/abs/2511.18409
- **Key findings:** 3 teams, 8 methods. Ensemble and regularization strategies were most effective. Methods that "filter components with unstable contributions" performed best.
- **Re: cross-method consensus:** Does not report inter-method agreement statistics.

### 10. "MIB: A Mechanistic Interpretability Benchmark"
- **Authors:** Mueller, Geiger, Wiegreffe, et al. (25+ authors)
- **Year/Venue:** ICML 2025
- **URL:** https://arxiv.org/abs/2504.13151
- **Methods benchmarked:** Attribution patching, mask optimization, information flow methods
- **Key findings:** Establishes standardized evaluation (faithfulness integral/CPR, minimality, AUROC). Attribution and mask optimization methods perform best. SAEs show no advantage over raw neurons for featurization.
- **Re: cross-method consensus:** Provides a common evaluation framework but does not measure inter-method agreement on discovered circuits.

---

## Tier 4: Additional Related Papers

### 11. "Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework" (HAP)
- **Authors:** Gu, Nair, Kumar, Sharma, Lagasse
- **Year/Venue:** NeurIPS 2025 MechInterp Workshop
- **URL:** https://arxiv.org/abs/2510.03282
- **Methods combined:** Attribution patching → Edge Pruning (sequential)
- **Key findings:** 46% faster than baselines. Case study shows attribution patching prunes S-inhibition heads at high sparsity that HAP preserves — demonstrating that attribution patching and edge pruning disagree on cooperative circuit components.

### 12. "Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees"
- **Authors:** (multiple)
- **Year/Venue:** 2025
- **URL:** https://arxiv.org/abs/2602.16823
- **Key contribution:** Proposes circuits with provable guarantees (robustness, minimality) using neural network verification. Shows standard circuit discovery methods lack robustness guarantees.

---

## Key Takeaways for Novelty Assessment

1. **No paper measures cross-method binary consensus as its primary contribution.** The Mondorf et al. (2025) ensemble paper comes closest by implementing union/intersection operations, but treats it as a practical combination strategy, not an analytical study of agreement.

2. **The evidence strongly suggests methods disagree substantially:**
   - Edge Pruning finds circuits with <50% of the edges that ACDC/EAP find (Bhaskar et al.)
   - High node overlap does NOT imply high faithfulness (Hanna et al.)
   - Even a SINGLE method (EAP-IG) produces circuits with Jaccard ~0.56 under bootstrap resampling (Méloux et al.)
   - Different methods preserve/prune different cooperative components (HAP paper)

3. **The gap is clear:** Nobody has systematically run N methods on the same tasks, binarized the outputs, computed pairwise Jaccard / agreement matrices, and analyzed WHERE methods agree vs. disagree (e.g., by layer, by component type, by edge importance rank). A "cross-method binary consensus" study would be novel.

4. **The Méloux et al. variance paper is the strongest cautionary result:** If intra-method variance is already high (Jaccard 0.56), cross-method consensus may be even lower, or the consensus signal may be more robust than any individual method (which is the hypothesis behind ensembling in Mondorf et al.).

agentId: a12b9308a37a2d7a7 (use SendMessage with to: 'a12b9308a37a2d7a7' to continue this agent)
&lt;usage>total_tokens: 43939
tool_uses: 35
duration_ms: 206231&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2580b9fb-40fa-4a2b-9fe2-cadacd68c941",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability. \n\n**Task**: Find papers that systematically compare different circuit discovery methods (e.g., EAP, ACDC, Edge Pruning, subnetwork probing, activation patching) and evaluate the consistency/agreement of the circuits they find.\n\nSearch using these keyword combinations (at least 3 different searches):\n1. \"circuit discovery comparison mechanistic interpretability\"\n2. \"circuit agreement consistency different methods transformers\"\n3. \"comparing automated circuit discovery ACDC EAP edge pruning\"\n4. \"circuit discovery benchmark evaluation\"\n5. \"mechanistic interpretability methods comparison 2024 2025\"\n\nFor each search, use WebSearch. For any highly relevant paper found, use WebFetch on its arXiv abstract page to confirm the content.\n\n**Output format**: For each relevant paper found, report:\n- Title\n- Authors (first author + et al.)\n- Year / Venue\n- URL\n- What methods they compare\n- Key findings about consistency/disagreement\n- How it relates to \"cross-method binary consensus\" or aggregation\n\nIf no paper directly compares method consistency, say so explicitly. Be thorough - this is the most important question for novelty assessment.",
    "agentId": "a12b9308a37a2d7a7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nHere is the comprehensive literature survey on cross-method comparison and consistency in circuit discovery.\n\n---\n\n## Summary of Findings\n\n**No paper directly studies \"cross-method binary consensus\" as a first-class research question.** No existing work systematically takes multiple circuit discovery methods, runs them on the same tasks, binarizes each method's output into edge-level masks, and then measures agreement rates (e.g., Jaccard, intersection-over-union, Cohen's kappa) across methods. This is a clear gap in the literature.\n\nHowever, several papers are closely adjacent and provide partial evidence or related frameworks. Below are the relevant papers organized by relevance.\n\n---\n\n## Tier 1: Papers That Directly Compare Multiple Circuit Discovery Methods\n\n### 1. \"Towards Automated Circuit Discovery for Mechanistic Interpretability\"\n- **Authors:** Conmy, Mavor-Parker, Lynch, Heimersheim, Garriga-Alonso\n- **Year/Venue:** NeurIPS 2023\n- **URL:** https://arxiv.org/abs/2304.14997\n- **Methods compared:** ACDC vs. Subnetwork Probing (SP) vs. Head Importance Score Pruning (HISP)\n- **Key findings:** ACDC achieved ROC AUC of 0.982 on Docstring (vs. SP 0.937, HISP 0.805) and 0.853 on Greater-Than (vs. SP 0.806, HISP 0.693). All manually-identified heads were recovered by ACDC, but ACDC also found additional components not in manual circuits.\n- **Re: cross-method consensus:** Compares methods via ROC AUC against ground-truth manual circuits, but does NOT measure pairwise agreement between automated methods themselves.\n\n### 2. \"Attribution Patching Outperforms Automated Circuit Discovery\"\n- **Authors:** Syed, Rager, Conmy\n- **Year/Venue:** NeurIPS 2023 ATTRIB Workshop; BlackboxNLP 2024 (ACL Anthology)\n- **URL:** https://arxiv.org/abs/2310.10348\n- **Methods compared:** EAP vs. ACDC vs. SP vs. HISP\n- **Key findings:** EAP achieves greater AUC from circuit recovery than ACDC while requiring only two forward passes and one backward pass (vs. ACDC's exponential scaling). EAP is competitive with ACDC on recovering ground-truth circuits.\n- **Re: cross-method consensus:** Evaluates each method against ground-truth via AUC. Does not measure inter-method overlap or agreement directly.\n\n### 3. \"Finding Transformer Circuits with Edge Pruning\"\n- **Authors:** Bhaskar, Wettig, Friedman, Chen\n- **Year/Venue:** NeurIPS 2024 (Spotlight)\n- **URL:** https://arxiv.org/abs/2406.16778\n- **Methods compared:** Edge Pruning vs. ACDC vs. EAP\n- **Key findings:** Edge Pruning is \"considerably more faithful on IOI and GT than both ACDC and EAP, especially at higher sparsities.\" Scales to CodeLlama-13B (100x larger). Finds circuits with less than half the edges of prior methods.\n- **Re: cross-method consensus:** Shows methods disagree substantially on which edges matter, especially at high sparsity. Edge Pruning finds sparser, more faithful circuits than EAP/ACDC, implying the circuits do NOT fully overlap.\n\n### 4. \"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition\" (CD-T)\n- **Authors:** Hsu, Zhou, Cherapanamjeri, Huang, Odisho, Carroll, Yu\n- **Year/Venue:** ICLR 2025\n- **URL:** https://arxiv.org/abs/2407.00886\n- **Methods compared:** CD-T vs. ACDC vs. EAP\n- **Key findings:** CD-T achieves 97% ROC AUC on average for recovering manual circuits, outperforming ACDC and EAP. Optimal granularity varies by task (fine-grained for IOI, coarse for Greater-Than).\n- **Re: cross-method consensus:** Evaluates against ground-truth circuits. Notes that manual circuits of the same size still exhibit higher faithfulness than any automated method, suggesting all automated methods miss some edges.\n\n### 5. \"GIM: Improved Interpretability for Large Language Models\"\n- **Authors:** Edin, Csordás, Ruotsalo, Wu, Maistro, Christensen, Huang, Maaløe\n- **Year/Venue:** 2025 (arXiv, tops HuggingFace MIB leaderboard)\n- **URL:** https://arxiv.org/abs/2505.17630\n- **Methods compared:** GIM vs. EActP, EAP, EAP-IG, NAP, IFR, UGS\n- **Key findings:** GIM significantly outperforms other gradient-based methods in early layers; Integrated Gradients has slight advantages in middle/late layers. Tested across Gemma, LLAMA, Qwen families.\n- **Re: cross-method consensus:** Compares faithfulness metrics across methods but does not measure structural overlap between discovered circuits.\n\n---\n\n## Tier 2: Papers That Address Method Agreement / Disagreement Directly\n\n### 6. \"Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms\"\n- **Authors:** Hanna, Pezzelle, Belinkov\n- **Year/Venue:** 2024 (arXiv)\n- **URL:** https://arxiv.org/abs/2403.17806\n- **Methods compared:** EAP vs. EAP-IG (with causal intervention baseline)\n- **Key findings:** **This is the closest paper to the \"consensus\" question.** It shows that EAP and EAP-IG circuits have HIGH NODE OVERLAP with causal intervention circuits, yet EAP circuits are LESS FAITHFUL than EAP-IG circuits. The critical insight: **overlap ≠ faithfulness**. Two methods can agree on ~same edges yet produce circuits with very different functional properties.\n- **Re: cross-method consensus:** Directly measures node overlap between methods and shows it is misleading. Argues faithfulness, not overlap, should be the evaluation criterion. This is a strong cautionary result for any \"binary consensus\" approach.\n\n### 7. \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis\"\n- **Authors:** Méloux, Portet, Peyrard\n- **Year/Venue:** 2025 (arXiv, v3 Feb 2026)\n- **URL:** https://arxiv.org/abs/2510.00845\n- **Methods compared:** Focuses on EAP-IG variants (does NOT compare across fundamentally different methods)\n- **Key findings:** **Circuits are highly unstable.** Bootstrap resampling produces circuits with Jaccard index of only 0.561. Hyperparameter variations yield Jaccard similarities ranging from 0.086 to 1.0. Small perturbations in input data or hyperparameters yield \"vastly different circuits.\" The method can converge to \"multiple, distinct, yet stable circuit solutions.\"\n- **Re: cross-method consensus:** Uses Jaccard index to measure overlap but only WITHIN one method under different conditions. Does NOT compare across methods. The finding of extreme instability within a single method raises serious questions about whether cross-method consensus is meaningful if intra-method consistency is already low.\n\n---\n\n## Tier 3: Ensemble / Aggregation Approaches (Most Relevant to \"Binary Consensus\")\n\n### 8. \"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods\"\n- **Authors:** Mondorf, Wang, Gerstner, Hakimi, Liu, Veloso, Zhou, Schütze, Plank\n- **Year/Venue:** BlackboxNLP 2025 (ACL Workshop)\n- **URL:** https://arxiv.org/abs/2510.06811\n- **Methods ensembled:** EAP, EAP-IG-inputs, EAP-IG-activations, Edge Pruning\n- **Key findings:** **This is the most directly relevant paper to \"binary consensus.\"** They explicitly frame score aggregation in binary terms:\n  - **Maximum** = union of circuits (edge selected by ANY method)\n  - **Minimum** = intersection of circuits (edge selected by ALL methods)\n  - **Mean** = soft consensus\n  - Result: **Mean outperforms both union and intersection.** The hybrid ensemble (parallel + sequential) achieved best results (CMD 0.03, CPR 1.83).\n- **Re: cross-method consensus:** Directly implements union/intersection as binary consensus operations. However, they do NOT report the agreement rate itself (what fraction of edges are selected by all methods vs. only one). They treat it as a score combination problem, not an analysis of disagreement.\n\n### 9. \"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models\"\n- **Authors:** Arad, Belinkov, Chen, Kim, Mohebbi, Mueller, Sarti, Tutek\n- **Year/Venue:** BlackboxNLP 2025\n- **URL:** https://arxiv.org/abs/2511.18409\n- **Key findings:** 3 teams, 8 methods. Ensemble and regularization strategies were most effective. Methods that \"filter components with unstable contributions\" performed best.\n- **Re: cross-method consensus:** Does not report inter-method agreement statistics.\n\n### 10. \"MIB: A Mechanistic Interpretability Benchmark\"\n- **Authors:** Mueller, Geiger, Wiegreffe, et al. (25+ authors)\n- **Year/Venue:** ICML 2025\n- **URL:** https://arxiv.org/abs/2504.13151\n- **Methods benchmarked:** Attribution patching, mask optimization, information flow methods\n- **Key findings:** Establishes standardized evaluation (faithfulness integral/CPR, minimality, AUROC). Attribution and mask optimization methods perform best. SAEs show no advantage over raw neurons for featurization.\n- **Re: cross-method consensus:** Provides a common evaluation framework but does not measure inter-method agreement on discovered circuits.\n\n---\n\n## Tier 4: Additional Related Papers\n\n### 11. \"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework\" (HAP)\n- **Authors:** Gu, Nair, Kumar, Sharma, Lagasse\n- **Year/Venue:** NeurIPS 2025 MechInterp Workshop\n- **URL:** https://arxiv.org/abs/2510.03282\n- **Methods combined:** Attribution patching → Edge Pruning (sequential)\n- **Key findings:** 46% faster than baselines. Case study shows attribution patching prunes S-inhibition heads at high sparsity that HAP preserves — demonstrating that attribution patching and edge pruning disagree on cooperative circuit components.\n\n### 12. \"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees\"\n- **Authors:** (multiple)\n- **Year/Venue:** 2025\n- **URL:** https://arxiv.org/abs/2602.16823\n- **Key contribution:** Proposes circuits with provable guarantees (robustness, minimality) using neural network verification. Shows standard circuit discovery methods lack robustness guarantees.\n\n---\n\n## Key Takeaways for Novelty Assessment\n\n1. **No paper measures cross-method binary consensus as its primary contribution.** The Mondorf et al. (2025) ensemble paper comes closest by implementing union/intersection operations, but treats it as a practical combination strategy, not an analytical study of agreement.\n\n2. **The evidence strongly suggests methods disagree substantially:**\n   - Edge Pruning finds circuits with <50% of the edges that ACDC/EAP find (Bhaskar et al.)\n   - High node overlap does NOT imply high faithfulness (Hanna et al.)\n   - Even a SINGLE method (EAP-IG) produces circuits with Jaccard ~0.56 under bootstrap resampling (Méloux et al.)\n   - Different methods preserve/prune different cooperative components (HAP paper)\n\n3. **The gap is clear:** Nobody has systematically run N methods on the same tasks, binarized the outputs, computed pairwise Jaccard / agreement matrices, and analyzed WHERE methods agree vs. disagree (e.g., by layer, by component type, by edge importance rank). A \"cross-method binary consensus\" study would be novel.\n\n4. **The Méloux et al. variance paper is the strongest cautionary result:** If intra-method variance is already high (Jaccard 0.56), cross-method consensus may be even lower, or the consensus signal may be more robust than any individual method (which is the hypothesis behind ensembling in Mondorf et al.)."
      }
    ],
    "totalDurationMs": 206231,
    "totalTokens": 43939,
    "totalToolUseCount": 35,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 40127,
      "output_tokens": 3117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 692
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3117,
          "cache_read_input_tokens": 40127,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 692,
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
      "otherToolCount": 35
    }
  }
}
```

</details>

---


### System

_source line 415_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for \"circuit stability\" \"cross-method\" OR \"inter-meth…",
  "usage": {
    "total_tokens": 31108,
    "tool_uses": 20,
    "duration_ms": 201396
  },
  "last_tool_name": "WebSearch",
  "uuid": "d0c97964-6772-4d22-a80e-52f21a6a5813",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 416_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017TE6DtY561skap7E6nfbSB`</summary>

```json
{
  "query": "\"circuit stability\" \"cross-method\" OR \"inter-method\" OR \"method agreement\" mechanistic interpretability scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "6ecdbfe7-ab72-434c-87fc-29e253e42bf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFn6K8bzzagHgBgoAudyeJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 29239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1101,
        "ephemeral_1h_input_tokens": 0
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

_source line 417 · 2026-05-12T22:11:21.945Z_

<details><summary>↩ Tool result · `toolu_017TE6DtY561skap7E6nfbSB`</summary>

```text
Web search results for query: ""circuit stability" "cross-method" OR "inter-method" OR "method agreement" mechanistic interpretability scoring"

Links: [{"title":"Certified Circuits: Stability Guarantees for Mechanistic Circuits","url":"https://arxiv.org/html/2602.22968"},{"title":"MECHANISTIC INTERPRETABILITY AS STATISTICAL ESTIMATION:","url":"https://www.arxiv.org/pdf/2510.00845"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG","url":"https://arxiv.org/html/2510.00845v2"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"},{"title":"Bridging the Black Box: A Survey on Mechanistic Interpretability in AI | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3787104"},{"title":"Mechanistic Interpretability in Neural Networks","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-method"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis","url":"https://arxiv.org/html/2510.00845"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"}]

The search results address important aspects of circuit stability and mechanistic interpretability scoring. Here are the key findings:

## Circuit Stability in Mechanistic Interpretability

Interpretability methods such as circuit discovery should be viewed as statistical estimators, subject to questions of variance and robustness. The circuits identified by EAP exhibit high variance under data resampling and are sensitive to hyperparameter choices: small perturbations in data or changes in the analysis pipeline often yield substantially different circuit structures.

## Cross-Method and Method Agreement Issues

A critical but often unstated issue is that the result depends on arbitrary analyst choices: two different pruning thresholds yield two different circuits, with no principled way to tell which edges reflect genuine model structure versus threshold sensitivity. This is, at its core, an uncertainty quantification problem: the analyst faces a family of plausible explanations and must decide which structural claims are robust.

To address this, CIRCUS reframes circuit discovery as a problem of uncertainty over explanations. CIRCUS prunes one attribution graph under multiple configurations and measures robustness across the configuration family, yielding a core/contingent/noise decomposition that separates robust structure from threshold-sensitive artifacts.

## Scoring and Evaluation Metrics

The Mechanistic Interpretability Benchmark provides circuit localization and causal variable localization tracks with metrics such as Circuit Performance Ratio (CPR), Circuit Model Distance (CMD), and interchange intervention accuracy to assess the faithfulness, specificity, and utility of discovered mechanisms.

## Best Practices

Best practices for the MI community include the systematic use of bootstrap resampling and the reporting of stability metrics to foster a more rigorous and reliable science of interpretability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "bcdf0888-498d-41d4-a3b9-f4d9276f387c"
}
```

</details>

---


### System

_source line 418_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for InterpBench comparing circuit discovery methods a…",
  "usage": {
    "total_tokens": 32083,
    "tool_uses": 21,
    "duration_ms": 216307
  },
  "last_tool_name": "WebSearch",
  "uuid": "2e00c72c-dfca-453c-afa9-4f26b2f27f3e",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 419_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CWPPJncpA96Vjbfs6mZ3GY`</summary>

```json
{
  "query": "InterpBench comparing circuit discovery methods agreement overlap benchmark semi-synthetic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "5e9a2d2b-e124-4242-ad17-17f36872c585",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WF7hk7mxkXmoYQsnJaRtRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 30340,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 936,
        "ephemeral_1h_input_tokens": 0
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

_source line 420 · 2026-05-12T22:11:35.023Z_

<details><summary>↩ Tool result · `toolu_01CWPPJncpA96Vjbfs6mZ3GY`</summary>

```text
Web search results for query: "InterpBench comparing circuit discovery methods agreement overlap benchmark semi-synthetic"

Links: [{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques | OpenReview","url":"https://openreview.net/forum?id=R9gR9MPuD5"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://arxiv.org/html/2407.14494v2"},{"title":"[2407.14494] InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://arxiv.org/abs/2407.14494"},{"title":"INTERPBENCH: Semi-Synthetic Transformers for ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/a8f7d43ae092d9a5295775eb17f3f4f7-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"NeurIPS Poster InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://neurips.cc/virtual/2024/poster/97689"},{"title":"(PDF) InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://www.researchgate.net/publication/382445770_InterpBench_Semi-Synthetic_Transformers_for_Evaluating_Mechanistic_Interpretability_Techniques"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques | alphaXiv","url":"https://www.alphaxiv.org/overview/2407.14494v1"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques | FAR.AI","url":"https://far.ai/research/interpbench-semi-synthetic-transformers-for-evaluating-mechanistic-interpretability-techniques"},{"title":"Paper page - InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://huggingface.co/papers/2407.14494"},{"title":"[Quick Review] InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://liner.com/review/interpbench-semisynthetic-transformers-for-evaluating-mechanistic-interpretability-techniques"}]

Based on the search results, here's information about InterpBench:

## Overview

InterpBench is a collection of semi-synthetic yet realistic transformers with known circuits for evaluating mechanistic interpretability techniques. Mechanistic interpretability methods aim to identify the algorithm a neural network implements, but it is difficult to validate such methods when the true algorithm is unknown.

## Methodology

The benchmark uses a stricter version of Interchange Intervention Training (IIT) called Strict IIT (SIIT), which trains neural networks by aligning their internal computation with a desired high-level causal model while also preventing non-circuit nodes from affecting the model's output. SIIT models maintain Tracr's original circuit while being more realistic and can train transformers with larger circuits, like Indirect Object Identification (IOI).

## Comparing Circuit Discovery Methods

The benchmark evaluates five circuit discovery techniques: Automatic Circuit DisCovery (ACDC), Subnetwork Probing (SP) on nodes and edges, Edge Attribution Patching (EAP), and EAP with integrated gradients. On InterpBench, the results conclusively favor ACDC over Node SP with statistical significance (p-value ≈ 0.0004), and EAP with integrated gradients is a strong contender against ACDC.

## Benchmark Scale

Since the initial evaluation on 16 Tracr circuits, InterpBench has been expanded with 69 new models: 10 trained on more Tracr circuits and 59 trained on TracrBench circuits.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "15fc32b7-7af6-4f14-a229-aa6f9cf8fc12"
}
```

</details>

---


### System

_source line 421_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for \"Méloux\" OR \"Peyrard\" EAP variance circuit stabil…",
  "usage": {
    "total_tokens": 33196,
    "tool_uses": 22,
    "duration_ms": 226239
  },
  "last_tool_name": "WebSearch",
  "uuid": "6fb9ab56-8d49-4ede-ba4f-7735b4dc1f02",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 422_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HwEm6qt7JjxiVaeNF2AZRo`</summary>

```json
{
  "query": "\"Méloux\" OR \"Peyrard\" EAP variance circuit stability multiple methods aggregation union median"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "7487b351-3fe1-474a-abde-f1c020e763c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiKDrFq5QgwRU5GTPF7PSG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 31276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1077,
        "ephemeral_1h_input_tokens": 0
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

_source line 423 · 2026-05-12T22:11:46.265Z_

<details><summary>↩ Tool result · `toolu_01HwEm6qt7JjxiVaeNF2AZRo`</summary>

```text
Web search results for query: ""Méloux" OR "Peyrard" EAP variance circuit stability multiple methods aggregation union median"

Links: [{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG","url":"https://arxiv.org/html/2510.00845v2"},{"title":"Maxime Méloux","url":"https://www.catalyzex.com/author/Maxime%20M%C3%A9loux"},{"title":"[2510.00845] Mechanistic Interpretability as Statistical Estimation: A Variance Analysis","url":"https://arxiv.org/abs/2510.00845"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis","url":"https://arxiv.org/html/2510.00845"},{"title":"[Literature Review] Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG","url":"https://www.themoonlight.io/en/review/mechanistic-interpretability-as-statistical-estimation-a-variance-analysis-of-eap-ig"},{"title":"Stability analysis of solutions in the helicoidal Peyrard -","url":"https://www.arxiv.org/pdf/2501.06967"},{"title":"Reliability Issues in High-Stakes Educational Tests | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-030-18480-3_11"},{"title":"The Dead Salmons of AI Interpretability - Archive ouverte HAL","url":"https://hal.science/hal-05449504v1"},{"title":"Microwaves101 | Stability factor","url":"https://www.microwaves101.com/encyclopedias/stability-factor"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"}]

Based on the search results, I found relevant research on this topic. The query returns results about a paper by Méloux and Peyrard on mechanistic interpretability and circuit discovery.

## Summary of Findings

The research focuses on Edge Activation Patching with Integrated Gradients (EAP-IG), which combines causal patching with gradient-based attribution to score individual edge importance and measures the impact of excluded components when producing a circuit.

The authors present a systematic stability analysis of this state-of-the-art circuit discovery method through a comprehensive suite of controlled perturbations, including input resampling, prompt paraphrasing, hyperparameter variation, and injected noise within the causal analysis itself.

Operational hyperparameters investigated include aggregation type (e.g., mean, median) and intervention type (e.g., zero ablation, patching from corrupted input, mean/mean-positional ablation).

Key findings related to your query include:

- Circuit discovery pipelines inherit variance from the base layer and further amplify it, with fast approximation methods introducing additional estimation noise, while aggregating these noisy scores over datasets leads to fragile structural estimates.

- The study differentiates between two sources of instability: Variance, which is the statistical variability of the discovered circuit when resampling the input data.

- The choice of EAP variant and hyperparameters significantly alters discovered circuit structures, with Jaccard similarities to the median circuit ranging widely.

The research also addresses methods for combining multiple analyses, as reflected in discussions of aggregation approaches and union-based methods for circuit discovery under uncertainty.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2e0730fd-4d94-410e-8271-b100b1147deb"
}
```

</details>

---


### System

_source line 424_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "acd29577a78bc2c01",
  "tool_use_id": "toolu_011k1dq6zk5AsEF3sipmxFHp",
  "status": "completed",
  "output_file": "",
  "summary": "Q4: Top venue circuit papers 2024-2025",
  "usage": {
    "total_tokens": 50394,
    "tool_uses": 45,
    "duration_ms": 233628
  },
  "uuid": "0936d02c-11f6-4a7a-9903-0da26569f41e",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool result

_source line 425 · 2026-05-12T22:11:54.800Z_

<details><summary>↩ Tool result · `toolu_011k1dq6zk5AsEF3sipmxFHp`</summary>

```text


Here is the compiled literature survey table. I excluded papers that are only workshop papers, papers not yet accepted at the target venues, and papers outside the scope (ICLR 2026, general XAI, etc.).

---

| Paper Title | Conference + Year | Main Contribution | URL |
|---|---|---|---|
| **Sparse Autoencoders Find Highly Interpretable Features in Language Models** | ICLR 2024 | Uses sparse autoencoders to discover monosemantic, interpretable features in LM residual streams, resolving superposition and enabling finer-grained causal analysis of circuits (e.g., IOI task) than neuron-level methods. | [OpenReview](https://openreview.net/forum?id=F76bwRSLeK) |
| **Towards Best Practices of Activation Patching in Language Models: Metrics and Methods** | ICLR 2024 | Systematically examines how methodological choices (corruption method, evaluation metric) in activation patching affect circuit discovery results, and provides best-practice recommendations for reliable circuit analysis. | [OpenReview](https://openreview.net/forum?id=Hf17y6u9BC) |
| **Circuit Component Reuse Across Tasks in Transformer Language Models** | ICLR 2024 | Demonstrates that circuits are not purely task-specific: the IOI circuit in GPT-2 is ~78% reused for the Colored Objects task, providing evidence that circuit-level insights generalize across tasks. | [arXiv](https://arxiv.org/abs/2310.08744) |
| **Successor Heads: Recurring, Interpretable Attention Heads In The Wild** | ICLR 2024 | Discovers and mechanistically explains "successor heads" — attention heads that perform incrementation (e.g., Monday→Tuesday) — recurring across architectures from 31M to 12B parameters. | [OpenReview](https://openreview.net/forum?id=kvcbV8KQsi) |
| **Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models** | ICLR 2025 (Oral) | Combines SAE-based dictionary learning with causal analysis to discover sparse feature circuits — human-interpretable causal subgraphs at the SAE-feature level — and demonstrates downstream editing (SHIFT) and unsupervised pipeline for thousands of circuits. | [OpenReview](https://openreview.net/forum?id=I4e82CIDxv) |
| **Scaling and Evaluating Sparse Autoencoders** | ICLR 2025 (Oral) | Proposes k-sparse autoencoders with systematic scaling laws; trains a 16M-latent SAE on GPT-4 activations; introduces new evaluation metrics for feature quality (recovery, explainability, downstream sparsity). Foundational infrastructure for SAE-based circuit work. | [OpenReview](https://openreview.net/forum?id=tcsZt9ZNKD) |
| **Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition** | ICLR 2025 | Introduces CD-T, which reduces automated circuit discovery runtime from hours to seconds while achieving 97% avg ROC AUC on standard benchmarks (IOI, greater-than, docstring), and supports circuits at any granularity level. | [arXiv](https://arxiv.org/abs/2407.00886) |
| **The Computational Complexity of Circuit Discovery for Inner Interpretability** | ICLR 2025 (Spotlight) | Proves that many circuit-finding queries are NP-hard / Σ²_p-hard and inapproximable; identifies tractable sub-queries that retain useful affordances, establishing theoretical limits of automated circuit discovery. | [OpenReview](https://openreview.net/forum?id=QogcGNXJVw) |
| **Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable?** | ICLR 2025 | Shows overwhelming non-identifiability in circuit-based interpretability: multiple circuits can replicate behavior, multiple interpretations exist per circuit, and algorithms align with different subspaces — challenging uniqueness assumptions. | [OpenReview](https://openreview.net/forum?id=5IWJBStfU7) |
| **Sparse Autoencoders Do Not Find Canonical Units of Analysis** | ICLR 2025 | Introduces SAE stitching and meta-SAEs to show SAE features are neither complete nor atomic — smaller SAEs miss information, larger SAE latents decompose into combinations — challenging the idea of a canonical feature set. | [OpenReview](https://openreview.net/forum?id=9ca9eHNrdH) |
| **Unifying and Verifying Mechanistic Interpretations: A Case Study with Group Operations** | ICLR 2025 | Unifies prior mechanistic explanations of group-operation networks and translates them into compact formal proofs of model accuracy, connecting interpretability completeness to proof tightness. | [arXiv](https://arxiv.org/abs/2410.07476) |
| **Transcoders Find Interpretable LLM Feature Circuits** | NeurIPS 2024 | Introduces transcoders (sparse MLP approximations) to enable weights-based circuit analysis through MLP sublayers, overcoming a key limitation of attention-head-only circuit methods; validated on models up to 1.4B params. | [NeurIPS](https://neurips.cc/virtual/2024/poster/95736) |
| **LLM Circuit Analyses Are Consistent Across Training and Scale** | NeurIPS 2024 | Tracks circuit emergence over 300B tokens across 70M–2.8B parameter models; finds that task circuits and their algorithms emerge at consistent token counts and replicate across scale, validating small-model circuit studies. | [arXiv](https://arxiv.org/abs/2407.10827) |
| **Compact Proofs of Model Performance via Mechanistic Interpretability** | NeurIPS 2024 | Formalizes using mechanistic interpretability to derive provable accuracy bounds; demonstrates on Max-of-K transformers with 102 proof strategies, finding shorter proofs require deeper mechanistic understanding. | [NeurIPS](https://neurips.cc/virtual/2024/poster/96781) |
| **Hypothesis Testing the Circuit Hypothesis in LLMs** | NeurIPS 2024 | Formalizes circuit criteria (behavior preservation, localization, minimality) and develops hypothesis tests; finds synthetic circuits satisfy idealized properties while discovered Transformer circuits satisfy them to varying degrees. | [NeurIPS](https://neurips.cc/virtual/2024/poster/96582) |
| **InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques** | NeurIPS 2024 (D&B Track) | Creates 86 semi-synthetic transformers with known ground-truth circuits via Strict IIT training; benchmarks ACDC, Edge Attribution Patching, and Subnetwork Probing, finding ACDC and EAP-IG statistically indistinguishable. | [OpenReview](https://openreview.net/forum?id=R9gR9MPuD5) |
| **MIB: A Mechanistic Interpretability Benchmark** | ICML 2025 | Large-scale benchmark for comparing circuit localization methods; evaluates attribution and mask optimization approaches, finding them best-performing for identifying circuits in transformers. | [ICML](https://icml.cc/virtual/2025/poster/43836) |
| **Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models** | ICML 2025 | Proposes ModCirc framework for discovering task-agnostic modular circuit (MC) vocabularies — reusable functional units — addressing the poor cross-task generalizability and high per-task cost of existing circuit discovery. | [OpenReview](https://openreview.net/forum?id=do5vVfKEXZ) |
| **Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis** | ICML 2025 | Tracks circuits across fine-tuning checkpoints; shows component identity is preserved but connection strengths change; introduces circuit-aware LoRA that allocates capacity to most-altered connections for better parameter efficiency. | [OpenReview](https://openreview.net/forum?id=45EIiFd6Oa) |

---

**Notes on scope exclusions:**
- ACDC ("Towards Automated Circuit Discovery for Mechanistic Interpretability") is NeurIPS 2023, outside the requested range.
- "Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees" is ICLR 2026.
- "Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability" — submitted to ICLR 2025 but no confirmed acceptance found.
- "Scaling Sparse Feature Circuits for Studying In-Context Learning" — only found as an ICLR 2025 workshop paper, not main track.
- No ICML 2024 main-track circuit discovery papers were identified; ICML 2024 hosted a large Mechanistic Interpretability Workshop (140+ submissions) but the circuit-relevant papers there were workshop-only.

agentId: acd29577a78bc2c01 (use SendMessage with to: 'acd29577a78bc2c01' to continue this agent)
&lt;usage>total_tokens: 52265
tool_uses: 45
duration_ms: 233630&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "85f8729e-a7a0-4e11-9d5f-4c9e7f1b7341",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are conducting a literature survey on circuit discovery and mechanistic interpretability at top ML venues.\n\n**Task**: Find circuit discovery / mechanistic interpretability papers published at these venues:\n- ICLR 2024, ICLR 2025\n- NeurIPS 2024\n- ICML 2024, ICML 2025\n\nSearch using these queries:\n1. \"circuit discovery ICLR 2024 2025\"\n2. \"mechanistic interpretability NeurIPS 2024\"\n3. \"circuit discovery ICML 2024 2025\"\n4. \"automated interpretability circuits top conference 2024 2025\"\n5. \"mechanistic interpretability ICLR 2025 accepted papers\"\n\nFor each search, use WebSearch. Use WebFetch to confirm venue/year for important papers.\n\n**Output format**: A table with columns:\n- Paper title\n- Conference + Year\n- Main contribution (1-2 sentences)\n- URL\n\nOnly include papers genuinely about circuit discovery or closely related mechanistic interpretability (not general XAI or probing studies).",
    "agentId": "acd29577a78bc2c01",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nHere is the compiled literature survey table. I excluded papers that are only workshop papers, papers not yet accepted at the target venues, and papers outside the scope (ICLR 2026, general XAI, etc.).\n\n---\n\n| Paper Title | Conference + Year | Main Contribution | URL |\n|---|---|---|---|\n| **Sparse Autoencoders Find Highly Interpretable Features in Language Models** | ICLR 2024 | Uses sparse autoencoders to discover monosemantic, interpretable features in LM residual streams, resolving superposition and enabling finer-grained causal analysis of circuits (e.g., IOI task) than neuron-level methods. | [OpenReview](https://openreview.net/forum?id=F76bwRSLeK) |\n| **Towards Best Practices of Activation Patching in Language Models: Metrics and Methods** | ICLR 2024 | Systematically examines how methodological choices (corruption method, evaluation metric) in activation patching affect circuit discovery results, and provides best-practice recommendations for reliable circuit analysis. | [OpenReview](https://openreview.net/forum?id=Hf17y6u9BC) |\n| **Circuit Component Reuse Across Tasks in Transformer Language Models** | ICLR 2024 | Demonstrates that circuits are not purely task-specific: the IOI circuit in GPT-2 is ~78% reused for the Colored Objects task, providing evidence that circuit-level insights generalize across tasks. | [arXiv](https://arxiv.org/abs/2310.08744) |\n| **Successor Heads: Recurring, Interpretable Attention Heads In The Wild** | ICLR 2024 | Discovers and mechanistically explains \"successor heads\" — attention heads that perform incrementation (e.g., Monday→Tuesday) — recurring across architectures from 31M to 12B parameters. | [OpenReview](https://openreview.net/forum?id=kvcbV8KQsi) |\n| **Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models** | ICLR 2025 (Oral) | Combines SAE-based dictionary learning with causal analysis to discover sparse feature circuits — human-interpretable causal subgraphs at the SAE-feature level — and demonstrates downstream editing (SHIFT) and unsupervised pipeline for thousands of circuits. | [OpenReview](https://openreview.net/forum?id=I4e82CIDxv) |\n| **Scaling and Evaluating Sparse Autoencoders** | ICLR 2025 (Oral) | Proposes k-sparse autoencoders with systematic scaling laws; trains a 16M-latent SAE on GPT-4 activations; introduces new evaluation metrics for feature quality (recovery, explainability, downstream sparsity). Foundational infrastructure for SAE-based circuit work. | [OpenReview](https://openreview.net/forum?id=tcsZt9ZNKD) |\n| **Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition** | ICLR 2025 | Introduces CD-T, which reduces automated circuit discovery runtime from hours to seconds while achieving 97% avg ROC AUC on standard benchmarks (IOI, greater-than, docstring), and supports circuits at any granularity level. | [arXiv](https://arxiv.org/abs/2407.00886) |\n| **The Computational Complexity of Circuit Discovery for Inner Interpretability** | ICLR 2025 (Spotlight) | Proves that many circuit-finding queries are NP-hard / Σ²_p-hard and inapproximable; identifies tractable sub-queries that retain useful affordances, establishing theoretical limits of automated circuit discovery. | [OpenReview](https://openreview.net/forum?id=QogcGNXJVw) |\n| **Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable?** | ICLR 2025 | Shows overwhelming non-identifiability in circuit-based interpretability: multiple circuits can replicate behavior, multiple interpretations exist per circuit, and algorithms align with different subspaces — challenging uniqueness assumptions. | [OpenReview](https://openreview.net/forum?id=5IWJBStfU7) |\n| **Sparse Autoencoders Do Not Find Canonical Units of Analysis** | ICLR 2025 | Introduces SAE stitching and meta-SAEs to show SAE features are neither complete nor atomic — smaller SAEs miss information, larger SAE latents decompose into combinations — challenging the idea of a canonical feature set. | [OpenReview](https://openreview.net/forum?id=9ca9eHNrdH) |\n| **Unifying and Verifying Mechanistic Interpretations: A Case Study with Group Operations** | ICLR 2025 | Unifies prior mechanistic explanations of group-operation networks and translates them into compact formal proofs of model accuracy, connecting interpretability completeness to proof tightness. | [arXiv](https://arxiv.org/abs/2410.07476) |\n| **Transcoders Find Interpretable LLM Feature Circuits** | NeurIPS 2024 | Introduces transcoders (sparse MLP approximations) to enable weights-based circuit analysis through MLP sublayers, overcoming a key limitation of attention-head-only circuit methods; validated on models up to 1.4B params. | [NeurIPS](https://neurips.cc/virtual/2024/poster/95736) |\n| **LLM Circuit Analyses Are Consistent Across Training and Scale** | NeurIPS 2024 | Tracks circuit emergence over 300B tokens across 70M–2.8B parameter models; finds that task circuits and their algorithms emerge at consistent token counts and replicate across scale, validating small-model circuit studies. | [arXiv](https://arxiv.org/abs/2407.10827) |\n| **Compact Proofs of Model Performance via Mechanistic Interpretability** | NeurIPS 2024 | Formalizes using mechanistic interpretability to derive provable accuracy bounds; demonstrates on Max-of-K transformers with 102 proof strategies, finding shorter proofs require deeper mechanistic understanding. | [NeurIPS](https://neurips.cc/virtual/2024/poster/96781) |\n| **Hypothesis Testing the Circuit Hypothesis in LLMs** | NeurIPS 2024 | Formalizes circuit criteria (behavior preservation, localization, minimality) and develops hypothesis tests; finds synthetic circuits satisfy idealized properties while discovered Transformer circuits satisfy them to varying degrees. | [NeurIPS](https://neurips.cc/virtual/2024/poster/96582) |\n| **InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques** | NeurIPS 2024 (D&B Track) | Creates 86 semi-synthetic transformers with known ground-truth circuits via Strict IIT training; benchmarks ACDC, Edge Attribution Patching, and Subnetwork Probing, finding ACDC and EAP-IG statistically indistinguishable. | [OpenReview](https://openreview.net/forum?id=R9gR9MPuD5) |\n| **MIB: A Mechanistic Interpretability Benchmark** | ICML 2025 | Large-scale benchmark for comparing circuit localization methods; evaluates attribution and mask optimization approaches, finding them best-performing for identifying circuits in transformers. | [ICML](https://icml.cc/virtual/2025/poster/43836) |\n| **Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models** | ICML 2025 | Proposes ModCirc framework for discovering task-agnostic modular circuit (MC) vocabularies — reusable functional units — addressing the poor cross-task generalizability and high per-task cost of existing circuit discovery. | [OpenReview](https://openreview.net/forum?id=do5vVfKEXZ) |\n| **Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis** | ICML 2025 | Tracks circuits across fine-tuning checkpoints; shows component identity is preserved but connection strengths change; introduces circuit-aware LoRA that allocates capacity to most-altered connections for better parameter efficiency. | [OpenReview](https://openreview.net/forum?id=45EIiFd6Oa) |\n\n---\n\n**Notes on scope exclusions:**\n- ACDC (\"Towards Automated Circuit Discovery for Mechanistic Interpretability\") is NeurIPS 2023, outside the requested range.\n- \"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees\" is ICLR 2026.\n- \"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability\" — submitted to ICLR 2025 but no confirmed acceptance found.\n- \"Scaling Sparse Feature Circuits for Studying In-Context Learning\" — only found as an ICLR 2025 workshop paper, not main track.\n- No ICML 2024 main-track circuit discovery papers were identified; ICML 2024 hosted a large Mechanistic Interpretability Workshop (140+ submissions) but the circuit-relevant papers there were workshop-only."
      }
    ],
    "totalDurationMs": 233630,
    "totalTokens": 52265,
    "totalToolUseCount": 45,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 49607,
      "output_tokens": 2272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 383
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2272,
          "cache_read_input_tokens": 49607,
          "cache_creation_input_tokens": 383,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 383,
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
      "otherToolCount": 45
    }
  }
}
```

</details>

---


### System

_source line 426_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Fetching https://arxiv.org/html/2510.00845v2",
  "usage": {
    "total_tokens": 34193,
    "tool_uses": 23,
    "duration_ms": 242785
  },
  "last_tool_name": "WebFetch",
  "uuid": "7b682e1c-a527-4c71-a8a8-e2de2d20625b",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 427_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DSoQKxDvA5XZZ4mjFAGN1r`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.00845v2",
  "prompt": "I need to know: 1) Does this paper propose any method for aggregating results from MULTIPLE DIFFERENT circuit discovery methods (ACDC, EAP, SP, etc.)? 2) Or is it purely an analysis of variance within one method family (EAP variants)? 3) Do they mention anything about combining outputs from different circuit discovery algorithms? 4) What exactly is their \"union circuit\" and \"median circuit\"? 5) Do they propose any cross-method stability metric?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "0e6218d8-ee3f-4476-ba0a-1e97d95f8186",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nc8Jae6EC6HDA9UskCeEvN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 934,
      "cache_read_input_tokens": 32353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 934,
        "ephemeral_1h_input_tokens": 0
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

_source line 428 · 2026-05-12T22:11:59.501Z_

<details><summary>↩ Tool result · `toolu_01DSoQKxDvA5XZZ4mjFAGN1r`</summary>

```text
# Analysis of Circuit Aggregation Methods in the Paper

**1) Multiple Method Aggregation:**
No, this paper does not propose methods for aggregating results across different circuit discovery algorithms (ACDC, SP, etc.). It focuses exclusively on EAP variants.

**2) Scope:**
The work is purely an analysis of variance *within* the EAP method family, examining how different EAP configurations produce varying results.

**3) Cross-Method Combination:**
The paper makes no mention of combining outputs from different circuit discovery algorithms.

**4) Union and Median Circuits:**
Figure 1 displays these concepts but lacks formal definition in the provided text. Based on context, these appear to be heuristic aggregations of multiple circuits discovered under different parameter settings—likely the union of all edges found across runs and the edges appearing in the majority of runs, respectively. However, the paper does not formally propose or validate these as methodological contributions.

**5) Cross-Method Stability Metrics:**
None are proposed. The stability framework applies only within EAP variants, measuring variance through bootstrap resampling and Jaccard index comparisons.

**Summary:** This is fundamentally a stability analysis of a single method family rather than a comparative or aggregation study across different circuit discovery techniques.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "067872d2-053a-4552-91f7-4ff9c1416b00"
}
```

</details>

---


### System

_source line 429_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for \"circuit discovery\" \"stability score\" edge inclus…",
  "usage": {
    "total_tokens": 34712,
    "tool_uses": 24,
    "duration_ms": 252721
  },
  "last_tool_name": "WebSearch",
  "uuid": "c61038fc-e8fe-4da4-9f80-a3126aa29aee",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 430_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FbkEP5rhMcSbvDmyBc2c3Y`</summary>

```json
{
  "query": "\"circuit discovery\" \"stability score\" edge inclusion frequency multiple algorithms vote intersection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "6b699d22-15d8-47de-88b0-a6586b67687b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TAGpG7oq8g77EsDMfEGZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 33287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 481,
        "ephemeral_1h_input_tokens": 0
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

_source line 431 · 2026-05-12T22:12:12.617Z_

<details><summary>↩ Tool result · `toolu_01FbkEP5rhMcSbvDmyBc2c3Y`</summary>

```text
Web search results for query: ""circuit discovery" "stability score" edge inclusion frequency multiple algorithms vote intersection 2025 2026"

Links: [{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523v2"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/html/2510.03282v1"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=9425&show=2000"},{"title":"Sparse Feature Circuit Discovery","url":"https://www.emergentmind.com/topics/sparse-feature-circuit-discovery"},{"title":"Automatic Circuit Discovery","url":"https://sidn.baulab.info/autocircuits/"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"[2502.04577] Position-aware Automatic Circuit Discovery","url":"https://arxiv.org/abs/2502.04577"},{"title":"Research Track: Call for Papers - KDD 2026 - SIGKDD","url":"https://kdd2026.kdd.org/research-track-call-for-papers/"}]

Based on the search results, I found highly relevant research on this topic. The most directly relevant result is **CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles**, a recent paper from March 2026.

## Key Findings

The CIRCUS method assigns per-edge scores s(e) ∈ [0,1] reflecting how often edges survive across configuration families, with scores playing a role analogous to posterior inclusion probabilities in Bayesian variable selection, summarizing which structural claims are supported across plausible analysis choices.

The approach extracts a consensus circuit of edges present in every view, combining multiple algorithmic approaches to reach agreement on circuit structure.

### Design Principles

A key design principle is that configurations must be non-nested: crossing node and edge thresholds in opposite directions ensures consensus is a genuinely new set that cannot be recovered from any single view.

### Efficiency

The pipeline adds only 5.5% overhead beyond a single attribution run.

### Performance Results

On Gemma-2-2B and Llama-3.2-1B, consensus circuits are ~40× smaller than the union of all configurations while retaining comparable influence-flow explanatory power, and are confirmed causally relevant by activation patching.

This approach uses ensemble methods where multiple discovery algorithms "vote" on edge inclusion through repeated runs across different threshold configurations, producing stability scores that indicate edge robustness across different analytical choices.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "24421659-a736-40b0-8a81-90ef3b1563ea"
}
```

</details>

---


### System

_source line 432_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Fetching https://arxiv.org/abs/2602.16823",
  "usage": {
    "total_tokens": 35571,
    "tool_uses": 25,
    "duration_ms": 264618
  },
  "last_tool_name": "WebFetch",
  "uuid": "060b2006-2b70-4c0e-9972-ec65e479874d",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 433_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Vy8KgNdKuSduVCWMzeEcYF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.16823",
  "prompt": "Extract full title, authors, year, venue. Does this paper propose combining results from multiple different circuit discovery methods? Or does it provide provable guarantees for a single method? Does it mention cross-method aggregation or ensemble of methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "168b3bfa-9706-41d3-afa5-ea0ef6649e43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MxZjtaScHguRkCi7FTzpG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 33768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 857,
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

_source line 434 · 2026-05-12T22:12:19.724Z_

<details><summary>↩ Tool result · `toolu_01Vy8KgNdKuSduVCWMzeEcYF`</summary>

```text
# Paper Summary

**Title:** Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees

**Authors:** Itamar Hadad, Guy Katz, Shahaf Bassan

**Year:** 2026

**Venue:** ICLR 2026

## Approach

This work proposes "a suite of automated algorithms that yield circuits with provable guarantees" rather than combining multiple existing methods. The paper focuses on developing single algorithmic approaches that provide formal guarantees across three dimensions: input domain robustness, robust patching, and minimality.

The abstract does not mention cross-method aggregation or ensemble approaches. Instead, it emphasizes that their algorithms "yield circuits with substantially stronger robustness guarantees than standard circuit discovery methods," suggesting they improve upon existing single-method approaches through formal verification techniques rather than by combining multiple discovery methods together.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "84ce984d-9734-46ff-aae1-d3d7b260c750"
}
```

</details>

---


### System

_source line 435_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for MIB shared task BlackboxNLP 2025 all submissions …",
  "usage": {
    "total_tokens": 35966,
    "tool_uses": 26,
    "duration_ms": 270270
  },
  "last_tool_name": "WebSearch",
  "uuid": "96d453c8-d1b8-40f7-bd59-8dc3b760dd9c",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 436_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012WkRTaVhsSjGg6xcmqHmzJ`</summary>

```json
{
  "query": "MIB shared task BlackboxNLP 2025 all submissions circuit localization ensemble methods results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "7bd425e9-de04-4389-8081-3c6e3f103e4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BAdzbuf9dRRxZ2fMAyupt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 358,
      "cache_read_input_tokens": 34625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 358,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-12T22:12:30.994Z_

<details><summary>↩ Tool result · `toolu_012WkRTaVhsSjGg6xcmqHmzJ`</summary>

```text
Web search results for query: "MIB shared task BlackboxNLP 2025 all submissions circuit localization ensemble methods results"

Links: [{"title":"[2510.06811] BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/abs/2510.06811"},{"title":"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/html/2511.18409"},{"title":"[2511.18409] Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/abs/2511.18409"},{"title":"Shared Task - BlackboxNLP 2025 - GitHub Pages","url":"https://blackboxnlp.github.io/2025/task/"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/html/2510.06811v1"},{"title":"BlackboxNLP 2025","url":"https://blackboxnlp.github.io/2025/"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.31/"},{"title":"[PDF] BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BlackboxNLP-2025-MIB-Shared-Task:-Exploring-for-Mondorf-Wang/6de77c59381b74de6e6f554c3f6e12690d6628e8"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://paperreading.club/page?id=345837"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods | Request PDF","url":"https://www.researchgate.net/publication/397423880_BlackboxNLP-2025_MIB_Shared_Task_Exploring_Ensemble_Strategies_for_Circuit_Localization_Methods"}]

Based on the search results, here's information about the MIB Shared Task at BlackboxNLP 2025:

## Overview

The BlackboxNLP 2025 Shared Task extends MIB into a community-wide reproducible comparison of MI techniques, featuring two tracks: circuit localization, which assesses methods that identify causally influential components and interactions driving model behavior, and causal variable localization, which evaluates approaches that map activations into interpretable features.

## Submissions and Results

Four teams submitted across the two tracks, spanning ten methods. Despite the relatively small number of submissions, the participating teams achieved notable performance gains across both tracks.

### Circuit Localization Track

Three teams spanning eight different methods achieved notable gains in circuit localization using ensemble and regularization strategies for circuit discovery. Ensembling strategies and regularization techniques that filter components with unstable contributions to model behavior proved particularly effective, suggesting promising directions for future circuit discovery research.

### Causal Variable Localization Track

One team spanning two methods achieved significant gains in causal variable localization using low-dimensional and non-linear projections to featurize activation vectors.

## Ensemble Methods Results

One notable submission explored ensemble strategies for circuit localization. The work investigated whether ensembling two or more circuit localization methods can improve performance, exploring two variants: parallel and sequential ensembling, where parallel ensembling combines attribution scores assigned to each edge by different methods (e.g., by averaging or taking the minimum or maximum value), and sequential ensemble uses edge attribution scores obtained via EAP-IG as a warm start for edge pruning. The combined hybrid approach achieved the best overall results on the private set, with the lowest CMD score (0.03 average) and the highest CPR score (1.83 average) on the leaderboard.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "8d32e305-8bab-446b-9d8b-f2265323cace"
}
```

</details>

---


### System

_source line 438_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Fetching https://arxiv.org/abs/2511.18409",
  "usage": {
    "total_tokens": 37153,
    "tool_uses": 27,
    "duration_ms": 284270
  },
  "last_tool_name": "WebFetch",
  "uuid": "96b6a13c-4fc9-42c1-b874-bdbe86589c12",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 439_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017rjGsza7DKoDzHGfQVxE26`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.18409",
  "prompt": "Extract full title, authors, year, venue. This is the findings paper for the BlackboxNLP 2025 MIB shared task. I need to know: 1) Did any team propose combining results from multiple fundamentally different circuit discovery methods (not just EAP variants)? 2) Did any team use binary consensus/voting across methods? 3) What were the winning approaches? 4) Was there any approach similar to \"Cross-method Stability Scoring\" where you run ACDC, EAP, SP etc. and mark edges as stable if found by multiple methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "2715df69-1cc6-4654-aea8-cee0e0b3369a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqFfBU6gnPBqJqeHg6zhit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1116,
      "cache_read_input_tokens": 34983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1116,
        "ephemeral_1h_input_tokens": 0
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

_source line 440 · 2026-05-12T22:12:40.344Z_

<details><summary>↩ Tool result · `toolu_017rjGsza7DKoDzHGfQVxE26`</summary>

```text
# Paper Summary

**Title:** Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models

**Authors:** Dana Arad, Yonatan Belinkov, Hanjie Chen, Najoung Kim, Hosein Mohebbi, Aaron Mueller, Gabriele Sarti, Martin Tutek

**Year:** 2025

**Venue:** BlackboxNLP 2025

---

## Answers to Your Questions

Based on the provided abstract content, I cannot answer your specific technical questions (1-4) about the methodologies employed by participating teams. 

The abstract only states that "participants achieved notable gains in circuit localization using ensemble and regularization strategies for circuit discovery" and that another team achieved "significant gains in causal variable localization using low-dimensional and non-linear projections."

The webpage excerpt does not contain sufficient detail about:
- Whether teams combined fundamentally different circuit discovery methods
- Whether binary consensus/voting approaches were used
- Specific winning approach names or descriptions
- Cross-method stability scoring or similar techniques

**To obtain these details, you would need to access the full paper via the PDF or HTML version linked on the arXiv page.**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "bdec7f66-b76d-4eef-8af0-d52a04d3e433"
}
```

</details>

---


### System

_source line 441_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Fetching https://arxiv.org/html/2511.18409",
  "usage": {
    "total_tokens": 37713,
    "tool_uses": 28,
    "duration_ms": 292148
  },
  "last_tool_name": "WebFetch",
  "uuid": "232559a1-9d78-4b18-afab-3dcdba5472a0",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 442_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J4J7jAEZn6VpN8CyUqKG2J`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.18409",
  "prompt": "I need detailed information about ALL submissions to the shared task. Specifically: 1) List all teams and their methods. 2) Did any team combine fundamentally different circuit discovery algorithms (ACDC + EAP + SP)? 3) Did any team use binary voting/consensus across methods? 4) What were the key findings about ensembling methods? 5) Was there any approach where edges are marked as \"stable\" based on agreement across multiple circuit discovery methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "d9c46a80-ad91-49e8-8ef3-f20fcf4f0eaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2fgWPTaKy3VwSeSGJRbxh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 497,
      "cache_read_input_tokens": 36099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 497,
        "ephemeral_1h_input_tokens": 0
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

_source line 443 · 2026-05-12T22:12:49.919Z_

<details><summary>↩ Tool result · `toolu_01J4J7jAEZn6VpN8CyUqKG2J`</summary>

```text
# BlackboxNLP 2025 Shared Task: Submission Analysis

## 1) Teams and Methods

Three teams submitted to the circuit localization track with eight methods total:

- **Mondorf et al.** (2025): Three ensemble variants (Parallel, Sequential, Hybrid)
- **Nikankin et al.** (2025): ILP + PNR + Bootstrapping approach
- **Brunello et al.** (2025): Isolating Path Effects (IPE)

One team submitted to the causal variable localization track:

- **Hirlimann et al.** (2025): Non-linear featurizer and orthogonal non-linear projection methods

## 2) Combining Fundamentally Different Algorithms

No evidence exists in the document of any team combining ACDC, EAP, and SP methods specifically. Mondorf's approach focused on different EAP variants and edge pruning.

## 3) Binary Voting/Consensus Approaches

The document makes no mention of binary voting or consensus-based methods across different circuit discovery algorithms.

## 4) Key Ensembling Findings

"Ensembling strategies may be an accessible and fruitful line of work for future circuit discovery research." Mondorf's hybrid ensemble combined parallel and sequential strategies, achieving "the strongest CPR scores."

## 5) Stability-Based Edge Marking

Yes. Nikankin's approach explicitly identified "edges with consistent score signs and filter[ed] out unstable ones" through bootstrapping across training data resamples—marking edges as stable based on agreement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "79763498-8022-4f53-bc15-c5a28ed52f37"
}
```

</details>

---


### System

_source line 444_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for Nikankin bootstrapping circuit discovery stable e…",
  "usage": {
    "total_tokens": 38305,
    "tool_uses": 29,
    "duration_ms": 301270
  },
  "last_tool_name": "WebSearch",
  "uuid": "fe534d15-cde8-4881-a058-2894879a0f9e",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 445_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Eunx4xUW1AJkcJEnCEmvxE`</summary>

```json
{
  "query": "Nikankin bootstrapping circuit discovery stable edges filtering BlackboxNLP MIB 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "82542d3c-5f31-412b-9e3f-93bd0b422c83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoX7kcqodBvGJNqWPqDbpB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 551,
      "cache_read_input_tokens": 36596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 551,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 446 · 2026-05-12T22:12:58.782Z_

<details><summary>↩ Tool result · `toolu_01Eunx4xUW1AJkcJEnCEmvxE`</summary>

```text
Web search results for query: "Nikankin bootstrapping circuit discovery stable edges filtering BlackboxNLP MIB 2025"

Links: [{"title":"[2510.25786] BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection","url":"https://arxiv.org/abs/2510.25786"},{"title":"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection","url":"https://arxiv.org/html/2510.25786"},{"title":"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.29/"},{"title":"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/html/2511.18409v1"},{"title":"BlackboxNLP 2025","url":"https://blackboxnlp.github.io/2025/accepted_papers/"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods | Request PDF","url":"https://www.researchgate.net/publication/397423880_BlackboxNLP-2025_MIB_Shared_Task_Exploring_Ensemble_Strategies_for_Circuit_Localization_Methods"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/html/2510.06811v1"},{"title":"Localizing Circuits and Causal Variables in Language ...","url":"https://aclanthology.org/2025.blackboxnlp-1.32.pdf"},{"title":"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via","url":"https://arxiv.org/pdf/2510.25786"},{"title":"Yaniv Nikankin's scientific contributions","url":"https://www.researchgate.net/scientific-contributions/Yaniv-Nikankin-2236582145"}]

I found relevant results for your search query. Here's what I found:

## Overview

The paper by Yaniv Nikankin and colleagues addresses circuit discovery in mechanistic interpretability, which involves determining which parts of a model perform a given task.

## Key Contributions

The authors propose three key improvements to circuit discovery: first, they use bootstrapping to identify edges with consistent attribution scores; second, they introduce a simple ratio-based selection strategy to prioritize strong positive-scoring edges, balancing performance and faithfulness; and third, they replace the standard greedy selection with an integer linear programming formulation.

## Results

These methods yield more faithful circuits and outperform prior approaches across multiple MIB tasks and models.

## Technical Details

The work focuses on stable edges through filtering: EAP-IG scores can vary across data samples from the same task, with some edges receiving both negative and positive values in different samples. By bootstrapping the scores across resamples of the training data, the researchers identify edges with consistent score signs and filter out unstable ones.

The paper was published as part of the BlackboxNLP 2025 Shared Task on the Mechanistic Interpretability Benchmark (MIB), with code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "0cdbf7e8-cd36-4c27-ac3e-f878895a5137"
}
```

</details>

---


### System

_source line 447_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Fetching https://arxiv.org/abs/2510.25786",
  "usage": {
    "total_tokens": 39288,
    "tool_uses": 30,
    "duration_ms": 311127
  },
  "last_tool_name": "WebFetch",
  "uuid": "f007be27-c666-4d81-8b7f-a9cdec5859e9",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 448_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019QCvvXuiJj9pFPHc16pBWS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.25786",
  "prompt": "Extract full title, all authors, year, venue. I need to understand: 1) Does this paper combine multiple fundamentally different circuit discovery methods, or does it just bootstrap within a single method (EAP-IG)? 2) Is the bootstrapping across different data samples or across different methods? 3) Does it use binary consensus across methods like ACDC, EAP, SP? 4) How exactly does the edge stability filtering work?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "f0bdb3b1-0866-424b-aa8b-63728557b7f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qPWVh7XPAua9WpjUmYvFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 37147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 918,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-12T22:13:08.314Z_

<details><summary>↩ Tool result · `toolu_019QCvvXuiJj9pFPHc16pBWS`</summary>

```text
# Paper Summary

**Full Title:** BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection

**Authors:** Yaniv Nikankin, Dana Arad, Itay Itzhak, Anja Reusch, Adi Simhi, Gal Kesten-Pomeranz, Yonatan Belinkov

**Year:** 2025

**Venue:** BlackboxNLP-2025 Shared Task

---

## Key Findings

**1) Method Scope:**
The paper does not combine fundamentally different circuit discovery methods. Instead, it works within a single framework, enhancing it through three specific improvements.

**2) Bootstrapping Approach:**
The bootstrapping operates "across different data samples" rather than across multiple distinct methodologies. The abstract states they "use bootstrapping to identify edges with consistent attribution scores."

**3) Binary Consensus:**
The paper does **not** use consensus voting across multiple methods (ACDC, EAP, SP). It focuses on within-method improvements rather than ensemble approaches.

**4) Edge Stability Filtering:**
The webpage content provides only high-level description: "bootstrapping to identify edges with consistent attribution scores." Specific implementation details of the filtering mechanism are not available in this excerpt—full technical details would require accessing the complete paper PDF.

The three core innovations are: bootstrapping for consistency, a "ratio-based selection strategy" for edge prioritization, and replacing greedy selection with integer linear programming.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "40cb2bff-3659-4476-9928-2094afc5d8bd"
}
```

</details>

---


### System

_source line 450_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for \"consensus circuit\" OR \"circuit voting\" OR \"multi…",
  "usage": {
    "total_tokens": 39823,
    "tool_uses": 31,
    "duration_ms": 323893
  },
  "last_tool_name": "WebSearch",
  "uuid": "9553c158-83b3-4204-bc46-d3341881110b",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 451_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015akvTnkER52vhbLNfW4geU`</summary>

```json
{
  "query": "\"consensus circuit\" OR \"circuit voting\" OR \"multi-algorithm circuit\" OR \"fusing circuit discovery\" mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "3367e3ca-e5ad-44b8-9956-c466c207686d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014egEoZCDt88GrxdmJQwqvD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 533,
      "cache_read_input_tokens": 38065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 533,
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

_source line 452 · 2026-05-12T22:13:26.185Z_

<details><summary>↩ Tool result · `toolu_015akvTnkER52vhbLNfW4geU`</summary>

```text
Web search results for query: ""consensus circuit" OR "circuit voting" OR "multi-algorithm circuit" OR "fusing circuit discovery" mechanistic interpretability"

Links: [{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523v2"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"Automated Circuit Discovery for Mechanistic Interpretability","url":"https://erdogan.dev/sias.pdf"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | FAR.AI","url":"https://www.far.ai/research/towards-automated-circuit-discovery-for-mechanistic-interpretability"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/html/2407.00886v2"},{"title":"(PDF) Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://www.researchgate.net/publication/370417693_Towards_Automated_Circuit_Discovery_for_Mechanistic_Interpretability"},{"title":"NeurIPS Poster Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://neurips.cc/virtual/2023/poster/72666"}]

Based on the search results, I found relevant research on circuit discovery in mechanistic interpretability. Here are the key findings:

## Main Research Areas

**Automated Circuit Discovery:**
Researchers have proposed several algorithms to identify circuits that implement specified behaviors in a model's computational graph and reproduce previous interpretability results to validate them. For example, the ACDC algorithm rediscovered 5/5 of the component types in a circuit in GPT-2 Small that computes the Greater-Than operation.

**Consensus Circuit Approach (CIRCUS):**
The most directly relevant to your query is recent work on consensus circuits. Circuit discovery has a measurement problem where different analyst choices yield different circuits, with no principled way to separate robust structure from threshold-sensitive artifacts. CIRCUS addresses this by computing empirical inclusion frequencies over a configuration family, turning analyst-choice variability into a diagnostic.

CIRCUS extracts a consensus circuit of edges present in every view, and on Gemma-2-2B and Llama-3.2-1B, consensus circuits are approximately 40× smaller than the union of all configurations while retaining comparable influence-flow explanatory power.

**Formal Mechanistic Interpretability:**
Automated circuit discovery is a central tool in mechanistic interpretability for identifying the internal components of neural networks responsible for specific behaviors.

The search results show active recent research (as of 2026) addressing robustness and consensus methods in circuit discovery, particularly the CIRCUS framework which directly tackles the challenge of creating reliable consensus circuits across different analysis configurations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "c0b83210-7ec6-4f7d-8115-3853f6ad36d3"
}
```

</details>

---


### System

_source line 453_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "description": "Searching for run ACDC EAP subnetwork probing same task interse…",
  "usage": {
    "total_tokens": 40824,
    "tool_uses": 32,
    "duration_ms": 337687
  },
  "last_tool_name": "WebSearch",
  "uuid": "7e0ee070-bf02-40db-8c6c-1c0433daf6eb",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool call

_source line 454_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hc6p5oew4wMfESsFC4XW1T`</summary>

```json
{
  "query": "run ACDC EAP subnetwork probing same task intersect overlap edges stable circuit 2024 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "31de908d-e780-439d-a0fa-32d6052e1754",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDgij2pPtLPqMUeAmpPj7o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 959,
      "cache_read_input_tokens": 38598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 959,
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

_source line 455 · 2026-05-12T22:13:35.740Z_

<details><summary>↩ Tool result · `toolu_01Hc6p5oew4wMfESsFC4XW1T`</summary>

```text
Web search results for query: "run ACDC EAP subnetwork probing same task intersect overlap edges stable circuit 2024 2025 2026 arXiv"

Links: [{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://arxiv.org/html/2407.14494v3"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=1975&show=2000"},{"title":"Computer Science Jan 2025","url":"https://arxiv.org/list/cs/2025-01?skip=3725&show=2000"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=5425&show=2000"},{"title":"Computer Science Aug 2024","url":"https://arxiv.org/list/cs/2024-08?skip=375&show=2000"},{"title":"Machine Learning Oct 2024","url":"https://arxiv.org/list/cs.LG/2024-10?skip=1475&show=2000"},{"title":"Computer Science Jan 2024","url":"https://arxiv.org/list/cs/2024-01?skip=3140&show=2000"},{"title":"Artificial Intelligence Dec 2024","url":"https://www.arxiv.org/list/cs.AI/2024-12?skip=800&show=2000"},{"title":"Artificial Intelligence Jul 2025","url":"https://arxiv.org/list/cs.AI/2025-07?skip=950&show=2000"},{"title":"Computer Science Oct 2024","url":"https://arxiv.org/list/cs/2024-10?skip=4350&show=2000"}]

Based on the search results, I found relevant information about circuit discovery techniques. The research compares the performance of circuit discovery techniques including Automated Circuit DisCovery (ACDC), Subnetwork Probing (SP), Edgewise SP, Edge Attribution Patching (EAP), and EAP using integrated gradients (EAP-IG).

More specifically, ACDC uses causal interventions to find which edges are part of the circuit, while SP and EAP rely on gradients of the model. EAP assigns scores to all edges at the same time by leveraging gradient information, and prunes edges below a certain threshold to form the final circuit.

The research evaluates these techniques on semi-synthetic transformers. ACDC is significantly better than SP and edgewise SP, but statistically indistinguishable from EAP with integrated gradients.

This information comes from the "InterpBench" paper (arXiv:2407.14494) from October 2025, which evaluates mechanistic interpretability techniques on a benchmark of semi-synthetic transformers with known ground-truth circuits.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "e2d45d02-c0d0-45e8-9dff-5bd06f5a0020"
}
```

</details>

---


### System

_source line 456_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ab23d576408a4772b",
  "tool_use_id": "toolu_01JX4st1y5kYpBpUAVKFTMdz",
  "status": "completed",
  "output_file": "",
  "summary": "Q2: Circuit aggregation/ensemble methods",
  "usage": {
    "total_tokens": 41633,
    "tool_uses": 32,
    "duration_ms": 391340
  },
  "uuid": "f6e8ebdc-1c5b-4f8a-8c6a-e12bc3fa91d8",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---


### Tool result

_source line 457 · 2026-05-12T22:14:23.486Z_

<details><summary>↩ Tool result · `toolu_01JX4st1y5kYpBpUAVKFTMdz`</summary>

```text
Now I have a comprehensive picture. Let me compile the findings.

---

## Literature Survey Results: Multi-Method Circuit Aggregation / Consensus Circuit Discovery

### Critical Finding: No paper proposes exactly "Cross-method Stability Scoring" (CSS) as described — binary consensus across fundamentally different circuit discovery algorithms (ACDC, EAP, SP, etc.). However, two papers are close enough to constitute partial novelty threats.

---

### Paper 1 (HIGHEST THREAT): CIRCUS

- **Title**: CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles
- **Authors**: Swapnil Parekh
- **Year/Venue**: March 2026, arXiv preprint (2603.00523)
- **URL**: https://arxiv.org/abs/2603.00523
- **Approach**: Computes per-edge inclusion frequencies by running ONE attribution method under multiple pruning threshold configurations (non-nested pairs of node/edge thresholds). Assigns each edge a stability score s(e) in [0,1]. Extracts a "consensus circuit" = edges present in ALL configurations. Produces a core/contingent/noise taxonomy.
- **Key distinction from CSS**: CIRCUS varies **hyperparameters within a single method** (pruning thresholds on one attribution graph), NOT across fundamentally different algorithms. It does not run ACDC + EAP + SP and intersect. The "configuration family" is threshold pairs, not different algorithmic approaches.
- **Similarity to CSS**: HIGH conceptually (stability scoring, consensus extraction, per-edge inclusion frequency). The mathematical framing is very similar — both assign edges a robustness score based on how consistently they appear. But the source of variation is different: CIRCUS varies thresholds within one method; CSS would vary across fundamentally different methods.

### Paper 2 (MODERATE THREAT): Mondorf et al. — Ensemble Strategies for Circuit Localization

- **Title**: BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods
- **Authors**: Philipp Mondorf, Mingyang Wang, Sebastian Gerstner, Ahmad Dawar Hakimi, Yihong Liu, Leonor Veloso, Shijia Zhou, Hinrich Schütze, Barbara Plank
- **Year/Venue**: October 2025, BlackboxNLP-2025 Workshop (ACL Anthology)
- **URL**: https://arxiv.org/abs/2510.06811
- **Approach**: Combines outputs from multiple circuit discovery methods via parallel ensembling (averaging continuous attribution scores from EAP, EAP-IG-inputs, EAP-IG-activations) and sequential ensembling (using EAP-IG scores to warm-start edge pruning). Also tested min (intersection) and max (union) aggregation. Hybrid ensemble combines all four methods.
- **Key distinction from CSS**: They aggregate **continuous scores** (mean/min/max of attribution values), not binary edge-in/edge-out decisions. The methods combined are mostly EAP variants + edge pruning — not the full diversity of ACDC + EAP + SP. No explicit "stability score" or "binary consensus" framing.
- **Similarity to CSS**: MODERATE. This is the closest to multi-method aggregation in the literature. They do combine fundamentally different method families (attribution-based + pruning-based). However, the aggregation is score averaging rather than binary consensus, and the paper is a short shared task submission (not a full method paper).

### Paper 3 (LOW-MODERATE THREAT): Méloux et al. — Variance Analysis

- **Title**: Mechanistic Interpretability as Statistical Estimation: A Variance Analysis
- **Authors**: Maxime Méloux, François Portet, Maxime Peyrard
- **Year/Venue**: October 2025, arXiv preprint (2510.00845)
- **URL**: https://arxiv.org/abs/2510.00845
- **Approach**: Analyzes variance of EAP-IG across data resampling, hyperparameter changes, and approximation choices. Shows that varying multiple parameters (resampling strategy, aggregation method, intervention type, EAP method, pruning strategy) yields very different circuits. Visualizes union and median circuits.
- **Key distinction from CSS**: This is purely a **diagnostic/analysis** paper. It does not propose aggregation as a solution — it identifies the problem that circuits are unstable. Stays within the EAP family; does not compare across ACDC/SP.
- **Similarity to CSS**: LOW. Motivates the need for CSS-like approaches but doesn't propose one.

### Paper 4 (LOW THREAT): Nikankin et al. — Bootstrapping for Edge Stability

- **Title**: BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection
- **Authors**: Yaniv Nikankin, Dana Arad, Itay Itzhak, Anja Reusch, Adi Simhi, Gal Kesten-Pomeranz, Yonatan Belinkov
- **Year/Venue**: October 2025, BlackboxNLP-2025 Workshop
- **URL**: https://arxiv.org/abs/2510.25786
- **Approach**: Bootstraps EAP-IG scores across data resamples to identify edges with consistent score signs; filters out unstable edges. Combines with ILP-based selection and ratio-based prioritization.
- **Key distinction from CSS**: Single method (EAP-IG) only. Bootstrapping is across **data samples**, not across different algorithms. No cross-method component.
- **Similarity to CSS**: LOW. The bootstrapping stability idea is related, but it's within-method data resampling, not cross-method.

### Paper 5 (LOW THREAT): Certified Circuits

- **Title**: Certified Circuits: Stability Guarantees for Mechanistic Circuits
- **Authors**: Alaa Anani, Tobias Lorenz, Bernt Schiele, Mario Fritz, Jonas Fischer
- **Year/Venue**: February 2026, arXiv preprint (2602.22968)
- **URL**: https://arxiv.org/abs/2602.22968
- **Approach**: Wraps any single circuit discovery algorithm with a certification layer using randomized data subsampling. Certifies stability under bounded dataset edits via deletion-based randomized smoothing. Abstains on unstable neurons.
- **Key distinction from CSS**: Method-agnostic wrapper but applied to ONE method at a time. Does not aggregate across methods.
- **Similarity to CSS**: LOW. Certifies single-method output, does not combine multiple methods.

### Paper 6 (CONTEXT): InterpBench

- **Title**: InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques
- **Year/Venue**: NeurIPS 2024 (Datasets & Benchmarks)
- **URL**: https://arxiv.org/abs/2407.14494
- **Relevance**: Compares ACDC, SP, EAP, EAP-IG on the same tasks with ground-truth circuits, showing they produce different results. Does NOT propose aggregation — purely evaluation.

### Paper 7 (CONTEXT): Miller et al.

- **Title**: Transformer Circuit Faithfulness Metrics are not Robust
- **Year/Venue**: CoLM 2024
- **URL**: https://arxiv.org/abs/2407.08734
- **Relevance**: Shows faithfulness metrics are highly sensitive to ablation methodology choices. Motivates the need for robust approaches but proposes no aggregation.

---

## Summary Assessment

**No paper found proposing the specific CSS approach of: running multiple fundamentally different circuit discovery algorithms (ACDC, EAP, SP, edge pruning), converting each output to binary edge inclusion, and computing a binary consensus/stability score across methods.**

The closest threats are:
1. **CIRCUS** — same mathematical spirit (per-edge stability scores, consensus extraction) but varies thresholds within ONE method, not across algorithms.
2. **Mondorf et al.** — actually combines different method families via score averaging, but uses continuous score aggregation (not binary consensus) and is a short workshop paper, not a full method contribution.

The CSS idea of running N fundamentally different circuit discovery algorithms and marking edges as "stable" if found by K-of-N methods remains novel. The key differentiator is the **cross-algorithm** dimension — all existing work either (a) varies hyperparameters within one method, or (b) averages continuous scores from method variants rather than applying binary consensus across truly different algorithmic families.

agentId: ab23d576408a4772b (use SendMessage with to: 'ab23d576408a4772b' to continue this agent)
&lt;usage>total_tokens: 42430
tool_uses: 32
duration_ms: 391341&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "87c17282-3df3-443c-97ca-f7fbc1fba390",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability.\n\n**Task**: Find papers that propose aggregating or ensembling results from multiple circuit discovery methods to get more robust circuits. This is the most critical novelty threat - if someone has done \"multi-method circuit aggregation\" or \"consensus circuit discovery\", we need to know.\n\nSearch using these keyword combinations (at least 3 different searches):\n1. \"circuit aggregation ensemble mechanistic interpretability\"\n2. \"robust circuit discovery multi-method consensus\"\n3. \"combining circuit discovery methods transformers\"\n4. \"cross-method circuit stability scoring\"\n5. \"circuit discovery robustness ensemble neural network\"\n\nFor each search, use WebSearch. For any highly relevant paper found, use WebFetch on its arXiv abstract page to confirm the content.\n\n**Output format**: For each relevant paper found, report:\n- Title\n- Authors\n- Year / Venue\n- URL\n- What aggregation/ensemble approach they use\n- How similar it is to \"Cross-method Stability Scoring\" (CSS) - binary consensus across methods\n\nIf nothing found, explicitly state \"No papers found proposing multi-method circuit aggregation.\" Be very thorough.",
    "agentId": "ab23d576408a4772b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Let me compile the findings.\n\n---\n\n## Literature Survey Results: Multi-Method Circuit Aggregation / Consensus Circuit Discovery\n\n### Critical Finding: No paper proposes exactly \"Cross-method Stability Scoring\" (CSS) as described — binary consensus across fundamentally different circuit discovery algorithms (ACDC, EAP, SP, etc.). However, two papers are close enough to constitute partial novelty threats.\n\n---\n\n### Paper 1 (HIGHEST THREAT): CIRCUS\n\n- **Title**: CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\n- **Authors**: Swapnil Parekh\n- **Year/Venue**: March 2026, arXiv preprint (2603.00523)\n- **URL**: https://arxiv.org/abs/2603.00523\n- **Approach**: Computes per-edge inclusion frequencies by running ONE attribution method under multiple pruning threshold configurations (non-nested pairs of node/edge thresholds). Assigns each edge a stability score s(e) in [0,1]. Extracts a \"consensus circuit\" = edges present in ALL configurations. Produces a core/contingent/noise taxonomy.\n- **Key distinction from CSS**: CIRCUS varies **hyperparameters within a single method** (pruning thresholds on one attribution graph), NOT across fundamentally different algorithms. It does not run ACDC + EAP + SP and intersect. The \"configuration family\" is threshold pairs, not different algorithmic approaches.\n- **Similarity to CSS**: HIGH conceptually (stability scoring, consensus extraction, per-edge inclusion frequency). The mathematical framing is very similar — both assign edges a robustness score based on how consistently they appear. But the source of variation is different: CIRCUS varies thresholds within one method; CSS would vary across fundamentally different methods.\n\n### Paper 2 (MODERATE THREAT): Mondorf et al. — Ensemble Strategies for Circuit Localization\n\n- **Title**: BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods\n- **Authors**: Philipp Mondorf, Mingyang Wang, Sebastian Gerstner, Ahmad Dawar Hakimi, Yihong Liu, Leonor Veloso, Shijia Zhou, Hinrich Schütze, Barbara Plank\n- **Year/Venue**: October 2025, BlackboxNLP-2025 Workshop (ACL Anthology)\n- **URL**: https://arxiv.org/abs/2510.06811\n- **Approach**: Combines outputs from multiple circuit discovery methods via parallel ensembling (averaging continuous attribution scores from EAP, EAP-IG-inputs, EAP-IG-activations) and sequential ensembling (using EAP-IG scores to warm-start edge pruning). Also tested min (intersection) and max (union) aggregation. Hybrid ensemble combines all four methods.\n- **Key distinction from CSS**: They aggregate **continuous scores** (mean/min/max of attribution values), not binary edge-in/edge-out decisions. The methods combined are mostly EAP variants + edge pruning — not the full diversity of ACDC + EAP + SP. No explicit \"stability score\" or \"binary consensus\" framing.\n- **Similarity to CSS**: MODERATE. This is the closest to multi-method aggregation in the literature. They do combine fundamentally different method families (attribution-based + pruning-based). However, the aggregation is score averaging rather than binary consensus, and the paper is a short shared task submission (not a full method paper).\n\n### Paper 3 (LOW-MODERATE THREAT): Méloux et al. — Variance Analysis\n\n- **Title**: Mechanistic Interpretability as Statistical Estimation: A Variance Analysis\n- **Authors**: Maxime Méloux, François Portet, Maxime Peyrard\n- **Year/Venue**: October 2025, arXiv preprint (2510.00845)\n- **URL**: https://arxiv.org/abs/2510.00845\n- **Approach**: Analyzes variance of EAP-IG across data resampling, hyperparameter changes, and approximation choices. Shows that varying multiple parameters (resampling strategy, aggregation method, intervention type, EAP method, pruning strategy) yields very different circuits. Visualizes union and median circuits.\n- **Key distinction from CSS**: This is purely a **diagnostic/analysis** paper. It does not propose aggregation as a solution — it identifies the problem that circuits are unstable. Stays within the EAP family; does not compare across ACDC/SP.\n- **Similarity to CSS**: LOW. Motivates the need for CSS-like approaches but doesn't propose one.\n\n### Paper 4 (LOW THREAT): Nikankin et al. — Bootstrapping for Edge Stability\n\n- **Title**: BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection\n- **Authors**: Yaniv Nikankin, Dana Arad, Itay Itzhak, Anja Reusch, Adi Simhi, Gal Kesten-Pomeranz, Yonatan Belinkov\n- **Year/Venue**: October 2025, BlackboxNLP-2025 Workshop\n- **URL**: https://arxiv.org/abs/2510.25786\n- **Approach**: Bootstraps EAP-IG scores across data resamples to identify edges with consistent score signs; filters out unstable edges. Combines with ILP-based selection and ratio-based prioritization.\n- **Key distinction from CSS**: Single method (EAP-IG) only. Bootstrapping is across **data samples**, not across different algorithms. No cross-method component.\n- **Similarity to CSS**: LOW. The bootstrapping stability idea is related, but it's within-method data resampling, not cross-method.\n\n### Paper 5 (LOW THREAT): Certified Circuits\n\n- **Title**: Certified Circuits: Stability Guarantees for Mechanistic Circuits\n- **Authors**: Alaa Anani, Tobias Lorenz, Bernt Schiele, Mario Fritz, Jonas Fischer\n- **Year/Venue**: February 2026, arXiv preprint (2602.22968)\n- **URL**: https://arxiv.org/abs/2602.22968\n- **Approach**: Wraps any single circuit discovery algorithm with a certification layer using randomized data subsampling. Certifies stability under bounded dataset edits via deletion-based randomized smoothing. Abstains on unstable neurons.\n- **Key distinction from CSS**: Method-agnostic wrapper but applied to ONE method at a time. Does not aggregate across methods.\n- **Similarity to CSS**: LOW. Certifies single-method output, does not combine multiple methods.\n\n### Paper 6 (CONTEXT): InterpBench\n\n- **Title**: InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques\n- **Year/Venue**: NeurIPS 2024 (Datasets & Benchmarks)\n- **URL**: https://arxiv.org/abs/2407.14494\n- **Relevance**: Compares ACDC, SP, EAP, EAP-IG on the same tasks with ground-truth circuits, showing they produce different results. Does NOT propose aggregation — purely evaluation.\n\n### Paper 7 (CONTEXT): Miller et al.\n\n- **Title**: Transformer Circuit Faithfulness Metrics are not Robust\n- **Year/Venue**: CoLM 2024\n- **URL**: https://arxiv.org/abs/2407.08734\n- **Relevance**: Shows faithfulness metrics are highly sensitive to ablation methodology choices. Motivates the need for robust approaches but proposes no aggregation.\n\n---\n\n## Summary Assessment\n\n**No paper found proposing the specific CSS approach of: running multiple fundamentally different circuit discovery algorithms (ACDC, EAP, SP, edge pruning), converting each output to binary edge inclusion, and computing a binary consensus/stability score across methods.**\n\nThe closest threats are:\n1. **CIRCUS** — same mathematical spirit (per-edge stability scores, consensus extraction) but varies thresholds within ONE method, not across algorithms.\n2. **Mondorf et al.** — actually combines different method families via score averaging, but uses continuous score aggregation (not binary consensus) and is a short workshop paper, not a full method contribution.\n\nThe CSS idea of running N fundamentally different circuit discovery algorithms and marking edges as \"stable\" if found by K-of-N methods remains novel. The key differentiator is the **cross-algorithm** dimension — all existing work either (a) varies hyperparameters within one method, or (b) averages continuous scores from method variants rather than applying binary consensus across truly different algorithmic families."
      }
    ],
    "totalDurationMs": 391341,
    "totalTokens": 42430,
    "totalToolUseCount": 32,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 39557,
      "output_tokens": 2064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 808
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2064,
          "cache_read_input_tokens": 39557,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 808,
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
      "otherToolCount": 32
    }
  }
}
```

</details>

---


### Assistant

_source line 458_

<details><summary>Logged reasoning block</summary>

```text
All four agents have returned comprehensive results. Let me now compile the findings into the required output file and register it as an artifact. Let me also load the MCP tools I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "af2aa9b1-1608-4323-b04d-16fd2af2f660",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARWwqA5T5WqpTauMZGxSKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4791,
      "cache_creation_input_tokens": 6802,
      "cache_read_input_tokens": 24970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6802
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 459_

四个方向的调研结果已返回。现在汇总写入产出文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "dd1318bf-1860-454b-845b-e035e0af00bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARWwqA5T5WqpTauMZGxSKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4791,
      "cache_creation_input_tokens": 6802,
      "cache_read_input_tokens": 24970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6802
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 460_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AKWWt5fNb1qVYrEHTzn8am`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
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
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "92ff2e55-82dc-4a9d-9338-c722cab21e5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARWwqA5T5WqpTauMZGxSKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4791,
      "cache_creation_input_tokens": 6802,
      "cache_read_input_tokens": 24970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6802
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-12T22:14:28.814Z_

<details><summary>↩ Tool result · `toolu_01AKWWt5fNb1qVYrEHTzn8am`</summary>

````text
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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "be092e04-11fe-478b-87ce-7eb6af3694a2",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---


### Tool call

_source line 462_

<details open><summary>🔧 Tool call — Write · `toolu_01JYAVxaD8PChTg5KgKGo2bJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
  "content": "# Circuit Discovery Related Work Notes (2024-2026)\n\n> 调研日期：2026-05-12 | 项目：structfuse-context\n> 核心问题：CSS（Cross-method Stability Scoring）的 novelty 是否站得住？\n\n---\n\n## 1. 方法一致性比较（Novelty 关键）\n\n**结论：没有论文以\"跨方法一致性分析\"为核心贡献。** 多篇论文在评估新方法时附带比较了不同方法的表现，但比较维度是各方法 vs ground-truth 的 faithfulness/AUC，而非方法之间的 pairwise agreement。\n\n### 直接比较多方法的论文\n\n| 论文 | 方法比较 | 比较维度 | 是否测量方法间一致性 |\n|------|----------|----------|---------------------|\n| Conmy et al. \"Towards Automated Circuit Discovery\" (NeurIPS 2023) | ACDC vs SP vs HISP | ROC AUC vs ground-truth | ❌ 不测方法间 overlap |\n| Syed et al. \"Attribution Patching Outperforms Automated Circuit Discovery\" (BlackboxNLP 2024) | EAP vs ACDC vs SP vs HISP | AUC vs ground-truth | ❌ |\n| Bhaskar et al. \"Finding Transformer Circuits with Edge Pruning\" (NeurIPS 2024 Spotlight) | Edge Pruning vs ACDC vs EAP | Faithfulness at various sparsities | ❌ 但隐含表明方法差异大：EP 找到的边不到 ACDC/EAP 的一半 |\n| Hsu et al. \"CD-T\" (ICLR 2025) | CD-T vs ACDC vs EAP | ROC AUC vs ground-truth | ❌ |\n| Edin et al. \"GIM\" (2025, arXiv) | GIM vs EActP vs EAP vs EAP-IG vs NAP vs IFR vs UGS | Faithfulness metrics | ❌ |\n| InterpBench (NeurIPS 2024 D&B) | ACDC vs EAP vs SP on 86 semi-synthetic models | Ground-truth recovery | ❌ 但发现 ACDC 与 EAP-IG 统计上不可区分 |\n\n### 最接近\"一致性分析\"的论文\n\n**Hanna et al. \"Have Faith in Faithfulness: Going Beyond Circuit Overlap\" (2024, arXiv 2403.17806)**\n- 比较 EAP vs EAP-IG 的 **node overlap**，发现两者 overlap 很高但 faithfulness 差异大\n- 核心结论：overlap ≠ faithfulness，高 overlap 不代表电路功能等价\n- **与 CSS 的关系**：这是对 overlap-based 评估的警告，但不是跨方法一致性的系统研究\n\n**Méloux et al. \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis\" (2025, arXiv 2510.00845)**\n- 对 EAP-IG 做 bootstrap resampling，发现 **单方法内** Jaccard 仅 0.561\n- 超参数变化导致 Jaccard 从 0.086 到 1.0 不等\n- **与 CSS 的关系**：揭示了电路不稳定性问题（motivates CSS），但仅限单方法内变异，未跨方法\n\n**总结：无人系统测量不同方法间的 pairwise Jaccard / agreement matrix。这正是 CSS 要填补的空白。**\n\n---\n\n## 2. Circuit Aggregation / Ensemble（Novelty 威胁）\n\n### 🔴 最高威胁：CIRCUS\n\n**CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles**\n- 作者：Swapnil Parekh\n- 时间：2026年3月, arXiv 2603.00523\n- 方法：对单一归因方法，在多组剪枝阈值配置下运行，计算每条边的 inclusion frequency → stability score s(e) ∈ [0,1]，提取 consensus circuit（所有配置下都存在的边），分为 core/contingent/noise\n- **与 CSS 的区别**：CIRCUS 变化的是**单方法内的超参数**（剪枝阈值），不是跨不同算法族。它不运行 ACDC + EAP + SP 然后求交集\n- **与 CSS 的相似度**：数学框架高度相似（per-edge stability scoring, consensus extraction, core/contingent taxonomy）\n- **威胁评级**：🔴 HIGH — 概念上最接近，但维度不同（intra-method vs cross-method）\n\n### 🟡 中等威胁：Mondorf et al. Ensemble\n\n**Mondorf et al. \"Exploring Ensemble Strategies for Circuit Localization Methods\" (BlackboxNLP 2025, arXiv 2510.06811)**\n- 方法：组合 EAP, EAP-IG-inputs, EAP-IG-activations, Edge Pruning 的输出\n  - Max = union（任一方法选中）\n  - Min = intersection（所有方法选中）\n  - Mean = 连续分数平均\n  - Hybrid = 并行+串行组合\n- 结果：Mean > union/intersection，Hybrid 最佳 (CMD 0.03, CPR 1.83)\n- **与 CSS 的区别**：聚合的是**连续归因分数**（mean/min/max），不是二值 edge-in/edge-out；方法主要是 EAP 变体，不是真正不同的算法族；workshop 短文非完整方法贡献\n- **与 CSS 的相似度**：确实跨方法组合（attribution + pruning），实现了 union/intersection 操作\n- **威胁评级**：🟡 MODERATE — 最接近跨方法聚合，但 framing 为 shared task 工程方案非方法论贡献\n\n### 🟢 低威胁\n\n| 论文 | 方法 | 与 CSS 区别 | 威胁 |\n|------|------|------------|------|\n| Nikankin et al. \"Improving Circuit Faithfulness via Better Edge Selection\" (BlackboxNLP 2025) | Bootstrap EAP-IG scores across data resamples | 单方法 + 数据重采样，非跨方法 | 🟢 LOW |\n| Anani et al. \"Certified Circuits: Stability Guarantees\" (2026, arXiv 2602.22968) | 随机化数据子采样 + 删除平滑认证 | 单方法 wrapper，不聚合多方法 | 🟢 LOW |\n| Miller et al. \"Transformer Circuit Faithfulness Metrics are not Robust\" (CoLM 2024) | 分析 faithfulness 指标敏感性 | 纯诊断，不提出聚合 | 🟢 LOW |\n\n**总结：没有论文提出 CSS 的精确方案——运行 N 种根本不同的算法族（ACDC, EAP, SP, EP），对每种输出做二值化，然后计算跨方法 binary consensus。CIRCUS 最接近但维度不同（intra-method threshold variation vs cross-method）。Mondorf et al. 确实跨方法但用连续分数聚合且为 workshop 工程方案。**\n\n---\n\n## 3. 2024-2026 新方法\n\n| 方法 | 论文 | 年份 | 会议 | 算法族 | 备注 |\n|------|------|------|------|--------|------|\n| CD-T | Hsu et al. \"Efficient Automated Circuit Discovery using Contextual Decomposition\" | 2024 | ICLR 2025 | 分解 (decomposition) | 无需 activation patching，秒级发现，97% AUC |\n| DiscoGP | Yu et al. \"Functional Faithfulness in the Wild\" | 2024 | ICML 2024 | 可微剪枝 | 联合权重+边剪枝，端到端学习二值 mask |\n| Transcoders | Dunefsky et al. \"Transcoders Find Interpretable LLM Feature Circuits\" | 2024 | NeurIPS 2024 | 稀疏替换模型 | 用稀疏 MLP 替换原 MLP，实现 weights-based 电路分析 |\n| Sparse Feature Circuits | Marks et al. \"Discovering and Editing Interpretable Causal Graphs\" | 2024 | ICLR 2025 (Oral) | 归因 + SAE 特征 | 在 SAE 特征级别发现电路，支持 SHIFT 编辑 |\n| Circuit Tracing | Ameisen, Olah et al. (Anthropic) \"Attribution Graphs\" | 2025 | Tech Report | 稀疏替换 + 归因 | Cross-layer transcoders → per-prompt DAG，应用于 Claude 3.5 |\n| GIM | Edin et al. \"Improved Interpretability for LLMs\" | 2025 | arXiv | 梯度修正 | 修正 softmax/LayerNorm 反传，MIB 排行榜第一 |\n| HAP | Gu et al. \"Hybrid Attribution and Pruning Framework\" | 2025 | arXiv | 混合 (EAP → EP) | 先 EAP 粗筛再 EP 精修，比 EP 快 46% |\n| ModCirc | He et al. \"Modular Circuits of LLMs\" | 2025 | ICML 2025 | 模块化分解 | 发现跨任务共享的模块化电路词表 |\n| Stream | Rosser et al. \"Scaling up MI to Long Context\" | 2025 | arXiv | 层次化剪枝 | O(T log T) 稀疏注意力 mask，支持 100K+ token |\n| Weight-Sparse Circuits | Gao et al. (OpenAI) | 2025 | arXiv | 稀疏训练 | 极端权重稀疏 (~1/1000) → 天然可解释电路 |\n| Formal MI | Hadad et al. \"Automated Circuit Discovery with Provable Guarantees\" | 2026 | ICLR 2026 | 验证 (verification) | 首个可证明保证的电路发现（鲁棒性 + 最小性） |\n| SVD Directional Masking | Ahmad et al. \"Beyond Components\" | 2025 | arXiv | SVD + 可微 mask | 揭示单头内叠加子功能 |\n\n---\n\n## 4. 顶会论文列表\n\n### ICLR 2024\n| 论文 | 主要贡献 |\n|------|----------|\n| Sparse Autoencoders Find Highly Interpretable Features in LMs | SAE 发现单语义特征，解决 superposition |\n| Towards Best Practices of Activation Patching in LMs | 系统分析 patching 方法选择对电路发现的影响 |\n| Circuit Component Reuse Across Tasks | IOI 电路 ~78% 被 Colored Objects 复用 |\n| Successor Heads: Recurring Interpretable Attention Heads | 发现跨架构的 successor heads（递增操作） |\n\n### ICLR 2025\n| 论文 | 主要贡献 |\n|------|----------|\n| Sparse Feature Circuits (Oral) | SAE 特征级电路发现 + SHIFT 编辑 |\n| Scaling and Evaluating Sparse Autoencoders (Oral) | k-sparse SAE 扩展到 GPT-4，16M latents |\n| CD-T: Contextual Decomposition for Circuit Discovery | 秒级电路发现，97% AUC |\n| Computational Complexity of Circuit Discovery (Spotlight) | 证明多数电路发现查询 NP-hard |\n| Everything Everywhere All at Once: Is MI Identifiable? | 电路非唯一性：多电路可复现同一行为 |\n| SAEs Do Not Find Canonical Units of Analysis | SAE stitching 证明特征非原子/非完备 |\n| Unifying and Verifying Mechanistic Interpretations | 统一群运算网络的机制解释并形式化证明 |\n\n### NeurIPS 2024\n| 论文 | 主要贡献 |\n|------|----------|\n| Finding Transformer Circuits with Edge Pruning (Spotlight) | EP 方法，更忠实且更稀疏，扩展到 13B |\n| Transcoders Find Interpretable LLM Feature Circuits | 稀疏 MLP 替换实现 weights-based 电路分析 |\n| LLM Circuit Analyses Are Consistent Across Training and Scale | 电路在训练过程和模型规模间一致出现 |\n| Compact Proofs of Model Performance via MI | MI → 可证明的准确率下界 |\n| Hypothesis Testing the Circuit Hypothesis | 形式化电路假设的假设检验 |\n| InterpBench: Semi-Synthetic Transformers for Evaluating MI | 86 个有 ground-truth 的半合成模型评估基准 |\n\n### ICML 2025\n| 论文 | 主要贡献 |\n|------|----------|\n| MIB: A Mechanistic Interpretability Benchmark | 标准化电路定位基准，归因+mask 优化方法领先 |\n| ModCirc: Modular Circuits of LLMs | 跨任务模块化电路词表 |\n| Towards Understanding Fine-Tuning via Circuit Analysis | 追踪微调中电路变化，提出 circuit-aware LoRA |\n\n---\n\n## 5. Novelty 评估\n\n### CSS 的 novelty 站得住吗？**站得住，但需要精确定位差异化。**\n\n#### ✅ Novelty 成立的理由\n\n1. **无人做跨算法族的 binary consensus**：所有现有工作要么是单方法内变异分析（CIRCUS, Méloux），要么是连续分数聚合（Mondorf），要么只是各方法 vs ground-truth 的性能比较。CSS 提出跨 N 种根本不同的算法族做二值共识，这个精确配方是新的。\n\n2. **方法间差异的系统分析是空白**：没有论文报告过不同方法的 pairwise Jaccard matrix / agreement heatmap。大量论文隐含表明方法差异很大（EP 边数不到 ACDC 一半），但无人将此作为研究问题。\n\n3. **core/contingent 分类的跨方法版本未被探索**：CIRCUS 做了类似的 core/contingent/noise taxonomy，但基于 intra-method threshold variation。CSS 基于 cross-method agreement 做分类，维度不同且信息更丰富。\n\n#### ⚠️ 需要小心的 Novelty 威胁\n\n1. **CIRCUS (2603.00523)** 是最大威胁。虽然维度不同，但 reviewer 可能认为 conceptual overlap 太大。**建议**：论文中必须明确讨论 CIRCUS，强调区别（intra-method hyperparameter variation vs cross-method algorithmic diversity），并论证为何跨方法维度更有意义（不同方法有不同 inductive bias，而阈值变化只探索同一方法的 Rashomon set）。\n\n2. **Mondorf et al.** 已经实现了 union/intersection 操作并发现 mean 优于两者。CSS 需要论证 binary consensus 相比连续分数平均的优势（如可解释性、对阈值选择的鲁棒性）。\n\n3. **Méloux et al. 的 intra-method instability 问题**：如果单方法内 Jaccard 仅 0.56，跨方法 consensus 可能更低。需要实验证明 CSS-core 的 faithfulness 确实优于单方法，否则 consensus 可能只是噪声的交集。\n\n4. **非唯一性问题 (ICLR 2025 \"Everything Everywhere All at Once\")**：如果电路本身就非唯一，跨方法共识的理论基础需要更强的论证。\n\n#### 🎯 差异化建议\n\n- **vs CIRCUS**：CSS 跨算法族（不同 inductive bias），CIRCUS 跨阈值（同一方法的 Rashomon set）。论证：不同方法捕获不同类型的因果关系，其交集比单方法阈值交集更有意义。\n- **vs Mondorf et al.**：CSS 是二值共识（edge in/out），Mondorf 是连续分数平均。论证：二值化消除了方法间分数不可比的问题，且产出可直接解释的 agreement matrix。\n- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "b6883c92-982c-414d-b9be-8eed3a44832d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DAZ866gJesKTxRaV24H2p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5844,
      "cache_read_input_tokens": 31772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5844
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
